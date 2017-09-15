#!/usr/bin/python
import json
import logging

import fandango as fn

DOCUMENTATION = '''
---
module: start_element

short_description: Start element device servers.

description:
    - Start the device servers in the element using Astor.

options:
    element_config:
        description:
            - A json file defining the list of device server instances grouped
              according to their startup levels.
        required: true

author:
    - CAM (cam@ska.ac.za)
'''

EXAMPLES = '''
- name: Start the Element's device servers.
  start_element:
    element_config: refelt_config_starter.json
'''

RETURN = '''
Running_servers:
    : The list of server instances running.
Servers_not_running:
    description: The list of server instances not running.
'''

running_servers = []
servers_not_running = []

def start_element(elt_config):

    astor = fn.Astor()

    with open(elt_config) as elt_config_file:
        facility_data = json.load(elt_config_file)

    hosts_data = facility_data["tango_hosts"]

    for host_name, host_data in hosts_data.items():

        for data in host_data:
            srv_instance_startup_level = data["startup_level"]
            server_instances = data["server_instances"]

            for server_instance in server_instances:
                try:
                    astor.set_server_level(server_instance, host_name,
                                           srv_instance_startup_level)
                except Exception as exc:
                    logging.error("EXCEPTION in register {} {}".format(
                        server_instance, exc))
                    print """EXCEPTION IN REGISTER in ASTOR"""
                    print """host={!r}  level={!r} server_instance={!r}.""".format(
                        host_name, srv_instance_startup_level, server_instance)
                    servers_not_running.append(server_instance)
                    continue

                # For now - start each server - else they do not show up in the
                # Astor GUI. Start them independently since they do not all exist
                # in StartDsPath yet
                try:
                    result = astor.start_servers([server_instance], host=host_name)
                    if not result:
                        logging.error("FAILED to start {}".
                                      format(server_instance))
                        print """FAILED TO START in ASTOR"""
                        print """host={!r}  level={!r} server_instance={!r}.""".format(
                            host_name, srv_instance_startup_level, server_instance)
                        servers_not_running.append(server_instance)
                    else:
                        running_servers.append(server_instance)
                except Exception as exc:
                    logging.error("EXCEPTION in start {} {}".
                                  format(server_instance, exc))
                    print """EXCEPTION IN START in ASTOR"""
                    print """host={!r}  level={!r} server_instance={!r}.""".format(
                        host_name, srv_instance_startup_level, server_instance)
                    servers_not_running.append(server_instance)


def run_module():
    # define the available arguments/parameters that a user can pass to
    # the module
    module_args = dict(
        element_config=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task.
    result = dict(
        changed=False,
        Running_servers='',
        Servers_not_running=''
    )
    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode.
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        return result

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    start_element(module.params['element_config'])
    result['Running_servers'] = running_servers
    result['Servers_not_running'] = servers_not_running

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    if running_servers:
        result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if servers_not_running:
        module.fail_json(msg='The script failed to start all the servers.',
                         **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(msg="Successful run!!!", **result)


from ansible.module_utils.basic import AnsibleModule

def main():
    run_module()

if __name__ == '__main__':
    main()
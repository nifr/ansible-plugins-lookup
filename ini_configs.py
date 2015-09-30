import ansible.utils as utils
import ansible.errors as errors

import pprint

class LookupModule(object):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, **kwargs):

        if not isinstance(terms, list):
            raise errors.AnsibleError("with_ini_configs expects a list of dicts")

        ret = []
        for item in terms:
            for ini in item:
                for section in ini["sections"]:
                    for directive in section["options"]:
                        ret.append({'name': ini["name"], 'path': ini["path"], 'section': section["name"], 'option': directive.keys()[0], 'value': directive[directive.keys()[0]] })

        return ret

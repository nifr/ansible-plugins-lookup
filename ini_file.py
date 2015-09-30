import ansible.utils as utils
import ansible.errors as errors

import pprint

class LookupModule(object):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, **kwargs):

        ret = []
        file = terms[0]
        for section in file["sections"]:

            if "options" in section:

                if not isinstance(section["options"], list):
                    raise errors.AnsibleError("options has to be a list.")

                for option in section["options"]:
                    ret.append({'path': file["path"], 'section': section["name"], 'option': option.keys[0], 'value': option[option.keys[0]] })

            else:
                ret.append({'path': file["path"], 'section': section["name"], 'option': section["option"], 'value': section["value"] })

            if "owner" in file:
                ret[-1]["pwner"] = file["owner"]

            if "group" in file:
                ret[-1]["group"] = file["group"]

            if "mode" in file:
                ret[-1]["mode"] = file["mode"]

        return ret

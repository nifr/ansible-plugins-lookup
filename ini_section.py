import ansible.utils as utils
import ansible.errors as errors

import pprint

class LookupModule(object):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, **kwargs):

        ret = []
        for directive in terms[1]:
            ret.append({'name': terms[0], 'option': directive.keys()[0], 'value': directive[directive.keys()[0]] })

        return ret

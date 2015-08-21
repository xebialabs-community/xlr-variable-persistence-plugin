#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import os, sys, time, re
import pprint
import com.xebialabs.xlrelease.domain.Release
import com.xhaus.jyson.JysonCodec as json


from java.lang import String
from java.util import Arrays
from org.apache.commons.collections.list import FixedSizeList;

__release = getCurrentRelease()
__id = getattr(__release, 'id')


def set_variable(key, value):

  regex = re.compile('^\$\{', re.IGNORECASE)
  if re.match(regex, key) is None:
    key = "${" + key + "}"

    print "setting %s to %s" % (k ,v)

  __release.setVariableValues({key : value})
  releaseApi.updateRelease(__id, __release)

def get_variable_store(variable_store):

    request = HttpRequest({'url': 'http://localhost:5516'}, release.scriptUsername, release.scriptUserPassword)

    response = request.get('/configurations', contentType='application/json')
    data = json.loads(response.getResponse())
    print data
    for i in range(0, len(data)):
        if variable_store['title'] == data[i]['properties']['title'] and variable_store['variable_json'] == \
                data[i]['properties']['variable_json']:
                return data[i]


var_string =  get_variable_store(variableStore)['properties']['variable_json']

variables = json.loads(var_string)

for k, v in variables.items():
    set_variable(k,v)




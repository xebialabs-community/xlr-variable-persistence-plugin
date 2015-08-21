#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import os, sys, time

import com.xebialabs.xlrelease.domain.Release
import com.xhaus.jyson.JysonCodec as json

from java.lang import String
from java.util import Arrays
from org.apache.commons.collections.list import FixedSizeList;
import urllib

__release = getCurrentRelease()



def get_variable_store(variable_store):

    request = HttpRequest({'url': 'http://localhost:5516'}, release.scriptUsername, release.scriptUserPassword)

    response = request.get('/configurations', contentType='application/json')
    data = json.loads(response.getResponse())

    for i in range(0, len(data)):
        if variable_store['title'] == data[i]['properties']['title'] and variable_store['variable_json'] == \
                data[i]['properties']['variable_json']:
                return data[i]

def save_variable_store(config_item, variables):
    config_item['properties']['variable_json'] = json.dumps(variables)

    jsonPayload=json.dumps(config_item)
    request = HttpRequest({'url': 'http://localhost:5516'}, release.scriptUsername, release.scriptUserPassword)
    response = request.put('/configurations/%s' % (config_item['id']), jsonPayload,contentType = 'application/json')


save_variable_store(get_variable_store(variableStore), getCurrentRelease().getVariableValues())

sys.exit(0)

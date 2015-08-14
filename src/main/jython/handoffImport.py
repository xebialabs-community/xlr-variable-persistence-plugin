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

def read_json_data():
    with open(handoff_file, "r+") as jsonFile:
     return json.loads(jsonFile.read())[handoff_field]


def set_variable(key, value):

  regex = re.compile('^\$\{', re.IGNORECASE)
  if re.match(regex, key) is None:
    key = "${" + key + "}"

  __release.setVariableValues({key : value})
  releaseApi.updateRelease(__id, __release)

data = read_json_data()

pprint.pprint(data)

for k, v in data.items():
    set_variable(k,v)
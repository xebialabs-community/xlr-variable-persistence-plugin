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

__release = getCurrentRelease()
__id = getattr(__release, 'id')
variables = __release.getVariableValues()


def save_release_variables_to_jsonfile(variable_map):
    with open(variable_file, "r+") as jsonFile:
        data = json.loads(jsonFile.read())

        data[variable_field] = variable_map

        jsonFile.seek(0)  # rewind
        jsonFile.write(json.dumps(data))
        jsonFile.truncate()


save_release_variables_to_jsonfile(variables)

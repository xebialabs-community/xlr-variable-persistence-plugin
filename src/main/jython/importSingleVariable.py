#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import os, sys, time, re

import com.xebialabs.xlrelease.domain.Release
import com.xhaus.jyson.JysonCodec as json

from java.lang import String
from java.util import Arrays
from org.apache.commons.collections.list import FixedSizeList;

__release = getCurrentRelease()
__id = getattr(__release, 'id')


def read_json_data():
    with open(handoff_file, "r+") as jsonFile:
        return json.loads(jsonFile.read())


def set_variable(key, value):
    regex = re.compile('^\$\{', re.IGNORECASE)
    if re.match(regex, key) is None:
        key = "${" + key + "}"

    __release.setVariableValues({key: value})
    releaseApi.updateRelease(__id, __release)


def get_single_value(field, key, data):

    secondary_key = None

    regex = re.compile('^\$\{', re.IGNORECASE)
    if re.match(regex, key) is None:
        secondary_key = "${" + key + "}"

    if field in data:
        if key in data[field]:
            value = data[field][key]
            print "found %s in %s" % (value, field)
            return value
        if secondary_key in data[field]:
            value = data[field][secondary_key]
            print "found %s in %s" % (value, field)
            return value
        else:
            print "%s not found in %s" % (key, field)
    else:
        print "%s not found in %s" % (field, handoff_file)

    sys.exit(1)


data = read_json_data()

value = get_single_value(handoff_field, variable_name, read_json_data())
output_variable_name = value

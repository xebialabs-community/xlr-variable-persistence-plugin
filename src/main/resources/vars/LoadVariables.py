#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import com.xhaus.jyson.JysonCodec as json

__release = getCurrentRelease()
variables = json.loads(variableStore['variablesJson'])

variable_start_regex = re.compile('^\$\{', re.IGNORECASE)
newVariables = {}
for key, value in variables.items():
    if re.match(variable_start_regex, key) is None:
        key = "${%s}" % (key)
    newVariables[key] = value
__release.setVariableValues(newVariables)
releaseApi.updateRelease(release.id, __release)
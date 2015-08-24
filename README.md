#XL Release variable persistence off plugin

## Preface
This document descripts the functionality provide by the `xlr-variable-persistence-plugin`, as well as potential future functionality.

## Overview
This plugin enables users to export the all the variables from one template and import them into another template.

## Installation

Copy the plugin JAR file into the `SERVER_HOME/plugins` directory of XL Release.

### Limitations

* This plugin uses the XL Release API to modify releases from a [Custom Script task](https://docs.xebialabs.com/xl-release/how-to/create-custom-task-types-in-xl-release.html). This requires the 'run as user' for the template to be set to the admin user.
* In order for the 'downstream' template that is trying to load the variables to start, mandatory variables should be given a dummy value when the release is create. These values will be overwritten by the `load variables` task. Alternatively, you can make the variables optional by including `make variable optional` tasks in your template.
* For now, this plugin only works when XL Release listens on port 5516.

## Supported Tasks

* Store Variables
* Load Variables
* Make Variable Optional

#### Store Variables

Writes the names and values of all variables in the release to a global variable store. The current contents of the variable store will be overwritten.

**Input properties**

* `variableStore`: the variable store to which variables should be written. You can create one or more variable stores via the [Configuration menu](https://docs.xebialabs.com/xl-release/how-to/create-custom-configuration-types-in-xl-release.html#configuration-page) in XL Release _required_

#### Load Variables

Imports the names and values of variables from a variable store into the current release and sets the values of all variables with matching names.

**Input properties**

* `variableStore`: the variable store from which variables are to be loaded _required_

#### Make Variable Optional

Makes a variable optional so that the release can start without a value having to be specified for it.

**Output properties**

* `variableName`: name of the variable to be made optional _required_

## Example Use Case

An example use-case for this plugin is a delivery process which is seperated into two separate "phases". The first phase, (the "Continuous Build/Integration phase") is triggered by code checkins and cranks out a build as soon as new code becomes available. The second phase (the "testing phase") is executed at regular intervals, using the latest "known good" release candidate.

This plugin allows users to "connect" the two seperate templates that represent the first and second phases of this process, by exporting variables from the Continuous Build/Integration release and then importing them in the testing release. The variables from the Continuous Build/Integration release will include, amongst others, information about the latest 'known good' release candidate version, which allows the testing release to deploy the correct version.

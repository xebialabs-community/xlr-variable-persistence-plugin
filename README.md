#XL Release variable persistence off plugin

## Preface
This document descripts the functionality provide by the `xlr-variable-persistence-plugin`, as well as potential future functionality.

## Overview
This plugin enables users to export the all the variables from one template to a json formatted file somewhere on the system xlr is running on and importing it into another template.
The import can either be done in one go or more selectively by importing one variable at a time.

## Installation
Copy the plugins jar file into the plugin directory of XL Release.

!! this plugin uses the XL Release jython api to modify releases from a scripted tast. This means that the run as user for the template has to set to the admin user.
!! in order fo the second template to start mandatory variables should be given a dummy value at template creation. these values will get overwritten by the load variables task.
!! for now this plugin only works when xl-release listens on port 5516

## Supported Tasks
* [store variables]
* [load variables]
* [mock variable]
* [variable store]

#### store variables
Writes the current names and values of all variables in the release to a ci to be persisted in the database

**input properties**

* `variable_store`: predefined variable store

#### load variables
imports names and values of variables in a certain variable store ci into the current release

**input properties**

* `variable_store`: predifined variable store

#### mock variable
mocks a variable so that the release will start although all of the required variables have not been set

**output properties**

* `variable_name`: name of the variable to be mocked (requires ${notation})

#### variable store

Config ci that will hold the persisted variables in a string field

**properties**

* `variable_json`: !! do not edit by hand !! (and if u did and stuff goes horrible wrong , don't call me)


## Usage
The typical use-case for this plugin is an environment which is seperated into two seperate "compartments". On compartment (the Continuous build/integration) cranks out a build as soon as new code becomes available and runs on a git/svn/artifactory trigger.
The other compartment (the testing compartment) needs to be deployed at certain time intervals but prefereble with the latest know good release. This plugin enables xlr to solve this problem with two seperate templates that are connected by the export of variables from the build/ci compartment template which will ten get picked up by the time triggerd compartment when it is time to run the template.


## Examples
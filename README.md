# cures-reporter-py3
Cures Reporter and EMR Scrapping Tool Implemented in Python3
Hope is to take Excel spreadsheet as input and then construct:
1) Patient query list from the spreadsheet
2) Iterate over the list query Cures data
3) Scrap EMR data as possible for patient
4) Log in second spreadsheet to then be reported as study data

Was initially impleneted in Node.js
Migrating to python3 due to what appears to be better scripting
tool support for computer vision tools.

Attempting to use pipenv to manage depdencies during development
$> pipenv shell
... produces subshell with environment setup to run correctly ...
... use exit to return to top level shell ...
$> pipenv install <module> so that it will be placed in the
correct location

Having problems with black screenshots for pyguiauto?  Seems that
won't work correctly with Wayland ... so you have to turn that
off in GDM as follows (/etc/gdm/custom.conf):

# GDM configuration storage

[daemon]
# Uncomment the line below to force the login screen to use Xorg
WaylandEnable=false

[security]

[xdmcp]

[chooser]

[debug]
# Uncomment the line below to turn on debugging
#Enable=true


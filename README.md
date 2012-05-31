ypcd
====

cd navigation helper


install
=======

1. copy ypcd.sh and ypcd.py to an executable directory (e.g. ~/bin)
2. add following line to .bashrc

. /path/to/ypcd.sh

usage
=====

cd -l
* show cd history

cd [number]
* change to last N directory

cd [partial path]
* change to last directory match the string

cd ...
* change to N level directory up

examples
========

<code>
~% cd src
~/src% cd solutions/
~/src/solutions% cd vmware/
~/src/solutions/vmware% cd -l
 3  ~
 2  ~/src
 1  ~/src/solutions
 0  ~/src/solutions/vmware
~/src/solutions/vmware% cd 2
~/src% cd vm
~/src/solutions/vmware% cd ....
~%
</code>


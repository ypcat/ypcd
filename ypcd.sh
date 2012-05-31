#!/bin/bash

# features:
# ~% cd src
# ~/src% cd solutions/
# ~/src/solutions% cd vmware/
# ~/src/solutions/vmware% cd -l
#  3  ~
#  2  ~/src
#  1  ~/src/solutions
#  0  ~/src/solutions/vmware
# ~/src/solutions/vmware% cd 2
# ~/src% cd vm
# ~/src/solutions/vmware% cd ....
# ~%

ypcd () {
    path=`dirs -v | ypcd.py $1`
    [[ $? -eq 0 ]] && pushd $path > /dev/null
    for i in `dirs -v | ypcd.py -d`; do
        popd -n +$i 2>/dev/null 1>/dev/null
    done
    popd -n +21 2>/dev/null 1>/dev/null
}
alias cd=ypcd


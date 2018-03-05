#!/bin/bash


pkg_list='
gcc
make
'

for apkg in $(echo $pkg_list);
do
   cmd="rpm -q $apkg"
   eval $cmd 2>&1 > /dev/null
   if [ $? -eq 0 ]; then
     printf "%s:%s\n" "ok" "$cmd"
   elif [ $? -ne 0 ]; then
     printf "%s:%s\n" "ng" "$cmd"
     printf "rpm pkg: $apkg is not installed\n" 
     printf "  Please install\n"
     printf "    yum install $apkg\n"
   fi
done



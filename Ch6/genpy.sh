#! /bin/bash
if [[ ! $@ ]];
    then echo "usage: genpy.sh name_of_py_script.py";
fi
cp "../template.py" $1


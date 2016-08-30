#! /bin/bash
if [[ ! $@ ]];
    then echo "usage: genpy.sh name_of_py_script.py";
    exit 0
fi
if [ -f $1 ];
    then echo "file already exists"
    exit 0
fi
cp "../template.py" $1
exit 1


#!/bin/bash

for py_file in $(find ./exchanges -name '*.py')
do
    python3 $py_file
done
for py_file in $(find ./queue_bind -name '*.py')
do
    python3 $py_file
done
for py_file in $(find ./queues -name '*.py')
do
    python3 $py_file
done
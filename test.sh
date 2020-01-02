#!/bin/bash

for i in $(seq 1 5)
do
 echo  "$i"
 curl localhost:8080 &
done
wait
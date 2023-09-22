#!/usr/bin/env bash

freq=${1}
dur=${2}
( speaker-test -t sine -f $freq )& pid=$! ; sleep $dur ; kill -9 $pid

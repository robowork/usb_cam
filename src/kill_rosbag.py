#!/usr/bin/env python3
import os
import time
import rosnode
import shutil
import sys
rosbag_node = '/rosbag_record_cam'
thresh = 3.0 # kill rosbag if disk space drops below this thresh
while True:
    if rosbag_node in rosnode.get_node_names():
        #check if disk space is low
        _,_,free_sp = shutil.disk_usage('/')
        free_sp = free_sp/1024**3
        if free_sp < thresh:
            print("killing rosbag record; disk full")
            rosnode.kill_nodes([rosbag_node])
            sys.exit(0)
    time.sleep(0.5)


#!/bin/bash

sudo bluetoothctl power on

python serial_reciever.py & PIDMIX=$!
sudo rfcomm watch hci0 & PIDIOS=$!

wait $PIDMIX
wait $PIDIOS

trap 'kill $(jobs -p)' EXIT


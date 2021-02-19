#!/bin/bash

sudo rfcomm watch hci0
exec python serial_reciever.py

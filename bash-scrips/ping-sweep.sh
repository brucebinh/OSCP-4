#!/bin/bash
for ip in {1..254}; do
	 ping -c 1 10.11.1.$ip | grep "64" | cut -d " " -f 4 | cut -d ":" -f 1  &
done

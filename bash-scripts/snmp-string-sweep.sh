#!/bin/bash
for ip in $(seq 1 254); do
	echo 10.11.1.$ip;
done > ip_list.txt

onesixtyone -c community_names_list.txt -i ip_list.txt

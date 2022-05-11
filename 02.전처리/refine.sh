#! /bin/bash

target=$1
cat "${target}.json" | jq '.[]' | jq '.["product_img"]' | while read line; do
        line=${line: (1):(-1)}
        if [[ -z "$(find ../PICS/Long/ -name "*${line}")" ]]; then
                echo DUP : $line >> "${target}-non.out"
        else
		    echo NON-DUP : $line
	fi
done

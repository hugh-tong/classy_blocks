#!/bin/bash  


DIR=${1:-.}  


for file in "$DIR"/*.py  
do   
    if [ -f "$file" ]; then  
        echo "Running Python script: $file"  
        
        python3 "$file"  
        
        if [ $? -eq 0 ]; then  
            echo "ok"  
        else  
            echo "bad"  
        fi  
    fi  
done
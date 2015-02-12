#!/bin/bash


PORT=$(docker port app-pc1 5000 | cut -d : -f 2); while [ ${#PORT} -eq 0 ]; do PORT=$(docker port app-pc1 5000 | cut -d : -f 2); echo "Fuck"; sleep 2; done;
echo $PORT

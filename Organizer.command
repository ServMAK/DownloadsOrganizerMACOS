#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "$DIR"

python3 DownloadOrganizer.py

echo ""
read -p "Nacisnij Enter, aby zamknac program..." 
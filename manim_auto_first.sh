#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide the Python script file."
    exit 1
fi

script_file="$1"
first_class=$(grep -oP '(?<=class )\w+(?=\(Scene\))' "$script_file" | head -1)

echo "Script file: $script_file"

if [ -z "$first_class" ]; then
    echo "No scene classes found in the script."
    exit 1
fi

echo "Rendering the first scene class: $first_class"
manim "$script_file" "$first_class" -pqm

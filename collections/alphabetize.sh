#!/bin/bash

# Create directories if they don't already exist
mkdir -p A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0

# Iterate over all files in the current directory (excluding subdirectories)
for file in *; do
    # Skip if it's a directory or the script itself
    if [[ -d "$file" ]] || [[ "$file" == "alphabetize.sh" ]]; then
        continue
    fi

    # Get the first character of the filename
    first_char="${file:0:1}"

    # Convert to uppercase for comparison
    upper_char=$(echo "$first_char" | tr '[:lower:]' '[:upper:]')

    # Determine the target directory
    if [[ "$upper_char" =~ ^[A-Z]$ ]]; then
        target_dir="$upper_char"
    else
        target_dir="0"
    fi

    # Move the file to the target directory
    mv "$file" "$target_dir/"
done

echo "Alphabetization complete."

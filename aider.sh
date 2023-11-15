#!/bin/bash

# Export the API key
export OPENAI_API_KEY=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

# Check if any arguments were provided
if [ "$#" -eq 0 ]; then
    # No arguments, run aider normally
    aider --model gpt-4-1106-preview
else
    # Concatenate all arguments into a single string
    filenames=""
    for filename in "$@"; do
        filenames="$filenames $filename"
    done

    # Run aider with the concatenated filenames
    aider --model gpt-4-1106-preview $filenames
fi


#!/bin/bash
export GIT_EDITOR=true

while true; do
  if ! git rebase --continue; then
    # if it fails, check if we are still rebasing
    if [ ! -d ".git/rebase-merge" ] && [ ! -d ".git/rebase-apply" ]; then
        echo "Rebase not in progress anymore. Did it finish or abort?"
        break
    fi
    
    if python3 resolve_json_conflict.py; then
      # it resolved, loop will continue to rebase
      continue
    else
      echo "Failed to resolve conflicts automatically."
      exit 1
    fi
  else
    # rebase completed successfully
    echo "Rebase complete!"
    break
  fi
done

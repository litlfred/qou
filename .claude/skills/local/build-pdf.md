---
name: build-pdf
roles: [collaborator, owner]
user_invocable: true
description: >
  Triggers the GitHub Actions PDF build workflow (build.yml) which produces the main
  full PDF as well as per-chapter PDFs.
allowed-tools: Bash AskUserQuestion
---

# /build-pdf

This command manually triggers the GitHub Actions `build.yml` workflow to generate PDFs.
The workflow automatically handles generating both the full monolithic PDF (`main.pdf`) and the individual per-chapter PDFs (using the `split-pdf-by-chapter.py` script).

## Behavior
1. Run `git branch --show-current` to get the current branch.
2. If there are unpushed commits, advise the user to push first so the build action catches the latest changes.
3. Run `gh workflow run build.yml --ref <current-branch>` to trigger the build.
4. Once triggered, optionally run `gh run list --workflow=build.yml -L 1` to get the URL of the newly created run.
5. Provide the user with the link to monitor the GitHub Action run.

## Example Usage
```
User: /build-pdf
Agent: I have triggered the PDF build on GitHub Actions for your branch. 
You can monitor the progress and download the resulting PDFs (both the full paper and the per-chapter splits) here:
https://github.com/litlfred/qou/actions/runs/123456789
```

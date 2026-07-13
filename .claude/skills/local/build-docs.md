---
name: build-docs
roles: [collaborator, owner]
user_invocable: true
description: >
  Triggers the GitHub Actions doc-gen4 build workflow (doc-gen4.yml) which produces the Lean HTML documentation.
allowed-tools: Bash AskUserQuestion
---

# /build-docs

This command manually triggers the GitHub Actions `doc-gen4.yml` workflow to generate the Lean HTML documentation using doc-gen4.

## Behavior
1. Run `git branch --show-current` to get the current branch.
2. If there are unpushed commits, advise the user to push first so the build action catches the latest changes.
3. Run `gh workflow run doc-gen4.yml --ref <current-branch>` to trigger the build.
4. Once triggered, optionally run `gh run list --workflow=doc-gen4.yml -L 1` to get the URL of the newly created run.
5. Provide the user with the link to monitor the GitHub Action run.

## Example Usage
```
User: /build-docs
Agent: I have triggered the Lean HTML documentation build on GitHub Actions for your branch. 
You can monitor the progress here:
https://github.com/litlfred/qou/actions/runs/123456789
```

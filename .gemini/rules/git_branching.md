---
name: git-branching-protocol
description: Rules for git branching, committing, and pushing.
---

# Git Branching Protocol

1. **Always branch first:** Before committing and pushing any code changes, you MUST verify your current branch and create a new branch if you are on `main` or a protected branch.
2. **Branch naming convention (Gemini Directive):** All new branches created by the agent MUST use the prefix `gemini/` followed by a descriptive name and the date (e.g., `gemini/update-auth-logic-2026-07-07`).
3. **Push to remote:** Always push your newly created branch to the remote repository so the user can access and review the changes.

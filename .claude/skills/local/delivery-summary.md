---
name: delivery-summary
description: Post-delivery summary with server restart command and viewer links
roles: [reader, collaborator, owner]
user_invocable: true
---

# Delivery Summary

After completing a feature or edit (i.e., after pushing changes), provide:

## 1. Server restart command

A single copy-paste block to fetch, switch to the branch, pull, and restart:

```bash
git fetch origin <BRANCH> && git switch <BRANCH> && git pull origin <BRANCH> && ./scripts/start-folio-assistant.sh --http &
```

Replace `<BRANCH>` with the actual branch name you pushed to.

## 2. Viewer links

Provide links to the relevant pages showing the changes. The viewer runs on
`localhost:3200` by default (or `$VIEWER_PORT`).

Common viewer URLs:
- **Paper viewer**: `http://localhost:3200/viewer/`
- **Assistant**: `http://localhost:3200/assistant/`
- **Chapter viewer**: `http://localhost:3200/viewer/#chapter-N`
- **Specific block**: `http://localhost:3200/viewer/#<label>` (e.g., `#def:quantum-connection`)

For remote/deployed builds:
- **GitHub Pages**: `https://litlfred.github.io/qou/`
- **Draft preview** (feature branches): `https://litlfred.github.io/qou/drafts/<branch>/`

Pick the links most relevant to the changes made. If you modified a specific
content block, link directly to it via its label anchor.

## Example output

After pushing changes to `claude/feature-xyz`:

> **Restart & preview:**
> ```bash
> git fetch origin claude/feature-xyz && git switch claude/feature-xyz && git pull origin claude/feature-xyz && ./scripts/start-folio-assistant.sh --http &
> ```
>
> **See changes:**
> - Paper viewer: http://localhost:3200/viewer/#def:quantum-connection
> - Assistant: http://localhost:3200/assistant/

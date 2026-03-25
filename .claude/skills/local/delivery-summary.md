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
git fetch origin <BRANCH> && git switch <BRANCH> && git pull origin <BRANCH> && ./scripts/start-folio-assistant.sh --http
```

Replace `<BRANCH>` with the actual branch name you pushed to.

## 2. Content block change links

**This is the most important part.** List every content block that changed,
with a clickable viewer link and a short explanation of what changed.

### How to find changed blocks

Run this to extract labels from changed content `.ts` files:

```bash
for f in $(git diff origin/main..HEAD --name-only -- 'content/**/*.ts' | grep -v '/rendered/' | grep -v 'schema/' | grep -v 'pipeline/'); do
  label=$(grep -oP "label:\s*['\"]\\K[^'\"]+" "$f" 2>/dev/null || echo "")
  if [ -n "$label" ]; then echo "$f|$label"; fi
done
```

### Link format

The viewer runs on `localhost:<viewer_port>` (from `lean-mcp.config.json`).
Each block links via its label anchor:

```
http://localhost:8080/viewer/#<label>
```

### Presentation format

Group by chapter. Use a markdown table with columns: **Block** (clickable
link), **What changed** (1-line description). For example:

| Block | What changed |
|-------|-------------|
| [def:quantum-universe](http://localhost:8080/viewer/#def:quantum-universe) | Updated notation from λ to ∫_A |
| [prf:dq-squared](http://localhost:8080/viewer/#prf:dq-squared) | Added first SVG render |

### Categorize changes

Explain the nature of changes — don't just list files. Common categories:
- **Narrative edit**: `.md` content was modified
- **Re-rendered SVG**: notation/style change caused SVG hash update
- **New SVG render**: block got its first rendered SVG
- **Structural change**: label, uses[], lean ref, or kind changed
- **New block**: entirely new content block added

### Remote/deployed links

For remote/deployed builds:
- **GitHub Pages**: `https://litlfred.github.io/qou/`
- **Draft preview** (feature branches): `https://litlfred.github.io/qou/drafts/<branch>/`

## 3. GitHub links

Also provide:
- **Commit links**: `https://github.com/litlfred/qou/commit/<hash>` for each commit
- **Branch diff**: `https://github.com/litlfred/qou/compare/main...<branch>`

## Example output

After pushing changes to `claude/feature-xyz`:

> **Restart & preview:**
> ```bash
> git fetch origin claude/feature-xyz && git switch claude/feature-xyz && git pull origin claude/feature-xyz && ./scripts/start-folio-assistant.sh --http
> ```
>
> ### Changed content blocks
>
> **Chapter 1:**
>
> | Block | What changed |
> |-------|-------------|
> | [def:quantum-universe](http://localhost:8080/viewer/#def:quantum-universe) | Rewrote axiom 3 for clarity |
> | [prop:frobenius-relation](http://localhost:8080/viewer/#prop:frobenius-relation) | Re-rendered SVG (notation update) |
> | [prf:dq-squared](http://localhost:8080/viewer/#prf:dq-squared) | Added first SVG render |
>
> **Commits:**
> - [Rewrite axiom 3](https://github.com/litlfred/qou/commit/abc123)
> - [Re-render SVGs](https://github.com/litlfred/qou/commit/def456)
>
> **Full diff:** [main...claude/feature-xyz](https://github.com/litlfred/qou/compare/main...claude/feature-xyz)

---
name: delivery-summary
description: Post-delivery summary with server restart command and viewer links
roles: [reader, collaborator, owner]
user_invocable: true
---

# Delivery Summary

> **The links are the delivery; the report is not optional (2026-08-25).**
> Everything below is *packaging* — restart command, viewer links, sibling
> file list. It sits **alongside** the substantive report of what you found,
> never in place of it. A summary that lists five links and says "done" has
> delivered the artifacts and dropped the finding. What the report must carry
> — claim, evidence, implications, options, and a recommendation marked as
> judgement — is specified in **AGENTS.md §User accessibility → "Terse ≠
> compressed"**. Read it before writing this section.

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

Extract labels from changed content `.ts`/`.md`/`.lean` triples
(a `.md`-only edit is still a block change):

```bash
# Collect changed content files (any sibling triggers the block)
changed=$(git diff origin/main..HEAD --name-only -- \
  'content/**/*.ts' 'content/**/*.md' 'content/**/*.lean' \
  | grep -v '/rendered/' | grep -v 'schema/' | grep -v 'pipeline/')

# For each, resolve to the sibling .ts and pull the label
for f in $changed; do
  ts="${f%.*}.ts"
  [ -f "$ts" ] || continue
  label=$(grep -oP "label:\s*['\"]\\K[^'\"]+" "$ts" 2>/dev/null || echo "")
  [ -n "$label" ] && echo "$ts|$label"
done | sort -u
```

### Link format

The viewer runs on `localhost:<viewer_port>` (from `lean-mcp.config.json`).
Each block links via its label anchor:

```
http://localhost:8080/assistant/#<label>
```

### Presentation format

Group by chapter. Use a markdown table with columns: **Block** (clickable
link — ALWAYS to the `.md` file), **Siblings** (GitHub blob links to
`.ts`/`.lean`/etc. that **also changed**), **What changed** (1-line
description).

**Rule: the Block column always links to the `.md` file.** Sibling
links (`.ts`, `.lean`, `.tex`) appear in a separate column and only
when that sibling was actually modified in this delivery.

| Block | Siblings changed | What changed |
|-------|------------------|-------------|
| [def:quantum-universe](https://github.com/litlfred/qou/blob/<branch>/content/.../quantum-universe.md) | [ts](https://github.com/litlfred/qou/blob/<branch>/content/.../quantum-universe.ts) · [lean](https://github.com/litlfred/qou/blob/<branch>/content/.../quantum-universe.lean) | Updated notation from λ to ∫_A |
| [prf:dq-squared](https://github.com/litlfred/qou/blob/<branch>/content/.../dq-squared.md) | — | Added first SVG render |

Viewer anchor links (`http://localhost:8080/assistant/#<label>`) may be
included as an additional row-end column when the folio-assistant is
running locally, but the `.md` blob URL is the canonical reference.

### GitHub blob links — ALWAYS PROVIDE, ALWAYS `.md` FIRST

For **every** created or modified file, include a direct GitHub blob URL
using the pattern:

```
https://github.com/litlfred/qou/blob/<branch>/<relative-path>
```

**The primary link for a block is always the `.md` file.** Sibling
files (`.ts`, `.lean`, `.tex`) are listed only if they were actually
modified.  Never make the `.ts` or `.lean` the primary clickable link
for a block reference — readers want narrative first.

This applies to **all** file kinds: `.md`, `.ts`, `.lean`, `.tex`, config
files, etc.  Never report "created/edited `foo.md`" without also
giving its clickable GitHub blob link on the pushed branch.

If the branch is not yet pushed, say so explicitly — do not fabricate a
URL that will 404.

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

Always provide:
- **File blob links**: `https://github.com/litlfred/qou/blob/<branch>/<path>`
  for every created/modified file (see §2, "GitHub blob links — ALWAYS
  PROVIDE")
- **Commit links**: `https://github.com/litlfred/qou/commit/<hash>` for each commit
- **Branch diff**: `https://github.com/litlfred/qou/compare/main...<branch>`

## 4. Decisions you leave with the author (STRICT, 2026-08-29)

A summary is one of the places agents hand the author a decision, and the
commonest way to do it badly is a closing one-liner: *"the one thing waiting on
you is whether to do X"*, or a `**next**` bean entry that names a choice and
nothing else.

**Naming a decision is asking a question**, so it owes the same frame as an
`AskUserQuestion` — see AGENTS.md §"NAMING A DECISION IS ASKING A QUESTION".
In a delivery summary that means, for each decision you raise:

1. **What is being decided**, in words that do not assume the reader watched
   you work. Expand every identifier on first use.
2. **The options**, each with what it means / costs / risks / commits to.
3. **The default** — what happens if they say nothing. Usually the honest
   answer is "nothing changes", and saying so lets them defer with confidence.
4. **The blast radius in real terms** — which files, which producers, which
   published numbers. "Three consumers" is not a blast radius; naming them is.
5. **Your recommendation**, marked as judgement rather than finding.

**If you are not willing to spend those words, do not raise it in the
summary.** Leave it in the bean, where the author reads it on their own
schedule. An unframed decision in a summary is worse than no mention: it
occupies the author's attention while withholding what would let them act, and
it hides how cheap the item might be to ignore.

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
> | [def:quantum-universe](http://localhost:8080/assistant/#def:quantum-universe) | Rewrote axiom 3 for clarity |
> | [prop:frobenius-relation](http://localhost:8080/assistant/#prop:frobenius-relation) | Re-rendered SVG (notation update) |
> | [prf:dq-squared](http://localhost:8080/assistant/#prf:dq-squared) | Added first SVG render |
>
> **Commits:**
> - [Rewrite axiom 3](https://github.com/litlfred/qou/commit/abc123)
> - [Re-render SVGs](https://github.com/litlfred/qou/commit/def456)
>
> **Full diff:** [main...claude/feature-xyz](https://github.com/litlfred/qou/compare/main...claude/feature-xyz)

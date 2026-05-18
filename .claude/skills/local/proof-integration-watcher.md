---
name: proof-integration-watcher
roles: [reader, collaborator, owner]
user_invocable: true
inherits: local/integration-watcher
description: >
  Proof-QA integration watcher — watches origin/main + open active
  PRs + newly-opened PRs for narrative-proof (`.md`) or Lean-proof
  (`.lean`) changes, runs the proof QA skill suite on every
  detected change, queues gaps, attempts auto-discharge for easy
  sorries / naked conjectures with provable scaffolding, and
  escalates the rest to the author. Inherits shared mechanics
  (Monitor, subscriptions, queue, ledger, idle sweep, author-ask,
  watch-prepared-PRs, witness-drift recovery, billing-quick-fail
  flake, post-completion one-voice, sibling-PR comment protocol)
  from `local/integration-watcher`.
allowed-tools: Read Edit Write Bash Grep Glob Agent Monitor Skill
---

# /proof-integration-watcher

A concrete instance of [`local/integration-watcher`](integration-watcher.md).
The parent encodes the shared mechanics (Monitor, subscriptions,
queue, ledger, idle sweep, author-ask, watch-PRs-you-prepare,
sibling-PR comment protocol, witness-drift recovery, billing
quick-fail, post-completion one-voice). This file fills the nine
domain-specific slots A-I.

**Setup:** use `NAME=proof-integration-watcher` everywhere the
parent's §1 references `${NAME}`. Files land at
`todos/proof-integration-watcher-queue.json` and
`todos/proof-integration-watcher-ledger.md`.

## Slot A — Goal statement

No bare `sorry`, no new axioms beyond the accepted set
(`Classical.choice`, `Quot.sound`, `propext`, and any
`-- Ref:`-cited axiomatic conjectures per CLAUDE.md §3b-cond), and
no naked `conjecture` blocks whose downstream scaffolding is
actually provable. Conjectures that genuinely need axiomatisation
as Lean classes per §3b-cond are fine.

## Slot B — §3 trigger filter

For a `MAIN <sha> <msg>` line (or PR commit event):

```bash
SHA=<event sha>
changed=$(git diff-tree --no-commit-id --name-only -r "$SHA")

is_proof_event=false
echo "$changed" | grep -qE '(^|/)proof.*\.md$|(-proof|_proof)\.md$' && is_proof_event=true
echo "$changed" | grep -qE '\.lean$'                              && is_proof_event=true
echo "$changed" | grep -qE 'content/.*\.md$' && {
  # An .md without "proof" in its name still counts if its sibling
  # .ts is a proof-kind block.
  for md in $(echo "$changed" | grep -E 'content/.*\.md$'); do
    ts="${md%.md}.ts"
    [ -f "$ts" ] && grep -qE '^export default (theorem|lemma|proposition|corollary|conjecture|definition)\(' "$ts" && is_proof_event=true
  done
}
```

For PR review-comment events, pass through if the comment body
mentions: `sorry`, `axiom`, `proof`, `conjecture`, OR cites a
content block label.

## Slot C — §4b dispatch table

| Specialist | When to run |
|------------|-------------|
| `proof-gap-audit` | Always (intra + inter gaps) |
| `proof-narrative-lean-equivalence` | **Whenever `.lean` is touched OR exists for the block** — covers the four drift classes A/B/C/D + the **missing-narrative** check (`.lean` exists, `.md` absent or stub-only) |
| `lean-proof-review` | If `.lean` changed |
| `lean-completeness-audit` | If `.ts` `kind` requires Lean and `.lean` is missing |
| `remark-audit` | If kind is `remark` |
| `proof-triage` | Always — produces fresh sorry inventory for the queue |

**Lean ↔ narrative coupling rule (STRICT):** for every block where
`.lean` exists, also check (1) `.md` presence + non-triviality and
(2) semantic match per the four drift classes.

## Slot D — §4c finding taxonomy

| Finding | Severity | Description |
|---------|----------|-------------|
| `uncited-sorry` | critical | `sorry` without a `-- Ref:` adjacent to it (within 6 lines OR above enclosing decl header) per CLAUDE.md §1 |
| `hidden-axiom` | critical | New `axiom` declaration that isn't a §3b-cond class encoding |
| `drift-class-A` | critical | Lean stub-weakening — `theorem foo : True := trivial` while narrative claims something substantive |
| `conditional-class-violation` | critical | Theorem's `uses[]` transitively includes a `conj:` but the block isn't class-axiomatised per §3b-cond |
| `naked-conjecture` | major | `conjecture` block with no `.lean` sibling whose downstream scaffolding suggests it's provable |
| `gap-existence` | major | "There exists X" without construction |
| `gap-uniqueness` | major | "The unique X" without uniqueness lemma |
| `inter-proof-bridge` | major | Cited fact has no block / no import / no `-- Ref:` |
| `drift-class-B` | major | Lean proves a special case; narrative claims the general one |
| `drift-class-C` | major | Hypothesis count/strength mismatch between Lean and narrative |
| `missing-narrative` | major | `.lean` exists but `.md` sibling absent |
| `narrative-stub` | major | `.lean` exists but `.md` is < 5 body lines + no math |
| `drift-class-D` | minor | Notation drift (paper uses `$\varrho$`, Lean uses `gamma`, etc.) |
| `cite-position-hygiene` | minor | `-- Ref:` is in the enclosing decl body but not in the 6-line window above the sorry |

## Slot E — §4d discharge bands (examples)

| Band | Examples |
|------|----------|
| **Auto-discharge** | `uncited-sorry` with goal matching positivity / ring / linarith / aesop / norm_num — try `lean_multi_attempt` with the canonical tactic set; `cite-position-hygiene` — move/add the `-- Ref:` line |
| **Auto-discharge (special)** | **Naked conjecture with fully-defined `uses[]` cone** — attempt discharge via `local/formalizer` + `local/lean-generation` before defaulting to author-assist. This is the *"if a conjecture is a placeholder for something to be proved, try"* clause of this watcher's mission. |
| **Author-assist** | Class A stub-weakening, hidden axiom, naked conjecture without conditional-class scaffolding, broken inter-proof chain, conjectural-propagation violation |
| **Defer** | Minor stylistic gap, sorry already carrying `-- Ref:`, conjecture correctly class-axiomatised per §3b-cond |

## Slot F — §4e author-ask templates

For `missing-narrative` / `narrative-stub`:

> The Lean sibling at `<lean-url>` proves `<lean-statement>`.
> The narrative `.md` is `<missing | stub | claims X instead>`.
> Question: 1) write narrative to match Lean, 2) weaken Lean to
> match narrative, 3) split into two blocks?

For `naked-conjecture` (after auto-attempt failed):

> Naked conjecture `<label>` at `<url>` has no `.lean` sibling and
> discharge attempts via formalizer + lean-generation failed
> (tried tactics: <…>). Question: 1) author conditional-class
> encoding, 2) demote to remark with `interprets`, 3) mark wontfix.

For `drift-class-A` (stub weakening):

> Lean `<decl>` at `<url>` is `: True := trivial` while narrative at
> `<url>` claims `<substantive statement>`. Question: 1) write a
> real Lean statement + sorry with Ref, 2) demote narrative to a
> remark with `interprets`, 3) confirm stub is intentional (will
> record as Class-A acknowledged).

## Slot G — §5a backlog discovery

```bash
# 1. Proof-relevant content blocks
grep -rlE '^export default (theorem|lemma|proposition|corollary|conjecture|definition)\(' \
  content/ --include='*.ts' 2>/dev/null \
  | sort -u > /tmp/_pw_proof_blocks.txt

# 2. Uncited sorries — smart detection: skip block comments, skip
#    "sorry-free" text, look in 6-line window above the sorry AND
#    in the 6 lines above the enclosing theorem/lemma/instance/def
#    header. This avoids both false positives (docstring "sorry-free")
#    and false negatives (cites on the wrong side of the sorry).
#    Implementation: see find_uncited_sorries() in this skill's
#    delivery (regex DECL_RE + per-line check + window scan + decl
#    walk-back).

# 3. Naked conjectures (no .lean sibling)
grep -rlE '^export default conjecture\(' content/ --include='*.ts' 2>/dev/null \
  | while IFS= read -r ts; do
      lean="${ts%.ts}.lean"
      [ ! -f "$lean" ] && echo "$ts"
    done > /tmp/_pw_naked_conjectures.txt

# 4. Dual-sibling discovery — .lean exists but .md missing or stub.
#    Heuristic must handle (a) .md files without `---` frontmatter
#    (don't count 0 body lines) and (b) .md files using LaTeX
#    `\begin{equation}` instead of `$...$` (count as has_math).
> /tmp/_pw_missing_narrative.txt
> /tmp/_pw_narrative_stub.txt
find content -name '*.lean' -type f 2>/dev/null \
  | grep -v '/lean/' \
  | while IFS= read -r lean; do
      md="${lean%.lean}.md"
      ts="${lean%.lean}.ts"
      [ ! -f "$ts" ] && continue
      if [ ! -f "$md" ]; then
        echo "$lean" >> /tmp/_pw_missing_narrative.txt
        continue
      fi
      if head -1 "$md" | grep -q '^---$'; then
        body_lines=$(awk '/^---$/{f++; next} f>=2 && NF' "$md" | wc -l)
      else
        body_lines=$(grep -c . "$md")
      fi
      has_math=$(grep -cE '\$|\\begin\{(equation|align|tikzcd|gather|displaymath)' "$md")
      if [ "$body_lines" -lt 5 ] && [ "$has_math" -eq 0 ]; then
        echo "$lean" >> /tmp/_pw_narrative_stub.txt
      fi
    done
```

## Slot H — §5b prioritisation

Override the parent's default rule with this proof-specific ordering:

1. **Sorry count** (more sorries → earlier): `grep -c '^[^-]*sorry' <block>.lean`
2. **Lean-without-narrative** (any `.lean` block whose `.md` sibling
   is missing or stub-only). These are presumed-published Lean
   results with no human-readable statement.
3. **Downstream dependents** (more dependents → earlier): walk
   `uses[]` from every other block; count edges pointing here.
4. **Last-audit recency** (older → earlier) from `queue.audited[]`.
5. **Alphabetical** as tie-breaker.

## Slot I — §6 invariants

| Invariant | Check |
|-----------|-------|
| Every `sorry` has `-- Ref:` | `grep -B6 '^[^-]*sorry' <file>.lean \| grep -qE -- '-- Ref:'` OR enclosing decl header carries it |
| No new `axiom` declarations | `git diff origin/main -- <file>.lean \| grep -E '^\+axiom '` is empty |
| Naked conjectures attempted | Every `conjecture` block touched in this branch has a `formalizer` attempt log in the queue (status `resolved` or `needs-author`) |
| No conjectural propagation regressions | `cd content && bun run pipeline/conjectural-propagation-audit.ts` reports no new violations vs main |

If any invariant fails on a proposed commit, **block the commit**,
queue the violation as `critical`, and ask the author (per
parent §6).

## Domain-specific anti-patterns (extends parent)

- ❌ Auto-fix a conjecture statement (turn `conjecture` block into
  a `theorem` block) without explicit author approval.
- ❌ Add a `-- Ref:` to a sorry without verifying it actually
  cites a real entry in `content/schema/references.ts`.
- ❌ Discharge a sorry without `lean_verify` post-check (axiom
  audit). An "easy fix" adding `Decidable.em` isn't a fix.

## Checklist (extends parent)

- [ ] Slot G discovery produced the four enumerations
- [ ] Slot D taxonomy applied to every finding
- [ ] Naked-conjecture special case (Slot E auto-discharge band)
      attempted before any conjecture finding is asked
- [ ] Conditional-class violations (Slot D
      `conditional-class-violation`) block the commit per
      Slot I invariants

---
# qou-vstf
title: Agent-kind QA verdicts are never recomputed — some quote prose that was never in the block
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T22:05:10Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-5vkl
---

Found 2026-09-04 while re-encoding the eight §3b-cond item-5 violations of `qou-tmmt`.

## The mechanism

`qa-sweep` recomputes `script`-kind criteria on every run. It does **not**
recompute `agent`-kind ones — an agent verdict stands until an agent replaces
it. So a wrong or outdated `fail` persists indefinitely and reads to every later
agent as a live defect on the block.

`scripts/check-sidecars.sh` does not catch it either: it keys on *changed files*,
not on missing or stale entries.

## Two confirmed instances, both verified against `git log`

- `mass-endomorphism/hecke-branching-trace-decomposition`, `trap-nonspeakable`,
  recorded 2026-08-22. Quotes copular substitution — *"A^lambda_{mu,nu}(I) …
  **constructs** the operator-valued coefficient"*. Grepping **every revision**
  of that `.md`: the wording never existed. The block has always read *"**is**
  the operator-valued coefficient"* — the copula the criterion asks for. Its
  `field_hash` still matches the file, so the verdict is not stale; it was
  wrong when written.
- `stochastic-mechanics/classical-limit-adelic-assembly`, `trap-superlative`.
  Quotes *"the rigorous mechanism behind the loss of quantum information"*. The
  `.md` has exactly one revision and the phrase is not in it.

Three more (`rho-k-h3a-refinement` ×2, `sigma-shell-…` ×1) were genuinely stale
rather than fabricated — they quoted prose this branch had just deleted — and
are re-adjudicated in the same PR.

## Triage tool

[`scripts/qa-stale-agent-verdicts.py`](../scripts/qa-stale-agent-verdicts.py)
splits two independent axes: **STALE** (recorded `field_hash` ≠
`sha256(file)[:12]`) and **UNFINDABLE** (no quoted prose run survives in the
block). Unfindable-and-stale = edited away; unfindable-but-current = the verdict
quotes prose that is not in the very file it was recorded against.

Measured on `main` 2026-09-04, over 3630 sidecars and 1103 agent-kind FAILs:

| bucket | count | unfindable | present | undecidable |
|---|---|---|---|---|
| STALE (hash mismatch/absent) | 179 | **27** | 62 | 90 |
| current (hash matches disk) | 924 | **166** | 560 | 198 |

## 🛑 Do NOT quote 166 as a count of bad verdicts

It is a **triage list**. Two separate over-counts were found and only one is
fixed:

1. **Fixed.** A plain substring test reported 393 in the current bucket. Evidence
   quotes ASCII-ise LaTeX (`$\lambda$` → `lambda`), so the quote cannot match
   the source verbatim. Comparing only *prose runs* (≥ 5 alphabetic words,
   ≥ 25 chars, math and punctuation as separators) gives 166 — the substring
   method over-reports by **2.4×**.
2. **Not fixed.** The tool cannot distinguish a quotation *of the block* from
   the reviewer's own prose set in quotes. `outro-stochastic-mechanics` is
   flagged on *"…'s own opening para…"*, which is the reviewer describing the
   block, not quoting it. So 166 is still an over-count of unknown size.

Confirm each case against `git log -p` on the block. A span absent from HEAD may
still have existed when the verdict was written.

## Next

- Triage the 27 stale-and-unfindable first: those are the cheap ones, since the
  block demonstrably changed.
- Decide whether `qa-sweep` should mark an agent verdict `needs-agent` when the
  `field_hash` drifts, rather than leaving it asserting `fail`. That is an
  owner/platform call — the change is in `litlfred/folio-assistant`, not here.
- Note the related trap found the same day: dropping a criterion and re-running
  `qa-sweep --only <crit>` prints `[needs-agent]` but writes **no entry**, so
  the criterion goes *absent* and a naive "any failing criteria?" check reads
  clean. An absence is not a pass.


---

## 🛑 2026-09-05 — RETRACTION: the "quotes text that was never in the block" claim is WRONG

**What I published on 2026-09-04** (bean above, PR #6681 body, commit
`1dca78c61f`): two verdicts were "confirmed against `git log`" as quoting prose
that **never existed at any revision** — hecke's `trap-nonspeakable` and
`classical-limit-adelic-assembly`'s `trap-superlative`.

**What is actually true.** Both quotes existed and were removed:

    git log --all --oneline -S "constructs the operator-valued" -- '*.md'
      5a5c153f72  qa(trap-drain): in-flight checkpoint — g01/h00/i00 partial [qou-ujp8]

    git log --all --oneline -S "rigorous mechanism behind the loss of quantum information" -- '*.md'
      e365b47d95  qa(trap-drain): in-flight checkpoint — n02/p01 partial [qou-ujp8]

Both are `qou-ujp8` trap-drain commits — i.e. the findings were **genuine**,
someone fixed the prose, and the verdicts outlived the fix. Ordinary staleness.

**How I got it wrong.** My check walked `git log --format=%h -- <current path>`,
which is not the file's history. Without `--follow` a renamed or moved block
shows a truncated log, and blocks here move between chapter directories — one
case returned **1** revision where `--follow` returns **12**. So "searched every
revision" searched almost none, and an empty result read as proof of absence.

**The rename-proof check**, which finds the text wherever it lived:

    git log --all --oneline -S '<distinctive phrase>' -- '*.md'

An empty path-limited log is not evidence. An empty `--all -S` search is.

**What survives, unchanged and still the point.** `qa-sweep` recomputes
`script`-kind criteria every run and **never** `agent`-kind ones, so a verdict
outlives the fix that addressed it and reads to every later agent as a live
defect. Five instances hit this session (hecke, rho-k ×2, sigma-shell, lr-tensor,
gb-residue). `check-sidecars.sh` does not catch it either — it keys on changed
files, not stale entries. Every re-adjudication recorded this session stands on
its own merits: in each case I read the current text and confirmed the finding
was addressed. Only the *explanation* was wrong.

**Confirmed fabricated quotes: ZERO.** Do not repeat that claim.

## A second method defect, found the same hour

The quote extractor `'([^']{25,})'` treats an **apostrophe as an opening quote**,
so a possessive or contraction in the reviewer's own prose — "the block's final
section is …", "the corpus's named token substitution" — opens a phantom
quotation running to the next apostrophe. That captures reviewer commentary that
was never in the block and never could be found there.

Fixed by requiring the opening `'` not to follow a letter. Measured effect on the
corpus:

| | before | after |
|---|---|---|
| unfindable, current bucket | 166 | **125** |
| unfindable, stale bucket | 27 | **21** |

About a quarter of the flags, not "most" — I wrote "most" in the script docstring
one command before I had the number, and corrected it. The substring-vs-prose-runs
over-report factor was also re-measured with the fix in place: **2.9×** (359
against 125), where the pre-fix figures were 393 against 166.

**So the triage list is now 125 + 21, and every entry still needs the
rename-proof per-case check before anything is cleared.**


## 2026-09-05 — the "never existed" question is CLOSED as unanswerable here, and the answer keeps moving toward "it existed"

After the retraction above I tried to get an honest count of the 21
stale-and-unfindable. Three methods, each overturning the last:

| method | confirmed genuinely stale, of 21 | why it under-reports |
|---|---|---|
| `git log --format=%h -- <path>` | 2 | not a file's history — truncates at a rename (1 revision where `--follow` gives 12) |
| `git log --all --follow -p -- <path>` | **8** | follows ONE rename chain; misses a block split, copied, or duplicated under another path |
| `git log --all -S '<phrase>' -- '*.md'` | ≥ 9 | best of the three, but only a POSITIVE test |

The third overturned the second on a case the second had cleared:
`yekutieli-quantum-li`'s *"This multiplicative integral provides the precise
formulation…"* was "no history hit" under `--follow -p`, and `-S` finds it in
`3e28f95d1e`, a `qou-ujp8` trap-drain. Note also that one `-S` hit was in an
**agent-scratch directory copy** — a path in no block's rename chain at all,
which is precisely what `--follow` cannot see.

**Every single case chased to a conclusion has turned out the same way: the
prose existed, a trap-drain fixed it, and the verdict outlived the fix.** The
count of confirmed-stale has risen at every attempt (2 → 8 → 9+) and the count
of confirmed-fabricated has stayed at **zero**.

**So the right conclusion is not a number, it is a reframing.** `UNFINDABLE`
means *the quote is not in the block now* — a staleness signal, nothing more.
The script now says so, records all three methods and why the first two
under-report, and states that its silence is not evidence a verdict was
fabricated. Do not try to produce a "never existed" count from this repo; no
method here supports one.

**What this does not change.** The mechanism is untouched and is the finding:
`qa-sweep` never recomputes `agent`-kind criteria, so a verdict outlives the fix
that addressed it. If anything this strengthens the case for the fix — if
essentially all of the 125 + 21 are drained findings rather than bad verdicts,
then the whole population is stale-and-clearable, and the right change is in
`litlfred/folio-assistant`: mark an agent verdict `needs-agent` when its
`field_hash` drifts, instead of leaving it asserting `fail`.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-5vkl`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

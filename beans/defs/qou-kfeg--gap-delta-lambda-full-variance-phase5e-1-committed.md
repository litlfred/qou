---
# qou-kfeg
title: 'GAP: delta-lambda-full-variance-phase5e-1 committed witness is not reproducible (~1e-8), cause unidentified'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T09:10:24Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

## What is established

`computations/delta_lambda_full_variance_phase5e_1.py` **could not run at all**
on `main`: `phi_k_with_K` called `qfac(n_strands, Q0_PROTON)` while the file
imported the one-argument `q_mpmath.qfac`, so the first statement of that
function raised

    TypeError: qfac() takes 1 positional argument but 2 were given

That is a plain arity error, not one of the domain guards the corpus defines,
so it is a real defect. It is fixed (import `hecke_characters.qfac(n, q)`,
which takes the anchor), and the producer now runs and writes its witness.

The shadow was already present at `78c74bc5ed4` (2026-08-29), the last commit
that touched the file. Whether it predates the committed witness cannot be
settled here: agent clones are shallow, and `git log -S` over the file returns
nothing beyond the fetched window.

## The open part

The re-run does **not** reproduce the committed witness. `B_dim` differs at the
8th significant digit:

| atom | committed | re-run | rel |
|---|---|---|---|
| D | 0.7099929209618748 | 0.709992911756563214 | 1.297e-8 |
| T | 2.904828630958546 | 2.9048286412962955 | 3.559e-9 |
| 3He | 2.7437891616643793 | 2.74378914750591524 | 5.16e-9 |
| 4He | 14.107328810729909 | 14.1073291888089628 | 2.68e-8 |

**Four hypotheses were tested and all four are refuted.**

1. *The f64 -> mpf precision fix explains it.* No. Holding everything else
   fixed and varying ONLY the q anchor between the 50-digit string and exact
   binary64 moves `B_dim` by **3.8e-17 to 2.1e-16** — nine orders of magnitude
   short of the gap.
2. *Catastrophic cancellation in `Phi_free - Phi_atom` amplifies f64 noise.*
   No. Measured for D: the two Phi agree to 1.3 % at k=0, 29 % at k=1, 34 % at
   k=2, 29 % at k=3, 1.4 % at k=4. There is no cancellation to amplify.
3. *The upstream `atom-chi-rust-*` witnesses drifted.* No. All four have been
   regenerated since `78c74bc5ed4`, but running against the OLD versions
   (extracted with `git show 78c74bc5ed4:`) gives **byte-identical** `B_dim` to
   running against the current ones.
4. *The hardcoded `m_e` (0.51099894999999995, which shadowed the CODATA import
   twice) explains it.* No. `alpha_k(k>=4) = m_e*8G` does feed `B_dim`, but the
   constant is only 1.35e-9 from CODATA and restoring it leaves the gap at
   1.297e-8 / 3.009e-9 / 5.746e-9 / 2.568e-8 — essentially unchanged.

Convention C is ruled out as the cause: substituting `z = sqrt(q)/(q+1)` moves
`B_dim` by 0.3 % to 15 %, so the committed witness is convention D.

## Why it matters, and why it is not urgent

The witness is small in the corpus's dependency graph — nothing was found
reading `delta-lambda-full-variance-phase5e-1.witness.json` — and the re-run is
now REPRODUCIBLE, which the committed value was not. So the new number is the
better one to hold even without knowing what produced the old one. What is
unresolved is the provenance question: something once computed this quantity
differently by ~1e-8 and left no trace of what.

## Next honest step

Diff the producer against its own recorded `scriptCommitSha` if a deeper clone
is available (`git fetch --unshallow`), which paths 1-6 of the corpus-grep
checklist cannot substitute for. Failing that, leave it: a documented
non-reproducible witness is worth more than a guessed explanation.


## A SECOND instance of the same class: `paper-six-term-isotope-sweep`

Found 2026-09-07 while draining the same producer. Same shape as the phase5e
case above, better characterised.

**The drain is precision-only, and that is measured, not assumed.** The
UNMODIFIED producer at `8f7e7829218` reproduces the same 15 moved values,
byte-for-byte (`term5_chirality_factor_a_K` for the proton: 2.3897210637310238
-> 1.5032359764467356 under both). So the committed witness is stale
independently of this session's edits.

**Hypotheses tested:**

1. *The braid-ordering ruling (`qou-hu1f`, 2026-09-05) changed the word.*
   REFUTED, and my first test of it was wrong. `mass_at_3A_proper.py` is the
   only file in `aK_v2`'s import cone dated after the witness, and
   `term5_v2_chirality._aK_v2_cached` does call `atom_braid_word_3A` -- so it
   looked exactly like import-cone drift. Comparing the FULL words (my first
   attempt compared only the first 6 elements) across `deb9ff5728f~1` -> HEAD:
   **identical at (1,0), (0,1) and (1,1)**, lengths 11/11/23. Feeding the old
   word to `aK_v2` gives 1.50323597644673557 -- the new value, not the
   committed one.
2. *`aK_v2` is non-deterministic.* Refuted: two separate processes agree to 20
   digits.
3. *An upstream witness drifted.* The four upstreams checked
   (`brane-tower-isospin-diagnosis`, `flavor-dressed-mass-from-substrate-split`,
   `per-nucleon-shift-derivation`, and the `term5_v2_chirality` /
   `wedderburn_jones_markov` / `hecke_characters` cone) are ALL dated
   2026-08-29, older than the witness (2026-08-30).

**Best-supported explanation, marked as inference rather than measurement:**
the witness was never regenerated as a whole. Its last commit,
`96a1315ab54` (2026-08-30), changed 62 lines and **did not touch
`term5_chirality_factor_a_K` at all** -- so those values predate it. The file
is a partially-updated artifact, and this session's run makes it
self-consistent for the first time.

**Environment caveat, disclosed rather than argued away.** This container
records python 3.11.15 / numpy 2.4.6 / scipy 1.17.1 against the committed
3.13.12 / 2.5.2 / 1.18.1 (mpmath goes the other way, 1.3.0 -> 1.4.1). The
producer contains **zero** `np.` uses -- numpy is imported `# noqa: F401 (kept
for downstream consumers)` -- so it does not use the downgraded libraries
itself. Whether a transitive import does is NOT established here, and the
HEAD-vs-modified comparison cannot separate environment from staleness because
both runs share this container.


---

## The commit archaeology in this bean, and in any sibling bean, CANNOT be done in an agent clone (measured 2026-09-07)

This bean records witnesses that are not reproducible from their own producers, and it — like several attempts since — reached for `git log -- <path>` to ask *when* and *why* producer and witness diverged. **That question is not answerable here, and the answer git gives is confidently wrong.**

Agent clones of this repo are **shallow**. `git rev-parse --is-shallow-repository` returns `true`, `.git/shallow` exists, and the boundary commit **`78c74bc5ed4`** has **no parents** in the clone. Everything older than the boundary is grafted onto it, so:

- `git log --oneline -- computations/delta_lambda_fr_identity_phase5c.py` returns **exactly one commit** — the boundary. Not "the file was written once"; "this clone cannot see before the boundary".
- `git show --name-only 78c74bc5ed4` lists **45,567 files** (3,427 witnesses, 4,298 `.py`). It is not a mass commit; it is the horizon.
- `git log -S "<symbol>" -- <file>` also returns only the boundary, so you cannot localise when a function appeared either.
- 2,625 of those 3,427 witnesses have a `computedAt` predating the boundary — which looks exactly like a systematic "edited the producer, committed a stale witness" pattern and **is not evidence of one at all**.

I walked into all four of these in one session, and built a causal story on the fourth ("the commit that fixed the layer straddle did not re-run the producer") before checking `.git/shallow`. The story was withdrawn; the underlying staleness was real, because it had been measured a different way.

**What IS measurable in a shallow clone, and is what these beans should rely on:**

- **Self-staleness**, from the witness alone: recorded `witness.scriptHash` vs a fresh SHA-256 of the producer. For `delta-lambda-fr-identity-phase5c`: recorded `7f4542540f92`, live `11711368bfb6`, `computedAt 2026-08-10` — self-stale, no history needed.
- **Input disagreement at HEAD**: does the committed witness's value match the committed input it reads? For `binding-reeb-phase-decomposition`, the recorded `χ_atom` matched **no** committed version of `atom-chi-rust-d`, while a fresh run matched it byte-for-byte. That settles *which* record is right without settling *when* it went wrong.
- **A fresh run**, diffed field-by-field against the committed witness.

AGENTS.md already warns about the shallow boundary — under the `rewritten`/`scriptCommitSha` discussion, where it notes a sha can be missing "merely because the history was never fetched". This is the same fact reached from the other side: **`git log -- <path>` is not a source of provenance here.** Do not ask a shallow clone *when*; ask the artifacts *what*.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8357, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

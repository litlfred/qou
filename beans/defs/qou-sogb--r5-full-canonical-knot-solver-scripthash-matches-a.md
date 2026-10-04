---
# qou-sogb
title: 'r5-full-canonical-knot-solver: scriptHash MATCHES and 733 fields move deterministically — the documented ''diff the producer first'' check says safe and is wrong'
status: todo
type: bug
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T12:41:19Z
updated_at: 2026-10-04T15:14:37Z
parent: qou-5vkl
---

Found 2026-09-13 while screening `r5-full-canonical-knot-solver.witness.json`
(637 baseline fields) as a raw-float64 drain target. It is not a drain — it is a
counterexample to the check AGENTS.md tells every idle pass to run.

## The finding

    committed witness scriptHash : 667a84ec1d91
    live producer sha256[:12]    : 667a84ec1d91          <- MATCH
    committed computedAt         : 2026-08-24T05:02:49Z

**The producer is byte-identical to the one that wrote the witness.** A re-run
today differs in **733 of 1448 fields**, and not only in precision:

    .data.per_atom_results[0].historical_cross_check.rank_in_full_search   990 -> 1013
    .data.per_atom_results[0].lp_dual.channel_braid_words[0][1]             -2 -> 1
    .data.per_atom_results[0].lp_dual.channel_braid_words[0][2]             -2 -> 2

A **rank** and the **LP's selected channel words** moved. Those are structural:
per AGENTS.md's LP/SDP section the active channels *are* the "most receptive
sub-braids" — which Wedderburn blocks the bound state saturates. 33 fields
appeared, 1 vanished.

## It is DETERMINISTIC — measured, not assumed

Two consecutive fresh runs are **byte-identical across all 1448 fields** (0 keys
differing). So the movement is not solver nondeterminism, and it is not the
producer. It is the producer's *environment* or its *import cone*.

## Which one is NOT established, and both changed

**Environment** — 3 of 8 recorded keys differ:

| key | committed | live |
|---|---|---|
| `clarabel` | **None** (absent) | **0.11.1** |
| `mpmath` | 1.3.0 | 1.4.1 |
| `pyhecke_native_build` | `e114ae83ee1a611f` | `e3fab84c4c1df76a` |

`clarabel` absent → present is the suggestive one: it is the SDP backend
`lp_dual_solver` uses, so the LP would have taken a fallback path when the
witness was written. That fits the channel-word change — **fits, not shown**.

**Import cone** — all six first-party modules changed after 2026-08-24:

    q_parameter             2026-09-05  f521d5da9ed
    experimental_constants  2026-09-07  320d9339725
    lp_dual_solver          2026-08-29  78c74bc5ed4
    witness_base            2026-08-29  78c74bc5ed4
    klr_canonical_basis_filter  2026-08-29  78c74bc5ed4
    mass_formula_6term      2026-08-29  78c74bc5ed4

Four in **one commit**, `78c74bc5ed4` (`fix(qou-vtlj): the anchor had 49 digits,
not 10`), and one of them is `lp_dual_solver` — the module that would decide the
channel words. That is the leading candidate and it is **not** the environment.

🛑 **So this instance does NOT discriminate**, and I am not claiming it as the
corpus's first confirmed environment case. AGENTS.md records that environment
drift is a *hazard not yet measured here* and that its one candidate
(`binding_canonical`, 48 %) turned out to be import-cone. This one has both
moving at once; calling it either would be the same over-scoping.

**The discriminator, for whoever picks this up:** check out `78c74bc5ed4^` for
the six cone modules only, leave the environment as-is, and re-run. If the 733
collapse, it is the cone; if they persist, it is the environment.

## Why it matters beyond this one witness

AGENTS.md's idle-pass discipline says, for a self-stale witness: **"Diff the
producer first (`git diff <witness.commitSha> -- <producer>`): `scriptHash` is a
whole-file hash, so a comment- or docstring-only edit drifts it while the
recomputed payload is byte-identical."** That guards the false-POSITIVE
direction. This is the false-NEGATIVE direction and the same passage's other
half already warns of it — *"a producer's own source can be byte-stable while the
module it calls changed … a file-local `git diff` cannot see this"* — but the
worked example given there (`binding_canonical`, `tr_M_atom` 0.388 -> 0.575) is
a **numeric** move. This one moves a **rank** and an **LP active set**, i.e. a
structural conclusion, which is the more expensive failure: a numeric drift is
visible as a changed digit, a changed active set reads as a different physical
statement about which blocks saturate.

**Nothing was committed.** Both runs were reverted with `git checkout --`;
regenerating this witness moves recorded results and belongs to whoever owns the
R5/SDP arc, not to a float64 drain pass, under the 2026-09-07 ASK-THE-OWNER
directive.

## Consequence for the drain queue

The 637 raw-float64 fields on this witness **cannot be drained by re-running the
producer** without also landing the 733-field regeneration. Same shape as
`binding-single-pipeline-comparison` (`qou-5c64` / `qou-gjkv`, 299 fields): a
drain blocked behind a regeneration decision. That is now **two** of the
baseline's larger entries in that state, 936 fields between them — worth knowing
before ranking targets by size.

Aside, unresolved and small: my non-integral float count for this witness is
**677** against a baseline entry of **637**. The same count matched the baseline
exactly on three other files (93/93, 117/117, 216/216), so the method is right in
general and something about this file differs. Not chased.

## RESOLVED 2026-09-14 — it is the IMPORT CONE. The environment is present, drifted, and INERT.

Ran the discriminator this bean prescribes. **Reproduced the baseline exactly in
a different container first**: 733 moved / 33 appeared / 1 vanished, byte-for-byte
the figures above. New detail: **61 of the 733 are structural** (rank /
channel_braid_words / active_set), the rest numeric.

### The discriminator

Used a better base than the one proposed: the witness's **own recorded
commitSha**, `550985daa5a` (2026-08-24 05:01:35), which **resolves** in this
clone. That is the exact tree when the witness was written, rather than
`78c74bc5ed4^`.

| run | moved | appeared | vanished | structural |
|---|---|---|---|---|
| current cone + current env (reference) | **733** | 33 | 1 | **61** |
| **OLD cone + current env** (discriminator) | **0** | 6 | 0 | **0** |

**Verdict: the import cone, unambiguously.** With the cone reverted and the
environment left untouched, the committed witness reproduces with **zero** moved
fields. The 6 that appear are additive LP-dual diagnostics
(`gap_recomputed_str`, `residual_dual_str`, `residual_primal_str`, ~1e-21 to
1e-46), not moved values.

The environment in this container **is** drifted, and is demonstrably inert:

    clarabel              absent           -> 0.11.1
    mpmath                1.3.0            -> 1.4.1
    pyhecke_native_build  e114ae83ee1a611f -> 5df83fbc24b06f8a   (a THIRD build, not the one above)

### Per-module attribution (each at HEAD, other two at the witness commit)

| module | moved | structural |
|---|---|---|
| `q_parameter.py` | **0** | 0 |
| `substrate/experimental_constants.py` | **360** | 27 |
| `mass_formula_6term.py` | **722** | 60 |

`mass_formula_6term` dominates; `experimental_constants` is a substantial
second; they overlap (722 + 360 > 733). `q_parameter` is inert for this witness.

## 🛑 The bean's cone evidence was wrong, and the way it was wrong is reusable

This bean names **`lp_dual_solver` as the leading candidate** — *'the module
that would decide the channel words'* — on the strength of *'four in one commit
78c74bc5ed4'*. Measured:

- `computations/lp_dual_solver.py` is **byte-identical** to the witness commit.
  It cannot be the cause. Same for `witness_base.py` and
  `klr_canonical_basis_filter.py`. **Three of the six named modules did not
  change at all**; only three did.
- `78c74bc5ed4` is **45,555 files changed, 15,589,663 insertions, zero
  deletions** — a bulk re-add / history artifact, not a code change. Every entry
  reads `| N +`.
- The real history: `lp_dual_solver.py` has **exactly one** commit between the
  witness and main (`638f298ffb`, itself a merge), with identical content.

**The lesson:** a `git log` date says a commit *touched* a path; it does not say
the *content* changed. A bulk re-add makes every file it sweeps look freshly
modified. Check `git diff <base> -- <file>` for content before attributing cause
— the same metadata-vs-content confusion this corpus keeps finding one level up.

The bean's discriminator **design** was right and is what settled this; only its
inputs were wrong.

## Consequence for the standing AGENTS.md question

AGENTS.md records environment drift as *'a hazard, not yet measured here'* whose
one candidate (`binding_canonical`, 48 %) turned out to be import-cone. **This
is a second candidate, also import-cone** — and stronger than the first, because
here the environment is *demonstrably* drifted on three keys and *demonstrably*
inert. Environment drift remains **unconfirmed in this corpus, now 0 for 2**.

## Unchanged

Nothing committed; tree verified byte-identical to HEAD afterwards (the producer
writes no sibling witnesses — confirmed, only its own). The 637 raw-float64
fields still cannot be drained without landing the 733-field regeneration, which
belongs to the R5/SDP arc. **Bean stays open on that**: what is resolved is the
cause, not the regeneration decision.

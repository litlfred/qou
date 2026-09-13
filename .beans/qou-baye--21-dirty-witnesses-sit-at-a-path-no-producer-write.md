---
# qou-baye
title: 21 dirty witnesses sit at a path NO producer writes — 1550 baseline fields undrainable, and the paper cites two of them
status: todo
type: task
priority: normal
created_at: 2026-09-07T17:37:47Z
updated_at: 2026-09-13T05:42:00Z
---

## What was measured

The raw-float64 baseline (`computations/raw-float64-baseline.json`) keys witnesses by **path**. For **21 dirty entries totalling 1,550 fields**, that path is one **no producer writes to**. Every producer here uses the `Path(__file__).parent / "<stem>.witness.json"` idiom and lives in a *different* directory — almost all in `computations/probes/`, with `substrate/` and `alpha/` accounting for two more. The orphans are pre-refactor copies left at the `computations/` root when the producer moved into a cluster subdir (the 2026-06-02 subdirectory refactor that `_path_bridge` exists to serve).

Consequence: **no amount of producer work drains them.** Fixing the producer regenerates the sibling; the baseline keeps counting the ghost.

Measured with `witness_raw_float64_audit.count_raw_floats` on both copies of every duplicated stem, plus a source scan of every `computations/**/*.py` for the stem in a write context.

| orphan (in the baseline) | its fields | live path | live fields |
|---|---:|---|---:|
| `computations/pentagon-rt-torus-knot-higgs-probe.witness.json` | 346 | `probes/` | **0** |
| `computations/pentagon-to-borromean-h4-probe.witness.json` | 216 | `probes/` | **0** |
| `computations/ew-couplings-substrate-derivation-probe.witness.json` | 178 | `probes/` | 176 |
| `computations/rt-route-w-specific-correction-probe.witness.json` | 117 | `probes/` | 117 |
| `computations/geom-leading-alt-q-locality-probe.witness.json` | 115 | `probes/` | 115 |
| `computations/rt-w-sqrt-quantum-two-probe.witness.json` | 105 | `probes/` | 105 |
| `computations/pentagon-multipair-borromean-h4-probe.witness.json` | 93 | `probes/` | 93 |
| `computations/six-fifths-deviation-h4-correction-probe.witness.json` | 45 | `probes/` | 45 |
| `computations/vol-density-borromean-h4-probe.witness.json` | 44 | `probes/` | 44 |
| `computations/per-knot-density-borromean-h4-probe.witness.json` | 44 | `probes/` | 44 |
| `computations/higgs-h6-correction-probe.witness.json` | 42 | `probes/` | 42 |
| `computations/hecke-core-symbolic-migration.witness.json` | 31 | `substrate/` | **0** |
| `computations/three-term-wedderburn.witness.json` | 29 | `alpha/` | 29 |
| `computations/qm-channel-contribution-probe.witness.json` | 26 | `probes/` | 26 |
| `computations/rt-binomial-trace-evaluation-probe.witness.json` | 25 | `probes/` | 25 |
| `computations/vol-density-borromean-q-locality-probe.witness.json` | 22 | `probes/` | 22 |
| `computations/per-knot-density-borromean-q-locality-probe.witness.json` | 22 | `probes/` | **0** |
| `computations/qbeta/qbeta-phib-2loop-bdictionary.witness.json` | 18 | `probes/` | 1 |
| `computations/he4-sdp-compositional-probe.witness.json` | 17 | `_deprecated/` | 14 |
| `computations/t6-tau-h5-embedding-probe.witness.json` | 10 | `probes/` | 10 |
| `computations/h4-h2-cross-algebra-bridge-probe.witness.json` | 5 | `probes/` | 5 |

**633 of those 1,550 fields are ALREADY FIXED at the live path** (the five rows with a live count of 0 or 1). Those producers were drained; the orphan was simply never removed, so the backlog still charges the corpus for work that is done.

## This is a DIFFERENT defect from what `qou-kcii` records

`qou-kcii` says duplicated stems are **double-counted** — both paths in the baseline, and re-running drains one. That is real and covers **18 stems / 2,374 fields**. It is not this. Here the baseline lists **only the orphan**, so the count is not merely doubled — it is attached to a file that cannot be regenerated at all. Any "N fields remaining" figure quoted off this baseline is inflated by both effects.

## The part that is not just bookkeeping: the paper cites two orphans by path

- **`pentagon-to-borromean-h4-probe.witness.json`** — cited by path in two Lean files, `QOU/BraidKnot/QRogersPentagonArchimedean.lean:154,158` (as a `-- Ref: [manuscript]`) and `QOU/BraidsAndKnots/PachnerPentagonBorromean.lean:18`.
- **`hecke-core-symbolic-migration.witness.json`** — cited by path in the **mass-binding-algorithms appendix**, `mba-step02-gs-reduction.ts:13` (`witness:` field) and `mba-step02-gs-reduction.md:74` (link), and in `predicted-spectra/e-hartree-categorical-derivation.ts:54`.

Both cited orphans are the **dirty** copy while the live sibling is at **0**. A reader following the appendix's own `witness:` field lands on a float64 record when a clean one exists one directory over. That is a paper-visible defect, not a housekeeping item.

## Options (my recommendation is 2, marked as judgement)

1. **Do nothing.** The backlog keeps overstating by 1,550 fields, the paper keeps citing stale copies. Zero risk, zero cost. This is the default if nobody acts.
2. **Repoint the citations, then delete the orphans.** Update the three `.ts`/`.md`/`.lean` citation sites to the live path, `git rm` the 21 orphans, drop them from the baseline. Cost: ~5 files touched plus 21 deletions; risk: a consumer I did not find reads one by path (I searched `.py`/`.ts`/`.md`/`.lean`/`.json` — the remaining path-hits are all *audit witnesses*, which regenerate). Reversible via git. Commits to the live path being canonical.
3. **Keep both, mark the orphans in the baseline as undrainable.** Cheapest honest fix to the *count* only; leaves the paper citing stale records and leaves two copies of every stem to go on diverging.

I would take 2 — the orphans are superseded copies of a file that exists, and the citation half is a real defect regardless of what is decided about the count. But deleting committed witnesses that the paper cites is the owner's call, not mine, so nothing has been deleted.

Found while screening drain targets: `pentagon-rt-torus-knot-higgs-probe` (346) looked like the largest solver-free target left and is in fact undrainable.


---

## Re-measured 2026-09-13 against `main` (456 commits later): UNCHANGED, and it corrects `qou-r47m`'s total

Same method, same script, `main` advanced by 456 commits: **21 witnesses, 1,550 fields**, identical. Nothing in the interval touched them, which is what you would expect of files no producer writes.

**One figure of mine to correct.** The body above says *"633 of those 1,550 fields are ALREADY FIXED at the live path"*. That counted rows whose live sibling was at **0 or 1**. Counting strictly `live == 0` — which is what "already fixed" should mean — it is **615 fields in 4 witnesses**: `pentagon-rt-torus-knot-higgs-probe` 346, `pentagon-to-borromean-h4-probe` 216, `hecke-core-symbolic-migration` 31, `per-knot-density-borromean-q-locality-probe` 22. The fifth row, `qbeta-phib-2loop-bdictionary` (orphan 18, live 1), is nearly-but-not-fully drained upstream. Quote **615**; the difference is one row, not a change in the finding.

## Bearing on `qou-r47m` (completed 2026-09-06)

That bean measures the backlog at **33,702 fields** and buckets it by producer shape — B "imports mpmath, does not bind `fmt`" 14,867 / 44.1 %, A "no mpmath at all" 8,600 / 25.5 %, unresolved-producer 8,181 / 24.3 %, C 2,054 / 6.1 %. Its conclusion — no central fix exists — is unaffected by anything here.

But **1,550 of that 33,702 is attached to files no producer writes**, so it is not drainable by any per-producer work the bucket map describes, and **615 of it is already done** at a sibling path the baseline does not track. That is **4.6 % of the backlog that cannot go down**, and it will sit in the denominator of every future "N fields remaining" figure until the orphans are resolved one way or the other.

Note also where these land in the bucket map: an orphan's *producer* is a real producer that imports mpmath, so these fields are counted in bucket B — the bucket the bean calls "the more tractable half … routing it through `fmt` is mechanical". For these, routing the producer through `fmt` is not merely mechanical, it is **inert**: it regenerates the sibling and never touches the counted file. That is a concrete instance of the bean's own caveat that B is "a CANDIDATE class, not a guaranteed-cheap one", reached from a different direction.

Disposition is still the owner's call; the three options and their costs are unchanged above. Nothing has been deleted.

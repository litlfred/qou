---
# qou-baye
title: 21 dirty witnesses sit at a path NO producer writes — 1550 baseline fields undrainable, and the paper cites two of them
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T17:37:47Z
updated_at: 2026-10-04T15:16:00Z
parent: qou-5vkl
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


---

**Drain 7 — `q_pochhammer_seed` (239 -> 0), and it is the one that changed an
answer rather than digits.** 2026-09-13, PR #7268.

Not a record-boundary cast: float64 all the way down through numpy and Python
`complex`, with the verdict read back off it. The defect that mattered was not
the casting at all — **`discriminant_derivative` was a central finite
difference with `h = 1e-7`**, so Newton divided by a derivative good to ~8
digits and every iterate inherited it:

    residual_trace[1]   73.80983470605896       ->  73.8098363816047...   2.27e-08
    residual_trace[8]    1.5295667703648856e-06 ->   1.5295935116521e-06  1.75e-05
    final_residual       2.997783086261874e-13  ->   2.1204641552487e-13  29.3 %

119 fields moved. Delta is an explicit polynomial whose coefficients are EXACT
INTEGERS (`[-16,-24,-35,-50,-35,-24,-16]`), so the derivative is analytic and
the polynomial carries no error at all.

**It overturned the k=3 reading.** Recorded `converged_at: null` is a
`max_iter = 16` artefact: under exact arithmetic k=3 reaches 1e-40 at iteration
**23** (`|Delta_*| = 4.84e-42`) against 11/13/12 for its siblings. A float64 run
could not have decided that at ANY step count — at ~1e-8 iterate error the
iteration stalls near 1e-13 and never reaches 1e-40. **This is the sharpest
instance yet of the AGENTS.md rule that a float64 input does not merely blur a
result, it makes a question unanswerable.**

**New TRAP for this bean: a finite difference is a float64 defect that no cast
audit can see.** There is no `float(...)` at the derivative, no `mpf(<float>)`,
nothing for the raw-float64 ratchet or the mixed-arithmetic gate to key on — the
producer looks clean at exactly the sites those detectors inspect, and is wrong
by 1e-8 where it counts. **Grep `computations/` for finite-difference
derivatives** (`(f(x+h) - f(x-h))`, `h = 1e-`, `/(2*h)`) as a class, separately
from the cast audits. Not yet done.

Second trap, mine: I added a `converged_at_tight` field inside a loop that
`break`s at the loose tolerance, so it could never fire. A
structurally-always-null field is the conjecture-carrier vacuity defect one
layer down. Moved to a separate pass.


### The finite-difference class: MEASURED, and it is a ONE-MEMBER class

Written an hour after the paragraph above told a future agent to grep for this
'as a class, not yet done'. It is now done, and the honest result is a negative —
recorded so nobody spends a pass on it.

**Surface searched:** `grep -rn --include=*.py` over `computations/` and
`tools/` (excluding `_deprecated`) for `(f(x+h) - f(x-h))`, `/(2*h)`,
`h = 1e-`. **~25 hits. On inspection, ZERO are the `q_pochhammer_seed`
defect**, and they fail to be it in four distinct ways:

1. **`h` is the HECKE PARAMETER, not a step.** `(4 - h*h)/(2*h)` in
   `qbeta_kc19_kappatilde_barodd_source_test` and
   `qbeta_bar_odd_qq_coefficient_leg_probe`'s `(X - bar(X))/(2*h)` are algebra.
   ~8 hits. The grep pattern cannot distinguish a difference quotient from a
   formula containing `2h`, and in THIS corpus `h = q - 1/q` is everywhere.
2. **mpmath at 50-70 dps with h <= 1e-12** — legitimate: at 70 dps, `h = 1e-20`
   leaves ~30 correct digits. Most of the remainder.
3. **The site documents its own ceiling.**
   `qbeta_5two_route8_envelope_deformation_cyclotomic_probe`: *"central
   differences at h=1e-12, so ~1e-20 agreement is the ceiling"*.
   `qbeta_c3_phib_mq_logderivative_constraint`: *"step h = 1e-20 at 70 dps"*.
   `hyperbolic_surface_law_probe` records that its FIRST version divided 50-dps
   rounding by 2h and was fixed. `alpha_em_4pi_q0_sensitivity` sweeps h and
   picks the most stable.
4. **The derivative feeds an ERROR BAR or a printed order of magnitude**, where
   8 digits is ample. `mass-from-q-symbolic` sets `_h = Q_ERR * 100` and uses
   `|dP/dq| * Q_ERR` as a propagated uncertainty — the textbook-correct use.
   `he4_gate_vs_magic_a_identity_probe` (h = 1e-5) prints the slope to two
   decimals to argue a crossing is vacuous; its conclusion is qualitative.

**What made `q_pochhammer_seed` different was not the finite difference.** It
was the finite difference **in float64** feeding a **Newton denominator** whose
**iteration trace is the recorded result**. Three conditions, and the class is
defined by their conjunction, not by any one of them. A detector keyed on the
difference quotient alone would have reported 25 and been wrong 25 times.

**So the trap in the paragraph above is over-scoped and this is its correction.**
The reusable part survives: *a finite difference is invisible to every cast
audit* — no `float(...)`, no `mpf(<float>)`, nothing at the sites those
detectors inspect. That remains true. What is not true is that the corpus is
full of them.

**Not claimed:** that no such site exists outside the grepped pattern. A
difference quotient written with two named variables (`(fp - fm) / dd`), or via
`mp.diff` with a bad step, or over a step held in a config dict, would not
match. `mp.diff` in particular chooses its own step and was not audited here —
`hyperbolic_surface_law_probe` uses it deliberately and says so. The claim is:
**the pattern a reader would grep for returns one real defect, already fixed.**


### RE-DERIVED INDEPENDENTLY, and this bean's 615 is confirmed (2026-09-13)

Walked into this from the other direction — `pentagon-to-borromean-h4-probe` came
up as drain target 8 off the baseline's size ranking, and turned out to be **this
bean's subject, not a drain**. Measured, with the method calibrated against the
audit's own definition first:

    computations/pentagon-to-borromean-h4-probe.witness.json         216 floats, 2026-07-18
    computations/probes/pentagon-to-borromean-h4-probe.witness.json    0 floats, 2026-09-06

The producer lives at `computations/probes/`, so **it writes the clean one**. Its
14 `float(` sites are display-only — the live witness has zero raw floats. So the
producer needs no drain at all; the 216 are July debris at a path nothing writes,
and **no amount of re-running can drain them.**

**Full orphan set, 4 entries / 615 fields — exactly this bean's figure, reached
by a different route:**

| baseline fields | stale path | clean twin the producer writes |
|---:|---|---|
| 346 | `computations/pentagon-rt-torus-knot-higgs-probe` | `computations/probes/...` (2026-09-07) |
| 216 | `computations/pentagon-to-borromean-h4-probe` | `computations/probes/...` (2026-09-06) |
| 31 | `computations/hecke-core-symbolic-migration` | `computations/substrate/...` (2026-08-30) |
| 22 | `computations/per-knot-density-borromean-q-locality-probe` | `computations/probes/...` |

**CALIBRATE THE COUNT OR YOU WILL REPORT THE WRONG NUMBER — I nearly did.** A
naive `isinstance(o, float)` walk gives 168 for
`pentagon-multipair-borromean-h4-probe` against a baseline entry of 93, which
reads as a stale baseline. It is not: the audit **excludes integral-valued
floats** (its own output says so — *"NOT a precision finding — exact in
binary64"*). Excluding them, my count matches the baseline **exactly** on every
still-dirty entry checked: 93/93, 117/117, 216/216. And `q-pochhammer-seed`
reads baseline 239, on-disk **0** — confirming today's drain from a second
direction.

So: the baseline is **not** stale relative to disk. The discrepancy was my
measure, and the calibration is the reusable part.

**What this means for the drain queue.** 615 of the 30,985 baseline fields cannot
be drained by any producer run. They can only be drained by deleting the orphan —
which is exactly the owner decision this bean is waiting on, and is why a drain
session keeps rediscovering them by size ranking. Until it is made, **skip these
four when picking a target**; the size ranking will keep offering them.

In-progress in Round 101 PR litlfred/qou#8450.

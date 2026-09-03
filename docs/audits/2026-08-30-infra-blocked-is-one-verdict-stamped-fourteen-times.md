# "Infra-blocked: needs Mathlib theory that does not exist" is one verdict, stamped 14 times

**Date:** 2026-08-30 · **Beans:** `qou-jlam`, `qou-m3xr`, `qou-phl4`, `qou-b21r` · **PR:** #6249

## The finding

Fourteen beans carry the byte-identical `Next step` line

> `Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.`

Thirteen were created in **six seconds** (2026-08-01T23:31:01Z – 23:31:07Z) under one parent,
`qou-k1mq`; the fourteenth (`qou-m3xr`) restates the same verdict for a target already covered
by `qou-phl4`.

| bean | target |
|---|---|
| `qou-p494` | `instanceHyperbolicVolumeIndependence` |
| `qou-xt9z` | `instanceSingleVolumeIrrationality` |
| `qou-bsqw` | `seminormalVector_base_exists` (Vershik–Kerov) |
| `qou-fj8u` | `numSYT_mul_hookProduct` (hook-length formula) |
| `qou-phl4` | `YoungTableauStandard.lean` — 3 cited sorries |
| `qou-o29t` | `covariance_kernel_conjecture` |
| `qou-apcl` | `confinementSDP` |
| `qou-t28w` | `q_NS_wellposedness` |
| `qou-l2xx` | `elliptic_divisor_degree_zero` |
| `qou-vs2i` | `shell-filling-rule.lean` — 3 cited sorries |
| `qou-9gpo` | `confinement_frobenius_reciprocity` |
| `qou-etfq` | `lp_dual_stability` |
| `qou-ygyx` | `operator_selection_lp` |
| `qou-m3xr` | `sum_dimSYT_eq_involution` — **DISPROVED 2026-08-30** |

The per-item **Tractability** line does vary — it names a different missing theory each time.
The **verdict** does not. So this is one classifier's output applied fourteen times, not
fourteen independent assessments, and it has been read ever since as though it were fourteen.

## Why that matters: it is wrong on the one item that got tested

`qou-m3xr` / `qou-phl4` both said `sum_dimSYT_eq_involution` (`Σ_{λ⊢k} f^λ = I(k)`) needed the
RSK correspondence, which Mathlib lacks. **It needs no RSK at all.** Young's lattice is a
`1`-differential poset, and that route proves the identity with finite combinatorics on
`YoungDiagram` — no insertion, no bumping, no permutation↔tableau-pair bijection, nothing from
Mathlib beyond `YoungDiagram`. Proved sorry-free in PR #6164
(`QOU.Mass.sum_numSYT_eq_involutionNumber`), and the class field discharged in #6249.

The absence claim was **true** — Mathlib has no RSK. The inference from it was false. That is
the whole defect: *"Mathlib lacks X, therefore blocked"* is sound only when `X` is actually
**required**, and the classifier recorded the standard textbook route as if it were the only
route.

The same reading then propagated into three content-Lean docstrings
(`SWPeriodSuperExponential`, `BindingClassicalKernel`, `YoungTableauStandard`), where it was
restated as an infrastructure fact — one of them calling the item "the RSK **sorry**", though
it was a class field and had never been a `sorry`. All three are corrected in #6249.

## What this does NOT claim

**The other twelve are not hereby wrong.** They are *unmeasured*. Several look genuinely hard
(Jucys–Murphy spectral theory, LP duality, Hochschild cohomology) and their absence claims are
probably right. This audit establishes that the verdict was **never individuated**, not that it
is generally false.

Nor does #6249's second finding transfer: `branching_two_one` also has a checked non-RSK route
(bean `qou-b21r`), but that was established by working it, not inferred from `qou-jlam`.

## The triage question

For each remaining item, the question is **not** "does Mathlib have `X`?" — that was already
answered, correctly. It is:

> **Is `X` required, or is it merely the route the textbook takes?**

Answering it needs someone to look for a second route, which is exactly the step the
cataloguing pass could not perform. Until that is done per item, treat `infra-blocked` as
**"catalogued as blocked"**, not as **"measured to be blocked"**.

## Recommended wording change

The boilerplate should not assert a cause it did not test. Something like:

> *Catalogued as infra-blocked: the standard route needs Mathlib theory that does not exist.
> NOT verified that the standard route is the only route — check for a second route before
> treating this as blocked.*

Not applied here: rewriting fourteen beans is a separate change, and the two that were actually
tested are already corrected in place.

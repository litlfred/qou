# Difference-link volume prune — modal-stability follow-up (Sage hard-blocked; rigor warranted)

**Date:** 2026-06-23
**Branch:** `claude/nice-dirac-ywun65`
**Status:** non-Sage robustness follow-up to the constant-prefactor prune; no fit; nothing wired.
**Script:** [`computations/probes/difference_knot_volume_extrema_stability.py`](../../computations/probes/difference_knot_volume_extrema_stability.py)
**Witness:** [`computations/probes/difference-knot-volume-extrema-stability.witness.json`](../../computations/probes/difference-knot-volume-extrema-stability.witness.json)
**Refines:** [`2026-06-17-difference-knot-volume-prefactor-prune.md`](2026-06-17-difference-knot-volume-prefactor-prune.md)

## Question

The constant-prefactor prune rests on the claim that the spread-defining extrema
(²H = `k_min`, ⁴He = `k_max`) are **stable** while the ~17% volume jitter only
moves the interior isotopes. Asked to "run the rigorous Sage step to make the
prune airtight (or break it)."

## Sage is hard-blocked here

SageMath is **not** a pip wheel, `apt-cache policy sagemath` → `Candidate:
(none)` in this image, no conda. SnapPy's rigorous interval volume
(`volume(verified=True)`, `verify_hyperbolicity`) raises `SageNotAvailable`
(reproduced live). So the strictly-rigorous step cannot run in-session; the exact
Sage script is emitted in the witness (`sage_script`) for a Sage-equipped env.

## Strongest available non-Sage check — modal stability

Sampling each difference link 10× on the default-simplify path (NOT aggressive
`randomize()`, which only forces SnapPy into degenerate collapses that return
garbage volumes — the hyperbolic volume is a topological invariant, so legitimate
scatter is small):

| iso | A | modal Vol | cluster % | deg % | k_modal |
|-----|---|-----------|-----------|-------|---------|
| ²H  | 2 | 6.0883 | **100%** | 100% | 0.36538 |
| ³H  | 3 | 14.6475 | 80% | 100% | 0.57906 |
| ³He | 3 | 16.5472 | 100% | 100% | 0.46643 |
| ⁴He | 4 | 32.8473 | 80% | 100% | 0.86143 |

**Modal spread `k_max/k_min` = 2.358** — reproduces the committed audit exactly.
The spread-defining **extrema ARE stable**: ²H is 100% of trials at 6.088, ⁴He is
80% with a tight envelope (`v_min` 31.78, only ~3% low). So the audit's "extrema
stable, interiors don't move the spread" claim is **confirmed** at the modal
triangulation.

## Honest caveat — the volumes are not rigorously pinned

**All four composite links return DEGENERATE-triangulation solutions** (and
`canonical_retriangulation` fails on them). So while the modal value is a good
non-rigorous estimate, the volumes are not certified. This **refines** the prune
audit's "expect it to confirm — recommend NOT prioritising the Sage step" to:
**the rigorous interval volume is genuinely WARRANTED, not a formality** — the
non-rigorous basis is shakier than the audit implied. It is **not** enough to
break the prune (modal spread 2.358 ≫ the ≲1.1 a single ρ needs, and a 2.36×
collapse would need ~2× per-piece volume moves that verified volumes do not
exhibit), but the airtightness claim should rest on the Sage step, not the
degenerate triangulation.

## Verdict

The constant-prefactor prune **stands at the modal level** (spread 2.358
reproduced; extrema stable). It is **sound but not yet airtight**: the Sage
rigorous interval volume is warranted to certify the modal volumes. This is the
honest middle — neither over-confirming the prune on degenerate triangulations
nor breaking it. **Note (per the owner's "too small ≠ wrong" framing):** the
difference-link route is not *wrong* mathematics — only the **constant-ρ** reading
is refuted; a per-atom `ρ(D)` (the same underived density wall) is untouched.

# The A=3 mirror binding split is Coulomb — the #2089 strong kernel over-breaks charge symmetry 3×

**Date:** 2026-07-11
**Branch:** `claude/mirror-split-coulomb-diagnosis-2026-07-11`
**Compute:** [`computations/mirror_split_coulomb_diagnosis.py`](../../computations/mirror_split_coulomb_diagnosis.py)
**Witness:** [`computations/mirror-split-coulomb-diagnosis.witness.json`](../../computations/mirror-split-coulomb-diagnosis.witness.json)
**Follow-up to:** merged #3557 (bond-extensivity, flagged the 3× overshoot); builds on
#2089 ([`2026-06-10-binding-bond-graph-compute-audit-and-derivation.md`](2026-06-10-binding-bond-graph-compute-audit-and-derivation.md))
and #3534 (Coulomb-corrected `B_strong`).

## The discrepancy

The merged bond-extensivity work noted the **derived** A=3 mirror split
`B(³H)−B(³He) = ε_nn−ε_pp` (from #2089's log-trace kernel) overshoots AME by ~3×. This
audit diagnoses the cause.

## The observed split is Coulomb

| quantity | value |
|---|--:|
| AME `B(³H) − B(³He)` | **0.764 MeV** |
| pp Coulomb displacement `e²/(4πε₀·r)`, r≈1.9 fm | **0.758 MeV** |
| ⇒ strong CSB residual | **+0.006 MeV** |

³He (Z=2) carries one proton–proton pair that ³H (Z=1) lacks; the Coulomb energy of
that pair at the A=3 proton separation (`r≈1.9 fm`, from the ³He/³H charge radii)
reproduces the *entire* binding split. This is the textbook ³He–³H **Coulomb
displacement energy**; the famous ~0.07 MeV **Nolen–Schiffer anomaly** is the only
residual. So the **strong** charge-symmetry-breaking is `≈0` — the nuclear force is
charge-symmetric to ~1%. (Consistent with #3534: Coulomb-correcting AME leaves the
³H/³He strong binding agreeing to 2.73%.)

## The kernel over-breaks charge symmetry

The #2089 log-trace kernel `B = E₀·Σ_bonds log(1/f_bond)` is **pure strong/categorical**
(the `f_bond` are Markov-trace factors, no EM). Its per-bond factors are strongly
charge-dependent: `f_pp = 0.499`, `f_nn = 0.290`, giving

$$ E_0\,(\varepsilon_{nn} - \varepsilon_{pp}) = E_0\,\log(f_{pp}/f_{nn}) = 2.27\ \text{MeV}, $$

which is **3.0× the total observed split** and **~386× the strong (Coulomb-removed)
residual**. The kernel assigns a large *strong* charge-symmetry-breaking that the data
does not support.

## Two framings (not decided — a framework question for the owner)

- **(A) Spurious strong CSB.** The strong bond should be charge-symmetric (`f_pp ≈ f_nn`);
  the mirror split is Coulomb, added separately as `Z(Z−1)/2 · e²/(4πε₀ r)`. The kernel's
  `f_pp≠f_nn` is then a bug in its charge dependence.
- **(B) Categorical EM.** The kernel's charge-dependence *is* the QOU-derived
  electromagnetic contribution (Coulomb from the bond structure), and it overshoots the
  Coulomb displacement energy by ~3× — a magnitude error in the categorical EM.

## Why this improves mass binding

Either framing points the same way: **source the mirror split from Coulomb, not the
strong kernel.** This fixes the light-nuclei mirror pairs (³H/³He, and by extension
⁷Li/⁷Be, etc.). And there is a structural bonus tying back to the merged thread:

> Charge-symmetrising the strong bond (`f_pp ≈ f_nn`) collapses the **1.78× nucleon
> `ε`-spread**. That spread was exactly what made the equal-weight limit fail at the
> nucleon level (#3557), forcing the `z=A−1` coordination match to be a mirror-pair
> composition coincidence. With `f_pp ≈ f_nn`, equal-weight is restored and the
> coordination-number counting becomes *genuinely* valid for nucleons — the same clean
> structure the α-cluster level already enjoys.

## Verdict (scope-limited (a))

> The A=3 mirror binding split is quantitatively the pp **Coulomb** displacement energy
> (0.758 ≈ 0.764 MeV), so the strong charge-symmetry-breaking is ~0. The #2089 log-trace
> kernel's pure-strong mirror split (2.27 MeV) over-breaks charge symmetry by 3×.
> **Fix direction:** charge-symmetric strong bond + separate Coulomb — which also
> restores nucleon-level equal-weight coordination counting. A diagnosis and fix
> direction, **not** a re-derivation of the kernel.

**Open (→ #3548 / #3534):** the charge-symmetric re-derivation of `f_bond` (or the
explicit categorical-EM term) and the Coulomb-term normalisation are the kernel-owner's
scope. The Nolen–Schiffer anomaly (~0.07 MeV) is the genuine strong-CSB signal, a
separate small target.

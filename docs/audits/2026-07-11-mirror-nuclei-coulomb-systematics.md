# The mirror binding split is Coulomb across the isobaric chain — a systematic charge-symmetry constraint

**Date:** 2026-07-11
**Branch:** `claude/mirror-nuclei-coulomb-systematics-2026-07-11`
**Compute:** [`computations/mirror_nuclei_coulomb_systematics.py`](../../computations/mirror_nuclei_coulomb_systematics.py)
**Witness:** [`computations/mirror-nuclei-coulomb-systematics.witness.json`](../../computations/mirror-nuclei-coulomb-systematics.witness.json)
**Generalises:** #3564 ([`2026-07-11-mirror-split-coulomb-diagnosis.md`](2026-07-11-mirror-split-coulomb-diagnosis.md)).

## Result

The A=3 finding (#3564: the ³H/³He mirror split is Coulomb) is not an accident — it
holds across the whole mirror-nuclei chain. A one-parameter Coulomb law

$$ \Delta E_C = \tfrac{3}{5}\,(\alpha\hbar c)\,\frac{Z_2^2 - Z_1^2}{r_0\,A^{1/3}} $$

with a single **physical** charge-radius `r₀ = 1.44 fm` fits all eight T_z mirror pairs
³H/³He … ³⁹K/³⁹Ca to an **RMS residual of 0.33 MeV** (against splits up to 7.3 MeV):

| pair | A | split_AME | ΔE_C | residual |
|---|--:|--:|--:|--:|
| ³H/³He | 3 | 0.764 | 1.247 | −0.484 |
| ⁷Li/⁷Be | 7 | 1.644 | 2.194 | −0.550 |
| ¹¹B/¹¹C | 11 | 2.764 | 2.966 | −0.202 |
| ¹³C/¹³N | 13 | 3.003 | 3.315 | −0.312 |
| ¹⁵N/¹⁵O | 15 | 3.537 | 3.647 | −0.111 |
| ²³Na/²³Mg | 23 | 4.839 | 4.850 | −0.011 |
| ²⁷Al/²⁷Si | 27 | 5.595 | 5.397 | +0.198 |
| ³⁹K/³⁹Ca | 39 | 7.307 | 6.896 | +0.411 |

## Honest reading of the residual

The 0.33 MeV RMS residual has a clear **A-trend** (negative for light, positive for
heavy), so it is **not** the pure Nolen–Schiffer anomaly (~0.07 MeV) — it is dominated
by the crude uniform-sphere model (`R ∝ A^{1/3}` mis-describes the light-nucleus radii).
So the residual **upper-bounds** the strong charge-symmetry-breaking at **≲0.5 MeV**;
the genuine strong CSB is smaller. The point is not a precise CSB measurement but the
*systematics*: the mirror split tracks `(Z₂²−Z₁²)/R` with one physical radius, i.e. it
is Coulomb.

## QOU consequence

Any strong/categorical binding kernel — #2089's log-trace `f_bond`, #3548's connected
`tr_M` — must be **charge-symmetric to within ≲0.5 MeV** across the chart, with the
mirror split sourced from Coulomb separately. The #2089 kernel's pure-strong A=3 mirror
split (2.27 MeV, #3564) violates this by **~7×**, and the Coulomb systematics shows the
violation is **systematic (all A)**, not an A=3 quirk. This is a concrete constraint on
the kernel derivation (→ #3548): the charge-dependence `f_pp ≠ f_nn` must be removed
(or reinterpreted as the categorical EM, framing (B) of #3564) — it cannot be a strong
contribution.

## Verdict (scope-limited (a))

> The mirror binding split is Coulomb across A=3–39 (one physical `r₀=1.44 fm`, RMS
> 0.33 MeV), so the QOU strong kernel must be charge-symmetric to ≲0.5 MeV systematically.
> A constraint on the kernel derivation, **not** a binding fit. `r₀` is the physical
> charge radius, not a free QOU parameter.

**Open (→ #3548 / #3534):** the charge-symmetric re-derivation of the strong kernel and
the explicit separate Coulomb term. The residual's A-trend also flags that a realistic
(non-uniform-sphere) charge distribution is needed to isolate the true ~0.07 MeV
Nolen–Schiffer strong-CSB signal.

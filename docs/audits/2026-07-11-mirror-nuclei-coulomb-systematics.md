# The mirror binding split is Coulomb across the isobaric chain — a systematic charge-symmetry constraint

**Date:** 2026-07-11
**Branch:** `claude/mirror-nuclei-coulomb-systematics-2026-07-11`
**Compute:** [`computations/mirror_nuclei_coulomb_systematics.py`](../../computations/mirror_nuclei_coulomb_systematics.py)
**Witness:** [`computations/mirror-nuclei-coulomb-systematics.witness.json`](../../computations/mirror-nuclei-coulomb-systematics.witness.json)
**Generalises:** #3564 ([`2026-07-11-mirror-split-coulomb-diagnosis.md`](2026-07-11-mirror-split-coulomb-diagnosis.md)).

## Result

The A=3 finding (#3564: the ³H/³He mirror split is Coulomb) is not an accident — it
holds across the whole mirror-nuclei chain. Using the repo's **canonical uniform-sphere
Coulomb** with the correct discrete-proton self-energy and standard radius
(`coulomb_energy.mirror_displacement_mev`, `Z(Z−1)`, `r₀=1.2 fm` — **no free
parameter**):

$$ \Delta E_C = \tfrac{3}{5}\,(\alpha\hbar c)\,\frac{Z_{\rm hi}(Z_{\rm hi}-1) - Z_{\rm lo}(Z_{\rm lo}-1)}{r_0\,A^{1/3}}, $$

the observed split is **proportional to `ΔE_C`** across all eight T_z mirror pairs:

| pair | A | split_AME | ΔE_C (canonical) | split/ΔE_C |
|---|--:|--:|--:|--:|
| ³H/³He | 3 | 0.764 | 0.998 | 0.765 |
| ⁷Li/⁷Be | 7 | 1.644 | 2.258 | 0.728 |
| ¹¹B/¹¹C | 11 | 2.764 | 3.237 | 0.854 |
| ¹³C/¹³N | 13 | 3.003 | 3.674 | 0.817 |
| ¹⁵N/¹⁵O | 15 | 3.537 | 4.087 | 0.865 |
| ²³Na/²³Mg | 23 | 4.839 | 5.570 | 0.869 |
| ²⁷Al/²⁷Si | 27 | 5.595 | 6.240 | 0.897 |
| ³⁹K/³⁹Ca | 39 | 7.307 | 8.068 | 0.906 |

**`split/ΔE_C = 0.838 ± 0.059` (7% scatter)** — the split is proportional to Coulomb.

## Honest reading

The ~0.84 proportionality factor is the **known uniform-sphere over-estimate** of the
Coulomb displacement energy (the model over-counts; `coulomb_energy.py` documents the
~20–40% over-estimate). The residual **7% ratio scatter** (with a mild A-trend, since
`R ∝ A^{1/3}` mis-describes the light-nucleus radii) plus the ~0.07 MeV Nolen–Schiffer
anomaly bound the strong charge-symmetry-breaking. The point is not a precise CSB
measurement but the *systematics*: the mirror split is proportional to `Coulomb` with
one standard radius, i.e. it **is** Coulomb.

## QOU consequence

Any strong/categorical binding kernel — #2089's log-trace `f_bond`, #3548's connected
`tr_M` — must be **charge-symmetric**, with the mirror split sourced from Coulomb
separately. The #2089 kernel's pure-strong A=3 mirror split (2.27 MeV, #3564) is
**3.0× the whole observed A=3 split** (0.764 MeV), and the Coulomb systematics shows
charge symmetry is required **at all A**, not an A=3 quirk. This is a concrete
constraint on the kernel derivation (→ #3548): the charge-dependence `f_pp ≠ f_nn` must
be removed (or reinterpreted as the categorical EM, framing (B) of #3564) — it cannot
be a strong contribution.

## Verdict (scope-limited (a))

> The mirror binding split is Coulomb across A=3–39: `split/ΔE_C = 0.838 ± 0.059` (7%)
> against the canonical uniform-sphere Coulomb (`Z(Z−1)`, `r₀=1.2 fm`, **no free
> parameter**). So the QOU strong kernel must be charge-symmetric systematically.
> A constraint on the kernel derivation, **not** a binding fit.

**Open (→ #3548 / #3534):** the charge-symmetric re-derivation of the strong kernel and
the explicit separate Coulomb term. The residual's A-trend also flags that a realistic
(non-uniform-sphere) charge distribution is needed to isolate the true ~0.07 MeV
Nolen–Schiffer strong-CSB signal.

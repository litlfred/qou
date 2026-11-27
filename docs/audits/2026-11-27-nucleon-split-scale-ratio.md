# One energy scale cannot size both pieces of the nucleon split

**Date:** 2026-11-27 · **Branch:** `claude/nucleon-split-scale-ratio-2026-11-27` · **Bean:** `qou-myts`
**Lean:** [`QOU/Nuclear/NucleonSplitScaleRatio.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitScaleRatio.lean) (generic field, sorry-free, lean-direct exit 0)
**Probe:** [`nucleon_split_scale_ratio_probe.py`](../../computations/probes/nucleon_split_scale_ratio/nucleon_split_scale_ratio_probe.py) (mpmath 50 dps, proton pin)

## 1. Claim

Every route on record for m_n − m_p applies one energy map `E` to both pieces:

- the flavour cell, `E·2 log q`;
- the electromagnetic term, `−E·α·Q` with `Q = 1/3`.

`#9475` used `E = E₀` and got −10.2 keV. `LITERATURE-COMPARISON.md` §45 used `E = M_QCD` and got −2.30 MeV.

`flavour_over_em` shows that the ratio of the two pieces is `−2L/(αQ)`, where `L` is `log q`. That ratio contains no `E`. So the energy map cannot be the lever. In this class of routes, the ratio is a fixed number.

## 2. Numbers

| quantity | value |
|---|---|
| `log q₀` | 0.10434072031951951232 |
| model ratio of flavour to EM (absolute value) | **85.79** (any `E`) |
| under the `E₀` map: flavour / EM | 0.8735 / −0.01018 MeV |

The ratio uses `α_em⁻¹ = 137.0359350940`, which is conditional on the Witten-κ Gram `sorry`. This is the value used in #9475.

## 3. Comparison boundary (data enters only here)

| source (held in `library/`) | QCD / QED ratio | model ÷ literature |
|---|---|---|
| BMW 2015, `arxiv-1406.4088v2`: +2.52 / −1.00 | 2.52 | 34.0 |
| Gasser–Leutwyler–Rusetsky 2020, `arxiv-2008.05806v2`: +1.87 / −0.58 | 3.22 | 26.6 |
| Walker-Loud–Carlson–Miller 2012, `arxiv-1210.7777v1`: +2.53 / −1.30 | 1.95 | 44.1 |

Two consequences follow:

- If `E` is set so that the EM term has its literature size, `E` is 240–530 MeV. The flavour term then becomes 50–110 MeV.
- If `E` is set so that the flavour term matches the QCD part, the EM term becomes about −0.02 to −0.03 MeV.

## 4. Scope

This result is scope (a) for the class "one map times (2L, −αQ)". It does not rule out a route in which the electromagnetic term carries its own scale. An example is a Coulomb energy `α/r`, with a length `r` that is not proportional to `1/E`. The numbers say that such a second scale has to sit 30 to 45 times above the flavour map. This document does not derive it.

Candidate scales already examined and excluded in §44 of the comparison file:
- the pion Compton length (it rests on an empirical r₀);
- the Breit–Wheeler threshold (its weights are fits);
- the γγ atom (it has no energy unit).

`E = M_QCD` (§45) is one map applied to both terms, so it falls inside this class. It also makes the flavour term about 197 MeV. That point was not raised in §45.

Nothing is adopted and nothing is wired.

## Addendum: spin and colour do not change the n − p charge factor

Owner question, 2026-11-27: *"are all repn and charatcters covered? all partiions"*.

- **Partitions.** By Schur–Weyl, H₃ on (ℂᴺ)^⊗3 sees only shapes with ≤ N rows. The nucleon traces use ℂ² (isospin), so only (3) and (2,1) appear. The uud and udd weight spaces both decompose as (3) ⊕ (2,1), with equal spectra for every q (PREREGISTRATION-charge-operator, PA1). No block separates p from n.
- **Colour.** The photon is colour-blind, so the colour singlet (1³ of ℂ³) multiplies every EM matrix element by the same factor. The 8-fold thread (#9651) puts ℂ³⊗ℂ² in the (1,1) channel of a strand *pair*, which convention D's three-row vanishing does not reach.
- **Spin.** [`nucleon_em_spin_colour_factor_probe.py`](../../computations/probes/nucleon_split_scale_ratio/nucleon_em_spin_colour_factor_probe.py), exact rationals, on the S = ½ nucleon states, with the charges 2/3 and −1/3 of `prop:neutral-lepton-fixes-charges`:

| | ⟨Σ qᵢqⱼ⟩ (Coulomb) | ⟨Σ qᵢqⱼ σᵢ·σⱼ⟩ (magnetic) |
|---|---|---|
| p | 0 | 4/3 |
| n | −1/3 | 1 |
| n − p | **−1/3** | **−1/3** |

So the n − p charge structure is −1/3 in both channels. Adding spin or colour supplies no dimensionless factor, and the 27–44× gap is entirely spatial: an energy-to-length map. The q-Bessel thread reports that E_q(2) has a q^ℤ dilation symmetry, so it fixes shapes but not an absolute length. This is a scope (a) finding about representation content. The quark-model spin wavefunction is used for comparison only.

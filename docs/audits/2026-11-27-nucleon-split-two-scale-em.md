# The n − p electromagnetic term with its own length

**Date:** 2026-11-27 · **Branch:** `claude/nucleon-split-two-scale-em-2026-11-27` · **Bean:** `qou-mbfv`
**Lean:** [`QOU/Nuclear/NucleonSplitTwoScale.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitTwoScale.lean) (generic field, no `sorry`, no numerals)
**Probe:** [`nucleon_split_two_scale_probe.py`](../../computations/probes/nucleon_split_two_scale/nucleon_split_two_scale_probe.py) (mpmath 50 dps, proton pin)
**Builds on:** #9654 (one-scale ratio, charge factor −1/3), #9697 (energy-to-length map), #9699 (shape factor f = 0.520011), `2026-11-27-energy-length-radius-routes.md` §9 (Casimir gap).

## 1. Claim

#9654 proved that if the flavour and electromagnetic (EM) terms of `m_n − m_p` share one energy
map, their ratio is a fixed 85.79, against 1.95–3.22 in the literature. Its scope note left open
the class where the EM term is a Coulomb energy with its own length. This document fills that class
with the pieces now on `main`, and with nothing chosen:

```
EM(n − p) = f · α · Q_np · ħc / r,    r = D · ħc / M     ⇒     EM(n − p) = f · α · Q_np · M / D
```

with `f` the q-Hankel shape factor, `Q_np = −1/3`, and `D` the radius factor.

**Lean (generic field, sorry-free):**
- `coulomb_hc_cancels`: `ħ_q c_q` cancels; the EM term needs only `D` and `M`.
- `coulomb_sq_of_casimir`: on the SU_q(2) route `D² = q/(2ε)`, `ε = E₁/M`, the EM term squared is `2 f² α² Q² M E₁ / q`. So the EM scale is the **geometric mean** of the rest energy `M` and the gap `E₁`.
- `ratio_sq_two_scale`: with flavour `2L·E₀` and `E₁ = c·E₀`, the squared ratio is `2 q L² E₀ / (f² α² Q² M c)`. It depends on `E₀/M`, so this class lies **outside** #9654's one-scale class.

## 2. Model numbers (no data)

The radius routes were taken as they stand on `main`. None was re-tuned. The Casimir operator `C` is
the one with the correct classical limit; that criterion is structural and was stated in §9 of the
radius-routes audit before this probe.

| route | D | EM n−p / m_e | flavour / \|EM\| |
|---|---|---|---|
| Casimir `C`, mass-formula unit `E₀` | 6.3930 | −0.36329 | **4.705** |
| Casimir `C`, trace unit `E₀/R` | 53.642 | −0.04330 | 39.48 |
| Casimir `h²C`, mass-formula unit | 30.580 | −0.07595 | 22.51 |
| Casimir `h²C`, trace unit | 256.59 | −0.00905 | 188.9 |
| Bekenstein saturated (route A) | 0.32837 | −7.0730 | 0.2417 |

The identity `EM² = 2 f² α² Q² M E₁ / q` is asserted in the probe for every Casimir row (to 1e-40).
`α⁻¹ = 137.0359350940` is conditional on the Witten-κ Gram `sorry`, as in #9654.

## 3. Comparison boundary (data enter only here)

| | value |
|---|---|
| `m_n − m_p` measured | 1.29333 MeV |
| literature QCD / QED | 1.95–3.22 (BMW 2015, GLR 2020, WCM 2012, held in `library/`) |
| flavour term, `E₀` map | 0.8735 MeV |
| EM, Casimir `C`, mass-formula unit | −0.1856 MeV, `r` = 1.345 fm |
| model total on that row | 0.688 MeV |
| EM with the measured `r_p` = 0.8409 fm (reference, not an input) | −0.2968 MeV |
| `D` the literature QED parts would need, Coulomb only | 2.05 (−0.58), 1.19 (−1.00), 0.91 (−1.30) |

## 4. What this establishes

- **The 27–44× miss of #9654 was a property of the one-scale class.** On the Casimir `C` row the
  flavour/EM ratio is 4.71 against 1.95–3.22: a 1.5–2.4× miss. That residual is the radius being
  1.6× long (§9 of the radius-routes audit), together with the Coulomb-only EM term (the magnetic
  channel, also −1/3, is not included because its `r⁻³` coefficient needs a strand mass not on record).
- **The EM term is no longer the main miss in the split.** On that row the total is 0.688 MeV
  against 1.293 MeV. The shortfall now sits in the flavour term: 0.874 MeV against a literature QCD
  part of 1.87–2.53 MeV.
- **The electron unit still decides the row.** The mass-formula and trace units differ by
  `R = 70.404`, and only the mass-formula unit gives the 4.7 ratio. Taking that row because it is
  closer would be selection. The unit is the open electron weight `w_e`
  (`ElectronUnitSplit`, the electron categorical-weight thread). This document reports both and
  adopts neither.
- **A = 3.** The same formula needs a gap `E₁` for the three-nucleon 0s state. No such gap is
  derived, so the ³He−³H Coulomb row stays on its conditional radius.

**Scope (a).** The two-scale Casimir route, alone and in either unit, does not reproduce the
literature EM part. Nothing here is a structural exclusion.

Nothing is adopted and nothing is wired.

## 5. Open inputs, in order

1. The electron weight `w_e` (fixes the row; owned by the electron categorical-weight thread).
2. The magnetic channel coefficient (needs a derived strand mass).
3. A three-nucleon gap `E₁(A = 3)` for the ³He−³H row (bean `qou-usft`).
4. The flavour term's own shortfall, which is now the larger miss in `m_n − m_p`.

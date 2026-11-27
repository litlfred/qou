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

## 6. Redone in the derived electron unit (#9718, added the same day)

#9718 (`ElectronCategoricalEnergy`) fixes the per-nat unit by additivity and CAL-1:
`c = m_e / ln τ_e`, `|c| = 2.70728 m_e = 0.330488 E₀`. It is negative on `1 < q ≤ 6/5`. The flavour cell
moves with it: `2 ln q · |c|` = 0.5650 m_e = 0.2887 MeV. The probe now carries three units. The
derived unit is the settled one, and the other two are kept for comparison only.

| route, derived unit | D | EM n−p / m_e | flavour / \|EM\| |
|---|---|---|---|
| β-dictionary isospin gap `ln(q²+q⁻²)` (trace-derived) | 22.948 | −0.10121 | 5.58 |
| Casimir `C` read per nat (reading **not** derived) | 11.121 | −0.20885 | **2.71** |
| Casimir `h²C` read per nat | 53.193 | −0.04366 | 12.94 |

**Sign.** Because `c < 0`, the β-dictionary gap now puts isospin 3/2 *above* 1/2. That is the
correct order, and it is an output of #9718, not imposed. Read with the same negative unit, the
Casimir gap would put isospin 3/2 below 1/2. That is a second reason the per-nat reading of a Casimir
eigenvalue needs its own derivation (#9718 §"Not settled").

**Comparison boundary (data enter only here).**

| route, derived unit | r | EM n−p | model total | measured |
|---|---|---|---|---|
| β gap | 4.83 fm | −0.0517 MeV | 0.237 MeV | 1.2933 MeV |
| Casimir `C` | 2.34 fm | −0.1067 MeV | 0.182 MeV | 1.2933 MeV |

**What changes.**
- On the Casimir `C` row the flavour/EM ratio is 2.71. That is inside the literature band
  1.95–3.22. The ratio scales as `√unit`, so the derived unit moved it there; nothing was tuned.
  But that row rests on the undetermined per-nat reading, and the absolute sizes are about 4.5× short
  of the literature (flavour 0.289 against 1.87–2.53 MeV; EM −0.107 against −0.58 to −1.30 MeV). So the
  ratio being in range is not evidence that the route is right.
- On the trace-derived β row the ratio is 5.58, a 1.7–2.9× miss, against 27–44× in the one-scale
  class.
- In both rows, the total split is now dominated by the **overall energy scale**, not by the EM/flavour
  balance. Both pieces scale with `|c|`, and both are short.

**Scope (a).** Neither route, in the derived unit, reproduces `m_n − m_p` or the literature EM part.
Nothing is adopted and nothing is wired.

## 7. The overall scale: what the flavour cell lacks (follow-up, same day)

Probe: [`flavour_flip_exponent_probe.py`](../../computations/probes/nucleon_split_two_scale/flavour_flip_exponent_probe.py).

With the EM term now within about 2× of its required size relative to the flavour term (§6), the
miss in `m_n − m_p` is the size of the flavour cell `|c|·ln(τ_p/τ_n)`. Two facts already on `main`
fix that cell:

- **The exponent.** `τ_p/τ_n = q^k` with `k = 2`. This is forced for one nucleon block in
  convention D (`markov_forces_K`, full-tower audit §1). On the tower the effective exponent stays in
  1.99–2.01. That is a structural result, scope (b), within convention D.
- **The unit.** For an energy read from trace weights, the unit is `|c| = m_e/(−ln τ_e)` (#9718).

So within convention D with trace-read energies, the cell is `2 ln q·|c|` = 0.2887 MeV, and nothing
inside that class can move it.

**Comparison boundary.** In the derived unit, the measured total would need 0.935 nats (`k` = 8.96),
and the literature QCD part would need 1.35–1.82 nats (`k` = 13.0–17.5). These are not integers and
not close to 2, and no `k` is proposed here.

**Where the lever must be.** In the same log chart the model proton mass is `M/|c|` = 678.2 nats.
#9718 states that nucleon-scale masses sit in the *mass-formula* chart (`m_e·Vol·ρ/ℏ_q²`), whose
electron weight is still hand-placed, and not in the log chart. The split is a difference of two
nucleon masses, so it belongs in the chart that gives the nucleon mass. Reading it in the log chart
while `M` comes from the mass-formula chart mixes the two charts. The overall-scale gap therefore
reduces to the open chart question of #9718 §"Not settled" (the mass-formula chart's electron
weight), which the electron-weight thread is working on (#9725). This is a reduction, not a
derivation. It is scope (a) for the log chart.

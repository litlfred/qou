# Route 1 for the nucleon split: the Gibbs map with the Coulomb pair term

**Date:** 2026-11-27 · **Branch:** `claude/nucleon-split-gibbs-coupling-2026-11-27` · **PR:** #9475 · follows #9453
**Owner card:** "Which route should the nucleon split try next?" → *1 Derive c_em and E (Gibbs)*
**Bean:** `qou-myts` (item C1)
**Lean:** [`QOU/Nuclear/NucleonSplitGibbsCoulomb.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitGibbsCoulomb.lean) (lean-verify exit 0)
**Probe:** [`computations/probes/nucleon_split_gibbs_coulomb_probe.py`](../../computations/probes/nucleon_split_gibbs_coulomb_probe.py) → `nucleon-split-gibbs-coulomb.witness.json` (80 dps, both q₀ anchors)

## 1. Short answer

- **E is derived:** route T gives `k_BT_q = E₀` exactly (`SpectatorEnergyMap.kT_eq_e0`, on main
  before this work). Nothing new is needed for the scale.
- **The coupling, placed correctly, is a Coulomb energy λ, and the temperature drops out of it.**
  In a Gibbs weight the pair energy enters as `exp(−λ·Q_pair/E)`, not as the linear `c·Q_pair` of
  #9453. On each nucleon weight space `Q_pair` is a scalar (`0` on the proton, `−1/3` on the
  neutron), so the free energy is exact:

      m_n − m_p = 2E₀·log q − λ/3        (gibbs_coulomb_split_eq)

  Repulsion (`λ > 0`) lowers the split (`gibbs_coulomb_split_lt_cell`).
- **λ is not derived.** The corpus has scale candidates on record, not a derivation. With the
  only one in use, `λ = α_em·E₀` (30.5 keV), the Coulomb term moves the cell by −10.2 keV.
- **Result (scope (a)):** the Gibbs route with the derived `E` and the on-record `λ` gives
  0.86335 MeV. It does not reach either reading. The `λ` that `Q_β` would need is about 9 times
  larger than `α·E₀`, and `m_n − m_p` would need an attractive `λ`.

## 2. Sign correction to #9453

The single-element audit (`2026-11-27-nucleon-split-single-element-theorem.md` §3) said that for
`c ≥ 0` the Gibbs cell can only grow, so it "can only be read as `m_n − m_p`". The theorems there
are unchanged and correct. The interpretation used the wrong sign for physics: the linear
coupling that corresponds to Coulomb **repulsion** is `c < 0` (energy up means Gibbs weight
down). With the physical sign the Coulomb term **lowers** the cell, toward `Q_β` and away from
`m_n − m_p`. That sentence in the earlier audit was repeated in the bean `qou-myts` note, in the
#9453 PR body and in the chat reply on this thread. This audit supersedes all three on that point.
This agrees with `NucleonChargeTerms.adopted_selfenergy_sign` (energy-map audit §26): an
electromagnetic term lowers `m_n − m_p` here.

## 3. Numbers (proton q₀ = 1.10997858275138…; the muon anchor agrees to 8 digits)

| quantity | value |
|---|---|
| `E₀` (order zero, = `k_BT_q`) | 4.18598136329 MeV |
| `α_em⁻¹(q₀)` (`alpha_em_inv_derived`, conditional on the Witten-κ Gram `sorry`) | 137.0359350940 |
| cell `2E₀·log q` | 0.873536621 MeV |
| `λ = α·E₀` | 30.5466 keV |
| `λ = α·E₀^tower` (the `crossing_covariant_qed_probe` scale) | 30.8495 keV |
| split, `λ = α·E₀` | **0.863354 MeV** |
| split, `λ = α·E₀^tower` | 0.863253 MeV |

`alpha_em_inv_derived` is not the newer Form-B value from #9360 (137.0359991). The difference
moves λ by 0.5 ppm, which is below 10⁻⁸ MeV in the split.

## 4. Comparison boundary (the only place data enters)

CODATA 2022: `m_n − m_p = 1.293332 MeV`, `Q_β = 0.782334 MeV`.

| split | vs `m_n − m_p` | vs `Q_β` |
|---|---|---|
| `λ = α·E₀` | −33.25 % | +10.36 % |
| `λ = α·E₀^tower` | −33.25 % | +10.34 % |

**Diagnostic, not adopted** (`gibbs_coulomb_lambda_of_split`):
- the `Q_β` reading needs `λ = 0.273609 MeV = 8.957·α·E₀`;
- the `m_n − m_p` reading needs `λ = −1.2594 MeV`, an attraction.

The factor 8.957 lies near 9, and a 9 is easy to motivate after the fact (`3²`, the denominators
of the quark charges). That is the shape of a selection against the target, and it is recorded
here so that nobody adopts it as evidence.

## 5. What would complete route 1

A derivation of λ: the Coulomb energy per unit charge product between strands of the nucleon
word, in units the Gibbs weight uses. The corpus fixes the coupling `α_em(q₀)` (conditionally) but
not the length or energy scale it multiplies. `α·E₀` is a candidate on record, not a derivation.
Without that scale the route stops at a scope-(a) negative: with the derived E and the one
on-record λ, the Gibbs route gives 0.8634 MeV.

Routes 2 (distinct uud and udd elements; sibling thread) and 3 (a non-scalar lepton factor) are
untouched by this audit.

## 6. Reproduce

```bash
scripts/lean-verify.sh folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitGibbsCoulomb.lean
python3 -u computations/probes/nucleon_split_gibbs_coulomb_probe.py
```

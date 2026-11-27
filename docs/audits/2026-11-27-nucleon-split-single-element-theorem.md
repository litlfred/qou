# The nucleon split from one element: what can discharge C1–C3

**Date:** 2026-11-27 · **Branch:** `claude/nucleon-split-c1-discharge-2026-11-27` · **PR:** #9453
**Beans:** `qou-myts` (compute-accuracy epic, item C1), `qou-99qc`, `qou-wxhi`
**Lean:** [`QOU/Nuclear/NucleonSplitSingleElement.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitSingleElement.lean) (lean-verify exit 0; axioms propext, Classical.choice, Quot.sound)
**Probe:** [`computations/probes/nucleon_split_single_element_probe.py`](../../computations/probes/nucleon_split_single_element_probe.py) → `nucleon-split-single-element.witness.json` (exact sympy over ℚ(q), then 80 dps; 16/16 assertions)

## 1. Short answer

The scored `Q_β = |ε_flavour(V³)|·E₀` rests on three conjectures (`QOU.QBeta.DecayConjectures`):
C1 the decay functional is the `T³` weight trace, C2 both nucleons carry `V³`, C3 the posited
scale. The obvious way to discharge C3 is energy conservation, `Q_β = m_n − m_p − m_e`, with each
nucleon mass read off a trace. This audit proves, for **every element** of the braid algebra:

1. When the same element is used for both nucleons, **only the Cartan weight `K` separates them.**
   The intertwiner `P` relates the proton and neutron weight-space representations on the whole
   free algebra on `σ₁^{±1}, σ₂^{±1}` (every word, every inverse letter, every photon product),
   so `tr ρ_n(X) = tr ρ_p(X)`. Under the owner-ruled two-term trace with coupling `c`:
   `τ_p = q·t`, `τ_n = (q⁻¹ − c/3)·t`, `t = tr ρ_p(X)`.
2. **Linear energy map: the neutron is lighter, for every element** (scope (b); invariant
   `q⁻¹ < q` with `t > 0`). So C3 cannot be discharged by linear energy conservation
   (`not_decayEnergyScale_of_linear`). This turns the owner's working conjecture of 2026-11-21,
   *"Q_beta I don't think is a linear map"*, into a theorem for the one-element case.
3. **Gibbs map `m = −E·log τ + c₀`: the neutron is heavier, for every element,** and
   `m_n − m_p = E·(2 log q − log(1 − c·q/3))`. At `c = 0` this is the route-T cell `2E₀·log q`
   already in the corpus (`2026-11-21-qbeta-energy-map-spectator.md`).

So with one element the split is **word-independent**: no word, photon weight, power of `V` or
inverse letter can move it. That is why every attempt to tune the element has left the split
where it was.

## 2. Evidence

| statement | Lean name | probe check |
|---|---|---|
| `P·A_i = B_i·P` on all four letters | `intertwine_gen` | `intertwine_all_letters` exact |
| intertwining on the free algebra | `intertwine_rho` | — |
| `tr ρ_n(X) = tr ρ_p(X)` | `trace_rhoB_eq_trace_rhoA` | V³, V⁶, symbolic photon pair, `σ₁σ₂⁻¹σ₂⁻¹σ₁⁻¹σ₂`: exact |
| `τ_p = q·t`, `τ_n = (q⁻¹ − c/3)·t` | `tauP_eq`, `tauN_eq`, `tau_diff_eq` | same four elements, `c` symbolic: exact |
| linear map ⇒ `m_n < m_p` | `linear_mass_neutron_lighter` | proton q₀: `−72.805 MeV` with `S = 2m_μ[3]_q!/q³` |
| C3 not dischargeable linearly | `not_decayEnergyScale_of_linear` | — |
| Gibbs split formula and sign | `gibbs_mass_split_eq`, `gibbs_mass_split_pos` | `0.873537 MeV` (E₀ ord0), `0.882197 MeV` (tower) |

Exact by-product: `tr_W(V³) = −P(q)/q⁶` with `P` the polynomial of `FlavourWeightSplit`
(so `ε_flavour(V³) = −h·tr_W(V³)/[2]³`, consistent with `epsFlavour_V3_eq`).

Numbers at the proton `q₀ = 1.10997858275138080759…` (muon anchor agrees to 8 digits; witness):

| quantity | value |
|---|---|
| `t(V³)` | 2.99418581297996 |
| linear map, `c = 0`, mass-channel `S` | −72.8054 MeV (wrong sign) |
| Gibbs, `c = 0`, `E₀` order zero | 0.873537 MeV |
| Gibbs, `c = 0`, `E₀` tower-summed | 0.882197 MeV |

## 3. Comparison boundary (the only place data enters)

CODATA 2022: `m_n − m_p = 1.293332 MeV`, `Q_β = 0.782334 MeV`.

- Gibbs cell `2E₀ log q` (order zero): −32.46 % against `m_n − m_p`, +11.66 % against `Q_β`.
- The two-term term only **adds** `−E·log(1 − c·q/3) ≥ 0` for `c ≥ 0`. So under the Gibbs map
  with a non-negative coupling the cell **cannot** be read as `Q_β` (it already overshoots at
  `c = 0`); it can only be read as `m_n − m_p`. This bears on the open owner decision of
  2026-11-21 ("the derived n–p cell is not yet assigned to an observable").
- **Diagnostic, not adopted:** the coupling the Gibbs map would need to reach `m_n − m_p` is
  `c = 0.2579` (order-zero `E₀`) or `0.2505` (tower `E₀`). It is printed so the gap is visible.
  Its closeness to `1/4` is exactly the kind of number this corpus must not select; `c_em` has
  no derivation on record (`2026-11-21-lepton-two-term-from-lagrangian-stokes.md`: "selected,
  never derived").

## 4. What can discharge C1–C3 (scope)

Energy conservation with one element for both nucleons leaves three ways out, and this audit
excludes none of them:

1. **A non-linear energy map.** The Gibbs map is one; its scale `E` (route T: `k_B T_q = E₀`)
   and the coupling `c` would both need derivations.
2. **Different elements for the two nucleons** (C2 replaced): any pair not related by the
   `σ₁ ↔ σ₂` intertwiner, e.g. words built from the `uud` / `udd` content under the 2026-11-22
   three-colour working assumption. Only then can the word itself contribute to the split.
3. **A lepton or spectator factor that is not a weight-space scalar** (the γγ pair-production
   route of the 2026-11-20 ruling).

The negative in item 2 of §1 is scope (b) for the stated class (one element, linear map, `c ≥ 0`,
positive proton trace). It says nothing about classes 1–3.

## 5. Reproduce

```bash
scripts/lean-verify.sh folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitSingleElement.lean
python3 -u computations/probes/nucleon_split_single_element_probe.py
```

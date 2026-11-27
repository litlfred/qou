# The nucleon split on the full tower: the K-weight exponent is forced, and one-sided

**Date:** 2026-11-27 · **Branch:** `claude/nucleon-split-full-tower-2026-11-27` · follows #9453, #9475
**Owner:** *"make sure you work on all strands on the full tower"*, *"dervie k-weight expoentn"*,
*"dont look at leadgin term only"* (ledger row in `docs/coordination/owner-rulings.md`, 2026-11-27)
**Beans:** `qou-myts`, `qou-99qc`
**Pre-registration:** [`computations/probes/nucleon_split_full_tower/PREREGISTRATION.md`](../../computations/probes/nucleon_split_full_tower/PREREGISTRATION.md) (committed before the probe ran)
**Lean:** [`QOU/Nuclear/NucleonSplitFullTower.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitFullTower.lean) (lean-verify exit 0; axioms propext, Classical.choice, Quot.sound). `gibbs_split_full_tower` (uses `Real.log`) is split off behind the transcendental boundary into [`QOU/Transcendental/Nuclear/NucleonSplitFullTowerGibbs.lean`](../../folio/quantum-observable-universe/lean/QOU/Transcendental/Nuclear/NucleonSplitFullTowerGibbs.lean), same namespace; the rest stays over a generic field
**Probe:** [`computations/probes/nucleon_split_full_tower_probe.py`](../../computations/probes/nucleon_split_full_tower_probe.py) → `nucleon-split-full-tower.witness.json`

## 1. Short answer

1. **The exponent 2 is derived, not chosen.** For the corpus braiding `Ř`, any `2 × 2` matrix `K`
   whose weighted partial trace over the right strand is Markov is diagonal with
   `K_uu = q²·K_dd`, and the Markov parameter is then `z_D = q³/(q²+1)`
   (`markov_forces_K`, `markov_forces_z`; existence `markov_K_exists`). Nothing is assumed about
   `K`: not diagonality, not commutation with `Ř`, not normalisation. The mirror braiding gives
   the same magnitude with `u ↔ d` (`mirror_forces_K`). Powers `K^m`, `m ≠ 1`, are not Markov.
   So within convention D the exponent cannot be anything other than 2 without changing the
   braiding or the Hecke normalisation `(σ − q)(σ + q⁻¹) = 0`. It does not depend on the tower
   level (`strandWeight_flip`).
2. **But the Markov property is one-sided.** The partial trace over the LEFT strand is Markov only
   for the inverse weight, `K_dd = q²·K_uu` (`left_markov_forces_K`), and no `K` is Markov on both
   sides unless `q⁴ = 1` (`no_two_sided_markov`). So the convention-D trace `Tr(K^{⊗n} ·)`
   reduces spectators on the right of a tagged nucleon by the conditional expectation `E_{n→3}`,
   and does not reduce spectators on its left.
3. **Consequence on the tower.** For the leftmost nucleon block, `τ_p/τ_n = q²` exactly, for every
   element tested at `n = 3, 6` (exact over `ℤ[q, q⁻¹]`) and `n = 9` (exact at `q = 11/10, 3/2`;
   80 dps at `q₀`). The split is `2E₀·log q` there, to all orders in `q`: **0.873537 MeV**
   (order-zero `E₀`) and **0.882197 MeV** (tower `E₀`). For a nucleon with entangled spectators on
   its left, `τ_p/τ_n` is element-dependent.
4. **The pre-registered observable (sum over all nucleon blocks, all colourings) is not a
   function of `q` alone.** It equals `q²` for disjoint products (`V³ ⊗ V³`, `V³ V³ V³`) and for
   24 of the 58 six-strand γγ survivors; for the other 34 its effective exponent is
   1.9929 – 2.0088 (split 0.8704 – 0.8774 MeV, order-zero `E₀`). With an interface letter between
   blocks it moves further, and random words give any value, including negative ratios. Scope (a).

## 2. Where the exponent comes from (derivation)

Convention D's Markov trace is `Tr(K^{⊗n}·)/[2]^n` (bean `qou-99qc`, 2026-11-19). Write
`K = [[a, b], [c, d]]` and require `(id ⊗ Tr)((1 ⊗ K)·Ř) = z·(id ⊗ Tr)(1 ⊗ K)`. The four entries
are `q·a`, `b`, `c`, `(q − q⁻¹)·a + q·d` against `z(a + d)`, `0`, `0`, `z(a + d)`. So `b = c = 0`,
`q·a = (q − q⁻¹)·a + q·d`, i.e. `d = a/q²`, and `z = q³/(q²+1)`. On a strand configuration with
`a` up and `b` down strands, `K^{⊗n}` acts by `k_u^a k_d^b`; turning one `d` into `u` multiplies
it by `q²`. The proton weight space `(2,1)` and the neutron `(1,2)` differ by one flip, so
`τ_p/τ_n = q²·tr_{W_p}/tr_{W_n}`, and the second factor is 1 for every 3-strand braid-algebra
element (#9453). The sympy solve in the probe reproduces both the right and left results.

The diagnostic `CODATA/(E₀ log q) = 2.961` (order zero), `2.932` (tower) does not correspond to
any Markov weight: the exponent is fixed at 2 by item 1.

## 3. Results on the tower (exact unless stated)

| level | element | leftmost block | sum over blocks (pre-registered) |
|---|---|---|---|
| 3 | `V³`, 5 random words | `q²` | `q²` |
| 6 | `V³ ⊗ 1₃`, `V³ ⊗ V³` | `q²` | `q²` |
| 6 | 58 γγ survivors | `q²` (all 58) | `q²` on 24; on 34 effective exponent 1.9929 – 2.0088 |
| 6 | `V³ σ₂ V³` | `q²` | exponent 2.543, split 1.1106 / 1.1216 MeV |
| 6 | `V³ σ₂⁻¹ V³` | `q²` | exponent 2.828, split 1.2352 / 1.2474 MeV |
| 6 | `V³ (σ₂ − h(½ − δ/4)) V³` (colour-weighted p–n letter) | `q²` | exponent 2.656, split 1.1599 / 1.1714 MeV |
| 6 | 5 seeded random words | `q²` | 1 is `q²`; others −14.7 … 2.22, two ratios negative |
| 9 | `V³ V³ V³` | `q²` | `q²` |
| 9 | `V³ σ₂ V³ σ₅⁻¹ V³` (`q₀`, 80 dps) | `q²` | exponent 2.917, split 1.2742 / 1.2868 MeV |
| 9 | 2 random words (`q₀`) | `q²` | exponent 3.52, 4.91 |

Splits are (order-zero `E₀` = 4.18598136329 MeV) / (tower `E₀` = 4.22748335563 MeV), proton
`q₀ = 1.10997858275138…`.

**Do not read the interface rows as progress toward CODATA.** They move the block sum because
the left-traced blocks are not reduced by a Markov map, not because of a derived mechanism, and
the value depends on which interface letter is placed: σ, σ⁻¹ and the colour-weighted letter give
three different exponents. The nuclear interface word is not ruled (the γγ rule covers bond
letters and the per-nucleus word is open, #7876). Choosing among these rows by closeness to
1.2933 MeV would be selection against the target.

## 4. Comparison boundary (the only place data enters)

CODATA 2022 `m_n − m_p = 1.29333251 MeV`.

| split | vs CODATA |
|---|---|
| leftmost block, order-zero `E₀` (every level) | −32.46 % |
| leftmost block, tower `E₀` | −31.79 % |

## 5. The colour-weighted convention (R3)

`bring_color_weighted` is a p–n **interface** prescription: the letter `σ − h(½ − δ/4)·1` with
`δ = flavor_split_leading(q) = (q−1)²(1 − q⁻⁴)/3`, which `closed_form_tau_M.py` labels
`(m_n − m_p)/M_N`. Two consequences:

- At `A = 1` there is no p–n interface, so the convention does not act on a single nucleon at
  all (the code says so: no `pn_convention` reaches `compute_tau_M_nucleon_H3`). It cannot change
  the K-weight exponent: shared by both tagged nucleons, it is one more element of the algebra,
  and the leftmost block stays `q²` (table, row 6).
- Using it as a nucleon-dependent weight in a derivation of `m_n − m_p` would feed that quantity
  in as `δ`. That is circular and was not done. `prop:flavor-split-substrate` itself states
  only the identity `(q−1)²(1−q⁻⁴)/3 = ℏ_q²·h·[2]/3`; whether the identification with
  `(m_n − m_p)/M_N` is derived in its companion block was not checked in this work.

## 6. Scope

- **(b), invariant = the Markov equations:** within convention D, a `K`-weight exponent other than
  2 is excluded for the right-reduced trace (any `K`, Lean).
- **(a):** the Gibbs split with a shared element on the full tower, leftmost block, does not
  reach `m_n − m_p` (0.8735 / 0.8822 MeV).
- **Not formalised:** the iteration of the Markov step to general `n` (Jones conditional
  expectation). Checked exactly at `n = 6` (over ℤ[q, q⁻¹]) and `n = 9` (at rational q), not proved.

## 7. Forks for the owner (not taken)

1. **Which nucleon is reduced, or how left spectators are traced.** The block sum is
   element-dependent because convention D is right-Markov only. Options: (a) leftmost-block / the
   conditional expectation `E_{n→3}` (what `gg_ntower_probe.level_chars` already uses) — gives 2
   at every level; (b) the pre-registered sum over blocks — needs the nuclear word; (c) trace left
   spectators with `K⁻¹` (left-Markov), which makes the global trace no longer `Tr(K^{⊗n}·)`.
2. **The nuclear interface word** (#7876). The block sum depends on it; it must be ruled
   (γγ construction + SDP) before any row of §3 beyond the survivors means anything.
3. **Distinct elements for p and n** (route 2, sibling thread) and the scale `E` / self-energy
   (sibling threads) remain the only ways for the leftmost-block split to move.

## 8. Reproduce

```bash
scripts/lean-verify.sh folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitFullTower.lean \
  folio/quantum-observable-universe/lean/QOU/Transcendental/Nuclear/NucleonSplitFullTowerGibbs.lean
python3 -u computations/probes/nucleon_split_full_tower_probe.py
```

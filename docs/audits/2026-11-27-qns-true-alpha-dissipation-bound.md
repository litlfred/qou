# q-NS item 5: the exponent α of Part A, and what the energy equality forces

Date: 2026-11-27. Bean `qou-d2tt` (item 5 of `qou-innq`). Lean:
`folio/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_alpha_dissipation_bound.lean`
(sorry-free; `#print axioms` on all theorems = `[propext, Classical.choice, Quot.sound]`;
no empirical value in any proof). Owner rulings used: Part A data sit in the
**substrate** layer (2026-11-27), so `q → 1⁺` is the vanishing-viscosity limit
`ν_q = (1 − q⁻¹)/2 → 0`; only QOU-formalized work is used (2026-11-27).

## Result

`p2-critical-exponent` gives two heuristic values: `α = 1` (dissipation closure) and
`α = 4/3` (Kolmogorov closure). Neither is derived. The first is now replaced by a theorem.
The theorem needs only the energy **equality** `E(T) + 2ν ∫₀ᵀ Ω = E(0)`, which holds exactly
for the semi-discrete system (`DEC.energy_equality`). The nonlinear term conserves energy,
so the equality holds **with** modal (triad) transfer. It does not use `modal_inequality`,
the Stokes-type clause that makes Part A false in `q_ns_enstrophy_order_parameter`.

| Lean | Statement |
|---|---|
| `sup_ge_energy_loss` | `sup_{[0,T]} Ω ≥ (E(0) − E(T)) / (2νT)` |
| `sup_ge_energy_loss_nuQ` | at `ν = ν_q`: an energy loss `≥ δ` forces `sup Ω ≥ δ / ((q − 1)T)` |
| `alpha_ge_one_of_anomaly` | a loss `≥ δ > 0` on a fixed window, uniform in `q ∈ (1, q₀]`, gives `(q − 1)·Ω_max(q) ≥ δ/T`, i.e. `α ≥ 1` |
| `balance_witness` | the hypotheses are consistent, and the bound is attained (constant enstrophy) |

So the question "is `α ≥ 1`?" is equivalent, along any family with the energy equality, to
the question "does the energy loss over a fixed window stay bounded below as `ν_q → 0`?".
The second question is a dissipation anomaly. The dissipation closure assumed the anomaly;
the theorem shows that the anomaly is the whole content of `α = 1`.

## Scope (AGENTS.md (a)/(b))

- `α ≥ 1` is **conditional** on the anomaly hypothesis `hloss`. That hypothesis is open, and
  this file does not prove it.
- For the linear Stokes family with `q`-independent data, the loss is
  `Σ_k a_k² (1 − e^{−2ν_q[k]_q² T})`. It tends to `0` (each term tends to `0`, dominated by
  `a_k²`), so the anomaly fails there. That is consistent with Part A being false in
  `stokesContext`. The anomaly needs nonlinear transfer to arbitrarily high `[k]_q`.
- **No upper bound on `α`** follows. The Kolmogorov value `4/3` is neither confirmed nor
  excluded. Getting it would need a spectral law for the nonlinear flow, which the corpus does
  not have (`q_turbulence_spectrum` carries 8 sorries).

## What stays open (bean `qou-d2tt`, not closed)

1. The dissipation anomaly for substrate-layer data under the nonlinear q-NS flow.
2. Any upper bound on `α`.
3. Property 3 of `thm:q-ns-wellposedness` (the per-mode decay) is still in the corpus. The
   Part A audit (`2026-11-27-qns-part-a-enstrophy-order-parameter.md`) shows that property 3
   keeps `Ω` bounded by `Ω(q₀)` in the substrate layer. By the energy equality, the loss is then
   at most `2ν_q T Ω(q₀) → 0`. So, while property 3 stands, the
   anomaly hypothesis is unsatisfiable inside `QNsWellposednessContext`, and `α ≥ 1` is
   vacuous there. That question is the Part A thread's, not this one's.

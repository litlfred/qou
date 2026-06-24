# Plan - Teamwork Proof Migration Project - Batch 2

Coordinate the proof migration for the second batch of 10 unresolved `sorry` stubs in `content/quantum-observable-universe/lean/QOU/`.

## Selected Stubs for Batch 2

| # | File | Declaration | Rationale |
|---|---|---|---|
| 1 | `HadronicMass/deuteron_binding_energy.lean` | `deuteron_binding_energy` | Prove using context properties `h_ΔE_exp` and `h_ΔE_bind_precision`. |
| 2 | `HadronicMass/nucleon_borromean_topology.lean` | `nucleon_borromean_topology` | Prove using context properties `h_vol_hopf`, `h_mass_volume`, and `h_mass_total`. |
| 3 | `HadronicMass/pair_skein_mass_formula.lean` | `pair_skein_mass_formula` | Prove by rewriting with context properties `h_S_ab`, `h_num`, and `h_den`. |
| 4 | `Experimental/local_substrate_q.lean` | `local_substrate_q` | Prove directly using context property `claim_local_substrate_q`. |
| 5 | `Experimental/terminal_resolution.lean` | `terminal_resolution` | Prove directly using context property `claim_terminal_resolution`. |
| 6 | `Interactions/nucleon_ordering_factorization.lean` | `nucleon_ordering_factorization` | Prove by constructor application of context properties `h_master`, `h_cost_std`, `h_cost_naive`, `h_symmetric_evaluations`, and `h_alternating_evaluations`. |
| 7 | `Interactions/UniversalILP.lean` | `UniversalILP` | Prove using context properties `h_n_levels` and `h_gram_dim`. |
| 8 | `Interactions/inductiveGBReduction.lean` | `inductiveGBReduction` | Prove using context properties `h_NF_size`, `h_multiplications`, and `h_reduction_steps`. |
| 9 | `Interactions/confinementUniversality.lean` | `confinementUniversality` | Prove by rewriting with context properties `h_N_F` and `h_N_F_zero`. |
| 10 | `Archimedean/knot_operator_selection.lean` | `knot_operator_selection` | Prove using context properties `claim_i_spectral_decomposition`, `claim_ii_multichannel_pair_production`, `claim_iii_frobenius_demand_supply`, and `claim_iv_minimum_action_selection`. |

## Steps

1. **Initialization**: Create `plan.md` and `progress.md`.
2. **Decompose & Dispatch**: Spawn worker subagents to replace the `sorry` stubs in the 10 target files with valid Lean proofs.
3. **Verification**: Verify that the files compile and compile successfully without errors or warnings.
4. **Git Branch & Commits**: Create the branch `claude/prove-stubs-batch2-2026-06-23`, add the changes, and commit them.
5. **Handoff & Reporting**: Deliver the final handoff to the parent Sentinel.

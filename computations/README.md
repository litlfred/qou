# computations/

This directory contains **524 Python compute scripts** (per
[`canonical-script-input-audit.witness.json`](./canonical-script-input-audit.witness.json)).
Most are exploratory/superseded. This README lists the **canonical**
scripts a new contributor needs to know about.

> **Authoritative scheme**: 3-input canonical per
> [`content/.../calibration-inputs.md`](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md):
> `m_μ/m_e` → `q_0`, `m_e`, `Q_β(n)`. The 6-term mass formula is
> documented in
> [`content/.../six-term-mass-formula-complete.md`](../../content/quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md).

## Infrastructure (do not modify lightly)

| Script | Purpose |
|---|---|
| [`q_parameter.py`](./q_parameter.py) | Substrate parameter `q_0` derived from `m_μ/m_e`; exports `Q`, `Q_INV`, `HA`, `q_int(n)`, etc. **Single source of truth for q_0.** |
| [`experimental_constants.py`](./experimental_constants.py) | CODATA constants with explicit uncertainties: `M_E_MEV`, `M_P_MEV`, `M_N_MEV`, `Q_NEUTRON_MEV`. **NOTE**: under the canonical scheme `m_n = m_p + Q_β`; importing both `M_P_MEV` AND `M_N_MEV` over-counts the hadronic input (see `canonical-script-input-audit.witness.json`). |
| [`witness_base.py`](./witness_base.py) | `WitnessBuilder` for emitting `*.witness.json`. Auto-captures git SHA, script hash, duration. **All new compute should use this.** |
| [`hecke_core.py`](./hecke_core.py) | Hecke-algebra utilities: `partitions_of(n)`, `partition_dimension`, `q_int`, `q_factorial`, `nucleon_gen_chains`, `atom_per_generator_volumes`, etc. |

## Canonical predictor

| Script | Purpose |
|---|---|
| [`categorical_q_decay_ba_low_isotopes.py`](./categorical_q_decay_ba_low_isotopes.py) | **Top-level canonical predictor** for B/A and Q-values for low isotopes (¹H, D, T, ³He, ⁴He, ⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹²C, ¹⁶O). Uses 3-input scheme + 4-tier formula. Sources: `mass-formula-6term.witness.json` (D: T1+T4) + `bw-chirality-isotopes.witness.json` (T/³He/⁴He/A≥5: T5). Emits `categorical-q-decay-ba-low-isotopes.witness.json`. |

## 6-term mass formula evaluators

Per `six-term-mass-formula-complete.md`, the unified mass formula
has 6 terms, all DERIVED:

| Script | Terms covered | Output |
|---|---|---|
| [`light_isotope_sweep.py`](./light_isotope_sweep.py) | Term 1 (Schur–Weyl Markov trace) at q_0 | `light-isotope-sweep.witness.json` |
| [`mass_formula_6term.py`](./mass_formula_6term.py) | Terms 1 + 4 (Frobenius co-Casimir); compares to Term 5 for D, T, ³He | `mass-formula-6term.witness.json` |
| [`bw_chirality_isotopes.py`](./bw_chirality_isotopes.py) | Term 5 (BW + chirality + shell) for D, T, ³He, ⁴He, ⁶Li–¹⁶O | `bw-chirality-isotopes.witness.json` |
| [`mass_endomorphism.py`](./mass_endomorphism.py) | Terms 1 + 2 + 3 (Φ_q tower) for proton, neutron, electron — gives m_p/m_e ≈ 1870 (1.84% off) | `mass-endomorphism.witness.json` |
| [`gb_residue_tower.py`](./gb_residue_tower.py) | Term 6 (jet-prefix; GB residue spectral sum) — partially DERIVED, currently has import bug | `gb-residue-tower.witness.json` |
| [`habiro_residue_symbolic.py`](./habiro_residue_symbolic.py) | Term 6 symbolic via Habiro cyclotomic | `habiro-residue-symbolic.witness.json` |
| [`frobenius_partition_sum.py`](./frobenius_partition_sum.py) | Term 4 (universal Frobenius co-Casimir, Lean-proved) | `frobenius-partition-sum.witness.json` |

## Theorem-driven utilities

| Script | Theorem | Use |
|---|---|---|
| [`chi_sym_alt_closed_form.py`](./chi_sym_alt_closed_form.py) | `χ_sym(β) · χ_alt(β) = (-1)^#(β) · (1 + H_A²/4)^(2A+1)` per `docs/chi-sym-alt-theorem.md` | Verifier; exports `closed_form_prediction(A, H_A)` to skip 2 Hoefsmit calls per atom |
| [`y_lambda_symbolic_validate.py`](./y_lambda_symbolic_validate.py) | Wenzl-bridge `y_λ` cyclotomic factorization | Validates `y-lambda-wenzl-witness.json` at 50 dps MPFR |
| [`atom_mass_partition.py`](./atom_mass_partition.py) | Partition-by-partition Markov trace `tr_M = Σ_λ y_λ · χ_λ` | Polynomial-time exact alternative to NF expansion |

## Audit / probe (informational)

| Script | Purpose | Output |
|---|---|---|
| [`canonical_script_input_audit.py`](./canonical_script_input_audit.py) | Classify all 524 scripts by hadronic-input scheme | `canonical-script-input-audit.witness.json` |
| [`probe_atom_shell_self_duality.py`](./probe_atom_shell_self_duality.py) | Test `x_λ = x_{λ*}` on atom braids (categorical magic probe) | `probe-atom-shell-self-duality.witness.json` |
| [`probe_proton_mass_scale.py`](./probe_proton_mass_scale.py) | Investigate algebraic source of `m_p/m_e ≈ 1836` | `probe-proton-mass-scale.witness.json` |

## Joint-tower SDP (R1–R5)

Per [`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md):

| Script | Phase | Output |
|---|---|---|
| [`joint_tower_sdp_solver.py`](./joint_tower_sdp_solver.py) | Phase 3a: H_3 verifier for {quark, electron, proton, neutron} | `joint-tower-sdp-h3.witness.json` |
| [`joint_tower_sdp_solver_v2.py`](./joint_tower_sdp_solver_v2.py) | Phase 3b: H_3 SDP feasibility for ²H, ³He | `joint-tower-sdp-h6-h9.witness.json` |
| (Rust) [`tools/hecke-engine/src/bin/joint_tower_sdp.rs`](../../tools/hecke-engine/src/bin/joint_tower_sdp.rs) | Production R1+R2+R3+R4+R5min in Rust | `joint-tower-sdp-rust.witness.json` |

H_5+ blocked on Clarabel-rs algorithmic bug (PR #444 `R5_5_BUG_REPORT.md`).

## Bypass / "no fits" demonstrations

| Script | Purpose |
|---|---|
| [`categorical_bypass_volmatch_demo.py`](./categorical_bypass_volmatch_demo.py) | Compute B = m_e · ρ · Σ y_λ · χ_λ at q_0 directly from joint-tower SDP, no Vol_hyp; surfaces the gap with Kashaev formula |

## Naming conventions

- `*.py` — script (executable, has `if __name__ == "__main__":`) or library module
- `*.witness.json` — emitted output, structured per `WitnessBuilder` schema
- `_deprecated_*` (proposed) — quarantined scripts; do not import
- `probe_*`, `*_probe.py` — exploratory; outputs labeled with their hypothesis

## Adding new compute

1. Use `WitnessBuilder` from `witness_base.py`.
2. Import constants from `q_parameter.py` and `experimental_constants.py`. **Do not hard-code CODATA values.** **Do not use both `M_P_MEV` and `M_N_MEV` directly** — derive `m_n = m_p + Q_β` per the 3-input scheme.
3. Cite the content block(s) you're computing for via `WitnessBuilder.set_content_block(...)`.
4. Avoid `Vol_hyp` / `VOL_*` constants in the chain — those are post-Archimedean and fitted under option B (per [`docs/audits/categorical-vs-fitted-q-decay-ba.md`](../../docs/audits/categorical-vs-fitted-q-decay-ba.md)).
5. Run `python3 canonical_script_input_audit.py` after to verify your script lands in the canonical bucket.

## See also

- [`docs/audits/categorical-vs-fitted-q-decay-ba.md`](../../docs/audits/categorical-vs-fitted-q-decay-ba.md) — by-witness audit
- [`content/quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md`](../../content/quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md) — 6-term formula master index
- [`content/quantum-observable-universe/braids-and-knots/calibration-inputs.md`](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md) — 3-input scheme
- [`content/quantum-observable-universe/braids-and-knots/np-discrepancy-resolution.md`](../../content/quantum-observable-universe/braids-and-knots/np-discrepancy-resolution.md) — 4-tier formula
- [`docs/chi-sym-alt-theorem.md`](../../docs/chi-sym-alt-theorem.md) — exact closed form for χ_sym · χ_alt

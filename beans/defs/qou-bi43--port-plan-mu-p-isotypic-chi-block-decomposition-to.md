---
# qou-bi43
title: 'PORT PLAN: mu_p-isotypic chi block-decomposition to hecke-engine (derived-chi catalogue phase 2)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T18:30:53Z
updated_at: 2026-10-04T15:22:08Z
parent: qou-5vkl
---

## Context

Follow-up to the Rust-GP port on branch
`claude/rust-port-chi-catalogue-2026-08-02` (commits aec7f04b, 5aafbc85).
That port moved the **total-character** `direct` reference in
`computations/derived_chi_catalogue_matrix_m.py` Tests 5/6/7 to the Rust
Geck–Pfeiffer engine via the new `chi_lambda_via_rust_gp` wrapper
(existing `pyhecke_native.chi_q_via_gp`). End-to-end wall 28.96s -> 12.62s
(2.3x).

**Remaining symbolic cost = the mu_p-isotypic block decomposition**
`chi_lambda_mu_p_contributions` (cProfile: ~24.9s cumulative on the
pre-port sweep). This has **no Rust equivalent**: `chi_q_via_gp` returns
the *total* character, not the per-mu_p contributions
`Tr[B_p[mu_p] · M_pp[mu_p] · B_n[mu_p]]`. It stays pure-sympy (Hoefsmit
seminormal matrices, sub-block `.extract`, per-block `sp.cancel`).

## Exact function to port

`chi_lambda_mu_p_contributions(shape, word_left, bridge_sign, word_right,
k_split, q)` in `computations/derived_chi_catalogue_matrix_m.py`
(lines ~437-501). It:
1. builds the seminormal generators `seminormal_matrices_qrat(shape, q)`,
2. forms `B_p = word_to_matrix(word_left)`, `M = get_sigma(k_split,...)`,
   `B_n = word_to_matrix(word_right)` (all dim×dim, sp.cancel per multiply),
3. groups SYTs by `mu_p = syt_first_k_shape(T, k_split)`
   (`group_syts_by_mu_p`),
4. for each mu_p: `Tr[ B_p.extract(idxs,idxs) · M.extract · B_n.extract ]`.

## hecke-engine entry point to ADD

`tools/hecke-engine/src/seminormal.rs` (or a new `chi_mu_p.rs`):

```
pub fn chi_mu_p_contributions_gp(
    shape: &[usize],
    word_left:  &[(i32, usize)],   // (sign, gen_1based)
    bridge_sign: i32,
    word_right: &[(i32, usize)],
    k_split: usize,
) -> Vec<(Vec<usize>, Vec<(i32, String)>)>   // (mu_p, Laurent coeffs)
```

- Reuse the existing seminormal-block machinery already backing
  `chi_q_via_gp` / `chi_via_gp_hoefsmit` (Hoefsmit natural form, exact
  `BigRational` entries; the total character is already exact-integer, so
  each mu_p block-trace is an exact Laurent poly too).
- Enumerate SYTs and their `first_k_shape` in Rust (there is already SYT
  enumeration behind `chi_q_via_gp`); build the sub-block trace with
  `num_rational::BigRational`, collect the integer Laurent poly per mu_p.
- **One FFI call per (shape, split-word)** — whole-compute granularity
  (compute-author §2.1). Do NOT cross the boundary per mu_p or per entry.

## pyhecke-native FFI signature (§2.3)

`tools/pyhecke-native/src/lib.rs`, mirroring `chi_q_via_gp`:

```
#[pyfunction]
fn chi_mu_p_contributions_gp(
    shape: Vec<usize>,
    word_left: Vec<(i32, usize)>,
    bridge_sign: i32,
    word_right: Vec<(i32, usize)>,
    k_split: usize,
) -> PyResult<Vec<(Vec<usize>, Vec<(i32, String)>)>>
```

Returns `[(mu_p_partition, [(half_exp_key, coeff_str), ...]), ...]`.
Python reassembles each mu_p Laurent list to a sympy Expr exactly as
`chi_rust_at_qval` does (half-exponent key convention: math q-exp =
d_int/2). Minor version bump on pyhecke-native (new public API).
Build: `maturin build --release` + `pip install` the wheel (§4.3;
`cargo`/`maturin` ship in the sandbox — do NOT `lake build`).

## Cross-check harness (mandatory, 40+ digits)

Extend `computations/derived_chi_catalogue_rust_gp_crosscheck.py`:
for each (shape, split-word), assert the Rust per-mu_p contributions
equal the pure-Python `chi_lambda_mu_p_contributions` dict —
`sp.cancel(py[mu_p] - rust[mu_p]) == 0` per mu_p — AND the summed
character matches `chi_q_via_gp`. Both exact-integer => exact agreement
(digits=inf); the 40-digit q0 floor is the compute-author bar. This is a
§3 algebraic preflight on the block-trace identity before shipping.

## Why >1 session

Requires new Rust: SYT-restriction/first_k_shape enumeration + per-mu_p
BigRational sub-block trace inside hecke-engine, a new pyhecke-native
binding, a wheel rebuild, and the extended cross-check. The total-character
port (this branch) was fast only because `chi_q_via_gp` already existed;
the mu_p variant does not, so it is genuinely new kernel work.

## Cheaper alternative (record, do not silently adopt)

The decomposition IDENTITY (direct == factored) could instead be validated
at enough EXACT-RATIONAL q sample points (q0 + a few integer probes >
Laurent degree) rather than symbolically — Test 8 already shows numerical-q
mu_p is ~17-27x faster and consistent. A Laurent-poly identity holding at >
(deg+1) distinct exact-rational points IS a proof. This needs NO Rust but
is a numerical-sampling change, not a Rust port; note it as an option, keep
the Rust kernel as the canonical route.

In-progress in Round 101 PR litlfred/qou#8450.

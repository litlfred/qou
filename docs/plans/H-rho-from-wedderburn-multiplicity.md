# Plan H — ρ(Z, N) derivation from Wedderburn multiplicity

**Status:** design pass. No code changes yet.
**Target:** the prefactor `ρ ∈ ℤ_{>0}` in
`B_pred = ρ · (mass-carrier) · (knot invariant)` for the four
census entries in
[`computations/low-isotope-mass-table.witness.json`](../../computations/low-isotope-mass-table.witness.json).
The master proposition's "Where the gaps actually are" section
specifies that ρ should come from "the multiplicity of T_w's SDP
solution in the Wedderburn decomposition".

Today
[`computations/sweeps/low_isotope_binding_sweep.py`](../../computations/sweeps/low_isotope_binding_sweep.py)
hand-picks ρ ∈ {`m_e`, `2 m_e`} per row:

| Entry | ρ today (hand-pick) | Comment |
|-------|---------------------|---------|
| ²H | `m_e` | "single-chirality" |
| ³H | `2 m_e` | "CPT-saturated" |
| ³He | `2 m_e` | "CPT-saturated" |
| ⁴He | (not census; α-cluster) | n/a |

The hand-pick gets ²H/⁴He to ppm accuracy but ³He has +81 ppm
residual.  The hypothesis is that a derived ρ from the Wedderburn
multiplicity will explain or eliminate the residual.

## Mathematical content of the multiplicity

For a Hecke element T_w ∈ H_n(q) and the Wedderburn isomorphism
H_n(q) ≅ ⊕_λ End(V_λ), each `λ ⊢ n` contributes a block of
dimension `d_λ²` with multiplicity `m_λ = d_λ` (the dimension of the
Specht module).  When solving the joint-tower SDP

    find α* ∈ [0, 1] : α · ρ_λ(T_w) + (1 − α) · I_{d_λ} ⪰ 0  ∀ λ

the **active set** is the set of partitions λ for which the PSD
constraint binds at α = α*.  The "Wedderburn multiplicity of the
SDP solution" is the integer

    ρ_W(T_w) := Σ_{λ ∈ active set} d_λ

(or similar; the exact definition needs to be pinned, see below).
For ²H (knot 6_2 in B_3) this should give `ρ_W = 1` (single block
binds), matching the empirical `m_e`.  For ³H/³He (CPT-paired)
two blocks should bind, giving `ρ_W = 2`, matching `2 m_e`.

## Existing infrastructure

| Asset | Path | Status |
|-------|------|--------|
| R5-minimal PSD-cone verifier | [`tools/hecke-engine/src/sdp_verifier.rs`](../../tools/hecke-engine/src/sdp_verifier.rs) | Computes α* and `min_eigenvalue_at_alpha_star` per atom; **does not currently report which blocks bind**. |
| Per-block PSD evaluator | [`tools/hecke-engine/src/wedderburn_psd.rs`](../../tools/hecke-engine/src/wedderburn_psd.rs) | Returns `WedderburnBlockReport { partition, d_lambda, eigvals, min_eig, max_eig, psd_symmetric_part }` per λ. |
| R5-full Clarabel SDP solver | `tools/hecke-engine/src/sdp_solver_clarabel.rs` | Full SDP with dual variables; would directly expose multiplicity, but currently disabled (system BLAS dependency). |
| Per-atom certificates | `tools/hecke-engine/certificate-{2h,3h,3he,4he,...}.json` | Already emit `wedderburn_blocks` and `psd_cone_alpha_star` when populated. |
| Joint-tower certificate type | `tools/hecke-engine/src/joint_tower_sdp_certificate.rs` | Has `rho_factor: u32` field — **already in schema, currently set by hand**. |

## What's missing

The R5-minimal verifier does not report the *active set*.  A
new function in `sdp_verifier.rs` is required:

```rust
pub struct WedderburnMultiplicityReport {
    pub n: usize,
    pub q0: f64,
    pub alpha_star: f64,
    pub binding_partitions: Vec<Vec<usize>>,  // active set
    pub binding_dims: Vec<usize>,             // d_λ for each
    pub rho_w: u32,                           // sum or count, see below
    pub binding_tolerance: f64,               // |min_eig − 0| ≤ tol means binding
}
```

The "ρ_W" definition is the load-bearing question.  Three
candidates:

1. **Count of binding partitions** — `ρ_W = #{λ : block λ binds}`.
   Test: ²H → 1, ³H → 2, ³He → 2.  Cleanest physically; matches
   the CPT-saturation narrative.
2. **Sum of dimensions over active set** — `ρ_W = Σ_{active} d_λ`.
   Test: ²H → ?, depends on which block is active.
3. **Multiplicity of zero eigenvalue across all active blocks** —
   `ρ_W = #{(λ, i) : ε_i(α* ρ_λ + (1−α*)I) = 0}`.

The plan: implement (1) first, validate against the four targets;
fall back to (2) or (3) only if (1) fails.

## Output contract — the new certificate field

In `joint_tower_sdp_certificate.rs` add to
`JointTowerSdpCertificate`:

```rust
#[serde(skip_serializing_if = "Option::is_none")]
pub wedderburn_multiplicity: Option<WedderburnMultiplicityReport>,
```

The existing `rho_factor: u32` field becomes a *derived* output:

- If `wedderburn_multiplicity` is present, `rho_factor` must equal
  `wedderburn_multiplicity.rho_w` (CI gate; mismatch is a build
  failure).
- If absent (legacy certificates), `rho_factor` retains its
  hand-picked value but is flagged in the methodology field.

## Test plan

| Atom | Expected ρ_W (hypothesis) | Empirical hand-pick | AME residual today |
|------|----------------------------|---------------------|---------------------|
| ¹H (proton) | 1 | n/a (no binding) | 0 |
| ²H (D / 6_2) | 1 | `m_e` (= 1·m_e) | −12 ppm |
| ³H (T / 8_11) | 2 | `2 m_e` | +5 ppm |
| ³He (Borromean) | 2 | `2 m_e` | +81 ppm |
| ⁴He (α-cluster) | n/a | n/a | 0 (anchor) |
| neutron (n_0) | 1 | n/a (used as anchor) | 0 |

The smoke test: run the new `WedderburnMultiplicityReport` for
each of `certificate-{2h,3h,3he,1h}.json`; confirm the
hypothesised ρ_W value falls out of the active-set count.  If
yes: the hand-pick is *empirically validated by category theory*
and Plan H closes.  If no: the multiplicity is something else,
and the residual on ³He may be telling us we have the wrong
braid word — handing back to Plan G.

## Effort estimate

| Phase | Person-days |
|-------|-------------|
| Define `WedderburnMultiplicityReport`; pick ρ_W formula | 0.5 |
| Implement `solve_alpha_psd_with_multiplicity` in `sdp_verifier.rs` | 1 |
| Schema gate: `rho_factor` matches `rho_w` | 0.5 |
| Re-run R5-minimal across {1h, 2h, 3h, 3he, 4h, 4he, neutron}; emit new certificates | 1 |
| Wire into `low_isotope_binding_sweep.py`: read `rho_factor` from certificate JSON instead of hard-coding `m_e`/`2 m_e` | 1 |
| Cross-check predictions against AME residuals; if mismatch, debug ρ_W definition | 1.5 |
| Documentation: update `prop:alpha-k-derivation-procedure` proof to cite the certificate field | 0.5 |
| **Total** | **6 days** |

## Smoke test / exit criterion

1. New certificates `certificate-{1h,2h,3h,3he,4he}.json` carry
   `wedderburn_multiplicity` with non-empty `binding_partitions`
   and an integer `rho_w`.
2. The values agree with the hypothesised table:
   ²H → 1, ³H → 2, ³He → 2, ⁴He → (whatever; α-cluster doesn't
   use this path), 1H → 1.
3. `low_isotope_binding_sweep.py` reads `rho_factor` from the
   certificate; the resulting `B_pred_MeV` values differ from
   today's hand-picked values by exactly **zero** when the
   hypothesis holds (since `rho_factor` is the same integer).
4. The `methodology` field of each certificate flips from
   `manual-historical-volume-match` to `principled-derivation`
   for the rows where multiplicity matches.
5. CI gate: `rho_factor == wedderburn_multiplicity.rho_w` for
   every certificate that has the new field.

## First concrete step

In `tools/hecke-engine/src/sdp_verifier.rs`, extend the existing
`solve_alpha_psd` so that after bisection converges, it iterates
through `evaluate_all_blocks(n, braid_word, q)` once more at the
final `α*` and records, for each block:

- `partition: Vec<usize>`
- `d_lambda: usize`
- `min_eig_at_alpha_star: f64`
- `is_binding: bool`  (true iff `|min_eig| ≤ binding_tolerance`)

Then `rho_w = binding.count()` is the count formula.  This is a
~30-line addition to `solve_alpha_psd` returning a richer report
struct; no algorithmic change.  Run on `certificate-2h.json` first
to confirm `rho_w = 1` falls out.

## Out of scope

- Plan F (precision) — multiplicity is a *combinatorial* output
  (an integer count), so f64 vs MPFR doesn't change it. The
  binding tolerance does need calibration: at f64 precision use
  `1e-9`; at MPFR precision use `mpf("1e-40")`.
- Plan G (Vol shortcut) — even after this plan derives ρ, the
  geometric carrier `Vol_hyp(K)` is still a SnapPy lookup until
  Plan G replaces it with `tr_M(T_w)`.

## Risk register

- **R1.** ρ_W definition (1) may fail to match empirics on ³He
  (the +81 ppm row).  Fallbacks (2) and (3) above; if all three
  fail, we escalate: the issue is not ρ — it's the braid word.
- **R2.** "Binding tolerance" is fragile.  At α*≈ 1−ε, the
  min-eigenvalue could be exactly on the boundary or numerically
  −1e-12.  Mitigation: report all eigenvalues per block, let the
  Python wrapper apply the threshold, and surface a sensitivity
  table in the certificate.
- **R3.** The R5-minimal verifier currently uses bisection with
  fixed iteration count.  Multiplicity counting is sensitive to
  the final α*; we may need ≥ 50 iterations to pin α* well
  enough for unambiguous binding-set extraction.
- **R4.** When R5-full (Clarabel SDP) eventually comes online,
  it returns dual variables that *directly* give multiplicity.
  This plan should write the contract such that swapping in the
  Clarabel path is a no-op for downstream consumers — i.e. the
  `WedderburnMultiplicityReport` schema must be solver-agnostic.

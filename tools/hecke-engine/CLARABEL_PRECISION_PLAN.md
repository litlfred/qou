# Clarabel high-precision integration — QOU workplan

Companion to [`RUST_INTEGRATION.md`](RUST_INTEGRATION.md) and
[`R5_FULL_PLAN.md`](R5_FULL_PLAN.md).  Tracks QOU's adoption of a
higher-precision Clarabel.rs build (work-in-progress upstream by the
repo owner) so the joint-tower SDP can be solved at the MPFR precision
that the Hoefsmit seminormal kernel already supports.

## Why precision is the bottleneck

The risk flagged in [`R5_FULL_PLAN.md` §Risks
(3)](R5_FULL_PLAN.md):

> $q_0 \approx 1.1097$ is not special — small perturbations can flip
> PSD signatures.  Use MPFR with $\geq 50$ digits and re-validate.

QOU already runs the **character path** at 167 bits ($\approx 50$ dps)
via [`seminormal_mpfr.rs`](src/seminormal_mpfr.rs).  But the
**SDP path** drops back to `f64` at every step from `q` through the
solver call.  At $H_{18}$ (⁶Li) onward the Wedderburn-block PSD
signatures are sign-sensitive in the last few `f64` bits — see the
H_5 anomaly diagnosed in
[`bin/r5_5_diagnose_h5.rs`](src/bin/r5_5_diagnose_h5.rs) and the
post-mortem in [`R5_5_BUG_REPORT.md`](R5_5_BUG_REPORT.md).  Closing
the f64→MPFR gap on the solver side is the missing rung for R5.6/R5.7.

---

## Section 1 — Audit of the f64 boundary

Every site below currently forces `f64` and must become generic over
a `FloatT` parameter (or be paralleled by an MPFR sibling).  Grouped
by file; each entry is `path:line — symbol — issue`.

### `src/sdp_verifier.rs` (bisection — no Clarabel call)

| Site | Type | Notes |
|---|---|---|
| `SdpVerifierReport.q0`, `alpha_star`, `min_eigenvalue_at_alpha_star` | `f64` | Public API surface |
| `min_eig_at_alpha(n, braid, q: f64, alpha: f64) -> f64` | `f64` | Calls `wedderburn_psd::evaluate_all_blocks(_, _, q: f64)` |
| `solve_alpha_psd(_, _, q: f64)` bisection | `f64` | Tolerance `1e-12` is f64-tuned |

This module is not strictly Clarabel-bound, but its eigenvalue source
(`wedderburn_psd`) is the same `seminormal_matrices(_, q: f64)` that
the Clarabel modules use — so any MPFR refactor must thread through
here too for the cross-validation tests in §3 to be meaningful.

### `src/sdp_solver_clarabel.rs` (R5.3 — α-PSD via Clarabel)

| Site | Type | Issue |
|---|---|---|
| `ClarabelSdpReport { q0, alpha_star }` | `f64` | API |
| `invert_matrix_h`, `sparse_to_dense`, `dense_dense_mul`, `symmetrize` | `Vec<Vec<f64>>` | All matrix ops f64 |
| `build_rho_lambda(_, _, q: f64)` | `f64` | Pulls from `seminormal_matrices(_, q: f64)` |
| `svec_pack` uses `2f64.sqrt()` | `f64` | √2 scaling at f64 precision |
| `q_vec: Vec<f64>`, `a_vals: Vec<f64>`, `b: Vec<f64>` | `f64` | Clarabel input vectors |
| `cones: Vec<SupportedConeT<f64>>` | `f64` | Clarabel cone descriptors |
| `DefaultSolver::new(...)` | `DefaultSolver<f64>` | Solver is monomorphised on f64 |
| `solver.solution.{x, obj_val}` | `Vec<f64>`, `f64` | Output |

### `src/sdp_solve_canonical_t_w.rs` (R5.5 — canonical $T_w$ solver)

| Site | Type | Issue |
|---|---|---|
| `LinearAnchor::TraceOfBlock { target: f64 }`, `SingleCoefficient { target: f64 }` | `f64` | API |
| `SolverReport.{q0, c_solved, l1_norm}` | `f64`, `BTreeMap<_, f64>`, `f64` | API |
| `build_rho_lambda_for_basis_element(_, _, q: f64)` | `f64` | Same chain as above |
| `svec_pack_symmetric` uses `2f64.sqrt()` | `f64` | √2 |
| `coef.abs() > 1e-18` (sparsity threshold for A) | `f64` | Tuned to f64 ε |
| `cw.abs() > 1e-9` (output prune threshold) | `f64` | Tuned to f64 ε |
| Clarabel CSC, cones, solver | `f64` | Same |

### `src/sdp_recover_canonical.rs` (R5.4 — recovery test)

| Site | Type | Issue |
|---|---|---|
| `RecoveryReport.{q0, c_recovered, c_target, max_residual}` | `f64` family | API |
| `eval_laurent_at(p: &LaurentQ, q: f64) -> f64` | `BigRational → f64` | **Information-losing**: collapses exact rational coefficients to f64 before they reach the SDP |
| `build_rho_lambda_for_basis_element(_, _, q: f64)` | `f64` | Same |
| svec packing with `2f64.sqrt()` | `f64` | Same |
| `coef.abs() > 1e-18` | `f64` | Same |
| Clarabel CSC, cones, solver | `f64` | Same |

### Upstream consumers (unchanged but f64-typed)

| Site | Type | Issue |
|---|---|---|
| `seminormal::seminormal_matrices(shape, q: f64)` | `Vec<Vec<(usize, f64)>>` | The kernel matrix builder used by every SDP module |
| `wedderburn_psd::evaluate_all_blocks(_, _, q: f64)` | f64 eigenvalues | Same |
| `joint_tower_sdp_certificate::WedderburnBlockReport.{matrix_at_q_0_sym_eigvals, min_eigenvalue}` | `Vec<f64>`, `f64` | Witness JSON schema |

### What already exists at MPFR precision

| Module | API | Reusable for |
|---|---|---|
| `seminormal_mpfr::chi_lambda_braid_mpfr(shape, word, q_str, dps) -> String` | character only | trace anchors, sanity checks |
| `seminormal_mpfr::chi_lambdas_braid_mpfr` | parallel batch | tier-2 cross-validation |
| `seminormal_mpfr::dps_to_bits` | dps → bit precision | shared helper |
| `laurent_poly_q::evaluate_mpfr` | LaurentQ → `rug::Float` | replacement for `eval_laurent_at` |

**Gap**: there is no `seminormal_matrices_mpfr` — the per-element
`BlockMpfr` machinery in `seminormal_mpfr.rs` materialises only the
contracted character via `apply_sigma_mpfr`.  The high-precision SDP
path needs the full per-block matrix, not just its trace.

---

## Section 2 — Integration shim

Six concrete deliverables, ordered by dependency.

### S1.  Add `seminormal_matrices_mpfr` (~120 LOC)

New function in `src/seminormal_mpfr.rs`:

```rust
pub fn seminormal_matrices_mpfr(
    shape: &[usize],
    q_str: &str,
    dps: u32,
) -> Vec<Vec<Vec<(usize, rug::Float)>>>;
```

Same shape as `seminormal::seminormal_matrices` but each entry is a
`rug::Float` at the requested precision.  Reuses `build_blocks_mpfr`
(already there); adds a materialisation pass that emits the sparse
generator matrices instead of contracting against a basis vector.

### S2.  Generic dense linear-algebra helpers (~200 LOC)

New `src/dense_la.rs`.  Generic over a `Scalar: Clone + Add + Mul + ...`
trait alias.  Ports the four helpers (`sparse_to_dense`,
`dense_dense_mul`, `invert_matrix_h`, `symmetrize`) once instead of
duplicating per Clarabel module.  Two instantiations:

- `Scalar = f64` — drop-in replacement for the existing `f64`
  helpers in the three SDP modules.
- `Scalar = rug::Float` — used by the MPFR path.

### S3.  Generic `svec_pack` (~30 LOC)

In `src/dense_la.rs` (alongside S2).  Replaces the three duplicate
`svec_pack`/`svec_pack_symmetric` definitions.  √2 is computed via
`Scalar::from(2u32).sqrt()` so MPFR uses the high-precision sqrt.

### S4.  `sdp_solver_clarabel_hp.rs` — the high-precision solver
       (~350 LOC)

New module sitting alongside `sdp_solver_clarabel.rs`.  Mirrors its
structure but generic over the Clarabel `FloatT` parameter that
upstream is adding:

```rust
pub struct ClarabelSdpReportHp<F: clarabel::algebra::FloatT> {
    pub n: usize,
    pub q_str: String,        // exact decimal — no f64 boundary at the API
    pub dps: u32,
    pub alpha_star: F,        // returned at solver precision
    pub solver_status: String,
    pub n_blocks: usize,
    pub block_dims: Vec<usize>,
    pub iterations: u32,
}

pub fn solve_alpha_psd_clarabel_hp<F: clarabel::algebra::FloatT>(
    n: usize,
    braid_word: &[i32],
    q_str: &str,
    dps: u32,
) -> ClarabelSdpReportHp<F>;
```

Key choices:
- **API takes `q_str`, not `f64`** — kills the lossy boundary at
  the entry.  Internally parses to `rug::Float` once then converts to
  `F` for Clarabel.
- **Returns at solver precision** — caller decides whether to project
  to `f64` for witness JSON or keep at `F`.
- **Sparsity threshold** is `F::epsilon() * <const factor>` instead
  of the hard-coded `1e-18`.

### S5.  Same treatment for `sdp_solve_canonical_t_w` and
       `sdp_recover_canonical` (~400 LOC each → ~800 LOC total)

Pattern-identical to S4.  Outputs:
`solve_canonical_t_w_hp(...) -> SolverReportHp<F>` and
`solve_recovery_h_n_hp(...) -> RecoveryReportHp<F>`.

In `sdp_recover_canonical_hp.rs`, replace `eval_laurent_at` with
`laurent_poly_q::evaluate_mpfr` so the LaurentQ → solver coefficient
path stays exact / arbitrary-precision end-to-end.

### S6.  Cargo wiring + feature flag (~20 LOC)

Bump `clarabel` to whatever version exposes the high-precision
generic.  Gate behind a feature flag so the f64 path stays the
default until S1–S5 land:

```toml
[dependencies]
clarabel = { version = "0.12", features = ["sdp-netlib"] }   # bump

[features]
default = []
clarabel-hp = ["dep:rug"]   # rug is already a hard dep; this gates the new modules
```

`lib.rs` adds `#[cfg(feature = "clarabel-hp")] pub mod
sdp_solver_clarabel_hp;` (and the two siblings).  Default builds
remain f64.

### Estimated effort

| Step | LOC | Time |
|---|---|---|
| S1 — `seminormal_matrices_mpfr` | ~120 | 4-6 hr |
| S2 — generic dense LA | ~200 | 4-6 hr |
| S3 — generic svec | ~30 | 1 hr |
| S4 — `sdp_solver_clarabel_hp` | ~350 | 1 day |
| S5 — `sdp_solve_canonical_t_w_hp` + `sdp_recover_canonical_hp` | ~800 | 2 days |
| S6 — Cargo + feature flag | ~20 | 1 hr |
| **Total** | **~1500 Rust** | **~4 working days** |

Blocker: needs the upstream Clarabel high-precision feature to be
mergeable / vendorable.  S1, S2, S3 are independent of Clarabel and
can land first as a non-breaking refactor.

---

## Section 3 — Test plan

Three tiers of regression / cross-validation, each with explicit
success criteria and witness format.

### Tier T1 — H_3 regression: f64 ↔ MPFR agreement

The existing test set in `sdp_solver_clarabel.rs` and
`sdp_recover_canonical.rs` already covers H_3 at f64.  Add an MPFR
twin for each:

| Test | f64 expectation | MPFR expectation | Cross-check |
|---|---|---|---|
| `proton_borromean_clarabel_alpha_one` (H_3, Borromean) | $\alpha^\* > 0.999$ | $\alpha^\* > 1 - 10^{-40}$ | $|\alpha^\*_{f64} - \alpha^\*_{mpfr}| < 10^{-12}$ |
| `deuteron_clarabel_alpha_quantifies_gap` (H_3, 6_2) | $\alpha^\* < 0.9999$ | same, gap to ≥40 dps | both agree on gap to 12+ dps |
| `clarabel_matches_bisection` (Borromean, 6_2, L6a4) | f64 diff $< 10^{-3}$ | MPFR diff $< 10^{-40}$ | MPFR is the canonical answer |
| `proton_borromean_recovery_at_h3` (R5.4) | residual $< 10^{-5}$ | residual $< 10^{-40}$ | every $c_w$ matches to 12+ dps |
| `h3_solver_with_identity_anchor` (R5.5, $c_e = 1$) | $|c_e - 1| < 10^{-4}$ | $|c_e - 1| < 10^{-40}$ | other $c_w \approx 0$ to 40 dps |

**Rationale.**  At H_3, both paths must succeed and agree.  This is
the smoke test that the MPFR plumbing did not break the algorithm.
If they disagree by more than the f64 envelope, MPFR is right and
the f64 path has an undiagnosed numerical issue we should be aware
of even at small n.

### Tier T2 — H_6 / H_9 cross-validation: bounded precision pickup

Same braids, two scales:

- **H_6**: ²H Hopf-link binding (`[1, -2, 1, 3, -2, 3]` family,
  precise word from
  [`confined-particle.md`](../../content/quantum-observable-universe/braids-and-knots/confined-particle.md))
- **H_9**: nucleon = 3 quarks (`H_3^{⊗ 3}` Borromean tensor, word
  per the same registry)

For each, run `solve_canonical_t_w` (R5.5) f64 vs MPFR with
identity anchor.  Report:

| Metric | f64 | MPFR | Pass criterion |
|---|---|---|---|
| `solver_status` | `Solved` | `Solved` | both succeed |
| support size $|\{w : c_w \ne 0\}|$ | $S_{f64}$ | $S_{mpfr}$ | $S_{mpfr} \subseteq S_{f64}$ (MPFR may prune more aggressively) |
| max $|c_{w,f64} - c_{w,mpfr}|$ over agreed support | — | — | $< 10^{-10}$ |
| $\ell_1$ norm | $L_{f64}$ | $L_{mpfr}$ | $|L_{f64} - L_{mpfr}| / L_{mpfr} < 10^{-10}$ |

**Witness output**: `joint-tower-sdp-{atom}-precision-comparison.witness.json`
with both solutions side-by-side and the diff metrics.  Lives under
`folio-assistant/computations/`.

### Tier T3 — H_18 (⁶Li): the precision-required regime

This is the test that *currently fails* and that the high-precision
work is meant to fix.  Per
[`R5_FULL_PLAN.md` §R5.5](R5_FULL_PLAN.md):

> base infra done; H_3..H_8 work.  H_18 needs Wedderburn-block
> decomposition (memory-bounded, not a correctness issue).

Two subtests:

**T3a — feasibility at MPFR.**  Run `solve_canonical_t_w_hp`
on ⁶Li at $H_{18}$ with filtration cutoff $L = 8$, AME-anchor
constraint, dps = 100.  Success iff:
- `solver_status == "Solved"` or `"AlmostSolved"`
- recovered $c$ passes the R3 Wedderburn-block PSD evaluator
  (`wedderburn_psd::evaluate_all_blocks` re-run at MPFR precision)
  with $\min \mathrm{eig}_\lambda \geq -10^{-30}$ for every $\lambda$
- AME mass anchor: $|B_\mathrm{pred} - B_\mathrm{AME}| / B_\mathrm{AME}
  < 10^{-9}$ (1 ppb)

**T3b — f64 negative control.**  Run the *same* problem on the f64
path.  Expected outcome (today): one of `MaxIterations`,
`NumericalError`, or `Solved` with PSD residual that fails the
R3 verifier.  This documents *why* MPFR was needed.  Witness:
`li6-precision-comparison.witness.json` with the failure mode.

**Witness output**: `joint-tower-sdp-li6.witness.json` with the new
principled-derivation methodology tag, replacing the deprecated
`li-atom-knot-search` entry per
[`R5_FULL_PLAN.md` §R5.8](R5_FULL_PLAN.md).

### Test infrastructure

1. **New CLI**: `src/bin/clarabel_precision_smoke.rs` — runs T1+T2 in
   under a minute, prints a comparison table, exits non-zero on any
   pass-criterion failure.  Wired to `[[bin]]` in `Cargo.toml`.

2. **CI gate**: add a step to `.github/workflows/lean_ci.yml` (or a
   new `clarabel-precision.yml`):

   ```yaml
   - name: Clarabel precision smoke (T1 + T2)
     run: cd tools/hecke-engine && cargo run --release --features
          clarabel-hp --bin clarabel-precision-smoke
   ```

   T3 stays out of CI (memory + time budget); runs locally and on
   demand via a separate `cargo run --release --bin
   joint-tower-sdp -- --atom 6Li --precision 100`.

3. **Witness staleness wiring**: extend
   [`witness_staleness_tracker.py`](../../folio-assistant/computations/witness_staleness_tracker.py)
   to invalidate the precision-comparison witnesses whenever any of
   the four SDP modules or the two MPFR helpers change.

---

## Cross-references

- [`prop:joint-tower-sdp-confinement`](../../content/quantum-observable-universe/braids-and-knots/joint-tower-sdp-confinement.md) — design spec
- [`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md) — consumer
- [`R5_FULL_PLAN.md`](R5_FULL_PLAN.md) — phase R5.6/R5.7 unblocked by this
- [`R5_5_BUG_REPORT.md`](R5_5_BUG_REPORT.md) — svec post-mortem (resolved at f64; high-prec validates)
- [`RUST_INTEGRATION.md`](RUST_INTEGRATION.md) — parent integration plan
- [`seminormal_mpfr.rs`](src/seminormal_mpfr.rs) — existing MPFR character path
- [Clarabel.rs](https://clarabel.org/stable/rust/) — solver

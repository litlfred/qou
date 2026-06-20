# `pyhecke_native` builds in this sandbox — the q-deformed compute is unblocked

> **Bean.** [`pyhk`](../../.beans/pyhk--pyhecke-native-build-unblocked.md).
> **Discipline.** Infra unblock + validation. Corrects a standing "this sandbox
> can't build the PyO3/maturin chain" claim. No fitting; the keystone 210 ppb
> evaluation remains owner-gated open (see §4).

## 1. Result — it builds (≈ 42 s)

Prior notes (CLAUDE.md Lean/infra context; `docs/scope/2026-06-04-hoefsmit-stage-b-per-block-tbeta-scope.md`
§"Infra blocker") state the `pyhecke_native` PyO3/maturin build is unavailable in
the web sandbox, which gated every arbitrary-q / cross-anchor / H₅ probe. **That is
no longer true here.** The toolchain is present and the wheel builds:

```bash
# cargo 1.94.1 + rustc 1.94.1 are already on PATH (/root/.cargo/bin)
python3 -m pip install maturin                     # 1.14.1
maturin build --release -m tools/pyhecke-native/Cargo.toml
#   -> tools/pyhecke-native/target/wheels/pyhecke_native-0.9.0-cp311-cp311-...whl
python3 -m pip install --force-reinstall tools/pyhecke-native/target/wheels/pyhecke_native-0.9.0-*.whl
```

- `rug = "1.26"` is a **direct** dep, so the default build pulls MPFR; there are no
  system `gmp.h`/`mpfr.h`, so `gmp-mpfr-sys` **compiles GMP+MPFR from source** via
  `cc` — this works and is fast (whole build ≈ 42 s with `lto = true`, opt-level 3).
- No `clarabel-lp` feature needed for characters / traces / weights / projectors.

## 2. Validation — independent cross-check (1e-15)

[`docs/audits/scripts/pyhecke_native_h3_crosscheck.py`](scripts/pyhecke_native_h3_crosscheck.py):
the Rust Hoefsmit character and the **independent** 2×2 sympy H₃ rep of
[`borromean_per_block_h4_localization.py`](scripts/borromean_per_block_h4_localization.py)
agree at q₀ on every per-block Borromean character, `b=(σ₁⁻¹σ₂)³`:

| block | `pyhecke_native.chi_lambda_braid` | independent target | \|Δ\| |
|-------|-----------------------------------|--------------------|-------|
| `(3)` | 1.000000000000002 | 1 | 2.4e-15 |
| `(1,1,1)` | 1.000000000000000 | 1 | 0 |
| `(2,1)` | 1.994185810381214 | `2−3h⁴−h⁶` = 1.994185810381213 | 6.7e-16 |

Two unrelated code paths agreeing to f64 epsilon validates **both** the wheel and
the keystone's h⁴-localization claim.

## 3. The keystone's H₅ algebra is reachable

`trace_weights_n(5, q₀)` returns the 7 Wedderburn/Markov weights `y_λ`, λ⊢5 — the
exact "block weighting" the functor-resolution doc says ℓ=2 shifts:

| λ⊢5 | `(5)` | `(4,1)` | **`(3,2)`** | **`(3,1,1)`** | `(2,2,1)` | `(2,1,1,1)` | `(1⁵)` |
|---|---|---|---|---|---|---|---|
| `y_λ(q₀)` | 0.11815 | 0.10938 | **0.06172** | **0.01677** | 0.00775 | −0.00093 | 0.0000862 |

The muon block `(3,2)` and electron block `(3,1,1)` weights are now directly
computable, alongside `chi_lambda_braid[_mpfr]`, `chi_lambda_matrix`,
`seminormal_matrices_mpfr`, and **`lagrange_projectors_mpfr`** (the `E_λ` Wedderburn
projectors the resolution-doc §4 needs).

## 4. What this unblocks — and the discipline on the open piece

Now compute-ready (no longer infra-blocked): the Hoefsmit **Stage-B** per-block
cross-anchor probe (arbitrary q), the q-deformed keystone projector shift
(`E_{(3,2)}` vs `E_{(3,1,1)}` at q₀), and ~15 other in-repo `pyhecke_native`
importers.

**The keystone q-deformed shift is now *compute-ready* but not *well-posed* yet.**
It still needs the **open structural inputs** the functor-resolution doc §4 lists:
which H₅ braid realises the muon, and how `E_λ` acts on the local knot module. And
per critical-distance: the 210 ppb target is itself an **anchor-shift artifact**
(the 2026-06-13 operator-branching doc §1: "mathematically identical to the
mechanical propagation of the proton-anchor shift"), so the disciplined next step is
a **bar-even, anchor-stable derivation** of the projector shift — **not** a numerical
hunt for `1.000000210` (which would be fitting a re-pin artifact). The tool is ready;
the structural choice is the gate.

## 5. Cross-references

- build target: `tools/pyhecke-native/` (Cargo.toml: `pyo3 0.25`, `nalgebra 0.33`, `rug 1.26`, `hecke-engine` path dep)
- validation: [`scripts/pyhecke_native_h3_crosscheck.py`](scripts/pyhecke_native_h3_crosscheck.py), [`scripts/borromean_per_block_h4_localization.py`](scripts/borromean_per_block_h4_localization.py)
- the keystone: [`2026-06-13-s5-so3-fiber-action-functor-resolution.md`](2026-06-13-s5-so3-fiber-action-functor-resolution.md) §4, [`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md)
- corrected stale blocker: [`docs/scope/2026-06-04-hoefsmit-stage-b-per-block-tbeta-scope.md`](../scope/2026-06-04-hoefsmit-stage-b-per-block-tbeta-scope.md) §"Infra blocker"

# `pyhecke_native` in-sandbox build + deuteron categorical-A reproduction

**Date:** 2026-06-28
**Branch:** `claude/backlog-drain-7c-orphan-2026-06-28` (PR #2990)
**Context:** owner steer to pursue Option-E PROBE 2 (the A=4 interface operator)
non-fit. The closure-(b) categorical extraction was flagged "Rust-gated" in
[`2026-06-23-interface-operator-derivation-and-4body-assembly.md`](2026-06-23-interface-operator-derivation-and-4body-assembly.md).
This note records that the gate is **removable in the web sandbox**, the working
recipe, and the verification it unblocks.

## The gate was narrower than "Rust-gated" implied

The `pyhecke_native` wheel does **not** need the proxy-blocked
`litlfred/Clarabel.rs` fork for the categorical-A path:

- `clarabel` is `optional = true` in `tools/hecke-engine/Cargo.toml` and is
  **not** enabled by the default feature `mpfr` (`mpfr = ["dep:rug"]`). Only the
  opt-in `clarabel-sdp` / `clarabel-lp` / `clarabel-bigrational` features pull it.
- The categorical-A primitive `seminormal_matrices_mpfr` (and
  `chi_lambda_braid_mpfr`) live in the `rug`/MPFR cone (`seminormal_mpfr.rs`,
  **no** `clarabel` use) and are exported **unconditionally** by
  `tools/pyhecke-native/src/lib.rs`.

The only reason a default `maturin build` fails is that the
`[patch.crates-io] clarabel = { git = … }` makes cargo *resolve* the fork's
feature names (`mpfr`, `sdp-netlib`, `serde`, `bigrational`); crates.io `clarabel`
0.11 lacks the `mpfr` feature, so resolution errors **even though clarabel is
never compiled**.

## Working recipe (web sandbox, ~2.5 min compile)

1. **Empty stub crate** `clarabel` v0.11.1 declaring the four referenced features
   as empty (`mpfr`, `sdp-netlib`, `serde`, `bigrational`) + empty `src/lib.rs`.
   Because clarabel is optional and off under default features, the stub is only
   *resolved*, never compiled into the wheel.
2. Repoint the patch in `tools/pyhecke-native/Cargo.toml` (local, **not**
   committed): `clarabel = { path = "<stub>" }`.
3. `pip install maturin` then `maturin build --release` (the only real native
   dep is `rug`'s bundled `gmp-mpfr-sys`, which compiles GMP+MPFR from source;
   `m4`/`make`/`gcc` are present). `pip install --force-reinstall
   target/wheels/pyhecke_native-*.whl`.
4. Restore `Cargo.toml`/`Cargo.lock` (the stub repoint is a sandbox-only hack).

Result: `import pyhecke_native; pyhecke_native.seminormal_matrices_mpfr(...)`
works. Runtime compute deps: `pip install mpmath numpy sympy`.

## Verification unblocked: deuteron categorical A reproduced (1e-49)

With the freshly-built kernel, `computations/a_operator/a_operator_categorical.py`
reproduces the closure-(b) preflight **end-to-end, ALL PASS**:

| check | result |
|---|---|
| `[1b]` dimension identity `d_λ = Σ c^λ_ξν d_ξ d_ν` | PASS (11 partitions) |
| `[1x]` χ^λ disjoint (I=identity) reduction, exact MPFR | PASS, 891 checks, max abs residual **1.56e-49** |
| `[2]` operator `A^λ_ξν(I_pn) = Π_ξν ρ_λ(I) Π_ξν`, exact | PASS, 891 checks, partition-of-unity=True, max abs residual **1.51e-49** |
| `[2g]` ρ_ξ⊗ρ_ν gauge alignment | `TODO(closure-b)` |
| `[3]` H₉ universality | `TODO(closure-b)` |

**Check `[2]` is the operator-level closure-(b) claim — and it is exactly the
invariant formalized in Lean as `trace_block_diagonal` (PR #2990):** only the
diagonal `(ξ,ν)` isotypic block of `ρ_λ(I)` survives, `A = Π ρ(I) Π`. The Lean
theorem is the abstract trace-algebra statement; this `1.5e-49` H₆ run is its
concrete numerical witness. The two are mutually corroborating: the compute shows
the decomposition holds at the deuteron; the Lean shows *why* (off-diagonal blocks
vanish under any cyclic trace for commuting projectors).

## Honest scope (no closure claimed)

- **Done / reproduced:** kernel build + deuteron categorical A (`[1x]`,`[2]`) at
  the 1e-25 L1 floor — confirms the structural claim, not the binding closure.
- **Still `TODO(closure-b)`:** STEP 2g (gauge alignment — a basis change) and
  STEP 3 (H₉ universality — the genuinely new ~500 LOC rep-theory that would
  reconstruct tr_M(T)/(³He), the case the fitted extract misses by 21–42%). Not
  rush-written here.
- **Launched (~25 min):** `a_operator_recursive_he4_crosscheck.py` — the A=4
  end-to-end recursion-kernel validation (`tr_M(⁴He) = Σ y_λ χ^λ` vs the
  canonical fine-Bratteli reference). Result to be appended.
- **No fit, no new constant.** LR data + seminormal matrices are existing
  categorical objects; this is reproduction + a build-unblock, not a closure.

## References

- [`docs/audits/2026-06-16-categorical-interface-operator-closure-b-design.md`](2026-06-16-categorical-interface-operator-closure-b-design.md)
- [`docs/audits/2026-06-23-interface-operator-derivation-and-4body-assembly.md`](2026-06-23-interface-operator-derivation-and-4body-assembly.md)
- `content/quantum-observable-universe/lean/QOU/BraidKnot/InterfaceOperatorBlockDiagonal.lean` (PR #2990)
- `computations/a_operator/a_operator_categorical.py`

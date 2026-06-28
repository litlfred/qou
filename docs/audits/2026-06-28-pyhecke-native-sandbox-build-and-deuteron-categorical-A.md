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
- **H₉ universality (STEP 3) — VALIDATED at A=3 and A=4.** The
  `TODO(closure-b)` in the *preflight* script (`a_operator_categorical.py`) was
  misleading: the operator-level recursion already lives in
  `a_operator_recursive.interface_blocks` (with the V_ξ⊗V_ν branching basis +
  the step-2g `_align_block_to_standard` gauge alignment). With the kernel built,
  the categorical (non-fit) recursion reconstructs `tr_M` end-to-end:

  | nucleus | (a) combiner vs `chi_young` | (b) vs transfer (rel) | `tr_M` (combiner) |
  |---|---|---|---|
  | ³H (H₉) | 5.91e-48 (exact) | 1.95e-16 | 0.104071087735434324 |
  | ³He (H₉) | 9.96e-48 (exact) | 1.07e-16 | 0.206578511677137038 |
  | ⁴He (H₁₂) | 2.44e-47 (exact, d≤120) | 2.25e-16 | 0.0553584360720161753 |

  The per-λ combiner χ^λ equals the direct seminormal χ^λ to ~1e-48 (exact,
  construction-internal), and the assembled `tr_M` matches the canonical
  fine-Bratteli transfer reference to the float64 atom-word-constant floor
  (~1e-16) — **for the A=3 case the fitted least-squares extract misses by
  21–42%.** Driver: [`a_operator_recursive_a3_crosscheck.py`](../../computations/a_operator/a_operator_recursive_a3_crosscheck.py)
  (+ witness `a-operator-recursive-a3-h9.witness.json`, 4 assertions pass);
  A=4: `a_operator_recursive_he4_crosscheck.py`.
- **Honest scope (mirrors the A=4 crosscheck's own framing):** this is a
  **correctness** validation — the operator-valued combiner *reproduces* the
  canonical `tr_M`, it does **not** change the binding value or close the
  CAL-2-floor residual. Its content is that the CATEGORICAL recursion is exact /
  universal-by-construction at A=3,4 (no test-word fit) — the property proved
  abstractly in Lean as `trace_block_diagonal` (#2990) and verified at the
  operator level here.
- **No fit, no new constant.** LR data + seminormal matrices are existing
  categorical objects; this is reproduction + a build-unblock, not a closure.

## References

- [`docs/audits/2026-06-16-categorical-interface-operator-closure-b-design.md`](2026-06-16-categorical-interface-operator-closure-b-design.md)
- [`docs/audits/2026-06-23-interface-operator-derivation-and-4body-assembly.md`](2026-06-23-interface-operator-derivation-and-4body-assembly.md)
- `content/quantum-observable-universe/lean/QOU/BraidKnot/InterfaceOperatorBlockDiagonal.lean` (PR #2990)
- `computations/a_operator/a_operator_categorical.py`

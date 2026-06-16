# Handover — Wenzl A≥3 categorical combiner: Rust port + remaining work

**Date:** 2026-06-16
**For:** the next agent picking up the closure-b / Wenzl A≥3 combiner thread.
**TL;DR:** The categorical interface-operator combiner `A^λ_{μν}(I)` is fully
derived, gauge-aligned, H₉-universality-verified, and ported to an exact-MPFR
Rust kernel — **all merged**. A Python drop-in wrapper gives the sibling wiring
PR (#2371) **26/30 λ⊢9** coverage. Two **nice-to-have** follow-ups remain (neither
unlocks new physics): a Rust **all-blocks** speedup, and an **algorithmic
intertwiner** to clear the last 4 large-`r` λ. This doc specifies both precisely.

---

## 1. What this is (the math)

The operator-valued Wenzl branching combiner computes the Hecke character of an
atomic braid by peeling one nucleon (an H₃ block) at a time:

```
χ^λ(W_inner · I · β_block) = Σ_{μ⊢n-3, ν⊢3} Tr_{V_μ⊗V_ν}[ A^λ_{μν}(I) · (ρ_μ(W_inner) ⊗ ρ_ν(β_block)) ]
```

The **interface operator** `A^λ_{μν}(I)` is the closed-form **categorical**
object (NOT a least-squares fit, NOT an "analytic continuation"):

```
A^λ_{μν}(I) = Π_{μν} · ρ_λ(I) · Π_{μν}     (the (μ,ν)-isotypic block of the seminormal interface generator)
```

where `I = σ_{n_inner-1} + d·1` is the bridge generator (`d`: 0 for pp, −h for
nn, −h/2 for pn; `h = q − q⁻¹`), and `Π_{μν} = P_μ^{(in)} · P_ν^{(bl)}` are
isotypic projectors built as **Lagrange spectral projectors of the transposition
class-sums** `C = Σ_{i<j} ρ_λ(T_{(i,j)})` of the inner/block H_k factors. The
class-sum separates all 11 H₆ irreps at the substrate q₀ (min eigen-gap 1.15; the
q≠1 deformation breaks the two q=1 content-sum degeneracies `(4,1,1)/(3,3)` at +3
and `(3,1,1,1)/(2,2,2)` at −3).

To express `A` in standard `V_μ⊗V_ν` coordinates (so the combiner pairs it with
`ρ_μ(W)⊗ρ_ν(β)` evaluated at the *small* H_inner/H_block level — the speedup),
one needs the **intertwiner** `U: V_μ⊗V_ν⊗ℂ^c → range(Π_{μν})`:

```
ã_a U = U (ρ_μ(σ_a)⊗I⊗I),  b̃_b U = U (I⊗ρ_ν(σ_b)⊗I)
A_combiner = partial-trace over ℂ^c of (U⁻¹ Ĩ U)
```

`U` is found as a generic invertible element of the **null space** of the
vectorised constraints `(I_r ⊗ g̃ − Rᵀ ⊗ I_r) vec(U) = 0` (column-major vec).
**No isometry/phase-fixing needed** — the combiner identity is preserved under
similarity, so any invertible intertwiner works.

**Wall framing (archimedean discipline):** this is all *pre-τ* / categorical —
q-rational seminormal data, valid for generic q; evaluation at the real substrate
q₀ is the archimedean shadow (post-τ). Do NOT introduce ordering / Real.sqrt /
analytic-continuation language. See
`docs/audits/2026-06-16-hyperbolic-hurdle-dialog-assessment.md`.

---

## 2. What is merged (all on `main`)

| PR | Artifact |
|----|----------|
| #2353 | `computations/a_operator/a_operator_categorical.py` — `A=ΠρΠ` construction, exact 1e-49; + new PyO3 binding `pyhecke_native.seminormal_matrices_mpfr` |
| #2360 | `computations/a_operator/a_operator_gauge_align.py` — gauge-aligned `A_combiner` (Python) + H₉ universality; verify functions |
| #2362 | `docs/audits/2026-06-16-unjustified-least-squares-fitting-audit.md` — least-squares fit audit |
| #2366 | rename `analytic`→`categorical` (it's categorical/closed-form, not analytic) |
| #2369 | `docs/audits/2026-06-16-wenzl-a3-wireup-scope-and-deflag.md` — H₉⁺ min-norm extracts are **inert** (A≥3 production uses the transfer matrix); 3 suspect scripts annotated |
| #2372 | Rust port 1–3a: `transposition_class_sum_mpfr`, `lagrange_projectors_mpfr`, and the MPFR Gauss primitives `mat_kron_mpfr`/`mat_nullspace_mpfr`/`mat_inverse_mpfr` (in `tools/hecke-engine/src/dense_la_mpfr.rs`: `kron_mpfr`, `rref_mpfr`, `nullspace_mpfr`, `inverse_mpfr`) |
| #2376 | Rust port 3b: `pyhecke_native.gauge_aligned_a_combiner_mpfr` — the full `A_combiner` (one whole-compute PyO3 call per `(λ,μ,ν)`) |
| #2380 | `a_operator_gauge_align.gauge_aligned_A_combiner_general_rust` — Python drop-in wrapper over the Rust combiner; gives #2371 its 26/30 coverage |
| #2384 (this branch) | `class_sum_from_gens` factoring (enabling refactor; see §4a) |

**Key Rust file:** `tools/pyhecke-native/src/lib.rs` (the combiner + bindings),
`tools/hecke-engine/src/dense_la_mpfr.rs` (the MPFR linalg primitives).
The seminormal matrices come from `tools/hecke-engine/src/seminormal_mpfr.rs`
(`seminormal_matrices_mpfr`).

## 3. Sibling coordination (#2371)

`claude/wenzl-a3-recursion-wiring` / PR #2371 (a parallel session) owns the
**production wiring**: `computations/wenzl_a3_combiner_end_to_end.py` assembles
the physical ³He `tr_M = Σ_λ y_λ χ^λ` using the combiner. It consumes our Rust
combiner via the one-line swap:
```python
from a_operator_gauge_align import gauge_aligned_A_combiner_general_rust as gauge_aligned_A_combiner_general, _kron
```
and lifts its `DIM_CAP=50`. **Division of labour: they own the ³He assembly +
canonical-chain wiring; we own the Rust combiner kernel.** Do not duplicate their
assembly.

---

## 4. Remaining task A — all-blocks Rust fn (the real speedup)

**Status:** NOT done. Level-1 caching (#2384) was a false start — see §4a.
**Value:** ~10× on feasible λ (e.g. `(5,3,1)` ~294s → ~30s), making #2371's λ⊢9
sweep fast. **Unlocks no new λ** — nice-to-have.

### 4a. Why level-1 caching (#2384) gave NO speedup (measured)

#2384 factored `class_sum_from_gens` so `gauge_aligned_a_combiner_mpfr` reuses
the λ seminormal for both class-sums (3×→1× rebuild *within a call*). Measured
`(5,3,1)`: 391s vs 294.5s — **noise, no improvement**. Reason: the bottleneck is
NOT the seminormal rebuild; it's the per-`(μ,ν)` dim-`d_λ` dense linear algebra
(class-sum matmuls + projectors + RREF + intertwiner), and the **Python wrapper
calls the Rust fn once per `(μ,ν)`** (11× for `(5,3,1)`), rebuilding the λ
seminormal *and* `C_in/C_bl` each time. #2384's factoring is correct + harmless
and is the *enabling groundwork* (the `class_sum_from_gens` helper) for the real
fix below.

### 4b. The real fix: `gauge_aligned_a_combiner_all_blocks_mpfr`

Add a Rust PyO3 fn that builds the shared parts **once** per λ and loops
`(μ,ν)` internally:

```
fn gauge_aligned_a_combiner_all_blocks_mpfr(
    lam, n_inner, n_block,
    inner_parts: Vec<Vec<usize>>, inner_eigs: Vec<String>,   // μ⊢n_inner + their class-sum eigenvalues
    block_parts: Vec<Vec<usize>>, block_eigs: Vec<String>,
    interface_d: String, q_str: String, dps: u32,
) -> PyResult<Vec<(Vec<usize>, Vec<usize>, Vec<Vec<String>>)>>   // (μ, ν, A) per non-empty block
```

Implementation:
1. Build λ seminormal gens **once**; `C_in = class_sum_from_gens(&gens,dim,0,n_inner-1,prec)`, `C_bl = class_sum_from_gens(&gens,dim,n_inner,n-1,prec)` **once**.
2. Cache `P_μ = lagrange_one(&C_in, &ein, &μ_eig, prec)` per μ; `P_ν` per ν.
3. Loop `(μ,ν)`: `Π = P_μ·P_ν` → the per-block orchestration → `A`; collect `(μ,ν,A)` for non-empty (`r>0`).

**Do this by factoring the per-block orchestration** (everything in
`gauge_aligned_a_combiner_mpfr` from `let p_mu = lagrange_one…` through the
partial-trace, lib.rs ~lines 1191–1331) into a helper
`combiner_block(gens, dim, &c_in, &c_bl, &ein, &mu_e, &ebl, &nu_e, mu, nu, n_inner, n_block, &d_coef, q_str, dps, prec) -> Result<Option<Vec<Vec<Float>>>, String>`
(`None` = empty block). Then BOTH the existing per-block binding and the new
all-blocks fn call `combiner_block`. (Single source of truth — don't duplicate.)

Then update `gauge_aligned_A_combiner_general_rust` (Python) to call the
all-blocks fn once instead of looping `gauge_aligned_a_combiner_mpfr` per `(μ,ν)`.
Keep the `mp.workdps(dps+10)` wrapper (precision discipline — see §6).

**Why deferred:** ~150-line refactor of the verified, merged combiner; high-value
but bug-prone; correctness is *gated* by the verification (§5) so a bug wastes
effort but cannot ship wrong.

---

## 5. Remaining task B — algorithmic intertwiner (clears the last 4 λ)

**Status:** NOT done. Research-grade. **Value:** unlocks the 4 large-`r` λ⊢9.

### Feasibility map (λ⊢9, `r = max_{μ,ν} c^λ_{μν}·d_μ·d_ν`, intertwiner `M` ≈ 8·r⁴ floats)

- **26/30 λ feasible** (r ≤ 40, M < 1 GB) — verified: `(8,1)` 8.3e-50, `(5,3,1)` dim162/r36 3.26e-51.
- **4 λ OOM** (r=64): `(3,3,2,1)`, `(4,3,2)`, `(4,2,2,1)`, `(4,3,1,1)`.

### The wall

The intertwiner is solved by vectorising to an `r²×r²` null space → **O(r⁴)
memory / O(r⁶) time**, an *algorithmic* complexity Rust cannot change. For r=64,
`M` ≈ 8·64⁴ ≈ 5.4 GB → OOM.

### The fix (sketch)

Avoid materialising the `r²×r²` system. `range(Π_{μν})` is `(V_μ⊗V_ν)^{⊕c}`;
decompose it **per factor**: first under the inner H₃-action (μ-isotypic, the
`d_μ`-dim structure via the inner generators' eigenstructure on range), then the
block H₃-action (ν), leaving the multiplicity ℂ^c. Build `U` as a tensor of the
two **smaller** per-factor intertwiners → **O(r³)** instead of O(r⁶), and no `r²`
matrix. This is the genuine unlock for the 4 λ (and would speed up all λ).
Verify against the per-block combiner identity at 1e-25 (§5 of #2360's design doc
has the structure).

---

## 6. Gotchas (learned the hard way — read before coding)

1. **Precision / `workdps` (Gemini #2380, critical):** any Python that does
   `mp.mpf(rust_string)` or `mp.nstr(value, n)` at the FFI boundary must run
   under `with mp.workdps(dps+10):` — else the caller's default global `mp.dps=15`
   silently truncates 50-digit values. Tie `nstr` digit counts to `mp.mp.dps`.
2. **Range basis = RREF(Π), not RREF(Πᵀ) (Gemini #2376, critical):** the pivot
   columns of `RREF(Π)` are the independent columns spanning `col(Π)=range(Π)`.
   `RREF(Πᵀ)` gives independent *rows* — wrong for the non-symmetric oblique
   projector (it passed tests only coincidentally).
3. **PyO3 input guards (Gemini):** validate `strand_lo ≤ strand_hi`, `strand_hi`
   in range, `n_inner/n_block > 0`, generator-list lengths — return
   `PyValueError`, never panic.
4. **Granularity (compute-author §2.1):** whole-compute per PyO3 call. The
   all-blocks fn (per-λ) is the right granularity; per-`(μ,ν)` FFI was the wrong
   one (the wrapper paying 11× rebuild cost).
5. **`rug` has no SVD/null-space** — the MPFR Gauss primitives in `dense_la_mpfr`
   (`rref_mpfr`/`nullspace_mpfr`/`inverse_mpfr`) are the only linalg; reuse them.
6. **The H₉⁺ least-squares extracts are inert** (#2369) — do NOT "fix" them as a
   live production bug; A≥3 values come from the transfer matrix.

---

## 7. Build + verify recipe

```bash
# Build the native wheel (sandbox ships cargo; ~1–2 min):
python3 -m pip install -q numpy mpmath sympy
python3 -m pip install -e tools/qou-substrate -e tools/pyhecke
python3 -m pip install --force-reinstall ./tools/pyhecke-native
cargo check --release --manifest-path tools/pyhecke-native/Cargo.toml   # fast compile gate
```

**Verification = the gauge-invariant combiner identity at 1e-25** (the matrix `A`
is gauge-dependent for multiplicity>1; the identity is not):

```
χ^λ(W·I·β)  ==  Σ_{μν} Tr[ A^λ_{μν} · (ρ_μ(W) ⊗ ρ_ν(β)) ]
```

with the ground-truth χ from the seminormal trace at H_n, and `ρ_μ(W)`/`ρ_ν(β)`
at the small H_inner/H_block level. The Python oracle
`a_operator_gauge_align.gauge_aligned_A_combiner_general` (pure-mpmath) is the
exact-precision reference — any Rust result must match its identity bit-for-(40+)
digits. Helpers: `aoa.exact_seminormal_matrices`, `aoa._trace`, `g._kron`,
`g._classsum_eigenvalues(n, q_str, dps)`. Always `mp.mp.dps=60`, `q = aoa.q0_mp(50)`.

---

## 8. Pointers

- Design: `docs/audits/2026-06-16-categorical-interface-operator-closure-b-design.md`
- Scope/de-flag: `docs/audits/2026-06-16-wenzl-a3-wireup-scope-and-deflag.md`
- Workplan: `docs/workplans/2026-06-16-wenzl-branching-a3-unlock.md`
- Sibling wiring: PR #2371 (`computations/wenzl_a3_combiner_end_to_end.py`)
- Oracle/spec: `computations/a_operator/a_operator_gauge_align.py`
- Rust kernel: `tools/pyhecke-native/src/lib.rs`, `tools/hecke-engine/src/dense_la_mpfr.rs`

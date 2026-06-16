# Lie / eigenvector decomposition of σ_g in the Hoefsmit basis

> **Status (2026-05-18, this branch):** the existing
> `_chi_lambda_of_word_mpf` matrix product is already dense×sparse
> at O(dim × nnz) per matmul. The Hoefsmit YSN basis is itself a
> partial eigendecomposition (1×1 blocks are eigenvectors); the
> 2×2 blocks have a clean Lie / eigendecomp structure that maps to
> a modest speedup. This audit documents the available wins and
> where they pay off.

## Eigenstructure of σ_g (Hoefsmit YSN)

Each Hecke generator σ_g acting on an irreducible H_n module
V_λ in the Hoefsmit seminormal basis has matrix structure:

- **1×1 blocks** along the diagonal where g separates two cells
  with axial-distance ±1 in the standard Young tableau basis.
  Eigenvalue = ±q or ±q^{-1} depending on the sign of the
  axial-distance. **Already eigendecomposed by the YSN basis.**
- **2×2 blocks** where g moves a cell across a "rim hook" cut.
  The block has the form
  $$
  \sigma_g\big|_{\text{2×2}} = \begin{pmatrix} a & b \\ b & d \end{pmatrix}
  \quad\text{with}\quad a + d = \mathrm{tr}, \; ad - b^2 = \det,
  $$
  where the trace and det are determined by the Hecke relation
  $\sigma_g^2 = (q - q^{-1})\sigma_g + 1$. Solving:
  - trace = q − q^{-1}
  - det = −1
  - eigenvalues = (q, −q^{-1}) (independent of which 2×2 block)
  - eigenvectors of the block are computable in closed form from
    (a, b, d), no general diagonalization needed

So **every σ_g has eigenvalues exactly q and −q^{-1}**, with
multiplicities determined by the partition λ.

## Where Lie / eigendecomp pays off

| Use case | Structure | Current cost | With eigendecomp | Speedup |
|---|---|---|---|---|
| Single σ_g matvec | 1 matmul | O(dim × nnz) | O(dim × nnz) | none |
| σ_g^M (repeated) | M matmuls | O(M × dim²) | O(dim²) (build P once, apply diag(λ)^M) | M× for large M |
| (σ_a σ_b)^k confinement | 2k matmuls | O(k × dim²) | O(dim²) (build F = σ_a σ_b once, then F^k via eigen) | 2k× |
| Atomic braid (varied σ's) | n matmuls | O(n × dim²) | O(n × dim²) (no eigen savings) | none |

**Key observation:** atomic braid words from `atom_braid_word_3A`
have **varied generators** (σ_0 then σ_1^{-1} then σ_0 etc.), so
naive per-σ eigendecomp gives no savings. The savings appear when
we **fuse repeated blocks** into a single transfer matrix and
then exponentiate that.

## Block fusion: the practical optimization

The B_3 confinement word `(σ_0 σ_1^{-1})^3` is the same building
block for **every nucleon** in every atom. Compute the fused
transfer matrix F = (σ_0 σ_1^{-1})^3 once per partition λ; reuse
across:
  - proton, neutron (1 nucleon)
  - deuteron, tritium, helium-3 (multiple nucleons)
  - ⁴He, ⁵Li, ⁶Li, ⁷Li, ⁷Be, ⁸Be (more nucleons)

For deuteron (A=2, 2 nucleons), F is applied twice. For ⁸Be
(A=8), F is applied 8 times. Savings: O(5 × A) matmuls per atom
(5 inner matmuls per F, minus the cost of one F build amortized
across multiple atoms).

**Implementation status:** not yet wired. The fused-matrix
approach is also addressable at the f64 level via the existing
Rust `hecke-canonical-chi` binary (cherry-picked from #683 into
this branch), which would benefit from the same fusion: per-λ
build F once in Rust, apply A times per atom call.

## Why this is a modest win in practice

1. **Matrix exponentiation** (F^A via repeated squaring + Lie
   diagonalization) is O(d² log A) instead of O(A × d²). For
   A ≤ 8, log₂(A) ≈ 3, so the savings are ≈ 3× not orders of
   magnitude.
2. **Inter-nucleon arc crossings** break the repeated structure.
   For multi-nucleon atoms the actual word is more like
   `F · ι · F · ι · F · ...` where ι is the inter-nucleon arc; F
   alone doesn't capture the full structure.
3. **Per-partition build cost** (~O(d²) eigendecomposition once)
   adds overhead that competes with the inner matmul savings.

## Recommended sequence (priority order)

1. **Fuse confinement block F = (σ_0 σ_1^{-1})^3 per partition,
   cache F^{powers}.** Reuse across atoms. ~3× speedup, easy.
2. **Per-λ eigendecomp for matrix exponentiation** F^A → via
   eigendecomp + diag exponentiation. Marginal gain on small A,
   significant for A ≥ 8.
3. **Apply same fusion in Rust** (hecke-canonical-chi binary).
   Combined Rust + fusion: 100× over baseline symbolic-q sympy.

## Status

**Documentation-only audit** — no implementation in this branch.
The matrix-product layer is already at the optimal complexity for
varied-generator braids; the residual wins require:
  - Confinement-block fusion (1-2 days, mechanical)
  - Eigendecomp + repeated-squaring (research; benefit limited to
    A ≥ 8 where Rust is also viable)

Cross-references:
  - [`tr_m_wenzl_bridge_mpfr.py:_chi_lambda_of_word_mpf`](../../computations/tr_m_wenzl_bridge_mpfr.py) — current dense×sparse inner loop
  - [`hecke-canonical-chi`](../../tools/hecke-engine/src/bin/hecke_canonical_chi.rs) — Rust kernel (cherry-picked from #683)
  - [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md) — defines σ_g eigenstructure
  - [`def:hoefsmit-seminormal-form`](../../content/quantum-observable-universe/braids-and-knots/) — partial eigendecomposition by construction

# Exact-SDP feasibility audit

**Question.** Can QOU run the joint-tower confinement SDP in
exact-rational arithmetic (i.e. `T = RationalReal` from the upstream
Clarabel-rs bigrational backend) and obtain bit-exact certified
solutions?

**Short answer.** No — for two distinct reasons that compound.  The
realistic path to "exact SDP-derived results" is **dual-certificate
verification** (Peyrl–Parrilo style): solve in `f64` or `MpfrFloat`,
then round the dual to nearby rationals and verify per-Wedderburn-block
PSD via Sturm sequences on rational characteristic polynomials.  This
is QOU [`CLARABEL_PRECISION_PLAN.md` §S9](../../tools/hecke-engine/CLARABEL_PRECISION_PLAN.md#section-4--s9-dual-certificate-verification-peyrl-parrilo).

## Reason 1 — Galois isn't the obstacle, IPM iterate-degree is

Eigenvalues of an `n × n` symmetric rational matrix are representable
as exact algebraic numbers (minimal polynomial over `ℚ` + isolating
real interval; SageMath `AA`, FLINT/Calcium, Mathematica `RootObject`).
Generic quintic+ polynomials are unsolvable in radicals (Abel-Ruffini),
but radical expression isn't required — sign tests and ordering
comparisons reduce to Sturm-sequence sign computations in the ambient
field.  So the eigenvalues are **exactly representable and computable**.

The obstacle is the **per-iteration IPM cost**, which compounds three
multiplicative blowups:

1. **Tower-of-extensions.** Adjoining all `n` eigenvalues of one
   `n × n` iterate to `ℚ` yields a field of degree up to `n!` (Galois
   group `⊆ Sₙ`).  After `k` IPM iterations the working field has
   degree up to `(n!)^k` in the worst case, and per-element arithmetic
   is cubic-or-worse in the degree.
2. **Sign / ordering tests** in the strict-feasibility check
   (`r_prim < tol_feas`) are Sturm-sequence sign computations in the
   current field — polynomial in degree, but degree is the thing
   exploding.
3. **Transcendentals destroy algebraic closure anyway.** Log-barrier
   centering and `exp(·)` step-size policies don't preserve the
   algebraic field.  The bigrational backend already concedes this
   by rounding transcendentals to a thread-local working precision
   (`set_max_arena_bits`).  An exact IPM would inherit the rounding
   compromise and still pay the algebraic-arithmetic cost.

## Reason 2 — Upstream Clarabel-rs explicitly excludes `bigrational + sdp`

The fork's SDP path (`cfg(feature = "sdp")`) defines

```rust
pub trait MaybeBlasFloatT: Copy + ...
```

— i.e. `T: Copy` is required by the SDP-cone code in
`src/solver/chordal/decomp/`.  `RationalReal` is not `Copy` (it wraps
a heap-allocated `BigRational` in a thread-local arena handle), so
`bigrational + sdp` fails to compile.  This is intentional per the
upstream design: PSD-cone projection on rationals would need
eigendecomposition over algebraic numbers, which is out of scope for
the Clarabel-rs project (deferred indefinitely; see Phase 8 docs in
the upstream PR).

The same constraint applies to `MpfrFloat` — also not `Copy`, also
incompatible with the `sdp` feature.  QOU enforces both at compile
time via `compile_error!` guards in
[`tools/hecke-engine/src/lib.rs`](../../tools/hecke-engine/src/lib.rs).

## What's actually feasible

| Approach | Exactness | Scale | QOU workplan section |
|---|---|---|---|
| **`n ≤ 4` closed-form** | radical eigenvalues via Cardano/Ferrari | block-by-block; narrow | not pursued — `d_λ` exceeds 4 quickly |
| **Ball arithmetic (Arb-style)** | proven enclosures, not exact | scales like f64 | not pursued |
| **Hybrid certify-after-the-fact** | exact rational dual + Sturm-PSD | works at QOU's `n_0 ≤ 18` since per-block degree is `d_λ ≪ n_0!` | **§S9** — chosen approach |
| **MpfrFloat IPM** | high precision, not exact | full SDP via the f64 chordal path is unavailable; LP/QP only | §S4-MPFR (constraint-prep wrapper, not solver) |

QOU's Wedderburn-block decomposition is the structural feature that
makes Reason-1's tower-degree blowup tractable in the verification
direction:

- A monolithic `H_{n_0}` PSD constraint becomes a direct sum
  `⨁_λ ρ_λ(T_w) ⪰ 0` over partitions `λ ⊢ n_0`.
- Each block is `d_λ × d_λ` with `d_λ` bounded by the dimension of
  the irrep `λ` of the symmetric group — much smaller than `n_0`.
- Per-block Sturm-PSD verification stays at degree `d_λ`, not
  `n_0!`.  At `n_0 = 18` (⁶Li) the largest `d_λ` is in the low
  thousands, well within rational-Sturm reach.

The Hoefsmit seminormal form contributes a second structural win:
each generator `ρ_λ(σ_i)` is block-diagonal with `1×1` and `2×2`
sub-blocks, and a single-generator multiplication operates in
extension degree `≤ 2`.  Tower compounding only happens via word
length `ℓ(w)`, bounded by the GB-NF filtration cutoff `L = O(n_0)` —
so the certificate-time extension degree is at most `2^L`,
polynomial in `n_0` for fixed `L`.

## Cross-references

- [`CLARABEL_PRECISION_PLAN.md` §S9](../../tools/hecke-engine/CLARABEL_PRECISION_PLAN.md) —
  dual-certificate verification implementation outline.
- [`tools/hecke-engine/src/lib.rs`](../../tools/hecke-engine/src/lib.rs) —
  `compile_error!` guards for the Clarabel-feature mutex.
- [Upstream Clarabel-rs PR #1](https://github.com/litlfred/Clarabel.rs/pull/1) —
  fork's bigrational + mpfr backend; the `MaybeBlasFloatT: Copy`
  constraint at `src/algebra/floats.rs:111` defines the boundary.
- [`prop:joint-tower-sdp-confinement`](../../content/quantum-observable-universe/braids-and-knots/joint-tower-sdp-confinement.md) —
  the design-spec SDP that motivates this analysis.
- [`prop:wedderburn-trace-identity`](../../content/quantum-observable-universe/braids-and-knots/wedderburn-trace-identity.md) —
  the block decomposition that makes per-block verification
  tractable.

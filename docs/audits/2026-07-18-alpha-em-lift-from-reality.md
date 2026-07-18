# α_EM B2 lift — the instance constructor: lift from reality (2026-07-18)

**Bean:** `qou-tq20` (B2 lift), third tranche — after #3985 (interface class)
and #3992 (ℂ-level vertex model).

**Lean (this PR):** [`QOU/Archimedean/LiftFromReality.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/LiftFromReality.lean)
— sorry-free, `lean`-direct exit 0 with Mathlib, lint-clean.

**Scope guard (STRICT):** the constructor is a theorem, never an `instance`
declaration; nothing derives the premise; nothing wired; `1/(8π)` stays
phase-4.

## The result

The honest attempt at the `TauRhoHodgeLift` instance, delivered as an
**instance-constructor theorem**:

> `tauRhoHodgeLift_of_real_operator` — any hermitian operator `M` on the
> conjugate-doubled space `H^{1,0} ⊕ H^{0,1}` that commutes with the
> antilinear swap-conjugation `C(x,y) = (ȳ, x̄)` induces a **legitimate**
> `TauRhoHodgeLift` on its diagonal blocks.

Both class fields are *proved* from the reality premise:

- `conjugated_of_real` — reality `C M C = M` (matrix form
  `P·(M.map star)·P = M`) **forces** the lower diagonal block to be the
  entrywise conjugate of the upper one. The lift's `conjugated` field is
  automatic for real operators.
- `hermitian_block_of_isHermitian` — self-adjointness passes to the
  `H^{1,0}` block.
- `equal_split_of_real_operator` — end-to-end: any real self-adjoint loop
  operator's two Hodge-block weights split equally — the ½ of `½·a₀`
  composed through the interface's conditional theorems.

## The wall's final form

Combining with the merged plan (B1 #3955 · B2s #3960 · B3 #3969 · B4a #3973
· B4b #3977 · B5 #3982 · interface #3985 · ℂ-model #3992), the entire α_EM
per-loop wall now reduces to **one named premise**:

> **(Reality realization.)** The α_EM loop weight operator on `H¹(Bring)` is
> real self-adjoint and commutes with the Hodge swap-conjugation, with
> `H^{1,0}`-block equal to the τ-image of the canonical Markov channel
> weight.

Two observations locate the remaining difficulty precisely:

1. For any **Laplacian-derived** weight (a real metric's heat weight — the
   B3 route), the reality premise holds *by construction*. So the geometric
   half of the premise is free.
2. What is genuinely open is the **τ-identification**: that the categorical
   Markov channel weight is realized by such a Laplacian-derived operator.
   This is where the Epstein det′Δ front (#3934) and the period-matrix
   integration (#3963) meet this program: the Jacobian flat metric (period
   matrix τ₀ from the Braden–Disney-Hogg data) gives a concrete real
   operator whose `H^{1,0}` heat block is computable — a future numerical
   consistency check of the identification (consistency only; the
   identification itself is functorial).

## Position

```
qou-tq20 tranches:  #3985 interface class → #3992 ℂ-model both endpoints →
                    THIS constructor (reality ⟹ instance, legitimately)
Wall = (Reality realization) — one named premise; geometric half free by
construction; open half = the τ-identification of the Markov weight.
```

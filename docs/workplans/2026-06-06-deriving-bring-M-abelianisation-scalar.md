# Deriving the Bring prolongation matrix `M` — symmetry + abelianisation narrowing

**Goal:** supply the last open input of the keystone — the explicit prolongation
operator `M` whose characteristic polynomial is the q-difference kernel `R`
(`bring_picard_fuchs_kernel.py`: `R = charpoly(M)`; existence proved in
`prop:prolonged-periods-fixed-depth`).

**This doc does not compute `M` from scratch (Griffiths–Dwork on the genus-4
quintic is a major undertaking). It narrows `M` structurally** — formalize-first
— so the eventual computation, or the empirical read-off from #1765's
`a_D⁽ⁿ⁾`, targets a small object.

## 1. The naive size, and why it is an overestimate

`M` acts on the Gauss–Manin period space `V = H¹_dR` of the Bring family. Bring's
curve is genus 4, so `dim V = 2g = 8` and the existence proof bounds the
recurrence depth by `8`. But two proved facts cut this down.

### 1a. Abelianisation (Cartan reduction) — the dominant cut

`prop:mi-sw-abelianisation` (proved) reduces the non-abelian multiplicative
integral over the exceptional divisor to its **Cartan component**
`A⁰ = X dz = λ_SW`. The prolonged periods `a_D⁽ⁿ⁾ = ∮ λ_SW⁽ⁿ⁾` are therefore
periods of the **abelianised** (Cartan) sub-connection, not the full rank-8
Gauss–Manin connection. So `M` is the prolongation on the **abelianised
sub-local-system**, whose rank is the number of independent Cartan periods —
bounded by the branch-point count, not by `2g`.

### 1b. `S₅ ≅ PSL₂(𝔽₅)` symmetry — isotypic pinning

Bring's surface has automorphism group `S₅` (order 120). It acts on `V = H¹`,
decomposing it into `S₅`-isotypic components. `λ_SW` lives in **one** such
component (the one carrying the Cartan datum). `M` commutes with the `S₅` action
(it is Gauss–Manin, hence equivariant), so by Schur it preserves each isotypic
block and **restricts to the single block containing `λ_SW`**. The depth `d` is
therefore the dimension of that block, read off the `S₅` character table on the
8-dimensional `H¹` — a small integer.

## 2. The depth is fixed *a priori* at 2 (S₅ Hodge theory)

The structural route (§3.2) supersedes the depth-1 guess. The
**representation-theoretic part is machine-checked** by
`s5_bring_hodge_depth.py` (3/3): it computes the character inner products and
the multiplicity, giving depth **≤ 2**. The step from `≤ 2` to **exactly 2** is
an additional geometric lemma (Griffiths transversality), labelled below as
*not* machine-checked. Concretely the script establishes:

- `H⁰(Ω)` of Bring's curve is the **irreducible** 4-dim `S₅`-rep `W` (Riera–
  Rodríguez 1992; either the standard rep `(4,1)` or its sign-twist
  `(2,1,1,1)` — the computation confirms `⟨χ_W, χ_W⟩ = 1` for both, and that
  they are distinct, `⟨χ_(4,1), χ_(2,1,1,1)⟩ = 0`).
- Hence `H¹ = H^{1,0} ⊕ H^{0,1} = W ⊕ conj W = 2·W`: the multiplicity of `W`
  in `H¹` is **2** (`⟨χ_{H¹}, χ_W⟩ = 2`).
- `M` (Gauss–Manin) is `S₅`-equivariant, so by Schur it acts as
  `id_W ⊗ B` with `B` a **2×2** matrix on the Hodge multiplicity space ⇒
  **depth `≤ 2`**.
- **Griffiths transversality** (`∇F^p ⊂ F^{p−1}⊗Ω`) couples `H^{1,0}↔H^{0,1}`
  non-trivially, so `B` is non-scalar ⇒ **depth is exactly 2**.

So `R = charpoly(B) = x² − tr(B)·x + det(B)` is degree 2. This is consistent
with — and explains — the depth-2 Chebyshev recurrence of the torus sector:
both are weight-1 (rank-2 Hodge) Picard–Fuchs.

### `det B = 1` — the second number is derived (one unknown left)

The Gauss–Manin monodromy preserves the curve's principal polarisation (the
cup-product symplectic form, non-degenerate on the rank-2 `W`-Hodge plane by
Hodge–Riemann), so `B ∈ Sp(2) = SL₂` ⇒ **`det B = 1`**
([`prop:sl2-prolongation-recurrence`](../../content/quantum-observable-universe/mass-theory/sl2-prolongation-recurrence.md),
Lean `sl2_prolongation_recurrence`, sorry-free). Hence

> `R = x² − τ·x + 1`,  recurrence `a_D⁽ⁿ⁺²⁾ = τ·a_D⁽ⁿ⁺¹⁾ − a_D⁽ⁿ⁾`,

with the **single** remaining unknown `τ = tr B`. The torus confirms it
(`τ = 2cosh(2η₀)`, `det = 1`; `sl2_tau_solver.py`, 2/2). For the binding sector
`τ = 2cosh θ` for a prolongation rapidity `θ`.

### The empirical cross-check (now needs only THREE values)

Because `det B = 1` removes one parameter, `τ` is solved from **three**
consecutive periods: `τ = (a_D⁽²⁾ + a_D⁽⁴⁾)/a_D⁽³⁾` (`sl2_tau_solver.tau_from_three`),
then verified by `a_D⁽⁵⁾ = τ·a_D⁽⁴⁾ − a_D⁽³⁾`. `a_D⁽⁴⁾` = Family-A is wired;
`a_D⁽²⁾, a_D⁽³⁾` are #1765's `λ(L)` at `c = 1, 2`. A non-constant `τ` across
windows, or a returned depth `≠ 2`, would
**refutes** the prolongation-symbol identification.

## 3. Forward path

1. **Structural (done):** `S₅`-character decomposition fixes depth = 2
   (`s5_bring_hodge_depth.py`). Remaining: the explicit 2×2 prolongation
   matrix `B` (local monodromy of `λ_SW` on the `W`-Hodge plane) ⇒
   `R = charpoly(B)`.
2. **Empirical (cross-check):** obtain `a_D⁽²,³,⁵,⁶⁾` from #1765; run
   `minimal_recurrence` and confirm depth 2 + constant kernel.
3. Either route closes the identification half ⇒ instantiate
   `QDifferenceKernelIsProlongationSymbol` ⇒ `thm:binding-closure-conditional`
   becomes unconditional ⇒ P1 (the many-body binding closure) is proved.

Both routes target a **small** object (`d ≤` an `S₅`-block dimension `≤ 8`,
likely far less), not an open-ended search.

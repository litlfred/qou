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

## 2. The immediate falsifiable test (depth-1 first)

The cheapest hypothesis consistent with §1 is that the abelianised block is
**rank-1**: then `M` is multiplication by a scalar `r` (the prolongation
eigenvalue / local monodromy), giving a **depth-1** recurrence
`a_D⁽ⁿ⁺¹⁾ = r · a_D⁽ⁿ⁾`. This is testable with only **three** values
`a_D⁽²⁾, a_D⁽³⁾, a_D⁽⁴⁾`:

> depth-1 holds  ⟺  `a_D⁽³⁾ / a_D⁽²⁾ = a_D⁽⁴⁾ / a_D⁽³⁾`  (= `r`).

`a_D⁽⁴⁾` = Family-A is wired; the moment #1765 supplies `a_D⁽²⁾, a_D⁽³⁾` this is
a one-line check (`minimal_recurrence` returns `(1, [r])` or escalates to the
next depth). If it escalates, the depth is the §1b block dimension and
`recurrence_kernel(M)` = `charpoly(M)` over that block gives `R`.

**Caveat (do not overclaim depth-1).** The non-hyperbolic torus periods
`cosh((2m+1)η₀)/(2cosh η₀)` are depth-2 (Chebyshev) — a *different* sequence
(Vol = 0 sector). The abelianised **hyperbolic** binding periods may be depth-1
or higher; §1 only bounds the depth small, it does not fix it at 1. The test
decides.

## 3. Forward path

1. **Empirical (fast):** obtain `a_D⁽²,³⁾` from #1765; run `minimal_recurrence`
   on `[a_D⁽²⁾, a_D⁽³⁾, a_D⁽⁴⁾, …]`. Depth-1 ⇒ `R` is one number, done.
2. **Structural (rigorous):** compute the `S₅`-character decomposition of `H¹`
   to fix the block dimension `d` a priori, then the local monodromy of
   `λ_SW` at the branch points to get the `d×d` matrix `M`; `R = charpoly(M)`.
3. Either route closes the identification half ⇒ instantiate
   `QDifferenceKernelIsProlongationSymbol` ⇒ `thm:binding-closure-conditional`
   becomes unconditional ⇒ P1 (the many-body binding closure) is proved.

Both routes target a **small** object (`d ≤` an `S₅`-block dimension `≤ 8`,
likely far less), not an open-ended search.

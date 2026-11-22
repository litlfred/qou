import QOU.Hecke.InteriorMarkovOfBraidedTower

/-!
# The general-`A` bond product, in the shape the binding arc quotes

`QOU/Hecke/MarkovBondFactor.lean` proves the one-bond factor
`tr_M(c·σ_i + d) = c·z + d` and the two-bond (`A = 3`) case, and records the
general-`A` case as an open gap: *"the general `A`-bond factorization
`tr_M(∏_k (c_k • σ_{i_k} + d_k)) = ∏_k (c_k·z + d_k)` for pairwise-distant
generators needs the cross-level Markov axiom (or a word-induction principle)
that the class does not yet carry."*

`QOU/Hecke/MarkovInteriorBond.lean` supplies that word-induction principle
(`tr_bondWord_of_interiorMarkov`) conditionally on `InteriorMarkov`, and
`QOU/Hecke/InteriorMarkovOfBraidedTower.lean` discharges `InteriorMarkov` on
every `BraidedTower`. What is missing between the two is only a *shape*: the
bond-word theorem is stated for a chain carrying blocks between the bonds, and
the gap above is quoted for the bare product of bond letters. This file closes
that shape gap:

* `pureChain` — the chain of bonds `g₀ < g₁ < ⋯` with every intervening block
  equal to `1`;
* `tr_pureBondChain_of_interiorMarkov` — `tr (∏_k (σ_{g_k} + d_k)) = ∏_k (z + d_k)`
  conditionally on `InteriorMarkov`;
* `tr_pureBondChain_of_braided` — the same on **every braided tower**, with no
  hypothesis beyond the Iwahori–Hecke relations and the Markov axioms.

## Scope — read before quoting this as "the gap is closed"

Three limits, each of which matters and none of which this file removes.

1. **The coefficient is `1`, not a general `c_k`.** The letter here is
   `σ_g + d • 1`, so this proves `∏_k (z + d_k)`, not `∏_k (c_k·z + d_k)`.
   `c_k • σ + d_k` is `c_k • (σ + (d_k/c_k) • 1)` only when `c_k` is invertible,
   and the ambient ring is a bare `CommRing`. This is not a restriction on the
   corpus's bonds: all three production bond types carry `c = 1`
   (`f_pp = z` at `(c,d) = (1,0)`, `f_nn = z − h` at `(1,−h)`,
   `f_pn = z − h(½ − δ/4)` at `(1, −h(½−δ/4))`), as `MarkovBondFactor`'s own
   docstring lists them.

2. **This is a different class from `MarkovBondFactor`'s.** That module's
   `QOU.Hecke.MarkovTrace n q A` is a **fixed-level, single-algebra** class: one
   `n`, one `A`, one `trace`, no filtration. It cannot *state* the interior
   hypothesis — "`a` below the bond and `b` above it" has no meaning without a
   filtration — which is exactly why its header calls the axiom one "the class
   does not yet carry". The theorem below lives in the tower vocabulary
   (`MarkovTower` / `OcneanuTrace.MarkovTrace`), which has the filtration. So the
   *mathematics* of the general-`A` gap is settled; transporting it into
   `MarkovBondFactor`'s own class is a separate bridge and is **not** done here.

3. **A braided tower is not yet the production trace.** The production Ocneanu
   trace of `H_n(q)` at `z = q³/(q²+1)` is constructed and proved unique as a
   `SchurWeyl.HeckeCoset.MarkovTraceFamily`; nothing in the tree packages that
   family as an `OcneanuTrace.MarkovTrace` carrying a `BraidedTower` instance
   (bean `qou-gr3t`, remaining item; `qou-0fmb`). The two `BraidedTower`
   instances the corpus does carry are the presented Hecke tower
   `heckeTowerMarkovTrace` (which factors through the rank-2 quotient and is not
   faithful) and the symmetric-group tower.

Generic `R`, `A`; no `ℝ`.

## References

- [jones1987] https://doi.org/10.2307/1971403
- [leitner2026] `docs/audits/2026-09-13-interior-markov-of-braided-tower.md`;
  `docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md` §A step 4.
-/

namespace QOU.Hecke.PureBondChainProduct

open QOU.MathlibExt.MarkovUnusedGenerator
open QOU.Hecke.MarkovInteriorBond
open QOU.Hecke.InteriorMarkovOfBraidedTower
open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.HeckeSandwichReduces

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

section Tower

variable (T : MarkovTower R A)

/-- The bond chain with no blocks: bonds `gs` in order, every intervening block
`1`. Paired with `bondWord … 1` this is the bare product
`(σ_{g₀} + d₀) * (σ_{g₁} + d₁) * ⋯`. -/
def pureChain (gs : List (ℕ × R)) : List (ℕ × R × A) :=
  gs.map fun p => (p.1, p.2, (1 : A))

omit [CommRing R] [Algebra R A] in
@[simp] theorem pureChain_nil : pureChain (A := A) ([] : List (ℕ × R)) = [] := rfl

omit [CommRing R] [Algebra R A] in
@[simp] theorem pureChain_cons (g : ℕ) (d : R) (gs : List (ℕ × R)) :
    pureChain (A := A) ((g, d) :: gs) = (g, d, (1 : A)) :: pureChain gs := rfl

/-- The bond multipliers of a pure chain are the `d`'s it was built from. -/
theorem map_pureChain_z (gs : List (ℕ × R)) :
    ((pureChain (A := A) gs).map fun p => T.z + p.2.1)
      = gs.map fun p => T.z + p.2 := by
  induction gs with
  | nil => rfl
  | cons p rest ih => obtain ⟨g, d⟩ := p; simpa using ih

omit [CommRing R] [Algebra R A] in
/-- Deleting every bond from a pure chain leaves `1`. -/
theorem freeWord_pureChain (gs : List (ℕ × R)) :
    freeWord (1 : A) (pureChain (A := A) gs) = 1 := by
  induction gs with
  | nil => rfl
  | cons p rest ih => obtain ⟨g, d⟩ := p; simpa [freeWord] using ih

/-- `Chain'`-style strict increase of the bond indices. -/
def Increasing : List (ℕ × R) → Prop
  | [] => True
  | [_] => True
  | (g, _) :: (g', d') :: rest => g < g' ∧ Increasing ((g', d') :: rest)

/-- A strictly increasing bond list gives a legal chain: every block is `1`, so
the `upper`/`H` memberships are `one_mem` and only the ordering has content. -/
theorem chainOK_pureChain (gs : List (ℕ × R)) (h : Increasing gs) :
    ChainOK T (pureChain (A := A) gs) := by
  induction gs with
  | nil => trivial
  | cons p rest ih =>
    obtain ⟨g, d⟩ := p
    cases rest with
    | nil => exact (upper T g).one_mem
    | cons p' rest' =>
      obtain ⟨g', d'⟩ := p'
      exact ⟨(upper T g).one_mem, (T.H g').one_mem, h.1, ih h.2⟩

/-- **The general-`A` bond product, conditionally on `InteriorMarkov`.**
For strictly increasing bonds `g₀ < g₁ < ⋯`,
`tr ((σ_{g₀} + d₀) * (σ_{g₁} + d₁) * ⋯) = ∏_k (z + d_k)`. -/
theorem tr_pureBondChain_of_interiorMarkov (hT : InteriorMarkov T)
    (gs : List (ℕ × R)) (h : Increasing gs) (h1 : T.tr 1 = 1) :
    T.tr (bondWord T 1 (pureChain (A := A) gs))
      = (gs.map fun p => T.z + p.2).prod := by
  have hx : (1 : A) ∈ T.H (headBond (pureChain (A := A) gs)) :=
    (T.H _).one_mem
  rw [tr_bondWord_of_interiorMarkov T hT _ 1 (chainOK_pureChain T gs h) hx,
    map_pureChain_z T gs, freeWord_pureChain gs, h1, mul_one]

end Tower

section Braided

variable (S : MarkovTrace R A) [BraidedTower S]

/-- **The general-`A` bond product on every braided tower.** No hypothesis
beyond the Iwahori–Hecke relations (quadratic, far-commutation, braid) and the
Markov axioms: the gap `MarkovBondFactor` names for general `A` is a theorem
here, in the `c_k = 1` shape every production bond type has. -/
theorem tr_pureBondChain_of_braided (gs : List (ℕ × R)) (h : Increasing gs) :
    (toTowerB S).tr (bondWord (toTowerB S) 1 (pureChain (A := A) gs))
      = (gs.map fun p => (toTowerB S).z + p.2).prod :=
  tr_pureBondChain_of_interiorMarkov _ (interiorMarkov_of_braided S) gs h S.tr_one

end Braided

end QOU.Hecke.PureBondChainProduct

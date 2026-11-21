/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.Hecke.InteriorMarkovOfBraidedTower
import QOU.Mass.StrandLayoutForcesChain

/-!
# The bond product for the PRODUCTION chain layout

Bean `qou-qqm4`. That bean measures

    tr_M(W_atom) / tr_M(W_free) = ∏_bonds (z + d_b)

on the production atom word to orders `≤ 5` and `A ≤ 5`, and records under
§"What is NOT established" that the identity is **NOT PROVED**. This file proves
it for the production *layout*, from two results that landed on 2026-09-13 and
were never connected:

* `Hecke.InteriorMarkovOfBraidedTower.tr_bondWord_of_braided` — the bond product
  `tr (bondWord) = (∏ (z + d_k)) · tr (freeWord)` on **every** braided tower,
  given the chain hypotheses `ChainOK`; and
* `Mass.StrandLayoutForcesChain` — nucleon `k` occupies strands `3k, 3k+1, 3k+2`
  of a `3A`-strand braid, so the inter-nucleon bridges are exactly the generators
  `σ_{3k+2}`, `k = 0 … A−2`, and they join **consecutive** nucleons only.

The second supplies precisely the indices the first quantifies over, and the
level arithmetic then discharges `ChainOK` outright.

## The layout, and why `ChainOK` is immediate

Block `k` is a word in the generators that stay inside nucleon `k`'s strands,
i.e. in `{σ_{3k}, σ_{3k+1}}`; bond `k` is `σ_{3k+2}`. `ChainOK` asks three
things of consecutive entries, and each is arithmetic on `3k+2`:

| requirement | here | why |
|---|---|---|
| bonds strictly increase | `3k+2 < 3(k+1)+2` | `omega` |
| block `k+1` lies **above** bond `k` | `blk (k+1) ∈ upper (3k+2)` | its generators are `3k+3, 3k+4 > 3k+2` |
| block `k+1` lies **below** bond `k+1` | `blk (k+1) ∈ H (3k+5)` | its generators are `3k+3, 3k+4 < 3k+5` |

So the production chain is a `ChainOK` chain **because of where the strands put
the bridges**, which is `StrandLayoutForcesChain`'s content, not an assumption
about the word.

## What is proved

`tr_productionChain` — the bond product for the production layout on any
`MarkovTower` satisfying `InteriorMarkov`.

`tr_productionChain_braided` — the same with **no hypothesis beyond
`BraidedTower`**, since `interiorMarkov_of_braided` discharges `InteriorMarkov`
there. This is the derived form: three defining relations of `H_n(q)` in, the
bond product out.

`prod_chainFrom` rewrites the list product into `∏ k ∈ range n, (z + d k)`, the
shape `qou-qqm4` states the measurement in.

## 🛑 What is NOT proved — read before quoting this as closing `qou-qqm4`

1. **The bond letters are hypotheses, not derived.** The chain carries an
   arbitrary scalar `d k` per bond. That the *production* letters are
   `pp ↦ 0`, `nn ↦ −h`, `pn ↦ d_averaged_weighted` is `qou-qqm4`'s **measured**
   input (`letter_d_series`), and nothing here derives it. What is derived is
   that *whatever* those scalars are, the trace factorises as the product of
   `z + d`.
2. **The blocks are hypotheses too.** `hlow` / `hup` say each nucleon word sits
   in its own strand window. That is what `StrandLayoutForcesChain` establishes
   about `atom_braid_word_3A`, but the bridge from the Python producer to a Lean
   term is not made here — there is no Lean model of `atom_braid_word_3A`.
3. **No binding coefficient.** Nothing here computes `c₂` or any `c_k`.
4. **`A = 1` is excluded** and is not a gap: a one-nucleon atom has no bond, the
   product is empty, and the statement degenerates.

So this closes the *structural* half of `qou-qqm4` item 3 — the factorisation is
a theorem rather than a measurement — and leaves the *identification* of the
letters where it was.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [leitner2026] beans qou-qqm4 / qou-gr3t / qou-brng.
-/

namespace QOU.Mass.ProductionChainBondProduct

open QOU.MathlibExt.MarkovUnusedGenerator
open QOU.Hecke.MarkovInteriorBond
open QOU.Hecke.InteriorMarkovOfBraidedTower
open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.HeckeSandwichReduces

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

section Tower

variable (T : MarkovTower R A)

/-- **The production chain.** `chainFrom blk d start n` lists `n` bonds starting
at nucleon `start`: bond `j` is the generator `σ_{3(start+j)+2}` carrying the
scalar `d (start+j)`, followed by nucleon block `blk (start+j+1)`.

The indices are `StrandLayoutForcesChain`'s: the bridge between nucleons `k` and
`k+1` is `σ_{3k+2}`, and no other single generator joins two nucleons. -/
def chainFrom (blk : ℕ → A) (d : ℕ → R) (start : ℕ) : ℕ → List (ℕ × R × A)
  | 0 => []
  | (n + 1) => (3 * start + 2, d start, blk (start + 1)) :: chainFrom blk d (start + 1) n

omit [CommRing R] [Ring A] [Algebra R A] in
@[simp] theorem chainFrom_zero (blk : ℕ → A) (d : ℕ → R) (start : ℕ) :
    chainFrom blk d start 0 = [] := rfl

omit [CommRing R] [Ring A] [Algebra R A] in
@[simp] theorem chainFrom_succ (blk : ℕ → A) (d : ℕ → R) (start n : ℕ) :
    chainFrom blk d start (n + 1)
      = (3 * start + 2, d start, blk (start + 1)) :: chainFrom blk d (start + 1) n := rfl

omit [CommRing R] [Ring A] [Algebra R A] in
@[simp] theorem headBond_chainFrom_succ (blk : ℕ → A) (d : ℕ → R) (start n : ℕ) :
    headBond (chainFrom blk d start (n + 1)) = 3 * start + 2 := rfl

/-- **`ChainOK` holds for the production layout**, by the level arithmetic of the
strand windows and nothing else. -/
theorem chainOK_chainFrom (blk : ℕ → A) (d : ℕ → R)
    (hlow : ∀ k, blk k ∈ T.H (3 * k + 2))
    (hup : ∀ k, blk (k + 1) ∈ upper T (3 * k + 2)) :
    ∀ (n start : ℕ), ChainOK T (chainFrom blk d start n) := by
  intro n
  induction n with
  | zero => intro start; trivial
  | succ n ih =>
      intro start
      cases n with
      | zero => exact hup start
      | succ m =>
          refine ⟨hup start, ?_, by omega, ih (start + 1)⟩
          have := hlow (start + 1)
          have e : 3 * (start + 1) + 2 = 3 * (start + 1) + 2 := rfl
          simpa [e] using this

/-- The bond-scalar product of the chain, as an ordinary indexed product. -/
theorem prod_chainFrom (blk : ℕ → A) (d : ℕ → R) :
    ∀ (n start : ℕ),
      ((chainFrom blk d start n).map fun p => T.z + p.2.1).prod
        = ∏ k ∈ Finset.range n, (T.z + d (start + k)) := by
  intro n
  induction n with
  | zero => intro start; simp
  | succ n ih =>
      intro start
      rw [chainFrom_succ, List.map_cons, List.prod_cons, ih (start + 1),
        Finset.prod_range_succ']
      simp [Nat.add_comm, Nat.add_left_comm, mul_comm]

/-- **The bond product for the production layout.**

For a tower with the interior-bond property, the trace of the production atom
word factorises as the product of `z + d` over its bonds times the trace of the
same word with every bond letter deleted. -/
theorem tr_productionChain (hT : InteriorMarkov T) (blk : ℕ → A) (d : ℕ → R) (n : ℕ)
    (hlow : ∀ k, blk k ∈ T.H (3 * k + 2))
    (hup : ∀ k, blk (k + 1) ∈ upper T (3 * k + 2)) :
    T.tr (bondWord T (blk 0) (chainFrom blk d 0 (n + 1)))
      = (∏ k ∈ Finset.range (n + 1), (T.z + d k))
        * T.tr (freeWord (blk 0) (chainFrom blk d 0 (n + 1))) := by
  have hOK := chainOK_chainFrom T blk d hlow hup (n + 1) 0
  have hx : blk 0 ∈ T.H (headBond (chainFrom blk d 0 (n + 1))) := by
    rw [headBond_chainFrom_succ]
    simpa using hlow 0
  have := tr_bondWord_of_interiorMarkov T hT (chainFrom blk d 0 (n + 1)) (blk 0) hOK hx
  rw [this, prod_chainFrom T blk d (n + 1) 0]
  simp

end Tower

/-- **The derived form: the bond product from the braid relations alone.**

No `InteriorMarkov` hypothesis — `interiorMarkov_of_braided` discharges it on
every `BraidedTower`, so the input is exactly the three defining relations of
`H_n(q)` (quadratic, braid, far commutation) together with the strand-window
memberships that `StrandLayoutForcesChain` establishes for the production word.

🛑 The bond scalars `d` remain arbitrary: this derives the *factorisation*, not
the identification of the production letters. See the module docstring. -/
theorem tr_productionChain_braided (S : MarkovTrace R A) [BraidedTower S]
    (blk : ℕ → A) (d : ℕ → R) (n : ℕ)
    (hlow : ∀ k, blk k ∈ (toTowerB S).H (3 * k + 2))
    (hup : ∀ k, blk (k + 1) ∈ upper (toTowerB S) (3 * k + 2)) :
    (toTowerB S).tr (bondWord (toTowerB S) (blk 0) (chainFrom blk d 0 (n + 1)))
      = (∏ k ∈ Finset.range (n + 1), ((toTowerB S).z + d k))
        * (toTowerB S).tr (freeWord (blk 0) (chainFrom blk d 0 (n + 1))) :=
  tr_productionChain (toTowerB S) (interiorMarkov_of_braided S) blk d n hlow hup

end QOU.Mass.ProductionChainBondProduct

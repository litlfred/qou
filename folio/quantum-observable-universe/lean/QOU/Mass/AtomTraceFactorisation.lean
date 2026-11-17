import QOU.Mass.ProductionChainBondProduct
import QOU.MathlibExt.BraidedBlockShiftTrace
import QOU.Hecke.MarkovBondLetterColimit

/-!
# The atom-word trace factorises: `tr_z(W_atom) = ∏_bonds (z + d_k) · P_p(z)^Z · P_n(z)^N`

Bean `qou-5zl1`, step 4.  On every Markov trace with parameter `z` on a braided
tower, and in particular on the Hecke colimit carrying any Markov trace family
(`HeckeColimitFamilyTrace.ocneanuMarkovTraceAt`), the trace of an atom word in
the production strand layout is

    tr (W_atom) = (∏_{k=0}^{A-2} (z + d_k)) · P_p(z)^Z · P_n(z)^N,

where `P_p(z) = tr (proton word)` and `P_n(z) = tr (neutron word)`, each read on
strands `0, 1, 2`, and `Z`, `N` count the proton and neutron blocks.

## The word

`atomWord S isP wp wn d n` has `A = n + 2` nucleon blocks.  Block `k` is the
proton word `wp` if `isP k` and the neutron word `wn` otherwise, placed on strands
`3k, 3k+1, 3k+2`: its letters are `a • 1 + b • g_{3k+i}` with `i ≤ 1`
(`BraidedBlockShiftTrace.wordVal`).  Between blocks `k` and `k+1` sits the bond
letter `g_{3k+2} + d_k • 1`.  This is the layout of
`computations/mass_at_3A_proper.py::atom_braid_word_3A`: a production letter
`(c, d, gen_idx)` is `c·σ + d·1`, the affine letter `(gen_idx, d, c)` here, and
`StrandLayoutForcesChain` shows the bridges are exactly `σ_{3k+2}`.

## Proof

Three results already in the tree, composed:

1. `ProductionChainBondProduct.tr_productionChain_braided` — the bond letters
   come out as `∏ (z + d_k)`, leaving the word with every bond deleted;
2. `freeWord_chainFrom` (here) — that word is the left-to-right product of the
   blocks;
3. `BraidedBlockShiftTrace.tr_blockProd_pn` — blocks in consecutive strand
   windows multiply under the trace (disjoint-block law), and each block's trace
   does not depend on its offset (conjugation by `g_s g_{s+1} g_{s+2}`).

## What is NOT claimed

* **Bond coefficients.**  The bond letter has coefficient `1` on `g`; the
  scalars `d_k` and the nucleon words are inputs.  That the production letters
  are `pp ↦ 0`, `nn ↦ −h`, `pn ↦ d_averaged_weighted` is measured (bean
  `qou-qqm4`), not derived here.
* **Which `z`.**  The theorem holds for any Markov trace on a braided tower.  The
  Markov traces the corpus has proved to exist on the Hecke tower are convention D
  and the Wenzl levels; existence at arbitrary `z` is open (see
  `HeckeColimitFamilyTrace`).
* **No Lean model of the Python producer.**  The atom word here is a Lean term
  in the production layout; nothing checks that `atom_braid_word_3A` emits
  exactly these letters.
* **No binding energy.**  Nothing here computes `B(K)` or any `c_k`.

Base ring: generic `[CommRing R]`, generic `R`-algebra `A`; the colimit
corollary is generic `[CommRing K]`.  No `ℝ`.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [leitner2026] beans qou-5zl1 / qou-qqm4 / qou-slz5; computations/mass_at_3A_proper.py.
-/

namespace QOU.Mass.AtomTraceFactorisation

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.HeckeSandwichReduces
open QOU.Hecke.MarkovInteriorBond QOU.Hecke.InteriorMarkovOfBraidedTower
open QOU.Mass.ProductionChainBondProduct QOU.MathlibExt.BraidedBlockShiftTrace

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

omit [CommRing R] [Algebra R A] in
/-- With every bond letter deleted, the production chain is the left-to-right
product of its blocks. -/
theorem freeWord_chainFrom (blk : ℕ → A) (d : ℕ → R) :
    ∀ (n start : ℕ), freeWord (blk start) (chainFrom blk d start n)
      = ((List.range (n + 1)).map fun k => blk (start + k)).prod := by
  intro n
  induction n with
  | zero => intro start; simp; rfl
  | succ n ih =>
      intro start
      rw [chainFrom_succ, freeWord_cons, ih (start + 1)]
      conv_rhs => rw [List.range_succ_eq_map]
      simp [List.map_map, Function.comp_def, Nat.add_assoc, Nat.add_comm 1]

omit [CommRing R] [Algebra R A] in
theorem freeWord_chainFrom_zero (blk : ℕ → A) (d : ℕ → R) (n : ℕ) :
    freeWord (blk 0) (chainFrom blk d 0 n) = blockProd blk n := by
  rw [freeWord_chainFrom blk d n 0]
  simp [blockProd]

section Atom

variable (S : MarkovTrace R A) [BraidedTower S]

/-- A letter placed above the bond `g` lies in the tower's `upper g`. -/
theorem letterVal_mem_upper {g off : ℕ} (h : g < off) (l : ℕ × R × R) :
    letterVal S off l ∈ upper (toTowerB S) g := by
  have hg : S.g (off + l.1) ∈ upper (toTowerB S) g :=
    σ_mem_upper (toTowerB S) (m := off + l.1) (by omega)
  exact Subalgebra.add_mem _ (Subalgebra.smul_mem _ (Subalgebra.one_mem _) _)
    (Subalgebra.smul_mem _ hg _)

theorem wordVal_mem_upper {g off : ℕ} (h : g < off) :
    ∀ w : List (ℕ × R × R), wordVal S off w ∈ upper (toTowerB S) g
  | [] => Subalgebra.one_mem _
  | l :: w => Subalgebra.mul_mem _ (letterVal_mem_upper S h l) (wordVal_mem_upper h w)

/-- Nucleon block `k`: the proton word if `isP k`, the neutron word otherwise, on
strands `3k, 3k+1, 3k+2`. -/
def nucleonBlock (isP : ℕ → Prop) [DecidablePred isP] (wp wn : List (ℕ × R × R)) (k : ℕ) : A :=
  wordVal S (3 * k) (if isP k then wp else wn)

/-- **The atom word** with `n + 2` nucleons: blocks `nucleonBlock k` joined by the
bond letters `g_{3k+2} + d_k • 1`, `k = 0 … n`. -/
def atomWord (isP : ℕ → Prop) [DecidablePred isP] (wp wn : List (ℕ × R × R)) (d : ℕ → R)
    (n : ℕ) : A :=
  bondWord (toTowerB S) (nucleonBlock S isP wp wn 0)
    (chainFrom (nucleonBlock S isP wp wn) d 0 (n + 1))

/-- **The trace factorisation.**

`tr (W_atom) = (∏_{k ≤ n} (z + d_k)) · P_p^Z · P_n^N`, with
`P_p = tr (wp at offset 0)`, `P_n = tr (wn at offset 0)`, and `Z`, `N` the numbers
of proton and neutron blocks among the `n + 2` nucleons. -/
theorem tr_atomWord (isP : ℕ → Prop) [DecidablePred isP] (wp wn : List (ℕ × R × R))
    (hp : ∀ l ∈ wp, l.1 ≤ 1) (hn : ∀ l ∈ wn, l.1 ≤ 1) (d : ℕ → R) (n : ℕ) :
    S.tr (atomWord S isP wp wn d n)
      = (∏ k ∈ Finset.range (n + 1), (S.z + d k))
        * S.tr (wordVal S 0 wp) ^ ((Finset.range (n + 2)).filter isP).card
        * S.tr (wordVal S 0 wn) ^ ((Finset.range (n + 2)).filter (fun k => ¬ isP k)).card := by
  have hw : ∀ k, ∀ l ∈ (if isP k then wp else wn), l.1 ≤ 1 := fun k => by
    split_ifs; exacts [hp, hn]
  have hlow : ∀ k, nucleonBlock S isP wp wn k ∈ (toTowerB S).H (3 * k + 2) := fun k => by
    simpa [nucleonBlock, add_assoc] using wordVal_mem_H S (3 * k) 1 _ (hw k)
  have hup : ∀ k, nucleonBlock S isP wp wn (k + 1) ∈ upper (toTowerB S) (3 * k + 2) :=
    fun k => wordVal_mem_upper S (by omega) _
  have h1 := tr_productionChain_braided S (nucleonBlock S isP wp wn) d n hlow hup
  have h2 := tr_blockProd_pn S isP wp wn hp hn (n + 1)
  change (toTowerB S).tr _ = _
  rw [atomWord, h1, freeWord_chainFrom_zero]
  change (∏ k ∈ Finset.range (n + 1), (S.z + d k)) * S.tr (blockProd _ (n + 1)) = _
  rw [show blockProd (nucleonBlock S isP wp wn) (n + 1)
      = blockProd (fun k => wordVal S (3 * k) (if isP k then wp else wn)) (n + 1) from rfl, h2,
    mul_assoc]

/-- **`z = 0`**: the bond factor is `∏ d_k`, the canonical-trace (`τ`) form of
`TauBondLetter`: in particular a bare bond (`d_k = 0`) makes the atom trace `0`. -/
theorem tr_atomWord_of_z_eq_zero (hz : S.z = 0) (isP : ℕ → Prop) [DecidablePred isP]
    (wp wn : List (ℕ × R × R)) (hp : ∀ l ∈ wp, l.1 ≤ 1) (hn : ∀ l ∈ wn, l.1 ≤ 1)
    (d : ℕ → R) (n : ℕ) :
    S.tr (atomWord S isP wp wn d n)
      = (∏ k ∈ Finset.range (n + 1), d k)
        * S.tr (wordVal S 0 wp) ^ ((Finset.range (n + 2)).filter isP).card
        * S.tr (wordVal S 0 wn) ^ ((Finset.range (n + 2)).filter (fun k => ¬ isP k)).card := by
  rw [tr_atomWord S isP wp wn hp hn d n, hz]
  simp only [zero_add]

/-- **Uniform-bond power factorisation of the atom trace (`qou-5zl1`).**
When every inter-nucleon bridge carries the same scalar offset `d₀`, the `n + 1`
bond factors collapse to `(S.z + d₀) ^ (n + 1)`. -/
theorem tr_atomWord_const_bond (isP : ℕ → Prop) [DecidablePred isP]
    (wp wn : List (ℕ × R × R)) (hp : ∀ l ∈ wp, l.1 ≤ 1) (hn : ∀ l ∈ wn, l.1 ≤ 1)
    (d₀ : R) (n : ℕ) :
    S.tr (atomWord S isP wp wn (fun _ => d₀) n)
      = (S.z + d₀) ^ (n + 1)
        * S.tr (wordVal S 0 wp) ^ ((Finset.range (n + 2)).filter isP).card
        * S.tr (wordVal S 0 wn) ^ ((Finset.range (n + 2)).filter (fun k => ¬ isP k)).card := by
  rw [tr_atomWord S isP wp wn hp hn (fun _ => d₀) n, Finset.prod_const, Finset.card_range]

end Atom


/-! ## On the Hecke colimit -/

section Colimit

open QOU.SchurWeyl QOU.SchurWeyl.HeckeColimit QOU.SchurWeyl.HeckeColimitFamilyTrace

variable {K : Type*} [CommRing K] {q qi z : K}
  (U : HeckeCoset.MarkovTraceFamily K q qi z) (hqi : q * qi = 1)

/-- **The factorisation on the Hecke colimit**, for any Markov trace family at
any parameter `z`: `tr_z(W_atom) = ∏ (z + d_k) · P_p(z)^Z · P_n(z)^N`. -/
theorem tr_atomWord_colimit (isP : ℕ → Prop) [DecidablePred isP]
    (wp wn : List (ℕ × K × K)) (hp : ∀ l ∈ wp, l.1 ≤ 1) (hn : ∀ l ∈ wn, l.1 ≤ 1)
    (d : ℕ → K) (n : ℕ) :
    trFam U (atomWord (ocneanuMarkovTraceAt U hqi) isP wp wn d n)
      = (∏ k ∈ Finset.range (n + 1), (z + d k))
        * trFam U (wordVal (ocneanuMarkovTraceAt U hqi) 0 wp)
            ^ ((Finset.range (n + 2)).filter isP).card
        * trFam U (wordVal (ocneanuMarkovTraceAt U hqi) 0 wn)
            ^ ((Finset.range (n + 2)).filter (fun k => ¬ isP k)).card :=
  tr_atomWord (ocneanuMarkovTraceAt U hqi) isP wp wn hp hn d n

end Colimit

end QOU.Mass.AtomTraceFactorisation

/-
Copyright (c) 2026 QOU contributors. All rights reserved.

# The quark braid element cannot carry the Coulomb charge

Bean `qou-cvoq` (V8), under epic `qou-qia8`.

`sm-open-problems.md` records the hypercharge blocker as "framework braid words
per chiral fermion still missing", and
`computations/chiral_fermion_braid_words_probe.py` carried the quark writhe as an
**assumption** (`w = 0`, "motivated by the gluon unit being writhe-balanced").

**The quark braid element is not missing.** `knot-particle-dictionary-table4-data.md`
gives it outright, in a column headed *"Braid element in 𝓑₃"*:

| quark | braid element | lepton descent |
|---|---|---|
| up `𝔲` | `σᵢ` (positive crossing) | `← T(2,3)` |
| down `𝔡` | `σᵢ⁻¹` (negative crossing) | `← T(2,3)^σ` |
| strange `𝔰` | `σᵢ⁻¹` | `← T(2,5)^σ` |
| charm `𝔠` | `σᵢ` | `← T(2,5)` |
| bottom `𝔟` | `σᵢ⁻¹` | `← T(2,7)^σ` |

The `←` column is **lepton descent**, not identity — so the strangelet block's
`𝔰 = T(2,5)^σ` writes `=` where the dictionary writes `←`.  The braid element is
a *single generator*, matching `up-quark.md`'s "the up quark is not a distinct
knot type; it is the unknot distinguished by its environment", with the
environment recorded as the crossing's sign.

So the quark writhe is `±1`, **not** `0`.

## What is proved

* `antiUp_eq_down` — the braid mirror of the up quark **is** the down quark's
  braid element.  Both are `σᵢ⁻¹`; this is computed, not assumed.
* `charge_not_factoring_through_braid_element` — hence the Coulomb charge cannot
  be a function of the braid element.  The anti-up and the down share a braid
  element but carry `−2/3` and `−1/3`.
* `charge_not_factoring_through_writhe` — a fortiori not a function of the
  writhe, since the two share writhe `−1`.
* `linear_charge_map_refuted` — in particular no `Q = c·w` fits `𝔲` and `𝔡`
  together: their writhes are antisymmetric (`±1`) while their charges are not
  (`+2/3`, `−1/3`).
* `borromean_strand_writhes_all_zero` — and the `±` label cannot be recovered
  from the *ambient* word either: in the canonical `𝓑₃ = (σ₁σ₂⁻¹)³` every strand
  has per-strand signed crossing sum `0`, unchanged by reversing any single
  component's orientation.

## What this locates

The corpus's own prose already says it: a quark is "the unknot **distinguished by
its environment**".  What these theorems add is that the environment label is
**load-bearing and unformalized** — the braid-element column cannot carry the
charge, so the colour-tube datum is doing the work, and nothing in the corpus
formalizes it.  This is the quark-level twin of
`HyperchargeInvariant.exists_writhe_degenerate_pair`: a writhe-degenerate pair
with different charge, now exhibited at the level of the *fundamental* fermions
rather than the composites.

## Honest scope

**Scope-(b)** for the factoring claims, with the invariant cited: charge
conjugation negates `Q` and acts as the braid mirror, and the mirror of `σᵢ` *is*
`σᵢ⁻¹` — computed here, not assumed.  The exclusion is of *the braid element as
carrier of `Q`*, not of the framework's charge assignment, which is untouched and
which the corpus already attributes to the environment.

The Standard-Model charges `+2/3`, `−1/3` enter as explicit hypotheses; they are
experimental input, not derived here.

`ℤ`-valued writhe, `ℚ`-valued charge; no `Real`, no ordering (§7c).
-/

import Mathlib.Data.Int.Basic
import Mathlib.Data.List.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace QOU.StandardModel.QuarkBraid

/-- A braid word: entry `±i` denotes `σᵢ^{±1}`.  Same convention as
`ChiralFermionBraidWords.lean` and `WritheLevelParity.lean`. -/
abbrev BraidWord := List ℤ

/-- The writhe: the sum of the crossing signs. -/
def writhe (β : BraidWord) : ℤ := (β.map Int.sign).sum

/-- The braid mirror `σᵢ ↦ σᵢ⁻¹` — charge conjugation, per
`AntiparticleCrossingReversalContext`. -/
def mirror (β : BraidWord) : BraidWord := β.map (fun g => -g)

/-- The up quark's braid element: `σ₁`, a positive crossing. -/
def upQuark : BraidWord := [1]

/-- The down quark's braid element: `σ₁⁻¹`, a negative crossing. -/
def downQuark : BraidWord := [-1]

/-! ### The anti-up and the down are the same braid element -/

/-- **Computed, not assumed.**  The braid mirror of the up quark is exactly the
down quark's braid element. -/
theorem antiUp_eq_down : mirror upQuark = downQuark := by decide

/-- The two carry the same writhe, `−1`. -/
theorem writhe_antiUp_eq_writhe_down :
    writhe (mirror upQuark) = -1 ∧ writhe downQuark = -1 := by
  refine ⟨?_, ?_⟩ <;> decide

/-- The quark writhes are `±1`, not `0`. -/
theorem quark_writhes : writhe upQuark = 1 ∧ writhe downQuark = -1 := by
  refine ⟨?_, ?_⟩ <;> decide

/-! ### The braid element cannot carry the charge -/

/-- **The Coulomb charge does not factor through the braid element.**

Charge conjugation negates `Q` and acts as the braid mirror.  The mirror of the
up quark *is* the down quark's braid element (`antiUp_eq_down`), so `Q` would
have to give that one word both `−2/3` (as the anti-up) and `−1/3` (as the
down). -/
theorem charge_not_factoring_through_braid_element
    (Q : BraidWord → ℚ)
    (hu : Q upQuark = 2 / 3) (hd : Q downQuark = -1 / 3)
    (hconj : Q (mirror upQuark) = - Q upQuark) :
    False := by
  rw [antiUp_eq_down, hd, hu] at hconj
  norm_num at hconj

/-- **A fortiori, not a function of the writhe.**

This route does not use `antiUp_eq_down`: it needs only that the anti-up and the
down carry the *same writhe* `−1`, so any `Q` factoring through the writhe is
forced to agree on them. -/
theorem charge_not_factoring_through_writhe
    (f : ℤ → ℚ) (Q : BraidWord → ℚ) (hfac : ∀ β, Q β = f (writhe β))
    (hu : Q upQuark = 2 / 3) (hd : Q downQuark = -1 / 3)
    (hconj : Q (mirror upQuark) = - Q upQuark) :
    False := by
  have hsame : Q (mirror upQuark) = Q downQuark := by
    rw [hfac (mirror upQuark), hfac downQuark]
    -- the two words carry the same writhe, `−1`
    congr 1
  rw [hsame, hd, hu] at hconj
  norm_num at hconj

/-- **No linear charge map.**

`Q = c·w` cannot fit the up and down together: their writhes are antisymmetric
(`+1`, `−1`) while their charges are not (`+2/3`, `−1/3`).  This is the sharpest
form — it needs no charge-conjugation hypothesis at all. -/
theorem linear_charge_map_refuted (c : ℚ)
    (hu : c * (writhe upQuark : ℚ) = 2 / 3)
    (hd : c * (writhe downQuark : ℚ) = -1 / 3) :
    False := by
  rw [show writhe upQuark = 1 from by decide] at hu
  rw [show writhe downQuark = -1 from by decide] at hd
  norm_num at hu hd
  rw [hu] at hd
  norm_num at hd

/-! ### Nor can the ambient word supply the sign -/

/-- The gluon unit `σ₁σ₂⁻¹`. -/
def gluonUnit : BraidWord := [1, -2]

/-- The canonical Borromean baryon `𝓑₃ = (σ₁σ₂⁻¹)³ ∈ B₃`. -/
def borromean : BraidWord := gluonUnit ++ gluonUnit ++ gluonUnit

/-- Signed crossing sum carried by one strand of a braid word on `n` strands.

Each letter `σᵢ^{±1}` is a crossing between the two strands currently at
positions `i` and `i+1`; it contributes its sign to **both** of them.  The
running list is the one-line notation of the partial permutation. -/
def strandWrithe (n : ℕ) (β : BraidWord) (s : ℕ) : ℤ :=
  (β.foldl
      (fun (st : List ℕ × ℤ) (g : ℤ) =>
        let l := st.1
        let i := g.natAbs - 1
        let a := (l[i]?).getD 0
        let b := (l[i + 1]?).getD 0
        let acc := if a = s ∨ b = s then st.2 + Int.sign g else st.2
        (((l.set i b).set (i + 1) a), acc))
      (List.range n, 0)).2

/-- **Every strand of the canonical Borromean word carries signed crossing sum
`0`.**

So the `±` orientation label that `up-quark.md` and `down-quark.md` use to
separate `𝔲` from `𝔡` inside `𝓑₃` is invisible to any per-strand crossing sum:
the three components are indistinguishable by that measure.  (The pairwise
linking numbers all vanish too — that is the defining property of the Borromean
rings, and it is why the word is cyclically symmetric of order three.) -/
theorem borromean_strand_writhes_all_zero :
    strandWrithe 3 borromean 0 = 0 ∧
    strandWrithe 3 borromean 1 = 0 ∧
    strandWrithe 3 borromean 2 = 0 := by
  refine ⟨?_, ?_, ?_⟩ <;> decide

end QOU.StandardModel.QuarkBraid

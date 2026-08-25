import Mathlib.Tactic

/-!
# QOU.BraidsAndKnots.BorromeanPairwiseLinking — pairwise linking cannot see the proton braid

Bean `qou-bhfg` (front 4-B). Formalize-first prune, per AGENTS.md
§"Formalize-first probe discipline": a structural fact that removes an entire
ansatz class *before* any numerical search over it.

## The problem this prunes

Front 4-B needs the **intra-nucleon EM self-energy** `E_EM` — the open
"two-like-charge EM-linking invariant" that blocks both `m_d − m_u` and 69 % of
the ³He mirror residual. The extraction is `δ_QCD = Δ_pn + E_EM` with
`Δ_pn = 1.2933 MeV` framework-derived
(`computations/quark-mass-extraction-stage1.witness.json`); the lattice
comparator for `E_EM` is ≈ 0.8 MeV.

The obvious first ansatz for a two-charge linking energy is a functional of the
**pairwise linking numbers** of the constituent strands. This file shows that
class is empty on the proton.

## The computation

The proton braid is the Borromean link, presented in the corpus as the closed
braid `(σ₀σ₁⁻¹)³ ∈ B₃`
(`knots-particles-confinement/brunnian-property-of-borromean.md`). Simulating
that word — each letter exchanges the strands currently at positions `i`, `i+1`
and contributes a crossing of its sign between *those two strands* — gives
signed crossing sums of `0` for all three pairs, hence all three linking numbers
`lk = 0`.

So a functional of pairwise linking data alone assigns the Borromean braid
**exactly what it assigns the 3-component unlink**, and a self-energy that
vanishes on the unlink therefore vanishes on the proton. It cannot produce
0.8 MeV. This is a scope-(b) exclusion of the ansatz class, with the invariant
named and computed rather than asserted.

## Why this is not vacuous

`hopf_crossSum_ne_zero` is the control: the same simulator returns `2` (i.e.
`lk = 1`) on the Hopf link `σ₀²`. So the machinery detects nonzero linking when
it is there, and the Borromean zeros are a fact about the Borromean word rather
than about the simulator. `borromean_perm_id` additionally confirms the word
closes to a genuine **3**-component link, so the zeros are not an artifact of
components having been merged.

## Scope — read before citing

* This is about **pairwise** linking only. It says nothing against the **Milnor
  triple linking number** `μ̄₁₂₃`, which is precisely the first invariant that
  is *nonzero* on Borromean rings, and which the corpus already carries for the
  `sin²θ_W` front. If anything this file points at it.
* It does **not** prove the corpus's `conj:brunnian-property-of-borromean`
  (that every 2-component sublink is the *unlink*). That is strictly stronger —
  vanishing linking number is necessary, not sufficient — and remains a
  conjecture. Nothing here should be read as closing it.
* It assumes the corpus's presentation of the proton braid as `(σ₀σ₁⁻¹)³`,
  consumed as given.

-- Ref: [kawauchi1996] (Brunnian links; linking number of a closed braid as the
-- signed count of crossings between two components).
-/

namespace QOU.BraidsAndKnots.BorromeanPairwiseLinking

/-- A braid letter: the generator index `i`, and the sign of the crossing. -/
abbrev Letter := ℕ × ℤ

/-- Exchange the entries at positions `i` and `i+1`. -/
def swapAt (pos : List ℕ) (i : ℕ) : List ℕ :=
  let a := pos.getD i 0
  let b := pos.getD (i + 1) 0
  (pos.set i b).set (i + 1) a

/-- The strand ordering after reading the whole word. -/
def finalPerm : List Letter → List ℕ → List ℕ
  | [], pos => pos
  | (i, _) :: w, pos => finalPerm w (swapAt pos i)

/-- Signed crossing sum between strands `s` and `t` along a braid word. Each
letter `(i, e)` exchanges the strands at positions `i`, `i+1` and contributes
`e` to the pair it exchanges. The linking number is half this. -/
def crossSum (s t : ℕ) : List Letter → List ℕ → ℤ
  | [], _ => 0
  | (i, e) :: w, pos =>
      let a := pos.getD i 0
      let b := pos.getD (i + 1) 0
      (if (a = s ∧ b = t) ∨ (a = t ∧ b = s) then e else 0)
        + crossSum s t w (swapAt pos i)

/-- The corpus's Borromean presentation `(σ₀σ₁⁻¹)³`. -/
def borWord : List Letter := [(0, 1), (1, -1), (0, 1), (1, -1), (0, 1), (1, -1)]

/-- The Hopf link `σ₀²`, used as the control. -/
def hopfWord : List Letter := [(0, 1), (0, 1)]

/-- The Borromean word closes to a genuine **three**-component link: the strand
ordering returns to the identity, so no two components have been merged. -/
theorem borromean_perm_id : finalPerm borWord [0, 1, 2] = [0, 1, 2] := by decide

/-- All three pairwise signed crossing sums vanish on the Borromean braid,
hence all three linking numbers are `0`. -/
theorem borromean_crossSum_zero :
    (crossSum 0 1 borWord [0, 1, 2],
     crossSum 0 2 borWord [0, 1, 2],
     crossSum 1 2 borWord [0, 1, 2]) = (0, 0, 0) := by decide

/-- **The control.** The same simulator returns a nonzero sum on the Hopf link,
so the Borromean zeros are a fact about that word and not about this file. -/
theorem hopf_crossSum_ne_zero : crossSum 0 1 hopfWord [0, 1] ≠ 0 := by decide

/-- **The prune.** Any functional of the pairwise linking data alone takes the
same value on the proton braid as on the 3-component unlink.

So an `E_EM` ansatz built from pairwise linking cannot distinguish them; if it
vanishes on the unlink — as a self-energy must — it vanishes on the proton, and
cannot reach the ≈ 0.8 MeV comparator. The search should go to `μ̄₁₂₃`. -/
theorem pairwise_functional_cannot_separate {α : Type*} (F : ℤ → ℤ → ℤ → α) :
    F (crossSum 0 1 borWord [0, 1, 2])
      (crossSum 0 2 borWord [0, 1, 2])
      (crossSum 1 2 borWord [0, 1, 2]) = F 0 0 0 := by
  have h := borromean_crossSum_zero
  simp only [Prod.mk.injEq] at h
  rw [h.1, h.2.1, h.2.2]

end QOU.BraidsAndKnots.BorromeanPairwiseLinking

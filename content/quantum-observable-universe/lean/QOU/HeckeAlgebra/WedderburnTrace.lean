/-
# The Markov trace against the regular trace

`QOU/HeckeAlgebra/MarkovTrace.lean`'s module doc used to advertise `wenzlBridge`
as

    markovTrace n (wedderburnEmbed x) = Σ_λ y_λ(q_0) · trace (x λ)

That is not what `wenzlBridge` says. Its statement is
`markovTraceOnWedderburn x = Σ_λ y_λ(q_0) · trace (x λ)`, whose left-hand side
*is* that sum by definition — it is proved by `rfl`, and it never mentions an
embedding. Relating a trace on the assembled matrix algebra to the per-block sum
is real content, and until `blockDiagonal` was constructed (bean `qou-usol`)
there was no embedding in the corpus to state it over. The doc was corrected in
`qou-kp2z`; this module supplies what it was reaching for.

## What is proved here

`blockDiagonal_trace` (in `WedderburnConstruction`) gives the regular-representation
side: `trace (blockDiagonal x) = Σ_λ f^λ · trace (x λ)`. Set beside
`markovTraceOnWedderburn x = Σ_λ y_λ(q_0) · trace (x λ)`, the two are **the same
functional form with `y_λ(q_0)` in place of `f^λ`**, and that is stated exactly:

* `markovTrace_sub_regular_trace` — the difference is
  `Σ_λ (y_λ(q_0) − f^λ) · trace (x λ)`, so the deformation is entirely in the
  coefficients and nowhere in the algebra.
* `markovTrace_eq_regular_trace_of_coeff_eq` — they agree when the coefficients
  agree.
* `coeff_eq_of_markovTrace_eq_regular_trace` — and only then. Agreement for
  *every* decomposition forces `y_λ(q_0) = f^λ` for every `λ`, read off the
  single-block indicator. This is the sharp form: the Markov trace is a genuine
  deformation of the regular trace unless the Jones–Markov coefficients are the
  seminormal dimensions.

## What is *not* proved here

Nothing about `markovTrace` on `HeckeElement` — that is `opaque` in
`QOU/HeckeAlgebra/Common.lean` and connecting it to this sum is a separate
obligation. The identity the old doc line stated, with `markovTrace` on the left,
therefore remains unproved; what is proved is the block-sum comparison it should
have said.
-/
import QOU.HeckeAlgebra.WedderburnConstruction
import QOU.HeckeAlgebra.MarkovTrace

namespace QOU.HeckeAlgebra.WedderburnTrace

open QOU.HeckeAlgebra QOU.HeckeAlgebra.Wedderburn QOU.HeckeAlgebra.MarkovTrace
open QOU.HeckeAlgebra.Hoefsmit

variable {n : ℕ}

/-- **The Markov trace is the regular trace with deformed coefficients.** The
difference collapses to a single sum over partitions in which the algebra plays
no part — only `y_λ(q_0) − f^λ` does. -/
theorem markovTrace_sub_regular_trace (x : WedderburnDecomposition n) :
    markovTraceOnWedderburn x - (blockDiagonal x).trace
      = ∑ lam : Nat.Partition n,
          (JonesMarkovCoefficient lam QSubstrate.q_0 - (seminormalDim lam : ℝ))
            * (x lam).trace := by
  classical
  have h1 : markovTraceOnWedderburn x
      = ∑ lam : Nat.Partition n,
          JonesMarkovCoefficient lam QSubstrate.q_0 * (x lam).trace := by
    rw [wenzlBridge]; rfl
  rw [h1, blockDiagonal_trace, ← Finset.sum_sub_distrib]
  exact Finset.sum_congr rfl fun lam _ => by ring

/-- If the Jones–Markov coefficients are the seminormal dimensions, the Markov
trace *is* the regular trace. -/
theorem markovTrace_eq_regular_trace_of_coeff_eq
    (h : ∀ lam : Nat.Partition n,
        JonesMarkovCoefficient lam QSubstrate.q_0 = (seminormalDim lam : ℝ))
    (x : WedderburnDecomposition n) :
    markovTraceOnWedderburn x = (blockDiagonal x).trace := by
  classical
  have := markovTrace_sub_regular_trace x
  rw [show (∑ lam : Nat.Partition n,
        (JonesMarkovCoefficient lam QSubstrate.q_0 - (seminormalDim lam : ℝ))
          * (x lam).trace) = 0 from
      Finset.sum_eq_zero fun lam _ => by rw [h lam]; ring] at this
  linarith

/-- **The single-block indicator.** `blockOne lam` is the decomposition carrying
the identity matrix on block `lam` and zero elsewhere; its block trace is `f^λ`
at `lam` and `0` away from it. This is what turns "the two traces agree on every
`x`" into a statement about the coefficients themselves. -/
noncomputable def blockOne (lam : Nat.Partition n) : WedderburnDecomposition n := by
  classical
  exact fun mu => if h : mu = lam then h ▸ (1 : Matrix (Fin (seminormalDim lam))
    (Fin (seminormalDim lam)) ℝ) else 0

@[simp] theorem blockOne_self (lam : Nat.Partition n) :
    blockOne lam lam = (1 : Matrix (Fin (seminormalDim lam))
      (Fin (seminormalDim lam)) ℝ) := by
  classical
  simp [blockOne]

@[simp] theorem blockOne_of_ne {lam mu : Nat.Partition n} (h : mu ≠ lam) :
    blockOne lam mu = 0 := by
  classical
  simp [blockOne, h]

/-- **Sharpness.** If the Markov trace agrees with the regular trace on *every*
decomposition, the coefficients were the dimensions all along. So any genuine
`q`-deformation of `y_λ` is visible on some element — the bridge is not a
restatement of the regular trace. -/
theorem coeff_eq_of_markovTrace_eq_regular_trace
    (h : ∀ x : WedderburnDecomposition n,
        markovTraceOnWedderburn x = (blockDiagonal x).trace)
    (lam : Nat.Partition n) :
    JonesMarkovCoefficient lam QSubstrate.q_0 = (seminormalDim lam : ℝ) := by
  classical
  have hsub := markovTrace_sub_regular_trace (blockOne lam)
  rw [h (blockOne lam), sub_self] at hsub
  have hterm : ∀ mu ∈ (Finset.univ : Finset (Nat.Partition n)), mu ≠ lam →
      (JonesMarkovCoefficient mu QSubstrate.q_0 - (seminormalDim mu : ℝ))
        * ((blockOne lam) mu).trace = 0 := by
    intro mu _ hne; rw [blockOne_of_ne hne]; simp
  rw [Finset.sum_eq_single lam hterm (by simp)] at hsub
  rw [blockOne_self, Matrix.trace_one, Fintype.card_fin] at hsub
  have hpos : (0 : ℝ) < (seminormalDim lam : ℝ) := by
    exact_mod_cast seminormalDim_pos' lam
  rcases mul_eq_zero.mp hsub.symm with hh | hh
  · exact sub_eq_zero.mp hh
  · linarith

/-! ## What a trace-factoring functional can carry

`qou-qb7p`'s surviving objection to the `(2,1)` clause of
`unified-iterative-correction-proof.md` is that the Wedderburn embedding has the
wrong *shape*: it assembles blocks into one matrix, while the clause needs one
block's scalar `C_{(2,1)}` split into three coefficients (volume, surface,
Coulomb). The probe accompanying that bean records why no Lean theorem was
offered — the tempting statement, "three independent coefficients cannot come
from one scalar", is **false as stated**, since set-theoretically a single real
encodes three, and manufacturing a hypothesis to rescue it would be the same
overreach the probe documents.

There is a hypothesis that does not have to be manufactured: **linearity**,
which this corpus already commits to for the Markov trace (`markovTrace_add`,
`markovTrace_smul`, `markovTrace_linear` in `Common.lean`). Under it the
statement becomes true and provable, and that is what this section does.

`markovTraceOnWedderburn` factors through the block **traces** — one real per
partition, not the whole block. A functional of that form supported at a single
`λ` is exactly `c λ · trace (x λ)`: one coefficient against one number. Three
such functionals at one partition are therefore linearly dependent, with an
explicit witness.

**What this does and does not settle.** It does *not* show the `(2,1)` clause is
false; the claim may well be true. It rules out one route to it — the route the
clause itself names — whenever that route is linear, factors through the Markov
trace, and is localised at `(2,1)`. Three independent coefficients need more
than one dimension, and that is all the trace supplies.

It also says where the room is, which is the useful half. For `λ = (2,1) ⊢ 3`,
`f^λ = 2`, so the block is `M₂(ℝ)` — **four** real dimensions, of which the
trace reads one. The information the clause wants is present in the block and
destroyed by taking its trace. A derivation that reads the block rather than its
trace is not blocked by anything here.
-/

/-- A functional that factors through the block traces. -/
noncomputable def traceFunctional (c : Nat.Partition n → ℝ)
    (x : WedderburnDecomposition n) : ℝ :=
  ∑ lam : Nat.Partition n, c lam * (x lam).trace

/-- Distinct coefficient families give distinct functionals. -/
theorem traceFunctional_injective :
    Function.Injective (traceFunctional (n := n)) := by
  classical
  intro c d h
  funext lam
  have hx := congrFun h (blockOne lam)
  unfold traceFunctional at hx
  have hterm : ∀ (e : Nat.Partition n → ℝ),
      (∑ mu : Nat.Partition n, e mu * ((blockOne lam) mu).trace)
        = e lam * (seminormalDim lam : ℝ) := by
    intro e
    rw [Finset.sum_eq_single lam
      (fun mu _ hne => by rw [blockOne_of_ne hne]; simp) (by simp)]
    rw [blockOne_self, Matrix.trace_one, Fintype.card_fin]
  rw [hterm c, hterm d] at hx
  have hpos : (0 : ℝ) < (seminormalDim lam : ℝ) := by
    exact_mod_cast seminormalDim_pos' lam
  exact mul_right_cancel₀ (ne_of_gt hpos) hx

/-- **A functional supported at one partition is one real times one real.** All
the freedom it has is the single coefficient `c lam`; the decomposition enters
only through the single number `(x lam).trace`. -/
theorem traceFunctional_supported_apply
    {c : Nat.Partition n → ℝ} {lam : Nat.Partition n}
    (hsupp : ∀ mu, mu ≠ lam → c mu = 0) (x : WedderburnDecomposition n) :
    traceFunctional c x = c lam * (x lam).trace := by
  classical
  unfold traceFunctional
  exact Finset.sum_eq_single lam
    (fun mu _ hne => by rw [hsupp mu hne]; ring) (by simp)

/-- **Any three are linearly dependent.** So volume, surface and Coulomb cannot
be three independent trace-factoring functionals localised at a single
partition: the span is one-dimensional, and three vectors in a line are
dependent. The witness is explicit, not an existence argument. -/
theorem three_supported_traceFunctionals_dependent
    {c₁ c₂ c₃ : Nat.Partition n → ℝ} {lam : Nat.Partition n}
    (h₁ : ∀ mu, mu ≠ lam → c₁ mu = 0) (h₂ : ∀ mu, mu ≠ lam → c₂ mu = 0)
    (h₃ : ∀ mu, mu ≠ lam → c₃ mu = 0) :
    ∃ a b e : ℝ, (a ≠ 0 ∨ b ≠ 0 ∨ e ≠ 0) ∧
      ∀ x : WedderburnDecomposition n,
        a * traceFunctional c₁ x + b * traceFunctional c₂ x
          + e * traceFunctional c₃ x = 0 := by
  classical
  rcases eq_or_ne (c₁ lam) 0 with hz | hz
  · refine ⟨1, 0, 0, Or.inl one_ne_zero, fun x => ?_⟩
    rw [traceFunctional_supported_apply h₁ x, hz]; ring
  · refine ⟨c₂ lam, -c₁ lam, 0, Or.inr (Or.inl (neg_ne_zero.mpr hz)), fun x => ?_⟩
    rw [traceFunctional_supported_apply h₁ x, traceFunctional_supported_apply h₂ x,
        traceFunctional_supported_apply h₃ x]
    ring

/-- The Markov trace is itself such a functional, with `c = y_·(q_0)`. So the
no-go applies to it, not merely to an abstract family. -/
theorem markovTraceOnWedderburn_eq_traceFunctional (x : WedderburnDecomposition n) :
    markovTraceOnWedderburn x
      = traceFunctional (fun lam => JonesMarkovCoefficient lam QSubstrate.q_0) x := by
  rw [wenzlBridge]; rfl

/-! ## The room, stated as a theorem rather than asserted

The section above says the information a three-coefficient derivation needs "is
present in the block and destroyed by taking its trace". That was an assertion.
Here it is a theorem: whenever a block has dimension at least 2 there are
**distinct** decompositions on which *every* block trace agrees — so every
trace-factoring functional, the Markov trace included, takes the same value on
both. The witness is an off-diagonal matrix unit, which is traceless.

So the trace is not merely one-dimensional per partition (previous section); it
is genuinely lossy, and the lost directions are where a derivation reading the
block rather than its trace would live.

**The `(2,1)` instance — gap closed 2026-09-05.** Instantiating this needs
`2 ≤ f^{(2,1)}`. When first written, no declaration in this corpus computed
`seminormalDim` at a named partition, so the `(2,1)` reading was conditional on
a classical fact the Lean side could not supply.
`QOU/HeckeAlgebra/SeminormalDimSmall.lean` now supplies it — `f^{(2,1)} = 2` via
the Frame–Robinson–Thrall hook-length formula (`QOU.Mathlib.dimSYT_eq_dimHLF`,
pointwise and axiom-clean) — and carries `trace_does_not_separate_p21` and
`indistinguishable_p21` unconditionally.

The theorems here keep the bound as a hypothesis, which is the right shape: they
are about any block of dimension ≥ 2, and `(2,1)` is one instance. Note the
boundary is real — `f^{(1,1)} = 1`, also proved there, so at the charge shape the
block *is* its trace and these results say nothing.
-/

/-- The decomposition carrying a single matrix on block `lam`, zero elsewhere. -/
noncomputable def blockAt (lam : Nat.Partition n)
    (A : Matrix (Fin (seminormalDim lam)) (Fin (seminormalDim lam)) ℝ) :
    WedderburnDecomposition n := by
  classical
  exact fun mu => if h : mu = lam then h ▸ A else 0

@[simp] theorem blockAt_self (lam : Nat.Partition n) (A) :
    blockAt lam A lam = A := by classical simp [blockAt]

@[simp] theorem blockAt_of_ne {lam mu : Nat.Partition n} (h : mu ≠ lam) (A) :
    blockAt lam A mu = 0 := by classical simp [blockAt, h]

/-- **The block traces do not separate decompositions.** Whenever a block has
dimension at least 2 there are distinct decompositions with *every* block trace
equal — so every trace-factoring functional, the Markov trace included, takes the
same value on both. The witness is an off-diagonal matrix unit, which is
traceless. -/
theorem trace_does_not_separate (lam : Nat.Partition n)
    (h2 : 2 ≤ seminormalDim lam) :
    ∃ x y : WedderburnDecomposition n, x ≠ y ∧
      ∀ mu : Nat.Partition n, (x mu).trace = (y mu).trace := by
  classical
  have h0 : (0 : ℕ) < seminormalDim lam := lt_of_lt_of_le (by norm_num) h2
  have h1 : (1 : ℕ) < seminormalDim lam := lt_of_lt_of_le (by norm_num) h2
  set i : Fin (seminormalDim lam) := ⟨0, h0⟩ with hi
  set j : Fin (seminormalDim lam) := ⟨1, h1⟩ with hj
  have hij : i ≠ j := by simp [hi, hj, Fin.ext_iff]
  refine ⟨blockAt lam 0, blockAt lam (Matrix.single i j 1), ?_, ?_⟩
  · intro hcon
    have := congrFun hcon lam
    rw [blockAt_self, blockAt_self] at this
    have hentry := congrFun (congrFun this i) j
    simp [Matrix.single] at hentry
  · intro mu
    rcases eq_or_ne mu lam with rfl | hne
    · rw [blockAt_self, blockAt_self, Matrix.trace_zero]
      have hempty : (Finset.univ.filter
          (fun x : Fin (seminormalDim mu) => i = x ∧ j = x)) = ∅ := by
        refine Finset.filter_eq_empty_iff.mpr ?_
        rintro x - ⟨rfl, hjx⟩
        exact hij hjx.symm
      simp [Matrix.trace, Matrix.diag, Matrix.single, hempty]
    · rw [blockAt_of_ne hne, blockAt_of_ne hne]

/-- **Every trace-factoring functional is blind to it.** The Markov trace
included — which is the point, since that is the functional the `(2,1)` clause
routes through. -/
theorem exists_indistinguishable_by_every_traceFunctional
    (lam : Nat.Partition n) (h2 : 2 ≤ seminormalDim lam) :
    ∃ x y : WedderburnDecomposition n, x ≠ y ∧
      (∀ c : Nat.Partition n → ℝ, traceFunctional c x = traceFunctional c y) ∧
      markovTraceOnWedderburn x = markovTraceOnWedderburn y := by
  classical
  obtain ⟨x, y, hne, htr⟩ := trace_does_not_separate lam h2
  have hall : ∀ c : Nat.Partition n → ℝ, traceFunctional c x = traceFunctional c y := by
    intro c
    unfold traceFunctional
    exact Finset.sum_congr rfl fun mu _ => by rw [htr mu]
  refine ⟨x, y, hne, hall, ?_⟩
  rw [markovTraceOnWedderburn_eq_traceFunctional,
      markovTraceOnWedderburn_eq_traceFunctional]
  exact hall _

end QOU.HeckeAlgebra.WedderburnTrace

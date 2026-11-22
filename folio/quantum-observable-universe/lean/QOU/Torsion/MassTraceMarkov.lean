import QOU.IwahoriHecke.JonesNormalisation
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Pi

/-!
# The Markov trace of a braid is a trace of its multiplicative integral

`QOU.Torsion.MassTraceIdentity` proved the mass identity with the categorical trace of
the Frobenius algebra `A` on itself, and recorded that this functional is the *regular*
trace, which is not a Markov trace (`tr(σ₁σ₂) = h²/6` against `(tr σ₁)² = h²/4` on
`H₃(q)`). This file states the identity with the trace that *is* a Markov trace: the
site-weighted (quantum) trace on `V^{⊗(m+1)}`, `V = R²`, through Jimbo's R-matrix.

## Statement

A braid word is a list of letters `(a, ε)`, `a : Fin m` a strand and `ε` the sign of the
crossing. Its *transport* is the R-matrix acting at strands `a, a+1` of `V^{⊗(m+1)}`:

    T(a, +) = Ř_a,        T(a, −) = Ř_a − (q − q⁻¹) = Ř_a⁻¹.

The discrete multiplicative integral of the word is the ordered product of its transports,
`Hol(ℓ₁ ⋯ ℓ_k) = T(ℓ₁) ⋯ T(ℓ_k)`. The theorems are:

1. `braidTrace_wordBraid` (the mass identity, Markov form):

       tr_M(β_ℓ) = wi^{m+1} · Tr(K^{⊗(m+1)} · Hol(ℓ)),

   where `β_ℓ` is the braid the word spells, `tr_M` is the normalised Markov trace
   `QOU.IwahoriHecke.BraidGroup.braidTrace`, `K = diag(w₀, w₁)` is the site weight and
   `wi` is the inverse of `w₀ + w₁`.
2. `jonesFn_wordBraid`: the framing-corrected trace of
   `QOU.IwahoriHecke.JonesNormalisation` is the same functional of `Hol(ℓ)`, times
   `A^{m+1} · B^{writhe}`, with the writhe read off the word as the signed letter count.

The weight is not chosen here. `QOU.IwahoriHecke.MarkovPeel.peel_forces_physical_weight`
shows the peel exists only for `w = (1, q²)` up to scale, and `MarkovNormalized` shows
the normalised peel scalar is then `q³/(q²+1)` (convention D). The two theorems hold for
every weight; the Markov property holds only for that one.

## What this does not say

* **Not a link invariant.** `jonesFn` is invariant under both Markov moves and under
  conjugation, but descending it to links needs Markov's theorem, which this corpus does
  not prove (`JonesNormalisation`, §"One gap remains").
* **Not the categorical trace of `A`.** That is `MassTraceIdentity`, and it is the regular
  trace. This file replaces it; it does not identify the two.
* **Not the continuous holonomy.** `Hol` is the ordered product of finitely many
  transports. That a KZ / Drinfeld–Kohno holonomy along a path of configurations equals
  such a product is a cited theorem, not proved here.
* **Not the abstract Markov trace.** The Ocneanu-weight trace on `H_n(q)` being this
  functional is bean `qou-0fmb`.

**Base ring (§7c).** `R` is any commutative ring; `q⁻¹` and `(w₀ + w₁)⁻¹` are carried as
`qi`, `wi` with witnessing equations. No order, norm or root is used.

## References

- Ref: [turaev2010] https://doi.org/10.1515/9783110221831 — enhanced Yang–Baxter operators;
  the functional `α^{-w} β^{-n} Tr(ρ(b) ∘ μ^{⊗n})` is this one with `μ = K`.
- Ref: [jones1987] https://doi.org/10.2307/1971403 — Hecke algebra representations of
  braid groups and link polynomials.
- Ref: [jimbo1986] https://doi.org/10.1007/BF00704588 — the R-matrix.
-/

namespace QOU.Torsion.MassTraceMarkov

open QOU.IwahoriHecke.Balanced QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.QuantumTrace
open QOU.IwahoriHecke.MarkovNormalized QOU.IwahoriHecke.BraidGroup
open QOU.IwahoriHecke.JonesNormalisation QOU.MathlibExt.SkeinRelation

variable {R : Type*} [CommRing R] (q qi : R) {m : ℕ}

/-- The braid generator of a letter, with the sign of the crossing. -/
def letterBraid (ℓ : Fin m × Bool) : BraidGroupN m :=
  if ℓ.2 then braidGen (coxA m) ℓ.1 else (braidGen (coxA m) ℓ.1)⁻¹

/-- The braid a word spells. -/
def wordBraid (ℓs : List (Fin m × Bool)) : BraidGroupN m :=
  (ℓs.map letterBraid).prod

/-- The R-matrix transport of a letter: `Ř_a` for a positive crossing,
`Ř_a − (q − q⁻¹) = Ř_a⁻¹` for a negative one. -/
def transport (ℓ : Fin m × Bool) : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R :=
  if ℓ.2 then strandBraid q qi ℓ.1 else negCrossing q qi (strandBraid q qi ℓ.1)

/-- The discrete multiplicative integral of a word: the ordered product of its transports. -/
def hol (ℓs : List (Fin m × Bool)) : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R :=
  (ℓs.map (transport q qi)).prod

@[simp] theorem hol_nil : hol q qi ([] : List (Fin m × Bool)) = 1 := rfl

@[simp] theorem hol_cons (ℓ : Fin m × Bool) (ℓs : List (Fin m × Bool)) :
    hol q qi (ℓ :: ℓs) = transport q qi ℓ * hol q qi ℓs := rfl

/-- **Non-abelian multiplicative-integral composition law (Option 1).**
    The holonomy of a concatenated braid word is the ordered product of the two holonomies. -/
theorem hol_append (ℓs ℓs' : List (Fin m × Bool)) :
    hol q qi (ℓs ++ ℓs') = hol q qi ℓs * hol q qi ℓs' := by
  simp [hol, List.map_append, List.prod_append]

/-- A letter's braid, represented in the Hecke algebra and then on `V^{⊗(m+1)}`, is its
transport. -/
theorem heckeActionN_letter (hqi : q * qi = 1) (ℓ : Fin m × Bool) :
    heckeActionN q qi hqi
        ((heckeRep (coxA m) hqi coxA_symm (letterBraid ℓ) : (BalancedHecke (coxA m) q)ˣ)
          : BalancedHecke (coxA m) q)
      = transport q qi ℓ := by
  rcases ℓ with ⟨a, _ | _⟩
  · have hval : ((heckeRep (coxA m) hqi coxA_symm (braidGen (coxA m) a)⁻¹
          : (BalancedHecke (coxA m) q)ˣ) : BalancedHecke (coxA m) q)
        = negCrossing q qi (sigma (coxA m) q qi a) := by
      rw [map_inv, heckeRep_braidGen]
      rfl
    simp only [letterBraid, transport, Bool.false_eq_true, if_false]
    rw [hval, negCrossing, negCrossing, map_sub, AlgHom.commutes, heckeActionN_sigma]
  · simp only [letterBraid, transport, if_true]
    rw [heckeRep_braidGen_val, heckeActionN_sigma]

/-- The representation of a word's braid is the multiplicative integral of the word. -/
theorem heckeActionN_wordBraid (hqi : q * qi = 1) (ℓs : List (Fin m × Bool)) :
    heckeActionN q qi hqi
        ((heckeRep (coxA m) hqi coxA_symm (wordBraid ℓs) : (BalancedHecke (coxA m) q)ˣ)
          : BalancedHecke (coxA m) q)
      = hol q qi ℓs := by
  induction ℓs with
  | nil => simp [wordBraid, hol]
  | cons ℓ ℓs ih =>
    have hw : wordBraid (ℓ :: ℓs) = letterBraid ℓ * wordBraid ℓs := by
      simp [wordBraid]
    rw [hw, map_mul, Units.val_mul, map_mul, ih, heckeActionN_letter]
    simp [hol]

/-- **Mass identity, Markov form.** The normalised Markov trace of the braid a word spells
is the site-weighted trace of the word's multiplicative integral:
`tr_M(β_ℓ) = wi^{m+1} · Tr(K^{⊗(m+1)} · Hol(ℓ))`. -/
theorem braidTrace_wordBraid (hqi : q * qi = 1) (w : Fin 2 → R) (wi : R)
    (ℓs : List (Fin m × Bool)) :
    braidTrace q qi hqi w wi (wordBraid ℓs)
      = wi ^ (m + 1) * Matrix.trace (siteWeight w * hol q qi ℓs) := by
  rw [braidTrace, markovTr, qTrace, heckeActionN_wordBraid]

/-- The signed letter count of a word. -/
def signedLength : List (Fin m × Bool) → ℤ
  | [] => 0
  | ℓ :: ℓs => (if ℓ.2 then 1 else -1) + signedLength ℓs

/-- The writhe of the braid a word spells is the word's signed letter count. -/
theorem braidWritheZ_wordBraid (ℓs : List (Fin m × Bool)) :
    braidWritheZ (wordBraid ℓs) = signedLength ℓs := by
  induction ℓs with
  | nil => simp [wordBraid, signedLength, braidWritheZ]
  | cons ℓ ℓs ih =>
    have hw : wordBraid (ℓ :: ℓs) = letterBraid ℓ * wordBraid ℓs := by
      simp [wordBraid]
    rw [hw, braidWritheZ_mul, ih, signedLength]
    rcases ℓ with ⟨a, _ | _⟩
    · simp [letterBraid, braidWritheZ_inv, braidWritheZ_gen]
    · simp [letterBraid, braidWritheZ_gen]

/-- **The framing-corrected trace** of a word's braid is the same functional of its
multiplicative integral, times the strand and writhe factors. -/
theorem jonesFn_wordBraid (wi : R) (hqi : q * qi = 1) (w : Fin 2 → R)
    (hw : (1 + q ^ 2) * wi = 1) (ℓs : List (Fin m × Bool)) :
    jonesFn q qi wi hqi w hw (wordBraid ℓs)
      = ((strandFactor q qi wi hqi hw ^ (m + 1) : Rˣ) : R)
          * ((writheFactor q qi hqi ^ signedLength ℓs : Rˣ) : R)
          * (wi ^ (m + 1) * Matrix.trace (siteWeight w * hol q qi ℓs)) := by
  rw [jonesFn, braidWritheZ_wordBraid, braidTrace_wordBraid]

/-! ## Option 3 — Temperley–Lieb state-sum expansion of the holonomy and Markov trace on `B_{m+1}`

Each crossing transport `T(a, ε)` decomposes over a bare `CommRing R` into the identity channel
and the Temperley–Lieb cup-cap generator `e_a = q • 1 − Ř_a`:

    T(a, +) = q • 1 − e_a,        T(a, −) = qi • 1 − e_a.

Expanding the ordered holonomy product `hol q qi ℓs` over all binary states
`s : Fin ℓs.length → Bool` (`false` = identity channel, `true` = Temperley–Lieb `e_a` channel)
expresses both `hol q qi ℓs` and its normalised Markov trace `braidTrace_wordBraid` as an exact
state sum over Temperley–Lieb words, with the `s ≡ false` leading state recovering the naive
per-crossing scalar product `∏_{ℓ ∈ ℓs} c(ℓ)`. -/

/-- The Temperley–Lieb generator `e_a = q • 1 − Ř_a` at strand `a` on `V^{⊗(m+1)}`, defined
over an arbitrary `CommRing R`. -/
def tlProjector (a : Fin m) : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R :=
  q • 1 - strandBraid q qi a

/-- **The Temperley–Lieb loop relation over a general `CommRing R`.**
    `e_a² = (q + q⁻¹) e_a`, proved from `isHeckeGenerator_braidAt` and `q * qi = 1` alone. -/
theorem tlProjector_sq (hqi : q * qi = 1) (a : Fin m) :
    tlProjector q qi a * tlProjector q qi a = (q + qi) • tlProjector q qi a := by
  have hne : a.castSucc ≠ a.succ := by simp [Fin.ext_iff]
  have hgen : strandBraid q qi a * strandBraid q qi a
      = (q - qi) • strandBraid q qi a + 1 := by
    have h := (isHeckeGenerator_braidAt (R := R) q qi hne hqi).eq
    rw [Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul] at h
    exact h
  simp only [tlProjector, sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, hgen]
  ext i j
  simp only [Matrix.sub_apply, Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply, smul_eq_mul]
  linear_combination -(if i = j then (1 : R) else 0) * hqi

/-- The identity-channel scalar of a signed crossing letter: `q` for a positive crossing,
`qi` (`= q⁻¹`) for a negative crossing. -/
def letterLeadScalar (ℓ : Fin m × Bool) : R :=
  if ℓ.2 then q else qi

/-- **Universal two-channel decomposition of a crossing transport.**
    Both positive and negative crossings satisfy `T(a, ε) = c(ε) • 1 − e_a`. -/
theorem transport_eq_lead_sub_tlProjector (ℓ : Fin m × Bool) :
    transport q qi ℓ = letterLeadScalar q qi ℓ • 1 - tlProjector q qi ℓ.1 := by
  rcases ℓ with ⟨a, _ | _⟩
  · simp only [transport, letterLeadScalar, tlProjector, Bool.false_eq_true, if_false,
      negCrossing, Algebra.algebraMap_eq_smul_one]
    ext i j
    simp only [Matrix.sub_apply, Matrix.smul_apply, Matrix.one_apply, smul_eq_mul]
    ring
  · simp only [transport, letterLeadScalar, tlProjector, if_true, sub_sub_cancel]

/-- Ordered product along a word `w : List α` in a binary state `s : Fin w.length → Bool`,
choosing `f a false` or `f a true` at each position. -/
def stateProd {α A : Type*} [Semiring A] (f : α → Bool → A) :
    (w : List α) → (Fin w.length → Bool) → A
  | [], _ => 1
  | a :: w, s => f a (s (0 : Fin (w.length + 1))) * stateProd f w (fun i => s i.succ)

/-- Splitting a finite sum over `Fin (n + 1) → Bool` by the head bit `b : Bool`. -/
theorem sum_fin_succ_bool {M : Type*} [AddCommMonoid M] {n : ℕ} (g : (Fin (n + 1) → Bool) → M) :
    (∑ s : Fin (n + 1) → Bool, g s) =
      ∑ b : Bool, ∑ s : Fin n → Bool, g (Fin.cons b s) := by
  rw [← (Fin.consEquiv (fun _ : Fin (n + 1) => Bool)).sum_comp, Fintype.sum_prod_type]
  rfl

/-- **Non-commutative binary state-sum expansion.**
    In any semiring `A`, the ordered product of binary sums `∏ (f a false + f a true)` along a
    word `w` equals the sum over all states `s : Fin w.length → Bool` of `stateProd f w s`. -/
theorem prod_map_add_eq_sum_stateProd {α A : Type*} [Semiring A]
    (f : α → Bool → A) (w : List α) :
    (w.map (fun a => f a false + f a true)).prod =
      ∑ s : Fin w.length → Bool, stateProd f w s := by
  induction w with
  | nil => simp [stateProd]
  | cons a w ih =>
    simp only [List.map_cons, List.prod_cons]
    rw [ih, show (∑ s : Fin (a :: w).length → Bool, stateProd f (a :: w) s) =
        ∑ b : Bool, ∑ s : Fin w.length → Bool, stateProd f (a :: w) (Fin.cons b s) from
      sum_fin_succ_bool _]
    simp only [stateProd, Fin.cons_zero, Fin.cons_succ]
    simp only [← Finset.mul_sum, Fintype.sum_bool]
    rw [add_mul, add_comm]

/-- Evaluating `stateProd` at the all-`false` state recovers the ordered product of the
`false`-channel factors. -/
theorem stateProd_const_false {α A : Type*} [Semiring A] (f : α → Bool → A) (w : List α) :
    stateProd f w (fun _ => false) = (w.map (fun a => f a false)).prod := by
  induction w with
  | nil => simp [stateProd]
  | cons a w ih => simp [stateProd, ih]

/-- Scalar factors pull out of `stateProd` in any `R`-algebra `A`. -/
theorem stateProd_smul_eq {α A : Type*} [Ring A] [Algebra R A]
    (c : α → Bool → R) (M : α → Bool → A) (w : List α) (s : Fin w.length → Bool) :
    stateProd (fun a b => c a b • M a b) w s = stateProd c w s • stateProd M w s := by
  induction w with
  | nil => simp [stateProd]
  | cons a w ih =>
    simp only [stateProd]
    rw [ih, smul_mul_smul_comm]

/-- The scalar weight of a Temperley–Lieb state `s` on a braid word `ℓs`: the product of
`letterLeadScalar q qi ℓ` at identity-smoothed crossings (`s i = false`) and `-1` at
cup-cap-smoothed crossings (`s i = true`). -/
def tlStateWeight (ℓs : List (Fin m × Bool)) (s : Fin ℓs.length → Bool) : R :=
  stateProd (fun ℓ b => if b then -1 else letterLeadScalar q qi ℓ) ℓs s

/-- The Temperley–Lieb word operator of a state `s` on `ℓs`: the ordered product of `tlProjector`
at crossings with `s i = true` (and `1` at crossings with `s i = false`). -/
def tlStateMatrix (ℓs : List (Fin m × Bool)) (s : Fin ℓs.length → Bool) :
    Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R :=
  stateProd (fun ℓ b => if b then tlProjector q qi ℓ.1 else 1) ℓs s

/-- Single-crossing state summand: `c(ℓ) • 1` for `b = false`, `-e_a` for `b = true`. -/
def tlStepFactor (ℓ : Fin m × Bool) (b : Bool) :
    Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R :=
  (if b then (-1 : R) else letterLeadScalar q qi ℓ) •
    (if b then tlProjector q qi ℓ.1 else 1)

/-- **Bridge between Option 1 and Option 3 (algebra level).**
    The non-abelian multiplicative integral `hol q qi ℓs` of a braid word expands as the
    Temperley–Lieb state sum over `s : Fin ℓs.length → Bool`. -/
theorem hol_eq_tlStateSum (ℓs : List (Fin m × Bool)) :
    hol q qi ℓs =
      ∑ s : Fin ℓs.length → Bool, tlStateWeight q qi ℓs s • tlStateMatrix q qi ℓs s := by
  have hmap : ℓs.map (transport q qi) =
      ℓs.map (fun ℓ => tlStepFactor q qi ℓ false + tlStepFactor q qi ℓ true) := by
    refine List.map_congr_left fun ℓ _ => ?_
    simp only [tlStepFactor, Bool.false_eq_true, if_false, if_true, neg_one_smul,
      sub_eq_add_neg, transport_eq_lead_sub_tlProjector]
  unfold hol
  rw [hmap, prod_map_add_eq_sum_stateProd (tlStepFactor q qi) ℓs]
  refine Finset.sum_congr rfl fun s _ => ?_
  exact stateProd_smul_eq
    (fun ℓ b => if b then -1 else letterLeadScalar q qi ℓ)
    (fun ℓ b => if b then tlProjector q qi ℓ.1 else 1) ℓs s

/-- **Mass identity on `B_{m+1}`, Temperley–Lieb state-sum form (Option 3).**
    The normalised Markov trace of `wordBraid ℓs` equals the state sum of the factorised scalar
    weights `tlStateWeight q qi ℓs s` times the normalised quantum traces of the Temperley–Lieb
    word matrices `tlStateMatrix q qi ℓs s`. -/
theorem braidTrace_wordBraid_eq_tlStateSum (hqi : q * qi = 1) (w : Fin 2 → R) (wi : R)
    (ℓs : List (Fin m × Bool)) :
    braidTrace q qi hqi w wi (wordBraid ℓs) =
      ∑ s : Fin ℓs.length → Bool,
        tlStateWeight q qi ℓs s *
          (wi ^ (m + 1) * Matrix.trace (siteWeight w * tlStateMatrix q qi ℓs s)) := by
  rw [braidTrace_wordBraid, hol_eq_tlStateSum, Finset.mul_sum, Matrix.trace_sum, Finset.mul_sum]
  refine Finset.sum_congr rfl fun s _ => ?_
  rw [mul_smul_comm, Matrix.trace_smul, smul_eq_mul]
  ring

/-- At the all-`false` (identity-smoothing) state, the state weight is the naive per-crossing
scalar product `∏_{ℓ ∈ ℓs} letterLeadScalar q qi ℓ`. -/
theorem tlStateWeight_const_false (ℓs : List (Fin m × Bool)) :
    tlStateWeight q qi ℓs (fun _ => false) = (ℓs.map (letterLeadScalar q qi)).prod := by
  simpa [tlStateWeight] using
    stateProd_const_false (fun ℓ b => if b then -1 else letterLeadScalar q qi ℓ) ℓs

/-- At the all-`false` (identity-smoothing) state, the Temperley–Lieb word operator is `1`. -/
theorem tlStateMatrix_const_false (ℓs : List (Fin m × Bool)) :
    tlStateMatrix q qi ℓs (fun _ => false) = 1 := by
  rw [tlStateMatrix, stateProd_const_false]
  induction ℓs with
  | nil => rfl
  | cons _ _ ih =>
    simp only [List.map_cons, List.prod_cons, Bool.false_eq_true, ↓reduceIte, one_mul]
    exact ih

/-- **Leading scalar product + Temperley–Lieb loop corrections.**
    When the site weight is normalised (`(∑ k, w k) * wi = 1`), the `s ≡ false` state contributes
    the naive per-crossing scalar product `(ℓs.map (letterLeadScalar q qi)).prod`, and the
    remaining states `s ≠ (fun _ => false)` collect all Temperley–Lieb cup-cap contractions. -/
theorem braidTrace_wordBraid_eq_leadProd_add_tlStates (hqi : q * qi = 1) (w : Fin 2 → R) (wi : R)
    (hw : (∑ k, w k) * wi = 1) (ℓs : List (Fin m × Bool)) :
    braidTrace q qi hqi w wi (wordBraid ℓs) =
      (ℓs.map (letterLeadScalar q qi)).prod +
        ∑ s ∈ Finset.univ.erase (fun _ : Fin ℓs.length => false),
          tlStateWeight q qi ℓs s *
            (wi ^ (m + 1) * Matrix.trace (siteWeight w * tlStateMatrix q qi ℓs s)) := by
  classical
  rw [braidTrace_wordBraid_eq_tlStateSum q qi hqi w wi ℓs,
    ← Finset.add_sum_erase _ _ (Finset.mem_univ (fun _ : Fin ℓs.length => false)),
    tlStateWeight_const_false, tlStateMatrix_const_false, mul_one]
  have h1 : wi ^ (m + 1) * Matrix.trace (siteWeight (n := m + 1) w) = 1 := by
    have htr := markovTr_one q qi (m := m) hqi w wi hw
    simpa [markovTr, qTrace] using htr
  rw [h1, mul_one]

/-- **Framing-corrected trace in Temperley–Lieb state-sum form.** -/
theorem jonesFn_wordBraid_eq_tlStateSum (wi : R) (hqi : q * qi = 1) (w : Fin 2 → R)
    (hw : (1 + q ^ 2) * wi = 1) (ℓs : List (Fin m × Bool)) :
    jonesFn q qi wi hqi w hw (wordBraid ℓs)
      = ((strandFactor q qi wi hqi hw ^ (m + 1) : Rˣ) : R)
          * ((writheFactor q qi hqi ^ signedLength ℓs : Rˣ) : R)
          * (∑ s : Fin ℓs.length → Bool,
              tlStateWeight q qi ℓs s *
                (wi ^ (m + 1) * Matrix.trace (siteWeight w * tlStateMatrix q qi ℓs s))) := by
  rw [jonesFn, braidWritheZ_wordBraid, braidTrace_wordBraid_eq_tlStateSum]

end QOU.Torsion.MassTraceMarkov

import QOU.IwahoriHecke.BraidTower

/-!
# The negative peel

`MarkovPeel` peeled a **positive** crossing: `tr(ι(x)·σ) = z·tr(x)`, with `z = q³` at the weight
the peel itself forces. Markov move II comes in two flavours, and the negative one is not the
same statement — `σ` and `σ⁻¹` do not peel to the same scalar. This file computes the other one.

## The computation is a subtraction

No new sum manipulation is needed. The skein relation gives `σ⁻¹ = σ − (q − qi)` on the nose
(`negCrossing`), so the peel of `σ⁻¹` is the peel of `σ` minus `(q − qi)` times the peel of `1`.
The only new ingredient is that last piece:

* **`trace_extendSite`** — `tr_w(X ⊗ 1) = (∑ₖ w k) · tr_w(X)`. Adding an inert site multiplies
  the weighted trace by the total weight, which is the same fact `qTrace_one` records at `X = 1`.

So `z⁻ = z − (q − qi)·(∑ₖ w k)`, and at the forced weight `w = (1, q²)` that is

    q³ − (q − qi)(1 + q²) = q³ − (q³ − qi) = qi,

i.e. **`z⁻ = q⁻¹`** (`negPeel_scalar_physical`) against `z⁺ = q³`. The asymmetry is real and it is
what a framing correction has to absorb.

## Why the two scalars matter

`z⁺ · z⁻ = q³ · qi = q²`, which is not `1`. So no rescaling by a power of the writhe alone can
make both moves invariant — the framing correction needs a *strand-count* factor as well. That
is the subject of `QOU.IwahoriHecke.JonesNormalisation`, where both constants are pinned by
exactly these two numbers.

-- Ref: [jones1987] Hecke algebra representations of braid groups and link polynomials
-- Ref: [leitner2026] bean qou-k4oq
-/

namespace QOU.IwahoriHecke.NegativePeel

open QOU.MathlibExt.IwahoriHecke QOU.MathlibExt.SkeinRelation
open QOU.IwahoriHecke.Balanced QOU.IwahoriHecke.TensorEmbed
open QOU.IwahoriHecke.QuantumTrace QOU.IwahoriHecke.MarkovPeel
open QOU.IwahoriHecke.BraidGroup QOU.IwahoriHecke.BraidTower

variable {R : Type*} [CommRing R] (q qi : R) {m : ℕ}

/-! ## Splitting a sum over states along the last site -/

/-- Summing over states of `V^{⊗(m+2)}` is summing over states of `V^{⊗(m+1)}` and the value at
the new site. -/
theorem sum_lastSplit (F : (Fin (m + 2) → Fin 2) → R) :
    (∑ a : Fin (m + 2) → Fin 2, F a)
      = ∑ a' : Fin (m + 1) → Fin 2, ∑ t : Fin 2, F (lastSplit m (t, a')) := by
  rw [← Equiv.sum_comp (lastSplit m) F, Fintype.sum_prod_type, Finset.sum_comm]

/-! ## An inert extra site multiplies the trace by the total weight -/

/-- **`tr_w(X ⊗ 1) = (∑ₖ w k) · tr_w(X)`.** The new site contributes its whole weight and
nothing else, which is `qTrace_one`'s `(∑ₖ w k)^{m+1}` one factor at a time. -/
theorem trace_extendSite (w : Fin 2 → R)
    (X : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R) :
    Matrix.trace (siteWeight (n := m + 2) w * extendSiteHom X)
      = (∑ k, w k) * Matrix.trace (siteWeight (n := m + 1) w * X) := by
  classical
  have hdiag : ∀ a : Fin (m + 2) → Fin 2,
      (extendSiteHom (R := R) (m := m) X) a a
        = X (fun k => a k.castSucc) (fun k => a k.castSucc) := by
    intro a
    rw [extendSiteHom_apply, if_pos rfl, one_mul]
  rw [trace_siteWeight_mul, trace_siteWeight_mul, Finset.mul_sum]
  simp only [hdiag]
  rw [sum_lastSplit]
  refine Finset.sum_congr rfl (fun a' _ => ?_)
  have hcs : ∀ (t : Fin 2) (k : Fin (m + 1)), lastSplit m (t, a') k.castSucc = a' k := by
    intro t k; simp [lastSplit]
  have hlst : ∀ t : Fin 2, lastSplit m (t, a') (Fin.last (m + 1)) = t := by
    intro t; simp [lastSplit]
  have hprod : ∀ t : Fin 2, (∏ k : Fin (m + 2), w (lastSplit m (t, a') k))
      = (∏ k : Fin (m + 1), w (a' k)) * w t := by
    intro t
    rw [Fin.prod_univ_castSucc]
    congr 1
    · exact Finset.prod_congr rfl (fun k _ => by rw [hcs t k])
    · rw [hlst t]
  have hstep : ∀ t : Fin 2,
      (∏ k : Fin (m + 2), w (lastSplit m (t, a') k))
          * X (fun k => lastSplit m (t, a') k.castSucc)
              (fun k => lastSplit m (t, a') k.castSucc)
        = w t * ((∏ k : Fin (m + 1), w (a' k)) * X a' a') := by
    intro t
    have hfun : (fun k => lastSplit m (t, a') k.castSucc) = a' := funext (fun k => hcs t k)
    rw [hprod t, hfun]
    ring
  refine (Finset.sum_congr rfl (fun t _ => hstep t)).trans ?_
  rw [← Finset.sum_mul]

/-! ## The negative peel -/

/-- **The peel of a negative crossing.** The skein relation turns it into the positive peel minus
`(q − qi)` times the inert-site factor. -/
theorem trace_peel_neg (w : Fin 2 → R) (z : R)
    (hP : ∀ u : Fin 2, (∑ t : Fin 2, w t * RMatrix.rCheck q qi (u, t) (u, t)) = z)
    (X : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R) :
    Matrix.trace (siteWeight (n := m + 2) w
        * (extendSiteHom X * negCrossing q qi (strandBraid q qi (Fin.last m))))
      = (z - (q - qi) * (∑ k, w k)) * Matrix.trace (siteWeight (n := m + 1) w * X) := by
  have hsplit : extendSiteHom (R := R) (m := m) X
        * negCrossing q qi (strandBraid q qi (Fin.last m))
      = extendSiteHom X * strandBraid q qi (Fin.last m)
        - algebraMap R (Matrix (Fin (m + 2) → Fin 2) (Fin (m + 2) → Fin 2) R) (q - qi)
          * extendSiteHom X := by
    rw [negCrossing, mul_sub]
    congr 1
    exact (Algebra.commutes _ _).symm
  have hscal : siteWeight (n := m + 2) w
        * (algebraMap R (Matrix (Fin (m + 2) → Fin 2) (Fin (m + 2) → Fin 2) R) (q - qi)
            * extendSiteHom X)
      = (q - qi) • (siteWeight (n := m + 2) w * extendSiteHom X) := by
    rw [Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul, mul_smul_comm]
  rw [hsplit, mul_sub, Matrix.trace_sub, trace_peel q qi w z hP, hscal, Matrix.trace_smul,
    trace_extendSite, smul_eq_mul]
  ring

/-- **At the forced weight the negative peel scalar is `qi = q⁻¹`.**

`q³ − (q − qi)(1 + q²) = q³ − (q³ − qi) = qi`, using `q·qi = 1` once. Against the positive
scalar `q³`, so the two differ by `q⁴` — the asymmetry a framing correction must absorb. -/
theorem negPeel_scalar_physical (hqi : q * qi = 1) (w : Fin 2 → R)
    (h0 : w 0 = 1) (h1 : w 1 = q ^ 2) :
    q ^ 3 - (q - qi) * (∑ k, w k) = qi := by
  have hsum : (∑ k, w k) = 1 + q ^ 2 := by rw [Fin.sum_univ_two, h0, h1]
  rw [hsum]
  linear_combination q * hqi

/-! ## Up the tower: the algebra and the braid group -/

/-- The negative peel in `H_{m+2}(q)`, for the normalised trace. -/
theorem markovTr_peel_neg (hqi : q * qi = 1) (w : Fin 2 → R) (wi : R) (z : R)
    (hP : ∀ u : Fin 2, (∑ t : Fin 2, w t * RMatrix.rCheck q qi (u, t) (u, t)) = z)
    (x : BalancedHecke (coxA m) q) :
    QOU.IwahoriHecke.MarkovNormalized.markovTr q qi (m := m + 1) hqi w wi
        (tower q qi hqi x * negCrossing q qi (sigma (coxA (m + 1)) q qi (Fin.last m)))
      = ((z - (q - qi) * (∑ k, w k)) * wi)
        * QOU.IwahoriHecke.MarkovNormalized.markovTr q qi (m := m) hqi w wi x := by
  have hact : heckeActionN q qi (m := m + 1) hqi
      (negCrossing q qi (sigma (coxA (m + 1)) q qi (Fin.last m)))
      = negCrossing q qi (strandBraid q qi (Fin.last m)) := by
    rw [negCrossing, negCrossing, map_sub, AlgHom.commutes, heckeActionN_sigma]
  rw [QOU.IwahoriHecke.MarkovNormalized.markovTr,
    QOU.IwahoriHecke.MarkovNormalized.markovTr, qTrace, qTrace, map_mul, heckeActionN_tower,
    hact, trace_peel_neg q qi w z hP, pow_succ]
  ring

/-- **Markov move II⁻, on braids.** -/
theorem braidTrace_peel_neg (hqi : q * qi = 1) (w : Fin 2 → R) (wi : R) (z : R)
    (hP : ∀ u : Fin 2, (∑ t : Fin 2, w t * RMatrix.rCheck q qi (u, t) (u, t)) = z)
    (β : BraidGroupN m) :
    braidTrace q qi hqi w wi
        (braidTower β * (braidGen (coxA (m + 1)) (Fin.last m))⁻¹)
      = ((z - (q - qi) * (∑ k, w k)) * wi) * braidTrace q qi hqi w wi β := by
  have hval : ((heckeRep (coxA (m + 1)) hqi coxA_symm
        (braidGen (coxA (m + 1)) (Fin.last m))⁻¹
          : (BalancedHecke (coxA (m + 1)) q)ˣ) : BalancedHecke (coxA (m + 1)) q)
      = negCrossing q qi (sigma (coxA (m + 1)) q qi (Fin.last m)) := by
    rw [map_inv, heckeRep_braidGen]
    rfl
  rw [braidTrace, braidTrace, map_mul, Units.val_mul, heckeRep_braidTower q qi hqi, hval,
    markovTr_peel_neg q qi hqi w wi z hP]

/-- **Both scalars at the forced weight.** `z⁺ = q³` and `z⁻ = qi`, so `z⁺·z⁻ = q²` — **not**
`1`. That is exactly why a writhe-only framing correction cannot make both moves invariant, and
why `JonesNormalisation` needs a strand-count factor too. -/
theorem peel_scalars_physical (hqi : q * qi = 1) (w : Fin 2 → R)
    (h0 : w 0 = 1) (h1 : w 1 = q ^ 2) :
    (q ^ 3) * (q ^ 3 - (q - qi) * (∑ k, w k)) = q ^ 2 := by
  rw [negPeel_scalar_physical q qi hqi w h0 h1]
  linear_combination (q ^ 2) * hqi

end QOU.IwahoriHecke.NegativePeel

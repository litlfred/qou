import QOU.IwahoriHecke.MarkovPeel

/-!
# The normalised Markov trace, and where convention D's `z` comes from

`QTraceCyclic` gave Markov move I (cyclicity) and `MarkovPeel` gave move II (the peel), both
for the *unnormalised* site-weighted trace `tr_w`. What is missing for a Markov trace proper is
the third axiom, **normalisation** `tr(1) = 1` — `qTrace_one` is `(∑ₖ w k)^{m+1}`, not `1`.

This file divides it out, and the peel scalar moves with it. That is the whole content, and it
is short; the reason to write it down is what the moved scalar turns out to be.

## Division without a field

`R` is a bare `CommRing` throughout this arc, so the inverse of the total weight is carried as a
separate scalar with a witnessing equation — exactly the idiom `q * qi = 1` already uses for
`q⁻¹`. So `wi` with `(∑ₖ w k) * wi = 1`, and

    tr̂(x) := wi^{m+1} · tr_w(x).

`markovTr_one`, `markovTr_mul_comm` and `markovTr_peel` are then the three Markov axioms:
normalised, cyclic, and peeling with scalar `z · wi`.

## 🟧 The scalar is convention D's `z`

Feeding in what `MarkovPeel` forces — the weight must be `w = (1, q²)` and the unnormalised peel
scalar is then `z = q³` — the total weight is `1 + q²`, so the **normalised** peel scalar is

    ẑ = q³ · (1 + q²)⁻¹ = q³ / (q² + 1),

which is the repo's **convention D** Markov parameter verbatim
([`tools/pyhecke/python/pyhecke/gram.py`](../../../../tools/pyhecke/python/pyhecke/gram.py),
`z_mp`: *"z = q³/(q² + 1) — convention D"*), and not convention C's `√q/(q+1)`. It is stated here
division-free as `markovParam_eq_conventionD` — `ẑ · (q² + 1) = q³` — with
`markovParam_unique` showing that equation pins `ẑ` whenever `1 + q²` is invertible.

Nothing along the way chose it. The weight was forced by the peel existing at all
(`peel_forces_physical_weight`), the unnormalised scalar was forced by the same two equations,
and the normalisation is division by `tr_w(1)`. Convention D is what the R-matrix does.

## 🛑 Two things this does not establish

**It is a match of algebraic form in the §7a balanced parameter, not a cross-file
identification.** `gram.py`'s `z` is evaluated at the substrate `q₀`, and the parameter it is
written in is the §7a one (AGENTS.md §7a fixes `(σ_i − q)(σ_i + q^{-1}) = 0`, which is
`IsHeckeGenerator q qi` here), so the reading is the natural one — but proving that the
*numerical* `z` of the compute layer is this object needs the two trace conventions identified,
which is not done here and is not attempted.

**This is still not a link invariant.** A Markov trace gives one only through the braid group:
`B_n → H_n(q)`, Markov's theorem, and closure-invariance. None of that is here, and
`QOU.IwahoriHecke.MarkovTrace.markovTrace` remains `noncomputable opaque`.

-- Ref: [jones1987] Hecke algebra representations of braid groups and link polynomials
-- Ref: [leitner2026] bean qou-k4oq; AGENTS.md §"q₀ anchor convention" R1 (convention D canonical)
-/

namespace QOU.IwahoriHecke.MarkovNormalized

open QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix QOU.IwahoriHecke.QuantumTrace
open QOU.IwahoriHecke.MarkovPeel

variable {R : Type*} [CommRing R] (q qi : R) {m : ℕ}

/-- **The normalised trace** `tr̂(x) = wi^{m+1} · tr_w(x)`, where `wi` is the inverse of the
total weight `∑ₖ w k`, carried explicitly rather than as a field division. -/
noncomputable def markovTr (hqi : q * qi = 1) (w : Fin 2 → R) (wi : R)
    (x : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) : R :=
  wi ^ (m + 1) * qTrace q qi hqi w x

/-- **Axiom 1 — normalisation.** `tr̂(1) = 1`. -/
theorem markovTr_one (hqi : q * qi = 1) (w : Fin 2 → R) (wi : R)
    (hw : (∑ k, w k) * wi = 1) :
    markovTr q qi (m := m) hqi w wi 1 = 1 := by
  rw [markovTr, qTrace_one, ← mul_pow, mul_comm wi, hw, one_pow]

/-- **Axiom 2 — cyclicity.** Inherited from `qTrace_mul_comm`: the normalisation is a scalar. -/
theorem markovTr_mul_comm (hqi : q * qi = 1) (w : Fin 2 → R) (wi : R)
    (x y : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) :
    markovTr q qi hqi w wi (x * y) = markovTr q qi hqi w wi (y * x) := by
  rw [markovTr, markovTr, qTrace_mul_comm]

/-- **Axiom 3 — the peel, normalised.** The scalar picks up one factor of `wi`: if the
unnormalised peel scalar is `z`, the normalised one is `z · wi`. -/
theorem markovTr_peel (hqi : q * qi = 1) (w : Fin 2 → R) (wi : R) (z : R)
    (hP : ∀ u : Fin 2, (∑ t : Fin 2, w t * rCheck q qi (u, t) (u, t)) = z)
    (x : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) :
    markovTr q qi (m := m + 1) hqi w wi
        (tower q qi hqi x * QOU.IwahoriHecke.Balanced.sigma (coxA (m + 1)) q qi (Fin.last m))
      = (z * wi) * markovTr q qi (m := m) hqi w wi x := by
  rw [markovTr, markovTr, qTrace_peel q qi hqi w z hP, pow_succ]
  ring

/-! ## The scalar, at the weight the peel forces -/

/-- **The normalised peel scalar is `q³·(1+q²)⁻¹`.** Stated division-free: it is the unique
solution of `ẑ · (q² + 1) = q³`, which is convention D's `z = q³/(q² + 1)`. -/
theorem markovParam_eq_conventionD (wi : R) (hw : ((1 : R) + q ^ 2) * wi = 1) :
    (q ^ 3 * wi) * (q ^ 2 + 1) = q ^ 3 := by
  linear_combination q ^ 3 * hw

/-- That equation pins the scalar: no other `z` satisfies it once `1 + q²` is invertible. So
"the Markov parameter is `q³/(q²+1)`" is a determination, not a choice of representative. -/
theorem markovParam_unique (wi : R) (hw : ((1 : R) + q ^ 2) * wi = 1) (z : R)
    (hz : z * (q ^ 2 + 1) = q ^ 3) : z = q ^ 3 * wi := by
  linear_combination wi * hz - z * hw

/-- **The whole statement in one place.** At the weight the peel forces — `w = (1, q²)`, whose
total is `1 + q²` — the normalised trace is a Markov trace with parameter `q³ · (1+q²)⁻¹`, i.e.
convention D's `z = q³/(q²+1)`.

The three conclusions are the three axioms; the fourth is the parameter's characterisation. -/
theorem markovTr_physical (hqi : q * qi = 1) (w : Fin 2 → R) (wi : R)
    (h0 : w 0 = 1) (h1 : w 1 = q ^ 2) (hw : (∑ k, w k) * wi = 1) :
    markovTr q qi (m := m) hqi w wi 1 = 1
      ∧ (∀ x y : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q,
          markovTr q qi hqi w wi (x * y) = markovTr q qi hqi w wi (y * x))
      ∧ (∀ x : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q,
          markovTr q qi (m := m + 1) hqi w wi
              (tower q qi hqi x
                * QOU.IwahoriHecke.Balanced.sigma (coxA (m + 1)) q qi (Fin.last m))
            = (q ^ 3 * wi) * markovTr q qi (m := m) hqi w wi x)
      ∧ (q ^ 3 * wi) * (q ^ 2 + 1) = q ^ 3 := by
  have hsum : (∑ k, w k) = 1 + q ^ 2 := by
    rw [Fin.sum_univ_two, h0, h1]
  refine ⟨markovTr_one q qi hqi w wi hw, markovTr_mul_comm q qi hqi w wi,
    fun x => markovTr_peel q qi hqi w wi (q ^ 3)
      (peel_scalar_of_physical q qi hqi w h0 h1) x,
    markovParam_eq_conventionD q wi (by rw [← hsum]; exact hw)⟩

end QOU.IwahoriHecke.MarkovNormalized

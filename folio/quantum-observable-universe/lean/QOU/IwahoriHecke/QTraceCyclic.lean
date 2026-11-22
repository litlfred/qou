import QOU.IwahoriHecke.QuantumTrace

/-!
# Full cyclicity of the site-weighted trace

`QOU.IwahoriHecke.QuantumTrace` proved cyclicity of `tr_w` only against a **generator** —
`tr_w(σ_a · y) = tr_w(y · σ_a)` — and said plainly that the general statement needed the
image of the action to lie in the centralizer of the site weight `W`, "an induction over the
algebra rather than over its generators". This file supplies exactly that, and with it the
general statement

> **`qTrace_mul_comm`** — `tr_w(x y) = tr_w(y x)` for *arbitrary* `x`, `y ∈ H_{m+1}(q)`.

so `tr_w` is a trace on the algebra, not merely a functional that happens to be cyclic on
generators.

## The mechanism, and why it is not an induction

The naive route is a `RingQuot` induction over `x`. That is not needed. `Ř` commutes with
`W` (`braidAt_comm_siteWeight`, for **every** weight), so the whole image lands in the
`R`-subalgebra `Subalgebra.centralizer R {W}` — and a subalgebra is closed under the
operations, so "the image is inside it" is a statement about a *lift*, not about a
traversal of elements:

* `heckeActionCentral` re-runs `liftBalanced` with the **subalgebra** as target. The three
  obligations are the same three, pulled back along the injective `Subalgebra.val`;
* `val_comp_heckeActionCentral` says composing back with `val` returns `heckeActionN`, by
  `hom_ext_sigma` — two algebra maps agreeing on the `σ_a`;
* so `heckeActionN x` is the image of a subalgebra element for **every** `x`
  (`heckeActionN_mem_weightCentralizer`), hence commutes with `W`.

The braid-relation obligation is not re-proved: `strandBraid_altProd` reads it off
`heckeActionN` itself, by pushing `Balanced.sigma_braid` through the map with
`map_altProd`. Nothing about `Fin` arithmetic is repeated.

## 🛑 Scope

This is cyclicity, and cyclicity alone. It is **not** the Markov property: a Markov trace
must additionally satisfy the *peel* `tr(x σ_n) = z · tr(x)` relating the trace on
`H_{n+1}(q)` to the one on `H_n(q)`, which is a statement about the tower and is not here.
See `QOU.IwahoriHecke.MarkovPeel` for that half. Normalisation (`tr_M(1) = 1`) is likewise
absent — `qTrace_one` gives `(∑ₖ w k)^{m+1}`, which is not `1`.

-- Ref: [jones1987] Hecke algebra representations of braid groups and link polynomials
-- Ref: [leitner2026] bean qou-k4oq
-/

namespace QOU.IwahoriHecke.QuantumTrace

open QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix
open QOU.MathlibExt.SkeinRelation QOU.MathlibExt.IwahoriHecke

variable {R : Type*} [CommRing R] (q qi : R) {m : ℕ}

/-! ## Pulling the Hecke relations back along an injection -/

/-- **`IsHeckeGenerator` descends along an injective algebra map.** The quadratic relation is
an equation between algebra expressions, so an injective algebra map reflects it. This is
what lets the `liftBalanced` obligations be discharged inside a subalgebra without redoing
any of the matrix computation. -/
theorem isHeckeGenerator_of_injective {A B : Type*} [Ring A] [Ring B] [Algebra R A]
    [Algebra R B] (φ : A →ₐ[R] B) (hinj : Function.Injective φ) {x : A}
    (h : IsHeckeGenerator q qi (φ x)) : IsHeckeGenerator q qi x := by
  have hx : x * x = algebraMap R A (q - qi) * x + 1 := by
    refine hinj ?_
    rw [map_mul, h.eq, map_add, map_mul, map_one, AlgHom.commutes]
  exact hx

/-! ## The centralizer of the site weight -/

/-- The centralizer of the site weight `W` inside `End(V^{⊗(m+1)})`. Everything the Hecke
action produces lives here — that is the content of this file. -/
def weightCentralizer (w : Fin 2 → R) :
    Subalgebra R (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R) :=
  Subalgebra.centralizer R {siteWeight (n := m + 1) w}

/-- Every strand's braiding centralises the weight — restating `braidAt_comm_siteWeight`
as a membership. -/
theorem strandBraid_mem_weightCentralizer (w : Fin 2 → R) (a : Fin m) :
    strandBraid q qi a ∈ weightCentralizer (m := m) w := by
  rw [weightCentralizer, Subalgebra.mem_centralizer_iff]
  rintro g rfl
  exact (braidAt_comm_siteWeight q qi w).symm

private theorem cs_ne_succ' (a : Fin m) : a.castSucc ≠ a.succ := by
  simp [Fin.ext_iff]

/-- **The braid relation for the strand braidings, read off the action.**

Not a new computation: `heckeActionN` already discharged this obligation, so applying it to
`Balanced.sigma_braid` and pushing through `map_altProd` returns the matrix-level statement.
Stated separately because the subalgebra lift below needs it in this form. -/
theorem strandBraid_altProd (hqi : q * qi = 1) (a b : Fin m) :
    altProd (strandBraid q qi a) (strandBraid q qi b) (coxA m a b)
      = altProd (strandBraid q qi b) (strandBraid q qi a) (coxA m b a) := by
  have h := congrArg (heckeActionN q qi hqi)
    (QOU.IwahoriHecke.Balanced.sigma_braid (R := R) (q := q) (qi := qi) (M := coxA m)
      coxA_symm a b)
  simp only [map_altProd, heckeActionN_sigma] at h
  exact h

/-- **The Hecke action, corestricted to the centralizer of the weight.**

The same three obligations as `heckeActionN`, pulled back along the injective
`Subalgebra.val`; nothing is reproved. -/
noncomputable def heckeActionCentral (hqi : q * qi = 1) (w : Fin 2 → R) :
    QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q →ₐ[R] weightCentralizer (m := m) w :=
  QOU.IwahoriHecke.Balanced.liftBalanced hqi
    (fun a => ⟨strandBraid q qi a, strandBraid_mem_weightCentralizer q qi w a⟩)
    (fun a => by
      refine isHeckeGenerator_of_injective q qi
        (Subalgebra.val (weightCentralizer (m := m) w)) Subtype.val_injective ?_
      exact isHeckeGenerator_braidAt q qi (cs_ne_succ' a) hqi)
    (fun a b => by
      have hinj : Function.Injective (Subalgebra.val (weightCentralizer (m := m) w)) :=
        Subtype.val_injective
      refine hinj ?_
      rw [map_altProd, map_altProd]
      exact strandBraid_altProd q qi hqi a b)
    coxA_symm

@[simp] theorem heckeActionCentral_sigma (hqi : q * qi = 1) (w : Fin 2 → R) (a : Fin m) :
    ((heckeActionCentral q qi hqi w
        (QOU.IwahoriHecke.Balanced.sigma (coxA m) q qi a) : weightCentralizer (m := m) w)
      : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R) = strandBraid q qi a := by
  rw [heckeActionCentral, QOU.IwahoriHecke.Balanced.liftBalanced_sigma]

/-- Composing the corestriction back with the inclusion returns the original action. Two
algebra maps agreeing on the balanced generators are equal. -/
theorem val_comp_heckeActionCentral (hqi : q * qi = 1) (w : Fin 2 → R) :
    (Subalgebra.val (weightCentralizer (m := m) w)).comp (heckeActionCentral q qi hqi w)
      = heckeActionN q qi hqi :=
  QOU.IwahoriHecke.Balanced.hom_ext_sigma hqi _ _ (fun a => by
    rw [AlgHom.comp_apply, heckeActionN_sigma]
    exact heckeActionCentral_sigma q qi hqi w a)

/-- **The whole image centralises the weight.** For *every* `x`, not merely for generators. -/
theorem heckeActionN_mem_weightCentralizer (hqi : q * qi = 1) (w : Fin 2 → R)
    (x : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) :
    heckeActionN q qi hqi x ∈ weightCentralizer (m := m) w := by
  have h : heckeActionN q qi hqi x
      = (Subalgebra.val (weightCentralizer (m := m) w)) (heckeActionCentral q qi hqi w x) := by
    rw [← val_comp_heckeActionCentral q qi hqi w]
    rfl
  rw [h]
  exact (heckeActionCentral q qi hqi w x).2

/-- The commutation, as an equation. -/
theorem siteWeight_comm_heckeActionN (hqi : q * qi = 1) (w : Fin 2 → R)
    (x : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) :
    siteWeight (n := m + 1) w * heckeActionN q qi hqi x
      = heckeActionN q qi hqi x * siteWeight w := by
  have h := heckeActionN_mem_weightCentralizer q qi hqi w x
  rw [weightCentralizer, Subalgebra.mem_centralizer_iff] at h
  exact h _ rfl

/-! ## Cyclicity -/

/-- **`tr_w` is cyclic.** `tr_w(x y) = tr_w(y x)` for arbitrary elements of `H_{m+1}(q)`,
at every weight `w`.

The proof is three associativity steps around one use of the commutation and one use of the
ordinary cyclicity of the matrix trace: `tr(W X Y) = tr(X W Y) = tr((W Y) X) = tr(W Y X)`.
This supersedes `qTrace_sigma_mul_comm`, which is the special case `x = σ_a`. -/
theorem qTrace_mul_comm (hqi : q * qi = 1) (w : Fin 2 → R)
    (x y : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) :
    qTrace q qi hqi w (x * y) = qTrace q qi hqi w (y * x) := by
  have hc := siteWeight_comm_heckeActionN q qi hqi w x
  rw [qTrace, qTrace, map_mul, map_mul]
  set W := siteWeight (n := m + 1) w with hW
  set X := heckeActionN q qi hqi x with hX
  set Y := heckeActionN q qi hqi y with hY
  calc Matrix.trace (W * (X * Y))
      = Matrix.trace (W * X * Y) := by rw [mul_assoc]
    _ = Matrix.trace (X * W * Y) := by rw [hc]
    _ = Matrix.trace (X * (W * Y)) := by rw [mul_assoc]
    _ = Matrix.trace (W * Y * X) := Matrix.trace_mul_comm _ _
    _ = Matrix.trace (W * (Y * X)) := by rw [mul_assoc]

/-- **Conjugation-invariance.** An immediate consequence of cyclicity: `tr_w` is a class
function on the Hecke algebra, so it is constant on conjugacy classes of units — in
particular on the braid-group images of conjugate braids, which is the Markov move I
(conjugation) invariance the Jones polynomial needs.

Markov move II is the *peel*, and is a separate statement — see
`QOU.IwahoriHecke.MarkovPeel`. -/
theorem qTrace_conj (hqi : q * qi = 1) (w : Fin 2 → R)
    (u : (QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q)ˣ)
    (x : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) :
    qTrace q qi hqi w ((u : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) * x
        * ((u⁻¹ : (QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q)ˣ)
            : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q))
      = qTrace q qi hqi w x := by
  rw [qTrace_mul_comm q qi hqi w ((u : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) * x)
      ((u⁻¹ : (QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q)ˣ)
        : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q),
    ← mul_assoc, Units.inv_mul, one_mul]

end QOU.IwahoriHecke.QuantumTrace

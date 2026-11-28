import QOU.StandardModel.HyperchargeSignIsBringOrientation

/-!
# Each strand is an elliptic quotient of Bring's surface

Bean `qou-h0zz` (owner, 2026-11-28: "All", including "Strands are Bring's symmetries").

`prop:strand-charges-are-holomorphic-differentials` shows that `H⁰(B, K) = [2,1,1,1]` is the
traceless strand charge space with the sign twist `g · y = sgn(g) (y ∘ g⁻¹)`. This file gives
each strand `i` an intrinsic home on Bring's surface.

## Results

1. `stab_conj`: the stabiliser `Stab(i)` (an `S₄`) satisfies `g Stab(i) g⁻¹ = Stab(g i)`, so
   strands are permuted exactly as the five point-stabiliser subgroups of `Aut⁺(B) = S₅`, and
   likewise for `Alt(i) = Stab(i) ∩ A₅` (an `A₄`). `stab_card`, `alt_card`: orders `24`, `12`.
2. `u_fixed_by_alt`, `u_flipped_by_odd_stab`: the strand vector `uᵢ = 5 eᵢ − (1,…,1)` is
   fixed by every element of `Alt(i)` under the twisted action, and sent to `−uᵢ` by every odd
   element of `Stab(i)`.
3. `alt0_invariants`: a traceless charge vector fixed by the twisted action of the two
   3-cycles `(123)`, `(234)` of `Alt(0)` is a multiple of `u₀`.

## Reading

By Chevalley–Weil, `dim H⁰(K)^H` is the genus of `B/H` (cited, as in
`BringSymmetryQuotientGenus.lean`, where `B/A₄` is a torus and `B/S₄` a sphere). Results 2 and
3 show the `Alt(i)`-invariant line of `H⁰(K)` is spanned by `uᵢ`. So strand `i` is the
holomorphic differential pulled back from the elliptic quotient `B → B/Alt(i)`, and the five
strands are the five elliptic quotients `B/A₄` of Bring's surface, permuted by `S₅` as the
strands are. The odd elements of `Stab(i)` negate it, which is why `B/S₄` is a sphere.

What is proved is the equivariant matching of the two `S₅`-sets and of the invariant lines.
That the physical strands *are* these quotients is the modelling identification. It is no
longer a bare label: up to isomorphism, a transitive `S₅`-set of size five is unique (its
stabilisers have index five, and every index-five subgroup of `S₅` is a point stabiliser;
cited, not proved here). So any identification of the strands with an `S₅`-set from Bring's
surface agrees with this one.

Integer and rational arithmetic only. No empirical value enters.
-/

namespace QOU.StandardModel.StrandQuotients

open Equiv QOU.StandardModel.BringTwist QOU.StandardModel.BringOrientation

/-- Stabiliser of strand `i`. -/
def stab (i : Fin 5) : Finset (Perm (Fin 5)) := Finset.univ.filter (fun g => g i = i)

/-- Its even part, an `A₄`. -/
def alt (i : Fin 5) : Finset (Perm (Fin 5)) := (stab i).filter (fun g => Perm.sign g = 1)

theorem stab_card : ∀ i, (stab i).card = 24 := by decide
theorem alt_card : ∀ i, (alt i).card = 12 := by decide

theorem stab_conj (g h : Perm (Fin 5)) (i : Fin 5) :
    h ∈ stab i ↔ g * h * g⁻¹ ∈ stab (g i) := by
  simp only [stab, Finset.mem_filter, Finset.mem_univ, true_and, Perm.mul_apply,
    Perm.inv_apply_self]
  exact ⟨fun h1 => by rw [h1], fun h1 => g.injective h1⟩

theorem sign_conj (g h : Perm (Fin 5)) : Perm.sign (g * h * g⁻¹) = Perm.sign h := by
  rw [Perm.sign_mul, Perm.sign_mul, Perm.sign_inv, mul_comm (Perm.sign g) (Perm.sign h),
    mul_assoc, Int.units_mul_self, mul_one]

theorem alt_conj (g h : Perm (Fin 5)) (i : Fin 5) :
    h ∈ alt i ↔ g * h * g⁻¹ ∈ alt (g i) := by
  simp only [alt, Finset.mem_filter, ← stab_conj, sign_conj]

/-- `uᵢ = 5 eᵢ − (1,…,1)`, integer form. -/
def u (i : Fin 5) : Fin 5 → ℤ := fun j => if j = i then 4 else -1

theorem u_fixed_by_alt : ∀ i, ∀ g ∈ alt i, twistZ g (u i) = u i := by decide +kernel

theorem u_flipped_by_odd_stab :
    ∀ i, ∀ g ∈ stab i, Perm.sign g = -1 → twistZ g (u i) = -u i := by decide +kernel

/-- **The `Alt(0)`-invariants of the traceless charges are the line of `u₀`.** -/
theorem alt0_invariants (y : Fin 5 → ℚ) (hsum : ∑ j, y j = 0)
    (h1 : twist (swap 1 2 * swap 2 3) y = y) (h2 : twist (swap 2 3 * swap 3 4) y = y) :
    y = fun j => (y 0 / 4) * ((u 0 j : ℤ) : ℚ) := by
  have e := fun j => congrFun h1 j
  have f := fun j => congrFun h2 j
  have s1 : ((Perm.sign (swap (1 : Fin 5) 2 * swap 2 3) : ℤˣ) : ℤ) = 1 := by decide
  have s2 : ((Perm.sign (swap (2 : Fin 5) 3 * swap 3 4) : ℤˣ) : ℤ) = 1 := by decide
  have e1 := e 1; have e2 := e 2; have f2 := f 2; have f3 := f 3
  simp only [twist, s1, s2, Int.cast_one, one_mul] at e1 e2 f2 f3
  have a1 : ((swap (1 : Fin 5) 2 * swap 2 3 : Perm (Fin 5))⁻¹) 1 = 3 := by decide
  have a2 : ((swap (1 : Fin 5) 2 * swap 2 3 : Perm (Fin 5))⁻¹) 2 = 1 := by decide
  have b2 : ((swap (2 : Fin 5) 3 * swap 3 4 : Perm (Fin 5))⁻¹) 2 = 4 := by decide
  have b3 : ((swap (2 : Fin 5) 3 * swap 3 4 : Perm (Fin 5))⁻¹) 3 = 2 := by decide
  rw [a1] at e1; rw [a2] at e2; rw [b2] at f2; rw [b3] at f3
  simp [Fin.sum_univ_five] at hsum
  funext j; fin_cases j <;> simp [u] <;> linarith

end QOU.StandardModel.StrandQuotients

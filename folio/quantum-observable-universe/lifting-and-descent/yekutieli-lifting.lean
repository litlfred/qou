import MathlibExt.CentralExtensionH2

set_option autoImplicit false

/-!
# QOU.YekutieliLifting — lifting in the brane tower: derived and conditional parts

`prop:yekutieli-lifting` says that the transitions `Aₙ ↪ Aₙ₊₁` of the brane
tower are central extensions of gerbes banded by an abelian sheaf `𝓑`, and
that a lift exists iff the obstruction `κₙ ∈ H²(M, 𝓑)` vanishes
(Yekutieli 2010, Thm 4.17).

This file used to carry that criterion as **structure fields**
(`lift_of_vanishing`, `no_lift_of_nonzero`), together with a `persistence`
field that was retracted on 2026-11-15 (bean `qou-lx8f`). Those fields assumed
what the proposition claims. They are replaced here by:

* `QOU.YekutieliLifting.lift_iff`: the **group-level** criterion, derived for
  any tower of central group extensions `1 → Aₙ → Eₙ → Gₙ → 1` and
  homomorphisms `φₙ : Hₙ →* Gₙ` (`φₙ` lifts iff `κ(φₙ) = 1` in
  `H²(Hₙ, Aₙ)`), from `QOU.CentralExtension.obstructionClass_eq_one_iff`;
* `QOU.YekutieliLifting.perpetual_obstruction`: the perpetual-obstruction
  argument as a **conditional**, with persistence an explicit hypothesis
  rather than a field;
* `QOU.YekutieliLifting.no_lift_of_persistent`: the two combined.

**Not formalised** (bean `qou-533l`): Thm 4.17 for gerbes over a site, and
Steps 1–3 of `prf:yekutieli-lifting` (that jet prolongation gives a gerbe
banded by `𝓑` whose Giraud class is `κₙ`). The torsor layer it needs is in
`MathlibExt/StackGerbe.lean`, `CocycleTorsor.lean` and `TorsorDescent.lean`.

## References

- [yekutieli2010] Central Extensions of Gerbes, Theorem 4.17
- [leitner2026] §3 Proposition: Yekutieli Lifting
-/

namespace QOU.YekutieliLifting

open QOU.CentralExtension

section Tower

variable {A E G H : ℕ → Type*} [∀ n, CommGroup (A n)] [∀ n, Group (E n)]
  [∀ n, Group (G n)] [∀ n, Group (H n)]
  (S : ∀ n, GroupExtension (A n) (E n) (G n))
  (hcen : ∀ n (a : A n) (e : E n), (S n).inl a * e = e * (S n).inl a)
  (σ : ∀ n, (S n).Section) (φ : ∀ n, H n →* G n)

/-- **Yekutieli lifting, group level (derived).** In a tower of central group
extensions, `φₙ` lifts through `Eₙ → Gₙ` iff its obstruction class
`κ(φₙ) ∈ H²(Hₙ, Aₙ)` is trivial.

LaTeX: `\label{prop:yekutieli-lifting}` (group-level case)
Ref: [yekutieli2010] Theorem 4.17 -/
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
theorem lift_iff (n : ℕ) :
    obstructionClass (hcen n) (σ n) (φ n) = 1 ↔ ∃ ψ : H n →* E n, (S n).rightHom.comp ψ = φ n :=
  obstructionClass_eq_one_iff (hcen n) (σ n) (φ n)

end Tower

/-- **Perpetual obstruction (conditional).** If `κ₀ ≠ 0` and non-vanishing
persists from each level to the next, then `κₙ ≠ 0` for every `n`.
Persistence is a hypothesis: the argument for it on the Kummer tower of
Bring's surface was withdrawn (owner decision 2026-11-15, PR #7747, bean
`qou-lx8f`). -/
-- Ref: [leitner2026] §3, Item (3)
theorem perpetual_obstruction {X : Type*} (κ : ℕ → X) (zero : X) (h₀ : κ 0 ≠ zero)
    (hpers : ∀ n, κ n ≠ zero → κ (n + 1) ≠ zero) : ∀ n, κ n ≠ zero := by
  intro n
  induction n with
  | zero => exact h₀
  | succ n ih => exact hpers n ih

/-- In a tower of central group extensions with a persistent non-trivial base
obstruction, no level lifts. -/
theorem no_lift_of_persistent {A E G H : ℕ → Type*} [∀ n, CommGroup (A n)] [∀ n, Group (E n)]
    [∀ n, Group (G n)] [∀ n, Group (H n)]
    (S : ∀ n, GroupExtension (A n) (E n) (G n))
    (hcen : ∀ n (a : A n) (e : E n), (S n).inl a * e = e * (S n).inl a)
    (σ : ∀ n, (S n).Section) (φ : ∀ n, H n →* G n)
    (h₀ : obstructionClass (hcen 0) (σ 0) (φ 0) ≠ 1)
    (hpers : ∀ n, obstructionClass (hcen n) (σ n) (φ n) ≠ 1 →
      obstructionClass (hcen (n + 1)) (σ (n + 1)) (φ (n + 1)) ≠ 1) (n : ℕ) :
    ¬ ∃ ψ : H n →* E n, (S n).rightHom.comp ψ = φ n := by
  rw [← lift_iff S hcen σ φ n]
  induction n with
  | zero => exact h₀
  | succ n ih => exact hpers n ih

end QOU.YekutieliLifting

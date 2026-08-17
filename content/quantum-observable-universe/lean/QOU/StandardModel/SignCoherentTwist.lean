/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic

/-!
# Sign-coherence closes the `d` residual — as an assumption, not a derivation

Bean `htw2` / `qou-kebu`. Companion to
[`ComponentFraming.lean`](ComponentFraming.lean).

## What is left open, and why nothing so far reaches it

`htw2` reduces the twist battery to a `1·2·2·1` residual: the SM spectrum pins
each fermion's **total** twist (`(u,d,ν,e) = (2,−1,0,−3) = 3Q`), and the
survivors are the `{−1,0,1}`-multisets realising those totals. It also proves
why the ambiguity is hard: `Y`, the `ℤ₆` condition and bar-negation are all
**total-only**, and the ambiguous pairs share a total by construction.

`ComponentFraming.lean` closed the `ν` half — leptons close to one-component
knots, so their framing is constant, which kills `ν = {−1,0,1}`. It is
**provably blind** to `d`: both `d`-survivors have shape `(2,1)`
(`d_residual_not_separated_at_swap`), so no constraint on orbit *shape* can
separate them. Separating `d` needs a constraint on which **value** sits where.

## The one rule that does it

`SignCoherent`: no fermion carries both a positive and a negative twist. Applied
to the pinned totals it collapses the residual completely:

| fermion | total | survivors | sign-coherent |
|---|---|---|---|
| `u` | `2` | `{0,1,1}` | ✔ |
| `d` | `−1` | `{−1,−1,1}`, `{−1,0,0}` | ✗, **✔** |
| `ν` | `0` | `{−1,0,1}`, `{0,0,0}` | ✗, **✔** |
| `e` | `−3` | `{−1,−1,−1}` | ✔ |

`1·2·2·1 → 1·1·1·1`. It is uniform — one rule, applied identically to all four —
and it destroys none of the surviving assignments.

## Why this is labelled an assumption

Sign-coherence is the **helon-model structure** (Bilson-Thompson,
`[bilson-thompson2005]`, already cited for the `1/3` normalisation): a fermion's
helons carry twists of a single sign. It is *not* derived from the QOU axioms,
and a corpus grep finds no framework statement of it. Its physical reading — a
state carrying `+1` and `−1` on different strands contains an internal
bar-conjugate pair, since `bar` negates the twist — is suggestive, **not** a
proof.

So the `d` result below is **conditional on adopting sign-coherence**. That is
the honest status, and it is exactly the kind of import the anti-fit discipline
requires be named rather than absorbed.

## The corroboration worth noting

Sign-coherence independently forces `ν = {0,0,0}` — the same answer
`ComponentFraming.nu_framing_is_zero` reaches from "leptons are knots". Those
two routes are epistemically different (one derived from framework structure,
one an imported convention) and they **agree where they overlap**. That is
evidence the convention is the right one; it is not a derivation of it. `d` is
where only the assumed route reaches.
-/

namespace QOU.StandardModel.SignCoherentTwist

variable {n : ℕ}

/-- **Sign-coherence**: no two strands carry twists of opposite sign. -/
def SignCoherent (t : Fin n → ℤ) : Prop :=
  ¬ ∃ i j, 0 < t i ∧ t j < 0

/-- Sign-coherence plus a **negative** total forbids any positive strand.

This is the whole mechanism: `{−1,−1,1}` dies because it carries a `+1` while
its total is `−1`. -/
theorem no_positive_of_negative_total {t : Fin 3 → ℤ}
    (hsum : t 0 + t 1 + t 2 < 0) (hcoh : SignCoherent t) :
    ∀ i, t i ≤ 0 := by
  by_contra hcon
  push_neg at hcon
  obtain ⟨i, hi⟩ := hcon
  -- some strand is positive, so coherence forbids any negative strand
  have hnonneg : ∀ j, 0 ≤ t j := by
    intro j
    by_contra hj
    push_neg at hj
    exact hcoh ⟨i, j, hi, hj⟩
  have h0 := hnonneg 0
  have h1 := hnonneg 1
  have h2 := hnonneg 2
  omega

/-- **`d = {−1,0,0}` is forced.**

With entries in `{−1,0,1}`, total `−1`, and sign-coherence, the twist datum is
`{−1,0,0}` in one of its three orderings — so `{−1,−1,1}` is excluded and `d`'s
ambiguity is closed. -/
theorem d_multiset_forced {t : Fin 3 → ℤ}
    (hrange : ∀ i, -1 ≤ t i ∧ t i ≤ 1)
    (hsum : t 0 + t 1 + t 2 = -1)
    (hcoh : SignCoherent t) :
    (t 0 = -1 ∧ t 1 = 0 ∧ t 2 = 0) ∨
    (t 0 = 0 ∧ t 1 = -1 ∧ t 2 = 0) ∨
    (t 0 = 0 ∧ t 1 = 0 ∧ t 2 = -1) := by
  have hle := no_positive_of_negative_total (by omega) hcoh
  have h0 := hrange 0
  have h1 := hrange 1
  have h2 := hrange 2
  have l0 := hle 0
  have l1 := hle 1
  have l2 := hle 2
  omega

/-- The excluded `d`-survivor, named: `{−1,−1,1}` is **not** sign-coherent. -/
theorem d_mixed_sign_not_coherent :
    ¬ SignCoherent ![(-1 : ℤ), -1, 1] := by
  intro h
  exact h ⟨2, 0, by simp, by simp⟩

/-- The surviving `d`-assignment **is** sign-coherent. -/
theorem d_survivor_coherent : SignCoherent ![(-1 : ℤ), 0, 0] := by
  rintro ⟨i, j, hi, hj⟩
  fin_cases i <;> fin_cases j <;> simp_all

/-! ### The rule destroys nothing else

Uniformity matters: a rule that closed `d` by breaking `u` or `e` would be a fit
dressed as a principle. -/

/-- `u = {0,1,1}` survives sign-coherence. -/
theorem u_survivor_coherent : SignCoherent ![(0 : ℤ), 1, 1] := by
  rintro ⟨i, j, hi, hj⟩
  fin_cases i <;> fin_cases j <;> simp_all

/-- `e = {−1,−1,−1}` survives sign-coherence. -/
theorem e_survivor_coherent : SignCoherent ![(-1 : ℤ), -1, -1] := by
  rintro ⟨i, j, hi, hj⟩
  fin_cases i <;> fin_cases j <;> simp_all

/-- `ν = {0,0,0}` survives sign-coherence — the same answer
`ComponentFraming.nu_framing_is_zero` derives from "leptons are knots". Two
independent routes, one derived and one assumed, agreeing. -/
theorem nu_survivor_coherent : SignCoherent ![(0 : ℤ), 0, 0] := by
  rintro ⟨i, j, hi, hj⟩
  fin_cases i <;> fin_cases j <;> simp_all

/-- And the `ν`-survivor sign-coherence kills: `{−1,0,1}` carries both signs. -/
theorem nu_mixed_sign_not_coherent :
    ¬ SignCoherent ![(-1 : ℤ), 0, 1] := by
  intro h
  exact h ⟨2, 0, by simp, by simp⟩

end QOU.StandardModel.SignCoherentTwist

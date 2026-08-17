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

/-! ### Upgrade: sign-coherence is a NORMAL FORM, not an extra assumption

The section above labelled sign-coherence an imported convention. The balancing
twist wired onto `QuantumUniverse` (bean `qou-pkf3`,
`CategoricalFoundations.lean`) supplies the missing half, and it changes the
status.

That work records: *"On the defining representation the twist axiom forces
`θ_V = q^{1/2} · id_V`"*. Because `θ_V` is a **scalar multiple of the
identity**, opposite framings on two strands cancel exactly, as morphisms:

    θ_V ⊗ θ_V⁻¹ = q^{1/2} · q^{−1/2} · id = id

So a `(+1, −1)` strand pair is **ribbon-invisible**. Cancelling it is a
rewriting of the same state, not a different physical choice — and cancellation
preserves the total, hence the whole `Y`/`Q` layer built on it.

Reducing until no such pair remains lands in a sign-coherent framing, and for
entries in `{−1,0,1}` the reduced form is unique per total:

    total  −3        −2        −1        0        1        2        3
    form   {−1,−1,−1} {−1,−1,0} {−1,0,0} {0,0,0} {0,0,1} {0,1,1} {1,1,1}

The two survivors sign-coherence excluded are exactly the un-reduced spellings
of the two it keeps: `{−1,−1,1} → {−1,0,0}` and `{−1,0,1} → {0,0,0}`.

**Remaining caveat, stated rather than buried.** This derives that the coherent
representative is canonical *given* `θ_V = q^{1/2}·id_V` and given that the
physical state is the ribbon-equivalence class rather than a chosen spelling.
The first is now framework structure; the second is an interpretive step. So `d`
is no longer resting on a Bilson-Thompson convention — it rests on the twist
being scalar, which is a categorical fact of the corpus. -/

/-- **Sign-coherence is exactly "all non-negative or all non-positive".** -/
theorem coherent_iff_all_same_sign {t : Fin 3 → ℤ} :
    SignCoherent t ↔ ((∀ i, 0 ≤ t i) ∨ (∀ i, t i ≤ 0)) := by
  constructor
  · intro h
    by_cases hpos : ∀ i, 0 ≤ t i
    · exact Or.inl hpos
    · refine Or.inr fun i => ?_
      push_neg at hpos
      obtain ⟨j, hj⟩ := hpos
      by_contra hi
      push_neg at hi
      exact h ⟨i, j, hi, hj⟩
  · rintro (hall | hall) ⟨i, j, hi, hj⟩
    · exact absurd (hall j) (by omega)
    · exact absurd (hall i) (by omega)

/-- **The excluded and kept `d` forms carry the same ribbon weight.**

With `θ` central the weight of a framing is `θ ^ total`, so `{−1,−1,1}` and
`{−1,0,0}` are indistinguishable to the twist — the choice between them is a
choice of representative, and sign-coherence picks the reduced one. -/
theorem d_forms_same_weight {M : Type*} [CommGroup M] (θ : M) :
    θ ^ ((-1) + (-1) + 1 : ℤ) = θ ^ ((-1) + 0 + 0 : ℤ) := by norm_num

/-- Same for the two `ν` forms: `{−1,0,1}` and `{0,0,0}` share a ribbon weight,
and the reduced one is `{0,0,0}` — independently the answer
`ComponentFraming.nu_framing_is_zero` derives from "leptons are knots". -/
theorem nu_forms_same_weight {M : Type*} [CommGroup M] (θ : M) :
    θ ^ ((-1) + 0 + 1 : ℤ) = θ ^ ((0 : ℤ) + 0 + 0) := by norm_num

/-- **Cancellation preserves the total.**  Moving one unit off a positive strand
onto a negative one — the reduction step — leaves `Σ t` fixed, so it leaves
`Q_twist = T/3`, `Y`, and the `ℤ₆` layer fixed too. Reduction is therefore
invisible to every constraint the battery imposes. -/
theorem cancel_preserves_total (a b c : ℤ) :
    (a - 1) + (b + 1) + c = a + b + c := by ring

end QOU.StandardModel.SignCoherentTwist

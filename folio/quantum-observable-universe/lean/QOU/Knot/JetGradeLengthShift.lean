/-
# The fresh generator raises the Coxeter length by exactly one

`QOU.Knot.JetGradePromotion` proves the two facts about the *pair* `(sub, top)`:
it is not an inversion of `w` when `w` fixes the top point, and it is an
inversion of `w * s` afterwards. That is the interesting half, and it stops one
step short of what the jet-promotion argument actually needs, which is a
statement about the *count*:

    l(w * s) = l(w) + 1        for every w fixing the top point.

One pair flipping does not by itself give this -- it gives it only together with
the fact that **no other pair changes**. That is what is proved here, by
exhibiting the bijection explicitly rather than appealing to it.

## The bijection

Write `s = swap sub top` and `v = w * s`, so `v x = w (s x)`. Since `s` is an
involution, `v (s a) = w a`. Hence for any ordered pair `(a, b)`,

    (s a, s b) is an inversion of v   <->   (a, b) is an inversion of w

*provided* `s a < s b`, so that `(s a, s b)` is a legitimately ordered pair. The
whole content is that `s a < s b` fails for **exactly one** pair with `a < b`,
namely `(sub, top)` -- and that pair is the one `JetGradePromotion` already
handles. Everything else is carried across untouched.

So `invSet (w * s) = insert (sub, top) ((invSet w).image φ)` with `φ` injective
and `(sub, top)` outside the image, and the cardinality follows.

## Why this is the statement the arc needs

`QOU.Knot.GradedGeneratingFunction.gf_shift` consumes a degree function shifted
by one with its coefficients intact. This supplies the `+ 1`, on the Coxeter
length, which is the Grobner-Shirshov filtration grade. It is still a statement
about permutations, not about algebra elements -- `HeckeTwBasis` is where that
step is taken.

-- Ref: [bjorner-brenti2005] https://doi.org/10.1007/3-540-27596-7
-/
import QOU.Knot.JetGradePromotion

namespace QOU.Knot.JetGradeLengthShift

open QOU.Knot.JetGradePromotion

variable {n : ℕ}

/-- The adjacent transposition of the top two points -- the "fresh generator". -/
abbrev sTop : Equiv.Perm (Fin (n + 2)) := Equiv.swap sub top

theorem val_sub : (sub : Fin (n + 2)).val = n := rfl

theorem val_top : (top : Fin (n + 2)).val = n + 1 := rfl

/-- Everything other than the top point lies at or below `sub`, because `sub` is
the immediate predecessor of the maximum. -/
theorem le_sub_of_ne_top {x : Fin (n + 2)} (hx : x ≠ top) : x ≤ sub := by
  have hlt : x.val < n + 2 := x.isLt
  have hne : x.val ≠ n + 1 := by
    intro h
    exact hx (Fin.ext (by simpa [val_top] using h))
  have : x.val ≤ n := by omega
  simpa [Fin.le_def, val_sub] using this

/-- `sTop` moves only the top two points. -/
theorem sTop_apply_of_ne {x : Fin (n + 2)} (h1 : x ≠ sub) (h2 : x ≠ top) :
    (sTop : Equiv.Perm (Fin (n + 2))) x = x :=
  Equiv.swap_apply_of_ne_of_ne h1 h2

/-- **The one-pair lemma.** For an ordered pair other than `(sub, top)`, applying
the fresh generator to both coordinates preserves the order. This is the fact
that makes the inversion count move by exactly one rather than by an unknown
amount. -/
theorem sTop_lt_sTop {a b : Fin (n + 2)} (hab : a < b) (hne : (a, b) ≠ (sub, top)) :
    (sTop : Equiv.Perm (Fin (n + 2))) a < sTop b := by
  by_cases hb : b = top
  · -- b is the top point, so a is neither sub (excluded) nor top (a < b)
    subst hb
    have ha_top : a ≠ top := ne_of_lt hab
    have ha_sub : a ≠ sub := by
      intro h; exact hne (by rw [h])
    rw [sTop_apply_of_ne ha_sub ha_top, Equiv.swap_apply_right]
    exact lt_of_le_of_ne (le_sub_of_ne_top ha_top) ha_sub
  · by_cases hbs : b = sub
    · -- b = sub, so a < sub < top and a is moved by nothing
      subst hbs
      have ha_sub : a ≠ sub := ne_of_lt hab
      have ha_top : a ≠ top := ne_of_lt (hab.trans sub_lt_top)
      rw [sTop_apply_of_ne ha_sub ha_top, Equiv.swap_apply_left]
      exact hab.trans sub_lt_top
    · -- neither coordinate is touched
      have hb_le : b ≤ sub := le_sub_of_ne_top hb
      have ha_sub : a ≠ sub := ne_of_lt (lt_of_lt_of_le hab hb_le)
      have ha_top : a ≠ top := ne_of_lt (hab.trans (hb_le.trans_lt sub_lt_top))
      rw [sTop_apply_of_ne ha_sub ha_top, sTop_apply_of_ne hbs hb]
      exact hab


/-- Membership in the inversion set, unfolded. -/
theorem mem_invSet {m : ℕ} {w : Equiv.Perm (Fin m)} {p : Fin m × Fin m} :
    p ∈ invSet w ↔ p.1 < p.2 ∧ w p.2 < w p.1 := by
  simp [invSet]

/-- Transport of ordered pairs along the fresh generator. -/
def phi (p : Fin (n + 2) × Fin (n + 2)) : Fin (n + 2) × Fin (n + 2) :=
  ((sTop : Equiv.Perm (Fin (n + 2))) p.1, sTop p.2)

theorem phi_phi (p : Fin (n + 2) × Fin (n + 2)) : phi (phi p) = p := by
  simp [phi, Equiv.swap_apply_self]

theorem phi_injective : Function.Injective (phi (n := n)) := by
  intro a b h
  have := congrArg phi h
  simpa [phi_phi] using this

theorem phi_sub_top : phi ((sub : Fin (n + 2)), top) = (top, sub) := by
  simp [phi, Equiv.swap_apply_left, Equiv.swap_apply_right]

/-- **The inversion set moves by exactly one pair.** Everything the fresh
generator can see other than `(sub, top)` is carried across by `phi`, and that
one pair is added. -/
theorem invSet_mul_sTop {w : Equiv.Perm (Fin (n + 2))} (hw : w top = top) :
    invSet (w * sTop) = insert ((sub : Fin (n + 2)), top) ((invSet w).image phi) := by
  ext q
  constructor
  · intro hq
    by_cases hqs : q = ((sub : Fin (n + 2)), top)
    · rw [hqs]; exact Finset.mem_insert_self _ _
    · refine Finset.mem_insert_of_mem ?_
      rw [Finset.mem_image]
      refine ⟨phi q, ?_, phi_phi q⟩
      rw [mem_invSet] at hq ⊢
      obtain ⟨hlt, hinv⟩ := hq
      refine ⟨sTop_lt_sTop hlt hqs, ?_⟩
      simpa [phi, Equiv.Perm.mul_apply, Equiv.swap_apply_self] using hinv
  · intro hq
    rcases Finset.mem_insert.mp hq with h | h
    · subst h
      rw [mem_invSet]
      exact ⟨sub_lt_top, sub_top_inversion_after hw⟩
    · rw [Finset.mem_image] at h
      obtain ⟨p, hp, rfl⟩ := h
      have hpne : p ≠ ((sub : Fin (n + 2)), top) := by
        intro hcontra
        rw [hcontra, mem_invSet] at hp
        exact sub_top_not_inversion hw hp.2
      rw [mem_invSet] at hp ⊢
      obtain ⟨hlt, hinv⟩ := hp
      refine ⟨sTop_lt_sTop hlt hpne, ?_⟩
      simpa [phi, Equiv.Perm.mul_apply, Equiv.swap_apply_self] using hinv

/-- **The promotion theorem, as a count.** Multiplying on the right by the fresh
generator raises the Coxeter length -- the Grobner-Shirshov filtration grade --
by exactly one, for every permutation fixing the top point.

This is what `GradedGeneratingFunction.gf_shift` consumes: a degree function
shifted by one with its coefficients untouched. -/
theorem length_mul_sTop {w : Equiv.Perm (Fin (n + 2))} (hw : w top = top) :
    length (w * sTop) = length w + 1 := by
  have hnot : ((sub : Fin (n + 2)), top) ∉ (invSet w).image phi := by
    rw [Finset.mem_image]
    rintro ⟨p, hp, hpe⟩
    have : p = ((top : Fin (n + 2)), sub) := by
      have := congrArg phi hpe
      rwa [phi_phi, phi_sub_top] at this
    rw [this, mem_invSet] at hp
    exact absurd hp.1 (not_lt.mpr (le_of_lt sub_lt_top))
  rw [length, length, invSet_mul_sTop hw, Finset.card_insert_of_notMem hnot,
    Finset.card_image_of_injective _ phi_injective]


/-! ## The length always moves, for every permutation

`length_mul_sTop` needs `w` to fix the top point. That hypothesis is not needed
for the weaker statement that the length *changes*, and the weaker statement is
what the Hecke relation requires -- if the length could stay put, the descending
branch of the right-action rule would be taken twice and `T_s^2 = A T_s + 1`
would fail.

The bijection `phi` never used any hypothesis on `w` (see `sTop_lt_sTop`), so it
generalises verbatim. Only the special pair needs care, and there the two
alternatives are exhaustive: `(sub, top)` is an inversion of `v * sTop` exactly
when it is *not* one of `v`, because right multiplication by `sTop` exchanges
the values at those two points and a permutation cannot take the same value
twice. So the count moves by exactly one, in one direction or the other. -/

theorem mem_invSet_sub_top {v : Equiv.Perm (Fin (n + 2))} :
    ((sub : Fin (n + 2)), top) ∈ invSet v ↔ v top < v sub := by
  rw [mem_invSet]
  exact ⟨fun h => h.2, fun h => ⟨sub_lt_top, h⟩⟩

/-- The fresh generator flips the status of the one pair it can see. -/
theorem mem_invSet_sub_top_mul {v : Equiv.Perm (Fin (n + 2))} :
    ((sub : Fin (n + 2)), top) ∈ invSet (v * sTop) ↔ ¬ (((sub : Fin (n + 2)), top) ∈ invSet v) := by
  have hne : v sub ≠ v top := fun h => absurd (v.injective h) (ne_of_lt sub_lt_top)
  rw [mem_invSet_sub_top, mem_invSet_sub_top, Equiv.Perm.mul_apply, Equiv.Perm.mul_apply,
    Equiv.swap_apply_left, Equiv.swap_apply_right, not_lt]
  exact ⟨fun h => le_of_lt h, fun h => lt_of_le_of_ne h hne⟩

/-- **Every other pair transports**, with no hypothesis on `v` at all. -/
theorem invSet_erase_image (v : Equiv.Perm (Fin (n + 2))) :
    (invSet (v * sTop)).erase ((sub : Fin (n + 2)), top)
      = ((invSet v).erase ((sub : Fin (n + 2)), top)).image phi := by
  ext q
  simp only [Finset.mem_erase, Finset.mem_image]
  constructor
  · rintro ⟨hqne, hq⟩
    refine ⟨phi q, ⟨?_, ?_⟩, phi_phi q⟩
    · intro hc
      have hq2 : q = ((top : Fin (n + 2)), sub) := by
        have := congrArg phi hc
        rwa [phi_phi, phi_sub_top] at this
      rw [hq2, mem_invSet] at hq
      exact absurd hq.1 (not_lt.mpr (le_of_lt sub_lt_top))
    · rw [mem_invSet] at hq ⊢
      obtain ⟨hlt, hinv⟩ := hq
      refine ⟨sTop_lt_sTop hlt hqne, ?_⟩
      simpa [phi, Equiv.Perm.mul_apply, Equiv.swap_apply_self] using hinv
  · rintro ⟨p, ⟨hpne, hp⟩, rfl⟩
    refine ⟨?_, ?_⟩
    · intro hc
      have hp2 : p = ((top : Fin (n + 2)), sub) := by
        have := congrArg phi hc
        rwa [phi_phi, phi_sub_top] at this
      rw [hp2, mem_invSet] at hp
      exact absurd hp.1 (not_lt.mpr (le_of_lt sub_lt_top))
    · rw [mem_invSet] at hp ⊢
      obtain ⟨hlt, hinv⟩ := hp
      refine ⟨sTop_lt_sTop hlt hpne, ?_⟩
      simpa [phi, Equiv.Perm.mul_apply, Equiv.swap_apply_self] using hinv

/-- **The length always moves.** For every permutation -- no hypothesis at all --
right multiplication by the fresh generator changes the Coxeter length. It rises
by one when `(sub, top)` was not an inversion and falls by one when it was, so in
particular it is never left where it was.

This is what the Hecke relation needs: if the length could stay put, the
descending branch of the right-action rule would be taken twice and
`T_s^2 = A T_s + 1` would fail. -/
theorem length_mul_sTop_ne (v : Equiv.Perm (Fin (n + 2))) :
    length (v * sTop) ≠ length v := by
  have hcard : ((invSet (v * sTop)).erase ((sub : Fin (n + 2)), top)).card
      = ((invSet v).erase ((sub : Fin (n + 2)), top)).card := by
    rw [invSet_erase_image, Finset.card_image_of_injective _ phi_injective]
  by_cases hv : ((sub : Fin (n + 2)), top) ∈ invSet v
  · have hnv : ((sub : Fin (n + 2)), top) ∉ invSet (v * sTop) :=
      fun h => (mem_invSet_sub_top_mul.mp h) hv
    rw [Finset.erase_eq_of_notMem hnv, Finset.card_erase_of_mem hv] at hcard
    have hpos : 0 < (invSet v).card := Finset.card_pos.mpr ⟨_, hv⟩
    rw [length, length]
    omega
  · have hnv : ((sub : Fin (n + 2)), top) ∈ invSet (v * sTop) :=
      mem_invSet_sub_top_mul.mpr hv
    rw [Finset.erase_eq_of_notMem hv, Finset.card_erase_of_mem hnv] at hcard
    have hpos : 0 < (invSet (v * sTop)).card := Finset.card_pos.mpr ⟨_, hnv⟩
    rw [length, length]
    omega

end QOU.Knot.JetGradeLengthShift

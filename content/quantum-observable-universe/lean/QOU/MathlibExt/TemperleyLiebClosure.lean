import QOU.MathlibExt.TemperleyLiebNormalForm

/-!
# The δ half of the Temperley–Lieb closure rule

**Bean `qou-cds1`.** `TemperleyLiebNormalForm` defines the general index
`NormalIdx m` as a pair `(I, J)`, because word length is refuted as a
termination measure. What blocks `dim TL_n = catalan n` is the **closure rule**:
a formula for

    e_k · elt(I, J)   =   δ^loops · elt(I', J')

as a function of `(k, I, J)`. `computations/tl_closure_rule_probe.py` computed
that product by planar diagrams for every `(k, I, J)` at `n = 2..7` — 3456
products — and tested candidate rules against it rather than guessing one.

**The δ half came back complete, and it is a condition on `I` alone:**

    loops = 1   ⟺   (I', J') = (I, J)
    loops = 1   ⟺   k ∈ I  ∧  k-1 ∉ I

Both hold on all 3456. The second is sharp: `k ∈ I` alone fails 650 products,
`k ∈ I ∧ k+1 ∉ I` fails 882, `k ∈ I ∧ k ∉ J` fails 846. **`J` never enters.**

This file proves the *mechanism* behind that rule, at the level of words where
it actually lives.

* `e_comm_prod` — `e_k` commutes past a whole word whose letters are all far
  from `k`.
* `e_mul_prod_eq_smul` — hence on a word `pre ++ k :: post` with `pre` far from
  `k`, left multiplication by `e_k` returns **the same word scaled by δ**.

`k ∈ I` puts `k` at the top of some block; `k-1 ∉ I` is exactly what forces
every *earlier* block's top — and so all its letters — to be `≤ k-2`, i.e. far
from `k`. So the measured condition is not a fit: it is the hypothesis of
`e_mul_prod_eq_smul` read off the block structure.

## 🛑 What is NOT proved

* **The instantiation is not here.** Deriving `pre` far from `k` from
  `k ∈ I ∧ k-1 ∉ I` needs `NormalIdx.word`'s block decomposition — that the word
  splits at the block whose top is `k`, with everything before it bounded by
  `k-2`. That is the next step, and it is not taken in this file.
* **The `loops = 0` branch is open.** 2378 of the 3456 products, and no simple
  candidate fits: `I' = I ∪ {k}` fails 1821, `I' ⊆ I ∪ {k}` fails 348,
  `J' ⊆ J ∪ {k}` fails 129. The size moves **both ways** —
  `|I'| - |I| ∈ {-1, 0, +1}` with counts 302 / 1519 / 557 — and that decrease is
  precisely the source of the word-length non-monotonicity. So the remaining
  rule cannot be insertion-shaped, which is *why* the earlier negative held.
* Two invariants hold on all 3456 products and are recorded in the witness
  rather than proved here: `k ∈ I'` always, and `|I'| = |J'|` always.

No class, axiom or `sorry` stands in for any of this.

-- Ref: [jones1985] https://doi.org/10.2307/1971403
-/

namespace QOU.MathlibExt.TemperleyLiebClosure

open QOU.MathlibExt.TemperleyLieb
open QOU.MathlibExt.TemperleyLiebNormalForm

variable {R : Type*} [CommRing R] {m : ℕ}

/-- **`e_k` commutes past a whole word all of whose letters are far from `k`.**

The engine the δ rule rests on. Stated for an arbitrary list rather than for a
normal form, so the instantiation is a separate obligation and this stays
reusable. -/
theorem e_comm_prod (δ : R) (k : Fin m) :
    ∀ (w : List (Fin m)), (∀ t ∈ w, ¬ adjFin k t ∧ k ≠ t) →
      e R δ (adjFin (n := m)) k * (w.map (fun i => e R δ (adjFin (n := m)) i)).prod
        = (w.map (fun i => e R δ (adjFin (n := m)) i)).prod
            * e R δ (adjFin (n := m)) k := by
  intro w
  induction w with
  | nil => intro _; simp
  | cons a t ih =>
      intro h
      have ha := h a (by simp)
      have hrest : ∀ x ∈ t, ¬ adjFin k x ∧ k ≠ x := fun x hx => h x (by simp [hx])
      simp only [List.map_cons, List.prod_cons, ← mul_assoc]
      rw [e_farCommute ha.1]
      rw [mul_assoc, ih hrest, ← mul_assoc]

/-- **The δ rule, abstractly.** On a word `pre ++ k :: post` whose prefix is all
far from `k`, left multiplication by `e_k` returns the same word scaled by `δ`.

This is the mechanism behind the measured `loops = 1 ⟺ k ∈ I ∧ k-1 ∉ I`:
`k ∈ I` puts `k` at a block top, and `k-1 ∉ I` forces every earlier block's
letters to be `≤ k-2` — exactly `hpre`. The `post` part is untouched, which is
why the resulting normal form is *unchanged* rather than merely equivalent. -/
theorem e_mul_prod_eq_smul (δ : R) (k : Fin m) (pre post : List (Fin m))
    (hpre : ∀ t ∈ pre, ¬ adjFin k t ∧ k ≠ t) :
    e R δ (adjFin (n := m)) k
        * (((pre ++ k :: post).map (fun i => e R δ (adjFin (n := m)) i)).prod)
      = δ • (((pre ++ k :: post).map (fun i => e R δ (adjFin (n := m)) i)).prod) := by
  simp only [List.map_append, List.prod_append, List.map_cons, List.prod_cons]
  rw [← mul_assoc, e_comm_prod δ k pre hpre, mul_assoc, ← mul_assoc
    (e R δ (adjFin (n := m)) k) (e R δ (adjFin (n := m)) k), e_sq k,
    ← Algebra.smul_def]
  rw [smul_mul_assoc, mul_smul_comm]

end QOU.MathlibExt.TemperleyLiebClosure

import QOU.Machinery.MarkovTraceOnHecke
import Mathlib.Tactic.NormNum
import Mathlib.Algebra.Group.Idempotent

/-!
# `JonesWenzlProjector` is just "`p` is idempotent"; its `q`, `n` are unused

`JonesWenzlProjector R H q n p` has a single field `p * p = p`. The
parameters `q` and `n` occur in no field, and the strand-killing relation
`p · σ_i = −q⁻¹ · p` that would make `p` the Jones–Wenzl projector is only a
comment.

**What is proved (sorry-free).**
* `jonesWenzlProjector_iff` — the class is equivalent to `IsIdempotentElem p`,
  for every `q` and `n`.
* `jonesWenzlProjector_one`, `jonesWenzlProjector_zero` — `1` and `0` inhabit
  it in every `R`-algebra, at every `q` and `n`.
* `not_jonesWenzlProjector_two` — it is a real constraint on `p`: `2 ∈ ℚ` is
  not idempotent.

So the class is satisfiable for wrong reasons (the identity is not the
Jones–Wenzl projector for `n ≥ 2`) and is not a debt item as stated.

**Related red flag (reported, not edited).** The brief mentions a
`HeckeAlgebra … where hecke_structure : True` marker at line 48 of the source.
On the current tree that class has already been **removed** (the source now
carries a note "Removed: the `QOU.Machinery.HeckeAlgebra` marker class"), so
there is nothing left to flag there.

**What is not proved.** Existence and uniqueness of the Jones–Wenzl projector
in `H_n(q)` (needs the generators in the signature and `[n]_q! ≠ 0`); making
the class say that is a refactor needing owner approval.

-- Ref: [leitner2026] QOU.Machinery.MarkovTraceOnHecke; [wenzl1987]
-- H. Wenzl, On sequences of projections, C. R. Math. Rep. Acad. Sci. Canada 9
-- (1987) 5–9 (the recursive projector and its uniqueness).
-/

namespace QOU.Machinery.Instances

open QOU.Machinery

theorem jonesWenzlProjector_iff {R H : Type*} [CommRing R] [Ring H] [Algebra R H]
    (q : R) (n : ℕ) (p : H) : JonesWenzlProjector R H q n p ↔ IsIdempotentElem p :=
  ⟨fun h => h.idempotent, fun h => ⟨h⟩⟩

theorem jonesWenzlProjector_one {R H : Type*} [CommRing R] [Ring H] [Algebra R H]
    (q : R) (n : ℕ) : JonesWenzlProjector R H q n (1 : H) := ⟨one_mul 1⟩

theorem jonesWenzlProjector_zero {R H : Type*} [CommRing R] [Ring H] [Algebra R H]
    (q : R) (n : ℕ) : JonesWenzlProjector R H q n (0 : H) := ⟨zero_mul 0⟩

theorem not_jonesWenzlProjector_two (q : ℚ) (n : ℕ) :
    ¬ JonesWenzlProjector ℚ ℚ q n (2 : ℚ) := by
  intro h
  have := h.idempotent
  norm_num at this

end QOU.Machinery.Instances

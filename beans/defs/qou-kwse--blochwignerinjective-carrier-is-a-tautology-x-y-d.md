---
# qou-kwse
title: BlochWignerInjective carrier is a tautology (x = y -> D x = D y -> x = y)
status: completed
type: task
priority: normal
tags:
    - lean
    - vacuity
created_at: 2026-11-22T15:20:06Z
updated_at: 2026-11-22T15:29:45Z
parent: qou-uwyf
---

Found by rule 6 of the self-assuming audit, 2026-11-22. predicted-spectra/bring-hyperbolic-knot-bloch-decomposition.lean:286: the class field `inj : ∀ {x y}, x = y → D x = D y → x = y` holds for every D, so the class asserts nothing. field_equivalence_via_uniqueness and class_equality_from_value_equality never use it; they are rw [h1, h2]. Their docstrings claim the two routes 'identify the same B(Q(ζ_60))⊗Q class'; the Lean proves only that two reals equal to the same real are equal. Fix: give the field the real injectivity (D x = D y → x = y on the relevant set) or drop the class and the class-identification wording. Sibling defect in the same file: qou-mokg.


2026-11-22: fixed in PR #9033 (rebase-merged, 1c2d81edee3). lean-direct exit 0.

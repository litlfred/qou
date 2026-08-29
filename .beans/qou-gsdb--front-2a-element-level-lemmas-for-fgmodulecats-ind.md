---
# qou-gsdb
title: 'Front 2a: element-level lemmas for FGModuleCat''s induced monoidal structure'
status: scrapped
type: task
priority: normal
created_at: 2026-08-26T16:22:42Z
updated_at: 2026-08-26T16:38:07Z
---

SCRAPPED as a dependency of the PivotalCategory instance -- that instance landed by
another route (qou-knsx), so nothing in this tranche needs these lemmas any more.

The GAP IS STILL REAL and is worth recording for whoever needs element-level
computation in FGModuleCat. Its monoidal structure is induced on a full subcategory
((ModuleCat.isFG R).IsMonoidal), so ModuleCat.MonoidalCategory.whiskerLeft_apply /
whiskerRight_apply / associator_inv_apply do NOT fire on it, and
Algebra/Category/FGModuleCat/Basic.lean supplies no replacements (grep whiskerLeft
there: two hits, both `open MonoidalCategory`). Any proof that has to touch
FGModuleCat morphisms elementwise hits this wall first.

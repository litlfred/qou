---
# qou-174s
title: Drop sorry instances of HiggsAsT28 and PeriodicTableDemand (instance-free hypothesis classes)
status: completed
type: task
priority: normal
created_at: 2026-11-27T21:30:48Z
updated_at: 2026-11-27T21:34:34Z
---

Both conjecture classes shipped a sorry-filled instance, so instance resolution discharged [HiggsAsT28]/[PeriodicTableDemand] silently and the conditional theorems were unconditional on a sorry. PR #9724 removes both instances (§3b-cond; precedent QOU.MassEndomorphism.VolumeBridge). Survey 2026-11-27 group 10. Remaining defect, not fixed here: higgs_three_colors takes [HiggsAsT28] but never uses it (its body is t28_genus_eq_three), so it is a vacuous conditional.


2026-11-27: PR #9724 merged.

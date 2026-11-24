---
# qou-jkmh
title: 'Close sRow3 Derivation Seam: Prove >=3-Row Signed Springer-Dimension Table from Frame-Robinson-Thrall Hook-Length dimHLF & nStatList in Lean'
status: completed
type: task
priority: high
created_at: 2026-11-18T22:15:54Z
updated_at: 2026-11-24T09:50:37Z
parent: qou-rgj8
---

Formalize QOU/MassTheory/ThreeRowSpringerSYTDerivation.lean (0 sorry, 0 axiom) importing QOU.MassTheory.ThreeRowExtensiveCumulant, QOU.BraidsAndKnots.DeltaLambdaDTIndexGeneralN, and QOU.Mathlib.IdentityIHLFBridge: (1) Enumerate the exact >=3-row partitions at k=1,2 (empty), k=3 ([[1,1,1]]), k=4 ([[2,1,1], [1,1,1,1]]), and k=5 ([[3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1]]); (2) Compute each partition's SYT dimension via the genuine Frame-Robinson-Thrall hook-length formula dimHLF and each partition's Springer grade via nStatList / dtEulerG; (3) Prove that summing dtEulerG (nStatList lam) (dimHLF lam) over the >=3-row partitions of k equals sRow3 k for all k <= 5 (0, 0, -1, -2, +4), discharging the sRow3 table derivation seam noted in ThreeRowExtensiveCumulant.lean and GPMTThreeRowCumulantBridge.lean.

ThreeRowSpringerSYTDerivation.lean (sRow3Derived_eq_sRow3, 0 sorry) already on main (917b6939954); stale downstream docstrings synced at 83a784c4bdd.

Closed post-merge: landed on origin/main in Batch 7 PR #9265 (8276b3ebc95 / 5ed19b735da).

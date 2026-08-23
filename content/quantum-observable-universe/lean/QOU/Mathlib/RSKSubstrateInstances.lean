import QOU.Mathlib.RSKBridge
import QOU.Mathlib.PartitionsOfBridge

/-!
# QOU.Mathlib.RSKSubstrateInstances — the RSK substrate, proved (not assumed) for `n ≤ 12`

`RSKBridge` carries the substrate assumption as a Lean `axiom`:
`RSK_substrate_axiom (n : ℕ) : RSKBurnsideHolds n` — the RSK/Burnside identity
`Σ_{p ⊢ n} dimSYT(p)² = n!` on the genuine `#SYT` count, for every `n`, pending Mathlib's RSK
cardinality theorem.  With the hook-length bridge (`IdentityIHLFBridge.dimSYT_eq_dimHLF`) and the
enumeration bridge (`PartitionsOfBridge.rskBurnsideHolds_le12`) both proved, the identity is now a
**theorem** for every `n ≤ 12`.  This file wires that in:

* `RSK_substrate_proved_le12` — the `n ≤ 12` route, via the enumeration bridge.
  **Corrected 2026-08-23:** this bullet used to call it "the axiom-free counterpart of
  `RSK_substrate_axiom`" and say "the axiom's live range is now `n ≥ 13` only". There is no live
  range, because there is no axiom: `RSKBridge.RSK_substrate_proved` proves the identity for every
  `n` from the Robinson–Schensted correspondence. This bullet's route is retained as the cheaper
  one at small `n`, not as the only one.
* `rskBijection_of_lt13` — the **first genuine `RSKBijection n` construction** (the class had no
  non-vacuous instance): `dim := dimSYT` with the proved Burnside field.  Registered as instances
  at the physically-used `n = 3` (deuteron `pn` channel), `n = 5` (the s5-so3 keystone), `n = 7`
  (the defect-cubic sign flip), and `n = 12` (the `decide`-coverage top).
* `cohortWitness_of_lt13` — a concrete `CohortRSKWitness n` from the `partitionsOf` enumerator
  and `dim_validated_le12`.

Pure combinatorics on `ℕ`; nothing archimedean; no fit; no new axioms (and no use of
`RSK_substrate_axiom` anywhere in this file).
-/

namespace QOU.Mathlib.RSKBridge

open QOU.BraidKnot.IdentityI (partitionsOf dimHLF dim_validated_le12)
open QOU.Mathlib.PartitionsOfBridge (rskBurnsideHolds_le12)

/-- **The substrate identity is a theorem for `n ≤ 12`** — the axiom-free counterpart of
`RSK_substrate_axiom`, via the hook-length bridge + the `partitionsOf` enumeration bridge.
Cite this (not the axiom) for any `n ≤ 12` use.  (Stated with a bare `n ≤ 12` hypothesis for
ergonomics, per review; `rskBurnsideHolds_le12` is the `List.range`-shaped source.) -/
theorem RSK_substrate_proved_le12 (n : ℕ) (hn : n ≤ 12) : QOU.Mathlib.RSKBurnsideHolds n :=
  rskBurnsideHolds_le12 n (List.mem_range.mpr (Nat.lt_succ_of_le hn))

/-- **Genuine `RSKBijection` construction for `n ≤ 12`** — `dim` is the real SYT count
(`dimSYT`, a `Nat.card`) and the Burnside field is the proved `rskBurnsideHolds_le12`, not the
axiom.  The class previously had no non-vacuous instance. -/
noncomputable def rskBijection_of_lt13 (n : ℕ) (hn : n < 13) : RSKBijection n where
  dim := QOU.Mathlib.dimSYT
  n_factorial_eq_sum_squares := rskBurnsideHolds_le12 n (List.mem_range.mpr hn)

/-- `n = 3` — the deuteron `pn` channel of the keystone's binding-side target. -/
noncomputable instance : RSKBijection 3 := rskBijection_of_lt13 3 (by norm_num)

/-- `n = 5` — the s5-so3 keystone itself. -/
noncomputable instance : RSKBijection 5 := rskBijection_of_lt13 5 (by norm_num)

/-- `n = 7` — the defect-cubic `144·C(n) = −n(n−1)(2n−13)` sign flip. -/
noncomputable instance : RSKBijection 7 := rskBijection_of_lt13 7 (by norm_num)

/-- `n = 12` — the top of the `decide`-verified coverage. -/
noncomputable instance : RSKBijection 12 := rskBijection_of_lt13 12 (by norm_num)

/-- A concrete `CohortRSKWitness` for every `n ≤ 12`: the cohort is the `partitionsOf n`
enumeration with hook-length dimensions, its Burnside field the `decide`-verified
`dim_validated_le12`. -/
def cohortWitness_of_lt13 (n : ℕ) (hn : n < 13) : CohortRSKWitness n where
  syt_counts := (partitionsOf n).map dimHLF
  burnside_holds := by
    rw [List.map_map]
    exact dim_validated_le12 n (List.mem_range.mpr hn)

end QOU.Mathlib.RSKBridge

import QOU.BraidKnot.SnIsotypicSpechtSplitInstance
import QOU.BraidKnot.OVTopAssembly
import QOU.BraidKnot.BurnsideDischarge
import QOU.BraidsAndKnots.PlancherelNormalisation

/-!
# QOU.BraidKnot.WedderburnUnconditional — the discharged cone, stated without hypotheses

`SnIsotypicSpechtSplitInstance` inhabits `SnWedderburnPartitionBridge.SnIsotypicSpechtSplit ℚ`, so
every result carrying that class as a hypothesis is satisfiable by instance resolution. This file
makes that concrete rather than leaving it as a claim about instance resolution: each theorem below
**restates a conditional result with no hypothesis**, and its proof is the conditional result
applied. If the instance ever stopped resolving, this file would stop compiling.

The hypotheses are left in place upstream on purpose — removing them would churn every signature,
and the class form is what lets instance resolution fill them at use sites downstream of the
instance. What this file adds is a checked record of *which* results are now unconditional.

## Stale docstrings this exposes (not edited here)

Two upstream comments describe the state of the world before the instance existed:

* `BurnsideDischarge` says `OVTopAssembly.sum_numSYT_sq_eq_factorial` "carries the residual
  `sorryAx`". It does not — it carries a class hypothesis, and the class is now inhabited.
* `RSKBurnsideDischarge` says of its class-conditional result "It is now a theorem". That overclaims
  a conditional proof; the unconditional one is `QOU.Mathlib.rskBurnsideHolds`.

Both are someone else's files and are flagged rather than rewritten.
-/

namespace QOU.BraidKnot.WedderburnUnconditional

open QOU.BraidKnot
open QOU.BraidKnot.DeltaLambdaSignRule

/-- **The keystone, with no hypothesis.** -/
theorem sn_isotypic_specht_split (n : ℕ) :
    ∃ e : MonoidAlgebra ℚ (Equiv.Perm (Fin n)) ≃ₐ[ℚ]
      (∀ i : SpechtClassification.PartitionIndex n,
        Matrix (Fin (Module.finrank ℚ (Specht.SpechtSubmodule (k := ℚ) i.diagram)))
               (Fin (Module.finrank ℚ (Specht.SpechtSubmodule (k := ℚ) i.diagram))) ℚ),
      e (RegularRepTrace.centralC2 n)
        = fun i : SpechtClassification.PartitionIndex n =>
            ((JucysMurphy.contentSqSum i.diagram : ℤ) : ℚ) •
            (1 : Matrix (Fin (Module.finrank ℚ (Specht.SpechtSubmodule (k := ℚ) i.diagram)))
                        (Fin (Module.finrank ℚ (Specht.SpechtSubmodule (k := ℚ) i.diagram))) ℚ) :=
  SnWedderburnPartitionBridge.sn_isotypic_specht_split n

/-- **The Wedderburn dimension sum, with no hypothesis.** -/
theorem sum_numSYT_sq_eq_factorial (n : ℕ) :
    ∑ i : SpechtClassification.PartitionIndex n, (numSYT i.diagram) ^ 2 = Nat.factorial n :=
  OVTopAssembly.sum_numSYT_sq_eq_factorial n

/-- **Burnside over the custom partition encoding, with no hypothesis.** -/
theorem burnside_proved (n : ℕ) (partitions : List (Partition n))
    (hcomplete : ∀ μ : Partition n, μ.parts ∈ partitions.map Partition.parts)
    (hnodup : (partitions.map Partition.parts).Nodup) :
    (partitions.map fun Λ => Λ.dimIrrep ^ 2).sum = Nat.factorial n :=
  BurnsideDischarge.burnside_proved n partitions hcomplete hnodup

/-- **The Plancherel tilt normalisation at zero, with no hypothesis.** -/
theorem tiltNorm_zero_eq_factorial (k : ℕ) :
    QOU.BraidsAndKnots.YoungDiagramKernelPincer.tiltNorm k 0 = (Nat.factorial k : ℝ) :=
  QOU.BraidsAndKnots.PlancherelNormalisation.tiltNorm_zero_eq_factorial k

end QOU.BraidKnot.WedderburnUnconditional

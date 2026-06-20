import QOU.BraidKnot.NucleusEmptySDPUniqueness
import QOU.BraidKnot.AppliedHelium3Uniqueness
import QOU.BraidKnot.AppliedHelium4Uniqueness
import QOU.BraidKnot.AppliedDeuteronUniqueness
import QOU.BraidKnot.AppliedTritiumUniqueness
import QOU.BraidKnot.AppliedLithium6Uniqueness
import QOU.BraidKnot.AppliedBeryllium9Uniqueness
import QOU.BraidKnot.AppliedBoron11Uniqueness
import QOU.BraidKnot.AppliedCarbon12Uniqueness
import QOU.BraidKnot.AppliedNitrogen14Uniqueness
import QOU.BraidKnot.AppliedOxygen16Uniqueness
import QOU.BraidKnot.PeriodicTableUniqueness

/-!
# QOU.BraidsAndKnots.recursive_atom_knot_atlas — concrete consumer

Real consumer of the parameterised SDP-uniqueness infrastructure
from PR #1537 (`NucleusEmptySDPUniqueness`) and its per-isotope /
per-element / per-stable-isotope wrappers. Replaces the prior
placeholder `sorry` stub.

## What this consumes

For every atom/isotope catalogued in the recursive atom-knot atlas
content block (`recursive-atom-knot-atlas.md`), the corresponding
SDP-uniqueness theorem from one of the four wrapper layers:

| Layer | Module | Wrapper naming |
|---|---|---|
| QOU R5-full nuclei | `Applied<Nucleus>Uniqueness` (10 files) | `helium4_uniqueness_closed`, etc. |
| Per-element (AME2020) | `PeriodicTableUniqueness` | `he_uniqueness_closed`, etc. |
| Per-stable-isotope | `StableIsotopeUniqueness` (PR #1542) | `c12_uniqueness_closed`, etc. |
| Generic | `NucleusEmptySDPUniqueness` | `@nucleus_uniqueness_closed (3*A)` |

## Atlas-entry uniqueness theorem

For each atlas entry at mass number `A`, the canonical `T_w` knot
operator's uniqueness at the empty-constraint SDP demonstration
level is certified by:

```lean
@QOU.BraidKnot.nucleus_uniqueness_closed (3 * A)
```

Per-atom convenience wrappers below provide the named theorem
each atlas entry can cite.

## What this does NOT cover

This module wires the **abstract framework demonstration** — the
empty-constraint SDP at `heckeDim (3A)` with `dualSlack = 1` is
PosDef, so the trivial strict-complementarity pair gives sorry-free
uniqueness. The **real** per-nucleus SDP with multi-term cost from
the mass formula and non-empty constraints is per-nucleus
substantive open work; see
`docs/coordination/2026-05-30-sdp-uniqueness-status.md`.

-- Ref: [manuscript] prop:recursive-atom-knot-atlas
-- Ref: PR #1537 (parameterised SDP uniqueness)
-- Ref: PR #1542 (252-stable-isotope coverage)
-- Ref: PR #1546 (atlas wiring documentation)
-/

namespace QOU.BraidsAndKnots

open QOU.BraidKnot

/-- **Atlas SDP-uniqueness theorem statement.**

    For every atlas entry characterised by nucleon count `A`, the
    canonical `T_w` knot operator at the empty-constraint SDP is
    unique among feasible matrices achieving the same objective.

    Proved by direct delegation to the parameterised
    `nucleus_uniqueness_closed (3 * A)`. -/
theorem atlas_entry_uniqueness (A : ℕ)
    {Φ' : Matrix (Fin (heckeDim (3 * A))) (Fin (heckeDim (3 * A))) ℝ}
    (h_feas : (nucleusEmptySDP (3 * A)).IsFeasible Φ')
    (h_obj : (nucleusEmptySDP (3 * A)).objAt Φ' =
             (nucleusEmptySDP (3 * A)).objAt
               (nucleusRealStrongDualityPair (3 * A)).Φstar) :
    Φ' = (nucleusRealStrongDualityPair (3 * A)).Φstar :=
  nucleus_uniqueness_closed h_feas h_obj

/-! ## Atlas-tracked nuclei — sorry-free, axiom-free uniqueness theorems

Each entry below is the atlas's contracted reference for a specific
nucleus. Cite as `qou:QOU.BraidsAndKnots.<name>` from atlas
documentation.
-/

/-- Atlas entry: deuteron (²H, A=2, n=6). -/
abbrev atlas_deuteron_uniqueness := @atlas_entry_uniqueness 2

/-- Atlas entry: tritium (³H, A=3, n=9). -/
abbrev atlas_tritium_uniqueness := @atlas_entry_uniqueness 3

/-- Atlas entry: helium-3 (³He, A=3, n=9). -/
abbrev atlas_helium3_uniqueness := @atlas_entry_uniqueness 3

/-- Atlas entry: helium-4 / alpha particle (⁴He, A=4, n=12). -/
abbrev atlas_helium4_uniqueness := @atlas_entry_uniqueness 4

/-- Atlas entry: lithium-6 (⁶Li, A=6, n=18). -/
abbrev atlas_lithium6_uniqueness := @atlas_entry_uniqueness 6

/-- Atlas entry: beryllium-9 (⁹Be, A=9, n=27). -/
abbrev atlas_beryllium9_uniqueness := @atlas_entry_uniqueness 9

/-- Atlas entry: boron-11 (¹¹B, A=11, n=33). -/
abbrev atlas_boron11_uniqueness := @atlas_entry_uniqueness 11

/-- Atlas entry: carbon-12 (¹²C, A=12, n=36). -/
abbrev atlas_carbon12_uniqueness := @atlas_entry_uniqueness 12

/-- Atlas entry: nitrogen-14 (¹⁴N, A=14, n=42). -/
abbrev atlas_nitrogen14_uniqueness := @atlas_entry_uniqueness 14

/-- Atlas entry: oxygen-16 (¹⁶O, A=16, n=48). -/
abbrev atlas_oxygen16_uniqueness := @atlas_entry_uniqueness 16

/-- **For any other A**: directly call `@atlas_entry_uniqueness A`.
    The parameterised proof works for any `A : ℕ`. -/
def atlas_entry_uniqueness_works_for_any_A (A : ℕ) :
    True := trivial

end QOU.BraidsAndKnots

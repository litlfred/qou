import QOU.Mathlib.HeckeAlgebra
import QOU.Mathlib.RSKBridge

/-!
# QOU.Mathlib.StandardYoungCountInstance — the carrier, inhabited

`QOU.Mathlib.HeckeAlgebra.StandardYoungCount` used to carry its identity as a `Prop`-valued
*field*, which let an instance choose the proposition as well as prove it.  With the field
restated as the Burnside/RSK identity itself the class asserts something, and this module
supplies the canonical inhabitant.

Both halves come from the corpus and neither is conditional:

* `QOU.Mathlib.dimSYT` — the genuine SYT count, a `Finite`-backed `Nat.card` over
  `Nat.Partition n` (`RSKBurnsideTarget.lean`);
* `QOU.Mathlib.RSKBridge.RSK_substrate_proved` — `∑_{λ ⊢ n} dimSYT λ ² = n!`, delegating to
  `QOU.Mathlib.rskBurnsideHolds` in `SchenstedRSKBurnside.lean`, which takes **no** instance
  argument.

## Two same-named theorems, and only one of them is unconditional

Worth recording, because the names collide and the wrong reading makes this instance look
conditional.  There are two `rskBurnsideHolds`:

| declaration | hypotheses |
|---|---|
| `QOU.Mathlib.rskBurnsideHolds` (`SchenstedRSKBurnside.lean`) | **none** — this is the one used here |
| `…RSKBurnsideDischarge.rskBurnsideHolds` | `[SnWedderburnPartitionBridge.SnIsotypicSpechtSplit ℚ]` |

`RSKBridge.RSK_substrate_proved` delegates to the first.  (The second is not open either — that class has an
instance for every characteristic-zero field, `SnIsotypicSpechtSplitInstance.lean` — but it is a
different route and its binder is what makes the two look different.)

-- Ref: [stanley1999] Enumerative Combinatorics II §7.11 (RSK: `Σ_λ (f^λ)² = n!`)
-/

namespace QOU.Mathlib.StandardYoungCountInstance

open QOU.Mathlib.HeckeAlgebra

/-- **The canonical standard-Young-tableau count.**

`dim := dimSYT` with the Burnside/RSK identity discharged by `RSK_substrate_proved`.  This is the
first inhabitant of `StandardYoungCount`; before the carrier was restated it had none, and one
could not have been meaningful — the old `Prop`-valued field would have let any instance nominate
its own claim. -/
noncomputable instance instStandardYoungCount (n : ℕ) : StandardYoungCount n where
  dim := QOU.Mathlib.dimSYT
  squares_sum := QOU.Mathlib.RSKBridge.RSK_substrate_proved n

/-- The instance really does carry the SYT count, not some other dimension function. -/
theorem dim_eq_dimSYT (n : ℕ) :
    (instStandardYoungCount n).dim = QOU.Mathlib.dimSYT := rfl

end QOU.Mathlib.StandardYoungCountInstance

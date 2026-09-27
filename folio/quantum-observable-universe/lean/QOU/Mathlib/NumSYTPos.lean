import QOU.BraidKnot.SytRowSuperstandard
import QOU.Mathlib.RSKBurnsideTarget

/-!
# `#SYT(μ) > 0` — positivity of the standard-tableau count

`numStandardYoungTableaux μ = Nat.card (StandardYoungTableau μ)`, so positivity
is `Nat.card_pos` given the two instances the corpus already carries:

* `QOU.Mathlib.StandardYoungTableau.instFinite` — finiteness, via the injective
  encoding in `QOU/Mathlib/StandardYoungTableau.lean`;
* `QOU.BraidKnot.instNonemptyStandardYoungTableau` — nonemptiness, sorry-free,
  witnessed by the **row-superstandard** tableau (fill `1, 2, …, |μ|` reading
  each row left to right, top row first) built in
  `QOU/BraidKnot/SytRowSuperstandard.lean`. Despite living in the `QOU.BraidKnot`
  namespace, that instance is for the `QOU.Mathlib` tableau type — the two
  same-named types are bridged in `QOU/BraidKnot/SytMathlibBridge.lean`.

**No nonemptiness hypothesis on `μ` is needed.** The empty diagram carries
exactly one standard tableau — the empty one — so the count is `1`, not `0`.
This is why `dimSYT_pos` below is unconditional even though the manuscript
statement it discharges (`seminormalDim_pos`) carried a `0 < n` hypothesis.

Both instances predate this file; nothing here is new mathematics. What was
missing was only the one-line consequence, which is why
`QOU.HeckeAlgebra.seminormalDim_pos` stood as a cited `axiom` while its content
was already proved a few modules away.
-/

namespace QOU.Mathlib

open YoungDiagram

/-- **`#SYT(μ) > 0`** for every Young diagram, the empty one included. -/
theorem numStandardYoungTableaux_pos (μ : YoungDiagram) :
    0 < numStandardYoungTableaux μ :=
  Nat.card_pos

/-- **`dim(p) > 0`** for every partition — the standard-tableau dimension of a
partition's shape is positive. -/
theorem dimSYT_pos {n : ℕ} (p : Nat.Partition n) : 0 < dimSYT p :=
  numStandardYoungTableaux_pos _

end QOU.Mathlib

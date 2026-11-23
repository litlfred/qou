import QOU.Shared.MarkovTraceClaim
import Mathlib.Data.Real.Basic

/-!
# QOU.Shared.ArchimedeanEval — tying `q_real` to the inherited `q : R`

Bean `qou-mt7r` / `qreal`. Four `MarkovTraceContext` descendants live past the
§7c wall and use `q_real : ℝ`:

* `QOU/Information/reeb_operations_per_planck.lean`
* `QOU/Information/toffoli_transfer_matrix.lean`
* `QOU/Observations/brane_tower_q_laplacian_decay.lean`
* `QOU/Observations/strangelet_crossing_energy.lean`

Each is genuinely archimedean — `1 < q_real`, `Real.sqrt q_real`, `inv_pos`,
`linarith` — so `ℝ` is the right type. The defect was that **nothing related
`q_real` to the inherited `q : R`**. The docstrings called it "the
specialisation of the generic shared `q : R`"; the type said no such thing.
`q_real` was an independent field, so a context could set `q_real := 37` while
carrying a Hecke algebra over an entirely unrelated `q`, and every proposition
downstream still held. The claims were archimedean statements about *a* real
number, not about *this* universe's substrate parameter.

## What this fixes, and what it does not

`ArchimedeanEval` carries a ring homomorphism `eval : R →+* ℝ` and **derives**
`q_real := eval q` rather than letting it be posited. The independent field is
gone, so the two can no longer disagree by construction.

`q_real_one_of_q_one` is the payoff and the test of whether the tie is worth
anything: `q = 1 → q_real = 1`. It is a one-line consequence of `eval` being a
ring hom, and it was **not provable at all** before — with `q_real` independent,
the classical limit of the substrate parameter said nothing about the classical
limit of the real one.

**This is not the archimedean τ-functor, and inhabiting it is not progress on
that wall.** `QOU/Archimedean/TauFunctorTargetSpec.lean` makes the distinction
machine-checked for its own interface — `interface_alone_is_trivially_inhabitable`
shows a bare diagonal matrix inhabits it — and the same caution applies here:
`ofRingHom` below builds an `ArchimedeanEval` from **any** ring hom at all, with
no functoriality, no naturality, and no reference to the braided category. So an
`ArchimedeanEval` instance is not evidence that the functor exists. What the
mixin buys is exactly one thing — `q_real` is *some* ring-homomorphic image of
`q` rather than an unrelated real — and that is enough to make the three
propositions statements about the substrate parameter.

The genuine τ-functor would *supply* this `eval` with provenance. Until it
exists, `eval` is a hypothesis, and it is labelled as one.

## Not a second parallel mechanism

Bean `qou-mt7r` warns that whatever τ gets introduced "should be the one
`qou-mt7r` needs, not a second parallel mechanism", and `qou-6ome` left the
same debt on the other side of the corpus: `SubstrateParameter` (categorical,
`M → R_q`) and `ArchimedeanSubstrateField` (`M → ℝ`) are also untied.

They are the same need, and the shared mechanism is not a new abstraction — it
is `RingHom _ ℝ`, which Mathlib already has. `ArchimedeanEval` invents nothing;
it is `MarkovTraceContext` plus a `R →+* ℝ`. The `qou-6ome` side should carry
an `R_q →+* ℝ` in the same way rather than growing its own notion, and there
`eval` is genuinely *constructible* — `R_q = LaurentPolynomial ℤ`, so evaluation
at a nonzero real is an ordinary ring hom, not a hypothesis. That asymmetry is
worth knowing before copying this file: here `R` is an opaque `CommRing`, so
`eval` has to be assumed; there it does not.

## Why a sibling mixin rather than extending the parent

Bean `qou-mt7r` route 1 proposed adding the evaluation to
`MarkovTraceContext` itself. That parent has 15 descendants, 12 of which are
correctly pre-archimedean and have no business carrying a map to `ℝ`. Extending
it would put an archimedean field on every one of them — the §7c wall in
reverse. A mixin costs the three archimedean descendants one word in their
`extends` clause and leaves the other twelve untouched.

-- Ref: [leitner2026] quantum-observable-universe/information-theory/reeb-operations-per-planck.md
-/

namespace QOU.Shared

/-- A `MarkovTraceContext` together with an **assumed** archimedean evaluation
    `R →+* ℝ`.

    The ring-homomorphism requirement is what carries the content: it forces
    `eval 1 = 1` and `eval` to respect the ring operations, so `q_real` moves
    with `q` instead of floating free. -/
class ArchimedeanEval extends MarkovTraceContext where
  /-- The archimedean evaluation. **Assumed, not constructed** — see the module
      docstring. The τ-functor that would supply it with provenance is open. -/
  eval : letI := ringR; R →+* ℝ

/-- The real substrate parameter, **derived** as `eval q` rather than posited.

    Kept under the name the three descendants already used, so every existing
    `ctx.q_real` call site reads identically: dot notation resolves to this
    definition exactly as it resolved to the field it replaces. -/
noncomputable def ArchimedeanEval.q_real (ctx : ArchimedeanEval) : ℝ :=
  letI := ctx.ringR
  ctx.eval ctx.q

/-- **The classical limit now transfers.** `q = 1 → q_real = 1`.

    This is the whole point of the mixin. With `q_real` an independent field it
    was not provable — `q = 1` constrained nothing about the real parameter, so
    a context could sit at the classical value of the substrate parameter and at
    an arbitrary real one simultaneously. -/
theorem ArchimedeanEval.q_real_one_of_q_one (ctx : ArchimedeanEval)
    (hq : letI := ctx.ringR; ctx.q = 1) : ctx.q_real = 1 := by
  letI := ctx.ringR
  unfold ArchimedeanEval.q_real
  rw [hq]
  exact map_one ctx.eval

/-- **The mixin demands nothing beyond a ring hom** — no functoriality, no
    naturality, no reference to the braided category.

    Stated as a constructor rather than left implicit, in the manner of
    `TauFunctorTargetSpec.interface_alone_is_trivially_inhabitable`: the reader
    who sees an `ArchimedeanEval` instance downstream should be able to check,
    mechanically, how little it took to build one. Anything claiming to be the
    archimedean τ-functor has to clear a bar this constructor does not. -/
def ArchimedeanEval.ofRingHom (ctx : MarkovTraceContext)
    (f : letI := ctx.ringR; ctx.R →+* ℝ) : ArchimedeanEval :=
  { ctx with eval := f }

end QOU.Shared

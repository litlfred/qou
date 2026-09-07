import QOU.Mathlib.HeckeAlgebra

/-!
# Probe: does `QOU.Mathlib.HeckeAlgebra.IwahoriHeckeAlgebra` encode its
# presentation, or only name it?

**Scope first, because the name is ambiguous.** There are TWO
`IwahoriHeckeAlgebra` declarations in the tree and this probe analyses exactly
one of them:

* `QOU.Mathlib.HeckeAlgebra.IwahoriHeckeAlgebra` — a `class`, the subject here;
* `QOU.BraidKnot.IwahoriHeckeAPI.IwahoriHeckeAlgebra` — a *different*
  `structure`, carrying `Ring`/`StarRing` on its carrier and stating the Hecke
  relations as SEPARATE AXIOMS rather than as instance-chosen `Prop` fields.
  **Nothing below applies to it.**

Both describe themselves as placeholders. Do not read this probe as a statement
about "the framework's Hecke algebra" — read it as a statement about the first
of two placeholders, which is what it is.

**🛑 THE DEFECT THIS PROBE FOUND WAS CLOSED ON 2026-09-07.  Read the finding as
history and the Lean below as a regression witness — not as a live report.**

**What it found (and this half stands).**  The class declared the three
relations of AGENTS.md §7a as BARE `Prop` FIELDS, each with a sibling field
proving it:

```lean
  /-- **Hecke relation**: `(σ_i - q)(σ_i + q⁻¹) = 0` … -/
  hecke_relation : Prop
  hecke_holds : hecke_relation
```

An instance therefore CHOSE what `hecke_relation` meant, and this probe
constructed one that chose `True` and satisfied the whole class.

**What replaced it.**  `hecke`, `braid` and `far_commute` are now equations in
the class's own `mul`, `smul`, `one` and `sigma`, so a model has to satisfy
them.  The class gained a `smul` field (the Hecke relation has a coefficient
and cannot be stated without one) and `carrier_addCommGroup` became
instance-implicit so `+` is available in the relation types.  `q⁻¹` is
`Ring.inverse q`, since the class is over a `CommRing`, which has no `Inv`.

**What the closure has to be measured against, or it is only a rewrite.**  A
relation field can be made honest and still be satisfied only by the zero
algebra, which is the `qou-z9ws` inhabitation discriminator: *satisfying a
constraint over `PUnit` is evidence the axioms are consistent and no evidence
they constrain anything.*  So the same change added `H3.heckeAlgebra`, a model
on the six-dimensional `H3Carrier R` with the concrete `H3.mul`, whose three
relations were already proved in that file and had, until then, no class that
could consume them.  `H3.heckeAlgebra_nondegenerate` witnesses `σ₁ ≠ 1` there.
Both models are now needed to read the class: `triv_hecke` says the axioms are
consistent, `H3.heckeAlgebra` says they are not vacuous.

What this DOES establish:

* the class is inhabited at every ring, size and parameter
  (`hecke_class_always_inhabited`);
* in that instance every generator is the ring unit, so `σ·σ = 1`, while §7a's
  relation demands `(q − q⁻¹)·σ + 1` — over `ℚ` at `q = 2` that is `5/2`
  (`degenerate_sigma_sq`, `degenerate_violates_hecke_at_two`);
* all three relation fields are literally `True` there
  (`degenerate_hecke_relation_is_True`, `degenerate_other_relations_are_True`).

So `[IwahoriHeckeAlgebra R n q]` as a hypothesis buys a carrier type, an
`AddCommGroup`, a `one`, a `mul` and a `sigma` family.  Nothing Hecke.

What this did NOT establish, and the distinction is the whole severity
question: **no downstream result was corrupted by it.**  Measured on `content/`
2026-08-30, `hecke_holds`, `hecke_relation`, `braid_holds` and
`far_commute_holds` had **ZERO consumers** — no declaration anywhere read
them — and none of the 10 `[IwahoriHeckeAlgebra …]`-conditional declarations
restated the relations as its own hypothesis.  The fields were write-only.
Nothing false was derived FROM them; the defect was that the class did not mean
what its docstrings said.

That measurement is also why the 2026-09-07 repair was cheap and is worth
recording as such: with no consumers there was nothing to migrate, so the whole
blast radius was the class, its one model, and this probe.  A defect found late
is not always expensive — but only a consumer count says which kind it is, and
the count has to be taken before the fix, not inferred from how the fix went.

Incidental, and it corroborated the reading: the CLASS provided no `One` or
`Mul` typeclass instance for `carrier` — only `one` and `mul` FIELDS — so the
presentation could not be stated in the class's own vocabulary without
projecting those fields.  The first draft of this probe failed to elaborate for
exactly that reason.

**The repair took the projection route rather than adding `Ring carrier`**, so
this observation still describes the class: `hecke` is written
`mul (sigma i) (sigma i) = …`, not `σ * σ = …`.  A `Ring`/`Algebra` carrier
would read better and is the shape Mathlib would want upstream; it is a larger
change than encoding the relations and was deliberately not bundled with it.

**Prior art, and my own corpus-grep failure.** `triv_hecke` (a hundred lines
below the class) ALREADY constructed a satisfying instance with all three
relations `True`, over `PUnit`, and cites its own probe
(`docs/audits/2026-08-23-trivial-global-instance-probe.lean`).  It was
deliberately demoted from `instance` to `def` for a related reason.  So the
INHABITATION half of this probe re-derived something the corpus already held,
and a grep for `hecke_relation :=` before writing it would have found it.  What
was new here was the FALSIFICATION half — a concrete `q` at which §7a's
relation is false in a satisfying instance, which `triv_hecke` does not state.

To run (needs the QOU oleans; `QOU.Mathlib.HeckeAlgebra` only):

    ROOT=$PWD; LP=""
    for d in "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do LP="$LP$d:"; done
    LEAN_PATH="$LP$ROOT/content/quantum-observable-universe/lean/.lake/build/lib/lean" \
      lean scripts/lean/probes/prop-field-carrier-vacuity.lean

Verified exit 0 on lean-v4.24.0 — 2026-08-30 as the defect report, and again
2026-09-07 as the regression witness after the repair.  Bean `qou-qcy6`.
-/

namespace QOU.Probe.PropFieldVacuity
open QOU.Mathlib.HeckeAlgebra

/-! ### The falsification, kept verbatim

The probe's original `degenerate` set every generator to the RING UNIT over
carrier `R` and chose `hecke_relation := True`.  Its point was this
inequality — §7a demands `σ² = (q − q⁻¹)·σ + 1`, so over `ℚ` at `q = 2` a
model with `σ = 1` would need `1 = 5/2`.  The statement is about rational
arithmetic, not about the class, so it is unaffected by the repair and is left
exactly as it was written. -/

/-- §7a's relation demands `σ² = (q − q⁻¹)·σ + 1`.  Over `ℚ` at `q = 2` that
    right-hand side is `5/2`, not `1`. -/
theorem degenerate_violates_hecke_at_two :
    ((2 : ℚ) - (2 : ℚ)⁻¹) * 1 + 1 ≠ (1 : ℚ) := by norm_num

/-! ### The regression witness

What changed is what that inequality now *costs*.  Before the repair it was a
true statement about a model that satisfied the class anyway; the relation
fields were `Prop` variables and the arithmetic never had to hold.  Now the
`hecke` field IS that equation, so the same all-generators-are-one assignment
is not a model at all — the field cannot be discharged.

Stated as arithmetic rather than as `¬ ∃ H, …`: the obstruction is entirely in
the numbers, and pinning it there keeps the witness readable and independent of
how the class is spelled next time. -/

/-- The unit-generator assignment is now **rejected** by the class at `q = 2`
    over `ℚ`: discharging `hecke` would require `1 * 1 = (2 − 2⁻¹) • 1 + 1`.

    `Ring.inverse` rather than `⁻¹` because that is what the class field says;
    the two agree over a `GroupWithZero` unconditionally. -/
theorem unit_generators_rejected_at_two :
    ¬ ((1 : ℚ) * 1 = ((2 : ℚ) - Ring.inverse (2 : ℚ)) • (1 : ℚ) + 1) := by
  norm_num [Ring.inverse_eq_inv']

/-- The class is still inhabited — the repair did not make it unsatisfiable,
    which is the failure mode a relation-tightening most often has. -/
theorem hecke_class_still_inhabited (R : Type) [CommRing R] (n : ℕ) (q : R) :
    Nonempty (IwahoriHeckeAlgebra R n q) := ⟨triv_hecke R n q⟩

/-- …and it is inhabited **non-degenerately**, which is the claim `triv_hecke`
    alone cannot support.  `H3.heckeAlgebra` puts the three relations on a
    carrier where `σ₁ ≠ 1`. -/
theorem hecke_class_inhabited_nondegenerately (q : ℚ) :
    ∃ H : IwahoriHeckeAlgebra ℚ 3 q,
      H.sigma ⟨0, by norm_num⟩ ≠ H.one :=
  ⟨H3.heckeAlgebra q, H3.heckeAlgebra_nondegenerate q⟩

end QOU.Probe.PropFieldVacuity

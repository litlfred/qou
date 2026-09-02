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

**Result: only name it.**  The class declares the three relations of AGENTS.md
§7a as BARE `Prop` FIELDS, each with a sibling field proving it:

```lean
  /-- **Hecke relation**: `(σ_i - q)(σ_i + q⁻¹) = 0` … -/
  hecke_relation : Prop
  hecke_holds : hecke_relation
```

An instance therefore CHOOSES what `hecke_relation` means.  Everything below
constructs one that chooses `True`, and it satisfies the whole class.

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

What this does NOT establish, and the distinction is the whole severity
question: **no downstream result is corrupted by it.**  Measured on `content/`
2026-08-30, `hecke_holds`, `hecke_relation`, `braid_holds` and
`far_commute_holds` have **ZERO consumers** — no declaration anywhere reads
them — and none of the 10 `[IwahoriHeckeAlgebra …]`-conditional declarations
restates the relations as its own hypothesis.  The fields are write-only.
Nothing false is derived FROM them; the defect is that the class does not mean
what its docstrings say.

Incidental, and it corroborates the reading: the CLASS provides no `One` or
`Mul` typeclass instance for `carrier` — only `one` and `mul` FIELDS — so the
presentation cannot be stated in the class's own vocabulary without projecting
those fields.  (The carrier type may of course have such instances of its own;
the class does not require or expose them.)  The first draft of this probe
failed to elaborate for exactly that reason.

**Prior art, and my own corpus-grep failure.** `triv_hecke`
(`HeckeAlgebra.lean:174`, a hundred lines below the class) ALREADY constructs a
satisfying instance with all three relations `True`, over `PUnit`, and cites its
own probe (`docs/audits/2026-08-23-trivial-global-instance-probe.lean`).  It was
deliberately demoted from `instance` to `def` for a related reason.  So the
INHABITATION half of this probe re-derives something the corpus already held,
and a grep for `hecke_relation :=` before writing it would have found it.  What
is new here is the FALSIFICATION half — `degenerate_sigma_sq` together with
`degenerate_violates_hecke_at_two` exhibits a concrete `q` at which §7a's
relation is false in a satisfying instance, which `triv_hecke` does not state.

To run (needs the QOU oleans; `QOU.Mathlib.HeckeAlgebra` only):

    ROOT=$PWD; LP=""
    for d in "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do LP="$LP$d:"; done
    LEAN_PATH="$LP$ROOT/content/quantum-observable-universe/lean/.lake/build/lib/lean" \
      lean scripts/lean/probes/prop-field-carrier-vacuity.lean

Verified exit 0 on lean-v4.24.0, 2026-08-30.  Bean `qou-qcy6`.
-/

namespace QOU.Probe.PropFieldVacuity
open QOU.Mathlib.HeckeAlgebra

/-- An instance in which every generator is the RING UNIT and each of the three
    presentation relations is `True`. -/
noncomputable def degenerate (R : Type) [CommRing R] (n : ℕ) (q : R) :
    IwahoriHeckeAlgebra R n q where
  carrier := R
  carrier_addCommGroup := inferInstance
  one := 1
  mul := fun a b => a * b
  sigma := fun _ => 1
  hecke_relation := True
  hecke_holds := trivial
  braid_relation := True
  braid_holds := trivial
  far_commute := True
  far_commute_holds := trivial

/-- The class is inhabited at EVERY ring, size and parameter. -/
theorem hecke_class_always_inhabited (R : Type) [CommRing R] (n : ℕ) (q : R) :
    Nonempty (IwahoriHeckeAlgebra R n q) := ⟨degenerate R n q⟩

/-- Every generator is the ring unit in that instance. -/
theorem degenerate_sigma_eq_one (R : Type) [CommRing R] (n : ℕ) (q : R)
    (i : Fin (n - 1)) : (degenerate R n q).sigma i = (1 : R) := rfl

/-- So `σ_i · σ_i = 1`, expressed through the class's OWN `mul`. -/
theorem degenerate_sigma_sq (R : Type) [CommRing R] (n : ℕ) (q : R)
    (i : Fin (n - 1)) :
    (degenerate R n q).mul ((degenerate R n q).sigma i)
                           ((degenerate R n q).sigma i) = (1 : R) := by
  show (1 : R) * 1 = 1
  ring

/-- §7a's relation would demand `σ² = (q − q⁻¹)·σ + 1`.  Over `ℚ` at `q = 2`
    that right-hand side is `5/2`, not `1`: the relation is FALSE in this
    instance, which satisfies the class anyway. -/
theorem degenerate_violates_hecke_at_two :
    ((2 : ℚ) - (2 : ℚ)⁻¹) * 1 + 1 ≠ (1 : ℚ) := by norm_num

/-- Because `hecke_relation` is a bare `Prop` field this instance takes to be `True`. -/
theorem degenerate_hecke_relation_is_True (R : Type) [CommRing R] (n : ℕ) (q : R) :
    (degenerate R n q).hecke_relation = True := rfl

/-- Same for the other two presentation relations. -/
theorem degenerate_other_relations_are_True (R : Type) [CommRing R] (n : ℕ) (q : R) :
    (degenerate R n q).braid_relation = True
    ∧ (degenerate R n q).far_commute = True := ⟨rfl, rfl⟩

end QOU.Probe.PropFieldVacuity

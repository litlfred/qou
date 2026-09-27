import QOU.Torsion.KnotParticleGeneration

/-!
# Probe: the decoy-hypothesis shape, and what is actually wrong with it

Subject: `QOU.Torsion.KnotParticleGenerationContext`.  Chosen because it is the
shape in its simplest form and its import cone needs no real arithmetic.

```lean
  particle_spectrum_generated : Prop            -- the decoy
  generation_active : particle_spectrum_generated
  impl_knot_particle_generation :
    particle_spectrum_generated -> n_linking_ops = 2 /\ ...
```

**CORRECTION to my own first reading (2026-08-30, same day).**  An earlier draft
of the audit doc said: take the `Prop` to be `True` and each `impl_` field "is
the conclusion, assumed", implying the class permits FALSE conclusions.  **That
is wrong.**  An instance must supply both `generation_active : P` and
`impl : P -> C`, so it must supply `C`; the conclusion therefore holds in every
instance and the class does constrain it.  Trying to build a counter-instance is
what showed this — the obligation cannot be discharged.

**The defect is not unsatisfiability, it is ELIMINABILITY.**  The decoy carries
no information: a class asserting the conclusion outright is interderivable.
`toStripped` / `ofStripped` below exhibit both directions, `ofStripped` taking
the decoy proposition to be `True`.  So `knot_particle_generation`'s proof
`ctx.impl_… ctx.generation_active` derives nothing — it projects an assumption
through an arrow that could be deleted.

**Why `proof-no-self-assuming-projection` misses it.**  That criterion looks for
a proof term that IS a projection, `ctx.field`.  Here the term is
`ctx.field ctx.other_field`, an APPLICATION.  The intervening arrow is exactly
what makes it read as a derivation from a stated hypothesis, and exactly what
hides it.

To run:

    ROOT=$PWD; LP=""
    for d in "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do LP="$LP$d:"; done
    LEAN_PATH="$LP$ROOT/folio/quantum-observable-universe/lean/.lake/build/lib/lean" \
      lean scripts/lean/probes/decoy-hypothesis-eliminable.lean

Verified exit 0 on lean-v4.24.0, 2026-08-30.  Bean `qou-qcy6`.
-/

namespace QOU.Probe.DecoyHypothesis
open QOU.Torsion

/-- A satisfying instance whose "particle spectrum is generated" proposition is
    `True`, discharged by `trivial`. -/
def decoy : KnotParticleGenerationContext where
  Link := Unit
  is_torus_generator := fun _ _ _ => False
  n_linking_ops := 2
  particle_spectrum_generated := True
  generation_active := trivial
  impl_knot_particle_generation := fun _ => ⟨rfl, fun _ _ _ h => absurd h not_false⟩

/-- The decoy is inhabited, so the class constrains nothing by emptiness. -/
theorem context_inhabited : Nonempty KnotParticleGenerationContext := ⟨decoy⟩

/-- Its "hypothesis" is literally `True`. -/
theorem decoy_hypothesis_is_True : decoy.particle_spectrum_generated = True := rfl

/-! ### The decoy is ELIMINABLE — the real content

The class is not unsatisfiable; the point is sharper.  Because an instance must
supply BOTH `generation_active : P` and `impl : P → C`, it must supply `C`.  So
the arrow adds nothing: a class asserting `C` outright is equivalent. -/

/-- The stripped form: the conclusion, asserted, with no decoy. -/
class Stripped where
  Link : Type
  is_torus_generator : Link → ℕ → ℕ → Prop
  n_linking_ops : ℕ
  conclusion : n_linking_ops = 2 ∧
    ∀ (K : Link) (m n : ℕ), is_torus_generator K m n → Nat.Coprime m n

/-- Every decoy-shaped context yields a stripped one — the arrow is discharged
    by the class's own `generation_active`, so nothing was ever hypothetical. -/
def toStripped (ctx : KnotParticleGenerationContext) : Stripped where
  Link := ctx.Link
  is_torus_generator := ctx.is_torus_generator
  n_linking_ops := ctx.n_linking_ops
  conclusion := ctx.impl_knot_particle_generation ctx.generation_active

/-- And every stripped one yields a decoy-shaped context, taking the decoy
    proposition to be `True`.  The two are interderivable: the hypothesis
    `particle_spectrum_generated` carries no information. -/
def ofStripped (s : Stripped) : KnotParticleGenerationContext where
  Link := s.Link
  is_torus_generator := s.is_torus_generator
  n_linking_ops := s.n_linking_ops
  particle_spectrum_generated := True
  generation_active := trivial
  impl_knot_particle_generation := fun _ => s.conclusion

/-- The round trip is the identity on the data that matters. -/
theorem roundtrip (s : Stripped) :
    (toStripped (ofStripped s)).n_linking_ops = s.n_linking_ops := rfl

end QOU.Probe.DecoyHypothesis

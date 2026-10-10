---
# qou-uno5
title: instSl2DemazureSubcrystal re-trivialises the demazure_closure field that was strengthened away from True
status: completed
type: bug
priority: normal
created_at: 2026-08-24T19:39:02Z
updated_at: 2026-08-24T21:04:08Z
---

`QOU/Machinery/KashiwaraCrystalBasic.lean:215`, verified present 2026-08-24.

## The tell is in the class, not the instance

`DemazureSubcrystal.demazure_closure` carries an annotation somebody left
deliberately (line 188):

```
  /-- **Demazure closure** (was `True`): the sub-crystal is closed under
      lowering by the first `level` simple roots -- exactly the operators
      in the support of the length-`level` Weyl word. -/
  demazure_closure :
    forall (i : N), i < level -> forall (v w : G.V),
      member v -> G.f i v = some w -> member w
```

So the field **was** `True` and was strengthened into a real closure condition.
That was the right repair. Then the only witness in the corpus undoes it:

```
instance instSl2DemazureSubcrystal : DemazureSubcrystal standardSl2Crystal 1 where
  member := fun _ => True
  highest := false
  highest_mem := trivial
  highest_isHighest := fun _ => by simp [standardSl2Crystal]
  demazure_closure := fun _ _ _ _ _ _ => trivial
```

`member := fun _ => True` makes the sub-crystal the whole crystal, so closure
under lowering is trivially true and `demazure_closure` closes by `trivial` —
back to exactly the strength the field had before it was strengthened. The
strengthening bought nothing while this is the only inhabitant.

Its docstring calls this *"a **genuine** `DemazureSubcrystal`"*, which is the
sentence that will mislead the next reader: it is genuine as an *inhabitation*
witness and empty as a *Demazure* witness. A Demazure sub-crystal is a proper
sub-object cut out by a Weyl word; the whole crystal is the degenerate case at
the longest word, not at `level = 1`.

## Blast radius

`DemazureSubcrystal` is consumed by `CompositeKashiwaraResidueA` in the same
file (which bundles it with `StembridgeCrystal` and `TypeACrystal` for the
residue-A identification). As an unguarded `instance`,
`instSl2DemazureSubcrystal` resolves for `standardSl2Crystal` everywhere, so any
conditional statement over that crystal gets the full-crystal witness for free.

## Disposition

The honest `level = 1` sub-crystal of B(Lambda_1) is *not* everything: it should be
the `f_1`-closure of the highest-weight vertex, which for the two-element sl2
crystal is both vertices — so `member := fun _ => True` may well be the
*correct value* here, and the defect is then presentational rather than
mathematical. That is the thing to settle first, and it is a five-minute read of
`standardSl2Crystal`.

- If it is correct: fix the docstring to say the level-1 Demazure sub-crystal of
  `B(Lambda_1)` **happens** to be the whole crystal, so this witness exercises
  `demazure_closure` vacuously and a non-trivial test needs a bigger crystal.
- If it is not: replace `member` with the real closure predicate.

Either way, add a witness at a rank where the sub-crystal is proper, or
`demazure_closure` has never been tested by anything.

**Detector note:** `checkNoVacuousInstanceData` does not flag this — its
degenerate-value regex is anchored, so it matches `True` but not
`fun _ => True`. One-line fix on the checker side, filed as
`folio-assistant-ilbh`.


## Resolved 2026-08-24 — FALSE POSITIVE on the mathematics; real gap was the test

**Verdict: `member := fun _ => True` is the CORRECT value.** The bean's own
"settle this first" branch is the right one. `sl₂` has one simple root, so
`W = {e, s₀}` and `B(Λ₁)` has exactly two Demazure sub-crystals: `B_e(Λ₁) =
{u_Λ}` at length 0, and `B_{s₀}(Λ₁) = {u_Λ, f₀ u_Λ}` at length 1. `standardSl2Crystal`
has `V = Bool` with the single arrow `f₀ : false ↦ true`, so the length-1 one is
**both vertices** — the whole crystal. At `level = 1` the class asks for closure
under the first 1 simple roots, i.e. `f₀` alone, and the whole crystal is the
honest answer. The instance is not a re-trivialisation; it is the degenerate case
being genuinely degenerate. Nothing was replaced.

**Consumers before the change: 10 mentions of `DemazureSubcrystal` across
`QOU/`** — 8 in `KashiwaraCrystalBasic.lean` itself (class, instance, the
`CompositeKashiwaraResidueA.has_demazure` field, and its witness
`⟨1, ⟨instSl2DemazureSubcrystal⟩⟩`), plus 2 that are **name collisions, not
consumers**: `QOU/MassTheory/DemazureSubcrystalGradedDim.lean` opens a *namespace*
called `QOU.MassTheory.DemazureSubcrystal` and never mentions this class, and
`DampingNonMonotoneWall.lean` cites that file in prose. Nothing imports
`QOU.Machinery.KashiwaraCrystalBasic`. So the class has one real consumer,
in-file.

**Kept as an `instance`, deliberately.** `DemazureSubcrystal standardSl2Crystal 1`
is a true fact about a concrete two-vertex crystal, not a conjecture, so
resolution supplying it is sound — same footing as the neighbouring
`instSl2TypeACrystal` and the `StembridgeCrystal` instance. Demoting a *correct*
witness would be noise, and `CompositeKashiwaraResidueA` names it explicitly
anyway.

**The real defects, both fixed.**

1. **Presentational.** The docstring called it *"a genuine `DemazureSubcrystal` …
   closed under lowering"*, which reads as though closure had been checked. It
   had not: with `member ≡ True` both sides of `demazure_closure` are trivially
   inhabited. Rewritten to say the level-1 sub-crystal of `B(Λ₁)` **happens** to
   be everything, that this witness therefore satisfies `demazure_closure`
   trivially, and that `highest_isHighest` is the one field it does exercise.
2. **`demazure_closure` had never been tested by anything** — the bean's last
   line, and the substantive half. Fixed with a rank where it bites:
   - `standardSl3Crystal` — `B(Λ₁)` for `sl₃`, three vertices `0 -f₀→ 1 -f₁→ 2`,
     two simple roots. An `abbrev` (not `def`) so `.V` reduces to `Fin 3` at
     reducible transparency and `decide` can see `OfNat`/`DecidableEq`/`Fintype`;
     reason recorded in its docstring.
   - `sl3DemazureLevelOne : DemazureSubcrystal standardSl3Crystal 1` with
     `member := fun v => v ≠ 2` — a **proper** sub-crystal (`{0,1}`), whose
     `demazure_closure` is a real obligation discharged by case analysis. A `def`,
     not an `instance`.
   - `sl3DemazureLevelOne_proper` — vertex `2` is not a member.
   - `sl3LevelOne_not_closed_at_level_two` — the same predicate **fails** closure
     at `level = 2`, because `f₁ : 1 ↦ 2` leaves it.
   - `sl3_singleton_not_closed_at_level_one` — the singleton `{0}` (which *is*
     `B_e(Λ₁)`) fails closure at `level = 1`, because `f₀ : 0 ↦ 1` leaves it.

   The last two pin the field down from both sides: at a fixed level it selects
   which subsets are Demazure sub-crystals, and for a fixed subset it selects
   which levels. That is what `member ≡ True` could never show, and it is now
   machine-checked rather than asserted.

**Verification.** Fresh `lean` on `KashiwaraCrystalBasic` — exit 0, no warnings.
`#print axioms` on the instance and all four new decls: `propext` /
`Quot.sound` / `Classical.choice` only, no `sorryAx`. No `sorry` in committed
work.

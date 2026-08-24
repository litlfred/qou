---
# qou-uno5
title: instSl2DemazureSubcrystal re-trivialises the demazure_closure field that was strengthened away from True
status: todo
type: bug
priority: normal
created_at: 2026-08-24T19:39:02Z
updated_at: 2026-08-24T19:39:02Z
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

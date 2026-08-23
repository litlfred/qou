---
# qou-0w42
title: 'GAP: no cat-unit electron scale, so TrefoilElectronMassConj stays dischargeable'
status: todo
type: task
priority: normal
created_at: 2026-08-23T09:27:59Z
updated_at: 2026-08-23T09:28:22Z
---

## What is open

`QOU.Interactions.TrefoilCanonicalMassUnit.TrefoilElectronMassConj` is now
parameterised (PR #5533) so the old `⟨2, 3, rfl, rfl, m_e_MeV_codata, rfl⟩`
discharge no longer typechecks. It is **not** closed. Given any `T` with
`markovTrace 2 T ≠ 0`:

```lean
example (T : HeckeElement 2) (h : markovTrace 2 T ≠ 0) :
    TrefoilElectronMassConj T 1 (1 / absMarkovTrace 2 T) := by
  constructor
  unfold categoricalMassMeV categoricalMass absMarkovTrace
  have hne : |markovTrace 2 T| ≠ 0 := abs_ne_zero.mpr h
  field_simp
  norm_num
```

elaborates (verified, lean-direct exit 0).

## Why

`m_e_cat` — "the cat-unit electron mass, distinct from the MeV-scale one"
per the module docstring — has **no definition anywhere in the corpus**.
`QOU.BraidKnot.MassFormulaCategorical` defines only `m_e_MeV_codata`, and
`categoricalMass rho m_e T_w = rho * m_e * absMarkovTrace n T_w` takes the
cat-unit scale as an argument. A free parameter appearing linearly in the
class's only equation can always be solved for.

## What would close it

Define the cat-unit electron scale (or fix `rho` and `m_e_cat` to framework
values) so the class constrains `T` alone. Then the field says something
about the trefoil's Markov trace rather than about a choice of units. Until
then the honest statement is the one now in the docstring: parameterising
raised the cost of the cheat and made it visible at the instance site, it
did not remove it.

## Not to be confused with

`markovTrace` is an `axiom` in `QOU/HeckeAlgebra/Common.lean:104`, so no
concrete trace value is available to test against either. That is a
separate limitation, not this gap.

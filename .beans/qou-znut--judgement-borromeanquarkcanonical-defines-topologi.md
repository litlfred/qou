---
# qou-znut
title: 'JUDGEMENT: BorromeanQuark.canonical defines topological_mass to be the formula it then asserts'
status: todo
type: task
priority: normal
created_at: 2026-08-24T19:39:26Z
updated_at: 2026-08-24T19:39:26Z
---

`QOU/Archimedean/BorromeanQuark.lean:114-126`, verified present 2026-08-24.
**Filed as a judgement call, not a confirmed defect** — the file argues the
other side and the argument is not stupid. Both readings below; pick one and
write the verdict into the docstring either way.

## The object

```
class BorromeanQuark where
  topological_mass : R -> R
  volume_calibrates_mass :
    forall q : R, q > 1 -> topological_mass q = borromean_volume / (1 - 1/q)^2

instance canonical : BorromeanQuark where
  topological_mass := fun q => borromean_volume / (1 - 1/q)^2
  volume_calibrates_mass := fun _ _ => rfl
```

## Reading A — this is definitional laundering

The data field is *defined* to be the right-hand side of the propositional
field, so `volume_calibrates_mass` closes by `rfl`. The class asserts that some
mass functional agrees with a volume formula; the instance answers by declaring
the functional to be that formula. Nothing connects the *physical* baryon mass
to `borromean_volume`. And it is an unguarded `instance`, so
`baryon_mass_from_volume` — stated as a 3b-cond conditional theorem — is
unconditional.

## Reading B — the file's own defence, which is pre-emptive

The instance docstring anticipates exactly this objection:

> **Faithful instance.** Defines `topological_mass` literally as the
> topological-volume formula ..., so `volume_calibrates_mass` closes by `rfl`.
> **This is genuine content — the mass-calibration identity holds definitionally
> — not a vacuous discharge.**

And the class docstring already concedes the harder half: exhibiting a
`BorromeanBaryon` value "is trivially possible and does not establish that the
physical nucleon is one", and that identification "stays an **open** conjectural
interpretation in the narrative". A former `is_baryon_realisation` field was
removed for being a self-assuming projection.

Reading B is coherent: if `topological_mass` is *by definition* the topological
quantity, then the class is a naming device and the conjecture lives entirely in
the narrative identification with physical mass — which the file says, in
writing, is open.

## What tips it, in my read

The class name and the theorem name are what a reader takes away, and they both
say *mass*. `baryon_mass_from_volume` reads as a derivation of baryon mass from
hyperbolic volume; it is a rewriting of a definition. If Reading B is the
intent, the honest shape is a plain `def` and a `theorem ... := rfl`, with no
class and no instance binder — a definition does not need a typeclass to be
resolved everywhere. Keeping the class *is* the claim that there was a
hypothesis to discharge.

## A correction to the note that produced this bean

That note said "13 hypothesis-uses". There are **three distinct classes named
`BorromeanQuark`** in the corpus, in three namespaces, and the count conflated
them:

| declaration | fields | consumers |
|---|---|---|
| `QOU/Archimedean/BorromeanQuark.lean:114` (**this bean**) | `topological_mass`, `volume_calibrates_mass` | `baryon_mass_from_volume`, same file only |
| `QOU/ParticleInteractions/neutron_qvalue_symbolic.lean:39` | different | 3 theorems there + 3 in `QOU/Mass/DeuteronBindingDressing.lean` |
| `QOU/Conjectures/ShellTransitionKnot.lean:70` | `crossingNumber`, `crossingNumber_eq = 3` | `ShellTransitionKnot` |

So this instance's blast radius is **one theorem in its own file**, which makes
the fix cheap whichever reading wins. The name collision is itself worth a
separate look — the third one has the same one-model shape as
`SubstrateWidthRule` (`qou-2y13`).

Related but distinct: `qou-kx92` covers `[BorromeanQuark] : True := trivial`
conditional theorems in `reidemeister-mass-invariance.lean` and
`hoefsmit-scattering-pipeline.lean`. Not this instance.

**Detector note:** `checkNoVacuousInstanceData` does not and cannot flag this —
the data value is a genuine formula. See `folio-assistant-ilbh`.

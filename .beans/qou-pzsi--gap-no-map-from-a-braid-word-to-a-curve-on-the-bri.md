---
# qou-pzsi
title: 'GAP: no map from a braid word to a curve on the Bring surface — the embedding-energy selection rule cannot be built without it'
status: todo
type: task
created_at: 2026-09-14T16:50:05Z
updated_at: 2026-09-14T16:50:05Z
---



## The gap, precisely

Opened 2026-09-14 from the owner's objection on `qou-99qc`: *"The selection rule
shouldn't be minimum crossing... It may be higher energy than a non-minimal
crossing. A sibling has worked on connecting hecke energy to O'Hara energy via
brings embedding... You're minimizing not just the hecke energy but how the knot
is embedded into brings surface."*

**Why it is needed.** The gluon-dressing selection on `qou-99qc` is blocked on
its cost function. Two proxies have been measured and both fail, for one
structural reason:

- **crossing count** — `FrobeniusSelected`'s own instantiation. Ties σ₁ with
  σ₁⁻¹.
- **crossing energy** (`def:crossing-energy`) — breaks that tie (σ₁⁻¹ = −0.90092
  beats σ₁ = +1.10998) but ties all three 2-crossing candidates at `2q`.

Both are **sums over letters**, hence constant on the permutation orbit of a
letter multiset — while the closure is not. That is now a **scope-(b) structural
exclusion of the whole letter-sum class** (probe
`qbeta_embedding_energy_can_discriminate_probe.py`, 5/5, PR #7370): σ₁σ₀ and
σ₀σ₁ have the same multiset and the same writhe `+2` and close to **different
links** (traces apart by 6.78e-2 / 1.42e-2). So no functional of the multiset
alone can select here, for any `q` and any coefficients.

**And an isotopy-class energy is NOT barred** — all four 2-crossing candidates
are distinct links, so the O'Hara/Möbius **infimum** can take different values on
them. Green light for the route on discriminability grounds.

## What exists

- [`mobius_cross_energy_hopf_calibration.py`](computations/mobius_cross_energy_hopf_calibration.py)
  — a cross-energy integrator **calibrated against the proved** `E(Hopf) = 2π²`
  (Agol–Marques–Neves, arXiv:1205.0825), mpmath end to end.
- `mobius_cross_energy_borromean.py`, `mobius_borromean_topology_guard.py`.
- `QOU.MobiusEnergy` — categorical `E_cat` from the Frobenius–Hopf
  comultiplication and the q-Hodge star, with the encoded relation
  `E_cat = ¼·E_classical + const`.
- Bring machinery: period matrix, mapping-torus residue weights, zero modes.
- Beans `qou-zfs6` (Möbius invariance / FHW bound / minimiser as Lean gates) and
  `qou-dux3` (the Möbius-invariant exponent) are `completed`; `qou-6xt9`
  (ingest the knot-energy literature) is `in-progress`.

## What is missing — the gap itself

**Any map from a braid word to a curve in or on the Bring surface.** The
integrators consume hand-parametrised *named* embeddings (Hopf, Borromean);
nothing feeds them an arbitrary 9/10/11-letter Hecke word. Searched
`computations/` and `tools/` for embedding/curve/parametrisation code near
"bring", and for every consumer of
`mobius_energy|ohara_energy|E_mobius|mutualIntegrand|cross_energy`.
`embeddable_knot_operator.py` is **not** it — it is σ/π orbital-overlap
weighting with a per-system `w_perp`. **An absence on the surfaces searched, not
a proof of absence.**

## Why it is hard, not merely unbuilt

Möbius energy is a property of an **embedding** and is **not a knot invariant** —
it varies over the isotopy class, and the invariant is the **infimum** (FHW). So
"the energy of a word" needs either

1. the **minimiser** over the isotopy class (existence is the FHW theorem's
   content, and computing it is a variational problem), or
2. a **canonical embedding** — which is exactly what the Bring surface would be
   for, and is the substantive proposal.

That is the research content. It is not a wiring job.

## Caveat that must not be skipped

`QOU/MobiusEnergy.lean` carries **2 sorries**, and its own header records a
prior vacuity incident in which `classicalLimit` made `E_cat` **blind**
(`E_cat = 1 + const` for every knot) **with no `sorry` to flag it**. The
categorical↔classical leg therefore cannot bear weight unexamined — check it
before building on it.

## Next honest step

Not "build the bridge". First establish which of (1) or (2) above the Bring
surface is supposed to supply, and whether `E_cat`'s classical limit is sound
after the recorded vacuity incident. Until then the gluon dressing stays
unselected and the `qou-99qc` dashboard rows stay un-re-scored.

## 2026-09-14 (session gifted-feynman) — the caveat checked: both its reasons are wrong, and its conclusion is right for a better one

This bean's "Next honest step" names two things to establish before building.
The second — *whether `E_cat`'s classical limit is sound after the recorded
vacuity incident* — is settled here. **Both stated grounds for doubt are wrong,
and a third, worse one is proved.**

**1. "`QOU/MobiusEnergy.lean` carries 2 sorries" — FALSE. It carries ZERO.**
Measured on the merged head: `grep -cE '(^|[[:space:]])sorry([[:space:]]|$)'`
returns **0**, and the file is `lean`-direct **exit 0**
(`-DautoImplicit=false -s 65536`), so that is an elaborated fact, not a parse
artifact. The three `sorry` strings in the file are all prose — two inside the
docstring *describing* the incident, one in a §-heading.

**2. The vacuity incident is FIXED, and has been since 2026-08-30.** The field
now reads `unknot_iff : value = 4 ↔ isUnknot`, which is the Freedman–He–Wang
statement. The broken spelling was `value = 4 ↔ True`; `P ↔ True` is `P`, so it
forced `value = 4` for *every* instance and, through `classicalLimit`, made
`E_cat = 1 + const` for every knot. The file's own docstring records the repair.
So the bean's caveat is **stale**, not merely imprecise.

**3. 🛑 But there is a SECOND defect in the very same field, it is live, and it
is worse.** `CategoricalMobiusEnergy.classicalLimit` reads

    energy = (1/4) * classicalEnergy.value + classicalLimitConst

and `classicalLimitConst` is a **free field of the same structure**, occurring
once and linearly. So the field **constrains the pair `(energy,
classicalEnergy)` not at all**: for any `e` and any `c` whatever, exactly one
constant satisfies it. Proved, sorry-free, appended to the file itself:

| declaration | statement |
|---|---|
| `QOU.classicalLimitConst_eq` | `classicalLimitConst = energy − ¼·classicalEnergy.value` — determined by the other two fields |
| `QOU.classicalLimit_unconstraining` | `∃! k, e = ¼·c.value + k` for **every** `e` and **every** `c` |

`#print axioms` on both: `[propext, Classical.choice, Quot.sound]`, no `sorryAx`.

**Why it matters, in the framework's terms.** The mathematical statement the
docstring quotes — `lim_{q→1} E_cat(γ) = ¼ E(γ) + const` — means a **universal**
constant, the same for every knot. That is what carries the content. Encoded
**per instance**, the content is gone: the categorical energy and the classical
energy are related by nothing.

**It is the same class as the incident the file already records** — *"no
`sorry`, no `axiom` and no tautological conclusion, so no vacuity detector saw
it"* — one field over, and it **survived that repair**. The 2026-08-30 fix
corrected `unknot_iff` and did not look at the field consuming it.

**Not repaired, deliberately.** Making the constant universal changes what the
structure asserts; that is an authoring decision for the owner, not an agent's
fix, and §ASK THE OWNER applies. Recorded in the file and here.

**Corpus-grep before claiming:** `classicalLimitConst` appears **nowhere else**
in the corpus — not in any bean, audit, probe or other `.lean`. Not previously
recorded.

**So this bean's conclusion stands and its reasons should be replaced.** The
categorical↔classical leg still cannot bear weight — not because of sorries
(there are none) or the old blindness (fixed), but because the bridge field is
unconstraining as encoded. Open item (1) — *which of minimiser-or-canonical-
embedding the Bring surface is meant to supply* — is untouched and remains the
live research question.

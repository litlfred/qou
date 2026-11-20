---
# qou-3ffh
title: 'FEATURE: partition-function unification — Z_statmech = Σ_λ Frobenius = J_K state-sum are one tr_M (β=ln q)'
status: todo
type: feature
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-qcd
created_at: 2026-08-02T18:33:15Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

## Question (owner, 2026-08-02)

How does the Euclidean↔Lorentzian bridge $Z=\mathrm{tr}\,e^{-\beta H}$ ↔
path integral correspond to the QOU sum-over-partitions (Young diagrams)?
Is there an implicit relation between these "partition functions"?

## Answer: THREE partition functions, ONE trace $\mathrm{tr}_M$

| # | Name | Expression | Basis / presentation |
|---|------|-----------|----------------------|
| 1 | Stat-mech | $Z=\mathrm{tr}\,e^{-\beta H}=\sum_{\text{states}}e^{-\beta E}$ | configuration / path-integral |
| 2 | Frobenius/Markov | $\mathrm{tr}_M=\sum_{\lambda\vdash n} y_\lambda(q)\,\chi_\lambda$ | irrep / Young-diagram (Wedderburn) |
| 3 | Knot state-sum | $J_K(q)=\mathrm{tr}_M(\rho(\beta_K))$ | crossing / Kauffman–Temperley–Lieb |

**The pun is not a coincidence.** Integer "partition" $\lambda$ (Young
diagram) and physics "partition function" $Z$ coincide because the
Wedderburn blocks — indexed by partitions $\lambda\vdash n$ — ARE the
thermal microstates. $Z$ counts states; $\mathrm{tr}_M$ counts the same
states organised by irrep. Same trace, two bases.

## The implicit relations (each a bean below)

- **(1)↔(2) — Schur–Weyl / Wedderburn change of basis.** Trace over the
  tensor state space $=\sum_\lambda$ character sum. The dictionary is
  **$\beta \leftrightarrow \ln q$** (inverse temperature = log substrate
  modulus). Corpus already has ln-q-as-temperature:
  `braids-and-knots/meridian-holonomy-boost`,
  `observations/q-deformed-nuclear-models-comparison`.
- **(2)↔(3) — Frobenius formula for the Jones polynomial.** The Markov
  trace of a braid word is exactly the weighted character sum
  $\sum_\lambda w_\lambda\chi_\lambda(\beta_K)$. Corpus:
  `braids-and-knots/frobenius-lepton-meson-bridge-proof`,
  `knot-eigenbasis-complete`.
- **(1)↔(3) — Jones = Potts / Temperley–Lieb partition function.** The
  DEEPEST and most historically grounded: Jones' 1985 derivation of the
  polynomial came FROM the Temperley–Lieb algebra of the Potts-model
  transfer matrix (Baxter). The Kauffman bracket literally IS a lattice
  state-sum = a vertex-model partition function. Corpus:
  `observations/skein-mass-relation-proof`,
  `quantum-observable-universes/braiding-unit-circle-convention`.

## Wick rotation ties the triangle to temperature (cross-ref qou-ud3o)

- **Real $q>1$** ⟺ $\beta=\ln q$ real ⟺ **Euclidean / thermal** (heat
  semigroup $e^{-\beta H}$, decaying).
- **$q$ on the unit circle** ($|q|=1$, $q=e^{i\theta}$) ⟺ $\beta$
  imaginary ⟺ **Lorentzian / unitary** (Schrödinger $e^{-i\theta H}$,
  oscillatory).
- The Wick bean's $i\mapsto -i$ = the $q$ real-axis ↔ unit-circle rotation
  = the $\beta\leftrightarrow i\beta$ thermal↔real-time rotation. So the
  three partition functions + Wick + `braiding-unit-circle-convention` are
  one story: **temperature = $\ln q$, and Wick rotation = moving $q$ off
  the real axis onto the unit circle.**

## Useful relations to PROVE (the point of these beans)

R1. $\beta=\ln q$ dictionary: identify the stat-mech Boltzmann weight
    $e^{-\beta E_\lambda}$ with the Frobenius weight $y_\lambda(q)$ ⇒
    read off the "energy" $E_\lambda=-\ln y_\lambda/\ln q$ of block
    $\lambda$. [near-term; mostly definitional + a Lean identity]
R2. (1)↔(2) Schur–Weyl: $\mathrm{tr}$ over $(\mathbb C^N)^{\otimes n}$
    $=\sum_{\lambda\vdash n}(\dim V_\lambda)\,\chi_\lambda$ — the
    partition-function-as-character-sum. [medium; Schur–Weyl is in the
    corpus at q=1, bean `1ict`]
R3. (1)↔(3) Jones = Potts/TL partition function: the Markov trace state-sum
    equals a vertex-model $Z$. [research; cite Jones 1985, Baxter;
    the historically-correct direction]

## Anti-guessing note
Do NOT declare "partition-function correspondence is open" — all three
objects and the ln-q-temperature link EXIST in the corpus. Open item is
the *proved equivalence/dictionary* (R1–R3), not the concepts.

## Progress Note (2026-11-16)
- Formalized partition-function Schur-Weyl cube unification (`sym3Dim N + 2 * mixed3Dim N + alt3Dim N = N^3` for `N = 2, 3, 4`: `8 = 4 + 4 + 0`, `27 = 10 + 16 + 1`, `64 = 20 + 40 + 4`) in `QOU/Eightfold/AtomicitySp2ElectroweakAndPartitionUnification.lean` (`partition_function_schur_weyl_cube_unification_certificate`) + 50-dps probe `atomicity_sp2_electroweak_and_partition_unification_probe.py` (PR `litlfred/qou#8172`, head `89a2a31a65a0d7dbf47567c813f9c48b755fae24`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8172, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

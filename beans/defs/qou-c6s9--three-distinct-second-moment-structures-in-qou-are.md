---
# qou-c6s9
title: Three distinct second-moment structures in QOU are NOT one object (Plancherel/Kerov, multiplet mixing, q-CLT)
status: in-progress
type: task
priority: normal
created_at: 2026-09-13T05:11:10Z
updated_at: 2026-09-13T05:12:50Z
---

## The finding (measured 2026-09-13)

Three DIFFERENT second-moment structures live in this corpus. They are routinely
referred to as "the variance" and they are not the same object. Conflating them
would be selection-against-the-target in the sense of the NO-FITTING directive.

| | index set | independence | status |
|---|---|---|---|
| **1. Plancherel / Kerov** `Cov_Planch` | partitions `lambda |- n` | **FREE** | exact; 26 covariance-epic witnesses under `computations/deltalambda/` (11 in the A2 moment sub-arc); sign of `M_1` **OPEN** (`qou-k5r5`) |
| **2. Multiplet mixing** (2x2 symmetric, off-diagonal `e`) | finite flavour space | **CLASSICAL** | `QOU.Eightfold.NonetMixingUnconstrained.mixing_unconstrained`, sorry-free |
| **3. q-CLT washout** `kappa_2^(q) = Var(sigma_i)` | strand position along a word | free | non-degenerate; wired to the macroscopic q-Gaussian of width `sqrt(kappa_2/n)` |

Exact results already in (1), from `wlambda-covariance-epic-M1-free-cumulant-reframing.witness.json`:
`Var(R_4) = 3n(n-1)(n-2) = 9|C_3|`; `Var(R_3) = 2n(n-1) = 4 C(n,2)`;
`Cov(R_3,R_4) = 0`; `Cov(Sum h, R_3) = 0`; `M_1 = (1/3) Cov(Sum h, R_4)`, exact to n<=15.
The witness calls itself "structural reframing, not a proof" - keep that scope.

## What prompted it
A user question about whether QOU could speak to the ALICE incoherent-J/psi result,
where the measured observable is literally a variance: in the Good-Walker formalism
`dsigma_incoh/d|t| ~ Var_Omega(A)`, the variance of the scattering amplitude over
TRANSVERSE SPATIAL configurations. That is a FOURTH ensemble and QOU has none of it
(`impact parameter` 0, `transverse plane` 0, `momentum space` 0).

**Structure (2) has the right algebraic SHAPE** - diagonal = coherent,
off-diagonal = the dissociation channel, and
`no_mixing_iff_eigenvalues_are_diagonal` is Good-Walker's statement one arena down.
The mismatch there is the index set (2-dim flavour vs a continuum in the plane),
not the structure.

## The trap this bean exists to prevent
An agent asked to connect QOU to any fluctuation observable will find "a variance"
in 600+ `computations/` files and 374 `.lean` files and map it across. Free
independence is not classical independence; free convolution is not classical
convolution; the free CLT gives a semicircle and the classical one a Gaussian.
A correspondence between (1) and a spatial ensemble is a THEOREM TO PROVE, never a
substitution to make.

## Default if nothing is done
Nothing changes; the three stay undistinguished in prose and the conflation stays
available.

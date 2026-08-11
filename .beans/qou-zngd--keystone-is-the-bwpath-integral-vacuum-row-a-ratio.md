---
# qou-zngd
title: 'Keystone: is the BW/path-integral vacuum row a RATIONAL function of q? (the load-bearing hypothesis of the roots-of-unity reduction)'
status: todo
type: task
created_at: 2026-08-11T01:04:19Z
updated_at: 2026-08-11T01:04:19Z
---


## Why this is the load-bearing item

`QOU/BraidKnot/KeystoneRootsOfUnityReduction.lean` (sorry-free) proves:

> If both sides of `bwS0_eq_hecke` are **rational functions of q**, then agreement
> at **all roots of unity** already forces agreement at `q₀`.

So the archimedean-continuation step — the thing `HabiroDomainVanishing.lean`
(#4957/#4962) showed a Habiro element structurally cannot do at real `q > 1` — is
**not a separate obligation**. It is free, *given rationality*.

The Hecke side is manifestly rational: `d_q(λ)` is a Laurent polynomial (bean
`qou-2v7k` item (i)), so `d_λ²/Σ_μ d_μ²` is a polynomial ratio after clearing the
pole at `q = 0`.

**Open: is the BW / path-integral side rational in q?** That is the single
hypothesis the reduction rests on, and it is NOT proved. It is carried as an
explicit hypothesis (`RationalPresentation`), never assumed true — per
AGENTS.md §"Axiomatization is NOT a Proof", stating it buys nothing toward
proving it.

## What would close this

Either (a) exhibit the BW vacuum row as an explicit ratio of polynomials in `q`,
or (b) show it is NOT rational — which would be a genuine scope-(b) obstruction
to the reduction (not to `bwse` itself) and would send the route back to needing
a real analytic continuation.

## What does NOT close it

Interpolation from the fibre data. `computations/probes/wlambda_rational_shadow_degree_probe.py`
measures the shortfall: the n=5 vacuum row needs **25..33** values, the 9-node
McKay `F_λ` needs **31..41**, and Σ(2,3,5) supplies **5** (three exceptional
fibres, two flat connections with `ℓ₂ = ℓ₃ = 1`, plus `q = 1`). Shortfall
20..36. The reduction needs agreement at *every* root of unity — a structural
statement, not a finite table to extend.

Related: `qou-2v7k` (FRONTIER B), PR #4969 (`bwse` MTC construction), PR #4973.

---
# qou-zngd
title: 'Keystone: is the BW/path-integral vacuum row a RATIONAL function of q? (the load-bearing hypothesis of the roots-of-unity reduction)'
status: completed
type: task
priority: normal
created_at: 2026-08-11T01:04:19Z
updated_at: 2026-08-11T01:12:58Z
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

## ANSWERED (2026-08-11) — yes, for the concrete RT/Seifert row; and it closes that route

The corpus already carried the concrete row (`BWVacuumRowConcrete.lean`):

    bwS0Concrete(λ) = S_{0λ} · θ_λ^f ,   S_{0λ} = d_q(λ)/D ,   θ_λ = q^{c(λ)}

`θ_λ` is a **zpow with INTEGER exponent** `c(λ) = contentSum λ`, so `θ_λ^f =
q^{f·c(λ)}` is a **Laurent monomial** — rational. It multiplies the same
`S_{0λ} = d_q/D` the Hecke side carries, so the irrational `D` cancels from the
comparison. **The BW side is rational for this construction**, and
`KeystoneRootsOfUnityReduction.lean` applies.

Applying it (`KeystoneFramingTrivialAtRootsOfUnity.lean`, sorry-free) gives more
than expected — it closes the route rather than advancing it:

> gate at EVERY root of unity ⟹ `f·c(λ) = 0` ⟹ (since 6 of 7 blocks λ⊢5 have
> `c(λ) ≠ 0`) **`f = 0`** — the framing `BWVacuumRowConcrete` itself calls
> "zero Σ(2,3,5) data … a tautology".

Both horns pinned:

| demand | consequence |
|---|---|
| match at ALL roots of unity | `f = 0`, tautological framing |
| match at finitely many | doesn't pin — n=5 row needs 25..33 values, Σ(2,3,5) supplies 5 |

This CLOSES the object `BWVacuumRowConcrete.lean` named as *surviving* (the fibre
root-of-unity form archimedean-continued to q₀): that continuation is now free
(the reduction), and the root-of-unity match is now impossible for `f ≠ 0`.

**Scope-(b), narrow.** Invariant cited: `f·c(λ) ∈ ℤ`, and a nonzero integer power
of the indeterminate is not `1` in `ℂ[X]` (degree). Excludes only the concrete
RT/Seifert row with an integer-power twist. Does NOT exclude: other constructions
of the BW vacuum row (non-monomial twist, λ-dependent or root-dependent framing,
correction terms), `bwS0_eq_hecke` under such a construction, or the
Beasley–Witten localization program (`bwse`, PR #4969) — untouched.

Probes: `keystone_framing_content_sum_probe.py` (premise bites, 6/7),
`wlambda_rational_shadow_degree_probe.py` (the finite-data horn).

---
# qou-ynff
title: 'GAP: 5_2 trace field is the cubic disc -23, NOT Q(sqrt-7) — retract the 2026-07-18 audit premise'
status: todo
type: task
created_at: 2026-08-11T11:23:32Z
updated_at: 2026-08-11T11:23:32Z
---

## The finding

`docs/audits/2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md` opens with

> The 5₂ invariant trace field is **ℚ(√−7)** (`det(5₂)=7`)

Both halves are wrong, and the parenthetical is the error in miniature: it reads
the **geometric** trace field off the **determinant**, an Alexander-polynomial
datum.

5₂'s invariant trace field is the **cubic of discriminant −23**. ℚ(√−7) cannot
embed in it — `[ℚ(√−7):ℚ] = 2` does not divide `[K:ℚ] = 3`. That is a
**scope-(b)** exclusion on a proved invariant (the tower law), not a numerical
near-miss: no precision can rescue it.

ℚ(√−7) *is* attached to 5₂, as the **Alexander** layer (`Δ = 2t²−3t+2`,
`disc = −7`, `det = |Δ(−1)| = 7`) — the quadratic subfield of `ℚ(ζ₇)` where the
ℤ/7 branched cover's metabelian data lives. Different layer.

## Certified

`computations/probes/qbeta_5two_trace_field_disc23_not_qsqrt7.py`, 5/5 passing,
driven from the corpus's own saddle solver rather than re-derived. The strongest
assertion is the **paired control**: at `tol = 1e-40`, degree ≤ 3, `Im(z₁)` and
`Im(z₁)/√7` satisfy no integer cubic, while `Im(z₁)/√23` satisfies
`−184x³ + 10x − 1` with `disc = −178112 = −23·88²` — squarefree part 23, back in
`K`. The numerics do not merely fail to support √−7; they select √−23.

## Blast radius — narrower than it first looked

- **The paper is clean.** No content block asserts it. `references.ts` describes
  the Hakimoglu-Brown paper correctly and ties its use to 4₁ / ℚ(√5).
- **Lean already proves the right answer**: `disc_eq_neg_23`
  (`FiveTwoSumRuleIntegrand.lean:249`, generic `[CommRing R]`).
- **The live probe lane had it right all along** and contradicts the audit —
  `qbeta_5two_gswz_saddle_arithmeticity_probe.py` §1 states the trace field as
  `ℚ[ξ]`, `x³−2x²+3x−1`, disc −23, and its §4 records the bar-odd σ-pair tower
  on the **√−23** line. Nothing wired to production depends on the field claim.

## Corrected in this bean

audit premise (banner) · inheriting audit (banner; its negative stands) · probe
docstring (retraction header) · `keystone-multivector-attack.md` §V2 · titles of
`qou-7lim`, `qou-dq2q`, `qou-ized` · new audit
`docs/audits/2026-08-11-5two-trace-field-is-disc-minus-23.md`.

## What is NOT retracted

No bar-odd action **value**. The 2026-07-18 audit's own anti-laundering note was
correct in claiming none, and none is claimed here. The `q₀`-derivation gate
(`qou-eic1`, forever) is untouched. The correction is to the **field a search
runs in**.

## Two side-findings, recorded so they are not re-discovered as results

1. `Vol(5₂) = 3·|D(z₁)|` is **forced**, not a discovery: at `m=1` the gluing
   equation gives `z₂ = 1/(1−z₁)`, a six-fold Bloch–Wigner partner for which
   `D(z₂) = D(z₁)` is textbook. Carries no field information.
2. "Theorem 3 IS the 5₂ dilog closed form" was argued by solving one equation in
   one unknown in an analytic function. Matching a sum's *value* is not matching
   the *triple*. Treat as unestablished.

## General guard worth keeping

A field claim about a hyperbolic knot needs a **degree check**. The trace field
of an `n`-tetrahedron hyperbolic knot is generically degree `n`, and a quadratic
cannot sit inside an odd degree.

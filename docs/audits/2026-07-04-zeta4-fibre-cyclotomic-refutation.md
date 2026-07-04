# ζ₄-residue route — refuted at the fibre-Laurent level (Φ₄ ∤ Q_β carrier)

**Date:** 2026-07-04
**Bean:** 0zr0 (ζ₄-residue odd-sector route)
**Probe:** [`computations/qbeta/qbeta_zeta4_fibre_cyclotomic_probe.py`](../../computations/qbeta/qbeta_zeta4_fibre_cyclotomic_probe.py)
**Witness:** `computations/qbeta/qbeta-zeta4-fibre-cyclotomic.witness.json`
**Companion (s-adic leg):** [`2026-07-04-fixed-ring-vacuity-ladder-membership.md`](2026-07-04-fixed-ring-vacuity-ladder-membership.md)

## Context

The fixed-ring vacuity theorem (companion audit) showed the ζ₄ / odd-degree
grading is **vacuous at the s-adic / formal-disk level** (Fix(σ) =
ℚ(√3)[[ũ]] = ℚ(√3)[[h²]]; ĥ = q+q⁻¹ ∈ ℚ[[h²]]). Its verdict pointed the
route to the only level where the grading is a real constraint: the **fibre
Laurent level**, where odd-degree support in q is genuine. This audit tests
the ζ₄-residue route there, on the actual Q_β carrier.

## Object

The bar-odd part (under the bar involution q ↦ q⁻¹) of the net decay-width
Laurent polynomial Δ_net(q) = Δ(neutron) − Δ(proton):

$$
  \Delta_{\mathrm{odd}}(q) \;=\; \tfrac12\bigl(\Delta_{\mathrm{net}}(q) - \Delta_{\mathrm{net}}(q^{-1})\bigr)
  \;=\; \frac{\mathrm{num}(q)}{4\,q^{7}},
$$
$$
  \mathrm{num}(q) = q^{14} - 5q^{12} + 10q^{10} - 16q^{8} + 16q^{6} - 10q^{4} + 5q^{2} - 1.
$$

## Two exact, falsifiable questions (pure ℤ[q] algebra, no fit, no s-expansion)

**(Q1) ζ₄-faithful grading — is Δ_odd supported on odd powers of q (the ±i
isotypes of q ↦ ζ₄q)?  → TRUE.**
num(q) is even in q (num(−q) = num(q), a polynomial in q²); with the odd
q-exponent of the denominator 4q⁷, the carrier Δ_odd is supported entirely
on odd powers of q. The ζ₄ *grading* the descent audit requires **holds**.

**(Q2) ζ₄-residue sharpening — does Φ₄ = q²+1 divide num(q)?  → FALSE.**
Exact factorisation over ℚ:
$$
  \mathrm{num}(q) = (q-1)(q+1)\,\bigl(q^{12} - 4q^{10} + 6q^{8} - 10q^{6} + 6q^{4} - 4q^{2} + 1\bigr).
$$
The only cyclotomic divisors are Φ₁, Φ₂ (⇒ the trivial q²−1). **Φ₄ does not
divide.** The descent audit's specific claim — that the shared ζ₄=i residue
is Φ₄ = q²+1 — is refuted for the actual Q_β carrier.

## Verdict — scope (b), structural exclusion (cited invariant: the factorisation)

Unlike a numerical near-miss, this is a **proved exact-arithmetic
impossibility**: (q²+1) ∤ num(q) in ℤ[q]. Per the (a)/(b) refutation
discipline this is a legitimate scope-(b) exclusion, the cited invariant
being the exact ℚ[q] factorisation. The ζ₄-**residue** route (Φ₄
divisibility) is therefore closed from **both** ends:

- **s-adic level:** vacuous (companion audit — the grading itself collapses).
- **fibre-Laurent level:** the grading survives, but the Φ₄ residue is
  absent; the cyclotomic content is only the trivial (q²−1).

## Open residue (not pursued here)

The substance of the odd carrier is the non-cyclotomic **palindromic
degree-12** factor
$$
  R_{12}(q) = q^{12} - 4q^{10} + 6q^{8} - 10q^{6} + 6q^{4} - 4q^{2} + 1
  \;=\; x^{6} - 4x^{5} + 6x^{4} - 10x^{3} + 6x^{2} - 4x + 1,\quad x = q^{2}.
$$
Any residual fibre-level ζ₄ / Habiro structure of the Q_β sector lives in
R₁₂, not in a cyclotomic factor. Its relation to the underlying 14-strand
net braid (Δ_net has denominator 4q⁷ ⇒ a 14-crossing / spanning object) —
e.g. whether R₁₂ is a knot-invariant specialization — is left open. This is
a *rung-structure* question at the Laurent/Habiro level, the one place the
companion audit flagged as non-vacuous.

## Cross-references

- Fixed-ring vacuity (s-adic leg): [`2026-07-04-fixed-ring-vacuity-ladder-membership.md`](2026-07-04-fixed-ring-vacuity-ladder-membership.md).
- ζ₄ descent audits: [`2026-06-28-frakV-descent-zeta4-partner.md`](2026-06-28-frakV-descent-zeta4-partner.md), [`2026-06-28-frakV-zeta4-fibre-vs-observable.md`](2026-06-28-frakV-zeta4-fibre-vs-observable.md).
- Q_β / complex-volume conjecture: [`conj:binding-qbeta-complex-volume`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.md).

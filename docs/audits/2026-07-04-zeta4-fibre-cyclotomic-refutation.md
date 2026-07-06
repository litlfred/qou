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

## The residue R₁₂ — identified as a cubic in the bar-even trace variable

The substance of the odd carrier is the non-cyclotomic **palindromic
degree-12** factor
$$
  R_{12}(q) = q^{12} - 4q^{10} + 6q^{8} - 10q^{6} + 6q^{4} - 4q^{2} + 1
  \;=\; x^{6} - 4x^{5} + 6x^{4} - 10x^{3} + 6x^{2} - 4x + 1,\quad x = q^{2}.
$$
Any residual fibre-level ζ₄ / Habiro structure of the Q_β sector lives in
R₁₂, not in a cyclotomic factor.

**Identification (Task 1, [`qbeta_r12_trace_variable_probe.py`](../../computations/qbeta/qbeta_r12_trace_variable_probe.py),
witness `qbeta-r12-trace-variable.witness.json`).** R₁₂ is even and
palindromic, so it collapses under the **bar-even loop-trace variable**
$y := q^2 + q^{-2} = 2\cosh 2\lambda$ to a cubic:
$$
  R_{12}(q)/q^{6} \;=\; C(y),\qquad C(y) = y^{3} - 4y^{2} + 3y - 2
$$
(verified exactly: $C(q^2+q^{-2})\,q^6 = R_{12}$). $C$ is **irreducible over
ℚ** (no rational root; discriminant $-152 < 0$), with one real root
$y_0 \approx 3.270$ (⇒ a real $q>1$ branch, $q \approx 1.71$) and a
complex-conjugate pair.

So the odd carrier's non-cyclotomic content is **not** a root-of-unity
object (consistent with the Φ₄ refutation above) — it is a degree-3
polynomial in the *same* $\cosh$-trace variable $y=q^2+q^{-2}$ that the
bar-even (binding) channel is built from. This is the honest structural
place of R₁₂: $\mathbb{Q}[y]$, degree 3. Whether the cubic $C$ (a genuine
$S_3$/non-abelian-cubic-field object, disc $-152 = -2^3\cdot 19$) is a
knot-invariant specialization of the 14-strand net braid ($\Delta_{\text{net}}$
has denominator $4q^7$) remains the open Laurent/Habiro-level question; but
the object to identify is now the concrete cubic $C(y)$, not a degree-12
polynomial.

## Is C(y) / R₁₂ a knot invariant of the net braid? — No (T1)

Probe: [`qbeta_r12_knot_invariant_probe.py`](../../computations/qbeta/qbeta_r12_knot_invariant_probe.py),
witness `qbeta-r12-knot-invariant.witness.json`.

The "net braid" is not a knot closure: `free-neutron-decay.witness.json`
gives the net decay carrier as the signed **isospin difference**
Δ(neutron[u,d,d]) − Δ(proton[u,u,d]) of Hecke-trace amplitudes over the
shared H₃ normal-form basis {𝟏, σ₀, σ₁, L₊, L₋, e⁻} (knots
unknot / virtual / Hopf / trefoil), the only n-vs-p difference being the
u/d crossing-weight assignment (u-u = σ, d-d = q²σ−qs·𝟏,
u-d = ½(1+q²)σ − ½qs·𝟏, all ∈ ℚ[q²]).

- **(A)** R₁₂ has q-span 12; every constituent-knot Jones has span ≤ 4
  (unknot 0, trefoil 3, Hopf 4), and R₁₂ neither equals nor divides any.
  R₁₂ is not the Jones (nor a factor) of any constituent knot.
- **(B)** R₁₂ is even in q ⇒ lives in ℚ[y], y = q²+q⁻² — the same even
  sector the crossing weights inhabit. It is a Hecke **crossing-weight
  (representation-theoretic)** object, not a topological invariant of a
  braid closure.
- **Galois note (does NOT separate).** C(y) = y³−4y²+3y−2 has disc
  −152 = −2³·19 (not a square) ⇒ **S₃** Galois. Tempting to argue "knot
  invariants are cyclotomic, C is not" — but this is **false**: the
  trefoil's own reduced Jones cubic (q³−q²−1) is also non-cyclotomic. The
  S₃ property is recorded as an arithmetic fingerprint of C, not as the
  separating invariant; (A)+(B) do the separating.

**Verdict (scope (a)):** R₁₂ is not a constituent-knot invariant and the
net is not a braid closure — R₁₂ is the isospin crossing-weight difference,
a cubic in the bar-even trace variable y = q²+q⁻². (Not claimed: that no
braid anywhere realises R₁₂ as an invariant.)

## Cross-references

- Fixed-ring vacuity (s-adic leg): [`2026-07-04-fixed-ring-vacuity-ladder-membership.md`](2026-07-04-fixed-ring-vacuity-ladder-membership.md).
- ζ₄ descent audits: [`2026-06-28-frakV-descent-zeta4-partner.md`](2026-06-28-frakV-descent-zeta4-partner.md), [`2026-06-28-frakV-zeta4-fibre-vs-observable.md`](2026-06-28-frakV-zeta4-fibre-vs-observable.md).
- Q_β / complex-volume conjecture: [`conj:binding-qbeta-complex-volume`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.md).

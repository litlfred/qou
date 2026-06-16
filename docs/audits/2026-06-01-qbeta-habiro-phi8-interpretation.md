# Φ_8² in the Hecke/braid structure of the deuteron (2026-06-01)

> **⚠ STRAND-DOUBLING INTERPRETATION FALSIFIED (2026-06-01, PR #1618).**
> The categorical interpretation below (Φ_8 = 4-strand B_4 strand-
> doubling map; predictions Φ_{2^{k+1}} for atomic step A=k → A=k+1)
> is **WRONG**. The Φ_16 / Φ_32 predictions did not hold: both
> (³He − D) and (⁴He − ³He) carry Φ_8², the SAME factor as (D − n).
> See:
>
> - [Falsification audit (2026-06-01)](2026-06-01-qbeta-habiro-strand-doubling-FALSIFIED.md)
> - [Phase 5q convention test (Φ_8² IS structural)](2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md)
>
> The **algebraic identity `Φ_8(X) = Φ_4(X²)` remains TRUE** (Lean-
> proved, [`cyclotomic-strand-doubling.lean`](../../content/quantum-observable-universe/braids-and-knots/cyclotomic-strand-doubling.lean)),
> and Φ_8² IS a real structural feature (convention-invariant). What's
> wrong is the *strand-doubling categorical content* of this audit —
> Φ_8² is universal across atomic-step pairs, not a per-atomic-number
> strand-count signature.
>
> Best current re-interpretation: Φ_8² is a universal atomic-step
> cyclotomic, most likely induced by the `z(q)²` interface factor or
> the m=8 Pochhammer boundary — see the mechanism audit (in progress)
> for the algebraic verification.

> Categorical interpretation of `Φ_8(u) = u^4 + 1` (squared) in the
> (D − n) Habiro element factorization, surfaced by the cross-pair
> probe [`2026-05-31-qbeta-habiro-cross-pair-quick-dp.md`](2026-05-31-qbeta-habiro-cross-pair-quick-dp.md).
>
> Branch: `claude/brave-mendel-FPxFl` (PR #1579).
> Probe script: [`computations/probes/qbeta_habiro_phi8_interpretation_probe.py`](../../computations/probes/qbeta_habiro_phi8_interpretation_probe.py).
> Witness: `qbeta-habiro-phi8-interpretation.witness.json`.

## TL;DR

**Φ_8(u) = u^4 + 1 = Φ_4(u²) — the deuteron's 4-strand B_4 braid signature, with the squared multiplicity arising from the Markov-trace strand-doubling map. Predicted pattern: A=k → A=k+1 atomic-step pair carries `Φ_{2^{k+1}}(u) = u^{2^k} + 1`.**

## What we found

The Σ_m Δa_m(D−n) · (u; u)_m factorization (from the cross-pair audit) contains the explicit factor

  `(u^4 + 1)² = Φ_8(u)²`

while the corresponding (n − p) factorization contained `(u² − 1) = Φ_1·Φ_2` (no Φ_8), and (D − p) had no clean cyclotomic factor. Φ_8 is the 8th cyclotomic polynomial; its roots are the primitive 8th roots of unity {ζ_8, ζ_8⁻¹, ζ_8³, ζ_8⁻³}.

## Categorical interpretation (best match: hypotheses (b) + (h))

Two hypotheses passed structural consistency checks:

**(b) 4-strand deuteron braid.** `deg Φ_8 = 4` matches the dimension of the 4-strand braid group B_4 representation that the deuteron carries: 2 nucleons × 2 isospin (or color) channels = 4 strands. The proton/neutron single-nucleon denominators carry `Φ_4(u) = u² + 1` (degree 2 = B_2), and the deuteron denominator is `32·u^40·(u²+1)³` — already a Φ_4³ multiplicity. The substitution `u → u²` lifts Φ_4 to Φ_8 (since `Φ_8(u) = Φ_4(u²)` identically).

**(h) Bar-symmetric quartet.** Φ_8 has exactly 2 bar-conjugate pairs of roots: `{ζ_8, ζ_8⁻¹}` and `{ζ_8³, ζ_8⁻³}`. For an isoscalar (I=0) bound state like the deuteron, the bar involution `q ↔ q⁻¹` is a symmetry of the state itself (not just of the formalism), so the appearance of an explicit bar-symmetric quartet polynomial as a structural factor is natural.

**Combined.** Φ_8 encodes the deuteron's 4-strand braid representation AS a bar-symmetric quartet of crossings — the structure of 2 nucleons bound by a bar-paired isospin-singlet interaction.

## The strand-doubling identity Φ_8(u) = Φ_4(u²)

This algebraic identity is the categorical bridge between the single-nucleon and 2-nucleon Habiro structures. In Markov-trace language, the substitution `u → u²` is the strand-doubling map: it lifts a B_2 representation to a B_4 representation by sending each generator σ_i ↦ σ_i^2 (or equivalently, doubling the number of strands and letting each crossing carry a doubled-q weight).

So the chain is:
- Single nucleon → Φ_4(u) = u² + 1 in the denominator (2-strand B_2)
- Deuteron (strand doubling) → Φ_8(u) = u⁴ + 1 = Φ_4(u²) in the (D−n) Habiro element (4-strand B_4)

## Why squared?

Φ_8 appears with multiplicity 2 in the (D − n) factorization. This is NOT "2 nucleons" naively — that would give Φ_8 with multiplicity 2 from a single Wedderburn-block decomposition, which the integer Habiro witness rules out (the per-m factorization is genuinely irreducible per block, only the SUM Σ_m Δa_m(u;u)_m carries the Φ_8² factor).

The squared multiplicity instead comes from the q-Pochhammer weighting: `(u; u)_m` contains successive `(1 − u^k)` factors, and at the m=4 boundary (where the deuteron's atomic-mass-4-doubled structure exhausts the strand count), Φ_8 appears with multiplicity equal to the next-shell multiplicity (2 in this case).

## Falsifiable structural predictions

The hypothesized pattern `A=k → A=k+1 atomic-step pair carries Φ_{2^{k+1}}` makes 4 concrete predictions:

| Pair | Predicted cyclotomic factor | Strand interpretation |
|---|---|---|
| **(³He − D)** (A=3 vs A=2) | `Φ_16(u) = u^8 + 1` | 8-strand B_8 |
| **(⁴He − ³He)** (A=4 vs A=3) | `Φ_32(u) = u^16 + 1` | 16-strand B_16 |
| **(any A=k+1 − A=k)** | `Φ_{2^{k+1}}(u) = u^{2^k} + 1` | 2^k-strand B_{2^k} |
| **Isospin mirror pairs** (³H/³He, ⁷Li/⁷Be, …) | `Φ_1·Φ_2 = u² − 1` (the n−p signature) | NOT Φ_8 — distinguishes isospin from atomic step |

These are testable as soon as the per-isotope Habiro coefficients land (currently only p, n, D are in [`habiro-coefficients-atomic.witness.json`](../../computations/habiro/habiro-coefficients-atomic.witness.json)).

## Hypotheses ruled out

- **(a) Hecke at level-2 SU(2) (q² = −1).** Φ_8(u) = 0 ⟺ u^4 = −1, i.e. q = u² has q² = −1, i.e. q = ±i. WZW SU(2) at level k has q = e^(iπ/(k+2)). For q = i: k+2 = 4, k = 2. The level matches, but the appearance is a coincidence of arithmetic — there is no quantum-group level-2 truncation acting on D−n. NEGATIVE in naive form.
- **(f) 8-fold rotational symmetry of the closure.** Under u → ζ_8·u, Φ_8(u) does not equal Φ_8(ζ_8 u). The actual symmetry of the factorization is bar-equivariance, not 8-fold rotation. NEGATIVE.
- **(g) Magic-A direct Φ_A pattern.** Naive Φ_A doesn't appear; instead Φ_{2A^2} or Φ_{2^{A+1}} per the strand-doubling map.

## What this advances on the keystone Q_β Habiro element search

The cyclotomic prefactor structure across pair classes is now categorically anchored:

| Pair class | Cyclotomic prefactor | Categorical content |
|---|---|---|
| Isospin doublet (n−p, ³H−³He, …) | Φ_1·Φ_2 = u² − 1 | Bar-involution classical-limit kill |
| A=1 → A=2 atomic step (D−n) | Φ_8² | 4-strand B_4 + bar-symmetric quartet |
| A=2 → A=3 atomic step (³He−D) | Φ_16 (predicted) | 8-strand B_8 |
| A=k → A=k+1 step (general) | Φ_{2^{k+1}} (predicted) | 2^k-strand B_{2^k} |

This is significant structural narrowing of the Q_β Habiro element search space:
- The single-nucleon factor `Φ_4(u) = u² + 1` already lives in the proton/neutron denominators.
- The atomic-step factors `Φ_{2^{k+1}}` arise from the strand-doubling map applied to Φ_4.
- The isospin factor `Φ_1·Φ_2` arises from the bar-involution closing the doublet.

The Q_β Habiro element's overall form should be **a product of cyclotomic factors indexed by the (A, I) quantum numbers**, with the residual irreducible polynomial encoding the genuine "non-cyclotomic" categorical content of the nucleon. This is consistent with the bar-twisted-palindromic property of P_8(u) found in [`2026-05-31-qbeta-habiro-p8-identification.md`](2026-05-31-qbeta-habiro-p8-identification.md).

## Cross-references

- Parent factorization: [`2026-05-31-qbeta-habiro-delta-am-factorization.md`](2026-05-31-qbeta-habiro-delta-am-factorization.md)
- Cross-pair audit: [`2026-05-31-qbeta-habiro-cross-pair-quick-dp.md`](2026-05-31-qbeta-habiro-cross-pair-quick-dp.md)
- P_8(u) identification: [`2026-05-31-qbeta-habiro-p8-identification.md`](2026-05-31-qbeta-habiro-p8-identification.md)
- u^15 interpretation: [`2026-05-31-qbeta-habiro-depth15-interpretation.md`](2026-05-31-qbeta-habiro-depth15-interpretation.md)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) PROBE NEW
- CLAUDE.md §7a (Hecke-Skein convention), §7b (symmetric-crystal techniques)

## Open follow-ups

1. Test predictions 1, 2, 4 above once per-isotope Habiro coefficients land (³He, ⁴He, ³H, ⁷Li, ⁷Be).
2. Confirm Markov-trace strand-doubling map `u → u²` algebraically: is this exactly the operation that lifts B_n to B_{2n} representations? Categorical reference needed.
3. Derive the multiplicity 2 of Φ_8 in (D−n) from the m=4 Pochhammer boundary instead of postulating it.
4. Cross-check against the Burau representation eigenvalues at q = ζ_8.

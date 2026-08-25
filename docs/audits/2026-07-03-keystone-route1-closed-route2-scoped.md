# Keystone W_λ carrier: route 1 (larger-D Seifert) executed on Σ(3,4,5) and closed by the constancy exclusion; route 2 (colored Ẑ/F_K blocks) scoped as the surviving class

**Date:** 2026-07-03
**Bean:** [`s013`](../../.beans/s013--keystone-value-map-colored-lawrence-rozansky-s-mat.md) (closing) → successor bean for route 2
**Follows:** [`2026-07-02-keystone-valuemap-genuine-smatrix.md`](2026-07-02-keystone-valuemap-genuine-smatrix.md) (merged #3208: Σ(2,3,5) is D=2 with golden-ratio row; owner redirected to routes 1+2)
**Script:** [`computations/probes/keystone_route1_sigma345_constancy_s013.py`](../../computations/probes/keystone_route1_sigma345_constancy_s013.py)
**Witness:** [`computations/probes/keystone-route1-sigma345-constancy-s013.witness.json`](../../computations/probes/keystone-route1-sigma345-constancy-s013.witness.json)
**Status:** route 1 closed (executed on the count-matching manifold + a class-level exclusion with the invariant cited); route 2 scoped and handed to a successor bean. No fit; nothing wired.

## Route 1 executed: Σ(3,4,5), the count-matching candidate

Σ(3,4,5) is the minimal Brieskorn sphere whose flat-connection count matches the target:
D(3,4,5) = 6 vector-valued components, γ(3,4,5) = 4 flat contributions — exactly the 4
bwS0 conjugation classes at n=5. Transcribed from Hikami math-ph/0405028 §5 and
machine-validated on this second manifold (same standard as #3208):

| check | result |
|---|---|
| χ^(1,1,1)₁₂₀ = paper's printed table | ✓ |
| flat selection Σnχ (0 for the 2 non-flat, 4P for the 4 flat) | ✓ |
| CS phases from (P/2)(1+Σℓⱼ/pⱼ)² mod 2 = printed (119/240, −49/240, −1/60, 11/60); same rule reproduces Σ(2,3,5)'s (−1/120, −49/120) | ✓ |
| φ(3,4,5) = 49/60 from Dedekind sums | ✓ |
| **Theorem 9 exact** at N=3,5,7 (≤1.2e−38) | ✓ |
| S (6×6) is an involution; flat vacuum-row entries = printed Cor-11 weights (1/√5)(sin π/5, sin 2π/5, √2 sin 2π/5, √2 sin π/5) | ✓ |
| Prop 8 assembled mechanically (S · Φ̃(−N) + L-tail), residuals 2.1e5 → 705 → 2.8 at N=25/51/101 | ✓ |

**Value screen:** the 4 flat vacuum-row magnitudes have ratios **(1, √2, φ, √2·φ) ≈
(1, 1.414, 1.618, 2.288)** — against bwS0 targets (1, 4.110, 5.220, 6.220) and classical
dims (1, 4, 5, 6): **refuted**. The 4 flat channel *functions* Φ̃^(ℓ)(1/q₀) (ratios
1.00–1.08) are refuted as well. The γ=4 count match does not extend to values.

## Route 1 closed as a class: the constancy exclusion (scope (b), invariant cited)

- Every entry of the false-theta S-matrix (Hikami eq. 3.8, and its plumbed
  generalizations) is a **constant algebraic number** — a product of sines at rational
  angles. There is no q anywhere in the formula.
- The keystone target `bwS0(λ; q) = d_q(λ)/D(q)` has **nonconstant-in-q ratios**:
  d_q(4,1)/d_q(5) = [4]_q = q³+q+q⁻¹+q⁻³, strictly increasing for q > 1 (witnessed
  numerically at two anchors: 4.1097 at q₀ vs 4.0238 at q=1.05; trivially provable — a
  one-line Lean lemma, queued as follow-up).
- `BWVacuumRowIsHecke` is a **fibre-level (q-family) statement**. A constant vector cannot
  equal a nonconstant q-function family on any interval; it can at most coincide at
  isolated q values — and a single-anchor numerical coincidence is precisely the
  fitted-coincidence failure mode the three-calibration discipline rejects.

**Conclusion: no fixed Seifert/plumbed manifold with any finite colouring — no matter how
large D — can carry the keystone vacuum row.** This closes route 1 generically, not
manifold-by-manifold. The (b)-classification is justified: the invariant (nonconstancy of
[4]_q vs constancy of sine products) is exact and cited, not a failed numeric probe.

## Route 2 scoped: the surviving type-correct class is q-function block families

The constancy exclusion is constructive about what survives: the carrier must be a family
of **q-functions**, not S-matrix constants. In the uploaded literature:

1. **Homological blocks Ẑ_b(q)** (GPPV; proved for negative-definite plumbed manifolds by
   Murakami, `library/arxiv-2205.01282v2/2205.01282v2.pdf` — "WRT invariants are radial limits of homological
   blocks"). For a ℤHS³ like Σ(2,3,5) there is **one** spin^c block, and its false-theta
   content is exactly the Φ̃ family already screened (rounds 2–3: channels refuted). Bare
   Ẑ does not supply a 4-dim λ-family.
2. **Colored/decorated blocks — F_K(x, q)** (Gukov–Manolescu knot-complement blocks, the
   two-variable extension GPPV/AM point to): the λ-dependence would enter through the
   colour variable x, giving a genuine q-function family with a tunable index set. This is
   the concrete surviving candidate — and it is **new corpus infrastructure** (no F_K
   object exists in-repo yet).
3. **Andersen–Mistegård resurgence** (`library/arxiv-1811.05376v4/1811.05376v4.pdf`) gives the general
   Seifert-fibered analytic machinery if more exceptional fibres are ever needed — but by
   the constancy exclusion, more fibres only enlarge a *constant* family, so this matters
   for route 2 only through its Borel-plane/Ẑ structure, not its S-data.

**Handoff:** successor bean (route-2 carrier) — owner-gated, since building F_K
infrastructure is a real tranche and the identification target must be stated before any
numerics (formalize-first: state the x-specialization hypothesis class and its invariants,
then probe narrow).

## s013 closes

The bean's task — "derive the genuine colored Lawrence–Rozansky/Hikami S-matrix amplitude
and check whether it reproduces bwS0 = d_q/D" — is complete: the amplitude was derived
(residue character: round 2; S-matrix + flat weights: round 3, #3208; second manifold:
this round), every step machine-validated against the primary sources, and the answer is
**no** — at the residue level (pure signs), the channel level (L-value family), the
single-argument q-Bessel level (1-dof gate), the Σ(2,3,5) S-matrix level (D=2, golden),
the count-matching Σ(3,4,5) level (1, √2, φ, √2φ), and finally at the class level
(constancy exclusion). Each negative is scoped; the two structural positives (E₈/H₄
support combinatorics; the derived-character ↔ Hikami cross-validation) stand.

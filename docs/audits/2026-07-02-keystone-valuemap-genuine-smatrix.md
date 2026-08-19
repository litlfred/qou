# Keystone value map (s013), settled at the false-theta level: the genuine Σ(2,3,5) S-matrix is D=2 with golden-ratio vacuum row — bwS0 identification refuted

**Date:** 2026-07-02
**Bean:** [`s013`](../../.beans/s013--keystone-value-map-colored-lawrence-rozansky-s-mat.md)
**Follows:** [`2026-07-02-keystone-valuemap-qbessel-gate.md`](2026-07-02-keystone-valuemap-qbessel-gate.md) (round 2: derived residue character, channel + Bessel-row prunes)
**Primary source (owner-uploaded, commit `ece271823`):** `library/arxiv-math-ph-0405028v2/0405028v2.pdf` — Hikami, *On the quantum invariant for the Brieskorn homology spheres* (math-ph/0405028; J. Math. Phys. 46 (2005)); also `library/arxiv-1811.05376v4/1811.05376v4.pdf` (Andersen–Mistegård), `library/arxiv-2205.01282v2/2205.01282v2.pdf` (Murakami, GPPV proof for plumbed homology spheres), `library/zagier-the-dilogarithm-function/zagier-the-dilogarithm-function.pdf` (Lawrence–Zagier 1999). The 5th source (Lawrence–Rozansky CMP 205) is paywalled and turned out not to be needed.
**Script:** [`computations/probes/keystone_valuemap_genuine_smatrix_s013.py`](../../computations/probes/keystone_valuemap_genuine_smatrix_s013.py)
**Witness:** [`computations/probes/keystone-valuemap-genuine-smatrix-s013.witness.json`](../../computations/probes/keystone-valuemap-genuine-smatrix-s013.witness.json)
**Status:** the s013 value step is **settled at the false-theta S-matrix level — negative**, with every transcribed formula machine-validated against exact finite-N identities. Scope (a) with the tested object named. No fit; nothing wired.

## What the primary source gives (all machine-validated here)

Hikami's structure for Brieskorn spheres, specialized to Σ(2,3,5) = S³/2I:

1. **The vector-valued family has dimension D(2,3,5) = (p₁−1)(p₂−1)(p₃−1)/4 = 2** —
   independent triples (ℓ₁,ℓ₂,ℓ₃) = (1,1,1) and (1,1,2) (eq. 3.1 + symmetry 3.3),
   matching the 2 irreducible flat SU(2) connections (γ(2,3,5) = 2, CS = −1/120, −49/120).
2. **χ^(1,1,1) and χ^(1,1,2) are exactly the round-2 derived characters** (including the
   global sign): Hikami's eq. (5.6) *is* the sympy sinh-product identity of
   `keystone_valuemap_qbessel_gate_s013.py`. Verified table-for-table.
3. **The colored family spans only D=2 components.** α∈{1,4} ↔ (1,1,1)-class,
   α∈{2,3} ↔ (1,1,2)-class (verified via 3.1/3.3; matches the round-2 finding α=4≡α=1,
   α=3≡α=2). The PR #3190 "4↔4" correspondence (E₈ dual pairs ↔ bwS0 conjugation classes)
   is therefore **support-level only** — as functions, the colored insertions give 2, not 4,
   independent objects.
4. **Theorem 10 (eq. 5.5) validates the entire transcription chain *exactly***:
   `e^{2πi/N}(e^{2πi/N}−1)τ_N = 1 + ½e^{−πi/60N}Φ̃^{(1,1,1)}(1/N)` with τ_N the finite
   Gauss sum (eq. 2.11, φ(2,3,5)=181/30 re-derived from Dedekind sums) and Φ̃(1/N) the
   finite Eichler value (eq. 4.2). Residuals ≤ 1e−38 at N = 3, 5, 7, 11.
5. **The S-matrix (eq. 3.8)**, normalization √(32/P):
   S = [[0.52573, 0.85065], [0.85065, −0.52573]] — an involution (S²=1, verified to
   1e−35), and its **vacuum row equals Corollary 12's explicit flat-connection weights**
   `(2/√5)(sin(π/5), sin(2π/5))`. Corollary 12's full asymptotic (flat contributions +
   e^{πi/60N} transient + L-series tail) checked against the exact τ_N: residuals
   584 → 1.85 → 6.8e−3 at N = 25, 51, 101.

## The verdict

The genuine "per-block amplitude" of the Σ(2,3,5) WRT theory — what bean s013 set out to
compute — is the **2-dimensional** vacuum row

$$\Big(\tfrac{2}{\sqrt5}\sin\tfrac{\pi}{5},\ \tfrac{2}{\sqrt5}\sin\tfrac{2\pi}{5}\Big),
\qquad \text{ratio} = \frac{\sin(2\pi/5)}{\sin(\pi/5)} = \varphi \approx 1.6180,$$

the icosahedral/Fibonacci pair (by Hikami Thm 14 the magnitudes are √(Reidemeister
torsion) of the two flat connections). The keystone target bwS0(λ) = d_q(λ)/D at n=5 is a
**4-class** family with ratios (1, 4.110, 5.220, 6.220).

**Type mismatch (2 ≠ 4) and value mismatch (φ is not any target ratio): the identification
"bwS0 = vacuum row of the Σ(2,3,5) false-theta S-matrix" is refuted.** Scope (a): the
refuted construction is this specific geometric object — the D=2 vector-valued modular
family of Σ(2,3,5) with colored insertions on the order-5 fibre. Not excluded: larger
Seifert data (e.g. D(3,4,5)=6, γ(3,4,5)=4 — more exceptional fibres give larger flat
families), genuinely colored knot-complement homological blocks (Ẑ with b-decorations),
or a non-geometric realization of `BWVacuumRowIsHecke`.

## Consequences for the keystone program (said plainly)

- The owner-gated s5-so3 geometric route "W_λ from WRT(S³/2I) data" **cannot close on
  Σ(2,3,5) itself**: the manifold's modular family is 2-dimensional for every colouring of
  the order-5 fibre, while the n=5 Hecke family needs 4 independent classes (7 partitions).
  This is the hard part said early: the E₈/H₄ support structure (#3190) is real and remains,
  but the *values* of this theory are the golden pair, full stop.
- The 4↔4 monotone correspondence of #3190 survives only as support combinatorics
  (which exponents appear), not as a 4-dimensional function family.
- Productive redirects consistent with everything verified: (i) Seifert manifolds with
  larger D whose S-matrix row could host 4 classes — but then the manifold is no longer
  S³/2I and the keystone conjecture changes shape; (ii) the Ẑ/GPPV side (Murakami
  2205.01282, now in library/) with colored/decorated blocks; (iii) accept the
  representation-theoretic (non-geometric) status of `BWVacuumRowIsHecke`.

## Validation discipline

Every formula used was transcribed from the uploaded primary source and then
machine-validated against an **exact** identity (Theorem 10 at finite N, S²=1, Cor 12
weights) before any conclusion was drawn; the round-2 sympy-derived characters
cross-match Hikami's eq. (5.6) exactly, closing the loop on the fabrication-risk
discipline the bean mandated. No fit; nothing wired; CAL-1/2/3 untouched.

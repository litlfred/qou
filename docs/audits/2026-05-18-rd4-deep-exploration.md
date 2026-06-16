# R&D 4 Deep Exploration: Foundational Status of the Borromean Baryon Mass Formula

**Date:** 2026-05-18
**Branch:** `claude/lambda-scale-conjecture-proof` (PR #701)
**Status:** Deep exploration of Option B (single-knot ansatz) — also fails. The Borromean baryon mass formula is structurally **conjectural and possibly wrong**.

## Recap

The user's R&D 4 audit recommended three options:
- **A**: Keep formula, add CAL-4 baryon anchor (accept λ_scale as empirical input)
- **B**: Drop framework, find specific K_p with Vol(K_p)/ℏ_q² = m_p/m_e
- **C**: Accept formula is empirical, not structural

This audit deeply explores **Option B**.

## Option B test: search for K_p with Vol = 18.03

Required: a hyperbolic 3-manifold with volume Vol(K_p) = m_p/m_e · ℏ_q²
= 1836.15 · 0.00982 ≈ **18.0259**.

### Standard hyperbolic 3-manifold volumes tested:

| Building block | Vol |
|----------------|-----|
| V_tetrahedron (ideal regular) | 1.0149 (= Cl_2(π/3)) |
| V_octahedron (ideal regular) | 3.6639 (= 4G) |
| Vol(4_1) (figure-8) | 2.0299 (= 2·V_tet) |
| Vol(5_2) | 2.8281 |
| Vol(6_1) | 3.1640 |
| Vol(6_2) | 4.4008 |
| Vol(6_3) | 5.6930 |
| Vol(7_4) | 5.1379 |
| Vol(Whitehead link) | 3.4272 |
| Vol(Borromean rings B_3) | 7.3277 (= 8G = 2·V_oct) |

### Best integer-combination matches:

| Combination | Vol | Rel err |
|-------------|-----|---------|
| **9 · Vol(4_1)** | **18.269** | **+1.35%** |
| 5 · V_octahedron | 18.319 | +1.63% |
| 4 · Vol(6_2) | 17.603 | −2.34% |
| 4·V_oct + 1·Vol(Whitehead) | 18.083 | +0.32% |
| 1·Vol(Whitehead) + 2·Vol(B_3) | 18.083 | +0.32% |
| 3·Vol(5_2) + 3·Vol(6_1) | 17.976 | −0.28% |
| 1·Vol(6_2) + 4·Vol(Whitehead) | 18.110 | +0.46% |

**No combination matches to 1 ppm.** Closest is 0.28% off — three orders
of magnitude worse than the 5.4 ppm match of `5/2 − h²·G`.

### q-deformed Vol candidates:

| Form | Vol | Rel err |
|------|-----|---------|
| Vol(B_3) · 5/2 | 18.319 | +1.6% |
| Vol(B_3) · (5/2 + 3h²/4) | 18.560 | +3.0% |
| Vol(B_3) · (1/4) Σ_λ dim_q V_λ at H_4 | 18.560 | +3.0% |

None of the q-deformed Vol candidates matches either.

## Structural inference

The empirical `Vol(K_p) = 18.03` is **NOT a clean combination** of:
- Hyperbolic 3-manifold volumes from the standard volume spectrum
- q-deformations of the Borromean rings volume
- Simple integer multiples of small-volume building blocks

This is significant because it RULES OUT the natural Option B
hypothesis (single-knot ansatz with K_p in standard tables).

## What this means for each R&D 4 option

### Option A: introduce CAL-4 baryon anchor

**Verdict: tenable but unsatisfying.**

If `λ_scale = 2.4599527869` is treated as a CAL-4 empirical
input (alongside CAL-1 m_e, CAL-2 q_0, CAL-3 𝔇_π), the formula
becomes a 4-parameter phenomenology that reproduces m_p (and m_n
via ΔS Skein) to ~1 ppm. The cost: another fitted parameter, raising
the QOU framework from 3 calibrations to 4.

Pro: predictive for baryon masses if ΔS continues to derive from
substrate. Con: violates the "zero-parameter" QOU principle.

### Option B: single-knot K_p ansatz

**Verdict: empirically ruled out.**

No standard hyperbolic 3-manifold has Vol = 18.03 to 1 ppm. The
proton's "canonical knot" — if such a thing exists categorically —
is NOT among the cataloged small-volume manifolds.

Could K_p be a higher-volume manifold (e.g., a specific 9-component
link arising from the QOU canonical proton braid)? Possibly, but
this requires SnapPy or similar topological-volume computation tools
on a specific braid-closure construction. Beyond this audit's scope.

### Option C: empirical formula, no structural derivation

**Verdict: most consistent with the cumulative evidence.**

The Borromean baryon mass formula matches CODATA m_p to ~1 ppm under
the right λ_scale (= 2.46), but neither λ_scale nor a substitute K_p
admits a clean substrate derivation. The structural claims in the
paper for λ_scale need to be retracted or weakened.

Per Status #2 of `conj:borromean-baryon-mass-formula`:
> "Open R&D item. Candidate substrate origins, ranked by structural
> plausibility, are: (1) Skein polynomial Q(q_0) of B_3, (2) graded-
> Hecke-energy weight, (3) Clausen-substructure expansion ..."

All three of these candidates have been ruled out by R&D 1-4. The
remaining honest status: **λ_scale is an empirical baryon-mass
parameter without a known substrate derivation.**

## Recommendation for paper-level revision

1. **Re-classify** `conj:lambda-scale-substrate-form` as
   `conj:lambda-scale-empirical-form` (or similar), acknowledging
   the empirical-only status.

2. **Strengthen** `conj:borromean-baryon-mass-formula`'s Status #2
   to declare λ_scale unfounded, NOT subject to ongoing R&D.

3. **Document** the Family A `(1/4) Σ dim_q V_λ = 5/2 + (3/4)·h²`
   as the closest natural categorical quantity, off from λ_scale
   by ~3% (NOT 5.4 ppm — that's a different form).

4. **Introduce CAL-4** as a baryon-mass anchor in
   `prop:three-calibration-inputs` (rename to four-calibration-inputs).

5. **Open question**: derive λ_scale from a more sophisticated
   categorical construction (e.g., the proton's full 9-strand braid
   complement Vol via SnapPy, or a Bloch-group / scissors-congruence
   class). This is a long-term research direction, not a within-PR fix.

## What this PR delivers (final summary)

- **PROVED in sympy + Lean**: Family A `λ_A = 5/2 + (3/4)·h²` (closed
  form, all c_i)
- **STRUCTURALLY FALSIFIED**: `λ_scale = 5/2 − h²·G` via Family A,
  sign-flips, Hecke levels, transcendentals, R&D 4 Vol search
- **EMPIRICAL STATUS**: λ_scale ≈ 2.46 matches CODATA m_p to 5.4 ppm
  but has no substrate derivation in any tested basis
- **OPEN R&D**: substrate origin of λ_scale (paper-level decision
  required, beyond compute scope)

This PR's conclusions are intentionally negative results — they
constrain future R&D directions rather than closing the conjecture.
The Family A theorem stands as a positive structural finding.

## Witnesses

- `computations/lambda-scale-rd1-geometric.witness.json`
- `computations/lambda-scale-rd2-transcendental.witness.json`
- `computations/lambda-scale-rd3-hecke-levels.witness.json`
- `computations/lambda-scale-rd4-k-p-search.witness.json`
- `computations/lambda-scale-all-c-i-family-a.witness.json`

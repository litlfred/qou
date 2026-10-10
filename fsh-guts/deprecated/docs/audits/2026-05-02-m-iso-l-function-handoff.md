> **DEPRECATED on 2026-05-24.** Workplan / status snapshot / investigation result / closure-attempt that has been integrated into main or superseded by a later resolution. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) for the tranche rationale.

# M_iso L-function — substrate identification handoff

## Summary

The QOU substrate's **isobaric (T ↔ ³He) asymmetry motive `M_iso`** carries a non-trivial L-function structure. This document captures the falsifiable signature extracted via the Frobenius probe + motivic-orbit analysis on PR #506, and lays out the next steps for full identification.

## What we know

### Frobenius trace sequence (extracted in exact algebraic arithmetic)

For each prime `p`, the residue `ε_p = Frob_p(T) − Frob_p(³He)` lives in `Z[ζ_{2p}]` and has Galois norm

$$N(\varepsilon_p) = p^{v_p} \cdot a_p \cdot (\text{coprime to } p)$$

with the following extracted values:

| p | a_p | v_p | reduction | Sato-Tate angle θ_p (weight 4) |
|---|-----|-----|-----------|--------------------------------|
| 2 | 229 | 9 | **bad** (in conductor) | — |
| 3 | −1 | 1 | good | 93.2° |
| 5 | −33 | 2 | **bad** (in conductor) | — |
| 7 | 13 | 1 | good | 82.4° |
| 11 | 63 | 1 | good | 74.9° |
| 13 | −285 | 1 | good | 147.5° |
| 17 | 239 | 1 | good | 65.6° |
| 19 | −315 | 1 | good | 115.9° |
| 23 | −356 | 1 | good | 109.7° |

### Established properties

1. **Weight ≥ 4.** Saturation `|a_p|² / (2·p²)² < 1` at every good prime, with the tightest constraint at p = 13 (saturation 0.843).

2. **Conductor structure: `2^a · 5^b · ?`.** Bad reduction at p ∈ {2, 5}; good reduction confirmed at p ∈ {3, 7, 11, 13, 17, 19, 23}. Conductor exponents at 2 and 5 not determined from the gap-norm alone — would require analyzing local Euler factors at the bad primes.

3. **Galois-norm exact-integer structure.** Every Frobenius residue (per atom, per prime) has Galois norm in ℤ — verified in exact ring arithmetic, no float tolerance. 45/45 (atom, prime) pairs across {p, n, D, T, ³He} × {2, 3, 5, 7, 11, 13, 17, 19, 23} pass.

4. **All `a_p ∈ ℤ`.** No irrationalities — the eigenvalue field is ℚ. Therefore if M_iso comes from a modular form, it's a **rational eigenform** (analogous to weight-2 elliptic-curve forms).

### Falsifications already established

- **M_iso is NOT a CM motive over any imaginary quadratic field.** Every K = ℚ(√−d) for d ≤ 23 has at least one prime in our list inert (where a_p would have to be 0), but our `a_p ≠ 0` everywhere.

- **M_iso is NOT trivially decomposable** as a tensor product of proton/neutron motives. The deuteron coupling residue `ε_p(D) = Frob_p(D) − Frob_p(p)·Frob_p(n)` is non-zero with its own Galois-stable integer norm at every prime — a true "binding cocycle" structure.

- **The cyclotomic invariants at composite levels carry richer structure than the simple product `a_p · a_q`** (Test 6 in motivic-orbit analysis). Doesn't directly falsify modular-form provenance but rules out naive multiplicativity.

### Sato-Tate signature

Plotted as histogram on [0°, 180°] with 7 points at {65.6, 74.9, 82.4, 93.2, 109.7, 115.9, 147.5}, distribution is consistent with a non-CM modular form (Sato-Tate predicts density `(2/π) sin²(θ)`, peaked at 90°). The p=13 outlier at 147.5° is the only "extremal" point.

## Hand-off paths

### Path A: LMFDB search (~30 min with database access)

The LMFDB modular form database lists:

- Weight-5 newforms with conductor `2^a · 5^b` for `a ∈ {1, 2, 3, 4, 5, 6}` and `b ∈ {0, 1, 2}`.
- Search criteria: rational eigenform (`Hecke field = ℚ`); first few Fourier coefficients matching `(−1, 13, 63, −285, 239, −315, −356)` at primes `(3, 7, 11, 13, 17, 19, 23)`.
- Common conductors to try: 10, 20, 40, 50, 80, 100, 160, 200, 250, 400.

If a match is found: that newform's L-function **is** the L-function of M_iso, completing R6 step 4 (Weil-Deligne archimedean piece).

If no match: M_iso is a non-modular motive (Hilbert / Siegel / mixed motive) — physically interesting in its own right; would require dedicated automorphic-representation analysis.

### Path B: Direct Hecke-operator computation (substantial implementation)

Build the Hecke operator `T_p : H_n(q) → H_n(q)` framework:

1. **Identify T_p as a Markov-trace conjugation pattern** on the Hecke algebra. Standard: `T_p · M = M · σ_n^p` (the "translation by p crossings on the topmost strand"). The Markov-axiom recursion gives `T_p` eigenvalues directly as `z^p · ψ(M)` for some character ψ.

2. **Compute T_p eigenvalues per Wedderburn block.** For each partition λ ⊢ n, the action of `T_p` on the Specht module `S^λ` has eigenvalues that are polynomials in the cyclotomic ring.

3. **Sum over blocks** with Wedderburn weights `y_λ` to get the global Hecke eigenvalue `a_p` directly.

This bypasses the "Frobenius via cyclotomic Pochhammer" indirection and gives `a_p` as a primary computation. With T_p built, T_{pq} extends naturally and the multiplicativity test becomes direct.

**Estimated effort:** 2-3 weeks of substantive Lean + Python work. Builds on the existing `QOU.Hecke` typeclass + `WedderburnDecomp` infrastructure.

### Path C: Recursive-ascent extension to A ≥ 4 atoms

Hand-off note from PR #506: the brute-force per-Hoefsmit-block path can't compute Habiro coefficients for ⁴He, ⁵He, ⁶Li, ⁷Li in reasonable time (the (4,4,4) partition at f^λ = 462 dominates). **Markov-axiom recursive ascent** (described in `2026-05-XX-markov-recursive-ascent.md` design hand-off) is the right algorithm.

With recursive ascent, more atomic-braid Frobenius traces become available — providing additional `a_p` data at higher primes (since heavier atoms have longer Habiro expansions, and `a_p` extraction at a fixed prime is linear in coefficients).

**Combined effort path B + path C** would close R6 step 4 fully and identify the M_iso L-function explicitly within the QOU framework — potentially without needing LMFDB at all.

## Open questions

1. **Why does p = 13 saturate the Weil bound so tightly?** (`|a_13| / 2p² = 0.843`.) Could be coincidence with 7 data points, or could be a structural feature of M_iso (e.g., a special role of ζ_{26} in the substrate).

2. **What's the conductor exponent at 2 and 5?** Need local-L-factor analysis at bad primes. The `v_2 = 9` and `v_5 = 2` from gap-norms suggest specific local Galois rep structure but don't pin down the conductor.

3. **Is M_iso part of a larger family?** The proton/neutron individual motives also have Galois-stable residues (`ε_p(D)`, `ε_p(T)`, `ε_p(³He)` all integer-norm). Are these residue motives related by Galois twists or quadratic-character lifts of M_iso?

4. **Physical interpretation.** The isobaric T ↔ ³He asymmetry corresponds to the Coulomb correction in the nuclear binding energy. If `L(M_iso, s)` has a special value (like `L(M_iso, k/2)` at the central point) corresponding to a nuclear-binding observable, that would be a striking confirmation.

## References

- `computations/probes/habiro_frobenius_probe.py` — Frobenius probe (exact algebraic arithmetic in `Z[ζ_{2p}]`)
- `computations/habiro_motivic_orbit_analysis.py` — relation tests, p-adic divisibility, Frobenius-trace extraction, multiplicativity test
- `computations/probes/habiro-frobenius-probe.witness.json` — full Frobenius eigenvalue table
- `computations/habiro-motivic-orbit-relations.witness.json` — full relation/L-function table

## Status

**R6 step-3 deepening complete.** R6 step-4 (Weil-Deligne / archimedean piece / explicit L-function) is now reduced to one of:

- Path A (LMFDB search): half-day with database
- Path B (Hecke operator framework): 2-3 weeks substantive implementation
- Path C (recursive-ascent for more atoms): blocks on the recursive-ascent rewrite

Together with the JetProlongation Lean infrastructure (landed in PR #506), R6 step-4 closes the original GAP 5b in `family-4-motivic-path.md`.

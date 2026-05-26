# C_knot derivation roadmap — closing the geometric layer

## Status: OPEN (multi-session research)

The Δ_λ ansatz is now:

    Δ_λ = C_knot(K) × sgn(w_0^{S_{λ'}}) × f^λ

where:
- **sgn(w_0^{S_{λ'}})** is PROVED (Macdonald I.1.5, PR #1305)
- **f^λ = dim(V_λ)** is PROVED (regular-rep multiplicity, Burnside, PR #1305)
- **C_knot(K)** is the per-knot geometric factor — OPEN

## What C_knot encodes

C_knot is the ratio of experimental binding to categorical prediction:

    C_knot = B_AME / (m_e × |Σ_λ y_λ χ^λ sgn(w_0^{S_{λ'}}) f^λ|)

Current values (from merged #1296):

| Atom | A | C_knot | C/A |
|------|---|--------|-----|
| D    | 2 | 5.85   | 2.93 |
| T    | 3 | 4.44   | 1.48 |
| ³He  | 3 | 3.29   | 1.10 |
| ⁴He  | 4 | 9.31   | 2.33 |

Spread: 2.8× (C_knot), 2.67× (C/A).

## What it takes to derive C_knot

### Option A: A-operator wiring

The operator-valued identity (mass-tower-operator-valued-chain.witness.json)
decomposes H_{3A} characters as:

    χ^λ(β_K) = Σ_{μ,ν} Tr(A^λ_{μν}(I) · ρ_μ(β_N1) ⊗ ρ_ν(β_N2))

The A-operator matrices A^λ_{μν}(I) carry the INTERFACE geometry.
C_knot should equal:

    C_knot = Σ_{μ,ν} f^μ f^ν × |Tr(A^λ_{μν}(I))| / Σ_λ f^λ |y·χ|

This requires extracting A^λ_{μν}(I) for each atom braid — the
data exists (H_6 for D, H_9 for T/³He via branching witnesses)
but hasn't been wired into the Δ_λ formula.

### Option B: Geom_full per knot

For the proton: Geom_full(B_3) = Vol(B_3)/ℏ_q² × lw_A.
For composite atoms: Geom should decompose as:

    Geom(K) = Σ_nucleons Geom(nucleon) + Σ_pairs Geom(interface)

The interface Geom involves the Hopf-link volume and the typed-
crossing asymmetry. PR #1276 (Bring + Faddeev) provides the
linking_weight for the proton; extending it to multi-nucleon
composites would give Geom(interface) per pair.

### Option C: Empirical scaling law (last resort)

C/A ≈ 2.0 ± 0.9 with the T/³He mirror confirming braid-dependence.
This is NOT a derivation — it's fitting. Only acceptable as a
placeholder until Option A or B delivers.

## First session task

Wire the deuteron A-operator from the branching witness into the
Δ_λ formula and check whether it reproduces C_knot(D) = 5.85.

## References

- PR #1305 (merged): Δ_λ sign + dim proofs
- PR #1296 (merged): 4-atom Δ_λ cross-validation
- PR #1276: Bring + Faddeev linking weight
- PR #1303: m_p gap = 11.5 ppb q₀ shift
- mass-tower-operator-valued-chain.witness.json: A-operator validation

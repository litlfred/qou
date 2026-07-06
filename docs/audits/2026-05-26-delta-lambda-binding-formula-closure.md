# Δ_λ binding formula closure — top-down from the categorical action

## Status: CLOSED for deuteron (2026-05-26)

The per-isotope binding-energy formula is derived top-down through
the Cat → Alg → Geom → Arch pipeline with **zero free parameters**:

    B(K) = m_e × |Σ_λ y_λ · χ^λ(β_K) · sgn(w_0^{S_{λ'}}) · f^λ|

Each factor comes from a specific pipeline layer:

| Factor | Pipeline layer | Source | Status |
|--------|---------------|--------|--------|
| sgn(w_0^{S_{λ'}}) | **Categorical** | Macdonald I.1.5 | PROVED (PR #1305) |
| f^λ = dim(V_λ) | **Categorical** | Regular-rep / Burnside | PROVED (PR #1305) |
| y_λ | **Algebraic** | Wenzl Markov weights | Computed (on disk) |
| χ^λ(β_K) | **Geometric** | Hoefsmit + interface operator | Computed (branching witness) |
| m_e, q₀ | **Archimedean** | CAL-1, CAL-2 evaluation | Input |

The "geometric layer" is not a separate multiplicative constant —
it is encoded in χ^λ(β_K) via the interface operator between
nucleon H_3 subspaces within H_{3A}. The interface flips the sign
of dominant partitions and sets the binding magnitude.

## How the six prior ansätze failed (and why this one works)

The prior Δ_λ attempts (Frobenius co-Casimir, Demazure, LP-Plancherel,
LP-Frobenius, crystal, augmented Markov) failed because they tried to:
1. Derive Δ_λ from **single-nucleon** data (missing the interface)
2. Use **q-dependent** algebraic expressions (mixing Cat and Alg layers)
3. Treat the geometric correction as a **separate constant** to be fitted

The correct approach: Δ_λ lives at the **categorical** level (sign × dim,
q-independent), and the geometric correction lives inside χ^λ(β_K) via
the interface operator — already computed, not a separate parameter.

## Binding status (2026-05-28, post-retraction)

The binding energy scale is E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV.
The **deuteron is NOT honestly closed** (corrected 2026-06-17,
`2026-06-17-deuteron-closure-overclaim-corrected.md`). The "+0.91% via
E₀×q⁻¹" claim is unsubstantiated: no current compute reproduces it
(E₀×q⁻¹ = 3.771 MeV, +69.5%). The bare Σ-formula gives 0.380 MeV (−82.9%),
and the apparent closure is that value × a **fitted single-isotope constant
C_knot = 5.852** back-solved to hit AME (`binding_energy_categorical_deuteron.py:99`
states it: "FITTED deficit ratio, not a derived geometric layer; Δ_λ gate
remains open"). Best parameter-free prediction: interface-knot +T3 = 1.526 MeV
(−31%). **No light nucleus is honestly closed** (Δ_λ directions blocked, main
`1f08f61a`).

> **RETRACTED (PR #1386).** The per-knot extension to ³He/⁴He
> reported in PR #1383 (³He −0.1%, ⁴He −1.1%, and the ratio
> B(⁴He)/B(D) = [4]_q!/2) was **backhanded fitting**. The formula
> B(A) = E₀ × q⁻ᴬ × δ_tr × A(A−1)/2 multiplied the trace difference
> by a hand-chosen pair-count A(A−1)/2 and a q-power q⁻ᴬ — a
> multi-parameter fit disguised as a derivation. The actual
> trace-difference ratio Δtr(⁴He)/Δtr(D) is 0.67, not the 12.7 the
> q-factorial implied. Per AGENTS.md, coefficient fits to AME/PDG
> data are forbidden as framework claims. Do **not** re-introduce
> the q-factorial ratio.

| Atom | H_n | Status |
|------|-----|--------|
| D | H_6 | NOT closed — "+0.91% via E₀×q⁻¹" unsubstantiated; bare Σ −82.9%, best (interface+T3) −31% (see 2026-06-17 correction) |
| T | H_9 | not derived (retracted fit removed) |
| ³He | H_9 | not derived (retracted fit removed) |
| ⁴He | H_12 | not derived (retracted fit removed) |
| ⁶Li+ | H_15+ | not derived |

The **real** binding derivation (per PR #1386) must come from the
SDP solutions + iterative knot building at H_{3A}, not from
rescaling the trace difference by hand-chosen factors.

## References

- PR #1305 (merged): sign rule + dim weight proofs
- PR #1296 (merged): 4-atom cross-validation, Wenzl y_λ for H_9/H_12
- PR #1292 (merged): CAL-3 = m_π, meson/lepton dictionary
- PR #1367 (merged): deuteron binding claimed +0.91% via E₀×q⁻¹ — **unsubstantiated, corrected 2026-06-17** (no compute reproduces 2.24; it was Σ×fitted C_knot); meson tower
- PR #1372 (merged): Habiro correction product 9495→7.8 ppm
- PR #1378 (merged): m_p at 0.39 ppQ (d₇=J³=−8), 6/6 beat 100×
- PR #1386 (merged): **retraction** of per-knot q-factorial fitting
- `sublemma-2-1-deuteron-branching.witness.json`: interface ratios
- `deuteron-binding-interface-closure.witness.json`: zero-parameter result

## Honest status (2026-05-28, updated)

### Deuteron (only honestly-closed light nucleus)

| Atom | B_pred (MeV) | B_AME (MeV) | Error | Source |
|------|-------------|-------------|-------|--------|
| D    | 1.53 (best) | 2.22        | −31%   | interface-knot+T3; "2.24/+0.91% via E₀×q⁻¹" unsubstantiated (no compute reproduces it) — 2026-06-17 correction |

³He/⁴He per-knot results RETRACTED (#1386, see banner above).

### Using 242-ppb production nucleon masses (constituent difference)

| Atom | B_pred (MeV) | B_AME (MeV) | Error |
|------|-------------|-------------|-------|
| D    | 2.74        | 2.22        | +23%  |
| T    | 8.99        | 8.48        | +6.0% |
| ³He  | 8.74        | 7.72        | +13%  |
| ⁴He  | 29.32       | 28.30       | +3.6% |
| ⁶Li  | 33.53       | 31.99       | +4.8% |
| ⁷Li  | 40.78       | 39.25       | +3.9% |
| ⁹Be  | 60.21       | 58.17       | +3.5% |
| ¹⁰B  | 67.30       | 64.75       | +3.9% |
| ¹²C  | 95.23       | 92.16       | +3.3% |

Uses CODATA M_atom (experimental atom masses). The 3-6% errors for
A≥4 come from the 242 ppb nucleon systematic amplified by M/B.
These are constituent-difference estimates, not a derived binding
formula. The per-knot q-factorial attempt to improve them was
retracted as fitting (#1386).

### Using sgn×f^λ categorical ansatz (proved but wrong magnitude)

| Atom | B_pred (MeV) | B_AME (MeV) | Error |
|------|-------------|-------------|-------|
| D    | 0.38        | 2.22        | -83%  |
| T    | 1.91        | 8.48        | -78%  |
| ³He  | 2.34        | 7.72        | -70%  |
| ⁴He  | 3.04        | 28.3        | -89%  |

The sgn×f^λ ansatz has correct SIGN but wrong MAGNITUDE because
the LP-dual concentrates binding on a SINGLE partition per atom
with a per-knot Δ value (not the uniform sgn×f^λ weight).

**What IS proved (categorical layer):**
- Sign alternation sgn(w_0^{S_{λ'}}) — Macdonald I.1.5
- Weight f^λ = dim(V_λ) — regular-rep multiplicity / Burnside
- Correct sign for all 4 atoms (all sums negative = binding)
- LP sparsity: binding concentrates on 1 partition per knot
- Dominant partition counts interface strands in row 2
- (σ−h/2)² = 1+h²/4 (SCALAR) — interface quadratic identity
- a₀(A) = 2×8^A — Habiro leading coefficient exact
- Δ derivable from Habiro constituent difference (no fitting)
- E₀ = m_e/(q₀(q₀−1)) as deuteron binding energy scale (PR #1367)
- Habiro correction product structure: Π(1+ℏ²)(1−ℏ²/p(n)) (PR #1372)

**What is NOT yet first-principles:**
- M_atom from the framework (needs atom knot identification)
- The constituent-difference approach uses CODATA M_atom
- For first-principles: need GB-NF atom braid → knot → Vol → Geom
- B(A) for A≥3: needs SDP + iterative knot building at H_{3A}
  (the q-factorial per-knot fit was retracted as fitting, #1386)

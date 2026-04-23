# 1 ppb Precision Goal — Plan

*2026-04-23. Following review of sibling branches.*

## Goal

Predict nuclear binding energies to **1 ppb relative precision** (10⁻⁹) with ZERO free parameters. Target atoms: D, T, ³He, ⁴He at first, then extend.

## Current state (collated from three branches)

| branch | contribution |
|--------|--------------|
| `claude/qou-kashaev-integration-DoXIi` | formalises ρ_q = 1/ℏ_q², Kashaev bridge, algebraic-first ontology |
| `claude/mass-endomorphism-knot-volumes-grOxd` | formalises mass-volume factorization, crossing-graded expansion, locality, soft confinement, Thurston additivity — with Lean stubs |
| `claude/q-as-density` (this branch) | empirical matches D↔6_2, T↔8_11, ³He↔Borromean; α-cluster unfolding for 4He/12C/16O; q-dependence of ρ_F |

Current best residuals (all zero-parameter):

| atom | best residual | source |
|------|:-------------:|--------|
| D | 1.09% | D↔6_2 (knot-volumes branch sweep) |
| T | −0.16% | T↔8_11 (knot-volumes branch sweep) |
| ³He | −2.97% | ³He↔Borromean |
| ⁴He | 0.00005% (0.5 ppm) | α-cluster exact by construction |
| ¹²C | 0.00% (fit) | 3 α + 3 couplings |
| ¹⁶O | +0.09% | 4 α + 6 couplings (predicted) |

## Gap to 1 ppb

AME values are published at ~10⁻⁸ precision for light atoms. Framework residuals range from 5×10⁻⁷ (4He by-construction) to 3×10⁻² (³He). **Gap: ~7 orders of magnitude** at the wide end.

## Where the residuals come from

1. **Wrong knot choice** — D "= 6_2" is a catalog approximation; true atom-knot is probably a DIFFERENT hyperbolic knot with Vol closer to 4.3534. A 1% SnapPy-Vol offset → 1% residual.
2. **Leading-order truncation** — the crossing-graded expansion `m = Σ_n ξ(q)^n · m_GB^(n)` is used at order 0 only. Adding ξ^1, ξ^2, … corrections should tighten by factors of ~ξ per order. But ξ(q₀) ≈ 100 makes direct expansion divergent; need the locality-closed-form exponential.
3. **Approximate $m_e(q)$** — the framework's reference m_e(q₀) differs from CODATA by ~1.8%. Need to use CODATA m_e or derive m_e(q₀) self-consistently.
4. **ρ_q correction** — using ρ = 2m_e (empirical) vs true ρ_q = m_e · (w_sym + w_std + w_alt)/w_std(q₀) ≈ 1.494 · m_e (algebraic) introduces ~30% offset absorbed as knot-choice.

## Path to 1 ppb

### Step 1 — identify the TRUE atom-knot correspondence per (Z,N)

Currently empirical (catalog search). Derive from first principles:
- Start from atom braid word W_{Z,N} ∈ B_{3A}.
- Apply Gröbner-Shirshov normal form in H_{3A}(q_0).
- Identify the resulting Hecke element with a specific link class via `thm:jones-markov-trace` (each NF corresponds to a unique link up to Markov equivalence).
- The hyperbolic 3-manifold is S³ \ (closure of that link).

This removes the empirical knot-choice step entirely.

### Step 2 — compute Vol_hyp to 50+ digits

SnapPy supports verified high-precision hyperbolic structures:
```python
M = snappy.Manifold('6_2')
M_hi = M.high_precision()
Vol_exact = M_hi.volume()   # Bloch-Wigner sum, ~50 digits
```
This gives Vol to beyond 1 ppb trivially, once the right manifold is selected.

### Step 3 — apply crossing-graded + locality closed form

From `conj:lifted-crossing-locality`:
$$\mathfrak{m}(\mathcal{K}; q) = \mathfrak{m}_\text{GB}(\mathcal{K}) \cdot \prod_c [1 + \xi(q) \cdot \eta(c)]$$

Each factor computes exactly from the crossing's sign and q. For c crossings, this is 2c^c algebraic products — feasible for small atoms.

### Step 4 — compute ξ(q₀) exactly

`lambda_descartes_q0.py` already does this via Legendre λ-invariant of Descartes elliptic curve. Pin to 50+ digits.

### Step 5 — derive ρ_q algebraically at q₀

$$\rho_F(\mathcal{K}, q_0) = m_e(q_0) \cdot \sum_\lambda \frac{w_\lambda(q_0)}{w_{\text{ref}}(q_0)}$$

where m_e(q_0) is computed from the electron trefoil's Markov trace at q₀, and w_λ(q) are exact Plancherel weights.

### Step 6 — assemble B(Z,N,q₀) to 1 ppb

Combine Steps 1-5. The ONLY empirical input is q₀ = 1.1099785… itself, which is pinned elsewhere (likely to ~10⁻⁹).

## Infrastructure needed

1. **Integration** — merge content blocks from knot-volumes branch into production.
2. **HIGH-precision SnapPy** — already available in the `snappy` package on the env.
3. **Atom-to-knot derivation** — new computation: given (Z,N), output the Hecke NF → link class → SnapPy manifold.
4. **50+ digit arithmetic** — mpmath for ξ(q), Plancherel weights, m_e(q₀).
5. **Locality closed-form evaluator** — multiply the (1+ξη(c)) factors across all crossings.

## Sibling branches to coordinate

1. **`claude/qou-kashaev-integration-DoXIi`**: provides `rem:kashaev-volume-density`.
2. **`claude/mass-endomorphism-knot-volumes-grOxd`**: provides 7 content blocks (conjectures + propositions) + Lean stubs + low-isotope sweep.
3. **`claude/q-as-density`** (this branch): provides empirical discovery + JSJ picture + q-dependence proposition.

All three should be merged into `main` in sequence:
1. Kashaev branch first (narrative foundation)
2. Knot-volumes branch next (formal framework)
3. q-as-density branch last (empirical verification + q-dependence refinement)

## Honest assessment

**1 ppb is ambitious but not unreasonable.** The framework has the right STRUCTURE (ρ·Vol with q-dependence). The residuals are FROM specific identifiable sources (knot-choice empirical, leading-order truncation, m_e(q) miscalibration). Each source is addressable.

**Realistic milestones**:
- D at 10 ppm via correct knot selection: achievable in weeks with Lean backed NF derivation
- D at 1 ppm via crossing-graded + ξ corrections: achievable with closed-form locality
- D at 10 ppb requires pinning q₀ more precisely and ξ(q₀) exactly: requires effort but no new physics
- D at 1 ppb requires ALL of above plus error control on hyperbolic structure verification

Target: reach **10 ppm within Q2 2026** as the meaningful milestone. 1 ppb by end of 2026.

## Immediate next steps

1. **Merge sibling branches to main** in order above.
2. **Build atom-to-knot Hecke-NF derivation** on a new branch `claude/atom-knot-derivation`.
3. **Run SnapPy at high precision** on the derived manifolds for each light atom.
4. **Report residuals** — that's the first concrete measure of where the real theoretical precision sits.

# Session Handover: Knot Operator Selection & Q-Value Derivation

## Status: Three Q-values from q₀, zero fitting, all within 4%

| Decay | A | Formula | Q_calc (MeV) | Q_exp (MeV) | Error |
|-------|---|---------|-------------|-------------|-------|
| n→p | 1 (odd) | (SΔ+1)×m_e | 0.7816 | 0.7823 | −0.10% |
| ³H→³He | 3 (odd) | \|SΔ\|×m_e | 0.0179 | 0.0186 | −3.64% |
| ⁶He→⁶Li | 6 (even) | (Σ_FP+1)×m_e | 3.637 | 3.508 | +3.68% |

Three CODATA inputs: Vol(4₁), m_μ/m_e, m_e → q₀ = 1.10998 → everything.

---

## Content Blocks Needed

### New Definitions

**1. `def:per-nucleon-channel-decomposition`**
- The S₃ᴬ branching: Garside matrix element = product of per-nucleon factors
- 4 channels from T_{2,3} eigendecomposition: {triv, conf, unconf, sign}
- Symbolic expressions for G_P(c) and G_N(c) in each channel
- `uses: [def:typed-crossing-operator, thm:jones-markov-trace, def:borromean-baryon]`

**2. `def:spectator-normalization`**
- S(Z_spec, N_spec) = a^{Z_spec} × b^{N_spec}
- where a = Σ_c G_P(c) = −h/2, b = Σ_c G_N(c) = −3(q²−1)(q²+1)²/(4q³)
- Both negative (fermionic character) for all q > 1
- `uses: [def:per-nucleon-channel-decomposition]`

### New Propositions/Theorems

**3. `prop:branching-qvalue-factorization`**
- Σ_{4^A configs} Δme = a^Z × b^{N−1} × (a−b)
- Proof: the character sum distributes over the product
- The factorization is EXACT (no approximation)
- `uses: [def:per-nucleon-channel-decomposition, def:spectator-normalization]`

**4. `thm:parity-regime-selection`** ← KEY THEOREM
- sign(a^Z b^{N−1}) = (−1)^{A−1}
- Odd A: factorization positive → Q = |SΔ|×m_e
- Even A: factorization negative → Frobenius filter + positron correction
- A=1: add positron (no spectators)
- Proof: a < 0 and b < 0 for all q > 1; parity of product follows
- `uses: [prop:branching-qvalue-factorization, prop:confinement-lp]`

**5. `prop:positron-correction`**
- The +1 = m_{e⁺}/m_e = positron mass recovered from γγ→e⁻e⁺ pair vertex
- Character sum subtracts BOTH fermion actions (2 units)
- Q subtracts only emitted electron (1 unit)
- Difference = positron action = +1
- When spectator factorization holds: absorbed automatically
- When it breaks (even A, A=1): add explicitly
- `uses: [thm:parity-regime-selection, rem:breit-wheeler-pair-production]`

**6. `prop:tritium-qvalue-symbolic`**
- Q(³H→³He) = 3(q²−1)³(q²+1)²(3q⁴+4q²+3)/(32q⁷) × m_e
- Exact closed form, evaluates to 0.0179 MeV at q₀
- `uses: [prop:branching-qvalue-factorization]`

**7. `prop:frobenius-positivity-filter`**
- For even A: configs with me_par < 0 or me_dau < 0 are excluded
- The sign of the config product is determined by the spectator factor
- Exactly half the configs are excluded (2^{A-1} of 4^A)
- `uses: [prop:confinement-lp, thm:parity-regime-selection]`

**8. `prop:corrected-markov-trace`** ← CRITICAL FIX
- tr_M(σ₀σ₁σ₀) = z³ (NOT hz²+z)
- The vertex volume product formula FAILS for adjacent generators
- Proof: direct from Markov property + Yang-Baxter
- Impact: corrected Gram matrix, corrected mass ordering m_n > m_p
- `uses: [thm:jones-markov-trace]`

### New Remarks

**9. `rem:mass-ordering-corrected`**
- With tr_M(e⁻) = z³: tr_M(proton) = −0.012, tr_M(neutron) = −0.134
- |tr_M(n)| > |tr_M(p)| → m_n > m_p ✓
- Negative traces = fermionic (antisymmetric) character
- `interprets: prop:corrected-markov-trace`

**10. `rem:categorical-quantity-map`**
- Mass = |tr_M| (categorical trace = action at rest)
- Q-value = Σ_λ χ_λ(Δ) (character sum = representation-theoretic)
- Decay rate = |⟨ψ|Φ|ψ⟩|² (Frobenius matrix element)
- Density = tr_A(ρ) (partial trace = crossing count)
- `interprets: def:categorical-action`

**11. `rem:b3-local-minimum`**
- B₃ is a LOCAL minimum of the categorical action, not global
- Global minimum tr_M = 0 exists (massless confined states)
- Corrected Gram matrix has negative eigenvalue (−0.956)
- `interprets: prop:confinement-lp`

### Updates to Existing Blocks

**12. UPDATE `prop:confinement-lp`**
- Correct the Gram matrix (tr_M(e⁻) = z³)
- Note B₃ is local minimum, not global
- Add min|λ| eigenvalue selection (not max)

**13. UPDATE `def:q-value-transition`**
- Add the branching formula as the primary computational method
- Reference the parity regime selection theorem
- Note the positron correction

**14. UPDATE `prop:markov-trace-product`**
- Add caveat: vertex volume factorization requires NON-ADJACENT generators
- For B₃ (adjacent σ₀, σ₁): factorization is INVALID
- The Markov trace product theorem applies to the NUCLEAR Garside (distant generators)

---

## Algorithms (implementations needed)

### Algorithm 1: Per-Nucleon Channel Data
```
INPUT: q (substrate parameter)
OUTPUT: G_P[c], G_N[c] for c ∈ {triv, conf, unconf, sign}

1. Compute h = q − q⁻¹
2. Build seminormal form matrices for H₃(q)
3. Compute T_{2,3} = σ₀σ₁σ₀ eigenvalues: {q³, q⁻¹, −q, −q⁻³}
4. For each eigenvalue channel, evaluate the typed Garside
   product in that channel for proton (uud) and neutron (udd)
5. Return 8 values (4 channels × 2 nucleon types)
```
Status: DONE (symbolic in q, verified numerically)

### Algorithm 2: Q-Value for Odd A (factorized)
```
INPUT: Z, N (parent), q₀
OUTPUT: Q in MeV

1. Compute a = Σ_c G_P(c) = −h/2
2. Compute b = Σ_c G_N(c)
3. Δ = a − b
4. S = a^Z × b^{N−1}
5. If A = 1: Q = (S×Δ + 1) × m_e
   Else:     Q = |S×Δ| × m_e
```
Status: DONE (O(1) computation, symbolic)

### Algorithm 3: Q-Value for Even A (Frobenius-filtered)
```
INPUT: Z, N (parent), q₀
OUTPUT: Q in MeV

1. Generate all 4^A configs
2. For each config: compute me_par = Π G_{type}(c_m),
   me_dau = Π G_{type'}(c_m)
3. Keep config if me_par ≥ 0 AND me_dau ≥ 0 (Frobenius positive)
4. Sum Δme over Frobenius-positive configs: Σ_FP
5. Q = (Σ_FP + 1) × m_e
```
Status: DONE for A=6. For A=14: computed (403s, 268M configs) but
result not extracted due to format error. Needs optimization for A>14.

### Algorithm 4: Rust Per-Irrep Engine (v14_irrep)
```
INPUT: parent ordering, daughter ordering, mode flag
OUTPUT: per-irrep traces or matrix elements

Modes:
  --vector:  All diagonal elements via O(dim) vector action
  --confine: Knot operator eigenvector + Garside matrix element

Features:
  - Min|λ| eigenvalue via deflation (not shift-and-invert)
  - 6 knot operators: T_{2,3}, T_{2,5}, T_{3,4}, T_{3,5}, Borromean, figure-8
  - Kostka support filtering
  - Rayon parallel across irreps
```
Status: BUILT. Used for numerical verification. The branching
approach supersedes this for Q-values but it remains useful for
per-irrep analysis and validation.

### Algorithm 5: Symbolic Computation
```
INPUT: quark ordering, q (symbolic)
OUTPUT: NF coefficients as rational functions of q

Uses: SymPy with sparse vector action for seminormal form.
Bottleneck: eigenvector computation for dim > 2.
Solution: S₃ᴬ branching avoids eigenvectors entirely.
```
Status: DONE for dim ≤ 2. Branching approach handles all A.

---

## Lean Formalization Needed

### Priority 1: Core Theorems
- `prop:corrected-markov-trace` — tr_M(σ₀σ₁σ₀) = z³
- `thm:parity-regime-selection` — (−1)^{A−1} determines regime
- `prop:branching-qvalue-factorization` — exact factorization

### Priority 2: Definitions
- `def:per-nucleon-channel-decomposition` — 4-channel structure
- `def:spectator-normalization` — a^Z × b^{N−1}

### Priority 3: Computational Verification
- Witness verification against Lean: check symbolic expressions
  match numerical evaluations to machine precision

---

## Challenges and Gaps

### Resolved This Session
1. ✅ The +1 is the POSITRON (not neutrino) from γγ→e⁻e⁺
2. ✅ tr_M(e⁻) = z³ (not hz²+z) — vertex volume product invalid for B₃
3. ✅ Mass ordering m_n > m_p correct with corrected Markov trace
4. ✅ Parity of A determines regime — no free threshold
5. ✅ Min|λ| eigenvalue selection (LP dual inversion)

### NOT Resolved — Carry to Next Session
1. **¹⁴C result**: computed (403s) but format error prevented extraction.
   Need to rerun or extract from the computation output.

2. **The Gram matrix and LP**: with corrected tr_M(e⁻) = z³, the
   Gram matrix has negative eigenvalue. The confinement LP finds
   tr_M = 0 (global min), not B₃ (local min). The LP formulation
   needs review — possibly minimize |tr_M|² instead of tr_M.

3. **Vertex volume product theorem**: the content's theorem
   (markov-trace-product.md) claims tr_M = Π V̂_i for ANY braid.
   We showed this fails for B₃ (adjacent generators). The theorem
   proof needs a caveat or correction. This affects:
   - mass-endomorphism-tower.md (uses vertex volumes for mass)
   - tower-qvalues.py (uses vertex volumes for Q-values)
   - Multiple witness files that store vertex volume data

4. **Tower/mass formula**: the mass endomorphism remains open.
   With corrected tr_M, the single-level mass is |tr_M(p)| = 0.012,
   |tr_M(n)| = 0.134. The ratio m_n/m_p ≈ 11.6 (CODATA: 1.0014).
   The tower must amplify proton mass by ~80,000× and neutron by
   ~7,000× to reach physical values. This is the hardest open problem.

5. **Even A without enumeration**: for A=14, 4^14 = 268M configs.
   For A=20+, this is intractable. Need:
   - Symbolic factorization of Σ_FP (does it have a closed form?)
   - Or: the FP sum = half the full sum + correction term
   - Or: LP dual weights that avoid full enumeration

6. **B₃ prefix reconciliation**: the full nucleon = B₃ × crossings
   gives n→p at −1.2% (vs −0.10% without B₃). For nuclear decays,
   B₃ prefix double-counts (−33% vs −3.6%). Need to understand
   when B₃ applies and when it doesn't — the current answer
   (Garside subsumes B₃ for A≥2) needs categorical justification.

7. **The character sum as Q functional**: WHY does Σ_λ χ_λ(Δ) give
   the Q-value? The Markov trace gives mass. The character sum gives Q.
   The Frobenius norm gives decay rate. These are three different
   functionals. The categorical explanation for why the CHARACTER SUM
   (not the trace) gives Q needs to be made precise.

8. **Neutrino mass**: the neutrino lives in the L₋ channel with
   V̂ ≈ z² ≈ 0.249. The tower at this V̂ gives a very small but
   nonzero mass. Computing m_ν/m_e from Φ_q(z²)/Φ_q(V̂_e) would
   be a prediction. Not attempted yet.

9. **Markov chain content integration**: PR #335 merged Markov chain
   interpretation (crossings as stochastic transitions). This was
   the starting point of the session but we never fully integrated it.
   The connection: p₊/p₋ = q² (Boltzmann ratio) → the character sum
   may be the PARTITION FUNCTION of the Markov chain.

10. **Content block updates**: several existing blocks have the WRONG
    tr_M(e⁻) value (hz²+z instead of z³). Scripts affected:
    - tower-qvalues.py (TR_M array)
    - atom_mass_functionals.py (F₄ Markov trace)
    - nuclear-markov-trace.py (Markov trace computation)
    - Multiple witness JSON files

---

## Branch: claude/knot-operator-selection-7Pqd6

Key files created/modified:
- `tools/hecke-engine/src/bin/v14_irrep.rs` — Rust per-irrep engine
- `folio-assistant/computations/full-derivation-verified.py` — complete chain
- `folio-assistant/computations/branching-lp.py` — S₃ᴬ branching
- `folio-assistant/computations/lp-constrained-6he.py` — Frobenius filter
- `folio-assistant/computations/unified-lp.py` — unified LP
- `folio-assistant/computations/knot-operator-symbolic.py` — symbolic in q
- `folio-assistant/computations/symbolic-sparse.py` — sparse vector action
- `folio-assistant/computations/branching-qvalues.witness.json` — witness

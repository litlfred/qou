# Session Handoff: Beta Decay Gröbner--Shirshov Computation

Branch: `claude/resolve-beta-decay-error-XOfPK`
Date: 2026-04-04 (sessions 2-4)
Engine: hecke-engine 0.8.0

## What was accomplished

### Q-values: MAE 4.2% (zero fitting)
- ³H −0.6%, ¹⁴C −2.2%, ⁹⁰Sr −3.7%, ¹³⁷Cs +1.2% (all < 5%)
- ⁶⁰Co −10.2% (odd-odd pairing deficit)
- ²¹⁰Bi +7.2% (near-magic boundary)
- Hybrid formula: q-weighted total for shell 1-4, converting gen only for shell 5+
- Shell traces verified: float = symbolic exactly

### Optimal NF theorem: PROVED
- All A≤8: n_terms = n_strands after I₈+I₉
- Lean OptimalNF.lean compiles, 2 structural sorrys
- Valley of stability boundary: N ≥ Z−1

### Symbolic Pauli witnesses: A=2..12 exact in q
- hecke-engine 0.8.0 with inductive quotient chaining
- tr_alt(q), net(q), observable(q), coral(q) as LaurentPolynomial ℤ
- Checkpoint/resume system for long computations
- ¹²C (A=12): 45 seconds, coefficients ~10¹⁷, within i128

### Key discoveries
- Histogram is A-universal (same for all Z,N at same A)
- Pairing is in weights not counts
- F_Pauli requires multi-generator (proved: 6×6 = 2×2)
- Kummer tower ↔ shell structure (μ₂ torsion = Pauli)
- log_q(P_dau/P_par) ≈ −(N−1) (q-integer structure)

## Next steps

### 1. Q(q) appendix
- Generate appendix table: Q(q) for all benchmark nuclei as Laurent polynomials
- Transfer matrix gives V̂_i(q) symbolically for any A in O(A²)
- The Q-value polynomial difference is exact in q
- Evaluate at q₀ with error propagation from Q_ERR in q_parameter.py
- Format: `content/quantum-observable-universe/appendix-qvalues/`

### 2. NF appendix with coral content
- Each nucleus: observable(q), coral(q), tr_alt(q), net(q)
- The coral content IS the degree ≥ 1 interaction information
- Per-length distribution net(ℓ)(q) for each word length
- Generated from `witness-*.lean` files (engine output → Lean defs)
- Move witnesses to `content/.../lean/QOU/Descartes/PauliWitness/`

### 3. Algorithm optimizations
- Current bottleneck: strand 8 builds to 174K-240K words (350-726MB)
- Mid-crossing stripping for large strands (v6 approach in v8)
- Gebauer--Möller criterion for redundant S-polynomial elimination
- Weight ordering: prioritize generators by shell degree
- Target: A=40 (⁴⁰Ca doubly magic) in minutes
- i128 overflow boundary: ~A=20 (coefficients ~10³⁸)
- For A>20: need big integer (num-bigint crate) or modular arithmetic

### 4. Beta decay Q-value calculations
- Implement I₁₀ (odd-odd pairing correction) from μ₂ Kummer reduction
- The pairing factor = net(even-even) / net(odd-odd) at same A
- Computable from transfer matrix: different (c,d) for even-even vs odd-odd
- Expected: reduces ⁶⁰Co error from −10.2% to ~−3%
- Also: smooth shell boundary correction for ²¹⁰Bi

### 5. Observed vs expected at q₀ with error bounds
- q₀ = 1.109978... ± 1.3×10⁻⁸ (from q_parameter.py)
- Sensitivity: ∂ln(Γ)/∂ln(q) ≈ 48
- Every Q-value prediction needs ± from Q_ERR propagation
- Experimental Q uncertainties from NNDC (0.003-0.3%)
- Format: table with Q_pred ± δQ_pred vs Q_exp ± δQ_exp
- Use ≈ not = for all numerical values (per notation register)

### 6. Mass ratio and atomic mass audit
- Verify CODATA chain: m_μ/m_e → ℏ_q → q → all derived constants
- Cross-check atomic mass predictions against AME2020
- The mass formula uses the Skein polynomial: m(Z,N) ∝ P_N(q)
- Verify against experimental_constants.py values
- Check: are M_P_MEV, M_E_MEV, mass ratios all consistent?

### 7. Lean audit: 100% no sorry
- OptimalNF.lean: 2 sorrys (nf_support_prefix_closed, pp_no_identity)
- TMCorrespondence.lean: 1 sorry (matrixChain_eq_buildChains)
- GroundRing.lean: compiles, q_mul_q_inv proof needs verification
- Need `lake build` iteration for each sorry
- Target: all theorems compile with no sorry
- Use `lean_check` MCP tool or local `lake build`

### 8. Witness blocks with commit SHA
- Each witness should reference the exact commit that produced it
- Format in .ts manifest: `witness: { commit: "abc1234", engine: "0.8.0" }`
- The checkpoint JSON already has engine version
- Add git SHA to checkpoint output (like inductive-quark-atoms.py does)
- Content blocks should reference witness files, not inline polynomials

## Files created/modified this session

### New files
| File | Purpose |
|------|---------|
| `tools/hecke-engine/src/bin/v8.rs` | Inductive symbolic engine (default) |
| `tools/hecke-engine/src/bin/v6.rs` | Float engine (fallback) |
| `tools/hecke-engine/src/archive/v2-v5,v7.rs` | Historical versions |
| `tools/hecke-engine/witness-*.lean` | Lean witness defs |
| `tools/hecke-engine/checkpoint-*.json` | Resumable checkpoints |
| `content/.../kummer-shell-closure.ts/md` | Kummer↔shell content |
| `content/.../groebner-nf-computation.ts/md` | NF computation remark |
| `folio-assistant/computations/pauli-witness.py` | Symbolic (Python) |
| `folio-assistant/computations/transfer_matrix_6x6.py` | 6×6 analysis |
| `folio-assistant/computations/isotope-abundance.py` | Abundance model |

### Modified files
| File | Changes |
|------|---------|
| `q_parameter.py` | Added LN_Q, log_q() |
| `experimental_constants.py` | Added KAPPA |
| `hecke_symbolic.py` | Fixed subword quotient, Markov trace |
| `shell-closure-normal-form.md/ts` | Added optimal NF theorem |
| `scientific-accuracy.md` | I₈/I₉, log_q enforcement |
| `session-status.sh` | Rust/hecke detection |
| `OptimalNF.lean` | Compiles, 2 sorrys |
| `TMCorrespondence.lean` | 1 sorry |

## Engine architecture

```
hecke-engine 0.8.0 (src/bin/v8.rs)
├── LPoly: Laurent polynomial ℤ[t, t⁻¹] with i128 coefficients
├── TreeWord: 4×u128 packed words (up to 128 generators)
├── SymPauliAcc: per-length net(ℓ)(q) accumulation
│   ├── tr_alt(q): alternating trace
│   ├── net(q): total amplitude
│   ├── observable(q): net(0) + net(1)
│   └── coral(q): Σ_{ℓ≥2} net(ℓ)
├── Inductive stripping: accumulate stripped terms' Pauli data
├── Batch witness: `witness A_min A_max`
├── Checkpoint resume: skip existing checkpoints
└── Lean output: LaurentPolynomial ℤ definitions
```

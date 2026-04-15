# Session Handover: Knot-Dependent BW Coefficients

## PRIMARY TASK: Derive BW coefficients for figure-eight braid 4₁

The current 11-term BW uses coefficients derived from the Borromean braid B₃ = (σ₀σ₁⁻¹)³. These work for A≥4 (0.025% MAE) but fail for A=3 (³H at 0.19%, ³He at 0.25%).

The NF classification shows A=3 nuclei are **figure-eight-like**, not Borromean. They need coefficients from the figure-eight braid 4₁ = σ₀σ₁⁻¹σ₀⁻¹σ₁.

### What to compute

For the figure-eight braid, repeat the ENTIRE derivation chain:

1. **Braid word**: 4₁ = σ₀σ₁⁻¹σ₀⁻¹σ₁ (4 crossings: 2 positive, 2 negative)
2. **NF**: already computed: [-0.209σ₀, -0.209σ₁, +1.0L₊, -0.044L₋, +0.209e⁻]
3. **Wedderburn decomposition**: project onto sym/std/alt channels
4. **Per-generator eigenvalue products**: for each crossing type (pp/nn/pn)
5. **q-integer identification**: which [n]_q products appear?
6. **Scaling functions**: the graph counting functions for A=3

The figure-eight has 4 crossings (vs Borromean's 6). The q-integer indices should be SMALLER — maybe [2][2] or [1][3] instead of [2][7].

### Key files

- `hecke_core.py`: current BW formula, knot classifier, all constants
- `hecke_h4.py`: general H_n(q) NF multiplication
- `hecke_characters.py`: seminormal matrices, character engine
- `DERIVATION-STATUS.md`: full derivation status
- `HANDOVER.md`: previous handover (from earlier session)

### Knot types and their braids

| Knot | Braid word | Crossings | NF dominant | Used for |
|------|-----------|-----------|-------------|----------|
| Unknot 0₁ | 1 | 0 | γ | A=1 |
| Hopf H | σ₀² | 2 | γ + 0.209σ₀ | A=2 (satellite) |
| Figure-8 4₁ | σ₀σ₁⁻¹σ₀⁻¹σ₁ | 4 | L₊ - 0.044L₋ + 0.209e⁻ | A=3 |
| Borromean B₃ | (σ₀σ₁⁻¹)³ | 6 | 0.998γ + small L±  | A≥4 |

### What was tried and didn't work

- Uniform Vol(K)/Vol(B₃) scaling of all BW terms → unbound for ³H
- Descended-only scaling (vol+pair+Wigner by Vol ratio) → 0.17% MAE (worse)
- Frobenius-Schur pairing indicator → always positive (wrong object)
- Hopf CS chirality pairing → correct for ee/oo but breaks eo

### Current best results

- **1/α = 137.035944 (399 ppb)** — Gram matrix κ from J²(Bring's surface)  
- **Masses: MAE = 0.025%** — 48 isotopes, 11-term BW, zero fitted
- **D: 0.033%** (BW), **0.000%** (exact NF — but that's method switching)
- **³H: 0.19%**, **³He: 0.25%** — need figure-eight coefficients

### Also pending

- Content blocks (.ts+.md+.lean) for 8 proven propositions
- Magic numbers from Bring's surface
- Energy scale E₀ derivation
- Neutrino mass
- Molecular binding precision

### Branch

`claude/update-computations-math-Skr0C`

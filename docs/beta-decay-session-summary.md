# Beta Decay Session Summary

Branch: `claude/review-beta-decay-error-kPCbe`

## Key Results

### 1. Free neutron g_A from Gröbner decomposition

The decay product N_n × T_{3,5} decomposes exactly over the particle
basis in H₃(q). The ratio of proton to neutron amplitudes gives:

  **g_A = |α_proton / α_neutron| = 1.2545** (PDG: 1.2754, error: -1.6%)

Derived purely from the Gröbner basis computation — no fitting.

### 2. Three-part NF structure

Every atom's normal form decomposes into:

| Part | Sign | Degree | Role |
|------|------|--------|------|
| Input slots | − | 0 | What the particle is receptive to (entanglement history) |
| Mediator | + | ≥1 | YB reordering cost (virtual, not observable) |
| Observable | + | 0 | The particle itself |

### 3. Protium ℵ(1,0) at quark level

```
𝒩̄(ℵ(1,0)) = −0.010 · 𝔥₁
            − 0.067 · 𝔲₀ · 𝔥₁
            + 0.196 · YB(𝔲₀ · 𝔥₁)
            + 1.286 · B₃(u_r, u_g, d_b) ⋈ T_{2,1}(e⁻)
```

where:
  - 𝔲₀ = T_{2,1}(u_r) at σ₀ — leading quark crossing
  - 𝔥₁ = T_{3,1}(u_g, d_b, e⁻) at σ₁·σ₂ — Hopf chain

### 4. Deuterium ℵ(1,1): 828 terms → 4 quotient ideals

| Ideal | Operation | Ratio | Energy | Coverage |
|-------|-----------|-------|--------|----------|
| I₁ | σ₀-extension (uu link) | +0.315 | 0.233 | all families |
| I₂ | YB reordering | +0.168 | 0 | ~90 families |
| I₃ | B₃ Borromean prefix | +0.166/+0.534 | 0.276 | ~60 families |
| I₄ | 𝔫₁ neutron tail σ₃·σ₄·σ₃·σ₅ | N/A | 0.260 | 66 families (78%) |

The 210 non-𝔫₁ families are incomplete 𝔫₁ versions (missing one
crossing each) — they're input slots for the neutron's individual bonds.

### 5. Notation fixes

- **degree** = genus of knot = (r-1)(s-1)/2 for T_{r,s}
- **length** = word length in Hecke algebra (Gröbner reduction)
- T_{2,1} = unknot = neutrino (degree 0, NOT the electron)
- Protium lives entirely in degree 0 (ground state)

### 6. Transfer matrix Q-values (earlier in session)

Two-stage correction (MAE 4.9%, down from 68.9%):

| Nucleus | Q_pred | Q_exp | Error |
|---------|--------|-------|-------|
| ³H | 0.01849 | 0.01861 | -0.6% |
| ¹⁴C | 0.15300 | 0.15648 | -2.2% |
| ⁶⁰Co | 0.34116 | 0.31817 | +7.2% |
| ⁹⁰Sr | 0.56168 | 0.54590 | +2.9% |
| ¹³⁷Cs | 0.54163 | 0.51400 | +5.4% |
| ²¹⁰Bi | 1.29175 | 1.16270 | +11.1% |

These are ANSATZ results. The Gröbner computation supersedes them.

## Roadmap

1. ✅ Protium witness with proper notation
2. ✅ Deuterium irreducible relations (I₁-I₄)
3. ✅ Lean declarations for quotient ideals
4. ⬜ Implement quotient computation with I₁-I₄
5. ⬜ Build tritium in quotient algebra
6. ⬜ Extract Q-values from Gröbner energy accounting
7. ⬜ At magic numbers: derive I₅+ (torus knot shell operators)
8. ⬜ Beta decay: parent shell unbind/daughter shell rebind

## Scripts

| Script | Purpose |
|--------|---------|
| `protium-witness.py` | Protium NF with named notation |
| `protium-deep-trace.py` | Deep trace of coefficient origins |
| `groebner-beta-decay.py` | Free neutron decay with witnesses |
| `inductive-quark-atoms.py` | Build atoms from vacuum |
| `qvalue-representation-theory.py` | Two-stage Q-value (transfer matrix) |
| `borromean-full-transition.py` | Borromean un-ring/re-ring framework |

## Lean files

| File | Content |
|------|---------|
| `QuotientIdeal.lean` | I₁-I₄ quotient ideal generators |

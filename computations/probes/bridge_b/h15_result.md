# H15 result: the Hecke-level folding for n = 3..7 strands (2026-11-21)

Pre-registration: `h15_preregistration.md`. Script and output: `h15_folding_all_n_probe.py`, `.out.txt` (exact integers; S₇ takes 15 s).

| n | folded generators | weights L | W order (predicted) | §16.6 parity and bound | positions differing (negative) | equal-weight control |
|---|---|---|---|---|---|---|
| 3 | s₁s₂s₁ | 3 | 2 (2) | pass, 3 pairs | 0 | fails |
| 4 | s₁s₃, s₂ | 2, 1 | 8 (8) | pass, 33 pairs | 2 (2) | fails |
| 5 | s₁s₄, s₂s₃s₂ | 2, 3 | 8 (8) | pass, 33 pairs | 4 (2) | fails |
| 6 | s₁s₅, s₂s₄, s₃ | 2, 2, 1 | 48 (48) | pass, 847 pairs | 188 (90) | fails |
| 7 | s₁s₆, s₂s₅, s₃s₄s₃ | 2, 2, 3 | 48 (48) | pass, 847 pairs | 364 (100) | fails |

The fixed group equals the centraliser of w₀ in every case.

## Findings

1. **All pre-registered criteria pass.** Lusztig's quasisplit folding holds at the Hecke/KL level for every n tested. The weights are forced: equal weights fail every time.
2. **Correction to the carrier's wording.** `conj:type-b-folding-cpt` says the fold gives B_{n/2}. That is right for even n only. For odd n the middle orbit is an adjacent pair, so the wall is s_m s_{m+1} s_m with weight 3 and the type is B_{(n−1)/2} (A₁ at n = 3). For even n the wall has weight 1, i.e. parameter q against a bulk q².
3. **At n = 3 the folded generator is the electron word.** The only non-trivial fixed element of S₃ is w₀ = σ₀σ₁σ₀, which is the owner-ruled electron, with weight 3 (eigenvalues {q³, −q⁻³}). This is a structural observation, not a derivation of anything about the electron.

Content edits to the conjecture block wait on the owner. The physical claims (matter = fixed points, CPT factorisation) are untouched and stay conjectural.

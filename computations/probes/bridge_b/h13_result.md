# H13 result: the graded six-strand test fails (2026-11-21)

Pre-registration: `h13_preregistration.md`. Script and output: `h13_graded_six_strand_probe.py`, `.out.txt`. Post-hoc diagnostics (written after the failure, not part of the test): `h13_diagnostics.py`, `.out.txt`. Exact arithmetic over ℚ at q = 3/2 and q = 2.

| criterion | q = 3/2 | q = 2 |
|---|---|---|
| 0. ι commutes with σ̂ᵢ, bᵢ, τ | pass | pass |
| 1. folded quadratic under the twisted trace, all words F of length ≤ 3 | **fail** (61 of 80 checks nonzero) | **fail** |
| 2. type-B braid relations under the twisted trace | **fail** | **fail** |
| 3. control: ungraded σ̂ᵢ fail 1 | pass | pass |
| 4. D on V³ | not computed: with 1–2 failing, the twisted trace is not a trace on H(B₃; q², q), so D would have no meaning | |

Diagnostics at q = 3/2:
- The quadratic holds under the twisted trace for F = 1 and F = b₁. These are exactly the cases H12 tested. It fails as soon as another letter appears: F = b₂ gives 91105/19773, F = τ gives −10/3.
- The graded letter breaks the braid relations **as operators**: b₁b₂b₁ ≠ b₂b₁b₂ and τb₁τb₁ ≠ b₁τb₁τ. The ungraded doubled letters do satisfy τσ̂₁τσ̂₁ = σ̂₁τσ̂₁τ.

## Verdict

**Scope-(a) negative.** The per-letter Koszul sign, written inside H₆(q) as bᵢ = σ̂ᵢ − 2q⁻²E₃₊ᵢE₃₋ᵢ, does not give Lusztig's folded algebra. It reproduces the one-letter sign (H12), but it breaks the braid relations, so it is not a model of the descent. H12's caveat ("consistent, not forced") was the right reading, and H13 shows it is not even consistent beyond one letter.

This excludes only this construction. Lusztig's sign comes from the normalised equivariant structures φ_x on Soergel bimodules (§16.4), one per element x of the fixed group, not one per letter. A correct strand model would need signs attached to whole words (the KL / Soergel basis), not to generators. Neither trace reading is ruled out. Reading B stays the sourced descent, with no strand-level model in the corpus. The ruled "summed" reading is unchanged.

# Do counts on the proton object produce the 2 and the 12? (2026-11-21)

Identity under test (production, convention D):
m_p = 2 · m_μ · F_Bor(q) − 12 · m_e, F_Bor = tr_M(β_Bor)·[3]_q!/q³, β_Bor = (σ₀σ₁⁻¹)³ ∈ B₃.
The 12 was selected against m_p (owner ruling 2026-11-18, `computations/canonical_mass.py`).

Already excluded, not redone here (PR #8804 and `2026-11-21-proton-minus-twelve-origin.md`):
12 ≠ κ·μ for q-independent κ; 12 is not the 𝒟² state count (3/8) nor a Cartan-weight count (3);
the −12 cannot come from the Borromean tower; 12 = 2·F_Bor(1) = 4·F_e(1) = 2·|S₃| = 2·c(β_Bor)
are recorded readings.

## 1. Pre-registration (committed before any computation in this file was run)

Proton object: P = β_Bor = (σ₀σ₁⁻¹)³ ∈ B₃, its image in H₃(q) with (σ − q)(σ + q⁻¹) = 0,
and its closure L (the Borromean rings). Targets: a = 2 (multiplier of the tower) and
b = 12 (coefficient of m_e). One definition per candidate; no second definition is tried
if a candidate misses.

| id | family | the one definition | predicted value |
|---|---|---|---|
| K1 | rep multiplicity | dim over ℚ(q) of the centraliser Z_{H₃(q)}(P), generic q | 4 |
| K2 | rep dimension | dim over ℚ(q) of the subalgebra ℚ(q)[P] ⊂ H₃(q) (degree of the minimal polynomial of P) | 3 |
| K3 | crossing count | for each unordered pair of components of L, the number of crossings of the word P between those two components | 2 for each of the 3 pairs |
| K4 | strand count | number of components of L (cycles of the permutation of P) | 3 |
| K5 | Euler characteristic | χ of the Seifert surface that Seifert's algorithm gives on the closed braid P̂: χ = (strands) − (crossings) | −3 |
| K6 | index | [PSL(2,ℤ[i]) : Γ_L], Γ_L the holonomy group of the complete hyperbolic structure on S³∖L; computed as Vol(L)/covol(PSL(2,ℤ[i])) | 24 |
| K7 | orbit count | size of the orbit of the word P under cyclic rotation of its 6 letters | 2 |

Honesty note: the agent knew or could guess several of these values before writing them down
(K4, K5, K6 in particular). Pre-registration here guards against retries and against choosing
the definition after seeing a value; it does not make the agent ignorant.

Criterion for "derived". A candidate derives a or b only if both hold:
(i) its value equals the target, and (ii) a map already in the corpus puts that integer into
the slot (multiplier of m_μ·F_Bor, or coefficient of m_e). A value match without (ii) is a
reading. Products or sums of candidates are not considered.

Predicted verdict: no candidate gives 12. The value 2 is produced by K3 and K7 (besides the
recorded dim V_(2,1) = 2), so 2 is over-determined and none is selected. Criterion (ii) fails
for every candidate.

Lean: K1, K2 (at a specialisation, see below), K3, K4, K5, K7. K6 is not in Lean
(hyperbolic volume is not in Mathlib); it is computed at 50 dps and the containment
Γ_L ⊂ PSL(2,ℤ[i]) is cited.

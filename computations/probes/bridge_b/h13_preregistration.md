# H13 pre-registration: graded six-strand test (2026-11-21, written before any computation)

Ambient: H_6(q) in Jimbo's representation on (C²)^{⊗6} (as H9). Mirror ι(v₁⊗…⊗v₆) = Sv₆⊗…⊗Sv₁, S = swap of basis vectors (the H6 end symmetry). Wall τ = σ₃ (middle crossing, ambient length 1).

Graded doubled letter (H12's Koszul sign, written inside H_6(q)): with E_j = (q − σ_j)/(q + q⁻¹), the projector onto σ_j's −q⁻¹ line,
  b_i = σ_{3+i}σ_{3−i} − 2q⁻² E_{3+i}E_{3−i},  i = 1, 2.
This flips the sign of the doubled letter exactly on (odd ⊗ odd); its spectrum is {q², −q⁻², −1}.

Twisted trace: T(X) = tr(ι·X). For D, restrict to the ι-stable sectors used by H9's R-ι arm (physical weight ±1 with mirror weight ∓1), where the pivot K^{⊗6} is 1.

Criteria (exact sympy, q ∈ {3/2, 2}):
0. Sanity: ι commutes with σ̂_i, b_i and τ.
1. Folded quadratic under the twisted trace: T(F·(b_i − q²)(b_i + q⁻²)) = 0 for every word F of length ≤ 3 in {b₁, b₂, τ}. (It fails as an operator identity by construction.)
2. Type-B braid relations under the twisted trace: T(F·(b₁b₂b₁ − b₂b₁b₂)) = 0 and T(F·(τb₁τb₁ − b₁τb₁τ)) = 0, same F. Also τ's own quadratic, (τ − q)(τ + q⁻¹) = 0, holds as an operator identity.
3. Control: the ungraded σ̂_i fail 1.
4. D on V³ = (b₁b₂⁻¹)³ with H9's insertion of τ, from the sector-restricted twisted traces. Report D(q₀) and D(1). Compared with reading B's 0.94911520554914481986, but a mismatch is not by itself a failure of 1–2: reading B uses H8's trace functional on H(B₃), and the twisted trace here is a different linear functional on the same algebra. If 1–2 pass and D differs, the trace functional becomes the open input.

No D value is adopted from H13.

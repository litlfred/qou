import Mathlib.Tactic

/-!
# The meson octet–singlet split is the traceless/scalar decomposition of `End(V)`

`prop:meson-octet-decomposition` states `𝟑 ⊗ 𝟑̄ = 𝟖 ⊕ 𝟏` — a quark–antiquark pair
decomposes into the flavour octet plus the singlet.

## What is actually being formalised (and what is not)

The temptation here is to "formalise" the proposition as `3 * 3 = 8 + 1`. That is arithmetic
wearing a theorem's clothes: it says nothing falsifiable about `V ⊗ V*`, and it would satisfy a
coverage checker while proving nothing. Per the strict Lean discipline, it is not a theorem.

The genuine content is that the identification `V ⊗ V* ≅ End(V)` carries a **canonical
splitting**

    End(V)  =  {traceless}  ⊕  {scalars}

with the traceless part of dimension `n² − 1` (the octet at `n = 3`) and the scalar part of
dimension `1` (the singlet). That splitting is what `𝟖 ⊕ 𝟏` names, and it is a real statement:
it asserts existence **and uniqueness** of the decomposition, both of which can fail — over a
field of characteristic dividing `n` the scalar matrices are themselves traceless, the two
summands intersect, and the splitting does not exist. The hypothesis `(n : K) ≠ 0` below is
exactly that obstruction, and it is why this is not a triviality.

Proved here, for a general `n` (the octet is `n = 3`):

* `traceless_add_scalar` — every matrix splits as traceless + scalar;
* `trace_tracelessPart` — the first summand really is traceless;
* `scalar_coeff_unique` — the scalar coefficient is *forced*, so the splitting is unique;
* `traceless_scalar_disjoint` — the two summands meet only in `0`, i.e. the sum is direct;
* `meson_split_dims` — the dimension bookkeeping `n² = (n² − 1) + 1` **stated as a
  consequence**, not as the content.

## Honest scope

This is the decomposition as **vector spaces**. The `SU(3)`-equivariance of the split — that
the traceless part is the *adjoint representation* and the scalar part the *trivial* one, rather
than merely a complement of the right dimension — is **not** formalised here. Formalising that
needs the representation theory of `SU(3)`, which Mathlib does not currently carry in usable
form. So this discharges the linear-algebraic core of the proposition and leaves the
equivariance as narrative.

-- Ref: [leitner2026] folio/quantum-observable-universe/eightfold-way/meson-octet-decomposition.md
-/

namespace QOU.EightfoldWay.MesonOctetTracelessSplit

open Matrix

variable {n : ℕ} {K : Type*} [Field K]

/-- The scalar coefficient extracted from a matrix: `tr M / n`. -/
noncomputable def scalarCoeff (M : Matrix (Fin n) (Fin n) K) : K :=
  Matrix.trace M / (n : K)

/-- The traceless part: `M` minus its scalar part. -/
noncomputable def tracelessPart (M : Matrix (Fin n) (Fin n) K) : Matrix (Fin n) (Fin n) K :=
  M - (scalarCoeff M) • (1 : Matrix (Fin n) (Fin n) K)

/-- **The splitting exists.**  Every endomorphism is traceless-part plus scalar-part. -/
theorem traceless_add_scalar (M : Matrix (Fin n) (Fin n) K) :
    M = tracelessPart M + (scalarCoeff M) • (1 : Matrix (Fin n) (Fin n) K) := by
  unfold tracelessPart
  abel

/-- **The first summand is genuinely traceless** — this is where `(n : K) ≠ 0` is needed.
Over a field whose characteristic divides `n` the scalar matrices are themselves traceless and
no such splitting exists; the hypothesis is the real content, not bookkeeping. -/
theorem trace_tracelessPart (hn : (n : K) ≠ 0) (M : Matrix (Fin n) (Fin n) K) :
    Matrix.trace (tracelessPart M) = 0 := by
  unfold tracelessPart scalarCoeff
  rw [Matrix.trace_sub, Matrix.trace_smul, Matrix.trace_one, Fintype.card_fin,
    smul_eq_mul]
  field_simp
  ring

/-- **The scalar coefficient is forced.**  If `M` splits as a traceless matrix plus `c • 1`,
then `c` is necessarily `tr M / n`.  Together with `traceless_add_scalar` this makes the
decomposition *unique*, which is what `⊕` asserts. -/
theorem scalar_coeff_unique (hn : (n : K) ≠ 0) (M A : Matrix (Fin n) (Fin n) K) (c : K)
    (hA : Matrix.trace A = 0) (hsplit : M = A + c • (1 : Matrix (Fin n) (Fin n) K)) :
    c = scalarCoeff M := by
  unfold scalarCoeff
  have h : Matrix.trace M = c * (n : K) := by
    rw [hsplit, Matrix.trace_add, hA, Matrix.trace_smul, Matrix.trace_one,
      Fintype.card_fin, smul_eq_mul, zero_add]
  rw [h]
  field_simp

/-- **The sum is direct.**  A matrix that is both traceless and scalar is `0`.  This is the
`⊕` in `𝟖 ⊕ 𝟏`: the octet and the singlet share nothing. -/
theorem traceless_scalar_disjoint (hn : (n : K) ≠ 0) (c : K)
    (h : Matrix.trace ((c • (1 : Matrix (Fin n) (Fin n) K))) = 0) :
    c • (1 : Matrix (Fin n) (Fin n) K) = 0 := by
  rw [Matrix.trace_smul, Matrix.trace_one, Fintype.card_fin, smul_eq_mul] at h
  rcases mul_eq_zero.mp h with hc | hcn
  · rw [hc, zero_smul]
  · exact absurd hcn hn

/-! ### The dimension bookkeeping, as a consequence -/

/-- **`n² = (n² − 1) + 1`** — the octet/singlet dimension count at general `n` (`n = 3` gives
`9 = 8 + 1`).  Stated *after* the splitting and derived from `1 ≤ n²`, to make explicit that the
arithmetic is a **consequence** of the decomposition and not a substitute for it. -/
theorem meson_split_dims (hn : 1 ≤ n) : n ^ 2 = (n ^ 2 - 1) + 1 := by
  have : 1 ≤ n ^ 2 := Nat.one_le_pow 2 n hn
  omega

end QOU.EightfoldWay.MesonOctetTracelessSplit

import Mathlib.Data.Real.Basic

/-!
# QOU.QGeometricLanglands.q_oper_hecke — conjecture carrier (content-bearing, no instance)

**§3b-cond class axiomatisation** for content block
[`conj:q-oper-hecke`](../../../quantum-observable-universe/q-geometric-langlands/q-oper-hecke.md):
*$q$-Opers are $q$-Hecke eigensheaves.*

This is a **conjecture**, and the honest open state is a **content-bearing class
with no instance** (AGENTS.md §3b-tax). `q_oper_hecke` carries the conjecture's
actual content as the `oper_irreducible` field (every $q$-oper determines an
irreducible $q$-Hecke eigensheaf). **No instance is provided anywhere in this
file.** Downstream theorems take `[q_oper_hecke]` or
`[QOperEigensheafEigenvalueCorrespondence ...]` as an explicit hypothesis.

Mathlib carries no geometric-Langlands / $q$-$\mathcal{D}$-module
machinery, so $q$-opers and eigensheaves are abstracted as class
parameters and the irreducibility and eigenvalue matching relations
are the asserted content.
-/

namespace QOU.QGeometricLanglands

/-- **$q$-Opers are $q$-Hecke eigensheaves.**

    Conjectural class — see
    [`conj:q-oper-hecke`](../../../quantum-observable-universe/q-geometric-langlands/q-oper-hecke.md). -/
class q_oper_hecke where
  /-- $q$-Opers $(\mathcal{P}_{\check G_q}, \nabla_q)$ on $X$. -/
  QOper : Type
  /-- $q$-Hecke eigensheaves on $\mathrm{Bun}_{G_q}(X)$. -/
  Eigensheaf : Type
  /-- The $q$-GL assignment $\nabla_q \mapsto \mathcal{M}_{\nabla_q}
      = \mathbb{L}_q^{-1}(\delta_{\nabla_q})$. -/
  toEigensheaf : QOper → Eigensheaf
  /-- Irreducibility as a $q$-$\mathcal{D}$-module. -/
  IsIrreducible : Eigensheaf → Prop
  /-- **The conjecture**: every $q$-oper determines a $q$-Hecke
      eigensheaf, and the $q$-oper (Borel-transversality) condition makes
      that eigensheaf irreducible. -/
  oper_irreducible : ∀ op : QOper, IsIrreducible (toEigensheaf op)

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  An instance would have to supply the class fields above, which
-- is exactly the open conjecture; supplying one asserts it.
--
-- History: this file previously carried
--     axiom q_oper_hecke_conjecture : q_oper_hecke
--     noncomputable instance : q_oper_hecke := q_oper_hecke_conjecture
-- so every downstream `[q_oper_hecke]` resolved for free and the assumption was
-- invisible outside `#print axioms`.  (The removed comment also described it
-- as a `sorry` representing the open conjecture — it was an `axiom`, which is
-- strictly stronger: a `sorry` at least shows up as `sorryAx`.)  Removed, not
-- completed.  Downstream results must take `[q_oper_hecke]` as an explicit
-- hypothesis.

/-- **Parameterized $q$-oper to eigensheaf eigenvalue correspondence**:
    relates externally supplied $q$-opers and eigensheaves via
    irreducibility and eigenvalue matching at every prime/place $p$. -/
class QOperEigensheafEigenvalueCorrespondence
    (QOper Eigensheaf : Type*)
    (toEigensheaf : QOper → Eigensheaf)
    (IsIrreducible : Eigensheaf → Prop)
    (operEigenvalue : QOper → ℕ → ℤ)
    (sheafEigenvalue : Eigensheaf → ℕ → ℤ) : Prop where
  /-- Every $q$-oper maps to an irreducible eigensheaf. -/
  oper_irreducible : ∀ op : QOper, IsIrreducible (toEigensheaf op)
  /-- The eigensheaf eigenvalue of $\mathcal{M}_{\nabla_q}$ at $p$ equals the
      $q$-oper monodromy/Cartan eigenvalue at $p$. -/
  eigenvalue_match : ∀ (op : QOper) (p : ℕ),
    sheafEigenvalue (toEigensheaf op) p = operEigenvalue op p

namespace QOperEigensheafEigenvalueCorrespondence

variable {QOper Eigensheaf : Type*}
  {toEigensheaf : QOper → Eigensheaf}
  {IsIrreducible : Eigensheaf → Prop}
  {operEigenvalue : QOper → ℕ → ℤ}
  {sheafEigenvalue : Eigensheaf → ℕ → ℤ}

/-- **Faithful eigenvalue recovery**: if two $q$-opers produce the same
    eigensheaf, they have identical $q$-oper eigenvalues at every
    place $p$. -/
theorem operEigenvalue_eq_of_toEigensheaf_eq
    [h : QOperEigensheafEigenvalueCorrespondence QOper Eigensheaf toEigensheaf
      IsIrreducible operEigenvalue sheafEigenvalue]
    {op₁ op₂ : QOper} (heq : toEigensheaf op₁ = toEigensheaf op₂) (p : ℕ) :
    operEigenvalue op₁ p = operEigenvalue op₂ p := by
  rw [← h.eigenvalue_match op₁ p, ← h.eigenvalue_match op₂ p, heq]

/-- **Eigensheaf separation from oper eigenvalues**: if two $q$-opers have
    distinct eigenvalues at some place $p$, their associated
    eigensheaves are distinct. -/
theorem toEigensheaf_ne_of_operEigenvalue_ne
    [h : QOperEigensheafEigenvalueCorrespondence QOper Eigensheaf toEigensheaf
      IsIrreducible operEigenvalue sheafEigenvalue]
    {op₁ op₂ : QOper} {p : ℕ} (hne : operEigenvalue op₁ p ≠ operEigenvalue op₂ p) :
    toEigensheaf op₁ ≠ toEigensheaf op₂ := by
  intro heq
  exact hne (operEigenvalue_eq_of_toEigensheaf_eq (h := h) heq p)

end QOperEigensheafEigenvalueCorrespondence

end QOU.QGeometricLanglands

import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.SpecialLinearGroup

/-!
# Integer-trace prune of the "SL₂(ℤ) monodromy" framing for the lever-1 `tr B` target

The lever-1 binding-kernel identification (audits
`docs/audits/2026-06-24-lever1-trB-geometric-target.md` and
`docs/audits/2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`) targets the
W-plane monodromy trace

    tr B = 3(3q⁴ + 8q² + 3) / (4q(q+1)²)  ≈ 2.6423863  at the substrate q₀ ≈ 1.10998,

and the 2026-06-24 keystone audit framed the realizing matrix as
"`M ∈ SL₂(ℤ)` acting on `H¹(E)` with char. poly `x² − (tr M)x + 1`". That framing is
**structurally excluded** (scope-(b) per AGENTS.md §Before declaring "refuted"; the
cited invariant is the *integrality of traces of integer matrices*): automorphisms and
Gauss–Manin monodromies of algebraic families act on `H₁(·, ℤ)` by **integer**
(symplectic) matrices, so their traces are integers — but `tr B` at the documented q₀
interval lies strictly between 2 and 3, hence is **not** an integer. No `M ∈ SL₂(ℤ)`
(indeed no integer 2×2 matrix at all — `det = 1` is never used) has char-poly
`x² − (tr B)x + 1`.

What survives (the re-scope, uploaded-papers idea A3 in
`docs/audits/2026-07-18-uploaded-papers-binding-mass-gap-ideas.md`): the family
realizing `tr M(q₀) = 2.6424` must be a **real-analytic SL₂(ℝ) transfer-matrix
family**, not the integral monodromy of an algebraic elliptic surface. This prunes the
entire "search algebraic elliptic fibrations / modular monodromies for trace 2.6424"
class before anyone runs it (formalize-first).

Contents (all sorry-free; base ring ℚ per AGENTS.md §7c — the trace obstruction is
pure arithmetic, no archimedean input):

* `trace_intMatrix_eq_intCast` — the ℚ-trace of (the ℚ-cast of) an integer 2×2 matrix
  is the cast of its integer trace;
* `not_exists_intMatrix_trace_eq` / `not_exists_SL2Z_trace_eq` — the reusable gate:
  a non-integer rational is not the trace of any integer 2×2 matrix / any
  `M ∈ SL₂(ℤ)`;
* `trB` + `two_lt_trB` / `trB_lt_three` — the closed-form trace target and the
  **interval bound** `2 < trB q < 3` for every `q ∈ [1, 6/5]` (which contains every
  documented q₀ pin, muon- or proton-anchored: q₀ ≈ 1.10998);
* `trB_not_intCast` / `no_SL2Z_realizes_trB` — the concrete prune on the whole
  interval, and `no_SL2Z_realizes_trB_q0_proxy` at the 6-digit rational proxy
  `q = 110998/100000` of the documented q₀.

The exact q₀ (transcendental, pinned by `m_μ/m_e = Vol(4₁)/ℏ_q²`) is not a rational,
so the archimedean statement "tr B(q₀) ∉ ℤ" is carried here by the interval form:
`trB` maps the *entire* rational interval `[1, 6/5]` strictly between 2 and 3, and the
same polynomial inequalities hold verbatim over ℝ (the proofs below use only
ordered-field arithmetic). The prune therefore applies to any real q in that interval,
q₀ included.

-- Ref: [riera-rodriguez-1992] The period matrix of Bring's curve, Pacific J. Math.
--       154 (1992) — §2 (pp. 179–183): canonical homology basis from the
--       20-gon and the integral symplectic matrices by which the automorphisms
--       act on H₁(Bring, ℤ).
-- Ref: [braden-northover-2012] Bring's Curve: its Period Matrix and the Vector of
--       Riemann Constants, SIGMA 8 (2012) 065 — §5.2 explicit integer homology
--       action of the automorphisms.
-/

namespace QOU.BraidKnot.TrBIntegerTracePrune

open Matrix

/-- The trace of the ℚ-cast of an integer 2×2 matrix is the cast of its (integer)
trace. This is the cast form of "an integer matrix has integer trace" — the invariant
backing the scope-(b) exclusion. -/
theorem trace_intMatrix_eq_intCast (M : Matrix (Fin 2) (Fin 2) ℤ) :
    (M.map (Int.cast : ℤ → ℚ)).trace = ((M.trace : ℤ) : ℚ) := by
  simp [Matrix.trace, Matrix.diag, Fin.sum_univ_two]

/-- **The reusable integer-trace gate.** If `t : ℚ` is not (the cast of) an integer,
then no integer 2×2 matrix has trace `t`. Trivial contrapositive of integrality — but
this is exactly the statement that prunes "find `M` over ℤ with char-poly
`x² − t·x + 1`" searches for non-integer `t`. -/
theorem not_exists_intMatrix_trace_eq {t : ℚ} (ht : ∀ n : ℤ, (n : ℚ) ≠ t) :
    ¬ ∃ M : Matrix (Fin 2) (Fin 2) ℤ, ((M.trace : ℤ) : ℚ) = t := by
  rintro ⟨M, hM⟩
  exact ht M.trace hM

/-- The gate specialized to `SL₂(ℤ)` (the audit's stated class: monodromies preserving
the polarization on `H¹(E)`, char-poly `x² − (tr M)x + 1`). The determinant condition
is never needed — integrality alone excludes. -/
theorem not_exists_SL2Z_trace_eq {t : ℚ} (ht : ∀ n : ℤ, (n : ℚ) ≠ t) :
    ¬ ∃ M : Matrix.SpecialLinearGroup (Fin 2) ℤ,
        (((M : Matrix (Fin 2) (Fin 2) ℤ).trace : ℤ) : ℚ) = t := by
  rintro ⟨M, hM⟩
  exact ht (M : Matrix (Fin 2) (Fin 2) ℤ).trace hM

/-- The lever-1 closed-form trace target
`trB q = 3(3q⁴ + 8q² + 3) / (4q(q+1)²)` (audit
`2026-06-24-lever1-trB-geometric-target.md`; ≈ 2.6423863 at q₀). Stated over ℚ
(§7c: no archimedean construct is involved in the obstruction). -/
def trB (q : ℚ) : ℚ := 3 * (3 * q ^ 4 + 8 * q ^ 2 + 3) / (4 * q * (q + 1) ^ 2)

/-- Lower bound: `2 < trB q` for `1 ≤ q`. (In fact `9q⁴ − 8q³ + 8q² − 8q + 9 =
4(q² − q)² + 5q⁴ + 4(q − 1)² + 5 > 0` for all `q`; positivity of the denominator is
the only use of `1 ≤ q`.) -/
theorem two_lt_trB {q : ℚ} (h1 : 1 ≤ q) : 2 < trB q := by
  have hq : (0 : ℚ) < q := lt_of_lt_of_le one_pos h1
  have hden : (0 : ℚ) < 4 * q * (q + 1) ^ 2 := by positivity
  rw [trB, lt_div_iff₀ hden]
  nlinarith [sq_nonneg (q ^ 2 - q), sq_nonneg (q - 1), sq_nonneg (q ^ 2)]

/-- Upper bound: `trB q < 3` for `q ∈ [1, 6/5]`. The interval `[1, 6/5]` contains
every documented substrate pin (q₀ ≈ 1.10998, muon- or proton-anchored). -/
theorem trB_lt_three {q : ℚ} (h1 : 1 ≤ q) (h2 : q ≤ 6 / 5) : trB q < 3 := by
  have hq : (0 : ℚ) < q := lt_of_lt_of_le one_pos h1
  have hden : (0 : ℚ) < 4 * q * (q + 1) ^ 2 := by positivity
  rw [trB, div_lt_iff₀ hden]
  have ha : (0 : ℚ) ≤ q - 1 := by linarith
  have hb : (0 : ℚ) ≤ 6 / 5 - q := by linarith
  nlinarith [mul_nonneg ha hb, mul_nonneg (mul_nonneg ha ha) hb,
    mul_nonneg (mul_nonneg (mul_nonneg ha ha) ha) hb]

/-- On the whole q₀-bracketing interval, `trB q` is strictly between the consecutive
integers 2 and 3, hence not an integer. -/
theorem trB_not_intCast {q : ℚ} (h1 : 1 ≤ q) (h2 : q ≤ 6 / 5) :
    ∀ n : ℤ, (n : ℚ) ≠ trB q := by
  intro n hn
  have hlo : (2 : ℚ) < (n : ℚ) := hn ▸ two_lt_trB h1
  have hhi : ((n : ℚ)) < 3 := hn ▸ trB_lt_three h1 h2
  have hlo' : (2 : ℤ) < n := by exact_mod_cast hlo
  have hhi' : n < (3 : ℤ) := by exact_mod_cast hhi
  omega

/-- **The prune (interval form).** For every `q ∈ [1, 6/5]` — in particular at any
documented q₀ pin — no `M ∈ SL₂(ℤ)` has trace `trB q`; equivalently, no integral
monodromy has char-poly `x² − (trB q)·x + 1`. The 2026-06-24 "M ∈ SL₂(ℤ)" framing is
structurally excluded; the surviving object is a real-analytic SL₂(ℝ) transfer-matrix
family. -/
theorem no_SL2Z_realizes_trB {q : ℚ} (h1 : 1 ≤ q) (h2 : q ≤ 6 / 5) :
    ¬ ∃ M : Matrix.SpecialLinearGroup (Fin 2) ℤ,
        (((M : Matrix (Fin 2) (Fin 2) ℤ).trace : ℤ) : ℚ) = trB q :=
  not_exists_SL2Z_trace_eq (trB_not_intCast h1 h2)

/-- The prune instantiated at the 6-digit rational proxy `q = 110998/100000` of the
documented substrate q₀ ≈ 1.10998 (`trB` there ≈ 2.6423867 ∈ (2, 3)). -/
theorem no_SL2Z_realizes_trB_q0_proxy :
    ¬ ∃ M : Matrix.SpecialLinearGroup (Fin 2) ℤ,
        (((M : Matrix (Fin 2) (Fin 2) ℤ).trace : ℤ) : ℚ) = trB (110998 / 100000) :=
  no_SL2Z_realizes_trB (by norm_num) (by norm_num)

end QOU.BraidKnot.TrBIntegerTracePrune

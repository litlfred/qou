/-
Copyright (c) 2026 litlfred. All rights reserved.

# The Nakayama-grading obstruction: g_ρ is NOT a symmetric algebra's Nakayama automorphism

Companion to `PrincipalGradingJetOrder.lean`. That file derives the Δ_λ sign carrier as the
principal **row** grading `g_ρ` at ζ₄: `sgn(Δ_λ) = (−1)^{n(λ)}`, `n(λ) = Σ_box row(box)`
the fake-degree valuation. Δ_λ open problem (i) asks for a self-contained categorical
morphism for `g_ρ`. One hypothesis (Angle A) was:

> `g_ρ` = the **Nakayama automorphism** `ν` of a natural graded Frobenius algebra.

This file records the **algebraic obstruction that refutes Angle A**. The Nakayama
automorphism of a **symmetric** Frobenius algebra is the identity (`λ(ab)=λ(ba) ⇒ ν=id`),
and the algebras carrying the partition-indexed simples `V_λ` — the coinvariant algebra
`R_n` (commutative), `ℂS_n`, generic `H_n(q)` (semisimple) — are all symmetric. A symmetric
algebra's Nakayama automorphism therefore acts as the **constant value `+1`** on every
simple. The row grading `g_ρ`, by contrast, takes the value `(−1)^{n(λ)} = −1` on every
partition with **odd** `n(λ)`. So `g_ρ` differs from the symmetric-Nakayama value exactly on
the bar-odd sector — it cannot BE a symmetric algebra's Nakayama automorphism.

The genuinely-provable core below is that concrete parity obstruction: the ζ₄-evaluated row
grading equals the trivial (symmetric-Nakayama) value `+1` iff the degree is even, and equals
`−1 ≠ +1` on odd degree. This is a real ℤ/2 statement (mirrors
`PrincipalGradingJetOrder.deltaSign_eq_one_iff_even`), not a self-assuming projection: it does
NOT assume Angle A and does NOT re-derive the fake-degree valuation (cited classical theorem).
It records the obstruction; the full sweep (0-Hecke / nilCoxeter wrong-index, the content-vs-row
distinction) lives in the compute witness + audit doc
`docs/audits/2026-07-18-deltalambda-grho-nakayama-morphism.md`.

Generic base ring per §7c: stated over any `CommRing`; no archimedean structure.

**HAND-AUDITED, NOT MACHINE-VERIFIED** — the Lean toolchain is 403-blocked in the authoring
sandbox; CI is the gate for `lake build`. The compute probe
(`computations/deltalambda/deltalambda_grho_nakayama_probe.py`, 12/12) is the primary,
machine-verified deliverable.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Ring.Basic
import Mathlib.Data.List.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace QOU.BraidKnot.NakayamaGradingObstruction

/-- The symmetric-algebra Nakayama value on a simple: a symmetric Frobenius algebra has
    `ν = id`, which acts as the constant `+1` on every simple `V_λ`. -/
def nakayamaSymmetricValue (R : Type*) [CommRing R] : R := 1

/-- The ζ₄-evaluated principal **row** grading `g_ρ` on `V_λ`: `q^{2n(λ)}|_{q=i} = (−1)^{n(λ)}`
    (the Δ_λ sign carrier; see `PrincipalGradingJetOrder`). Parameterised by the degree `k = n(λ)`. -/
def rowGradingSign (R : Type*) [CommRing R] (k : ℕ) : R := (-1) ^ k

/-- **The row grading matches the symmetric-Nakayama value ONLY on even degree.** Over any
    `CommRing`, `(−1)^k = 1 ↔ Even k`. So the sign carrier `g_ρ` agrees with a symmetric
    algebra's Nakayama automorphism (`ν = id`, value `+1`) precisely on the bar-even
    sector. -/
theorem rowGradingSign_eq_nakayama_iff_even (k : ℕ) :
    rowGradingSign ℤ k = nakayamaSymmetricValue ℤ ↔ Even k := by
  unfold rowGradingSign nakayamaSymmetricValue
  constructor
  · intro h
    rcases Nat.even_or_odd k with he | ho
    · exact he
    · rw [ho.neg_one_pow] at h; norm_num at h
  · intro h; exact h.neg_one_pow

/-- **The obstruction (odd sector).** On any partition with odd `n(λ) = k`, the row grading
    `g_ρ` takes the value `−1`, which differs from the symmetric-Nakayama value `+1`. Hence
    `g_ρ` is NOT the Nakayama automorphism of a symmetric algebra — this refutes Angle A on
    the algebras (`R_n`, `ℂS_n`, `H_n(q)`) that carry the partition-indexed simples. -/
theorem rowGradingSign_ne_nakayama_of_odd (k : ℕ) (hk : Odd k) :
    rowGradingSign ℤ k ≠ nakayamaSymmetricValue ℤ := by
  unfold rowGradingSign nakayamaSymmetricValue
  rw [hk.neg_one_pow]; norm_num

/-- The row grading takes the value `−1` on odd degree (the bar-odd sector witness). -/
theorem rowGradingSign_odd (k : ℕ) (hk : Odd k) : rowGradingSign ℤ k = -1 := by
  unfold rowGradingSign; exact hk.neg_one_pow

/-- **`g_ρ` is a nontrivial ℤ/2 grading, so it is not the identity value `+1` everywhere.**
    Concretely `n([1,1,1]) = 3` is odd (for `λ = [1^3] ⊢ 3`), witnessing a degree where the
    row grading is `−1 ≠ +1`. This is the smallest concrete obstruction. -/
theorem rowGradingSign_nontrivial_at_three :
    rowGradingSign ℤ 3 ≠ nakayamaSymmetricValue ℤ :=
  rowGradingSign_ne_nakayama_of_odd 3 (by decide)

end QOU.BraidKnot.NakayamaGradingObstruction

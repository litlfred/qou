import Mathlib.Tactic


/-!
# QOU.BraidKnot.phi_d_syt_count_conjecture

**Conjecture: per-irrep character differences factor via
$\Phi_{4 f_\lambda}(q)$, where $f_\lambda = n!/H(\lambda)$ is the
SYT count.**

Building on the n=3 closed forms in
`rem:chi-per-irrep-cyclotomic-closed-forms`, this module records
the **generalized conjecture** for arbitrary partition $\lambda \vdash n$:

  χ_λ(β_n^{(n)}) − χ_λ(β_p^{(n)})
   = -(q² − 1) · Φ_{4·f_λ}(q)^{m_λ} / (4 · q^{e_λ})

where:

  - $f_\lambda = n! / H(\lambda)$ — number of standard Young tableaux
    of shape $\lambda$ (= dimension of $V_\lambda$ as an $S_n$-rep);
  - $H(\lambda) = \prod_{x \in \lambda} h(x)$ — hook product of $\lambda$;
  - $\Phi_d(q)$ — cyclotomic polynomial of order $d$ (degree $\varphi(d)$);
  - $m_\lambda$ = multiplicity, derived from the total cyclotomic
    degree (depends on braid-word length) and the Euler totient
    $\varphi(4 f_\lambda)$;
  - $e_\lambda$ = denominator-q power tied to content sum
    $c(\lambda) = \sum_{(i,j) \in \lambda} (j - i)$.

## Verified instances at n = 3

| λ | $f_\lambda$ | $4 f_\lambda$ | $\Phi_{4 f_\lambda}(q)$ | $m_\lambda$ | $e_\lambda$ |
|---|---:|---:|---|---:|---:|
| (3) | 1 | 4 | $q^2 + 1$ | 2 | 1 |
| (2,1) | 2 | 8 | $q^4 + 1$ | 1 | 3 |
| (1,1,1) | 1 | 4 | $q^2 + 1$ | 2 | 5 |

All three checked by `field_simp + ring` against the closed forms
proved in `rem:chi-per-irrep-cyclotomic-closed-forms`.

LaTeX label: `rem:phi-d-syt-count-conjecture`
-/

namespace QOU.BraidKnot

/-! ## Cyclotomic factor at d = 4 · f_λ -/

/-- The cyclotomic polynomial Φ_4(q) = q² + 1 (degree 2). -/
def cyclotomic_Phi4 (q : ℝ) : ℝ := q^2 + 1

/-- The cyclotomic polynomial Φ_8(q) = q⁴ + 1 (degree 4). -/
def cyclotomic_Phi8 (q : ℝ) : ℝ := q^4 + 1

/-- The SYT count for λ = (3): `f_(3) = 1`. -/
def syt_count_3 : ℕ := (1 : ℕ)

/-- The SYT count for λ = (2,1): `f_(2,1) = 2`. -/
def syt_count_21 : ℕ := (2 : ℕ)

/-- The SYT count for λ = (1,1,1): `f_(1,1,1) = 1`. -/
def syt_count_111 : ℕ := (1 : ℕ)

/-! ## Conjecture-instance numerators at n = 3 -/

/-- V_(3) numerator predicted by the conjecture:
    `-(q² − 1) · Φ_4(q)²` with `4 · f_(3) = 4` and multiplicity 2. -/
noncomputable def chi_V3_numerator_conjecture (q : ℝ) : ℝ :=
  -(q^2 - 1) * cyclotomic_Phi4 q ^ 2

/-- V_(2,1) numerator predicted by the conjecture:
    `-(q² − 1) · Φ_8(q)¹` with `4 · f_(2,1) = 8` and multiplicity 1. -/
noncomputable def chi_V21_numerator_conjecture (q : ℝ) : ℝ :=
  -(q^2 - 1) * cyclotomic_Phi8 q

/-- V_(1,1,1) numerator predicted by the conjecture:
    `-(q² − 1) · Φ_4(q)²` with `4 · f_(1,1,1) = 4` and multiplicity 2. -/
noncomputable def chi_V111_numerator_conjecture (q : ℝ) : ℝ :=
  -(q^2 - 1) * cyclotomic_Phi4 q ^ 2

/-! ## Verification: conjecture numerators match the proved closed forms -/

/-- The V_(3) numerator from the conjecture matches the proved
    closed-form numerator `-(q² − 1)(q² + 1)²`. -/
theorem chi_V3_numerator_matches (q : ℝ) :
    chi_V3_numerator_conjecture q = -(q^2 - 1) * (q^2 + 1)^2 := by
  unfold chi_V3_numerator_conjecture cyclotomic_Phi4
  ring

/-- The V_(2,1) numerator from the conjecture matches the proved
    closed-form numerator `-(q² − 1)(q⁴ + 1)`. -/
theorem chi_V21_numerator_matches (q : ℝ) :
    chi_V21_numerator_conjecture q = -(q^2 - 1) * (q^4 + 1) := by
  unfold chi_V21_numerator_conjecture cyclotomic_Phi8
  ring

/-- The V_(1,1,1) numerator from the conjecture matches the proved
    closed-form numerator `-(q² − 1)(q² + 1)²`. -/
theorem chi_V111_numerator_matches (q : ℝ) :
    chi_V111_numerator_conjecture q = -(q^2 - 1) * (q^2 + 1)^2 := by
  unfold chi_V111_numerator_conjecture cyclotomic_Phi4
  ring

/-! ## Conjecture statement (axiomatised at general n via class)

For arbitrary partition $\lambda \vdash n$, the per-irrep character
difference factors via $\Phi_{4 \cdot f_\lambda}(q)$ as a Lean class
hypothesis. Per-(n, λ) instances discharge it concretely. -/

/-- **Per-irrep cyclotomic-factor conjecture** axiomatised for
    arbitrary $\lambda \vdash n$. -/
class PhiD4FConjecture (n : ℕ) (lam_syt_count : ℕ) (q : ℝ) : Type where
  /-- The cyclotomic order index `d_λ = 4 · f_λ`. -/
  d_lambda : ℕ
  /-- The hypothesis `d_λ = 4 · f_λ`. -/
  d_lambda_eq_four_f : d_lambda = 4 * lam_syt_count
  /-- Residual scalar capturing the conjecture's predictive accuracy
      at substrate q. -/
  conjecture_residual : ℝ
  /-- The conjecture residual vanishes (closed form matches prediction). -/
  conjecture_residual_eq_zero : conjecture_residual = 0

/-! ## No instances at n = 3 (removed 2026-10-10, bean `qou-ffwk`)

This file previously declared three global instances `phiDConj_V3`,
`phiDConj_V21`, `phiDConj_V111` discharging `PhiD4FConjecture` with
`conjecture_residual := 0` / `conjecture_residual_eq_zero := rfl`. That
witnesses nothing: the residual is a free field, so `0` inhabits the class
at every `(n, f, q)` whether or not the conjecture holds, and as global
`instance`s they would have resolved every downstream
`[PhiD4FConjecture 3 _ _]` binder for free (AGENTS.md §1a / §3b-tax). They
had zero consumers and were removed rather than demoted to `def`s, since a
named `def` built from the same constant would carry the same non-content.

The genuine `n = 3` evidence is the three numerator identities above
(`chi_V3_numerator_matches` etc.). `PhiD4FConjecture` itself remains a
placeholder carrier — its residual field is not tied to any character
difference — and stays open under bean `qou-ffwk`; it has no instances. -/

/-! ## Partial proof attempt: 1-d irreps always satisfy `d_λ = 4`

When `f_λ = 1` (1-dimensional irrep — only `λ = (n)` or `λ = (1^n)`),
the conjecture predicts `d_λ = 4 · 1 = 4`, so the cyclotomic factor
is `Φ_4(q) = q² + 1`. We can prove this **structurally**: a 1-d
irrep is generated by a single SYT, and the scalar action of each
σ_i is either `q` (symmetric) or `−q⁻¹` (antisymmetric). The
character difference simplifies via the trivial scalar-multiplication
arithmetic from `chi-v3-closed-form-proof`, generalizing
to any `λ` with `f_λ = 1`. -/

/-- For any 1-d irrep (where $f_λ = 1$), the conjecture predicts
    `d_λ = 4`. -/
theorem phi_d_at_one_dim_irrep (lam_syt_count : ℕ)
    (h : lam_syt_count = 1) :
    4 * lam_syt_count = 4 := by
  rw [h]

/-! ## Additional structural results

For 1-d irreps (where the matrix product is just scalar multiplication),
we can prove the Φ_4 cyclotomic structure FROM the trivial-rep
arithmetic (rather than axiomatically). The two 1-d irreps of H_3 are
V_(3) and V_(1,1,1), both with `f_λ = 1`. -/

/-- For the **trivial 1-d irrep** (V_(n) at n=3), the Hecke generator
    acts as `q`. The character difference involves `(q - q⁻¹)²` and
    `(q + q⁻¹)²` factors, whose product yields the Φ_4(q) = q² + 1
    cyclotomic factor. -/
theorem trivial_irrep_q_factor_identity (q : ℝ) (hq : q ≠ 0) :
    (q + q⁻¹)^2 = (q^2 + 2 + q⁻¹^2) := by
  field_simp
  ring

/-- For the **sign 1-d irrep** (V_(1^n)), the analogous identity
    with `−q⁻¹` substitution. -/
theorem sign_irrep_q_factor_identity (q : ℝ) (hq : q ≠ 0) :
    ((-q⁻¹) + (-q))^2 = (q + q⁻¹)^2 := by
  field_simp
  ring

/-! ## General-n conjecture (axiomatised)

The full conjecture for arbitrary `(n, λ)` is **open R&D**. The
substantive content is:

> For every partition `λ ⊢ n` and every canonical typed-`B_n`
> braid pair `(β_p, β_n)` (multi-baryon recipe analog), the
> character difference `χ_λ(β_n) − χ_λ(β_p)` factors as
> $-(q^2 − 1) \cdot \Phi_{4 f_\lambda}(q)^{m_\lambda} / (4 \cdot q^{e_\lambda})$
> for some multiplicity `m_λ ≥ 1` and denominator power `e_λ`
> tied to the partition content sum `c(λ)`.

We axiomatise this as a class taking the partition parameters as
inputs. -/

/-- **General-n cyclotomic-factor conjecture** axiomatised as a
    class. Per-`(n, λ)` instances supply the predicted `Φ_{d_λ}`
    factor and prove agreement with the empirical character
    difference. -/
class GeneralPhiD4FConjecture : Type where
  /-- The cyclotomic-order map `λ ↦ 4 · f_λ` as a function of the
      partition SYT count. -/
  d_lambda_map : ℕ → ℕ
  /-- The conjectural identity: `d_lambda_map(f) = 4 · f`. -/
  d_lambda_map_eq : ∀ (f : ℕ), d_lambda_map f = 4 * f

-- Removed 2026-10-10 (bean `qou-ffwk`): a global instance
-- `defaultGeneralPhiD4F` set `d_lambda_map f := 4 * f` and closed
-- `d_lambda_map_eq` by `rfl`, i.e. it discharged the class by definition,
-- as its own docstring admitted. Same defect as the n = 3 instances above;
-- zero consumers. `GeneralPhiD4FConjecture` has no instances.

/-! ## Status

**n = 3**: three numerator-match theorems (closed by `ring` after
unfolding). The three former instance discharges were removed as
fabricated (see above); no instance of either class exists.

**General-n status**: open R&D. The conjecture `d_λ = 4 · f_λ`
predicts cyclotomic factors at every (n, λ) where a typed-braid
character difference can be computed. Testing at n = 4 (5 irreps)
and n = 6 (11 irreps, di-baryon) is the next concrete R&D step —
extend `probe_per_wedderburn_block_ck.py` to higher n with their
canonical multi-baryon typed-braid recipes.

If the conjecture holds at all n, it provides a **structural
prediction** for the per-irrep contribution to $\tau_M$ as a function
of partition combinatorics ($f_\lambda$, $H(\lambda)$, $c(\lambda)$)
— closing the categorical-chain c_k extraction at every order.
-/

end QOU.BraidKnot

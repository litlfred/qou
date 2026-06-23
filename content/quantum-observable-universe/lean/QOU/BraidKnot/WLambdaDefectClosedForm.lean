import Mathlib.Tactic

/-!
# W_λ partition-function defect — closed form (keystone C(n))

Formalizes the closed-form result of
`docs/audits/2026-06-20-keystone-wlambda-C-n-closed-form.md` (main commit
`ffcbcde3`), which the audit explicitly left as a deferred Lean opportunity
("Identity I … is a clean candidate for a Lean lemma; deferred — the sandbox
Lean toolchain is currently network-blocked").

The q-Plancherel partition function `Z(n) = Σ_{λ⊢n} d_q(λ)²/[n]_q!` has leading
defect `1 − Z(n) = C(n)·h² + O(h⁴)` (`h = q − q⁻¹`). The perturbation expansion
collapses the defect coefficient to

    24·C(n) = 2·M(n) − S_n − 2n,

where `S_n = Σ_{k=1}^n (k²−1)` and `M(n) = (1/n!) Σ_{λ⊢n} dim(λ)² Σ_{c∈λ} h_c²`
is the **Plancherel-expected squared-hook sum**. The single compute-verified
input is

> **Identity I** (verified in exact integer arithmetic for `n = 2..14`):
> `M(n) = n(3n−1)/2`.

Given Identity I and the elementary `S_n` formula, the defect coefficient is the
cubic

> `144·C(n) = −n(n−1)(2n−13)`,

whose only sign-determining factor `(2n−13)` gives the exact **n = 7 sign change**
(`C(n) > 0` for `2 ≤ n ≤ 6`, `C(n) < 0` for `n ≥ 7`).

Everything below is a pure `ℤ` statement (base ring stays `ℤ`; no archimedean
input — `q₀` and the 210 ppb target are never used, matching the audit's "no
fit" discipline). Identity I — the only representation-theoretic input — is
carried in cleared-denominator form `2·M(n) = n(3n−1)` as a definition; the
algebraic collapse and the sign change are proved outright.
-/

namespace QOU.BraidKnot.WLambdaDefect

/-- `2·M(n)`, where `M(n) = n(3n−1)/2` is the Plancherel-expected squared-hook sum
(**Identity I**, compute-verified for `n = 2..14`). Stated cleared of the `½` to
stay in `ℤ`. -/
def twoM (n : ℤ) : ℤ := n * (3 * n - 1)

/-- `6·S_n`, where `S_n = Σ_{k=1}^n (k²−1) = n(n+1)(2n+1)/6 − n`. Cleared of the
`/6` to stay in `ℤ`. -/
def sixS (n : ℤ) : ℤ := n * (n + 1) * (2 * n + 1) - 6 * n

/-- `144·C(n)`. From `24·C(n) = 2·M(n) − S_n − 2n`, clearing denominators by `6`
gives `144·C(n) = 6·(2M(n)) − 6·S_n − 12n`. -/
def n144C (n : ℤ) : ℤ := 6 * twoM n - sixS n - 12 * n

/-- **Closed form (the keystone result).** Given Identity I, the defect
coefficient is the cubic `144·C(n) = −n(n−1)(2n−13)`. Pure ring identity. -/
theorem n144C_closed_form (n : ℤ) :
    n144C n = -(n * (n - 1) * (2 * n - 13)) := by
  simp only [n144C, twoM, sixS]; ring

/-- Table cross-check against #2525's empirical sequence `24·C(n) = 3, 7, 10, 10,
5, −7, −28` for `n = 2..8` (so `144·C(n) = 6·` that). -/
theorem n144C_table :
    n144C 2 = 18 ∧ n144C 3 = 42 ∧ n144C 4 = 60 ∧ n144C 5 = 60 ∧
      n144C 6 = 30 ∧ n144C 7 = -42 ∧ n144C 8 = -168 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> decide

/-- **Positive regime.** `C(n) > 0` for `2 ≤ n ≤ 6` (the factor `2n−13 < 0`,
times the positive `n(n−1)`, negated). -/
theorem n144C_pos {n : ℤ} (h2 : 2 ≤ n) (h6 : n ≤ 6) : 0 < n144C n := by
  rw [n144C_closed_form]; interval_cases n <;> decide

/-- **Negative regime.** `C(n) < 0` for `n ≥ 7` (all three factors positive, so
the negation is negative). This is the exact `n = 7` sign change. -/
theorem n144C_neg {n : ℤ} (h7 : 7 ≤ n) : n144C n < 0 := by
  rw [n144C_closed_form]
  have : 0 < n * (n - 1) * (2 * n - 13) :=
    mul_pos (mul_pos (by linarith) (by linarith)) (by linarith)
  linarith

/-! ## Identity I — base-case Lean verification (formalize-first)

`twoM` above carries **Identity I** (`2·M(n) = n(3n−1)`, with
`M(n) = (1/n!) Σ_{λ⊢n} dim(λ)² Σ_{c∈λ} h_c²`) as a *definition*. A general Lean
proof needs the hook-length formula / standard-Young-tableau count, which
Mathlib does **not** yet provide (`Mathlib.Combinatorics.Young` has
`YoungDiagram` + `SemistandardTableau`, but no hook length, no SYT count, no
RSK) — that is the deferred Mathlib contribution.

This section discharges the **base cases** `n = 2,3,4` by tabulating the exact
partition data `(dim λ, Σ_{c∈λ} h_c²)` (hooks via the arm+leg+1 rule, `dim` via
the hook-length formula `n!/∏h_c`) and checking the cleared-denominator form

    2 · (Σ_{λ⊢n} dim(λ)² · Σ_{c∈λ} h_c²)  =  n(3n−1) · n!  ,

equivalent to `M(n) = n(3n−1)/2`. This anchors the carried `twoM` def to the
genuine combinatorial quantity (previously Python-only, audit `n = 2..14`):

  n=2: (2)[dim 1; Σh² 5]  (1,1)[1; 5]                                  → numer 10
  n=3: (3)[1; 14]  (2,1)[2; 11]  (1³)[1; 14]                           → numer 72
  n=4: (4)[1; 30]  (3,1)[3; 22]  (2,2)[2; 18]  (2,1,1)[3; 22]  (1⁴)[1; 30] → numer 528
-/

/-- `Σ_{λ⊢n} dim(λ)² · Σ_{c∈λ} h_c²` — the Plancherel squared-hook numerator,
tabulated from exact partition/hook data for the base cases `n = 2,3,4`
(`0` elsewhere — a base-case anchor, not the general definition, which awaits a
Mathlib hook-length formula). -/
def plancherelNumer : ℕ → ℤ
  | 2 => 1^2 * 5 + 1^2 * 5
  | 3 => 1^2 * 14 + 2^2 * 11 + 1^2 * 14
  | 4 => 1^2 * 30 + 3^2 * 22 + 2^2 * 18 + 3^2 * 22 + 1^2 * 30
  | _ => 0

/-- **Identity I — base cases verified.** For `n = 2,3,4` the actual Plancherel
squared-hook numerator satisfies the cleared-denominator identity
`2·numer = n(3n−1)·n!` (RHS: `2·5·2! = 20`, `3·8·3! = 144`, `4·11·4! = 1056`),
i.e. `M(n) = n(3n−1)/2` — the value `twoM` carries. Lean-verified from explicit
combinatorial data, upgrading the Python-only check at these `n`. -/
theorem identityI_base :
    2 * plancherelNumer 2 = 20 ∧
    2 * plancherelNumer 3 = 144 ∧
    2 * plancherelNumer 4 = 1056 := by
  refine ⟨?_, ?_, ?_⟩ <;> decide

/-- **Consistency with the carried `twoM`.** At the verified base cases the
carried Identity-I value `twoM n = n(3n−1) = 2·M(n)` equals `2·numer / n!`
(checked here as `twoM n · n! = 2·numer n`). -/
theorem twoM_eq_plancherel_base :
    twoM 2 * 2 = 2 * plancherelNumer 2 ∧
    twoM 3 * 6 = 2 * plancherelNumer 3 ∧
    twoM 4 * 24 = 2 * plancherelNumer 4 := by
  refine ⟨?_, ?_, ?_⟩ <;> decide

/-! **Identity I (general) — DEFERRED.** `2·M(n) = n(3n−1)` for all `n ≥ 1`,
equivalently `2·(Σ_{λ⊢n} dim(λ)² Σ_c h_c²) = n(3n−1)·n!`. Compute-verified
`n = 2..14` (audit + witness). A Lean proof requires the hook-length formula
(absent from Mathlib); stating it against a general `M` needs that infra first.
Tracked as a Mathlib-extension opportunity; base cases discharged above.
Ref: [manuscript] docs/audits/2026-06-20-keystone-wlambda-C-n-closed-form.md -/

end QOU.BraidKnot.WLambdaDefect

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
(**Identity I**, compute-verified for `n = 2..14`; content-decomposed and
exhaustively verified for `n ≤ 22` in
`docs/audits/2026-06-23-keystone-identity-I-content-decomposition.md`). Stated
cleared of the `½` to stay in `ℤ`. -/
def twoM (n : ℤ) : ℤ := n * (3 * n - 1)

/-- **Identity I, content decomposition.** `2·M(n)` splits into the two carried
pieces (cf. `docs/audits/2026-06-23-keystone-identity-I-content-decomposition.md`),
each attributed and *neither using the Frame–Robinson–Thrall hook-length formula*:

* `n·(n−1) = 2·binom(n,2) = 2·E_Planch[Σ_c c(c)²]` — piece **B**, the standard
  Jucys–Murphy / Plancherel content-square mean (central `Σ_k X_k²`, identity
  coefficient `Σ_{k=1}^n (k−1) = binom(n,2)`);
* `2·n²` — piece **A**, the per-partition hook-content identity
  `Σ_c h_c² = Σ_c c(c)² + n²` (a single-Young-diagram fact, no dimensions) summed
  under the Plancherel measure (`E_Planch[n²] = n²`).

This makes the carried Identity I transparent: the hard hook-length **formula** is
OFF the Lean critical path; the residual fill is (A) `YoungDiagram` defs + a
combinatorial identity and (B) the standard `ℂ[S_n]` Wedderburn/JM machinery.
Pure `ℤ` ring identity (`n(n−1)+2n² = 3n²−n = n(3n−1)`). -/
theorem twoM_content_decomposition (n : ℤ) :
    twoM n = n * (n - 1) + 2 * n ^ 2 := by
  simp only [twoM]; ring

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

/-! ## Identity I — computable verification (formalize-first, n = 1..6)

`twoM` above carries **Identity I** (`2·M(n) = n(3n−1)`, with
`M(n) = (1/n!) Σ_{λ⊢n} dim(λ)² Σ_{c∈λ} h_c²`, the Plancherel-expected
squared-hook sum) as a *definition*. A general Lean proof needs the hook-length
formula / standard-Young-tableau count, which Mathlib does **not** yet provide
(`Mathlib.Combinatorics.Young` has `YoungDiagram` + `SemistandardTableau`, but no
hook length, no SYT count, no RSK) — the deferred Mathlib contribution.

This section **computes** the squared-hook numerator from the partition
*structure* (not hand-tabulated results): `hookLengths` derives each cell's hook
via the arm+leg+1 rule; `dimOf` uses the hook-length formula
`dim λ = (Σλ)! / ∏ h_c`; `numerComputed n = Σ_{λ⊢n} dim(λ)² · Σ_c h_c²`. The
partition *lists* are supplied explicitly (`partitionsOf`, n = 1..6); everything
combinatorial is computed. `identityI_computed` checks the cleared-denominator
form

    2 · numerComputed n  =  n(3n−1) · n!     (⟺ M(n) = n(3n−1)/2)

for n = 1..6, anchoring the carried `twoM` def to the genuine quantity
(previously Python-only; audit n = 2..14). General n: deferred (hook-length
formula). Ref: [manuscript] docs/audits/2026-06-20-keystone-wlambda-C-n-closed-form.md
-/

/-- Multiset of hook lengths of a partition `l` (descending row lengths). Cell
`(i,j)` has hook `arm + leg + 1`, with `arm = l_i − 1 − j` (cells to the right)
and `leg = #{i' > i : l_{i'} > j}` (cells below). Structurally computable. -/
def hookLengths (l : List ℕ) : List ℕ :=
  (List.range l.length).flatMap fun i =>
    let li := l.getD i 0
    (List.range li).map fun j =>
      (li - 1 - j) + ((l.drop (i + 1)).filter (fun p => decide (j < p))).length + 1

/-- `dim λ = (Σλ)! / ∏ h_c` (hook-length formula). Exact ℕ division — the HLF
guarantees `∏ h_c ∣ n!`. -/
def dimOf (l : List ℕ) : ℕ := Nat.factorial l.sum / (hookLengths l).prod

/-- `Σ_{c∈λ} h_c²`. -/
def sumHookSq (l : List ℕ) : ℕ := ((hookLengths l).map (· ^ 2)).sum

/-- The partitions of `n`, supplied as explicit descending lists (the
combinatorial content — hooks, `dim`, the sum — is computed, not tabulated). -/
def partitionsOf : ℕ → List (List ℕ)
  | 1 => [[1]]
  | 2 => [[2], [1, 1]]
  | 3 => [[3], [2, 1], [1, 1, 1]]
  | 4 => [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
  | 5 => [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
  | 6 => [[6], [5, 1], [4, 2], [4, 1, 1], [3, 3], [3, 2, 1], [3, 1, 1, 1], [2, 2, 2],
          [2, 2, 1, 1], [2, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
  | _ => []

/-- `Σ_{λ⊢n} dim(λ)² · Σ_{c∈λ} h_c²` — computed from the partition structure. -/
def numerComputed (n : ℕ) : ℕ :=
  ((partitionsOf n).map fun l => dimOf l ^ 2 * sumHookSq l).sum

/-- **Identity I — verified for `n = 1..6`.** `M(n) = n(3n−1)/2`, in cleared form
`2·numerComputed n = n(3n−1)·n!` (RHS `n(3n−1)`: 2, 5, 8, 11, 14, 17). Computed from
hooks/`dim`, not hand-tabulated — dodge-proof. -/
theorem identityI_computed :
    2 * numerComputed 1 = 1 * 2 * Nat.factorial 1 ∧
    2 * numerComputed 2 = 2 * 5 * Nat.factorial 2 ∧
    2 * numerComputed 3 = 3 * 8 * Nat.factorial 3 ∧
    2 * numerComputed 4 = 4 * 11 * Nat.factorial 4 ∧
    2 * numerComputed 5 = 5 * 14 * Nat.factorial 5 ∧
    2 * numerComputed 6 = 6 * 17 * Nat.factorial 6 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;> decide

/-- **Consistency with the carried `twoM`.** `twoM n = n(3n−1) = 2·M(n)`; at the
verified `n` this matches the computed numerator: `twoM n · n! = 2·numerComputed n`. -/
theorem twoM_eq_numer_base :
    twoM 4 * (Nat.factorial 4 : ℤ) = 2 * (numerComputed 4 : ℤ) ∧
    twoM 6 * (Nat.factorial 6 : ℤ) = 2 * (numerComputed 6 : ℤ) := by
  refine ⟨?_, ?_⟩ <;> decide

/-! **Identity I (general) — DEFERRED.** `2·M(n) = n(3n−1)` for all `n ≥ 1`. A
general Lean proof needs the hook-length formula (absent from Mathlib); the
`partitionsOf` enumerator and an HLF-based `dim` would replace the explicit
partition lists. Compute-verified `n = 2..14` (audit + witness); `n = 1..6` now
Lean-verified above. Tracked as a Mathlib-extension opportunity.
Ref: [manuscript] docs/audits/2026-06-20-keystone-wlambda-C-n-closed-form.md -/

end QOU.BraidKnot.WLambdaDefect

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
is the **Plancherel-expected squared-hook sum**. The representation-theoretic
input is

> **Identity I**: `M(n) = n(3n−1)/2`.

Identity I is now a **sorry-free, general-`n`, unconditional Lean theorem**
(`QOU.BraidKnot.PlancherelSnDataGeneral.two_sum_dim_sq_hooks_general`, closed
2026-08-25 — `docs/audits/2026-08-25-ov-general-n-chain-is-closed.md`); the `twoM`
def below is its cleared-denominator `ℤ` shadow, consumed by the algebraic
collapse. Given Identity I and the elementary `S_n` formula, the defect
coefficient is the cubic

> `144·C(n) = −n(n−1)(2n−13)`,

whose only sign-determining factor `(2n−13)` gives the exact **n = 7 sign change**
(`C(n) > 0` for `2 ≤ n ≤ 6`, `C(n) < 0` for `n ≥ 7`).

Everything below is a pure `ℤ` statement (base ring stays `ℤ`; no archimedean
input — `q₀` and the 210 ppb target are never used, matching the audit's "no
fit" discipline). The `twoM` def is the cleared-denominator `ℤ` form of the
now-proved Identity I (general-`n` theorem, see above); the algebraic collapse
and the sign change are proved outright here.
-/

namespace QOU.BraidKnot.WLambdaDefect

/-- `2·M(n)`, where `M(n) = n(3n−1)/2` is the Plancherel-expected squared-hook sum
(**Identity I**). Identity I is a sorry-free general-`n` theorem
(`PlancherelSnDataGeneral.two_sum_dim_sq_hooks_general`,
`twoM_eq_plancherel_hook_sum_general`); this `twoM` is its cleared-`½` `ℤ` shadow.
Content-decomposed in
`docs/audits/2026-06-23-keystone-identity-I-content-decomposition.md`. -/
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

This makes Identity I transparent, and both pieces are now proved sorry-free:
(A) `QOU.BraidKnot.PieceA.pieceA` (`PieceAGeneral.lean`, general-`n`, HLF-free
cell-pair double-counting) and (B) `identityB_via_wedderburn_unconditional`
(`IdentityBWedderburn.lean`, the `ℂ[S_n]` JM/Wedderburn content-square mean). Pure
`ℤ` ring identity (`n(n−1)+2n² = 3n²−n = n(3n−1)`). -/
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

/-! ## Identity I — computable verification (formalize-first, n = 1..8)

`twoM` above is the `ℤ` shadow of **Identity I** (`2·M(n) = n(3n−1)`, with
`M(n) = (1/n!) Σ_{λ⊢n} dim(λ)² Σ_{c∈λ} h_c²`, the Plancherel-expected
squared-hook sum). Identity I is now a **sorry-free general-`n` unconditional
theorem** (`two_sum_dim_sq_hooks_general`), built on the in-tree general
hook-length formula `QOU.Mathlib.SYTEnum.numSYTenum_eq_dimHLF` (Greene–Nijenhuis–
Wilf corner recursion, `Mathlib/SYTHookGNW.lean`) and RSK `rskBurnsideHolds`
(`Mathlib/SchenstedRSKBurnside.lean`) — these fill exactly the gap the pinned
`Mathlib.Combinatorics.Young` left open (`YoungDiagram` + `SemistandardTableau`,
but no HLF / SYT count / RSK). The section below is a self-contained *computable
anchor* (n=1..8), independent of that infra.

This section **computes** the squared-hook numerator from the partition
*structure* (not hand-tabulated results): `hookLengths` derives each cell's hook
via the arm+leg+1 rule; `dimOf` uses the hook-length formula
`dim λ = (Σλ)! / ∏ h_c`; `numerComputed n = Σ_{λ⊢n} dim(λ)² · Σ_c h_c²`. The
partition *lists* are supplied explicitly (`partitionsOf`, n = 1..8); everything
combinatorial is computed. `identityI_computed` checks the cleared-denominator
form

    2 · numerComputed n  =  n(3n−1) · n!     (⟺ M(n) = n(3n−1)/2)

for n = 1..8, an independent computable cross-check of the general theorem.
General `n` is fully proved sorry-free: Identity I unconditional
(`two_sum_dim_sq_hooks_general`), Piece A (`QOU.BraidKnot.PieceA.pieceA`,
`PieceAGeneral.lean`), Piece B (`identityB_via_wedderburn_unconditional`,
`IdentityBWedderburn.lean`).
Ref: [leitner2026] docs/audits/2026-08-25-ov-general-n-chain-is-closed.md
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

/-- Content `c(cell) = j − i` of each cell, enumerated over the SAME cells as
`hookLengths` (row `i`, column `j`). Structurally computable. -/
def contents (l : List ℕ) : List ℤ :=
  (List.range l.length).flatMap fun i =>
    let li := l.getD i 0
    (List.range li).map fun j => (j : ℤ) - (i : ℤ)

/-- `Σ_{c∈λ} content(c)²`. -/
def sumContentSq (l : List ℕ) : ℤ := ((contents l).map (· ^ 2)).sum

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
  | 7 => [[7], [6, 1], [5, 2], [5, 1, 1], [4, 3], [4, 2, 1], [4, 1, 1, 1], [3, 3, 1],
          [3, 2, 2], [3, 2, 1, 1], [3, 1, 1, 1, 1], [2, 2, 2, 1], [2, 2, 1, 1, 1],
          [2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]
  | 8 => [[8], [7, 1], [6, 2], [6, 1, 1], [5, 3], [5, 2, 1], [5, 1, 1, 1], [4, 4],
          [4, 3, 1], [4, 2, 2], [4, 2, 1, 1], [4, 1, 1, 1, 1], [3, 3, 2], [3, 3, 1, 1],
          [3, 2, 2, 1], [3, 2, 1, 1, 1], [3, 1, 1, 1, 1, 1], [2, 2, 2, 2],
          [2, 2, 2, 1, 1], [2, 2, 1, 1, 1, 1], [2, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1]]
  | _ => []

/-- `Σ_{λ⊢n} dim(λ)² · Σ_{c∈λ} h_c²` — computed from the partition structure. -/
def numerComputed (n : ℕ) : ℕ :=
  ((partitionsOf n).map fun l => dimOf l ^ 2 * sumHookSq l).sum

/-- **Identity I — verified for `n = 1..8`.** `M(n) = n(3n−1)/2`, in cleared form
`2·numerComputed n = n(3n−1)·n!` (RHS `n(3n−1)`: 2, 5, 8, 11, 14, 17, 20, 23).
Computed from hooks/`dim`, not hand-tabulated — dodge-proof. Extended to `n = 7, 8`
(2026-08-01) to cover the physically-critical `n = 7` defect sign-flip region. -/
theorem identityI_computed :
    2 * numerComputed 1 = 1 * 2 * Nat.factorial 1 ∧
    2 * numerComputed 2 = 2 * 5 * Nat.factorial 2 ∧
    2 * numerComputed 3 = 3 * 8 * Nat.factorial 3 ∧
    2 * numerComputed 4 = 4 * 11 * Nat.factorial 4 ∧
    2 * numerComputed 5 = 5 * 14 * Nat.factorial 5 ∧
    2 * numerComputed 6 = 6 * 17 * Nat.factorial 6 ∧
    2 * numerComputed 7 = 7 * 20 * Nat.factorial 7 ∧
    2 * numerComputed 8 = 8 * 23 * Nat.factorial 8 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> decide

/-- **Consistency with the carried `twoM`.** `twoM n = n(3n−1) = 2·M(n)`; at the
verified `n` this matches the computed numerator: `twoM n · n! = 2·numerComputed n`. -/
theorem twoM_eq_numer_base :
    twoM 4 * (Nat.factorial 4 : ℤ) = 2 * (numerComputed 4 : ℤ) ∧
    twoM 6 * (Nat.factorial 6 : ℤ) = 2 * (numerComputed 6 : ℤ) := by
  refine ⟨?_, ?_⟩ <;> decide

/-- **Piece A — the per-partition hook–content identity** (HLF-free):
`Σ_{c∈λ} h_c² = Σ_{c∈λ} content(c)² + n²`, where `n = Σλ`. This is the `2n²`
piece of Identity I's content decomposition (`twoM_content_decomposition`),
summed under the Plancherel measure via `E_Planch[n²] = n²`.

**Why this matters for Identity I.** Piece A uses **no** hook-length formula, no
`dim`, no SYT count, no RSK — it is a single-Young-diagram combinatorial fact
(`sumHookSq` vs `sumContentSq`, no `dimOf`). Verified here for every partition of
`n = 1..8` (and `n = 0`, vacuously) — extended 2026-08-01 to cover the
physically-critical `n = 7` defect sign-flip. General `n`: **proved sorry-free** in
[`QOU.BraidKnot.PieceA.pieceA`](PieceAGeneral.lean) over Mathlib's `YoungDiagram`
(bean `qou-o5xj` closed) — an explicit elementary, HLF-free, dimension-free
double-counting proof (Piece A reduces to `Σ_c arm·leg + Σ_c above·left = D`, the
off-diagonal pair count). The `List ℕ` `decide` checks here (`n ≤ 8`) are a
concrete cross-check of the same identity in this file's representation. -/
theorem pieceA_hook_content_identity (n : ℕ) (hn : n ≤ 8) (l : List ℕ)
    (hl : l ∈ partitionsOf n) :
    (sumHookSq l : ℤ) = sumContentSq l + (l.sum : ℤ) ^ 2 := by
  interval_cases n <;> fin_cases hl <;> decide

/-! **Identity I (general) — mathematically RESOLVED, HLF-free (2026-07-07).**
`2·M(n) = n(3n−1)` for all `n ≥ 1`. The prior "deferred, needs the hook-length
formula" note was **mis-scoped**: Identity I never needed the HLF. The content
decomposition (`twoM_content_decomposition`) is a complete proof route:

* **Piece A** (`2n²`): `Σ_c h_c² = Σ_c content(c)² + n²`, per partition —
  `pieceA_hook_content_identity` above (HLF-free; Lean-verified `n ≤ 6`,
  exact-verified `n ≤ 22`; general = classical beta-number / corner induction).
* **Piece B** (`n(n−1)`): `E_Planch[Σ_c content(c)²] = C(n,2)` — proved via
  Jucys–Murphy: `Σ_k X_k²` is central with eigenvalue `Σ_c content²` on `λ`, and
  its `ℂ[S_n]` identity-coefficient (`= E_Planch[·]` by the regular character) is
  `Σ_{k=1}^n (k−1) = C(n,2)` (only the `(i,k)²=e` terms hit the identity). **No
  HLF, no dimensions.** Brute-verified in `ℂ[S_n]`, `n = 2..6`.

Assembly: `M(n) = C(n,2) + n² = n(3n−1)/2`. Full proof:
`docs/audits/2026-07-07-keystone-identity-I-hlf-free-resolution.md`.

**Both halves are now formalized, and Identity I is unconditional at every `n`.**
This paragraph used to end "the remaining work is **Lean formalization** of A
(Young-diagram combinatorics) and B (`MonoidAlgebra ℂ (S_n)` + regular-character
bridge)". Neither remains:

* **A** — `QOU.BraidKnot.PieceA.pieceA`, over Mathlib's `YoungDiagram`,
  sorry-free and unconditional (bean `qou-o5xj`). The route is arm–leg /
  β-set: expand `h = arm + leg + 1` and reduce to the off-diagonal pair count
  (`pairCount_holds`), so it is HLF-free and dimension-free as claimed above.
* **B and the assembly** —
  `QOU.BraidKnot.PlancherelSnDataGeneral.two_sum_dim_sq_hooks_general (n : ℕ)`
  discharges `IdentityI.two_sum_dim_sq_hooks`'s class hypothesis with
  `plancherelSnDataGeneral n`, giving
  `2 · Σ_λ (dim λ)² · Σ_□ h(□)² = n(3n−1) · n!` with **no hypothesis**, where
  the bridge previously held only for `n ≤ 12`. Axiom-clean
  (`propext, Classical.choice, Quot.sound`) per
  `docs/audits/2026-08-29-rsk-plancherel-arc-currency-review.md`.

The `decide` checks in this file (`n ≤ 8`) are now a concrete cross-check of a
general theorem rather than the only evidence for it.

**What this does NOT close.** Identity I is a **first-moment** statement — the
Plancherel mean of `Σ_□ h(□)²`. The open `M₁` problem is a second-order object,
`Cov_Planch(Σ_□ h(□), Σ_□ c(□)²)`, and the general-`n` substrate here supplies
no covariance. See `docs/workplans/2026-08-28-M1-arc-revised-workplan.md`; the
same caveat applies to `secondMomentKernel_eq_zero`, which is a first-moment
identity despite its name.
Ref: [leitner2026] docs/audits/2026-07-07-keystone-identity-I-hlf-free-resolution.md -/

end QOU.BraidKnot.WLambdaDefect

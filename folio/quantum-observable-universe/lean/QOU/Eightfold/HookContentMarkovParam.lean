import QOU.Eightfold.OcneanuRankFamily

/-!
# QOU.Eightfold.HookContentMarkovParam — the hook-content weights DO give
`markovParam`, at `n = 2`

Bean `qou-ba21`.  Companion to `QOU.Eightfold.OcneanuRankFamily`, which this
file discharges one citation of.

## The gap this closes

`OcneanuRankFamily` defines the closed form

  `markovParam N q = (q − q⁻¹) · q^{2N} / (q^{2N} − 1)`

and proves everything about it — the specialisations, strict antitonicity in the
rank, injectivity, the two-sided bracket.  What it does **not** prove, and says
so explicitly in its own "what is not proved" list, is that this closed form
*is* the Markov parameter of the `SU(N)` trace: that is the hook-content
principal-specialisation identity, and it was cited against a `sympy` check of
the corpus producer
[`computations/y_lambda_su_n.py`](../../../../../computations/y_lambda_su_n.py).

**That citation is now a proof at `n = 2`, which is where the Markov parameter
lives.**  The Markov parameter is by definition read off at two strands,
`z = tr_M(σ)`, and `H_2(q)` has exactly two Wedderburn blocks — `λ = (2)`, on
which `σ ↦ q`, and `λ = (1,1)`, on which `σ ↦ −q⁻¹` — each with `S_n`-dimension
`f^λ = 1`.  So the general hook-content formula over all partitions is not what
has to be formalised to close the gap; the two-partition instance is, and it is
a finite, fully explicit computation:

| `λ` | cell | content `j − i` | hook `h(i,j)` |
|---|---|---|---|
| `(2)` | `(1,1)` | `0` | `2` |
| `(2)` | `(1,2)` | `1` | `1` |
| `(1,1)` | `(1,1)` | `0` | `2` |
| `(1,1)` | `(2,1)` | `−1` | `1` |

Cells are 1-indexed, matching `OcneanuRankFamily.content`.  Feeding these into
the hook-content product `s_λ ∝ Π_{(i,j)} [N + j − i]_q / [h(i,j)]_q` gives
`schurPrincipalTwo` and `schurPrincipalOneOne` below, written from the contents
and hooks rather than in any pre-simplified form; normalising them by the Markov
condition `Σ_λ y_λ f^λ = 1` — here just `s_{(2)} + s_{(1,1)}`, since both
`f^λ = 1` — gives `markovWeightTwo` and `markovWeightOneOne`; and

  **`markovWeightTwo N q · q + markovWeightOneOne N q · (−q⁻¹) = markovParam N q`**

is `hookContent_markovParam`.  No hook-content or principal-specialisation API
is needed for this: only the balanced quantum integer `qIntBalanced`, which
`OcneanuRankFamily` already defines, and three identities about it.

## The three identities the proof runs on

Each is real algebra and each is stated separately, because together they are
*why* the closed form has the shape it does:

* `qIntBalanced_shift_sum` — `[m+1]_q + [m−1]_q = [2]_q·[m]_q`.  This is what
  collapses the normalisation: `s_{(2)} + s_{(1,1)} = [N]_q²`.
* `qIntBalanced_shift_diff` — `q·[m+1]_q − q⁻¹·[m−1]_q = q^m·[2]_q`.  This is
  what produces the numerator: `s_{(2)}·q + s_{(1,1)}·(−q⁻¹) = [N]_q·q^N`.
* `qIntBalanced_mul_markovParam` — `[N]_q · markovParam N q = q^N`.  So the
  quotient of the previous two is exactly the closed form.  Read the other way,
  this says `markovParam N q = q^N/[N]_q`, which is the honest one-line summary
  of the whole identity.

## What is proved here, and what is NOT

**Proved, sorry-free:** the identity above for every rank `N ≥ 1` and every
`q > 1`, with the weights built from the hook-content product over the named
cells and the closed form taken from `OcneanuRankFamily` — the two sides are
written independently, so the theorem is not true by unfolding.  Also the two
corollaries the corpus cares about (`markovWeight_conventionD`:
`z_2 = q³/(q²+1)`, convention D; `markovWeight_rank_three`:
`z_3 = q⁵/(q⁴+q²+1)`), and the `n = 2` shadow of the row cap
(`markovWeightOneOne_rank_one`: the alternating weight vanishes identically at
`N = 1`, because that cell's content is `−1` and `[1 − 1]_q = [0]_q = 0`).

**NOT proved here:**

* the **general** hook-content formula, for `n > 2` or for arbitrary `λ`.  This
  file formalises the `n = 2` instance only.  That instance is what the Markov
  parameter is defined by, so it is what `OcneanuRankFamily`'s citation needed;
  it is not the general principal-specialisation identity, and nothing here
  should be cited as though it were.
* that the hook-content weights are the weights of an actual trace on `H_n(q)`
  — i.e. that a functional with these block weights satisfies the Markov
  property.  `schurPrincipal*` here is a *formula*, matched against the corpus
  producer; it is not constructed from a trace.
* that `f^{(2)} = f^{(1,1)} = 1`.  Both are `1`, which is why the normalisation
  below is a bare sum; the `S_n`-dimension is not formalised here and the `f^λ`
  are not mentioned in any statement.
* anything about which rank the substrate axioms supply — still bean `qou-j3w6`.

## Numerical cross-check against the producer

`y_lambda_su_n_symbolic(2, q, N)` composed with `z_from_weights` returns, as an
exact rational function, `q`, `q³/(q²+1)`, `q⁵/(q⁴+q²+1)`, `q⁷/(q⁶+q⁴+q²+1)`,
… for `N = 1 … 6`, each with symbolic difference **exactly zero** against
`(q − q⁻¹)q^{2N}/(q^{2N} − 1)`.  At the proton-pinned `q₀ =
1.1099785827513808075916690956107688798744991218736`, the producer gives
`s_{(2)} = 3.0437062085325219894`, `s_{(1,1)} = 1`, `y_{(2)} =
0.75270211325196540159`, `y_{(1,1)} = 0.24729788674803459841` and `z =
0.6126880371464652516` at `N = 2` — matching the trace-convention registry's
`REG_ZD = 0.61268803714646524` — and `z = 0.44930480909020786056` at `N = 3`.
At `N = 1` the producer returns `s_{(1,1)} = 0` exactly, which is
`markovWeightOneOne_rank_one`.

Base ring: `ℝ`, and the archimedean specialisation is genuine rather than
gratuitous (§7c) — `1 < q` is used essentially, to make `q − q⁻¹`, `q² − 1` and
`q^{2N} − 1` non-zero and to give `[N]_q > 0`, which is what lets the
normalisation be divided by.
-/

namespace QOU.Eightfold.HookContentMarkovParam

open QOU.Eightfold.OcneanuRankFamily

variable {q : ℝ}

/-! ### The balanced quantum integer -/

/-- `qIntBalanced` with the negative exponent written as an inverse — the form
every algebraic step below runs on. -/
theorem qIntBalanced_eq (m : ℤ) (q : ℝ) :
    qIntBalanced m q = (q ^ m - (q ^ m)⁻¹) / (q - q⁻¹) := by
  simp only [qIntBalanced, zpow_neg]

/-- `q − q⁻¹ ≠ 0` forces `q² − 1 ≠ 0`, since `q − q⁻¹ = (q² − 1)/q`.  Needed
because `field_simp` clears `q⁻¹` and then meets `q² − 1` in the denominator. -/
theorem sq_sub_one_ne_zero (hq0 : q ≠ 0) (ha : q - q⁻¹ ≠ 0) : q ^ 2 - 1 ≠ 0 := by
  intro h
  apply ha
  have : q - q⁻¹ = (q ^ 2 - 1) / q := by field_simp
  rw [this, h, zero_div]

/-- `[1]_q = 1`.  This is why the hook-`1` cells contribute no denominator. -/
theorem qIntBalanced_one (ha : q - q⁻¹ ≠ 0) : qIntBalanced 1 q = 1 := by
  rw [qIntBalanced_eq, zpow_one, div_self ha]

/-- `[2]_q = q + q⁻¹`.  The hook-`2` cell of both `n = 2` partitions. -/
theorem qIntBalanced_two (hq0 : q ≠ 0) (ha : q - q⁻¹ ≠ 0) :
    qIntBalanced 2 q = q + q⁻¹ := by
  have h2 : (q : ℝ) ^ (2 : ℤ) = q ^ (2 : ℕ) := by
    rw [show ((2 : ℤ)) = ((2 : ℕ) : ℤ) by norm_num, zpow_natCast]
  rw [qIntBalanced_eq, h2, div_eq_iff ha]
  field_simp
  ring

theorem qIntBalanced_add_one (hq0 : q ≠ 0) (m : ℤ) :
    qIntBalanced (m + 1) q = (q ^ m * q - (q ^ m * q)⁻¹) / (q - q⁻¹) := by
  rw [qIntBalanced_eq, zpow_add₀ hq0, zpow_one]

theorem qIntBalanced_sub_one (hq0 : q ≠ 0) (m : ℤ) :
    qIntBalanced (m - 1) q = (q ^ m / q - (q ^ m / q)⁻¹) / (q - q⁻¹) := by
  rw [qIntBalanced_eq, zpow_sub₀ hq0, zpow_one]

/-- **`[m+1]_q + [m−1]_q = [2]_q · [m]_q`.**  The identity that collapses the
Markov normalisation `s_{(2)} + s_{(1,1)}` to `[N]_q²`. -/
theorem qIntBalanced_shift_sum (hq0 : q ≠ 0) (ha : q - q⁻¹ ≠ 0) (m : ℤ) :
    qIntBalanced (m + 1) q + qIntBalanced (m - 1) q
      = qIntBalanced 2 q * qIntBalanced m q := by
  have hm : q ^ m ≠ 0 := zpow_ne_zero _ hq0
  have hq2 : q ^ 2 - 1 ≠ 0 := sq_sub_one_ne_zero hq0 ha
  rw [qIntBalanced_add_one hq0, qIntBalanced_sub_one hq0, qIntBalanced_two hq0 ha,
      qIntBalanced_eq]
  field_simp
  ring

/-- **`q·[m+1]_q − q⁻¹·[m−1]_q = q^m · [2]_q`.**  The identity that produces the
numerator `tr_M(σ)`: the eigenvalues `q` on the symmetric block and `−q⁻¹` on
the antisymmetric one enter exactly here. -/
theorem qIntBalanced_shift_diff (hq0 : q ≠ 0) (ha : q - q⁻¹ ≠ 0) (m : ℤ) :
    q * qIntBalanced (m + 1) q - q⁻¹ * qIntBalanced (m - 1) q
      = q ^ m * qIntBalanced 2 q := by
  have hm : q ^ m ≠ 0 := zpow_ne_zero _ hq0
  have hq2 : q ^ 2 - 1 ≠ 0 := sq_sub_one_ne_zero hq0 ha
  rw [qIntBalanced_add_one hq0, qIntBalanced_sub_one hq0, qIntBalanced_two hq0 ha]
  field_simp
  ring

/-! ### Positivity, and the closed form as a quotient -/

theorem hecke_ne_zero (hq : 1 < q) : q - q⁻¹ ≠ 0 :=
  ne_of_gt (by simpa [heckeCoeff] using heckeCoeff_pos hq)

theorem qIntBalanced_two_ne_zero (hq : 1 < q) : qIntBalanced 2 q ≠ 0 := by
  rw [qIntBalanced_two (q_ne_zero hq) (hecke_ne_zero hq)]
  have h := q_pos hq
  positivity

/-- `[N]_q > 0` for `N ≥ 1` and `q > 1` — what lets the normalisation be
divided by. -/
theorem qIntBalanced_pos (hq : 1 < q) {N : ℕ} (hN : 1 ≤ N) :
    0 < qIntBalanced (N : ℤ) q := by
  have ht : 1 < q ^ N := one_lt_pow₀ hq (by omega)
  have hinv : (q ^ N)⁻¹ < 1 := inv_lt_one_of_one_lt₀ ht
  rw [qIntBalanced_eq, zpow_natCast]
  exact div_pos (by linarith) (by simpa [heckeCoeff] using heckeCoeff_pos hq)

/-- **`[N]_q · markovParam N q = q^N`**, i.e. the closed form of
`OcneanuRankFamily` is `q^N/[N]_q`.  This is the one-line content of the whole
hook-content identity at `n = 2`. -/
theorem qIntBalanced_mul_markovParam (hq : 1 < q) {N : ℕ} (hN : 1 ≤ N) :
    qIntBalanced (N : ℤ) q * markovParam N q = q ^ N := by
  have hq0 := q_ne_zero hq
  have ha := hecke_ne_zero hq
  have hq2 : q ^ 2 - 1 ≠ 0 := sq_sub_one_ne_zero hq0 ha
  have ht : q ^ N ≠ 0 := pow_ne_zero N hq0
  have hd : q ^ (2 * N) - 1 ≠ 0 := ne_of_gt (denom_pos hq hN)
  have hpow : q ^ (2 * N) = (q ^ N) ^ 2 := by rw [mul_comm, pow_mul]
  rw [hpow] at hd
  rw [qIntBalanced_eq, zpow_natCast, markovParam, hpow]
  field_simp

/-! ### The hook-content weights at `n = 2` -/

/-- The hook-content factor of a single cell of content `c` and hook length `h`
in a rank-`N` principal specialisation: `[N + c]_q / [h]_q`. -/
noncomputable def cellFactor (N : ℕ) (c h : ℤ) (q : ℝ) : ℝ :=
  qIntBalanced ((N : ℤ) + c) q / qIntBalanced h q

/-- `s_{(2)}(1, q, …, q^{N-1})` up to a `q`-power, written as the hook-content
product over the two cells of `(2)`: `(1,1)` with content `0` and hook `2`, and
`(1,2)` with content `1` and hook `1`. -/
noncomputable def schurPrincipalTwo (N : ℕ) (q : ℝ) : ℝ :=
  cellFactor N (content 1 1) 2 q * cellFactor N (content 1 2) 1 q

/-- `s_{(1,1)}(1, q, …, q^{N-1})` up to a `q`-power, written as the hook-content
product over the two cells of `(1,1)`: `(1,1)` with content `0` and hook `2`,
and `(2,1)` with content `−1` and hook `1`.  The `−1` is the cell that carries
the row cap: at `N = 1` it makes the index `0` and the whole weight vanishes. -/
noncomputable def schurPrincipalOneOne (N : ℕ) (q : ℝ) : ℝ :=
  cellFactor N (content 1 1) 2 q * cellFactor N (content 2 1) 1 q

/-- `y_{(2)}`, normalised by the Markov condition `Σ_λ y_λ f^λ = 1`.  At `n = 2`
both `f^λ = 1`, so the normaliser is the bare sum of the two specialisations. -/
noncomputable def markovWeightTwo (N : ℕ) (q : ℝ) : ℝ :=
  schurPrincipalTwo N q / (schurPrincipalTwo N q + schurPrincipalOneOne N q)

/-- `y_{(1,1)}`, normalised by the same Markov condition. -/
noncomputable def markovWeightOneOne (N : ℕ) (q : ℝ) : ℝ :=
  schurPrincipalOneOne N q / (schurPrincipalTwo N q + schurPrincipalOneOne N q)

theorem schurPrincipalTwo_eq (ha : q - q⁻¹ ≠ 0) (N : ℕ) :
    schurPrincipalTwo N q
      = qIntBalanced (N : ℤ) q / qIntBalanced 2 q * qIntBalanced ((N : ℤ) + 1) q := by
  have c11 : content 1 1 = 0 := by norm_num [content]
  have c12 : content 1 2 = 1 := by norm_num [content]
  rw [schurPrincipalTwo, cellFactor, cellFactor, c11, c12, qIntBalanced_one ha,
    add_zero, div_one]

theorem schurPrincipalOneOne_eq (ha : q - q⁻¹ ≠ 0) (N : ℕ) :
    schurPrincipalOneOne N q
      = qIntBalanced (N : ℤ) q / qIntBalanced 2 q * qIntBalanced ((N : ℤ) - 1) q := by
  have c11 : content 1 1 = 0 := by norm_num [content]
  have c21 : content 2 1 = -1 := by norm_num [content]
  rw [schurPrincipalOneOne, cellFactor, cellFactor, c11, c21, qIntBalanced_one ha,
    add_zero, div_one, ← sub_eq_add_neg]

/-- **The Markov normaliser is `[N]_q²`** — `s_{(2)} + s_{(1,1)} = [N]_q²`, by
`[N+1]_q + [N−1]_q = [2]_q[N]_q`. -/
theorem schur_sum (hq : 1 < q) (N : ℕ) :
    schurPrincipalTwo N q + schurPrincipalOneOne N q = qIntBalanced (N : ℤ) q ^ 2 := by
  have hq0 := q_ne_zero hq
  have ha := hecke_ne_zero hq
  have hd := qIntBalanced_two_ne_zero hq
  rw [schurPrincipalTwo_eq ha, schurPrincipalOneOne_eq ha]
  have expand : qIntBalanced (N : ℤ) q / qIntBalanced 2 q * qIntBalanced ((N : ℤ) + 1) q
      + qIntBalanced (N : ℤ) q / qIntBalanced 2 q * qIntBalanced ((N : ℤ) - 1) q
      = qIntBalanced (N : ℤ) q / qIntBalanced 2 q
        * (qIntBalanced ((N : ℤ) + 1) q + qIntBalanced ((N : ℤ) - 1) q) := by ring
  rw [expand, qIntBalanced_shift_sum hq0 ha]
  field_simp

/-- **The unnormalised trace is `[N]_q · q^N`** — `s_{(2)}·q + s_{(1,1)}·(−q⁻¹)`,
by `q[N+1]_q − q⁻¹[N−1]_q = q^N[2]_q`.  The two coefficients are the eigenvalues
of `σ` on the two blocks of `H_2(q)`. -/
theorem schur_combo (hq : 1 < q) (N : ℕ) :
    schurPrincipalTwo N q * q + schurPrincipalOneOne N q * (-(q⁻¹))
      = qIntBalanced (N : ℤ) q * q ^ N := by
  have hq0 := q_ne_zero hq
  have ha := hecke_ne_zero hq
  have hd := qIntBalanced_two_ne_zero hq
  have key := qIntBalanced_shift_diff hq0 ha (N : ℤ)
  rw [zpow_natCast] at key
  rw [schurPrincipalTwo_eq ha, schurPrincipalOneOne_eq ha]
  have expand : qIntBalanced (N : ℤ) q / qIntBalanced 2 q * qIntBalanced ((N : ℤ) + 1) q * q
      + qIntBalanced (N : ℤ) q / qIntBalanced 2 q * qIntBalanced ((N : ℤ) - 1) q * (-(q⁻¹))
      = qIntBalanced (N : ℤ) q / qIntBalanced 2 q
        * (q * qIntBalanced ((N : ℤ) + 1) q - q⁻¹ * qIntBalanced ((N : ℤ) - 1) q) := by ring
  rw [expand, key]
  field_simp

/-! ### The identity -/

/-- **The hook-content weights give `markovParam`.**

`tr_M(σ) = y_{(2)}·q + y_{(1,1)}·(−q⁻¹) = (q − q⁻¹)q^{2N}/(q^{2N} − 1)`, for
every rank `N ≥ 1` and every `q > 1`, with the left side built from the
hook-content product over the four named cells of the two partitions of `2` and
the right side taken unchanged from `OcneanuRankFamily`.

This is the `n = 2` instance of the hook-content principal-specialisation
identity that `OcneanuRankFamily`'s module docstring cites rather than proves.
It is **not** the general formula — see this file's docstring. -/
theorem hookContent_markovParam (hq : 1 < q) {N : ℕ} (hN : 1 ≤ N) :
    markovWeightTwo N q * q + markovWeightOneOne N q * (-(q⁻¹)) = markovParam N q := by
  have hA : qIntBalanced (N : ℤ) q ≠ 0 := ne_of_gt (qIntBalanced_pos hq hN)
  have hmp := qIntBalanced_mul_markovParam hq hN
  rw [markovWeightTwo, markovWeightOneOne]
  have expand : schurPrincipalTwo N q / (schurPrincipalTwo N q + schurPrincipalOneOne N q) * q
      + schurPrincipalOneOne N q / (schurPrincipalTwo N q + schurPrincipalOneOne N q)
        * (-(q⁻¹))
      = (schurPrincipalTwo N q * q + schurPrincipalOneOne N q * (-(q⁻¹)))
        / (schurPrincipalTwo N q + schurPrincipalOneOne N q) := by ring
  rw [expand, schur_combo hq N, schur_sum hq N, div_eq_iff (pow_ne_zero 2 hA)]
  linear_combination (-(qIntBalanced (N : ℤ) q)) * hmp

/-- **Convention D from the weights.**  At `N = 2` the hook-content weights give
`z = q³/(q²+1)` — the corpus's canonical Markov parameter (owner ruling
2026-08-15 R1).  So convention D is not a normalisation choice: it is the `SU(2)`
principal specialisation, cell by cell. -/
theorem markovWeight_conventionD (hq : 1 < q) :
    markovWeightTwo 2 q * q + markovWeightOneOne 2 q * (-(q⁻¹)) = q ^ 3 / (q ^ 2 + 1) := by
  rw [hookContent_markovParam hq (by omega), markovParam_two hq]

/-- **The rank-3 specification from the weights.**  `z_3 = q⁵/(q⁴+q²+1)`, what a
flavour `SU(3)` trace on the same `H_n(q)` would have to carry.  A specification,
not a construction. -/
theorem markovWeight_rank_three (hq : 1 < q) :
    markovWeightTwo 3 q * q + markovWeightOneOne 3 q * (-(q⁻¹))
      = q ^ 5 / (q ^ 4 + q ^ 2 + 1) := by
  rw [hookContent_markovParam hq (by omega), markovParam_three hq]

/-! ### The row cap at `n = 2` -/

/-- **The `gl(1)` corner.**  At `N = 1` the antisymmetric specialisation vanishes
identically — the cell `(2,1)` has content `−1`, so its numerator factor is
`[1 + (−1)]_q = [0]_q = 0`.  This is the `n = 2` shadow of
`OcneanuRankFamily.rowCapFactor_eq_zero`: a partition with more rows than the
rank dies at the cap cell.  No hypothesis on `q` is needed. -/
theorem schurPrincipalOneOne_rank_one (q : ℝ) : schurPrincipalOneOne 1 q = 0 := by
  norm_num [schurPrincipalOneOne, cellFactor, content]

/-- The normalised form of the same statement: `y_{(1,1)} = 0` at `N = 1`, which
is what the producer returns numerically. -/
theorem markovWeightOneOne_rank_one (q : ℝ) : markovWeightOneOne 1 q = 0 := by
  rw [markovWeightOneOne, schurPrincipalOneOne_rank_one, zero_div]

end QOU.Eightfold.HookContentMarkovParam

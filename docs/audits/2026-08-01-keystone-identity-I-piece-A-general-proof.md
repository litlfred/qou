# Keystone Identity I, Piece A — general-n elementary proof (HLF-free, dimension-free)

**Date:** 2026-08-01. **Bean:** `qou-ph2a` (μ–p / Δ_λ push) → keystone `s5bb`.
**Result:** an explicit, self-contained, general-`n` proof of **Piece A** of
Identity I — the per-partition hook–content identity

$$
  \sum_{c\in\lambda} h(c)^2 \;=\; \sum_{c\in\lambda} \mathrm{content}(c)^2 \;+\; n^2,
  \qquad n=|\lambda|,
$$

using **no hook-length formula, no dimensions, no SYT/RSK** — only elementary
double-counting of cell pairs. This upgrades the prior corpus status of Piece A
from *"general = classical beta-number / corner induction (deferred)"*
([`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean),
[`2026-07-07-keystone-identity-I-hlf-free-resolution.md`](2026-07-07-keystone-identity-I-hlf-free-resolution.md))
to an **explicit elementary derivation**. Piece A is the `2n²` half of Identity I
`2M(n) = n(3n−1)`; the other half (Piece B, the Plancherel content-square mean
`= C(n,2)`) is the Jucys–Murphy input, unchanged.

## Why this matters for the derivation chain

Identity I is the single carried representation-theoretic input to the
**heat-kernel-defect closed form** `144·C(n) = −n(n−1)(2n−13)`
(`n144C_closed_form`, sorry-free), which is the **falsifiable, `q₀`-free
sub-target** any geometric realization of the s5-so3 `W_λ` index must reproduce
(the `n=7` sign change). Closing Identity I in general therefore removes the last
representation-theoretic hypothesis from the defect gate on the surviving μ–p /
Δ_λ route (`docs/coordination/s5-so3-keystone.md`). This note closes the
*mathematics* of Piece A generally; the residual is Lean formalization (bean
below).

## Setup

Fix a partition `λ = (λ_0 ≥ λ_1 ≥ …)` with Young diagram (0-indexed) cells
`c = (i,j)`, `0 ≤ i < ℓ`, `0 ≤ j < λ_i`, `n = Σ_i λ_i`. For a cell `c=(i,j)`:

- **arm** `a(c) = λ_i − 1 − j` (cells strictly right in the row),
- **leg** `l(c) = |{i' > i : λ_{i'} > j}|` (cells strictly below in the column),
- **left** `= j` (cells strictly left in the row), **above** `= i` (cells strictly above in the column),
- **hook** `h(c) = a(c) + l(c) + 1`, **content** `content(c) = j − i`.

Row `i` has length `λ_i = j + 1 + a(c)`; column `j` has height `λ'_j = i + 1 + l(c)`.

## The separable-sum reduction

Expand `h² − content² = (a+l+1)² − (j−i)²` and sum over cells:

$$
  h^2 - c^2 = a^2 + l^2 + 1 + 2al + 2a + 2l - j^2 + 2ij - i^2 .
$$

Now use the **row/column-separable** sums (each is a sum over rows or columns
alone, elementary):

| sum | value | reason |
|---|---|---|
| `Σ_c a(c)` | `A := Σ_i C(λ_i,2)` | in a row of length `λ_i`, arms are `0,1,…,λ_i−1` |
| `Σ_c j` | `A` | left-counts in that row are `0,1,…,λ_i−1` — **same multiset as arms** |
| `Σ_c a²` = `Σ_c j²` | `Sa` | same multiset per row |
| `Σ_c l(c)` | `L := Σ_j C(λ'_j,2)` | column-wise, dual to arms |
| `Σ_c i` | `L` | above-counts, dual to left |
| `Σ_c l²` = `Σ_c i²` | `Sl` | dual |

The `a²`/`j²` and `l²`/`i²` terms **cancel in pairs** (`Sa − Sa = 0`,
`Sl − Sl = 0`), and `Σ1 = n`, leaving

$$
  \boxed{\;\sum_c h^2 - \sum_c c^2 \;=\; n + 2A + 2L + 2\!\sum_c a\,l + 2\!\sum_c i\,j\;}
$$

So Piece A (`Σh² − Σc² = n²`) is **equivalent** to

$$
  A + L + \sum_c a(c)\,l(c) + \sum_c i\,j \;=\; \binom{n}{2}. \tag{$\ast$}
$$

## The pair-counting identity

Partition the `C(n,2)` unordered pairs of cells by their mutual position:

$$
  \binom n2 \;=\; \underbrace{A}_{\text{same row}} \;+\; \underbrace{L}_{\text{same column}} \;+\; \underbrace{D}_{\text{distinct row \& column}} ,
$$

since same-row pairs number `Σ_i C(λ_i,2)=A`, same-column pairs `Σ_j C(λ'_j,2)=L`.
So `(∗)` reduces to the single clean claim

$$
  \sum_c a(c)\,l(c) \;+\; \sum_c i\,j \;=\; D. \tag{$\ast\ast$}
$$

**Proof of `(∗∗)`.** Every distinct-row-distinct-column pair is either
**upper-right/lower-left** (UR/LL: `i_1<i_2`, `j_1>j_2`) or **upper-left/lower-right**
(UL/LR: `i_1<i_2`, `j_1<j_2`).

- `Σ_c a(c)l(c)` counts, for each cell `c=(i,j)`, pairs (one arm cell `(i,j')`,
  `j'>j`; one leg cell `(i',j)`, `i'>i`). The pair `{(i,j'),(i',j)}` is UR/LL, and
  `c=(i,j)` is recovered as `(\text{UR.row},\text{LL.col})`, which is **always a
  cell** (`(i,j')` a cell ⇒ `(i,j)` a cell). So `Σal` counts **every UR/LL pair
  exactly once**.
- `Σ_c i·j` counts, for each `c=(i,j)`, pairs (one left cell `(i,j'')`, `j''<j`;
  one above cell `(i'',j)`, `i''<i`). The pair `{(i,j''),(i'',j)}` is again UR/LL
  (above cell is upper-right, left cell is lower-left), with `c=(i,j)` recovered as
  `(\text{LL.row},\text{UR.col})` — the **opposite rectangle corner**, which is a
  cell **iff** `(i,j)∈λ`, i.e. iff the full rectangle `[i'',i]×[j'',j]` is filled.

So a UR/LL pair is counted **once** by `Σal` and **once more** by `Σij` **exactly
when its rectangle is full**. A UL/LR pair is counted by **neither**. But a full
rectangle carries **both** diagonals: its UR/LL pair (double-counted: `1+1`) and
its UL/LR pair (zero-counted: `0`). Summed, `2+0 = 1+1`, matching `D`'s count of
one per diagonal. For a non-full configuration the missing rectangle corner means
the UL/LR pair is not a pair of cells at all, and the UR/LL pair is counted once —
again matching `D`. Hence `Σal + Σij = D` for **every** Young diagram. ∎

Piece A follows: `Σh² − Σc² = n + 2(A+L+D) − 2D + … `; concretely `(∗)` holds, so
`Σh² − Σc² = n²`. ∎

## Verification

Numerically confirmed for 12 partitions spanning full rectangles
(`(4,4,4,4)`, `(2⁶)`), staircases (`(7,5,3,1)`), hooks, and mixed shapes — all four
sub-claims (Piece A, the separable reduction, `(∗∗)`, and `A+L+D=C(n,2)`) hold.
Machine-checked sorry-free in Lean for **`n ≤ 8`** (`pieceA_hook_content_identity`,
extended this PR from `n ≤ 6` to cover the physically-critical `n=7` defect
sign-flip), each diagram computed from its structure (not tabulated).

## Lean formalization — COMPLETE (2026-08-01, bean `qou-o5xj` closed)

The elementary proof above is now a **general-`n`, sorry-free Lean theorem** over
Mathlib's `YoungDiagram`:
[`QOU.BraidKnot.PieceA.pieceA`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/PieceAGeneral.lean)
— `Σ_c hook² = Σ_c content² + n²` for **every** Young diagram, HLF-free and
dimension-free (`lean`-direct exit 0). The formalization follows the proof above
in stages: the row/column reflections (`sum_armZ_generic` / `sum_legZ_generic`),
the separable reduction (`pieceA_reduction`), the two pair-counting bijections
`Σ(arm·leg) = |UR/LL|` (`sum_armLeg_eq_urll`) and `Σ(i·j) = |UL/LR|`
(`sum_prod_eq_ullr` — clean, since down-closure fills the up-left rectangle so no
compensation is needed at the Lean level), the same-row/col counts
(`sum_snd_eq_srLower` / `sum_fst_eq_scLower`), and the off-diagonal 8-sign-class
assembly (`pairCount_holds`). Piece B (Plancherel/JM content-square mean
`= C(n,2)`) remains the rep-theory half (needs `ℂ[S_n]` / Jucys–Murphy or RSK
infra Mathlib lacks — bean `qou-su6h`).

## Cross-refs

- [`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean) — `pieceA_hook_content_identity` (`n≤8`), `n144C_closed_form`.
- [`2026-07-07-keystone-identity-I-hlf-free-resolution.md`](2026-07-07-keystone-identity-I-hlf-free-resolution.md) — the HLF-free split (prior status: "deferred").
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — the defect sub-target on the surviving W_λ route.
- [`docs/audits/2026-08-01-mu-p-tension-attack-recon-floor-verdict.md`](2026-08-01-mu-p-tension-attack-recon-floor-verdict.md) — why this route is the one un-refuted μ–p / Δ_λ path.

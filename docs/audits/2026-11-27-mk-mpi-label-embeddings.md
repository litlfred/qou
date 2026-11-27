# m_K/m_π: where the quark labels enter (bean qou-mk34)

**Route:** Carl took the recommended option on 2026-11-27: define the kaon and the pion as Hecke objects built from strands and quark labels, then test whether 12, or [3]_q[4]_q, comes out. An honest negative was allowed.

## What the corpus already defines

The existing Hecke objects are the gluon-clasp braids β_clasp(n₁, n₂) = σ₁^{n₁} σ₂^{-n₂} σ₁ σ₂⁻¹ ∈ B₃. The pion is (3, 3) and the kaon is (3, 5) (`HyperbolicMesonClaspAndDiquarkSplit.lean`).

From these words the corpus builds the S^(2,1) block trace and the full H₃(q) Markov traces at z₂ and z₃.

A rerun of the exact sympy calculation gave, for every one of these invariants (the symmetric block, the S^(2,1) block, the alternating block, and the z₂ Markov trace), a kaon/pion ratio that is a rational function of q equal to **1 at q = 1**. None of them equals [3]_q[4]_q.

This is the case `MesonRatioSelectionStatus.clasp_reading_pion_eq_kaon` (PR #9449) already proves in general. When q = 1 the labels enter only as exponents of involutions, so every function of the clasp words takes the same value on the pion and the kaon.

## New in this PR (`QOU/EightfoldWay/MesonLabelEmbeddings.lean`, sorry-free)

- `classical_ratio_ne_p34`. Suppose a polynomial reading N/D has classical ratio r ≠ 12, meaning N(1) = r·D(1). Then N/D ≠ [3]_q[4]_q as an identity in q. This generalises the r = 1 lemma from #9449.
- `label_embedding_ratios_ne_twelve`. The kaon-to-pion ratio for each way the labels could enter:

| labels enter as | pion | kaon | ratio |
|---|---|---|---|
| exponents of clasp generators (corpus definition) | — | — | 1 |
| sl₂ colour dimensions n₁n₂ | 9 | 15 | 5/3 |
| strand count n₁+n₂ | 6 | 8 | 4/3 |
| Hecke dimension (n₁+n₂)! | 720 | 40320 | 56 |

  None of these ratios is 12.
- `half_sum_product_eq_twelve`. The half-sums are 3 for the pion and 4 for the kaon. So 12 does appear, but only as the **product** of a pion number and a kaon number. Reading m_K²/m_π² as that product is the sl₂ fusion reading dim(V₃ ⊗ V₄), which the corpus already records as a post-hoc spin assignment (`meson-3x4-structural-origin.witness.json`).

The axioms used are only propext, Classical.choice and Quot.sound. lean-direct exit 0.

## Verdict

This is a negative of scope (a). It excludes the four embeddings listed. It is not a structural exclusion of every definition of K and π.

The row stays **Selected**. The half-sum observation shows where (3, 4) would have to come from: the labels must enter additively, halved, and the two numbers must be multiplied. That is a reading, not a consequence of the meson definitions.

## Addendum: no meson-total ratio is 12 (Carl's pick, same day)

`no_meson_total_ratio_twelve`: let a, b, c, d be quark labels, each in {3, 5, 7}. Then a+b ≠ 12(c+d) and ab ≠ 12cd.

The largest possible ratio of label sums is 14/6, and the largest ratio of label products is 49/9. So no ratio of label totals between any two mesons is 12, kaon to pion included. The proof checks all 81 cases.

One meson does have a label total of exactly 12, the pair (5, 7). That is a single meson's total, though, not a ratio between two mesons, and (5, 7) is neither the kaon nor the pion.

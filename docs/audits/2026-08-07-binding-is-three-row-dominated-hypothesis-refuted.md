# The two-row hypothesis is refuted — and binding turns out to be ≥3-row *dominated*

**Date:** 2026-08-07 · **Branch:** `claude/1ppq-l2-closure-attacks-ufrfun` · **PR #4664**
**Probe:** [`computations/two_row_vs_higher_row_binding_split.py`](../../computations/two_row_vs_higher_row_binding_split.py)
**Witness:** `two-row-vs-higher-row-binding-split.witness.json` · **Beans:** `qou-lh7l`, `qou-kemt`
**Supersedes the §2 claim of** [`2026-08-07-two-row-projection-is-the-pairwise-cap.md`](2026-08-07-two-row-projection-is-the-pairwise-cap.md)

`free_parameters = 0`. Reads committed 50-dps witnesses, stdlib `decimal` at 60 dps,
**no float64**. Audit-only; nothing wired.

---

## 0. My hypothesis was wrong — stated first

I claimed the missing super-pairwise binding term is *"the sector the corpus explicitly
sets to zero"* — that the binding formula inherits the `ℓ(λ) ≤ 2` restriction from
`def:two-row-stratum`, and that the six failed ansätze failed because they reweighted
`Δ_λ` inside a truncated sum.

**That is refuted by the data. The binding formula does not truncate.** It already sums
**all** partitions. Two independent corpus cross-checks confirm my implementation
reproduces the existing compute exactly:

| corpus value | source | this probe |
|---|---|---|
| `B(D)` bare per-λ sum `= 0.380 MeV` | `binding_energy_categorical_deuteron.py` header | **0.3801** ✓ |
| `C_knot` deuteron deficit `= 5.852` | same (the *fitted* deficit ratio) | **5.8530** ✓ |

So the two-row projection is a statement about which stratum the **SU(2) spin-pairing
observable** sees — *not* a restriction applied in the binding sum. I conflated the two.
The identification `N=2 ⟺ two-row ⟺ pairwise` still stands as algebra; what does **not**
stand is my inference that binding therefore discards the ≥3-row sector.

---

## 1. What the measurement actually found — the dominance is *inverted*

Two different sums, deliberately kept apart:

- **(a) Markov trace** `tr_M = Σ_λ y_λ χ^λ`
- **(b) binding sum** `B/m_e = |Σ_λ y_λ χ^λ Δ_λ|`, with the **proved**
  `Δ_λ = (−1)^{n(λ)}·f^λ` (`dtEuler_eq_deltaLambda_unconditional`, sorry-free)

| atom | A | `tr_M` in ≥3-row | **binding sum in ≥3-row** | `B_2row` | `B_full` | `B_AME` |
|---|---|---:|---:|---:|---:|---:|
| deuteron | 2 | 5.42 % | **26.21 %** | 0.2804 | 0.3801 | 2.2246 |
| tritium | 3 | 8.72 % | **62.07 %** | 0.7240 | 1.9085 | 8.4818 |
| ³He | 3 | 2.99 % | **61.17 %** | 0.9105 | 2.3446 | 7.7180 |
| ⁴He | 4 | 7.34 % | **100.02 %** | **0.0007** | 3.0382 | 28.2957 |

> **The trace is two-row dominated; the binding sum is ≥3-row dominated. They are
> opposite.**

The mechanism is not mysterious: `y_λ` (Wenzl weight) concentrates on two-row
partitions, but `Δ_λ = ±f^λ` weights by the **SYT count**, which is largest for
balanced, many-row diagrams. The `Δ_λ` factor **inverts the stratum dominance.**

At ⁴He the two-row sector contributes `0.0007 MeV` against a full sum of `3.0382` —
**0.02 %**, with near-total internal cancellation (hence the `100.02 %`). The binding
observable at ⁴He is, to four significant figures, an **entirely ≥3-row object**.

---

## 2. The genuinely useful part: the ≥3-row share grows with A

| A | 2 | 3 | 3 | 4 |
|---|---:|---:|---:|---:|
| ≥3-row share of binding | 26.2 % | 62.1 % | 61.2 % | **100.0 %** |

This is the **super-pairwise sector's share growing with mass number** — the direction
the missing extensive term must go, measured rather than assumed. It is also exactly
what the row-cap algebra predicts qualitatively: more strands ⇒ more partitions with
`ℓ(λ) ≥ 3` ⇒ more irreducibly-≥3-body channels available.

**Four points, two of them the same A.** This is a trend, not a law, and `⁴He` is the
only `A=4` point. Do not quote it as an `A`-scaling exponent.

---

## 3. What this does *not* fix

The full-sum deficit ratios are **not constant**:

| atom | deuteron | tritium | ³He | ⁴He |
|---|---:|---:|---:|---:|
| `B_AME / B_full` | 5.853 | 4.444 | 3.292 | **9.313** |

A **2.8× spread**, and ⁴He is the *worst*. So including the ≥3-row sector — which the
compute already does — does **not** close the magnitude, and no single scalar rescaling
can (that is the `C_knot` fit, retracted in the corpus, and the ℓ¹-ceiling prune said
the same thing from the sign side).

The missing magnitude therefore remains open, and this probe **narrows where it is
not**: it is not a truncation artifact, and it is not recoverable by re-including a
discarded stratum, because nothing was discarded.

---

## 4. Corpus-currency note (a real trap for readers)

`prop:he4-two-row-dominance` reports the two-row stratum carrying **86.6 %** (top-5
cumulative) / **92.7 %** (full `Λ²(12)`) of `tr_M(β_{⁴He})`. **Both figures are correct
and both are about `tr_M`.**

The trap: a reader who carries "two-row dominance" over to the **binding** observable
gets it backwards by two orders of magnitude — binding at ⁴He is `0.02 %` two-row. The
content blocks are amended in this PR to say so explicitly.

*(Also corrected in passing: my earlier docs quoted "86.6 % ⇒ 13.4 % discarded". The
full-stratum figure is 92.7 %, so the `tr_M` discard is ~7.3 %, and the per-isotope
measured values are in the table above. `probe_he4_canonical_tr_m_fingerprint.py`
already flagged the 86.6-vs-92.7 distinction; I missed it.)*

---

## 5. Status of the arc after this probe

| claim | status |
|---|---|
| `N=2 ⟺ ℓ(λ)≤2 ⟺ pairwise ⟺ `ρ_A ≤ C(A,2)` | **stands** (algebra, row cap) |
| three-body channels exist iff `N ≥ 3` (#4640 read for binding) | **stands** |
| binding truncates to two rows, missing term = discarded stratum | **REFUTED** (this probe) |
| binding sum is ≥3-row dominated, share grows with A | **new, measured** |
| `≥3`-row inclusion closes the magnitude | **no** — deficit spread 3.29–9.31 |

**Next honest step:** the deficit is *worst* at ⁴He (9.31) and *best* at ³He (3.29),
while the ≥3-row share is *highest* at ⁴He. Those move together in the wrong direction
— more ≥3-body content correlates with a **larger** deficit, not a smaller one. That is
a concrete, falsifiable anti-correlation worth chasing, and it argues the missing object
is **not** simply "more of the same higher-row terms."

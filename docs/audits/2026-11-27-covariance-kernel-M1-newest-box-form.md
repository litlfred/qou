# Covariance kernel (`qou-x631`): M₁ as a covariance of the newest box, and half of single crossing

**Date:** 2026-11-27 · **Branch:** `claude/m1-newest-box-form-2026-11-27` · **Beans:** `qou-jmgu`
(single crossing), `qou-k5r5` (M₁ > 0 gap), epic `qou-x631` · **Tier:** exact reformulation with a
pen-and-paper derivation, computer-verified; one half of the single-crossing statement proved. It
does **not** prove M₁ > 0 for all n.

## Setting

[`2026-11-27-covariance-kernel-M1-jucys-murphy-form.md`](2026-11-27-covariance-kernel-M1-jucys-murphy-form.md)
wrote `M₁(n) = (n(n−1)(n−2)/3) · Σ_s s ρ_n(s)` with

```
ρ_n(s) = E_PG[ 1{i_n + j_n = s} / (r_{n−1} r_{n−2}) ],   r_k = c(k+1) − c(k),
```

an average over the last **three** boxes of a Plancherel-growth tableau. It stated the single-crossing
criterion (SC): if `ρ_n` changes sign once (negative, then positive), then `M₁(n) > 0`
(`YoungDiagramKernelSingleCrossing.firstMoment_pos_of_single_crossing`, sorry-free).

## Result 1: the last two boxes integrate out

Let `ν ~ Plancherel(n−1)` and add one box `x` with the transition probability `f^{ν+x}/(n f^ν)`. Write
`(i, j)` for its 1-indexed position, `s = i + j`, `c = j − i`, `m = min(i, j)`. Then

```
ρ_n(s) = E[ 1{i + j = s} · (c² − (n−1)) ] / ((n−1)(n−2)).
```

**Derivation.** Fix `λ = ν + x` with `c(x) = z`. Box `n−1` is a removable corner `y` of `ν`, and box
`n−2` a removable corner `u` of `ν' = ν − y`. The weight of the path is `f^μ f^λ / n!` with
`μ = ν' − u`. Use Kerov's identity for the cotransition measure `q_π(y) = f^{π−y}/f^π` of a diagram
`π` (Kerov, *Transition probabilities of continual Young diagrams*):

```
Σ_y q_π(y) / (w − y) = ( w − Π_a (w − x_a) / Π_b (w − y_b) ) / |π|,
```

with `x_a` the addable and `y_b` the removable contents of `π`. At an addable content `w` of `π`, the
product vanishes and the sum is `w/|π|`.

1. Sum over `u`. The content `c(y)` is addable for `ν'`, so `Σ_u f^{ν'−u}/(c(y) − c(u)) = f^{ν'} c(y)/(n−2)`.
2. Sum over `y`. `Σ_y f^{ν−y} c(y)/(z − c(y)) = f^ν (z · Σ_y q_ν(y)/(z − c(y)) − 1) = f^ν (z²/(n−1) − 1)`,
   since `z` is addable for `ν`.

The weight of `(ν, x)` is therefore `f^ν f^λ (z² − (n−1)) / ((n−1)(n−2) n!)`, which is the claim.

**Corollaries.** The weights `f^ν f^λ / n!` sum to 1. Since `Σ_s ρ_n(s) = 0`, the same step gives
`E[c²] = n − 1`: the second moment of the transition measure of `ν` is `|ν|`. Then

```
M₁(n) = (n/3) Cov(s, c²),     P(n) = (n/3) Cov(|c|, c²),     N(n) = −(2n/3) Cov(m, c²),
```

for the one random box `x`. Here `P = Cov_Planch(Σ|c|, ω₃)` and `N = −Cov_Planch(Σ d_u², ω₃)` are the
Fulman split, so `M₁ = P − N`. The split is the identity `s = |c| + 2m`.

So `M₁(n) > 0` says: **for the newest box of Plancherel growth, the antidiagonal index `i + j`
correlates positively with the squared content `c²`.** The earlier reformulation
([`2026-08-21-…-antidiagonal-reformulation.md`](2026-08-21-covariance-kernel-M1-antidiagonal-reformulation.md))
is `M₁ = Cov_Planch(Σ_□ b, Σ_□ c²)`, a covariance of two sums over all `n` cells. This one involves a
single cell.

**Verification.** [`wlambda_covariance_M1_newest_box_form.py`](../../computations/deltalambda/wlambda_covariance_M1_newest_box_form.py)
checks exact equality with the three-box `ρ_n` and with the hook-formula `M₁`, `P`, `N` for
`n = 4…10`, and `E[c²] = n − 1`. Arithmetic is exact integers and `Fraction` throughout. Witness:
`wlambda-covariance-M1-newest-box-form.witness.json`.

## Result 2: P > 0 is immediate (a second proof)

`|c|` and `c²` are both increasing functions of `|c|`, so by Chebyshev's sum inequality
`Cov(|c|, c²) ≥ 0`, with equality only if `|c|` is a.s. constant. That fails for `n ≥ 3`: the newest
box can be at `(1, n)` or at a cell of smaller `|c|`. Hence `P(n) > 0` for every `n ≥ 3`.

This is **not new as a sign statement**: Fact A of
[`2026-08-21-…-fulman-exchangeable-pair-reduction.md`](2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md)
proves `P ≥ 0` edge by edge. It is a shorter independent proof, and it gives strict positivity.

## Result 3: the lower half of single crossing

On antidiagonal `s`, every cell has `|c| = |j − i| ≤ i + j − 2 = s − 2`. So
`c² − (n−1) ≤ (s−2)² − (n−1)`, and

```
ρ_n(s) ≤ 0   whenever (s − 2)² ≤ n − 1.
```

This proves the negative half of SC on `s ≤ 2 + √(n−1)`. What remains open is the window
`2 + √(n−1) < s < t_n`, plus `ρ_n(s) ≥ 0` for `s ≥ t_n`, where `t_n` is the measured threshold
(`t_55 = 12`, against `2 + √54 = 9.35`).

## Result 4: two candidate sufficient conditions fail

Both would have closed SC, and both are measured false (exact):

1. **Monotone regression.** If `E[c² | s]` were non-decreasing in `s`, SC would follow at once. It
   fails at `s = 4`, first at `n = 24`, and for every larger `n` checked.
2. **Per-ν covariance.** If `Cov_{p_ν}(s, c²) ≥ 0` held under the transition measure of every `ν`,
   averaging would give `M₁ > 0` directly. It fails at `ν = (3,3,2)`, the first failing `|ν|`
   being 8. Further failures occur at `|ν| = 12, 13, …`; the counts are in the witness.

Both are scope (a): they say these two routes do not work as stated, not that SC is false.

## Measurement

`ρ_n` has exactly one sign change for every `n = 4…58`. The threshold is `t_n = 11` for `n = 41…46`,
`t_n = 12` for `n = 47…56` and `t_n = 13` for `n = 57, 58`. The witness records `n ≤ 45`; `n = 46…58` came from the same integer sign computation in a separate run, not recorded in the witness. This extends the `n ≤ 40` check of the Jucys–Murphy audit. The
single-box formula is about 100× faster than the three-box one (`n = 42` takes 2.7 s).

The exhaustive table already gives `M₁(n) > 0` for `n ≤ 78`, so this extension adds no new value of
`n`. It only supports SC as the right structural statement.

## What it is, and what it is not

- **Is:** a one-cell form of `M₁`, `P`, `N` and `ρ_n`, with a derivation; a proof of the lower half
  of SC; and two refuted sufficient conditions.
- **Is not:** a proof of SC or of `M₁ > 0` for all `n`. The open input of `qou-k5r5` is unchanged.
- **Not formalized.** The Kerov identity and the Plancherel-growth law are not in this repo's Lean.
  The elementary step behind Result 3 is the inequality `|j − i| ≤ i + j − 2`.
- **Next, on this route:** an upper-half statement in Kerov's continual-diagram language, i.e.
  `E[(c² − (n−1)) · 1{s}] ≥ 0` for `s ≥ t_n`, using the limit-shape concentration of the newest box.

## Cross-references

- Single-crossing criterion and three-box form: [`2026-11-27-covariance-kernel-M1-jucys-murphy-form.md`](2026-11-27-covariance-kernel-M1-jucys-murphy-form.md)
- Fulman split, Fact A: [`2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md`](2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md)
- All-cell antidiagonal form: [`2026-08-21-covariance-kernel-M1-antidiagonal-reformulation.md`](2026-08-21-covariance-kernel-M1-antidiagonal-reformulation.md)

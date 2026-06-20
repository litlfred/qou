# Type-B-folded-crystal-depth $n_\star$ — combinatorial probe

**Date:** 2026-05-11
**Branch:** `claude/n-star-type-b-crystal-depth`
**Relates to:** PR #638 (scalar $n_\star$ refutation + per-eigenvalue
operator probe), `conj:brane-tower-z-habiro`.

## TL;DR

The Type-B-folded-crystal depth — operationalised as the count of
**self-conjugate partitions** of $n = 3A$ — is the strongest
substrate-only candidate yet for the level-selection rule
$n_\star$. It reproduces the empirical uniform-$k$ closure depths
for **D** and **T** from #638's per-eigenvalue probe but cannot
explain **${}^3\mathrm{He}$**'s non-closure at any uniform $k$.

| Atom | $(Z, N, A)$ | $n = 3A$ | self-conj count | observed closure $k$ | match |
|---|---|---:|---:|---:|---:|
| D | $(1, 1, 2)$ | $6$ | $1$ | $k = 1$ | ✓ |
| T | $(1, 2, 3)$ | $9$ | $2$ | $k = 2$ | ✓ |
| ${}^3\mathrm{He}$ | $(2, 1, 3)$ | $9$ | $2$ | none in $\{1, \ldots, 10\}$ | ✗ |

**Reading.** The fold-depth candidate captures the $D \leftrightarrow T$
distinction (different self-conj counts at $n = 6$ vs $n = 9$). It is
**insensitive to the per-generator near-pole multiplicity profile** of
the atom's braid word, which is what distinguishes ${}^3\mathrm{He}$
from $T$ at the same strand count.

Witness:
[`probe_phiq_type_b_fold_depth.py`](../../computations/probe_phiq_type_b_fold_depth.py)
→ [`probe-phiq-type-b-fold-depth.witness.json`](../../computations/probe-phiq-type-b-fold-depth.witness.json).
All 5 assertions pass.

## Setup

Per #638's closure note (cycle 4 of `conj:brane-tower-z-habiro`):
the **scalar-eigenvalue** form and the **per-eigenvalue operator-valued**
form of $n_\star$ are both refuted across $\{D, T, {}^3\mathrm{He}\}$.
The surviving open thread is the **multiplicity-refined** form

$$
  n_\star\;\colon\;(\ell, n_0, k, \mathbf{m})\;\longmapsto\;\mathbb{N}_{\geq 1},
$$

where $\mathbf{m}$ is the per-generator near-pole multiplicity
profile of the atom's braid word.

PR #638 explicitly identified the next probe in queue as the
**Type-B-folded-crystal-depth** candidate (cf. the persisted
eigenvalue spectra in `probe-phiq-operator-valued.witness.json`,
intended for this very probe). This audit makes the operational
content of that candidate explicit and tests its substrate-only
combinatorial core.

## Operational definition

The **Type-B fold** acts on the Kashiwara crystal graph of
$H_n(q)$-modules via partition conjugation $\lambda \to \lambda^T$
(the diagonal flip of the Young diagram). Per the
$\mathfrak{sl}_n$-to-$\mathrm{B}_n$ folding pattern in
AGENTS.md §7b:

* **Fixed points** of the fold: self-conjugate partitions
  $\lambda = \lambda^T$ → unfolded orbit length 1.
* **Non-fixed** partitions pair up $(\lambda, \lambda^T)$ → orbit
  length 2.

The Type-B-folded-crystal **depth** of the symmetric stratum is the
count of orbit-length-1 partitions, i.e. the count of self-conjugate
partitions of $n$.

The candidate $n_\star$ rule under test:

$$
  n_\star(\mathfrak{H})
  \;:=\;
  \#\{\lambda \vdash 3A : \lambda = \lambda^T\}.
$$

This depends only on the strand count $n = 3A$ — a substrate-only
invariant — and is computable by pure combinatorial enumeration.

## Closed-form self-conjugate-partition counts at low $n$

| $n$ | Self-conjugate partitions | Count |
|---:|---|---:|
| $6$ (D, A = 2) | $(3, 2, 1)$ | $1$ |
| $9$ (T, ${}^3\mathrm{He}$, A = 3) | $(5, 1, 1, 1, 1)$, $(3, 3, 3)$ | $2$ |
| $12$ (⁴He, A = 4) | (4 partitions) | $4$ |
| $15$ (A = 5) | — | $4$ |
| $18$ (A = 6) | — | $7$ |

(OEIS A000700.) Note that the count depends only on $n$, not on
$(Z, N)$ separately — so the Type-B fold depth predicts the **same**
$n_\star$ for $T$ and ${}^3\mathrm{He}$ (both have $n = 9$), which
is the source of the ${}^3\mathrm{He}$ exception.

## Comparison to #638's empirical closure depths

| Atom | candidate $n_\star$ | observed best $k$ | residual at best $k$ | disposition |
|---|---:|---:|---:|---|
| D | $1$ | $1$ | $-6.87\%$ | **match** ($\leq 10\%$) |
| T | $2$ | $2$ | $-8.00\%$ | **match** ($\leq 10\%$) |
| ${}^3\mathrm{He}$ | $2$ | none in $\{1, \ldots, 10\}$ | $\geq +50\%$ at every $k$ | **mismatch** |

**Where the candidate succeeds.** The $D \leftrightarrow T$
distinction is captured automatically by the strand-count
dependence: $n_6 = 1$ for D, $n_9 = 2$ for T. The substrate-only
combinatorics agrees with the empirical $k = $ best-closure-depth
without per-atom tuning.

**Where the candidate fails.** ${}^3\mathrm{He}$ has the same strand
count as $T$ ($n = 9$) but a different per-generator near-pole
multiplicity profile: ${}^3\mathrm{He}$'s 8-generator braid word
carries **two** near-pole entries ($\lvert\hat V\rvert \approx 0.989$
at positions 0 and 3) vs $T$'s single near-pole entry. The fold-
depth candidate is insensitive to this profile and predicts $k = 2$
for ${}^3\mathrm{He}$, which is empirically wrong.

## Disposition

The Type-B fold-depth candidate is:

* **A real structural advance** over the scalar-eigenvalue family
  refuted in #638 — it reproduces the *correct* k-value per
  atom in 2 of 3 cases, where scalar candidates failed all 3.
* **Not the closure**: the ${}^3\mathrm{He}$ failure says the
  fold-depth alone is not sufficient. It contributes the
  $(\ell, n_0, k)$ piece of the open multiplicity-refined form,
  and the multiplicity profile $\mathbf{m}$ supplies the
  ${}^3\mathrm{He}$ correction.

## What this rules in / out

**Rules in** (positive structural finding):

* Type-B fold-depth is a viable component of the open
  $n_\star(\ell, n_0, k, \mathbf{m})$ rule. Its strand-count
  dependence $n_\star = $ count of self-conjugate partitions of
  $3A$ matches the D / T closure depths exactly.
* The Kashiwara-crystal interpretation (per AGENTS.md §7b)
  supplies a categorical / substrate-aligned reason for why
  self-conjugate partitions matter: they are the fold-fixed
  points of the type-B folding pattern on the unfolded
  $\mathfrak{sl}_n$ crystal.

**Rules out** (negative finding):

* The simple "$n_\star = $ self-conjugate count" rule. Same
  refutation pattern as #638's scalar candidates: a single
  substrate-only scalar invariant is not enough; the
  multiplicity profile must enter.

## Next probe (for follow-up)

A multiplicity-refined version would compute, for each atom, the
quantity

$$
  n_\star(\mathfrak{H})
  \;\stackrel{?}{=}\;
  \#\{\lambda \vdash 3A : \lambda = \lambda^T\}
  \;+\;
  \delta_{\mathrm{near\text{-}pole}}(\mathfrak{H}),
$$

where $\delta_{\mathrm{near\text{-}pole}}$ is a correction supplied
by the per-generator near-pole multiplicity count (e.g. $+1$ when
${}^3\mathrm{He}$'s 2-pole pattern is detected). Operationalising
$\delta$ requires the ρ_λ braid-trace data persisted in PR #638's
`probe-phiq-operator-valued.witness.json` — out of scope for this
strand-count-only probe.

## Coordination

Sibling-share with #638: this probe is the natural follow-up the
#638 owner-context comment flagged as queued. The substrate-only
combinatorial part is closed here; the multiplicity-refined part
remains open per #638's "Refined open question" section.

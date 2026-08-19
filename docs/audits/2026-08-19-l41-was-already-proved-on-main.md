# L4-1 was already proved on `main`, in full, and stronger — since 2026-08-10

**Date**: 2026-08-19 · **Beans**: `qou-me9q`, `qou-itg0`, `qou-q8lc`,
`qou-ph2s`, `qou-shrp` (epic `qou-u1b5`) · **Verdict**: the entire L4-1 brick
is redundant, not merely its Euler–Maclaurin step. Follow-on to
[`2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md`](2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md),
which found the E–M part and re-scoped the epic's *future* bricks. Applying
that same re-scope rule to the *finished* brick turned up the larger result.

## The corpus result

[`QOU/Knot/KashaevAsymptotic.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/KashaevAsymptotic.lean),
`kashaev_log_sum_asymptotic`, for `1 ≤ k`, `k < N`, `4 ≤ N`:

    | ∑_{j=1}^{k} log(2 sin(jπ/N))
        − ( −(N/π)·Lob(kπ/N)  +  ½·log(2N·sin(kπ/N))  +  (π/(12N))·cot(kπ/N) ) |
      ≤  1/(144k²)  +  (7/12)(π/N)²  +  (π/N)²/(12·sin²(kπ/N))

**Verified here**: import cone of 17 modules builds `ok=17`; `#print axioms`
gives `[propext, Classical.choice, Quot.sound]` — no `sorryAx`. The single
occurrence of the string "sorry" in the file is the word in a comment.

## Versus what L4-1 was chasing

[`2026-08-11-l41-euler-maclaurin-feasibility.md`](2026-08-11-l41-euler-maclaurin-feasibility.md)
states the target as

    S(n) = −(N/π)·Λ(nπ/N) + ½·log( n·sin(rπ)/(rπ) ) + O(1/N),   r = n/N.

The two ½-log terms agree up to an explicit additive constant — not "modulo
bookkeeping":

    n·sin(rπ)/(rπ)  =  k·sin(kπ/N)·N/(kπ)  =  N·sin(kπ/N)/π

so the target's term is `½·log(N sin(kπ/N)/π)` and the corpus's is
`½·log(2N sin(kπ/N))`; they differ by `½·log(2π)` — precisely the Stirling
constant that L4-1's `log n!` route was going to produce, placed differently by
the two conventions.

The corpus result is then **strictly stronger** on two counts:

1. it **identifies** the `O(1/N)` term as `(π/(12N))·cot(kπ/N)`, where the
   target left it as a symbol;
2. its error is **effective** — explicit constants, no asymptotic notation.

## What this makes redundant

Everything built for L4-1, not just the E–M step already retracted:

| Bean | File(s) | Superseded by |
|---|---|---|
| `qou-me9q` | `LogSineCellDefect.lean` (`cell_defect_repr`) | `sum_log_two_sin_split` — an *exact algebraic* split, no cell integrals at all |
| `qou-itg0` | `LogFactorialStirling.lean` | the `log(k!)` handling inside the corpus proof |
| `qou-q8lc`, `qou-ph2s` | `LogSineSingularPart`, `LogSineSmoothPart`, `LogSineRiemannForm` | the same proof's `logSinc` half |
| `qou-shrp` | `LogSineSharpConstant`, `EulerMaclaurinFirst` | `abs_sum_logSinc_sub_euler_maclaurin` (already recorded) |

The decomposition the whole brick was organised around,

    ∑_{j=1}^{k} log(2 sin(jπ/N)) = k·log(2π/N) + log(k!) + ∑_{j=1}^{k} logSinc(jπ/N)

is `KashaevEndpointSplit.sum_log_two_sin_split` — **exact**, with no integral
representation and no telescope. L4-1 reached the same split the long way,
through a cell-defect representation and an exact singular telescope, and then
stopped one order short of where the corpus already was.

## Timeline

`KashaevAsymptotic.lean` has been on `main` since **2026-08-10 19:24 UTC**. The
L4-1 feasibility pass that opened these beans is dated **2026-08-11** — the day
after. Every L4-1 brick was opened, worked and merged against a corpus that
already contained a stronger statement of the brick's own target.

## Root cause: the same one, at the level above

The prior audit found the corpus-grep checklist was not run before declaring
an *infrastructure* gap. This one is the same failure at the level of the
*mathematical target*: the feasibility pass wrote a target and decomposed it
into sub-bricks without grepping `content/` for the target itself.

`grep -rlniE "lobachevsky|Lambda|clausen" .../QOU/Knot/*.lean` lists
`KashaevAsymptotic.lean`. One grep, before opening five beans.

There is a further sharpening worth recording. Van der Veen's Lemma 3 was
treated throughout as the thing to be formalised. It is a *cited source's*
statement of a result; the question that should have been asked first is
whether the corpus already proves the result, not whether it already
formalises the paper's route to it. Those are different greps, and only the
first one matters.

## What is NOT redundant

* **`SincDeriv.lean`** — `Real.sinc` differentiability, absent from Mathlib and
  from this corpus. Stands, as already recorded.
* **The epic's target.** `VdVWhiteheadLemma4` still has no instance anywhere;
  the `Kashaev*` lane is `4₁` (`kashaevProd` is defined in
  `FigureEightVolume.lean`), not the Whitehead link. **`qou-u1b5` remains open
  and worth doing** — with its remaining bricks assembled from existing generic
  infra per the prior audit, and its *finished* brick L4-1 replaced by a
  citation of `kashaev_log_sum_asymptotic`.

## Actions

1. `qou-me9q`, `qou-itg0`, `qou-q8lc`, `qou-ph2s`, `qou-shrp` annotated
   redundant, pointing at `kashaev_log_sum_asymptotic`.
2. The seven L4-1 Lean files get headers saying so. **Nothing deleted** — the
   proofs are correct and sorry-free, and the repo's standing rule is to
   re-scope findings, not remove them.
3. Whatever consumes L4-1 downstream should cite
   `kashaev_log_sum_asymptotic`, which is stronger and effective.

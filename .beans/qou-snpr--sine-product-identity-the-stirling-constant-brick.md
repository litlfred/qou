---
# qou-snpr
title: 'The brick that supplies the Stirling constant: prod_{j=1}^{N-1} 2 sin(j pi/N) = N'
status: todo
type: task
priority: high
tags:
    - lean
    - mathlib
    - c-sigma
    - one-loop
    - clausen
created_at: 2026-08-08T23:30:00Z
updated_at: 2026-08-08T23:30:00Z
---

## The statement

```lean
theorem prod_two_sin_pi_div (N : ℕ) (hN : 2 ≤ N) :
    ∏ j ∈ Finset.Icc 1 (N - 1), (2 * Real.sin ((j : ℝ) * Real.pi / N)) = N
```

equivalently `s_{N-1} = -log N`, where `s_k := -∑_{j=1}^k log(2 sin(j pi/N))`.

## Why this is the right brick, precisely

`QOU/Knot/FigureEightVolumeSqueeze.lean` proves the figure-eight volume
conjecture at LEADING order: `(2 pi/N) log(kashaev N) -> Vol(4_1)`. The tool is
`Clausen.abs_deviation_le`, which bounds

    |(pi/N) * sum_{j=1}^k log(2 sin(j pi/N))  -  (-clausen(2 k pi/N)/2)| <= masterErr N

with `masterErr N -> 0`. That is `s_k = (N/pi) Lambda(k pi/N) + O(log N)`.

The ONE-LOOP order needs

    s_k = (N/pi) Lambda(k pi/N) - (1/2) log(2 N sin(k pi/N)) + O(1/N)

and the correction term is ITSELF `O(log N)`. **So the existing bound is exactly
one order too coarse to see it.** Sharpening it is (A) of `qou-mlgp`.

This identity is the anchor of that sharpening: it is the exact endpoint value
that pins the constant, and it is where the `N` inside `log(2 N sin)` comes
from. Without it the refined expansion has an undetermined additive constant,
which is precisely the quantity `c_sigma(4_1) = 3^{-1/4}` depends on.

## Proof sketch

Let `zeta = exp(2 pi i/N)`. From `X^N - 1 = prod_{j=0}^{N-1}(X - zeta^j)`,
divide by `(X - 1)` and evaluate at `X = 1`:

    prod_{j=1}^{N-1}(1 - zeta^j) = N

Then `|1 - zeta^j| = 2 sin(j pi/N)` for `0 < j < N`, since
`|1 - e^{i t}|^2 = 2 - 2 cos t = 4 sin^2(t/2)`, and `sin(j pi/N) > 0` on that
range. Take absolute values.

## Mathlib API — DISCOVERED BY COMPILING, do not re-guess

EXISTS:

    Complex.isPrimitiveRoot_exp   (n : ℕ) → n ≠ 0 → IsPrimitiveRoot (cexp (2 pi I/n)) n
    X_pow_sub_one_eq_prod         0 < n → IsPrimitiveRoot zeta n →
                                  X^n - 1 = prod_{z in nthRootsFinset n 1} (X - C z)
    IsPrimitiveRoot.geom_sum_eq_zero
    Complex.normSq_apply          normSq z = z.re*z.re + z.im*z.im
    Real.sin_sq_eq_half_sub       sin x ^ 2 = 1/2 - cos (2x)/2      <- gives 4 sin^2(t/2) = 2 - 2 cos t

DOES NOT EXIST (checked, all `unknown constant`):

    IsPrimitiveRoot.prod_one_sub_pow
    Complex.abs_exp_mul_I,  Complex.abs_exp_mul_I_sub_one
    Complex.norm_exp_ofReal_mul_I_sub_one
    Real.cos_sq_half
    Real.log_eq_zero_iff        (use Real.exp_log + Real.exp_zero instead)

## Mathlib genuinely lacks this — it is an UPSTREAM contribution target

Confirmed by grepping declaration NAMES across all 6990 modules (see technique
below): no sine-product formula anywhere, and `prod_one_sub` over roots of unity
returns only `Finset.prod_one_sub_ordered`, which is unrelated. So

    prod_{k=1}^{n-1} sin(k pi/n) = n / 2^{n-1}

is missing from Mathlib outright. It is a classical, self-contained, widely
wanted identity — worth contributing upstream rather than burying in `QOU/`.

## SEARCH TECHNIQUE for a source-less Mathlib (reusable, worth knowing)

This repo's mathlib package is cache-only: `.lake/packages/mathlib/` contains
build artifacts and NO `.lean` source, so `grep` over Mathlib source fails
silently and looks like "Mathlib doesn't have it". It does not follow.

**`.ilean` index files carry declaration names.** So:

    cd .lake/packages/mathlib/.lake/build/lib/lean/Mathlib
    grep -roh '"[A-Za-z_.]*<pattern>[A-Za-z_.]*"' --include=*.ilean . | sort -u

finds declarations without source and without a compile cycle. Three earlier
`#check` guessing rounds this session would have been one grep.

## The route, now identified

`nthRootsFinset`'s API is thin — `card_nthRootsFinset`, `mem_nthRootsFinset`,
`nthRootsFinset_def`, and no image/bijection lemma — which is what makes the
finset surgery painful. The key that unlocks it is on the MULTISET side:

    IsPrimitiveRoot.nthRoots_eq :
      IsPrimitiveRoot zeta n -> alpha^n = a ->
        nthRoots n a = Multiset.map (fun x => zeta^x * alpha) (Multiset.range n)

At `alpha = a = 1` this IS the bijection `range n -> {zeta^j}`, as a multiset
equality — exactly what was missing. Plan:

  1. `nthRoots n 1 = Multiset.map (zeta ^ .) (Multiset.range n)`   [above]
  2. get `X^n - 1 = prod over that multiset of (X - C z)` — check for a
     multiset-valued form of `X_pow_sub_one_eq_prod` (grep `.ilean` for
     `prod_multiset_X_sub_C`)
  3. split off the `j = 0` factor `(X - 1)`, divide, evaluate at `X = 1`
  4. take `Complex.abs`, use `|1 - e^{i t}|^2 = 2 - 2 cos t = 4 sin^2(t/2)`
     via `Complex.normSq_apply` + `Real.sin_sq_eq_half_sub`

## The hard step, named in advance

Going from `X_pow_sub_one_eq_prod` to `prod_{j=1}^{N-1}(1 - zeta^j) = N` means
working with `nthRootsFinset` and removing the `j = 0` factor. That is the part
that will take the compile cycles; everything after it is routine. An
alternative worth trying first is differentiating `X^N - 1` at `X = 1`
(`N * 1^{N-1} = prod_{j != 0}(1 - zeta^j)`), which may avoid the finset surgery.

## Check the repo before starting

Not in qou: no theorem states this (`QOU/Knot/WhiteheadChainVolume.lean` has the
PARTIAL product `prod_{j in Icc 1 M} 2 sin(j pi/N)` as `whiteheadDen`, with
positivity but no closed form). Not in Mathlib. But grep again anyway —
this session added four duplicates by not doing so; see `qou-mlgp`.

## Definition of done

The theorem above, sorry-free, in `QOU/MathlibExt/` or beside
`QOU/Knot/Clausen.lean`, wired into `QOU.lean`. It does NOT by itself close
(A) — the refined Euler-Maclaurin still has to be done — but it is the piece
that makes the constant determinate rather than free.

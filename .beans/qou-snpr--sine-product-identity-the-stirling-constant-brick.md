---
# qou-snpr
title: 'The brick that supplies the Stirling constant: prod_{j=1}^{N-1} 2 sin(j pi/N) = N'
status: completed
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

## Progress 2026-08-08 — the hard half is BUILT

`QOU/MathlibExt/RootsOfUnityProduct.lean`, sorry-free on the three standard
axioms, wired into `QOU.lean`:

```lean
theorem prod_one_sub_nthRoots_erase_one {n : ℕ} (hn : n ≠ 0) :
    (Multiset.map (fun a : ℂ => 1 - a)
        ((Polynomial.nthRoots n (1 : ℂ)).erase 1)).prod = (n : ℂ)
```

This is the whole difficulty. The `nthRootsFinset` surgery the bean warned
about is AVOIDED entirely by the classical derivative trick:
differentiate `X^n - 1 = ∏(X - ζ)` and evaluate at the root `1`, which kills
every factor except those with `ζ ≠ 1`. `eval 1 (d/dX (X^n - 1)) = n`.

The step that made it work is `Polynomial.eval_multiset_prod_X_sub_C_derivative`,
found by the `.ilean` grep rather than by guessing — it is stated over
MULTISETS, so no finset bijection is ever needed.

Assembled from: `Complex.isPrimitiveRoot_exp`, `monic_X_pow_sub_C`,
`natDegree_X_pow_sub_C` (parameter is `r`, not `a`),
`IsPrimitiveRoot.card_nthRoots_one`,
`prod_multiset_X_sub_C_of_monic_of_roots_card_eq`, `mem_nthRoots`,
`eval_multiset_prod_X_sub_C_derivative`, `derivative_X_pow`.
`p.roots = nthRoots n 1` holds by `rfl`.

## What is left — the bookkeeping half

Converting the multiset product to the real sine form:

```lean
theorem prod_two_sin_pi_div (N : ℕ) (hN : 2 ≤ N) :
    ∏ j ∈ Finset.Icc 1 (N - 1), (2 * Real.sin ((j : ℝ) * Real.pi / N)) = N
```

needs (i) `(nthRoots N 1).erase 1 = Multiset.map (ζ ^ ·) (range N |>.erase 0)`
via `IsPrimitiveRoot.nthRoots_eq`, and (ii) `|1 - e^{iθ}| = 2 sin(θ/2)` from
`Complex.normSq_apply` + `Real.sin_sq_eq_half_sub`, then `Complex.abs` of the
identity above. Both are routine; neither is the difficulty that stalled this
bean.

## DONE 2026-08-08 — both halves built, sorry-free

`QOU/MathlibExt/RootsOfUnityProduct.lean`, three theorems, all on
`[propext, Classical.choice, Quot.sound]`, wired into `QOU.lean`:

```lean
prod_one_sub_nthRoots_erase_one : (map (1 - ·) ((nthRoots n 1).erase 1)).prod = n
prod_one_sub_zeta_pow           : ∏ j ∈ Ico 1 n, (1 - ζ^j) = n
prod_two_sin_pi_div             : ∏ j ∈ Ico 1 n, 2 sin(j π/n) = n     <- THE TARGET
```

Numerically confirmed afterwards at `n = 2,3,5,7,12,30` (exact to 1e-12), and
the endpoint consequence `s_{n-1} = -log n` likewise — i.e. the statement proved
is the statement wanted, not a vacuous or mis-indexed one.

**Both "hard steps" this bean warned about turned out not to exist.**

  * The `nthRootsFinset` surgery: avoided entirely by the derivative trick.
  * The injectivity needed to push `erase` through `map`: NOT needed —
    `Multiset.map_erase_of_mem` requires only membership, because multiset
    `erase` removes a single occurrence. `j ↦ ζ^j` is periodic and not
    injective, and that never mattered.

Both were found by grepping `.ilean` declaration names rather than guessing.
The two genuine snags were mundane: `natDegree_X_pow_sub_C` takes `r` not `a`,
and `simp` normalising `↑(2*x)` to `2*↑x` so that `exp_ofReal_mul_I_re` stopped
matching (fixed with `simp only` and an explicit lemma list).

## What this does and does not close

DOES: the additive constant in the `s_k` expansion is now pinned rather than
free — `s_{n-1} = -log n` is a theorem.

DOES NOT: `c_sigma(4_1) = 3^{-1/4}` is still not Lean-proved. That needs
`qou-mlgp` (A) the refined Euler-Maclaurin — sharpening
`QOU.Knot.abs_deviation_le` from `O(log N)` to `O(1)`, which is the step that
can actually SEE this constant — and (B) Laplace's method for a sum. This brick
is a prerequisite for (A), not a substitute.

Worth contributing upstream: Mathlib has neither this nor
`∏ sin(kπ/n) = n/2^{n-1}`, confirmed across all 6990 modules.


## CORRECTION 2026-08-08 — the `.ilean` technique covers only 42% of Mathlib

The search technique recorded above is useful but I OVERSTATED it, and the
overstatement propagated into two commit messages ("confirmed across all 6990
modules"). It is not true.

    .olean files : 6990
    .ilean files : 2946      = 42.1%

`.ilean` index files are NOT emitted for every module — e.g.
`Analysis/SpecialFunctions/Gaussian/PoissonSummation.ilean` does not exist while
its `.olean` does. **A negative result from an `.ilean` grep is therefore not
evidence of absence.** It searches under half the library.

### The reliable method: grep the `.olean` binaries

Declaration names appear as plain strings inside the compiled `.olean` files, so

    cd .lake/packages/mathlib/.lake/build/lib/lean/Mathlib
    grep -rla "<name-fragment>" --include=*.olean .
    strings <Module>.olean | grep -E '^[a-zA-Z][A-Za-z_.0-9]*$' | sort -u

covers 100% of modules. Sanity-checked: it finds `sin_pos_of_pos_of_lt_pi`
where it should. Use `.ilean` for fast positive hits, `.olean` before ever
claiming absence.

### The conclusion itself survives — re-checked at full coverage

`prod_two_sin`, `prod_sin_pi_div`, `gaussianSum`, `tsum_exp_neg_mul_sq`: all
absent from all 6990 `.olean` files. So Mathlib really does lack the
sine-product formula and this really is an upstream contribution target. The
claim was right; the evidence I cited for it was not.

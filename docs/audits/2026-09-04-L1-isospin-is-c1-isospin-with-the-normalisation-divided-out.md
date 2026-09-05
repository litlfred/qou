# `L1` is not a new coincidence — it is `c₁`'s isospin term with the normalisation divided out

**Follows up** the log-ratio audit, which reported
`L1 = 2·(i_nn − i_pp)` as *"pattern-matched on six points, not derived"* and
named deriving it as the highest-value next step. This reduces it to the
already-verified `c₁` closed form plus **one** simpler observed identity.
Beans `qou-brng` / `qou-pdg9`.

## The split

Writing `tr_free = f₀ + f₁ε + …`, `tr_atom = a₀ + a₁ε + …`, the two
first-order logarithmic derivatives are, **exact on all six cases**:

    f₁/f₀ = (21Z + 16N)/2
    a₁/a₀ = (21Z + 16N)/2 + 2(i_pp − i_nn)

with `i_pp = max(Z−1,0)`, `i_nn = max(N−1,0)` (chain-interface counts).

    case  Z  N    f1/f0  predicted    a1/a0  predicted
    pp    2  0      21      21          23      23
    pn    1  1    37/2    37/2        37/2    37/2
    nn    0  2      16      16          14      14
    T     1  2    53/2    53/2        49/2    49/2
    3He   2  1      29      29          31      31
    4He   2  2      37      37          37      37

Hence directly `L1 = f₁/f₀ − a₁/a₀ = −2(i_pp − i_nn) = 2(i_nn − i_pp)`.

## The consistency check that makes this a reduction rather than a second pattern

`f₀ = 2^{−A}` and `a₀ = 2^{1−2A}` are the **proved** `c₀` structure. Feeding the
split above through them:

    f₁ − a₁ = (21Z+16N)·2^{−A−1} − (21Z+16N)·2^{−2A} − 4(i_pp−i_nn)·2^{−2A}
            = (21Z+16N)(2^{−A−1} − 2^{−2A}) − 4(i_pp−i_nn)·2^{−2A}

which is **exactly the independently-verified `c₁` closed form** (#6492), and it
reproduces all six recorded values on the nose:

    pp 19/8    pn 37/16   nn 9/4   T 163/64   3He 85/32   4He 259/128

So the split is not a second free-floating pattern fitted alongside the first.
Given `c₁`'s closed form, `a₁` is **determined** by `f₁` (`a₁ = f₁ − c₁`), so the
only new empirical input in this whole document is the single identity
`f₁/f₀ = (21Z + 16N)/2`.

## What that buys — the structural point

**`L1` and `c₁` carry the same isospin object.** In `c₁` it appears as
`−4(i_pp − i_nn)·2^{−2A}`; in `L1` as `2(i_nn − i_pp)`. Same term, differing by
the factor `2^{−2A}` — which is exactly `a₀`, the atom-side normalisation that
the log-ratio divides out and the difference does not.

That answers *why* `L1` has no A-dependence, which the previous audit could only
report as an observation: **the A-dependence of the isospin term in `Δtr` is
normalisation, not content.**

**And it cuts against the replacement law, not for it.** In `Δtr` the isospin
term is suppressed by `2^{−2A}` — drowned at large A. In `log(tr_free/tr_atom)`
it survives at full strength, `O(1)` and A-independent. So the log-ratio
*promotes* the isospin term from negligible to first-order — and that term has
the **wrong sign** (#6611: *"the derived isospin asymmetry has the wrong sign"*;
mechanism in the previous audit). Taking the log-ratio therefore does not merely
inherit the defect, it **amplifies** it from `O(2^{−2A})` to `O(1)`.

## Scope, and what is NOT established

- **`f₁/f₀ = (21Z+16N)/2` is still observed, not derived** — six cases, A ≤ 4.
  It is a simpler and more natural statement than the `L1` pattern it replaces,
  and it is the *only* remaining empirical input, but it is not proved. A
  derivation of it would close the chain.
- **This is a reduction, not a proof of `L1`.** The claim is that `L1` follows
  from `c₁` + `c₀` + one identity — not that `L1` is proved from first
  principles.
- **`c₁`'s own closed form is verified, not proved.** It is #6492's result,
  checked here against all six recorded values; its provenance is theirs.
- **Six cases, A ≤ 4, Z ≤ 2, N ≤ 2.** The `21` and `16` are per-nucleon
  coefficients seen only in this range; nothing here tests them at A ≥ 5.
- **No claim about the physics.** Whether the amplification argument above
  matters for the binding law is #6611's question; this establishes the
  algebraic fact, not its consequence for the fit.
- **Scope-(a)** throughout.

## Method

Log-derivatives taken from the `P = 5`/`P = 6` series runs recorded in the
log-ratio audit; all arithmetic in exact `Fraction`. Both the split and the
`c₁` reproduction were checked on all six cases; neither is a spot check.

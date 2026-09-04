# What `L` is, and what "retiring" it would actually cost

**Date:** 2026-09-04 · **Bean:** `qou-qnqf` · **Scope:** identification plus an
inventory. Nothing renamed, nothing deleted, nothing wired. This is the reading
that has to happen before anyone decides to retire `B = alpha L`.

## `L` is a free-energy difference, exactly

The Markov trace under convention D is a **state sum**. On `H_2` the two
Wedderburn blocks `(2)` and `(1,1)` carry Wenzl weights

    w+ = [3]_q / ([3]_q + 1) = 0.752702113
    w- = 1     / ([3]_q + 1) = 0.247297887
    w+ + w- = 1     (exactly; `wPlus_add_wMinus` in QOU.Mass.ChainTraceFactor)

so `w` is a genuine probability measure on the blocks, and `sigma` acts by the
block eigenvalues `q` on `(2)` and `-1/q` on `(1,1)`. The two-strand trace of an
interface letter is therefore an expectation,

    tr_2(sigma + d)  =  E_w[ lambda + d ]  =  z + d,     z = q^3/(q^2 + 1),

which reproduces all three bond constants exactly:

| bond | `d` | `E_w[lambda + d]` | `-log` |
|---|---|---|---|
| pp | `0` | 0.612688037146 | 0.489899384255 |
| nn | `-h` | 0.403627738351 | 0.907262265533 |
| pn | `d_pn` | 0.508229789377 | 0.676821592386 |

Since `qou-m3sh` proved the chain's Markov trace is exactly the product of these
per-interface factors (`~1e-59`), the quantity the binding arc has been
computing is

    L  =  log( Z_free / Z_bonded )  =  sum over interfaces of  -log E_w[lambda + d]

i.e. **a free-energy difference in the standard sense** — dimensionless, in
units of `kT` — between the unbonded and bonded state sums. Per-interface,
additive, and positive, since every factor `z + d` lies in `(0, 1)` at `q_0`.

That is a real, canonical, exactly-computable quantity. It is not wrong and it
should not be deleted. What is in question is only the identification
`B = alpha L` as a binding **energy**.

### One caveat that matters

The observable is **signed**: the `(1,1)` eigenvalue is `-1/q = -0.900918`. So
this is the free energy of a signed observable over a quasi-probability, not of
a positive one — and the sign is exactly the `sigma` / `sigma^-1` split, which
is the p/n distinction itself. Convexity intuitions imported from ordinary
statistical mechanics need checking rather than assuming, which is precisely the
lesson of `qou-mu1h`'s Jensen argument.

## What retiring `B = alpha L` would cost

Measured on `origin/main`:

| surface | count |
|---|---|
| Python files referencing the bond constants or `B_chain` / `B_allpairs` / `B_sym` | **80** |
| of which probes | **61** |
| witness JSON files | **31** |
| exposition blocks | **6** |

That is not a small cleanup, and it changes the calculus. "Retire `L`" was
proposed in `qou-qnqf` as the honest option after six consecutive negatives; the
inventory says it is also the expensive one.

**But the expense is avoidable, because retiring the interpretation is not
retiring the quantity.** `L` remains a correct free-energy difference in all 80
files. Only the sentence "and this is the binding energy" is in question. The
minimal honest action is therefore a re-labelling, not a deletion:

- keep every computation of `L` as-is;
- mark the `B = alpha L` identification as an open interpretation rather than a
  result, in the six exposition blocks and wherever a probe compares `alpha L`
  to AME;
- leave the numbers standing, since they are correct free energies.

## What survives regardless of the decision

None of these depend on `B = alpha L` being a binding energy:

- the connected-sum theorem and its contrapositive (`qou-m3sh`, `qou-bygw`);
- the affine interface law `tr_2(sigma + d) = z + d` and the closed forms
  `L_pp = -log z`, `L_nn = log(q(q^2+1))`, `L_pp + L_nn = 2 log[2]_q`
  (`QOU.Mass.ChainTraceFactor`, sorry-free);
- the Fary-Milnor curvature floor `2 pi (2A+1)` and the Frenet-framing jump
  (`qou-m3sh`);
- the ordering ambiguity of the all-pairs word (`qou-bygw`), which is a
  statement about links, not energies.

## Recommendation

Do not delete. Re-label the interpretation in the six exposition blocks and
mark the probes that compare `alpha L` to AME, and record `L`'s identification
as a free-energy difference so the quantity keeps a correct name. Whether the
framework wants a different binding channel is a separate decision and is not
made here.

## Status

- [x] Say what `L` is: a free-energy difference between unbonded and bonded
      Markov state sums, per-interface additive, over a signed observable.
- [x] Inventory the dependency surface: 80 Python files, 61 probes, 31
      witnesses, 6 exposition blocks.
- [ ] The re-labelling itself, which is a decision for the owner, not a
      computation. `B_sym` and the `t7qv` / `qou-brng` numbers stay correct as
      free energies either way.

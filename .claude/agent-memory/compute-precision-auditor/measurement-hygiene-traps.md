# compute-precision-auditor — detail file: measurement-hygiene traps

Read on demand. Summarised in `MEMORY.md`; this file carries worked cases.
Every trap below is one I actually fell into during bean `t7qv`
(2026-08-31/09-01) and caught before or shortly after publishing. Each cost a
wrong claim that had to be withdrawn.

## TRAP — `abs(x) > tol` on a quantity with a PROVEN sign

**Worked case.** The aggregation gap `free - atom` is `>= 0` structurally,
because aggregation is a relaxation and `x_p + x_n` is an explicit feasible point
of the aggregate with cost exactly `free`. I detected "gap opens" with
`abs(gap) > 1e-9`. What that caught was a run of **negative** gaps at
`-1.79e-11`, `-1.79e-10`, `-1.79e-9` — structurally impossible, i.e. LP solver
noise scaling with the perturbation. I reported a knife-edge radius of `3e-8`
off the back of it. There was no knife edge at that radius; along that direction
the gap never opened at all, even at a 63 % perturbation of the cost.

**Rule.** If you can prove a sign, assert the sign. `gap > tol`, never
`abs(gap) > tol`. And count the sign violations you see — if a "structurally
impossible" value shows up at all, that is your noise floor announcing itself,
and it is far above machine epsilon.

The corrected measurement (positive-only, relative threshold) found zero spurious
negatives and a real boundary established by **linear scaling over six decades**
(`gap/eps` constant to `< 5e-8` from `1e-1` down to `1e-6`) rather than by a
radius. A scaling law is a much stronger boundary claim than a threshold
crossing.

## TRAP — single-root bisection on a function that has 0 or 2 roots

**Worked case.** I located dual-vertex transitions by bisecting the margin over
`h in [0.02, 3]`, assuming one sign change. For one parameter choice the margin
has **no** root in that range and the bisection returned `h* = 2.0009` — a
number with no meaning, which I then tabulated alongside real ones and used to
claim a non-monotonicity.

**Rule.** Scan a grid for sign changes FIRST, bisect only inside a bracketed one,
and return `None` when there is no bracket. Report the bracket count. The
committed probes do this and the proton/neutron values were never affected — but
only because they happen to have a single crossing each, which I had not checked.

## TRAP — a linear solve that is not verified is not a solve

**Worked case.** Solving `v_n . W = v_p` for the weak transition operator, I built
the matrix of right-multiplications and used `lu_solve(M.T, ...)`. The relation
is `v_n . W = sum_k W_k (v_n . b_k)`, so the columns must be `v_n . b_k` — the
transpose was simply wrong. It produced a plausible-looking six-component `W`,
whose verification residual was `1.3e-1`. Corrected, it is `1.15e-41`.

**Rule.** Every solve gets a residual printed next to its answer, always. A
wrong answer to a linear system looks exactly like a right one.

## TRAP — assertion thresholds that encode your PROSE rather than your finding

Three separate probes failed on my own thresholds while the underlying
measurement was correct:

* asserted the saturation spread was `< 5e-4`; it is `5.9e-4`;
* asserted all-pairs is `4x` less ordering-sensitive; it is `3.4x` and `3.7x`;
* asserted `b_2` dominates by `> 3x` at both nucleons; it is `8.1x` at the proton
  and `1.9x` at the neutron.

Each time the sentence had been written before the number was read back.

**Rule.** Write the assertion from the printed value, not from the sentence you
intend to write about it. And when a threshold fails, check which of the two is
wrong before touching either — twice it was the prose, once (the monotonicity
check) it was a sort whose tie-break silently inverted the comparison.

## TRAP — a container reset can move you to a DIFFERENT BRANCH silently

**Worked case, and this one nearly produced two fabricated defect reports.** A
mid-session container reset dropped me from
`claude/mt7r-archimedean-eval-2026-08-24` onto
`claude/omegaorder-exponent-group-2026-08-16`. Same probe, same inputs, different
`pyhecke`: a transition I had measured at `0.477184636796` came back
`0.679319435`, and `atom_gen_chains` open-coded `-h/2` where my branch has
`D_PN`. I was one step from filing both as bugs.

**Rule.** After any reset — and the tell is `ModuleNotFoundError` on `mpmath`,
since the reset also wipes `pip install` — run `git branch --show-current` before
running anything else. If a previously-measured number changes, suspect the
checkout before suspecting the code.

## TRAP — `--depth=1` poisons `merge-base` and every ancestry count

Recovering the branch after that reset, I used `git fetch --depth=1`. The repo
stayed shallow (4 grafts) and afterwards `git merge-base HEAD origin/main`
returned **empty**, while `git rev-list --left-right --count` reported `7` vs
`33685` — both meaningless. Substituting an empty merge-base into
`git log -1 $(...)` silently reports `HEAD` instead, which is how the number
looked plausible.

**Rule.** `test -f .git/shallow` before trusting any ancestry command.
`git fetch --unshallow` first. The true counts here were `119` vs `1343`.

## NOTE — the `y_lambda` tables are stored f64, and that sets a floor

Agreement between anything routed through `nucleus_real_sdp.load_cost` and an
independent computation bottoms out around `1e-8`, not machine epsilon. Measured:
`6.1e-9` on the deuteron free trace against `tr_3(p) tr_3(n)`, and `5.6e-9`
between two determinations of `L_pn`. `h3a_frobenius_gram_offdiagonal_probe` sees
the same `1.1e-8` scale. Quote seven digits from that path, not fourteen, and do
not read a `1e-9` residual there as a defect.

By contrast, quantities computed entirely within one route reach machine
epsilon — the chain transfer scalar `F` is prefix-independent to `2.8e-16`, and
bond constants measured as `H_6`/`H_9` trace ratios agree with the closed form
`-log(z + d)` to `1.3e-13`. Knowing which floor applies to which number is the
difference between reporting a cross-check and reporting a discrepancy.

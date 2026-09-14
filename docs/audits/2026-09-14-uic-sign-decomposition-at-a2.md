# The ungated UIC sum by sign: at A = 2 the positive mass vanishes

**Date.** 2026-09-14  **Bean.** `qou-21oc` (stays OPEN)
**Probe.** [`computations/probes/uic_sign_decomposition_probe.py`](../../computations/probes/uic_sign_decomposition_probe.py) — 12/12
**Witness.** `computations/probes/uic-sign-decomposition.witness.json`

## What was asked

The Pass-2 sign gate was dropped on 2026-09-12 (owner ruling; its
complementary-slackness justification refuted sorry-free in PR #7251), and
`hecke_core_legacy.unified_iterative_correction` now sums over every enumerated
partition. The total is still wrong-signed against AME2020, and dropping the
gate moved it *further* from the data. `qou-21oc` asks why.

## What is summed

$$S \;=\; \sum_\lambda C_\lambda\, L_\lambda, \qquad
  L_\lambda \;=\; \ell_\lambda + \ln\lvert t_\lambda\rvert - \ln d_\lambda$$

where $(t_\lambda, \ell_\lambda)$ are the final trace and the **accumulated
log** returned by `lp_accumulator_step_traces_mpfr`, and
$C_\lambda$ is `C_lambda_resolvent_MeV`.

The $\ell_\lambda$ is easy to drop and matters: $L_\lambda$ is **not**
$\ln\lvert\mathrm{tr}\rvert - \ln d$. An earlier framing of this quantity that
omitted it is withdrawn. Since $C_\lambda \ge 0$, we have
$\operatorname{sign}(\text{term}) = \operatorname{sign}(L_\lambda)$, so "why is
$S < 0$" is exactly "why does the negative-$L$ mass outweigh the positive-$L$
mass".

## The decomposition

Writing $P$ for the mass on blocks with $L > 0$ and $N$ for the mass on blocks
with $L < 0$, at cap $\lvert\lambda\rvert \le 6$:

| atom | $P$ | $N$ | $S = P + N$ | $\lvert N\rvert / P$ | $n_+$ | $n_-$ | top-1 share of $\lvert N\rvert$ |
|---|---|---|---|---|---|---|---|
| ²H | $0$ | $-2.251132$ | $-2.251132$ | — | 5 | 23 | 15.2 % |
| ³H | $0.06637092$ | $-1.869988$ | $-1.803617$ | 28.18 | 6 | 22 | 16.9 % |
| ³He | $0.07795215$ | $-1.824545$ | $-1.746593$ | 23.41 | 6 | 22 | 19.3 % |
| ⁴He | $0.06897519$ | $-1.439094$ | $-1.370119$ | 20.86 | 7 | 21 | 16.2 % |
| ⁶Li | $0.02960591$ | $-1.999284$ | $-1.969678$ | 67.53 | 6 | 22 | 20.1 % |

No single block carries more than 20.1 % of $\lvert N\rvert$, so the sign is
not one outlier and cannot be repaired by fixing one partition.

## The result at A = 2

At ²H the positive mass vanishes, and it is not a low-truncation artifact:

| cap $\lvert\lambda\rvert$ | partitions | blocks with $L>0$ | all one-dimensional | all zero-weight | $P$ | $S$ |
|---|---|---|---|---|---|---|
| $\le 6$ | 28 | 5 | yes | yes | $0$ | $-2.251132$ |
| $\le 8$ | 65 | 7 | yes | yes | $-6.3\times10^{-74}$ | $-5.721795$ |
| $\le 10$ | 137 | 9 | yes | yes | $-9.6\times10^{-74}$ | $-12.46904$ |

Every block with $L > 0$ at ²H is a one-dimensional **row** partition $(k)$ —
and those are exactly the blocks the weight annihilates. The mechanism is
already in the corpus:
[`prop:unified-iterative-correction`](../../content/quantum-observable-universe/mass-theory/unified-iterative-correction.md)
states that the subtrahend $1/[k]_q!$ equals $\min_\lambda (w_\lambda/d_\lambda)$,
so it kills the one-dimensional blocks $(k)$ and $(1^k)$ at every level and
nothing else.

**What is new is not the mechanism but the coincidence:** at $A = 2$ the
annihilated set and the positive-$L$ set are the same set, so $S < 0$ is
*forced* rather than observed.

### "Vanishes", not "is exactly zero"

$P$ is zero to the precision of the arithmetic, about 74 orders of magnitude
below $\lvert S\rvert$ ($\max \lvert P\rvert/\lvert S\rvert = 1.10\times10^{-74}$),
and that is the strongest form in which this computation establishes it.

Of the 28 one-dimensional blocks in the table, **16 carry $C_\lambda$ exactly
$0$ and 12 carry a residue at $\sim 10^{-74}$**, some of it *negative* — which
is why $P$ comes out as a small negative number rather than a small positive
one. That is the signature of an **exact cancellation evaluated at 70 dps**: a
difference of two equal quantities computed to finite precision lands on the
floor, not on zero. It is consistent with the corpus's exact claim about the
subtrahend, and it is not a substitute for it.

Two consequences stated rather than left implicit: $C_\lambda \ge 0$ holds *to
tolerance* $10^{-40}$ and is **not** established exactly here; and an assertion
written as `P == 0` fails at caps 8 and 10. The probe's first draft made
exactly that mistake and the re-run caught it.

## Scope: (a), not (b), and it does not generalise

1. **Measured, not proved.** Verified at caps 6, 8, 10. The implication
   $L_\lambda > 0 \Rightarrow \lambda$ one-dimensional is not established for
   all $k$. This is a **scope-(a)** negative in the sense of AGENTS.md
   §"Before declaring refuted": it constrains this construction at this atom,
   and excludes no ingredient.
2. **False at $A \ge 3$.** At ⁴He and ⁶Li the blocks $(2,1)$ and $(2,2)$ carry
   $L > 0$ **and** $C > 0$, so $P > 0$ — merely 21–68× too small. The probe
   asserts this explicitly so the ²H headline cannot be read as general. **The
   A ≥ 3 sign remains unexplained**, which is why `qou-21oc` stays open.
3. **This is the probe's own reconstruction**, over $\lvert\lambda\rvert \le$ cap
   with ordering `["p"]*Z + ["n"]*N` — *not* the producer's return. Validated
   where they agree: cap $\le 6$ gives $-2.251132$ against the producer's
   $k = 6$ row $-2.251131977321312$. Do not quote these sums as
   `unified_iterative_correction` values.

### What would make it scope-(b)

A proof that $L_\lambda(A{=}2) > 0 \Rightarrow \lambda \in \{(k), (1^k)\}$.
Then the positive set is contained in the annihilated set for every $k$, and
$S < 0$ at deuterium becomes a structural exclusion rather than a measurement.
This is a small, well-posed formalize-first target.

## A separate observation: no evidence of convergence

The ungated ²H sum grows monotonically in magnitude with the truncation:

| $k$ | 4 | 5 | 6 | 8 | 10 | 11 |
|---|---|---|---|---|---|---|
| $S$ | $-0.412$ | $-1.227$ | $-2.251$ | $-5.722$ | $-12.469$ | $-17.691$ |
| ratio | — | ×2.98 | ×1.83 | ×2.54 | ×2.18 | ×1.42 |

($k = 4, 5, 11$ from the producer docstring; $6, 8, 10$ measured here.)

The producer already warns that this quantity spans 43× across tiers and that a
bare figure is meaningless without its tier. What this adds is that the growth
shows **no sign of a limit over the measured range**, which would mean the
production $k = 11$ value is not a converged quantity but wherever the
truncation stopped.

**This is deliberately not a divergence claim.** Six points cannot establish
one. Settling it needs $k = 12 \ldots 15$ (the partition table reaches
$\lvert\lambda\rvert = 15$).

## Not the entanglement result

[`computations/meson/binding_cut_entropy_sign_is_forced_probe.py`](../../computations/meson/binding_cut_entropy_sign_is_forced_probe.py)
also concludes "the sign is forced", about a **different** quantity —
entanglement entropy across the proton|neutron cut, where non-negativity is a
theorem. The two results are unrelated and are cross-referenced here only so a
reader does not conflate them.

## Anti-fit note

Nothing here is fitted, and nothing is tuned. The decomposition is a
partition of an existing sum; no parameter was chosen, no truncation was
selected for accuracy, and the honest negative (that $A = 2$ does not
generalise) is asserted in the witness alongside the positive finding.

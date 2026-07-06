# Volume + Shell w_λ^(1) probe — simple Plancherel ansatz fails

**Pair:** [`volume_shell_w_lambda_level1_probe.py`](../../computations/volume_shell_w_lambda_level1_probe.py)
+ witness [`2026-05-02-w-lambda-level1-probe.witness.json`](2026-05-02-w-lambda-level1-probe.witness.json).

## Tested ansatz

The simplest shell-aware level-1 weight that follows from
`conj:categorical-neutrality-saturated-shells` is the Plancherel
weight restricted to self-conjugate partitions:

$$
w_\lambda^{(1)} \;=\; \frac{\dim_q(\lambda)^2}{[n]_q!} \cdot \delta_{c(\lambda) = 0}
$$

Level-1 contribution to atom $(Z, N)$ at strand count $n = 3A$:

$$
\mathfrak{m}^{(1)}(Z, N) \;=\; \sum_{\substack{\lambda \vdash 3A \\ c(\lambda) = 0}} w_\lambda^{(1)} \cdot \chi^\lambda_{q=1\,\mathrm{MN}}(W_{\mathrm{atom}})
$$

## Result

| atom | $A$ | $3A$ | self-conj $\lambda$ | $\|m^{(1)}\|$ |
|------|----:|----:|-----------------:|------------------:|
| D | 2 | 6 | 1 | 0 |
| 3He | 3 | 9 | 2 | $5.87 \times 10^{-3}$ |
| 3H | 3 | 9 | 2 | $5.87 \times 10^{-3}$ |
| **4He** | **4** | **12** | **3** | **0** |
| 6Li | 6 | 18 | 5 | 0 |
| 9Be | 9 | 27 | 14 | $1.78$ |
| 12C | 12 | 36 | 33 | $0.135$ |
| **16O** | **16** | **48** | **87** | **0** |

Correlation with AME binding-per-nucleon: **+0.246** (weak).

## Diagnosis: cancellations in the MN character

The zeros at D, 4He, 6Li, 16O are NOT from missing partitions —
they have 1, 3, 5, 87 self-conjugate partitions respectively. The
zeros come from **MN character cancellations**: at $q = 1$, the
characters $\chi^\lambda_{\mathrm{MN}}(W_{\mathrm{atom}})$ for
different self-conjugate $\lambda$ partially cancel when summed
with positive Plancherel weights.

Specifically: a self-conjugate $\lambda$ has $\lambda = \lambda'$
(its own conjugate). Under the q=1 MN character, $\chi^{\lambda}
= \mathrm{sgn}(\sigma) \cdot \chi^{\lambda'}$ on certain
permutation classes — and self-conjugacy implies pair
cancellations in the weighted sum.

## What this rules out

The simple ansatz $w_\lambda^{(1)} = w_\lambda^{(0)} \cdot
\delta_{c(\lambda) = 0}$ at the q=1 MN character level **does
not** capture binding-energy structure. Three corrective paths:

1. **q-deformed character** instead of MN. The full Hecke
   character $\chi^\lambda_q$ depends on $q$; the cancellations
   at q=1 may not survive the q-deformation. Implementation
   exists in `hecke_character_q_deformed.py`. Likely the right
   next step.

2. **BB-spectral-sequence weight** instead of bare Plancherel.
   `conj:homological-shell-condensation` says the level-1 weight
   should include a factor that vanishes off the BB-saturated
   stratum. The proper weight is more refined than the bare
   Plancherel restriction.

3. **Different shell predicate** instead of $c(\lambda) = 0$. The
   self-conjugate condition is necessary but possibly not
   sufficient; perhaps a stronger predicate (e.g., $\lambda$
   admits an $\mathfrak{S}_2$-fixed Frobenius core) would
   eliminate the cancelling characters.

## What this confirms

The problem IS shell-saturation-driven: only partitions with
$c(\lambda) = 0$ contribute structurally. The cancellation at
4He/16O suggests these magic atoms have a SYMMETRIC distribution
of self-conjugate $\lambda$ contributions that cancel in the q=1
limit — but a q-deformation should break the cancellation.

## Status

Negative result for the simplest level-1 weight ansatz. The
hypothesis that level-1 lives on self-conjugate $\lambda$ is
supported (by structural argument from
`conj:categorical-neutrality-saturated-shells`), but the
character-q=1 + bare-Plancherel combination cancels too much.

**Next step (deferred):** repeat with `q_mn_character` from
`hecke_character_q_deformed.py` (full q-deformed Hecke
character) to break the q=1 cancellations. This is research-
level work that ties to the q-ribbon-tableau approach in PR
#499's queued R1.

The Volume + Shell derivation as a closed-form formula remains
**open** at the framework level; only direct BB-spectral-
sequence work (per `conj:homological-shell-condensation`) is
likely to close it from first principles.

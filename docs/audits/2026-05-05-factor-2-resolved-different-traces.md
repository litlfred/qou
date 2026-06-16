# Factor-of-2 normalization mismatch — resolved as DIFFERENT TRACES

**Date:** 2026-05-05
**Branch:** `claude/categorical-mass-divergence-audit` (PR #534)
**Refs:**
- [`computations/factor_2_normalization_trace_probe.py`](../../computations/factor_2_normalization_trace_probe.py)
- [`computations/factor-2-normalization-trace.witness.json`](../../computations/factor-2-normalization-trace.witness.json)
- [`prop:categorical-mass-markov`](../../content/quantum-observable-universe/braids-and-knots/categorical-mass-markov.md)
- Sibling [PR #546](https://github.com/litlfred/qou/pull/546) — closed-form trace

## Resolution

The "factor of 2 normalization mismatch" between PR #546's `tr_M_symbolic` and char_fast + Plancherel-Markov-axiom convention is **not a normalization issue** — they compute **different categorical traces**.

### Per-irrep weight comparison at $q_0$

| $\lambda \vdash 3$ | $f^\lambda$ | $w_\lambda^{(\text{PR #546})} = \dim_q^2 / [n]_q!$ | $w_\lambda / f^\lambda$ | $y_\lambda^{(\text{char fast})}$ | ratio |
|:---:|:---:|---:|---:|---:|---:|
| $(3)$ | $1$ | $0.1634$ | $0.1634$ | $0.4154$ | $2.54$ |
| $(2, 1)$ | $2$ | $0.6607$ | $0.3303$ | $0.2809$ | $0.85$ |
| $(1, 1, 1)$ | $1$ | $0.1634$ | $0.1634$ | $0.0227$ | $0.14$ |

The ratios are not equal — **not a uniform rescaling**. The two conventions disagree per irrep.

### The two traces

**PR #546's trace.**
$$\mathrm{tr}_M^{(\text{PR #546})}(\beta) \;=\; \sum_\lambda \frac{\dim_q^2(\lambda)}{[n]_q!} \cdot \frac{\chi^\lambda(\beta)}{f^\lambda}.$$

This is the **Plancherel/regular trace** on the Hopf algebra $H_n(q)$. It does **not** satisfy the Markov stabilization axiom $\mathrm{tr}(\beta \cdot \sigma_n) = z \cdot \mathrm{tr}(\beta)$, only normalizes correctly at $q = 1$ (where it gives $\mathrm{tr}(1) = (\dim^2 \text{sum}) / n! = 1$).

At general $q$, $\mathrm{tr}_M^{(\text{PR #546})}(1) = (2 + [2]_q^2) / [3]_q! \approx 0.987$ at $q_0$ (not $1$).

**char_fast's trace.**
$$\mathrm{tr}_M^{(\text{Markov})}(\beta) \;=\; \sum_\lambda y_\lambda \cdot \chi^\lambda(\beta),$$
where $y_\lambda$ is solved from the **Markov-axiom system**:
$$\{\mathrm{tr}_M(1) = 1, \;\;\mathrm{tr}_M(\sigma_1) = z, \;\;\mathrm{tr}_M(\sigma_1 \sigma_2) = z^2\}, \qquad z = 1/(q^{1/2} + q^{-1/2}).$$

This is the **Hoefsmit-Wenzl Markov trace**, the canonical knot invariant satisfying Markov stabilization.

### Trace comparison on test braids

| Braid | PR #546 $\mathrm{tr}$ | char_fast $\mathrm{tr}_M$ | ratio |
|:---|---:|---:|---:|
| identity | $0.9874$ | $1.0000$ | $1.013$ |
| $\sigma_1$ | $0.1032$ | $0.4993$ | $4.84$ |
| $\sigma_1^2$ | $1.0090$ | $1.1044$ | $1.09$ |
| trefoil $\sigma_1^3$ | $0.3142$ | $0.7302$ | $2.32$ |

Ratios vary across braids — **convention difference is per-irrep**, not a uniform scale.

## Implication for the categorical-mass program

`prop:categorical-mass-markov` defines the categorical mass via the **Markov trace** (the descended Frobenius integral on $H_n(R, q)$):
$$\mathfrak{m}_{q, K}|_{\text{single level}} \;=\; \bigl|\!\int_A\! \rho(\beta_K)\!\bigr| \;=\; |\mathrm{tr}_M(T_w)|.$$

This is the **Markov trace**, not the Plancherel trace. PR #546's closed-form $\mathrm{tr}_M(\mathrm{proton}) = (q^{20} + q^{18} + 2q^{12} - 2q^{8} - q^{2} - 1) / (12 q^{10})$ represents the **Plancherel trace** on the proton braid, not the Markov trace required by the categorical mass identity.

To use PR #546's closed form for the dimensional bridge $E_0/\alpha$:
1. Either **convert** their Plancherel trace to the Markov trace by re-weighting the per-irrep contributions
2. Or **rederive** the closed form using the Markov-axiom-normalised weights $y_\lambda$

The conversion: given PR #546's per-irrep characters $\chi^\lambda(\mathrm{proton})$, the Markov trace is
$$\mathrm{tr}_M^{(\text{Markov})}(\mathrm{proton}) \;=\; \sum_\lambda y_\lambda \cdot \chi^\lambda(\mathrm{proton}),$$
with $y_\lambda$ determined by Markov axioms (not $w_\lambda / f^\lambda$).

## Implication for `prop:markov-trace-antipode-polynomial-symmetry`

The polynomial identity $q^{20} p(1/q) = -p(q)$ I proved in PR #534 holds for **PR #546's specific Plancherel-trace closed form**, not for the canonical Markov trace. This needs to be reflected in the proposition's statement:

> **Updated statement:** The polynomial $p(q)$ is the numerator of the Plancherel-weighted trace $\sum_\lambda (\dim_q^2 / [n]_q!) \cdot \chi^\lambda(\mathrm{proton}) / f^\lambda$ in $H_3(q)$. It satisfies the anti-self-reciprocity identity $q^{20} p(1/q) = -p(q)$, equivalently $\mathrm{tr}^{\mathrm{Plan}}(\mathrm{proton})(1/q) = -\mathrm{tr}^{\mathrm{Plan}}(\mathrm{proton})(q)$.

The categorical interpretation via Hopf antipode descent is unchanged — both Plancherel and Markov traces descend through the antipode — but the polynomial form is convention-specific.

## Action items for #534 + #546 coordination

1. **PR #546**: clarify in their closed-form derivation whether they intend Plancherel or Markov trace. The closed form $p(q) / (12 q^{10})$ is the Plancherel trace; deriving the **Markov** trace closed form would require Markov-axiom-determined weights $y_\lambda$.
2. **PR #534**: update `prop:markov-trace-antipode-polynomial-symmetry.md` to specify Plancherel convention.
3. **Both**: post-resolution, the dimensional bridge $E_0/\alpha$ requires the Markov-trace closed form (per `prop:categorical-mass-markov`), so PR #546's eventual Markov-normalised closed form is the actual anchor.

## Open question

What is the **Markov-trace closed form** for the proton in $H_3(q)$? Using char_fast's $y_\lambda$ and PR #546's per-irrep characters:
$$\mathrm{tr}_M^{(\text{Markov})}(\mathrm{proton})(q) \;=\; y_{(3)} \cdot \chi^{(3)} + y_{(2,1)} \cdot \chi^{(2,1)} + y_{(1,1,1)} \cdot \chi^{(1,1,1)}$$
where $y_\lambda$ are Markov-axiom-determined functions of $q$. Their symbolic forms (closed in $q$) need to be extracted from the Markov-axiom system at general $q$, not just numerically at $q_0$.

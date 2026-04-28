**Proposition (Shannon: Jones--Markov measure no-go).**

*Let $y_\lambda(q) \cdot d_\lambda$ denote the canonical
"Jones--Markov $\times$ dimension" candidate for the Shannon-conjecture
probability measure $p_q$ on partitions $\lambda \vdash n$
([Shannon conjecture](#conj:tau-codim-shannon)).  This candidate is
distinguished by the Plancherel-type normalisation
$\sum_\lambda y_\lambda^{(n)} d_\lambda = 1$
([Wedderburn--Bratteli recursion, §Per-level invariant]).
Then for every $n \geq 4$ there exists a partition
$\lambda^\star \vdash n$ with $y_{\lambda^\star}(q_0) < 0$, so
$p_q(\lambda^\star) < 0$ and $p_q$ is **not** a probability measure.
Consequently the Shannon-entropy formula*

$$
  \tau(C_{\dim_q}) \;\stackrel{?}{=}\; -\kappa(q) \sum_\lambda
  p_q(\lambda) \log p_q(\lambda)
$$

*([universal Frobenius co-dimension](#thm:frobenius-codim-universal))
**cannot** be evaluated with $p_q = y_\lambda \cdot d_\lambda$ at
$n \geq 4$ — the logarithm is undefined on negative arguments.*

**Independent validation.**  This proposition is **not** taken on
trust from the existing
[$y_\lambda$ sign-pattern remark](#rem:y-lambda-sign-pattern).  It
is independently re-verified in
[`tau_codim_conjectures_validate.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/tau_codim_conjectures_validate.py)
by re-running the seminormal-representation linear solve from
scratch at $n \in \{3, 4, 5\}$ and recording the witness
[`tau-codim-conjectures-validation.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/tau-codim-conjectures-validation.witness.json).
Three independent pathways agree to $\sim 10^{-15}$ on the
critical entry $y_{(1,1,1,1)}(q_0)$:

| Pathway | $y_{(1,1,1,1)}(q_0)$ |
|---|---|
| Fresh numpy linear solve (this PR's witness) | $-8.4253 \times 10^{-4}$ |
| Pre-existing 50-digit mpfr witness | $-8.4252749 \times 10^{-4}$ |
| Sympy $q$-rational symbolic solve | $-8.4253 \times 10^{-4}$ |

The linear system has condition number $\sim 3$ and residual
$\sim 10^{-16}$ — the negative sign is real, not a numerical
artifact.  A continuous $q$-sweep
($q \in \{1.0001, 1.001, 1.01, 1.05, 1.1097\}$) shows
$y_{(1,1,1,1)}(q)$ remains negative across the whole interval and
varies smoothly, ruling out any singularity at $q_0$.

**Consequence for the Shannon conjecture.**  Any proof of
[`conj:tau-codim-shannon`](#conj:tau-codim-shannon) must use a
probability measure $p_q$ **other than** the canonical Jones--Markov
$\times$ dimension product.  Candidates that remain open:

1. **The crystal-basis Plancherel measure** $p_q(\lambda) =
   \dim_q(\lambda)^2 / [n]_q!$ in the Kashiwara crystal limit
   $q \to 0, \infty$ (lattice-endpoint concentration);
2. **A heat-kernel regularisation** of the Markov trace on
   $\mathbf{Rep}(H_n(q))$ that kills negative components;
3. **A symmetric reformulation** $p_q(\lambda) = |y_\lambda|
   d_\lambda / Z_q$ — at the cost of losing the direct Markov-trace
   interpretation, since $|y_\lambda|$ is no longer a central
   pairing weight.

This proposition is therefore both a no-go (rules out one
candidate) and a refinement of the conjecture (narrows the search
to the three candidates above).

**Conjecture (q-CLT for Hecke transfer matrices).**
*Let $(H_\infty(q), \mathrm{tr}_M)$ be the QOU non-commutative
probability space in the Wenzl positivity regime
([algebraic GNS embedding](#prop:algebraic-gns-embedding)). Let
$\{\sigma_1, \sigma_2, \ldots\}$ be the braid transfer matrices.
Define the rescaled sum*
$$
  S_n \;:=\; \frac{1}{\sqrt{n}}
    \sum_{i=1}^{n} \bigl(\sigma_i - \mathrm{tr}_M(\sigma_i) \cdot 1\bigr).
$$
*Then under the joint Faddeev scaling $n \to \infty$ with
$n \lvert 1 - q \rvert \to \infty$, the joint moments of $S_n$
converge to those of a non-commutative q-Gaussian process:*
$$
  \mathrm{tr}_M\bigl(S_n^{\,k_1} S_n^{\,k_2} \cdots S_n^{\,k_m}\bigr)
  \;\xrightarrow{n \to \infty}\;
  \mathbb{E}_{q}\bigl[X^{k_1} X^{k_2} \cdots X^{k_m}\bigr],
$$
*where $X$ is a Blitvić $(q, t)$-Gaussian random variable at
parameter $q$ [`blitvic2012`] and $\mathbb{E}_q$ is the expectation
against the q-Gaussian measure $G_q(t, x)$ — the q-deformed bell
curve of non-extensive Tsallis statistics [`marsh2006`]. The
characteristic function of $S_n$ converges, in the sense of
non-commutative moment generating functions, to*
$$
  \mathrm{tr}_M(\exp_q(i \xi \cdot S_n))
  \;\xrightarrow{n \to \infty}\;
  \exp_q\!\bigl(-\tfrac{1}{2}\, \xi^2 \,\kappa_2^{(q)}\bigr),
$$
*where $\exp_q$ is the q-exponential and $\kappa_2^{(q)}$ is the
second free q-cumulant of $\sigma_i$ under $\mathrm{tr}_M$.*

**Why this is conditional.** Three inputs feed the conjecture, each
either an existing theorem or a class-encoded hypothesis:

1. **Non-commutative moment conditions on $\sigma_i$**
   ([rem:non-commutative-probability-dictionary](#rem:non-commutative-probability-dictionary)).
   Provable — the Hecke transfer matrices satisfy the trace and
   Markov properties needed for a Voiculescu non-commutative
   probability space.

2. **Two-parameter non-commutative CLT** [`blitvic2012`]. Established
   theorem — Blitvić shows that any sequence of non-commuting random
   variables with pair-partition combinatorial structure (which
   Hecke generators have, via the q-shuffle Hopf algebra
   $\mathcal{H}_q$ machinery) converges to the $(q, t)$-Gaussian
   under appropriate scaling. The conjecture invokes Blitvić's
   theorem at parameter values consistent with the QOU substrate.

3. **q-Gaussian attractor for systems with global correlations**
   [`marsh2006`]. Established theorem — Marsh–Fuentes–Moyano–Tsallis
   prove that under Tsallis non-extensive statistics, systems with
   global (long-range) correlations converge to a q-Gaussian rather
   than a classical Gaussian. The braid relations $\sigma_i
   \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ are
   precisely such global correlations.

**Specialisation to scalar invariants.** At $q = 1$, the conjecture
reduces to Biane's free CLT [`biane1998`]: the Jucys–Murphy elements
$J_k$ converge to free semicircular random variables, and the
limiting partition function is the semicircle distribution. The
q-deformation extends this to the QOU substrate.

**Mathematical bridge to the classical case.** The classical CLT
asymptotic $\lim_n (1 - t^2/2n)^n = e^{-t^2/2}$ generalises to
$$
  \lim_{n \to \infty}
    \bigl[1 \ominus_q \tfrac{1}{n}\bigl(\tfrac{t^2}{2}\bigr)\bigr]_q^{\boxtimes_q n}
  \;=\;
  \exp_q\!\bigl(-\tfrac{t^2}{2}\bigr),
$$
where $\ominus_q$ is the q-subtraction, $\boxtimes_q$ is the
categorical q-convolution on the Hecke algebra
($n$-fold convolution of stochastic transition operators), and
$\exp_q$ is the q-exponential generating the q-Gaussian. The
characteristic-function statement above is the moment-generating-
function form of this categorical convolution limit.

**Lean class.** Encoded as `MuArchContinuumLimit`-style class with
fields:
- `secondCumulant : R` (the limit variance),
- `qGaussianMeasure : Λ → R` (the limit measure),
- `momentConvergence` (the moment-convergence statement at each
  fixed multi-index $(k_1, \ldots, k_m)$),
- `characteristicFunctionLimit` (the q-exponential limit identity).

Per CLAUDE.md §3b-cond, downstream Lean theorems requiring the
q-CLT carry `[QCltNonCommutative ...]` as an explicit hypothesis.
The class is non-vacuous: each field carries actual mathematical
content (a real number, a function, a quantitative convergence
statement).

**Resolution of issue #649 §1.** This block is the formal statement
the author-agent requirements document requested, with the proof
split into the three citable inputs above plus the QOU-internal
input from
[the non-commutative probability dictionary](#rem:non-commutative-probability-dictionary).

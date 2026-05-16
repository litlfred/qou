**Proposition (q-Plancherel asymptotic skeleton).**
*Let $\tilde w_\lambda^{(n)} := \dim_q^2(\lambda) / [n]_q!$ be the
q-deformed Wedderburn weight on partitions of $n$
([Wedderburn weight canonical form](#prop:wedderburn-weight-canonical)).
There exists a topological space $\Omega_q$ (the q-deformed Thoma
simplex) and a sequence of pushforward maps*
$$
  \iota_n \colon \{\lambda \vdash n\}
    \;\longrightarrow\; \Omega_q,
  \qquad
  n \in \mathbb{N},
$$
*such that the pushforward measures
$\mu_n^{(q)} := (\iota_n)_*\,\tilde w_\lambda^{(n)}$ on $\Omega_q$
satisfy:*

1. *(Existence of limit at $q = 1$, established.) For $q = 1$, the
   sequence $\{\mu_n^{(1)}\}$ converges weakly to a measure
   $\mu_\infty^{(1)}$ on the classical Thoma simplex* [`kerov1981`,
   `biane1998`].
2. *(Variance bound at generic $q$, established by Féray–Méliot.)
   The character fluctuations $\chi_\lambda - \mathbb{E}_q[\chi]$
   measured under $\mu_n^{(q)}$ have variance
   $O(1/\sqrt{n - 3})$* [`feray2010`].
3. *(Limit identification, conjectural.) For $q \neq 1$ in the
   Wenzl positivity regime
   ([algebraic GNS embedding](#prop:algebraic-gns-embedding)),
   $\{\mu_n^{(q)}\}$ converges weakly to a limit measure
   $\mu_\infty^{(q)}$ on $\Omega_q$. The identification of
   $\mu_\infty^{(q)}$ with a measure on the GNS operator algebra
   $\pi_{\mathrm{GNS}}(H_\infty(q))$ is conditional on the existence
   of a continuous map $\Omega_q \to L(\mathcal{H})$ compatible with
   $\iota_n$.*

**What is established.** Parts (1) and (2) are theorems in the
asymptotic Plancherel literature. The QOU codebase already carries
the Féray–Méliot CLT as the typeclass `HasQPlancherelCLT` in
[`QPlancherel.lean`](/content/quantum-observable-universe/lean/QOU/MathlibExt/QPlancherel.lean).
Convergence in measure is therefore part of the existing
infrastructure; nothing about the *measure-theoretic limit alone*
is conjectural in QOU.

**What is conjectural.** Part (3) names two separable open problems:

- (3a) *q-deformed Kerov–Vershik.* Extension of the classical
  $q=1$ Thoma-simplex convergence to generic $q$. The variance
  bound (Féray–Méliot) is consistent with such convergence but
  does not by itself produce a limit measure.
- (3b) *Operator-algebra realisation.* Identification of the
  limit measure $\mu_\infty^{(q)}$ with the pushforward of a
  bona fide measure on the GNS image
  $\pi_{\mathrm{GNS}}(H_\infty(q)) \subset L(\mathcal{H})$, via a
  continuous map $\Omega_q \to L(\mathcal{H})$. This is where the
  measure-valued route to CFS picks up
  ([CFS comparison summary](#rem:cfs-comparison-summary)).

**Status summary.** The bulk of clause 2 of
[CFS comparison summary](#rem:cfs-comparison-summary) leaves the
conjecture upon promotion of this proposition: the *convergence
itself* is established or near-established; only the
*operator-algebra realisation* of the limit measure is conjectural.
This narrows the conjectural surface to (3a)+(3b) above, both
matters of identification rather than analysis.

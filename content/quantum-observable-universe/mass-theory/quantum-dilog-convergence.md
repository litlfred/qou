**Proposition (convergence of the quantum dilogarithm).**

*Let $q \in \mathbb{R}$ with $1 < q$, and let $z \in \mathbb{R}$ with
$\lvert z \rvert < q$. Then the quantum dilogarithm*

$$
  \Phi_q(z) \;=\; \prod_{k \geq 1} \bigl(1 - q^{-k} z\bigr)^{-1}
$$

*is multipliable: the infinite product converges to a well-defined,
non-zero real number.*

*Proof.* Each factor is non-zero on the domain: $\lvert q^{-k} z\rvert
< q^{-k} \cdot q = q^{\,1-k} \leq 1$ for $k \geq 1$, so
$1 - q^{-k} z \neq 0$
([quantum dilogarithm](#cor\:quantum-dilogarithm)). Writing
$a_k = q^{-k} z$, the geometric series $\sum_{k \geq 1} \lvert a_k\rvert
= \lvert z\rvert \sum_{k\geq 1} q^{-k}$ converges since $q > 1$. On the
domain every denominator obeys the uniform lower bound
$1 - a_k \geq 1 - \lvert z\rvert / q > 0$, so the deviation terms
$g_k = (1 - a_k)^{-1} - 1 = a_k/(1 - a_k)$ satisfy
$\lvert g_k\rvert \leq \lvert a_k\rvert /(1 - \lvert z\rvert/q)$ and are
summable by comparison. Multipliability of $\prod_k (1 + g_k) =
\prod_k (1 - a_k)^{-1}$ then follows from the one-plus-summable
criterion for infinite products. $\square$

*This is the **convergence half** of the brane-tower programme — the
claim of [brane tower in $z$-Habiro](#conj\:brane-tower-z-habiro) that
survives the refutation of the level-selection rule $n_\star$. It
establishes that $\Phi_q$ is a genuine analytic object on $\lvert z\rvert
< q$, so the $z$-Habiro Cauchy-limit construction has a well-defined
target.*

**Note (scope).** *Convergence does not make the per-generator
$\Phi_q(\lvert\hat V_i\rvert)$ form a production mass input. At the
physical brane-tower argument $z_i = \lvert\hat V_i^{\mathrm{full}}\rvert
\in [0.85, 1)$ the product is convergent but enormous
($\Phi_q(0.989) \approx 6.7 \times 10^5$), which is why the canonical
mass tower [mass-endomorphism tower](#prop\:mass-endomorphism-tower)
evaluates the bounded symmetric form $-\mathrm{Li}_2^q(-\lvert\hat
V_i\rvert)$ rather than $\Phi_q$. The proposition closes the analytic
existence question, not the regularization question.*

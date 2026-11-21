Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$ and Planck-$q$ constant
$\hbar_q = (q-1)/q$.  For a vortex $\varrho$ with braid
representative $\beta \in B_n$, the brane-tower refinement of the
mass endomorphism
([mass tower](#prop:mass-endomorphism-tower),
[jet-brane reformulation](#rem:mass-endomorphism-jet-tower))
takes the form

$$
  \mathfrak{m}(\varrho)
  = \mathfrak{m}^{(0)}(\varrho)
  + \sum_{n=1}^{\infty} \hbar_q^{2n} \cdot \Delta^{(n)}(\varrho),
$$

where $\mathfrak{m}^{(0)}$ is the canonical Markov-trace term at
brane level zero and $\Delta^{(n)}(\varrho) = \mathfrak{m}^{(n)}
(\varrho_\mathrm{free}) - \mathfrak{m}^{(n)}(\varrho_\mathrm{atom})$
is the per-level binding contribution at brane level $n$.  The
$\hbar_q^{2n}$ weight comes from the recursive brane tower
$A_{n+1} = A_n \otimes \Omega^1(A_n)$: each jet-up step pairs a
Kähler form with its Frobenius dual, contributing $\hbar_q^2$ to
the weight.

**Proposition.**
*Assume $q > 1/2$ and $q \neq 1$, so that $0 < \hbar_q^2 < 1$, and assume there exists $\Delta_{\max}(\varrho) < \infty$ with
$|\Delta^{(n)}(\varrho)| \leq \Delta_{\max}(\varrho)$ for all
$n \geq 1$.  Then the brane-tower sum
$T(\varrho) := \sum_{n \geq 1} \hbar_q^{2n} \Delta^{(n)}(\varrho)$
converges absolutely, and the $N$-term truncation error is
bounded by*

$$
  \bigl\lvert T(\varrho)
    - \sum_{n=1}^{N} \hbar_q^{2n}\,\Delta^{(n)}(\varrho) \bigr\rvert
  \;\leq\; \Delta_{\max}(\varrho) \cdot
  \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^{2}}.
$$

*In particular, to achieve binding-energy precision
$\varepsilon_B$ (in MeV) at archimedean calibration $E_0$, it
suffices to take*

$$
  N \;\geq\;
  \left\lceil \frac{\log\bigl( \tfrac{\varepsilon_B \,(1 - \hbar_q^{2})}
                                {E_0 \,\Delta_{\max}(\varrho)} \bigr)}
                 {\log(\hbar_q^{2})} \right\rceil.
$$

The discussion of the boundedness hypothesis, the engineering
consequence, and the relation to the confinement SDP are collected in
[the jet-tower convergence context](#rem:jet-tower-convergence-context).

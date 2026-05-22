Let $K$ be a hyperbolic knot or link appearing in the Archimedean universe
mass spectrum, and let $\{\mathfrak{G}_n\}_{n \geq 0}$ be the
[cosimplicial crossed groupoid](#prop:cosimplicial-crossed-groupoid) of
the brane tower with [obstruction classes](#def:quantum-characteristic-classes)
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$.

**Proposition.**
There exists a decomposition of the hyperbolic volume into tower-level
contributions:

$$
  \mathrm{Vol}(K)
  = \sum_{n=0}^{\infty} \Phi_n(K),
$$

where $\Phi_n(K)$ is the Chern--Simons period integral of the $n$-th
twisted sector, satisfying:

1. **Convergence.** The series converges absolutely.  The tail
   $\sum_{n > N} |\Phi_n(K)|$ is controlled by the spectral gap
   of the $\mathrm{SU}_{q_n}(2)$-adjoint action at level $n$.

2. **Yekutieli control.** Each $\Phi_n(K)$ is determined by the
   Yekutieli triple $(x^{(n)}, g^{(n)}, a^{(n)})$ at level $n$:

$$
  \Phi_n(K) = \int_{\gamma_n}
    \mathrm{CS}\bigl(g_{ij}^{(n)},\, a_{ij}^{(n)}\bigr),
$$

   where $\gamma_n$ is the Picard--Lefschetz thimble at level $n$
   and $\mathrm{CS}$ denotes the Chern--Simons 3-form evaluated on
   the transition data.

3. **Coface compatibility.** The coface map
   $\delta^0 \colon \mathfrak{G}_n \to \mathfrak{G}_{n+1}$ relates
   consecutive terms: $\Phi_{n+1}(K) = \Phi_n(K) \cdot r_n + \varepsilon_n$,
   where $r_n$ is the spectral contraction ratio at level $n$ and
   $\varepsilon_n$ is the genuinely new contribution from
   $\kappa_n \neq 0$.

4. **Classical limit.** At $q = 1$ all levels collapse to the
   single hyperbolic structure: $\Phi_0(K) = \mathrm{Vol}(K)$ and
   $\Phi_n(K) = 0$ for $n \geq 1$.

The existing two-level structure (Level 0 inter-nucleon, Level 1
intra-Borromean, as in
[quantum dilogarithm volume](#prop:quantum-dilogarithm-volume)) is the
truncation of this series at $n = 1$.

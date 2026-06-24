*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The torus knots embeddable on $\Sigma_4$ form a **complete,
self-dual basis** for the regular representation of the
Iwahori--Hecke algebra $H_n(q)$.  The $Q$-value of beta decay is the
spectral decomposition of the decay operator in this basis.
The decomposition is **exact and finite** — it terminates at
degree $2$ because the embeddability bound on $\Sigma_4$ kills
all higher jets.

## Corollary (spectral decomposition of the $Q$-value)

*This is a direct consequence of the
[cohomological embedding](#prop:cohomological-embedding) (completeness
of the torus knot basis on $\Sigma_g$) applied to the beta decay
[transfer matrix](#prop:beta-decay-transfer-matrix).*

*Let $\Sigma_g$ be a genus-$g$ surface and
$\mathcal{E}_g = \{\tau(r,s) : \tfrac{(r-1)(s-1)}{2} \leq g\}$
the set of torus knot labels embeddable on $\Sigma_g$.  For
$\beta^-$ decay $\mathcal{N}_{Z,N} \to \mathcal{N}_{Z+1,N-1}$,
the $Q$-value admits the spectral decomposition:*

$$
  Q
  = 
  \underbrace{
    \Bigl|\log_q\frac{P_{\mathrm{dau}}(q)}{P_{\mathrm{par}}(q)}\Bigr|
    \cdot \hbar_q \cdot \frac{m_e}{3}
  }_{\displaystyle\mathcal{Q}_{\mathrm{bare}}}
   \times 
  \underbrace{
    \prod_{\tau(r,s) \in \mathcal{E}_g}
    F\!\bigl(\tau(r,s), N\bigr)
  }_{\displaystyle\text{knot operator product}}
$$

*where:*

**(i)** *$P(q) = \prod_{j=0}^{A-2} \hat{V}_j(q)$ is the Skein
polynomial from the inductive chain construction
([transfer matrix](#prop:beta-decay-transfer-matrix)).  Each
chain $\hat{V}_j = z \cdot M_j[0][0] + M_j[1][0]$ (with
$z = (q^{1/2} + q^{-1/2})^{-1}$ the Markov parameter) is
pre-reduced via the $2\!\times\!2$ matrix recurrence (zero
Hecke steps), ensuring $\mathcal{N}_{Z,N}$ is in Gröbner--Shirshov
normal form at every inductive stage.*

**(ii)** *$\log_q(x) = \ln x / \ln q$ is the $q$-natural
logarithm — it counts exceptional divisor levels along the
coral tube fiber of $\Sigma_g$.
The constant $\hbar_q = (q - 1)/q$ is the quantum Planck constant (action
per divisor step).  The factor $m_e/3$ is the mass per
crossing of the trefoil $\mathcal{K}_e = \mathcal{K}_{\tau(2,3)}$
(the electron is $3$ crossings).  The product
$\hbar_q \cdot m_e / 3$ replaces the intermediate notation
$\mathfrak{E} \cdot \mu_0$ — these cancel algebraically.*

**(iii)** *$F(\tau(r,s), N)$ is the **knot operator** of
$\tau(r,s)$ acting on the converting neutron's
shell:*

$$
  F(\tau(r,s), N)
  = 
  \begin{cases}
    1
    & \tau(r,s) \notin \mathcal{E}_g
     \text{(null: zero action on $\Sigma_g$)} \\[4pt]
    1
    & \text{shell unchanged by decay (cancels in ratio)} \\[4pt]
    \mathrm{tr}_M\!\bigl(
      \tau(r,s) \cdot T_{\beta\text{-decay}}(q)
    \bigr)
    & \text{active shell, partially filled} \\[4pt]
    \dfrac{\bigl|\mathrm{tr}_M\!\bigl(
      e_{(1^3)} \cdot \tau(r,s) \cdot
      T_{\beta\text{-decay}}(q) \cdot e_{(1^3)}
    \bigr)\bigr|}{\bigl|\mathrm{tr}_M\!\bigl(T_{\beta\text{-decay}}(q)\bigr)\bigr|}
    & \text{active shell, fully filled (Pauli)}
  \end{cases}
$$

*with $T_{\beta\text{-decay}}(q) = \sigma_0 \sigma_1^{-1} \in H_3(q)$ the
beta decay operator
([beta decay](#def:beta-decay-skein)), and $e_{(1^3)}$ the
alternating Young symmetrizer of $H_3(q)$
([glossary](#rem:y-lambda-sign-pattern)).*

**(iv)** *The product over $\mathcal{E}_g$ **collapses to a
single term**: only the converting neutron's shell knot
$\tau(k^*)$ is active; all other shells cancel between parent
and daughter.  Non-embeddable knots contribute $F = 1$.*

**(v)** *The decomposition is **exact**: the embeddable torus
knots form a complete basis for the representation ring of
$H_n(q)$ restricted to $\Sigma_g$ (by the self-duality
$\tau(r,s) \leftrightarrow \tau(s,r)$ and the Rosso–Jones
completeness of torus knot invariants
([cohomological embedding](#prop:cohomological-embedding))).
No higher-order corrections exist — the tower terminates at
degree $\lfloor 2g/(g-1) \rfloor$.*

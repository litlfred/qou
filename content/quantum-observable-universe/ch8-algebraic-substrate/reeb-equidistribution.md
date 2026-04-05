**Proposition (Reeb equidistribution).**
Let $(\mathbf{C}, \theta, G, \mathcal{S})$ be a QOU with
substrate parameter $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$
and Reeb bundle $\mathcal{R}_p = (S^3 \to S^2, \xi_q)$
([Reeb bundle](#def:reeb-bundle)).  The holonomy of the
Reeb connection is $e^{2\pi i/[2]_q}$, giving rotation
number

$$
  \alpha(q) \;:=\; \frac{1}{[2]_q} \;=\; \frac{1}{q + q^{-1}}.
$$

Then:

**(a)** The rotation number $\alpha(q)$ is **irrational**
if and only if $q \notin \mu_\infty$ (torsion avoidance).

*Proof sketch.*
If $\alpha(q) = p/r$ is rational, then
$q + q^{-1} = r/p$, so $q$ satisfies $pq^2 - rq + p = 0$
— a quadratic with discriminant $r^2 - 4p^2$. For $q$ to
be a root of unity $e^{2\pi i m/n}$, we need
$q + q^{-1} = 2\cos(2\pi m/n)$, which is algebraic of
degree $\leq \varphi(n)/2$.  But $\alpha$ rational forces
$q$ algebraic of degree $\leq 2$.  If additionally $|q| = 1$,
then $q \in \mu_\infty$.  The converse: $q \in \mu_\infty$
gives $q + q^{-1} = 2\cos(2\pi m/n) \in \mathbb{Q}$ only
for $n \in \{1, 2, 3, 4, 6\}$ (Niven's theorem); for other
$n$, $\alpha$ is irrational but $q$ is still a root of unity,
so the stronger condition $q \notin \mu_\infty$ is needed.
In the QOU with $q \in \mathbb{R}_{>1}$: $\alpha(q)$ is
irrational for all $q > 1$ (since $q + q^{-1} > 2$ is
transcendental for generic $q$).  $\square$

**(b)** By the **Weyl equidistribution theorem**, the
sequence of Reeb phases

$$
  \theta_k \;=\; k \cdot 2\pi\alpha(q) \pmod{2\pi},
  \qquad k = 0, 1, 2, \ldots
$$

is equidistributed on $[0, 2\pi)$.  For any continuous
$f \colon [0, 2\pi) \to \mathbb{R}$:

$$
  \lim_{N \to \infty} \frac{1}{N} \sum_{k=0}^{N-1}
  f(\theta_k)
  \;=\;
  \frac{1}{2\pi} \int_0^{2\pi} f(\theta)\,d\theta.
$$

**(c)** Applying (b) to the Hecke projector
$f(\theta) = \|e_+(\xi_q)\|^2 = \cos^2(\theta/2)$
(the fraction of energy in $A_H$ at phase $\theta$):

$$
  \bigl\langle f_+ \bigr\rangle_{\mathrm{Reeb}}
  \;=\;
  \frac{1}{2\pi} \int_0^{2\pi} \cos^2(\theta/2)\,d\theta
  \;=\;
  \frac{1}{2}.
$$

The bare Reeb flow equidistributes with $\langle f_+ \rangle = 1/2$,
which exceeds the critical fraction $f_+^*(q) < 1/2$
([q-Collatz](#conj:q-collatz)) for all $q > 0$.

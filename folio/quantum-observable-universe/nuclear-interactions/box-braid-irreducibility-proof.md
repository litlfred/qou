*Proof that $c(T_{3,5}) = 10$ is irreducible.*

The crossing number of a torus knot $T_{m,n}$ with $\gcd(m,n) = 1$ and $2 \leq m < n$ is:

$$
  c(T_{m,n}) =  \min\bigl((m-1)n, (n-1)m\bigr).
$$

For $T_{3,5}$: $\min(2 \cdot 5, 4 \cdot 3) = \min(10, 12) = 10$. The $B_3$ representation $(\sigma_0\sigma_1)^5$ achieves this minimum. The braid index of $T_{3,5}$ is $\min(3, 5) = 3$ (Morton–Williams inequality). This confirms that $B_3$ provides the minimum strand count.

**Irreducibility below 10 crossings:**

**(i) Topological invariance.** The crossing number $c(K)$ is a knot invariant. It is the minimum number of crossings over all diagrams of $K$ (not just positive braids, but all braid groups $B_n$ and all non-braid diagrams). For torus knots, this minimum is known in closed form. No isotopy, Reidemeister move, or change of braid representation can reduce $c(T_{3,5})$ below $10$.

**(ii) Distinction from the Iwahori--Hecke algebra normal form.** In the Iwahori--Hecke algebra $H_3(q)$, which has dimension $|S_3| = 6$, the word $(\sigma_0\sigma_1)^5$ reduces to a polynomial in the standard basis $\{T_w : w \in S_3\}$. The maximum word length is $3$ per basis element (since the longest element of $S_3$ has length $3$). This algebraic reduction computes the amplitude of the process (the Markov trace gives the Jones polynomial $J_{T_{3,5}}(q)$), not the physical crossing count. Each $\sigma_i$ in the original braid word represents one physical $R$-matrix application, which corresponds to one Planck step. The Iwahori--Hecke algebra computes what amplitude results from $10$ $R$-matrix applications; it does not reduce the number of applications.

**(iii) $T_{3,5}$ is the unique cross-family mediator.** The only torus knots embeddable on the genus-$4$ Bring surface with winding numbers from both the $m = 2$ (lepton) and $m = 3$ (quark) families are $T_{3,4}$ and $T_{3,5}$ ([unmapped torus knots](#rem:unmapped-torus-knots)). $T_{3,4}$ connects $m = 3$ to $n = 4$ (force carrier: Hopf${}^2$ color binding in $H^{0,1}$). $T_{3,5}$ connects $m = 3$ to $n = 5$ (second generation). Only $T_{3,5}$ mediates flavor-changing charged-to-neutral transitions. No alternative mediator with fewer crossings exists on the Bring's surface.

**(iv) No direct $\gamma$–$\nu$ coupling.** A direct coupling requires connecting the photon (no braid strands, $Q = 0$) to the neutrino ($Q = 0$) without charged intermediaries. However, the photon's electromagnetic interaction is the antisymmetric component of the crossing energy under the $\dagger$-involution. It couples only to objects with $Q \neq 0$. The neutrino has $Q(\nu) = 0$. The charge-neutrality gap between the photon and neutrino can only be bridged by passing through charged intermediaries ($e^{\pm}$, trefoils with $Q = \pm 1$) and converting via the weak mediator $T_{3,5}$. $\square$

**Connection to the Jones polynomial.**

The Jones polynomial $J_K(q)$ of a knot $K$ is the quantum trace over the spin-$\tfrac{1}{2}$ representation:

$$
  J_K(q) =  \mathrm{tr}_{V_{1/2}}(\rho(\beta))
$$

The colored Jones polynomial $J_K^{(j)}(q)$ uses the spin-$j$ representation. The **recursion** between colored Jones polynomials encodes the $q$-angular momentum:

$$
  J_K^{(j+1/2)}(q) =  [2j+1]_q \cdot J_K^{(j)}(q)
  +  \text{(lower-order terms)}
$$

**Building block values.**

| Knot | $n$ (strands) | $j$ | $J_q^2$ at the aether parameter $q$ | Classical $j(j+1)$ |
|------|:---:|:---:|:---:|:---:|
| $0_1$ (unknot) | $1$ | $0$ | $0$ | $0$ |
| $3_1$ (trefoil) | $2$ | $\frac{1}{2}$ | $[1/2]_q [3/2]_q = 0.7507$ | $0.75$ |
| $4_1$ (figure-eight) | $2$ | $\frac{1}{2}$ | $0.7507$ | $0.75$ |
| $5_1$ (cinquefoil) | $2$ | $\frac{1}{2}$ | $0.7507$ | $0.75$ |
| $\mathcal{B}_3$ (Borromean) | $3$ | $\frac{1}{2}$ | $0.7507$ | $0.75$ |

All single-component knots in $B_2$ carry spin $j = \tfrac{1}{2}$. The nuclear spin depends on coupling: $A$ nucleons (each $j = 1/2$) couple to total $J$ via $q$-Clebsch--Gordan coefficients. The parity of $A$ (modulo 2) determines the $J$ parity ([nuclear spin parity](#prop:nuclear-spin-parity)).

**Nuclear $q$-angular momentum.**

For a nucleus $\mathcal{N}(Z, N)$ with $A = Z + N$:

$$
  J_q^2(\mathcal{N}) =  [J]_q  [J+1]_q
$$

Here $J$ is the ground-state spin fixed by the nuclear link's embedding in the Temperley--Lieb algebra $TL_A(\delta)$ with loop parameter $\delta = [2]_q = q + q^{-1}$ under Convention D (contrasted with $\delta = -(q^{1/2} + q^{-1/2})$ in the $q^{1/2}$ Kauffman convention).

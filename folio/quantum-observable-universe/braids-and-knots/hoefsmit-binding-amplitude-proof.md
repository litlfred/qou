**Proof.** The Hoefsmit seminormal matrix for $\sigma_2$ on
$V_{(2,1)}$ has a $2 \times 2$ block with entries

$$
  a_\rho = \frac{h}{1 - q^{-2\rho}},
  \qquad
  a_{-\rho} = \frac{h}{1 - q^{2\rho}},
  \qquad
  b = \sqrt{a_\rho \cdot a_{-\rho} + 1},
$$

where $\rho = 2$ is the axial distance and $h = q - q^{-1}$. For $q^4 \neq 1$, both denominators $1 - q^{-4}$ and $1 - q^4$ are non-zero, and the product of the diagonal entries is

$$
  a_\rho \cdot a_{-\rho}
  = \frac{h^2}{(1 - q^{-4})(1 - q^4)}
  = \frac{h^2}{-(h^2)(h^2 + 4)}
  = -\frac{1}{h^2 + 4}
  = -\frac{1}{[2]_q^2}.
$$

At $q = \pm 1$ ($q^2 = 1$), $h = q - q^{-1} = 0$ and $1 - q^{\mp 4} = 0$, so the unsimplified fractions $h/(1 - q^{\mp 4})$ have a $0/0$ removable singularity: cancelling $h$ via $1 - q^4 = -h q^2 [2]_q$ and $1 - q^{-4} = h q^{-2} [2]_q$ yields the simplified forms $a_{-2} = -q^{-2}/[2]_q$ and $a_2 = q^2/[2]_q$, which are defined and satisfy $a_2 a_{-2} = -1/[2]_q^2$ for every $q \in R^\times$ at which $[2]_q = q + q^{-1}$ is invertible (excluding only $q^2 = -1$, where $[2]_q = 0$).

Therefore $b^2 = a_2 a_{-2} + 1 = -1/[2]_q^2 + 1 = ([2]_q^2 - 1)/[2]_q^2$, and $1 - b^2 = 1/[2]_q^2$.
Since $[2]_q^2 = (q + q^{-1})^2 = h^2 + 4$ and
$[3]_q = q^2 + 1 + q^{-2} = h^2 + 3 = [2]_q^2 - 1$:

$$
  b^2 = \frac{[2]_q^2 - 1}{[2]_q^2} = \frac{[3]_q}{[2]_q^2},
  \qquad
  1 - b^2 = \frac{1}{[2]_q^2}.
  \qquad\square
$$

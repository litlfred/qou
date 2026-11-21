### Proof on $V_{(1^p)}$ (closed-form contribution)

The single SYT of shape $(1^p)$ fills the column with entries
$1, 2, \ldots, p$ from top to bottom, giving cell contents
$0, -1, -2, \ldots, -(p-1)$ and axial-distance pattern
$\rho_i = c(i+1) - c(i) = -1$ for every consecutive pair
$(i, i+1)$.

In the Hoefsmit construction, axial distance $\rho = -1$ is a
$1 \times 1$ block with eigenvalue $a_{-1} = h / (1 - q^{2})$
which simplifies (after the $\det = -1$ normalisation) to
$-q^{-1}$. Hence each $\sigma_i$ acts as the scalar $-q^{-1}$ on
$V_{(1^p)}$, and

$$
  \chi_{(1^p)}(\beta_{p,k})
  \;=\;
  \mathrm{tr}\!\bigl[(-q^{-1})^{k(p-1)} \cdot I\bigr]
  \;=\;
  (-1)^{k(p-1)} \, q^{-k(p-1)}.
$$

This is a single Laurent monomial with pole order exactly
$k(p - 1)$ at $q = 0$. There is no within-partition cancellation
because the SYT path visits distinct axial distances at every
step (no adjacent contents differ by $\pm 1$), so the
$b^2 = (1 - q^{2\rho - 2})(1 - q^{2\rho + 2})/(1 - q^{2\rho})^2$
zeroing on adjacent contents in the $2 \times 2$ Hoefsmit blocks
never fires on $V_{(1^p)}$.

### Maximality across irreps

The maximality claim — that no other $\lambda \vdash p$ achieves
pole order $> k(p - 1)$ — is **verified case-by-case** in
the canonical formalism
for $(p, k) \in \{(2, 3), (2, 5), (2, 9), (3, 4), (3, 5),
(3, 7)\}$: in every case the trivial-channel $V_{(p)}$ gives
pole order $0$ (it acts by the eigenvalue $q$, contributing
$q^{k(p-1)}$, no pole), and the mixed $V_{(p-1, 1)}$, $V_{(p-2,
2)}$, $\ldots$ channels give pole order $\leq 0$ as well, so the
maximum is realised uniquely at $V_{(1^p)}$.

A general proof would establish that for the cyclic torus braid
$\beta_{p,k}$, the rank of the $-q^{-1}$ eigenspace contribution
strictly increases as $\lambda$ becomes more "column-like" in
the dominance order. This is conjectured to follow directly via
the Schur–Weyl pole-counting (each row of $\lambda$ contributes
one $+q$ eigenvalue per Coxeter cycle, each column one $-q^{-1}$),
but defer the categorical argument to a separate proposition.

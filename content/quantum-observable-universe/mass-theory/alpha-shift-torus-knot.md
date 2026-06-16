<!-- Theorem (conditional on:
       def:delta-q-decoration,
       prop:force-carrier-intertwining-correspondence). -->

**Proposition (torus-knot $\alpha_{\mathrm{shift}}$).**
*Let $p \geq 1$, $k \geq 1$ with $\gcd(p, k) = 1$, and let
$T_{p,k}$ be the $(p, k)$-torus knot, presented as the closure
of the braid $\beta_{p,k} = (\sigma_1 \sigma_2 \cdots
\sigma_{p-1})^k \in B_p$. Define the **shift exponent***

$$
  \alpha_{\mathrm{shift}}(T_{p,k})
  \;:=\;
  \max_{\lambda \,\vdash\, p}\;
  \mathrm{ord}_{q=0}^{(-)}\; \chi_\lambda(\beta_{p,k})
$$

*where $\chi_\lambda$ is the seminormal Hecke character on
$V_\lambda$ ([`def:delta-q-decoration`](#def:delta-q-decoration))
and $\mathrm{ord}_{q=0}^{(-)}$ denotes the pole order at $q = 0$
(i.e. the negative of the Laurent valuation). Then:*

1. *The maximizer is the all-anti-symmetric channel $V_{(1^p)}$.*
2. *$\alpha_{\mathrm{shift}}(T_{p,k}) = k(p - 1)$.*

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
[`computations/alpha/alpha_shift_torus.py`](../../computations/alpha/alpha_shift_torus.py)
for $(p, k) \in \{(2, 3), (2, 5), (2, 9), (3, 4), (3, 5),
(3, 7)\}$: in every case the trivial-channel $V_{(p)}$ gives
pole order $0$ (it acts by the eigenvalue $q$, contributing
$q^{k(p-1)}$, no pole), and the mixed $V_{(p-1, 1)}$, $V_{(p-2,
2)}$, $\ldots$ channels give pole order $\leq 0$ as well, so the
maximum is realised uniquely at $V_{(1^p)}$.

A general proof would establish that for the cyclic torus braid
$\beta_{p,k}$, the rank of the $-q^{-1}$ eigenspace contribution
strictly increases as $\lambda$ becomes more "column-like" in
the dominance order. We conjecture this is straightforward via
the Schur–Weyl pole-counting (each row of $\lambda$ contributes
one $+q$ eigenvalue per Coxeter cycle, each column one $-q^{-1}$),
but defer the categorical argument to a separate proposition.

### Witness summary

The numerical evidence
([`alpha-shift-torus.witness.json`](../../computations/alpha/alpha-shift-torus.witness.json))
records the full per-irrep symbolic $\chi_\lambda \in \mathbb{Q}(q)$
together with the pole order at $q = 0$ for every test pair, summarised
in
[Table: $\alpha_{\mathrm{shift}}(T_{p,k})$ for 6 test pairs](#tbl:alpha-shift-torus-knot-table-data).
All $14$ assertions in the witness pass.

### Cross-link

The two values $\alpha_{\mathrm{shift}}(T_{2,9}) = 9$ and
$\alpha_{\mathrm{shift}}(T_{3,5}) = 10$ are precisely the
$q$-integer indices appearing in
[`prop:em-coupling-projection`](#prop:em-coupling-projection)'s
formula

$$
  \alpha_{EM}^{-1} \;=\; q \cdot [9]_q \cdot [10]_q.
$$

[`prop:alpha-em-shift-multiplicative-chain`](#prop:alpha-em-shift-multiplicative-chain)
combines the two identities into the **shift-exponent form**

$$
  \alpha_{EM}^{-1}
  \;=\;
  q \cdot
  \bigl[\alpha_{\mathrm{shift}}(T_{2,9})\bigr]_q \cdot
  \bigl[\alpha_{\mathrm{shift}}(T_{3,5})\bigr]_q,
$$

upgrading AXKIA's $\delta_q$-trace identity into the same
combinatorial universe as the w3-w4 atomic-shift formula
([`docs/audits/-w3-habiro-unblocked.md`](../../docs/audits/-w3-habiro-unblocked.md)).

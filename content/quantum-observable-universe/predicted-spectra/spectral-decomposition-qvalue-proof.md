1. **Completeness.**  The Rosso–Jones formula decomposes
   $J_{\tau(r,s)}(q) = \sum_{\lambda \vdash r} d_\lambda(q) \cdot \omega_\lambda^s$ into irreps of $H_r(q)$.  Every
   irrep $\lambda$ is recoverable from the torus knot data
   (by Möbius inversion on the power sums $\omega^s$).  The
   self-duality $\tau(r,s) \leftrightarrow \tau(s,r)$ provides
   the inner product.  Hence $\mathcal{E}_g$ spans the
   representation ring at each degree $\leq \lfloor 2g/(g-1) \rfloor$.

2. **Inductive chain construction.**  Each nucleon $k$ is
   added by extending the $2\!\times\!2$ chain matrices:
   $M_j \leftarrow M_j \cdot T_{j {}^j\!\bowtie_k k}(q)$
   for existing positions $j < k$, and
   $M_{k-1} = T_{(k\!-\!1) {}^{k-1}\!\bowtie_k k}(q)$ for the new
   position.  The Hecke reduction $\sigma^2 = (q - q^{-1})\sigma + 1$ is handled within each
   $2\!\times\!2$ chain — zero Yang–Baxter steps, zero Hecke
   steps on the multi-generator element.  The nuclear word
   $\mathcal{N}_{Z,N} = \prod_j (\mathfrak{w}^+_j \sigma_j + \mathfrak{w}^0_j)$ uses
   **distinct generators** and is always in Gröbner--Shirshov normal form.

3. **Shell cancellation.**  Since parent and daughter share
   all chains except those crossing the converting nucleon,
   the log ratio $\log_q(P_{\mathrm{dau}}/P_{\mathrm{par}}) = \sum_j [\log_q \hat{V}_j^{\mathrm{dau}} - \log_q \hat{V}_j^{\mathrm{par}}]$ receives contributions
   only from generators $j$ that interact with the converting
   nucleon.

4. **Pauli projection.**  A fully occupied shell of $n$
   fermions is totally antisymmetric.  Under the Schur–Weyl
   decomposition of $H_3(q)$, the decay operator
   $T_{\beta\text{-decay}}(q)$ is projected onto the alternating irrep
   $(1^3)$ via $e_{(1^3)} \cdot T_{\beta\text{-decay}}(q) \cdot e_{(1^3)}$.
   The symmetric and standard irreps cancel in the fully
   occupied state.

5. **Tower termination.**  The degree-$k$ tower knot
   $\tau(r, s^k)$ requires genus $(r-1)(s^k - 1)/2$.  For
   $g = 4$: degree $1$ admits $4$ knots, degree $2$ admits
   $2$ knots ($\tau(2,9)$ and $\tau(3,4)$), degree $3$
   requires genus $\geq 13$ — so the jet bundle over
   $\Sigma_4$ has **exactly three non-zero levels**
   ($k = 0, 1, 2$).

### The six embeddable torus knots on $\Sigma_4$

See [Table 1](#tbl:spectral-decomposition-qvalue-table1-data).

Degree-$1$ knots are already encoded in $\mathcal{Q}_{\mathrm{bare}}$
through distinct vertex weights ($\mathfrak{p} {}^i\!\oplus_j \mathfrak{p}$, $\mathfrak{n} {}^i\!\oplus_j \mathfrak{n}$, $\mathfrak{p} {}^i\!\oplus_j \mathfrak{n}$ — inter-particle Hopf links with crossing indices $i, j$), so $F = 1$ for shells $1$–$4$.
The active correction comes from degree-$2$ knots only.

### Jet bundle structure

The knot operators form a **jet bundle over the exceptional
divisor chain** of $\Sigma_g$, with jet index given by the
Gröbner--Shirshov class (= degree in the degree tower) of each torus knot.

See [Table 2](#tbl:spectral-decomposition-qvalue-table2-data).

The jet decomposition is **exact and finite** — not by truncation
but by the finite dimensionality of the regular representation of
$H_n(q)$ on $\Sigma_g$.
Completeness follows from the self-duality $\tau(r,s) \leftrightarrow \tau(s,r)$ and the Rosso–Jones expansion: every irrep of $H_n(q)$ is
recoverable from the torus knot invariants, so the knots form a
complete orthogonal basis under the Markov trace inner product.

### Geometric interpretation

Each factor in $Q$ reads geometrically:

See [Table 3](#tbl:spectral-decomposition-qvalue-table3-data).

The ratio $\hbar_q / \ln q = 0.9496$ is the **discretisation
correction**: the exceptional divisors are $q$-spaced (discrete),
not $e$-spaced (continuous).

### Shell correction proportions

The product $\prod F(\tau, N)$ reduces to two categorically defined
proportions for shells $\geq 5$ ($N > 28$):

**Degree-2 shell factor** ($F_{\mathrm{deg2}}$).
For shells at degree $2$ in the torus knot tower, the two embeddable
degree-$2$ knots $\tau(2,9)$ and $\tau(3,4)$ contribute a
**Rosso--Jones weighted average**:

$$
  F_{\mathrm{deg2}}
  = \frac{
      J(\tau(2,9)) \cdot \mathrm{tr}_M(\tau(2,9) \cdot \Delta_\beta)
    + J(\tau(3,4)) \cdot \mathrm{tr}_M(\tau(3,4) \cdot \Delta_\beta)
    }{
      \bigl(J(\tau(2,9)) + J(\tau(3,4))\bigr)
      \cdot \mathrm{tr}_M(\Delta_\beta)
    }
  \approx 0.5904
$$

where $J(\tau(r,s)) = \sum_{\lambda \vdash r} d_\lambda(q) \cdot \omega_\lambda^s$
is the Rosso--Jones invariant (quantum-dimension weighted trace of
the full twist on each irrep of $H_r(q)$), and $\Delta_\beta = T_{\mathrm{mix}} - T_{nn}$ is the beta-decay
difference operator.  The Rosso--Jones weights are the
[canonical inner product on $R(H_r(q))$](#prop:rj-canonical-inner-product),
forced by Schur orthogonality — they assign each degree-$2$ knot its
Rosso--Jones invariant $J(\tau)$ with zero fitting freedom.

At $q = q_0$:
$J(\tau(2,9)) \approx 2.167$ and $J(\tau(3,4)) \approx 5.794$
(computed from the Rosso--Jones expansion
$J(\tau(r,s)) = \sum_\lambda d_\lambda(q_0)\omega_\lambda^s$;
see `computations/qvalue-representation-theory.py`),
so $\tau(3,4)$ receives approximately $2.67\times$ the weight
of $\tau(2,9)$.

**Kummer tower decomposition.**
The two degree-$2$ knots correspond to the prime factorisation
of the Euler characteristic $|\chi(A)| = 6 = 2 \times 3$ through
the Kummer tower filtration
([Kummer filtration](#rem:kummer-filtration-obstruction)):

- $\tau(3,4)$ has $s = 4 = 2^2$ — the **$\mu_2$ branch** of the
  Kummer tower (even/odd parity);
- $\tau(2,9)$ has $s = 9 = 3^2$ — the **$\mu_3$ branch**
  (threefold symmetry).

The Chinese Remainder Theorem decomposition
$\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$
produces exactly these two independent components.
The Rosso--Jones weights are the quantum dimensions of the
corresponding Kummer components: $J(\tau(3,4)) > J(\tau(2,9))$
because the $\mu_2$ component (parity) has a larger quantum
dimension in the degree-$2$ representation ring than the
$\mu_3$ component (threefold symmetry).

**Pauli exclusion factor** ($F_{\mathrm{Pauli}}$).
For magic-number neutron shells ($N \in \{2, 8, 20, 28, 50, 82, 126\}$),
the filled shell projects onto the alternating irrep $(1^3)$ via the
Young symmetrizer $e_{(1^3)}$:

$$
  F_{\mathrm{Pauli}}
  = \frac{|\mathrm{tr}_{\mathrm{alt}}(\Delta_\beta)|}
         {|\mathrm{tr}(\Delta_\beta)|}
  = \frac{|\lambda_{\mathrm{alt}}|}{|\lambda_{\mathrm{sym}}|}
  \approx 0.6382
$$

where $\mathrm{tr}_{\mathrm{alt}}$ evaluates each Hecke word $w$ with
eigenvalue $(-q^{-1})^{\ell(w)}$ (alternating channel) and $\mathrm{tr}$
with $q^{\ell(w)}$ (symmetric channel).  This is the ratio of
alternating to symmetric eigenvalues of $\Delta_\beta$ in the
$6 \times 6$ regular representation of $H_3(q)$.

**Combined formula.**  For a $\beta^-$ decay with the converting
neutron in shell degree $d$ and neutron occupation parity $p$:

$$
  Q
  = \mathcal{Q}_{\mathrm{bare}}
    \times F_{\mathrm{deg2}}^{[d \geq 2]}
    \times F_{\mathrm{Pauli}}^{[N \in \mathrm{magic}]}
$$

where $[\cdot]$ is the Iverson bracket.  The proportion
$F_{\mathrm{deg2}} \times F_{\mathrm{Pauli}} = 0.5904 \times 0.6382 \approx 0.377$
applies to magic-number nuclei in heavy shells (e.g. ${}^{137}\mathrm{Cs}$
with $N = 82$).

### Error structure

Let $\varepsilon = \delta q / q \approx 1.2 \times 10^{-8}$
(CODATA).  The parametric error is $O(\varepsilon)$ (negligible).
The structural errors ($2$–$10\%$) are $O(1)$ relative to
$\varepsilon$: nucleon ordering in $\mathcal{Q}_{\mathrm{bare}}$,
degree-$2$ Rosso--Jones weighting over two knots, and the degree tower
truncation.  These do not arise from missing spectral
components — the decomposition is complete.

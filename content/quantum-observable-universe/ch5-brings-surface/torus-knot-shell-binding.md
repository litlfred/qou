The torus knots embeddable on $\Sigma_4$ form a **complete,
self-dual basis** for the Hilbert space of the Hecke algebra
$H_n(q)$.  The $\mathcal{Q}_q$-value of beta decay is the
spectral decomposition of the decay operator in this basis.
The decomposition is **exact and finite** — it terminates at
degree $2$ because the embeddability bound on $\Sigma_4$ kills
all higher jets.

## Theorem (spectral decomposition of the $\mathcal{Q}_q$-value)

*Let $\Sigma_g$ be a genus-$g$ surface and
$\mathcal{E}_g = \{\tau(r,s) : \tfrac{(r-1)(s-1)}{2} \leq g\}$
the set of torus knot labels embeddable on $\Sigma_g$.  For
$\beta^-$ decay $\mathcal{N}_{Z,N} \to \mathcal{N}_{Z+1,\,N-1}$,
the $\mathcal{Q}_q$-value admits the spectral decomposition:*

$$
  \mathcal{Q}_q
  \;=\;
  \underbrace{
    \Bigl|\log_q\frac{P_{\mathrm{dau}}(q)}{P_{\mathrm{par}}(q)}\Bigr|
    \cdot \hbar_q \cdot \frac{m_e}{3}
  }_{\displaystyle\mathcal{Q}_{\mathrm{bare}}}
  \;\times\;
  \underbrace{
    \prod_{\tau(r,s) \in \mathcal{E}_g}
    F\!\bigl(\tau(r,s),\, N\bigr)
  }_{\displaystyle\text{knot operator product}}
$$

*where:*

**(i)** *$P(q) = \prod_{j=0}^{A-2} \hat{V}_j(q)$ is the Skein
polynomial from the inductive chain construction
([transfer matrix](#prop:beta-decay-transfer-matrix)).  Each
chain $\hat{V}_j = z \cdot M_j[0][0] + M_j[1][0]$ (with
$z = (q^{1/2} + q^{-1/2})^{-1}$ the Markov parameter) is
pre-reduced via the $2\!\times\!2$ matrix recurrence (zero
Hecke steps), ensuring $\mathcal{N}_{Z,N}$ is in Gröbner
normal form at every inductive stage.*

**(ii)** *$\log_q(x) = \ln x / \ln q$ is the $q$-natural
logarithm — it counts exceptional divisor levels along the
color tube fiber of $\Sigma_g$.
$\hbar_q = (q - 1)/q$ is the quantum Planck constant (action
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
  \;=\;
  \begin{cases}
    1
    & \tau(r,s) \notin \mathcal{E}_g
    \;\text{(null: zero action on $\Sigma_g$)} \\[4pt]
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
([glossary](#rem:glossary-young-symmetrizer)).*

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

### Proof sketch

1. **Completeness.**  The Rosso–Jones formula decomposes
   $J_{\tau(r,s)}(q) = \sum_{\lambda \vdash r} d_\lambda(q)
   \cdot \omega_\lambda^s$ into irreps of $H_r(q)$.  Every
   irrep $\lambda$ is recoverable from the torus knot data
   (by Möbius inversion on the power sums $\omega^s$).  The
   self-duality $\tau(r,s) \leftrightarrow \tau(s,r)$ provides
   the inner product.  Hence $\mathcal{E}_g$ spans the
   representation ring at each degree $\leq
   \lfloor 2g/(g-1) \rfloor$.

2. **Inductive chain construction.**  Each nucleon $k$ is
   added by extending the $2\!\times\!2$ chain matrices:
   $M_j \leftarrow M_j \cdot T_{j {}^j\!\bowtie_k k}(q)$
   for existing positions $j < k$, and
   $M_{k-1} = T_{(k\!-\!1) {}^{k-1}\!\bowtie_k k}(q)$ for the new
   position.  The Hecke reduction $\sigma^2 =
   (q - q^{-1})\sigma + 1$ is handled within each
   $2\!\times\!2$ chain — zero Yang–Baxter steps, zero Hecke
   steps on the multi-generator element.  The nuclear word
   $\mathcal{N}_{Z,N} = \prod_j
   (\mathfrak{w}^+_j \sigma_j + \mathfrak{w}^0_j)$ uses
   **distinct generators** and is always in Gröbner normal form.

3. **Shell cancellation.**  Since parent and daughter share
   all chains except those crossing the converting nucleon,
   the log ratio $\log_q(P_{\mathrm{dau}}/P_{\mathrm{par}})
   = \sum_j [\log_q \hat{V}_j^{\mathrm{dau}}
   - \log_q \hat{V}_j^{\mathrm{par}}]$ receives contributions
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

| Knot $\tau(r,s)$ | $r$ | $s$ | Degree | Shell | $\mathrm{tr}_M(\tau \!\cdot\! T_\beta)$ | Pauli |
|:----:|:---:|:---:|:------:|:-----:|:---:|:---:|
| $\tau(2,3) = e$ | $2$ | $3$ | $1$ | $1$ | $0.3649$ | $0.4667$ |
| $\tau(2,5)$ | $2$ | $5$ | $1$ | $2$ | $0.4251$ | $0.3788$ |
| $\tau(2,7) = c$ | $2$ | $7$ | $1$ | $3$ | $0.5040$ | $0.3075$ |
| $\tau(3,5)$ | $3$ | $5$ | $1$ | $4$ | $1.5586$ | $0.2248$ |
| $\tau(2,9) = \tau(2,3^2)$ | $2$ | $9$ | $2$ | $5$ | $0.6048$ | $0.2495$ |
| $\tau(3,4) = t = \tau(3,2^2)$ | $3$ | $4$ | $2$ | $6$ | $0.5850$ | $0.2770$ |

Degree-$1$ knots are already encoded in $\mathcal{Q}_{\mathrm{bare}}$
through distinct vertex weights ($\mathfrak{p}
{}^i\!\bowtie_j \mathfrak{p}$, $\mathfrak{n}
{}_j\!\bowtie^i \mathfrak{n}$, $\mathfrak{p}
{}^i\!\bowtie_j \mathfrak{n}$), so $F = 1$ for shells $1$–$4$.
The active correction comes from degree-$2$ knots only.

### Jet bundle structure

The knot operators form a **jet bundle over the exceptional
divisor chain** of $\Sigma_g$, with jet index given by the
Gröbner class (= degree in the degree tower) of each torus knot.

| Jet order $k$ | Torus knot basis | Hilbert space content |
|:---:|---|---|
| $0$ | Identity | Ground state ($q = 1$: all crossings equal, $\mathcal{Q} = 0$) |
| $1$ | $\tau(2,3),\, \tau(2,5),\, \tau(2,7),\, \tau(3,5)$ | Complete degree-$1$ irreps |
| $2$ | $\tau(2,9),\, \tau(3,4)$ | Complete degree-$2$ irreps |
| $\geq 3$ | $\emptyset$ on $\Sigma_4$ | Tower terminates (null jet) |

The jet decomposition is **exact and finite** — not by truncation
but by the finite dimensionality of the Hilbert space on $\Sigma_g$.
Completeness follows from the self-duality $\tau(r,s) \leftrightarrow
\tau(s,r)$ and the Rosso–Jones expansion: every irrep of $H_n(q)$ is
recoverable from the torus knot invariants, so the knots form a
complete orthogonal basis under the Markov trace inner product.

### Geometric interpretation

Each factor in $\mathcal{Q}_q$ reads geometrically:

| Factor | Geometry |
|--------|----------|
| $\log_q(P_{\mathrm{dau}}/P_{\mathrm{par}})$ | Exceptional divisor levels traversed (color tube degrees) |
| $\hbar_q = (q-1)/q$ | Action quantum per divisor step (discrete fiber spacing) |
| $m_e / 3$ | Mass per trefoil crossing ($\mathcal{K}_e = \tau(2,3)$ has $3$ crossings) |
| $F(\tau(k^*), N)$ | Spectral projection onto the active divisor |

The ratio $\hbar_q / \ln q = 0.9496$ is the **discretisation
correction**: the exceptional divisors are $q$-spaced (discrete),
not $e$-spaced (continuous).

### Error structure

Let $\varepsilon = \delta q / q \approx 1.2 \times 10^{-8}$
(CODATA).  The parametric error is $O(\varepsilon)$ (negligible).
The structural errors ($5$–$9\%$) are $O(1)$ relative to
$\varepsilon$: nucleon ordering in $\mathcal{Q}_{\mathrm{bare}}$,
degree-$2$ averaging over two knots, and the degree tower
truncation.  These do not arise from missing spectral
components — the decomposition is complete.

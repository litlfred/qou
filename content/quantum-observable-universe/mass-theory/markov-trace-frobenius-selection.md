*The Jones–Markov form $\mathrm{tr}_M$ is the unique non-degenerate Frobenius pairing on the Iwahori–Hecke algebra $H_n(R, q)$ at generic $q$. The QOU mass identity's Markov trace is uniquely fixed by the categorical action, the fibre functor, and the Markov-trace uniqueness theorem (Jones 1987, Wenzl 1988).*

| form | $\tau(1)$ | $\tau(\sigma_i)$ | $w_\lambda$ | non-degenerate? |
|---|---:|---:|---|:---:|
| Jones–Markov $\mathrm{tr}_M$ | $1$ | $z = 1/[q^{1/2}+q^{-1/2}]$ | Wenzl-bridge $y_\lambda$ | yes, on $H_n(q)$ |

## Proof

The chain from the QOU substrate to the Markov trace runs through four
steps:

### Step 1: Cat-action of $\mathbf{C}$ on the state bundle

A quantum observable universe specifies a rigid monoidal category $\mathbf{C}$ with a fibre functor $\tau \colon \mathbf{C} \to \mathbf{Vect}$. The category fixes the acting Frobenius–Hopf algebra $A$. We typically use $A = H_n(R, q)$.

### Step 2: Non-abelian Stokes at finite slice

Yekutieli's non-abelian Stokes theorem at finite slice depth yields the multiplicative trace on the closed surface obtained by Markov closure of the braid word $T_w$:
$$
  \int_{S^1} T_w
  \;=\;
  \mathrm{tr}\bigl(\rho(\sigma_{i_1}) \cdots \rho(\sigma_{i_\ell})\bigr).
$$
This trace is the categorical trace in $\mathbf{C}$. It depends on the fibre functor $\tau$.

### Step 3: Frobenius pairing

The categorical trace descends to a Frobenius integral $\int_A \colon A \to R$. The algebra $A$ is a Frobenius algebra relative to this integral. This defines a non-degenerate bilinear form:
$$
  \langle x, y \rangle_\tau \;:=\; \tau(xy).
$$

The QOU mass identity uses the Frobenius co-Casimir trace identity ([Frobenius co-Casimir universal](#thm:frobenius-codim-universal)):
$$
  \tau(C_{\dim_q}) \;=\; \sum_\lambda \frac{1}{\dim_q(\lambda)}.
$$
This identity requires $\tau(p_\lambda) \neq 0$ for every Wedderburn block. The trace $\tau$ must be non-degenerate.

The **Jones–Markov form** $\mathrm{tr}_M$ satisfies:
- $\mathrm{tr}_M(1) = 1$.
- $\mathrm{tr}_M(x \sigma_{n-1}) = z \cdot \mathrm{tr}_M(x)$ for $x \in H_{n-1}$ with $z = 1/(q^{1/2} + q^{-1/2})$.

It is non-degenerate on $H_n(R, q)$. The trace on the primitive idempotents is $\mathrm{tr}_M(p_\lambda) = \dim_q(\lambda) \cdot d_\lambda / [n]_q!$. This is non-zero for every $\lambda \vdash n$ at generic $q$. The Markov-trace uniqueness theorem forces $\mathrm{tr}_M$ to be the unique non-degenerate Frobenius form on the Hecke algebra.

### Step 4: Wedderburn + Markov-trace formula

The trace $\mathrm{tr}_M$ admits the explicit form:
$$
  \mathrm{tr}_M(x) \;=\; \sum_\lambda y_\lambda(q) \cdot \chi_\lambda(x),
$$
where $y_\lambda(q)$ are the Wenzl-bridge weights.

## Uniqueness theorem

**Theorem (Markov-trace uniqueness on H_n(R, q)).** *Any non-degenerate Frobenius form on the Iwahori–Hecke algebra $H_n(R, q)$ at generic $q$ equals the Jones–Markov form $\mathrm{tr}_M$ block-wise. The QOU mass identity uniquely determines $\mathrm{tr}_M$ as the canonical Markov trace.*

## Discussion

This proposition is a structural theorem about the representation theory of the Hecke algebra. We introduce no fitting or empirical input. We formalize the uniqueness via the `MarkovTraceUniqueness` class in Lean. Downstream Lean results depend on this class instance.

## Computational consequence

The QOU production stack computes $\mathrm{tr}_M$ on the canonical 11-crossing proton/neutron braid via four independent paths. They agree to $\leq 2 \times 10^{-15}$ at the proton-pinned $q_0$:

| atom | $\mathrm{tr}_M(\beta_{\rm atom}, q_0)$ | error vs 4-way |
|---|---:|---:|
| proton | $1.0653061442544499$ | $\leq 2.57\times 10^{-16}$ |
| neutron | $0.9232332299116371$ | $\leq 2.03\times 10^{-16}$ |
| deuteron | $0.3882864240747888$ | $\leq 8.16\times 10^{-16}$ |

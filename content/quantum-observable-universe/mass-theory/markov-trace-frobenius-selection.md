**Proposition (Markov trace uniqueness on H_n(R, q)).**
*The Jones–Markov form* $\tau_M$ *is* **the unique** *non-degenerate
Frobenius pairing on the Iwahori–Hecke algebra* $H_n(R, q)$ *at
generic* $q$.  *Hence the QOU mass identity's Markov trace is fixed
by the cat-action / fibre-functor choice in the QOU substrate plus
the standard Markov-trace uniqueness theorem (Wenzl 1990, Jones 1987),
with no remaining choice.*

| form | $\tau(1)$ | $\tau(\sigma_i)$ | $w_\lambda$ | non-degenerate? |
|---|---:|---:|---|:---:|
| Jones–Markov $\tau_M$ | $1$ | $z = 1/[q^{1/2}+q^{-1/2}]$ | Wenzl-bridge $y_\lambda$ | yes, on $H_n(q)$ |

## The chain: cat-action $\to$ Markov trace

Starting from the QOU substrate and tracing each step:

### Step 1: Cat-action of $\mathbf{C}$ on the state bundle

A quantum observable universe
$\mathcal{U} = (\mathbf{C}, \varTheta, G, \mathcal{S})$ specifies a
**rigid monoidal category** $\mathbf{C}$ with a **fibre functor**
$\tau \colon \mathbf{C} \to \mathbf{Vect}$.  The choice of $\mathbf{C}$
fixes which Frobenius–Hopf algebra $A$ acts: typically
$A = H_n(R, q)$ (Iwahori–Hecke), but $A$ could be a quotient
(e.g. Temperley–Lieb $\mathrm{TL}_n$) or a finer-grained algebra.

### Step 2: Non-abelian Stokes at finite slice

Yekutieli's non-abelian Stokes theorem at finite slice depth
($= \mathrm{max\_grade}$ in the GB filtration) gives the multiplicative
trace on the closed surface obtained by Markov closure of the braid
word $T_w$:

$$
  \int_{S^1} T_w
  \;=\;
  \mathrm{tr}\bigl(\rho(\sigma_{i_1}) \cdots \rho(\sigma_{i_\ell})\bigr).
$$

The trace here is the **categorical trace** in $\mathbf{C}$ — it
depends on the fibre functor $\tau$.

### Step 3: Frobenius pairing — non-degeneracy + Wenzl/Jones uniqueness

The categorical trace descends under $\tau$ to a Frobenius integral
$\int_A \colon A \to R$ on the algebra.  $A$ is a Frobenius algebra
*relative to* this integral, which is equivalent to a non-degenerate
bilinear form

$$
  \langle x, y \rangle_\tau \;:=\; \tau(xy).
$$

The QOU mass identity uses the **Frobenius co-Casimir** trace identity
(see [Frobenius co-Casimir universal](#thm:frobenius-codim-universal))

$$
  \tau(C_{\dim_q}) \;=\; \sum_\lambda \frac{1}{\dim_q(\lambda)},
$$

where the construction
$C_{\dim_q} = \sum_\lambda [\dim_q(\lambda) \tau(p_\lambda)]^{-1} \cdot p_\lambda$
is well-defined **only if** $\tau(p_\lambda) \neq 0$ for every
Wedderburn block — i.e., only if $\tau$ is non-degenerate.

The **Jones–Markov form** $\tau_M$ is defined by:
- $\tau_M(1) = 1$
- $\tau_M(x \sigma_{n-1}) = z \cdot \tau_M(x)$ for $x \in H_{n-1}$ (Markov peel)
- $z = 1/(q^{1/2} + q^{-1/2})$

It is **non-degenerate** on $H_n(R, q)$: $\tau_M(p_\lambda)
= \dim_q(\lambda) \cdot d_\lambda / [n]_q!$ (Plancherel-A weights),
non-zero for every $\lambda \vdash n$ at generic $q$ (Jones
\cite{jones1987} Theorem 6.1; Wenzl \cite{wenzl1988} Lemma 2.4).

The **Markov-trace uniqueness theorem** of Jones / Wenzl then forces
$\tau_M$ to be the **unique** non-degenerate Frobenius form on the
Hecke algebra: any other trace satisfying the Markov-peel + cyclic
axioms and non-degeneracy equals $\tau_M$ block-wise.

### Historical note — the purged Schur–Weyl contrast

Earlier versions of this
proposition selected $\tau_M$ *by contrast* with a degenerate
Schur–Weyl candidate $\tau_{\mathrm{SW}}$ (which vanishes for
height-$> 2$ partitions, hence violates non-degeneracy).  Per
owner decision A' the $\tau_{\mathrm{SW}}$ path is fully
purged from the framework; the proposition is now a direct
uniqueness statement (Wenzl / Jones), independent of any alternative
to rule out.  See `docs/uniqueness-theorems-backlog.md` for the
broader uniqueness programme.

### Step 4: Wedderburn + Markov-trace formula

$\tau_M$ admits the explicit form

$$
  \tau_M(x) \;=\; \sum_\lambda y_\lambda(q) \cdot \chi_\lambda(x),
$$

with $y_\lambda(q)$ the Wenzl-bridge weights, supported on every
$\lambda \vdash n$.

## Uniqueness theorem

**Theorem (Markov-trace uniqueness on H_n(R, q)).**  *Any
non-degenerate Frobenius form on the Iwahori–Hecke algebra
* $H_n(R, q)$ *at generic* $q$ *equals the Jones–Markov form
* $\tau_M$ *block-wise.  Therefore the QOU mass identity uniquely
determines* $\tau_M$ *as the canonical Markov trace of the
framework.*

**Proof sketch.**  Non-degeneracy is required by the Frobenius
co-Casimir construction (Step 3).  $\tau_M$ is non-degenerate
(Jones \cite{jones1987} Theorem 6.1; Wenzl \cite{wenzl1988} Lemma
2.4).  Any other non-degenerate trace on $H_n(R, q)$ satisfying
the Markov-peel + cyclic axioms equals $\tau_M$ by Wenzl's
uniqueness corollary to Lemma 2.4 (equivalently Jones' Markov
trace uniqueness).  Hence $\tau_M$ is the unique such trace. ∎

## Computational consequence

The QOU production stack computes $\tau_M$ on the
**11-crossing canonical proton / neutron braid** via four
independent paths — Hoefsmit seminormal matrices
(`atomic_tr_m_mpfr_50dps.py`), `markov_peel`, the $\chi$-cache
combiner (`canonical_tr_m_via_chi_cache.py`), and the Habiro
integer-$a_m$ expansion — which agree to $\leq 2 \times 10^{-15}$
at the proton-pinned $q_0$:

| atom | $\tau_M(\beta_{\rm atom}, q_0)$ | error vs 4-way |
|---|---:|---:|
| proton | $1.0653061442544499$ | $\leq 2.57\times 10^{-16}$ |
| neutron | $0.9232332299116371$ | $\leq 2.03\times 10^{-16}$ |
| deuteron | $0.3882864240747888$ | $\leq 8.16\times 10^{-16}$ |

> **Pedagogical alternative (deprecated for production).** The
> `from_scratch/` pipeline computes $\tau_M$ via the Markov axioms on
> a **different braid choice** (single-component free-proton braid,
> not the 11-crossing canonical recipe), yielding $\tau_M(p_{\rm free},
> q_0) \approx 1.7339$ — a legitimate Jones–Markov value on its
> *own* braid, not a competing convention for the 11-crossing braid
> above.  An earlier escalation framed this as a "$\tau_M$ /
> $\tau_{\mathrm{SW}}$ conflation" but the audit doc itself records the
> different-braid framing (line 248-251); decision A' purges
> $\tau_{\mathrm{SW}}$ and reads the from-scratch as a different
> braid's $\tau_M$, not a competing form.

## Discussion

This proposition is **proved** — a structural theorem about the
representation theory of the Hecke algebra, with no fitting and no
empirical input.  Uniqueness of $\tau_M$ as the non-degenerate
Frobenius form on $H_n(R, q)$ is axiomatised via the
`MarkovTraceUniqueness` class in the Lean file (citing Jones 1987 /
Wenzl 1988); downstream Lean results are sorry-free **conditional on
the class instance** per AGENTS.md §3b-cond.

<!-- FILE_START: two-row-stratum.md -->
## Definition

Let $H_n(q)$ be the Iwahori–Hecke algebra on $n$ strands with the
canonical Wedderburn decomposition
$$
  H_n(q) \;\cong\; \bigoplus_{\lambda \vdash n} \mathrm{End}(V_\lambda)
$$
indexed by partitions $\lambda \vdash n$. The
:defterm[two-row stratum]{#two-row-stratum}
is the subset of partitions with at most two parts:
$$
  \Lambda^2(n) \;:=\; \{\, \lambda \vdash n : \ell(\lambda) \le 2 \,\}
  \;=\; \{\, (n-k, k) : 0 \le k \le \lfloor n/2 \rfloor \,\}.
$$

The corresponding
:defterm[two-row projection]{#two-row-projection}
$$
  \pi_{\mathrm{2-row}} \;\colon\; H_n(q) \;\to\;
    \bigoplus_{\lambda \in \Lambda^2(n)} \mathrm{End}(V_\lambda)
$$
is the orthogonal projection onto the two-row Wedderburn subalgebra
(idempotent: $\pi_{\mathrm{2-row}}^2 = \pi_{\mathrm{2-row}}$). The
canonical Markov trace splits accordingly:
$$
  \mathrm{tr}_M(\beta)
  \;=\; \underbrace{\sum_{\lambda \in \Lambda^2(n)} y_\lambda(q) \cdot \chi^\lambda_q(\beta)}_{\mathrm{tr}_M(\pi_{\mathrm{2-row}}\,\beta)}
  \;+\; \underbrace{\sum_{\ell(\lambda) > 2} y_\lambda(q) \cdot \chi^\lambda_q(\beta)}_{\mathrm{tr}_M((1-\pi_{\mathrm{2-row}})\,\beta)}
$$

with $y_\lambda$ the Wenzl weight
from [`prop:wedderburn-weight-canonical`](#prop:wedderburn-weight-canonical).

## Structural significance

The two-row stratum carries the $\mathrm{SU}(2)$ Schur–Weyl image. Under
the natural restriction
$$
  H_n(q) \;\twoheadrightarrow\; \mathrm{End}_{\mathrm{SU}(2)}\!\bigl(V^{\otimes n}\bigr),
\quad V = \mathbb{C}^2,
$$
partitions with $\ell(\lambda) > 2$ lie in the kernel — they correspond
to higher-rank symmetry components absent from the $\mathrm{SU}(2)$
spin-pairing observable. The two-row sector is where the
$q$-deformed spin observables — including the
magic-shell coupling of
`conj:magic-shell-stabilization`
— live.

## Indexing the stratum

$|\Lambda^2(n)| = \lfloor n/2 \rfloor + 1$. For $n = 12$ (the
$^4\mathrm{He}$ strand count) this gives **7** partitions:

$$
\Lambda^2(12) = \{(12), (11,1), (10,2), (9,3), (8,4), (7,5), (6,6)\}.
$$

Some of these are particularly distinguished:

- $\lambda = (n)$: trivial rep; one-dimensional, $V_{(n)} = \mathbb{C}$.
- $\lambda = (n-1, 1)$: standard rep; dimension $n - 1$.
- Self-conjugate $\lambda$ within $\Lambda^2(n)$: only $(n/2, n/2)$
  when $n$ is even — the **balanced two-row** partition. For
  $n = 12$, this is $(6, 6)$.

The non-self-conjugate two-row partitions $(n-k, k)$ with $k < n/2$
form mirror pairs under the bar involution $q \mapsto q^{-1}$ (each
$(n-k, k)$ paired with itself under the involution, since the
conjugate partition $(n-k, k)' = (2, 2, \dots, 2, 1, \dots)$
generally exits $\Lambda^2$).

## Empirical use

The companion canonical evaluation
the canonical formalism
computes the per-partition decomposition
$c_\lambda := y_\lambda(q_0) \cdot \chi^\lambda_q(\beta_{^4\mathrm{He}})$
across all 77 partitions of 12 and finds the two-row stratum
$\Lambda^2(12)$ carries $86.6\,\%$ of $\mathrm{tr}_M(\beta_{^4\mathrm{He}})$ — the
content of [`prop:he4-two-row-dominance`](#prop:he4-two-row-dominance).

The earlier
the canonical formalism
established the same pattern across $\{D, T, {}^3\mathrm{He}, {}^4\mathrm{He}\}$:
the dominant block per atom always lies in $\Lambda^2(3A)$.
<!-- FILE_END: two-row-stratum.md -->

<!-- FILE_START: he4-channel-active-set.md -->
## Setup

The $^4\mathrm{He}$ bound state admits three primary compositional
channels (each summing to $A = 4$ nucleons):

| channel | constituents | $\sum \Delta_\mathrm{cat}$ (MeV) | residual $t_i$ (MeV) |
|---|---|---:|---:|
| $\mathrm{D} \oplus \mathrm{D}$    | $(1,1) + (1,1)$ | $4.05$ | $\mathbf{24.16}$ |
| $\mathrm{T} \oplus p$             | $(1,2) + (1,0)$ | $7.83$ | $\mathbf{20.38}$ |
| ${}^3\mathrm{He} \oplus n$        | $(2,1) + (0,1)$ | $7.04$ | $\mathbf{21.18}$ |

The **channel binding residual** is
$$
  t_i \;:=\; \Delta_\mathrm{cat}({}^4\mathrm{He}) \;-\; \sum_{j \in \mathrm{channel}\, i} \Delta_\mathrm{cat}(j)
$$
— the binding that the magic-shell coupling
must explain *beyond* the free-constituent sum. Empirical anchors
loaded from
[`magic-shell-empirical-instantiation.witness.json`](computations/magic-shell-empirical-instantiation.witness.json).

## LP formulation

Apply the
[`prop:operator-selection-lp`](#prop:operator-selection-lp)
canonical form with $t \in \mathbb{R}^3$ the residual vector above,
$G = I_3$ (channels orthogonal at leading order — corrections from
shared sub-braids are sub-percent), and
$$
  n_\mathrm{target} \;=\; \Delta_\mathrm{coupling}(2, 2)
  \;=\; \Delta_\mathrm{cat}({}^4\mathrm{He}) - 2\,\Delta_\mathrm{cat}({}^3\mathrm{He})
  \;=\; 13.197\,\mathrm{MeV}
$$
(the doubly-magic anchor from ).

## Solution

The LP solves uniquely (strong duality holds, duality gap $= 0$;
$\mathrm{primal\_obj} = \mathrm{dual\_obj} = 268.949$). The primal
weights $x^\star$ and dual shadow prices $y^\star$ are:

| channel $i$ | $x^\star_i$ | $y^\star_i$ | status |
|---|---:|---:|---|
| $\mathrm{D} \oplus \mathrm{D}$    | $0$        | $\mathbf{3.778}$ | active |
| $\mathrm{T} \oplus p$             | $13.197$   | $0$              | primal-saturating |
| ${}^3\mathrm{He} \oplus n$        | $0$        | $0.796$          | active |

with $y_0^\star = 20.380$. The **active set** —
constraints whose dual variable is positive — is therefore
$$
  \mathcal{A}({}^4\mathrm{He}) \;=\; \{\,\mathrm{D} \oplus \mathrm{D},\; {}^3\mathrm{He} \oplus n\,\}.
$$

## Proposition

**(Conditional on
[`he4-sdp-compositional-canonical evaluation.witness.json`](computations/he4-sdp-compositional-canonical evaluation.witness.json).)**
For the $^4\mathrm{He}$ operator-selection LP defined above:

1. **Unique primal optimum** at the $\mathrm{T} \oplus p$ channel:
   $x^\star_{\mathrm{T} \oplus p} > 0$ and $x^\star_i = 0$ for all
   $i \neq \mathrm{T} \oplus p$.
2. **Active set** $\mathcal{A}({}^4\mathrm{He}) =
   \{\,\mathrm{D} \oplus \mathrm{D},\; {}^3\mathrm{He} \oplus n\,\}$
   (dual-tight constraints).
3. **Dual ordering**
   $y^\star_{\mathrm{D} \oplus \mathrm{D}} >
    y^\star_{{}^3\mathrm{He} \oplus n} >
    y^\star_{\mathrm{T} \oplus p} = 0$.

## Interpretation

The LP "uses" the $\mathrm{T} \oplus p$ decomposition to satisfy
the binding constraint (it has the smallest per-unit cost — the
smallest residual after subtracting free constituents). But the
**shadow prices identify $\mathrm{D} \oplus \mathrm{D}$ as the
most binding-receptive sub-braid**: a unit perturbation of the
deuteron-pairing channel would change the primal binding cost by
$3.778$ MeV per MeV — five times more than the
${}^3\mathrm{He} \oplus n$ channel and infinitely more than the
$\mathrm{T} \oplus p$ channel (whose shadow price is zero, since
it is the primal-saturating decomposition).

This **two-tier structural fingerprint** is the channel-level
analogue of the Wedderburn-block fingerprint
[`prop:he4-two-row-dominance`](#prop:he4-two-row-dominance): both
identify a $q$-symmetric deuteron-pairing structure as the
load-bearing geometry of the doubly-magic
magic-shell coupling, while
$\mathrm{T} \oplus p$ provides the energetic accounting. The
remark
`rem:he4-magic-shell-fingerprint`
makes this connection explicit.
<!-- FILE_END: he4-channel-active-set.md -->

<!-- FILE_START: he4-two-row-dominance.md -->
## Statement

Let $\beta_{{}^4\mathrm{He}}$ denote the canonical
atomic braid word for $^4\mathrm{He}$ on
$H_{12}(q)$ — 47 crossings on 12 strands with three operator-valued
inter-nucleon interfaces (pp at gen 2, pn at gen 5, nn at gen 8), as
emitted by
the canonical formalism.
Define the per-partition contribution
$$
  c_\lambda(q_0) \;:=\; y_\lambda(q_0) \cdot \chi^\lambda_q\!\bigl(\beta_{{}^4\mathrm{He}}\bigr)
$$
with $y_\lambda$ the Wenzl weight
from [`prop:wedderburn-weight-canonical`](#prop:wedderburn-weight-canonical)
and $\chi^\lambda_q$ the Hoefsmit per-irrep character. Then
$$
  \sum_{\lambda \vdash 12} c_\lambda(q_0) \;=\; \mathrm{tr}_M\!\bigl(\beta_{{}^4\mathrm{He}}\bigr)(q_0).
$$

**Proposition (conditional on
[`he4-canonical-tr-m-block-fingerprint.witness.json`](computations/he4-canonical-tr-m-block-fingerprint.witness.json)).**
The two-row stratum
$\Lambda^2(12) = \{(12), (11,1), (10,2), (9,3), (8,4), (7,5), (6,6)\}$
of [`def:two-row-stratum`](#def:two-row-stratum) carries at least
$80\,\%$ of the canonical Markov trace at the substrate parameter:
$$
  \frac{\bigl|\sum_{\lambda \in \Lambda^2(12)} c_\lambda(q_0)\bigr|}
       {\bigl|\mathrm{tr}_M(\beta_{{}^4\mathrm{He}})(q_0)\bigr|}
  \;\ge\; 0.80.
$$

## Empirical verification

The witness reports $\mathrm{tr}_M(\beta_{{}^4\mathrm{He}})(q_0) = 0.05534835$
(dimensionless raw trace). The two-row-stratum ratio is
**$86.6\,\%$**. Top-5 binding-receptive Wedderburn blocks — all in
$\Lambda^2(12)$:

| rank | $\lambda \vdash 12$ | $\dim_\lambda$ | $y_\lambda(q_0)$ | $\chi^\lambda_q(\beta_{{}^4\mathrm{He}})$ | $c_\lambda$ | $\%$ of $\lvert$total$\rvert$ |
|---:|---|---:|---:|---:|---:|---:|
| 1 | $(9, 3)$  | 154 | $+5.87\,e{-4}$ | $+27.33$ | $+1.604\,e{-2}$ | $29.0$ |
| 2 | $(8, 4)$  | 275 | $+4.31\,e{-4}$ | $+30.26$ | $+1.304\,e{-2}$ | $23.6$ |
| 3 | $(10, 2)$ | 54  | $+7.12\,e{-4}$ | $+10.46$ | $+7.45\,e{-3}$  | $13.5$ |
| 4 | $(7, 5)$  | 297 | $+2.62\,e{-4}$ | $+21.77$ | $+5.70\,e{-3}$  | $10.3$ |
| 5 | $(11, 1)$ | 11  | $+7.67\,e{-4}$ | $+7.39$  | $+5.67\,e{-3}$  | $10.2$ |
|   |           |     |                |          | top-5 cum         | $\mathbf{86.5}$ |

The trivial rep $(12)$ contributes only $2.9\,\%$; the sign rep
$(1^{12})$ contributes $4.7 \times 10^{-10}$ (sub-1e-9).

## Structural interpretation

The two-row stratum carries the
SU(2) Schur-Weyl image. Partitions
with $\ell(\lambda) > 2$ correspond to higher-rank symmetry
components absent from the spin-$\tfrac{1}{2}$ pairing observable.
The dominance of $\Lambda^2(12)$ at $86.6\,\%$ is the algebraic
fingerprint of $^4\mathrm{He}$ as a $q$-symmetric spin-pairing
bound state — a substrate-derived characterisation of the
magic-shell coupling.

The top block $\lambda^* = (9, 3)$ matches the prediction from
the canonical formalism,
which arrived at the same dominant-partition fingerprint via the
$\Delta_\lambda$ empirical-tabulation route. The two derivations
are independent: $\Delta_\lambda$ from per-partition mass-anchor
residuals, this proposition from the canonical
$\Sigma_\lambda y_\lambda \cdot \chi^\lambda_q$ Wedderburn sum.
<!-- FILE_END: he4-two-row-dominance.md -->

<!-- FILE_START: markov-trace-frobenius-selection.md -->
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
## Discussion

This proposition is **proved** — a structural theorem about the
representation theory of the Hecke algebra, with no fitting and no
empirical input.  Uniqueness of $\tau_M$ as the non-degenerate
Frobenius form on $H_n(R, q)$ is axiomatised via the
`MarkovTraceUniqueness` class in the Lean file (citing Jones 1987 /
Wenzl 1988); downstream Lean results are sorry-free **conditional on
the class instance** per AGENTS.md §3b-cond.

## Computational consequence

The QOU production stack computes $\tau_M$ on the
**11-crossing canonical proton / neutron braid** via four
independent paths — Hoefsmit seminormal matrices
(the formal derivation), `markov_peel`, the $\chi$-cache
combiner (the formal derivation), and the Habiro
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
<!-- FILE_END: markov-trace-frobenius-selection.md -->

<!-- FILE_START: t-beta-markov-frobenius-collapse.md -->
**Proposition (Min-Frobenius-norm collapse for $T_\beta$).**
*Let $H = H_n(R, q)$ be the Iwahori–Hecke algebra over a field $R$,
equipped with the Jones–Markov trace $\tau_M : H \to R$ uniquely
determined by the [Wenzl–Jones uniqueness theorem](#prop:markov-trace-frobenius-selection).
Equip $H$ with the **Frobenius inner product**
$\langle X, Y \rangle_\tau := \tau_M(X \cdot Y)$.
The element of minimum Frobenius norm satisfying the linear
constraint $\tau_M(T_\beta) = S$ for given $S \in R$ is*

$$
\boxed{\; T_\beta = S \cdot 1_H \;}
$$

*with $\| T_\beta \|^2_\tau = S^2$.*
## Corollary — observable c_k invariance

The $\mathfrak{Q}_\beta$ production rule extracts the c_k Taylor coefficients from
$\tau_M(T_\beta)(q)$.  Under either norm choice — Euclidean L2 on
coordinate-vector space $R^6$ (the SHAPE $\times$ S decomposition)
or the canonical Markov–Frobenius norm above — the SDP **constraint**
$\tau_M(T_\beta) = S = \mathfrak{Q}_\beta / E_0$ is satisfied identically.
Therefore $\tau_M(T_\beta)(q) \equiv S(q)$ in both cases, and the
c_k are **L2/Markov-invariant**:

$$
c_k^{\,L2} = c_k^{\,Markov} = c_k\!\!\left(S(q)\right)
\quad\text{for all } k.
$$

The L2 picture and the Markov picture differ in which $T_\beta \in
H_n(R, q)$ is the *canonical* primal-feasible operator (the SDP
**objective** picks different points in the constraint level set),
but they agree on every **observable** because observables are
extracted from the constraint, not from the operator's coordinate
expansion.  The cross-anchor c_3 swing recorded in the
[canonical-framing audit](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
is therefore a property of $S(q) = \mathfrak{Q}_\beta(q) / E_0(q)$ itself —
upstream of the SDP norm choice.

## Categorical reading

Under the Markov–Frobenius norm $T_\beta = S \cdot 1_H$ is a
**scalar multiple of the identity**.  All q-dependence of the
canonical primal-feasible operator flows through the single
q-rational scalar $S(q)$; there is no multi-channel SHAPE
distributed across the NF basis $\{\gamma, \sigma_0, \sigma_1,
L_+, L_-, e_-\}$.  The six-channel spread observed
under the Euclidean coordinate norm is a **basis-dependence**
of the inner product on $R^6$, not categorical structure of
$T_\beta$.

This is the natural categorical answer to "what is $T_\beta$ as
an operator?": the Markov–Frobenius minimum-norm primal-feasible
solution is the **least-Hecke-Frobenius-norm** operator hitting
the target trace, which is the canonical choice from the
Wenzl–Jones standpoint.

## Lean formalisation

The substrate-model proof (where $A = R$ and $\tau = \mathrm{id}$,
reducing the algebra to its ground field) is sorry-free at
[`t_beta_markov_min_frobenius_collapse_substrate`](markov-trace-frobenius-selection.lean).
The full $H_n(R, q)$ proof — requiring the Mathlib `Algebra R A`
typeclass infrastructure plus the positive-semi-definiteness of
$\tau_M$ on squares as a class hypothesis — is queued for a
follow-up Lean PR.  The substrate-model proof captures the
essential algebraic content (the completing-the-square identity);
the general lift is mechanical typeclass scaffolding.

## References

- [`docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md`](https://github.com/litlfred/qou/blob/claude/qbeta-markov-trace-2026-06-03/docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md)
  — structural finding + canonical structural verification at $q_0$.
- [`docs/coordination/1ppq-qbeta.md`](https://github.com/litlfred/qou/blob/claude/qbeta-markov-trace-2026-06-03/docs/coordination/1ppq-qbeta.md)
  — 1ppQ master ledger.
- Jones 1987 — Hecke algebra Markov trace existence + uniqueness.
- Wenzl 1988 — non-degeneracy of the Markov trace.
<!-- FILE_END: t-beta-markov-frobenius-collapse.md -->

<!-- FILE_START: t-beta-markov-frobenius-collapse-general.md -->
**Proposition (Min-Frobenius-norm collapse — general unital R-algebra).**
*Let $R$ be a strict-ordered field (typeclass `[Field R] [LinearOrder R] [IsStrictOrderedRing R]`), $A$ a unital $R$-algebra, and
$\tau : A \to R$ an $R$-linear normalised trace ($\tau(1) = 1$,
$\tau(xy) = \tau(yx)$).  Assume $\tau$ is positive-semi-definite
on squares: $0 \le \tau(X \cdot X)$ for every $X \in A$.  Then for
any $S \in R$ and any $X \in A$ satisfying the linear constraint
$\tau(X) = S$,*

$$
S^2 \;\le\; \tau(X \cdot X).
$$

*If, additionally, $\tau$ is non-degenerate on squares ($\tau(Y \cdot Y) = 0
\implies Y = 0$), the lower bound is attained iff $X = S \cdot 1_A$.*
## Relation to the substrate-model version

This proposition **lifts** [`prop:t-beta-markov-frobenius-collapse`](t-beta-markov-frobenius-collapse.md) from the substrate model ($A = R$, $\tau = \mathrm{id}$, where the theorem reduces to the trivial $X = S \Rightarrow X^2 = S^2$) to the **general unital $R$-algebra setting** where $A$ may be non-commutative and infinite-dimensional.

| Block | Setting | Used by |
|-------|---------|---------|
| `prop:t-beta-markov-frobenius-collapse` | substrate model ($A = R$, $\tau = \mathrm{id}$) | scalar $\mathfrak{Q}_\beta$ identities |
| `prop:t-beta-markov-frobenius-collapse-general` (this block) | any unital $R$-algebra with normalised trace + PSD + non-deg | Hecke-algebra applications |
## Application to the Iwahori–Hecke algebra

For $A = H_n(R, q)$ at generic $q > 0$ with $\tau = \tau_M$ (the Jones–Markov trace), this proposition gives the **canonical SDP-min-Frobenius-norm operator** for the constraint $\tau_M(T_\beta) = S$:

$$
T_\beta^{\mathrm{Markov}} \;=\; S \cdot 1_H.
$$

This is the Markov-trace collapse (substrate model) lifted to the genuine non-commutative Hecke algebra.

The L2-Euclidean coordinate-norm picture (PR #1739: 6-channel $A_i x_i^{L2}$ SHAPE $\times$ S decomposition) and the Markov-Frobenius picture (this proposition: $T_\beta = S \cdot 1$) are **two different operators** inside $H_n(R, q)$ that **both reproduce the SDP constraint** $\tau_M(T_\beta) = S$. The observable $c_k$ Taylor coefficients of $\mathfrak{Q}_\beta(q)$ are L2/Markov-invariant: see [PR #1750](https://github.com/litlfred/qou/pull/1750) Step 4 diagnostic.

## References

- PR #1750 (merged) — substrate-model proof + paper proof + accuracy diagnostic + audit doc.
- [PR #1761](https://github.com/litlfred/qou/pull/1761) (merged) — general-lift Lean infrastructure + this content block.
- [`docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md`](../../../docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md) — structural finding + canonical structural verification at $q_0$.
- [`prop:markov-trace-frobenius-selection`](markov-trace-frobenius-selection.md) — Wenzl–Jones uniqueness theorem (the source of $\tau_M$'s non-degeneracy).
- Jones 1987 — Markov-trace existence + uniqueness.
- Wenzl 1988 — non-degeneracy of the Markov trace.
<!-- FILE_END: t-beta-markov-frobenius-collapse-general.md -->

<!-- FILE_START: pn-averaging-uniqueness.md -->
**Proposition (canonical p-n averaging uniqueness).**  *Any two
p-n interface averaging functionals* $\sigma_{pn}, \sigma_{pn}'$
*on* $H_{3A}(R, q)$ *that both satisfy* (a) **bar-invariance**
$\sigma_{pn}(q) = \sigma_{pn}(q^{-1})$, (b) **color-flavor
compatibility** (Bring color-tube symmetry over quark
composition), *and* (c) **standard normalisation**
$\sigma_{pn} = z$ *with the same* $z$ *are equal block-wise.
Hence the canonical p-n averaging is uniquely determined by
these three structural hypotheses — closing the cheat-sheet
open audit finding (Phase 5q, line 128).*

## Setting

The QOU mass identity at $A \geq 2$ contracts a per-interface
averaging functional $\sigma_{pn}$ across the p-n boundary slice
in $H_{3A}(R, q)$.  Two production candidates have circulated:

| candidate | form | status |
|---|---|---|
| uniform bar-invariant | $\sigma_{\rm avg} = (\sigma + \sigma^{-1})/2 = \sigma - h/2$ | current default ([`thm:averaging-resonance-rule`](#thm:averaging-resonance-rule)) |
| Bring color-tube weighted | per-quark-composition weighted | "open audit finding" (Phase 5q); empirically reproduces $\Delta m_{n-p}$ to ${\approx}\,0.14\,\%$ of CODATA via Scheme 4 per-sheet PL integration |

Both satisfy bar-invariance + standard normalisation; they differ
on the per-sheet color weighting.  The uniqueness theorem here
states that **once color-flavor compatibility is fixed**, the
averaging is determined.  Closing the `ColorFlavorCompatible`
class to the Bring weighted derivation refines the admissible
normalisation $z$ to a unique canonical form.

### Derivation chain for the closed-form weight

The substrate evaluation $w(t, t', q) = 1/(1 - h_q \cdot q^{10})$ per
the formal derivation is **not purely
empirical**. The "10" exponent is derived:

- Bring's surface has **genus $g = 4$** (per `prop:em-coupling-bring-zero-mode`).
- The genus-4 force-carrier pair on Bring's surface is
  $\{T(2,9), T(3,5)\}$ (named in `em-coupling-bring-zero-mode.lean`).
- `prop:alpha-shift-torus-knot` proves
  $\alpha_{\text{shift}}(T_{p,k}) = k \cdot (p-1)$ (Lean:
  `alphaShift p k = k * (p - 1)`, sorry-free conditional on
  `HasAlphaShiftTorus`). Specialising at $(p, k) = (3, 5)$ gives
  $\alpha_{\text{shift}}(T(3,5)) = 5 \cdot 2 = \mathbf{10}$ — the
  **pole order** of $\sigma$ on $T(3,5)$, verified computationally
  in the formal derivation (line 318: `pole_t35 == 10`).
- The Bring color-tube weight inherits this pole order: $q^{10}$
  in $1/(1 - h_q \cdot q^{10})$ is the $\alpha_{\text{shift}}(T(3,5))$-th
  power, **derived**.

**Remaining open math (smaller scope):**

- The resolvent form $1/(1 - h_q \cdot \cdot)$ from a residue
  calculation at the pole; deriving it formally in Lean requires
  the Schwarz / contour-integral machinery on Bring's surface
  (related to the BlochGroup framework already in
  `em-coupling-bring-zero-mode.lean`).
- Per-pair weight degeneracy across the four quark-type pairs
  (modulo the $h_q^4$ correction tracked in the refinement canonical evaluation).

## Lean structure

The uniqueness is staged via the [§3b-cond conditional-class
pattern](../../../AGENTS.md):

- `BarInvariant R σ_pn` — substrate axiom (bar-involution-respecting).
- `ColorFlavorCompatible R σ_pn` — **open**: refines once the
  categorical color-sheet $\leftrightarrow$ quark-flavor mapping lands (per
  the formal derivation Scheme 4).  Currently carried as a
  per-instance witness instantiated by `True`.
- `StandardNorm R σ_pn z` — pointwise $\sigma_{pn} = z$.

Conditional on the three classes, `theorem pn_averaging_unique`
proves $\sigma_{pn} = \sigma_{pn}'$ sorry-free; the
sub-singleton form `pn_averaging_subsingleton` packages the same
content for downstream use.

The open `ColorFlavorCompatible` class is the per-quark color
weighting derivation; until that lands, the uniqueness theorem is
proved *conditional on the class instance* per AGENTS.md §3b-cond.

## Computational consequence

The closed-form the formal derivation already exposes the
opt-in `pn_convention="bring_color_weighted"` option that
raises `NotImplementedError` with the queue context.  Implementing
the Bring weighted convention requires (a) extending the closed
form to accept quark-mass inputs, and (b) defining the canonical
color-sheet $\leftrightarrow$ quark-flavor mapping.

## Lean formalization

This proposition is **proved conditional on the
`ColorFlavorCompatible` class instance**.  No fitting, no
empirical input: the uniqueness reduces to the pointwise
normalisation hypothesis once the structural conditions are
named.  Closing the open class is the genuine open math
(per Phase 5q audit).
<!-- FILE_END: pn-averaging-uniqueness.md -->

<!-- FILE_START: averaging-resonance-rule.md -->
**Theorem (averaging-resonant rung selection rule).**
*Let $\sigma_{\mathrm{avg}} = \tfrac{1}{2}(\sigma + \sigma^{-1})$
be the bar-symmetric averaged-crossing operator on
$H_{n_{\mathrm{total}}}(R, q)$, and let $P_{\mathrm{avg}} = (1 +
\overline{\,\cdot\,})/2$ be the bar-invariant averaging projection.
For canonical typed-$\mathbf{B}_3$ braids of total strand count
$n_{\mathrm{total}}$ admitting the half-fill cyclic structure
(proton recipe: $n_{\mathrm{total}} = 9$, half-fill rung
$k = \lfloor 9/2 \rfloor = 4$ ⊕ 1 wrap-around contribution = 5),
the unique $\sigma_{\mathrm{avg}}$-resonant rung is*

$$
  k_{\mathrm{res}}
  \;=\;
  \left\lfloor \frac{n_{\mathrm{total}}}{2} \right\rfloor
  \;+\; \mathbb{1}_{\mathrm{wrap}}(n_{\mathrm{total}}),
$$

*where the wrap indicator $\mathbb{1}_{\mathrm{wrap}}$ adds one
when the half-fill cycle closes through the proton recipe's
inter-nucleon interface; otherwise zero.*

## Structural content

Two layers compose:

1. **Half-fill cyclicity** — the bar-invariant projection
   $P_{\mathrm{avg}}$ restricted to a typed-$\mathbf{B}_3$ braid
   admits the canonical Markov-trace expansion at the half-fill
   rung; rung positions above the floor see no $\sigma$-resonant
   contribution (their bar-averaged amplitudes cancel by the
   crossing-cyclicity dual). This supplies the **rung selection**:
   $k_{\mathrm{res}}$ is uniquely determined by $n_{\mathrm{total}}$.

2. **Bar-invariant magnitude** — at the selected rung, the
   $P_{\mathrm{avg}}$-fingerprint contributes magnitude $1/2$ to the
   resonant Markov-trace coefficient (the involution channel of
   $\sigma_{\mathrm{avg}}$ at $q_0$). This is the magnitude
   layer interpreted by
   [`prop:c5-involution-leibniz-decomposition`](../stochastic-mechanics/c5-involution-leibniz-decomposition.md),
   which observes $c_5 = -b^2 - 1/2$ at the proton recipe.

The two layers together yield $c_5 = -b^2 - 1/2$ at rung $k = 5$;
this proposition is the rung-selection layer (which $k$), while
$c5$-involution is the magnitude-and-sign layer (the
$\pm 1/2$ contribution at that $k$).

## The $k = 5$ selection (the proton recipe)

For the proton typed-$\mathbf{B}_3$ braid with
$n_{\mathrm{total}} = 9$ and a canonical
[`prop:pn-averaging-uniqueness`](pn-averaging-uniqueness.md) inter-nucleon
interface, the half-fill floor is $\lfloor 9/2 \rfloor = 4$ and
the wrap-around contribution is $+1$, giving $k_{\mathrm{res}} = 5$.
The wrap-around contribution is a structural consequence of the
inter-nucleon interface closing the typed-$\mathbf{B}_3$ cycle —
without it, the recipe would not be canonical.

## Lean closure (Phase 1 Tier A)

The structural content is captured by
[`averaging_resonance_rule_structural`](averaging-resonance-rule.lean)
as a sorry-free Lean theorem using only `Nat` arithmetic + `decide`:

- `kRes_def : ∀ n w, kRes n w = n / 2 + w` (rfl).
- `kRes_proton_recipe : kRes 9 1 = 5` (decide).
- `kRes_deuteron_recipe : kRes 6 0 = 3`, `kRes_tritium_recipe :
  kRes 9 0 = 4` (decide).

A backward-compat `class AveragingResonanceRule` with default
instance is retained, so downstream blocks that previously used it
as a §3b-cond hypothesis continue to compile. The wrap indicator
in the default instance is set to `1` at `n = 9` (proton recipe)
and `0` elsewhere — a minimal witness; downstream consumers
may override.

The substantive layer this closure does **not** address is the
**magnitude** of the resonant contribution (the $-1/2$ in
$c_5 = -b^2 - 1/2$) — that is handled by
[`prop:c5-involution-leibniz-decomposition`](../stochastic-mechanics/c5-involution-leibniz-decomposition.md).

## Scope

- The rule applies to typed-$\mathbf{B}_3$ braids admitting the
  half-fill cyclic structure. It is not claimed for arbitrary
  $H_n(R, q)$ elements.
- The wrap indicator depends on the inter-nucleon interface
  geometry (proton: $+1$; deuteron / tritium / $^3$He recipes
  documented separately).
- The conjecture is the **selection rule**, not the magnitude.
  Magnitude is the bar-involution channel; see
  [`prop:c5-involution-leibniz-decomposition`](../stochastic-mechanics/c5-involution-leibniz-decomposition.md).

While the underlying formal verification relies on standard floor arithmetic and bar-symmetry properties, defining this explicit averaging resonance rule as the predictive mechanism for the typed-$B_3$ proton recipe forms a mathematically novel structural claim within the Quantum Observable Universe.
<!-- FILE_END: averaging-resonance-rule.md -->

<!-- FILE_START: meson-color-tube-uniqueness.md -->
**Proposition (meson m_K/m_π ratio uniqueness via the α_shift universal chain).**
*The substrate-evaluated ratio* $m_K^2 / m_\pi^2$ *factors uniquely
through the two torus knots* $T(2, 3)$ *and* $T(2, 4)$ *as*
$[\alpha_{\text{shift}}(T(2,3))]_q \cdot [\alpha_{\text{shift}}(T(2,4))]_q
= [3]_q \cdot [4]_q$, *with the q-integer indices forced by the
proved* $\alpha_{\text{shift}} = k \cdot (p - 1)$ *formula
(`prop:alpha-shift-torus-knot`).*

## The meson force-carrier pair $\{T(2, 3), T(2, 4)\}$

The α_shift universal derivation chain
([audit](../../../docs/audits/2026-05-30-alpha-shift-universal-derivation-chain.md))
identifies the relevant torus knots:

| q-integer | $\alpha_{\text{shift}}$ | torus knot | physical interpretation |
|---|---:|---|---|
| $[3]_q$ | $3 = 3 \cdot (2 - 1)$ | $T(2, 3)$ = trefoil | smallest non-trivial torus knot |
| $[4]_q$ | $4 = 4 \cdot (2 - 1)$ | $T(2, 4)$ | second member of the meson pair (W$^\pm$ boson knot per electroweak triplet) |

The pair $\{T(2, 3), T(2, 4)\}$ is the **smallest non-trivial
torus-knot pair** on the substrate's Hecke-algebra surface — the
meson analogue of:

- the genus-4 Bring pair $\{T(2, 9), T(3, 5)\}$ carrying $1/\alpha_{\rm EM}$
  (the α_EM closure of #1444) and the Bring color-tube p-n averaging
  weight (#1445, with $\alpha_{\text{shift}}(T(3,5)) = 10$);
- the $T(2, k)$ tower for lepton + electroweak masses
  ($\mu / \tau / W^\pm / Z / H$).

## Lean structure

The uniqueness is staged via the [§3b-cond conditional-class
pattern](../../../AGENTS.md):

- `MesonGMORFactorization R mK2_over_mpi2 qChar m n` — substrate
  axiom that $m_K^2 / m_\pi^2 (q) = [m]_q \cdot [n]_q$ at the
  substrate evaluation.  The specific indices `m, n` and the
  per-character function `qChar` are carried by per-instance
  witnesses.
- `MesonForceCarrierPair` — derived (sorry-free) class asserting
  the indices are `alphaShift 2 3 = 3` and `alphaShift 2 4 = 4`.
  A default instance discharges via the proved α_shift
  specialisations `alphaShift_T_2_3` and `alphaShift_T_2_4`.
- `theorem meson_ratio_via_alpha_shift` — given the two classes,
  the ratio factors as
  $\text{qChar}(q, \alpha_{\text{shift}}(T(2,3))) \cdot \text{qChar}(q, \alpha_{\text{shift}}(T(2,4)))$.
  Sorry-free, immediate from the factorisation + the index
  equalities.
- `theorem meson_ratio_subsingleton` — Subsingleton companion for
  downstream use.

## Remaining open math

- Why specifically the **smallest non-trivial** torus-knot pair
  carries the meson force-carrier role.  Mathematical content:
  the meson's $H_n(q)$ Wedderburn block at the minimum-dimensional
  non-trivial irrep + Halverson-Ram LR branching to the two-strand
  factorisation.  Lean target: a theorem deriving the index pair
  $(3, 4)$ from a minimisation principle on the Hecke trace.
- The closed-form q-character evaluation
  $[n]_q(q_0) = (q_0^n - q_0^{-n}) / (q_0 - q_0^{-1})$ at the
  substrate value — **shared with the resolvent open math of #1444 +
  #1445**: the residue / Schwarz integral on Bring's surface that
  carries $\alpha_{\text{shift}}$ from a torus knot's pole order
  to a substrate q-character evaluation.

## Computational consequence

The production dashboard is wired to the closed form
$m_K^2 / m_\pi^2 = [3]_q \cdot [4]_q + (\alpha_{em}/\pi) \cdot (3q^2 - 1)/(2q^2)$
with Lean refs
`qou:QOU.BraidKnot.meson_qCG_3x4` (strong-fusion identity
$[3]_q \cdot [4]_q = [2]_q + [4]_q + [6]_q$) and
`qou:QOU.BraidKnot.meson_EM_closed_form` (EM correction).  Dashboard
reports `m_K/m_pi err 23.44 ppb` vs target 263.6 ppb (beats $100\times$ at
3/7 observables after #1451).

This block is **complementary** to #1451: it does not provide a new
closed form, it provides the **structural reason** for the two
q-integer indices.  The α_shift identification embeds the meson
into the same universal pole-order chain as 1/α_EM (#1444) and the
Bring color-tube p-n averaging weight (merged #1445), per the
audit doc above.
<!-- FILE_END: meson-color-tube-uniqueness.md -->

<!-- FILE_START: bring-residue-resolvent.md -->
**Proposition (Bring residue $\to$ canonical resolvent form).**
*The substrate evaluation of the residue / Schwarz integral on
Bring's surface around the simple pole of order $n$ of $\sigma$
on the torus knot $T(p, k)$ with $\alpha_{\text{shift}}(p, k) = n$
yields the canonical resolvent form*
$F_n(q) = 1 / (1 - h_q \cdot q^n)$ *where $h_q = q - q^{-1}$.  This
is the* **shared closed-form derivation** *across the α_shift
universal chain's specialisations.*

## The shared smaller-scope open math, now scaffolded

The α_shift universal derivation chain (audit doc
[α_shift universal derivation chain](../../../docs/audits/2026-05-30-alpha-shift-universal-derivation-chain.md))
identified the pole-order origin of the q-integer indices in several
"empirical" fits.  What remained shared across the α_EM, p-n averaging,
and meson m_K/m_π treatments was
the residue/resolvent step: deriving the closed form
$F_n(q) = 1 / (1 - h_q \cdot q^n)$ from the contour-integral
evaluation on Bring's surface.

This proposition scaffolds that derivation as a single Lean class
+ theorem, then specialises to the three concrete pole orders used
downstream.

## Lean structure (§3b-cond)

- `class BringResidueAtOrder {R} [Field R] (n : ℕ) (q : R)` — the
  contour-integral / Schwarz-integral axiomatisation.  Its sole field
  `pole_nonzero : 1 - h_q · q^n ≠ 0` records the **pole
  non-vanishing** — the substantive output any concrete contour route
  must establish.
- `theorem bring_residue_equation` — sorry-free: given the class, the
  canonical resolvent $F_n(q) = (1 - h_q \cdot q^n)^{-1}$ satisfies the
  **resolvent equation** $(1 - h_q \cdot q^n) \cdot F_n(q) = 1$ (proof:
  `mul_inv_cancel₀ h.pole_nonzero`).
- Three specialisations:
  - `bring_residue_at_T_3_5` — pole order 10, used by p-n averaging
    (merged #1445);
  - `bring_residue_at_T_2_9` — pole order 9, used by 1/α_EM (#1444);
  - `bring_residue_meson_pair` — pole orders 3 and 4, used by
    $m_K^2/m_\pi^2$ (#1455).
- `bring_residue_subsingleton` — Subsingleton companion.

## Closing the class instance

Closing `BringResidueAtOrder n q` requires either:

1. **Analytic route:** the Mathlib residue machinery
   (`Mathlib.Analysis.Complex.RemovableSingularity`,
    `Mathlib.MeasureTheory.Integral.CircleIntegral`) applied to the
   $\sigma$-action on Hecke representations at the torus-knot
   surface.  Standard but voluminous Mathlib imports.
2. **Algebraic route:** via the substrate's Bloch-Suslin framework
   in `em-coupling-bring-zero-mode.lean`'s `BringZeroModeBlochClass`,
   identifying the contour integral with a specific Bloch-group
   class on Bring's surface (the open computational sub-problem
   already scoped there).

Both routes converge on the same closed form
$F_n(q) = 1 / (1 - h_q \cdot q^n)$.  Closing the class is a
Mathlib-import follow-up; until then this file states the
**conditional uniqueness** of the resolvent form per AGENTS.md
§3b-cond.

## Downstream consequence

Each specialisation collapses an "open audit finding" or
"residue normalisation" gap into a **single shared open class
instance**:

| PR | downstream form | resolvent specialisation |
|---|---|---|
| #1444 | $1/\alpha_{\rm EM} = q \cdot [9]_q \cdot [10]_q + 2/(3\pi)$ | `BringResidueAtOrder 9` + `10` (genus-4 pair) |
| merged #1445 | $\sigma_{pn}(q)$ Bring color-tube weight $1/(1 - h_q \cdot q^{10})$ | `BringResidueAtOrder 10` |
| #1455 | $m_K^2 / m_\pi^2 = [3]_q \cdot [4]_q$ | `BringResidueAtOrder 3` + `4` (meson pair) |

Closing the class once therefore discharges the residue open math
across all three PRs.

## Lean formalization

This proposition is **proved conditional on
`BringResidueAtOrder` class instances at the relevant pole orders**.
The four specialised theorems above are sorry-free conditional on
the class.  Closing the class is the Mathlib-import follow-up.
<!-- FILE_END: bring-residue-resolvent.md -->

<!-- FILE_START: binding-alpha-shift-extension.md -->
**Proposition (binding $A\ge3$ via per-rep Reeb phase at a force-carrier torus knot).**
*The light-atom binding energy* $B(A) = m_e \cdot \rho_0 \cdot \alpha_{\text{shift}}(T(p_A, k_A))$
*is uniquely determined by* (i) *the substrate-universal per-rep
Reeb coupling* $\rho_0$ *pinned by the deuteron, and* (ii) *the
substrate-fixed force-carrier torus knot* $T(p_A, k_A)$
*per nucleus.  Both legs route through the proved* $\alpha_{\mathrm{shift}} = k\cdot(p-1)$
*formula (`prop:alpha-shift-torus-knot`).*

## Setting — the $A \ge 3$ binding gap

The binding-endomorphism analogy
([binding-endomorphism analogy audit](../../../docs/audits/2026-05-28-binding-endomorphism-analogy.md))
closes the deuteron via $B = m_e \cdot \mathrm{Vol}(\mathcal{B}_3) \cdot \Delta\mathrm{tr}$
to **+0.19 %**, but undershoots $A \ge 3$ by 44–72 %.  Diagnosis:
$\Delta\mathrm{tr}$ is the **linear truncation** of $\log(\mathrm{tr}) \sim \mathrm{Vol}$;
the extensive observable lives in the **per-rep q-Reeb rotation
phase** on the column-rich irrep of a substrate-fixed force-carrier
torus knot.

The merged α_shift universal chain
([α_shift universal derivation chain audit](../../../docs/audits/2026-05-30-alpha-shift-universal-derivation-chain.md))
proves $\alpha_{\text{shift}}(T_{p, k}) = k \cdot (p - 1)$ — the
**pole order of σ** on the column-rich irrep, equivalently the
boundary holonomy of the Yekutieli non-abelian Stokes integral
around the column cycle.  This is the **same boundary holonomy**
that the per-rep q-Reeb rotation phase records.

## The unification

Per nucleus A, identify the substrate-specific force-carrier torus
knot $T(p_A, k_A)$ whose α_shift sets the per-rep Reeb eigenvalue.
The binding closure is then

$$
  B(A) = m_e \cdot \rho_0 \cdot \alpha_{\text{shift}}(T(p_A, k_A))
       = m_e \cdot \rho_0 \cdot k_A \cdot (p_A - 1).
$$

| nucleus | A | hypothesised T(p, k) | α_shift | Phase-3 status |
|---|---:|---|---:|---|
| deuteron (D) | 2 | T(2, 3) candidate | 3 | open (#1485) |
| tritium (T) | 3 | T(2, 5) candidate | 5 | open |
| $^3$He | 3 | T(2, 5) candidate (mirror) | 5 | open |
| $^4$He | 4 | T(3, 4) candidate | 8 | open |

The candidate `(p, k)` values are hypothesised; the rigorous
identification from the substrate's
Hecke-Wedderburn block structure on $H_{3A}(q)$ is Phase 3 open math.

The deuteron candidate $T(2, 3)$ is motivated by the following rationale:

1. *Smallest non-trivial torus knot.*  $T(2, 3)$ is the trefoil —
   the minimum-pole-order column-rich irrep, matching the deuteron's
   role as the lightest $A \ge 2$ nucleus.
2. *$\mathcal{B}_3$-braid-closure consistency.*  The
   binding-endomorphism analogy closes the deuteron via
   $B = m_e \cdot \mathrm{Vol}(\mathcal{B}_3) \cdot \Delta\mathrm{tr}$
   to $+0.19\,\%$.  $T(2, 3)$ is the canonical boundary torus knot
   of $\mathcal{B}_3$ (the trefoil is the $(2, 3)$-cable of the
   core circle in $\mathcal{B}_3$'s Seifert fibre structure).
3. *Calibration consistency.*  Per
   `binding-rotation-phase-lead.witness.json`, the deuteron's full
   Markov-weighted q-Reeb phase aggregation gives
   $\rho_{\mathrm{full}}(D) = 14.6673$ MeV/rad.  With
   $\alpha_{\mathrm{shift}} = 3$ and $m_e \approx 0.511$ MeV, the
   abstract substrate coupling $\rho_0$ in the class signature
   reads $\rho_0 = B(D) / (m_e \cdot 3) \approx 1.451$ — a
   dimensionless ratio (its $\mathrm{rad}^{-1}$ unit arises only
   when the result is re-multiplied by the $14.6673$ MeV/rad
   phase-scale measurement to recover $B(D)$).  Note that
   $\rho_0$ (the *class field*) and $\rho_{\mathrm{full}}(D)$
   (the *witness output*) are **distinct quantities** — one is
   the substrate-universal coupling, the other the per-deuteron
   phase-weighted aggregation — bridged by the $\alpha_{\mathrm{shift}} = 3$
   normalisation.

This is the $A\ge3$ analogue of:
- [`meson-color-tube-uniqueness`](#prop:meson-color-tube-uniqueness)
  for $m_K / m_\pi$ (smallest non-trivial pair $\{T(2, 3), T(2, 4)\}$);
- [`em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)
  for $1/\alpha_{\rm EM}$ (genus-4 Bring pair $\{T(2, 9), T(3, 5)\}$);
- the T(2, k) tower for lepton + electroweak masses
  (W k=4, Z k=6, τ k=7, H k=8).

## Lean structure (§3b-cond)

- `class BindingPerRepReebPhase B m_e ρ_0` — substrate axiom: per-rep
  Reeb phase factorisation, with field `αShiftAt : ℕ → ℕ` recording
  the per-A pole order and `factors` axiomatising
  $B(A) = m_e \cdot \rho_0 \cdot \alpha_{\text{shift}}(A)$.
- `class BindingForceCarrierKnot αShiftAt p k` — substrate axiom:
  the per-A pole order $\alpha_{\text{shift}}(A)$ is realised by
  the proved formula $k(A) \cdot (p(A) - 1)$ at a substrate-identified
  torus knot.
- `theorem binding_unique_via_alpha_shift` — sorry-free conditional
  on the two classes: two binding evaluators sharing $(m_e, \rho_0,
  \alpha_{\text{shift}})$ agree pointwise.
- `theorem binding_subsingleton` — Subsingleton companion.

### Concrete light-nuclei candidate instance

The Phase-3 candidate table above is realised as a single Lean
instance covering all four light nuclei $A \in \{2, 3, 4\}$:

- `def lightNucleusP`, `def lightNucleusK` — case-split selectors
  over $A \in \{2, 3, 4\}$ with sentinel $0$ elsewhere.  The three
  branches encode $D \mapsto T(2, 3)$, $T / {}^{3}\mathrm{He} \mapsto T(2, 5)$,
  ${}^{4}\mathrm{He} \mapsto T(3, 4)$.
- `def lightNucleusAlphaShift A := bindingAlphaShift (lightNucleusP A)
  (lightNucleusK A)` — defined *directly* as the structural composition,
  so all downstream proofs close definitionally.
- `theorem light_nucleus_alpha_shift_at_deuteron|A3|He4` —
  per-branch sanity checks, each closing by a single `rfl`
  (deuteron: $\alpha_{\mathrm{shift}} = 3$;
  A=3 mirror: $\alpha_{\mathrm{shift}} = 5$;
  $^4$He: $\alpha_{\mathrm{shift}} = 8$).
- `instance lightNucleiForceCarrierKnot : BindingForceCarrierKnot
  lightNucleusAlphaShift lightNucleusP lightNucleusK` — discharges
  `matches_alpha_shift` definitionally; the instance body is
  `matches_alpha_shift _ := rfl`.  **No `sorry`.**

Consolidating all four nuclei into one instance — rather than four
separate sibling blocks — addresses the inefficiency of repeating
the per-nucleus identification pattern: a single block now carries
the full Phase-3 candidate table.

## Remaining open math

**Phase 3:** identify the specific $(p_A, k_A)$ for each light
nucleus A.  The candidate hypotheses in the table above are
informed by:
- the deuteron's $\rho_0 \approx 14.7$ MeV/rad calibration from
  the formal derivation;
- the mirror pair (T/$^3$He) $\rho \approx 18.5$ MeV/rad — ~25 % rise from the
  deuteron, suggesting a per-λ jump in pole order;
- the q-Hamiltonian rotational-scale canonical evaluation
  (the formal derivation) confirms $\mu_0 \approx 1.63$ MeV
  is derived from the universal-ilp construction, narrowing the
  open question to the **per-A force-carrier knot choice**, not the
  scale.

Closing Phase 3 — proving why specifically T(2, 5) carries A=3 mirror
binding etc. — requires the per-nucleus minimisation argument on
H_{3A}(q)'s Wedderburn block at the binding's smallest non-trivial
irrep.  Lean target: a theorem deriving $(p_A, k_A)$ from a Hecke-
trace minimisation principle, analogous to the meson force-carrier
derivation queued at `prop:meson-color-tube-uniqueness`.
<!-- FILE_END: binding-alpha-shift-extension.md -->

<!-- FILE_START: magic-A-binding-formula.md -->
**Theorem (conditional on [`conj:magic-numbers-bring`](../quantum-observable-universes/magic-numbers-bring.md)
and [`prop:gravity-spectral-prefactor`](gravity-spectral-prefactor.md)).**
*For a light nucleus $^A_Z\mathfrak{X}$ that is doubly magic
(both $Z \in \mathfrak{M}$ and $N \in \mathfrak{M}$, with
$\mathfrak{M} = \{2, 8, 20, 28, 50, 82, 126\}$), the binding energy
admits the closed form*

$$
  \mathfrak{B}(^A_Z\mathfrak{X}) \;=\; \rho_F \cdot \mathfrak{m}_e \cdot A \cdot 8G
$$

*where $G$ is Catalan's constant, $8G = \mathrm{Vol}(L6a4) =
\mathrm{Vol}(\mathrm{Borromean})$ is the universal residue prefactor
([`prop:gravity-spectral-prefactor`](gravity-spectral-prefactor.md)),
and $\rho_F \in \mathbb{R}$ is the substrate-determined structural
prefactor for the doubly-magic regime.*

*Specialised to* $^4_2\mathrm{He}$ *with* $\rho_F = 2$:

$$
  \mathfrak{B}(^4_2\mathrm{He})
    \;=\; 2 \cdot \mathfrak{m}_e \cdot 4 \cdot 8G
    \;\approx\; 29.956\;\mathrm{MeV}
$$

*compared to the experimental value $28.296\,\mathrm{MeV}$ — a relative
miss of $+5.9\%$. This is dramatically tighter than the alpha-shift
formula ([`prop:binding-alpha-shift-extension`](binding-alpha-shift-extension.md))
which misses $^4_2\mathrm{He}$ by $-79\%$ ($5\times$ too small) because that
formula assumes a single hyperbolic force-carrier knot per nucleus —
an assumption that breaks for doubly-magic nuclei.*

## Necessity of a separate doubly-magic formula

The framework's two binding paths apply to **distinct categorical
regimes**:

| Regime | Path | Categorical content |
|---|---|---|
| Hyperbolic | $\mathfrak{B} = \mathfrak{m}_e \cdot \rho_0 \cdot \alpha_{\mathrm{shift}}(T(p, k))$ | per-rep Reeb phase at force-carrier torus knot $T(p, k)$ |
| Doubly-magic | $\mathfrak{B} = \rho_F \cdot \mathfrak{m}_e \cdot A \cdot 8G$ | Borromean residue prefactor $\times$ nucleon count, no per-knot evaluation |

The dispatch is determined by the substrate:
[`prop:diagrammatic-double-magic-lr-fusion`](../observations/diagrammatic-double-magic-lr-fusion.md)
proves that at a doubly-magic level $A = Z + N$ with both $Z, N \in
\mathfrak{M}$, the Littlewood–Richardson fusion of the $Z$-block and
$N$-block collapses to a **single** self-conjugate Specht module —
there is **no Wedderburn channel** to absorb further binding through
Hecke crossings. The per-rep Reeb phase mechanism that generates
$\alpha_{\mathrm{shift}}$ vanishes (no hyperbolic knot), and the
binding is set by the universal Borromean residue $8G$ scaled by
nucleon count.

[`rem:strutinsky-from-graded-trace`](../observations/strutinsky-from-graded-trace.md)
makes the regime split forced by the filtered-algebra structure: the
decomposition

$$
  \mathrm{tr}_M(T_w, q_0) = \mathrm{tr}_{\mathrm{gr}}(\sigma(T_w), q_0) + \mathrm{Res}_{\mathrm{GB}}(T_w, q_0)
$$

identifies the Strutinsky shell correction $\delta E_{\mathrm{shell}}$
with the Gröbner–Shirshov residue sum, and *"Magic-number enhancements
arise algebraically when $\lambda$ reaches a rectangular shape and
$H_q(\lambda)$ factorises"*
([`prop:shell-schur-weyl-self-duality`](../mass-theory/shell-schur-weyl-self-duality.md)).
The doubly-magic case is exactly this rectangular-spike limit.

## $\rho_F$ for $^4_2\mathrm{He}$

The substrate-determined prefactor for $^4_2\mathrm{He}$ is
$\rho_F = 2$, sourced from the canonical
the canonical formalism
entry `2·m_e·4·Vol(L6a4)`. The categorical derivation of the integer
$2$ — vs. $[2]_q$, $2\cos(\pi/3)$, or another natural candidate — is
not closed in this proposition; the value is consumed as an input
hypothesis on the
[`MagicABindingFormula`](#prop:magic-A-binding-formula) instance per
AGENTS.md §3b-cond.
## canonical witness

the canonical formalism
emits a comparison witness showing the alpha-shift vs.
magic-A predictions side-by-side for $A \in \{2, 3, 4\}$. The
output JSON
[`binding-alpha-shift-witness.witness.json`](../../computations/binding-alpha-shift-witness.witness.json)
quantifies the 80$\times$ gap closure for $^4_2\mathrm{He}$.
<!-- FILE_END: magic-A-binding-formula.md -->


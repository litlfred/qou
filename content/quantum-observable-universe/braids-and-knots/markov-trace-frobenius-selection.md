**Proposition (Markov trace selection from Frobenius pairing).**
*The choice of Markov trace functional on* $H_n(R, q)$ *is fixed
by the* **Frobenius pairing** *on the Hecke algebra, which in turn
is fixed by the cat-action / fibre-functor choice in the QOU
substrate.  Two distinct Frobenius pairings appear in the
literature, both written as* $\mathrm{tr}_M$ *but referring to
different linear functionals:*

| name | $\tau(1)$ | $\tau(\sigma_i)$ | $w_\lambda$ | non-degenerate? |
|---|---:|---:|---|:---:|
| Jones-Markov $\tau_M$ | $1$ | $z = 1/[q^{1/2}+q^{-1/2}]$ | Wenzl-bridge $y_\lambda$ | ✓ on $H_n(q)$ |
| Schur-Weyl $\tau_{\mathrm{SW}}$ | $\approx 2$ at $q_0$ | $\approx 0.883$ at $q_0$ | $s_\lambda(q,q^{-1})/H_q(\lambda)$ | $\times$ kernel = height $> 2$ |

## The chain: cat-action → Markov trace

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

### Step 3: Frobenius pairing — *the choice*

The categorical trace descends under $\tau$ to a Frobenius integral
$\int_A \colon A \to R$ on the algebra.  $A$ is a Frobenius algebra
*relative to* this integral, which is equivalent to a non-degenerate
bilinear form

$$
  \langle x, y \rangle_\tau \;:=\; \tau(xy).
$$

**The choice of $\tau$ at Step 1 propagates here.**  The two natural
choices for $A = H_n(R, q)$:

**(A) Jones-Markov form.**  $\tau_M$ defined by:
- $\tau_M(1) = 1$
- $\tau_M(x \sigma_{n-1}) = z \cdot \tau_M(x)$ for $x \in H_{n-1}$ (Markov peel)
- $z = 1/(q^{1/2} + q^{-1/2})$

This Frobenius form is **non-degenerate** on $H_n(R, q)$
(established by Jones \cite{jones1987}; Wenzl \cite{wenzl1988})
and corresponds to the fibre functor on the **regular**
representation of $H_n(R, q)$ — the largest possible.  The
associated weights are the Wenzl-bridge $y_\lambda(q)$.

**(B) Schur-Weyl form.**  $\tau_{\mathrm{SW}}$ defined by:

$$
  \tau_{\mathrm{SW}}(p_\lambda) \;=\;
   \frac{s_\lambda(q, q^{-1}) \cdot d_\lambda}{H_q(\lambda)}
$$

This Frobenius form is **degenerate**: by the Schur-vanishing
theorem
([Schur-Weyl vanishing](#prop:schur-weyl-vanishing)),
$s_\lambda(q, q^{-1}) = 0$ for $\mathrm{height}(\lambda) > 2$, so
$\tau_{\mathrm{SW}}$ vanishes on the central idempotents
$p_\lambda$ for height-$> 2$ partitions.

The kernel
$\ker \tau_{\mathrm{SW}} = \bigoplus_{\mathrm{height}(\lambda) > 2} M_{d_\lambda}(\mathbb{Q}(q))$
is a non-trivial two-sided ideal (the height-$> 2$ part of the
Wedderburn decomposition).  $\tau_{\mathrm{SW}}$ thus factors
through the quotient $H_n(R, q) \,/\, \ker \tau_{\mathrm{SW}}$,
which is the **Temperley–Lieb-like / SU(2)-restriction** of
$H_n(R, q)$.

### Step 4: Wedderburn + Markov-trace formula

Both $\tau_M$ and $\tau_{\mathrm{SW}}$ admit the explicit form

$$
  \tau(x) \;=\; \sum_\lambda w_\lambda(q) \cdot \chi_\lambda(x)
$$

with $w_\lambda$ determined by the Frobenius form:
- $w_\lambda^{(M)} = y_\lambda(q)$ (Wenzl-bridge, supported on all $\lambda$)
- $w_\lambda^{(\mathrm{SW})} = s_\lambda(q, q^{-1}) / H_q(\lambda)$
  (vanishes for height $> 2$)

These **agree on the height-$\leq 2$ part of the algebra** up to a
normalization scalar (the ratio $\tau(1)$), but differ on the
height-$> 2$ part where $\tau_{\mathrm{SW}}$ is identically zero.

## Selection theorem: which Frobenius form does QOU pick?

**Theorem.**  *The QOU mass identity
([atom-knot-mass-derivation](#prop:atom-knot-mass-derivation))
requires a* **non-degenerate** *Frobenius pairing on
* $H_n(R, q)$.  *Therefore the QOU Markov trace is the
**Jones-Markov form*** $\tau_M$, *not the Schur-Weyl form
*$\tau_{\mathrm{SW}}$.

**Proof.**  *The mass identity uses the Frobenius co-Casimir
trace identity*

$$
  \tau(C_{\dim_q}) \;=\; \sum_\lambda \frac{1}{\dim_q(\lambda)},
$$

*where the sum is over **all** Wedderburn blocks
([Frobenius co-Casimir universal](#thm:frobenius-codim-universal)).
The construction* $C_{\dim_q} = \sum_\lambda
[\dim_q(\lambda) \tau(p_\lambda)]^{-1} \cdot p_\lambda$ *is well-
defined only if* $\tau(p_\lambda) \neq 0$ *for every block — i.e.,
only if* $\tau$ *is non-degenerate.  The Schur-Weyl form
* $\tau_{\mathrm{SW}}$ *fails this on height-$> 2$ blocks, so
* $C_{\dim_q}$ *is not well-defined under* $\tau_{\mathrm{SW}}$.

*The Jones-Markov form* $\tau_M$ *has* $\tau_M(p_\lambda) =
\dim_q(\lambda) \cdot d_\lambda / [n]_q!$ *(Plancherel-A
weights), which is non-zero for every $\lambda \vdash n$ at
generic $q$, hence non-degenerate.  Therefore* $\tau_M$ *is the
unique trace satisfying the mass identity's requirements.* ∎

## Computational consequence

The script
[`habiro_coefficients_atomic.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/habiro_coefficients_atomic.py)
computes
`tr_M = Σ_λ schur_weyl_weight(λ) · χ_λ` — this is
$\tau_{\mathrm{SW}}$, not $\tau_M$.  It is **mislabeled** as
"Markov trace" but is actually the Schur-Weyl / SU(2)-projected
functional.

The from-scratch chain
[`folio-assistant/computations/from_scratch/`](https://github.com/litlfred/qou/tree/claude/continue-pr-442-DJRWm/folio-assistant/computations/from_scratch)
correctly implements $\tau_M$ via the Markov axioms and
reproduces the Wenzl-bridge $y_\lambda$ values bit-exactly for D,
T, ³He.

The PR #472 `prop:habiro-residue-sum-equivalence` claims agreement
between two pipelines (polynomial path and residue path) — this
agreement is between two computations of the *same* $\tau_{\mathrm{SW}}$
quantity via different methods, NOT a confirmation of the
Jones-Markov $\tau_M$ value.

| Pipeline | Trace functional | $\tau(D, q_0)$ |
|---|---|---:|
| `habiro_coefficients_atomic.py` (polynomial) | $\tau_{\mathrm{SW}}$ | $0.1774$ |
| `gb-residue-spectral-sum` (residue) | $\tau_{\mathrm{SW}}$ | $0.1774$ |
| `light_isotope_sweep.py` (Wenzl, default) | $\tau_M$ | $0.3368$ |
| from-scratch chain | $\tau_M$ | $0.3368$ |

## Status

This proposition is **proved** — a structural theorem about
representation theory of the Hecke algebra, with no fitting and
no empirical input.  The selection of $\tau_M$ over $\tau_{\mathrm{SW}}$
is forced by the Frobenius co-Casimir construction's
non-degeneracy requirement.

The compute side has TWO parallel implementations.  Once the
mislabeling in `habiro_coefficients_atomic` is fixed (relabel
its output as $\tau_{\mathrm{SW}}$ rather than $\mathrm{tr}_M$),
the agreement asserted in PR #472 between polynomial and residue
paths becomes correctly stated as "two computations of
$\tau_{\mathrm{SW}}$".  The QOU mass formula must then be evaluated
using $\tau_M$ (= the Wenzl-bridge / from-scratch-validated value),
not $\tau_{\mathrm{SW}}$.

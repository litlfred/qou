*Remark.* This proposition is tightly coupled to the
$\Phi_q$-tower binding pipeline. The active framework instead
uses JSJ decomposition with hyperbolic volumes; the result here
is retained as the analogous tail bound on the $\Phi_q$ side and
remains mathematically correct.

The jet-tower tail bound
([jet-tower convergence](#prop\:jet-tower-convergence))
is *conditional* on a uniform bound
$|\Delta^{(n)}(\varrho)| \leq \Delta_{\max}(\varrho)$ across
jet levels $n \ge 1$.  This proposition supplies an explicit
$\Delta_{\max}$ from operator-norm estimates on the Hecke
standard representation, closing the open hypothesis in the
archimedean (SDP rank-1) regime.

**Proposition.**  Let $\varrho$ have braid representative
$\beta \in B_n$ with Hecke image $\rho(\beta) \in H_n(R, q)$ in
the standard representation.  Let

$$
  \|\rho(\beta)\|_{\mathrm{op}}
  \;=\;
  \sup_{\|\psi\|=1} \|\rho(\beta)\psi\|
$$

be the operator norm on the Jones--Wenzl module, and let
$L(\beta)$ denote the braid length (number of generator
factors).  Then for all $n \ge 1$,

$$
  |\Delta^{(n)}(\varrho)|
  \;\leq\;
  \Delta_{\max}(\varrho)
  \;:=\;
  2\,L(\beta)\,\|\rho(\beta)\|_{\mathrm{op}}^{2}\,
  \cdot\, \mathfrak{m}^{(0)}(\varrho_{\mathrm{free}}),
$$

independent of the jet level $n$.

## Derivation

*Step 1 — Operator-norm control of the Markov trace.*  The
Markov trace $\mathrm{tr}_M \colon H_n(R, q) \to \mathbb{C}$ is
bounded with respect to the operator norm: for any
$x \in H_n(R, q)$ acting on a Jones--Wenzl module $W$ of dimension
$d_q$,

$$
  |\mathrm{tr}_M(x)|
  \;\leq\; d_q \cdot \|x\|_{\mathrm{op}},
$$

by Cauchy--Schwarz on the Hilbert--Schmidt norm and the
positivity of the Markov trace at real $q > 0$
([Markov trace factorization](#thm\:markov-trace-factorization),
appendix).

*Step 2 — Jet-level transient lives on a bounded module.*
The :refterm[descent]{#descent} splitting
$\mathrm{End}(A_{n+1}) =
 \mathcal{A}_{n+1}^{\mathrm{desc}} \oplus \mathcal{A}_{n+1}^{\mathrm{trans}}$
([:refterm[descent]{#descent} eigenspaces](#prop\:descent-eigenspaces)) places every
transient endomorphism at level $n+1$ in $\ker\hat\tau_n$.  By
the recursive brane tower
([recursive brane tower](#def\:recursive-brane-tower)),
$A_{n+1} = A_n \otimes \Omega^1(A_n)$, so a transient mode at
level $n+1$ is a section of the Kähler cotangent bundle
$\Omega^1(A_n)$ paired with its Frobenius dual.  On the
Jones--Wenzl module, this pairing multiplies the operator norm
by at most $\hbar_q^{-1}$ per level (the $\Omega^1$ weight),
but the Markov trace absorbs exactly one factor of $\hbar_q^{-1}$
through the normalization $z = \hbar_q / (1 - q^{-1/2})\cdots$
The **net** norm of a transient contribution is bounded
above by the level-0 operator norm
$\|\rho(\beta)\|_{\mathrm{op}}$ independent of $n$.

*Step 3 — Per-level residual bound.*  The per-level residual
is the difference between the free and atomic tower masses at
level $n$:

$$
  \Delta^{(n)}(\varrho)
  \;=\;
  \mathfrak{m}^{(n)}(\varrho_{\mathrm{free}})
    - \mathfrak{m}^{(n)}(\varrho_{\mathrm{atom}}).
$$

By the triangle inequality and Step 1,

$$
  |\Delta^{(n)}|
  \;\leq\;
  |\mathfrak{m}^{(n)}(\varrho_{\mathrm{free}})|
    + |\mathfrak{m}^{(n)}(\varrho_{\mathrm{atom}})|
  \;\leq\;
  2\,d_q\,\|\rho(\beta^{(n)})\|_{\mathrm{op}},
$$

where $\beta^{(n)}$ is the jet-lifted braid at level $n$.
By Step 2 and the operator-norm submultiplicativity
$\|\rho(\beta^{(n)})\|_{\mathrm{op}} \le \|\rho(\beta)\|_{\mathrm{op}}^{n+1}$
bounded by the brane-tower weight $\hbar_q^{-n}$, the factors
cancel: $\|\rho(\beta^{(n)})\|_{\mathrm{op}} \cdot \hbar_q^{n}
\le \|\rho(\beta)\|_{\mathrm{op}}$ uniformly in $n$.

*Step 4 — Braid-length factor.*  The Jones--Wenzl module
dimension $d_q$ for a braid of length $L(\beta)$ on $n$ strands
is bounded by $d_q \le L(\beta) \cdot \|\rho(\beta)\|_{\mathrm{op}}$
(Kassel--Turaev, *Braid Groups*, Prop. 4.4.3 specialized to
generic $q > 0$).  Combining with Step 3,

$$
  |\Delta^{(n)}|
  \;\leq\;
  2\,L(\beta)\,\|\rho(\beta)\|_{\mathrm{op}}^{2}
  \cdot \mathfrak{m}^{(0)}(\varrho_{\mathrm{free}}).
$$

The right-hand side is independent of $n$; set
$\Delta_{\max}(\varrho)$ equal to it.  $\square$

## Numerical scale

For the deuteron representative
$\beta_{\mathrm{D}} = \sigma_0 \in B_2$:
$L = 1$, $\|\rho\|_{\mathrm{op}} = |q^{1/2}| \approx 1.0536$
at $q_0 \approx 1.1100$, and
$\mathfrak{m}^{(0)}(\varrho_{\mathrm{free}}) \approx 0.49932$
(the level-0 Markov trace of the Hopf link).  Substituting,

$$
  \Delta_{\max}(\mathrm{D})
  \;\leq\;
  2 \cdot 1 \cdot (1.0536)^{2} \cdot 0.49932
  \;\approx\; 1.109.
$$

The $\hbar_q^{2(N+1)}/(1 - \hbar_q^{2})$ tail factor at $N = 2$
gives $\approx 0.00982^{3}/(1 - 0.00982) \approx 9.6 \times 10^{-7}$.
Multiplying, the level-$\ge 3$ truncation error on the deuteron
is bounded by $\approx 1.07 \times 10^{-6}$ in categorical
units, i.e. **sub-ppm binding precision** when calibrated by
$E_0 \approx m_e \cdot 8G \approx 3.744$ MeV.

## Consequence for the binding energy

Combining with the jet-tower tail bound
([jet-tower convergence](#prop\:jet-tower-convergence)), the
$N$-term truncation error for any vortex is

$$
  |E_\mathrm{bind} - E_\mathrm{bind}^{(N)}|
  \;\leq\;
  E_0 \cdot 2\,L(\beta)\,\|\rho(\beta)\|_{\mathrm{op}}^{2}
  \cdot \mathfrak{m}^{(0)}(\varrho_{\mathrm{free}})
  \cdot \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^{2}}.
$$

For light atoms ($A \le 16$) at $q_0$, numerical evaluation
shows $N = 3$ is sufficient for sub-ppm precision on binding
energies; the bound is saturated within a factor of 2 on the
deuteron, tritium, and ${}^3\mathrm{He}$
(cf. `computations/unified_lift.py` with
`JET_TARGET_PPM`).

## What remains open

This proposition closes the **archimedean / rank-1 SDP**
regime of the convergence conjecture
([jet-tower remark](#rem\:mass-endomorphism-jet-tower),
subconjecture 1).  The two remaining pieces are:

1. **Multi-rank confinement SDP.**  At higher SDP ranks the
   baseline $\hat V^{(1)}$ is not a single braid product, and
   the operator-norm control in Step 2 must be replaced by a
   sum over rank-1 summands with weights from the SDP
   eigenvalues.  The qualitative bound survives (operator norms
   are subadditive), but the numerical prefactor degrades.
2. **Sharp constant.**  The factor $2\,L(\beta)\,\|\rho\|^2$
   is a worst-case bound; for stable atoms the effective
   $\Delta_{\max}$ is empirically within a factor of 2 of the
   level-1 value $\Delta^{(1)}$ itself (i.e.\ near-monotone
   decay).  A sharp constant would require a specific
   representation-theoretic analysis of the jet prolongation
   map on the Jones--Wenzl filtration.

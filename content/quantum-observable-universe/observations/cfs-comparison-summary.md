Finster's causal fermion systems (CFS)
[`finster2021`, `finster2022`, `finster2024`, `dappiaggi2024`] are a
parallel programme for unifying quantum field theory with general
relativity. CFS posits a Borel measure $\rho$ on a set of operators
with bounded signature, with dynamics determined by a causal action
$\mathcal{S}_{\mathrm{CFS}} = \iint \mathcal{L}_{\mathrm{CFS}}(x, y)\,d\rho\,d\rho$
where $\mathcal{L}_{\mathrm{CFS}}$ is built from differences
$\lvert\lambda_i\rvert - \lvert\lambda_j\rvert$ of eigenvalues of the
operator product $x \cdot y$. The non-commutative probability lens
of this section places CFS and QOU on common ground; the comparison
yields three structural conclusions.

**What can be shown.**

1. *Same carrier algebra.* Both QOU's inductive-limit Hecke algebra
   $(H_\infty(q), \mathrm{tr}_M)$ — embedded via Jones–Wenzl GNS as a
   type II$_1$ factor
   ([algebraic GNS embedding](#prop:algebraic-gns-embedding)) — and
   CFS's regularised operator algebra (after Planck-scale UV cutoff)
   are finite type II$_1$ factors with faithful tracial state.

2. *Same universality class.* Under joint Faddeev / Kerov–Vershik
   scaling, both sit in the free-probability universality class
   (Voiculescu–Biane, Féray–Méliot
   [`biane1998`]); the asymptotic spectral measure of QOU under the
   q-Plancherel weight
   ([q-Plancherel asymptotic skeleton](#prop:q-plancherel-asymptotic-skeleton))
   and CFS's universal measure $\rho$ are objects in the same class
   of free-probability spectral distributions.

3. *Common commutative-shadow data type.* The traceful Plancherel
   projection $\Pi_{\mathrm{tr}} \colon (A_q, \mathrm{tr}_M) \to
   (\widehat{A}_q, \tilde w_\lambda, \{\chi_\lambda\})$ sends QOU's
   non-commutative algebraic data to a (measure, functional-family)
   pair on the commutative spectrum — structurally a CFS-style data
   type. The kernel of $\Pi_{\mathrm{tr}}$ contains commutators,
   braid relations, knot crossing-order, and non-trace free-probability
   cumulants: data QOU has and CFS structurally cannot represent.

**What differs.**

The two continuum theories evaluate **different real-valued
functionals** on the shared spectral data. The QOU natural quadratic
kernel is the Frobenius Gram matrix
$G(x, y) := \mathrm{tr}_M(x \cdot y)$ (bilinear, trace-additive in
the spectrum of $x \cdot y$). The Finster causal Lagrangian
$\mathcal{L}_{\mathrm{CFS}}(x, y)$ is built from eigenvalue
*differences* (non-linear, trace-subtractive).

This functional mismatch is exhibited concretely:

- **Strict pointwise mismatch at $n = 2$.** On the unit pair
  $(1, 1) \in H_2(R, q) \times H_2(R, q)$:
  $$
    G(1, 1) = \mathrm{tr}_M(1) = 1
    \qquad\text{but}\qquad
    \mathcal{L}_{\mathrm{CFS}}(1, 1) = 0
  $$
  (Finster's pair-difference functional vanishes when all eigenvalues
  of $x \cdot y$ are equal).

- **Integral mismatch under any centered free-probability limit.**
  By a parity argument: $G$ is *odd* under $x \mapsto -x$ (trace is
  linear), $\mathcal{L}_{\mathrm{CFS}}$ is *even* (depends on
  $\lvert\lambda\rvert$). Under any centered limit measure
  $\rho_\infty$ symmetric under $x \mapsto -x$:
  $\langle G \rangle_{\rho_\infty\otimes\rho_\infty} = 0$ but
  $\langle \mathcal{L}_{\mathrm{CFS}}\rangle > 0$ strictly, by
  Finster's non-negativity.

- **Explicit algebraic decomposition.** Even taking the squared
  QOU kernel $G_2(x, y) := \mathrm{tr}_M((x\cdot y)^2)$ (an *even*
  modification of $G$) does not produce equality. For self-adjoint
  $x, y$ with real-spectrum product on a block of dimension $n$
  with normalised Markov trace ($\mathrm{tr}_M(1) = 1$), the Finster
  pair-difference Lagrangian admits the identity
  $$
    \mathcal{L}_{\mathrm{CFS}}(x, y)
    \;=\; n^{2}\,\bigl(G_2(x, y) \;-\; \lVert x \cdot y\rVert_1^{\,2}\bigr),
  $$
  where $\lVert x \cdot y\rVert_1 = \mathrm{tr}_M\lvert x \cdot y\rvert$
  is the (normalised) trace-class norm. Equivalently, after
  normalising $\mathcal{L}_{\mathrm{CFS}}$ by $n^{2}$:
  $\mathcal{L}_{\mathrm{CFS}}^{(\mathrm{norm})}(x, y) = G_2(x, y) -
  \lVert x \cdot y\rVert_1^{\,2}$. So the Finster action equals
  QOU's energy-quadratic *minus* an explicit trace-class
  correction. The correction term $\lVert x \cdot y\rVert_1^{\,2}$
  is the "concentration penalty" that distinguishes CFS dynamics
  from QOU's natural quadratic dynamics; on the unit pair
  $(1, 1)$ it equals $G_2$, giving $\mathcal{L}_{\mathrm{CFS}}(1,1) = 0$
  exactly.

**Open numerical question.** Whether the correction moment
$\langle \lVert x \cdot y\rVert_1^{\,2}\rangle_{\rho_\infty}$ might
*coincidentally* vanish at the QOU substrate value $q_0 \approx
1.110$ remains open — generically expected to be non-zero given the
full support of the limit measure. If this single moment integral
were to vanish at exactly $q_0$, QOU and CFS would predict equal
total action values at the substrate (though still differ in local
dynamics by the pointwise mismatch above). Otherwise, QOU and CFS
are confirmed as **distinct continuum theories of the same
operator-algebra substrate**, differing by a named correction term
in their action functionals.

**Consequence for QOU.** The framework developed in this section —
non-commutative probability, q-CLT, Jones–Wenzl carrier, Plancherel
asymptotics — stands independently of any CFS comparison. The
specific QOU phenomena that CFS cannot natively express (knot
topology, braid statistics, chirality, Gröbner–Shirshov reduction)
are *pre-projection* algebra data, killed by $\Pi_{\mathrm{tr}}$ and
therefore outside the reach of any commutative-shadow framework.
These are also the QOU phenomena from which particle physics is
derived — confirming that QOU's predictions are *not* recoverable
from a Finster-style continuum theory alone.

A detailed comparison block-by-block is deferred to a separate work;
this remark records only the summary status.

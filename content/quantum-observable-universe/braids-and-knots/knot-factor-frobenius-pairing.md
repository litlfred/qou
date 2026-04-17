**Proposition.**
*The knot factor $a(N)$ from the nuclear-braid Bethe-Weizsäcker
formula ([nuclear knot classification](#prop:nuclear-knot-classification))
is the **Frobenius self-pairing ratio** of the atom braid word
against the free-nucleon baseline.  In the rigid monoidal category
$\mathbf{C}$ ([fibre-functor rigidity](#prop:fibre-functor-rigidity)),
every element $X \in \mathrm{End}_{\mathbf{C}}(A)$ has a categorical
dual $X^\dagger$ and a non-degenerate Frobenius pairing*

$$
  \langle X, Y \rangle_F \;=\; \mathrm{tr}_M(X \cdot Y^\dagger)
  \;\in\; R
$$

*valued in the ground ring $R = \mathbb{Z}[q, q^{-1}]$.  The knot
factor is:*

$$
  a(N)
  \;=\; \frac{\langle W_{\mathrm{nuclear}}, W_{\mathrm{free}} \rangle_F}
             {\langle W_{\mathrm{free}}, W_{\mathrm{free}} \rangle_F}
$$

*— the Frobenius projection of the nuclear atom braid onto the
free-nucleon subspace, normalised by the free-nucleon self-pairing.*

*The **bulk categorical binding** is the $\hbar_q^2$-weighted
deviation from this ratio:*

$$
  \boxed{\;
    B_{\mathrm{bulk}}(Z, N)
    \;=\; m_e \cdot \hbar_q^2 \cdot
      \frac{\lVert W_{\mathrm{atom}} \rVert_F^2 - \lVert W_{\mathrm{free}} \rVert_F^2}
           {\lVert W_{\mathrm{free}} \rVert_F^2}
  \;}
$$

*replacing the empirical $\lambda_V \cdot A + \lambda_S \cdot A^{2/3}
+ a(N) \cdot \mathrm{(old BW)}$ structure with a single categorical
scalar.*

*Proof.*
By [fibre-functor rigidity](#prop:fibre-functor-rigidity), the
ambient category $\mathbf{C}$ is rigid monoidal; every object $A$
has a dual $A^*$ and the Frobenius pairing is non-degenerate.  The
adjoint trace
([adjoint trace](#def:adjoint-trace)) descends to a symmetric
bilinear form on $\mathrm{End}_{\mathbf{C}}(A)$ valued in
$\mathbf{1}_{\mathbf{C}}$.

For the Hecke algebra $H_n(q) \subset \mathrm{End}_{\mathbf{C}}(A)$,
the Markov trace realises this Frobenius pairing.  Decomposing
into Wedderburn blocks
([BW coefficient shadow price](#prop:bw-coefficient-shadow-price)):

$$
  \langle X, Y \rangle_F \;=\; \sum_\lambda w_\lambda \cdot
    \frac{\chi_\lambda(X \cdot Y^\dagger)}{d_\lambda}
$$

For $X = Y = W$, this reduces via the class-function property to

$$
  \lVert W \rVert_F^2 \;=\; \sum_\lambda w_\lambda \cdot
    \left| \frac{\chi_\lambda(W)}{d_\lambda} \right|^2
$$

— the **Schur-Weyl norm**, a positive-definite bilinear form on
the archimedean realisation $R \otimes \mathbb{R}$.

**Knot-factor specialization.**
For small $A$ the Markov trace is dominated by the braid's **knot
type**:
- $A = 3$ (figure-8 nuclear braid): $\lVert W \rVert_F^2 / \lVert W_{\mathrm{free}} \rVert_F^2 = 1 - h^2$
  — the Skein-polynomial eigenvalue of $4_1$ at $\sigma^2$,
  recovering $a(N) = 1 - h^2$ from the old BW.
- $A = 4$ (Borromean): $(1 - h^2)^2$ by tensor-product factorisation
  (two independent amphicheiral figure-eight closures).
- $A = 2$ (satellite): $1 + h$ — single chiral $pn$ pair.

For $A \geq 5$ the formula generalises beyond the small-knot
regime: $\lVert W \rVert_F^2$ depends on the full braid-word
structure, no longer reducing to a per-pair product.  This is the
**deformation** of the knot factor at large $A$.

**Frobenius reciprocity.**
For the Hecke tower $H_n(q) \supset H_{n-1}(q)$, by Frobenius
reciprocity:

$$
  \mathrm{Hom}_{H_n}(\mathrm{Ind}\, V, W)
    \;\cong\; \mathrm{Hom}_{H_{n-1}}(V, \mathrm{Res}\, W)
$$

The knot factor is the **Frobenius-reciprocity defect** of the
atom braid from being the simple induced product of disconnected
nucleons:

$$
  \mathrm{Res}\, W_{\mathrm{atom}} \;=\;
  a(N) \cdot W_{\mathrm{free}} \;+\; \text{(higher-order, } A \ge 5\text{)}
$$

At leading order in $h = q - q^{-1}$, the defect vanishes
(disconnected nucleons are trivially restricted).  The non-trivial
knot-type contribution at $A = 3, 4$ appears at order $h^2$.

**Base-ring behaviour.**
The Frobenius pairing $\langle X, Y \rangle_F \in R$ is
base-ring-independent
([base-field independence](#rem:base-field-independence)).  Over
the archimedean realisation ($R \to \mathbb{R}$ at $q = q_0$) it is
a positive-definite form; over $\mathbb{F}_p$ or $\mathbb{Q}_p$ it
is only a non-degenerate bilinear form — the notion of
"positivity" requires an ordered-field structure, which finite and
$p$-adic fields lack.

The BULK BINDING ENERGY is an archimedean quantity (it's a
measured physical mass defect); its categorical formulation via
the Frobenius pairing lives in $R$ but the observation that it is
POSITIVE REAL is an archimedean specialization.

$\square$

**Witness.**
`folio-assistant/computations/hecke_core.py`:
- `atom_frobenius_norm_sq(Z, N, k_cap)`: $\lVert W_{\mathrm{atom}} \rVert_F^2$
  via Schur-Weyl sum over partitions.
- `binding_from_frobenius_pairing(Z, N)`: the $B_{\mathrm{bulk}}$
  formula above.

**Current status (2026-04):**
Implementation is a first-pass scaffold: the free-nucleon
baseline $\lVert W_{\mathrm{free}} \rVert_F^2$ is approximated by
the Wedderburn-trace identity value $\Sigma w_\lambda = 1$ rather
than the proper tensor-product decomposition via
$H_3(q)^{\otimes A} \hookrightarrow H_{3A}(q)$.  Numerical values
from this scaffold are preliminary.  A subsequent commit should
implement the disconnected-tensor baseline exactly.

**Related**:
- Replaces the scaling functions $\lambda_V \cdot A +
  \lambda_S \cdot A^{2/3}$ of the old BW path, now retired.
- Complementary to the LP-dual shadow-price corrections
  ([BW coefficient shadow price](#prop:bw-coefficient-shadow-price))
  and SDP cross-channel terms
  ([SDP regime switch](#prop:sdp-regime-switch)).
- Categorically grounded in $q$-heat equation framework
  ([$q$-heat equation](#def:q-heat-equation)) via the ℏ_q² prefactor
  from the pure-spin $\Delta_\xi$ eigenvalue.

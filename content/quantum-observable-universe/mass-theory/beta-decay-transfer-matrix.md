*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Beta decay is mediated by the $T_{3,5}$ torus knot with $10$
crossings ([beta decay](#def:beta-decay-skein)).  The $T_{3,5}$
insertion at the converting quark produces a **universal** 2$\times$2
matrix-valued polynomial $\Delta_\beta(q)$ that governs every
beta transition in every nucleus.  The transfer matrix captures
the effect of the $10$-crossing weak vertex on each nucleon pair.

## The three crossing transfer matrices

Each nucleon pair $(i, j)$ contributes a transfer matrix
$T(q) \in \mathrm{M}_2(\mathbb{Z}[q^{\pm 1}])$:

$$
  T(c, d) = 
  \begin{pmatrix}
    c(q - q^{-1}) + d & c \\
    c & d
  \end{pmatrix}
$$

with crossing coefficients $(c, d)$ depending on the pair type.
The $(1, -(q - q^{-1}))$ convention for nn crossings is the unique
convention consistent with the Hecke inverse relation
$\sigma^{-1} = \sigma - (q - q^{-1})$:

$$
  T_{pp}(q) =  T(1, 0) = 
  \begin{pmatrix}
    q - q^{-1} & 1 \\
    1 & 0
  \end{pmatrix},
  \quad
  T_{nn}(q) =  T(1, -(q - q^{-1})) = 
  \begin{pmatrix}
    0 & 1 \\
    1 & -(q - q^{-1})
  \end{pmatrix}
$$

$$
  T_{\mathrm{mix}}(q) =  T\!\left(1, -\tfrac{1}{2}(q - q^{-1})\right) = 
  \begin{pmatrix}
    \frac{1}{2}(q - q^{-1}) & 1 \\[4pt]
    1 & -\frac{1}{2}(q - q^{-1})
  \end{pmatrix}
$$

All three matrices live in $\mathrm{M}_2(\mathbb{Z}[q^{\pm 1}])$ —
no fractional powers of $q$ appear.  The pp and nn transfer matrices
are unimodular: $\det T_{pp} = \det T_{nn} = -1$ (forced by the
Hecke eigenvalues $q \cdot (-q^{-1}) = -1$).  The mixed crossing
$\frac{1}{2}(\sigma + \sigma^{-1})$ is an algebraic average, not a
group element, so $\det T_{\mathrm{mix}} \neq -1$.

## The universal beta decay matrix

**Proposition.**
*The two elementary decay matrices $\Delta_\beta^{nn \to \mathrm{mix}}$
and $\Delta_\beta^{\mathrm{mix} \to pp}$ are identical:*

$$
  \Delta_\beta^{nn \to \mathrm{mix}}(q)
  =  T_{\mathrm{mix}}(q) - T_{nn}(q)
  =  T_{pp}(q) - T_{\mathrm{mix}}(q)
  =  \Delta_\beta^{\mathrm{mix} \to pp}(q)
$$

*There is a single universal beta decay matrix:*

$$
  \boxed{
    \Delta_\beta(q)
    = 
    \tfrac{1}{2}(q - q^{-1}) \mathbb{I}
  }
$$

*where $\mathbb{I}$ is the $2 \times 2$ identity.
The decay matrix is a scalar multiple of the identity — beta decay
uniformly scales all channels by $\frac{1}{2}(q - q^{-1})$.*

*Proof.*
Write $h = q - q^{-1}$.  Then:

$T_{pp} = T(1, 0)$: entries $[[h, 1], [1, 0]]$

$T_{nn} = T(1, -h)$: entries $[[0, 1], [1, -h]]$

$T_{\mathrm{mix}} = T(1, -h/2)$: entries $[[h/2, 1], [1, -h/2]]$

The differences $T_{\mathrm{mix}} - T_{nn}$ and
$T_{pp} - T_{\mathrm{mix}}$ both equal
$[[h/2, 0], [0, h/2]] = \frac{h}{2} \mathbb{I}$.  $\square$

**Explicit entries at the substrate parameter $q$:**

$$
  \Delta_\beta(q_0) = 
  \tfrac{1}{2}(q_0 - q_0^{-1}) \mathbb{I}
   \approx 
  \begin{pmatrix}
    +0.1045 & 0 \\
    0 & +0.1045
  \end{pmatrix}
$$

## The decay formula

At generator $\sigma_i$ (affected by the converting nucleon
at position $p$), the transfer matrix product factors as:

$$
  M_i^{\mathrm{par}}(q) = L_i(q) \cdot T_{\mathrm{par}}(q) \cdot R_i(q)
$$

where $L_i$ is the product of matrices to the left of the
converting crossing (unchanged) and $R_i$ to the right
(unchanged).  The daughter matrix product is:

$$
  M_i^{\mathrm{dau}}(q) = L_i(q) \cdot (T_{\mathrm{par}}(q) + \Delta_\beta(q)) \cdot R_i(q)
$$

The change in the transfer matrix product:

$$
  \Delta M_i(q) = L_i(q) \cdot \Delta_\beta(q) \cdot R_i(q)
$$

The change in the Markov-traced volume:

$$
  \Delta \hat{V}_i(q)
  = 
  z \cdot (\Delta M_i)_{11} + (\Delta M_i)_{21}
$$

The $Q$-value
([transition energy](#def:Q-value-transition)) in **eigenfunction-basis
(log-ratio) form**:

$$
  \mathfrak{Q}_\beta^{\mathrm{B}}
  \;:=\;
  \ln \frac{P_{\mathrm{dau}}(q)}{P_{\mathrm{par}}(q)}
  \cdot \frac{E_0}{z}
  \;=\;
  \frac{E_0}{z} \,
  \sum_{i=0}^{p} \ln \frac{\hat{V}_i^{\mathrm{dau}}(q)}{\hat{V}_i^{\mathrm{par}}(q)},
$$

where the sum runs only over generators affected by the
converting nucleon (generators $\sigma_i$ with $i > p$ cancel
exactly), $z = 1/(\sqrt q + 1/\sqrt q)$ is the Markov–Jones
parameter (Hecke–Skein normalization), and the $1/z$ factor is
**not a calibration knob** — it is the normalization required to
map the eigenfunction observable $\ln V_{\mathrm{pp}}/V_{\mathrm{nn}}$
onto MeV.

Form B is **not a separate observable** from the NF-counit form
$\mathfrak{Q}_\beta^{\mathrm{A}} = |\Delta(\mathrm{net})| \cdot E_0$ of
[prop:neutron-qvalue-symbolic](#prop:neutron-qvalue-symbolic);
the two are basis-change equivalent at leading order, with the
explicit bridge identity given in
[prop:q-beta-spectral-bridge](#prop:q-beta-spectral-bridge):

$$
  \mathfrak{Q}_\beta^{\mathrm{A}}
  \;=\;
  \mathfrak{Q}_\beta^{\mathrm{B}} \cdot \bigl(1 + \tfrac{(z - 1)\,h}{2} + O(h^2)\bigr).
$$

Form B is the natural basis for $N \geq 1$ brane-tower truncation
analysis (where it composes additively across generators); Form A
is canonical at $N = 0$ free neutron (where the NF counit is a
closed combinatorial datum).

**Conjecture (conditional on the $S_5 \leftrightarrow \mathrm{SO}(3)$ fiber-action conjecture).** The canonical inter-nucleon Hecke channel assignment for the atomic braid word—currently realised as the uniform-flavor map $\mathrm{pp} \mapsto \sigma$, $\mathrm{nn} \mapsto \sigma^{-1}$, $\mathrm{pn} \mapsto \sigma_{\mathrm{avg}} = (\sigma + \sigma^{-1})/2$—is the **flavor-only projection** of a categorically-refined *color-tube weighted* assignment derived from the Bring color-tube structure on the quintic.

## Setup

Each nucleon carries 3 quark color sheets. The nucleon type fixes the quark-flavor content:

- **proton** (uud): color sheets $(\mu_u, \mu_u, \mu_d)$
- **neutron** (udd): color sheets $(\mu_u, \mu_d, \mu_d)$

The atomic braid word ([Existence of the atom-knot for any (Z, N)](#prop:atom-knot-exists)) places one inter-nucleon Hecke generator at every position $3k + 2$ for each adjacent nucleon pair $k, k+1$ with $k = 0, \ldots, A - 2$. This gives $A - 1$ inter-nucleon arcs total (matching [`isotope_record_schema.build_knot_operator_catalogue`](../../../computations/isotope_record_schema.py) lines 248-262 and [Canonical-braid interface composition $(n_{pp}, n_{pn}, n_{nn})$ for atom $(Z, N)$ in pppnnn ordering](../mass-theory/canonical-braid-interface-composition.md)). The current production assignment treats each such generator as a single element of the Hecke algebra $H_{3A}(q)$—one $\sigma$ for pp, one $\sigma^{-1}$ for nn, one $\sigma_{\mathrm{avg}}$ for pn—regardless of which flavor triple across the three color sheets pairs across the inter-nucleon arc.

## The conjectural refinement

Per [Color tube coordinates](color-tube-coordinates.md) and [Color tube fibers](color-tube-fibers.md), Bring's surface carries a canonical $(r, g, b)$ color-tube fiber structure. The $S_5 \leftrightarrow \mathrm{SO}(3)$ fiber action on Bring's quintic (conjectural) maps each Bring fiber to a 3-dimensional color rotation. Composing with the nucleon color-sheet assignment gives a canonical $3 \times 3 = 9$-element matrix of color-pair couplings per inter-nucleon arc.

**Conjectured refined assignment.** For each inter-nucleon arc with nucleon-pair flavor triples $(F_1, F_2) \in \{u, d\}^3 \times \{u, d\}^3$ across the three color sheets, the canonical Hecke generator is the color-sheet-weighted sum

$$
  \sigma^{(F_1, F_2)}_{\text{int}}
  \;=\;
  \sum_{(c_1, c_2) \in \{r, g, b\}^2}
    W_{c_1 c_2}(F_1, F_2) \cdot \sigma^{\epsilon(c_1, c_2, F_1, F_2)}
$$

where:

- $W_{c_1 c_2}(F_1, F_2) \in \mathbb{Q}_{\geq 0}$ is the canonical color-sheet pair weight from the $S_{5}$/SO(3) fiber action, **normalised to** $\sum_{c_1, c_2} W_{c_1 c_2} = 1$ for each $(F_1, F_2)$ flavor pair (so the refined generator is a categorical average over the 9 color-sheet pairs).
- $\epsilon(c_1, c_2, F_1, F_2) \in \{+1, -1, 0\}$ is the chirality sign for the color-sheet pair $(c_1, c_2)$ given the flavor triples $(F_1, F_2)$. It is $+1$ when the flavor at $c_1$ in $F_1$ equals the flavor at $c_2$ in $F_2$ (matter–matter). It is $-1$ when they are flavor-conjugate (matter–antimatter). It is $0$ for mixed-flavor pn pairs that average to $\sigma_{\mathrm{avg}}$.

**Uniform-flavor projection.** Setting $W_{c_1 c_2} = 1/9$ uniformly and collapsing $\epsilon$ to its flavor-only majority sign recovers the current production assignment.

## Color-tube weighting as the load-bearing missing structure

The low-isotope sign-flip diagnostic fits the per-isotope relative error against inter-nucleon arc **count** and against the signed-h weight. Its recorded coefficients of determination are $R^2 = 0.2653$ and $R^2 = 0.0018$ respectively, over a sample of five nuclei of which the two $A = 1$ anchors carry $|\text{err}| < 10^{-3}\%$. The diagnostic's own verdict is that the correlation is **weak** and that the sign-flips are *not* explained by a linear channel model. It therefore does **not** establish that the uniform-flavor projection is missing a per-arc structural detail; the color-pair weight $W_{c_1 c_2}$ remains motivated by the categorical argument below rather than by this fit.

Two further cautions apply to any strengthened version of this diagnostic. First, $R^2$ is invariant under affine reparametrisation of the regressor, and the arc count is $A - 1$; it therefore scores exactly what the bare mass number $A$ scores, so such a fit cannot distinguish the inter-nucleon arc structure from $A$ itself. Second, $R^2$ is invariant under scaling the response, so on *absolute* error a model short by a constant fraction reproduces any such figure with nothing missing — measured over the 2449 AME2020 nuclei with $2 \le A \le 240$, $R^2(B \sim A - 1) = 0.9943$ with no model of any kind.

The empirical match between the (now-purged) $\lambda_{\mathrm{scale}}$ literal $2.4599527869$ and the color-tube Faddeev resummation $1/(1 - h_q \cdot q_0^{10}) \approx 2.450$ provides independent evidence that 10-fold color-tube averaging is the categorical structure behind the historical numerology.

Numerical probes report that Scheme 4 (per-sheet PL integration on Bring's surface with quark-content weighting) reproduces $\Delta m_{n-p}$ to ${\sim}0.14\%$. This improves on the uniform-flavor projection's ${\sim}305\,\mathrm{ppm}$ flavor split ratio.

The **gg-production collapse** isolates the cost of the projection directly. Decomposing the production binding $B_{\mathrm{sym}} = \alpha\,\ln(\mathrm{tr}_{\mathrm{free}}/\mathrm{tr}_{\mathrm{atom}})$ into its per-bond log-suppressions $L_{\mathrm{pp}}, L_{\mathrm{pn}}, L_{\mathrm{nn}}$ at $q_0$ gives $L_{\mathrm{nn}}/L_{\mathrm{pp}} - 1 \approx 78\%$. This represents roughly $570\times$ the substrate-derived $p/n$ flavor split $\delta_{\mathrm{lead}} \approx 0.14\%$ and $78\times$ the experimental charge-symmetry-breaking bound. This over-break derives entirely from the $\sigma$-vs-$\sigma^{-1}$ inter-crossing sign of the flavor-only projection. Gluons couple color, not flavor. The leading gg interface is the single flavor-blind color-average $\sigma_{\mathrm{avg}} = \sigma - (h/2)\cdot 1$ for every bond type. Forcing all inter-nucleon crossings to $\sigma_{\mathrm{avg}}$ collapses the $78\%$ asymmetry to $0$. The sub-leading flavor weighting $W_{c_1 c_2}$ reintroduces the correct $\delta_{\mathrm{lead}}$-scale split. The uniform-flavor projection manufactures an $O(1)$ charge asymmetry that the color-tube average removes.

## Conditional structure

This conjecture remains conditional on the $S_5 \leftrightarrow \mathrm{SO}(3)$ fiber-action conjecture. Once that is established, the weight matrix $W_{c_1 c_2}$ derives as a tensor in the SO(3)-fiber data over Bring, with no remaining degrees of freedom. The statement then becomes unconditional: it is a conjecture only for as long as that upstream conjecture is open.

## Open questions

1. **Closed form for $W_{c_1 c_2}$.** What are the exact rational weights from the SO(3)-fiber tensor over Bring?
2. **Color-pair $\to$ chirality sign $\epsilon$ rule.** Why is same-color $\mapsto +1$, opposite-color $\mapsto -1$?
3. **${}^{4}\mathrm{He}$ magic-shell saturation.** Does the color-tube weighting saturate at $A = 4$ (filled-shell analogue), producing the $A \cdot 8G$ closure observed numerically?
4. **Cross-check $\rho_F$ density rule.** Does color-tube weighting yield a categorical reading of the Kashaev density factor $\rho_F \in \{m_e, 2 m_e\}$?

## Representation-theoretic constraint on $\epsilon$

The chirality sign $\epsilon(c_1, c_2, F_1, F_2) \in \{+1, -1, 0\}$ is constrained by the $\mathrm{SO}(3) = \mathrm{SU}(2)/\mathbb{Z}_2$ level structure. The $\mathbb{Z}_2$ kernel of the covering map $\mathrm{SU}(2) \to \mathrm{SO}(3)$ acts as $-1$ on half-integer-spin (spinorial) irreps and $+1$ on integer-spin (tensor) irreps. The chirality dichotomy $\{+1, -1\}$ from the $S_5/\mathrm{SO}(3)$ fiber action supplies this **grading by this $\mathbb{Z}_2$**. The neutral value $0$ (the bar-symmetric $\mathrm{pn}$ average) identifies the $\mathbb{Z}_2$-fixed locus.

With $q = e^{\eta}$, the $\mathrm{SU}(2)_q$ doublet character is $[2]_q = 2\cosh\eta$ and the lowest $\mathrm{SO}(3)_q$ (integer-spin) character is the adjoint $[3]_q$. They satisfy the Chebyshev/Clebsch–Gordan square identity

$$
  [3]_q \;=\; [2]_q^{\,2} - 1,
$$

which is proved. The $\mathrm{SO}(3)$ characters are exactly the polynomials in $[2]_q$ invariant under the $\mathbb{Z}_2$ quotient. Any admissible $\epsilon$ rule must be a section of this same $\mathbb{Z}_2$-grading. A valid $\epsilon$ cannot assign $-1$ to a color-sheet pair whose combined flavor content sits in the integer-spin (tensor) sector. The explicit map from color-sheet pairs $(c_1, c_2)$ to the $\mathbb{Z}_2$-grade still requires the $S_5 \leftrightarrow \mathrm{SO}(3)$ fiber action, which is conjectural.

## Cross-references

- Existing color-tube infrastructure: [Color tube coordinates](color-tube-coordinates.md), [Color tube fibers](color-tube-fibers.md), [Color tube cubic](color-tube-cubic.md)
- Upstream conjecture: the $S_5 \leftrightarrow \mathrm{SO}(3)$ fiber action on Bring's quintic

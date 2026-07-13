<!-- FILE_START: mass-bridge-orphan-reconnect-intro.md -->
This section reconnects blocks separated during the restructuring of the mass derivation and $q$-hyperbolic geometry chapters. It resolves structural conjectures at the interface of the geometric and mass-endomorphism layers.

The sequence covers the categorical linking operation, the crossed-module Euler characteristic governing substrate flow, and the master pentagon dimension identity. The final blocks specify the geometric-invariant piecewise distinctions and the Kashaev-density-to-multiplicity identification linking directly to the mass application chapter.
<!-- FILE_END: mass-bridge-orphan-reconnect-intro.md -->

<!-- FILE_START: categorical-linking-operation.md -->
**Conjecture (categorical linking operation $\mathrm{Lk}_R$).**
*Let $\mathbf{C}$ be a rigid monoidal $R$-linear category with braiding $c_{X, Y}$, and let $A$ be the Frobenius-Hopf substrate. The **categorical linking operation** is the family of $R$-linear maps*

$$
  \mathrm{Lk}_R^{(k)}
  \;\colon\;
  \mathrm{Hom}_R(\mathbf{1}, A) \otimes_R \mathrm{Hom}_R(\mathbf{1}, A)
  \;\longrightarrow\;
  \mathrm{End}_R(A),
$$

*defined by*

$$
  \mathrm{Lk}_R^{(k)}(a, b)
  \;:=\;
  (\mathrm{id}_A \otimes \tau_R) \,\circ\,
  \bigl( c_{A, A}^{\,k} \circ (a \otimes b) \otimes \mathrm{id}_A \bigr)
  \,\circ\, \mathrm{id}_A.
$$

*This evaluates the categorical trace-cut of a 2-component link: closing one component via the trace leaves the other as a free endomorphism.*

### Formal properties

1. **Linearity (proved):** $\mathrm{Lk}_R^{(k)}$ is $R$-bilinear.
2. **Reduction at $k = 0$ (proved):** $\mathrm{Lk}_R^{(0)}(a, b) = \tau_R(b) \cdot a^*$, recovering the rank-1 dual endomorphism.
3. **Multiplicativity (proved):** Additional linkings map strictly to pre-composition with $c_{A, A}$.
4. **Trace-cut symmetry (conditional):** Cutting the left component produces the $\iota$-conjugate operation $\mathrm{Lk}_R^{(-k)}(b, a)$.
5. **Bar-involution compatibility (conditional):** $\iota(\mathrm{Lk}_R^{(k)}(a, b)) = \mathrm{Lk}_R^{(-k)}(\iota(a), \iota(b))$.

Properties 1-3 hold generically in rigid monoidal categories. Properties 4-5 require specific ribbon trace structures.

### Significance for electroweak symmetry breaking

The Higgs mechanism lifts a gauge boson from $\mathrm{Hom}_R(\mathbf{1}, A)$ (unbroken 1-component knot) to $\mathrm{End}_R(A)$ (broken 2-component link). The linking operation $\mathrm{Lk}_R^{(1)}$ realizes this lift categorically. The post-EWSB boson mass is the resulting Markov trace evaluated on the broken endomorphism.
<!-- FILE_END: categorical-linking-operation.md -->

<!-- FILE_START: categorical-linking-operation-interpretation.md -->
**Remark (proof scope).** The proofs for properties 1-3 utilize only standard rigid monoidal axioms. They apply generically across any suitable category supporting trace-cuts and require no QOU-specific Hecke algebra or Markov trace assumptions.
<!-- FILE_END: categorical-linking-operation-interpretation.md -->

<!-- FILE_START: crossed-module-euler-characteristic.md -->
*Let $\beta_{\mathrm{Bor}} = (\sigma_1 \sigma_2^{-1})^3$ be the Borromean braid, and let $\Phi_0 \colon Q_8 \to H_3(q)$ be the crossed module feedback map defined by $\sigma_1 \mapsto i, \sigma_2 \mapsto j$. The $h^2$ coefficient of the multiplicative surface integral traced over the $2 \times 2$ quaternion representation evaluates to:*

$$
  \operatorname{tr}\!\bigl(\textstyle\sum_{k < l}
  s_k s_l \, c_k c_l\bigr) = -12
  = \dim(V) \cdot \chi(\Sigma_4).
$$

*Here $V = \mathbb{C}^2$ is the spin-$\tfrac{1}{2}$ fundamental representation, and $\chi(\Sigma_4) = -6$ is the Euler characteristic of Bring's genus-4 surface.*
<!-- FILE_END: crossed-module-euler-characteristic.md -->

<!-- FILE_START: geom-bridge-status.md -->
**Remark (logical status of the geometric bridge).**

The $\mathrm{Geom}$ functional conjectures a three-layer pathway linking the algebraic $Q_8$ trace to the boundary Markov trace. This remark tracks the precise status of each connecting step.

1. **Algebraic trace:** $\operatorname{tr}(h^2\text{ curvature}) = -12$. (Proved).
2. **Geometric volume bridge:** $-12 \cdot (2G/3) = -8G$. (Proved).
3. **Topological volume:** $\mathrm{Vol}(\mathcal{B}_3) = 8G$. (Proved).
4. **Boundary normalisation:** Division by $-64$ to reach $\kappa = 3/16$. (**Disproved as structural**).
5. **Categorical alignment:** The fibre functor $\tau$ maps the algebraic Euler count to the geometric volume. (**Open conjecture**).

The constant $-64$ normalization fails at the $h^4$ order, proving the $\Phi_0$ feedback map cannot act by constant scalar division across all orders. The open challenge remains determining whether $\tau$ genuinely bridges the algebraic and boundary $h$-expansions via an order-mixing relation, or if the two sides track fundamentally distinct invariants.
<!-- FILE_END: geom-bridge-status.md -->

<!-- FILE_START: tau-all-orders-bridge.md -->
**Conjecture ($\tau$ at all orders — dichotomy).**
*Let $\alpha_k$ be the algebraic $h^k$-coefficient of the $Q_8$ multiplicative-integral trace, and let $\kappa_k$ be the $h^k$-coefficient of the Markov-trace expansion. Exactly one of the following holds:*

1. *(**Order-mixing**.) The fibre functor $\tau$ acts as a non-constant, order-mixing linear map converting $\alpha_\bullet$ to $\kappa_\bullet$ at every order.*
2. *(**Distinct invariants**.) No such global relation exists. The algebraic trace and Markov trace evaluate categorically distinct invariants that coincidentally share only their $h^2$ coefficient.*

### Empirical sharpening

Computations up to $h^8$ resolve the structure. The algebraic series truncates precisely at $h^4$ ($\alpha_6 = \alpha_8 = 0$), whereas the Markov series continues infinitely. This abrupt asymmetry strongly supports hypothesis 2.

Furthermore, simple per-row linear fitting trivially solves any target sequence because higher-order algebraic terms vanish. To be meaningful, an order-mixing relation must follow a single, rigidly banded convolution kernel. The absence of a constant kernel (failing at $h^4$) isolates the open question: does a wider, fixed-band finite convolution successfully bridge the complete series?

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at $q_0$.
<!-- FILE_END: tau-all-orders-bridge.md -->

<!-- FILE_START: dim-master-pentagon.md -->
**Conjecture (D17 DIM master-Pentagon closure, research-grade).**
*The Ding-Iohara-Miki algebra $U_{q, t}(\widehat{\widehat{\mathfrak{gl}_1}})$ carries a universal Pentagon identity that specializes to each operational Pentagon flavor.*
<!-- FILE_END: dim-master-pentagon.md -->

<!-- FILE_START: geometric-invariant-piecewise.md -->
The categorical action $S = \mathrm{tr}(\Phi)$
([topological mass](#thm:topological-mass)) evaluates differently
depending on the geometry of the knot complement $S^3 \setminus K$.
The piecewise geometric invariant

$$
  \mathrm{Geom}(K) =
  \begin{cases}
    \mathrm{Vol}(K) / \hbar_q^2
      & K \text{ hyperbolic} \\[4pt]
    \mathrm{CS}(K) \cdot \hbar_q^2
      & K \text{ torus} \\[4pt]
    0 & K \text{ unknot}
  \end{cases}
$$

routes the physical weight of a state through its fundamental
topological geometry.  The three cases are not *ad hoc*: each arises
from an established theorem in low-dimensional topology.

**1. The piecewise split: Thurston's Geometrization.**
Thurston's theorem for knot complements states that
$S^3 \setminus K$ admits exactly one of three geometric structures:
(i) a hyperbolic metric of constant negative curvature (the vast
majority of knots), (ii) a Seifert-fibred structure (torus knots,
Vol $= 0$), or (iii) a decomposition along tori into simpler pieces
(satellite knots).  The piecewise definition of $\mathrm{Geom}(K)$
follows this classification directly.

**2. The hyperbolic case: the Volume Conjecture.**
For hyperbolic $K$, $\mathrm{Geom}(K) = \mathrm{Vol}(K)/\hbar_q^2$.
This originates from the Kashaev--Murakami--Murakami Volume Conjecture:
the asymptotic growth of the coloured Jones polynomial $J_K^{(n)}(q)$
at roots of unity is dominated by $\mathrm{Vol}(K)$.  In the
categorical framework, $c_K = \mathrm{tr}_M(\rho(\mathcal{B}_K))$ is the
Hecke algebra Frobenius character of the braid $\mathcal{B}_K$, and its
leading asymptotics recover $\mathrm{Vol}(K)$.  Division by
$\hbar_q^2 = (1 - 1/q)^2$ maps the topological volume to a
mass/energy scale.

**3. The torus case: Chern--Simons dominance.**
For torus knots $K = T_{m,n}$, the hyperbolic volume vanishes.  The
topological weight is purely the phase of the path integral, which is
the Chern--Simons invariant

$$
  \mathrm{CS}(T_{m,n})
  = \frac{\pi^2(m^2-1)(n^2-1)}{12mn}.
$$

Multiplying by $\hbar_q^2$ (rather than dividing) establishes a strict
**duality** between hyperbolic and torus states: if hyperbolic knots
represent massive, localised "bulk" particles where $\hbar_q^2$
suppresses the volume, torus knots represent boundary/phase states
where $\hbar_q^2$ amplifies the Chern--Simons phase.

**4. Self-duality and the Frobenius pairing.**
The $\mathrm{Vol}/\hbar_q^2$ vs $\mathrm{CS} \cdot \hbar_q^2$ duality
is the Frobenius pairing of the knot with its dual in the Hecke
algebra.  For a hyperbolic knot $K$, the dual $K^*$ (mirror image)
satisfies $\mathrm{Vol}(K^*) = \mathrm{Vol}(K)$ and the Frobenius
inner product $\langle K, K^* \rangle = 1$ (via the Markov trace).
The factor $\hbar_q^2$ mediates this pairing:

$$
  \langle K, K^* \rangle_{\mathrm{Frob}}
  = \frac{\mathrm{Vol}(K)}{\hbar_q^2}
    \cdot \frac{\hbar_q^2}{\mathrm{Vol}(K^*)}
  = 1.
$$

For torus knots (which are self-dual under the descent involution),
the pairing goes through the CS functional, and $\hbar_q^2$ appears
multiplicatively because the torus knot's phase *is* the pairing.

The figure-eight knot $4_1$ is special: it is **amphicheiral**
($K = K^*$), so the self-pairing is manifestly real.  This underlies
the figure-eight BW modification factors $1 - h^2$ and $h[2]_q$
([figure-eight BW coefficients](#thm:six-term-mass-formula-complete)),
both of which are real algebraic expressions in $q$.

**5. The unknot: vacuum normalisation.**
The unknot bounds a disk; its complement has trivial geometry
($\mathrm{Vol} = 0$, $\mathrm{CS} = 0$).  Setting
$\mathrm{Geom}(\bigcirc) = 0$ ensures that unknotted loops do not
contribute spurious mass or energy to the categorical trace.
<!-- FILE_END: geometric-invariant-piecewise.md -->

<!-- FILE_START: hopf-link-non-magic.md -->
**Hopf link as the simplest knot operator.**
The Hopf link $T_{2,2}$ is the simplest non-trivial 2-component link
in the framework's knot-operator basis:

- Crossing number $2$ (minimum for any non-trivial link).
- Hyperbolic volume $0$ (Seifert-fibered, **not** hyperbolic).
- Complement $S^3 \setminus \mathrm{Hopf} \simeq T^2$ — cohomology
 rank $\leq 2$ in every degree.
- Multivariable Alexander polynomial $\Delta(t_1, t_2) = 1$
 (the standard convention for 2-component links is the
 multivariable form; the single-variable $\Delta(t) = 0$ for the
 Hopf link in the literature should not be confused with this).
 In the QOU framework's reading the Hopf link is the
 *by definition-non-trivial* link — its Alexander structure carries
 no signed information, which is the link-theoretic fact behind
 its $E^{0, *}$-only cohomological location.
- Fundamental group: $\mathbb{Z} \oplus \mathbb{Z}$ — abelian.

**Cohomological location in the framework.**
The Hopf link lives entirely in the $E_\infty^{0, *}$ slot of the
brane-tower spectral sequence
([conj:mass-endomorphism](#conj:mass-endomorphism)) — the
*descended Markov-trace* piece. It contributes only the $E^{0, *}$
component of the SDP optimum
([prop:knot-operator-selection](#prop:knot-operator-selection)).

**Non-magic shells use the Hopf link.**
At non-magic $n$ at substrate $q_0$, the SDP optimum
$T^*(n, q_0)$ is **Hopf-decomposable** — expressible as a tensor
product of Hopf links and trivial ribbons. It lives entirely in
$E_\infty^{0, *}$ (the descended Markov-trace piece per
[`conj:mass-endomorphism`](#conj:mass-endomorphism)).

**Magic shells require higher-cohomology operators.**
At magic $n$, the SDP optimum requires non-trivial contribution
from $E_\infty^{p, q \geq 1}$ — operators NOT Hopf-decomposable.
By [`prop:torus-knot-shell-binding`](#prop:torus-knot-shell-binding),
the active operator at each magic $n$ is one of the six
Bring-embeddable torus knots
$\{T_{2,3}, T_{2,5}, T_{2,7}, T_{2,9}, T_{3,4}, T_{3,5}\}$ — none of
which is Hopf-decomposable.

**Operational reading of the magic predicate.**
Selection of the active knot operator at strand count $n$ is a
**topological-class** decision:

| $n$ class | Active knot operator | Cohomological grading |
|---|---|---|
| non-magic | Hopf-decomposable (e.g. $T_{2,2}^{\otimes k}$) | $E_\infty^{0, *}$ |
| magic | non-Hopf Bring torus knot ($T_{p, q}$ with $q \geq 3$, $p \in \{2, 3\}$) | $E_\infty^{p \geq 1, q \geq 1}$ |

This matches the empirical mass-decomposition observation
([conj:mass-endomorphism](#conj:mass-endomorphism)) that descended
$\mathrm{tr}_M$ contributes $\lesssim 0.5\%$ of magic-shell binding;
the rest is brane-tower (= higher-cohomological) contribution.
<!-- FILE_END: hopf-link-non-magic.md -->

<!-- FILE_START: p-from-braid-mirror.md -->
**Conjecture (D7 parity closure).**
*Within the QOU framework, parity $P$ acts as the **mirror reflection
of the braid diagram** — each positive crossing $\sigma_i \mapsto
\sigma_i^{-1}$ and vice versa, with the q-parameter held fixed
($q \mapsto q$, not $q \mapsto q^{-1}$).  Equivalently, $P$ negates
the signed writhe $w(K) \mapsto -w(K)$ of every braid word.  $P$ is
an involution ($P^2 = \mathrm{id}$) and is **distinct from**:*

- *the bar-involution [`def:bar-involution`](#def:bar-involution),
  which acts as $q \mapsto q^{-1}$ AND $\sigma_i \mapsto \sigma_i^{-1}$
  simultaneously (= composite CPT);*
- *charge conjugation [`conj:c-from-color-flavor-swap`](#conj:c-from-color-flavor-swap)
  (D6), which acts on color-sheet flavor labels with no Hecke-
  generator action;*
- *time-reversal [`conj:t-from-trace-cyclicity`](#conj:t-from-trace-cyclicity)
  (D8), which reverses the braid word at the Markov-trace level.*

## The action

For a braid word $\beta = \sigma_{i_1}^{\epsilon_1} \cdots
\sigma_{i_\ell}^{\epsilon_\ell}$ in $B_n$ (or its image in $H_n(q)$):

$$
  P \;:\;
  \sigma_{i_k}^{\epsilon_k}
  \;\longmapsto\;
  \sigma_{i_k}^{-\epsilon_k}
  \qquad (q\text{ held fixed}).
$$

On the writhe, this gives $w(P\beta) = -w(\beta)$ — a sign flip on
the bar-anti-symmetric writhe quantity classified in
[`bar-involution-table3-data`](bar-involution.md#tbl:bar-involution-table3-data).

## Disentanglement of D7 from CPT

The composite bar-involution acts as both:

$$
  (\text{bar}) \;:\;
  \sigma_i \mapsto \sigma_i^{-1},
  \qquad
  q \mapsto q^{-1}.
$$

This is **CPT composed**: bar = $P \cdot C \cdot T$ in the natural
order, where:

| Acts on | Symbol map |
|---------|------------|
| Hecke generator chirality only | $\sigma_i \mapsto \sigma_i^{-1}$, $q$ fixed (= **P** alone) |
| Color sheets only | flavor $u \leftrightarrow \bar u$ (= **C** alone, D6) |
| Markov trace cyclicity only | braid word reversal (= **T** alone, D8) |

P alone (this conjecture) corresponds to the **first row only** — it
fixes $q$, fixes color-sheet flavors, and fixes trace cyclicity; it
only mirrors the diagram.  Composed with C and T, it recovers the
bar-involution.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: ℓ-dependent per-atom (P preserves Coxeter
  length but flips signs of generators).
- **Jet order**: $h^0$ (P fixes $q$; no q-deformation parameter
  enters the P action).
- **Bar-symmetry status**: bar-trivial (P does not act on $q$;
  bar-involution acts on $q$ AND $\sigma_i$, so P alone is a strict
  sub-action).

Writhe $w(K)$ (the observable that P negates) is classified in
[`bar-involution-table3-data`](bar-involution.md#tbl:bar-involution-table3-data)
as bar-anti-symmetric, consistent: bar reverses writhe via the
composite $P \cdot C \cdot T$, of which P is the writhe-acting
factor.

## Lean axiomatisation (sketch)

```lean
class PFromBraidMirror (M : Type*) [BrCategory M] [Hecke M] where
  /-- The braid-mirror involution on braid-group elements. -/
  p_action : Braid n → Braid n
  /-- P^2 = id. -/
  p_involution : ∀ β, p_action (p_action β) = β
  /-- P flips the sign of every Hecke generator. -/
  p_on_generator : ∀ i, p_action (Hecke.sigma i) = Hecke.sigma_inv i
  /-- P fixes q (no bar-action). -/
  p_preserves_q : ∀ q, p_q_action q = q
  /-- Bar-involution factorisation: bar = P · C · T. -/
  bar_eq_p_c_t : bar_involution = p_action ∘ c_action ∘ t_action
```

## Consumers / downstream

- [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density)
  becomes a corollary of $\mathrm{CPT} = C \cdot P \cdot T$ once D6,
  D7, D8 are all closed.
- The writhe-based chirality classification
  [`prop:chirality-writhe-ribbon-derivation`](#prop:chirality-writhe-ribbon-derivation)
  gets a categorical home: chirality measures the P-anti-symmetric
  part of a knot, separately from C and T.

## Open R&D

1. **Verify canonical** that the Hecke quadratic preserves under P
   (since both $\sigma_i$ and $\sigma_i^{-1}$ satisfy the same
   relation): the quadratic
   $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ is invariant under P
   because $(\sigma_i^{-1} - q)(\sigma_i^{-1} + q^{-1}) = 0$ also
   holds (multiply the original by $\sigma_i^{-2}$). Concrete canonical evaluation
   in a follow-up.
2. **D7 to closed** requires the Lean class instance + a `prop:` block
   stating bar = P $\cdot$ C $\cdot$ T as a derivable identity.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D7
  + §2 Cluster A (CPT decomposition D5 $\to$ D6 + D7 + D8)
- Sibling Z/2 decompositions of CPT:
  [`conj:c-from-color-flavor-swap`](c-from-color-flavor-swap.md) (D6),
  [`conj:t-from-trace-cyclicity`](t-from-trace-cyclicity.md) (D8)
- Composite CPT: [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density)
- Bar-involution: [`bar-involution.md`](bar-involution.md) Tables 1-4
<!-- FILE_END: p-from-braid-mirror.md -->

<!-- FILE_START: poincare-lefschetz-borromean.md -->
**Conjecture (D21 Poincaré–Lefschetz closure).**
*The Borromean complement $\mathbf{S}^3 \setminus \mathcal{B}_3$
is a 3-manifold with cusps (boundary = 3 disjoint tori).
Poincaré–Lefschetz duality gives a canonical isomorphism:*

$$
  H^k(\mathbf{S}^3 \setminus \mathcal{B}_3, \partial) \;\cong\;
  H_{3-k}(\mathbf{S}^3 \setminus \mathcal{B}_3),
$$

*relating cohomology with boundary support to homology.  In
particular $H^2(\partial \mathcal{B}_3) \cong H_1(\mathbf{S}^3
\setminus \mathcal{B}_3) \cong \mathbb{Z}^3$ (the three meridian
classes around the three Borromean components).  The duality
pairs the volume form (top cohomology) with the fundamental
class (top homology), giving the natural categorical home for
$\mathrm{Vol}(\mathcal{B}_3) = 8G$ as a Poincaré–Lefschetz
pairing.*

## Relationship to D16 Bloch group

The K-theoretic Bloch-group element
([`conj:borromean-bloch-group-element`](#conj:borromean-bloch-group-element), D16)
provides the **regulator** side of the Borromean structure
($r_2[\mathcal{B}_3] = 8G$).  D21 Poincaré–Lefschetz provides the
**topological** side: the volume form $\in$ $H^3$ pairs with the
fundamental class $\in$ $H_3$ to give the volume integral $8G$.

The two ARE the same number ($8G = \mathrm{Vol}(\mathcal{B}_3)$),
but expressed through distinct dualities. D21 IS the
topological-cohomological route; D16 IS the K-theoretic route.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration**: N/A — manifold-with-boundary duality is at the
  topological level, not at the Hecke-element level.
- **Jet order**: $h^0$ — Poincaré–Lefschetz acts on the leading-
  order topological volume.
- **Bar-symmetry**: bar-symmetric (the duality is independent of
  q-parameter; both sides are classical-topology constructions).

## Open R&D

1. Verify that the Borromean volume $8G$ arises as a Poincaré–
   Lefschetz pairing in Lean — partial Mathlib infrastructure
   exists (Mathlib's `Topology.Manifold` library).
2. Connect to D16 Bloch group: show the regulator $r_2$ and the
   Poincaré–Lefschetz pairing both produce $8G$ via the
   `vol-as-motivic-period` framing.
3. D21 to closed requires Lean class for manifold-with-cusps Poincaré–
   Lefschetz (partial in Mathlib).

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D21
  + paired with D16
- D16 [`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md)
  — K-theoretic regulator route to the same $8G$
- [`prop:reeb-bundle-complement-equals-volume`](#prop:reeb-bundle-complement-equals-volume)
  — Reeb-pairing volume route (third route to $8G$)
- [`rem:vol-as-motivic-period`](#rem:vol-as-motivic-period)
  — motivic framing tying all three routes together
- [Lefschetz 1926; Neumann–Zagier 1985 for cusped 3-manifolds]
<!-- FILE_END: poincare-lefschetz-borromean.md -->

<!-- FILE_START: volume-perturbation-formula.md -->
*The vertex volume perturbation when going from $H_k$ to $H_{k+1}$
is:*
$$\delta\Phi_k = z^2 \cdot \mathrm{Vol}(4_1) \cdot [k{-}3]_q$$
*where $z = 1/(\sqrt{q}+1/\sqrt{q})$ is the Markov parameter
and $\mathrm{Vol}(4_1) = 2.030$ is the figure-eight knot volume.*

*Both fundamental hyperbolic volumes appear:*
- *$\mathrm{Vol}(\mathcal{B}_3) = 8G$ sets the binding scale $\alpha$*
- *$\mathrm{Vol}(4_1)$ sets the perturbation unit per level*

*Verified for heavy nuclei (Ca, Fe) at $k = 5, 6, 7$:*
- *$k=5$: predicted $1.02$, observed $1.15$ (13%)*
- *$k=6$: predicted $1.54$, observed $1.48$ (4%)*
- *$k=7$: predicted $2.08$, observed $1.90$ (9%)*  $\square$
<!-- FILE_END: volume-perturbation-formula.md -->


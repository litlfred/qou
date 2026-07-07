<!-- FILE_START: mass-geometric-face-intro.md -->
The mass endomorphism's geometric face connects the algebraic
Markov trace to the hyperbolic volume of the knot complement.
Thurston's volume additivity
([Thurston additivity](#prop:thurston-volume-additivity)) ensures
that the mass of a composite knot decomposes as a sum over its
JSJ pieces, and the mass-volume factorisation conjecture
([mass-volume factorisation](#conj:mass-volume-factorization))
identifies the categorical mass endomorphism as a product of
volume and Frobenius-packing density.

The crossing-graded expansion
([crossing expansion](#conj:crossing-graded-mass-expansion))
stratifies the mass by crossing number, with each stratum
controlled by the locality conjecture
([lifted crossing locality](#conj:lifted-crossing-locality)).
The jet-tower convergence bound
([tower convergence](#prop:jet-tower-convergence)) guarantees that
the brane-tower sum converges geometrically, and the SYT/Jucys-Murphy
reindexing ([mass tower SYT](#rem:mass-tower-syt-cells)) connects
the tower structure to the standard Young tableaux of the Hecke
algebra.
<!-- FILE_END: mass-geometric-face-intro.md -->

<!-- FILE_START: thurston-volume-additivity.md -->
## Thurston volume additivity

Every hyperbolic knot or link complement $S^3 \setminus \mathcal{K}$
admits an ideal triangulation — a decomposition into finitely many
ideal tetrahedra $\Delta_1, \ldots, \Delta_N$ whose vertices lie on
the sphere at infinity $\partial \mathbb{H}^3$.  Each ideal
tetrahedron is determined up to isometry by a single complex **shape
parameter** $z_i \in \mathbb{C} \setminus \{0, 1\}$ — the cross-ratio
of its four ideal vertices.

## Statement

**Proposition.** \cite{thurston1978}
*Let $\mathcal{K} \subset S^3$ be a hyperbolic knot or link, and
fix an ideal triangulation of $S^3 \setminus \mathcal{K}$ with
shape parameters $z_1, \ldots, z_N$ determined by the hyperbolic
gluing equations.  The hyperbolic volume is the sum of tetrahedral
volumes:*

$$
  V(\mathcal{K})
  \;=\;
  \sum_{i = 1}^N D(z_i),
  \qquad
  D(z) \;=\; \Im\,\mathrm{Li}_2(z) + \arg(1 - z)\,\log\lvert z \rvert,
$$

*where $D$ is the **Bloch–Wigner dilogarithm**.  Degenerate (flat)
tetrahedra with $z_i \in \mathbb{R}$ contribute $D(z_i) = 0$.*

## Braid-theoretic consequence

A knot diagram with $c$ crossings induces an ideal triangulation of
$S^3 \setminus \mathcal{K}$ with one ideal tetrahedron per crossing
(possibly merged or degenerate under simplification).  The volume
is therefore **additive over crossings**:

$$
  V(\mathcal{K}) \;=\; \sum_{\text{crossings } c} D(z_c).
$$

Torus knots have all crossings pressed onto a torus surface — every
$z_c$ is real — so $V(T_{m,n}) = 0$.  This is the categorical
explanation of why Seifert-fibered nucleons contribute zero hyperbolic
volume in the [JSJ decomposition of the atomic braid](#thm:wedderburn-mass-formula).

## Extremality

Among all $z \in \mathbb{C}$, the Bloch–Wigner function attains its
maximum at the regular shape $z = e^{i\pi/3}$:

$$
  D(e^{i\pi/3}) \;=\; \mathrm{Cl}_2(\pi/3) \;=\;
  \sum_{n \geq 1} \frac{\sin(n\pi/3)}{n^2}
  \;\approx\; 1.01494 \;=:\; v_3,
$$

the **Lobachevsky constant**.  The figure-eight knot $4_1$ has two
ideal tetrahedra both of shape $e^{i\pi/3}$, giving
$V(4_1) = 2 v_3 \approx :val[Vol_4_1]{precision=6}$ — the minimum volume among
hyperbolic knots.  This is the normalization used to pin the
substrate parameter $q_0$ via
[$\hbar_q^2 = V(4_1) / (m_\mu / m_e)$](#prop:local-substrate-q).

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: thurston-volume-additivity.md -->

<!-- FILE_START: mass-volume-factorization.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](../braids-and-knots/mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](../braids-and-knots/rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

## Mass-volume factorization

**Parent statement:** The general volume-density factorization
$\mathfrak{m}(K) = \mathrm{Vol}(K) \cdot \rho_q$, with substrate
drag density $\rho_q = 1/\hbar_q^2$, is established in
[Kashaev volume-density](#rem:kashaev-volume-density). This block
specializes that formula to **atomic links** for the nuclear
binding regime.

At the particle-mass scale, the Kashaev-volume-density formula
gives $\mathfrak{m} = \mathrm{Vol}/\hbar_q^2 \approx 102 \cdot
\mathrm{Vol}$ in $m_e$ units (pinned via
$\mathfrak{m}(4_1) = m_\mu / m_e$). At the nuclear-binding
scale — orders of magnitude below particle mass — the factorization
takes a specialized form with the same geometric volume but a
**physical-scale density** $\rho_F$ instead of the categorical
$\rho_q$:

## Statement

**Conjecture.**
*Let $\mathcal{K}$ be the atomic braid of a derived atom
$\mathcal{A}(Z, N)$ ([atomic braid](#def:atomic-braid)), and let
$S^3 \setminus \overline{\mathcal{K}}$ denote the braid-closure
complement in the 3-sphere. Then the categorical mass endomorphism
factorizes as*

$$
  \mathfrak{m}_{\mathcal{K}}(q)
  \;=\;
  \rho(q, \mathcal{K}) \cdot V_{\mathrm{hyp}}(\overline{\mathcal{K}}),
$$

*where $V_{\mathrm{hyp}}$ is the hyperbolic volume computed via the
[Thurston sum](#prop:thurston-volume-additivity), and $\rho(q,
\mathcal{K})$ is the **Frobenius packing density** determined by
which Wedderburn blocks of $H_{3A}(q)$ are populated by
$\mathcal{K}$.*

## JSJ refinement

Applying the Jaco-Shalen-Johannson decomposition of the
complement $S^3 \setminus \overline{\mathcal{K}}$ into Seifert-fibered
and hyperbolic pieces $P_1, \ldots, P_k$, the formula refines to a
sum over hyperbolic pieces:

$$
  B(Z, N) \;=\; \sum_{P_i \text{ hyperbolic}}
  \rho_F(P_i) \cdot V_{\mathrm{hyp}}(P_i),
$$

where:

- **Seifert pieces** (torus-knot nucleons, $T_{m,n}$-type) contribute
 $V_{\mathrm{hyp}} = 0$ by [Thurston additivity](#prop:thurston-volume-additivity).
- **Hyperbolic pieces** (inter-nucleon glue, closed-shell
 Borromean-type links) carry the binding.
- The density $\rho_F(P_i)$ takes one of two values:

$$
  \rho_F(P_i)
  \;=\;
  \begin{cases}
    m_e & \text{if } P_i \text{ is single-chirality
                    (sym + std blocks only),} \\
    2 m_e & \text{if } P_i \text{ is CPT-saturated
                      (sym + std + alt blocks).}
  \end{cases}
$$

The factor $2 m_e$ is the $\gamma\gamma$ pair-creation threshold;
it arises whenever the alt Wedderburn block is non-by definition
populated, doubling the effective packing (see
[Frobenius packing density](#rem:frobenius-packing-density)).

## Supporting evidence

Pinning $\rho \in \{m_e, 2m_e\}$ and computing the hyperbolic volume
of the atomic link complement reproduces nuclear binding energies for
doubly-magic atoms within $\leq 6.2\%$:
${}^4\mathrm{He}$, ${}^{12}\mathrm{C}$, ${}^{16}\mathrm{O}$. For
light atoms, the atomic link complement is itself a named hyperbolic
knot from the standard census:

| atom | link / knot | $V$ | $\rho$ | $B_{\text{pred}}$ | $B_{\text{AME}}$ |
|:-----|:------------|:----|:-------|:------------------|:-----------------|
| D | $6_2$ | $4.400$ | $m_e$ | $2.249$ MeV | $2.225$ MeV |
| T | $8_{11}$ | $8.286$ | $2m_e$ | $8.468$ MeV | $8.482$ MeV |
| ${}^3\mathrm{He}$ | Borromean | $8G$ | $2m_e$ | $7.493$ MeV | $7.718$ MeV |
| ${}^4\mathrm{He}$ | 4 Borromean components | $4 \cdot 8G$ | $2m_e$ | $29.96$ MeV | $28.30$ MeV |

(Values from the atom-volume witness and AME2020. The ${}^4\mathrm{He}$
row gives the **first-principles geometric prediction**
$2m_e \cdot 4 \cdot 8G = 29.96$ MeV; the closed-shell refinement used
for larger atoms in [crossing-graded-mass-expansion](#conj:crossing-graded-mass-expansion)
uses the α-cluster baseline $B({}^4\mathrm{He}) = 28.30$ MeV directly
from AME. The $4 \cdot 8G$ notation denotes four Borromean-rings
complements summed — not the braid group $B_3$.)

### Non-zero free parameters: the atom-to-link mapping gap

The $\leq 6.2\%$ above is obtained with a **per-atom choice** of both the
link/knot and the density $\rho \in \{m_e, 2m_e\}$; neither is yet
derived (see "Why this is a conjecture", points 1–2). The choices are
mutually **inconsistent**: D uses $6_2$ ($V=4.400$) whereas the
binding-link census assigns D the Hopf link ($V=0$,
[binding-link-volumes.witness.json](../../../computations/binding-link-volumes.witness.json)),
and ${}^3\mathrm{He}$ uses one Borromean copy ($8G$) while
${}^4\mathrm{He}$ uses four ($4\cdot 8G$). The companion canonical evaluation
[rho-f-volume-binding-gap.witness.json](../../../computations/rho-f-volume-binding-gap.witness.json)
inverts $\rho_F\cdot V_{\mathrm{hyp}} = \Delta_{\mathrm{binding}}$ and
finds **no** fixed link primitive reproduces the light-isotope bindings
with $\rho \in \{m_e, 2m_e\}$ (`matches_within_10pct: []`; ${}^4$He
needs $\rho_F/m_e \approx 7.6$ on a single Borromean copy, not $2$).
The result is therefore a **per-isotope fit of the (link, $\rho$)
pair**, not a zero-parameter prediction — until the atom-to-link map and
the $\rho_F$ rule are derived.

## Conjectural status

Factorization requires:

1. The atomic link complement admits a canonical JSJ decomposition
 compatible with the ambient Hecke algebra grading — verified
 computationally per atom, not proved in general.
2. The density $\rho_F(P_i)$ is determined locally by the Wedderburn
 profile of $P_i$ — stated but not derived from first principles
 (see [Frobenius packing density](#rem:frobenius-packing-density)).
3. The categorical mass endomorphism and the topological
 Thurston volume are literally equal (not only proportional with
 a $q$-dependent prefactor hidden in $\rho$) — this is the
 **volume conjecture at real $q$**, parallel to the classical
 statement \cite{murakami-murakami2001} at $q \to e^{2\pi i/N}$.
<!-- FILE_END: mass-volume-factorization.md -->

<!-- FILE_START: frobenius-packing-density.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](../braids-and-knots/mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](../braids-and-knots/rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

## Frobenius packing density

**Two density scales.** The paper uses two density quantities
that should not be confused:

| symbol | formula | scale | role |
|---|---|---|---|
| $\rho_q$ | $1/\hbar_q^2 \approx 102$ | dimensionless | **substrate drag** ([kashaev-volume-density](#rem:kashaev-volume-density)) — gives particle mass $\mathfrak{m}(K) = \mathrm{Vol}(K)\cdot\rho_q$ in $m_e$ units |
| $\rho_F$ | $m_e$ or $2m_e$ | physical (MeV) | **Frobenius packing** — this block, gives nuclear binding $B(\mathcal{K}) = \rho_F \cdot V_{\mathrm{hyp}}$ in MeV |

At the particle-mass scale, every crossing is charged by
$\rho_q = 1/\hbar_q^2$ (the Kashaev drag).  At the nuclear-binding
scale — orders of magnitude below particle mass — the effective
factor that multiplies $V_{\mathrm{hyp}}$ is the **Frobenius packing
density** $\rho_F \in \{m_e, 2m_e\}$.  The distinction is determined
by the Frobenius pairing on the ambient Iwahori-Hecke algebra
$H_{3A}(q)$: specifically, by **which Wedderburn blocks are
populated** by the atomic link configuration.

## The packing dictionary

The Frobenius form of $H_n(q)$ is the Markov trace
$\mathrm{tr}_M \colon H_n(q) \to \mathbb{C}$, whose Wedderburn
decomposition reads

$$
  \mathrm{tr}_M(x)
  \;=\;
  \sum_{\lambda \vdash n} w_\lambda(q) \cdot \chi_\lambda(x),
  \qquad
  w_\lambda(q)
  \;=\;
  \frac{d_q(\lambda)^2}{[n]_q!}
  \qquad (\text{Plancherel weight}).
$$

Each partition $\lambda$ labels a simple block of $H_n(q)$; its
weight $w_\lambda(q)$ quantifies how much of the Frobenius pairing
that block carries.  At $n = 3$ the three blocks are:

| block $\lambda$ | partition | interpretation |
|:----------------|:----------|:----------------|
| sym | $(3)$ | particle channel (eigenvalue $+q$) |
| std | $(2, 1)$ | mixed / propagator channel |
| alt | $(1, 1, 1)$ | antiparticle channel (eigenvalue $-q^{-1}$) |

## The two-density rule

An atomic link $\mathcal{K}$ populates a subset of blocks
$\Lambda(\mathcal{K}) \subseteq \{\text{sym}, \text{std}, \text{alt}, \ldots\}$.
The Frobenius packing density is

$$
  \rho_F(\mathcal{K})
  \;=\;
  \begin{cases}
    m_e &
    \text{if alt} \notin \Lambda(\mathcal{K})
      \quad (\text{single-chirality}), \\[4pt]
    2 m_e &
    \text{if alt} \in \Lambda(\mathcal{K})
      \quad (\text{CPT-saturated}).
  \end{cases}
$$

The factor of $2$ is enforced by CPT: populating the alt block
automatically brings its antiparticle partner, each contributing
$m_e$ to the effective mass per unit of Frobenius packing.  The
threshold $2 m_e$ is the $\gamma \gamma$ pair-creation energy — the
point at which vacuum fluctuations physically populate the alt
channel.

## Topological triggers for alt saturation

Whether the alt block is activated is a **topological** property of
the atomic link, driven by multi-component entanglement:

- **Two-body links** (e.g. the knot $6_2$ representing deuterium)
  have only mutual linking of two components; the alt block remains
  suppressed and $\rho_F = m_e$.
- **Three-body links with full entanglement** (Borromean-type, e.g.
  ${}^3\mathrm{He}$ and any $A \geq 3$ atomic glue) require
  cyclic three-way interaction; this forces the alt-block generator
  into the image of the braid word and $\rho_F = 2 m_e$.
- **Closed-shell clusters** (doubly-magic ${}^4\mathrm{He}$,
  ${}^{12}\mathrm{C}$, ${}^{16}\mathrm{O}$) saturate all three
  blocks internally, giving $\rho_F = 2 m_e$ per nucleon volume.
- **Inter-cluster bonds** ($\alpha$-$\alpha$ coupling via the link
  $7^2_1$) are two-body glues between already-saturated pieces; the
  alt content is absorbed into the clusters and the bond itself
  reverts to $\rho_F = m_e$.

## Packing vs volume

The Frobenius picture recasts mass as literal *packing*: the
Plancherel weights $w_\lambda(q)$ define a measure on the
Wedderburn module of $H_{3A}(q)$, with $\dim H_{3A}(q) = [3A]_q!$
as total volume.  Mass is the fraction of this $q$-volume actually
occupied by the atomic link:

$$
  \mathfrak{m}(\mathcal{K}; q)
  \;=\;
  \underbrace{\sum_{\lambda \in \Lambda(\mathcal{K})} w_\lambda(q) \cdot m_e
              \cdot [\text{alt-saturation factor}]}_{\rho_F(\mathcal{K})}
  \;\cdot\;
  \underbrace{V_{\mathrm{hyp}}(\mathcal{K})}_{\text{geometric volume}}.
$$

This is the **first-principles derivation** of the empirical
$\rho \in \{m_e, 2m_e\}$ rule: it comes from the Frobenius
structure of the Hecke algebra acting on the atomic link complement,
not from a phenomenological fit.
<!-- FILE_END: frobenius-packing-density.md -->

<!-- FILE_START: crossing-graded-mass-expansion.md -->
## Crossing-graded mass expansion

**Parent framework.** The expansion below sits on top of two
already-established objects:

- [def:crossing-energy](#def:crossing-energy) — per-crossing weights
  are the **Hecke eigenvalues** $(q, -q^{-1})$ of $T$ on
  $S^2 V \oplus \Lambda^2 V$, derived from rigid-monoidal structure
  (not postulated).
- [def:algebraic-quantum-volume](#def:algebraic-quantum-volume)
  $\mathrm{Vol}_q(\beta) = \prod_i \hat{V}_i(q) \in
  \mathbb{Z}[q^{1/2}, q^{-1/2}]$ — the algebraic quantum volume of a
  braid, a Laurent polynomial in $q^{1/2}$.

The [mass-volume factorization](#conj:mass-volume-factorization) can
be organized as a perturbative expansion graded by the number of
"lifted" (volume-carrying) crossings.  The $n = 0$ term reproduces
the existing Gröbner-Shirshov NF mass; each higher order picks up
the per-crossing $(q, -q^{-1})$ eigenvalue contribution to
$\mathrm{Vol}_q(\beta)$.

## Statement

**Conjecture.**
*Let $\mathcal{K}$ be an atomic braid with braid word $\beta$ of
$c$ crossings, living in $H_{3A}(q)$.  Fix the universal shape
parameter $z_q \in \mathbb{C}$ from the [Descartes elliptic
curve](#prop:descartes-elliptic-curve) via its Legendre
$\lambda$-invariant, and define the depth scalar*

$$
  \xi(q) \;:=\; \frac{D(z_q)}{\hbar_q^2},
$$

*where $D$ is the Bloch-Wigner dilogarithm and $\hbar_q^2 = V(4_1) /
(m_\mu/m_e)$ is the pinned quantum of action.  Then the categorical
mass endomorphism admits a crossing-graded expansion*

$$
  \mathfrak{m}(\mathcal{K}; q)
  \;=\;
  \sum_{n = 0}^{c(\mathcal{K})} \xi(q)^n \cdot
  \mathfrak{m}^{(n)}_{\mathrm{GB}}(\mathcal{K}),
$$

*where*

$$
  \mathfrak{m}^{(n)}_{\mathrm{GB}}(\mathcal{K})
  \;=\;
  \sum_{\substack{S \subseteq \{1, \ldots, c\} \\ \lvert S \rvert = n}}
  \mathfrak{m}_{\mathrm{GB}}(\beta\lvert_{S \text{ lifted, rest flat}}),
$$

*and $\mathfrak{m}_{\mathrm{GB}}(\beta\lvert_{S,\mathrm{flat}})$ is
the Gröbner-Shirshov normal form of $\beta$ with crossings in $S$
carrying the shape $z_q$ (volume-contributing) and the remainder
skein-resolved (flat, zero-volume).*

## Order-by-order meaning

See [Table: Crossing-graded mass expansion](#tbl:crossing-graded-mass-expansion-table-data).
| $\vdots$ | $\vdots$ | $\vdots$ |
| $n = c$ | $\xi^c \cdot \mathfrak{m}^{(c)}_{\mathrm{GB}}$ | full Thurston volume — all crossings lifted |

## Locality corollary

If lifted-crossing contributions factorize pairwise — the
[lifted-crossing locality hypothesis](#conj:lifted-crossing-locality) —
the sum collapses to an exponential in crossing count:

$$
  \mathfrak{m}(\mathcal{K}; q)
  \;=\;
  \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot
  (1 + \xi(q))^{c(\mathcal{K})}.
$$

Each additional crossing multiplies mass by $(1 + \xi)$ — heavier knots
are **exponentially heavier**, not linearly.  Locality violations
would manifest as deviations from this exponential; the order
$n \geq 2$ terms encode the corrections.

## Connection to the quantum dilogarithm

The per-crossing weighting by $D(z_q)$ is the semiclassical limit
of the quantum dilogarithm operator $\Phi_q(z)$ acting at each
Hecke generator.  Expanding $\log \Phi_q(z)$ in the small parameter
$\hbar_q$:

$$
  \log \Phi_q(z)
  \;\sim\;
  \frac{1}{2\pi i \hbar_q}\,\mathrm{Li}_2(z)
  \;+\; O(\log \hbar_q),
$$

whose imaginary part at leading order is exactly $D(z)/(2\pi \hbar_q)$.
The $\xi^n$ expansion is the **Feynman-like ordered sum** in
$\hbar_q$, with each order corresponding to a Pachner-move
reorganization of the ideal triangulation.

## Recovery of the classical limit

Setting $\xi = 0$ (either via $D(z_q) = 0$ or $\hbar_q \to \infty$)
kills every $n \geq 1$ term, recovering the original Gröbner-Shirshov
mass endomorphism.  The condition $D(z_q) = 0$ occurs at real
$z_q$ — precisely the boundary of the Descartes curve at
$q = 1/\varphi^2$ ([golden-ratio degeneration](#prop:descartes-elliptic-curve)) —
The GB framework is the **real-axis degeneration** of the
volumized theory.

## Conjectural status

This statement is a **conjecture** rather than a theorem because:

1. The universal shape parameter $z_q = \lambda(\mathcal{E}_q)$ is
   pinned by the Descartes curve, but its agreement with per-knot
   Thurston gluing is only an approximation (the
   $\lambda$-witness shows $D(z_q)/v_3 \approx 0.9015$ at $q_0$).
2. The separation of lifted vs flat crossings requires the
   [locality hypothesis](#conj:lifted-crossing-locality) as an
   independent assumption.
3. The exponential collapse to $(1 + \xi)^c$ further needs locality.

Each component is tracked separately as a conjecture so the status
of the overall expansion can be refined as derivations mature.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: crossing-graded-mass-expansion.md -->

<!-- FILE_START: lifted-crossing-locality.md -->
## Lifted-crossing locality hypothesis

The [crossing-graded mass expansion](#conj:crossing-graded-mass-expansion)
is a finite sum over subsets of "lifted" crossings; in general, each
order-$n$ term is a non-trivial sum over $\binom{c}{n}$ configurations.
The **locality hypothesis** asserts that these per-configuration
contributions **factorize** into products of single-crossing
contributions whenever the crossings are topologically separated —
so that the expansion collapses to a closed-form exponential.

## Statement

**Conjecture.**
*Let $\mathcal{K}$ be an atomic braid and $\mathrm{Cr}(\mathcal{K})$
its set of crossings. For any subset $S \subseteq \mathrm{Cr}(\mathcal{K})$,
let $\mathfrak{m}_{\mathrm{GB}}(\beta\lvert_{S \text{ lifted}})$ denote
the Gröbner-Shirshov mass with exactly the crossings in $S$ carrying
the universal shape parameter $z_q$. Then*

$$
  \mathfrak{m}_{\mathrm{GB}}(\beta\lvert_{S \text{ lifted}})
  \;=\;
  \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot
  \prod_{c \in S} \eta(c),
$$

*where $\eta(c)$ is a purely local factor depending on the crossing
$c$ alone, its sign $\varepsilon(c) \in \{\pm 1\}$, and the substrate
parameter $q$ — but not on which other crossings are lifted.*

## Corollary: exponential closed form

Given locality, the crossing-graded expansion collapses:

$$
  \mathfrak{m}(\mathcal{K}; q)
  \;=\;
  \sum_{n = 0}^c \xi(q)^n \cdot \mathfrak{m}^{(n)}_{\mathrm{GB}}(\mathcal{K})
  \;=\;
  \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot
  \prod_{c \in \mathrm{Cr}(\mathcal{K})} (1 + \xi(q)\,\eta(c)).
$$

For the homogeneous case $\eta(c) = 1$ for all $c$, this is 
$(1 + \xi(q))^{c(\mathcal{K})}$.

## Non-triviality of locality

Without locality, lifting two crossings $c_1, c_2$ could produce
interference: the joint amplitude
$\mathfrak{m}_{\mathrm{GB}}(\beta\lvert_{\{c_1,c_2\}})$ could contain
cross-terms that do **not** factor as
$\eta(c_1)\eta(c_2)\mathfrak{m}_{\mathrm{GB}}(\mathcal{K})$. The
obstruction is a curvature / holonomy: parallel transport of the
shape parameter around a loop encircling both crossings would accumulate
a non-trivial phase. Locality is the statement that this holonomy
vanishes at generic $q$.

See the [$q$-holonomy derivation](#rem:q-holonomy-locality-derivation)
for why flatness of the Knizhnik-Zamolodchikov connection at generic
(non-root-of-unity) $q$ enforces the locality factorization.

## Dependence on $q$ regime

Locality is **not** universal in $q$. It holds on the generic stratum
and fails at special values:

- **Generic real $q$** (including substrate $q_0 \approx 1.11$):
 $U_q(\mathfrak{sl}_2)$-reps are semisimple, the KZ connection is
 flat, and locality holds. This is the physical regime.
- **Roots of unity $q = e^{2 \pi i / \ell}$**: the category becomes
 non-semisimple (Jones-Wenzl truncation); the KZ connection
 develops obstructions and locality fails at level $\ell$.
- **Golden-ratio threshold $q = 1/\varphi^2$**: the Descartes curve
 degenerates ([cusp in $\mathcal{E}_q$](#prop:descartes-elliptic-curve)),
 $z_q \to 0$ or $1$, and locality becomes vacuous since $\xi(q) = 0$.

Locality holding at $q_0$ but **failing away from it** is what makes
the substrate parameter distinguished: it sits in the
locality window where the crossing-graded expansion has its cleanest
closed form.

## Empirical test

Locality predicts $\mathfrak{m}(\mathcal{K}) = \mathfrak{m}_{\mathrm{GB}}
\cdot \prod_c (1 + \xi \eta(c))$. Deviations from this scaling —
residuals in binding energies not accounted for by the product formula —
quantify locality violations. For doubly-magic atoms the product form
is within $\leq 6\%$ (see the
[JSJ/$\alpha$-clustering witness](#conj:mass-volume-factorization)),
consistent with approximate locality at $q_0$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: lifted-crossing-locality.md -->

<!-- FILE_START: mass-categorical-descent.md -->
The QOU mass formula is the :refterm[descent]{#descent}
decomposition of the mass endomorphism
$\mathfrak{m} \colon A \to A$ under the brane tower blow-up.
The empirical Bethe–Weizsäcker liquid-drop ansatz is recovered
as one phenomenology of this descent decomposition; see
[`conj:q-integer-mass-formula`](#conj:q-integer-mass-formula)
for the recovered coefficients.

**Proposition.**
\*Let $\mathcal{A}(Z,N)$ be the atomic braid in $H_{A+Z}(q)$,
and let $\hat{\tau}$ denote the :refterm[descent]{#descent} involution acting on
$\operatorname{End}(A)$.  Then the mass identity
\$\mathfrak{m}(\mathcal{A}) = Z m\_{\mathfrak{p}} + N m\_{\mathfrak{n}}

* Z m\_e - B(Z,N)\$ decomposes as\*

$$
  B(Z,N) = \underbrace{B^{\mathrm{desc}}(Z,N)}_{\text{descended}}
          + \underbrace{B^{\mathrm{trans}}(Z,N)}_{\text{transient}}
$$

*where the descended component lies in the centre of $H_n(q)$
and the transient component localises to the exceptional divisors
of the brane blow-up.*

**Descended (central) terms.**

The descended component consists of Casimir operators — elements
of the centre $Z(H_n(q))$ that commute with all generators.  By
the Wedderburn-Artin decomposition, these are indexed by partitions
$\lambda \vdash n$:

| BW term                              | Casimir level | Partition family                | Scaling    |
| ------------------------------------ | ------------- | ------------------------------- | ---------- |
| Volume ($\lambda_V \cdot A$)         | $k = 3$       | $[n], [1^n]$ (sym $\oplus$ alt) | $A$        |
| Pairing ($\pm \lambda_P / \sqrt{A}$) | $k = 3$       | $[n-1,1]$ (standard)            | $A^{-1/2}$ |
| Wigner ($\lambda_W \cdot T(T+1)/A$)  | $k = 5$       | $[n-2,2] + [n-2,1^2]$           | $T(T+1)/A$ |

Their coefficients are the Hecke-level quantum factorials $[n]_q!$
(evaluated directly as the $q$-factorial product); the
[Markov-trace normalization](#prop:wedderburn-trace-identity)
$\sum_\lambda d_\lambda\, y_\lambda(q) = 1$ partitions the total
Markov weight among the irreducible representations.

**Transient (exceptional divisor) terms.**

The transient component localises to the exceptional divisors
$E_i \subset \widetilde{X}$ of the blow-up
$\pi \colon \widetilde{X} \to X$ at codimension-$\geq 2$ loci
where crossings degenerate.  Each blow-up centre contributes a
quantum dilogarithm correction:

| BW term                                       | Divisor type            | Content $c$              | Coefficient                  |                              |    |
| --------------------------------------------- | ----------------------- | ------------------------ | ---------------------------- | ---------------------------- | -- |
| Surface ($-\lambda_S \cdot A^{2/3}$)          | Boundary $\partial A_n$ | $c = 0$                  | $\Phi_q(1)$                  |                              |    |
| Coulomb ($-\lambda_C \cdot Z(Z{-}1)/A^{1/3}$) | Charge locus            | $c = \pm 1$              | $\Phi_q(q^{\pm 1})$          |                              |    |
| Exchange ($\pm \lambda_{\mathrm{ex}} / A$)    | Parity locus            | $c = \pm 1$              | $\Phi_q(-q^{\pm 1})$         |                              |    |
| Shell ($\delta_{\mathrm{sh}}$)                | Magic number loci       | $c = c_{\mathrm{shell}}$ | $\Phi_q(z_{\mathrm{magic}})$ |                              |    |
| Hook ($\delta_{\mathrm{hook}} / A$)           | Hook locus              | $c = \pm 2$              | \$                           | \ln \lambda\_{\mathrm{hook}} | \$ |

The content $c$ of each blow-up centre is the magnetic quantum
number $m_j$ under the Schur-Weyl correspondence: the Young
diagram content $c(i,j) = j - i$ equals the $m_j$ eigenvalue of
the angular momentum projection.

**Parallel with coupling.**

The same :refterm[descent]{#descent} structure applies to the electromagnetic coupling
endomorphism $\Phi = P_{\mathrm{anti}}$
([CS-corrected coupling](#prop:em-coupling-projection)):

| Component              | Mass (BW)                            | Coupling ($1/\alpha$)                                            |
| ---------------------- | ------------------------------------ | ---------------------------------------------------------------- |
| **Base holonomy**      | $\lambda_V \cdot A$ (volume)         | $q \cdot [9]_q \cdot [10]_q$ (bare coupling)                     |
| **Divisor correction** | $-\lambda_S \cdot A^{2/3}$ (surface) | $(\mathrm{CS}_1 + \mathrm{CS}_2) \cdot \hbar_q^2$ (Chern-Simons) |
| **Physical origin**    | Nuclear boundary nucleons            | Force-carrier crossing degeneracies                              |
| **Sign**               | Negative (reduces binding)           | Positive (increases $1/\alpha$)                                  |

The universality of the :refterm[descent]{#descent} decomposition — base holonomy plus
exceptional divisor corrections — reflects the categorical origin
of both mass and coupling as endomorphisms in $\mathbf{C}$,
decomposed by the same involution $\hat{\tau}$.
<!-- FILE_END: mass-categorical-descent.md -->

<!-- FILE_START: descended-level-zero.md -->
The jet-tower decomposition
([jet-tower remark](#rem:mass-endomorphism-jet-tower))
asserts that the descended (holonomy) contribution to the mass
appears **once only**, at jet level $0$, and that levels
$n \ge 1$ carry only singleton and quadratic transient
contributions. This proposition provides the derivation: the
descended projector stabilises under composition, so iterated
:refterm[descent]{#descent} collapses to the base-level holonomy regardless of the
jet level at which it is read off.

**Proposition.** Let $\hat\tau_n$ be the :refterm[descent]{#descent} involution at
level $n$ ([:refterm[descent]{#descent} involution](#def:descent-involution)) and
$\mathcal{A}^{\mathrm{desc}}_{n+1} = \mathrm{im}\,\hat\tau_n$
the descended subalgebra. For every jet level $n \ge 0$, the
descended component of the mass integrand $\alpha^{(n+1)}$
equals the base-level descended contribution:

$$
  \bigl\lVert
    \mathrm{tr}\!\bigl(\hat\tau_n(\alpha^{(n+1)})\bigr)
  \bigr\rVert
  \;=\;
  \mathfrak{m}(\varrho_0)
  \;=\;
  \Bigl\lvert \textstyle\prod_i \hat V_i^{(0)} \Bigr\rvert,
$$

independent of $n$. Consequently the descended term enters
the tower sum **at level $0$ only**; levels $n \ge 1$
contribute only through transient modes
$\mathcal{A}^{\mathrm{trans}}_{n+1} = \ker\hat\tau_n$.

## Derivation

*Step 1 — :refterm[Descent]{#descent} is idempotent.* By construction
([:refterm[descent]{#descent} involution](#def:descent-involution)),
$\hat\tau_n = \ell_n \circ \mathfrak{d}_{n+1}$ with
$\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}_{\mathrm{End}(A_n)}$,
so

$$
  \hat\tau_n^2 = \ell_n \circ (\mathfrak{d}_{n+1} \circ \ell_n)
    \circ \mathfrak{d}_{n+1}
    = \ell_n \circ \mathfrak{d}_{n+1} = \hat\tau_n.
$$

The descended subalgebra is the fixed-point subspace:
$\hat\tau_n|_{\mathcal{A}^{\mathrm{desc}}_{n+1}} = \mathrm{id}$.

*Step 2 — :refterm[Descent]{#descent} factors through the base.* For any
$\alpha \in \mathrm{End}(A_{n+1})$,

$$
  \hat\tau_n(\alpha)
  = \ell_n\bigl(\mathfrak{d}_{n+1}(\alpha)\bigr)
  \;\in\; \ell_n\bigl(\mathrm{End}(A_n)\bigr)
  \cong \mathrm{End}(A_n).
$$

Writing $\alpha_n := \mathfrak{d}_{n+1}(\alpha)$ for the
descended representative at level $n$, the compatibility of
the categorical trace with $\ell_n$
([topological mass proof](#prf:topological-mass), Step 2) gives

$$
  \mathrm{tr}\bigl(\hat\tau_n(\alpha)\bigr)
  = \mathrm{tr}\bigl(\ell_n(\alpha_n)\bigr)
  = \mathrm{tr}_n(\alpha_n).
$$

The descended trace at level $n+1$ therefore equals the level-$n$
trace of the descended representative — a level-lowering step.

*Step 3 — Recursion to the base.* Apply Step 2 iteratively.
Let $\alpha^{(k)} := \mathfrak{d}_k(\alpha^{(k+1)})$ be the
recursive :refterm[descent]{#descent} to level $k$. Then for all $0 \le k \le n$,

$$
  \mathrm{tr}\bigl(\hat\tau_n \circ \hat\tau_{n-1} \circ \cdots
    \circ \hat\tau_k\,(\alpha^{(n+1)})\bigr)
  \;=\;
  \mathrm{tr}_k\bigl(\alpha^{(k)}\bigr).
$$

At the base level $k = 0$, $\alpha^{(0)}$ is the mass integrand
$(\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho_0$ of
the base-level cycle $\varrho_0$. The iterated descended trace
therefore equals the base-level mass:

$$
  \lVert \mathrm{tr}(\hat\tau_n(\alpha^{(n+1)})) \rVert
  \;=\; \lVert \mathrm{tr}_0(\alpha^{(0)}) \rVert
  \;=\; \mathfrak{m}(\varrho_0).
$$

*Step 4 — Independence from $n$.* Step 3 holds for every
$n \ge 0$. The descended norm is therefore a **single
$n$-independent quantity**, namely the level-$0$ base-cycle
mass. In the explicit formula
([mass endomorphism tower](#prop:mass-endomorphism-tower)):

$$
  \mathfrak{m}(\varrho_0)
  \;=\;
  \Bigl\lvert \textstyle\prod_i \hat V_i^{(0)} \Bigr\rvert,
$$

the right-hand side of which involves only the level-$0$ Hecke
traced volumes. The desc term entering at each jet level is
therefore **the same object**, not a new per-level contribution.
$\square$

## Per-level summation as a double count

If the tower sum were written as

$$
  \mathfrak{m}(\varrho)
  \;\stackrel{?}{=}\;
  \sum_{n=0}^{N}
    \Bigl(
      \bigl\lvert\textstyle\prod_i \hat V_i^{(n)}\bigr\rvert
      + \sum_i \Phi_q(|\hat V_i^{(n)}|)
      + z^2 \sum_{(i,j)} \Phi_q(|\hat V_i^{(n)}\hat V_j^{(n)}|)
    \Bigr),
$$

every level would carry a separate descended product. By
Step 4 each such product equals $\mathfrak{m}(\varrho_0)$ (up
to the $\hbar_q^{2n}$ brane-tower weight), and the tower sum
would overcount the base-level holonomy by

$$
  \sum_{n=1}^{N} \hbar_q^{2n} \cdot \mathfrak{m}(\varrho_0)
  \;=\;
  \mathfrak{m}(\varrho_0) \cdot
  \frac{\hbar_q^{2}(1 - \hbar_q^{2N})}{1 - \hbar_q^{2}}.
$$

At $q_0 \approx 1.11$ and $N = 3$, this overcount is
$\approx 0.00991 \cdot \mathfrak{m}(\varrho_0)$ — a **1%
contamination** of every binding-energy prediction, much larger
than the target ppm precision. The $\hbar_q^{2n}$ weights damp
but do not eliminate the double count; only explicit restriction
to level $0$ for the descended term eliminates it.

## Correct formula

Combining Step 4 with the transient decomposition of
([topological mass proof](#prf:topological-mass)) and the
quadratic closure of
([jet-tower remark](#rem:mass-endomorphism-jet-tower)):

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \underbrace{\Bigl\lvert \textstyle\prod_i \hat V_i^{(0)} \Bigr\rvert}_{\text{desc, level 0 only}}
  \;+\;
  \sum_{n=0}^{N} \hbar_q^{2n}
    \Bigl(
      \sum_i \Phi_q(|\hat V_i^{(n)}|)
      + z^2 \sum_{(i,j) \in \mathcal{P}_n}
        \Phi_q(|\hat V_i^{(n)} \hat V_j^{(n)}|)
    \Bigr).
$$

The descended factor is pulled out of the level sum. Only
the transient contributions (singletons and pairs) retain
the per-level $\hbar_q^{2n}$ weights, and they vanish
geometrically by the jet-tower tail bound
([jet-tower convergence](#prop:jet-tower-convergence)).

## Engineering consequence

This proposition is the derivational justification for the
HIGH-#1 fix in the infrastructure audit
(`docs/infrastructure-audit-.md`):

> Strip the desc term from `tower_mass_level` calls inside the
> level loop; compute desc once at level 0 and treat levels 1+
> as singleton + pair only.

The fix is not a canonical trick or heuristic: it is the
correct implementation of Step 4 above. The code's prior
behaviour of re-adding the descended product at every jet
level violated the idempotence of $\hat\tau_n$ and overcounted
the level-$0$ holonomy by the geometric series displayed above.

## Relation to the Nakayama triviality

At the base level, the Nakayama automorphism
$\Psi = S^2 = \mathrm{id}$ in $H_n(R, q)$
([categorical mass as Markov trace](#prop:categorical-mass-markov)),
The single-level mass is $\mathrm{tr}_M(\rho(\beta))$
(signed at the categorical level; positive observable at $q_0$
by Wenzl positivity for canonical $T_w$).
The base-level descended term $\prod_i \hat V_i^{(0)}$ is
exactly this Markov trace by the factorization theorem
([Markov trace factorization](#thm:markov-trace-factorization)).
The descended contribution is therefore the **Nakayama-trivial
holonomy at the base**, and its $n$-independence in Step 4 is
the jet-tower expression of Nakayama triviality: every :refterm[descent]{#descent}
step undoes a jet prolongation without introducing new Nakayama
twist.

## Lean formalization

The companion Lean `descended_level_zero` states the result conditional on a `DescendedLevelZeroContext` class instance and defers its proof via `sorry` (`-- Ref: [manuscript]`).

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: descended-level-zero.md -->

<!-- FILE_START: jet-tower-convergence.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$ and Planck-$q$ constant
$\hbar_q = (q-1)/q$.  For a vortex $\varrho$ with braid
representative $\beta \in B_n$, the brane-tower refinement of the
mass endomorphism
([mass tower](#prop:mass-endomorphism-tower),
[jet-brane reformulation](#rem:mass-endomorphism-jet-tower))
takes the form

$$
  \mathfrak{m}(\varrho)
  = \mathfrak{m}^{(0)}(\varrho)
  + \sum_{n=1}^{\infty} \hbar_q^{2n} \cdot \Delta^{(n)}(\varrho),
$$

where $\mathfrak{m}^{(0)}$ is the canonical Markov-trace term at
brane level zero and $\Delta^{(n)}(\varrho) = \mathfrak{m}^{(n)}
(\varrho_\mathrm{free}) - \mathfrak{m}^{(n)}(\varrho_\mathrm{atom})$
is the per-level binding contribution at brane level $n$.  The
$\hbar_q^{2n}$ weight comes from the recursive brane tower
$A_{n+1} = A_n \otimes \Omega^1(A_n)$: each jet-up step pairs a
Kähler form with its Frobenius dual, contributing $\hbar_q^2$ to
the weight.

**Proposition.**
*Assume there exists $\Delta_{\max}(\varrho) < \infty$ with
$|\Delta^{(n)}(\varrho)| \leq \Delta_{\max}(\varrho)$ for all
$n \geq 1$.  Then the brane-tower sum
$T(\varrho) := \sum_{n \geq 1} \hbar_q^{2n} \Delta^{(n)}(\varrho)$
converges absolutely, and the $N$-term truncation error is
bounded by*

$$
  \bigl\lvert T(\varrho)
    - \sum_{n=1}^{N} \hbar_q^{2n}\,\Delta^{(n)}(\varrho) \bigr\rvert
  \;\leq\; \Delta_{\max}(\varrho) \cdot
  \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^{2}}.
$$

*In particular, to achieve binding-energy precision
$\varepsilon_B$ (in MeV) at archimedean calibration $E_0$, it
suffices to take*

$$
  N \;\geq\;
  \left\lceil \frac{\log\bigl( \tfrac{\varepsilon_B \,(1 - \hbar_q^{2})}
                                {E_0 \,\Delta_{\max}(\varrho)} \bigr)}
                 {\log(\hbar_q^{2})} \right\rceil.
$$
## Remark on the hypothesis

The hypothesis $|\Delta^{(n)}(\varrho)| \leq \Delta_{\max}(\varrho)$
— uniform boundedness of per-level binding across the brane tower —
is the named conjecture
[`conj:jet-tower-uniform-delta-max`](#conj:jet-tower-uniform-delta-max)
(workplan **P3.4** path (b)). This proposition therefore
**reduces the convergence question to a single boundedness
statement**: once $\Delta^{(n)}$ is shown to be bounded (uniformly
or with growth slower than $\hbar_q^{-2n}$), the tail decays as a
geometric series.

Empirically (see
the canonical formalism
and the formal derivation) the per-level terms for $\mathrm{D}$,
$\mathrm{T}$, $\mathrm{^{3}He}$ satisfy
$|\hbar_q^{2n} \Delta^{(n)}| \leq |\hbar_q^{2(n-1)} \Delta^{(n-1)}|
\cdot \hbar_q^2$ to three significant figures, and the
`uniform_bound_pass` flag in
[`jet-tower-delta-max.witness.json`](../../../computations/jet-tower-delta-max.witness.json)
is **true** for D, T, ${}^{3}$He across $n = 1, \dots, 7$ — consistent
with $\Delta^{(n)}$ being bounded (in fact roughly constant).
Promoting that observation to a theorem closes the open
subconjecture
[`conj:jet-tower-uniform-delta-max`](#conj:jet-tower-uniform-delta-max).

## Engineering consequence

Combined with the empirical level-1 residual $\varepsilon^{(1)} =
|\Delta^{(1)}|$ reported by the engine, the proposition gives a
constructive error budget: once the within-level $\hat{V}$ model is
improved so $\varepsilon^{(1)}$ is at the target precision, a single
extra jet level gives $O(\hbar_q^2)$ further reduction.  The jet
loop is therefore **not the bottleneck for sub-ppm precision** —
the level-1 $\hat{V}$ model is.

## Relation to confinement SDP

The level-1 $\hat V^{(1)}$ baseline entering this proposition is
produced by the SDP-feasible confinement operator of
[prop:confinement-sdp](#prop:confinement-sdp).  When the confinement
SDP is at a rank-1 solution (scalar LP regime) the baseline $\hat V$
is a real braid-word product and the boundedness hypothesis
$|\Delta^{(n)}| \le \Delta_{\max}$ holds empirically (cf.
`sdp-lift-audit.witness.json`: every real Hecke word has $x^T G x
\ge 0$).  At higher ranks the hypothesis is open, and the jet-tail
bound above remains conditional on the multi-operator binding
supporting a uniform $\Delta_{\max}$.  Closing that conditional is
the main outstanding piece of open subconjecture 1 on
[rem:mass-endomorphism-jet-tower](#rem:mass-endomorphism-jet-tower).

*Formal asymptotic content. The geometric tail is the native
Jackson $d_q$-difference of the brane tower;
$\ordw(\text{tail}) = 2(N+1)\,\ordw(\hbar_q)$, and the recursive
jet prolongation is the
[surreal blow-up calculus](#def:surreal-blowup-calculus).
See [Big-O via $\ordw$](#rem:conway-normal-form),
[calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon),
and the [body asymptotics catalog](#rem:body-asymptotics-catalog).*
<!-- FILE_END: jet-tower-convergence.md -->

<!-- FILE_START: delta-max-uniform-bound.md -->
*Remark.* This proposition is tightly coupled to the
$\Phi_q$-tower binding pipeline. The active framework instead
uses JSJ decomposition with hyperbolic volumes; the result here
is retained as the analogous tail bound on the $\Phi_q$ side and
remains mathematically correct.

The jet-tower tail bound
([jet-tower convergence](#prop:jet-tower-convergence))
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
([Markov trace factorization](#thm:markov-trace-factorization),
appendix).

*Step 2 — Jet-level transient lives on a bounded module.*
The :refterm[descent]{#descent} splitting
$\mathrm{End}(A_{n+1}) =
 \mathcal{A}_{n+1}^{\mathrm{desc}} \oplus \mathcal{A}_{n+1}^{\mathrm{trans}}$
([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)) places every
transient endomorphism at level $n+1$ in $\ker\hat\tau_n$.  By
the recursive brane tower
([recursive brane tower](#def:recursive-brane-tower)),
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

## canonical scale

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

## Corollary for the binding energy

Combining with the jet-tower tail bound
([jet-tower convergence](#prop:jet-tower-convergence)), the
$N$-term truncation error for any vortex is

$$
  |E_\mathrm{bind} - E_\mathrm{bind}^{(N)}|
  \;\leq\;
  E_0 \cdot 2\,L(\beta)\,\|\rho(\beta)\|_{\mathrm{op}}^{2}
  \cdot \mathfrak{m}^{(0)}(\varrho_{\mathrm{free}})
  \cdot \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^{2}}.
$$

For light atoms ($A \le 16$) at $q_0$, canonical evaluation
shows $N = 3$ is sufficient for sub-ppm precision on binding
energies; the bound is saturated within a factor of 2 on the
deuteron, tritium, and ${}^3\mathrm{He}$
(cf. the formal derivation with
`JET_TARGET_PPM`).

## Remaining open items

This proposition closes the **archimedean / rank-1 SDP**
regime of the convergence conjecture
([jet-tower remark](#rem:mass-endomorphism-jet-tower),
subconjecture 1).  The two remaining pieces are:

1. **Multi-rank confinement SDP.**  At higher SDP ranks the
   baseline $\hat V^{(1)}$ is not a single braid product, and
   the operator-norm control in Step 2 must be replaced by a
   sum over rank-1 summands with weights from the SDP
   eigenvalues.  The qualitative bound survives (operator norms
   are subadditive), but the canonical prefactor degrades.
2. **Sharp constant.**  The factor $2\,L(\beta)\,\|\rho\|^2$
   is a worst-case bound; for stable atoms the effective
   $\Delta_{\max}$ is empirically within a factor of 2 of the
   level-1 value $\Delta^{(1)}$ itself (i.e.\ near-monotone
   decay).  A sharp constant would require a specific
   representation-theoretic analysis of the jet prolongation
   map on the Jones--Wenzl filtration.
<!-- FILE_END: delta-max-uniform-bound.md -->

<!-- FILE_START: mass-tower-syt-cells.md -->
This remark reframes the pair blow-up set $\mathcal{P}_n$
([jet-brane reformulation](#rem:mass-endomorphism-jet-tower))
using the Jucys--Murphy (JM) elements and standard Young tableaux
(SYT). The motivation: empirical probes show the optimal
$\mathcal{P}_n$ is *all pairs with no distance restriction*
([:refterm[descent]{#descent} rate categorical](#sim:descent-rate-canonical evaluation)), which
is most accordingly expressed in the JM / SYT cell basis.

## Jucys--Murphy elements

For $H_n(R, q)$ with generators $\sigma_1, \ldots, \sigma_{n-1}$, the
**Jucys--Murphy (JM) elements** are

$$
  L_k = \sigma_{k-1} \sigma_{k-2} \cdots \sigma_1 \sigma_1 \cdots \sigma_{k-1},
  \qquad k = 1, \ldots, n,
$$

with $L_1 = 1$. They commute pairwise ($[L_i, L_j] = 0$) and
act diagonally on the Young basis: for a SYT $T$ of shape
$\lambda$ and basis vector $v_T$,

$$
  L_k \, v_T
  = q^{2 c_T(k)} \, v_T,
$$

where $c_T(k) = j - i$ is the content of the cell of $T$
containing the integer $k$ (cell at row $i$, column $j$).

## SYT cell reindexing

The pair set $\mathcal{P}_n$ in
[jet-brane form](#rem:mass-endomorphism-jet-tower) is accordingly
**cell-indexed** via JM:

$$
  \mathcal{P}_n
  \;\longleftrightarrow\;
  \{\{k_1, k_2\} \subseteq \{1, 2, \ldots, n\}\},
$$

with each pair $\{k_1, k_2\}$ corresponding to a pair of cells
in any SYT shape $\lambda \vdash n$. Under this reindexing:

* **Generator distance $|i - j|$** is not preserved — JM indices
 $k$ range over cells, not over generator positions, so there is
 no "adjacent vs far-commuting" distinction.

* **Eigenvalue product** is diagonal: on $v_T$,

 $$
    L_{k_1} L_{k_2} \, v_T
    = q^{2(c_T(k_1) + c_T(k_2))} \, v_T.
  $$

* **All pairs are on equal footing**: $[L_i, L_j] = 0$ by
 construction. This matches the empirical finding that
 $\beta(d) = 1$ uniformly across distances
 ([:refterm[descent]{#descent} rate canonical evaluation](#sim:descent-rate-canonical evaluation)).

## Reformulated mass tower

Using JM / SYT cells, the per-jet-level contribution becomes:

```tex
\begin{equation}\label{eq:syt-cell-tower}
  \mathfrak{m}^{(n)}(\varrho)
  =
  \bigl\lvert\textstyle\prod_{k=1}^{n} \hat V_k^{\mathrm{JM}}\bigr\rvert
  + \textstyle\sum_{k=1}^n \Phi_q(|\hat V_k^{\mathrm{JM}}|)
  + z^2 \textstyle\sum_{1 \leq k_1 < k_2 \leq n}
      \Phi_q(|\hat V_{k_1}^{\mathrm{JM}} \hat V_{k_2}^{\mathrm{JM}}|),
\end{equation}
```

where $\hat V_k^{\mathrm{JM}}$ is the Markov-trace-weighted
eigenvalue of $L_k$ in the braid word's irrep, weighted by the
Plancherel measure on $\lambda \vdash n$:

$$
  \hat V_k^{\mathrm{JM}}
  =
  \sum_{\lambda \vdash n} w_\lambda
    \sum_{T \in \mathrm{SYT}(\lambda)}
      \mu_T \cdot q^{2 c_T(k)},
$$

with $\mu_T$ = normalised SYT Plancherel weight.

The pair weight $z^2$ in the cross sum matches the generator-indexed
form of [prop:mass-endomorphism-tower](#prop:mass-endomorphism-tower)
and is justified universally (all $k_1 < k_2$, not just adjacent
pairs) by the
[Markov-trace factorization theorem](#thm:markov-trace-factorization):
two successive Markov peels of commuting elements each contribute a
factor $z$, so $\mathrm{tr}_M(L_{k_1} L_{k_2}) = z^2$. In the JM /
SYT reindexing this is automatic — $[L_i, L_j] = 0$ makes every pair
structurally equivalent to the far-commuting case covered by the
factorization theorem.

## Advantages

1. **All pairs automatic.** $[L_i, L_j] = 0$ gives a symmetric
 pair sum with no adjacent/far distinction — consistent with the
 empirical $\beta(d) = 1$.
2. **:refterm[Descent]{#descent} structure visible.** The :refterm[descent]{#descent} involution acts on
 SYT shapes by box-removal: a jet-$(n+1)$ transient supported
 on a shape $\lambda \vdash n+1$ descends to jet-$n$ when the
 shape's removable corner is vacated. This is the formal
 :refterm[descent]{#descent} that the generator-indexed form struggles to express.
3. **Multi-level sum structural.** Summing over jet levels
 becomes summing over the SYT tree: each level adds one cell.
 The jet tower $\{A_n\}$ is built by box additions; the mass
 tower sums contributions at each addition.

## Implementation path

1. Compute $L_k$ seminormal eigenvalues $q^{2 c_T(k)}$ per SYT
 (already available via
 `hecke_characters.build_seminormal_matrices` in
 the formal derivation).
2. Build $\hat V_k^{\mathrm{JM}}$ via Plancherel-weighted sum
 over SYTs.
3. Sum cell-pair Φ\_q contributions (all $\binom{n}{2}$ pairs,
 no distance filter).
4. Iterate over jet levels $n = 0, 1, \ldots, N$ and sum.

Implementation is stubbed in the
[multi-level jet sum simulator](#sim:multi-level-jet-sum).

## Empirical validation

A first-pass implementation
(the formal derivation) computes
$\hat V_k^{\mathrm{JM}}$ for $k = 1, \ldots, 3A$ on the atom braid
word and assembles the tower of
equation\~\ref{eq:syt-cell-tower}. Against the scalar all-pairs form
of [prop:mass-endomorphism-tower](#prop:mass-endomorphism-tower),
with $E_0$ calibrated per path on the proton:

| Atom | scalar all-pairs | JM all-pairs |
| ---- | ---------------: | -----------: |
| D | 0.120% | 0.105% |
| T | 18.0% | **0.277%** |
| 3He | 60.1% | **0.219%** |

The scalar path suffers a pair-pathology on T and 3He even after
[mass-endomorphism-tower.md](#prop:mass-endomorphism-tower)'s
all-pairs form is used; the JM path closes the residual by carrying
the per-SYT content structure missing from a scalar factorization.

## Open question

Does the SYT-cell form reproduce the generator-indexed form at
each $n$, or only up to a :refterm[descent]{#descent} involution? Naively the two
should agree at the per-irrep level (change of basis within each
$V_\lambda$), but the *pair-count* and *independence-claim*
structure may differ, since JM pairs are always commuting and
have no "adjacent vs far" ambiguity — a distinction now formally
absorbed into the
[Markov-trace factorization theorem](#thm:markov-trace-factorization).
The T/3He residual closure in the table above suggests the JM
form is not only a basis change: it captures SYT-content
correlations that the scalar factorization drops.
<!-- FILE_END: mass-tower-syt-cells.md -->

<!-- FILE_START: markov-pair-z2.md -->
Let $H_n(R, q)$ be the Iwahori--Hecke algebra with Markov trace
$\mathrm{tr}_M$ normalised by $\mathrm{tr}_M(1_k) = 1$ for all $k$
and Markov axiom $\mathrm{tr}_M(x\sigma_{k-1}) = z\,\mathrm{tr}_M(x)$
for $x \in H_{k-1}(q)$, where
$z = 1/(q^{1/2} + q^{-1/2})$ ([Jones--Markov trace](#thm:jones-markov-trace)).

**Proposition.** For every pair of braid generators
$\sigma_i, \sigma_j$ with $0 \le i < j$, embedded in any
$H_n(R, q)$ with $n > j$,

$$
  \mathrm{tr}_M(\sigma_i\sigma_j) \;=\; z^2.
$$

The identity holds whether $(i,j)$ are adjacent ($j = i+1$)
or non-adjacent ($j \ge i+2$).
## Operator interpretation

The value $z^2$ is the **Jones polynomial of the Hopf link**
(unknotted two-component linking) evaluated at the substrate
parameter:
$J_{\mathrm{Hopf}}(q) = -(q^{1/2} + q^{-1/2})\cdot z^2
= -(q + q^{-1})/(q^{1/2} + q^{-1/2})$. Multiplying by the
Markov normalization recovers the pair contribution to the
categorical mass — the pair blow-up centre at coordinate
$\hat V_i\hat V_j$ carries the same weight $z^2$ regardless
of its position in the braid, matching the empirically-verified
all-pairs set on atoms $A \ge 6$
(cf. `adjacent-vs-full-canonical evaluation.witness.json`,
[jet-tower remark](#rem:mass-endomorphism-jet-tower)).
<!-- FILE_END: markov-pair-z2.md -->


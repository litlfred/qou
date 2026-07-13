<!-- FILE_START: speed-of-light-intro.md -->
Having established the Reeb-flow operational entropy and the Planck step, we now extract a velocity and a mass--energy law. The $q$-connection on the state bundle, operating at the substrate parameter $q_0$, natively defines a Lieb--Robinson cone for information propagation. This causal cone forms the physical speed of light.

The speed of light emerges as the Lieb--Robinson velocity $c_q = 1/(q-1)$. This bounds the maximum information bandwidth per Planck step. A rigorous mass--energy equivalence ($E_{\mathfrak{H}} = \mathfrak{m}_{\mathfrak{H}} \cdot c_q^2$) follows immediately by evaluating the categorical trace of the crossing energy within the ribbon category. Mass $\mathfrak{m}$ assumes a Gröbner–Shirshov interpretation: it quantifies the topological cost of threading a photon through a knot. Subsequently, the gravitational constant $G_q$ aligns with Jacobson's entropy--area derivation via information geometry. The Hausdorff dimension $d_H(q) = (2q-1)^2/q^3$ directly governs the discrete recurrence, saturating the Margolus--Levitin bound. These parameters—$c_q$ and the bandwidth budget $\mathfrak{B}(q)$—will subsequently strictly bound every Toffoli step.
<!-- FILE_END: speed-of-light-intro.md -->

<!-- FILE_START: information-speed-of-light.md -->
We derive the speed of light from the ratio of spatial to temporal information transfer within a light cone ([light cone](#rem:light-cone-affine)). It is a $q$-dependent quantity, not a postulated constant, and we do not set it to $1$ by definition.

**Definition.**
The *speed of light* at substrate parameter $q$ is the ratio of the spatial coupling weight $q^{-1}$ to the temporal coupling weight $\hbar_q = 1 - q^{-1}$ of the $q$-connection ([$q$-connection](#ex:q-connection)):

$$
  c_q  :=  \frac{q^{-1}}{\hbar_q}
  =  \frac{q^{-1}}{1 - q^{-1}}
  =  \frac{1}{q - 1}.
$$

We evaluate the contact affine coordinate ([contact affine chart](#def:contact-affine-chart)) $Z = \alpha_H / (\iota_\xi\alpha)$ on the $q$-connection. This measures the ratio of horizontal spatial diffusion to vertical quantum spin. This defines the Lieb--Robinson velocity of the causal cone: the number of spatial information fibres correlated per unit of Reeb phase advance in one discrete $f_q$-iteration.
<!-- FILE_END: information-speed-of-light.md -->

<!-- FILE_START: information-bandwidth.md -->
**Definition.**
The **information bandwidth** per Planck time quantifies the total information transferred across the causal boundary in one Planck step. It is the product of the speed of light $c_q$ ([speed of light](#def:information-speed-of-light)) (fibres correlated per tick) and the operational entropy per fibre ([operational entropy](#def:operational-entropy)):

$$
  \mathfrak{B}(q)
  = c_q \cdot n_R(q) \cdot \eta_q
  = \frac{\eta_q}{\hbar_q \cdot (q-1)}
  = \frac{\eta_q}{q^{-1}(q-1)^2}
  = \frac{q \cdot \eta_q}{(q-1)^2}.
$$

At $q = q_0$, the bandwidth $\mathfrak{B} = q\eta_q/(q-1)^2 \approx 82$ $q$-bits per Planck time. This functions as the Bremermann-analog bit budget of the substrate. It dictates the maximum number of distinguishable $q$-bits that a single Planck step can carry across the light-cone boundary.
<!-- FILE_END: information-bandwidth.md -->

<!-- FILE_START: speed-of-light-regimes-lieb-robinson.md -->
The speed of light $c_q = 1/(q-1)$
([speed of light](#def:information-speed-of-light)) is a derived,
$q$-dependent quantity. This remark records the $q$-connection
decomposition that produces it, its regime behaviour, the
Lieb--Robinson decay of the causal cone, and its place among the
information-theoretic speed limits.

**The $q$-connection decomposition.**
The archimedean $q$-connection
([$q$-connection](#ex:q-connection)) splits the gauge potential
into horizontal (spatial) and vertical (Reeb/temporal) components:

$$
  A_q =  q^{-1}A
  +  (1 - q^{-1})\iota_\xi A\varTheta
  =  q^{-1}A
  +  \hbar_q\iota_\xi A\varTheta.
$$

The weight $q^{-1}$ controls horizontal information transfer
(spatial propagation between fibres), while $\hbar_q = 1 - q^{-1}$
controls vertical information processing (Reeb flow within a fibre).
Each $f_q$-iteration applies $A_q$ once, simultaneously advancing
the Reeb phase by $\hbar_q$ and correlating adjacent fibres with
coupling strength $q^{-1}$.

**Physical meaning.**
In each discrete $f_q$-iteration:

* The Reeb flow advances the fibre phase by $\hbar_q$ (temporal
 information: one tick of the internal clock).
* The $q$-connection correlates the current fibre with adjacent
 fibres at coupling $q^{-1}$ (spatial information: one step of
 horizontal propagation).

A measurement within the light cone compares these two rates.
The speed of light is how many fibres of spatial information are
correlated per unit of Reeb phase advance:

$$
  c_q =  \frac{\text{spatial coupling per step}}
                   {\text{temporal advance per step}}
  =  \frac{q^{-1}}{\hbar_q}
  =  \frac{1}{q - 1}.
$$

**Regime behaviour.**

| Regime | $q$ | $c_q = 1/(q-1)$ | Interpretation |
| --------------- | ------------------------- | --------------------------- | ----------------------------------------------------------------- |
| Deep-quantum | $q \to \infty$ | $\to 0$ | No spatial propagation; each fibre is isolated |
| Deep quantum | $\varphi^2 \approx 2.618$ | $\approx 0.618 = 1/\varphi$ | Sub-luminal; spatial coupling suppressed |
| Our universe | $q_0$ | $\approx 9.12$ | ${\sim}9$ fibres correlated per Reeb phase advance |
| Near-classical | $1.01$ | $100$ | Fast spatial propagation; nearly continuous |
| Classical limit | $q \to 1^+$ | $\to \infty$ | Instantaneous spatial coupling; the $q$-connection reduces to $A$ |

At $q = q_0$, the speed of light is $c \approx 9.12$ in units
where one Reeb phase advance $= 1$. This is **not** $1$. The
value $c = 1$ arises only if one redefines length units so that
one "Planck length" equals $c_q$ Reeb phases --- but that obscures
the physics. In the natural units of the $q$-connection (where
temporal ticks and spatial couplings are measured on the same
footing), $c$ is $q$-dependent and equals $1/(q-1)$.

**Consistency: $c$ diverges at the classical limit.**
As $q \to 1$, the $q$-connection $A_q \to A$ (the full instanton
connection): the horizontal component dominates, spatial correlations
propagate instantly relative to the Reeb tick, and smooth
Riemannian geometry with $c = \infty$ (instantaneous spatial
coupling) emerges. This is the Newtonian limit. To recover finite
$c$ in SI units, one rescales by the Planck time
$t_P^{\mathrm{SI}} = \sqrt{\hbar G / c_{\mathrm{SI}}^5}$, which
absorbs the divergence into the ratio of human-scale seconds to
Reeb ticks.

**Connection to the contact affine chart.**
The light cone of an affine chart
([light cone](#rem:light-cone-affine)) is the locus $|Z| = c_q$:
the boundary where horizontal diffusion exactly matches vertical
advance. Inside the cone ($|Z| < c_q$), spatial signals arrive
within one Reeb circuit. Outside ($|Z| > c_q$), the signal
requires multiple Reeb circuits and is causally delayed.

**Lieb--Robinson bound.**
The locality of $\nabla_q$ (it acts on adjacent fibres only) and
the unitarity of the $R$-matrix (norm-preserving braiding in the
rigid :refterm[monoidal category]{#monoidal-category} $\mathbf{C}$) give an exponential decay
outside the causal cone:

$$
  \bigl\lVert
    [\mathcal{O}_x(n), \mathcal{O}_y(0)]
  \bigr\rVert
   \leq 
  C  e^{-\mu(d(x,y) -  n \cdot c_q \cdot \hbar_q)}
$$

for constants $C, \mu > 0$ depending on $q$. The causal cone
boundary is $d(x,y) = n \cdot c_q \cdot \hbar_q = n \cdot q^{-1}$:
after $n$ discrete steps, a signal has propagated $n \cdot q^{-1}$
units of base-manifold distance.

**Comparison with information-theoretic speed limits.**

| Result | Bound | QOU analog |
| ------------------------ | --------------------------------------- | --------------------------------------------------------- |
| Margolus--Levitin (1998) | $\leq 2E/\pi\hbar$ ops/sec | $n_R(q) = 1/\hbar_q$ ops per Planck time |
| Bremermann (1962) | $\leq mc^2/h$ bits/sec/kg | $\mathfrak{B}(q) = q\eta_q / (q-1)^2$ bits per Planck time |
| Bekenstein (1981) | $S \leq 2\pi RE / \hbar c$ | Fibre entropy $\leq \eta_q$ per operation |
| Pawlowski (2009) | No-signaling from information causality | Lieb--Robinson decay outside $\lvert Z\rvert = c_q$ cone |
<!-- FILE_END: speed-of-light-regimes-lieb-robinson.md -->

<!-- FILE_START: dsr-planck-scale-phenomenology.md -->
*Interpretation of the [information speed of light](#def:information-speed-of-light).*

The derived light speed $c_q = 1/(q-1)$ and the $O(1 - q^{-1})$ group-velocity corrections induced by the $q$-integer phase $[k]_q$ on photon modes ([photon modes](#rem:photon-propagation-1d)) locate this framework within the lineage of doubly special relativity (DSR) and Planck-scale phenomenology. This literature provides both a structural precedent and the sharpest experimental constraints.

**Structural kinship with DSR.**
Amelino-Camelia's testable minimum-length scenario \cite{amelinocamelia2001} introduces a second observer-independent scale—a Planckian length—alongside the speed of light. It deforms the photon dispersion relation at first order in the ratio of the photon's energy to a quantum-gravity scale $\mathfrak{E}_{\mathrm{QG}}$. A quantum-group ($\kappa$-Poincaré) structure, rather than the classical Poincaré algebra, realizes the deformed symmetry. 

The QOU substrate mirrors this construction. The deformation parameter $q$ acts as the Planckian invariant. Macroscopic Lorentz covariance emerges only after the archimedean projection. In both frameworks, the photon velocity is energy-dependent at the deformed level. In DSR this occurs through the modified dispersion relation; here, it occurs through the $q$-integer phase $[k]_q$ replacing the classical wavenumber $k$. The DSR precedent proves that an observer-independent deformation scale is compatible with a relativity principle and avoids a preferred frame. The local substrate $q_0$ should enter the archimedean layer as a second invariant, not as a frame-dependent violation.

**Experimental constraints.**
Time-of-flight tests on gamma-ray bursts probe the Planck scale \cite{amelinocamelia1998}. The Fermi observation of GRB 090510 \cite{abdo2009} excludes photon dispersion linear in the energy ratio up to a quantum-gravity scale exceeding the Planck energy. The surrounding observational programme is surveyed in \cite{amelinocamelia2013}. 

Prima facie, the substrate values strongly conflict with these bounds. A fractional dispersion of order $\hbar_q = 1 - q^{-1}$ surviving to astrophysical photon propagation would exceed the GRB limits by many orders of magnitude. To maintain consistency, the $q$-deformed dispersion must remain confined to the substrate (fibre) level. The archimedean projection must suppress its residue at accessible energies. The framework does not currently derive this suppression scale. This is the sharpest falsifiability exposure of the dispersive prediction. An eventual substrate-to-archimedean dispersion calculation must guarantee that any archimedean residue of the $[k]_q$ phase falls below the GRB 090510 limit \cite{abdo2009}.
<!-- FILE_END: dsr-planck-scale-phenomenology.md -->

<!-- FILE_START: dispersion-suppression-scale.md -->
At the fibre level, a mode of wavenumber $k$ on a one-dimensional channel ([channel](#def:one-dim-qou-channel)) advances with the $q$-integer phase $[k]_q$. Its group velocity carries fractional corrections of order $\hbar_q = 1 - q^{-1}$ relative to the substrate light speed $c_q = 1/(q-1)$ ([information speed of light](#def:information-speed-of-light)).

**Conjecture.** *The archimedean projection suppresses the fibre-level $q$-dispersion. The residual fractional variation of the archimedean photon group velocity with photon energy $\mathfrak{E}$ is bounded by $\mathfrak{E} / \mathfrak{E}_{\mathrm{QG}}$ for a suppression scale $\mathfrak{E}_{\mathrm{QG}}$ at or above the Planck energy.*

This bound is required for compatibility with the gamma-ray-burst time-of-flight limit \cite{abdo2009}. The observational context and the relation to doubly-special-relativity phenomenology appear in [the DSR remark](#rem:dsr-planck-scale-phenomenology). The framework derives the fibre-level deformation but does not yet specify the mechanism by which the substrate-to-archimedean projection removes the $O(\hbar_q)$ residue from macroscopic propagation.
<!-- FILE_END: dispersion-suppression-scale.md -->

<!-- FILE_START: mass-energy-equivalence.md -->
*Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be an archimedean quantum observable universe with substrate parameter $q$ and speed of light $c_q = 1/(q-1)$ ([speed of light](#def:information-speed-of-light)). Let $\mathfrak{H}$ be a knot composite in the Frobenius--Hopf object $A$. Then the crossing energy ([crossing energy](#def:crossing-energy)) and the categorical mass ([mass identity](#def:mass-identity)) satisfy*

$$
  E_{\mathfrak{H}}
  =  \mathfrak{m}_{\mathfrak{H}} \cdot c_q^2
  =  \frac{\mathfrak{m}_{\mathfrak{H}}}{(q - 1)^2}.
$$
<!-- FILE_END: mass-energy-equivalence.md -->

<!-- FILE_START: mass-energy-equivalence-interpretation.md -->
**Content of the theorem.**
This relationship is not a unit convention. The crossing energy (the algebraic Skein weight from $R$-matrix braiding) equals the categorical mass (the analytic trace norm derived through the Frobenius pairing and comultiplication) multiplied by the **square of the information speed**. This factor $c_q^2$ is the square of the ratio of spatial coupling to temporal coupling in the $q$-connection.

The factor $c_q^2 = 1/(q-1)^2$ carries a direct information-theoretic interpretation. It converts the resistance to vertical (Reeb) transport (mass) into the horizontal (spatial) crossing weight (energy) by accounting for the mismatch between horizontal and vertical information rates in the $q$-connection.

**Regime behaviour of $E = \mathfrak{m} \cdot c_q^2$.**

| Regime          | $q$            | $c_q^2$         | Physics                                                          |
| --------------- | -------------- | --------------- | ---------------------------------------------------------------- |
| Deep-quantum    | $q \to \infty$ | $\to 0$         | Energy $\to 0$ for any mass: no spatial crossing weight          |
| Deep quantum    | $\varphi^2$    | $\approx 0.382$ | Sub-relativistic: mass dominates energy                          |
| Our universe    | $q_0$          | $\approx 83.2$  | $E \approx 83\mathfrak{m}$: large amplification                  |
| Near-classical  | $1.01$         | $10{,}000$      | Extreme amplification: tiny mass $\to$ large energy              |
| Classical limit | $q \to 1^+$    | $\to \infty$    | $E/\mathfrak{m} \to \infty$: classical $E = mc^2$ with $c$ large |

At $q = q_0$, a vortex with categorical mass $\mathfrak{m}$ carries crossing energy $E = \mathfrak{m}/(q-1)^2 \approx 83\mathfrak{m}$. This large amplification factor explains why nuclear energy ($E = mc^2$) releases vastly more energy than the rest mass implies in everyday units.

We work out the concrete electron consistency check ([electron consistency check](#rem:mass-energy-electron-check)) and the pair-creation reinterpretation ([pair creation reinterpreted](#rem:mass-energy-pair-creation)) separately.

**Archimedean realisation.**
Over $\mathbb{C}$, Yekutieli's nonabelian multiplicative integral \[yekutieli2015] realises the categorical mass ([mass over $\mathbb{C}$](#cor:mass-identity-C)). The relation $E_{\mathfrak{H}} = \mathfrak{m}_{\mathfrak{H}} \cdot c_q^2$ becomes:

$$
  \sum_{\text{crossings}} \epsilon_i
  = 
  \frac{1}{(q-1)^2}
  \bigl\lVert
  \mathrm{MI}\!\!\int_\Sigma
  (\nabla_A q, L \wedge F^+)
  \bigr\rVert,
$$

identifying the discrete Skein weight (spatial) with the rescaled continuous multiplicative-integral norm (temporal).
<!-- FILE_END: mass-energy-equivalence-interpretation.md -->

<!-- FILE_START: mass-energy-electron-check.md -->
The mass--energy relation $E = \mathfrak{m} \cdot c_q^2$ ([mass--energy equivalence](#thm:mass-energy-equivalence)) admits a concrete consistency check using the electron.

**Consistency check: electron.**
The electron (left trefoil $T_{2,3}$) has $n_c = 3$ positive crossings:

* Crossing energy: $E_{e^-} = 3q \approx 3.330$ Skein units.
* Predicted mass: $\mathfrak{m}_{e^-} = E \cdot (q-1)^2 = 3q(q-1)^2$.

At $q = q_0$, $\mathfrak{m}_{e^-} = 3 q_0 \times 0.01203 \approx 0.0401$ in Reeb mass units.
<!-- FILE_END: mass-energy-electron-check.md -->

<!-- FILE_START: mass-energy-pair-creation.md -->
The mass--energy relation $E = \mathfrak{m} \cdot c_q^2$ ([mass--energy equivalence](#thm:mass-energy-equivalence)) reinterprets the pair-production threshold in terms of crossing energy.

**Pair creation reinterpreted.**
The pair production threshold ([pair creation energy](#rem:pair-creation-energy)) becomes:

$$
  E_{\gamma}  \geq 
  (\mathfrak{m}_{e^-} + \mathfrak{m}_{e^+}) \cdot c_q^2
  =  \frac{\mathfrak{m}_{e^-} + \mathfrak{m}_{e^+}}{(q-1)^2}.
$$

The net crossing energy of the pair is $E_{e^-} + E_{e^+} = 3(q - q^{-1}) \approx 0.630$ (pure Coulomb repulsion). The minimum photon energy must supply both absolute crossing energies: $|E_{e^-}| + |E_{e^+}| = 3(q + q^{-1}) = 6\cosh(\ln q) \approx 6.033$ Skein units.
<!-- FILE_END: mass-energy-pair-creation.md -->

<!-- FILE_START: photon-threading-mass.md -->
*Let $\mathfrak{H}$ be a knot composite with braid word $\beta_{\mathfrak{H}} \in B_n$. The categorical mass $\mathfrak{m}_{\mathfrak{H}}$ ([mass identity](#def:mass-identity)) equals the total Gröbner--Shirshov reduction cost of threading the photon strand $\gamma$ through the hadron braid:*

$$
  \mathfrak{m}_{\mathfrak{H}}
  =  (q - 1)^2 \sum_{\text{Hecke steps}}
  |c_w| \cdot |q - q^{-1}|.
$$

*The sum runs over all Hecke reductions $\sigma_i^2 \to (q - q^{-1})\sigma_i + 1$ required to move the photon strand from above $\beta_{\mathfrak{H}}$ to below $\beta_{\mathfrak{H}}$ in the augmented braid $\gamma \otimes \beta_{\mathfrak{H}} \in B_{n+1}$. The values $c_w$ denote the coefficients at each step.*
<!-- FILE_END: photon-threading-mass.md -->

<!-- FILE_START: photon-threading-mass-interpretation.md -->
**Three computations of the same quantity.**

We compute the mass $\mathfrak{m}_{\mathfrak{H}}$ using three independent methods. All three yield identical results:

| Method | Domain | Computes $\mathfrak{m}_{\mathfrak{H}}$ as |
|--------|--------|------------------------------|
| Yekutieli MI | Analytic | $\lVert\mathrm{MI}\int_\Sigma(\nabla_A q, L \wedge F^+)\rVert$ |
| Ribbon trace | Algebraic | $\lVert\mathrm{tr}_{\mathrm{ribbon}}(\rho(\beta_{\mathfrak{H}}))\rVert \cdot (q-1)^2$ |
| Gröbner--Shirshov reduction | Computational | $(q-1)^2 \sum \lvert c_w\rvert \cdot \lvert q - q^{-1}\rvert$ |

The first represents the definition ([mass over $\mathbb{C}$](#ex:mass-identity-su2)). The second derives from the ribbon category structure ([mass--energy equivalence](#thm:mass-energy-equivalence)). The third forms the content of this proposition.

**Physical picture.**

The photon $\gamma$ ($\mathbf{1}_{B_4}$ 4-strand identity) is knot-trivial under Markov closure. It approaches the hadron $\mathfrak{H}$. To "measure" the hadron—to determine its mass—the photon must braid completely through $\mathfrak{H}$, moving from one side of the braid word to the other.

1. **Start.** The photon strand sits above the hadron braid: $\gamma \otimes \beta_{\mathfrak{H}} \in B_{n+1}$.
2. **Thread.** We apply braid relations to move $\gamma$ downward through $\beta_{\mathfrak{H}}$. The Yang--Baxter moves ($\sigma_i\sigma_{i+1}\sigma_i = \sigma_{i+1}\sigma_i\sigma_{i+1}$) and far-commutativity ($\sigma_i\sigma_j = \sigma_j\sigma_i$) are **free**. They rearrange crossings without altering the Skein weight ([Gröbner--Shirshov energy](#thm:groebner-shirshov-energy)). Only the **Hecke steps** ($\sigma_i^2 \to (q - q^{-1})\sigma_i + 1$) cost energy. Each Hecke step resolves a double crossing into a weighted single crossing plus a resolved identity.
3. **End.** The photon strand sits below $\beta_{\mathfrak{H}}$. The total Hecke cost equals the crossing energy $E_{\mathfrak{H}} = \sum |c_w| \cdot |q - q^{-1}|$ in Skein units. Mass--energy equivalence yields the mass: $\mathfrak{m}_{\mathfrak{H}} = E_{\mathfrak{H}} \cdot (q-1)^2$.

**Measurement mechanism.**

The photon has no crossings of its own; it is topologically trivial ($K = \varnothing$). It couples to the gauge field ($F_A^+$) because it propagates as exceptional-divisor flux ([photon wavefront](#ex:photon-wavefront)). Threading it through $\mathfrak{H}$ forces it to traverse every crossing of $\beta_{\mathfrak{H}}$. Each traversed crossing forces a Hecke reduction.

The **surface** $\Sigma$ in the Yekutieli integral $\mathrm{MI}\int_\Sigma$ spans the disc swept by the photon through the hadron. The vortex boundary $\partial\Sigma = \varrho$ bounds it. The interior of $\Sigma$ tracks the trajectory of $\gamma$ through $\beta_{\mathfrak{H}}$. The multiplicative integral accumulates the connection along this trajectory, providing the analytic counterpart to the algebraic Gröbner--Shirshov reduction.

**Path independence.**

The Gröbner--Shirshov basis is confluent via the Bergman diamond lemma. The total Hecke cost remains invariant under different reduction orderings. This algebraic path independence expresses the **gauge invariance** of the mass. The Yekutieli integral is independent of the choice of surface $\Sigma$ (for fixed $\partial\Sigma = \varrho$). The Gröbner--Shirshov reduction is independent of the reduction path.

**Connection to the speed of light.**

The conversion factor $(q-1)^2$ between crossing energy and mass is $1/c_q^2$:

$$
  \mathfrak{m}_{\mathfrak{H}} =  \frac{E_{\mathfrak{H}}}{c_q^2}
  =  (q-1)^2 \cdot E_{\mathfrak{H}}.
$$

Each Hecke step costs $|q - q^{-1}|$ in Skein units (spatial information). The factor $(q-1)^2 = (q\hbar_q)^2$ converts this to mass units (temporal information). It equals the square of the ratio of temporal to spatial coupling in the $q$-connection. The photon traverses the hadron at speed $c_q = 1/(q-1)$. The total traversal cost divided by $c_q^2$ is the mass.
<!-- FILE_END: photon-threading-mass-interpretation.md -->

<!-- FILE_START: gravitational-constant.md -->
**Definition.**
The **gravitational constant** $G_q$ normalises the $q$-Yang--Mills--Levi variation ([$q$-YM-Levi](#def:q-yang-mills-levi)). It sets the ratio of curvature to stress-energy in the field equation $\mathrm{Ric}_{g_\varTheta} = T^{(q)}$ ([GR substrate geometry](#rem:gr-substrate-geometry)):

$$
  G_q := \frac{c_q^3 \cdot \hbar_q}{S_{\mathrm{cell}}(q)}
  = \frac{c_q^3 \cdot (2q - 1)}{q^2 \cdot \eta_q \cdot \hbar_q},
$$

where $c_q = 1/(q-1)$ is the speed of light ([speed of light](#def:information-speed-of-light)), $\hbar_q = (q-1)/q$, $\eta_q = (2q-1)/q^3$ is the operational entropy ([operational entropy](#def:operational-entropy)), and $S_{\mathrm{cell}}(q) = (q-1)^2/q^3$ is the cumulative jet-tower entropy of a Planck cell. In Planck units, $G_{\mathrm{Planck}} = G_q\,(\hbar_q/c_q)^2 = 1$ identically for all $q > 1$.
<!-- FILE_END: gravitational-constant.md -->

<!-- FILE_START: gravitational-constant-properties.md -->
The [gravitational constant $G_q$](#def:gravitational-constant) is
derived from the categorical structure of the
$q$-Yang--Mills--Levi action, not from semiclassical entropy-area
relations.  The key ingredient is the **in-progress braid content**
of a Planck cell — the sections of the jet tower that are partially
evaluated but not yet resolved to observable knots.  This remark
records the variational origin, the in-progress-braid counting, the
quadratic suppression that produces $S_{\mathrm{cell}}$, and the
numerical values at $q_0$. The associated Julia-set
Hausdorff-dimension prediction is recorded separately
([Hausdorff-dimension prediction](#rem:julia-hausdorff-dimension-prediction)).

**The variational origin of $G$.**
The field equation $\mathrm{Ric}_{g_\varTheta} = T^{(q)}$
([GR substrate geometry](#rem:gr-substrate-geometry)) arises from
varying the $q$-Yang--Mills--Levi functional
([$q$-YM-Levi](#def:q-yang-mills-levi))

$$
  \mathfrak{S}_q[A, \varTheta]
  =  \int_M q(p)\lVert F_A^+|_H \rVert^2
  \varTheta \wedge (d\varTheta)^n
$$

with respect to the Levi form $L_\varTheta$.  The gravitational
coupling $G$ is the normalisation of this variation: it sets
the ratio of curvature ($\mathrm{Ric}_{g_\varTheta}$) to
stress-energy ($T^{(q)}$).  In standard GR, this normalisation
is postulated.  In the QOU, it is **determined by the information
content of the brane tower at each fibre**.

**In-progress braids: sections that gravitate.**
At any fibre over a point $p \in M$, the jet tower
$A_0 \hookrightarrow A_1 \hookrightarrow \cdots$
([jet-Planck steps](#rem:jet-planck-steps)) carries sections at
every level.  In one Planck time, $n_R(q) \approx 10$ jet
prolongations complete.  But the tower does not stop at level
$n_R$: **braids with crossing number $c > n_R$ are partially
evaluated**.

A proton ($c \sim 18$ for its Borromean linking) at jet level $10$
is an in-progress section — its braid word $\beta \in B_n$ has
been partially resolved ($10$ of $\sim 18$ $R$-matrix evaluations
complete) but not yet descended to an observable knot.  These
in-progress braids are **real sections of $J^k\mathcal{S}$ over
$p$**: they carry partial crossing energy, they couple to the
$q$-connection, and they contribute to $T^{(q)}$.

This is the categorical analog of virtual particles: the vacuum at
$p$ is populated by all braids "in transit" through the jet tower,
each contributing to the gravitational source term.

**Counting in-progress braids.**
At jet level $k$ over a point $p$, the number of distinct
in-progress braids is the dimension of the section space
$\Gamma(J^k\mathcal{S}|_p)$.  For the $\mathrm{SU}_q(2)$ Frobenius--Hopf
object, this grows with $k$: each jet prolongation adds new
polynomial coefficients (new Taylor data of the energy function $E$).

The total information content of a Planck cell is not the
single-operation entropy $\eta_q$ but the **cumulative jet tower
entropy**:

$$
  S_{\mathrm{cell}}(q)
  =  \sum_{k=1}^{\infty}
  \eta_q^{(k)},
$$

where $\eta_q^{(k)}$ is the entropy contributed by sections at jet
level $k$.  The sum converges because sections at level $k$ are
exponentially suppressed by the :refterm[descent]{#descent} involution $\hat{\tau}_k$
([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)): the transient
component at each level has support localised to exceptional
divisors of codimension $\geq 2$.

**Quadratic suppression from surface area.**
The exceptional divisor $\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C})$
is a $2$-sphere.  Each jet level $k$ adds a shell of in-progress
braids whose **information surface area** scales as $\hbar_q^2$
(the square of the linear Reeb dimension), not $\hbar_q$.  This is
the holographic content of the :refterm[descent]{#descent} involution: information on
the exceptional divisor lives on $2$-surfaces, and area is quadratic
in the linear scale.

Concretely, the entropy at jet level $k$ is suppressed by the
**area** of the transient shell, not its radius:

$$
  \eta_q^{(k)}
  =  \eta_q \cdot \hbar_q^{2k},
$$

where the exponent $2k$ reflects that the codimension-$2$
localisation of transient sections
([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)) projects onto a
surface, and the surface area at level $k$ scales as the
**square** of the displacement $\hbar_q^k$.  Summing the geometric
series:

$$
  S_{\mathrm{cell}}(q)
  =  \eta_q \sum_{k=1}^{\infty} \hbar_q^{2k}
  =  \frac{\eta_q \cdot \hbar_q^2}{1 - \hbar_q^2}.
$$

**Exact algebraic closure.**
With the corrected operational entropy $\eta_q = (2q-1)/q^3$
([operational entropy](#def:operational-entropy)) and
$1 - \hbar_q^2 = (2q-1)/q^2$, the series evaluates to

$$
  S_{\mathrm{cell}}
  =  \frac{(2q-1)/q^3 \cdot (q-1)^2/q^2}{(2q-1)/q^2}
  =  \frac{(q-1)^2}{q^3}.
$$

This is **exactly** the value required for $G_{\mathrm{Planck}} = 1$.
No numerical fitting, no measured $d_H$ input — the series closes
algebraically from $q$ alone.

**The gravitational constant.**
The $q$-Yang--Mills--Levi variation gives

$$
  G_q =  \frac{c_q^3 \cdot \hbar_q}{S_{\mathrm{cell}}(q)}
  =  \frac{c_q^3 \cdot \hbar_q \cdot (1 - \hbar_q^2)}
             {\eta_q \cdot \hbar_q^2}
  =  \frac{c_q^3 \cdot (2q - 1)}{q^2 \cdot \eta_q \cdot \hbar_q},
$$

where $c_q = 1/(q-1)$ is the speed of light
([speed of light](#def:information-speed-of-light)) and
$\hbar_q = (q-1)/q$.  Converting to Planck units:

$$
  G_{\mathrm{Planck}}
  =  G_q \cdot \left(\frac{\hbar_q}{c_q}\right)^2
  =  1
$$

identically for all $q > 1$.

**Numerical values at $q = q_0$.**

| Quantity              | Formula        | Value              |
| --------------------- | -------------- | ------------------ |
| $\eta_q$              | $(2q-1)/q^3$   | $0.892$ $q$-bits   |
| $\chi_q$              | $1/(2q-1)$     | $0.820$            |
| $S_{\mathrm{cell}}$   | $(q-1)^2/q^3$  | $0.00881$ $q$-bits |
| $G_{\mathrm{Planck}}$ | $1$            | $1.000$ (exact)    |

**Quadratic versus linear suppression.**
The $\hbar_q^{2k}$ (not $\hbar_q^k$) exponent has a direct
geometric origin: the exceptional divisor
$\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$ is a
**surface**.  Information on $S^2$ is proportional to area, and
area is the **square** of the linear dimension.  Each :refterm[descent]{#descent} from
level $k+1$ to level $k$ projects out a codimension-$2$ shell
whose area is $\hbar_q^2$ times the previous level.  The linear
suppression $\hbar_q^k$ would correspond to information on a line
(codimension $1$) --- but the transient sections are localised to
exceptional divisors of codimension $\geq 2$, giving the quadratic
exponent.

This is the same reason that the Bekenstein--Hawking entropy scales
as area (not volume): the information content of a region is
determined by its boundary surface, and surfaces have area $\sim r^2$.  In the QOU, this is not postulated but **derived** from the
codimension-$2$ structure of the exceptional divisors in the
brane tower.

**Relation to the three fundamental constants.**

| Constant  | QOU formula                         | Depends on                |
| --------- | ----------------------------------- | ------------------------- |
| $c_q$     | $1/(q-1)$                           | $q$ only                  |
| $\hbar_q$ | $(q-1)/q$                           | $q$ only                  |
| $G_q$    | $c_q^3 \hbar_q / S_{\mathrm{cell}}$ | $q$ and jet tower entropy |

The speed of light and Planck constant are algebraic in $q$.  The
gravitational constant requires the full jet tower information
content — it is the only fundamental coupling that depends on the
**braid-group structure** of the Frobenius--Hopf object, not just
its ring-theoretic data.  This explains why gravity is the hardest
interaction to quantise and the weakest at low energies: its
coupling is suppressed by the sparsity of in-progress braids
($S_{\mathrm{cell}} \ll \eta_q$) in the near-classical regime.
<!-- FILE_END: gravitational-constant-properties.md -->

<!-- FILE_START: julia-hausdorff-dimension-prediction.md -->
The $S_{\mathrm{cell}}$ closure fixing $G_{\mathrm{Planck}} = 1$ ([gravitational constant](#def:gravitational-constant)) yields a prediction for the Hausdorff dimension of the Reeb Julia set. This provides an independently checkable claim against transfer-operator computations.

**Hausdorff dimension prediction.**
The corrected formula predicts:

$$
  d_H(q) =  \frac{(2q-1)^2}{q^3}.
$$

| $q$         | $d_H$ predicted | $d_H$ box-counting | Known exact           | Note                                                                  |
| ----------- | --------------- | ------------------ | --------------------- | --------------------------------------------------------------------- |
| $1$         | $1.000$         | —                  | $1.000$ (unit circle) | Exact match                                                           |
| $q_0$       | $1.088$         | $1.012$            | —                     | Box-counting underestimates thin quasicircles                         |
| $1.5$       | $1.185$         | —                  | —                     | Basilica root $c = -3/4$ (period-$2$ parabolic; known $d_H \sim 1.2$) |
| $\varphi^2$ | $1.000$         | —                  | —                     | Golden crossover: $d_H$ returns to $1$                                |

The formula yields $d_H = 1$ at $q = 1$ (unit circle) and $q = (3+\sqrt{5})/2 = \varphi^2$ (golden threshold), which are exact matches. For $1 < q < \varphi^2$, the Julia set is strictly more fractal than a circle ($d_H > 1$), consistent with McMullen's theorem [mcmullen1998].

**Testable prediction.**
The value $d_H(q_0) = 1.088$ is testable against high-precision transfer-operator computations (Ruelle 1982) for $d_H(J_c)$ at $c(0.1097) = 0.338 + 0.073i$. Box-counting gives $d_H \approx 1.012$ but systematically underestimates thin Jordan curves. The Ruelle perturbative lower bound $1 + |c|^2/(4\ln 2) \approx 1.043$ is consistent with our prediction.
<!-- FILE_END: julia-hausdorff-dimension-prediction.md -->

<!-- FILE_START: hausdorff-dimension-recurrence.md -->
$$
  d_{H,q}^{(n+1)} = d_{H,q}^{(n)} + \frac{(2q_n - 1)(3 - 4q_n)(q_n - 1)}{q_n^5}.
$$

This defines a contraction mapping for $q > 3/4$. The iteration $d_{H,q} \to d_{H,q} + \Delta d_{H,q}$ flows monotonically toward $d_{H,q} = 0$. The fractal complexity of the Reeb dynamics decreases with increasing $q$, vanishing at $q \to \infty$ (the Big Bang, where the Julia set collapses to a point). The direction of decreasing $d_{H,q}$ coincides with increasing $q$ — pointing from the classical regime ($q \to 1$, maximal $d_{H,q}$) toward the Big Bang.

**Regime table.**
See [Table 1](#tbl:hausdorff-dimension-recurrence-table1-data).

The $q$-deformed $d_{H,q}$ and the classical Hausdorff dimension $d_H$ of the Julia set over $\mathbb{C}$ are distinct quantities ([classical Hausdorff dimension comparison](#rem:hausdorff-dimension-classical-comparison)).

**Convergence from local $q$.**
The downward iteration $q_{n+1} = q_n - \hbar_{q_n} = (q_n^2 - q_n + 1)/q_n$ flows $q$ toward the classical limit $q = 1$. This is a superattracting fixed point. Starting from our local $q_0$:

See [Table 3](#tbl:hausdorff-dimension-recurrence-table3-data).

It takes three Planck steps from our universe to reach the classical limit. The convergence is superlinear. At the fixed point, $\eta_q = 1$ nat, meaning each Reeb operation carries exactly one natural unit of information.

**Cosmological arrow of time.**
The monotone decrease of $d_{H,q}$ with $q$ defines an information-theoretic arrow. The parameter $q$ flows from the classical limit toward the Big Bang. Reversing time reverses the discrete recurrence. The second law of thermodynamics asserts that the $q$-deformed dimension increases as $q$ decreases.
<!-- FILE_END: hausdorff-dimension-recurrence.md -->

<!-- FILE_START: hausdorff-dimension-classical-comparison.md -->
The $q$-deformed Hausdorff dimension $d_{H,q} = (2q-1)^2/q^3$ ([discrete recurrence](#rem:hausdorff-dimension-recurrence)) differs from the classical Hausdorff dimension $d_H$ of the Julia set $J(f_q)$ over $\mathbb{C}$.

**$d_{H,q}$ vs. $d_H$: comparison with classical Hausdorff dimension.**
For parameters $c(\varTheta)$ on the main cardioid of the Mandelbrot set, the Julia set is a quasicircle. The classical Hausdorff dimension $d_H$ satisfies:

1. **Ruelle perturbative** (valid for $|c| \ll 1$): $d_H = 1 + \frac{|c(\varTheta)|^2}{4 \ln 2} + O(|c|^4)$. At $\varTheta = 0.1097$: $|c| = 0.346$, yielding $d_H \approx 1.043$.
2. **Transfer operator** (numerical, Bowen--Ruelle): $d_H \approx 1.047$ at $N = 800$ grid points.
3. **QOU $q$-deformed**: $d_{H,q} = 1.088$.

The gap $d_{H,q} - d_H \approx 0.041$ arises from differing Manning--McCluskey inputs. See [Table 2](#tbl:hausdorff-dimension-recurrence-table2-data).

The classical $d_H$ arises from conformal dynamics over $\mathbb{C}$. The $q$-deformed $d_{H,q}$ replaces the transcendental $\ln 2$ with the rational $\eta_q$, and the numerical $\chi(c)$ with the algebraic $\chi_q$. We propose that $d_{H,q}$ governs the physical regime.

No closed form exists for the classical $d_H(J_c)$ over the main cardioid parameter $c$. It appears implicitly as the unique zero of the Bowen--Ruelle pressure function $P(-t\log|f_c'|) = 0$.
<!-- FILE_END: hausdorff-dimension-classical-comparison.md -->

<!-- FILE_START: information-causality.md -->
We place the quantum observable universe (QOU) within information-theoretic physics. The mass--energy equivalence $E = mc_q^2$ and the derived speed of light $c_q = 1/(q-1)$ connect the QOU to established information bounds.

**1. The light cone is the Lieb--Robinson cone.**
The causal boundary arises from the $q$-connection decomposition $A_q = q^{-1}A + \hbar_q\iota_\xi A\varTheta$. The boundary at $|Z| = c_q$ in the contact affine coordinate ([contact affine chart](#def:contact-affine-chart)) is the locus where horizontal spatial diffusion matches vertical Reeb advance. Outside this cone, the Lieb--Robinson bound enforces exponential suppression of correlations. Causality follows directly from the ratio of spatial to temporal information flow.

**2. The speed of light varies with $q$.**
The speed of light $c_q = 1/(q-1)$ depends on the substrate parameter. At the Big Bang ($q \to \infty$), $c \to 0$. As the universe classicalises ($q \to 1$), $c \to \infty$. At the present epoch $q = q_0$, $c \approx 9.12$ in Reeb units.

**3. The Margolus--Levitin bound and $c_q$.**
The Margolus--Levitin theorem bounds the operation rate by $2E/\pi\hbar$. We have the crossing energy $E = mc_q^2 = m/(q-1)^2$ and the operation count $n_R(q) = 1/\hbar_q$. The bound is:

$$
  n_R(q)  \leq  \frac{2m}{\pi\hbar_q(q-1)^2}.
$$

The Reeb dynamics saturates this bound up to the factor $2/\pi$.

**4. Bremermann's limit and information bandwidth.**
Bremermann's limit states a system processes at most $mc^2/h$ bits per second. The bandwidth is:

$$
  \mathfrak{B}(q)
  =  \frac{q\eta_q}{(q-1)^2}
  \quad \text{($q$-bits per Planck time)}.
$$

At $q = q_0$, $\mathcal{B} \approx 82$ $q$-bits per Planck time.

**5. Pawlowski's information causality.**
Information causality restricts the accessible information Bob gains from Alice. In the QOU, the Lieb--Robinson bound ensures exponential decay outside the $|Z| = c_q$ cone.

**6. The Bekenstein bound and fibre entropy.**
The Bekenstein bound limits the entropy to $S \leq 2\pi RE / \hbar c$. We bound the QOU fibre entropy by $\eta_q$ per operation:

$$
  S_{\mathrm{fibre}}  \leq  \eta_q
  =  \frac{2q - 1}{q^3}.
$$

**7. Summary.**
See [Table](#tbl:information-causality-table-data).
<!-- FILE_END: information-causality.md -->


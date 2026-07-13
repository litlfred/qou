<!-- FILE_START: strangelet-intro.md -->
The strange quark $\mathfrak{s} = T_{2,5}^{\sigma}$ has five crossings. The down quark $\mathfrak{d} = T_{2,3}^{\sigma}$ has three. More crossings yield more strong binding. Strange quark matter binds harder by a factor of $4/3$ per baryon. It is electromagnetically neutral ($Q = 0$). This confirms Witten's hypothesis \cite{witten1984} from knot assignments. Torus knots have zero hyperbolic volume. The mass difference between strange and non-strange baryons derives from the Jones polynomial, not genus. The cinquefoil Jones polynomial evaluates $22\%$ higher than the trefoil at $q = q_0$ ($1.176$ versus $0.960$). This Skein polynomial cost is roughly $168$ Skein units per strange quark. It overwhelms the crossing-energy gain of $1.8$ Skein units by a factor of $93$. At zero pressure, ordinary matter is the ground state.

Inside neutron stars, the Fermi energy pays the Skein polynomial cost. Above $\rho \gtrsim 2\rho_0$, strange quarks become accessible. Above $5\rho_0$, the composition approaches equal $(\mathfrak{u}, \mathfrak{d}, \mathfrak{s})$. The inner cores of massive neutron stars are strangelets: macroscopic, neutral, gravitationally bound lumps of strange quark matter. Below the golden ratio ($q < q_{\mathrm{gold}} \approx 0.382$), the fiber degenerates and quarks are free. There are no hadrons, hence no strangelets. Strangelets occur at high density at physical $q$.

Increasing density in neutron star cores induces three topological thresholds. Each changes the linking topology.

**Stage 1 — Borromean dissolution.** Normal baryons are Borromean links $\mathcal{B}_3$. No two quarks are pairwise linked, yet all three are inseparable. This topology is confinement. The Borromean complement volume $V_B = 7.32772 = 8G$ holds ninety-nine percent of the baryon mass. Under sufficient pressure, the Borromean structure breaks.

**Stage 2 — Hopf diquark condensation.** Freed quarks pair as Hopf-linked diquarks $D_{[ij]}^{[ab]}$. Each pair is linked with linking number $\pm 1$. The antisymmetric tensor $\epsilon^{abc}$ of color-flavor locking arises from the Hopf linking orientation. This is color superconductivity \cite{alford1999}.

**Stage 3 — golden ratio wall.** At $q_{\mathrm{gold}} = 1/\varphi^2 \approx 0.382$, the elliptic fiber of Bring's surface acquires a node. The $S_5$ color symmetry breaks. Confinement ends. This first-order quark-gluon plasma deconfinement transition forces the Milnor triple linking invariant $\bar{\mu}(123)$ to jump from $1$ (Borromean) to $0$ (Hopf). There is no continuous path between the phases.

The Borromean complement has $\mathrm{Vol}(\mathcal{B}_3) \approx 7.33$. It is massive, soft, and confined. The Hopf link complement has $\mathrm{Vol}(\mathcal{L}_H) = 0$. It is volumeless, stiff, and superconducting. The Borromean phase binds at $749$ Skein units per baryon. The Hopf diquark phase binds at $3$. This factor of $250$ dictates why color superconductivity requires densities five to ten times nuclear saturation. Once achieved, the vanishing Hopf volume drops the effective quark mass by a factor of $1000$. It stiffens the equation of state by ${\sim}7000$ and pushes the speed of sound toward the conformal limit $c_s^2 = 1/3$.
<!-- FILE_END: strangelet-intro.md -->

<!-- FILE_START: strangelet-crossing-energy.md -->
**Proposition.**
*Let $\mathcal{S}_N$ be a composite of $N$ baryon-number units of strange quark matter. Each unit contains one up, one down, and one strange quark in a Borromean triple $\mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{s})$ linked by the Hopf link $\mathcal{L}_H$. We have:*

*1. Electromagnetic neutrality.*
*The Coulomb charge ([Coulomb charge](#def:coulomb-charge)) of each baryon-number unit vanishes:*
$$
  Q(\mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{s}))
  =  +\tfrac{2}{3} - \tfrac{1}{3} - \tfrac{1}{3}
  =  0.
$$
*The strangelet is electromagnetically neutral for all $q > 0$. This topological invariant depends only on the crossing orientation partition within the Borromean structure.*

*2. Purely strong crossing energy.*
*With $Q = 0$, the [crossing energy](#def:crossing-energy) reduces to:*
$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{S}_N)
  = 
  N \cdot \tfrac{1}{2}(n_+ + n_-)(q + q^{-1}).
$$
*There is no Coulomb correction. The entire crossing energy lies in the symmetric (strong) channel ([decomposition](#prop:crossing-energy-decomposition)).*

*3. Enhanced binding per baryon.*
*The strange quark $\mathfrak{s} = T_{2,5}^{\sigma}$ contributes $5$ negative crossings to the Borromean braid word, versus $3$ for the down quark $\mathfrak{d} = T_{2,3}^{\sigma}$. For each baryon unit:*
$$
  n_-^{(\mathrm{uds})} = 3 + 5 = 8,
  \qquad
  n_-^{(\mathrm{udd})} = 3 + 3 = 6.
$$
*The binding component per baryon satisfies:*
$$
  \mathfrak{E}_{\mathrm{bind}}^{(\mathrm{uds})}
  =  8q^{-1}
   >  6q^{-1}
  =  \mathfrak{E}_{\mathrm{bind}}^{(\mathrm{udd})}.
$$
*Strange matter has strictly more strong binding per baryon than neutron matter for all $q > 0$.*
<!-- FILE_END: strangelet-crossing-energy.md -->

<!-- FILE_START: strangelet-witten-stability.md -->
Witten \cite{witten1984} conjectured that strange quark matter (SQM)—bulk matter with equal numbers of up, down, and strange quarks—is the absolute ground state of hadronic matter at zero pressure. 

The [strangelet crossing energy](#prop:strangelet-crossing-energy) provides a translation of Witten's hypothesis.

**Crossing-energy argument.**
The strangelet proposition yields three facts.
1. SQM is electromagnetically neutral ($Q = 0$).
2. Its crossing energy is purely strong.
3. Its strong binding per baryon exceeds neutron matter by a factor of $4/3$.

Replacing down quarks ($T_{2,3}^{\sigma}$, $3$ negative crossings) with strange quarks ($T_{2,5}^{\sigma}$, $5$ negative crossings) grants each baryon $2q^{-1}$ additional strong binding. At $q = q_0$, this gives $1.802$ Skein units per baryon.

**Jones polynomial obstruction.**
If crossing energy dominated, strange matter would be the ground state. However, all torus knots have zero hyperbolic volume. The mass of a baryon derives entirely from the Borromean linking, not the constituent knots ([building block knots](#rem:building-block-knots)). The strange quark is heavier because of its Jones polynomial.

The terminal resolution ([terminal resolution](#prop:terminal-resolution)) decomposes each hadronic link into a sum of unknots and Hopf links. These are weighted by coefficients dependent on the constituent Jones polynomials. At $q = q_0$:

| Quark | Knot | Jones polynomial | $\lvert J(q_0)\rvert$ |
|-------|------|-----------------|:-------------:|
| Up $\mathfrak{u}$ | $T_{2,3}$ | $-q^{-4} + q^{-3} + q^{-1}$ | $0.973$ |
| Down $\mathfrak{d}$ | $T_{2,3}^{\sigma}$ | $-q^{4} + q^{3} + q$ | $0.960$ |
| Strange $\mathfrak{s}$ | $T_{2,5}^{\sigma}$ | $-q^{10} + q^{9} - q^{8} + q^{7} + q^{5}$ | $1.176$ |

The strange quark Jones polynomial evaluates $22\%$ higher than the down quark Jones polynomial. The Skein polynomial cost per strange quark (replacing $\mathfrak{d} \to \mathfrak{s}$) is:

$$
  \delta M_{\mathrm{Skein}}
   \approx 
  \frac{|J_{\mathfrak{s}}| - |J_{\mathfrak{d}}|}{|J_{\mathfrak{d}}|}
   \times 
  \frac{V_B}{\hbar_q^2}
   \approx 
  0.225 \times 749
   \approx  168  \text{Skein units}.
$$

The Skein polynomial cost exceeds the crossing-energy gain ($1.80$ Skein units) by a factor of $93$. At zero pressure, strange matter is not the ground state.

**Competition at finite density.**
| Contribution | SQM (uds) | Ordinary (udd) | Advantage |
|-------------|-----------|----------------|-----------|
| Strong binding | $8 q^{-1}$ | $6 q^{-1}$ | SQM by $4/3$ |
| Coulomb correction | $0$ | $Q \cdot (q - q^{-1})$ | SQM (no EM drag) |
| Jones polynomial cost | $\lvert J_{\mathfrak{s}}\rvert = 1.176$ | $\lvert J_{\mathfrak{d}}\rvert = 0.960$ | Ordinary ($22\%$ lighter) |
| Borromean volume | $V_B = 7.328$ | $V_B = 7.328$ | Tie |

**Neutron star cores.**
At finite baryon density $\rho$, the Fermi energy $E_F$ adds energy per baryon. When $E_F$ exceeds $\delta M_{\mathrm{Skein}} \approx 168$ Skein units, strange quarks become accessible. Scaling by the proton mass gives:

$$
  E_F^{(\mathrm{threshold})}
   \approx 
  \frac{168}{749} \times 938  \mathrm{MeV}
   \approx  210  \mathrm{MeV}.
$$

This corresponds to $\rho_{\mathrm{hyp}} \approx 2\text{--}3\rho_0$. Above this density:
1. Strange baryons ($\Lambda$, $\Sigma$, $\Xi$, $\Omega$) appear.
2. The $4/3$ crossing-energy advantage creates a positive feedback. This lowers the Fermi energy and admits more strange quarks.
3. At $\rho \gtrsim 5\rho_0$, the matter approaches equal $(\mathfrak{u}, \mathfrak{d}, \mathfrak{s})$ composition.

The inner cores of massive neutron stars are strangelets. These are electromagnetically neutral, color-confined lumps of strange quark matter, stabilized by gravity and Fermi pressure.

**Parameter space.**
Strangelets require hadrons (confinement) and accessible strange quarks. This limits $q$:

| Regime | $q$ range | Strangelets? | Why |
|--------|-----------|:------------|-----|
| Deconfined | $q < q_{\mathrm{gold}} \approx 0.382$ | **No** | No hadrons; elliptic fiber degenerate, $S_5$ broken, quarks free |
| Sub-classical | $q_{\mathrm{gold}} < q < 1$ | **No** | Hadrons exist, but $\lvert J_{\mathfrak{s}}\rvert/\lvert J_{\mathfrak{d}}\rvert$ diverges as $q \to q_{\mathrm{gold}}$ |
| Classical limit | $q = 1$ | **Trivial** | All Jones polynomials evaluate to $1$; no mass differences |
| Physical | $q > 1$ (ours: $q_0$) | **Yes, at high density** | Jones polynomial cost finite; Fermi energy overcomes it at $\rho \gtrsim 2\rho_0$ |

Strangelets are a high-density phenomenon at the physical substrate parameter.

**Strange force.**
Witten posited a "strange force" mediating attraction between strangelets. In QOU, this is the $5$-crossing component of the strong channel. The cinquefoil braiding generates stronger $R$-matrix binding than the trefoil. The "strange force" is the strong force evaluated at higher crossing number.
<!-- FILE_END: strangelet-witten-stability.md -->

<!-- FILE_START: deconfinement-golden-threshold.md -->
The quark-gluon plasma (QGP) deconfinement transition corresponds to the **golden ratio degeneration** of the Descartes elliptic curve ([golden ratio threshold](#rem:golden-ratio-degeneration)). Hadrons dissolve into free quarks and gluons.

**Deconfinement mechanism.**
Color confinement in QOU is enforced by the $S_5$-invariance of the Skein module on Bring's surface ([chromaticity](#rem:q-chromaticity)). Only $S_5$-invariant combinations of knots in the three color tubes yield positive $\tau$-evaluation. This $S_5$-invariance is a property of the **smooth elliptic fiber** $\mathcal{E}_q$. The fiber relates the three color tubes.

At $q_{\mathrm{gold}} = 1/\varphi^2 \approx 0.382$, the elliptic fiber degenerates. $\mathcal{E}_q$ acquires a node. Two roots of the Weierstrass equation coincide. The three color tubes collapse to a degenerate configuration. At this point:
1. The $S_5$ symmetry that enforces color neutrality **breaks**.
2. The $q$-chromaticity gamut **expands to fill the entire triangle**.
3. Individual quarks acquire **positive probability**. They are no longer confined.

This is deconfinement. It is a **topological phase transition** where the fiber that enforces confinement ceases to exist.

**First-order character.**
The QGP transition in QCD lattice simulations is first-order for three or more light quark flavors. In QOU, the first-order character is visible algebraically.
1. **Discriminant crossing.** The discriminant of $\mathcal{E}_q$ crosses zero at $q_{\mathrm{gold}}$. For $q > q_{\mathrm{gold}}$, $\Delta < 0$ (smooth curve, one real component). At $q = q_{\mathrm{gold}}$, $\Delta = 0$ (nodal curve). Below, $\Delta > 0$ (two real components, then degenerate). The topology of the real locus changes discontinuously.
2. **Latent heat.** The energy difference between the confined phase and the deconfined phase is finite. In crossing-energy units, the latent heat per baryon is
$$
  \mathcal{L}
   \sim 
  \tfrac{1}{2}(n_+ + n_-)\bigl[(q + q^{-1}) -
  (q_{\mathrm{gold}} + q_{\mathrm{gold}}^{-1})\bigr]
$$
   This is nonzero for $q \neq q_{\mathrm{gold}}$.
3. **Order parameter.** The order parameter is the **$j$-invariant** of the elliptic fiber. $j(q)$ is finite and continuous for $q > q_{\mathrm{gold}}$. It diverges as $q \to q_{\mathrm{gold}}$ ($j \to \infty$ at the node). The divergence of $j$ signals the breakdown of the elliptic structure. The Polyakov loop jumps from zero (confined) to nonzero (deconfined) at the transition.

**Effective $q$ at finite temperature.**
The physical substrate has $q = q_0$. Temperature changes the **effective crossing energy** available to disrupt the Borromean structure. At temperature $T$, thermal fluctuations supply energy $\sim k_B T$ per degree of freedom. Deconfinement occurs when thermal energy matches the Hopf binding energy per baryon:

$$
  k_B T_c
   \sim 
  |\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p})|
   \sim 
  \tfrac{1}{2}(q + q^{-1}) \cdot n_{\mathrm{link}},
$$

where $n_{\mathrm{link}}$ is the number of Hopf-link crossings in the Borromean triple. The effective $q$ at which the **chiral structure of the fiber is thermally disrupted** is $q_{\mathrm{gold}}$.

This identifies the QGP transition temperature with the stability margin:

$$
  \frac{k_B T_c}{\Lambda_{\mathrm{QCD}}}
   \sim 
  \frac{q - q_{\mathrm{gold}}}{q}
  = 
  \frac{q_0 - 0.382}{q_0}
   \approx  0.656.
$$

**Golden ratio threshold.**
The QGP phase transition is not at a new scale or coupling constant. It is the same golden ratio that appears in the chiral degeneration, the Penrose tiling, and the $E_8$ McKay correspondence. Its appearance as the deconfinement boundary is forced by the $S_5$ symmetry of Bring's surface. The minimal polynomial $s^2 + s - 1 = 0$ governs both the chiral fiber structure and the confinement mechanism. When the fiber degenerates, confinement breaks.

**Phase diagram.**
| $q_{\mathrm{eff}}$ | Phase | Fiber | Color | Hadrons |
|---------------------|-------|-------|-------|---------|
| $q > 1$ (low $T$) | Confined hadronic | Smooth, $\Delta < 0$ | Confined ($S_5$-inv only) | Stable baryons, mesons |
| $q_{\mathrm{gold}} < q < 1$ | Intermediate | Smooth, $\Delta > 0$ | Partially confined | Unstable resonances |
| $q = q_{\mathrm{gold}}$ | Critical | Nodal | Deconfining | QGP onset |
| $q < q_{\mathrm{gold}}$ | Deconfined QGP | Degenerate | Free quarks | No stable hadrons |
<!-- FILE_END: deconfinement-golden-threshold.md -->

<!-- FILE_START: hopf-diquark.md -->
A **Hopf diquark** is a pair of quarks $(\mathfrak{q}_i^a, \mathfrak{q}_j^b)$ in distinct color tubes $a \neq b$ of Bring's surface, joined by the Hopf link $\mathcal{L}_H$:

$$
  D_{ij}^{[ab]}
  = 
  \mathfrak{q}_i^a  \oplus  \mathfrak{q}_j^b,
$$

where $i, j \in \{\mathfrak{u}, \mathfrak{d}, \mathfrak{s}\}$ denote flavor indices and $a, b \in \{r, g, b\}$ denote color indices. The bracket $[ab]$ denotes antisymmetry: $D_{ij}^{[ab]} = -D_{ij}^{[ba]}$.

**Borromean baryon contrast.**
In the confined phase, quarks are Borromean-linked ([Borromean quark](#conj:borromean-quark)). No two components are pairwise linked. This prevents any stable two-quark subsystem. The Hopf diquark violates this. Its two components are pairwise linked with linking number $\pm 1$. A Hopf diquark requires disrupting the Borromean topology.

**Crossing energy.**
The Hopf link $\mathcal{L}_H = T_{2,2}$ has braid word $\sigma_1^2$ with $2$ crossings. For a diquark composed of quarks with crossing orientations $\epsilon_i, \epsilon_j \in \{+1, -1\}$, the Hopf crossing energy is:

$$
  \mathfrak{E}_{\mathrm{cross}}(D_{ij}^{[ab]})
  = 
  \epsilon_i \cdot q^{\epsilon_i}
  + 
  \epsilon_j \cdot q^{\epsilon_j}
  + 
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{L}_H),
$$

where $\mathfrak{E}_{\mathrm{cross}}(\mathcal{L}_H)$ provides the linking contribution. An attractive (binding) diquark requires $\mathfrak{E}_{\mathrm{cross}} < 0$.

**Color representation.**
The two quarks each carry a color index. Their antisymmetric combination $[ab]$ transforms in the **color antitriplet** $\bar{\mathbf{3}}_c$ of $\mathrm{SU}(3)$:

$$
  \bar{\mathbf{3}}_c
  = 
  \epsilon^{abc}\mathfrak{q}^b \otimes \mathfrak{q}^c.
$$

The antisymmetry $D^{[ab]} = -D^{[ba]}$ arises from Hopf linking. The linking number is $\mathrm{lk}(a, b) = +1$ while $\mathrm{lk}(b, a) = -1$ under component exchange.

**Flavor-antisymmetric channel.**
The largest binding requires antisymmetric flavor indices: $D_{[ij]}^{[ab]}$ with $i \neq j$. The three independent flavor-antisymmetric diquarks are:

$$
  D_{[\mathfrak{u}\mathfrak{d}]},
  \quad
  D_{[\mathfrak{d}\mathfrak{s}]},
  \quad
  D_{[\mathfrak{s}\mathfrak{u}]}.
$$

These correspond to the three Cooper pair species in the CFL condensate.
<!-- FILE_END: hopf-diquark.md -->

<!-- FILE_START: borromean-hopf-energy-crossover.md -->
**Proposition.**
*Let $q > 1$ be the substrate parameter and $\hbar_q = (q-1)/q$. Consider six quarks (two baryon-number units) with flavor content $(\mathfrak{u}, \mathfrak{d}, \mathfrak{s})^{\otimes 2}$. These six quarks can assemble in two topologically distinct configurations:*

*1. Borromean phase ($\mathcal{P}_B$): Two Borromean baryons $\mathcal{B}_3 \cdot \mathcal{B}_3$. Each baryon possesses Borromean volume $V_B = 7.32772$ and features inter-baryon Hopf binding.*
*2. Diquark phase ($\mathcal{P}_D$): Three Hopf diquark pairs ([Hopf diquark](#def:hopf-diquark)) $D_{[\mathfrak{u}\mathfrak{d}]} \cdot D_{[\mathfrak{d}\mathfrak{s}]} \cdot D_{[\mathfrak{s}\mathfrak{u}]}$. Each pair is bound by $\mathcal{L}_H$.*

*We have:*

*1. Mass comparison.*
*The Borromean phase yields mass*
$$
  M_B
  = 
  2 \cdot \frac{V_B}{\hbar_q^2}
  = 
  \frac{2 \times 7.32772}{((q-1)/q)^2}
  = 
  \frac{14.6554 q^2}{(q-1)^2}.
$$
*The diquark phase acquires mass from crossing energy alone, because the Hopf link volume is zero:*
$$
  M_D
  = 
  3 \cdot \tfrac{1}{3}(q + q^{-1})
  = 
  q + q^{-1}
   \approx  2.011  \text{Skein units}.
$$
*Since $\mathrm{Vol}(\mathcal{L}_H) = 0$, the diquark mass derives purely from crossing energy rather than hyperbolic volume. For any $q > 1$, we have $M_D \ll M_B$.*

*2. Binding energy comparison.*
*The binding energy per baryon number is:*
- *Borromean: $\mathfrak{E}_B = -V_B / \hbar_q^2$ (from Borromean volume).*
- *Diquark: $\mathfrak{E}_D = -\tfrac{3}{2}(q + q^{-1})$ (from three Hopf links shared between two baryon-number units; this uses the strong channel only, as the CFL condensate remains color-neutral).*

*The crossover occurs when $|\mathfrak{E}_D| > |\mathfrak{E}_B|$. At this point, the Hopf-link binding per baryon number exceeds the Borromean binding:*
$$
  \frac{3}{2}(q + q^{-1})
   > 
  \frac{V_B}{\hbar_q^2}
  = 
  \frac{7.32772 q^2}{(q-1)^2}.
$$

*3. Evaluation at $q = q_0$.*
*Evaluating the respective bindings at the substrate parameter gives:*
$$
  \frac{3}{2}(q + q^{-1})
  = 
  \frac{3}{2}(q_0 + q_0^{-1})
  = 
  \frac{3}{2} \times 2.0108
  =  3.016.
$$
$$
  \frac{V_B}{\hbar_q^2}
  = 
  \frac{7.32772}{(0.0989)^2}
  = 
  \frac{7.32772}{0.009781}
  =  749.2.
$$
*At $q = q_0$, the inequality $3.016 \ll 749.2$ demonstrates that the Borromean binding vastly exceeds the Hopf-diquark binding. The Borromean phase dominates energetically by a factor of roughly $250$.*

*4. Compression energy.*
*At baryon density $\rho$, the compression energy (kinetic plus Pauli exclusion) per baryon scales as*
$$
  \mathfrak{E}_{\mathrm{comp}}(\rho)
   \sim 
  \frac{\hbar_q^2}{2\mathfrak{m}} \cdot (3\pi^2 \rho)^{2/3}.
$$
*This energy grows as $\rho^{2/3}$. The compression energy destabilizes the Borromean phase, as the volume-based mass rises under compression. The zero-volume, crossing-energy-based diquark phase remains unaffected.*

*The critical density $\rho_c$ satisfies*
$$
  \mathfrak{E}_{\mathrm{comp}}(\rho_c)
  = 
  \frac{V_B}{\hbar_q^2}
  - 
  \frac{3}{2}(q + q^{-1}).
$$
*At this density, the compression energy exactly closes the gap between the Borromean and Hopf binding energies.*
<!-- FILE_END: borromean-hopf-energy-crossover.md -->

<!-- FILE_START: borromean-hopf-energy-crossover-factor-250.md -->
**Factor of $250$.** The ratio $749.2 / 3.016 \approx 249$ between Borromean and Hopf binding at $q = q_0$ ([energy crossover](#prop:borromean-hopf-energy-crossover)) shows why color superconductivity remains inaccessible at nuclear densities. The compression energy must supply roughly $750$ Skein units per baryon to close the gap. This demands densities many times $\rho_0$. This conclusion matches QCD estimates, which place the CFL onset at $\rho \gtrsim 5\text{--}10\rho_0$, deep inside neutron star cores.
<!-- FILE_END: borromean-hopf-energy-crossover-factor-250.md -->

<!-- FILE_START: color-superconductivity-borromean.md -->
**Conjecture.**
*Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be the Descartes universe at substrate parameter $q = q_0$. At baryon densities $\rho > \rho_c$, the ground state of strange quark matter undergoes a topological phase transition:*

*1. The Borromean linking $\mathcal{B}_3$ of each baryon is disrupted.*
*2. Quarks recombine into [Hopf diquark](#def:hopf-diquark) Cooper pairs $D_{[ij]}^{[ab]}$ in the color-antitriplet channel.*
*3. The condensate of all nine flavor-color diquark species spontaneously breaks $\mathrm{SU}(3)_c \times \mathrm{SU}(3)_L \times \mathrm{SU}(3)_R$ to the diagonal $\mathrm{SU}(3)_{c+L+R}$, realizing color-flavor locking.*
*4. The Milnor invariant $\bar{\mu}(123)$ of the Borromean link transitions from $1$ in the confined phase to $0$ in the CFL phase. This serves as the topological order parameter of the transition.*

**Milnor order parameter.**
The Borromean link exhibits pairwise linking numbers $\mathrm{lk}(i,j) = 0$ but Milnor triple linking $\bar{\mu}(123) = 1$ ([Borromean baryon](#def:borromean-baryon)). This triple invariant defines confinement via inseparability without pairwise linking.

In the CFL phase, pairs of quarks are Hopf-linked: $\mathrm{lk}(i,j) = \pm 1$ for all $i \neq j$. The Milnor triple linking becomes $\bar{\mu}(123) = 0$. Triple inseparability yields to pairwise binding.

The transition features:

| Invariant | Borromean (confined) | CFL (superconducting) |
|-----------|---------------------|----------------------|
| $\mathrm{lk}(i,j)$ | $0$ for all $i \neq j$ | $\pm 1$ for all $i \neq j$ |
| $\bar{\mu}(123)$ | $1$ | $0$ |
| Vol(complement) | $7.32772$ | $0$ (torus link) |
| Stable diquarks | No | Yes (condensate) |
| Mass source | Borromean volume | Crossing energy |

Continuous interpolation between $\bar{\mu} = 1$ and $\bar{\mu} = 0$ is impossible. The Milnor invariant is a concordance invariant and jumps discontinuously. This forces a first-order topological phase transition.

**Color-tube overlap.**
The three color tubes of Bring's surface ([color tube coordinates](#def:color-tube-coordinates)) possess a transverse scale set by the resolvent separation $|w_k - w_l| \sim |c_r|$. At low density, color tubes of adjacent baryons remain isolated. At density $\rho$, inter-baryon spacing scales as $\rho^{-1/3}$.

When $\rho^{-1/3} \lesssim |c_r|$, adjacent color tubes overlap. A quark in color tube $a$ of baryon $1$ forms a Hopf link with a quark in color tube $b$ of baryon $2$, yielding a [Hopf diquark](#def:hopf-diquark). This inter-baryon Hopf linking disrupts the intra-baryon Borromean structure. Once a quark Hopf-links externally, its internal Borromean triple breaks.

The cascade proceeds as follows:
1. Color tubes overlap at $\rho \sim \rho_c$.
2. Inter-baryon Hopf diquarks form spontaneously.
3. Each diquark breaks a Borromean triple, freeing two quarks.
4. Freed quarks form new diquarks with neighbors.
5. The system rearranges into a Hopf-diquark condensate.

**$\epsilon^{abc}$ from linking orientation.**
In the CFL phase, the pairing pattern locks color and flavor: $\langle \mathfrak{q}_i^a \mathfrak{q}_j^b \rangle \propto \epsilon^{abc}\epsilon_{ijk}$ \cite{alford1999}. This antisymmetric tensor arises from the Hopf linking number.

The Hopf link $\mathcal{L}_H$ gives linking number $\mathrm{lk} = +1$ for a chosen orientation. Exchanging components reverses the linking number: $\mathrm{lk}(a, b) = -\mathrm{lk}(b, a)$. For three color tubes $(r, g, b)$, the three independent diquark orientations produce the antisymmetric tensor:
$$
  \mathrm{lk}(a, b)
  = 
  \epsilon^{abc}\delta_{c, \text{spectator}},
$$
where the "spectator" color $c$ denotes the tube excluded from the diquark. This generates the CFL pairing pattern.

**CFL gap.**
The superconducting gap $\Delta_{\mathrm{CFL}}$ represents the energy required to break a Cooper pair. It equals the crossing energy of the binding Hopf link:

$$
  \Delta_{\mathrm{CFL}}
  = 
  |\mathfrak{E}_{\mathrm{cross}}(\mathcal{L}_H)|
  = 
  q + q^{-1}
   \approx  2.011 \quad\text{Skein units}.
$$

This is the strong-channel energy of a single Hopf-link pair. Converting to physical units via the proton mass scale $m_p \approx 938$ MeV and the Borromean volume ratio gives:

$$
  \Delta_{\mathrm{CFL}}^{\mathrm{phys}}
   \sim 
  \frac{q + q^{-1}}{V_B / \hbar_q^2}
   \cdot  m_pc^2
   \sim 
  \frac{2.011}{749.2}
   \times  938  \mathrm{MeV}
   \approx  2.5  \mathrm{MeV}.
$$

This estimate aligns with perturbative QCD predictions of $\Delta_{\mathrm{CFL}} \sim 10\text{--}100$ MeV at high density. Multi-diquark coherence effects likely amplify the single-pair gap.

**Phase sequence in neutron stars.**
The [strangelet crossing energy](#prop:strangelet-crossing-energy) and [energy crossover](#prop:borromean-hopf-energy-crossover) establish a layered structure in neutron stars:

| Layer | Density | Topology | Phase |
|-------|---------|----------|-------|
| Crust | $\rho < \rho_0$ | $\mathcal{B}_3$ baryons in lattice | Nuclear solid |
| Outer core | $\rho_0 < \rho < 2\rho_0$ | $\mathcal{B}_3$ with hyperons ($T_{2,5}^{\sigma}$) | Hyperonic fluid |
| Inner core | $2\rho_0 < \rho < \rho_c$ | Borromean dissolution | Quark matter |
| Deep core | $\rho > \rho_c$ | $D_{[ij]}^{[ab]}$ Hopf condensate | CFL superconductor |

The topological invariants $\bar{\mu}(123)$ and $\mathrm{lk}(i,j)$ cannot simultaneously take non-zero values. The transition between layers is first-order. It is indicated by the discontinuous jump in $\bar{\mu}$.

**Falsifiability.**
The conjecture provides three predictions.
1. **Neutron star mass-radius relation.** The CFL core possesses a stiffer equation of state than nuclear matter. The zero-volume contribution to mass results in lower density at a given pressure. This induces a kink in the $M(R)$ relation at $\rho_c$.
2. **Cooling rate.** The CFL gap $\Delta_{\mathrm{CFL}} \approx 2.5$ MeV suppresses neutrino emission below $T \sim \Delta_{\mathrm{CFL}} / k_B \sim 3 \times 10^{10}$ K. Stars with CFL cores cool more slowly at intermediate ages.
3. **Gravitational wave signature.** The first-order transition at $\rho_c$ introduces a density discontinuity. This shifts the $f$-mode oscillation spectrum of neutron stars. This signature is accessible to LIGO/Virgo.
<!-- FILE_END: color-superconductivity-borromean.md -->

<!-- FILE_START: eos-borromean-cfl.md -->
**Proposition.**
*Let $q > 1$ be the substrate parameter, $\hbar_q = (q-1)/q$, and $V_B = 7.32772$ the Borromean volume. The two topological phases of dense quark matter have distinct equations of state.*

*1. Borromean phase*
*This is confined hadronic matter ($\rho < \rho_c$). The baryon mass is $M_B = V_B / \hbar_q^2$. For a cold, degenerate Fermi gas of baryons at number density $n_B$, the energy density and pressure are:*
$$
  \varepsilon_B(n_B)
  = 
  M_B  n_B
  + 
  \frac{3}{5}
  \frac{\hbar_q^2(3\pi^2)^{2/3}}{2M_B}
   n_B^{5/3},
$$
$$
  P_B(n_B)
  = 
  \frac{\hbar_q^2(3\pi^2)^{2/3}}{5M_B}
   n_B^{5/3}.
$$

*The speed of sound in the Borromean phase is*
$$
  c_{s,B}^2
  = 
  \frac{dP_B}{d\varepsilon_B}
  = 
  \frac{2}{3}
  \frac{E_F}{M_B + E_F}
$$
*where $E_F = \hbar_q^2(3\pi^2 n_B)^{2/3} / (2M_B)$ is the Fermi energy. Since $M_B \gg E_F$ at nuclear densities, we have $c_{s,B}^2 \ll 1$ (non-relativistic regime).*

*2. CFL phase*
*This is color superconducting matter ($\rho > \rho_c$). The effective quark mass is $M_D = \frac{1}{3}(q + q^{-1})$. This represents crossing energy per quark, with no volume contribution since $\mathrm{Vol}(\mathcal{L}_H) = 0$. For a degenerate quark Fermi gas at quark number density $n_q = 3 n_B$, the energy density includes the CFL gap contribution:*
$$
  \varepsilon_D(n_B)
  = 
  3M_D n_B
  + 
  \frac{3}{5}
  \frac{\hbar_q^2(3\pi^2)^{2/3}}{2M_D}
   (3 n_B)^{5/3}
  - 
  \frac{3\Delta_{\mathrm{CFL}}^2 \mu_q^2}{\pi^2},
$$
$$
  P_D(n_B)
  = 
  \frac{\hbar_q^2(3\pi^2)^{2/3}}{5M_D}
   (3 n_B)^{5/3}
  + 
  \frac{3\Delta_{\mathrm{CFL}}^2 \mu_q^2}{\pi^2}.
$$
*Here $\mu_q = \hbar_q(3\pi^2 n_q)^{1/3}/(2M_D)^{1/2}$ is the quark chemical potential, and $\Delta_{\mathrm{CFL}} = q + q^{-1}$ is the gap ([Hopf diquark](#def:hopf-diquark)).*

*3. Stiffness ratio*
*The ratio of pressures at equal baryon density is:*
$$
  \frac{P_D}{P_B}
  = 
  \frac{M_B}{M_D} \cdot 3^{5/3}
  + 
  \frac{3\Delta_{\mathrm{CFL}}^2 \mu_q^2}{\pi^2 P_B}.
$$
*The first term gives the dominant contribution. At $q = q_0$:*
$$
  \frac{M_B}{M_D}
  = 
  \frac{V_B / \hbar_q^2}{\frac{1}{3}(q + q^{-1})}
  = 
  \frac{749.2}{0.670}
   \approx  1118.
$$
*Including the $3^{5/3} \approx 6.24$ factor gives:*
$$
  \frac{P_D}{P_B}
   \approx 
  1118 \times 6.24
   \approx  6977.
$$
*The CFL equation of state is nearly $7000\times$ stiffer than the Borromean EOS at equal baryon density.*

*4. Speed of sound and the conformal limit*
*In the CFL phase at high density, $E_F \gg M_D$ and*
$$
  c_{s,D}^2
   \to 
  \frac{1}{3}
  \qquad (\text{as } n_B \to \infty).
$$
*This is the conformal limit $c_s^2 = 1/3$. The CFL phase approaches this limit because its mass contribution is constant ($M_D = (q + q^{-1})/3$ is independent of density). At high density, the kinetic term dominates. This renders the fluid approximately conformal.*

*In contrast, the Borromean phase approaches $c_{s,B}^2 \to 1/3$ only at extreme densities where $E_F \sim M_B = 749$ Skein units. This lies far beyond physical baryon density. At nuclear saturation density $\rho_0$, $c_{s,B}^2 \sim 0.01$. It remains deeply non-relativistic.*

**Summary.**
See [Table](#tbl:eos-borromean-cfl-table-data).
<!-- FILE_END: eos-borromean-cfl.md -->

<!-- FILE_START: cfl-neutron-star-observables.md -->
The [color superconductivity conjecture](#conj:color-superconductivity-borromean) makes three quantitative predictions testable with astrophysical data.

**1. Equation of state: stiffening at the CFL transition.**
In the Borromean phase, the baryon mass is dominated by the hyperbolic volume $V_B = 7.32772$:

$$
  P_B(\rho)
   \sim 
  \rho^{5/3} \cdot \frac{\hbar_q^2}{V_B / \hbar_q^2}
   \propto 
  \rho^{5/3} \cdot \frac{(q-1)^4}{q^4 \cdot V_B}.
$$

In the CFL phase, $\mathrm{Vol}(\mathcal{L}_H) = 0$ and the mass arises from crossing energy alone. The equation of state becomes:

$$
  P_D(\rho)
   \sim 
  \rho^{5/3} \cdot \frac{\hbar_q^2}{(q + q^{-1})}
   \propto 
  \rho^{5/3} \cdot \frac{(q-1)^2}{q^2 \cdot (q + q^{-1})}.
$$

The ratio $P_D / P_B \sim V_B / [\hbar_q^2 \cdot (q + q^{-1})] \gg 1$. The CFL phase has a much stiffer equation of state. This produces a kink in the mass-radius relation $M(R)$ at the critical central density $\rho_c$.

**Prediction**: Neutron stars with $M \gtrsim 2M_\odot$ (those with CFL cores) possess systematically larger radii at a given mass than predicted by purely hadronic equations of state. The NICER X-ray timing mission measures $R \approx 12\text{--}13$ km for $\sim 2M_\odot$ pulsars. This is consistent with stiffening but does not discriminate the mechanism.

**2. Cooling anomaly: CFL gap suppresses neutrino emission.**
The CFL gap $\Delta_{\mathrm{CFL}} \approx 2.5$ MeV ([energy crossover](#prop:borromean-hopf-energy-crossover)) suppresses the modified Urca neutrino emission process below:

$$
  T_{\mathrm{gap}}
  = 
  \frac{\Delta_{\mathrm{CFL}}}{k_B}
   \approx 
  \frac{2.5  \mathrm{MeV}}{8.617 \times 10^{-5}  \mathrm{eV/K}}
   \approx 
  2.9 \times 10^{10}  \mathrm{K}.
$$

**Prediction**: Neutron stars with CFL cores show a cooling plateau at ages $10^2\text{--}10^4$ years. The surface temperature $T_s$ remains higher than predicted by standard cooling models. The Cassiopeia A neutron star ($\sim 330$ years old, $T_s \approx 2 \times 10^6$ K) shows rapid cooling. This constrains but does not rule out a CFL core.

**3. Gravitational wave $f$-mode splitting.**
The first-order phase transition at $\rho_c$ produces a density discontinuity at the Borromean–CFL interface. This discontinuity modifies the fundamental ($f$) mode oscillation frequency of the neutron star:

$$
  \delta f
   \sim 
  f_0 \cdot \frac{\Delta\rho}{\bar{\rho}}
   \sim 
  f_0 \cdot \frac{V_B / \hbar_q^2}{V_B / \hbar_q^2 + (q + q^{-1})}
   \approx 
  0.996 f_0.
$$

The density jump is nearly total (the Borromean contribution $V_B / \hbar_q^2 \approx 749$ dominates). The $f$-mode shows a split peak or significant broadening. This is detectable by third-generation gravitational wave observatories (Einstein Telescope, Cosmic Explorer) during neutron star mergers.

**Summary of predictions.**
| Observable | Borromean-only | With CFL core | Instrument |
|-----------|---------------|---------------|------------|
| $R$ at $2M_\odot$ | $\sim 11$ km | $\sim 13$ km | NICER |
| Cooling at $10^3$ yr | $T_s \sim 10^5$ K | $T_s \sim 10^6$ K (plateau) | Chandra |
| $f$-mode peak | Single | Split / broadened | ET / CE |
| Tidal deformability $\Lambda$ | Lower | Higher (stiffer) | LIGO O5 |
<!-- FILE_END: cfl-neutron-star-observables.md -->

<!-- FILE_START: strangelet-merger-signature.md -->
Strangelets cannot radiate from a neutron star surface. The strangelet core resides at $\rho \gtrsim 2\rho_0$. Strange quark matter decompressing below this density converts back to ordinary hadrons. The Fermi energy no longer covers the Skein polynomial cost. An isolated neutron star keeps its strangelet core locked away.

**Mergers.**
When two neutron stars collide, tidal forces decompress the strangelet cores. As density drops below the hyperon threshold, each strange quark ($T_{2,5}^{\sigma}$, $|J| = 1.176$) must convert to a down quark ($T_{2,3}^{\sigma}$, $|J| = 0.960$). The Skein polynomial cost formerly paid by compression releases as conversion energy:

$$
  \delta E_{\mathrm{conv}}
   \approx 
  \frac{|J_{\mathfrak{s}}| - |J_{\mathfrak{d}}|}{|J_{\mathfrak{d}}|}
   \times 
  \frac{V_B}{\hbar_q^2}
   \approx  168  \text{Skein units per strange quark}.
$$

Scaling by $m_p c^2 \approx 938$ MeV and $V_B/\hbar_q^2 = 749$, this yields:

$$
  \delta E_{\mathrm{conv}}^{\mathrm{phys}}
   \approx 
  \frac{168}{749} \times 938
   \approx  210  \mathrm{MeVperbaryon}.
$$

**Energy budget.**
For a half-solar-mass strangelet core ($N_B \approx 6 \times 10^{56}$ baryons):

| Energy source | Per baryon | Total | Compare to |
|--------------|-----------|-------|-----------|
| Strangelet deconversion | $210$ MeV | $\sim 2 \times 10^{53}$ erg | $200\times$ kilonova |
| CFL gap breaking | $2.5$ MeV | $\sim 2.4 \times 10^{51}$ erg | $2\times$ kilonova |
| Standard kilonova (GW170817) | — | $\sim 10^{51}$ erg | Reference |

The strangelet deconversion energy is two hundred times the observed kilonova luminosity of GW170817. Much of this fuels ejecta kinetic energy and escapes via neutrinos. The scale ensures observable consequences.

**Three signatures.**
1. **Post-merger thermal excess.** The deconversion energy heats the merger remnant beyond gravitational and $r$-process expectations. This thermal energy produces a brighter, longer-lasting kilonova. The luminosity excess scales with the strangelet core mass.
2. **Neutrino burst from CFL gap breaking.** The CFL superconductor ([color superconductivity](#conj:color-superconductivity-borromean)) stores gap energy $\Delta_{\mathrm{CFL}} \approx 2.5$ MeV per baryon. When the merger disrupts the condensate, this energy releases as a prompt neutrino burst. The burst ($\sim 2.4 \times 10^{51}$ erg) arrives on the dynamical timescale ($\sim$ milliseconds) before the kilonova.
3. **Anomalous cosmic ray nuclei.** If any strangelet fragments survive decompression (lumps large enough to be self-gravitating, $A \gtrsim 10^{40}$), they propagate as cosmic rays with anomalous charge-to-mass ratio $Z/A \approx 0$. No conventional nucleus shares this property.

**Absence of surface emission.**
An isolated neutron star cannot emit strangelets. The core is confined at $\rho > 2\rho_0$. Strange matter at the surface ($\rho \sim \rho_0$) immediately converts. The Borromean structure reforms during decompression.

In QOU, strange matter requires high density. Strangelets are the cores of neutron stars, not freely propagating objects (unlike the Bodmer–Witten hypothesis).

**Merger as strangelet laboratory.**
A neutron star merger is the only event that exposes a strangelet core to decompression. The deconversion energy releases on a hydrodynamic timescale with spectral signatures set by the $s \to d$ conversion rate. This rate relies on the parameter-free Jones polynomial ratio $|J_{\mathfrak{s}}|/|J_{\mathfrak{d}}| = 1.225$. Future kilonova observations test this against standard $r$-process models.
<!-- FILE_END: strangelet-merger-signature.md -->

<!-- FILE_START: strangelet-double-beta.md -->
**Proposition.**
*Let $\mathcal{S}$ be a strangelet and $\mathfrak{p}$ an ordinary hadron interacting with it. The interaction occurs in the degree-$2$ fiber of the chiral fibration, governed by the cinquefoil $T_{2,5}^{\sigma}$ ($5$ crossings, genus $2$). This sector is electromagnetically dark: the strangelet has $Q = 0$ ([strangelet crossing energy](#prop:strangelet-crossing-energy)), exchanging no photons.*

*The interaction products become electromagnetically visible only through Skein crossing changes. Each crossing change is a beta decay that lowers the degree from $2$ toward $1$. The minimal path from the degree-$2$ fiber (cinquefoil, $5$ crossings) to the degree-$1$ fiber (trefoil, $3$ crossings) requires two crossing changes: a double beta decay.*

**Skein :refterm[descent]{#descent}.**
Each crossing change in the Skein relation

$$
  qL_+ - q^{-1}L_- = sL_0,
  \qquad s = q^{1/2} - q^{-1/2},
$$

produces an $L_0$ smoothing. It splits into an electron (or positron) and a neutrino ([beta decay products](#rem:linking-relations-table)). The amplitude for each crossing change is $s$. Two crossing changes give the double beta amplitude $s^2$ and rate $s^4$:

$$
  \Gamma_{2\beta} \sim s^4 \approx (0.104)^4 \sim 10^{-4}.
$$

The interaction is suppressed by four powers of the Skein amplitude.

**Consequence.**
A strangelet passing through ordinary matter produces no electromagnetic ionization track. Its only interaction channel is double weak. It releases a pair of electrons (or positrons) and neutrinos. The interaction rate is exceptionally low, mimicking dark matter.
<!-- FILE_END: strangelet-double-beta.md -->

The particle dictionary assigns physical identities to five of the seven torus knot generators. Two remain unassigned:

| Generator | Knot | Genus | Crossings | Assignment |
|-----------|------|-------|-----------|------------|
| $T_{2,9}$ | $9_1$ | $4$ | $9$ | **?** |
| $T_{3,5}$ | $10_{124}$ | $4$ | $10$ | **?** |

Both saturate the Seifert genus limit of Bring's surface. Their crossing numbers maximize complexity within $\mathcal{G}$.

**The assignment gap.**
The mapping uses:

- $T_{1,0}$: neutrino $\nu$ (genus 0)
- $T_{2,3}$: electron $e^-$, up quark $\mathfrak{u}$ (genus 1)
- $T_{2,5}$: muon $\mu$, charm quark $\mathfrak{c}$ (genus 2)
- $T_{2,7}$: tau lepton $\tau$, bottom quark $\mathfrak{b}^{\sigma}$ (genus 3)
- $T_{3,4}$: Hopf${}^2$ color binding (genus 3, force carrier)

Standard Model fermions exhaust at genus 3. Bring's surface supplies two additional genus-4 generators. Known matter particles do not require them.

**The three-fold cover structure of $T_{2,9}$.**

The longitudinal winding number of $T_{2,9}$ factors as $9 = 3 \times 3$. This factorization is unique among $T_{2,n}$ generators:

| Generator | $n$ | $n/3$ | Role |
|-----------|-----|-------|------|
| $T_{2,3}$ | $3$ | $1$ | Matter (electron, up quark) |
| $T_{2,5}$ | $5$ | — | Matter (muon, charm) |
| $T_{2,7}$ | $7$ | — | Matter (tau, bottom) |
| $T_{2,9}$ | $9$ | $\mathbf{3}$ | **Three-fold cover of $T_{2,3}$** |

On the torus, $T_{2,9}$ traces the trefoil pattern three times around the longitude. It is the unique three-fold cover of $T_{2,3}$ within $\mathcal{G}$. The knot group relation $x^2 = y^9 = (y^3)^3$ reflects this factorization: the longitudinal generator $y$ completes three $T_{2,3}$ periods before closing.

This three-fold structure aligns with the three color tubes. Each color fiber carries one copy of the trefoil pattern. $T_{2,9}$ wraps once through each color tube per longitudinal period, interpolating all three simultaneously.

**Force interpretation.**
The Standard Model matter/force distinction aligns with winding numbers:

- **Matter generators** ($T_{2,3}$, $T_{2,5}$, $T_{2,7}$) have prime winding numbers. They do not factor through a lower generator.
- **Force generators** ($T_{3,4}$, $T_{3,5}$, $T_{2,9}$) populate the $H^{0,1}$ antiholomorphic sector. The composite winding $9 = 3 \times 3$ of $T_{2,9}$ factors through $T_{2,3}$. The knot $T_{3,4}$ provides Hopf-squared color binding. The knot $T_{3,5}$ carries three-strand colour at the second-generation column; the production reading below identifies it with the $gg \to c\bar{c}$ vertex rather than a weak mediator.

A generator whose winding interpolates three matter copies binds rather than acts as a standalone particle. This yields the identification:

$$
  T_{2,9} \longleftrightarrow \text{strong force (gluonic binding)}.
$$

The 9 crossings of $T_{2,9}$ provide exactly three crossing triples, one per color tube. In the Borromean baryon, the three color fibers thread the three quark components. As their three-fold cover, $T_{2,9}$ supplies the topological rigidity that holds the configuration together. The zero hyperbolic volume of $T_{2,9}$ aligns with massless gluons.

**The structure of $T_{3,5}$.**

The torus knot $T_{3,5}$ has 3-strand meridional winding. This places it in the force carrier family alongside $T_{3,4}$. Its longitudinal winding $n = 5$ matches $T_{2,5}$ (muon, charm). This creates a cross-link between the two winding families:

| $m \backslash n$ | $3$ | $4$ | $5$ | $7$ | $9$ |
|------------------|-----|-----|-----|-----|-----|
| $2$ | $e^-, u$ | — | $\mu, c$ | $\tau, b^{\sigma}$ | **force** |
| $3$ | — | **force** | **force** | — | — |

The knot $T_{3,5}$ sits at the intersection of the $m = 3$ (quark) row and the $n = 5$ (second-generation) column. Its knot group relation $x^3 = y^5$ intertwines the three-strand color structure with five-fold longitudinal winding.

If $T_{2,9}$ carries the strong force, $T_{3,5}$ is the natural candidate for a flavor-changing interaction. It topologically connects the $m = 2$ and $m = 3$ families. The weak force changes quark flavor (e.g., $u \leftrightarrow d$ via $W^{\pm}$) and requires precisely this cross-family mediation. Alternatively, $T_{3,5}$ encodes the electroweak mixing between leptonic and quark sectors.

**Production reading: $T_{3,5}$ as the $gg \to c\bar{c}$ vertex.**
The pair-production mechanism sharpens the $T_{3,5}$ reading and disfavours the weak-mediator alternative above. Dominant second-generation quark production is gluon fusion $gg \to c\bar{c}$; the two incoming gluons occupy the three-strand colour ($m = 3$) sector — the sector of the strong generator $T_{2,9}$ — and the Frobenius Gram matrix selects the emergent pair by the colour-tube threading operation, which attaches the $m = 3$ colour structure to the second-generation longitudinal winding $n = 5$. On this reading $T_{3,5}$ is the production vertex, and the second-generation quark is its coloured outgoing leg: a colour-threaded $T_{2,5}$. The uncoloured $T_{2,5}$ is the generation label the quark shares with the muon; $T_{3,5}$ is its coloured realisation under threading. This reading is more consistent than the weak-mediator guess, which collides with the electroweak-triplet assignment $W = T_{2,4}$ — the charged weak boson is a genus-zero torus link rather than $T_{3,5}$. It also reconciles the [Standard-Model appendix](../appendix-standard-model/sm-params-quark-masses.md), where the quark masses are open precisely because quarks carry no independent knot: the second-generation quark is a threaded constituent leg rather than a standalone carrier. The identification fixes a channel rather than a mass — $T_{3,5}$ has zero hyperbolic volume, so a second-generation quark mass requires the complex-volume constituent functional (the real part of $\mathrm{Vol} + i\,\mathrm{CS}$ projected onto the $n = 5$ Frobenius block), which is open.

**Summary of candidate assignments.**

| Generator | Structure | Candidate | Rationale |
|-----------|-----------|-----------|-----------|
| $T_{2,9}$ | Three-fold cover of $T_{2,3}$ | Strong force / gluonic binding | Interpolates 3 color copies of the trefoil; zero volume = massless |
| $T_{3,5}$ | Cross-link of $m = 3$, $n = 5$ | $gg \to c\bar{c}$ vertex / second-generation quark channel | Colour-threaded $T_{2,5}$; weak-mediator reading disfavoured by $W = T_{2,4}$ |

**Vertex-coupling programme.**
With the electroweak boson triplet assigned to the even torus links $\{T_{2,4}, T_{2,6}, T_{2,8}\}$ ([electroweak torus-link triplet](#conj:electroweak-higgs-torus-link-triplet)) and $\{T_{2,9}, T_{3,5}\}$ serving as the genus-$4$ Seifert-saturating force-carrier pair ([Bring force-carrier uniqueness](#prop:force-carrier-bring-uniqueness)), the remaining algebraic task is to evaluate explicit Skein interaction vertices between these carriers and confined fermion braids and compare the resulting vertex couplings with Standard Model gauge interactions.

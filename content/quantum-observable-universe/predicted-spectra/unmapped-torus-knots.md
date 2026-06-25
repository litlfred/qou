The particle dictionary
([knot formula table](#rem:knot-formula-table)) assigns physical
identities to five of the seven torus knot generators. Two generators
remain without particle assignments:

| Generator | Knot | Genus | Crossings | Assignment |
|-----------|------|-------|-----------|------------|
| $T_{2,9}$ | $9_1$ | $4$ | $9$ | **?** |
| $T_{3,5}$ | $10_{124}$ | $4$ | $10$ | **?** |

Both are **genus-$4$ saturating** generators — they exactly fill the
maximal Seifert genus allowed by the Bring's surface. Their high
crossing numbers ($9$ and $10$) place them at the top of the
complexity hierarchy within $\mathcal{G}$.

**The assignment gap.**
The current mapping uses:

- $T_{1,0}$: neutrino $\nu$ (genus $0$)
- $T_{2,3}$: electron $e^-$, up quark $\mathfrak{u}$ (genus $1$)
- $T_{2,5}$: muon $\mu$, charm quark $\mathfrak{c}$ (on divisor) (genus $2$)
- $T_{2,7}$: tau lepton $\tau$, bottom quark $\mathfrak{b}^{\sigma}$ (on divisor) (genus $3$)
- $T_{3,4}$: Hopf${}^2$ color binding (genus $3$, force carrier)

The Standard Model fermion content is exhausted at genus $3$. Yet
the Bring's surface provides two additional generators at genus $4$
that the generation scheme
([knot-particle generation](#def:knot-particle-generation)) does not
require for known matter particles.

**The three-fold cover structure of $T_{2,9}$.**

The longitudinal winding number of $T_{2,9}$ factorises as
$9 = 3 \times 3$. This is unique among the $T_{2,n}$ generators:

| Generator | $n$ | $n/3$ | Role |
|-----------|-----|-------|------|
| $T_{2,3}$ | $3$ | $1$ | Matter (electron, up quark) |
| $T_{2,5}$ | $5$ | — | Matter (muon, bottom) |
| $T_{2,7}$ | $7$ | — | Matter (tau, charm) |
| $T_{2,9}$ | $9$ | $\mathbf{3}$ | **Three-fold cover of $T_{2,3}$** |

On the torus, $T_{2,9}$ traces the trefoil pattern **three times
around the longitude** — it is the unique three-fold cover of
$T_{2,3}$ within $\mathcal{G}$. The knot group relation
$x^2 = y^9 = (y^3)^3$ reflects this factorisation: the longitudinal
generator $y$ completes three full $T_{2,3}$ periods before closing.

This three-fold structure resonates with the three color tubes
([color tube interpretation](#rem:color-tube-interpretation)). Each
color fiber carries one copy of the trefoil pattern; $T_{2,9}$
interpolates all three simultaneously, wrapping once through each
color tube per longitudinal period.

**Force interpretation.**
The matter/force distinction in the Standard Model aligns with a
winding number dichotomy:

- **Matter generators** ($T_{2,3}$, $T_{2,5}$, $T_{2,7}$)
 have winding numbers that are *prime* and do not factor through a
 lower generator.
- **Force generators** ($T_{3,4}$, $T_{3,5}$, $T_{2,9}$)
 populate the $H^{0,1}$ antiholomorphic sector
 ([cohomological embedding](#prop:cohomological-embedding)):
 $T_{2,9}$ has composite winding $9 = 3 \times 3$ that factors
 through $T_{2,3}$; $T_{3,4}$ provides Hopf-squared color
 binding; $T_{3,5}$ mediates the weak interaction.

A generator whose winding interpolates three matter copies is
accordingly a **binding agent** rather than a standalone particle.
The candidate identification is:

$$
  T_{2,9} \longleftrightarrow \text{strong force (gluonic binding)}.
$$

The $9$ crossings of $T_{2,9}$ — all of the same sign, as for any
torus knot — provide exactly three crossing triples, one per color
tube. In the Borromean baryon
([categorical proton](#def:categorical-proton)), the three quark
components (each $T_{2,3}$) are threaded through the color fibers;
$T_{2,9}$ as their three-fold cover supplies the topological rigidity
that holds the configuration together. The zero hyperbolic volume of
$T_{2,9}$ (shared by all torus knots) is consistent with gluons
being massless force carriers.

**The structure of $T_{3,5}$.**

The torus knot $T_{3,5}$ has $3$-strand meridional winding, placing it in the force
carrier family alongside $T_{3,4}$ (Hopf${}^2$ color binding). Its longitudinal winding
$n = 5$ is the same as that of $T_{2,5}$ (muon, bottom), creating a
cross-link between the two winding families:

| $m \backslash n$ | $3$ | $4$ | $5$ | $7$ | $9$ |
|------------------|-----|-----|-----|-----|-----|
| $2$ | $e^-, u$ | — | $\mu, b$ | $\tau, c$ | **force** |
| $3$ | — | **force** | **force** | — | — |

$T_{3,5}$ sits at the intersection of the $m = 3$ (quark) row and the
$n = 5$ (second-generation) column. Its knot group relation
$x^3 = y^5$ intertwines the three-strand color structure with
five-fold longitudinal winding.

If $T_{2,9}$ carries the strong force, $T_{3,5}$ is a natural
candidate for a **flavor-changing interaction** — a topological
mediator that connects the $m = 2$ and $m = 3$ families. The
weak force, which is the only Standard Model interaction that
changes quark flavor (e.g., $u \leftrightarrow d$ via $W^{\pm}$),
requires precisely this kind of cross-family mediation.
Alternatively, $T_{3,5}$ could encode the **electroweak mixing**
between the leptonic ($m = 2$) and quark ($m = 3$) sectors.

**Summary of candidate assignments.**

| Generator | Structure | Candidate | Rationale |
|-----------|-----------|-----------|-----------|
| $T_{2,9}$ | Three-fold cover of $T_{2,3}$ | Strong force / gluonic binding | Interpolates 3 color copies of the trefoil; zero volume = massless |
| $T_{3,5}$ | Cross-link of $m = 3$, $n = 5$ | Weak / electroweak mediator | Connects quark and lepton winding families; flavor-changing |

**Open problem.**
Make the force interpretation precise: identify $T_{2,9}$ and $T_{3,5}$
with specific gauge bosons (gluon, $W^{\pm}$, $Z^0$) by computing
their Skein interaction terms with matter generators and comparing
coupling constants derived from the mass functional with Standard
Model values.

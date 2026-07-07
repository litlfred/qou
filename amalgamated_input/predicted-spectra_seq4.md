<!-- FILE_START: torus-hopf-stability.md -->
**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with $\chi(A) = -6$. Every baryon formed from torus knot generators $\mathcal{G}$ linked by the Hopf link $\mathcal{L}_H$ satisfies the stability condition

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) < 0
$$

and is therefore a hadron.
<!-- FILE_END: torus-hopf-stability.md -->

<!-- FILE_START: unmapped-torus-knots.md -->
The particle dictionary assigns physical identities to five of the seven torus knot generators. Two generators remain unassigned:

| Generator | Knot | Genus | Crossings | Assignment |
|-----------|------|-------|-----------|------------|
| $T_{2,9}$ | $9_1$ | $4$ | $9$ | **?** |
| $T_{3,5}$ | $10_{124}$ | $4$ | $10$ | **?** |

Both exactly fill the maximal Seifert genus allowed by the Bring's surface. Their high crossing numbers place them at the top of the complexity hierarchy within $\mathcal{G}$.

**The assignment gap.**
The current mapping uses:

- $T_{1,0}$: neutrino $\nu$ (genus 0)
- $T_{2,3}$: electron $e^-$, up quark $\mathfrak{u}$ (genus 1)
- $T_{2,5}$: muon $\mu$, charm quark $\mathfrak{c}$ (genus 2)
- $T_{2,7}$: tau lepton $\tau$, bottom quark $\mathfrak{b}^{\sigma}$ (genus 3)
- $T_{3,4}$: Hopf${}^2$ color binding (genus 3, force carrier)

Standard Model fermions exhaust at genus 3. Yet the Bring's surface provides two additional generators at genus 4 that the generation scheme does not require for known matter particles.

**The three-fold cover structure of $T_{2,9}$.**

The longitudinal winding number of $T_{2,9}$ factorizes as $9 = 3 \times 3$. This is unique among $T_{2,n}$ generators:

| Generator | $n$ | $n/3$ | Role |
|-----------|-----|-------|------|
| $T_{2,3}$ | $3$ | $1$ | Matter (electron, up quark) |
| $T_{2,5}$ | $5$ | — | Matter (muon, bottom) |
| $T_{2,7}$ | $7$ | — | Matter (tau, charm) |
| $T_{2,9}$ | $9$ | $\mathbf{3}$ | **Three-fold cover of $T_{2,3}$** |

On the torus, $T_{2,9}$ traces the trefoil pattern three times around the longitude, making it the unique three-fold cover of $T_{2,3}$ within $\mathcal{G}$. The knot group relation $x^2 = y^9 = (y^3)^3$ reflects this factorization: the longitudinal generator $y$ completes three full $T_{2,3}$ periods before closing.

This three-fold structure resonates with the three color tubes. Each color fiber carries one copy of the trefoil pattern; $T_{2,9}$ interpolates all three simultaneously, wrapping once through each color tube per longitudinal period.

**Force interpretation.**
The matter/force distinction in the Standard Model aligns with a winding number dichotomy:

- **Matter generators** ($T_{2,3}$, $T_{2,5}$, $T_{2,7}$) have prime winding numbers that do not factor through a lower generator.
- **Force generators** ($T_{3,4}$, $T_{3,5}$, $T_{2,9}$) populate the $H^{0,1}$ antiholomorphic sector: $T_{2,9}$ has composite winding $9 = 3 \times 3$ that factors through $T_{2,3}$; $T_{3,4}$ provides Hopf-squared color binding; $T_{3,5}$ mediates the weak interaction.

A generator whose winding interpolates three matter copies acts as a binding agent rather than a standalone particle. We thus identify:

$$
  T_{2,9} \longleftrightarrow \text{strong force (gluonic binding)}.
$$

The 9 crossings of $T_{2,9}$ provide exactly three crossing triples, one per color tube. In the Borromean baryon, the three quark components are threaded through the color fibers. As their three-fold cover, $T_{2,9}$ supplies the topological rigidity that holds the configuration together. The zero hyperbolic volume of $T_{2,9}$ aligns with massless gluons.

**The structure of $T_{3,5}$.**

The torus knot $T_{3,5}$ has 3-strand meridional winding, placing it in the force carrier family alongside $T_{3,4}$. Its longitudinal winding $n = 5$ matches that of $T_{2,5}$ (muon, bottom), creating a cross-link between the two winding families:

| $m \backslash n$ | $3$ | $4$ | $5$ | $7$ | $9$ |
|------------------|-----|-----|-----|-----|-----|
| $2$ | $e^-, u$ | — | $\mu, b$ | $\tau, c$ | **force** |
| $3$ | — | **force** | **force** | — | — |

$T_{3,5}$ sits at the intersection of the $m = 3$ (quark) row and the $n = 5$ (second-generation) column. Its knot group relation $x^3 = y^5$ intertwines the three-strand color structure with five-fold longitudinal winding.

If $T_{2,9}$ carries the strong force, $T_{3,5}$ is a natural candidate for a flavor-changing interaction—a topological mediator that connects the $m = 2$ and $m = 3$ families. The weak force, which changes quark flavor (e.g., $u \leftrightarrow d$ via $W^{\pm}$), requires precisely this cross-family mediation. Alternatively, $T_{3,5}$ could encode the electroweak mixing between leptonic and quark sectors.

**Summary of candidate assignments.**

| Generator | Structure | Candidate | Rationale |
|-----------|-----------|-----------|-----------|
| $T_{2,9}$ | Three-fold cover of $T_{2,3}$ | Strong force / gluonic binding | Interpolates 3 color copies of the trefoil; zero volume = massless |
| $T_{3,5}$ | Cross-link of $m = 3$, $n = 5$ | Weak / electroweak mediator | Connects quark and lepton winding families; flavor-changing |

**Open problem.**
Make the force interpretation precise: identify $T_{2,9}$ and $T_{3,5}$ with specific gauge bosons (gluon, $W^{\pm}$, $Z^0$) by computing their Skein interaction terms with matter generators and comparing coupling constants derived from the mass functional with Standard Model values.
<!-- FILE_END: unmapped-torus-knots.md -->

<!-- FILE_START: torus-knot-prime-powers.md -->
The torus knots $T_{3,n}$ with $n = p^k$ (a prime power, $p \neq 3$) form natural subfamilies whose genus grows exponentially. The Bring surface genus bound selects a small number of these.

**Genus formula.**
For $T_{3,p^k}$ with $\gcd(3, p^k) = 1$:

$$
  g(T_{3,p^k}) = \frac{(3-1)(p^k - 1)}{2} = p^k - 1.
$$

Embeddability requires $p^k - 1 \leq 4$, which implies $p^k \leq 5$.

**The $p = 2$ tower: $T_{3, 2^k}$.**

| $k$ | Knot | Genus $= 2^k - 1$ | Crossings | Embeddable? | Assignment |
|-----|------|--------------------|-----------|-------------|------------|
| $1$ | $T_{3,2} = T_{2,3}$ (trefoil $3_1$) | $1$ | $3$ | Yes | Electron $e^-$, up quark $\mathfrak{u}$ |
| $2$ | $T_{3,4}$ ($8_{19}$) | $3$ | $8$ | Yes | Hopf${}^2$ color binding |
| $3$ | $T_{3,8}$ | $7$ | $21$ | **No** | Excluded |
| $4$ | $T_{3,16}$ | $15$ | $45$ | **No** | Excluded |

The genus sequence $1, 3, 7, 15, \ldots$ follows Mersenne numbers $g = 2^k - 1$. The Bring's surface admits exactly two levels of this tower: the trefoil ($k = 1$) and $T_{3,4}$ ($k = 2$, a force carrier in the Hodge decomposition). No third generation of $p = 2$ knots is possible.

**The trefoil as self-intersection of two families.**

The identity $T_{3,2} = T_{2,3}$ means the trefoil belongs to both winding families simultaneously:

$$
  T_{2,3} \in \{T_{2,n}\}_{n \text{ odd}} \qquad\text{and}\qquad T_{3,2} \in \{T_{3,p^k}\}_{p \neq 3}.
$$

It is the unique generator at the intersection of the $m = 2$ (leptonic) and $m = 3$ (quark) families. This self-intersection explains why the same knot type encodes both the electron and the up quark: the trefoil is the common seed from which both families grow.

| Family | Generators from trefoil seed |
|--------|----------------------------|
| $m = 2$: $T_{2,3} \to T_{2,5} \to T_{2,7} \to T_{2,9}$ | $e^-, \mu, \tau,$ **strong force** |
| $m = 3$: $T_{3,2}, T_{3,4}, T_{3,5}$ | $u,$ **color binding,** **weak force** |

The trefoil is the root node of both generation chains.

**The $p = 5$ tower: $T_{3,5^k}$.**

| $k$ | Knot | Genus $= 5^k - 1$ | Embeddable? |
|-----|------|--------------------|-------------|
| $1$ | $T_{3,5}$ ($10_{124}$) | $4$ | Yes (saturating) |
| $2$ | $T_{3,25}$ | $24$ | No |

Only $k = 1$ fits. Unlike $T_{3,4} = T_{3,2^2}$, which squares the trefoil's winding number, $T_{3,5}$ is an isolated prime. It does not extend to a tower within the Bring's surface.

**The $p = 7$ tower and beyond.**

For $p \geq 7$: $g(T_{3,p}) = p - 1 \geq 6 > 4$. No knot $T_{3,p^k}$ with $p \geq 7$ is embeddable.

**Complete classification of embeddable $T_{3,p^k}$.**

$$
  \{T_{3,p^k} : \gcd(3,p^k) = 1, p^k - 1 \leq 4\} = \{T_{3,2}, T_{3,4}, T_{3,5}\}.
$$

The $p = 2$ tower contributes the trefoil (matter) and $T_{3,4}$ (Hopf${}^2$ color binding — force carrier in $H^{0,1}$). The $p = 5$ singleton sits at the genus boundary.

**Matter vs. force dichotomy from prime-power structure.**

The power tower $T_{3,2^k}$ establishes a clear physical pattern:

- $k = 1$: $T_{3,2}$ = trefoil — lightest matter (electron, up quark).
- $k = 2$: $T_{3,4}$ — Hopf${}^2$ color binding (force carrier in $H^{0,1}$).
- $k = 3$: excluded — the Bring's surface forbids a third level.

The mass ratio $m_t / m_u \approx 7.5 \times 10^4$ spans four orders of magnitude across the single step $k = 1 \to k = 2$. Exponential genus growth ($2^k - 1$) separates the levels, and the Hodge decomposition places $T_{3,4}$ in the $H^{0,1}$ force carrier sector rather than the $H^{1,0}$ matter sector.

Meanwhile, $T_{3,5}$, isolated outside any power tower, is structurally distinguished from both matter generations. Its prime winding ($n = 5$, not a power of 2) and saturating genus (4) mark it as categorically different. This is consistent with its force carrier interpretation.

**Remark on $T_{2,9}$ in this framework.**
The three-fold cover $T_{2,9}$ has $n = 9 = 3^2$, a prime power in the $m = 2$ family. Its genus is $(9 - 1)/2 = 4$ (saturating). 

| Family | Power tower (matter) | Isolated prime (force?) |
|--------|---------------------|------------------------|
| $m = 2$ | $T_{2,3}, T_{2,5}, T_{2,7}$ | $T_{2,9}$ ($n = 3^2$) |
| $m = 3$ | $T_{3,2}, T_{3,4}$ ($n = 2^k$) | $T_{3,5}$ ($n = 5$) |

In both families, matter generators have lower genus and the saturating genus-4 generator stands apart. The genus-4 boundary consistently separates matter from force across both winding families.
<!-- FILE_END: torus-knot-prime-powers.md -->

<!-- FILE_START: force-knot-identification.md -->
The three fundamental forces of the Standard Model arise from three distinct layers of the torus knot architecture on Bring's surface. The strong and weak forces are carried by the saturating genus-$4$ generators $T_{2,9}$ and $T_{3,5}$. Electromagnetism is not a knot, but the involutive structure of the category itself.

**I. Electromagnetism: the involutive structure.**
Electromagnetism does not require a dedicated torus knot generator. It exists in the $\dagger$-structure on $\mathbf{C}$ and the crossing-sign decomposition of the Skein algebra.

The crossing energy at each site decomposes into symmetric and antisymmetric channels:

$$
  \mathfrak{E}_{\mathrm{cross}} = 
  \underbrace{E_{\mathrm{sym}}}_{\text{mass (strong)}}
  + 
  \underbrace{E_{\mathrm{anti}}}_{\text{Coulomb (EM)}}.
$$

The antisymmetric Coulomb channel reverses sign under the crossing reversal involution $\sigma \colon K \mapsto K^{\sigma}$, which implements charge conjugation $C$ at the categorical level. Electromagnetic charge is the eigenvalue of the involution $\sigma$ acting on the crossing energy:

$$
  Q(K) =  \frac{1}{2}\bigl(\mathfrak{E}_{\mathrm{cross}}(K)
  - \mathfrak{E}_{\mathrm{cross}}(K^{\sigma})\bigr).
$$

This involution descends from three interlocking structures on Bring's surface:

1. **The $\dagger$-involution** on $\mathbf{C}$: the positive-definite contravariant endofunctor $f \mapsto f^{\dagger}$ that defines observability. Every morphism carries a sign under $\dagger$. The electromagnetic coupling is the component of the Skein pairing that is odd under this involution.
2. **The complex structure** on the color elliptic curve $\mathcal{E}_z$: Bring's surface admits a Kähler structure inherited from the embedding $\Sigma_4 \hookrightarrow \mathbb{P}^4$. The complex structure $J$ satisfies $J^2 = -1$ and determines the phase of the crossing energy. Electromagnetic charge is the winding number of this phase around the $\mathrm{U}(1)$ fiber of the Hopf map $\mathrm{SU}(2) \to \mathbb{CP}^1$.
3. **The symplectic pairing** on the color tube coordinates: the T-duality involution $\iota \colon (X, z) \mapsto (z, X)$ on the symmetric cubic $F(X, z) = F(z, X)$ exchanges color and spacetime degrees of freedom. The symplectic form $\omega = dX \wedge dz$ is preserved by $\iota$. The Coulomb interaction is the component of the crossing energy that transforms as a $(1,1)$-form under the complex structure.

Electromagnetism is intrinsic to any knot. Every charged particle (every knot with nonzero antisymmetric crossing energy) automatically couples electromagnetically. This structure yields three consequences:
- **Universality of EM**: all charged particles interact, regardless of knot type or genus.
- **Charge quantisation**: $Q$ is an eigenvalue of an involution, hence discrete ($\pm 1$ for leptons, $\pm 1/3, \pm 2/3$ for quarks in the Borromean decomposition).
- **Masslessness of the photon**: EM is not carried by a knot, but by the algebraic structure itself. The $\dagger$-involution has no Seifert genus, so it contributes no topological mass.

**II. Strong force: $T_{2,9}$ as gluonic binding.**
The strong interaction is carried by $T_{2,9}$, the three-fold cover of the trefoil.

| Property | Value | Physical implication |
|----------|-------|---------------------|
| Winding | $9 = 3 \times 3$ | Interpolates 3 color copies of $T_{2,3}$ |
| Genus | $4$ (saturating) | Maximal topological complexity |
| Crossings | $9$ (all same sign) | Three crossing triples, one per color tube |
| Hyperbolic volume | $0$ | Massless carrier (gluon) |
| Meridional strands | $m = 2$ | Same winding family as leptons/quarks |

The strong force binds by interpolation. $T_{2,9}$ wraps through all three color fibers in a single closed curve, providing the topological rigidity that confines quarks into baryons. The three $S_3$ subgroups of the automorphism group of Bring's surface $S_5$ are the subgroups that leave one of the three $T_{2,3}$ periods of $T_{2,9}$ invariant.

This topology explains confinement. We cannot continuously deform $T_{2,9}$ to separate the three color copies without breaking the torus embedding. Extracting a single color strand requires cutting $T_{2,9}$ into an open arc, which is topologically forbidden. 

At scales smaller than the color tube radius, the three strands of $T_{2,9}$ are locally parallel. The binding provided by their global winding becomes negligible. This yields asymptotic freedom.

**III. Weak force: $T_{3,5}$ as flavor-changing mediator.**
The weak interaction is carried by $T_{3,5}$, the cross-family generator connecting $m = 2$ (leptons) and $m = 3$ (quarks).

| Property | Value | Physical implication |
|----------|-------|---------------------|
| Winding | $(3, 5)$ | Bridges $m = 3$ (quark) and $n = 5$ (second generation) |
| Genus | $4$ (saturating) | Near-boundary of embeddability |
| Crossings | $10$ | High complexity $\to$ weak coupling |
| Hyperbolic volume | $0$ | Zero bare mass from volume; mass from crossings |
| Knot group | $\langle x, y \mid x^3 = y^5 \rangle$ | Intertwines 3-color and 5-fold winding |

The torus knot $T_{3,5}$ is the only generator whose winding numbers draw from both families: $m = 3$ from the quark sector, and $n = 5$ from the $T_{2,5}$ column. This cross-link enables flavor-changing processes. The weak interaction transmutes quarks between generations and converts quarks to leptons because $T_{3,5}$ topologically connects both sectors.

Parity violation follows from the Skein asymmetry at $q \neq 1$. The Skein relation $q[L_+] - q^{-1}[L_-] = (q^{1/2} - q^{-1/2})[L_0]$ treats positive and negative crossings differently. The weak force inherits this asymmetry maximally because $T_{3,5}$ has the highest crossing count ($10$) among generators. The $q$-vs-$q^{-1}$ imbalance accumulates over these crossings.

Unlike the massless $T_{2,9}$, $T_{3,5}$ contributes nonzero mass to the weak bosons. Although its hyperbolic volume is zero, its $10$ crossings generate crossing energy via the mass formula. The $10$ crossings of $T_{3,5}$ do not cancel, yielding the massive $W$ and $Z$.

**Summary.**

| Force | Source | Knot? | Mass | Parity |
|-------|--------|-------|------|--------|
| **EM** | Involutive structure ($\dagger$, $J$, $\omega$) | No knot | Massless (no topology) | Conserved |
| **Strong** | $T_{2,9}$: three-fold cover of trefoil | Genus $4$, vol $= 0$ | Massless (color-averaged crossings cancel) | Conserved |
| **Weak** | $T_{3,5}$: cross-family mediator | Genus $4$, vol $= 0$ | Massive (net crossing energy $\neq 0$) | Violated ($q \neq 1$) |

All three forces are determined by the genus-$4$ constraint $\chi(A) = -6$.
<!-- FILE_END: force-knot-identification.md -->

<!-- FILE_START: torus-knot-genus-four-unique.md -->
**Proposition (genus-$4$ torus knots are exhausted by two pairs).**
*Let $g \in \mathbb{Z}_{\geq 0}$ and consider torus knots $T_{m,n}$
with $2 \leq m \leq n$ and $\gcd(m, n) = 1$.  The genus is
$g(T_{m,n}) = (m-1)(n-1)/2$
([torus knot generators](#prop:torus-knot-generators)).  At $g = 4$
the equation $(m-1)(n-1) = 8$ has exactly two solutions in positive
integers with $m \leq n$ and $\gcd(m, n) = 1$:*

| Solution | $(m, n)$ | crossing number $c = m(n-1)$ | $\gcd(m, n)$ |
|---|---|---|---|
| $(m{-}1,\, n{-}1) = (1,\, 8)$ | $(2,\, 9)$ | $9$ | $1$ (yes) |
| $(m{-}1,\, n{-}1) = (2,\, 4)$ | $(3,\, 5)$ | $10$ | $1$ (yes) |
<!-- FILE_END: torus-knot-genus-four-unique.md -->

<!-- FILE_START: force-carrier-bring-uniqueness.md -->
**Proposition (Bring-supported force-carrier sector is forced).**
*Bring's surface $\Sigma_4$ has genus $4$. A torus knot $K$ embeds as a saturating generator of the symplectic homology $H_1(\Sigma_4, \mathbb{Z}) \cong \mathbb{Z}^{2 g} = \mathbb{Z}^8$ only if $g(K) = g(\Sigma_4) = 4$. By the genus-$4$ classification, the force-carrier sector of any QOU built on $\Sigma_4$ contains exactly the two-element set $\{T_{2,9}, T_{3,5}\}$.*
<!-- FILE_END: force-carrier-bring-uniqueness.md -->

<!-- FILE_START: force-carrier-bring-uniqueness-novelty.md -->
**Remark.** The underlying Diophantine constraint $(m-1)(n-1)=2g$ acts as a genus-saturation condition on the symplectic homology of Bring's surface. This condition determines the force-carrier pair (the crossing-number 9 and 10 knots) through algebraic geometry, removing the need for auxiliary symmetry assumptions.
<!-- FILE_END: force-carrier-bring-uniqueness-novelty.md -->


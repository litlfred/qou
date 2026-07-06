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

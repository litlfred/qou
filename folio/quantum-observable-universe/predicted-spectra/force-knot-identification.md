The three Standard Model forces arise from three distinct layers of the torus knot architecture on Bring's surface. The saturating genus-$4$ generators $T_{2,9}$ and $T_{3,5}$ carry the strong and weak forces. Electromagnetism is not a knot. It is the involutive structure of the category itself.

**I. Electromagnetism.**
Electromagnetism requires no dedicated torus knot generator. It exists in the $\dagger$-structure on $\mathbf{C}$ and the crossing-sign decomposition of the Skein algebra.

The crossing energy at each site decomposes into symmetric and antisymmetric channels:

$$
  \mathfrak{E}_{\mathrm{cross}} = 
  \underbrace{E_{\mathrm{sym}}}_{\text{mass (strong)}}
  + 
  \underbrace{E_{\mathrm{anti}}}_{\text{Coulomb (EM)}}.
$$

The antisymmetric Coulomb channel reverses sign under the crossing reversal involution $\sigma \colon K \mapsto K^{\sigma}$. This implements charge conjugation $C$ categorically. Electromagnetic charge is the eigenvalue of the involution $\sigma$ acting on the crossing energy:

$$
  Q(K) =  \frac{1}{2}\bigl(\mathfrak{E}_{\mathrm{cross}}(K)
  - \mathfrak{E}_{\mathrm{cross}}(K^{\sigma})\bigr).
$$

This involution descends from three interlocking structures on Bring's surface:

1. **The $\dagger$-involution** on $\mathbf{C}$. The positive-definite contravariant endofunctor $f \mapsto f^{\dagger}$ defines observability. Every morphism carries a sign under $\dagger$. The electromagnetic coupling is the component of the Skein pairing that is odd under this involution.
2. **The complex structure** on the color elliptic curve $\mathcal{E}_z$. The embedding $\Sigma_4 \hookrightarrow \mathbb{P}^4$ induces a Kähler structure on Bring's surface. The complex structure $J$ satisfies $J^2 = -1$ and determines the phase of the crossing energy. Electromagnetic charge is the winding number of this phase around the $\mathrm{U}(1)$ fiber of the Hopf map $\mathrm{SU}(2) \to \mathbb{CP}^1$.
3. **The symplectic pairing** on the color tube coordinates. The T-duality involution $\iota \colon (X, z) \mapsto (z, X)$ on the symmetric cubic $F(X, z) = F(z, X)$ exchanges color and spacetime degrees of freedom. The symplectic form $\omega = dX \wedge dz$ is invariant under $\iota$. The Coulomb interaction is the component of the crossing energy that transforms as a $(1,1)$-form under the complex structure.

Electromagnetism is intrinsic to any knot. Every charged particle (knot with nonzero antisymmetric crossing energy) automatically couples electromagnetically. This structure yields three consequences:
- **Universality**. All charged particles interact, regardless of knot type or genus.
- **Charge quantisation**. $Q$ is an eigenvalue of an involution, hence discrete ($\pm 1$ for leptons, $\pm 1/3, \pm 2/3$ for quarks in the Borromean decomposition).
- **Masslessness**. Electromagnetism is not carried by a knot. The $\dagger$-involution has no Seifert genus, contributing zero topological mass.

**II. Strong force.**
The knot $T_{2,9}$, the three-fold cover of the trefoil, carries the strong interaction.

| Property | Value | Physical implication |
|----------|-------|---------------------|
| Winding | $9 = 3 \times 3$ | Interpolates 3 color copies of $T_{2,3}$ |
| Genus | $4$ (saturating) | Maximal topological complexity |
| Crossings | $9$ (all same sign) | Three crossing triples, one per color tube |
| Hyperbolic volume | $0$ | Massless carrier (gluon) |
| Meridional strands | $m = 2$ | Same winding family as leptons/quarks |

The strong force binds by interpolation. The knot $T_{2,9}$ wraps through all three color fibers in a single closed curve. This provides the topological rigidity that confines quarks into baryons. The three $S_3$ subgroups of the automorphism group $S_5$ of Bring's surface are the subgroups that leave one of the three $T_{2,3}$ periods of $T_{2,9}$ invariant.

This topology forces confinement. The knot $T_{2,9}$ cannot continuously deform to separate the three color copies without breaking the torus embedding. Extracting a single color strand requires cutting $T_{2,9}$ into an open arc. This is topologically forbidden. 

At scales smaller than the color tube radius, the three strands of $T_{2,9}$ are locally parallel. The binding from their global winding vanishes. This yields asymptotic freedom.

**III. Weak force.**
The knot $T_{3,5}$ carries the weak interaction. It is the cross-family generator connecting $m = 2$ (leptons) and $m = 3$ (quarks).

| Property | Value | Physical implication |
|----------|-------|---------------------|
| Winding | $(3, 5)$ | Bridges $m = 3$ (quark) and $n = 5$ (second generation) |
| Genus | $4$ (saturating) | Near-boundary of embeddability |
| Crossings | $10$ | High complexity $\to$ weak coupling |
| Hyperbolic volume | $0$ | Zero topological mass from volume; mass from crossings |
| Knot group | $\langle x, y \mid x^3 = y^5 \rangle$ | Intertwines 3-color and 5-fold winding |

The torus knot $T_{3,5}$ uniquely combines winding numbers from both families: $m = 3$ from the quark sector, and $n = 5$ from the $T_{2,5}$ column. This cross-link drives flavor-changing processes. The weak interaction transmutes quarks between generations and converts quarks to leptons because $T_{3,5}$ topologically connects both sectors.

Parity violation follows from the Skein asymmetry at $q \neq 1$. In the Hecke algebra $H_n(q)$ a positive crossing is the generator $\sigma_i = L_+$, a negative crossing is $\sigma_i^{-1} = L_-$, and the smoothing is $1 = L_0$. The Skein relation is the Hecke relation multiplied by $\sigma_i^{-1}$:

$$
  L_+ - L_- = (q - q^{-1})\,L_0 .
$$

Weighting the two crossings unequally separates the two eigenlines of $\sigma_i$. Let $P_+$ and $P_-$ be the idempotents of $\sigma_i$ for its eigenvalues $q$ and $-q^{-1}$; these are the left and right circular channels of the Breit–Wheeler vertex. With $[2]_q = q + q^{-1}$,

$$
  q\,\sigma_i - q^{-1}\sigma_i^{-1} = (q - q^{-1})\,[2]_q\,P_+ .
$$

The $q$-weighted crossing difference therefore acts on one eigenline only, and it vanishes at $q = 1$. Let $W_L = P_+\sigma_i^{-1}P_+ + P_-\sigma_i P_-$ be the element that inverts $\sigma_i$ on the $P_+$ line and leaves the $P_-$ line unchanged. It is the generator minus this difference:

$$
  [2]_q\,W_L = [2]_q\,\sigma_i - \bigl(q\,\sigma_i - q^{-1}\sigma_i^{-1}\bigr).
$$

Both identities hold for every $q$ with $q \neq 0$ and $q + q^{-1} \neq 0$. Which eigenline is singled out is fixed by which crossing carries the weight $q$: the mirror weighting $q^{-1}\sigma_i - q\,\sigma_i^{-1}$ gives $(q - q^{-1})\,[2]_q\,P_-$ instead. This one-sidedness holds at a single crossing. The convention-D trace of $T_{3,5}$ itself is not supported on the left line.

The following is a model statement without derivation. The weak force maximizes this asymmetry because $T_{3,5}$ has the highest crossing count ($10$) among generators, and the $q$-vs-$q^{-1}$ imbalance accumulates over these crossings. No computation here relates the crossing count to the size of the asymmetry.

Unlike the massless $T_{2,9}$, $T_{3,5}$ gives nonzero mass to the weak bosons. Its hyperbolic volume is zero, but its $10$ crossings generate crossing energy via the mass formula. The $10$ crossings of $T_{3,5}$ do not cancel. This yields the massive $W$ and $Z$. This too is a model statement without derivation: the crossing energy of $T_{3,5}$ is not computed here, and no $W$ or $Z$ mass is derived from it.

**Summary.**

| Force | Source | Knot? | Mass | Parity |
|-------|--------|-------|------|--------|
| **EM** | Involutive structure ($\dagger$, $J$, $\omega$) | No | Massless (no topology) | Conserved |
| **Strong** | $T_{2,9}$: three-fold cover of trefoil | Genus $4$, vol $= 0$ | Massless (color-averaged crossings cancel) | Conserved |
| **Weak** | $T_{3,5}$: cross-family mediator | Genus $4$, vol $= 0$ | Massive (net crossing energy $\neq 0$) | Violated ($q \neq 1$) |

The genus-$4$ constraint $\chi_{\mathrm{eu}}(M_0) = -6$ specifies all three forces.

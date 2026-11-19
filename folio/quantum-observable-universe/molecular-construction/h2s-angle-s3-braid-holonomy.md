**Conjecture (H$_2$S bond-angle chiral residue $=$ S$^3$ braid holonomy).**

*The bond-angle residual of $\mathrm{H_2S}$ — the opening $\Delta\theta \approx +2.1^\circ$ of the H–S–H angle above the pure-$p$ base $\theta_0 = 90^\circ$ — equals the $q$-deformed Chern–Simons holonomy (the monodromy phase around the singular fibre $\zeta_\ell$) of the chiral $3p_z$ lone-pair braid $\beta_{3p_z}$ on the chirality cell — the signed-content-zero standard Wedderburn block $V_{(2,1)}$ (the $q$-Dirac kernel $D_q^2(\lambda)=0$):*

$$
  \Delta\theta_{\mathrm{H_2S}}
  \;=\;
  \arg \mathrm{Res}_{q=\zeta_\ell}\!\Bigl[\,\Phi_q \cdot
        \mathrm{tr}_{M,(2,1)}\bigl(\beta_{3p_z}\bigr)\Bigr].
$$

*Equivalently, $\Delta\theta$ is the bar-anti-symmetric ($P_{\mathrm{skew}}$, odd-in-$h$) part of the chiral lone's S$^3$ braid holonomy. This is the chiral channel the framework otherwise projects away. It vanishes for the bar-symmetric (self-dual, palindromic) lone pairs of $\mathrm{H_2O}$, which is why $\mathrm{H_2O}$'s angle is the clean $q^2$ prediction with no residual.*

## Concrete realisation

A third-row (pure-$p$) atom retains a small residual $s$-character $f_s = (1/\sqrt5)/(n-1)^2$ that opens the $90^\circ$ base toward sp$^3$:

$$
  \theta(n) \;=\; 90^\circ \;+\; \frac{1}{\sqrt5}\cdot
    \frac{\arccos(-\tfrac13) - 90^\circ}{(n-1)^2}.
$$

| | $n$ | predicted | observed |
|---|---|---|---|
| $\mathrm{H_2S}$ | $3$ | $92.18^\circ$ | $92.1^\circ$ |
| $\mathrm{H_2Se}$ | $4$ | $90.97^\circ$ | $91.0^\circ$ |
| $\mathrm{H_2Te}$ | $5$ | $90.54^\circ$ | $90.0^\circ$ |

$\mathrm{H_2S}$ and $\mathrm{H_2Se}$ match the observation within $0.1^\circ$. The coefficient is the Bring (quintic) constant $1/\sqrt5$, the $S^3$-embedding chiral curvature surfacing as the quintic $\sqrt5$ of Bring's surface. The size dependence is inverse-square in the $s$–$p$ gap. The concrete content of the conjecture is that the chiral residue is the $1/\sqrt5$ Bring curvature, inverse-square in central-atom size. This is a Bring-grounded near-match constrained by two data points. The exact $\zeta_\ell$ monodromy remains the formal target.

The explicit geometry of this $\sqrt5$ is the provable scaffold of the [Bring trefoil–cinquefoil channel proposition](../brings-surface/bring-trefoil-cinquefoil-channel.md): the chiral channel is the trefoil $T_{2,3}$ (Seifert genus $1$) and the $\zeta_5$ is the cinquefoil $T_{2,5}$ (genus $2$). These are distinct torus knots sharing Bring's $\Sigma_4$ (genus $4$) and linked by $\mathrm{Aut}(B) = S_5$.

> [!NOTE]
> The global *Bring curve* (a genus-4 curve in $\mathbb{CP}^4$ whose $S_5$ characters fix the $2 \times 2$ Picard-Fuchs matrix and depth-2 recurrence for the mass tower) is distinct from the *hyperelliptic quintic* $\mathcal{X}_5 \colon y^2 = x^5 - 1$. The latter is a genus-2 curve embedded within Bring's surface. The chiral normalisation specifically relies on the $\mathbb{Z}_5$ automorphism of this embedded quintic.

The $\sqrt5$ is supplied by the $\mathbb{Z}_5$-orbit quadratic Gauss sum $\bigl(\sum_k \zeta_5^{k^2}\bigr)^2 = 5$ carried by the first Lagrange resolvent $w_1$ that embeds the hyperelliptic quintic $\mathcal{X}_5$. With that structural scaffold in place, evaluating the exact analytic Picard-Lefschetz monodromy of the $\zeta_5$-residue on the homology of $y^2 = x^5 - 1$ to formally return precisely $1/\sqrt5$ and the $+2.1^\circ$ phase remains open.

**Archimedean specialisation.** What follows invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.

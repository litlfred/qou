**Conjecture (H₂S bond-angle chiral residue $=$ S³ braid holonomy).**

*The bond-angle residual of $\mathrm{H_2S}$ — the opening
$\Delta\theta \approx +2.1^\circ$ of the H–S–H angle above the pure-$p$ base
$\theta_0 = 90^\circ$ — equals the $q$-deformed Chern–Simons holonomy (the
monodromy phase around the singular fibre $\zeta_\ell$) of the chiral $3p_z$
lone-pair braid $\beta_{3p_z}$ on the chirality cell — the signed-content-zero
standard Wedderburn block $V_{(2,1)}$ (the $q$-Dirac kernel $D_q^2(\lambda)=0$):*

$$
  \Delta\theta_{\mathrm{H_2S}}
  \;=\;
  \arg \operatorname{Res}_{q=\zeta_\ell}\!\Bigl[\,\Phi_q \cdot
        \mathrm{tr}_{M,(2,1)}\bigl(\beta_{3p_z}\bigr)\Bigr].
$$

*Equivalently, $\Delta\theta$ is the **bar-anti-symmetric**
($P_{\mathrm{skew}}$, odd-in-$h$) part of the chiral lone's S³ braid holonomy —
the chiral channel the framework otherwise projects away — and it **vanishes**
for the bar-symmetric (self-dual, palindromic) lone pairs of $\mathrm{H_2O}$,
which is why $\mathrm{H_2O}$'s angle is the clean $q^2$ prediction with no
residual.*

## Status of the pieces

What is **established** (not conjectural):

- The chiral channel is exactly the $c_\lambda=0$ block $V_{(2,1)}$
  ([`prop:chirality-residue-mass-term`](#prop:chirality-residue-mass-term):
  $c_\lambda(3)=+3$, $c_\lambda(2,1)=0$, $c_\lambda(1,1,1)=-3$).
- The residue is the braid holonomy around the singular fibre — the q-deformed
  Chern–Simons holonomy of a Wilson loop in $S^3$
  ([`rem:residue-as-braid-holonomy`](#rem:residue-as-braid-holonomy)).
- The split is the bar-involution ([`def:bar-involution`](#def:bar-involution)):
  the clean second-row angles are the bar-symmetric backbone, the H₂S residual
  the bar-anti-symmetric ($P_{\mathrm{skew}}$) part. **Parity is established**:
  the residual is odd in $h$ (scale $h z^2 \approx 3^\circ$, $h z^3 \approx
  1.5^\circ$, observed $2.1^\circ$ between).

The **conjectural content** is the identification itself — that the
molecular-angle opening $\Delta\theta_{\mathrm{H_2S}}$ *is* this S³ holonomy
phase, and that the monodromy/Reshetikhin–Turaev evaluation at $\zeta_\ell$
returns the observed $\approx 2.1^\circ$.

> **Caveat (the exact form is open).** Three a-priori distinct involutions are
> in play and must not be conflated: the **palindromic reversal** (which fixes
> the orbital $\ell = \tfrac12$ defect, so $s$ self-dual / $p$ chiral), the
> **bar-involution** $\sigma_i \mapsto \sigma_i^{-1}$ (the $P_{\mathrm{avg}}$ /
> $P_{\mathrm{skew}}$ even–odd split), and the **longest-element** $w \mapsto
> w_0 w$ (the self-duality of `palindromicity-orbital-type`). The naive
> $P_{\mathrm{skew}}$ of the length-3 chiral word on $V_{(2,1)}$ in fact
> *vanishes*, so $\Delta\theta$ is **not** the leading bar-skew matrix part;
> the parity argument ($\Delta\theta$ odd in $h$, bracketed by $hz^2/hz^3$) is
> observational. Pinning the exact form requires the monodromy phase at
> $\zeta_\ell$ with the correct involution — this is the open content.

## Concrete realisation — the Bring $1/\sqrt5$ residual-mixing form

A predictive realisation (no fit): a third-row (pure-$p$) atom retains a small
**residual $s$-character** $f_s = (1/\sqrt5)/(n-1)^2$ that opens the $90^\circ$
base toward sp³, so

$$
  \theta(n) \;=\; 90^\circ \;+\; \frac{1}{\sqrt5}\cdot
    \frac{\arccos(-\tfrac13) - 90^\circ}{(n-1)^2}.
$$

| | $n$ | predicted | observed |
|---|---|---|---|
| $\mathrm{H_2S}$ | $3$ | $92.18^\circ$ | $92.1^\circ$ |
| $\mathrm{H_2Se}$ | $4$ | $90.97^\circ$ | $91.0^\circ$ |
| $\mathrm{H_2Te}$ | $5$ | $90.54^\circ$ | $90.0^\circ$ |

$\mathrm{H_2S}$ and $\mathrm{H_2Se}$ land within $0.1^\circ$. The coefficient is
the **Bring / quintic constant** $1/\sqrt5$ ($\varphi = (1+\sqrt5)/2$; $\sqrt5$
the quintic discriminant) — the conjectured $S^3$-embedding chiral curvature
surfacing as the quintic $\sqrt5$ of Bring's surface — and the size dependence
is inverse-square in the $s$–$p$ gap. This is the concrete content of the
conjecture: the chiral residue is the $1/\sqrt5$ Bring curvature, inverse-square
in central-atom size. *Tier:* a strong, Bring-grounded near-match constrained by
two data points — reported as a tiered observation; the exact $\zeta_\ell$
monodromy is still the formal target.

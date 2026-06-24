*Lean sibling: `QOU.Archimedean.PhotonIRZeroMode`. The topological/geometric core is unconditional; the heat-kernel zero-mode is a cited standard result; the $\tau_{\mathrm{arch}}$ uniqueness is the upstream conditional input.*

**Proposition (photon IR zero-mode on Bring's surface — the from-the-Lagrangian source of $2/(3\pi)$).** *Let $M_g$ be a closed orientable genus-$g$ hyperbolic surface (constant curvature $-1$). The photon IR zero-mode contribution to $1/\alpha_{EM}$ at zero external momentum is the harmonic $1$-form sector $H^1(M_g)$ — the gauge field's flat-connection moduli — normalised by the surface area:*

$$
  \delta\!\left(\tfrac{1}{\alpha_{EM}}\right)_{\mathrm{IR}}
  \;=\; \frac{\dim H^1(M_g)}{\operatorname{Area}(M_g)}
  \;=\; \frac{b_1(M_g)}{4\pi(g-1)}
  \;=\; \frac{2g}{4\pi(g-1)},
  \qquad
  b_1 = 2g,\quad \operatorname{Area} = -2\pi\chi = 4\pi(g-1).
$$

*At the Bring genus $g=4$ ($\chi=-6$) this is $\tfrac{8}{12\pi} = \tfrac{2}{3\pi}$ — the additive correction of [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode). The "$/3$" is the Gauss–Bonnet factor $(g-1)=3$, not a ball-volume dimension.*

## Mechanism (the derivation)

The Maxwell sector of the categorical Lagrangian, restricted to the UV-completing surface $M_g$ — the genus-$4$ Bring surface carrying the force-carrier pair $\{T_{2,9}, T_{3,5}\}$ ([`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness)) — has its zero-momentum two-point function governed by the kernel of the $1$-form Laplacian $\Delta_1$. By Hodge theory $\dim\ker\Delta_1 = b_1(M_g) = 2g$; the heat-kernel zero-mode of a Laplacian contributes one constant mode $1/\operatorname{Vol}$ per harmonic generator, so the infrared shift is $b_1/\operatorname{Area}$. Gauss–Bonnet fixes $\operatorname{Area} = -2\pi\chi = 4\pi(g-1)$ at curvature $-1$ (Lean `area_eq_neg_two_pi_chi`), giving $2g/(4\pi(g-1))$ (Lean `photonZeroModeShift_eq`), $= 2/(3\pi)$ at $g=4$ (Lean `photonZeroModeShift_at_g4`).

**Why the naive attempt failed.** The first-pass attempt recorded in the Status section of [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode) placed the zero-mode on the $3$-manifold $M_g\times S^1$, where $b_1 = 2g+1$ and $\operatorname{Vol} = \operatorname{Area}\cdot 2\pi$, giving $(2g+1)/(8\pi^2(g-1)) = 9/(24\pi^2) \approx 0.038$ — strictly smaller, by $\approx 5.6\times$. Crossing with $S^1$ adds a spurious harmonic generator and a factor $2\pi$ of volume; the photon zero-mode lives on the $2$-surface itself. The surface-minus-naive difference $(16\pi-9)/(24\pi^2) > 0$ is Lean `surface_minus_naive_g4`.

**Jet-order placement and the $n=2$ self-energy.** In the jet-graded decomposition of the Archimedean functor ([`prop:jet-sw-tau-decomposition`](#prop:jet-sw-tau-decomposition)), $\tau = \sum_{n\ge 0} a_D^{(n)}$, the $n=0$ term is the electron period and this photon zero-mode is the $n=1$ infrared term, the first prolongation beyond the tree coupling $q[9]_q[10]_q$. The $n=2$ self-energy has the established form $\alpha\,[2]_q/(8\pi)\,(1-h^2\alpha)$ (the $\alpha/(4\pi)$ thread), and its denominator is **the same Hodge datum**:

$$
  8\pi \;=\; \pi\cdot\dim H^1(M_{\text{Bring}}) \;=\; \pi\,b_1, \qquad b_1 = 2g = 8
$$

(Lean `selfEnergyDenominator_at_g4`). So the single Betti number $b_1 = 8$ controls **both** infrared corrections — the $n=1$ zero-mode carries it in the numerator ($b_1/\operatorname{Area}$), the $n=2$ self-energy in the denominator ($\pi\,b_1$); their $b_1$-placements multiply to the $\pi$-free $b_1^2/(4(g-1))$ (Lean `photon_selfEnergy_betti_product`, the archimedean $\pi$ cancelling). **Boundary discipline**: in both terms $b_1$ is topological, $\pi$ is archimedean, and the $[2]_q$ numerator is the substrate Hecke integer ($\tau_{\mathrm{arch}}$-evaluated, *not* an object of the archimedean Hodge computation).

Grouping the $n=2$ form reveals it as $\alpha\,H(q)/(\pi\,b_1)$, where $H(q) = [2]_q(1-h^2\alpha)$ is the **$\alpha_{EM}$ Habiro element** ([`prop:alpha-em-habiro-bar-involution`](#prop:alpha-em-habiro-bar-involution); bar-involution fixed point, $e_+$ cosh sector). So **Identity 2 is the Habiro deformation** $(1-h^2\alpha)$, and the entire $n=2$ self-energy is $\alpha\cdot(\text{Habiro element})/(\pi\cdot\dim H^1)$ — substrate $H$, archimedean $\pi$, topological $b_1$. This also indicates the **$\tau_{\mathrm{arch}}$/Bloch-class reconciliation** that the bare Hodge route otherwise sidesteps: the Habiro element lives in the Habiro ring, whose root-of-unity evaluations (e.g. the modular zero $H(\zeta_4)=0$ recorded in [`prop:alpha-em-habiro-bar-involution`](#prop:alpha-em-habiro-bar-involution)) connect to the cyclotomic / Bloch-group structure — the candidate bridge between the Hodge ($b_1/\operatorname{Area}$) and dilogarithm ($\tau_{\mathrm{arch}}$-via-$D$) realizations. Establishing that bridge — and the $-h^2\alpha$ fermion-loop end-to-end — is open (PR #1495's RT 2-loop track + the Bloch-class identification).

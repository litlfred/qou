Can a vortex tube reverse its circulation? ([chirality remark](#rem:chirality-trefoil-electron-positron)). Classical fluid dynamics provides a sharp contrast to the categorical framework.

**Classical result: trefoil vortices are unstable.**
Kleckner and Irvine \cite{kleckner2013} observed trefoil-knotted vortex loops in water. A trefoil vortex unties within few circulation timescales via reconnections. Two anti-parallel segments approach, reconnect, and separate, exchanging topology. Scheeler et al. \cite{scheeler2014} demonstrated helicity $\mathcal{H} = \int \mathbf{v} \cdot \boldsymbol{\omega} dV$ conservation during reconnection. It redistributes from writhe to twist:

$$
  \mathcal{H} =  \underbrace{Wr}_{\text{writhe}}
  +  \underbrace{Tw}_{\text{twist}}, \qquad
  \Delta Wr = -\Delta Tw \quad (\text{during reconnection}).
$$

Reconnections reduce the trefoil to unknotted loops. No chirality flip occurs. The trefoil dissolves.

**Obstructions to classical chirality reversal.**

Three obstructions prevent smooth chirality reversal in Navier--Stokes fluids:

1. **Kelvin's theorem.** Ideal fluid circulation $\Gamma = \oint \mathbf{v} \cdot d\mathbf{l}$ is conserved. Reversing $\Gamma$ requires external forcing.
2. **Topological protection of writhe sign.** A trefoil has writhe $Wr = \pm 3$. Flipping from $+3$ to $-3$ requires passing through $Wr = 0$ (unknot). Reconnections only decrease $|Wr|$.
3. **Dissipation.** Reconnections convert kinetic energy to heat. Untying dissipates energy $\sim 3 \Gamma^2 \rho$. Re-tying lacks an energy budget.

**The categorical trefoil is different.**
In the QOU framework, the trefoil is an element of the representation ring of $\mathrm{SU}_q(2)$ rather than a fluid filament.

| Property | Classical vortex | Categorical trefoil |
|----------|-----------------|---------------------|
| Identity | Embedding $S^1 \hookrightarrow \mathbb{R}^3$ | Knot type (isotopy class) |
| Stability | Reconnection-unstable | Topologically protected |
| Circulation | Continuous $\Gamma \in \mathbb{R}$ | Quantised by Casimir $[j]_q[j+1]_q$ |
| Chirality | Sign of $Wr$ | Knot invariant (left vs right trefoil) |
| Helicity transfer | $Wr \leftrightarrow Tw$ | Encoded in $R$-matrix |

The categorical trefoil's chirality is a knot invariant. The Jones polynomial distinguishes $T_{2,3}$ from $T_{2,3}^{\sigma}$: $J_{T_{2,3}}(q) \neq J_{T_{2,3}^{\sigma}}(q)$. Continuous deformation cannot interconvert them.

**Three routes to chirality reversal in the QOU.**

The theory admits three mechanisms:

1. **Passage through the exceptional divisor.** The [fiber adjoint involution](#prop:fiber-adjoint-involution) reverses Reeb flow. Extended to the [exceptional divisor](#def:exceptional-divisor), it maps $T_{2,3}$ to $T_{2,3}^{\sigma}$. This is a discrete jump (pair creation), destroying the knot type and creating its mirror.
2. **Complex aether rotation.** The pre-observable sector ([complex aether interpretation](#rem:complex-substrate-interpretation)) allows continuous phase rotation of $q$ via $\mathcal{X}_\varphi$. The [chirality rotation conjecture](#conj:complex-chirality-rotation) identifies the discrete flip $T_{2,3} \leftrightarrow T_{2,3}^{\sigma}$ as the $\mathbb{Z}_2$ shadow of this $\mathrm{U}(1)$ rotation.
3. **Reconnection as Reidemeister move.** Classical reconnections represent local Reidemeister moves (R-II). R-II moves alter embedding and crossing energy without changing knot type. Writhe changes by $\pm 2$, corresponding to orbital shell transitions. Changing knot type requires surpassing a topological barrier.

**Summary.**
A classical trefoil vortex unties and dissipates. The categorical trefoil is topologically stable. Its chirality is protected against continuous deformation. Reversal requires either discrete passage through the exceptional divisor or continuous pre-observable complex rotation.

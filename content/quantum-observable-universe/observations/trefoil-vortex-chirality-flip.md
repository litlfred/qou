The open question posed in the [chirality remark](#rem:chirality-trefoil-electron-positron) — *can a vortex tube in the brane fluid reverse its circulation?* — has a sharp answer in classical fluid dynamics. The gap between that answer and the categorical framework is itself informative.

**Classical result: trefoil vortices are unstable.**
Kleckner and Irvine \cite{kleckner2013} created trefoil-knotted vortex loops in water and tracked their evolution. The trefoil vortex unties itself within a few circulation timescales via vortex reconnection events. Two anti-parallel filament segments approach, reconnect, and separate with exchanged topology. Scheeler et al. \cite{scheeler2014} showed that helicity $\mathcal{H} = \int \mathbf{v} \cdot \boldsymbol{\omega} dV$ is approximately conserved during reconnection but redistributes from writhe (global coiling) to twist (local spinning):

$$
  \mathcal{H} =  \underbrace{Wr}_{\text{writhe}}
  +  \underbrace{Tw}_{\text{twist}}, \qquad
  \Delta Wr = -\Delta Tw \quad (\text{during reconnection}).
$$

After several reconnections the trefoil reduces to unknotted loops. Each loop carries a portion of the original helicity as twist. No chirality flip occurs. The trefoil dissolves.

**Obstructions to classical chirality reversal.**

Three obstructions prevent a smooth chirality reversal in Navier--Stokes fluid dynamics:

1. **Kelvin's theorem.** In ideal fluids, circulation $\Gamma = \oint \mathbf{v} \cdot d\mathbf{l}$ around a material loop is conserved. Reversing the sign of $\Gamma$ requires external forcing or viscous dissipation. It cannot happen spontaneously in an inviscid flow.
2. **Topological protection of writhe sign.** The writhe $Wr$ of a trefoil is $\pm 3$. To flip from $+3$ to $-3$ requires passing through $Wr = 0$ (the unknot). The trefoil must first untie completely and then re-tie with opposite handedness. Reconnection events only reduce $|Wr|$.
3. **Dissipation at reconnection sites.** Each reconnection event converts kinetic energy into heat via viscous dissipation. The trefoil has three essential crossings. Complete untying dissipates energy $\sim 3 \Gamma^2 \rho$ (per unit length). There is no energy budget for re-tying.

**The categorical trefoil is different.**
In the QOU framework, the trefoil is not a fluid-dynamical vortex filament. It is an element of the representation ring of $\mathrm{SU}_q(2)$.

| Property | Classical vortex | Categorical trefoil |
|----------|-----------------|---------------------|
| Identity | Embedding $S^1 \hookrightarrow \mathbb{R}^3$ | Knot type (isotopy class) |
| Stability | Reconnection-unstable | Topologically protected |
| Circulation | Continuous $\Gamma \in \mathbb{R}$ | Quantised by Casimir $[j]_q[j+1]_q$ |
| Chirality | Sign of $Wr$ (embedding-dependent) | Knot invariant (left vs right trefoil) |
| Helicity transfer | $Wr \leftrightarrow Tw$ | No classical analogue; encoded in $R$-matrix |

The categorical trefoil's chirality is a knot invariant, not an embedding property. The Jones polynomial distinguishes $T_{2,3}$ from $T_{2,3}^{\sigma}$: $J_{T_{2,3}}(q) \neq J_{T_{2,3}^{\sigma}}(q)$. No continuous deformation can convert one to the other.

**Three routes to chirality reversal in the QOU.**

The theory offers three mechanisms for chirality reversal:

1. **Passage through the exceptional divisor.** The [fiber adjoint involution](#prop:fiber-adjoint-involution) reverses the Reeb flow direction. If it extends to the [exceptional divisor](#def:exceptional-divisor), it maps $T_{2,3}$ to $T_{2,3}^{\sigma}$. This is not a continuous deformation but a discrete jump at the blow-up locus. It is the categorical analogue of a pair-creation event. The knot type is destroyed and its mirror is created.
2. **Complex substrate rotation.** In the pre-observable sector ([complex substrate interpretation](#rem:complex-substrate-interpretation)), the chirality operator $\mathcal{X}_\varphi$ rotates the phase of $q$ continuously. The [chirality rotation conjecture](#conj:complex-chirality-rotation) proposes that the discrete flip $T_{2,3} \leftrightarrow T_{2,3}^{\sigma}$ is the $\mathbb{Z}_2$ shadow of a continuous $\mathrm{U}(1)$ rotation in the $\theta$-direction. Upon projection to the observable sector ($\theta = 0$), only the endpoints of this rotation survive as particle and antiparticle.
3. **Reconnection as Reidemeister move.** The classical reconnection events correspond to local Reidemeister moves (R-II). In the categorical setting, R-II moves do not change the knot type. They change the embedding, altering crossing energy and binding energy while leaving the bare mass and particle identity invariant. The writhe $Wr$ changes by $\pm 2$ per R-II move. This physically corresponds to orbital shell transitions, not chirality reversal. To change the knot type requires crossing a topological barrier that R-II moves cannot surmount.

**Summary.**
A classical trefoil vortex in a real fluid cannot flip chirality. It unties and dissipates. The categorical trefoil is topologically stable and its chirality is a knot invariant, protected against continuous deformation. Chirality reversal requires either a discrete passage through the exceptional divisor (pair creation), a continuous rotation in the pre-observable complex-$q$ sector, or both. The classical vortex reconnection phenomenon maps to shell transitions (R-II Reidemeister moves), not chirality reversal.

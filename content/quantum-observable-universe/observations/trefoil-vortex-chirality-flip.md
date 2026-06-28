The open question posed in the
[chirality remark](#rem:chirality-trefoil-electron-positron) — *can a
vortex tube in the brane fluid reverse its circulation?* — has a
sharp answer in classical fluid dynamics, and the gap between that
answer and the categorical framework is itself informative.

**Classical result: trefoil vortices are unstable.**
Kleckner and Irvine \cite{kleckner2013} created trefoil-knotted vortex
loops in water using 3D-printed hydrofoils and tracked their evolution
with high-speed imaging. The trefoil vortex **untied itself** within
a few circulation timescales via a sequence of local **vortex
reconnection** events: two anti-parallel filament segments approach,
reconnect, and separate with exchanged topology. Scheeler et al.
\cite{scheeler2014} showed that helicity — the integral
$\mathcal{H} = \int \mathbf{v} \cdot \boldsymbol{\omega} dV$ — is
approximately conserved during reconnection but is redistributed from
writhe (global coiling) to twist (local spinning):

$$
  \mathcal{H} =  \underbrace{Wr}_{\text{writhe}}
  +  \underbrace{Tw}_{\text{twist}}, \qquad
  \Delta Wr = -\Delta Tw \quad (\text{during reconnection}).
$$

After several reconnections the trefoil reduces to unknotted loops,
each carrying a portion of the original helicity as twist. **No
chirality flip occurs** — the trefoil dissolves.

**Obstructions to classical chirality reversal.**

Three obstructions prevent a smooth chirality reversal in
Navier--Stokes fluid dynamics:

1. **Kelvin's theorem** (ideal fluids): circulation
 $\Gamma = \oint \mathbf{v} \cdot d\mathbf{l}$ around a material
 loop is conserved. Reversing the sign of $\Gamma$ (the
 circulation analogue of chirality reversal) requires external
 forcing or viscous dissipation — it cannot happen spontaneously
 in an inviscid flow.

2. **Topological protection of writhe sign.** The writhe $Wr$ of
 a trefoil is $\pm 3$ (sign determined by chirality). To flip
 from $+3$ to $-3$ requires passing through $Wr = 0$, which is
 the unknot — the trefoil must first untie completely and then
 re-tie with opposite handedness. But reconnection events only
 reduce $|Wr|$ (they cannot increase it without external energy
 injection), so the vortex untangles before it could ever flip.

3. **Dissipation at reconnection sites.** Each reconnection event
 converts a finite amount of kinetic energy into heat via viscous
 dissipation at the approach zone (scale $\sim \nu / \Gamma$).
 The trefoil has three essential crossings, so complete untying
 dissipates energy $\sim 3 \Gamma^2 \rho$ (per unit length).
 There is no energy budget for re-tying.

**The categorical trefoil is different.**
In the QOU framework, the trefoil is *not* a fluid-dynamical
vortex filament — it is an element of the representation ring of
$\mathrm{SU}_q(2)$. The key distinctions are:

| Property | Classical vortex | Categorical trefoil |
|----------|-----------------|---------------------|
| Identity | Embedding $S^1 \hookrightarrow \mathbb{R}^3$ | Knot type (isotopy class) |
| Stability | Reconnection-unstable | Topologically protected |
| Circulation | Continuous $\Gamma \in \mathbb{R}$ | Quantised by Casimir $[j]_q[j+1]_q$ |
| Chirality | Sign of $Wr$ (embedding-dependent) | Knot invariant (left vs right trefoil) |
| Helicity transfer | $Wr \leftrightarrow Tw$ | No classical analogue; encoded in $R$-matrix |

The categorical trefoil's chirality is a **knot invariant**, not an
embedding property. The Jones polynomial distinguishes
$T_{2,3}$ from $T_{2,3}^{\sigma}$: $J_{T_{2,3}}(q) \neq J_{T_{2,3}^{\sigma}}(q)$.
No continuous deformation (Reidemeister moves) can convert one to the
other.

**Three routes to chirality reversal in the QOU.**

Despite the topological protection, the theory offers three mechanisms
by which chirality can reverse — none of which are available in
classical fluids:

1. **Passage through the exceptional divisor.** The
 [fiber adjoint involution](#prop:fiber-adjoint-involution) reverses
 the Reeb flow direction and, if it extends to the
 [exceptional divisor](#def:exceptional-divisor), maps $T_{2,3}$
 to $T_{2,3}^{\sigma}$. This is not a continuous deformation
 of the knot but a **discrete jump** at the blow-up locus — the
 categorical analogue of a pair-creation event. The trefoil vortex
 does not "unwind"; instead, it passes through a singular point
 where the old knot type is destroyed and a new one (the mirror)
 is created.

2. **Complex substrate rotation.** In the pre-observable sector
 ([complex substrate interpretation](#rem:complex-substrate-interpretation)),
 the chirality operator $\mathcal{X}_\varphi$ rotates the phase
 of $q$ continuously. The
 [chirality rotation conjecture](#conj:complex-chirality-rotation)
 proposes that the discrete flip $T_{2,3} \leftrightarrow
   T_{2,3}^{\sigma}$ is the $\mathbb{Z}_2$ shadow of a continuous
 $\mathrm{U}(1)$ rotation in the $\theta$-direction. After
 projection to the observable sector ($\theta = 0$), only the
 endpoints of this rotation survive as particle and antiparticle.

3. **Reconnection as Reidemeister move.** The classical
 reconnection events of Kleckner--Irvine correspond to local
 Reidemeister moves (R-II: addition/removal of crossing pairs).
 In the categorical setting, R-II moves do not change the
 knot type — they change the *embedding* (and hence the
 crossing energy and binding energy) but leave the bare mass
 and particle identity invariant. The writhe $Wr$ changes by
 $\pm 2$ per R-II move, which physically corresponds to
 orbital shell transitions, *not* chirality reversal. To change
 the knot type requires crossing a topological barrier that R-II
 moves cannot surmount.

**Summary.**
A classical trefoil vortex in a real fluid *cannot* flip chirality —
it unties and dissipates. The categorical trefoil is topologically
stable and its chirality is a knot invariant, protected against any
continuous deformation. Chirality reversal requires either (a) a
discrete passage through the exceptional divisor (pair creation),
(b) a continuous rotation in the pre-observable complex-$q$ sector,
or (c) both — with the discrete event being the observable shadow of
the continuous rotation. The classical vortex reconnection phenomenon
maps not to chirality reversal but to **shell transitions** (R-II
Reidemeister moves that change the writhe while preserving the
knot type).

The Reeb vector field $\xi_q$
([$q$-Reeb vector field](#ex:q-reeb-vector-field)) is the dynamical
complement to the static topology of the Bring's surface.  While the
surface itself provides the handles (genus $4$), the Reeb vector
provides the "wind" blowing through them, and the substrate parameter $q$
([substrate parameter](#def:substrate-parameter)) sets the strength of
that wind.

**The classical limit ($q\to 1$): cones and frozen geometry.**
If the substrate parameter $q\to 1$
([substrate parameter](#def:substrate-parameter)), the
torsion coupling vanishes and the phase rotation
$w_k\mapsto\zeta^k\,w_k$ loses its temporal component.  The fibre
over each base point ceases to twist as one moves along a path on
$\mathbb{P}^1(\mathbb{C})$: the chiral tubes are frozen in the configuration
determined by the power-sum equations.  Metrically this is a conical
limit---the curvature concentrates at the blow-up points but no
circulating torsion field smooths it out.  In terms of the Reeb
flow ([$q$-Reeb flow](#ex:q-reeb-flow)), $\xi_q\to\xi_1=\xi$ becomes
the classical Reeb field, and the Heisenberg commutator
$[\hat{X},\hat{P}]_q\to 0$
([Heisenberg commutator](#rem:heisenberg-commutator)): the Bring variety
collapses to a non-rotating algebraic surface.

**Exceptional divisor as mixing interface.**
Blowing up a spacetime defect $z_c$ where chiral sheets merge
([Bring's surface smoothness](#rem:brings-smoothness)) replaces the singular point with
an exceptional divisor $\mathcal{S}_c\cong\mathbb{P}^1(\mathbb{C})\cong S^2$.  This
sphere acts as the boundary between the macroscopic coordinates
$(x_0,x_1)$ and the internal chiral modes $(w_1,w_2,w_3)$: the
self-intersections of the chiral fibres are resolved, and the
$C_5$ phase rotation now circulates *around* the exceptional
divisor rather than passing through a singularity.

**Reeb bundle and torsion field.**
On the blown-up surface, the Reeb vector field $\xi_q$ is the
infinitesimal generator of the $U(1)$ action that rotates the chiral
fibre above the exceptional divisor.  The total space of this
$U(1)$ fibration is the **Reeb bundle**:
$U(1) \hookrightarrow S^3 \xrightarrow{\pi_H} \mathcal{S}_c \cong S^2$.
The $q$-deformed Reeb flow $\phi_t^q$
([$q$-Reeb flow](#ex:q-reeb-flow)) restricted to $\mathcal{S}_c$ generates
this Hopf fibration, and the substrate
parameter $q$ controls the pitch of the rotation.  The vector
field $\xi_q$ thereby provides the "time-like" direction within the
chiral space: it is the flow that allows the spectral modes $w_k$ to
execute the spinning phase rotation
$w_k\mapsto\zeta^k\,w_k$.  All braiding --- Hecke generators,
Skein resolutions, crossing changes --- takes place within this
Reeb bundle
([vertex is the exceptional divisor](#prop:vertex-is-exceptional-divisor)).

**Global picture.**
The Bring's surface provides the genus-$4$ topology---four handles
through which the chiral tubes thread.  The Reeb vector field gives
the longitudinal flow along these handles.  The substrate parameter $q$
modulates the pitch of this flow: when $q\to\infty$ (deep-quantum,
Big Bang) the spinning is maximal and the Heisenberg uncertainty
$[\hat{X},\hat{P}]_q\to J$; when $q\to 1$ (heat death) the spinning
ceases, the Reeb field trivialises, and the topology reduces to a
static cone.

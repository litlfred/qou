Let $K$ be an archimedean field.  A quantum universe over $K$
([quantum universe](#def:quantum-universe)) is realised by a $5$-tuple
$(M, \theta, G, P, E)$: here $M$ is the spacetime (a CR manifold),
$\theta$ encodes the contact geometry and Reeb structure,
$G = \mathrm{SU}(2)$ is the gauge group, $P$ is the gauge bundle,
and $E$ is the state bundle carrying the quantum degrees of freedom.
The precise requirements are:

1. $M$ is a CR manifold of hypersurface type
   (real dimension $2n+1$, $n \geq 1$) with non-degenerate Levi form
   of signature $(r,s)$, $r + s = n$;
2. $\theta$ is a pseudo-Hermitian structure (contact form) on $M$,
   determining the Levi distribution $H = \ker\theta$, the Reeb vector
   field $\xi$, the Webster metric $g_\theta$ (of signature $(2r,2s)$
   on $H$), and the Levi form $L_\theta$;
3. $G = \mathrm{SU}(2)$;
4. $P \to M$ is a principal $G$-bundle whose holonomy reduces to
   $\mathrm{SO}(3) \subset \mathrm{SU}(2)/\{\pm I\}$;
5. $E = P \times_G \mathbb{P}^1(\mathbb{C}) \to M$ is the associated
   *state bundle*, where $\mathrm{SU}(2)$ acts on
   $\mathbb{P}^1(\mathbb{C})$ by Mobius transformations.

The monoidal category is $\mathcal{C} = \mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$
(the representation category of the quantum group at the substrate
parameter $q(p)$, [substrate parameter](#def:substrate-parameter)), the
Frobenius--Hopf object is
$A = \mathcal{O}_q(\mathrm{SU}(2))$ with Frobenius form given by the
Haar state, and the fibre functor $\tau$ is the forgetful functor
to $K\text{-}\mathrm{Mod}$.

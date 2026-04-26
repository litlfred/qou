Let $K$ be an archimedean field.  A quantum universe over $K$
([quantum universe](#def:quantum-universe)) is realised by the $4$-tuple
$(\mathbf{C}, \varTheta, G, \mathcal{S})$: here
$\varTheta$ is a contact form on a CR manifold $M$ (encoding the contact
geometry and Reeb structure),
$G = \mathrm{SU}(2)$ is the gauge group, and
$\mathcal{S}$ is the state bundle carrying the quantum degrees of freedom.
The base manifold $M$ is implicit as the domain of $\varTheta$; the
principal bundle $P$ is implicit as the frame bundle of $\mathcal{S}$
under $G$.  The precise requirements are:

1. $M$ (the domain of $\varTheta$) is a CR manifold of hypersurface type
   (real dimension $2n+1$, $n \geq 1$) with non-degenerate Levi form
   of signature $(r,s)$, $r + s = n$;
2. $\varTheta$ is a pseudo-Hermitian structure (contact form) on $M$,
   determining the Levi distribution $H = \ker\varTheta$, the Reeb vector
   field $\xi$, the Webster metric $g_\varTheta$ (of signature $(2r,2s)$
   on $H$), and the Levi form $L_\varTheta$;
3. $G = \mathrm{SU}(2)$;
4. $\mathcal{S} = P \times_G \mathbb{P}^1(\mathbb{C}) \to M$ is the
   associated *state bundle*, where $P \to M$ is the principal
   $G$-bundle (with holonomy reducing to
   $\mathrm{SO}(3) \subset \mathrm{SU}(2)/\{\pm I\}$) and
   $\mathrm{SU}(2)$ acts on $\mathbb{P}^1(\mathbb{C})$ by Möbius
   transformations.

The monoidal category is $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$
(the representation category of the quantum group at the substrate
parameter $q(p)$, [substrate parameter](#def:substrate-parameter)), the
Frobenius--Hopf object is
$A = \mathcal{O}_q(\mathrm{SU}(2))$ with Frobenius form given by the
Haar state, and the fibre functor $\tau$ is the forgetful functor
to $K\text{-}\mathrm{Mod}$.

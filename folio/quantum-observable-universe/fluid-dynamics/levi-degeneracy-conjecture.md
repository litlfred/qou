**Setting.** Let $D$ be $\mathbb{R}^3$ or $\mathbb{T}^3$. This is the three-dimensional flow domain, not the state bundle $\mathcal{S}$, which the chapter also uses as a surface. Let $u$ be a smooth solution of the unforced Navier--Stokes equations on $D \times [0, T^\ast)$, with vorticity $\omega$ and vorticity direction $\xi = \omega/|\omega|$ where $\omega \neq 0$. Following the [core Levi form proposition](#prop:core-levi-form), the plane field is $\ker\varTheta = \xi^\perp$ with $\varTheta = f\,\xi^\flat$, and its Levi datum is the scalar $\xi\cdot\mathrm{curl}\,\xi$. For $\Omega > 0$ write $H_\Omega(t) = \{x : |\omega(x, t)| > \Omega\}$ for the high-vorticity set.

**Conjecture (Levi degeneracy, branch (B)).** If for some $\Omega > 0$ the Levi scalar $\xi\cdot\mathrm{curl}\,\xi$ vanishes on $H_\Omega(t)$ for every $t < T^\ast$, then $u$ does not blow up at $T^\ast$.

**Status of the conjecture.** It is open, and no standard result supports it. The Constantin--Fefferman criterion \cite{constantin1993} and its improvement by Beirão da Veiga and Berselli \cite{beiraodaveiga2002} give regularity from coherence of the line field $[\xi]$ on $H_\Omega$. That hypothesis bounds all of $\nabla\xi$ from above. Vanishing of $\xi\cdot\mathrm{curl}\,\xi$ fixes one component of $\nabla\xi$ and does not imply it. Non-vanishing does not imply it either.

**Branch (A) is withdrawn.** The former branch (A) read "the Levi data stays bounded and non-degenerate at the collision, hence Navier--Stokes blows up". With $\varTheta = f\,\xi^\flat$ this implication is false. On $\mathbb{T}^3$ take

$$
  u(x, t) = e^{-\nu t}\,(\sin z,\ \cos z,\ 0).
$$

Then $\mathrm{curl}\,u = u$, so $\omega = u$ and $\xi = (\sin z, \cos z, 0)$. The advection term $(u\cdot\nabla)u = u_3\,\partial_z u$ vanishes, so with $p \equiv 0$ the field is an exact, global, smooth solution of the unforced equations. Its Levi scalar is $\xi\cdot\mathrm{curl}\,\xi = 1$ everywhere, so $\ker\varTheta$ is a contact structure on all of $\mathbb{T}^3$, and $|\omega| = e^{-\nu t}$ stays bounded. This refutes the implication under the reading $\varTheta = f\,\xi^\flat$, with the explicit solution as the invariant. It does not address any reading the chapter has not stated.

**The growth exponent is withdrawn with it.** The previous statement was a trichotomy on $\beta = \limsup_\kappa \log\mathcal{C}_L(\kappa)/\log\kappa$, where $\mathcal{C}_L$ is the Levi condition number along a root-of-unity ladder $q_\kappa \to 1$. In dimension $3$ the Levi form of a plane field is $1\times 1$, so $\mathcal{C}_L$, $\beta$ and the marginal window $0 < \beta < 1$ are undefined. Records computed for $\mathcal{C}_L$ remain valid as statements about the core aspect ratio of [the Townsend model](#rem:townsend-biot-savart-strain), not as Levi data.

**What is true: a necessary condition for blow-up (standard, cited).** Let $u$ be a smooth solution of the unforced equations on $D\times[0, T^\ast)$, in the class of \cite{beiraodaveiga2002}. If $u$ blows up at $T^\ast$, then for every $\Omega > 0$ and $C \geq 0$ there are $t < T^\ast$ and $x, y \in H_\Omega(t)$ with

$$
  |\sin\angle(\xi(x, t), \xi(y, t))| > C\,|x - y|^{1/2}.
$$

This is the contrapositive of the Beirão da Veiga--Berselli theorem. The Lipschitz form of Constantin--Fefferman follows a fortiori. In words, blow-up forces the vorticity line field to lose $\tfrac{1}{2}$-Hölder control on the high-vorticity set.

For a straight anti-parallel vortex pair the line field is constant, so this necessary condition fails and no blow-up occurs. A realisation of the [Navier--Stokes counterexample conjecture](#conj:ns-counterexample) by smooth solutions would therefore need the filaments to bend or twist without bound inside the high-vorticity set. This applies to the chapter's $q \to 1$ limit flow only if that flow is a smooth solution on $[0, T^\ast)$, which is not established here.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Generic categorical identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.

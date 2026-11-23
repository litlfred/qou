The proof proceeds in the rigid :refterm[monoidal category]{#monoidal-category} underlying the quantum
observable universe.  Let $A$ denote the Frobenius--Hopf object
representing the gauge-bundle data of $(\mathbf{C}, \varTheta, G, \mathcal{S})$.

The tangent algebra $T(A) := \mathrm{Sym}_A(\Omega^1_{A/R})$ is an object of the
ambient category, and for $A = \mathcal{O}(G)$ it is the coordinate Hopf algebra of
the tangent group $TG$, with Hopf data $(\Delta', \varepsilon', S')$ for which the
structure map $A \to T(A)$ and the augmentation $T(A) \to A$ are Hopf maps.

*No Frobenius form at level $n \ge 1$.*
The statement does not ask for a Frobenius form on $T(A)$. A Haar-type form is excluded: a left integral on the coordinate algebra $k[X]$ of the additive group kills every derivative, since $p(X + \varepsilon) = p(X) + \varepsilon\, p'(X)$ with $\varepsilon^2 = 0$, so it vanishes in characteristic zero; and $TG$ contains the vector group $\mathrm{Lie}(G)$.

*Geometric realisation.*
Applying the fibre functor $\tau\colon \mathbf{C} \to \mathrm{Vect}_k$
recovers the geometric data: $\tau(T(A))$ is the space of sections of the
tangent bundle $T\mathcal{S}$, the frame bundle $P'$ is the geometric counterpart of the Hopf
structure on $T(A)$, and the connection $A'$ is the image under $\tau$
of the comultiplication $\Delta'$.  $\square$

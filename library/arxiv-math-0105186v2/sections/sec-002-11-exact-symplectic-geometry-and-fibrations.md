---
doc_id: arxiv-math-0105186v2
doc_title: "A long exact sequence for symplectic Floer cohomology"
section_id: sec-002-11-exact-symplectic-geometry-and-fibrations
section_title: "Exact symplectic geometry and fibrations"
section_number: 1.1
pages: 4-10
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.609
latex_coverage_ratio: 0.985
doc_brief: "A long exact sequence for symplectic Floer cohomology — 17 sections: Front matter; Introduction; Dehn twists, and all that"
---
By an exact symplectic manifold we mean a compact manifold $M$ with boundary, together with a symplectic form $\o$ and a one-form $\theta$ satisfying $d\theta = \o$, such that $\theta|\partial M$ is a contact one-form and makes $\partial M$ convex. An isomorphism of exact symplectic manifolds is a diffeomorphism $\phi: M \rightarrow M'$ which is symplectic, satisfies $\phi^*\theta' = \theta$ in some neighbourhood of $\partial M$, and such that $[\phi^*\theta' - \theta] \in H^1(M,\partial M;\R)$ is zero. This means that there is a unique function $K_\phi \in \smooth_c(M \setminus \partial M,\R)$ such that $\phi^*\theta' = \theta + dK_\phi$. We denote by $\Sympe(M)$ the group of those exact symplectic automorphisms of $M$ which are the identity near $\partial M$. Its Lie algebra consists of vector fields $X$ such that $\o(\cdot,X) = dH$ for some $H$ which vanishes near $\partial M$, and is thus identified with $\smooth_c(M \setminus \partial M,\R)$.

An exact Lagrangian submanifold in $M$ is a pair consisting of a Lagrangian submanifold $L \subset M$ (always assumed to be disjoint from $\partial M$) and a function $K_L$ on it such that $dK_L = \theta|L$. The image of $L$ under an isomorphism $\phi: M \rightarrow M'$ of exact symplectic manifolds is again an exact Lagrangian submanifold, in a canonical way; the associated function is $$\label{eq:induced-k}
K_{\phi(L)} = (K_L + K_\phi|L) \circ \phi^{-1}.$$ In particular, $\Sympe(M)$ acts on the set of exact Lagrangian submanifolds. A special situation which will occur later on is that $\phi \in \Sympe(M)$ satisfies $\phi(L) = L$ in the ordinary sense. Then (supposing $L$ to be connected) $K_{\phi(L)} = K_L + c$ for some constant $c = K_\phi|L$, which needs not be zero. This means that $\phi$ may not map $L$ to itself as an exact Lagrangian submanifold, instead "shifting" it by some amount.

A notion of fibre bundle suitable for exact symplectic geometry is as follows. Let $S$ be a smooth connected manifold, possibly with boundary (one could also allow corners), and $\pi: E \rightarrow S$ a differentiable fibre bundle whose fibres are compact manifolds with boundary. Write $\partial_hE \subset E$ for the union of the boundaries of all the fibres. If the boundary of $S$ is empty, $\partial_hE = \partial E$; otherwise $\partial E$ has another face $\partial_vE = \pi^{-1}(\partial S)$, and the two faces meet at a codimension two corner. An exact symplectic fibration is such an $(E,\pi)$ equipped with $\Omega \in \Omega^2(E)$ and $\Theta \in \Omega^1(E)$, satisfying $d\Theta =
\Omega$, such that each fibre $E_z$ with $\o_z = \Omega|E_z$ and $\theta_z =
\Theta|E_z$ is an exact symplectic manifold. There is an additional condition of triviality near $\partial_hE$, by which we mean the following: choose some $z \in S$ and consider the trivial fibration $\tilde{\pi} : \tilde{E} = S
\times E_z \rightarrow S$, with the forms $\tilde{\Omega},\tilde{\Theta}$ which are pullbacks of $\o_z,\theta_z$. There should be a fibrewise diffeomorphism $$\label{eq:boundary-trivialization}
\xymatrix{
 {N} \ar[rr] \ar[dr]_{\pi} && {\tilde{N}} \ar[dl]^{\tilde{\pi}} \\
 & {S} &
}$$ betweeen neighbourhoods $N \subset E$, $\tilde{N} \subset \tilde{E}$ of $\partial_hE$ resp. $\partial_h\tilde{E}$, which maps $\partial_hE$ to $\partial_h\tilde{E}$, equals the identity on the fibre over $z$, and sends $\Omega,\Theta$ to $\tilde{\Omega},\tilde{\Theta}$. Note that the choice of $z$ and the diffeomorphism are not considered to be part of the data defining an exact symplectic fibration; only their existence is assumed.

::: lemma
[]{#th:fibre-bundles label="th:fibre-bundles"} Take a point $z \in S$ and a chart $\psi: U \rightarrow S$, with $U \subset
\R^k$ a contractible neighbourhood of $0$, such that $\psi(0) = z$. Then there is a trivialization $\Psi: U \times E_z \rightarrow \psi^*E$, such that $\Psi\,|\,\{0\} \times E_z = \id$ and $$\Psi^*\Theta = \theta_z + \sum_{i=1}^k H_i dt_i + dR.$$ Here $H_1,\dots,H_k,R \in \smooth(U \times E_z,\R)$ are functions which vanish near $U \times \partial E_z$, and $t_i$ the coordinates on $\R^k$. Moreover, the difference between any two such trivializations $\Psi_1,\Psi_2$ is a map $\Psi_2^{-1} \circ \Psi_1: (U,0) \rightarrow (\Sympe(E_z),\id)$. 0◻
:::

The proof is by a standard argument involving Moser's Lemma. The result means first of all that any exact symplectic fibration $(E,\pi)$ has a structure of $\Sympe(E_z)$-fibre bundle, where $E_z$ is any fibre. In addition to that, $E$ carries a preferred connection, which gives rise to canonical parallel transport maps $\rho_c: E_{c(a)} \rightarrow E_{c(b)}$ over smooth paths $c:
[a;b] \rightarrow S$; these are exact symplectic isomorphisms, and lie in $\Sympe(E_{c(a)})$ if $c$ is closed. To define the preferred connection, one can use a local trivialization as before and set $A = \sum_i H_i\,dt_i$, which is a one-form on $U$ with values in $\smooth_c(E_z \setminus \partial E_z,\R)$. It is easy to check that this transforms in the proper way. A more intrinsic approach is to observe that $TE_x = TE^h_x \oplus TE^v_x$ splits into a horizontal and a vertical piece, given by $TE^v_x = \ker(D\pi_x)$ and $$\label{eq:connection}
TE^h_x = \{X \in TE_x \suchthat \Omega(X,\cdot)|TE^v_x = 0\}.$$ Each $Z \in TS_z$ has a unique lift $Z^h \in \smooth(TE^h|E_z)$, and these vectors define the same connection as before (conversely, one can show that given a $\Sympe(M)$-fibre bundle and a compatible connection, one can equip its total space with the structure of an exact symplectic fibration). In a local trivialization as in Lemma [\[th:fibre-bundles\]](#th:fibre-bundles){reference-type="ref" reference="th:fibre-bundles"}, the curvature of the connection is $$\label{eq:curvature}
F_A = \sum_{i<j} \left( -\frac{\partial H_i}{\partial t_j} + \frac{\partial
H_j}{\partial t_i} - \o_z(X_i,X_j) \right) dt_i \wedge dt_j,$$ where $X_i$ is the family of Hamiltonian vector fields on $E_z$ corresponding to $H_i(t,\cdot)$. If one takes the more intrinsic view, the curvature is a two-form on $S$ with values in functions on the fibres, and is given by $(Z_1,Z_2) \mapsto \Omega(Z_1^h,Z_2^h)$. In the case where the base $S$ is an oriented surface, we say that $(E,\pi)$ is nonnegatively curved if for any oriented chart $\psi$ and trivialization $\Psi$, the function in front of $dt_1
\wedge dt_2$ in [\[eq:curvature\]](#eq:curvature){reference-type="eqref" reference="eq:curvature"} is nonnegative; or equivalently, if $\Omega|TE^h$ is nonnegative for the induced orientation of $TE^h$. To see what this means, consider an exact symplectic fibration $(E,\pi)$ over the closed unit disc $\bar{D}(1) \subset \C$, and the monodromy $\rho = \rho_{\partial
\bar{D}(1)} : E_1 \rightarrow E_1$ around the boundary in positive sense. If the curvature is nonnegative, one can write $\rho$ as time-one map of some (time-dependent) Hamiltonian on $E_1$ which vanishes near $\partial E_1$ and is $\leq 0$ everywhere.

::: example
[]{#ex:mapping-torus label="ex:mapping-torus"} Let $E^\rho = \R \times M / (t,x) \sim (t-1,\rho(x))$ be the mapping torus of $\rho \in \Sympe(M)$. To make this into an exact symplectic fibration over $S^1 = \R/\Z$, one chooses a function $R_\rho \in
\smooth(\R \times M,\R)$ such that $R_\rho(t-1,\rho(x)) = R_\rho(t,x)
- K_\rho(x)$, and then sets $\Omega_{E^\rho} = \o$, $\Theta_{E^\rho}
= \theta + dR_\rho$. The preferred connection is the one induced from the trivial connection on $\R \times M$, and its monodromy is $\rho$ itself. It is easy to prove that all exact symplectic fibrations over a circle are of this form.
:::

For future use, we make an observation on the compatibility of symplectic parallel transport with Lagrangian submanifolds. Let $c: [a;b] \rightarrow S$ be a smooth embedded path. Suppose that we have an exact Lagrangian submanifold in each fibre $E_{c(t)}$, depending smoothly on $t$; by this we mean a subbundle $Q \subset E|\im(c)$ such that each fibre $Q_{c(t)} \subset E_{c(t)}$ is Lagrangian, together with a $K_Q \in \smooth(Q,\R)$ whose restrictions $K_{Q_{c(t)}} = K_Q|Q_{c(t)}$ make the $Q_{c(t)}$ exact.

::: lemma
[]{#th:submanifold label="th:submanifold"} Assume that all the $Q_{c(t)}$ are connected. Then the following conditions are equivalent:

::: condensedlist
$\Omega|Q = 0$;

$\Theta|Q = dK_Q + \pi^*\kappa_Q$ for some $\kappa_Q \in \Omega^1(\im(c))$;

[]{#item:carry-along label="item:carry-along"} the maps $\rho_{c|[s;s']}: E_{c(s)} \rightarrow E_{c(s')}$ satisfy $\rho_{c|[s;s']}(Q_{c(s)}) = Q_{c(s')}$ for all $s,s'$. 0◻
:::
:::

The proof is straightforward. To be precise, [\[item:carry-along\]](#item:carry-along){reference-type="ref" reference="item:carry-along"} concerns $Q_{c(s)}$ as Lagrangian submanifolds only. Taking the functions into account and using [\[eq:induced-k\]](#eq:induced-k){reference-type="eqref" reference="eq:induced-k"} yields $$K_{\rho_{c|[s;s']}(Q_{c(s)})} = K_{Q_{c(s')}} + \int_{c|[s;s']} \kappa_Q.$$ Hence $\rho_{c|[s;s']}(Q_{c(s)}) = Q_{c(s')}$ holds in the sense of exact Lagrangian submanifolds iff $\kappa_Q = 0$, or what is the same, $\Theta|Q =
dK_Q$.

Just like any kind of fibre bundle with connection, exact symplectic fibrations can be manipulated by cut-and-paste methods. As an example, take two oriented surfaces $S^k$, $k = 1,2$, and boundary circles $C^k \subset \partial S^k$; and let $S$ be the surface obtained by identifying $C^1,C^2$ orientation-reversingly. Suppose that we have exact symplectic fibrations $(E^k,\pi^k,\Omega^k,\Theta^k)$ over $S^k$ whose monodromies around $C^k$, taken in opposite senses, coincide. Then, assuming additionally that $(E^k,\pi^k)$ is flat (has zero curvature) near $C^k$, one can construct from them an exact symplectic fibration $(E,\pi)$ over $S$. It is maybe useful to give some details of this. To start, take oriented collars $\psi^1: (-1;0]
\times \R/\Z \rightarrow S^1$, $\psi^2: [0;1) \times \R/\Z \rightarrow S^2$ around $C^1,C^2$ respectively, so that $S$ can be defined by using $\psi^2
\circ (\psi^1)^{-1}$ to identify the two circles. Our main assumption is that there should be an exact symplectic isomorphism between the fibres of $E^k$ over $\psi^k(0,0)$, say, which relates the monodromies around $\psi^k(\{0\}
\times \R/\Z)$. Because of flatness, an equivalent formulation is that there is some mapping torus $E^\rho$ as in Example [\[ex:mapping-torus\]](#ex:mapping-torus){reference-type="ref" reference="ex:mapping-torus"} and diffeomorphisms $$\xymatrix{
 {(-1;0] \times E^\rho} \ar[d] \ar[r]^-{\Psi^1} & {E^1} \ar[d]^{\pi^1} \\
 {(-1;0] \times \R/\Z} \ar[r]^-{\psi^1} & {S^1}
} \qquad \xymatrix{
 {[0;1) \times E^\rho} \ar[d] \ar[r]^-{\Psi^2} & {E^2} \ar[d]^{\pi^2} \\
 {[0;1) \times \R/\Z} \ar[r]^-{\psi^2} & {S^2}
}$$ such that $(\Psi^k)^*\Omega^k = \Omega_{E^\rho}$ and $(\Psi^k)^*\Theta^k =
\Theta_{E^\rho} + dR^k$ for some functions $R^k$. Clearly, one can introduce modified forms $\tilde{\Theta}^k = \Theta^k - d\tilde{R}^k$ with suitable functions $\tilde{R}^k$, in such a way that $(\Psi^k)^*\tilde{\Theta}^k =
\Theta_{E^\rho}$ near $\{0\} \times E^\rho$. Gluing together the $(E^k,\pi^k)$ along $C^k$ via $\Psi^2 \circ (\Psi^1)^{-1}$ yields a smooth fibration $(E,\pi)$ over $S$, and the $\Omega^k, \tilde{\Theta}^k$ match up to forms $\Omega,\Theta$ on it, making it an exact symplectic fibration. Since we have not changed the symplectic connection, nonnegativity of the curvature of $(E^k,\pi^k)$ implies the same for $(E,\pi)$.

::: remark
[]{#re:squeeze-boundary label="re:squeeze-boundary"} The flatness condition on $(E^k,\pi^k)$ near $C^k$ can be removed. Namely, suppose that it is not satisfied for $k = 1$. What one does then is to choose a function $g \in \smooth([-1;0],\R)$ such that $g(s) = s$ for $s$ close to $-1$, $g(s) = 0$ for $s$ close to $0$, and $g'(s) \geq 0$ everywhere; and define a self-map $p$ of the surface $S^1$ by $p(z) = z$ for $z \notin \im(\psi^1)$, $p(\psi^1(s,t)) = \psi^1(g(s),t)$. This collapses a small neighbourhood of $C^1$ onto that boundary circle, so if we replace $(E^1,\pi^1)$ by its pullback under $p$, it becomes flat near $C^1$, and the previous construction goes through. It is noteworthy that this still preserves nonnegative curvature, because $Dp$ has determinant $\geq 0$ everywhere.
:::

The basic objects of Picard-Lefschetz theory are fibrations over surfaces, where the fibres are allowed to have certain particularly simple singularities. Let $S$ be a connected oriented surface, possibly with boundary. An *exact Lefschetz fibration*[^1] over $S$ consists of data $(E,\pi,\Omega,\Theta,J_0,j_0)$ as follows. $E$ is a $(2n+2)$-dimensional manifold whose boundary is the union of two faces $\partial_hE$ and $\partial_vE$, meeting at a codimension two corner. $\pi: E
\rightarrow S$ is a proper map with $\partial_vE = \pi^{-1}(\partial S)$ (so this may be empty), and such that both $\pi|\partial_hE: \partial_hE
\rightarrow S$ and $\pi|\partial_vE: \partial_vE \rightarrow \partial S$ are smooth fibre bundles. $\pi$ can have at most finitely many critical points, and no two may lie on the same fibre (moreover, because of the previous assumptions, they must lie in the interior of $E$). Denote by $E^\crit \subset
E$, $S^\crit \subset S$ the set of critical points resp. of critical values. $J_0$ is an almost complex structure on a neighbourhood of $E^\crit$, and $j_0$ a positively oriented complex structure on a neighbourhood of $S^\crit$. These are such that $\pi$ is $(J_0,j_0)$-holomorphic near $E^\crit$, and the Hessian $D^2\pi$ at any critical point is nondegenerate as a complex quadratic form. The closed two-form $\Omega \in \Omega^2(E)$ must be nondegenerate on $TE_x^v =
\ker(D\pi_x)$ for each $x \in E$, and a Kähler form for $J_0$ in some neighbourhood of $E^\crit$. $\Theta \in \Omega^1(E)$ must satisfy $d\Theta =
\Omega$. We also require triviality near $\partial_hE$, which means the existence of a map [\[eq:boundary-trivialization\]](#eq:boundary-trivialization){reference-type="eqref" reference="eq:boundary-trivialization"} with the same properties as for exact symplectic fibrations. For brevity, exact Lefschetz fibrations will usually be denoted by $(E,\pi)$ alone, as we have already done for exact symplectic fibrations.

For any $x \in E$ there is a decomposition $TE_x = TE^h_x \oplus TE^v_x$ with $TE^h_x$ defined as in [\[eq:connection\]](#eq:connection){reference-type="eqref" reference="eq:connection"}; the horizontal part is zero at critical points, and projects isomorphically to $TS_z$, $z = \pi(x)$, at any other point. We say that an exact Lefschetz fibration has nonnegative curvature if $\Omega|TE^h_x \geq 0$ for each $x$. Note that if $x \notin E^\crit$ is close to a critical point, $\Omega|TE^h_x$ is strictly positive anyway, because of the Kählerness assumption on $\Omega$. A standard argument based on this shows

::: lemma
[]{#th:add-base label="th:add-base"} If $\beta \in \Omega^2(S)$ is a sufficiently positive two-form, $\Omega +
\pi^*\beta$ is a symplectic form on $S$. 0◻
:::

Symplectic parallel transport for an exact Lefschetz fibration is well-defined as long as one avoids the critical fibres; indeed, if one removes those fibres, the remainder is an exact symplectic fibration over $S \setminus S^\crit$. We now take a look at the structure of the critical points. Take $z_0 \in S^\crit$ and local $j_0$-holomorphic coordinates $\xi: U \rightarrow S$, where $U
\subset \C$ is a neighbourhood of the origin, such that $\xi(0) = z_0$. By assumption there is a unique critical point $x_0 \in E_{z_0}$. The holomorphic Morse Lemma says that one can find a neighbourhood of the origin $W \subset
\C^{n+1}$ and a $J_0$-holomorphic chart $\Xi: W \rightarrow E$ with $\Xi(0) =
x_0$, such that $$(\xi^{-1} \circ \pi \circ \Xi)(x) = x_1^2 + \dots + x_{n+1}^2$$ is the standard nondegenerate quadratic form on $\C^{n+1}$. We call $(\xi,\Xi)$ a holomorphic Morse chart. In general, it is not possible to choose $\Xi$ in such a way that $\Xi^*\Omega$ is the standard Kähler form on $W \subset
\C^{n+1}$; however, one can remedy this by a suitable local deformation.

::: lemma
[]{#th:local-deformation label="th:local-deformation"} Let $(E,\pi,\Omega,\Theta,J_0,j_0)$ be an exact Lefschetz fibration, and $x_0$ a critical point of $\pi$. Then there are smooth families $\Omega^\mu \in
\Omega^2(E)$, $\Theta^\mu \in \Omega^1(E)$, $0 \leq \mu \leq 1$, such that

::: condensedlist
$\Omega^0 = \Omega$, $\Theta^0 = \Theta$;

for all $\mu$, $\Omega^\mu = \Omega^0$ and $\Theta^\mu = \Theta^0$ outside a small neighbourhood of $x_0$;

each $(E,\pi,\Omega^\mu,\Theta^\mu,J_0,j_0)$ is an exact Lefschetz fibration;

there is a holomorphic Morse chart $(\xi,\Xi)$ around $x_0$ such that $\Xi^*\Omega^1$, $\Xi^*\Theta^1$ agree near the origin with the standard forms $\o_{\C^{n+1}} = \frac{i}{2} \sum dx_k \wedge d\bar{x}_k$, $\theta_{\C^{n+1}} =
\frac{i}{4} \sum x_k d\bar{x}_k - \bar{x}_k dx_k$.
:::
:::

The proof is based on an elementary local statement about Kähler forms.

::: lemma
[]{#th:kaehler label="th:kaehler"} Let $\o$ be a Kähler form on the ball $B = B^{2n+2}(r)$ of radius $r>0$ in $\C^{n+1}$. Then there is another Kähler form $\o'$ which agrees with $\o$ near $\partial B$, and which close to the origin is some small multiple of $\o_{\C^{n+1}}$.
:::

The first step is to find a Kähler form $\o''$ which is equal to $\o$ near $\partial B$, and which has constant coefficients near the origin. For this write[^2] $\o = \beta + dd^c f$, with $\beta$ constant and $f$ vanishing to second order at $x = 0$. Take a cutoff function $g \in
\smooth(\R^+,\R)$ such that $g(t) = 1$ for $t \leq 1$ and $g(t) = 0$ for $t
\geq 2$, and set $f_\epsilon(x) = g(||x||/\epsilon)f(x)$. A straightforward computation shows that as $\epsilon \rightarrow 0$, the functions $f_\epsilon$ not only have increasingly small support, but also tend to $0$ in the $C^2$ topology. The desired form is, for small $\epsilon$, $$\label{eq:ohalf}
\o'' = \o - dd^c f_\epsilon = \beta + dd^c (f - f_\epsilon).$$

In a second step, choose some small $t>0$ such that the constant form $\beta' =
\beta - t\o_{\C^{n+1}}$ is still Kähler. Take a two-form $\gamma$ on $\C^{n+1}$ which is of type (1,1) and nonnegative everywhere, which vanishes near the origin, and which is equal to $\o_{\C^{n+1}}$ outside a compact subset; this can be obtained as $\gamma = -dd^c h(||x||^2)$ for a suitable convex function $h$. Pulling $\gamma$ back by a linear map transforms it into another nonnegative (1,1)-form $\gamma'$, zero near the origin and equal to $\beta'$ outside a compact subset. Then $\gamma'' = \gamma' + t\o_{\C^{n+1}}$ is Kähler, equals $t\o_{\C^{n+1}}$ near the origin, and $\beta$ outside a compact subset. That compact subset can be made arbitrarily small by retracting linearly and rescaling; the two-form obtained in that way can be plugged into $\o''$ locally near zero, yielding $\o'$. 0◻

Take some holomorphic Morse chart $(\xi,\Xi)$ for $x_0$. Lemma [\[th:kaehler\]](#th:kaehler){reference-type="ref" reference="th:kaehler"} says that one can find a two-form $\Omega^1$ on $E$ which agrees with $\Omega = \Omega^0$ outside $\im(\Xi)$, such that $\Xi^*\Omega^1$ is Kähler and, near the origin, equals $c\, \o_{\C^{n+1}}$ for some small constant $c>0$. The obstruction to finding a $\Theta^1 \in \Omega^1(E)$ which agrees with $\Theta = \Theta^0$ outside $\im(\Xi)$ and satisfies $d\Theta^1 = \Omega^1$ lies in $H^2(B,\partial
B;\R)$, with $B$ a $(2n+2)$-dimensional ball; which is zero. An arbitrarily chosen $\Theta^1$ needs to be modified to make $\Xi^*\Theta^1$ equal to $c\,\theta_{\C^{n+1}}$ near $x = 0$, but that can be done by adding the differential of some function to it. By restricting $\xi,\Xi$ to smaller neighbourhoods, and rescaling them by $c^{-1/2}$ and $c^{-1}$ respectively, one achieves that $\Xi^*\Omega^1 = \o_{\C^{n+1}}$ and $\Xi^*\Theta^1 =
\theta_{\C^{n+1}}$ near the origin. Finally, $\Omega^\mu$ and $\Theta^\mu$ are defined by interpolating linearly between $\mu = 0$ and $1$; the required properties are obvious. 0◻

## The local model[]{#sec:model label="sec:model"}

Consider $T = T^*\!S^n$ with its standard forms $\o_T \in \Omega^2(T)$, $\theta_T \in \Omega^1(T)$. For concrete computations we use the coordinates $T
= \{ (u,v) \in \R^{n+1} \times \R^{n+1} \suchthat \leftsc u, v \rightsc = 0, \;
||v|| = 1 \}$. For each $\lambda>0$, the subspace $T(\lambda)$ of cotangent vectors of length $\leq \lambda$ is an exact symplectic manifold. We write similarly $T(0) \subset T$ for the zero-section. The length function $\mu: T
\rightarrow \R$, $\mu(u,v) = ||u||$, generates a Hamiltonian circle action $\sigma$ on $T \setminus T(0)$ which, after identifying $T \iso TS^n$ via the standard metric, can be described as the normalized geodesic flow on $S^n$. In coordinates $$\sigma_t(u,v) = (\cos(t)u - \sin(t) ||u|| v,\cos(t)v + \sin(t)\frac{u}{||u||}).$$ $\sigma_\pi$ is the antipodal involution $A(u,v) = (-u,-v)$, hence extends continuously over $T(0)$ (unlike any $\sigma_t$, $0 < t < \pi$). This can be used to define certain symplectic automorphisms of $T$. The construction is by now well-known, but we repeat it here since precise control over the parameters will be important later on.

::: lemma
[]{#th:on-invariant label="th:on-invariant"} Let $R \in \smooth(\R,\R)$ be a function which vanishes for $t \gg 0$ and which satisfies $R(-t) = R(t) - kt$ for small $|t|$, with some $k \in \Z$. Let $(\phi_t^H)$ be the Hamiltonian flow of $H = R(\mu)$, defined on $T \setminus
T(0)$. Then $\phi_{2\pi}^H$ extends smoothly over $T(0)$ to a compactly supported symplectic automorphism $\phi$ of $T$. The function $K = 2\pi
\,(R'(\mu)\mu - R(\mu))$ also extends smoothly over $T(0)$, and $$\label{eq:k-function}
\phi^*\theta_T - \theta_T = dK.$$
:::

Two Hamiltonians $H_1,H_2$ which are both functions of $\mu$ always Poisson-commute, so that $\phi_t^{H_1} \phi_t^{H_2} = \phi_t^{H_1 + H_2}$. Decomposing $H$ into $H_1 = R(\mu) - (k/2)\mu$ and $H_2 = (k/2)\mu$, one gets $$\phi_{2\pi}^H = \phi_{2\pi}^{H_1} \circ \sigma_{k\pi}.$$ We may assume that $R(-t) = R(t) - kt$ holds everywhere, since that can be achieved by modifying $R$ for negative values only, which does not affect $\phi$. Then $R(t) - (k/2)t$ is an even function, so it can be written as a smooth function of $t^2$. This proves that $H_1$ and its flow extend smoothly over $T(0)$. We know that $\sigma_{k\pi} = A^k$ extends smoothly, so the same holds for $\phi_{2\pi}^H$. Since $H(y)$ vanishes for points with $\mu(y) \gg
0$, $\phi$ is compactly supported (one can show that the compactly supported symplectic automorphisms which are obtained in this way are precisely those which are equivariant for the obvious $O(n+1)$-action). The function $R'(t)t -
R(t)$ is even, so $K$ extends smoothly over $T(0)$ for the same reason as before. A computation shows that the Hamiltonian vector field $X$ of $H$ satisfies $L_{2\pi X}\theta_T = dK$. Since $H$ and $K$ are both functions of $\mu$, $\phi_t^H$ preserves $K$, which implies [\[eq:k-function\]](#eq:k-function){reference-type="eqref" reference="eq:k-function"}. 0◻

Clearly, if $supp(R) \subset (-\infty;\lambda)$ then $\phi$ restricts to a symplectic automorphism of $T(\lambda)$ which is the identity near the boundary. [\[eq:k-function\]](#eq:k-function){reference-type="eqref" reference="eq:k-function"} shows that this is an exact symplectic automorphism. In the case $k = 1$ we call these automorphisms *model Dehn twists*, and generally denote them by $\tau$; any two of them are isotopic in $\Sympe(T(\lambda))$. An explicit formula is $$\label{eq:explicit-twist}
\tau(y) =
 \begin{cases}
 \sigma_{2\pi R'(\mu(y))}(y) & y \in T(\lambda) \setminus T(0),\\
 A(y) & y \in T(0),
 \end{cases}$$ where the angle of rotation goes from $2\pi R'(0) = \pi$ to $2\pi R'(\lambda) =
0$. Note that $\tau$ maps $T(0)$ to itself, and is the antipodal map on it. If one considers $T(0)$ as an exact Lagrangian submanifold, with a function $K_{T(0)} = const.$ associated to it, then by [\[eq:induced-k\]](#eq:induced-k){reference-type="eqref" reference="eq:induced-k"} and [\[eq:k-function\]](#eq:k-function){reference-type="eqref" reference="eq:k-function"} $$\label{eq:self-shift}
K_{\tau(T(0))} = (K_{T(0)} + K_{\tau_L}|T(0)) \circ \tau_L^{-1} = K_{T(0)} -
2\pi R(0).$$ On occasion, it is useful to demand that the angle $R'(t)$ does not oscillate too much. We say that $\tau$ is *$\delta$-wobbly* for some $0 < \delta <
1/2$ if $R'(t) \geq 0$ for all $t \geq 0$, and $R''(t) < 0$ for all $t \geq 0$ such that $R'(t) \geq \delta$.

::: lemma
[]{#th:local-intersections label="th:local-intersections"} Suppose that $\tau$ is $\delta$-wobbly. Let $F_0 = T(\lambda)_{y_0}$, $F_1 =
T(\lambda)_{y_1}$ be the fibres of $T(\lambda) \rightarrow S^n$ at points $y_0,y_1$, whose distance in the standard metric is $\dist(y_0,y_1) \geq 2\pi
\delta$. Then $\tau(F_0)$ intersects $F_1$ transversally and at a single point $y$, which satisfies $$2\pi R'(||y||) = \dist(y_0,y_1).$$ In the special case where $y_1 = A(y_0)$ one has $y = y_1$; and then the tangent space of $T(\lambda)$ at $y$ can be identified symplectically with $\C^n$ in such a way that the subspaces tangent to $\tau(F_0)$, $T(0)$, $F_1$ become respectively, $\R^n$, $e^{2\pi i/3}\R^n$, and $e^{\pi i/3}\R^n$.
:::

Consider first the case when $y_1 \neq A(y_0)$. Suppose that $y \in F_1$ is a point with $\tau^{-1}(y) \in F_0$. By identifying $T \iso TS^n$ and using the interpretation of $\sigma$ as normalized geodesic flow, one sees that $y$ must be a positive multiple of $c'(1)$, where $c: [0;1] \rightarrow S^n$ is the minimal geodesic from $c(0) = y_0$ to $c(1) = y_1$. Moreover, the angle of rotation must be $2\pi R'(||y||) = ||c'(1)|| = dist(y_0,y_1)$. These two conditions are also sufficient. $\delta$-wobblyness implies that $2\pi R'(t) =
dist(y_0,y_1)$ has exactly one solution $t > 0$, which proves that there is exactly one $y$. Combine the two conditions above into one, $c'(1) = 2\pi
R'(||y||)(y/||y||)$. Taking the derivative, one sees that a vector $Y \in
T(F_1)_y \iso T(S^n)_{y_1}$ satisfies $(T\tau)^{-1}(Y) \in T(F_0)$ iff $$\textstyle R''(||y||) \leftsc \frac{y}{||y||}, Y \rightsc \frac{y}{||y||} +
 R'(||y||) \big( Y - \leftsc \frac{y}{||y||}, Y \rightsc \frac{y}{||y||} \big) = 0.$$ We know that $R'(||y||) \geq \delta$; by $\delta$-wobblyness this implies $R''(||y||) < 0$, which shows that $Y = 0$. Therefore $y \in \tau(F_0) \cap
F_1$ is a transverse intersection point.

Now consider the case when $y_1 = A(y_0)$. Then $y = y_1$ clearly lies in $\tau(F_0) \cap F_1$, and because $R'(t) < 1/2$ for all $t>0$, there is no other intersection point. In the notation from the proof of Lemma [\[th:on-invariant\]](#th:on-invariant){reference-type="ref" reference="th:on-invariant"}, $\tau(F_0) = \phi^{H_1}_{2\pi}(A(F_0)) =
\phi^{H_1}_{2\pi}(F_1)$, and $y$ is a stationary point of $(\phi^{H_1}_t)$. It follows that $T(\tau(F_0))_y$ is the image of $T(F_1)_y$ under the time $2\pi$ map of the linear Hamiltonian flow generated by the quadratic form $\half
Hess(H_1)_y$. If one identifies the tangent space to $T$ at $y$ with $T(S^n)_y
\oplus T(S^n)_y$ in such a way that the first summand is $T(F_1)_y$, then $$Hess(H_1)_y = \begin{pmatrix} R''(0) \cdot I & 0 \\ 0 & 0 \end{pmatrix}.$$ Taking some isomorphism $T(S^n)_y \iso \R^n$ and its complexification $T(S^n)_y
\oplus T(S^n)_y \iso \C^n$, one finds that the tangent spaces of $\tau(F_0)$, $T(0)$, and $F_1$ at $y$ correspond respectively to $$\label{eq:i-angle}
(1 + 2\pi i R''(0)) \R^n,\; i\R^n, \; \R^n \subset \C^n.$$ In particular, since $R''(0) < 0$ by $\delta$-wobblyness, the intersection $\tau(F_0) \cap F_1$ is transverse. At this point we need to recall a fact from symplectic linear algebra, see e.g. [@lion-vergne p. 40]: the classification of triples of mutually transverse linear Lagrangian subspaces, up to the action of $Sp(2n)$, is equivalent to the classification of nondegenerate quadratic forms on $\R^n$, up to $GL(n,\R)$. In particular there is a finite number of equivalence classes, and deforming a triple continuously while keeping transversality will not change its equivalence class. One can clearly deform the three subspaces [\[eq:i-angle\]](#eq:i-angle){reference-type="eqref" reference="eq:i-angle"} in this way to $\R^n$, $e^{2\pi i/3}\R^n$, $e^{\pi i/3}\R^n$, which proves the last part of the statement. 0◻

The next result links model Dehn twists to exact Lefschetz fibrations. The connection has been known to algebraic geometers for a very long time, as attested by the terminology "Picard-Lefschetz transformations" used for model Dehn twists. But while the traditional approach ignores symplectic forms, they are of course crucial for our purpose.

::: lemma
[]{#th:model-fibrations label="th:model-fibrations"} Fix $\lambda>0$ and $r>0$, and let $\bar{D}(r) \subset \C$ be the closed disc of radius $r$ around the origin. There is an exact Lefschetz fibration $(E,\pi)$ over $\bar{D}(r)$, together with a diffeomorphism $\phi : E_r
\rightarrow T(\lambda)$ which respects both the symplectic forms and the exact one-forms, such that the following holds. Denote by $\rho \in \Sympe(E_r)$ the symplectic monodromy around $\partial \bar{D}(r)$, in positive sense. Then $\tau = \phi \circ \rho \circ \phi^{-1} \in \Sympe(T(\lambda))$ is a model Dehn twist.
:::

Take $\C^{n+1}$ with its standard forms $\o_{\C^{n+1}}$, $\theta_{\C^{n+1}}$ and the function $q: \C^{n+1} \rightarrow \C$, $q(x) =
x_1^2 + \dots + x_{n+1}^2$. Even though $(\C^{n+1},q)$ is clearly not an exact Lefschetz fibration (its fibres are not even compact), much of what was said in the previous section carries over to it. The horizontal subspaces $$\label{eq:horizontal-model}
 T(\C^{n+1})_x^h =
 \{X \in \C^{n+1} \suchthat \o_{\C^{n+1}}(X,\ker\, Dq_x) = 0\} = \C \bar{x}$$ define a symplectic connection away from the critical point $x = 0$, so that one has parallel transport maps $q^{-1}(c(a)) \rightarrow q^{-1}(c(b))$ along paths $c: [a;b] \rightarrow \C^*$. Consider the family of Lagrangian spheres $$\label{eq:model-spheres}
\Sigma_z = \sqrt{z}S^n = \{ (\sqrt{z}y_1, \dots, \sqrt{z}y_{n+1}) \suchthat y
\in S^n \subset \R^{n+1} \} \subset q^{-1}(z),$$ $z \neq 0$, which for $z \rightarrow 0$ degenerate to $\Sigma_0 = \{0\} \subset
q^{-1}(0)$. Write $\Sigma^*$ for the union of all $\Sigma_z$, $z \neq 0$, and $\Sigma = \Sigma^* \cup \Sigma_0$. One computes that $$\label{eq:theta-sigma}
 \theta_{\C^{n+1}} \, | \, \Sigma^* = q^* d^c({-\textstyle\quarter}|z|).$$ Actually, the precise formula does not matter much for the moment. All we need is that $\o_{\C^{n+1}} \,|\, \Sigma^*$ is the pullback by $q$ of some two-form on $\C^*$, since that implies that parallel transport in any direction in $\C^*$ takes the $\Sigma_z$ into each other; compare Lemma [\[th:submanifold\]](#th:submanifold){reference-type="ref" reference="th:submanifold"}. The next observation is that if one removes $\Sigma$ then parallel transport can be extended even to the singular fibre, so that for any path $c$ in $\C$ one has a canonical symplectic isomorphism $$q^{-1}(c(a)) \setminus \Sigma_{c(a)} \rightarrow q^{-1}(c(b)) \setminus
\Sigma_{c(b)}.$$ Since taking out $\Sigma_0$ removes the critical point, the only possible problem is that a point in $\C^{n+1} \setminus \Sigma$ might move in horizontal direction and converge to some point of $\Sigma$, which means that the flow of some horizontal vector field would not be defined for all time. However, that cannot happen since there is a function, $h(x) = ||x||^4 - |q(x)|^2$, which satisfies $dh_x(\C\bar{x}) = 0$, hence is constant horizontally, and with $h^{-1}(0) = \Sigma$. Therefore one can use parallel transport in radial direction to trivialize $q: \C^{n+1} \setminus \Sigma \longrightarrow \C$ symplectically. In particular, if $\tilde{\rho}_s: q^{-1}(s) \rightarrow
q^{-1}(s)$ is the monodromy along the circle of radius $s>0$ around the origin, $\tilde{\rho}_s\,|\,(q^{-1}(s) \setminus \Sigma_s)$ will be isotopic to the identity in the group of all symplectic automorphisms of $q^{-1}(s) \setminus
\Sigma_s$. We have mentioned all this mainly to motivate the subsequent proof, which is more computational.

Consider the map $$\label{eq:phi}
\begin{split}
 & \Phi: \C^{n+1} \setminus \Sigma \longrightarrow \C \times (T \setminus T(0)), \\
 & \Phi(x) = (q(x),\sigma_{\alpha/2}(-\im(\hatx)\,||\re(\hatx)||,
 \re(\hatx)\,||\re(\hatx)||^{-1})),
\end{split}$$ where $s e^{i\alpha} = q(x)$ are polar coordinates on the base, and $\hatx =
e^{-i\alpha/2}x$. We claim that this is a diffeomorphism fibered over $\C$. First of all, because of the use of polar coordinates, it is not obvious that $\Phi$ is well-defined and smooth at $q^{-1}(0) \setminus \Sigma_0$. To dispel any doubts about that one writes, after some manipulations, $$\begin{gathered}
\Phi(x) = \big(q(x),
 - \half \im(x) \beta(x)
 - \half \im(\overline{q(x)}x) \beta(x)^{-1}, \\
 \qquad\qquad  h(x)^{-1/2} \re(x) \beta(x)
 - h(x)^{-1/2} \re(\overline{q(x)}x) \beta(x)^{-1}
 \big),
\end{gathered}$$ where $\beta(x) = (||x||^2 + h(x)^{1/2})^{1/2}$. The fact that $\Phi$ is a diffeomorphism on each fibre is easy to see, either directly or by using the symplectic forms and [\[eq:theta-pullback\]](#eq:theta-pullback){reference-type="eqref" reference="eq:theta-pullback"} below. Moreover, if one restricts $\Phi$ to a fibre over $s > 0$, it extends to a diffeomorphism $\phi_s: q^{-1}(s) \rightarrow T$. Such an extension does not exist for other fibres, due to the non-continuity of $\sigma$ at $T(0)$. A computation yields $$\label{eq:theta-pullback}
 (\Phi^{-1})^*\theta_{\C^{n+1}} = \theta_T - \tilde{R}_s(\mu)\, d\alpha, \quad
 \tilde{R}_s(t) = \half t - \half\big(t^2 + s^2/4\big)^{1/2}.$$ This implies that the restriction of $\Phi$ to any fibre is symplectic, and actually maps the respective one-forms into each other. Of course, the same will then be true for the continuous extensions $\phi_s$, $s>0$. In fact [\[eq:theta-pullback\]](#eq:theta-pullback){reference-type="eqref" reference="eq:theta-pullback"} shows even more: if one restricts to any ray $\alpha
= const.$ in the basis then $\Phi^*\o_T = \o_{\C^{n+1}}$, which means that $\Phi$ trivializes the symplectic parallel transport on $(\C^{n+1} \setminus
\Sigma,q)$ in radial directions, in accordance with the strategy which we set out before. Consider $\tilde{\tau}_s = \phi_s \circ \tilde{\rho}_s \circ
\phi_s^{-1} : T \rightarrow T$, where $\tilde{\rho}_s$ is the monodromy map introduced above. From [\[eq:theta-pullback\]](#eq:theta-pullback){reference-type="eqref" reference="eq:theta-pullback"} it follows that $\tilde{\tau}_s$ restricted to $T \setminus T(0)$ is the time $2\pi$ map of the Hamiltonian $\tilde{H}_s = \tilde{R}_s(\mu)$. Since $\tilde{R}_s(-t) =
\tilde{R}_s(t) - t$, this is quite close to the case $k = 1$ of Lemma [\[th:on-invariant\]](#th:on-invariant){reference-type="ref" reference="th:on-invariant"}. The difference is that $\tilde{R}_s(t)$ does not vanish for $t \gg 0$. Instead, it decays as follows: $$\label{eq:decay}
 0 > \tilde{R}_s(t) \geq -\textstyle{\frac{1}{16}} s^2t^{-1}, \quad
 0 < \textstyle{\frac{d}{dt}}
 \tilde{R}_s(t) \leq \textstyle{\frac{1}{16}} s^2t^{-2}.$$ This is good enough to imply that $\tilde{\tau}_s$ is asymptotic to the identity at infinity, for each $s>0$. It remains to tweak the given data slightly, so as to produce a honest exact Lefschetz fibration, whose monodromy is an actual model Dehn twist.

Fix $\lambda>0$, $r>0$. Choose a cutoff function $g \in \smooth(\R^+,\R)$ such that $g'(t) \geq 0$ everywhere, $g(t) = 0$ for small $t$, and $g(t) = 1$ if $t$ is close to $\lambda$. We claim that there is a unique $\gamma \in
\Omega^1(\C^{n+1})$ with, again in polar coordinates on the base, $$\label{eq:cutoff-form}
(\Phi^{-1})^*\gamma = g(\mu)\tilde{R}_s(\mu) d\alpha.$$ Since $\tilde{R}_0(t) = 0$, the function $\tilde{R}_s(t)/s$ extends smoothly to $s = 0$, $t \neq 0$. Therefore the right hand side of [\[eq:cutoff-form\]](#eq:cutoff-form){reference-type="eqref" reference="eq:cutoff-form"} can be written as $g(\mu)(\tilde{R}_s(\mu)/s)\, s d\alpha$, which means that $\gamma$ is smooth at least on $\C^{n+1} \setminus \Sigma$. Now $\mu(\Phi(x)) =
(1/2) h(x)^{1/2}$; since $\Sigma = h^{-1}(0)$ and $g(t) = 0$ for small $t$, one sees that $\Phi^*(g(\mu)\tilde{R}_s(\mu)d\alpha)$ vanishes near $\Sigma$, so that $\gamma$ extends by zero over $\Sigma$. Set $$\label{eq:define-model}
\begin{cases}
 E = \Phi^{-1}(\bar{D}(r) \times (T(\lambda) \setminus T(0)))
 \cup (\Sigma \cap q^{-1}(\bar{D}(r))), \\
 \pi = q|E: E \longrightarrow \bar{D}(r), \\
 \Theta = (\theta_{\C^{n+1}} + \gamma) \,|\,E, \quad
 \Omega = d\Theta, \\
 \phi = \phi_r|E_r: E_r \longrightarrow T(\lambda).
\end{cases}$$ $E \subset \C^{n+1}$ is cut out by the inequalities $h(x) \leq 4\lambda^2$, $|q(x)| \leq r$. This makes it easy to show that it is a compact manifold with corners, whose boundary faces are $\partial_vE = \pi^{-1}(\partial \bar{D}(r))$ and $\partial_hE = \{h(x) = 4\lambda^2\} = \{\mu(\Phi(x)) = \lambda\} =
\Phi^{-1}(\bar{D}(r) \times \partial T(\lambda))$. Because $\gamma$ vanishes when restricted to any fibre, $\Omega|TE^v_x = \o_{\C^{n+1}} | \ker\, Dq_x$ is nondegenerate for all $x$. In $$\label{eq:tilde-pullback}
\Theta\,|\,(E \setminus \Sigma) = \Phi^*(\theta_T + (g(\mu)-1)
\tilde{R}_s(\mu)\, d\alpha)$$ the second term on the right hand side vanishes close to $\bar{D}(s) \times
\partial T(\lambda)$, so that $\Phi$ provides a trivialization near $\partial_hE$ in the sense introduced in the previous section. Moreover, since $\gamma$ vanishes near the critical point $x = 0$, equipping $E$ with the standard complex structure $J_0$ near that point, and $\bar{D}(r)$ with the standard complex structure $j_0$, turns $(E,\pi)$ into an exact Lefschetz fibration. As for the statement about the monodromy $\rho$, one can repeat the argument above, using [\[eq:tilde-pullback\]](#eq:tilde-pullback){reference-type="eqref" reference="eq:tilde-pullback"} instead of [\[eq:theta-pullback\]](#eq:theta-pullback){reference-type="eqref" reference="eq:theta-pullback"}. This shows that $\tau = \phi \circ \rho \circ
\phi^{-1}$, when restricted to $T(\lambda) \setminus T(0)$, is the time $2\pi$ map of $R_r(\mu)$, where $$\label{eq:r-function}
R_r(t) = (1-g(t))\tilde{R}_r(t);$$ by definition, this is a model Dehn twist. 0◻

Let $(M,\o,\theta)$ be an exact symplectic manifold. A *framed*[^3] *exact Lagrangian sphere* is an exact Lagrangian submanifold $L \subset M$ together with an equivalence class $[f]$ of diffeomorphisms $f: S^n \rightarrow L$. Here $f_1,f_2$ are equivalent iff $f_2^{-1}f_1$ can be deformed inside $\Diff(S^n)$ to an element of $O(n+1)$. To any such $(L,[f])$ one associates a Dehn twist $\tau_{(L,[f])} \in \Sympe(M)$ as follows. Choose a representative $f$ and extend it to a symplectic embedding $\iota: T(\lambda) \rightarrow M$ for some $\lambda>0$. Take a model Dehn twist $\tau$ which is supported in the interior of $T(\lambda)$, and define $$\tau_{(L,[f])} = \begin{cases}
 \iota \circ \tau \circ \iota^{-1} & \text{on $\im(\iota)$,} \\
 \id & \text{elsewhere.}
\end{cases}$$ The exactness of $\tau_{(L,[f])}$ follows from that of $L$; moreover, the analogue of [\[eq:self-shift\]](#eq:self-shift){reference-type="eqref" reference="eq:self-shift"} holds. It is not difficult to show that the isotopy class $[\tau_{(L,[f])}] \in \pi_0(\Sympe(M))$ is independent of the choices made in the definition. In contrast, it is unknown whether a change of the framing $[f]$ can affect $[\tau_{(L,[f])}]$; if the answer is negative the notion of framing could be dropped altogether, but while the question is open one cannot do without it. Still, for the sake of brevity we will often omit framings from the notation and write $\tau_L$ instead of $\tau_{(L,[f])}$. We will say that $\tau_L$ is $\delta$-wobbly if the local model it is constructed out of has this property.

::: prop
[]{#th:standard-fibrations label="th:standard-fibrations"} Let $(L,[f])$ be a framed exact Lagrangian sphere in $M$. Fix some $r>0$. There is an exact Lefschetz fibration $(E^L,\pi^L)$ over $\bar{D}(r)$ together with an isomorphism $\phi^L: E^L_r \rightarrow M$ of exact symplectic manifolds, such that if $\rho^L$ is the symplectic monodromy around $\partial \bar{D}(r)$, then $\tau_L = \phi^L \circ \rho^L \circ (\phi^L)^{-1}$ is a Dehn twist along $(L,[f])$.
:::

We will prove this under the assumption that there is an embedding $\iota:
T(\lambda) \rightarrow M$ as before, with $\iota^*\theta = \theta_T$. This is not really a restriction, since one can always satisfy it by adding the derivative of a function to $\theta$, which does not change $M$ up to exact symplectic isomorphism. On the other hand, it allows us to make the statement slightly sharper: $\phi^L$ will map the one-forms on $E^L_r$ and $M$ into each other, and the Dehn twist obtained from the monodromy of $(E^L,\pi^L)$ will be one constructed using the given embedding $\iota$.

Take $(E,\pi)$ and $\phi$ from Lemma [\[th:model-fibrations\]](#th:model-fibrations){reference-type="ref" reference="th:model-fibrations"}, with the given $r$ and $\lambda$. We will construct $(E^L,\pi^L)$ by attaching a trivial piece to $(E,\pi)$. By construction, there is a neighbourhood $N \subset E$ of $\partial_hE$, a neighbourhood $V$ of $\partial T(\lambda)$ in $T(\lambda)$, and a diffeomorphism $\Phi: N \rightarrow \bar{D}(r) \times V$ fibered over $\bar{D}(r)$, such that $\Theta|N = \Phi^*\theta_T$. Moreover, $\Phi$ agrees with $\phi$ on $N \cap E_r$. Set $$E^L = E \cup_{\sim} \bar{D}(r) \times (M \setminus \iota(T(\lambda) \setminus
V)),$$ where $\sim$ identifies $N$ with $\bar{D}(r) \times \iota(V)$ through $(\id
\times \iota) \circ \Phi$. One similarly defines $\pi^L$ from $\pi$ and the projection $\bar{D}(r) \times M \rightarrow \bar{D}(r)$. The forms $\Omega^L,\Theta^L$ on $E^L$ come from the corresponding ones on $E$ and the pullbacks of $\o,\theta$ on the trivial part. $\phi^L$ is constructed from $\iota \circ \phi$ and the identity map. The complex structure near the critical point and critical value are inherited from $E$. All properties stated above are obvious from the construction and the definition of Dehn twists. 0◻

We call the $(E^L,\pi^L)$ *standard fibrations*. For future reference, we will now state certain properties which these fibrations inherit from the local model $(E,\pi)$, and which depend on the details of its construction.

::: lemma
[]{#th:standard-properties label="th:standard-properties"} Any standard fibration $(E^L,\pi^L)$ has the following properties.

::: romanlist
[]{#item:lagrangian-subbundle label="item:lagrangian-subbundle"} There is a closed subset $\Sigma^L \subset E^L$ such that $$\Sigma^L_z = \Sigma^L \cap E^L_z =
 \begin{cases}
 \text{is an embedded $n$-sphere} & \text{if $z \neq 0$,} \\
 \text{is the unique critical point $x_0 \in E^L_0$} &
 \text{if $z = 0$.}
 \end{cases}$$ In fact $(\Sigma^L)^* = \Sigma^L \setminus \Sigma^L_0$ is a smooth $n$-sphere bundle over $\bar{D}(r) \setminus \{0\}$, and satisfies $$\label{eq:theta-sigma-l}
 \Theta^L \, | \, (\Sigma^L)^* =
 (\pi^L)^* d^c(-\textstyle\quarter|z|).$$ As in the discussion following [\[eq:theta-sigma\]](#eq:theta-sigma){reference-type="eqref" reference="eq:theta-sigma"}, this implies that each $\Sigma^L_z \subset E^L_z$, $z \neq 0$, is an exact Lagrangian submanifold, and that symplectic parallel transport within $\bar{D}(r) \setminus \{0\}$ carries these spheres into each other. Moreover, $\phi^L(\Sigma^L_r) = L$.

[]{#item:preferred-charts label="item:preferred-charts"} There are holomorphic Morse charts $(\xi,\Xi)$ around the unique critical point $x_0 \in E^L_0$, such that $\xi$ is the inclusion $U \hookrightarrow
\bar{D}(r)$ of some neighbourhood $U \subset \C$ of the origin; $\Xi^*\Theta^L
= \theta_{\C^{n+1}}$ and $\Xi^*\Omega^L = \omega_{\C^{n+1}}$; and $\Xi^{-1}(\Sigma^L_z) = \Sigma_z$ for all sufficiently small $z \in \C$.

[]{#item:nonnegatively-curved label="item:nonnegatively-curved"} $(E^L,\pi^L)$ has nonnegative curvature.

[]{#item:precise-twist label="item:precise-twist"} $\tau_L = \phi^L \circ \rho^L \circ (\phi^L)^{-1}$ is the Dehn twist defined using $\iota$ and the function $R_r$ from [\[eq:r-function\]](#eq:r-function){reference-type="eqref" reference="eq:r-function"}; in particular $R_r(0) = -r/4$. By making $r$ smaller while keeping all other choices in the construction fixed, one can achieve that $\tau_L$ is $\delta$-wobbly for an arbitrary $\delta$.
:::
:::

[\[item:lagrangian-subbundle\]](#item:lagrangian-subbundle){reference-type="ref" reference="item:lagrangian-subbundle"} From [\[eq:define-model\]](#eq:define-model){reference-type="eqref" reference="eq:define-model"} one sees that $\Sigma \cap q^{-1}(\bar{D}(r)) \subset E$, and that $\Theta =
\theta_{\C^{n+1}}$ in a neighbourhood of that subset. $\Sigma^L$ is defined to be the image of this in $E^L$, so that [\[eq:theta-sigma-l\]](#eq:theta-sigma-l){reference-type="eqref" reference="eq:theta-sigma-l"} is a consequence of [\[eq:theta-sigma\]](#eq:theta-sigma){reference-type="eqref" reference="eq:theta-sigma"}. [\[item:preferred-charts\]](#item:preferred-charts){reference-type="ref" reference="item:preferred-charts"} The definition of $\xi,\Xi$ is obvious, and the claim about $\Xi^*\Theta^L$ follows from the fact that in [\[eq:define-model\]](#eq:define-model){reference-type="eqref" reference="eq:define-model"} $\Theta = \theta_{\C^{n+1}}$ near the critical point. [\[item:nonnegatively-curved\]](#item:nonnegatively-curved){reference-type="ref" reference="item:nonnegatively-curved"} One can compute the curvature of $(E,\pi)$ from [\[eq:theta-pullback\]](#eq:theta-pullback){reference-type="eqref" reference="eq:theta-pullback"} and [\[eq:cutoff-form\]](#eq:cutoff-form){reference-type="eqref" reference="eq:cutoff-form"}; it turns out to be $$\Phi^*\big( (g(\mu)-1) \textstyle\frac{\partial}{\partial s} \tilde{R}_s(\mu)
\big) ds \wedge d\alpha,$$ which is $\geq 0$ everywhere. This implies the same property for $(E^L,\pi^L)$. [\[item:precise-twist\]](#item:precise-twist){reference-type="ref" reference="item:precise-twist"} The nontrivial statement is $\delta$-wobblyness, which requires that we take another look at the function $R_r$. There is a $t_0>0$ such that $g(t) = 0$ for $t \in [0;t_0]$, and in that interval $R_r(t) =
\tilde{R}_r(t)$, so that $(\partial/\partial t) R_r(t) > 0$, $(\partial^2/\partial t^2) R_r(t) < 0$. For $t \in [t_0;\lambda]$ one estimates using [\[eq:decay\]](#eq:decay){reference-type="eqref" reference="eq:decay"} that $$0 \leq {\textstyle\frac{\partial}{\partial t}}R_r(t) = -g'(t) \tilde{R}_r(t) +
(1-g(t)) {\textstyle\frac{\partial}{\partial t}} \tilde{R}_r(t) \leq
\textstyle{\frac{r^2}{16}} (||g'|| t_0^{-1} + t_0^{-2}).$$ By choosing $r$ small while keeping $g$ and hence $t_0$ fixed, one can make this $< \delta$ for an arbitrary $\delta$. 0◻

## Vanishing cycles[]{#sec:picard-lefschetz label="sec:picard-lefschetz"}

We have seen that all Dehn twists can be realized as monodromy maps (of standard fibrations). Conversely, the geometry of any exact Lefschetz fibration can be understood in terms in Dehn twists. This is again well-known on a topological level, and our exposition repeats the classical arguments while paying more attention to symplectic forms. The results will not be used again in this paper, but they are important in applications.

Let $(E,\pi)$ be an exact Lefschetz fibration over $S$. Take $z_0 \in S^\crit$, and the unique critical point $x_0 \in E_{z_0}$. Let $c: [a;b] \rightarrow S$ be a smooth embedded path with $c(b) = z_0$, $c^{-1}(S^\crit) = \{b\}$; and let $\rho_{c|[s,s']}: E_{c(s)} \rightarrow E_{c(s')}$ be the parallel transport maps along it, which is defined for all $s \leq s' < b$. Following a suggestion of Donaldson, we define $$\label{eq:vanishing-ball}
B_c = \{x \in E_{c(s)}, \; a \leq s < b \suchthat \lim_{s' \rightarrow b}
\rho_{c|[s;s']}(x) = x_0 \} \cup \{ x_0 \} \subset E.$$

::: lemma
[]{#th:vanishing-ball label="th:vanishing-ball"} $B_c$ is an embedded closed $(n+1)$-ball, with $\partial B_c = B_c \cap
E_{c(a)}$. The function $p = c^{-1} \circ \pi: B_c \rightarrow [a;b]$ has $x_0$ as its unique critical point, which is a nondegenerate local maximum. Moreover, $\Omega|B_c = 0$.
:::

Put a symplectic form $\Omega + \pi^*\beta$ on $E$ as in Lemma [\[th:add-base\]](#th:add-base){reference-type="ref" reference="th:add-base"}. Choose an oriented embedding $\tilde{c}:
(a-\epsilon;b+\epsilon) \times (-\epsilon;\epsilon) \rightarrow S$ such that $\tilde{c}(0,t) = c(t)$. Let $h$ be the function defined on $\im(\tilde{c})$ with $h(\tilde{c}(s,t)) = -t$. The Hamiltonian vector field $X$ of $H = h \circ
\pi$ has the following properties:

::: condensedlist
[]{#item:h-one label="item:h-one"} it is horizontal everywhere, $X_x \in TE^h_x$;

[]{#item:h-two label="item:h-two"} for each $x \neq x_0$, $D\pi(X)_x$ is a positive multiple of $\partial\tilde{c}/\partial s$;

[]{#item:h-three label="item:h-three"} $x_0$ is a hyperbolic stationary point of $X$, with $n+1$ positive and negative eigenvalues.
:::

[\[item:h-one\]](#item:h-one){reference-type="ref" reference="item:h-one"} and [\[item:h-two\]](#item:h-two){reference-type="ref" reference="item:h-two"} are straightforward; [\[item:h-three\]](#item:h-three){reference-type="ref" reference="item:h-three"} can be seen by looking at $X$ in a holomorphic Morse chart, where it is $J_0\nabla H$. Let $\tilde{B} \subset E$ be the stable manifold of $x_0$. It is an open $(n+1)$-ball, lies in $\pi^{-1}\tilde{c}((a-\epsilon;b] \times \{0\})$, and the projection $$\tilde{p} = \tilde{c}^{-1}\pi : \tilde{B} \longrightarrow
 (a-\epsilon;b] \times \{0\}$$ is a proper map. The tangent space of $\tilde{B}$ at $x_0$ is the negative eigenspace of $DX_{x_0}$; one shows easily that $D^2\tilde{p}|T\tilde{B}_{x_0}$ differs from $DX|T\tilde{B}_{x_0}$ only by a positive constant, which means that $x_0$ is a nondegenerate maximum of $\tilde{p}$. There are no other critical points, because elsewhere $d\tilde{p}(X)_x>0$ by [\[item:h-two\]](#item:h-two){reference-type="ref" reference="item:h-two"}. Finally, since the flow $X$ is symplectic and contracts the tangent spaces of $\tilde{B}$, these must be Lagrangian subspaces, so $(\Omega +
\pi^*\beta)|\tilde{B} = \Omega|\tilde{B} = 0$.

We claim that $B_c = \tilde{B} \cap \pi^{-1}(\im(c))$, which implies all desired properties of $B_c$. Let $Y$ be the vector field on $\pi^{-1}(\im(\tilde{c})) \setminus \{x_0\}$ which is horizontal and satisfies $D\pi(Y) = \partial\tilde{c}/\partial s$. From [\[item:h-one\]](#item:h-one){reference-type="ref" reference="item:h-one"} and [\[item:h-two\]](#item:h-two){reference-type="ref" reference="item:h-two"} above one sees that $Y = gX$ for some function $g$, bounded from below by a positive constant, and which goes to $\infty$ as one approaches $x_0$. Therefore the orbits of $X$ and $Y$ coincide, except of course for $\{x_0\}$. Since $Y|\pi^{-1}(\im(c))$ defines parallel transport along $c$, the claim follows. 0◻

::: lemma
[]{#th:vanishing-cycle label="th:vanishing-cycle"} $V_c = \partial B_c$ is an exact Lagrangian sphere in $E_{c(a)}$, and comes with a canonical framing.
:::

Since $B_c$ is a ball and $\Theta|B_c$ is closed, there is a unique $K
\in \smooth(B_c,\R)$ with $K(x_0) = 0$ and $dK = \Theta|B_c$. The restriction $K_{V_c} = K|V_c$ makes $V_c$ into an exact Lagrangian submanifold. It remains to explain the framing. In any chart on $B_c$ around $x_0$, the level sets $p^{-1}(s')$ of the function from Lemma [\[th:vanishing-ball\]](#th:vanishing-ball){reference-type="ref" reference="th:vanishing-ball"}, for $s'$ close to $b$, will be strictly convex hypersurfaces, so that one can map them to $S^n$ by radial projection. On the other hand, $V_c = p^{-1}(a)$ can be identified with $p^{-1}(s')$ by the gradient flow with respect to some metric. Combining these two maps gives a diffeomorphism $V_c \rightarrow S^n$, which is unique up to isotopy and action of $O(n+1)$; its inverse is our framing. 0◻

The framed exact Lagrangian sphere $V_c \subset E_{c(a)}$ is called the *vanishing cycle* associated to $c$. It exists more generally for any path $c:
[a;b] \rightarrow S$ which is smooth, not necessarily embedded, but still satisfies $$\label{eq:path}
c^{-1}(S^\crit) = \{b\}, \quad c'(b) \neq 0.$$ To construct it in this situation, one first extends $c$ to a map $(a-\epsilon;b+\epsilon) \times (-\epsilon;\epsilon) \rightarrow S$ which is a local oriented diffeomorphism at $(b,0)$, pulls back $(E,\pi)$ by that map, and then applies Lemma [\[th:vanishing-ball\]](#th:vanishing-ball){reference-type="ref" reference="th:vanishing-ball"} to the pullback exact Lefschetz fibration. Note also that deforming $c$ smoothly, rel endpoints, within the class [\[eq:path\]](#eq:path){reference-type="eqref" reference="eq:path"} yields an exact Lagrangian isotopy of the corresponding vanishing cycles, which is compatible with their framings.

::: prop
[]{#th:picard-lefschetz label="th:picard-lefschetz"} Let $c$ be a path satisfying [\[eq:path\]](#eq:path){reference-type="eqref" reference="eq:path"}, and $l$ the loop in $S \setminus
S^\crit$ obtained by "doubling" $c$, as in Figure [\[fig:doubling\]](#fig:doubling){reference-type="ref" reference="fig:doubling"}. Then the monodromy around $l$ is isotopic to the Dehn twist along the vanishing cycle $V_c$: $$\label{eq:picard-lefschetz}
[\rho_l] = [\tau_{V_c}] \in \pi_0(\Sympe(E_{c(a)})).$$
:::

We start with a rather special case. Let $(E,\pi)$ be an exact Lefschetz fibration with base $\bar{D}(r)$ for some $r>0$, and which has exactly one critical point $x_0 \in E_0$. Write $M = E_r$. In addition, $x_0$ should admit a holomorphic Morse chart $(\xi,\Xi)$ where $\Xi$ is defined on $W = \{x \in
\C^{n+1} \suchthat ||x|| \leq 2\sqrt{r}, \; |q(x)| \leq r\}$, where $\xi =
\id_{\bar{D}(r)}$, and such that $\Xi^*\Omega$, $\Xi^*\Theta$ are standard. This means that the symplectic geometry of $(E,\pi)$ equals that of the local model $(\C^{n+1},q)$ discussed in Lemma [\[th:model-fibrations\]](#th:model-fibrations){reference-type="ref" reference="th:model-fibrations"}, at least in a suitable neighbourhood of $x_0$. In particular, each fibre $E_z$, $z \neq 0$, contains an exact Lagrangian sphere $\Sigma_z^E = \Xi(\Sigma_z)$, degenerating to $\Sigma_0^E = \{x_0\}$. Write $L = \Sigma_r^E \subset M$; this inherits an obvious framing from $\Sigma_r = \sqrt{r}S^n$. We claim that the monodromy around $\partial \bar{D}(r)$, denoted by $\rho \in \Sympe(M)$, is isotopic to $\tau_L$.

From [\[eq:theta-sigma\]](#eq:theta-sigma){reference-type="eqref" reference="eq:theta-sigma"} one deduces that parallel transport in $\bar{D}(r)
\setminus \{0\}$ carries the $\Sigma_z^E$ into each other. Moreover, by the same argument as in Lemma [\[th:model-fibrations\]](#th:model-fibrations){reference-type="ref" reference="th:model-fibrations"}, if one removes $\Sigma^E =
\bigcup_z \Sigma^E_z$ from $E$, parallel transport can be extended over the singular fibre. Using parallel transport in radial directions one constructs a trivialization $\Phi^E: E \setminus \Sigma^E \longrightarrow \bar{D}(r) \times
(M \setminus L)$ which is the identity on the fibre over $r$; this is such that, in radial coordinates $z = se^{i\alpha}$ on the basis, $((\Phi^E)^{-1})^*\Theta = \theta - R^E \wedge d\alpha + dS^E$ for some functions $R^E = R^E(s,\alpha,x)$ and $S^E = S^E(s,\alpha,x)$ which vanish for $x$ close to $\partial M$. This implies that $\rho$ restricted to $M \setminus
L$ is the time-$2\pi$ map of the flow generated by the time-dependent Hamiltonian $(\alpha,x) \mapsto R^E(r,\alpha,x)$. Clearly, $[\rho] \in
\pi_0(\Sympe(M))$ depends only on the behaviour of this function in an arbitrarily small neighbourhood of $L$, or equivalently on $(E,\pi)$ and $\Omega$ close to $\Sigma^E$; since $\Sigma^E \subset \Xi(W)$ by definition, this can be determined from the local model $(\C^{n+1},q)$. It remains to spell out the computation.

Define an embedding $\iota: T(\lambda) \rightarrow M$, for some $\lambda>0$, by combining $\Xi_r = \Xi|(W \cap q^{-1}(r)) \rightarrow M$ with the inverse of the isomorphism $\phi_r: q^{-1}(r) \rightarrow T$ from the proof of Lemma [\[th:model-fibrations\]](#th:model-fibrations){reference-type="ref" reference="th:model-fibrations"}. This satisfies $\iota^*\theta = \theta_T$, $\iota^*\o = \o_T$, and $\iota(T(0)) = L$. Because both $\Phi^E$ and the trivialization $\Phi$ from [\[eq:phi\]](#eq:phi){reference-type="eqref" reference="eq:phi"} are defined by radial parallel transport, there is a commutative diagram $$\xymatrix{
 {\C^{n+1} \setminus \Sigma} \ar[r]^-{\Phi} &
 {\C \times (T \setminus T(0))} \\
 {W \setminus \Sigma} \ar@{^{(}->}[u] \ar[d]_{\Xi\,|\,W \setminus \Sigma} &
 {\bar{D}(r) \times (T(\lambda) \setminus T(0))} \ar@{^{(}->}[u]
 \ar[d]^{\id \times (\iota \,|\, T(\lambda) \setminus T(0))} \\
 {E \setminus \Sigma^E} \ar[r]^-{\Phi^E} & {\bar{D}(r) \times (M \setminus L).}
}$$ From this, $\Xi^*\Omega = \o_{\C^{n+1}}$ and [\[eq:theta-pullback\]](#eq:theta-pullback){reference-type="eqref" reference="eq:theta-pullback"} it follows that $$\begin{aligned}
 & (\id \times \iota)^*(\theta_T - R^E d\alpha + dS^E)
 = (\id \times \iota)^*((\Phi^E)^{-1})^*\Theta \\
 & = (\Phi^{-1})^*\theta_{\C^{n+1}} = \theta_T - \tilde{R}_s(\mu) \wedge d\alpha,
\end{aligned}$$ and in particular that $R^E(r,\alpha,\iota(y)) = \tilde{R}_r(\mu(y))$ for all $\alpha$. In view of the discussion above, and the fact that $\tilde{R}_r(-t) =
\tilde{R}_r(t) - t$, this implies the desired equality $[\rho] = [\tau_L]$. Now consider the path $c: [0;r] \rightarrow \bar{D}(r)$, $c(s) = r-s$. Because symplectic parallel transport takes the $\Sigma^E_z$ into each other, the ball $B_c$ from Lemma [\[th:vanishing-ball\]](#th:vanishing-ball){reference-type="ref" reference="th:vanishing-ball"} must be the union of $\Sigma^E_z$ for all $z \in [0;r]$, and the vanishing cycle is $V_c = \Sigma^E_r = L \subset M$, with the same framing as before. Therefore, what we have done up to now proves [\[eq:picard-lefschetz\]](#eq:picard-lefschetz){reference-type="eqref" reference="eq:picard-lefschetz"} for this special class of exact Lefschetz fibrations $(E,\pi)$ and the particular path $c$.

More generally, let $(E,\pi)$ be a exact Lefschetz fibration with arbitrary base $S$, and $x_0 \in E_{z_0}$ a critical point which admits a holomorphic Morse chart $(\xi,\Xi)$ such that $\Xi^*\Omega$, $\Xi^*\Theta$ are standard. By restricting to a suitably small disc around $z_0$ in the base, and making the domains of $\xi,\Xi$ smaller, one can arrive at the situation considered before. This means that [\[eq:picard-lefschetz\]](#eq:picard-lefschetz){reference-type="eqref" reference="eq:picard-lefschetz"} is true at least for one (short) path $c$ with endpoint $z_0$. But from that it follows easily for all other paths with the same endpoint.

It remains to remove the assumption concerning $\Xi$. Let $(E,\pi)$ be an arbitrary exact Lefschetz fibration, $c$ a path as in [\[eq:path\]](#eq:path){reference-type="eqref" reference="eq:path"}, and $l$ a corresponding loop. With respect to the critical point in $E_{c(b)}$, take smooth families $\Omega^\mu$, $\Theta^\mu$ as in Lemma [\[th:local-deformation\]](#th:local-deformation){reference-type="ref" reference="th:local-deformation"}. These can be chosen such that in a neighbourhood of $E_{c(a)}$, $\Omega^\mu = \Omega$ and $\Theta^\mu = \Theta$ for all $\mu$. The corresponding vanishing cycles $V^\mu_c \subset E_{c(a)}$ form a smooth isotopy of framed exact Lagrangian spheres, and similarly there is a smooth family of monodromies $\rho_l^{\mu}$. For $\mu = 1$ our previous assumption about holomorphic Morse charts is satisfied, and hence $[\rho_l] = [\rho_l^0] =
[\rho_l^1] = [\tau_{V^1_c}] = [\tau_{V^0_c}] = [\tau_{V_c}] \in
\pi_0(\Sympe(E_{c(a)}))$. 0◻

[^1]: Called "exact Morse fibration" in [@seidel00]. The present terminology is more in line with general usage, since the notion is closely related to, even though not quite the same as, the symplectic Lefschetz fibrations considered by Donaldson, Gompf, and others.

[^2]: The definition of $d^c$ in this paper is such that $\o_{\C} = -dd^c(\quarter|z|^2)$. This differs from the majority convention by a negative constant.

[^3]: This has little or nothing to do with the usual topological notion of framed manifold.

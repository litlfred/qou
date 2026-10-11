---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-011-44-horizontal-sections-over-a-disk-with-one-crit
section_title: "Horizontal sections over a disk with one critical value"
section_number: 4.4
pages: 40-52
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped with a binodal cubic curve as"
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.977
---
[]{#sec:horiz-sections label="sec:horiz-sections"}

We now determine the counts of pseudo-holomorphic sections of the Lefschetz fibrations $E_i \to D_i$ using the theory of horizontal sections developed by Seidel in [@seidel-les]. In particular we will apply results from section 2.5 of that paper, so we adopt its notation. This theory involves analysis of the symplectic connection, whose horizontal subspaces are the symplectic orthogonal subspaces to the fibers, and the symplectic parallel transport defined by horizontal lifting of paths in the base of the fibration.

In order for this technique to work, we need to set up carefully a model Lefschetz fibration over a base $S$, the disk with one end, in order to ensure that all the sections we need to count are in fact horizontal. The key properties are:

-   Transversality of the boundary conditions over the strip-like end. This means that we cannot use a standard model Dehn twist fibration, but need to introduce a perturbation somewhere.

-   Non-negative curvature. The curvature of the symplectic connection is a two-form on the base with values in functions on the fibers (the Lie algebra of the group of Hamiltonian diffeomorphisms), and we require that this two-form evaluated on a positive basis of the tangent space to the base yields a non-negative function on the fiber. The standard model Dehn twist fibration has non-negative curvature, but requiring the perturbation to have non-negative curvature imposes a constraint.

-   Vanishing action of horizontal sections. This imposes a further constraint on the perturbation.

As we progress through the construction, the definitions of all of these terms will be recalled.

The first step is to construct a fibration which is flat away from the critical point, following section 3.3 of [@seidel-les]. Let $S$ be the Riemann surface $\{\re z \leq 0, |\im z| \leq 1\} \cup \{|z| \leq 1\}$ (a negative half-strip which has been rounded off with a half-disk).

Let $M$ denote the fiber, which is a cylinder with three bands attached. The vanishing cycle $V$ is the equator of the cylinder. The circle running through the core of one of these bands is $L$. Equip $M$ with a symplectic form $\omega = d\theta$ such that $L$ is exact. Over $S^- =
(-\infty,-1]\times [-1,1]$, we let $\pi: E^- \to S^-$ be a trivial fibration and equip $E$ with 1-form $\Theta$ and 2-form $\Omega =
d\Theta$ which are pulled back from the fiber (to get a symplectic form we add the pullback a positive 2-form $\nu \in \Omega^2(S)$, but this does not affect the symplectic connection). Following the pasting procedure described in [@seidel-les §3.3] (though with the cut on the right rather than the left), we can complete this fibration $\pi: E \to S$ to one where the monodromy around the boundary is $\tau_V$, a standard model Dehn twist supported near the vanishing cycle. The result has non-negative curvature, is actually trivial on the part of the fiber away from the support of the Dehn twist, and is flat over the part of the base away from the critical value.

For this fibration, there is a Lagrangian boundary condition which over the end corresponds to the pair $(L,\tau_V(L))$. Of course, these are not transverse since $\tau_V$ is identity in the band. Hence we will perturb the symplectic form by a term which depends on a Hamiltonian. We will introduce the perturbation in a neighborhood of the edge $(-\infty,-1]\times \{1\}$. Let $\beta$ be a cutoff function which

-   is supported in $U = \{s+it\mid -2\leq s \leq -1, 1-\epsilon \leq t
      \leq 1 \}$,

-   vanishes along the bottom, left and right sides of $U$, and

-   has $\partial\beta/\partial t \geq 0$.

Figure [1](#fig:horizontal-sections){reference-type="ref" reference="fig:horizontal-sections"} shows the base of the fibration; the region where $\beta$ has support is shaded.

![The base of the fibration with the region of perturbation shaded.](horizontal-sections){#fig:horizontal-sections width="2.5in"}

Let $H$ be a Hamiltonian function on the fiber $M$, and let $X_H$ be its vector field defined by $\omega(\cdot, X_H) = dH$. Then over $S^-$, where our fibration was originally trivial with $\Omega =
d\Theta$ pulled back from the fiber, consider $$\Theta' = \Theta + H \beta ds$$ $$\Omega' = d\Theta' = \Omega + \beta dH \wedge ds - H(\partial
  \beta/\partial t) ds\wedge dt$$

This modifies the symplectic connection as follows: Let $Y \in TE^v$ denote the general vertical vector. Then if $Z \in TS$, and $Z^h$ is its horizontal lift $$0= \Omega'(Y,Z^h) = \Omega(Y,Z^h) + \beta dH(Y)ds(Z)$$

If we denote by $Z$ again the horizontal lift with respect to the trivial connection, we have $Z^h = Z - \beta ds(Z) X_H$. Since $\beta
\geq 0$, this means that as we parallel transport in the *negative* $s$-direction through the region $U$, we pick up a bit of the Hamiltonian flow of $H$, compared with the trivial connection. By adjusting the function $\beta$, we can ensure that the parallel transport along the boundary in the positive sense picks up $\phi_H$, the time 1 flow of $H$.

We must compute the curvature of this connection. This is the 2-form on the base with values in functions on the fibers given by $\Omega'(Z_1^h,Z_2^h)$. It will suffice to compute for $Z_1
= \partial/\partial s$ and $Z_2 = \partial/ \partial t$, a positive basis. We have $Z_1^h = \partial/\partial s - \beta X_H$ and $Z_2
= \partial/\partial t$. $$\begin{split}
  \Omega'(Z_1^h,Z_2^h) &=\\
 \Omega(Z_1^h,Z_2^h) &+ \beta
  dH(Z_1^h)ds(Z_2^h) - \beta dH(Z_2^h)ds(Z_1^h) -
  H(\partial\beta/\partial t) ds\wedge dt(Z_1^h,Z_2^h)
\end{split}$$ The first term vanishes because $Z_2^h$ is horizontal for the trivial connection, the second term because $ds(Z_2^h) = 0$, and the third because $dH(Z_2^h) = 0$. This leaves $-H(\partial\beta/ \partial
t)ds\wedge dt(Z_1^h,Z_2^h) = -H(\partial \beta/\partial t)$. By our assumptions on $\beta$, this is non-negative as long as $H \leq 0$.

We equip the deformed fibration with a Lagrangian boundary condition $Q$ given by parallel transport of $L$ around the boundary. This picks up a Dehn twist and the time 1 flow of $H$, so over the end we have the pair $(L,\phi_H(\tau_V(L)))$.

A *horizontal section* is a map $u: S \to E$ such that $Du(TS) =
TE^h$. The importance of such sections is that, while they are determined by the symplectic connection, they are pseudo-holomorphic for any *horizontal complex structure* $J$, meaning an almost complex structure that preserves $TE^h$ and for which the projection $E \to S$ is holomorphic.

The *action* $A(u)$ of a section $u$ is defined to be $\int_S u^*
\Omega'$. The symplectic area of $u$ is then $A(u) + \int_S \nu$. The identity relating action to energy is ([@seidel-les], eq. 2.31) $$\label{eq:energy-action}
\frac{1}{2}  \int_S ||(Du)^v||^2 + \int_S f(u) \nu = A(u) + \int_S
||\bar{\partial}_J u||^2$$ for any horizontal complex structure $J$. Here $Du = (Du)^h + (Du)^v$ is the splitting induced by the connection, and $f$ is the function determined by the curvature as $f(\pi^*\nu|TE^h) = \Omega'|TE^h$. In our example $f$ is supported near the critical point and in $\Supp
\beta$, where $f = -H(\partial\beta/\partial t)$.

A direct consequence of [\[eq:energy-action\]](#eq:energy-action){reference-type="eqref" reference="eq:energy-action"} is the following:

::: proposition
[]{#prop:action-zero label="prop:action-zero"} If the curvature of $\pi: E \to S$ is non-negative, and if $u$ is a $J$-holomorphic section with $A(u) = 0$, then $u$ is horizontal and the curvature function $f$ vanishes on the image of $u$.
:::

With all this in mind, we choose our Hamiltonian $H: M \to \R$ as follows:

-   $H \leq 0$ and $H = 0$ near $\partial M$. This ensures that the fibration is still trivial near the horizontal boundary and that the curvature is non-negative within $\Supp \beta$.

-   $H$ achieves its global maximum of $0$ near $\partial M$ and on the "cocore" of the band in $M$. It achieves its minimum along the vanishing cycle, and has no other critical points in the cylinder or lying on $L$ (which intersects the vanishing cycle and the cocore once). The first condition implies that horizontal sections passing through the cocore do not pick up any curvature, while the second is there in order to ensure that $(L,\phi_H(\tau_V(L)))$ is a transverse pair.

-   The flow $\phi_H$ has the property that $L \cap
      \phi_H(\tau_V(L))$ consists of one point $x$ lying on the cocore of the band. At this point, the tangent space to $\phi_H(\tau_V(L))$ is a small clockwise rotation of the tangent space to $L$.

    This implies that this intersection point has degree zero. To see this, recall from Section [\[sec:gradings\]](#sec:gradings){reference-type="ref" reference="sec:gradings"} that the fiber has foliation by circles. We extend this foliation into the attached bands, foliating each band by intervals. The Dehn twist $\tau_V$ preserves this foliation, so it admits a grading in the sense of [@seidel-book (12i)], namely an $\R$-valued lift of the $S^1$-valued function $\alpha(D\tau_V(\Lambda))/\alpha(\Lambda)$ defined on the Lagrangian Grassmannian bundle. We can choose the lift to be zero in the bands, where $\tau_V$ is the identity. The Lagrangians $L$ and $\phi_H(\tau_V(L))$ do not rotate with this foliation, so they admit gradings. Thus, if we equip $L$ with some grading and $\phi_H(\tau_V(L))$ with the induced grading, the $\R$-valued grading functions for $L$ and $\phi_H(\tau_V(L))$ differ by a small amount. Since tangent space to $\phi_H(\tau_V(L))$ is a small clockwise rotation of the tangent space to $L$, the intersection point $x$ has degree zero.

After this setup, we come to the problem of determining the set $\cM_J(x)$ of $J$-holomorphic sections $u: S \to E$ satisfying $u(\partial S) \subset Q$ which are asymptotic to $x \in L \cap \phi_H(\tau_V(L))$ over the end.

::: proposition
[]{#prop:horiz-sections label="prop:horiz-sections"} Let $J$ be a horizontal complex structure. Then $\cM_J(x)$ consists of precisely one section. It is horizontal, has $A(u) = 0$, and is regular.
:::

::: proof
*Proof.* The first step is to construct a horizontal section. Any horizontal section, if it exists, is determined by parallel transport of the point $x \in L\cap \phi_H(\tau_V(L))$ throughout $E$. Consider the section over $S^-$ given by $u^-: (s,t) \mapsto (s,t,x)$. This is horizontal outside $\Supp \beta$, since the fibration is trivial over $S^- \setminus \Supp \beta$. In $\Supp \beta$, the fact that $x$ lies at a critical point of $H$ means that $(TE^h)_{(s,t,x)}$ is the same as for the trivial connection, so the section is horizontal there as well. Near the singularity, the fibration is trivial in the band where $x$ lies, so $u^-$ extends to a horizontal section $u: S
  \to E$.

For this section, we compute $A(u) = \int_S u^*\Omega'$. Since $u$ lies in the region where $\tau_V$ is trivial, $\int_{S \setminus
    \Supp \beta} u^* \Omega' = 0$. Since $u$ passes through the point $x$ where $H(x) = 0$, the contribution $\int_{\Supp \beta}
  u^*\Omega' = \int_{\Supp \beta} -H(x)(\partial \beta/\partial t)\nu$ vanishes.

Since $A(u) = 0$, any $u' \in \cM_J(X)$ must also have action $0$. To see this, note that $\Theta'$ is exact on each fiber of the boundary Lagrangian $Q$. This implies that $\Theta'|_Q = \pi^*\kappa_Q + dK_Q$, where $\kappa_Q$ is a one-form on $\partial S$, and $K_Q$ is a function on $Q$. Thus $$A(u) = \int_S u^*\Omega' = \int_{\partial S} u^*\Theta' = \int_{\partial S} \kappa_Q + \int_{\partial S} dK_Q$$ The first term on the right-hand side does not depend on $u$, and the second term, which is the net change in $K_Q$ along $u(\partial S)$, depends on the asymptotic data for $u$, which is the same for all $u \in \cM_J(X)$.

Because the curvature of $\pi: E\to S$ is non-negative, proposition [\[prop:action-zero\]](#prop:action-zero){reference-type="ref" reference="prop:action-zero"} implies that $u'$ is horizontal. Since $u'$ and $u$ are both asymptotic to $x$, they are equal. Hence $\cM_J(x) = \{u\}$.

It remains to show that $u$ is regular. The linearization of parallel transport along $u$ trivializes $u^*(TE^v)$ such that the boundary condition $u^*(TQ)$ is mapped to a family of Lagrangian subspaces which, as we traverse $\partial S$ in the positive sense, tilt clockwise by a small amount. That $\ind D_{u,J} = 0$ follows from Proposition 11.13 of [@seidel-book]. On the other hand, Lemma 2.27 of [@seidel-les] applies to the section $u$, implying $\ker D_{u,J} = 0$. We could also appeal to Lemma 11.5 of [@seidel-book] (with $\mu(\rho_1) = 0$ and $|\Sigma^-| = 1$) to see that $\ker D_{u,J} = 0$. Hence $\coker D_{u,J} = 0$ as well. ◻
:::

## Polygons with fixed conformal structure {#sec:sections-polygon}

Recall from section [\[sec:degenerated-spaces\]](#sec:degenerated-spaces){reference-type="ref" reference="sec:degenerated-spaces"} the trivial fibration $\pi: \hat{X}^0 \to T^0$, with fiber $M$, where $T^0$ is a a disk with $(k+3)$ boundary punctures. We have $\hat{X}^0 = M \times T^0$ symplectically. We equip $\hat{X}^0$ with a product almost complex structure $J = J_M \times j$, where $j$ is the complex structure on $T^0$.

::: proposition
[]{#prop:sections-polygon label="prop:sections-polygon"} The $(j,J)$-holomorphic sections $u: T^0 \to \hat{X}^0$ are in one-to-one correspondence with $(j,J_M)$-holomorphic maps $u_M: T^0
  \to M$.
:::

::: proof
*Proof.* Given $u: T^0 \to \hat{X}^0$, write $u =(u_M, u_{T^0})$ with respect to the product splitting. Since $J$ is a product each component is pseudo-holomorphic in the appropriate sense. But $u_{T^0}$ is the identity map because $u$ is a section. This correspondence is clearly invertible. ◻
:::

This reduces the problem of counting sections $u:T^0 \to \hat{X}^0$ to the problem of counting maps $u_M: T^0 \to M$. We emphasize that we are counting maps from a Riemann surface with a fixed conformal structure.

The maps $u_M:T^0 \to M$ are holomorphic maps between Riemann surfaces, and hence their classification is mostly combinatorial. However, because we are in a situation where the conformal structure on the domain is fixed, we are not quite in the situation described, for example, in [@seidel-book §13]. The holomorphic curves we are looking for have non-convex corners and hence boundary branch points or "slits," and if the situation is complicated enough they may also have branch points in the interior. However, the condition that the conformal structure of the domain is fixed makes this an index zero problem, which is to say it prevents these slits and branch points from deforming continuously. The question is then, given a combinatorial type of such a curve, what conformal structures (with multiplicity) can be realized by holomorphic representatives?

The $(k+3)$ boundary components of $T^0$ are equipped with Lagrangian boundary conditions $\hat{L}(0)^0, \hat{L}(n)^0_0,
\dots, \hat{L}(n)^0_k, \hat{L}(n+m)^0$. Recall that over the ends where disk bubbles are attached we have $\hat{L}(n)^0_i = \tau_i(
\hat{L}(n)^0_{i-1})$, where $\tau_i$ is the monodromy around the $i$-critical point inside the $i$-th disk bubble. In section [\[sec:horiz-sections\]](#sec:horiz-sections){reference-type="ref" reference="sec:horiz-sections"}, we refined the construction and made a particular choice for this monodromy: $$\label{eq:monodromies-equal}
  \tau_i = \phi_H \circ \tau_V$$ Since all of these symplectomorphisms are isotopic, we will denote them all by $\tau$ for most of this section.

In order to simplify notation, for the rest of this section [0.1](#sec:sections-polygon){reference-type="ref" reference="sec:sections-polygon"} we will drop the hats and superscript zeros and denote by $$L(0),L(n),\tau L(n), \tau^2 L(n),\dots \tau^k L(n), L(n+m) \subset M$$ the Lagrangians in the fiber $M$ which give rise to the boundary conditions over the $(k+3)$-punctured disk $T$. Though the monodromies are all denoted by $\tau$, we actually choose the perturbations slightly differently so as to ensure that this collection of Lagrangians is in general position in $M$; this is necessary for the argument in Lemma [\[lem:existence\]](#lem:existence){reference-type="ref" reference="lem:existence"}.

Recall that $q_1 = q_{a,i}$ and $q_2 = q_{b,j}$ are the morphisms whose product we wish to compute. We now regard $q_{a,i} \in L(0)\cap
L(n)$ and $q_{b,j}\in \tau^kL(n)\cap L(n+m)$. Let $x_i \in
\tau^{i-1}L(n) \cap \tau^i L(n)$ denote the unique intersection point.

Recall that the possible output points $q_{a+b,h} \in L(0)\cap L(n+m)$ are indexed by $h \in \{0,1,\dots,
\left\lfloor\frac{(n+m)-|a+b|}{2}\right\rfloor\}$.

We can now state the main results of this section.

::: proposition
[]{#prop:which-output label="prop:which-output"} If $h$ is such that $0 \leq h-(i+j) \leq k$, then there are $\binom{k}{h-(i+j)}$ homotopy classes of maps $u:T\to M$ satisfying the boundary conditions and asymptotic to $q_{a,i},x_1,\dots,x_k,q_{b,j},q_{a+b,h}$ at the punctures. For $h$ outside this range there are no holomorphic maps satisfying these conditions.
:::

::: proposition
[]{#prop:polygon-count label="prop:polygon-count"} For each feasible homotopy class from Proposition [\[prop:which-output\]](#prop:which-output){reference-type="ref" reference="prop:which-output"}, and for each complex structure $j$ on $T$, there is exactly one holomorphic representative $u: T \to M$.
:::

The strategy of proof is first to prove Proposition [\[prop:which-output\]](#prop:which-output){reference-type="ref" reference="prop:which-output"}, which is done in §[0.1.1](#sec:homotopy-classes){reference-type="ref" reference="sec:homotopy-classes"}. Then we show the existence of holomorphic representatives for some conformal structure (§[0.1.2](#sec:existence){reference-type="ref" reference="sec:existence"}), and show that the number of representatives does not depend on the conformal structure. By degenerating the domain we are able to show uniqueness (§[0.1.3](#sec:moduli-space){reference-type="ref" reference="sec:moduli-space"}).

### Homotopy classes {#sec:homotopy-classes}

The analysis of homotopy classes requires some explicit combinatorics, which we shall now set up. Recall that $M$ is a cylinder with three bands attached, one for each of $L(0),L(n),L(n+m)$. We will classify homotopy classes of maps $u: T\to M$ by their boundary loop $\partial
u$, which must be contractible, traverse $L(0),L(n),\dots,\tau^kL(n),L(n+m)$ in order, and hit the intersection points $q_{a,i},x_1,\dots,x_k,q_{b,j},q_{a+b,h}$ in order. That they arise as the boundary of a holomorphic map controls their behavior within the bands.

Let us use $L(n)$ to frame the cylinder, so that winding around the cylinder is computed with respect to $L(n)$. Let $x \in M$ be a basepoint which is located in the band near the intersection points $x_r$. Let $\alpha \in \pi_1(M,x)$ denote a loop that enters the cylinder from the bottom, veers right, winds around once, and goes back downward to $x$. We also have a class $\beta \in \pi_1(M)$ that is represented by the loop $L(n)$, oriented upward through the cylinder. Note that $\alpha$ and $\beta$ generate a free group in $\pi_1(M)$.

::: lemma
$L(0)$ winds $-(n-|a|)/2$ times relative to $L(n)$. $\tau^r L(n)$ winds $r$ times relative to $L(n)$. $L(n+m)$ winds $(m-|b|)/2 + k$ times relative to $L(n)$.
:::

::: proof
*Proof.* We are using the symbols $L(0), \tau^rL(n), L(n+m)$ to represent certain Lagrangians in a single fiber $M$, but we can compute the windings by comparing our situation to certain fibers of the original fibration. In the original fibration, $L(0)$ and $L(n)$ intersect in the fiber containing $q_{a,i}$. Thus we have that $L(0)$ winds $-(n-|a|)/2$ times relative to $L(n)$. Now $\tau^r L(n)$ winds $r$ times relative to $L(n)$ by construction. Finally, in the original fibration $L(n+m)$ and $L(n)$ intersect in the fiber containing $q_{b,j}$, and the relative winding in that fiber is $(m-|b|)/2$. In the current context, this becomes the winding of $L(n+m)$ relative to $\tau^k L(n)$. Thus the winding of $L(n+m)$ relative to $L(n)$ in current context is $(m-|b|)/2 + k$. ◻
:::

The only unknown is how many times the boundary path traverses $L(0)$, $L(n)$, $\tau L(n)$, etc., as we traverse the boundary in the positive sense. The argument from Proposition [\[prop:extended-sections\]](#prop:extended-sections){reference-type="ref" reference="prop:extended-sections"} shows that a holomorphic map cannot enter the bands corresponding to $L(0)$ and $L(n+m)$. Hence the portion of our loop along $L(0)$ and $L(n+m)$ lies within the cylinder, and therefore it is determined by the choices of $q_{a,i}$, $q_{b,j}$ and $q_{a+b,h}$.

As for the portion of the loop along $\tau^r L(n)$, this can be represented by a sequence of integers $(\delta_r)_{r=0}^k$, where $\delta_r$ represents the number of times we wind around $\tau^r
L(n)$.

With these conventions in place, we can compute the winding of a choice of paths satisfying the boundary and asymptotic conditions. We record the parts of the computation:

-   Passing from $x_k$ to $q_{b,j}$ by a short upward path on $\tau^k L(n)$ contributes $$\left(1-\frac{j}{(m-|b|)/2}\right)\left(k\right)$$

-   The winding around the cylinder along $L(n+m)$ as we pass from $q_{b,j}$ to $q_{a+b,h}$ is $$\left[\frac{h}{(n+m-|a+b|)/2} - \frac{j}{(m-|b|)/2}\right]
      (-1)((m-|b|)/2 + k)$$

-   The winding around the cylinder along $L(0)$ as we pass from $q_{a+b,h}$ to $q_{a,i}$ is $$\left[\frac{i}{(n-|a|)/2} - \frac{h}{(n+m-|a+b|)/2}\right] (n-|a|)/2$$

-   Passing from $q_{a,i}$ to $x_1$ by a short downward path on $L(n)$ contributes $0$ to the winding around the cylinder.

Adding up these contributions and using the fact that $(m-|b|)/2 +
(n-|a|)/2 + k = (n+m-|a+b|)/2$, we get a total of $i+j - h+ k$. Thus, if we go up on $\tau^k L(n)$ and down on $L(n)$, we pick up the class $\alpha^{i+j-h+k} \in \pi_1(M,x)$ for the loop from $x_k$ to $x_1$.

Thus, the class $\alpha^{i+j-h+k}$ corresponds to the choice $\delta_r = 0$ for $0 \leq r \leq k$. The homotopy class of any other path can be computed from this as follows:

-   Taking another path on $L(n)$ contributes a factor $\beta^{\delta_0}$ on the right.

-   Passing from $x_{r}$ to $x_{r+1}$ along $\tau^r L(n)$ contributes the word $$(\alpha^r\beta)^{\delta_r}$$ where $\delta_r \in \Z$, and this class is added on the right.

-   Going down on $\tau^kL(n)$ rather than up contributes the class $(\alpha^k\beta)^{\delta_k}$ on the left, which up to conjugation is the same as adding the class $(\alpha^k\beta)^{\delta_k}$ on the right.

Thus the class in question is $$\label{eq:homotopy-class}
  \alpha^{i+j-h+k} \prod_{r = 0}^k (\alpha^r \beta)^{\delta_r}$$ The key condition is that this class is trivial in $\pi_1(M)$. This means in particular that all of the $\beta$'s must cancel out. Because $\alpha$ and $\beta$ generate a free group we have the following:

::: lemma
[]{#lem:beta-cancel label="lem:beta-cancel"} In the word [\[eq:homotopy-class\]](#eq:homotopy-class){reference-type="eqref" reference="eq:homotopy-class"}, the $\beta$'s cancel out if and only if $\delta_r \in \{-1,0,1\}$ for $0 \leq r \leq k$, the first nonzero $\delta$ is $1$, the last nonzero $\delta$ is $-1$, and the nonzero $\delta$'s alternate in sign.
:::

::: proof
*Proof.* The first thing to see is that $|\delta_r| \leq 1$ for $1 \leq r
  \leq k$. This is because $(\alpha^r\beta)^2 =
  \alpha^r\beta\alpha^r\beta$ contains an isolated $\beta$, while $(\alpha^r \beta)^{-2}$ contains an isolated $\beta^{-1}$. Then we can see that the nonzero $\delta$'s must alternate sign, since having two consecutive $\delta$'s equal to $1$ yields $\alpha^{r_1}\beta\alpha^{r_2}\beta$, which has an isolated beta, while having two consecutive $\delta$'s equal to $-1$ would yield an isolated $\beta^{-1}$.

Since the nonzero $\delta$'s in the range $1 \leq r \leq k$ alternate in sign, all the $\beta$'s coming from the range $1 \leq r \leq k$ cancel, except for possibly the first or the last. This implies that $|\delta_0| \leq 1$ as well, since the only thing that can cancel $\beta^{\delta_0}$ is the first non-identity factor or the last non-identity factor.

Now the $\beta$ from the first non-identity factor can only cancel the $\beta$ from the last non-identity factor if all the $\alpha$'s as well as $\beta$'s in between cancel. This means that $$\sum_{r = a}^b r\delta_r = 0$$ for the appropriate range of $r$: $a \leq r \leq b$. Since the $\delta$'s are in $\{-1,0,1\}$ and they alternate in sign, the only solution to this equation is when all $\delta = 0$. In this case, the first and the last non-identity factors are in fact consecutive, the first has $\delta = 1$, while the last has $\delta
  = -1$. This shows that it is impossible to have $\beta^{-1}$ from the first factor cancel a $\beta$ from the last factor.

In general, we find that each $\beta$ is canceled by a $\beta^{-1}$ from the next non-identity factor, so that the nonzero $\delta$'s alternate sign for $0 \leq r \leq k$, the first nonzero $\delta$ is $1$, and the last nonzero $\delta$ is $-1$. ◻
:::

By passing to $H_1(M;\Z)$, we obtain the relations $$\label{eq:sum-zero}
  \sum_{r=0}^k \delta_r = 0$$ $$\label{eq:get-h}
  i+j-h+k + \sum_{r=0}^k r\delta_r =0$$ Equation [\[eq:sum-zero\]](#eq:sum-zero){reference-type="eqref" reference="eq:sum-zero"} is implied by Lemma [\[lem:beta-cancel\]](#lem:beta-cancel){reference-type="ref" reference="lem:beta-cancel"}, while [\[eq:get-h\]](#eq:get-h){reference-type="eqref" reference="eq:get-h"} determines which $h$ the homotopy class contributes to.

The sequences $(\delta_r)_{r=0}^k$ which solve the constraints are in one-to-one correspondence with sequences $(s_r)_{r=0}^{k-1}$ such that $s_r \in \{0,1\}$. In one direction, we extend the sequence by $s_{-1}
= 0 = s_k$, and set $$\delta_r = s_r - s_{r-1}$$ In the other direction, given $\delta_r$, we can solve for $s_r$ using this equation the initial condition $s_{-1}=0$. Since the signs of the nonzero $\delta_r$ alternate, and the first nonzero term is $1$, we will have $s_r \in \{0,1\}$, and since the final nonzero term is $-1$, we will have $s_k = 0$, thus inverting the correspondence. This yields $2^k$ solutions.

Plugging this into the summation in [\[eq:get-h\]](#eq:get-h){reference-type="eqref" reference="eq:get-h"}, we have $$\sum_{r=0}^k r\delta_r = \sum_{r=0}^k r(s_r-s_{r-1}) =
  \sum_{r=0}^{k-1} (-1)s_r$$ because the summation telescopes. This is simply minus the number of $1$'s in the sequence $s_r$. Thus we obtain $$\label{eq:get-h-2}
  h-(i+j) = k - \sum_{r=0}^{k-1}s_r$$ The right hand side is always an integer between $0$ and $k$, and it takes the value $s$ for $\binom{k}{s}$ choices of the sequence $(s_r)_{r=0}^{k-1}$. Thus homotopy classes of maps exist for $h$ such that $0 \leq h-(i+j) \leq k$, and there are $\binom{k}{h-(i+j)}$ such classes. This proves Proposition [\[prop:which-output\]](#prop:which-output){reference-type="ref" reference="prop:which-output"}.

### Existence of holomorphic representatives for some conformal structure {#sec:existence}

The first step in characterizing the holomorphic representatives of these homotopy classes is to prove the existence of holomorphic sections for some conformal structure. This is also essentially combinatorial.

We begin with some general concepts that will be useful in the proof.

::: definition
Let $\gamma: S^1 \to \C$ be a piecewise smooth loop. A *subloop* $\gamma'$ of $\gamma$ is the restriction $\gamma' =
  \gamma|\bigcup_\alpha I_{\alpha}$ to a collection of intervals $\bigcup_\alpha I_{\alpha}$. The indexing set inherits a cyclic order from $S^1$, and we require that for each $\alpha$, $\gamma(\max I_{\alpha}) = \gamma(\min I_{\alpha+1})$ is a self-intersection of $\gamma$. Thus $\gamma'$ simply "skips" the portion of $\gamma$ between $\max I_\alpha$ and $\min
  I_{\alpha+1}$. A subloop is called *simple* if it is non-self-intersecting.
:::

Note that a subloop is not the same as a loop formed by segments of $\gamma$ joining self-intersections. Such an object is only a subloop if the segments appear in a cyclic order compatible with $\gamma$.

::: definition
A piecewise smooth loop $\gamma: S^1 \to \C$ is said to have the *(weak) positive winding property* (PWP) if the winding number of $\gamma$ around any point in $\C \setminus \image(\gamma)$ is non-negative. The loop $\gamma$ is said to have the *strong positive winding property* (SPWP) if every subloop $\gamma' \subset
  \gamma$ has the positive winding property.
:::

::: lemma
[]{#lem:simple-spwp label="lem:simple-spwp"} A loop $\gamma: S^1 \to \C$ has SPWP if and only if every *simple* subloop has PWP.
:::

::: proof
*Proof.* The "only if" direction is contained in the definition. Suppose that every simple subloop of $\gamma$ has PWP. If $\gamma'$ is a subloop that is not simple, then by splitting $\gamma'$ at a self-intersection, we can write $\gamma'$ as the composition of two proper subloops. Repeating this inductively, we can write $\gamma'$ as the composition of simple subloops. By hypothesis, each of these subloops winds positively, and the winding of $\gamma'$ about a point is the sum of the contributions from each of the simple subloops. ◻
:::

The next lemma shows that the strong positive winding property is stable under branched covers. Suppose $\gamma$ is a loop and $y \in \C
\setminus \image(\gamma)$ is a point where the winding number of $\gamma$ is $m > 1$. Taking the $m:1$ cover branched at $y$, we can lift $\gamma$ to a path $\tilde{\gamma}$. The path $\tilde{\gamma}$ is a loop that covers $\gamma$.

::: lemma
[]{#lem:spwp label="lem:spwp"} Suppose $\gamma$ has SPWP. Then $\tilde{\gamma}$ has SPWP.
:::

::: proof
*Proof.* Suppose that $\tilde{\gamma}$ does not have SPWP. Then some subloop $\tilde{\gamma}'$ does not have PWP. By Lemma [\[lem:simple-spwp\]](#lem:simple-spwp){reference-type="ref" reference="lem:simple-spwp"}, we may take $\tilde{\gamma}'$ to be a *simple* subloop. Thus $\tilde{\gamma}'$ winds around some region once clockwise, and we have $\tilde{\gamma}' = \partial \tilde{C}$, where $\tilde{C}$ is the chain consisting of this region with coefficient $-1$. Pushing $\tilde{\gamma}'$ and $\tilde{C}$ forward under the branched cover, we obtain a subloop $\gamma' \subset \gamma$, and chain $C$ such that $\gamma' = \partial C$. Since $\tilde{C}$ is purely negative, no cancellation can occur when we push forward, and $C$ is purely negative as well. Thus $\gamma'$ winds negatively about a point in the support of $C$, which contradicts SPWP for $\gamma$. ◻
:::

::: lemma
[]{#lem:spwp-mapping label="lem:spwp-mapping"} Suppose $\gamma: S^1 \to \C$ is a piecewise smooth loop with SPWP. Then there is a map $u:D^2 \to \C$ holomorphic on the interior of $D^2$ such that $\partial[u] = \gamma$.
:::

::: proof
*Proof.* The idea of the proof is to iteratively take branched covers of the plane and lift $\gamma$ so as to reduce the density of winding. So let $y \in \C \setminus \image(\gamma)$ be a point where the winding number is $m > 1$. Taking the $m:1$ branched cover at $y$, we obtain as in Lemma [\[lem:spwp\]](#lem:spwp){reference-type="ref" reference="lem:spwp"} a lift $\tilde{\gamma}$ that covers $\gamma$ once and has SPWP. Repeating this process and using Lemma [\[lem:spwp\]](#lem:spwp){reference-type="ref" reference="lem:spwp"} to guarantee that the lift always has SPWP, eventually we obtain a *simple* piecewise smooth loop with positive winding. This loop bounds a simply connected region in $M$, where $M$ is the Riemann surface resulting from the branched covering construction. By the Riemann mapping theorem, there is a map from this region to the unit disk $D^2$, biholomorphic on the interior and continuous on the closure, that maps each boundary segment to an arc in $\partial D^2$ and each corner to a point on $\partial D^2$. Let $\tilde{u} : D^2 \to M$ be the inverse of that map. Composing $\tilde{u}$ with the covering $M \to \C$ yields the desired map $u$. ◻
:::

Fix a choice of homotopy class $\phi$ of polygons $u: T\to M$, which essentially means fixing a choice for the sequence $(\delta_r)_{r=0}^k$. Passing to the universal cover $\tilde{M}$ of the fiber, fix a choice of lift $\tilde{u}:T \to \tilde{M}$. Let $y
\in \tilde{M}$ be any point. Because the boundary loop $\partial[u]$ is contractible in $M$, it lifts to a closed loop $\partial[\tilde{u}]$ in $\tilde{M}$. In fact $\partial[\tilde{u}]$ is contained in a domain which is isomorphic to a domain in $\C$, and with this identification, we have the following.

::: lemma
[]{#lem:positive-winding label="lem:positive-winding"} The boundary loop $\partial[\tilde{u}]$ has SPWP.
:::

::: proof
*Proof.* The key observation is that the slopes of the paths $L(0),
  L(n),\dots,\tau^k L(n), L(n+m)$ through the cylinder are positive and monotonically decreasing. If we frame the cylinder using $L(0)$, then

-   $L(0)$ has slope $\infty$

-   $L(n)$ has slope $[(n-|a|)/2]^{-1}$

-   $\tau^r L(n)$ has slope $[r+(n-|a|)/2]^{-1}$

-   $L(n+m)$ has slope $[(n+m-|a+b|)/2]^{-1}$.

Only at the intersection between $L(n+m)$ and $L(0)$ does the slope increase.

Hence as we traverse $\partial[\tilde{u}]$, or any subloop thereof, the slope can only increase at one point. This point is either where the subloop either uses or skips over $L(0)$.

Now we use some elementary plane geometry. Suppose that $P$ is an oriented polygonal path in the plane (possibly self-intersecting), all of whose sides $(S_i)_{i=1}^N$ have positive slope. Suppose that $P$ winds negatively around some point $y$. We claim the slope has to increase at no fewer than two vertices. We prove this by induction on the number of sides $N$.

Checking cases proves the claim when $N=3$ and $P$ is a triangle. See figure [2](#fig:spwp){reference-type="ref" reference="fig:spwp"}(a).

Suppose for induction that the claim is true for $N < N_0$. Now we prove the claim if $P$ is a *simple* $N_0$-gon, so assume for a contradiction that $P$ is a simple $N_0$-gon that winds negatively and has at most one vertex where the slope increases. We assume that $N_0 > 3$, so there must be a side $S_i$ such that at both ends there is a decrease in slope. We remove the side $S_i$ from the $N_0$-gon $P$ and extend the two incident sides $S_{i-1}$ and $S_{i+1}$ in order to obtain an $(N_0-1)$-gon $P'$. Since $P$ has at most one vertex where the slope increases, so does $P'$: Since the slope decreased at both $S_{i-1}S_i$ and at $S_iS_{i+1}$, it will decrease at the new vertex $S_{i-1}S_{i+1}$. See Figure [2](#fig:spwp){reference-type="ref" reference="fig:spwp"}(b). Since the original simple loop $P$ winds negatively, the new loop $P'$ must also wind negatively around some point. This contradicts the induction hypothesis. Now we have established the claim for simple $N_0$-gons.

![(a) Negatively winding triangles with positive slopes have two slope increases ($m$ denotes slope). (b) Removing the side $S_2$.](spwp){#fig:spwp width="3.75in"}

Now suppose $P$ is a self-intersecting $N_0$-gon, that winds negatively around $y$. Using Lemma [\[lem:simple-spwp\]](#lem:simple-spwp){reference-type="ref" reference="lem:simple-spwp"}, we can find a simple subloop $P'$ winding negatively around $y$. Since $P'$ is a simple $N$-gon for some $N \leq N_0$, it must have at least two vertices where the slope increases. For each vertex $v$ of $P'$ where the slope of $P'$ increases, there is a vertex in the original polygon $P$ where the slope increases, either at $v$ itself, or at some point in the interval of $P$ that was deleted at $v$. Thus, since $P'$ has at least two vertices where the slope increases, so does $P$. ◻
:::

Having chosen a lift $\partial[\tilde{u}]$ of the boundary loop, define a $2$-chain $C$ on $\tilde{M}$ whose multiplicity at $y$ is the winding number of $\partial[\tilde{u}]$ around $y$. This has $\partial C
= \partial[\tilde{u}]$.

::: lemma
[]{#lem:existence label="lem:existence"} There is a complex structure $j$ on $T$ and a holomorphic map $\tilde{u}: T \to \tilde{M}$ such that $\tilde{u}_*[T] = C$.
:::

::: proof
*Proof.* Lemma [\[lem:positive-winding\]](#lem:positive-winding){reference-type="ref" reference="lem:positive-winding"} allows us to apply Lemma [\[lem:spwp-mapping\]](#lem:spwp-mapping){reference-type="ref" reference="lem:spwp-mapping"}, which yields map $\tilde{u} : T \to \tilde{M}$. More precisely, the complex structure on $T$ is the one obtained from uniformization of the region bounded by the simple lift of $\gamma =
  \partial[u]$ at the end of the construction in [\[lem:spwp-mapping\]](#lem:spwp-mapping){reference-type="ref" reference="lem:spwp-mapping"}, as a Riemann surface with boundary and punctures (at the non-smooth points of the loop). ◻
:::

Pushing the map $\tilde{u}$ from Lemma [\[lem:existence\]](#lem:existence){reference-type="ref" reference="lem:existence"} down to $M$, we obtain the existence of a holomorphic representative in the homotopy class $\phi$, for a particular complex structure on the domain.

### The moduli space of holomorphic representatives with varying conformal structure {#sec:moduli-space}

Let $\cM(\phi,j)$ denote the moduli space of $(j,J_M)$-holomorphic maps $u: T \to M$ in the homotopy class $\phi$. Let $\cM(\phi) =
\bigcup_{j} \cM(\phi,j)$ denote the moduli space of such maps with varying conformal structure on the domain. Let $\cR^{k+3}$ denote the moduli space of conformal structures on the disk with $(k+3)$ boundary punctures. There is a natural map $\pi: \cM(\phi) \to \cR^{k+3}$ which forgets the map.

::: lemma
[]{#lem:no-kernel label="lem:no-kernel"} For any $u \in \cM(\phi,j)$, we have $\ind D_{u,(j,J_M)} = 0$ and $\ker D_{u,(j,J_M)} = 0$.
:::

::: proof
*Proof.* Let the intersection points $q_{a,i},x_1,\dots,x_k,q_{b,j}$ be regarded as positive punctures and let $q_{a+b,h}$ be regarded as a negative puncture. Then by the conventions for Maslov index, we have that all of these intersection points have index $0$, for as we go $L(0)\to L(n)$, $L(n) \to \tau L(n)$, ..., $\tau^k L(n) \to
  L(n+m)$, and $L(0) \to L(n+m)$, the Lagrangian tangent space tilts clockwise by a small amount. Then by Proposition 11.13 of [@seidel-book] (with $|\Sigma^-| = 1$ for the negative puncture), we have $\ind D_{u,(j,J_M)} = 0$.

Furthermore, the operator $D_{u,(j,J_M)}$ is a Cauchy--Riemann operator acting on the line bundle $u^*TM$, so the results of Section (11d) of [@seidel-book] apply. The hypotheses of Lemma 11.5 are satisfied with $\mu(\rho_1) = 0$ and $|\Sigma^-| = 1$, so $\ker D_{u,(j,J_M)}
  = 0$. ◻
:::

::: lemma
[]{#lem:covering label="lem:covering"} The map $\pi: \cM(\phi) \to \cR^{k+3}$ is a proper submersion of relative dimension zero (that is, a finite covering).
:::

::: proof
*Proof.* The index $\ind D_{u,(j,J_M)} = 0$ is the expected dimension of the space of curves with fixed conformal structure. When we allow the conformal structure to vary, this adds $k = \dim \cR^{k+3}$ dimensions, so $\cM(\phi)$ has expected dimension $k$. Lemma [\[lem:no-kernel\]](#lem:no-kernel){reference-type="ref" reference="lem:no-kernel"} implies $\coker D_{u,(j,J_M)} = 0$, so $\cM(\phi)$ is a manifold of dimension $k$.

If $u \in \cM(\phi,j) \subset \cM(\phi)$ is a point where the map $\pi: \cM(\phi) \to \cR^{k+3}$ is not a submersion, we must have $\ker D\pi \neq 0$. On the other hand $\ker D\pi$ consists of infinitesimal deformations of the map which do not change the conformal structure on the domain, and so is equal to $\ker
  D_{u,(j,J_M)}$, which is zero by the previous lemma. Hence $\pi$ is a submersion.

The properness of $\pi$ is an instance of Gromov--Floer compactness. The only thing to check is whether, as we vary $j \in
  \cR^{k+3}$, any strips can break off. This is impossible because our boundary conditions do not bound any bigons in $M$. ◻
:::

::: lemma
[]{#lem:degree-1 label="lem:degree-1"} The map $\pi: \cM(\phi) \to \cR^{k+3}$ has degree one.
:::

::: proof
*Proof.* For this Lemma we will pass to the Gromov--Floer compactification $\bar{\pi}: \bar{\cM}(\phi) \to \bar{\cR}^{k+3}$. Because no bigons can break off, this compactification consists entirely of stable disks, and $\bar{\pi}$ is also a proper submersion. Hence to count the degree of $\pi$, it will suffice to count the points in the fiber of $\bar{\pi}$ over a corner of $\bar{\cR}^{k+3}$, which is to say when the domain is a maximally degenerate stable disk.

A maximally degenerate stable disk $S = (G, (S_\alpha))$ consists of a trivalent graph $G = (V,E^{fin} \cup E^\infty)$ without cycles, with $(k+3)$ infinite edges $E^\infty$, and a disk $S_\alpha$ with three boundary punctures for each $\alpha \in V$. The boundary punctures of $S^\alpha$ are labeled by elements of $E^{fin}\cup E^\infty$. The elements of $E^{fin}$ correspond to nodes of the stable disk, while the elements of $E^\infty$ correspond to boundary punctures of the smooth domains in $\cR^{k+3}$. The homotopy class $\phi$ determines the Lagrangian boundary conditions on each component $S_\alpha$, and the asymptotic values at the boundary punctures labeled by $E^\infty$. The position of the nodes labeled by $E^{fin}$ is not determined *a priori*.

Looking at the Lagrangians $L(0)$, $L(n)$, ..., $L(n+m)$ shows that any three of them bound triangles, and that such triangles are determined by two of the corners. Hence by tree-induction starting at the leaves of stable disk (those $S_\alpha$ for which two punctures are labeled by $E^\infty$), the positions of all the nodes are determined by $\phi$, or we run into a contradiction because no triangles consistent with the labeling exist.

Furthermore, in each homotopy class of triangles consistent with the labeling of $S_\alpha$, there is exactly one holomorphic representative.

Hence there is at most one stable map from the stable domain $S =
  (G,(S_\alpha))$ to $M$ consistent with the homotopy class $\phi$.

Thus we have shown that the degree of $\pi: \cM(\phi) \to \cR^{k+3}$ is either zero or one. On the other hand, Lemma [\[lem:existence\]](#lem:existence){reference-type="ref" reference="lem:existence"} shows that $\cM(\phi)$ is not empty, so the degree must be one. ◻
:::

Proposition [\[prop:polygon-count\]](#prop:polygon-count){reference-type="ref" reference="prop:polygon-count"} follows immediately from Lemmas [\[lem:covering\]](#lem:covering){reference-type="ref" reference="lem:covering"} and [\[lem:degree-1\]](#lem:degree-1){reference-type="ref" reference="lem:degree-1"}.

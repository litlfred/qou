---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-016-44-horizontal-sections-over-a-disk-with-one-crit
section_title: "Horizontal sections over a disk with one critical value"
section_number: 4.4
pages: 40-44
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.985
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
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

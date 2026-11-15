---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-017-46-tentacles-and-vacua
section_title: "Tentacles and vacua"
section_number: 4.6
pages: 37-42
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.983
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:tent label="sec:tent"}

Some interesting physical consequences of the difference equations [\[Meqs\]](#Meqs){reference-type="eqref" reference="Meqs"} result from the fact that they control the behavior of the index at large charges $(m,e)$, in a fairly simple manner. There are actually two ways to send $m$ and/or $e$ to infinity: we can either keep $|q|<1$ fixed, or simultaneously send $m\to \infty$ and $q\to 1$ ($\hbar\to 0$) so that $q^m$ stays fixed. In the latter case, the index $\mathcal{I}_M$ diverges, with leading asymptotics governed by the volume of $M$. Mathematically, this is a familiar phenomenon, closely related to the "Volume Conjecture" for Chern-Simons partition function. Physically, it seems closely related to $Z$-extremization [@Jafferis-Zmin], though the precise connection is still not well understood.

We will mention some aspects of the $q\to 1$ limit at the end of this section. For now, let's instead consider the less familiar limit $(m,e)\to \infty$ with $|q|<1$ fixed. The leading behavior of the index

[^1]

in this limit is simply governed by the *classical* Lagrangian $\mathcal{L}_M(x,p)$ [\[classLM\]](#classLM){reference-type="eqref" reference="classLM"}, and turns out to detect the presence of unconstrained chiral operators in the theory $T_M$. Equivalently, the leading behavior can detect when $T_M$ has a moduli space of vacua.

In order to make a more precise statement, note that superconformal theories $T_M$ (and more generally theories in class $\mathcal{R}$) should have an index $\mathcal{I}_M(m,e;q)$ such that the powers of $q$ appearing at fixed $(m,e)$ are bounded from below (*cf.* Section [\[sec:actions\]](#sec:actions){reference-type="ref" reference="sec:actions"}). Then we can define $\mathrm{lead}_M(m,e)$ to be the lowest power of $q$ the appears in $\mathcal{I}_M(m,e;q)$ --- this is the first nontrivial $R+\tfrac{j_3}{2}$ contribution of an operator with charge $e$ in the presence of flux $m$. We claim that $\mathrm{lead}_M(m,e)$ generically grows quadratically as $m,e\to \infty$, but that restricted to special rays in charge space it may instead grow linearly. These are exactly the rays along which the "amoeba" of $\mathcal{L}_M$ has a "tentacle." Moreover, when we are in an $Sp(2N,{\mathbb Z})$ duality frame such that a ray/tentacle lies in a purely electric direction, the theory $T_M$ should have an unconstrained chiral operator $\mathcal{O}$ that prodces the leading contribution to the index, and parametrizes a 3d moduli space of vacua.

![Amoebas for the tetrahedron, trefoil, and figure-eight knot Lagrangians.](amoebas){#fig:amoebas width="6.5in"}

We will try to motivate these statements physically and mathematically. To begin, let us recall the formal definition of an amoeba [@GKZ-amoeba]. Given an algebraic variety in $({\mathbb C}^*)^{2N}$, say with coordinates $(x_i,p_i)$, the amoeba is its projection to the real subspace spanned by the magnitudes

$${\rm Re}X_i = \log|x_i|\,,\qquad {\rm Re}P_i = \log|p_i|\,.$$

For example, the classical Lagrangians $\mathcal{L}_M$ for the tetrahedron, trefoil, and figure-eight knot,

[^2]

$$\begin{align} &\mathcal{L}_\Delta\,=\, p+x^{-1}-1 = 0\,, \\
 &\mathcal{L}_{\mathbf{3_1}} \,=\,  p-x^3 = 0\,,\\
 &\mathcal{L}_{\mathbf{4_1}} \,=\,  p^{-1}+(x^{-2}-x^{-1}-2-x+x^2)+p=0\,,
\end{align}$$

have the amoebas shown in Figure [1](#fig:amoebas){reference-type="ref" reference="fig:amoebas"}. A salient feature of the amoebas is that they extend asymptotically along a finite collection of semi-infinite rays, or tentacles. These tentacles occur whenever there is a solution to the defining equations of $\mathcal{L}_M$ in the limit $(|x|,|p|)=(e^{nr},e^{ns})$, $n\to \infty$, for some nontrivial integer slope vector $(r,s)$.

The tentacles of amoebas in $\mathcal{L}_M$ actually arise physically as parameter spaces of vacua for the 3d theories $T_M$ in flat ${\mathbb R}^3$. One indirect but instructive way to see this is to recall from [@DG-Sdual] or [@DGG] that the entire complex Lagrangian $\mathcal{L}_M$ is the SUSY parameter space for $T_M$ compactified on (untwisted) ${\mathbb R}^2\times S^1_R$. This effective 2d $\mathcal{N}=(2,2)$ theory has a complex, periodic twisted mass associated to each $U(1)$ global symmetry, obtained by complexifying the 3d real mass with the Wilson line of the background $U(1)$ gauge field. We can multiply this mass by the radius $R$ to make it dimensionless, and express it as

$$X = R\,m_{3d} +i\oint_{S^1_R} A\,.$$

The 2d theory also has a complexified, periodic FI parameter (or moment map), naturally obtained by combining the 3d FI parameter $\xi_{3d}$ and the 2d background $\theta$-angle:

$$P = R\,\xi_{3d} +i\theta\,.$$

The 2d twisted superpotential preserves supersymmetry when

$$\exp\left( \frac{\partial\widetilde\mathcal{W}}{\partial X}\right) = \exp(P) \label{WXP}$$

(put differently, the FI parameter $P$ contributes to $\mathcal{W}$ as $XP$), and it was argued in [@DG-Sdual; @DGG] that [\[WXP\]](#WXP){reference-type="eqref" reference="WXP"} are just the defining equations for $\mathcal{L}_M$.

To lift back up to a SUSY parameter space in 3d, we can first restrict to the real parts of $X$ and $P$, and then send $R\to\infty$. The first operation projects $\mathcal{L}_M$ onto its amoeba, and the second scales the amoeba so that only the tentacles --- a collection of semi-infinite rays --- are left. Sufficiently far along these rays, ${\rm Re}\,X$ and ${\rm Re}\,P$ (or rather $m_{3d}$ and $\xi_{3d}$) are the 3d masses and FI parameters consistent with SUSY. Near the origin, quantum corrections may still play an interesting role, which will not affect the current story.

[^3]

We emphasize that the tentacles map onto a *parameter* space of vacua. However, if any of the tentacles happen to align with the $P$ axis (or plane) at $X=0$, an actual SUSY moduli space in $T_M$ also opens up. This is because the effective background FI parameter ${\rm Re}\,P$ ($\xi_{3d}$) is a real moment map for a $U(1)$ symmetry. Then, for example, SUSY requires that $\xi_{3d}$ sets the vev for a sum of chiral fields $\sum_j Q_j|\phi_j|^2$, where $Q_j$ are the $U(1)$ charges. Preserving SUSY at any value of ${\rm Re}\,P\sim \xi_{3d}$ while simultaneously having zero mass ${\rm Re}\,X\sim m_{3d}$ means there must be an infinite flat direction in dynamical field space.

This phenomenon is simple to illustrate in the tetrahedron theory. Its amoeba does have a tentacle on the negative ${\rm Re}\,P$ axis (or $|p|\to 0$). Correspondingly, $T_\Delta$ has a free chiral operator $\phi_Z$ charged under the single global $U(1)$, whose vev parametrized a moduli space. We have $|\phi_Z|^2+\xi_{3d}=0$, or $|\phi_Z|^2\sim -\xi_{3d}\sim -{\rm Re}\,P$. The other tentacles of the amoeba lie along $|x|\to\infty$ and $|p|\to \infty,\,|x|\to 0$. In either case, we can happily preserve SUSY, though the field $\phi_Z$ becomes massive. If we apply a $T^k\in Sp(2,{\mathbb Z})$ transformation to $T_\Delta$ to shift the Chern-Simons level by $k$, the story remains essentially the same; we clearly still get a moduli space, while the amoeba gets "skewed" horizontally without lifting its tentacle from the $P$-axis. (Recall that $Sp(2,{\mathbb Z})$ simply acts by multiplication on the symplectic vector ${X\choose P}$, so $T^k:{X \choose P}\mapsto {X \choose {P+kX}}$.) On the other hand, generic $Sp(2,{\mathbb Z})$ images of $T_\Delta$ have no moduli space at all.

Now, let us return to the index. Suppose that $T_M$ has a moduli space corresponding to a tentacle of $\mathcal{L}_M$ at ${\rm Re}\,X=0$, along a ray in the ${\rm Re}\,P$ plane pointing in direction $s$ (with $s$ an $N$-dimensional vector of coprime integers). The direction $s$ selects a $U(1)$ symmetry inside $U(1)^N$ whose moment map can be nonzero. We would then expect that the moduli space is parametrized by the vev of a chiral operator $\mathcal{O}$ with electric charge $e=-s$. This operator and its powers $\mathcal{O}^n$ can potentially contribute to the index. It is not completely clear that the contribution will be the dominant one (at leading order in $q$), but if it is, then

$$\mathrm{lead}(0,-ns) = \frac{R_\mathcal{O}}{2}n\,,\qquad n\gg 0\,,$$

where $\mathcal{R}_\mathcal{O}$ is the R-charge of $\mathcal{O}$. This behavior should at east hold true for sufficiently large $n$. Thus the index (potentially) develops an asymptotically "flat" direction along the tentacles of the amoeba.

::: wrapfigure
r2.7in ![image](lead41){width="2.5in"}
:::

Here we used the presence of a moduli space to argue for linear growth of $\mathrm{lead}(m,e)$ in a distinguished electric direction --- corresponding to a tentacle in the $P$ plane. However, an $Sp(2N,{\mathbb Z})$ transformation could be used to align *any* tentacle with the $P$ plane. Since $Sp(2N,{\mathbb Z})$ acts covariantly on the index, preserving the growth of $\mathrm{lead}(m,e)$, this implies that we could actually expect linear growth along every tentacle, in any direction. Explicitly, if a tentacle extends in direction $(r,s)$, so that $(|x|,|p|)\sim (e^{nr},e^{ns})$, $n\to\infty$, lies in $\mathcal{L}_M$, then

$$\mathrm{lead}(-rn,-sn)\,\sim\,n\,,\qquad n\to \infty\,. \label{leadrs}$$

It is easy to see from Figure [\[fig:lead\]](#fig:lead){reference-type="ref" reference="fig:lead"} that this holds for $T_\Delta$: flat directions (anti)align with tentacles. In Figure [\[fig:lead41\]](#fig:lead41){reference-type="ref" reference="fig:lead41"}, we similarly plot $\mathrm{lead}_{\mathbf{4_1}}(m,e)$ for the figure-eight knot.

[^4]

For the trefoil, [\[leadrs\]](#leadrs){reference-type="eqref" reference="leadrs"} holds in a trivial way: the index $\mathcal{I}_{\mathbf{3_1}}=\delta_{e,3m}$ vanishes except right on the tentacles, where it is constant.

The behavior [\[leadrs\]](#leadrs){reference-type="eqref" reference="leadrs"} is (roughly) predicted mathematically by the general structure of the difference equations $\hat \mathcal{L}_M$, and the fact that they are quantizations of the classical Lagrangian $\mathcal{L}_M$. The simple property that the operators $\hat\mathcal{L}_M$ are polynomials in $\hat x_\pm,\,\hat p_\pm,$ and $q$, along with the assumption that indices $\mathcal{I}_M(m,e;q)$ are $q$-series bounded from below, implies that the generic growth of $\mathrm{lead}(m,e)$ is quadratic (*cf.* [@Garoufalidis-slopes]). This is essentially because the operators $\hat x_\pm, \hat p_\pm$ only involve linear factors $q^{\frac m2}$ and $q^{\frac e2}$, and can also only generate other linear factors when shifting $m$ and $e$ in quadratic parts of the index. For example, $\hat x_+\cdot q^{e^2} = (q^{\frac m2-2e-1})q^{e^2}$. All these linear factors then enable cancellations between different terms in the equations $\hat\mathcal{L}_M\mathcal{I}_M=0$.

Nevertheless, linear growth of the index is permitted along directions (anti)parallel to tentacles of the amoeba of $\mathcal{L}_M$. The tentacles are normal vectors to boundary surfaces of the Newton polygon of $\mathcal{L}_M$, and also (roughly) the Newton polygon of $\hat \mathcal{L}_M$. This allows extra cancellations to happen in the difference equations, along these distinguished directions. A more detailed, albeit heuristic, explanation is given in Appendix [\[app:tent\]](#app:tent){reference-type="ref" reference="app:tent"}.

One potential application of the observed growth rates of the index is to shed some light on the convergence of sums [\[indsum\]](#indsum){reference-type="eqref" reference="indsum"} that define $\mathcal{I}_M$. Specifically, suppose that we start with a triangulation of $M$ and first construct a product index $\mathcal{I}_{\{\Delta_i\},\{\Pi_i\}}=\mathcal{I}_{\Delta_1}\times\cdots\times \mathcal{I}_{\Delta_N}$. We then transform this to a polarization $\widetilde\Pi$, in which all internal edges of $M$ are electric. If we chose a refined, "easy" triangulation --- so that it properly defines a theory $T_M$ --- there must be a chiral operator $\mathcal{O}_I$ associated to every internal edge, and charged under the edge coordinate's $U(1)$ symmetry. Moreover, before doing the final index sum [\[indsum\]](#indsum){reference-type="eqref" reference="indsum"}, we shift R-charge so that every $\mathcal{O}_I$ has $R_{\mathcal{O}_I}=2$. In this affine $Sp(2N,{\mathbb Z})$ frame, we know that the leading exponent function $\mathrm{lead}_{\{\Delta_i\},\tilde\Pi}(m,e)$ of the product index $\mathcal{I}_{\{\Delta_i\},\tilde\Pi}(m,e)$ should grow linearly in any electric direction $e_I$ corresponding to the charge of $\mathcal{O}_I$, with slope $R_{\mathcal{O}_I}/2$. In the negative direction $-e_I$, we generically expect quadratic growth instead. To compute the final index $\mathcal{I}_M$, we set magnetic charges $m_I \to 0$ (just like in the analysis above), and sum along both positive and negative $e_I$ directions. We would then expect the sum not only to converge, but to do so "uniformly": in order to compute $\mathcal{I}_M(m,e)$ at fixed external charges $(m,e)$ to $n^{\rm th}$ order in $q$, we should need to sum only from about $-ne_I$ to $ne_I$ in each direction. This has certainly been observed in examples.\
To close this discussion, let us also return to the other, 't Hooft-like, asymptotic limit of the index. Rather than taking $(m,e)\to\infty$ along a ray, with $|q|<1$, we send both $m\to\infty$ and $q\to 1$ ($\hbar\to 0$) with $q^m$ held fixed. Working in an electric fugacity basis, we can use $\zeta$ to complexify the naturally real number $q^m$, and set

$$x = q^m\zeta$$

as in [\[tetasymp\]](#tetasymp){reference-type="eqref" reference="tetasymp"}. Then, just as we found in Section [\[sec:T1\]](#sec:T1){reference-type="ref" reference="sec:T1"} that the tetrahedron index is dominated approximately by the hyperbolic volume of a tetrahedron,

$$\mathcal{I}_\Delta(m;q,\zeta)\;\sim\; \exp\left(\frac{2}{i\hbar}V_\Delta(z)+\ldots\right)\,,\qquad V_\Delta(z) = -{\rm Im}\,{\rm Li}_2(z^{-1})\,,$$

we now find that the index $\mathcal{I}_M$ is dominated approximately by the hyperbolic volume

[^5]

of $M$,

$$\mathcal{I}_M(m;q,\zeta)\;\sim\;\exp\left(\frac{2}{i\hbar}V_M(x)+\ldots\right)\,. \label{volM}$$

Note that this volume depends on boundary conditions $x$. For example, the volume depends on the external dihedral angles of a geodesic boundary, or on the metric (or $SL(2,{\mathbb C})$) holonomy around a cusp boundary of $M$. It differs very slightly from the actual hyperbolic volume, but the difference is easy to correct: the actual volume is

$${\rm Vol}_M(x) = V_M(x) + ({\rm Im}\,P)\cdot({\rm Re}\,X)\,,$$

where $(x,p)=(e^X,e^P)$ is a point on the Lagrangian $\mathcal{L}_M$ (a solution to the defining equations for $\mathcal{L}_M$ at fixed $x$). Note that while $V_M(x)$ and ${\rm Im}\, P$ have branch cuts, ${\rm Vol}_M(x)$ should be well defined.

One way to check [\[volM\]](#volM){reference-type="eqref" reference="volM"}, up to a constant, is to note that the leading asymptotics of the index must be governed by the classical $\hbar\to 0$ ($q\to 1$) limit of the difference operators $\hat \mathcal{L}_M$. In particular, the point $(X,\,P = \frac{\partial V_M}{\partial X})$ must lie on the classical $\mathcal{L}_M$. This property is known to characterize volumes of 3-manifolds [@NZ]. Physically, the asymptotics [\[volM\]](#volM){reference-type="eqref" reference="volM"} are extremely familiar from the study of ellipsoid partition functions $\mathcal{Z}_b[T_M]$ and twisted ${\mathbb R}^2\times S^1$ partition functions of $T_M$, both of which are very closely related to the index. We will discuss the relations further in Section [\[sec:6d\]](#sec:6d){reference-type="ref" reference="sec:6d"}.

[^1]: The leading behavior is all we will look at here. It would be very interesting to also consider subleading corrections and their physical implications.

[^2]: It is easy to see that these are classical $q\to 1$ limits of the corresponding operators in Section [\[sec:glueops\]](#sec:glueops){reference-type="ref" reference="sec:glueops"}, with $x=M$ and $p=-\ell$ in the case of knot complements. For the figure-eight knot, one must throw out an extra factor of $(x^2-1)$ that only arises in [\[A41M\]](#A41M){reference-type="eqref" reference="A41M"} as a quantum correction. Evidently, this factor is not relevant for analyzing vacua or flat directions in the index.

[^3]: In 2d, quantum corrections are responsible for smoothing the asymptotic regions of the parameter $\mathcal{L}_M$ into a connected algebraic variety. Otherwise, $\mathcal{L}_M$ would be a collection of "cigars" centered around each tentacle.

[^4]: The tentacles and flat directions of knot complements always occur back-to-back, due to the ${\mathbb Z}_2$ Weyl symmetry [\[indZ2\]](#indZ2){reference-type="eqref" reference="indZ2"}. This is nicely illustrated in Figures [1](#fig:amoebas){reference-type="ref" reference="fig:amoebas"} and [\[fig:lead41\]](#fig:lead41){reference-type="ref" reference="fig:lead41"}.

[^5]: If $M$ does not admit a deformed hyperbolic structure with specified boundary conditions, the formula still holds, but "volume" means volume of a flat $SL(2,{\mathbb C})$ connection.

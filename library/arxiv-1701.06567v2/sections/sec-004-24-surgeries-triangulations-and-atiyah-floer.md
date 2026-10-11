---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-004-24-surgeries-triangulations-and-atiyah-floer
section_title: "Surgeries, triangulations, and Atiyah-Floer"
section_number: 2.4
pages: 16-27
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.985
---
In order to give a mathematical formulation of the homological invariants that can be useful for practical calculations on an arbitrary 3-manifold, the starting point must be a construction of the 3-manifold itself.

Then, different ways to present the same 3-manifold may lead to different but equivalent definitions of ${\mathcal H}_a[M_3]$ which, in physics, correspond to different ways of looking at the fivebrane system [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"}.

For example, in addition to its original combinatorial definition [@khovanov1999categorification], the Khovanov homology of knots by now has definitions based on matrix factorizations [@khovanov2008matrix], algebraic geometry [@MR2411561], symplectic geometry [@MR2254624; @MR2313538; @AbouzaidSmith], *etc.* As expected, they are all equivalent [@Cautis; @MackaayWebster] and offer different useful perspectives. Similarly, we expect that our homological invariants ${\mathcal H}_a[M_3]$ of 3-manifolds admit several mathematical definitions, thus providing new opportunities and bridges among different areas of mathematics.

A standard way to produce a symplectic definition is based on the Atiyah-Floer conjectures, which relate gauge theory version of Floer homology and its symplectic version (see *e.g.* [@Gukov:2007ck] for a review and an application in a closely related context). The idea is to represent a 3-manifold $M_3$ as a Heegaard decomposition $$M_3 \; = \; M_3^{-} \cup_{\Sigma} M_3^+$$ of two handlebodies $M_3^{\pm}$ joined by a long "neck" $\cong {\mathbb R}\times \Sigma$. Then, topological reduction on $\Sigma$ gives a 2d sigma-model with target space ${\mathcal M}(G, \Sigma)$ and space-time ("world-sheet") ${\mathbb R}\times I$, with the boundary conditions ${\mathcal B}^{\pm}$ at the end-points of the interval $I$ determined by $M_3^{\pm}$. Then, the Floer homology of the higher-dimensional theory can be equivalently formulated as a symplectic Floer homology in the topological A-model with target space ${\mathcal M}(G, \Sigma)$ and two Lagrangian submanifolds ${\mathcal B}^+$ and ${\mathcal B}^-$: $${\mathcal H}_a[M_3] \; = \; HF^*_{\text{symp}} ({\mathcal B}^+, {\mathcal B}^-).$$ As with other candidates for the mathematical definition of ${\mathcal H}_a[M_3]$, the main challenge is to describe precisely the moduli spaces ${\mathcal M}(G, \Sigma)$ and ${\mathcal B}^{\pm}$. For example, to obtain ${\mathcal M}(G, \Sigma)$ it is convenient to first reduce 6d $(0,2)$ theory on $\Sigma$ times the circle fiber of $D^2$ to obtain a sigma-model with target space ${\mathcal M}_{\text{flat}} (G_{{\mathbb C}}, \Sigma) \cong {\mathcal M}_H (G,\Sigma)$, the Hitchin moduli space (in which $M_3^+$ and $M_3^-$ cut out holomorphic Lagrangian submanifolds).

Another way to build 3-manifolds is to start with a simpler 3-manifold, say 3-sphere, remove a tubular neighborhood of some knot (or link) and then glue it back in a different way. This operation is called surgery and, in fact, every 3-manifold can be realized as a sequence of surgery operations on a 3-sphere $S^3$. In view of this, it is natural to ask if 3-manifold homology ${\mathcal H}_a[M_3]$ of the resulting manifold $M_3$ is related to homology of knots and links.

As is well known in the theory of quantum group invariants, at the decategorified level the answer is "yes" and here we argue that this is also true at the homological level. Indeed, a quantum group invariant (WRT invariant) of a 3-manifold $M_3$ obtained by surgery on $K$ is completely determined by polynomial invariants of $K$, with a proviso that one needs to know all colored invariants of $K$. In the case of $G=SU(2)$ these are colored Jones polynomials and to obtain the WRT invariant of $M_3$ one basically need to sum over color (which is typical for any state sum type models).

Since at present all colored polynomial invariants of $K$ have rigorous mathematical definition one could try to write a surgery formula where colored Jones polynomials of $K$ are replaced by the corresponding homologies (or their Poincaré polynomials). Surprisingly, in a few examples that we checked this indeed gives the 3-manifold homology ${\mathcal H}_a[M_3]$, and it is natural to conjecture that this is true in general. If so, one extremely concrete, mathematically well-defined and computable definition of ${\mathcal H}_a[M_3]$ could be via surgery formula and sum over colored knot (link) homologies.

As a concrete example, consider a Lens space $M_3 = L(p,1)$ constructed as a surgery on the unknot. In fact, this also gives an example of genus-$1$ Heegaard splitting since the unknot complement is a solid torus. Let $P_n (q,t)$ be the Poincaré polynomial of $n$-colored $sl(2)$ homology categorifying the $n$-colored Jones polynomial $J_n (q)$. As usual, it is convenient to package all $P_n (q,t)$ in a single function $F(x;q,t)$ such that $$P_n (q,t) \; = \; F(x;q,t) \vert_{x = q^n}.$$ Put differently, if $\widehat A (\widehat x, \widehat y; q,t)$ is the operator that generates recursion relation among $P_n (q,t)$, such that $\widehat x P_n (q,t) = q^n P_n (q,t)$ and $\widehat y P_n (q,t) = P_{n+1} (q,t)$, then [@Fuji:2012pm; @Gukov:2015gmm]: $$\widehat A \, F (x;q,t) \; = \; 0.$$

In terms of the function $F(x;q,t)$ that packages Poincaré polynomials of colored unknot homology, the Poincaré polynomial of ${\mathcal H}_a[M_3]$, where $M_3 = L(p,1)$, is given by the "Laplace transform" [@Gukov:2016njj; @BBLlaplace; @MR2457479] of $F(x;q,t)$, $$P({\mathcal H}_a[M_3];q,t) \; = \; \oint \frac{dx}{2\pi i x} \, F(x;q,t) \, \theta_p^{(a)} (x;q)$$ *i.e.* by a convolution with the theta-function $\theta_p^{(a)} (x;q)$. Note, all the information about homological grading (that is, $t$-dependence) comes entirely from $F(x;q,t)$, *i.e.* from the colored unknot homology, and not from the Laplace transform that produces 3-manifold invariant out of the knot invariant. In other words, categorification of the surgery formula affects only the Jones polynomial part (by replacing it with the Poincaré polynomial).

Another way to build 3-manifolds and, therefore, another candidate for constructing ${\mathcal H}_a[M_3]$ is based on triangulations. This approach is especially attractive due to its combinatorial nature and has been extensively used as a platform for mathematical definitions of various supersymmetric partition functions of 3d ${\mathcal N}=2$ theory $T[M_3]$, see *e.g.* [@Andersen:2011bt; @Andersen:2013rxa; @Andersen:2015tma; @Garoufalidis:2013rca; @MR3522084; @Garoufalidis:2013axa; @Garoufalidis:2016ckn]. Reducible flat connections, again, are special, for the same reason as before. However, in partition functions, the non-trivial stabilizer of reducible flat connections works against them and formally makes their contribution vanish in a Chern-Simons theory with non-compact gauge group. This has to be contrasted with homological invariants, where redicible solutions produce infinite contributions (*e.g.* ${\mathcal T}_+$ in Heegaard Floer homology) compared to finite contributions of irreducible solutions. This suggests that in partition functions too, both reducible and irreducible contributions can be seen together if we consider framed gauge transformations[^1] and then instead of further dividing by $G$ work equivariantly. To the best of our knowledge, this has not been done and presents a nice and tractable problem for future work.[^2]

## Superconformal index of ${T[M_3]}$ and its factorization

Although the new invariants $\widehat{Z}_a(q)$ and their categorification ${\mathcal H}_a[M_3]$ have a direct connection to the WRT invariant via ([\[WRT-decomposition\]](#WRT-decomposition){reference-type="ref" reference="WRT-decomposition"}), from the viewpoint of 3d ${\mathcal N}=2$ theory $T[M_3;SU(2)]$, it is not the most natural or simplest object to consider. The main reason is that, in principle, there are infinitely many possible boundary conditions that could be considered.[^3] Identifying the correct subset that appears in ([\[BlockD2S1\]](#BlockD2S1){reference-type="ref" reference="BlockD2S1"}) may be subtle, yet possible, as we shall see in concrete examples.

The more natural object is the superconformal index of $T[M_3]$ or, equivalently, the partition function on $S^2\times S^1$ with a certain supersymmetry preserving background: $${\mathcal I}(q) \; \equiv \; {\rm Tr}_{{\mathcal H}_{S^2}}(-1)^Fq^{R/2+J_3} \; = \; Z_{T[M_3]}(S^2\times_q S^1)$$ where ${\mathcal H}_{S^2}$ is the space of BPS states of 3d ${\mathcal N}=2$ SCFT $T[M_3]$ or, equivalently, $Q$-cohomology of all physical local operators, $F$ is the fermion number, $R$ is the generator of the $U(1)_R$ R-symmetry and $J_3$ is the Cartan generator of the $SO(3)$ isometry of $S^2$. By construction, this index has the desired integrality property[^4] and can be categorified, $${\mathcal H}_{S^2}=\bigoplus_{i,j}{\mathcal H}^{i,j}_{S^2} \,,\qquad {\mathcal I}(q)=\sum_{i,j\in{\mathbb Z}}q^{i}(-1)^j\dim{\mathcal H}_{S^2}^{i,j}\;\in {\mathbb Z}[[q]] \,.
    \label{IndexEuler}$$ Another advantage of ${\mathcal H}_{S^2}$ compared to ${\mathcal H}_{D^2}$ is that it has a natural ring structure which is given by multiplication of BPS operators. One of the statements of 3d/3d correspondence is that the partition function $Z_{T[M_3]}(S^2\times_q S^1)$ computes the partition function of complex Chern-Simons on $M_3$ with real part of the "level" being $0$ and analytically continued imaginary part $\propto \tau\equiv \log q/(2\pi i)$. Motivated by the topological/anti-topological fusion [@Cecotti:1991me] and its recent 3d incarnation [@Pasquetti:2011fj; @Beem:2012mb; @Cecotti:2013mba; @Blau:2016vfc], we would like to make the following conjecture:

::: conj
For $\widehat{Z}_a(q)$ as in Conjecture [\[Conjecture1\]](#Conjecture1){reference-type="ref" reference="Conjecture1"}, the following holds $${\mathcal I}(q)=\sum_{a\,\in\, {\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})/{\mathbb Z}_2}\, |{\mathcal W}_a|\widehat{Z}_a(q)\widehat{Z}_a(q^{-1})
        \qquad \in{\mathbb Z}[[q]]
        \label{IndexFactorization}$$ where $\widehat{Z}_a(1/q)$ is an apropriate extension[^5] of $\widehat{Z}_a(q)$ to the region $|q|>1$. []{#Conjecture2 label="Conjecture2"}
:::

## Further refinement

As we discussed above, for Seifert 3-manifolds the theory $T[M_3]$ has an extra $U(1)_{\beta}$ flavor symmetry. In particular, this is the case for $M_3=L(p,1)$, which will serve as an important example to us later. This flavor symmetry in $T[M_3]$ results in the presence of an extra ${\mathbb Z}$-grading in homological invariants ${\mathcal H}_{D^2}$ and ${\mathcal H}_{S^2}$ considered in the previous sections and a possibility to consider the corresponding refined indices (equivariant Euler characteristics): $$\widehat{Z}_a(q;t)=\sum_{i\in {\mathbb Z}+\Delta_a,\atop j,\ell \in{\mathbb Z}}q^{i}t^{\ell}(-1)^j\dim{\mathcal H}^{i,j;\,\ell}_a,
    \label{BlockEuler}$$ and $${\mathcal I}(q;t)=\sum_{i,j,\ell\in{\mathbb Z}}q^{i}t^{\ell}(-1)^j\dim{\mathcal H}_{S^2}^{i,j;\,\ell}.$$ where, from the physics point of view, $\ell$ is the $U(1)_{\beta}$ charge. The refined indices obviously provide more information about the underlying vector spaces and, as we will see in examples, can be used sometimes to compute (conjecturally) the full homological invariants via the "homological-flavor locking" phenomenon that we will explain later.

The refined version of the factorization formula [\[IndexFactorization\]](#IndexFactorization){reference-type="eqref" reference="IndexFactorization"} reads $${\mathcal I}(q;t)=\sum_{a\,\in\, {\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})/{\mathbb Z}_2}\, |{\mathcal W}_a|\widehat{Z}_a(q;t)\widehat{Z}_a(q^{-1};t^{-1}).
        \label{IndexRefDecomp}$$

## Topologically twisted index of ${T[M_3]}$

Another interesting invariant of $M_3$ which can be realized as an observable of $T[M_3]$ and has a categorification by construction is the topologically twisted index on $S^2\times S^1$ [@Benini:2015noa]. Namely, one can consider the 3d ${\mathcal N}=2$ theory $T[M_3]$ with a background value of the $U(1)_R$-symmetry connection equal to the spin connection on $S^2$. In terms of the effective 2d ${\mathcal N}=(2,2)$ theory obtained by compactifying $T[M_3]$ on $S^1$, this is the familiar A-twist along the $S^2$.

The topologically twisted index and the underlying homological invariant of $M_3$ have the same fugacities/gradings as the superconformal index: $${\mathcal I}_{\text{top}}(q;t) \; = \; \sum_{i,j,\ell \in{\mathbb Z}}q^{i}t^{\ell}(-1)^j\dim{\mathcal H}_{S^2_{\text{top}}}^{i,j;\,\ell}.$$ As in the superconformal index ${\mathcal I}(q;t)$, here the parameter $q$ plays the role of the Omega-background parameter corresponding to rotating $S^2$ along one of the axes. However, in general the topologically twisted index ${\mathcal I}_{\text{top}}(q;t)$ has a much simpler structure (as will be explained later) compared to the superconformal index ${\mathcal I}(q)$. Namely, ${\mathcal I}_{\text{top}}(q;t)$ is a rational function of $q,t$ (*i.e.* it has a form of the index of quantum mechanics with two supercharges), whereas ${\mathcal I}(q,t)$ can be as transcendental as, say, a quantum dilogarithm or (Jacobi) mock modular form. Nevertheless, the topologically twisted index is expected to have a similar factorization into homological blocks: $${\mathcal I}_{\text{top}}(q,t)=\sum_{a\,\in\, {\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})/{\mathbb Z}_2}\, |{\mathcal W}_a|\widehat{Z}_a(q;t)\widehat{Z}_a(q^{-1};t).
\label{Itop-decomp}$$ The difference from ([\[IndexRefDecomp\]](#IndexRefDecomp){reference-type="ref" reference="IndexRefDecomp"}) is due to the fact that the supersymmetric backround chosen for superconformal $S^2\times S^1$ index can be interpreted as doing topological A-twist along one of the $D^2\times S^1$ halves and anti-A-twist along the other $D^2\times S^1$ half, $${\mathcal I}(q;t)
\; =
{\,\raisebox{-.5cm}{\includegraphics[width=6.0cm]{twist2}}\,}$$ whereas the background for the topologically twisted $S^2\times S^1$ index is such that the same A-twist is performed along both halves: $${\mathcal I}_{\text{top}}(q;t)
\; =
{\,\raisebox{-.5cm}{\includegraphics[width=6.0cm]{twist1}}\,}.$$

## Generalization to ${U(N)}$ {#sec:higherrk}

For simplicity, in this paper we mostly consider Chern-Simons theory on $M_3$ with gauge group being $G=SU(2)$ and the 3d/3d dual theory $T[M_3;SU(2)]$. However, in principle, everything we say above and below for $SU(2)$ can be easily generalized to the $SU(N)$ or $U(N)$ case; there are no obstructions for that. In particular, the formulae appearing in Conjecture [\[Conjecture1\]](#Conjecture1){reference-type="ref" reference="Conjecture1"} generalize as follows for $G = U(N)$: $$Z_{U(N)_k}[M_3]=(i\sqrt{2k})^{N(b_1(M_3)-1)/2}\sum_{a\;\in \;({\mathrm{Tor}\,}H_1(M_3,{\mathbb Z}))^{N}/S_N}e^{\pi ik\,\sum_{i=1}^N{\ell k}(a_i,a_i)}\,Z_a(q),
\label{WRT-UN-decomp}$$ $$Z_a(q)=\sum_{b\;\in \;({\mathrm{Tor}\,}H_1(M_3,{\mathbb Z}))^{N}/S_N}e^{\pi ik\,\sum_{i=1}^N{\ell k}(a_i,a_i)}\,S_{ab}
    \, \left.\widehat{Z}_b(q)\right|_{q\rightarrow e^{\frac{2\pi i }{k}}},$$ $$S_{ab}=\frac{\sum_{\sigma\in S_N}e^{2\pi i \sum_{i=1}^N{\ell k}(a_i,b_{\sigma(i)})}}{|\mathrm{Stab}_{S_N}(a)|\cdot|{\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})|^{N/2}},$$ $$\widehat{Z}_a(q)\in (N!)^{-c}\,q^{\Delta_a}{\mathbb Z}[[q]].$$ As before, using the linking pairing one can identify $({\mathrm{Tor}\,}H_1(M_3))^N/S_N$ with the set of connected components of abelian flat connections: $$\begin{gathered}
    ({\mathrm{Tor}\,}H_1(M_3))^N/S_N\stackrel{{\ell k}}{\cong}\, \mathrm{Hom}\left({\mathrm{Tor}\,}H_1(M_3),U(1)^N\right)/S_N
 \cong \pi_0{\mathcal M}_\text{flat}^\text{ab}(M_3,U(N))
\label{UN-ab-set}
\end{gathered}$$ where $S_N$ is the permutation group of a set with $N$ elements. The factorization formulae ([\[IndexRefDecomp\]](#IndexRefDecomp){reference-type="ref" reference="IndexRefDecomp"}) and ([\[Itop-decomp\]](#Itop-decomp){reference-type="ref" reference="Itop-decomp"}) generalize as follows $${\mathcal I}(q,t)\quad = \sum_{a\,\in\, ({\mathrm{Tor}\,}H_1(M_3,{\mathbb Z}))^N/S_N}\, |{\mathcal W}_a|\widehat{Z}_a(q,t)\widehat{Z}_a(q^{-1},t^{-1}),
\label{I-UN-decomp}$$ $${\mathcal I}_{\text{top}}(q,t) \quad =\sum_{a\,\in\, ({\mathrm{Tor}\,}H_1(M_3,{\mathbb Z}))^N/S_N}\, |{\mathcal W}_a|\widehat{Z}_a(q,t)\widehat{Z}_a(q^{-1},t),
\label{Itop-UN-decomp}$$ with $${\mathcal W}_a\equiv \text{Stab}_{S_N}(a).$$

Physically, there are several ways to understand the special role of abelian flat connections or, more generally, reducible flat connections for $G$ of higher rank. As we already mentioned in section [\[sec:summaryConj\]](#sec:summaryConj){reference-type="ref" reference="sec:summaryConj"}, from the viewpoint of quantum field theory (on fivebrane world-volume or its various reductions and limits) this follows directly from the resurgent analysis. On the other hand, by looking at the same system [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"} from the vantage point of the Calabi-Yau 3-fold, the set [\[UN-ab-set\]](#UN-ab-set){reference-type="eqref" reference="UN-ab-set"} which labels the new invariants $\widehat{Z}_a(q)$ and their categorification ${\mathcal H}_a[M_3]$ can be understood as charges of the BPS states or enumerative invariants of the Calabi-Yau 3-fold. We elaborate on this perspective in the following two subsections, expanding the web of dualities and interpretations.

## Relation to open GW invariants on ${T^*M_3}$

Consider $U(N)$ level-$k$ Chern-Simon theory on a rational homology sphere $M_3$, $$b_1(M_3) \; = \; 0 \,,$$ *i.e.* $H_1(M_3,{\mathbb Z})={\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})$ is a finite abelian group. (What follows can be considered as a generalization from the case $H_1(M_3,{\mathbb Z})\cong {\mathbb Z}$ considered in [@Labastida:2000yw]).

Similar to the $SU(2)$ case, $\sum_{i=1}^N{\ell k}(a_i,a_i)=\mathrm{CS}(a)$ is the Chern-Simons invariant of the abelian flat connection $a$, and $Z_a(q)$ is a Borel resummation [@Gukov:2016njj] of the asymptotic expansion around $a$. Correspondingly, $\widehat{Z}_b(q)$ is a Borel resummation of the series of the following type: $$\widehat{Z}_b(q)=\sum_{m\geq 0}n^b_m\,q^{\Delta_b+m}\;\;\stackrel{\text{resum}}{=\joinrel=\joinrel=}\;\; \widehat{Z}^\text{pert}_b(k)
=\sum_{m\geq 1} N^b_m\left(\frac{2\pi i}{k}\right)^m
    \qquad \in{\mathbb Q}[[2\pi i/k]].
    \label{resum}$$ Consider $$e^{2\pi i\,a}\;\;\in \;\;\mathrm{Hom}\left(H_1(M_3),U(1)^N\right)/S_N$$ as a formal variable in a generating series. Then $S_{ab}$, for each $b$, up to a factor, can be viewed as a basis element of the symmetric part of the group ring[^6] of $(H_1(M_3,{\mathbb Z}))^N$: $$|H_1(M_3)|^{N/2}|\text{Stab}_{S_N}(b)|^{-1}\,S_{ab}\in
    {\mathbb Z}\left[\left(H_1(M_3,{\mathbb Z})\right)^N\right]^{S_N},\qquad b\in (H_1(M_3))^N/S_N,
    \label{group-ring-basis}$$ if we identify $$\prod_{i=1}^Ne^{2\pi i{\ell k}(a_i,c_i)}\equiv 1\cdot c
    \label{ring-id}$$ in the group ring of $(H_1(M_3))^N$.

Then $$\left(2k|H_1(M_3)|\right)^{N/2}\left|\text{Stab}_{S_N}(a)\right|\,Z_a(q)\;\;\in\;\;
    {\mathbb Z}[[q^{1/|H_1|}]]\;\otimes_{\mathbb Z}\;
    {\mathbb Z}\left[\left(H_1(M_3,{\mathbb Z})\right)^N\right]^{S_N}
    \label{Zq}$$ while $$\sum_{b\in (H_1(M_3))^N/S_N}S_{ab}\widehat{Z}^\text{pert}_b(k)\;\;
    \in\;\;
        {\mathbb Q}[[2\pi i/k]]\;\otimes_{\mathbb Z}\;
        {\mathbb Z}\left[\left(H_1(M_3,{\mathbb Z})\right)^N\right]^{S_N}.
        \label{Zk}$$

On the other hand, one can consider open topological strings (A-model) on $T^*M_3$ with a Lagrangian brane along $M_3$ equipped with a rank-$N$ bundle and an abelian flat connection (local system) $a$. The free energy is given by $$F^\text{top}_a[T^*M_3](g_s)=
    \sum_{g,\, h}g_s^{2g+h-2}\sum_{c\in (H_1(M_3,{\mathbb Z}))^h}
    N_{g;c_1,\ldots,c_h}
    \prod_{j=1}^h\,e^{2\pi i\sum_{i=1}^N {\ell k}(a_i,c_j)}
    \label{Ftop}$$ where the open GW invariants $$N_{g;c_1,\ldots,c_h}\;\;\in \;\; {\mathbb Q}$$ count pseudoholomorphic maps from a genus-$g$ Riemann surface with $h$ holes to $T^*M_3$ such that the image of the $j$-th boundary component lands in a homology class $c_j\in H_1(M_3,{\mathbb Z})$. The factor $$e^{2\pi i\sum_{i=1}^N {\ell k}(a_i,c_j)}\;=\;\text{Hol}_a(c_j)$$ is the holonomy of the abelian flat connection $a$ along $c_j$. Note that $$N_{g;c_1,\ldots,c_h}=0\qquad \text{unless}\qquad c_1+\ldots+c_h= 0\;\;\in H_1(M_3,{\mathbb Z})$$ because there are no non-trivial 2-cycles in $T^*M_3$. When the flat connection $a$ is trivial, the generating function ([\[Ftop\]](#Ftop){reference-type="ref" reference="Ftop"}) takes a familiar form $$F^\text{top}_0[T^*M_3](g_s)=
    \sum_{g,\, h}g_s^{2g+h-2}\,
    N_{g;h}\,N^{h}$$ where the averaged version of open GW invariants $$N_{g;h}=\sum_{c\in (H_1(M_3,{\mathbb Z}))^h}\,N_{g;c_1,\ldots,c_h}$$ "forgets" where the boundary components map to.

Again, using the identification ([\[ring-id\]](#ring-id){reference-type="ref" reference="ring-id"}), the generating function ([\[Ftop\]](#Ftop){reference-type="ref" reference="Ftop"}) can be regarded as $$F^\text{top}_a[T^*M_3](g_s)\;\; \in \;\;
    {\mathbb Q}[[g_s]] \otimes_{\mathbb Z}
    {\mathbb Z}\left[\left(H_1(M_3,{\mathbb Z})\right)^N\right]^{S_N}.
    \label{Fk}$$ Then, the relation between CS and open topological strings can be formulated as follows:[^7] $$\left.\exp\,F^\text{top}_a[T^*M_3](g_s)\right|_{g_s=\frac{2\pi i}{k}}\;\; \propto \;\;
    \sum_{b}S_{ab}\widehat{Z}_b^\text{pert}(k)
    \label{top-CS}$$ where the exponent is taken using multiplication rules in the ring in ([\[Fk\]](#Fk){reference-type="ref" reference="Fk"}), the same as the ring[^8] in ([\[Zk\]](#Zk){reference-type="ref" reference="Zk"}). The integer numbers $n^b_m$ in ([\[resum\]](#resum){reference-type="ref" reference="resum"}) are the "massless variants" of open DT/Ooguri-Vafa invariants of $T^*M_3$.

## Langlands duality and flat connections {#sec:Langlands}

Motivated by the results of this paper, combined with [@Gukov:2016njj], we can make another conjecture:

::: conj
Let $G$ be a compact Lie group (not necessarily of ADE type) and $^LG$ its Langlands dual. Then, under S-duality, the boundary condition ${\mathcal B}_a$ corresponding to a connected component in ${\mathcal M}_{\text{flat}}^{\text{ab}} (M_3, G_{{\mathbb C}})$ of $G_{{\mathbb C}}$ flat connections on a 3-manifold $M_3$ maps to $${\mathcal B}_a \quad \mapsto \quad
{}^L{\mathcal B}_a \; = \; \sum_{{b \atop \text{abelian}}} S^{ab} \; (\, {\mathcal B}_b + \sum_{{c \atop \text{non-abelian}}} n_{bc} \; {\mathcal B}_c \, )
\label{Langlands}$$ where $S_{ab}$ is the S-matrix as in Conjecture [\[Conjecture1\]](#Conjecture1){reference-type="ref" reference="Conjecture1"} and $n_{bc}$ are the transseries coefficients from [@Gukov:2016njj]. []{#conjLanglands label="conjLanglands"}
:::

In formulating this Conjecture, we used ${\mathcal B}_a$ (instead of $a$) to emphasize its role as a boundary condition on $\partial (D^2\times_q S^1) = T^2$. The mapping class group $SL(2,{\mathbb Z})$ of the 2-torus acts on the boundary conditions and we claim that, at least for boundary conditions associated with abelian flat connections, the S-transformation is given by [\[Langlands\]](#Langlands){reference-type="eqref" reference="Langlands"}. Indeed, at the "far end" of the cigar, the geometry of the fivebrane world-volume looks like ${\mathbb R}\times M_3 \times T^2$, and we can first reduce on $T^2$ to obtain 4d ${\mathcal N}=4$ super-Yang-Mills on ${\mathbb R}\times M_3$. The mapping class group of $T^2$ then becomes the S-duality group of 4d ${\mathcal N}=4$ SYM, in particular, exchanging $G$ and $^LG$ under the electric-magnetic duality.

When $G$ is of Cartan type A or D, the left-hand side of [\[Langlands\]](#Langlands){reference-type="eqref" reference="Langlands"} is the choice of boundary condition we used in [\[aHW\]](#aHW){reference-type="eqref" reference="aHW"}, whereas the right-hand side describes the boundary condition that gives ${\mathcal H}_a [M_3]$ and is used in most of the paper. Then, Conjecture [\[conjLanglands\]](#conjLanglands){reference-type="ref" reference="conjLanglands"} is basically a statement that both sets of boundary conditions lead to integrality and are compatible.

## 3-manifolds and the "bottom row"

Using a relation between the physical realizations of 3-manifold homology and a HOMFLY-PT homology, respectively, we can produce a purely *mathematical* relation between the familiar knot homologies and less familiar 3-manifold homologies of this paper.

Namely, the familiar setup for homology of a knot $K\subset S^3$ involves $Q$-cohomology (space of BPS states) of the following system: $$\begin{array}{rcl}
\multicolumn{3}{c}{~~\text{doubly-graded}~} \\[.1cm]
\hline
{\mbox{\rm space-time:}} && ~~  {\mathbb R}\times T^* S^3 \times TN \\
{\mbox{\rm $N$ M5-branes:}} && ~~  {\mathbb R}\times ~S^3~ \times ~D^2 \\
{\mbox{\rm M5$'$-branes:}} && ~~  {\mathbb R}\times ~L_K~ \times  ~D^2
\end{array}
\quad \xleftarrow[~\text{transition}]{~\text{phase}} \!\!\! \to \quad

\begin{array}{rcl}
\multicolumn{3}{c}{~~~\text{triply-graded}~~} \\[.1cm]
\hline
&& {\mathbb R}\times X \times  ~TN \\
{\mbox{\rm M5$'$:}} && {\mathbb R}\times L_K \times  D^2
\end{array}
\label{conifoldphases}$$ where $L_K$ is the conormal bundle of the knot $K$, and $X$ is the resolved conifold, *i.e.* the total space of ${\mathcal O}(-1) \oplus {\mathcal O}(-1)$ bundle over ${\mathbb{C}}{\mathbf{P}}^1$.

Note, on the triply-graded ("resolved") side the original M5-branes disappear and we are only left with a system of M5$'$-branes in a non-trivial Calabi-Yau background $X$. This is very similar to a physical realization of 3-manifold homology in [\[CatGeom0\]](#CatGeom0){reference-type="eqref" reference="CatGeom0"} or [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"} where, compared to the right-hand side of [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"}, the Lagrangian 3-manifold $M_3$ plays the role of $L_K$. Indeed, according to the McLean's theorem, the neighborhood of the Lagrangian submanifold $L_K \subset X$ in [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"} can be identified with the total space of the cotangent bundle, $$N (L_K) \; \cong \; T^* L_K$$ which is precisely the setup of [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"}. There is an important difference, however.

While in [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"} the Calabi-Yau space is simply the cotangent bundle to the Lagrangian 3-manifold $M_3$, in [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"} it only looks like $T^* L_K$ in the neighborhood of $L_K$. Globally, the topology of $X$ is different from $T^* L_K$ and, in particular, has non-trivial relative homology group $$H_2 (X,L_K) \cong {\mathbb Z}.$$ It plays an important role in the physical realization of the colored HOMFLY-PT homology of the knot $K$; namely, the conserved charge captured by this relative homology is the so-called $a$-grading of the HOMFLY-PT homology of $K$.

As in [@Gorsky:2013jxa], we can bridge the gap between the two systems [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"} and [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"} by taking the limit[^9] $$\log (a) = \text{Vol} ({\mathbb{C}}{\mathbf{P}}^1) \to \infty.
\label{alimit}$$ This limit has a simple interpretation in almost every duality frame. For example, from the vantage point of the Calabi-Yau 3-fold $X$ it corresponds to the limit $$X \quad \leadsto \quad {\mathbb C}^3
\label{Xlimit}$$ that, on the toric diagram of the resolved conifold $X$, corresponds to moving two trivalent vertices far away from each other. Keeping only one vertex in sight, we end up with ${\mathbb C}^3$ (whose enumerative invariants are counted by the refined topological vertex). After making this replacement in [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"}, we obtain a simpler fivebrane system, whose BPS spectrum ($Q$-cohomology) categorifies only the bottom (resp. top) row of the HOMFLY-PT polynomial that contains the terms with minimal (resp. maximal) $a$-degree [@Gorsky:2013jxa].

::: {#tab:examples}
    Knot $K$     ${\mathcal H}_{\text{bottom}} (K)$
  ------------- ------------------------------------
   ${\bf 3_1}$           $q^{-2} + q^2 t^2$
   ${\bf 4_1}$                $t^{-2}$
   ${\bf 5_1}$        $q^{-4} + t^2 + q^4 t^4$
   ${\bf 5_2}$         $q^{-2} + t + q^2 t^2$
   ${\bf 6_1}$        $t^{-2} + q^{-2} t^{-1}$

  : The reduced Poincaré polynomial of the bottom row of the HOMFLY-PT homology for simple knots colored by $\lambda = \Box$. The unreduced HOMFLY-PT homology is infinite-dimensional and its Poincaré "polynomial" is, in fact, a power series in $q$ and $t$.
:::

Now, after taking the limit [\[alimit\]](#alimit){reference-type="eqref" reference="alimit"}--[\[Xlimit\]](#Xlimit){reference-type="eqref" reference="Xlimit"}, the second cohomology of $X$ is trivial and there is no winding around ${\mathbb{C}}{\mathbf{P}}^1$ that we had in the original system [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"}. This, of course, corresponds to the fact that, by taking the limit, we lost the $a$-grading focusing only on terms with the lowest $a$-degree. The $q$-degree and $t$-degree, however, are still present and come from $U(1)_q \times U(1)_R$ symmetry acting on $D^2 \subset TN$.

To summarize, by taking the limit [\[alimit\]](#alimit){reference-type="eqref" reference="alimit"}--[\[Xlimit\]](#Xlimit){reference-type="eqref" reference="Xlimit"} in the physical system [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"}, we obtain a relation between the bottom row of the HOMFLY-PT homology of $K$ and the homology of the 3-manifold $M_3 = L_K$: $${\mathcal H}_{\text{bottom}} (K) \; \cong \; {\mathcal H}(M_3).
\label{knotsvsmflds}$$ In fact, the geometry and topology of $M_3 = L_K$ is closely related to that of the knot complement $S^3 \setminus K$, see [@Aganagic:2013jpa]. Namely, for a knot (= a link with one component), both $M_3 = L_K$ and $S^3 \setminus K$ have $H_1 \cong {\mathbb Z}$. In particular, in both cases the abelian flat connections are labeled by ${\mathbb C}^*$-valued holonomies $x_1, \ldots, x_N$.

Note, [\[knotsvsmflds\]](#knotsvsmflds){reference-type="eqref" reference="knotsvsmflds"} is a purely mathematical relation whose left-hand side is knot homology and whose right-hand side is a 3-manifold homology. One can explore it and try to make it more concrete, in particular using the physical setup [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"} and [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"}. First, we need to develop a more precise dictionary between the RHS and LHS of [\[knotsvsmflds\]](#knotsvsmflds){reference-type="eqref" reference="knotsvsmflds"}. Following the above derivation, we see that the M5$'$-branes in [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"} correspond to M5-branes in [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"}. Therefore, the $sl(N)$ homology of $M_3 = L_K$ gets related to the bottom row of $\lambda$-colored HOMFLY-PT homology of $K$, where $\lambda$ is a partition with $N$ rows (or $N$ columns). Moreover, as in [@Ooguri:1999bv; @Labastida:2000yw], we need to relate the "partition basis" (natural on the LHS of [\[knotsvsmflds\]](#knotsvsmflds){reference-type="eqref" reference="knotsvsmflds"}) to the "holonomy basis" (natural on the RHS of [\[knotsvsmflds\]](#knotsvsmflds){reference-type="eqref" reference="knotsvsmflds"}). And, finally, it is important to keep in mind that in relating the physical systems [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"} and [\[conifoldphases\]](#conifoldphases){reference-type="eqref" reference="conifoldphases"} we obtain a relation [\[knotsvsmflds\]](#knotsvsmflds){reference-type="eqref" reference="knotsvsmflds"} that involves unreduced knot homology[^10] in the sense of [@khovanov2008matrix].

As a warm-up, let us take a closer look at the simple case of $N=1$ and $\lambda = \Box$. Recall, that $L_K$ is a special Lagrangian submanifold in ${\mathbb R}^6 \cong {\mathbb C}^3$. The moduli space ${\mathcal M}(L_K)$ of its Lagrangian deformations, together with a local system that it carries, is the space of SUSY vacua of 3d ${\mathcal N}=2$ theory $T[L_K;U(1)]$ on a circle, $${\mathcal M}(L_K) \; \cong \; {\mathcal M}_{\text{SUSY}} (T[L_K;U(1)]) \; \cong \; {\mathcal M}_{\text{flat}} (L_K, U(1)_{{\mathbb C}}),
\label{MLK}$$ where in the last relation we used the McLean theorem. The cohomology of this moduli space is precisely the bottom row of the HOMFLY-PT homology of $K$ colored by $\lambda = \Box$ [@Shende:2014ira]: $${\mathcal H}_{\text{bottom}} (K) \; \cong \; H^* ({\mathcal M}(L_K)).$$ In [@Shende:2015mzx], the moduli space ${\mathcal M}(L_K)$ is described as a cluster variety.

Another simple example is $K = \text{unknot}$ and $\lambda = S^r$ (or $\lambda = \Lambda^r$), a single-row Young tableaux. The corresponding superpolynomial is $${\mathcal P}^{S^r}_{\text{bottom}} (\text{unknot}) \; = \; \prod_{i=1}^r \frac{1}{1-q^{2i} t^{2(i-1)}} \,.
\label{SrHOMFLY}$$ These expressions can be found as $x^r$-coefficients of $Z_{\text{vortex}} (x;q,t)$ for a single 3d ${\mathcal N}=2$ chiral multiplet. More generally, for $K = \text{unknot}$ colored by Young diagrams with $n$ rows (or columns) we end up with the $S^1 \times D^2$ vortex partition function of $n$ 3d ${\mathcal N}=2$ chiral multiplets. This has to be compared with $gl(n)$ homology of $M_3 = S^3 \setminus (\text{unknot})$.

It would be useful to develop the relation [\[knotsvsmflds\]](#knotsvsmflds){reference-type="eqref" reference="knotsvsmflds"} between the familiar HOMFLY-PT homology and the less familiar 3-manifold homology further. We leave this to future work and now turn to detailed analysis of the latter.

[^1]: A framed gauged transformation acts trivially at a chosen point on $M_3$.

[^2]: A closely related $U(1)$-equivariant rather than $G$-equivariant regularization of complex Chern-Simons partition function was used [@equivariant] for 3-manifolds of the form $M_3 = S^1 \times \Sigma$. As expected, this equivariant localization does help to see contributions of both abelian and non-abelian flat connections in the same partition function.

[^3]: If we understand the boundary condition as a coupling of the 3d theory to a 2d theory living on the boundary, then the infinite number of possibilities can be seen, for example, from the fact that we can always introduce a 2d theory decoupled from the bulk.

[^4]: For reasons similar to the ones described at the end of the previous section, in general a negative power of 2 can appear as an overall factor. We omit it in some generic formulas to avoid clutter and instead focus attention on the conceptual structure. As mentioned earlier and as we shall see in examples, the effect of such fractions on categorification can typically be traced to the existence of bosonic modes with zero $q$-grading.

[^5]: For a generic 3-manifold $M_3$, the analytic continuation of the series $\widehat{Z}_a(q)\in {\mathbb Z}[[q]]$ convergent in $|q|<1$ may not exist outside $|q|=1$, at least in the standard way. However, one possible way to define it for general $M_3$ is $$\widehat{Z}_a(q^{-1}) \; \equiv \; \left.\widehat{Z}_a(q)\right|_{M_3\rightarrow \overline{M}_3},$$ where $\overline{M}_3$ denotes $M_3$ with the reversed orientation. Note that therefore ${\mathcal I}(q)$, unlike $\widehat{Z}_a(q)$, is insensetive to the orientation.

[^6]: For example, when $N=2$ and $H_1(M_3,{\mathbb Z})={\mathbb Z}_2$ we have: $${\mathbb Z}\left[\left(H_1(M_3,{\mathbb Z})\right)^N\right]^{S_N}\cong
        {\mathbb Z}[x_1,x_2]^{S_2}/\{x_1^2=1,x_2^2=1\}$$ and $$\begin{array}{rl}
            S_{a,(0,0)} & \propto 1 \\
            S_{a,(1,0)} & \propto x_1+x_2 \\
            S_{a,(1,1)} & \propto x_1x_2 \\
        \end{array}$$ where $x_i=e^{\pi i a}$.

[^7]: Normalizations of $Z_{U(N)_k}$, as well as the first few terms in $F^\text{top}$, are subject to ambiguity, and we won't attempt to fix them here.

[^8]: Note, that any element of this ring has the form as in the right-hand side of ([\[top-CS\]](#top-CS){reference-type="ref" reference="top-CS"}) since ([\[group-ring-basis\]](#group-ring-basis){reference-type="ref" reference="group-ring-basis"}) are basis elements.

[^9]: Note, in relating HOMFLY-PT homology to $sl(N)$ knot homology one sets $a = q^N$, so that $\log (a) \sim N$.

[^10]: The reduced HOMFLY-PT homology categorifies normalized HOMFLY-PT polynomial; it is finite-dimensional for $\lambda = \Box$ and links with one component (*i.e.* for knots). The unreduced version, on the other hand, categorifies unnormalized HOMFLY-PT polynomial and is infinite-dimensional for any color $\lambda$. The former has no obvious analogue for 3-manifolds.

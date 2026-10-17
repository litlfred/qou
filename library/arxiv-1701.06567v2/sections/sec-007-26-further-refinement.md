---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-007-26-further-refinement
section_title: "Further refinement"
section_number: 2.6
pages: 19-24
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.876
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
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
    \label{resum}$$ Consider $$e^{2\pi i\,a}\;\;\in \;\;\mathrm{Hom}\left(H_1(M_3),U(1)^N\right)/S_N$$ as a formal variable in a generating series. Then $S_{ab}$, for each $b$, up to a factor, can be viewed as a basis element of the symmetric part of the group ring[^1] of $(H_1(M_3,{\mathbb Z}))^N$: $$|H_1(M_3)|^{N/2}|\text{Stab}_{S_N}(b)|^{-1}\,S_{ab}\in
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
    \label{Fk}$$ Then, the relation between CS and open topological strings can be formulated as follows:[^2] $$\left.\exp\,F^\text{top}_a[T^*M_3](g_s)\right|_{g_s=\frac{2\pi i}{k}}\;\; \propto \;\;
    \sum_{b}S_{ab}\widehat{Z}_b^\text{pert}(k)
    \label{top-CS}$$ where the exponent is taken using multiplication rules in the ring in ([\[Fk\]](#Fk){reference-type="ref" reference="Fk"}), the same as the ring[^3] in ([\[Zk\]](#Zk){reference-type="ref" reference="Zk"}). The integer numbers $n^b_m$ in ([\[resum\]](#resum){reference-type="ref" reference="resum"}) are the "massless variants" of open DT/Ooguri-Vafa invariants of $T^*M_3$.

[^1]: For example, when $N=2$ and $H_1(M_3,{\mathbb Z})={\mathbb Z}_2$ we have: $${\mathbb Z}\left[\left(H_1(M_3,{\mathbb Z})\right)^N\right]^{S_N}\cong
        {\mathbb Z}[x_1,x_2]^{S_2}/\{x_1^2=1,x_2^2=1\}$$ and $$\begin{array}{rl}
            S_{a,(0,0)} & \propto 1 \\
            S_{a,(1,0)} & \propto x_1+x_2 \\
            S_{a,(1,1)} & \propto x_1x_2 \\
        \end{array}$$ where $x_i=e^{\pi i a}$.

[^2]: Normalizations of $Z_{U(N)_k}$, as well as the first few terms in $F^\text{top}$, are subject to ambiguity, and we won't attempt to fix them here.

[^3]: Note, that any element of this ring has the form as in the right-hand side of ([\[top-CS\]](#top-CS){reference-type="ref" reference="top-CS"}) since ([\[group-ring-basis\]](#group-ring-basis){reference-type="ref" reference="group-ring-basis"}) are basis elements.

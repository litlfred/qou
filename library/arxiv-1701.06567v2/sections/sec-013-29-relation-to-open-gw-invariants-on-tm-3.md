---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-013-29-relation-to-open-gw-invariants-on-tm-3
section_title: "Relation to open GW invariants on $T^*M_3$"
section_number: 2.9
pages: 22-24
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.97
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
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

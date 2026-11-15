---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-023-331-homological-blocks-and-wrt-invariant
section_title: "Homological blocks and WRT invariant"
section_number: 3.3.1
pages: 47-48
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.982
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
Consider the partition function of $T[M_3]$ on $D^2\times S^1$ with the following 2d ${\mathcal N}=(0,2)$ boundary conditions (which generalize the boundary conditions for $T[L(p,1)]$ that produce $\widehat{Z}_a(q,t)$):

-   Neumann for ${\mathcal N}=2$ vector multiplet,

-   Neumann for adjoint chiral $\Sigma$,

-   Dirichlet for $g$ adjoint chirals $\Phi_i$,

-   Neumann for $g$ adjoint chirals $\widetilde\Phi_i$,

-   3d vector multiplet is coupled to modules of ${\mathbb Z}_2$-orbifolded $\sqrt{2p}{\mathbb Z}$ lattice VOA by gauging its flavor symmetry. Note that when $p=0$ the boundary conditions preserve 2d ${\mathcal N}=(2,2)$ supersymmetry. This cancels gauge anomaly inflow due to the level-$p$ CS term.

The $D^2\times_q S^1$ partition then reads [@Yoshida:2014ssa] $$\begin{gathered}
    \widehat{Z}_a(q,t,u)\equiv Z_{T[M_3]}(D^2_a\times_q S^1)= \frac{1}{|{\mathcal W}_a|}\int_\gamma \frac{dz}{2\pi i z}
    \frac{(z^{\pm2};q)_\infty(q;q)_\infty}{(z^{\pm2}tq;q)_\infty(tq;q)_\infty}
    \times\\
\prod_{i=1}^g   \frac{(z^{\pm2}tu_iq;q)_\infty(tu_iq;q)_\infty}{(z^{\pm2}u_i;q)_\infty(u_i;q)_\infty}
\times\,\frac{\sum_{n\in p{\mathbb Z}+a}q^{n^2/p}\,z^{2n}}{(q;q)_\infty}.    
    \label{TCircFibBlock}
\end{gathered}$$ The choice of the contour $\gamma$, which corresponds to a precise choice of the boundary condition for the vector multiplet (or, equivalently, Lagrangian submanifold in the complexified maximal torus of $SU(2)$), will be discussed below.

The WRT invariant of $M_3$ can be computed as follows in terms of $S$ and $T$ matrices[^1]: $$Z_{SU(2)_k}^\text{CS}[M_3]=\sum_{n=1}^{k-1} (S_{1n})^{2-2g}(T_{nn})^{-p}=
    {\sum}'_{n\in {\mathbb Z}_{2k}} (q^{n/2}-q^{-n/2})^{2-2g}q^{-\frac{pn^2}{4}}$$ where we use notation such that matrix indices are "colors" (= dimensions of representations), $q=e^{\frac{2\pi i}{k}}$ and a prime over the sum means that we skip singular terms. After applying the Gauss reciprocity formula $$\sum_{m\in {\mathbb Z}_{2k}}q^{-\frac{pm^2}{4}}\cdot q^{\frac{n\ell}{2}} \; = \;
    \frac{e^{-\frac{\pi i}{4}}(2k)^{1/2}}{|p|^{1/2}}
    \sum_{a\in {\mathbb Z}_p} e^{2\pi i k\frac{a^2}{p}}\cdot
    e^{2\pi i \frac{a\ell}{p}}\cdot
    q^{\frac{\ell^2}{4p}},$$ we arrive at $$Z_{SU(2)_k}^\text{CS}[M_3]
    \; = \; \sum_{a,b\in {\mathbb Z}_p /{\mathbb Z}_2} e^{2\pi ik\text{CS}(a)}\cdot
    S_{ab}\cdot \frac{1}{|{\mathcal W}_b|}\,\left.\widehat{Z}_b(q)\right|_{q\rightarrow e^{\frac{2\pi i}{k}}}$$ where the $S$-matrix is given in ([\[SZp\]](#SZp){reference-type="ref" reference="SZp"}) and, *formally*, $$\widehat{Z}_a(q) \; = \; {\mathcal L}_a^{(p)}\left[(z-z^{-1})^{2-2g}\right]$$ with Laplace transform given in ([\[LaplaceZp\]](#LaplaceZp){reference-type="ref" reference="LaplaceZp"}). To be precise, it can be computed using $$\widehat{Z}_a(q)=\frac{1}{|{\mathcal W}_a|}\cdot\text{v.p.}
    \int_{|z|=1}(z-z^{-1})^{2-2g}\,\sum_{n\in p{\mathbb Z}+a}q^{n^2/p}\,z^{2n}
    \label{WRTCircFibBlock}$$ as a series in $q$, convergent in the unit disk $|q|<1$. One can see that ([\[WRTCircFibBlock\]](#WRTCircFibBlock){reference-type="ref" reference="WRTCircFibBlock"}) coincides with the unrefined partition function of $T[M_3]$ on $D^2\times S^1$, *cf.* ([\[TCircFibBlock\]](#TCircFibBlock){reference-type="ref" reference="TCircFibBlock"}), with removed contribution of Cartan components of the adjoint chiral: $$\widehat{Z}_a(q)=\left.\widehat{Z}_a(q,t,u)\,(qt;q)_\infty\,\prod_{i=1}^g\frac{(u_i;q)_\infty}{(tu_iq;q)_\infty}\right|_{t=1,u_i=1}.$$ The principal value contour prescription in ([\[WRTCircFibBlock\]](#WRTCircFibBlock){reference-type="ref" reference="WRTCircFibBlock"}) suggests that the contour $\gamma$ in ([\[TCircFibBlock\]](#TCircFibBlock){reference-type="ref" reference="TCircFibBlock"}) should be chosen as shown in Figure [\[fig:TCircFib-contour\]](#fig:TCircFib-contour){reference-type="ref" reference="fig:TCircFib-contour"}. Note, that the labels $a$ of homological blocks now correspond to the *connected components* of the space of abelian flat connections.

[^1]: We omit simple overall factors below.

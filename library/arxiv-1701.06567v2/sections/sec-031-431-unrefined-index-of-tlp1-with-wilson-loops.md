---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-031-431-unrefined-index-of-tlp1-with-wilson-loops
section_title: "Unrefined index of $T[L(p,1)]$ with Wilson loops"
section_number: 4.3.1
pages: 64-65
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 1.0
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
[]{#sec:LensWilson label="sec:LensWilson"}

The unrefined superconformal index --- with contribution of the Cartan component of the adjoint chiral removed, as in [\[I-UN-unref\]](#I-UN-unref){reference-type="eqref" reference="I-UN-unref"} --- with the Wilson line inserted at the north pole reads: $$\label{SU2Int}
\begin{aligned}
\langle W_\lambda\rangle\equiv     {\mathcal I}(q;W_\lambda) & =  \frac{1}{2} \sum_{m \in \mathbb{Z}} \int \frac{dz}{2\pi i z} z^{ p m}\cdot \chi_\lambda(q^{m/2}z)\\
&\ \ \ \times \left( q^{2 \left| m \right|}+q^{-2 \left| m \right|}+4 - 2 \left(q^{ \left| m \right|}+q^{- \left| m \right|} \right) \left( z^2 +\frac{1}{z^2} \right)+\left( z^4+\frac{1}{z^4} \right) \right).
\end{aligned}$$ Assuming $\lambda$ is irreducible, we identify it with its highest weight in $\Lambda_{\text{wt},\mathfrak{su}(2)}/{\mathbb Z}_2 \cong {\mathbb Z}_{\geq 0}$. Our convention is such that $$\chi_{\lambda}(z)=\frac{z^{\lambda+1}-z^{-\lambda-1}}{z-z^{-1}}.$$ So, the insertion of an operator $W_\lambda$ with odd value of $\lambda$ automatically gives zero, because of the non-trivial action of the center ${\mathbb Z}_2 \subset SU(2)$.

In the table below we present explicit results for $p=5$ up to $\lambda=38$:\

   $\lambda$   $\langle W_\lambda\rangle$   $\lambda$   $\langle W_\lambda\rangle$   $\lambda$   $\langle W_\lambda\rangle$   $\lambda$   $\langle W_\lambda\rangle$   $\lambda$   $\langle W_\lambda\rangle$
  ----------- ---------------------------- ----------- ---------------------------- ----------- ---------------------------- ----------- ---------------------------- ----------- ----------------------------
       0                   3                    2                  $-1$                  4                   0                    6                $q^{-3}$                8           $-q^{-3}-2q^{-5}$
      10            $2q^{-5}+q^{-7}$           12               $-q^{-7}$               14                   0                   16               $q^{-16}$               18          $-q^{-16}-2q^{-20}$
      20           $2q^{-20}+q^{-24}$          22               $-q^{-24}$              24                   0                   26               $q^{-39}$               28          $-q^{-39}-2q^{-45}$
      30           $2q^{-45}+q^{-51}$          32               $-q^{-51}$              34                   0                   36               $q^{-72}$               38          $-q^{-72}-2q^{-80}$

 .\
This table is almost periodic. This can be understood from the action of Wilson lines on the homological blocks. For the $D^2\times S^1$ partition function of $T[M_3]$ with $W_\lambda$ inserted at the center of the disk, $O \in D^2$, we have: $$\widehat{Z}_a(q;W_\lambda) \; = \; \frac{1}{|{\mathcal W}_a|}\int\frac{dz}{2\pi i z}
    (1-z^{\pm 2})\,\chi_{\lambda}(z)\,\sum_{n\in p{\mathbb Z}+a}q^{n^2/p}\,z^{2n}.
    \label{block-Lp1-knot}$$ Wilson loops act in a very simple way on the homological blocks $\widehat{Z}_a(q)$. For $L(p,1)$, we have $$\widehat{Z}_0=1,\quad \widehat{Z}_1=-q^{1/p},$$ with the rest of the blocks being zero. Let us also formally extend $\widehat{Z}_a$ for $a$ outside the range $\{0,1,\ldots,\lfloor\frac{p}{2}\rfloor\}$ by $\widehat{Z}_a=0$ and define a "shift operator" $$\widehat{Z}_a(q) \; := \; q^{j(2a-j)/p}\widehat{Z}_{a-j}(q),\qquad a,j\in {\mathbb Z}.$$ Then, $$\widehat{Z}_a(q;W_{\lambda}) \; =  \sum_{b \, \equiv \, \pm a \pmod p}[\lambda/2] \, \widehat{Z}_b(q) ,\qquad a\in {\mathbb Z}_p/{\mathbb Z}_2.$$ This equation is not cyclic, and we took $a$ to live in ${\mathbb Z}_{\ge 0}$. Then, one can verify that $$\langle W_\lambda \rangle \; = \sum_{a\in {\mathbb Z}_p/{\mathbb Z}_2}|{\mathcal W}_a|\widehat{Z}_a(q;W_\lambda)\widehat{Z}_a(q^{-1}).$$

One can also deduce the action of $W_\lambda$ on $Z_a=\sum_{b}S_{ab}\widehat{Z}_b$ by applying the $S$-transform, but it won't be very illuminating because $Z_a(q;W_\lambda)$ will be a linear combination of all $Z_a(q)$'s. This difference between $\widehat{Z}_a$ and $Z_a$ again demonstrates the advantage of working with the homological blocks $\widehat{Z}_a$, rather than $Z_a(q)$.

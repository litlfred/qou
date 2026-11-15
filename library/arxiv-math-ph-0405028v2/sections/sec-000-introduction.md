---
doc_id: arxiv-math-ph-0405028v2
doc_title: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 0405028v2.pdf
source_sha256: 90a0e4ba456988d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 0.983
doc_brief: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES — We study an exact asymptotic behavior of the Witten–Reshetikhin–Turaev SU(2) in- variant for the Brieskorn homology spheres Σ(p1, p2, p3)"
---
The quantum invariant for the 3-manifold $\mathcal{M}$ was introduced as a path integral on $\mathcal{M}$ by Witten [@EWitt89a]; as the $SU(2)$ invariant we have $$\label{Witten}
  Z_{k} (\mathcal{M})
  =
  \int \exp\Bigl(
    2 \, \pi \, \mathrm{i} \, k \,
    \mathop{\mathrm{CS}}(A)
  \Bigr) \,
  \mathcal{D} A$$ where $k \in \mathbb{Z}$, and $\mathop{\mathrm{CS}}(A)$ is the Chern--Simons functional defined by $$\mathop{\mathrm{CS}}(A)=
  \frac{1}{8 \, \pi^2} \,
  \int\limits_{\mathcal{M}}
  \mathop{\mathrm{Tr}}
  \left(
    A \wedge \mathrm{d} A +
    \frac{2}{3} \, A \wedge A \wedge A
  \right)$$ Since this work, studies of the quantum invariants of the 3-manifolds have been extensively developed, and a construction of the 3-manifold invariant was reformulated combinatorially and rigorously in Refs.  using a surgery description of $\mathcal{M}$ and the colored Jones polynomial defined in Ref. .

By applying a stationary phase approximation, an asymptotic behavior of the Witten invariant in large $k\to\infty$ is expected to be [@EWitt89a; @FreeGomp91a] (see also Ref. ) $$\label{asymptotic_Witten}
  Z_k(\mathcal{M})
  \sim
  \frac{1}{2} \, \mathrm{e}^{-\frac{3}{4} \pi \mathrm{i}} \,
  \sum_\alpha
  \sqrt{T_\alpha(\mathcal{M})} \,
  \mathrm{e}^{- 2 \pi \mathrm{i} I_\alpha/4} \,
  \mathrm{e}^{2 \pi \mathrm{i} (k+2) \mathop{\mathrm{CS}}(A)}$$ Here the sum runs over a flat connection $\alpha$, and $T_\alpha$ and $I_\alpha$ are the Reidemeister torsion and the spectral flow defined modulo $8$ respectively.

In this article we consider the Brieskorn homology spheres $\Sigma(p_1, p_2, p_3)$ where $p_i$ are pairwise coprime positive integers. This is the intersection of the singular complex surface $$z_1^{~p_1} +   z_2^{~p_2} +   z_3^{~p_3} =0$$ in complex three-space with the unit five-sphere $|z_1|^2 + |z_2|^2  + |z_3|^2  =1$. The manifold $\Sigma(2,3,5)$ is the Poincaré homology sphere. These manifolds have a rational surgery description as in Fig. [1](#fig:Brieskorn){reference-type="ref" reference="fig:Brieskorn"}, and the fundamental group has the presentation $$\label{presentation}
  \pi_1 \bigl( \Sigma(p_1,p_2,p_3) \bigr)
  =
  \Bigl\langle
  x_1, x_2, x_3, h
  ~\big|~
  \text{$h$  center},
  \text{$x_k^{~p_k} = h^{-q_k}$ for $k=1,2,3$},
  x_1 \, x_2 \, x_3 =1
  \Bigr\rangle$$ where $q_k \in \mathbb{Z}$ such that $$\begin{gathered}
  \label{P_p_q}
  P \,  \sum_{k=1}^3 \frac{q_k}{p_k} = 1
\end{gathered}$$ Here and hereafter we use $$\begin{gathered}
  P = P(p_1,p_2, p_3)
  = p_1 \, p_2 \, p_3
\end{gathered}$$

<figure id="fig:Brieskorn">
<div class="psfrags">
<embed src="surgery_brieskorn.ps" />
</div>
<figcaption> Rational surgery description of the Brieskorn homology sphere <span class="math inline"><em>Σ</em>(<em>p</em><sub>1</sub>,<em>p</em><sub>2</sub>,<em>p</em><sub>3</sub>)</span></figcaption>
</figure>

Asymptotic behavior of the quantum invariant for the homology spheres was studied in Refs. . Our purpose here is to reformulate these results number theoretically by use of properties of the modular form following a method of Lawrence and Zagier [@LawrZagi99a]. A key observation is a fact that the Witten--Reshetikhin--Turaev (WRT) invariant for the Brieskorn homology spheres is regarded as a limit value of the Eichler integral of the modular form with weight $3/2$ as was suggested in Ref. . Using a nearly modular property of the Eichler integral, we can derive an exact asymptotic behavior of the WRT invariant. Correspondingly, we can find an interpretation for topological invariants such as the Chern--Simons invariant, the Casson invariant [@KWalk92a], the Ohtsuki invariant [@HMuraka93a; @HMuraka95a; @Ohtsu95b; @TOhtsu96a], and the Ray--Singer--Reidemeister torsion from the viewpoint of the modular form.

This paper is organized as follows. In section [\[sec:invariant\]](#sec:invariant){reference-type="ref" reference="sec:invariant"} we construct the WRT invariant for the Brieskorn homology spheres $\Sigma(p_1,p_2,p_3)$ following Ref. . We use a surgery description of the 3-manifold, and apply a formula in Ref. . In section [\[sec:modular\]](#sec:modular){reference-type="ref" reference="sec:modular"} we introduce the modular form with weight $3/2$. This gives a $(p_1-1) \, (p_2 -1 ) \, (p_3 -1)/4$-dimensional representation of the modular group $PSL(2;\mathbb{Z})$. We consider the Eichler integral thereof in section [\[sec:Eichler\]](#sec:Eichler){reference-type="ref" reference="sec:Eichler"}. We study a limiting value of the Eichler integral at $\tau\in \mathbb{Q}$, and show that the number of the Eichler integrals which have non-zero value in a limit $\tau\to N\in\mathbb{Z}$ is related to the Casson invariant of the Brieskorn homology spheres. It will be discussed that we have a one-to-one correspondence with the irreducible representation of the fundamental group, and that the Chern--Simons invariant is given from this limiting value of the Eichler integral. We further give a nearly modular property of the Eichler integral. In section [\[sec:WRT\]](#sec:WRT){reference-type="ref" reference="sec:WRT"} we reveal a key identity that the WRT invariant for the Brieskorn spheres coincides with a limiting value of the Eichler integral at $\tau\to 1/N$. This was suggested in Ref.  where a correspondence was proved only for a case of the Poincaré homology sphere. Combining with results in section [\[sec:Eichler\]](#sec:Eichler){reference-type="ref" reference="sec:Eichler"} we obtain an exact asymptotic expansion of the WRT invariant which is constituted from two terms; one is a sum of dominating exponential term which gives the Chern--Simons term, and another is a "tail" part which may be regarded as a contribution from a trivial connection. In section [\[sec:torsion\]](#sec:torsion){reference-type="ref" reference="sec:torsion"} we prove that the $\mathbf{S}$-matrix of the modular transformation gives both the Reidemeister torsion and the spectral flow. We show in section [\[sec:Ohtsuki\]](#sec:Ohtsuki){reference-type="ref" reference="sec:Ohtsuki"} that a tail part gives the Ohtsuki invariant. Explicitly computed is the $n$-th Ohtsuki invariant in terms of the $L$-function. The last section is devoted to concluding remarks.

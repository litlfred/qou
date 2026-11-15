---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-005-21-quantum-volume-conjecture-refined
section_title: "Quantum volume conjecture: refined"
section_number: 2.1
pages: 7-7
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.771
latex_coverage_ratio: 0.929
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
The fact that a $q$-difference operator $\widehat A (\widehat x, \widehat y; q)$ annihilates the partition function of Chern-Simons theory / matrix model / B-model / instanton partition function is easy to refine. Just like each of these partition functions becomes $t$-dependent, so does the operator $\widehat A (\widehat x, \widehat y; q,t)$ that annihilates it. The commutation relations [\[xycomm\]](#xycomm){reference-type="eqref" reference="xycomm"} do not change and, therefore, our proposal for the refinement of [\[VCquant\]](#VCquant){reference-type="eqref" reference="VCquant"} is easy to state: $$\label{VCquantref}
\begin{equation}
\widehat A^{\text{ref}} (\widehat x, \widehat y; q, t) \; P_* (K;q,t) \; \simeq \; 0 \qquad \qquad \text{(knots)}
\end{equation}
or
\begin{equation}
\widehat A^{\text{ref}} (\widehat x, \widehat y; q, t) \; Z_{\text{BPS}}^{\text{open}} (u,q,t) \; \simeq \; 0 \qquad \qquad \text{(BPS states)}
\end{equation}$$ While the formulation of this refined / homological version is simple and follows the lines of the ordinary quantum volume conjecture [\[VCquant\]](#VCquant){reference-type="eqref" reference="VCquant"}, its interpretation is rather deep and non-trivial. It involves details of the framework in which [\[VCquantref\]](#VCquantref){reference-type="eqref" reference="VCquantref"} arises and will be given a proper treatment in the following sections. Here, we only remark that polynomials $P_n (K;q,t)$ which appear in ([\[VCquantref\]](#VCquantref){reference-type="ref" reference="VCquantref"}a) as $t$-dependent analogs of the colored Jones polynomials $J_n (K;q)$ are Poincaré polynomials of the $n$-colored $sl(2)$ knot homology groups ${\cal H }^{sl(2),V_n} (K)$: $$P_n (K;q,t) \; = \; \sum_{i,j} q^i t^j \dim {\cal H }_{i,j}^{sl(2),V_n} (K) \,,
\label{Pnoptimistic}$$ such that $$J_n (K;q) \; = \; P_n (K;q,t=-1) \,.$$ Because the $t$-deformation does not affect the commutation relation [\[xycomm\]](#xycomm){reference-type="eqref" reference="xycomm"}, the operators $\widehat x$ and $\widehat y$ act on $P_n$ exactly as in [\[xyactionJ\]](#xyactionJ){reference-type="eqref" reference="xyactionJ"}: $$\begin{aligned}
& \widehat x P_n \; = \; q^n P_n \label{xyactionP} \\
& \widehat y P_n \; = \; P_{n+1} \notag
\end{aligned}$$

::: {#table-qt}
    **Model**                                           $\widehat{A}^{\text{ref}} (\widehat{x},\widehat{y};q,t)$
  ------------- ----------------------------------------------------------------------------------------------------------------------------------------
     unknot                                 $(1 + t^3 q \widehat{x}) ( - q^{-1} t^{-3})^{1/2} - (1 - \widehat{x})\widehat y$
                                                         $\frac{1}{q + \widehat{x}^2 q^{2} t^3} \; \widehat{y}
                              + \frac{\widehat{x}^3 (x - q) t^4}{q (q + \widehat{x}^2 t^3) (1 + \widehat{x} q t^3)} \; \widehat{y}^{-1} +$
                                                        $-   \frac{t^2 \widehat{x}^2}{1 + \widehat{x}^2 q t^3} -
                                                          \frac{ q - \widehat{x} q t^2 + \widehat{x}^{4} t^6 +
                                          \widehat{x}^{2} t^2 (1 + t + q t)}{(q + \widehat{x}^{2} t^3) (1 + \widehat{x} q t^3)}$
   tetrahedron                            $1 + t \widehat{y} - t \sqrt{q} \, \widehat{x}(-\widehat{y})^f  \; \simeq  \; 1 + t$
    conifold     $1 + t \widehat{y} - t \sqrt{q} \, \widehat{x}(-\widehat{y})^f  + Q \sqrt{-tq} \, \widehat{x}(-\widehat{y})^{f+1} \; \simeq \; 1 + t$ 

  : Refined quantum curves derived in this paper. The notation "$\ldots \simeq 1 + t$" should be understood as $\widehat{A}^{\text{ref}} Z_{\text{BPS}}^{\text{open}} = 1 + t$. Note that in section [\[sec:Bmodel\]](#sec:Bmodel){reference-type="ref" reference="sec:Bmodel"} the quantization parameter $q$ is identified with $q_2$, and the deformation parameter is $t= - \frac{q_1}{q_2}$.
:::

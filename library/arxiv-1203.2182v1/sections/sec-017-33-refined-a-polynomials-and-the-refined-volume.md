---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-017-33-refined-a-polynomials-and-the-refined-volume
section_title: "Refined $A$-polynomials and the refined ``volume'' $S_0 (u,t)$"
section_number: 3.3
pages: 38-39
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.985
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
[]{#sec:knotS0 label="sec:knotS0"}

One next goal is to test the second new conjecture of the present paper -- namely, the refinement of the generalized volume conjecture ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}a) -- in a large class of examples associated with $(2,2p+1)$ torus knots.

Specifically, in this section we derive the refined $A$-polynomials $A^{\text{ref}}(x,y;t)$ for $(2,2p+1)$ torus knots and analyze the refined "volume" $S_0 (u,t)$ that dominates the asymptotic behavior ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}a), thereby verifying [\[S0ref\]](#S0ref){reference-type="eqref" reference="S0ref"}.

At a very practical level, the refined $A$-polynomials arise as the $q \to 1$ limit of $\widehat{A}^{\text{ref}}(\widehat{x},\widehat{y};q,t)$, as we explained earlier and illustrated in Figure [\[fig:AAAA\]](#fig:AAAA){reference-type="ref" reference="fig:AAAA"}. Therefore, if one knows the quantum operator $\widehat{A}^{\text{ref}}(\widehat{x},\widehat{y};q,t)$, say, as in the case of the unknot or the trefoil knot, then it is trivial to find its classical version, $A^{\text{ref}}(x,y;t)$. However, our conjecture ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}) provides another way to look at the refined $A$-polynomial. Namely, according to [\[S0ref\]](#S0ref){reference-type="eqref" reference="S0ref"}, it determines the asymptotic behavior of the $n$-colored homological invariants $P_n (q,t)$ in the limit [\[reflimit\]](#reflimit){reference-type="eqref" reference="reflimit"}. Our conjecture says that, in this limit, the homological invariants $P_n (q,t)$ exhibit exponential growth with the leading term $S_0(u,t)$, such that $$y = e^{S'_0(u,t)} \; = \; e^{\frac{d}{du} S_0(u,t)} \; = \; e^{x \frac{d}{dx} S_0(\log x,t)} \,.   \label{yS0prim}$$ This gives another way of expressing the dependence of $y$ on $x$, which is equivalent to the equation $A^{\text{ref}}(x,y;t)=0$. In other words, the leading order free energy $S_0(u,t)$ computed directly from the asymptotics of $P_n (q,t)$ must agree with the integral ([\[S0ref\]](#S0ref){reference-type="ref" reference="S0ref"}) on an algebraic curve $A^{\text{ref}}(x,y;t) = 0$. In this section, we will test this equivalence and our conjecture ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}a). We also determine the refined $A$-polynomials even in those examples where the full quantum curve $\widehat{A}^{\text{ref}}(\widehat{x},\widehat{y};q,t)$ is not known at present!

In particular, for the unknot and for the trefoil knot, for which we already found $\widehat{A}^{\text{ref}}(\widehat{x},\widehat{y};q,t)$ in the previous section, we will show that their $q \to 1$ limits indeed agree with the refined $A$-polynomials computed from the asymptotics of the corresponding colored homological invariants. Furthermore, even for more general $(2,2p+1)$ torus knots, for which the full quantum $A$-polynomials are not known at present, we will find the refined $A$-polynomials by testing our conjecture ([\[VCparamref\]](#VCparamref){reference-type="ref" reference="VCparamref"}). Impatient reader can skip directly to Table [\[table_A-poly4\]](#table_A-poly4){reference-type="ref" reference="table_A-poly4"}, where we list the explicit form of $A^{\text{ref}}_{T^{2,2p+1}} (x,y;t)$ for several small values of $p$. In section [\[sec:Bmodel\]](#sec:Bmodel){reference-type="ref" reference="sec:Bmodel"}, we will use analogous techniques to analyze the refined $A$-polynomials and asymptotic expansions in examples coming from refined BPS state counting.

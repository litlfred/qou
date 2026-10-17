---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-012-47-proof-of-theorem-37
section_title: "Proof of Theorem 3.7"
section_number: 4.7
pages: 13-14
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.824
latex_coverage_ratio: 0.933
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sub.thm.2 label="sub.thm.2"}

First we show that $I_{\Delta}$ satisfies the required equations:

-   $I_{\Delta}\in V$ from Section [\[sub.isindex\]](#sub.isindex){reference-type="ref" reference="sub.isindex"}. Lemma [\[lem.degID\]](#lem.degID){reference-type="ref" reference="lem.degID"} and Equation [\[eq.degID\]](#eq.degID){reference-type="eqref" reference="eq.degID"} manifestly imply that $\delta(I_{\Delta}(m,e)) \geq 0$ for all integers $m$ and $e$. Thus, $I_{\Delta}\in V_+$. Moreover, $I_{\Delta}(0,0)=1+O(q)$.

-   $I_{\Delta}$ satisfies the pentagon identity from Section [\[sub.pentagon\]](#sub.pentagon){reference-type="ref" reference="sub.pentagon"}.

It remains to show the uniqueness part in Theorem [\[thm.2\]](#thm.2){reference-type="ref" reference="thm.2"}. Suppose $f \in V_+$ satisfies the pentagon and $f(0,0)(0) \neq 0$. Corollary [\[cor.V+\]](#cor.V+){reference-type="ref" reference="cor.V+"} implies that $f(m,e)(q)=C(q)I_{\Delta}(e,m)(q)$ for some $C(q)
\in \mathbb Q((q))$. Consider the special pentagon for $f$ and $I_{\Delta}$: $$f(0,0)^2=\sum_{e \in \mathbb Z} f(0,e)^3 q^e 
\qquad I_{\Delta}(0,0)^2=\sum_{e \in \mathbb Z} I_{\Delta}(0,e)^3 q^e
\,.$$ It follows that $C(q)^2=C(q)^3$ and since $C(q) \neq 0$, we get $C(q)=1$. This concludes the uniqueness part of Theorem [\[thm.2\]](#thm.2){reference-type="ref" reference="thm.2"}. 0◻

---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-010-44-proof-of-triality-part-c-of-theorem-32
section_title: "Proof of triality: part (c) of Theorem 3.2"
section_number: 4.4
pages: 12-13
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.946
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sub.prop.S3 label="sub.prop.S3"}

In this section we prove part (c) of Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"}. Equation [\[eq.Z3\]](#eq.Z3){reference-type="eqref" reference="eq.Z3"} concerns the following $\mathbb Z/3$-action on $V$.

::: definition
[]{#def.Sf label="def.Sf"} Consider the action $f \mapsto Sf$ on a function $f: \mathbb Z^2 \longrightarrow\mathbb Z((q^{1/2}))$ given by: $$\label{eq.Sf}
Sf(m,e)=(-q^{\frac{1}{2}})^{-e} f(e,-e-m) \,.$$
:::

::: proposition
[]{#prop.S3 label="prop.S3"} (a) We have: $S^3=Id$. (b) If $f \in V$, then $Sf=f$, and of course, also $S^2f=f$.
:::

Part (c) of Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"} follows from part (b) of the above proposition.

::: proof
*Proof.* (of Proposition [\[prop.S3\]](#prop.S3){reference-type="ref" reference="prop.S3"}) Part (a) is elementary. For part (b), assume that $f$ satisfies Equation [\[eq.rec1\]](#eq.rec1){reference-type="eqref" reference="eq.rec1"} for all $(m,e)$. Replace $(m,e)$ by $(e,-1-e-m)$ in [\[eq.rec1\]](#eq.rec1){reference-type="eqref" reference="eq.rec1"} and we obtain that $$\label{eq.em1}
-f(e, -1 - e - m) + q^{-\frac{e}{2}} f(e, -e - m) + 
 q^{-\frac{1}{2} - \frac{e}{2} - \frac{m}{2}} f(1 + e, -1 - e - m)=0 \,.$$ Now, replace $f$ by $Sf$ in the left hand side of Equation [\[eq.rec1\]](#eq.rec1){reference-type="eqref" reference="eq.rec1"}, and compute that the result is given by $$(-1)^{e+1}\left( -f(e, -1 - e - m) + q^{-\frac{e}{2}} f(e, -e - m) + 
 q^{-\frac{1}{2} - \frac{e}{2} - \frac{m}{2}} f(1 + e, -1 - e - m) \right)$$ The above vanishes from Equation [\[eq.em1\]](#eq.em1){reference-type="eqref" reference="eq.em1"}.

Likewise, assume that $f$ satisfies Equation [\[eq.rec2\]](#eq.rec2){reference-type="eqref" reference="eq.rec2"} for all $(m,e)$. Replace $(m,e)$ by $(e,1-e-m)$ in [\[eq.rec2\]](#eq.rec2){reference-type="eqref" reference="eq.rec2"} and we obtain that $$\label{eq.em2}
q^{\frac{1}{2} - \frac{e}{2} - \frac{m}{2}} f(-1 + e, 1 - e - m) 
+ q^{-\frac{e}{2}} f(e, -e - m) -  f(e, 1 - e - m)=0$$ Now, replace $f$ by $Sf$ in the left hand side of Equation [\[eq.rec2\]](#eq.rec2){reference-type="eqref" reference="eq.rec2"}, and compute that the result is given by $$(-1)^{e+1}\left( q^{\frac{1}{2} - \frac{e}{2} - \frac{m}{2}} f(-1 + e, 1 - e - m) + q^{-\frac{e}{2}} f(e, -e - m) - 
 f(e, 1 - e - m) \right)$$ It follows that if $f \in V$, then the above vanishes from Equation [\[eq.em2\]](#eq.em2){reference-type="eqref" reference="eq.em2"}. In other words, if $f \in V$ then $Sf \in V$. To conclude that $f=Sf$, it suffices to show (by part (a) of Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"}) that $f(0,0)=(Sf)(0,0)$. If $f(0,0)=A$, $f(0,1)=B$, using Remark [\[rem.thm1a\]](#rem.thm1a){reference-type="ref" reference="rem.thm1a"} we have: $$(Sf)(0,0)=f(0,0)=A \qquad (Sf)(0,1)=f(0,1)+q^{-\frac{1}{2}}f(1,-1)=
B + q^{-\frac{1}{2}} (- B q^{\frac{1}{2}})=0 \,.$$ This concludes the proof of Proposition [\[prop.S3\]](#prop.S3){reference-type="ref" reference="prop.S3"}. ◻
:::

## $I_{\Delta}$ is a tetrahedron index {#sub.isindex}

Observe that by its definition, $$I_{\Delta}(m,e)=\sum_{e \in \mathbb Z} S(m,e,n)$$ is given by a one-dimensional sum of a *proper $q$-hypergeometric term* ([@WZ; @PWZ]) $$S(m,e,n)=(-1)^n \frac{q^{\frac{1}{2}n(n+1)
-\left(n+\frac{1}{2}e\right)m}}{(q)_n(q)_{n+e}} \,.$$ It follows by [@WZ] that $I_{\Delta}(m,e)$ is $q$-holonomic in both variables $m$ and $e$. Moreover, recursion relations for $I_{\Delta}(m,e)$ can be found by the creative telescoping method of [@WZ]. For instance, $S$ satisfies the recursion $$\label{eq.Scert2}
q^{\frac{e}{2}} S(m - 1, e, n)+ q^{-\frac{m}{2}} S(m, e - 1, n) -S(m,e,n)=0$$ which implies that $I_{\Delta}$ satisfies Equation [\[eq.rec2\]](#eq.rec2){reference-type="eqref" reference="eq.rec2"}. To prove Equation [\[eq.Scert2\]](#eq.Scert2){reference-type="eqref" reference="eq.Scert2"}, divide by $S(m,e,n)$ and use the fact that $$q^{\frac{e}{2}} \frac{S(m - 1, e, n)}{S(m,e,n)}=q^{e + n}
\qquad
 q^{-\frac{m}{2}} \frac{S(m, e - 1, n)}{S(m,e,n)}=1-q^{e + n} \,.$$ The proof of Equation [\[eq.rec1\]](#eq.rec1){reference-type="eqref" reference="eq.rec1"} is similar. For an alternative proof, using the quantum dilogarithm, see Section [\[sec.QDL\]](#sec.QDL){reference-type="ref" reference="sec.QDL"}.

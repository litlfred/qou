---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-034-the-dependence-of-a-categorical-connection-holon
section_title: "The dependence of a categorical connection holonomy on the point in the principal bundle"
section_number: null
pages: 40-41
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.938
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
Let ${\Gc=(\d\colon E \to G,\tr)}$ be a Lie crossed module. Fix a smooth manifold $M$, and a smooth principal $G$-bundle $P \to M$ with a connection $\w \in \A^1(P,\lg)$. Let $(\w,m)$ be a $\Gc$-categorical connection on $P$. Let $x,y\in M$. Choose $v \in P_y$. Let $\n$ be a 1-path connecting $y$ with $x$. This curve $\n$ defines a categorical group isomorphism $T_\n\colon \Pc_2(M,y)  \to  \Pc_2(M,x)$ in the obvious way, by considering horizontal compositions. More precisely let $\G_\n$ be the 2-path such that $\G_\n(t,s)=\n(t);\forall s,t \in [0,1]$. Let also $\G_{\n^{-1}}(t,s)=\n^{-1}(t);\forall s,t \in [0,1].$ Then $T_\n([\G])\doteq [\G_{\n^{-1}}] \circ_h [\G]\circ_h [\G_{\n}] \in \P_2(M,x)$ for each $[\G] \in \P_2(M,y),$ and $T_\n([\g])=[\n^{-1}\g\n]$ for $[\n] \in \pi_1^1(M,y)$.

::: Theorem
Let $u={\mathcal{H}}_\w(\n,1,v)$. We have: $$F_{(\w,m,v)}=F_{(\w,m,u)}\circ T_\n.$$
:::

::: Proof
Let $[\G] \in \P_2(M,y)$. Then $[\G]=[\G_{\n}] \circ_h  T_\n([\G]) \circ_h [\G_{\n^{-1}}]$. Let $\G^1= \G_{\n} \circ_h \G_{\n^{-1}} \circ_h \G  \circ_h \G_{\n} \circ_h  \G_{\n^{-1}}$, thus $[\G^1]=[\G]$. Put $\g_s(t)=\G^1(t,s); \forall s,t \in [0,1]$. Let also $\G'= \G_{\n^{-1}}  \circ_h \G \circ_h \G_{\n}$, thus $[\G']=T_\n[\G].$ Put $\g_s'(t)=\G'(t,s); \forall s,t \in [0,1]$. We have $$\begin{aligned}
\frac{d}{d s} e_{\G^1}(s)&=e_{\G^1}(s)\int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,v) } dt\\
&=e_{\G^1}(s)\int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g'_s(t)},\t{\frac{\d}{\d s}\g'_s(t)} \right)  _{{\mathcal{H}}_\w(\g'_s,t,{\mathcal{H}}_\w(\n,1,v)) } dt \\
&{=e_{\G^1}(s)\int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g'_s(t)},\t{\frac{\d}{\d s}\g'_s(t)} \right)  _{{\mathcal{H}}_\w(\g'_s,t,u) } dt }
\end{aligned}$$ The second equation follows since $\G_\n(s,t)$ does not depend on $s$. Comparing with equation [\[G\]](#G){reference-type="ref" reference="G"} it follows that $e_{\G^1}(s)=e_{\G'}(s)$, for each $s \in [0,1]$. Therefore: $$\begin{aligned}
F_{(\w,m,v)}^2([\G])&=F_{(\w,m,v)}^2([\G^1])=e_{\G^1} =e_{\G'} 
                 =F_{(\w,m,u)}^2([\G'])
                 =F_{(\w,m,u)}^2(T_\n([\G])).
\end{aligned}$$ This finishes the proof of the result at the level of the elements of $\P_2(M,y)$. The proof at the level of the elements of $\pi_1^1(M,y)$ is similar.
:::

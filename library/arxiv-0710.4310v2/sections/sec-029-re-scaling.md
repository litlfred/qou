---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-029-re-scaling
section_title: "Re-scaling"
section_number: null
pages: 33-34
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 1.0
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
Let $\G$ be a 2-path in $M$ such that $\d_l(\G)=\d_r(\G)=*$. As usual put $\G(t,s)=\g_s(t); s,t \in [0,1]$. Consider a smooth map $f \colon [a,b] \to [0,1]$, where $-\infty < a <b <+\infty$. We suppose that $f(a)=0$ and $f(b)=1$. Let $\G'(s,t)=\g'_s(t)$ be such that $\g'_s(t)=\g_{f(s)}(t)$, where $s \in [a,b]$ and $t \in [0,1]$. Even though $\G'$ is not a 2-path, for its domain is $[0,1]\times [a,b]$, the elements $g_{\g'_s}\in E$ and $e_{\G'}(s)\in E$, where $s \in [a,b]$, defined in [\[dchcc\]](#dchcc){reference-type="ref" reference="dchcc"}, still make sense.

::: Lemma
[]{#rescaling label="rescaling"} We have $${g_{\g'_s}=g_{\g_{f(s)}} \quad \textrm{and}\quad
e_{\G'}(s)=e_{\G}(f(s)),}$$ for each $s\in [a,b]$.
:::

::: Proof
The first equation follows since $\g'_s=\g_{f(s)}$, as curves $[0,1] \to M$, for each $s\in [a,b]$. As for the second one we have: $$\begin{aligned}
\frac{d}{d s} e_{\G'}(s)&={e_{\G'}(s) \int_{0}^{1} m \left (\t{\frac{\d}{\d t}{\G'}(t,s)},\t{\frac{\d}{\d s}{\G'}(t,s)} \right)_{{\mathcal{H}}_\w(\g'_s,t,u) } dt}\\
&{=e_{\G'}(s)\frac{d}{d s} f(s)\int_{0}^{1} m \left (\t{ \frac{\d \G }{\d t}(t,f(s))},\t{\frac{\d \G}{\d s}(t,f(s))} \right)  _{{\mathcal{H}}_\w(\g_{f(s)},t,u) } dt .}
\end{aligned}$$ Whereas: $${\frac{d}{d s} e_\G(f(s))= e_\G(f(s))\frac{d}{d s} f(s)\int_{0}^{1} m \left (\t{ \frac{\d \G }{\d t}(t,f(s))},\t{\frac{\d \G}{\d s}(t,f(s))} \right)  _{{\mathcal{H}}_\w(\g_{f(s)},t,u) } dt .}$$ Therefore $s \mapsto e_{\G'}(s)$ and $s \mapsto e_\G(f(s))$ are both solutions of the same differential equation and they have the same initial conditions.
:::

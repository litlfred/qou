---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-033-the-dependence-of-a-categorical-connection-holon
section_title: "The dependence of a categorical connection holonomy on the elements of the fibre"
section_number: null
pages: 39-40
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.933
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
Choose $u,v \in P$. We want to relate $F_{(\w,m,u)}$ with $F_{(\w,m,v)}$. Suppose first that $u,v$ each belong to the fibre $P_x$ of $P$ at a certain point $x\in M$. Let $g\in G$ be the unique element such that $u=vg$. Let $\g$ be a 1-path of $M$ starting and ending at $x$. Then ${\mathcal{H}}_\w(\g,1,u)={\mathcal{H}}_\w(\g,1,vg)={\mathcal{H}}_\w(\g,1,v)g$. Therefore since $\mathcal{H}_\w(\g,1,u)F_{(\w,u)}^1(\g)=u$ and ${\mathcal{H}}_\w(\g,1,v)F_{(\w,v)}^1(\g)=v$ we have the well-known formula: $$\label{A1}F^1_{(\w,v)}(\g)=g F^1_{(\w,u)}(\g) g^{-1},$$ for $\g$ a smooth curve starting and ending at $x$ and $u=vg$, where $u,v \in P_x$ and $g \in G$.

Let us now see how $F^2_{(m,\w,u)}$ is related to $F^2_{(m,\w,v)}$.

::: Lemma
For any 2-path $\G$ in $M$, with $\d_l(\G)=\d_r(\G)=x$, we have:

$$\label{A2}F^2_{(\w,m,v)}(\G)=g \tr F^2_{(\w,m,u)}(\G),$$ where $u,v$ belong to the fibre $P_x$ of $P$, and $g \in G$ is such that $u=vg$.
:::

::: Proof
As usual, put $\G(t,s)=\g_s(t); s,t \in [0,1].$ Let $e_\G(s)$ and $f_\G(s)$ be defined by the differential equations: $${\frac{d}{d s} e_\G(s)=e_\G(s)\int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,u) } dt,}$$ and $${\frac{d}{d s} f_\G(s)=f_\G(s)\int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,v) } dt };$$ with initial conditions $e_\G(0),f_\G(0)=1_E$; see equation [\[G\]](#G){reference-type="ref" reference="G"}. Then: $$\begin{aligned}
\frac{d}{d s} g^{-1}\tr f_\G(s)
&=g^{-1} \tr \frac{d}{d s} f_\G(s)\\
&{= g^{-1}\tr  \Big( f_\G(s)  \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,v) } dt \Big)}\\
&{=\left (g^{-1}\tr f_\G(s) \right) \Big(g^{-1}\tr \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right) _{{\mathcal{H}}_\w(\g_s,t,v) } dt \Big)}\\
&=\left (g^{-1}\tr f_\G(s) \right)  \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,ug^{-1}) g} dt\\
&=\left (g^{-1}\tr f_\G(s) \right) \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,u) } dt. 
\end{aligned}$$ The fourth equation follows from ([\[Refer\]](#Refer){reference-type="ref" reference="Refer"}). Therefore $g^{-1} \tr f_\G(s)= e_\G(s)$, for each $s \in [0,1]$, thus, in particular, $F^2_{(\w,m,v)}(\G)=g \tr F^2_{(\w,m,u)}(\G)$.
:::

There is a natural left action of $G$ on $G\ltimes E$, given by $g\tr (h,e)=(ghg^{-1},g\tr e)$. Using this, we can summarise the results of this subsection, equations ([\[A1\]](#A1){reference-type="ref" reference="A1"}) and ([\[A2\]](#A2){reference-type="ref" reference="A2"}), in the following:

::: Theorem
[]{#I label="I"} If $v \in P_x$ then $${F_{(\w,m,vg)}=g^{-1} \tr F_{(\w,m,v)}}$$ for any $g \in G$.
:::

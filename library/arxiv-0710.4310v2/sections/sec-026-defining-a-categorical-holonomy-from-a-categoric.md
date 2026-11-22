---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-026-defining-a-categorical-holonomy-from-a-categoric
section_title: "Defining a categorical holonomy from a categorical connection"
section_number: null
pages: 25-27
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 1.0
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#dchcc label="dchcc"} Consider a base point $*\in M$. Choose also $u \in P_*$, the fibre of $P$ at $*$. To describe $F_{(\w,m,u)}$ on the set $\pi_1^1(M,*)$ of objects of $\Pc_2(M,*)$, we use theorem [\[E\]](#E){reference-type="ref" reference="E"}. Therefore we define: $$F_{(\w,m,u)}^1([\g])=F_{(\w,u)}^{{1}}([\g]), \textrm{ where } [\g] \in \pi_1^1(M,*).$$

Let now $\G$ be a 2-path in $M$ with $\d_l(\G)=\d_r(\G)=*$. Let $\g_s(t)=\G(t,s); s,t \in [0,1]$. To define $F^2_{(\w,m,u)}$, consider the smooth function $s \in [0,1] \mapsto e_\G(s)\in E$, which solves the following differential equation in $E$: $$\label{G}
{\frac{d}{d s} e_\G(s)=e_\G(s) \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,u) } dt,}$$ with initial condition $e_\G(0)=1_E.$ Set $e_\G=e_\G(1)$ to be the element of $E$ assigned to the 2-path $\G$. Then we define: $$F^2_{(\w,m,u)}(\G)=\left ( F_{(\w,u)}^{{1}}\big ({[\d_d(\G)]}\big) ,e_\G\right).$$

Recall the elements $g_{\g_s}\in G$, where $s \in [0,1]$, which are given by the condition: $ug_{\g_s}={\mathcal{H}}_\w(\g_s,1,u);$ see [\[BBB\]](#BBB){reference-type="ref" reference="BBB"}. Thus $F^1_{(\w,m,u)}({[\g_s]})=g^{-1}_{\g_s},$ where $g^{-1}_{\g_s}\doteq \big (g_{\g_s}\big )^{-1}$. In local coordinates, our definition of a categorical holonomy coming from a categorical connection coincides with definition 2.32 of [@BS].

We will prove that $F_{(\w,m,u)}=\left ( F^1_{(\w,m,u)},F^2_{(\w,m,u)}\right)$ defines a categorical holonomy $\Pc_2(M,*) \to \C(\Gc)$. Explicitly, we need to prove that the assignment:

$$\begin{CD} \d_u(\G )\\ @AA\G A \\ \d_d(\G) \end{CD} \mapsto \begin{CD} g^{-1}_{\g_1}\\  @AA e_\G  A \\ g^{-1}_{\g_0} \end{CD} \quad \quad  ,$$ where $\G$ is a 2-path in $M$ such that $\d_l(\G)=\d_r(\G)=*$, and $\G(t,s)=\g_s(t);\forall s,t \in [0,1]$, depends only on the rank-2 homotopy class to which $\G$ belongs, and defines a monoidal functor $\Pc_2(M,*)\to \C(\Gc)$, such that the induced maps on the set of objects and morphisms of $\Pc_2(M,*)$ are smooth.

First of all:

::: Lemma
[]{#DDD label="DDD"} Let $\G$ be a 2-path in $M$ with $\d_l(\G)=\d_r(\G)=*$. Then for each $s \in [0,1]$ we have: $g_{\g_0}\d(e_\G(s))= g_{\g_s}.$ Here $\G(t,s)=\g_s(t);\forall s,t \in [0,1]$.
:::

::: Proof
The previous equation holds for $s=0$, by definition of $e_\G(s)$. We have: $$\frac{d}{d s} \big( g_{\g_0}\d(e_\G(s)) \big)= g_{\g_0}\frac{d}{d s}\d\left ( e_\G(s)\right)= g_{\g_0}\d\left(\frac{d}{d s} e_\G(s)\right),$$ therefore: $$\begin{aligned}
\frac{d}{d s} \big( g_{\g_0}\d(e_\G(s)) \big)&= {g_{\g_0}\d  \Big( e_\G(s) \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,u) } dt \Big)} \\
&= g_{\g_0}\d  ( e_\G(s)) \int_{0}^{1} \W \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,u) }  dt,
\end{aligned}$$ since $\d(m)=\W$. By equation ([\[C\]](#C){reference-type="ref" reference="C"}) we also have: $$\begin{aligned}
 \frac{d}{d s} g_{\g_s}    =       g_{\g_s}              \int_{0}^{1} \W \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,u) }.
    
\end{aligned}$$ Thus both sides of the equation are solutions of the same differential equation in $G$, and have the same initial condition.
:::

We remark that, using the terminology of [@BS], this result corresponds to the condition that a local pre-$2$-holonomy gives rise to a local true $2$-holonomy, which there also follows from the vanishing of the fake curvature.

Let $\G \colon [0,1]^2 \to M$ be a 2-path in $M$ with $\d_l(\G)=\d_r(\G)=*$. We need to prove that $F^2_ {(\w,m,u)} (\G)$ depends only on the 2-track defined by $\G$, in other words on the rank-2 homotopy class of 2-paths to which $\G$ belongs. This will be shown shortly in Corollary [\[cormain2\]](#cormain2){reference-type="ref" reference="cormain2"} of Theorem [\[Main2\]](#Main2){reference-type="ref" reference="Main2"}. For now, consider a 3-path $J$, where $J(t,s,x)=\G^x(t,s); \forall t,s,x \in [0,1]$, defining a homotopy (not necessarily rank-2) connecting the 2-paths $\G^0$ and $\G^1$. Suppose that $\d_l(\G^0),\d_r(\G^0)=*$, thus $\d_l(\G^1),\d_r(\G^1)=*$. We want to calculate $\frac{\d}{\d x}e_{\G^x}(s),$ where $s,x \in [0,1]$.

In fact, for later applications, we will consider the more general case when, for each $x \in [0,1]$, we have that $\d_l(\G^x)=q(x)$ and $\d_r(\G^x)=q(x)$, where $q\colon [0,1] \to M$ is a smooth map. This generality will be important to define Wilson spheres in [\[WS\]](#WS){reference-type="ref" reference="WS"}. The lemma in the following subsection will be useful for our purpose.

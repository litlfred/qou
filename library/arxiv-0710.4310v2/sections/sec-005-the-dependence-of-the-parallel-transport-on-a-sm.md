---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-005-the-dependence-of-the-parallel-transport-on-a-sm
section_title: "The dependence of the parallel transport on a smooth family of curves - the Ambrose-Singer theorem"
section_number: null
pages: 6-9
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.964
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#BBB label="BBB"}

Let $M$ be a smooth manifold. Let ${{\rm D}}^n\doteq [0,1]^n$ be the $n$-cube, where $n \in \N$. A map $f\colon  {{\rm D}}^n \to M$ is said to be smooth if its partial derivatives of any order exist and are continuous as maps ${{\rm D}}^n \to M$. Let $G$ be a Lie group with Lie algebra $\lg$. Consider a smooth principal $G$-bundle $\pi \colon P \to M$ with a connection 1-form $\w \in \A^1(P,\lg)$.

Now let $s \in [0,1] \mapsto \g_s$ be a smooth 1-parameter family of smooth curves $[0,1] \to M$. Here smooth means that the map $\G\colon (t,s) \in [0,1]^2 \mapsto \ga_s(t) \in M$ is smooth. Define the initial point map $q\colon [0,1] \to M$ by $q(s)=\g_s(0)$ for each $s\in[0,1]$. Choose $u \in P_{q(0)}$ and set $u_s={\mathcal{H}}_\w(q,s,u)\in P_{q(s)}$, where $s \in  [0,1]$. Our purpose is to analyse the $s$-dependence of ${\mathcal{H}}_\w(\ga_s,t,u_s)$, where $s,t \in  [0,1]$, by calculating: $$\begin{aligned}
\frac{\d}{\d s} {\mathcal{H}}_\w(\g_s,t,u_s).
\end{aligned}$$ This analysis is of course classical.

For convenience of notation, define $$f(s,t)={\mathcal{H}}_\w(\g_s,t,u_s);s,t \in [0,1].$$ Let the coordinate vector fields of $[0,1]^2$ be $\frac{\d}{\d t}$ and $\frac{\d}{\d s}$. We have: $$\begin{aligned}
\frac{\d}{\d t} \w \left (\frac{\d}{\d s} f(s,t) \right) & =  \frac{\d}{\d t} f^*(\w) \left (  \frac{\d}{\d s} \right )\\
&=f^*(d \w) \left ( \frac{\d}{\d t}, \frac {\d}{\d s}\right)+\frac{\d}{\d s} f^*(\w) \left (  \frac{\d}{\d t} \right )\\
&=d \w \left ( \frac{\d}{\d t}f(s,t), \frac {\d}{\d s}f(s,t)\right).
\end{aligned}$$ Note that the second equation follows from the well-known formula $$\label{A}
d\f(X,Y)=X\f(Y)-Y\f(X)-\f([X,Y]),$$ valid for any 2-form $\f$ on a manifold $M$ and any $X,Y \in \X(M)$. The last equation follows from the fact that $\frac{\d}{\d t} f(s,t)$ is horizontal, by definition of parallel transport.

Therefore by Cartan's structure equation ([\[cse\]](#cse){reference-type="ref" reference="cse"}) and the fact that $\frac{\d}{\d t} f(s,t)$ is horizontal it follows that: $$\label{CC}
\frac{\d}{\d t} \w \left (\frac{\d}{\d s} f(s,t) \right) =\W\left ( \frac{\d}{\d t}f(s,t), \frac {\d}{\d s}f(s,t)\right).$$ Since $\W(X,Y)=0$ if either of the vectors $X$ or $Y$ is vertical we can conclude: $$\frac{\d}{\d t} \w \left (\frac{\d}{\d s} f(s,t) \right) =\W\left ( \left (\frac{\d}{\d t}f(s,t)\right )^H, \left (\frac {\d}{\d s}f(s,t)\right)^H\right).$$

Note that, by definition of parallel transport, we have $$\left (\frac{\d}{\d t}f(s,t)\right)^H=\frac{\d}{\d t}f(s,t)= \left (\t{\frac{\d}{\d t}\g_s(t)}\right)_{{\mathcal{H}}_\w(\g_s,t,u_s) }.$$ Given that $\left (\frac{\d}{\d s}f(s,t)\right )^H$ is horizontal and the fact that: $$\pi_*\left (\left (\frac{\d}{\d s}f(s,t)\right)^H \right) =\pi_* \left(\frac{\d}{\d s}f(s,t) \right)=\frac{\d}{\d s}\pi \big ( f(s,t)\big )=\frac{\d}{\d s}\g_s(t),$$ it follows $$\left (\frac{\d}{\d s}f(s,t)\right)^H= \left (\t{\frac{\d}{\d s}\g_s(t)}\right)_{{\mathcal{H}}_\w(\g_s,t,u_s) }.$$

Going back to equation ([\[CC\]](#CC){reference-type="ref" reference="CC"}), we have that, for each $s \in [0,1]$, $\w \left (\frac{\d}{\d s} f(s,0) \right)=0,$ since $f(s,0)=u_s={\mathcal{H}}_\w(q,s,u)$, hence $\frac{\d}{\d s} f(s,0)$ is horizontal for each $s \in [0,1]$. We thus arrive at the following well known result:

::: Lemma
[]{#Main1 label="Main1"} Let $G$ be a Lie group with Lie algebra $\lg$. Let $P$ be a smooth principal $G$-bundle over the manifold $M$. Let $s \in [0,1] \mapsto \g_s$ be a smooth 1-parameter family of curves $[0,1] \to M$. Here smooth means that the map $(s,t) \in [0,1]^2 \mapsto \g_s(t)\in M$ is smooth. Consider a connection $\w \in \A^1(P,\lg)$. Let $q\colon [0,1] \to M$ be the curve such that $q(s)=\g_s(0), \forall s \in [0,1]$. Choose $u \in P_{q(0)}$, and let $u_s={\mathcal{H}}_\w(q,s,u)\in P_{q(s)}$, where $s \in  [0,1]$. The following holds for each $s,t' \in [0,1]$: $$\w\left (\frac{\d}{\d s} { {\mathcal{H}}_\w(\g_s,t',u_s)}\right)=\int_{0}^{t'} \W \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)_{{\mathcal{H}}_\w(\g_s,t,u_s) }  d t.$$
:::

Consider the case when all curves $\g_s\colon [0,1] \to M$, where $s \in [0,1]$, are closed, though possibly with varying initial points. (This flexibility will be important to define Wilson spheres in [\[WS\]](#WS){reference-type="ref" reference="WS"}). Then we can define a family of holonomies $g_{\g_s}\in G$, where $s \in [0,1]$, by: $$u_sg_{\g_s}= {\mathcal{H}}_\w(\g_s,1,u_s), \forall s \in [0,1].$$ We will use the preceding lemma to obtain a differential equation satisfied by $g_{\g_s}$.

Because $\frac{d}{d s} u_s$ is horizontal it follows that: $${\w \left ( \frac{d}{d s} (u_s g_{\g_s})\right) = \w \left ( u_s\frac{d}{d s} g_{\g_s}\right)=\int_{0}^{1} \W \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)_{{\mathcal{H}}_\w(\g_s,t,u_s) }dt.}$$ Since, for each $s \in [0,1]$, the vector $u_s\frac{d}{d s} g_{\g_s}$ is vertical, this means, by the second condition of the definition of a connection 1-form $\w$ (see [\[CCC\]](#CCC){reference-type="ref" reference="CCC"}): $$\label{D}
u_s\frac{d}{d s} g_{\g_s} =\left (\int_{0}^{1} \W \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)_{{\mathcal{H}}_\w(\g_s,t,u_s)  } dt\right)^\#_{{\mathcal{H}}_\w(\g_s,1,u_s) },$$ or $$\begin{aligned}
&\left [\frac{d}{d t'}u_s g_{\g_{(s+t')}}\right]_{t'=0}\\&\quad\quad \quad \quad=\frac{d}{d t'} {{\mathcal{H}}_\w(\g_s,1,u_s) }\exp\left (t'\int_{0}^{1} \W \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right) _{{\mathcal{H}}_\w(\g_s,t,u_s) } dt \right) _{t'=0}\\
&\quad \quad\quad \quad =\frac{d}{d t'} u_s g_{\g_s}\exp\left (t'\int_{0}^{1} \W \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)   _{{\mathcal{H}}_\w(\g_s,t,u_s) } dt\right) _{t'=0},
\end{aligned}$$ which, given the fact that the right action of $G$ on $P$ is free, is equivalent to:

::: Lemma
[]{#EEE label="EEE"} $$\label{C}
\frac{d}{d s} g_{\g_s}=g_{\g_s} \int_{0}^{1} \W \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right) _{{\mathcal{H}}_\w(\g_s,t,u_s) } dt.$$
:::

This fact will be of major importance later.

---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-027-a-well-known-lemma
section_title: "A well-known lemma"
section_number: null
pages: 27-27
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.944
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#wkl label="wkl"} Let $G$ be a Lie group. Consider a $\lg$-valued smooth function $V(s,x)$ defined on $[0,1]^2$. Consider the following differential equation in $G$: $$\frac{\d}{\d s} a(s,x)=a(s,x)V(s,x),$$ with initial condition $a(0,x)=1_G, \forall x \in [0,1]$. We want to know $\frac{\d}{\d x} a(s,x)$.

Let $\theta$ be the canonical $\lg$-valued $1$-form on $G$. Thus $\theta$ is left invariant and satisfies $\theta(A)=A, \forall A \in \lg$, being defined uniquely by these properties. Also $$\label{AAA}
d \theta(A,B)=- \theta ([A,B]),$$ where $A,B \in \lg$. We have: $$\frac{\d }{ \d x} \theta\left (\frac{\d}{\d s} a(s,x) \right )= \frac{\d }{ \d x}\theta\big (  a(s,x)V(s,x) \big )= \frac{\d }{ \d x}V(s,x).$$ On the other hand: $$\begin{aligned}
\frac{\d }{ \d x} \theta\left (\frac{\d}{\d s} a(s,x) \right ) 
&= d a^*(\theta)\left(  \frac{\d }{ \d x}, \frac{\d }{ \d s}\right) {+}\frac{\d }{ \d s} a^*(\theta) \left ( \frac{\d }{ \d x} \right){+} a^*(\theta)\left(  \left [\frac{\d }{ \d x}, \frac{\d }{ \d s} \right]\right) \\
&=d \theta\left(  \frac{\d }{ \d x}  a(s,x) , \frac{\d }{ \d s} a(s,x) \right)  {+}\frac{\d }{ \d s} \theta \left ( \frac{\d }{ \d x}a(s,x) \right).
\end{aligned}$$ Therefore: $$\begin{gathered}
\theta \left ( \frac{\d }{ \d x} a(s,x) \right)\\= \int_0^s \left ({-}d \theta\left(  \frac{\d }{ \d x}  a(s',x) , \frac{\d }{ \d s'} a(s',x) \right) {+}\frac{\d }{ \d x} V(s',x)\right )ds'+\theta\left (\frac{\d }{ \d x}a(0,x)\right).
\end{gathered}$$ Since $\frac{\d }{ \d x}a(0,x)=0$ (due to the initial conditions) we have the following:

::: Lemma
[]{#WKL label="WKL"} $$\frac{\d }{ \d x} a(s,x)= a(s,x)  \int_0^s \left ({-}d \theta\left(  \frac{\d }{ \d x}  a(s',x) , \frac{\d }{ \d s'} a(s',x) \right) {+} \frac{\d }{ \d x} V(s',x)\right )ds',$$ for each $x,s \in [0,1]$.
:::

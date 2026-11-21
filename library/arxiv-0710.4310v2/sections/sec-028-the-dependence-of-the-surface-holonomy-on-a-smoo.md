---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-028-the-dependence-of-the-surface-holonomy-on-a-smoo
section_title: "The dependence of the surface holonomy on a smooth family of surfaces"
section_number: null
pages: 27-33
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.993
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
The discussion in this subsection will be very similar to that of [\[BBB\]](#BBB){reference-type="ref" reference="BBB"}. We want to prove an analogue of lemma [\[EEE\]](#EEE){reference-type="ref" reference="EEE"} for the surface holonomy of a family of 2-paths $\G^x$.

Consider a smooth map $J\colon [0,1]^3 \to M$, where $J(t,s,x)=\G^x(t,s); \forall t,s,x \in [0,1]$. Given $x,s \in [0,1]$, a smooth curve $\g^x_s\colon [0,1] \to M$ is defined as $\g^x_s(t)=J(t,s,x)$, where $t,s,x \in [0,1]$. Suppose that, for each $x \in [0,1]$, there exists $q(x) \in M$ such that $J(0,s,x)=J(1,s,x)=q(x)$ for each $s \in  [0,1]$. In other words $\d_l(\G^x)=\d_r(\G^x)=q(x)$. Note that the map $x \in [0,1] \mapsto q(x) \in M$ is necessarily smooth. Let $q(0)=* \in M$. Choose $u \in P_*$, the fibre of $P$ at $*$. Let also $u_x={\mathcal{H}}_\w(q,x,u)$, where $x \in [0,1]$. In particular $u_0=u$.

Note that the conditions above imply that: $$\label{S1}
\Rank ({ {\EuScript{D}}}_{(s,x)} J)_{(t,s,x)}\leq 1 \textrm{ if } t=0 \textrm{ or } t=1,\textrm{ for each } s,x \in [0,1].$$ Suppose that we also have: $$\label{S2}
\Rank ({{\EuScript{D}}}_{(t,x)} J)_{(t,s,x)}\leq 1 \textrm{ if } s=0 \textrm{ or } s=1,\textrm{ for each } t,x \in [0,1].$$

For each $x \in [0,1]$, let $s \in [0,1] \mapsto e_{\G^x}(s)\in E$ be the solution of the differential equation in $E$: $$\label{E1}
{\frac{d}{d s} e_{\G^x}(s)=e_{\G^x}(s)\int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g^x_s(t)},\t{\frac{\d}{\d s}\g^x_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s^x,t,u_x) } dt ,}$$ with initial condition: $$\label{E2}
e_{\G^x}(0)=1_E, \forall x \in [0,1].$$ See equation ([\[G\]](#G){reference-type="ref" reference="G"}). Our purpose is to calculate the $x$-dependence of $e_{\G^x}= e_{\G^x}(1)$, the element of $E$ assigned to $\G_x$, by calculating ${\frac{d}{d x}} e_{\G^x} .$ The result of this calculation, Theorem [\[Main2\]](#Main2){reference-type="ref" reference="Main2"}, is entirely analogous to Lemma [\[EEE\]](#EEE){reference-type="ref" reference="EEE"}, with the 2-curvature 3-form $\M$ replacing the curvature 2-form $\W$.

Lemma ([\[WKL\]](#WKL){reference-type="ref" reference="WKL"}) leads to: $$\begin{gathered}
 \frac{d }{ d x} e_{\G^x} =e_{\G^x}  \int_0^1 \int_{0}^{1} \frac{\d }{ \d x}  \left (m \left (\t{\frac{\d}{\d t}\g^x_s(t)},\t{\frac{\d}{\d s}\g^x_s(t)} \right)  _{{\mathcal{H}}_\w(\g_{s} ^x,t,u_x) }  \right) dt ds\\
{-} e_{\G^x}  \int_0^1   d \theta\left(  \frac{\d }{ \d x}  e_{\G^x}(s) , \frac{\d }{ \d s} e_{\G^x}(s) \right)   ds.
\end{gathered}$$ Let $$\begin{aligned}
A_x&=\int_0^1 \int_{0}^{1} \frac{\d }{ \d x} \left ( m \left (\t{\frac{\d}{\d t}\g^x_s(t)},\t{\frac{\d}{\d s}\g^x_s(t)} \right)  _{{\mathcal{H}}_\w(\g_{s} ^x,t,u_x) } \right) dt ds\in \le\\
B_x&=\int_0^1 d \theta\left(  \frac{\d }{ \d x}  e_{\G^x}(s) , \frac{\d }{ \d s} e_{\G^x}(s) \right)   ds \in \le.
\end{aligned}$$ Thus $$\label{torefer}
 \frac{d }{ d x} e_{\G^x} =e_{\G^x} (A_x-B_x).$$

Let us analyse $A_x$ and $B_x$ separately. Consider the map $f\colon [0,1]^3 \to P$ such that $f(x,s,t)={{\mathcal{H}}_\w(\g_s^x,t,u_x) }$, for each $x,s,t \in [0,1].$ This map is smooth; see [@KN page 74]. By definition we have $\frac{\d}{\d t } f(x,s,t) = \t{ \frac{\d}{\d t}\g^x_s(t)}_{{\mathcal{H}}_\w(\g_s^x,t,u_x) }.$ Also, we trivially get: $\left (\frac{\d}{\d s } f(x,s,t)\right) ^H = \t{ \frac{\d}{\d s}\g^x_s(t)}_{{\mathcal{H}}_\w(\g_{s}^x,t,u_x) }$ and $\left ( \frac{\d}{\d x } f(x,s,t)\right)^H = \t{ \frac{\d}{\d x}\g^x_s(t)}_{{\mathcal{H}}_\w(\g_{s}^x,t,u_x) }$; see [\[BBB\]](#BBB){reference-type="ref" reference="BBB"}. Therefore, since $m(X,Y)$ vanishes if either $X$ or $Y$ is vertical, it follows that: $$\begin{aligned}
A_x&= \int_{0}^{1}\int_{0}^{1} \frac{\d }{ \d x}  m \left (\frac{\d}{\d t} f(x,s,t),\frac{\d}{\d s}f(x,s,t) \right) dt ds\\ 
  &  =    \int_0^1 \int_{0}^{1} dm\left ( \frac{\d}{\d x} f(x,s,t), \frac{\d}{\d t}f(x,s,t), \frac{\d}{\d s}f(x,s,t)\right)dtds
\\ & \quad \quad\quad \quad\quad \quad {-} \int_0^1 \int_{0}^{1} \frac{\d}{\d t} m\left ( \frac{\d}{\d s}f(x,s,t), \frac{\d}{\d x}f(x,s,t)\right )dtds
\\  &\quad \quad\quad \quad \quad \quad {-}  \int_0^1 \int_{0}^{1} \frac{\d}{\d s} m\left ( \frac{\d}{\d x}f(x,s,t), \frac{\d}{\d t}f(x,s,t)\right )dtds.
\end{aligned}$$ We have used the well known equation: $$\begin{gathered}
d\a(X,Y,Z)=X\a(Y,Z)+Y\a(Z,X)+Z\a(X,Y)\\+\a(X,[Y,Z])+ \a(Y,[Z,X])+\a(Z,[X,Y]),
\end{gathered}$$ valid for any smooth 2-form $\a$ in a manifold. Therefore: $$\begin{aligned}
A_x&=\int_{0}^{1}\int_{0}^{1} dm\left ( \frac{\d}{\d x} f(x,s,t), \frac{\d}{\d t}f(x,s,t), \frac{\d}{\d s}f(x,s,t)\right)dtds
\\ &{-} \int_0^1  \left [m\left ( \frac{\d}{\d s}f(x,s,1), \frac{\d}{\d x}f(x,s,1)\right )-m\left ( \frac{\d}{\d s}f(x,s,0), \frac{\d}{\d x}f(x,s,0)\right )\right]ds
\\  &{-} \int_0^1  \left [m\left ( \frac{\d}{\d x}f(x,1,t), \frac{\d}{\d t}f(x,1,t)\right ) - m\left ( \frac{\d}{\d x}f(x,0,t), \frac{\d}{\d t}f(x,0,t)\right )\right]dt.
\end{aligned}$$ We analyse each term separately. Since $m(X,Y)=0$ if either $X$ or $Y$ is vertical we have: $${
m\left ( \frac{\d}{\d x}f(x,1,t), \frac{\d}{\d t}f(x,1,t)\right )=m\left (\t{\frac{\d}{\d x}\g^x_1(t)},\t{\frac{\d}{\d t}\g^x_1(t)} \right)  _{{\mathcal{H}}_\w(\g_1^x,t,u_x) } =0,}$$ by equation ([\[S2\]](#S2){reference-type="ref" reference="S2"}). Analogously from equation ([\[S1\]](#S1){reference-type="ref" reference="S1"}) or equation ([\[S2\]](#S2){reference-type="ref" reference="S2"}) it follows that: $m\left ( \frac{\d}{\d x}f(x,0,t), \frac{\d}{\d t}f(x,0,t)\right )=0,$ $m\left ( \frac{\d}{\d s}f(x,s,0), \frac{\d}{\d x}f(x,s,0)\right )=0,$ and $m\left ( \frac{\d}{\d s}f(x,s,1), \frac{\d}{\d x}f(x,s,1)\right )=0.$ Therefore we have: $$\label{torefer2}
A_x=\int_{0}^{1}\int_{0}^{1} dm\left ( \frac{\d}{\d x} f(x,s,t), \frac{\d}{\d t}f(x,s,t), \frac{\d}{\d s}f(x,s,t)\right)dtds,$$ for each $x \in [0,1]$.

We now analyse $B_x$, for each $x \in [0,1]$. We have: $$\begin{aligned}
& d \theta\Big(  \frac{\d }{ \d x}  e_{\G^x}(s) , \frac{\d }{ \d s} e_{\G^x}(s) \Big)  
\\ &= \int_0^1   d \theta\Big(  \frac{\d }{ \d x}  e_{\G^x}(s) ,e_{\G^x}(s) m\left (\t{\frac{\d}{\d t}\g^x_s(t)},\t{\frac{\d}{\d s}\g^x_s(t)} \right)_{{\mathcal{H}}_\w(\g_s^x,t,u_x) }  \Big)  dt,\\
&= \int_0^1   d \theta\Big( e_{\G^x}(s)^{-1} \frac{\d }{ \d x}  e_{\G^x}(s) , m \left (\t{\frac{\d}{\d t}\g^x_s(t)},\t{\frac{\d}{\d s}\g^x_s(t)} \right )_{{\mathcal{H}}_\w(\g_s^x,t,u_x) } \Big )dt
\\& = -\int_0^1   \Big[ e_{\G^x}(s)^{-1} \frac{\d }{ \d x}  e_{\G^x}(s) , m \left (\t{\frac{\d}{\d t}\g^x_s(t)},\t{\frac{\d}{\d s}\g^x_s(t)}  \right)    _{{\mathcal{H}}_\w(\g_s^x,t,u_x) }\Big]   dt
\\& = -\int_0^1  \partial \left ( e_{\G^x}(s)^{-1} \frac{\d }{ \d x}  e_{\G^x}(s) \right ) \triangleright m \left (\t{\frac{\d}{\d t}\g^x_s(t)},\t{\frac{\d}{\d s}\g^x_s(t)} \right)     _{{\mathcal{H}}_\w(\g_s^x,t,u_x) }   dt.
\end{aligned}$$ The first equation follows by definition of $e_{\G^x}(s)$, the second since the $\le$-valued 2-form $d \theta$ on $E$ is left invariant (since $\theta$ is left invariant) and the third by the well-known formula ([\[AAA\]](#AAA){reference-type="ref" reference="AAA"}). Finally, the last equation follows since $(\partial\colon \le \to \lg, \tr )$ is a differential crossed module.

By lemma [\[DDD\]](#DDD){reference-type="ref" reference="DDD"}, we also have that $g_{\g^x_0}\d(e_{\G^x}(s))= g_{\g^x_s}$, for each $s,x \in [0,1]$. Therefore: $$\begin{aligned}
\partial \Big ( e_{\G^x}^{-1}(s) \frac{\d }{ \d x}  e_{\G^x}(s) \Big )&=
   \partial \Big ( e_{\G^x}^{-1} (s)\Big) \partial \Big(\frac{\d }{ \d x}  e_{\G^x}(s) \Big )\\
&= g_{\g^x_s}^{-1} g_{\g^x_0}     \frac{\d }{ \d x} \Big(g_{\g^x_0}^{-1} g_{\g^x_s}\Big)         \\
&= \int_{0}^{1} \W \left (\t{\frac{\d}{\d t}\g_s^x(t)},\t{\frac{\d}{\d x}\g_s^x(t)} \right) _{{\mathcal{H}}_\w(\g_s^x,t,u_x) } dt,
\end{aligned}$$ where the last equation follows by lemma [\[EEE\]](#EEE){reference-type="ref" reference="EEE"}. We also use the fact that $\frac{\d }{ \d x} g_{\g^x_0}=0.$ This follows from lemma [\[EEE\]](#EEE){reference-type="ref" reference="EEE"} and equation [\[S2\]](#S2){reference-type="ref" reference="S2"}. Putting everything together, we obtain: $$\begin{gathered}
{d \theta\left(  \frac{\d }{ \d x}  e_{\G^x}(s) , \frac{\d }{ \d s} e_{\G^x}(s) \right)}
 =-\int_{0}^{1} \W \left (\t{\frac{\d}{\d t}\g_s^x(t)},\t{\frac{\d}{\d x}\g_s^x(t)} \right) _{{\mathcal{H}}_\w(\g_s^x,t,u_x) } dt\,   \tr\\ \int_0^1 m \left (\t{\frac{\d}{\d t}\g^x_s(t)},\t{\frac{\d}{\d s}\g^x_s(t)}  \right) _{{\mathcal{H}}_\w(\g_s^x,t,u_x) }   dt.
\end{gathered}$$ Due to the fact that $(\d\colon \le  \to \lg, \tr )$ is a differential crossed module, given $e,f \in \le$ we have: $\d(e)\tr f=[e,f]=-[f,e]=-\d(f) \tr e.$ If we use this together with the fact that $\W(X,Y)$ and $m(X,Y)$ vanish if either of the vectors $X$ or $Y$ is vertical it thus follows that (since $\d(m)=\W$): $$\begin{gathered}
\label{tcompare}
{B_x} =
\int_0^1 \left (\int_{0}^{1} \W \left (\frac{\d}{\d t}f{(x,s,t)},\frac{\d}{\d s}f{(x,s,t)}  dt \right )  \tr\right. \\ \left .\int_0^1 m \left (\frac{\d}{\d t}f{(x,s,t)},\frac{\d}{\d x}f{(x,s,t)}  \right)   dt\right)ds.
\end{gathered}$$

The following is a 2-dimensional version of Lemma [\[EEE\]](#EEE){reference-type="ref" reference="EEE"}.

::: Theorem
[]{#Main2 label="Main2"} Let $M$ be a smooth manifold. Let ${\Gc=(\d\colon E \to G,\tr)}$ be a Lie crossed module. Let $P \to M$ be a principal $G$-bundle over $M$. Consider a $\Gc$-categorical connection $(\w,m)$ on $P$. Let $J\colon [0,1]^3 \to M$ be a smooth map. Let $J(t,s,x)=\G^x(t,s)=\g^x_s(t);\forall t,s,x \in [0,1]$. Suppose that $\d_l(\G^x)=\d_r(\G^x)=q(x),\forall x \in [0,1]$, where $q\colon [0,1] \to M$ is a smooth curve. Choose $u \in P_{q(0)}$, the fibre of $P$ at $q(0)$. Let also $u_x=\H_\w(q,{x},u)$, where $x \in [0,1]$. In particular $u_0=u$.

Consider the map $(s,x)\in [0,1]^2 \mapsto e_{\G^x}(s)\in E$ defined by equations ([\[E1\]](#E1){reference-type="ref" reference="E1"}) and ([\[E2\]](#E2){reference-type="ref" reference="E2"}). Let $e_{\G^x}=e_{\G^x}(1)$. For each $x\in [0,1]$, we have:

$$\begin{aligned}
\frac{d }{ d x}e_{\G^x}  &=e_{\G^x} \int_0^1 \int_{0}^{1} dm\left ( \t{\frac{\d}{\d x} \g_s^x(t)},\t{ \frac{\d}{\d t} \g_s^x(t)},\t{ \frac{\d}{\d s} \g_s^x(t)}\right)_{{\mathcal{H}}_\w(\g_s^x,t,u_x) }  dtds\\
&=e_{\G^x} \int_0^1 \int_{0}^{1} \M\left ( \t{\frac{\d}{\d x} \g_s^x(t)},\t{ \frac{\d}{\d t} \g_s^x(t)},\t{ \frac{\d}{\d s} \g_s^x(t)}\right)_{{\mathcal{H}}_\w(\g_s^x,t,u_x) }  dtds.
\end{aligned}$$
:::

::: Proof
By the 2-structure equation, see [\[se\]](#se){reference-type="ref" reference="se"}, and equation ([\[BB\]](#BB){reference-type="ref" reference="BB"}) it follows that: $$\begin{aligned}
\int_0^1 \int_{0}^{1} &dm\left ( \t{\frac{\d}{\d x} \g_s^x(t)},\t{ \frac{\d}{\d t} \g_s^x(t)},\t{ \frac{\d}{\d s} \g_s^x(t)}\right)_{{\mathcal{H}}_\w(\g_s^x,t,u) }  dtds\\
&=\int_0^1 \int_{0}^{1} \M\left ( \frac{\d}{\d x} f{(x,s,t)}, \frac{\d}{\d t}f{(x,s,t)}, \frac{\d}{\d s} f{(x,s,t)}\right) dtds\\
&=\int_0^1 \int_{0}^{1} dm\left ( \frac{\d}{\d x} f{(x,s,t)}, \frac{\d}{\d t}f{(x,s,t)}, \frac{\d}{\d s} f{(x,s,t)}\right) dtds\\
& \quad \quad +\int_0^1 \int_{0}^{1} \w\left ( \frac{\d}{\d x} f{(x,s,t)}\right) \tr m\left (\frac{\d}{\d t}f{(x,s,t)}, \frac{\d}{\d s} f{(x,s,t)}\right) dtds\\
& \quad \quad -\int_0^1 \int_{0}^{1} \w\left ( \frac{\d}{\d s} f{(x,s,t)}\right) \tr m\left (\frac{\d}{\d t}f{(x,s,t)}, \frac{\d}{\d x} f{(x,s,t)}\right) dtds.
\end{aligned}$$ Note that $\w\left ( \frac{\d}{\d t} f(x,t,s\right )=\w\left (\frac{\d}{\d t}{\mathcal{H}}_\w(\g^x_s,t,u_x)\right) =0$.

Also by lemma [\[Main1\]](#Main1){reference-type="ref" reference="Main1"} and the fact that $\W$ is horizontal: $$\begin{aligned}
&\int_{0}^{1} \w\left ( \frac{\d}{\d s} f{(x,s,t)}\right) \tr m\left (\frac{\d}{\d t}f{(x,s,t)}, \frac{\d}{\d x} f{(x,s,t)}\right) dt \\
   &= \int_{0}^{1} \int_0^{t} \W  \left (\frac{\d}{\d t'}f{(x,s,t')}, \frac{\d}{\d s} f{(x,s,t')}\right){dt'} \tr m\left (\frac{\d}{\d t}f{(x,s,t)}, \frac{\d}{\d x} f{(x,s,t)}\right) dt \\
&= \int_{0}^{1}   \W  \left (\frac{\d}{\d t'}f{(x,s,t')}, \frac{\d}{\d s} f{(x,s,t')}\right)dt' \tr \int_0^1 m\left (\frac{\d}{\d t'}f{(x,s,t')}, \frac{\d}{\d x} f{(x,s,t')}\right) dt' \\          
&  - \int_0^1\W\left (\frac{\d}{\d t}f{(x,s,t)}, \frac{\d}{\d s} f{(x,s,t)}\right) \tr \left (\int_0^t m\left (\frac{\d}{\d t'}f{(x,s,t')}, \frac{\d}{\d x} f{(x,s,t')}\right) dt' \right )dt.
\end{aligned}$$ The last equation follows from integrating by parts. Indeed, given a smooth $\lg$-valued function $V(t)$ and a smooth $\le$-valued function $W(t)$, each defined on $[0,1]$, we have: $$\begin{gathered}
 \int_0^1 \int_0^tV(t')dt' \tr W(t)dt\\=\left [ \left (\int_0^tV(t')dt'\right) \tr \left (\int_0^tW(t')dt'\right)\right]_{t=1}- \int_0^1 V(t) \tr \left(\int_0^tW(t')dt'\right) dt.
\end{gathered}$$ Let us analyse the very last term. Applying the fact that $(\d\colon \le \to \lg, \tr  )$ is a differential crossed module together with $\d(m)=\W$, part of the definition of a categorical connection $(\w,m)$, we have, since $\d(e)\tr f=-\d(f) \tr e; \forall e,f \in {\le}$: $$\begin{aligned}
&\int_0^1\W\left (\frac{\d}{\d t}f{(x,s,t)}, \frac{\d}{\d s} f{(x,s,t)}\right) \tr \left (\int_0^t m\left (\frac{\d}{\d t'}f{(x,s,t')}, \frac{\d}{\d x} f{(x,s,t')}\right) dt' \right )dt\\
 &=-\int_0^1 \int_0^t \W\left (\frac{\d}{\d t'}f{(x,s,t')}, \frac{\d}{\d x} f{(x,s,t')}\right) dt' \tr m\left (\frac{\d}{\d t}f{(x,s,t)}, \frac{\d}{\d s} f{(x,s,t)}\right)   dt\\
&=- \int_0^1 \w\left (\frac{\d}{\d x}f{(x,s,t)}\right) dt' \tr m\left (\frac{\d}{\d t}f{(x,s,t)}, \frac{\d}{\d s} f{(x,s,t)}\right)   dt.
\end{aligned}$$ Therefore: $$\int_0^1 \int_{0}^{1} \M\left ( \t{\frac{\d}{\d x} \g_s^x(t)},\t{ \frac{\d}{\d t} \g_s^x(t)},\t{ \frac{\d}{\d s} \g_s^x(t)}\right)_{{\mathcal{H}}_\w(\g_s^x,t,{u_x}) }  dtds =A_x-B_x,$$ by equations ([\[torefer2\]](#torefer2){reference-type="ref" reference="torefer2"}) and ([\[tcompare\]](#tcompare){reference-type="ref" reference="tcompare"}). Comparing with equation ([\[torefer\]](#torefer){reference-type="ref" reference="torefer"}), yields theorem [\[Main2\]](#Main2){reference-type="ref" reference="Main2"}.
:::

From this theorem and the fact that the horizontal lift $X \mapsto \t{X}$ of vector fields on $M$ defines a linear map $\X(M) \to \X(P)$ we obtain the following:

::: Corollary
[]{#cormain2 label="cormain2"} Let $M$ be a smooth manifold with a base point $*$. Let also ${\Gc=(\d\colon E \to G,\tr)}$ be a Lie crossed module. Let $P \to M$ be a principal $G$-bundle over $M$, and let $u \in P_*$, the fibre at $*\in M$. Consider a $\Gc$-categorical connection $(\w,m)$ on $P$. Let $\G$ be a 2-path in $M$ with $\d_l(\G)=\d_r(\G)=*$. Let $\G(t,s)=\g_s(t)$, for each $t,s \in [0,1]$. Then $F_{(\w,m,u)}^2(\G)=(g_{\g_0}^{-1},e_\G )$ depends only on the rank-2 homotopy class of 2-tracks $[\G]$ to which $\G$ belongs.
:::

Consider a crossed module ${\Gc=(\d\colon E \to G,\tr)}$. Let the categorical group it defines be $\C(\Gc)$; see [\[CCG\]](#CCG){reference-type="ref" reference="CCG"}. Let also be given a smooth manifold $M$ with a base point $*$, a principal $G$-bundle $P$ over $M$ and $\Gc$-categorical connection $(\w,m)$ on $P$. We defined maps $F^1_{(\w,m,u)}\colon \pi_1^1(M,*) \to G$ (the sets of objects of $\Pc(M,*)$ and of $\C(\Gc)$, respectively) and $F^2_{(\w,m,u)}\colon \P_2(M,*) \to G \ltimes E$ (the sets of morphisms of $\Pc(M,*)$ and $\C(\Gc)$, respectively). We now prove that this assignment, defined in [\[dchcc\]](#dchcc){reference-type="ref" reference="dchcc"}, is a categorical holonomy. This will complete the proof of theorem [\[FFF\]](#FFF){reference-type="ref" reference="FFF"}.

---
doc_id: arxiv-1411.6062v2
doc_title: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-007-21-some-lemmas-from-complex-analysis
section_title: "Some lemmas from complex analysis"
section_number: 2.1
pages: 7-10
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.914
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quantum diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨uller theory"
---
[]{#sub.two.lemmas label="sub.two.lemmas"}

::: lemma
[]{#lem1 label="lem1"} Let $\operatorname{f}\colon \mathcal{U}\to\mathbb{C}$ be an analytic function satisfying the functional equation $$\label{per}
\operatorname{f}(z-a)\operatorname{f}(z+a)=\operatorname{f}(z)^2,$$ with some fixed $a\in\mathbb{C}\setminus\{0\}$, the domain $\mathcal{U}\subset\mathbb{C}$ being a translationally invariant open set, $\mathcal{U}=a+\mathcal{U}$, and $\mathcal{C}\subset \mathcal{U}$ an oriented path such that $\operatorname{f}(z)(\operatorname{f}(z)-\operatorname{f}(z+a))\ne0$ for all $z\in \mathcal{C}$. Then $$\label{residue1}
\int_{\mathcal{C}}\operatorname{f}(z)\operatorname{d}\!z = 
\left(\int_{\mathcal{C}}- \int_{a+\mathcal{C}}\right)
\frac{\operatorname{f}(z)}{1-\operatorname{f}(z+a)/\operatorname{f}(z)}
\operatorname{d}\!z.$$
:::

::: proof
*Proof.* We have $$\begin{gathered}
\left(\int_{\mathcal{C}}- \int_{a+\mathcal{C}}\right)
\frac{\operatorname{f}(z)}{1-\operatorname{f}(z+a)/
\operatorname{f}(z)}\operatorname{d}\!z 
=\int_{\mathcal{C}}\frac{\operatorname{f}(z)}{
1-\operatorname{f}(z+a)/\operatorname{f}(z)}\operatorname{d}\!z\\ 
-\int_{a+\mathcal{C}}\frac{\operatorname{f}(z)}{
1-\operatorname{f}(z)/\operatorname{f}(z-a)}\operatorname{d}\!z
=\int_{\mathcal{C}}\frac{\operatorname{f}(z)-\operatorname{f}(z+a)}{
1-\operatorname{f}(z+a)/\operatorname{f}(z)}\operatorname{d}\!z= 
\int_{\mathcal{C}}\operatorname{f}(z)\operatorname{d}\!z .
\end{gathered}$$ ◻
:::

Given a rational function $\operatorname{r}(z)\in\mathbb{C}(z)$, a nonzero complex number $q\in\mathbb{C}\setminus\{0\}$ and an integer $k$ we define $\operatorname{r}_k(z;q)\in\mathbb{C}(z)$, $k\in\mathbb{Z}$, by: $$\label{rk}
\frac{\operatorname{r}_{k+1}(z;q)}{\operatorname{r}_k(z;q)}
=\operatorname{r}(zq^k),\quad \operatorname{r}_0(z;q)=1.$$ Note that $$\operatorname{r}_{1}(z;q)=\operatorname{r}(z)$$ and $$\operatorname{r}_{k+l}(z;q)
=\operatorname{r}_k(zq^l;q)\operatorname{r}_l(z;q)
=\operatorname{r}_l(zq^k;q)\operatorname{r}_k(z;q)\,,$$ for all integers $k,l$. In particular, in the case of roots of unity this implies a quasi-periodicity property: $$\operatorname{r}_{k+N}(z;q)=\operatorname{r}_k(z;q)\operatorname{r}_N(z;q),
\quad \text{if}\quad q^N=1,$$ and the invariance property $$\operatorname{r}_{N}(zq;q)=\operatorname{r}_N(z;q),\quad \text{if}\quad q^N=1.$$

Let $(M,N)$ be an admissible pair, and recall $\mathsf{b}$ and $\mathsf{s}$ from Equation [\[eq.bs\]](#eq.bs){reference-type="eqref" reference="eq.bs"}. Choose two integers $P$ and $Q$ which satisfy the equation $MP+NQ=1$. Let $\operatorname{f}(z)$ be a meromorphic function and $\operatorname{g^\pm}(z)\in\mathbb{C}(z)$ two rational functions such that $$\frac{\operatorname{f}(z+\mathsf{b}^{\pm1}\mathsf{i})}{\operatorname{f}(z)}=
\operatorname{g^\pm}\!\left(e^{2\pi\mathsf{b}^{\pm1}z}\right).$$ Then, for $k \in \mathbbm Z$ we have $$\operatorname{g^\pm}_k\!\left(e^{2\pi\mathsf{b}^{\pm1}z};q_{\pm}\right)
=\frac{\operatorname{f}(z+\mathsf{b}^{\pm1}\mathsf{i}k)}{\operatorname{f}(z)}\,,$$ and, in particular, $$\operatorname{g^+}_{N}\!\left(e^{2\pi\mathsf{b}z};q_+\right)
= \frac{\operatorname{f}(z+\mathsf{b}\mathsf{i}N)}{\operatorname{f}(z)}
=\frac{\operatorname{f}(z+\mathsf{s}\mathsf{i})}{\operatorname{f}(z)}
=\frac{\operatorname{f}(z+\mathsf{b}^{-1}\mathsf{i}M)}{\operatorname{f}(z)}=
\operatorname{g^{--}}_{M}\!\left(e^{2\pi\mathsf{b}^{-1}z};q_-\right).$$ Define $$\begin{aligned}
\label{gx}\operatorname{g}\!\left(x\right) &= 
\operatorname{g^+}_{N}\!\left(x^{\frac1N};q_+\right)= 
\operatorname{g^{--}}_{M}\!\left(x^{\frac1M};q_-\right)
\\
\label{sxy}\operatorname{S}(x,y)&= 
\sum_{k=0}^{\mathsf{s}^2-1}\operatorname{g^+}_{kP}\!
\left(x;q_+\right)\operatorname{g^{--}}_{kQ}\!
\left(y;q_-\right)
\end{aligned}$$

::: lemma
[]{#lem.gg label="lem.gg"} (a) We have $\operatorname{g}\!\left(x\right) \in\mathbb{C}(x)$ and $\operatorname{S}(x,y) \in\mathbb{C}(x,y)$. (b) The function $\operatorname{S}(x,y)$ is independent of $P$ and $Q$ provided $x^N=y^M$.
:::

::: proof
*Proof.* Since $$\operatorname{g^+}_{N}\!\left(xq_+;q_+\right)
=\operatorname{g^+}_{N}\!\left(x;q_+\right),\qquad 
\operatorname{g^{--}}_{M}\!\left(xq_-;q_-\right)
=\operatorname{g^{--}}_{M}\!\left(x;q_-\right),$$ it follows that $\operatorname{g}\!\left(x\right) \in\mathbb{C}(x)$, and consequently, $\operatorname{S}(x,y) \in\mathbb{C}(x,y)$.

For (b), let $P', Q'$ be another pair satisfying the equation $MP'+NQ'=1$. Then there exists an integer $R$ such that $P'=P+RN$ and $Q'=Q-RM$. Denoting the function [\[sxy\]](#sxy){reference-type="eqref" reference="sxy"} with $P$ and $Q$ replaced by $P'$ and $Q'$ as $\operatorname{S}'(x,y)$, we have $$\begin{aligned}
 \operatorname{S}'(x,y) 
&=\sum_{k=0}^{\mathsf{s}^2-1}\operatorname{g^+}_{kP'}\!
\left(x;q_+\right)\operatorname{g^{--}}_{kQ'}\!
\left(y;q_-\right)
=\sum_{k=0}^{\mathsf{s}^2-1}\operatorname{g^+}_{kP+kRN}\!
\left(x;q_+\right)\operatorname{g^{--}}_{kQ-kRM}\!
\left(y;q_-\right)\\
&=\sum_{k=0}^{\mathsf{s}^2-1}\operatorname{g^+}_{kP}\!
\left(x;q_+\right) \operatorname{g^+}_{N}\!
\left(x;q_+\right)^{kR}\operatorname{g^{--}}_{kQ}\!
\left(y;q_-\right)\operatorname{g^{--}}_{M}\!
\left(y;q_-\right)^{-kR}\\
&=\sum_{k=0}^{\mathsf{s}^2-1}\operatorname{g^+}_{kP}\!
\left(x;q_+\right) \left(\frac{\operatorname{g^+}_{N}\!
\left(x;q_+\right)}{\operatorname{g^{--}}_{M}\!
\left(y;q_-\right)}\right)^{kR}\operatorname{g^{--}}_{kQ}\!
\left(y;q_-\right)
=\sum_{k=0}^{\mathsf{s}^2-1}\operatorname{g^+}_{kP}\!
\left(x;q_+\right)\operatorname{g^{--}}_{kQ}\!
\left(y;q_-\right) \\
&=\operatorname{S}(x,y)
\end{aligned}$$ where we used the second equality in [\[gx\]](#gx){reference-type="eqref" reference="gx"}. ◻
:::

For a complex number $x$, we denote $\mathcal{C}_x= x\mathsf{i}/\mathsf{s}+\mathbb{R}\subset \mathbbm C$.

::: lemma
[]{#lem.main label="lem.main"} Let $\operatorname{f}(z)$, $\operatorname{g}\!\left(z\right)$, $\operatorname{S}\!\left(x,y\right)$ be as above and $\lambda$ a real number in general position such that the form $\operatorname{f}(z)\operatorname{d}\!z$ is absolutely integrable along $\mathcal{C}_{\lambda}$, $$\label{cii}
\lim_{x\to\pm\infty}
\sup_{y\in \left[{\lambda\over \mathsf{s}},{\lambda\over \mathsf{s}}+\mathsf{s}\right]}|
\operatorname{f}(x+\mathsf{i}y)|=0,$$ and $$\label{ciii}
\operatorname{g}\!\left(0\right)\ne 1\ne \operatorname{g}\!\left(\infty\right).$$ Then the following equalities hold

$$\begin{aligned}
\label{eq.main}
\int_{\mathcal{C}_{\lambda}}\operatorname{f}(z)\operatorname{d}\!z &=
\left(\int_{\mathcal{C}_{\lambda}}-\int_{\mathcal{C}_{\lambda+1}}\right)
\frac{\operatorname{f}(z)\operatorname{S}\!
\left(e^{2\pi\mathsf{b}z},e^{2\pi\mathsf{b}^{-1}z}\right)}{1-\operatorname{g}\!
\left(e^{2\pi\mathsf{s}z}\right)}\operatorname{d}\!z \\ \notag
& =2\pi\mathsf{i}\sum_{0<\mathsf{s}\mathrm{Im}\alpha-\lambda<1}\operatorname{Res}_{z=\alpha}
\frac{\operatorname{f}(z)\operatorname{S}\!
\left(e^{2\pi\mathsf{b}z},e^{2\pi\mathsf{b}^{-1}z}\right)}{1-\operatorname{g}\!
\left(e^{2\pi\mathsf{s}z}\right)} \,.
\end{aligned}$$
:::

::: proof
*Proof.* Let us derive the first equality. We denote $$q_\pm= e^{2\pi\mathsf{i}\mathsf{b}^{\pm2}},$$ so that we have $$q_+=e^{2\pi\mathsf{i}\frac MN},\quad q_-=e^{2\pi\mathsf{i}\frac NM}.$$ We also have $$\operatorname{f}(z+k\mathsf{b}^{\pm1}\mathsf{i})=\operatorname{f}(z)
\operatorname{g^\pm}_{k}\!\left(e^{2\pi\mathsf{b}^{\pm1}z};q_\pm\right), 
\quad \forall k\in\mathbb{Z}.$$ In particular, $$\operatorname{f}(z+\mathsf{s}\mathsf{i})=\operatorname{f}(z+N\mathsf{b}\mathsf{i})=
\operatorname{f}(z+M\mathsf{b}^{-1}\mathsf{i})=
\operatorname{f}(z)\operatorname{g}\!\left(e^{2\pi\mathsf{s}z}\right).$$ The function $$\label{hf}
\operatorname{h}(z)= \operatorname{f}\!
\left(\frac z{2\pi\mathsf{s}}\right)$$ has the properties $$\label{g+g-}
\frac{\operatorname{h}(z+k2\pi \mathsf{i})}{\operatorname{h}(z)}=
\operatorname{g^+}_{Pk}\!\left(e^{z/N};q_+\right)
\operatorname{g^{--}}_{Qk}\!\left(e^{z/M};q_-\right),\quad \forall k\in\mathbb{Z}.$$ From equation [\[g+g-\]](#g+g-){reference-type="eqref" reference="g+g-"}, it follows that $$\label{Sh}
\sum_{k=0}^{\mathsf{s}^2-1}
\frac{\operatorname{h}(z+k2\pi\mathsf{i})}{\operatorname{h}(z)}=
\operatorname{S}\!\left(e^{z/N},e^{z/M}\right).$$ As $\lambda$ is generic, the contour $\mathcal{C}_\lambda$ satisfies the conditions of Lemma [\[lem1\]](#lem1){reference-type="ref" reference="lem1"} with $a=\mathsf{s}\mathsf{i}$. Thus, we write $$\begin{gathered}
\label{pro1}
\int_{\mathcal{C}_\lambda}\operatorname{f}(z)\operatorname{d}\!z=
\!\left(\int_{\mathcal{C}_\lambda}-\int_{\mathsf{s}\mathsf{i}+\mathcal{C}_\lambda}\right)
\frac{\operatorname{f}(z)}{1-\operatorname{g}\!\left(e^{2\pi\mathsf{s}z}\right)}
\operatorname{d}\!z \\
=\left(\int_{\mathcal{C}_{\lambda 2\pi\mathsf{s}}}
-\int_{\mathcal{C}_{(\lambda+\mathsf{s}^2) 2\pi\mathsf{s}}}\right)
\frac{\operatorname{h}(z)}{1-\operatorname{g}\!\left(e^{z}\right)}
\frac{\operatorname{d}\!z}{2\pi\mathsf{s}} \\
=\sum_{k=0}^{\mathsf{s}^2-1}\left(\int_{\mathcal{C}_{(\lambda +k)2\pi\mathsf{s}}}
-\int_{\mathcal{C}_{(\lambda+k+1) 2\pi\mathsf{s}}}\right)
\frac{\operatorname{h}(z)}{1-\operatorname{g}\!\left(e^{z}\right)}
\frac{\operatorname{d}\!z}{2\pi\mathsf{s}} \\
=\sum_{k=0}^{\mathsf{s}^2-1}\left(\int_{\mathcal{C}_{\lambda 2\pi\mathsf{s}}}
-\int_{\mathcal{C}_{(\lambda+1) 2\pi\mathsf{s}}}\right)
\frac{\operatorname{h}(z+k2\pi\mathsf{i})}{1-\operatorname{g}\!
\left(e^{z}\right)}\frac{\operatorname{d}\!z}{2\pi\mathsf{s}} \\
=\left(\int_{\mathcal{C}_{\lambda 2\pi\mathsf{s}}}-
\int_{\mathcal{C}_{(\lambda+1) 2\pi\mathsf{s}}}\right)
\frac{\operatorname{h}(z)\operatorname{S}\!
\left(e^{z/N},e^{z/M}\right)}{1-\operatorname{g}\!\left(e^{z}\right)}
\frac{\operatorname{d}\!z}{2\pi\mathsf{s}} \\
=\left(\int_{\mathcal{C}_{\lambda}}-\int_{\mathcal{C}_{\lambda+1}}\right)
\frac{\operatorname{f}(z)\operatorname{S}\!
\left(e^{2\pi\mathsf{b}z},e^{2\pi\mathsf{b}^{-1}z}\right)}{1-\operatorname{g}\!
\left(e^{2\pi\mathsf{s}z}\right)}\operatorname{d}\!z.
\end{gathered}$$

The second equality in Equation [\[eq.main\]](#eq.main){reference-type="eqref" reference="eq.main"} follows from the residue theorem. To justify its application note that $\mathcal{C}_{\lambda}-
\mathcal{C}_{\lambda+1}$ union two vertical segments is the boundary of a disk. Conditions [\[cii\]](#cii){reference-type="eqref" reference="cii"}, [\[ciii\]](#ciii){reference-type="eqref" reference="ciii"} imply that for sufficiently large negative or positive $x$ the integrand in last part of [\[pro1\]](#pro1){reference-type="eqref" reference="pro1"} is regular on the vertical segment $\mathcal C'= x+\mathsf{i}[\lambda,\lambda+1]/\mathsf{s}$ and the following estimate holds $$\begin{aligned}
\left|\int_{\mathcal C'}{\operatorname{f}(z)\operatorname{S}\!
\left(e^{2\pi\mathsf{b}z},e^{2\pi\mathsf{b}^{-1}z}\right)\over 1-\operatorname{g}\!
\left(e^{2\pi\mathsf{s}z}\right)}\operatorname{d}\!z\right|
 & \le
\sum_{k=0}^{\mathsf{s}^2-1}\int_{\lambda}^{\lambda+1}
\left |{\operatorname{f}\left(x+\mathsf{i}{y+k\over\mathsf{s}}\right)\over1-\operatorname{g}\!
\left(e^{2\pi(\mathsf{s}x+\mathsf{i}y)}\right)} \right |{\operatorname{d}\!y\over \mathsf{s}}\\
 & \le
{1\over\mathsf{s}}\sum_{k=0}^{\mathsf{s}^2-1}
\sup_{y\in [\lambda,\lambda+1]}\left |{\operatorname{f}\left(x+\mathsf{i}{y+k\over\mathsf{s}}\right)\over1-\operatorname{g}\!
\left(e^{2\pi(\mathsf{s}x+\mathsf{i}y)}\right)} \right |\\
& \le
{1\over\mathsf{s}}\sup_{y\in [\lambda,\lambda+1]}{1\over\left|1-\operatorname{g}\!
\left(e^{2\pi(\mathsf{s}x+\mathsf{i}y)}\right) \right |} 
\sum_{k=0}^{\mathsf{s}^2-1}
\sup_{t\in [\lambda,\lambda+1]}\left |\operatorname{f}\left(x+\mathsf{i}{t+k\over\mathsf{s}}\right)\right| \\
& \le\mathsf{s}{\sup_{z\in x+\mathsf{i}\left[{\lambda\over\mathsf{s}},{\lambda\over\mathsf{s}}+\mathsf{s}\right]}\left|\operatorname{f}(z)\right|\over\inf_{|w|=e^{2\pi\mathsf{s}x}}\left|1-\operatorname{g}\!
\left(w\right) \right |}
\xrightarrow{|x|\to\infty} 0
\end{aligned}$$ ◻
:::

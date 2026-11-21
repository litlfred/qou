---
doc_id: arxiv-math-9905032v2
doc_title: "Asymptotics of Plancherel measures for symmetric groups"
section_id: sec-016-42-proof-of-theorem
section_title: "Proof of Theorem"
section_number: 4.2
pages: 26-33
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.932
doc_brief: "Asymptotics of Plancherel measures for symmetric groups — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
[]{#s42 label="s42"}

Suppose we have a point process on $\mathbb{R}$ with determinantal correlation functions

$$\rho_k(x_1,\dots,x_k)=\det[K(x_i,x_j)]_{1\le i,j \le k}\,,$$

for some kernel $K(x,y)$. Let $I$ be a possibly infinite interval $I\subset\mathbb{R}$. By $[K]_I$ we denote the operator in $L^2(I,dx)$ obtained by restricting the kernel on $I\times I$. Assume $[K]_I$ is a trace class operator. Then the intersection of the random configuration $X$ with $I$ is finite almost surely and

$$\operatorname{Prob}\{|X\cap I|=N\}=\left.\frac{d^N}{dz^N}\det\Big(1-z[K]_I\Big)\right|_{z=1}\,.$$

In particular, the probability that $X\cap I$ is empty is equal to

$$\operatorname{Prob}\{X\cap I=\emptyset\}=\det\Big(1-[K]_I\Big)\,.$$

More generally, if $I_1,\dots,I_m$ is a finite family of pairwise nonintersecting intervals such that the operators $[K]_{I_1},\dots,[K]_{I_m}$ are trace class then

$$\begin{gathered}
\label{e41} 
\operatorname{Prob}\{|X\cap I_1|=N_1,\dots,|X\cap I_m|=N_m \}\\
=\left.\frac{\partial^{N_1+\dots+N_m}}
{\partial z_1^{N_1}\dots\partial z_m^{N_m}}
\det\Big(1-z_1[K]_{I_1}-\dots-z_m[K]_{I_m}\Big)\right|_{z_1=\dots=z_m=1}.
\end{gathered}$$

Here operators $\{[K]_{I_i}\}$ are considered to be acting in the same Hilbert space, for example, in $L^2(I_1\sqcup I_2,\sqcup\dots\sqcup I_m,dx)$.

In case of intersecting intervals $I_1,\dots,I_m$, the probabilities $$\operatorname{Prob}\{|X\cap I_1|=N_1,\dots,|X\cap I_m|=N_m \}$$ are finite linear combinations of expressions of the form [\[e41\]](#e41){reference-type="eqref" reference="e41"}. Therefore, in order to show the convergence in distribution of point processes with determinantal correlation functions, it suffices to show the convergence of expressions of the form [\[e41\]](#e41){reference-type="eqref" reference="e41"}.

The formula [\[e41\]](#e41){reference-type="eqref" reference="e41"} is discussed, for example, in [@TW2]. It remains valid for processes on a lattice such as $\mathbb{Z}$ in which case the kernel $K$ should be an operator on $\ell^2(\mathbb{Z})$.

As verified, for example, in Proposition [\[p58\]](#p58){reference-type="ref" reference="p58"} in the Appendix, the right-hand side of [\[e41\]](#e41){reference-type="eqref" reference="e41"} is continuous in each $[K]_{I_i}$ with respect to the trace norm. We shall show that after a suitable embedding of $\ell^2(\mathbb{Z})$ inside $L^2(\mathbb{R})$ the kernel $\mathsf{J}(x,y;\theta)$ converges to the Airy kernel $\mathsf{A}(x,y)$ as $\theta\to\infty$.

Namely, we shall consider a family of embeddings $\ell^2(\mathbb{Z})\to L^2(\mathbb{R})$, indexed by a positive number $r>0$, which are defined by

$$\label{e402}
\ell^2(\mathbb{Z})\owns\chi_k \mapsto r^{1/6} \, \chi_{\left[\frac{k-2r}{r^{1/3}},\frac{k+1-2r}{r^{1/3}}\right]}
\in L^2(\mathbb{R})\,,
\quad k\in\mathbb{Z}\,,$$

where $\chi_k\in\ell^2(\mathbb{Z})$ is the characteristic function of the point $k\in\mathbb{Z}$ and, similarly, the function on the right is the characteristic function of a segment of length $r^{-1/3}$. Observe that this embedding is isometric. Let $\mathsf{J}_r$ denote the kernel on $\mathbb{R}\times\mathbb{R}$ that is obtained from the kernel $\mathsf{J}(\,\cdot\,,\,\cdot\,,r^2)$ on $\mathbb{Z}\times\mathbb{Z}$ using the embedding [\[e402\]](#e402){reference-type="eqref" reference="e402"}. We shall establish the following

::: proposition
[]{#p44 label="p44"} We have

$$_{[a,\infty)}\to[\mathsf{A}]_{[a,\infty)}\,, \quad r\to\infty \,,$$

in the trace norm for all $a\in\mathbb{R}$ uniformly on compact sets in $a$.
:::

This proposition immediately implies Theorem [\[t4\]](#t4){reference-type="ref" reference="t4"} as follows

::: proof
*Proof of Theorem [\[t4\]](#t4){reference-type="ref" reference="t4"}.* Consider the left-hand side of [\[e401\]](#e401){reference-type="eqref" reference="e401"} and choose for each $a_i$ a pair of functions $k_i^-(r),k_i^+(r)\in\mathbb{Z}$ such that

$$\frac{k_i^-(r)-2r}{r^{1/3}}=a_i^-(r) \le a_i  \le  a_i^+(r) = \frac{k_i^+(r)-2r}{r^{1/3}}$$

and $a_i^-(r),a_i^+(r)\to a_i$ as $r\to \infty$. Then, on the one hand, the probability in left-hand side of [\[e401\]](#e401){reference-type="eqref" reference="e401"} lies between the corresponding probabilities for $a_i^-(r)$ and $a_i^+(r)$. On the other hand, the probabilities for $a_i^-(r)$ and $a_i^+(r)$ can be expressed in the form [\[e41\]](#e41){reference-type="eqref" reference="e41"} for the kernel $\mathsf{J}_r$ and by Propositions [\[p44\]](#p44){reference-type="ref" reference="p44"} and continuity of the Airy kernel they converge to one and same limit given by the Airy kernel as $r\to\infty$. ◻
:::

Now we get to the proofs of Propositions [\[p41\]](#p41){reference-type="ref" reference="p41"} and [\[p44\]](#p44){reference-type="ref" reference="p44"} which will require some computations. Recall that the Airy function can be expressed in terms of Bessel functions as follows

$$A(x)=\cases \frac 1\pi \sqrt{\frac x3}K_{\frac 13}\left(\frac 23 x^{\frac 
32}\right)\,,&x\ge 0\,,\\
\frac{\sqrt{|x|}} 3\left[J_{\frac 13}\left(\frac 23 |x|^{\frac 
32}\right)+J_{-\frac 13}\left(\frac 23 |x|^{\frac 32}\right)\right]\,,&x\le 0\,,
\endcases$$

see Section 6.4 in [@W]. Also recall that

$$\label{e42} 
A(x) \sim \frac1{2 x^{1/4} \sqrt{\pi}}\, e^{-\frac32 x^{3/2}}\,, \quad x\to+\infty \,,$$

see, for example, the formula 7.23 (1) in [@W].

::: lemma
[]{#l45 label="l45"} For any $x\in\mathbb{R}$ we have

$$\label{e43}
\left|r^{\frac 13}J_{2r+xr^{\frac 13}}(2r)- A(x)\right|= O(r^{-\frac 13})\,, \quad r\to\infty\,,$$

moreover, the constant in $O(r^{-\frac 13})$ is uniform in $x$ on compact subsets of $\mathbb{R}$.
:::

::: proof
*Proof.* Assume first that $x\ge 0$. We denote

$$\nu=2r+xr^{\frac 13},\quad \alpha=\operatorname{arccosh}\left(1+xr^{-\frac 
23}/2\right)\ge 0.$$

It will be convenient to use the following notation

$$P=\nu(\tanh\alpha-\alpha),\quad
Q=\frac \nu3 \tanh^3\alpha.$$

The formula 8.43(4) in [@W] reads

$$\label{e44} 
J_{\nu}(2r)=\frac {\tanh\alpha}{\pi\sqrt{3}}e^{P+Q}K_{\frac 
13}\left(Q\right)+\frac{3\gamma_1}{\nu}\,e^{P}$$

where $|\gamma_1|<1$. We have the following estimates as $r\to+\infty$

$$\begin{aligned}
&\alpha=x^{\frac 12}r^{-\frac 13}+O(r^{-1}),\\
&\tanh\alpha=\alpha+O(\alpha^3)=x^{\frac 12}r^{-\frac 13}+O(r^{-1}),\\
&P+Q=\nu\cdot O(\alpha^5)=O(r^{-\frac 23}),\quad
e^{P+Q}=1+O(r^{-\frac 23}),\\
&Q=\frac 13\,\left(2r+xr^{\frac 13}\right)\left(x^{\frac 32}r^{- 1}+O(r^{-\frac 
43})\right)=\frac{2x^{\frac 32}}3+O(r^{-\frac 13}),\\
&K_{\frac 13}\left(Q\right)=K_{\frac 13}\left(\frac {2x^{\frac 
32}}{3}\right)+O(r^{-\frac 13}),\\
&P\le 0,\quad\frac{3\gamma_1}{\nu}\,e^{P}=O(r^{-1}).
\end{aligned}$$

Substituting this into [\[e44\]](#e44){reference-type="eqref" reference="e44"}, we obtain the claim [\[e43\]](#e43){reference-type="eqref" reference="e43"} for $x\ge 0$.

Assume now that $x\le 0$. Denote

$$\nu=2r+xr^{\frac 13},\quad \beta=\operatorname{arccos}\left(1+xr^{-\frac 
23}/2\right)\ge 0,\quad y=|x|.$$

Introduce the notation

$$\widetilde P=\nu(\tan\beta-\beta),\quad
\widetilde Q=\frac \nu 3\tan^3\beta\,.$$

The formula 8.43 (5) in [@W] reads

$$\begin{gathered}
\label{e45}
J_{\nu}(r)=\frac 13 \tan \beta\cos\left(\widetilde P-\widetilde Q\right)\left[J_{-\frac 
13}\left(\widetilde Q\right)+J_{\frac 13}\left(\widetilde Q\right)\right]\\
+\frac 1{\sqrt{3}} \tan \beta\sin\left(\widetilde P-\widetilde Q\right)\left[J_{-\frac 
13}\left(\widetilde Q\right)-J_{\frac 13}\left(\widetilde
Q\right)\right]+\frac{24\gamma_2}{\nu}
\end{gathered}$$

where $|\gamma_2|<1$. Again we have the estimates as $r\to+\infty$

$$\begin{aligned}
&\beta=y^{\frac 12}r^{-\frac 13}+O(r^{-1}),\\
&\tan\beta=\beta+O(\beta^3)=y^{\frac 12}r^{-\frac 13}+O(r^{-1}),\\
&\widetilde P-\widetilde Q=\nu\cdot O(\beta^5)=O(r^{-\frac 23}),\\
&\cos\left(\widetilde P-\widetilde Q\right)=1+O(r^{-\frac 43}),\quad
\sin\left(\widetilde P-\widetilde Q\right)=O(r^{-\frac 23}),\\
&\widetilde Q=\frac 13\left(2r-yr^{\frac 13}\right)\left(y^{\frac 32}r^{- 1}+O(r^{-\frac 
43})\right)=\frac{2y^{\frac 32}}3+O(r^{-\frac 13}),\\
&J_{\pm\frac 13}\left(\widetilde Q\right)=J_{\pm\frac 13}\left(\frac {2y^{\frac 
32}}{3}\right)+O(r^{-\frac 13}).
\end{aligned}$$

These estimates after substituting into [\[e45\]](#e45){reference-type="eqref" reference="e45"} produce [\[e43\]](#e43){reference-type="eqref" reference="e43"} for $x\le 0$. ◻
:::

::: lemma
[]{#l46 label="l46"} There exist $C_1,C_2,C_3,\varepsilon>0$ such that for any $A>0$ and $s>0$ we have

$$\begin{aligned}
{2}
\left|J_{r+Ar^{\frac 13}+s}(r)\right|&\le
C_1\,{r^{-\frac13}}{\exp\left(-C_2\left(A^{\frac 32}+sA^{\frac
12}r^{-\frac 13}\right)\right)},\quad &s\le \varepsilon r \,, \label{e46a} \\
\left|J_{r+Ar^{\frac 13}+s}(r)\right|&\le
\exp\left(-C_3(r+s)\right), \quad &s\ge \varepsilon r\,, \label{e46b}
\end{aligned}$$

for all $r\gg 0$.
:::

::: proof
*Proof.* First suppose that $s\le\varepsilon r$. Set $\nu=r+Ar^{\frac 13}+s$. We shall use [\[e44\]](#e44){reference-type="eqref" reference="e44"} with $\alpha=\operatorname{arccosh}(\nu/r)$. Provided $\varepsilon$ is chosen small enough and $r$ is sufficiently large, $\alpha$ will be close to $0$ and we will be able to use Taylor expansions. For $r\gg 0$ we have

$$\alpha=\operatorname{arccosh}(1+Ar^{-\frac 23}+sr^{-1})\ge
\operatorname{const}\,(Ar^{-\frac 23}+sr^{-1})^{\frac 12} \,,$$

and, similarly,

$$-P=\nu(\alpha-\tanh\alpha)\ge \operatorname{const}\,(A+sr^{-\frac 13})^{\frac 32}\,.$$

Since the function $x^{\frac 32}$ is concave, we have

$$-P\ge \operatorname{const}\,(A^{\frac 32}+sA^{\frac 12}r^{-\frac 13})\,.$$

The constant here is strictly positive.

Since $K_{\frac 13}(x)\le \operatorname{const}\, x^{-\frac 12} e^{-x}$ (see, for example, the formula 7.23 (1) in [@W]) we obtain

$$\begin{gathered}
\tanh\alpha \,e^{P+Q}K_{\frac 13}\left(Q\right)\le \operatorname{const}\, 
\frac{e^{P}}{\sqrt{\nu\tanh\alpha}}\\ \le \frac{\operatorname{const}}  {r^{\frac 
13}}
\exp\left(-\operatorname{const}\,\left(A^{\frac 32}+sA^{\frac 12}r^{-\frac 13}\right)\right)\,,
\end{gathered}$$

where we used that $\tanh\alpha\ge \operatorname{const}\, r^{-\frac 13}$. Finally, we note that

$$\frac {e^P}{\nu}\le \frac1r\, \exp\left({-\operatorname{const}\,\left(A^{\frac 32}+sA^{\frac 
12}r^{-\frac 13}\right)}\right),$$

and this completes the proof of [\[e46a\]](#e46a){reference-type="eqref" reference="e46a"}.

The estimate [\[e46b\]](#e46b){reference-type="eqref" reference="e46b"} follows directly from the formulas 8.5 (9), (4), (5) in [@W]. ◻
:::

::: lemma
[]{#l47 label="l47"} For any $\delta>0$ there exists such $M>0$ that for all $x,y>M$ and large enough $r$

$$\left|\mathsf{J}\left(2r+xr^{\frac 13},2r+yr^{\frac 13}, {r^2}\right)\right|<\delta 
r^{-\frac 13}.$$
:::

::: proof
*Proof.* From [\[e214\]](#e214){reference-type="eqref" reference="e214"} we have

$$\label{e47}
\mathsf{J}\left(2r+xr^{\frac 13},2r+yr^{\frac 13}, {r^2} \right)=\sum_{s=1}^\infty 
J_{2r+xr^{\frac 13}+s}(2r)\,J_{2r+yr^{\frac 13}+s}(2r).$$

Let us split the sum in [\[e47\]](#e47){reference-type="eqref" reference="e47"} into two parts

$${\sum}_1=\sum_{l\le \varepsilon r}\,, \quad  
{\sum}_2=\sum_{l> \varepsilon r}\,,$$

that is, one sum for $l\le\varepsilon r$ and the other for $l> \varepsilon r$, and apply Lemma [\[l46\]](#l46){reference-type="ref" reference="l46"} to these two sums. Note that $2r$ here corresponds to $r$ in Lemma [\[l46\]](#l46){reference-type="ref" reference="l46"}; this produces factors of $2^{\frac 13}$ and does not affect the estimate.

Let the $c_i$'s stand for some positive constants not depending on $M$. From [\[e46a\]](#e46a){reference-type="eqref" reference="e46a"} we obtain the following estimate for the first sum $${\sum}_1 \le  c_1\, r^{-\frac 23}\,
\exp\left(-c_2\,M^{\frac 32}\right) \, \sum_{s=1}^{[\varepsilon r]} q^s$$ where $$q=\exp\left(-c_2M^{\frac 12}r^{-\frac 13}\right)\,, \quad 0<q<1\,.$$ Therefore, $${\sum}_1 \le \frac{c_1\, r^{-\frac 23}\,
\exp\left(-c_2\,M^{\frac 32}\right) }{1-q} \le 
r^{-\frac 13}\cdot c_3\exp(-c_2M^{\frac 32})M^{-\frac 12} \,.$$ We can choose $M$ so that $c_3\exp(-c_2M^{\frac 32})M^{-\frac 12}<\delta/2$.

For the second sum we use [\[e46b\]](#e46b){reference-type="eqref" reference="e46b"} and obtain

$${\sum}_2 \le \sum_{s\ge \varepsilon r} \exp(-c_4 (r+s))\le  c_5\exp(-c_4r).$$

Clearly, this is less than $\delta r^{-\frac 13}/2$ for $r\gg0$. ◻
:::

::: proof
*Proof of Proposition [\[p41\]](#p41){reference-type="ref" reference="p41"}.* As shown in [@CL; @TW], the Airy kernel has the following integral representation

$$\label{e48}
\mathsf{A}(x,y)=\int_{0}^\infty A(x+t)A(y+t)dt.$$

The formula [\[e47\]](#e47){reference-type="eqref" reference="e47"} implies that for any integer $N>0$

$$\begin{gathered}
\label{e49}
\mathsf{J}\left(2r+xr^{\frac 13},2r+yr^{\frac 13},{r^2} \right)=
\sum_{s=1}^N J_{2r+xr^{\frac 13}+s}(2r)\,J_{2r+yr^{\frac 13}+s}(2r)\\ 
+\mathsf{J}\left(2r+xr^{\frac 13}+N,2r+yr^{\frac 13}+N,{r^2} \right)\,.
\end{gathered}$$

Let us fix $\delta>0$ and pick $M>0$ according to Lemma [\[l47\]](#l47){reference-type="ref" reference="l47"}. Since, by assumption, $x$ and $y$ lie in compact set of $\mathbb{R}$, we can fix $m$ such that $x,y \ge m$. Set $$N=[(M-m+1)\, r^\frac13] \,.$$ Then the inequalities

$$x+Nr^{-\frac 13}>M,\quad y+Nr^{-\frac 13}>M$$

are satisfied for all $x,y$ in our compact set and Lemma [\[l45\]](#l45){reference-type="ref" reference="l45"} applies to the sum in [\[e49\]](#e49){reference-type="eqref" reference="e49"}. We obtain

$$\begin{gathered}
\left|r^{\frac 23}\sum_{s=1}^{N} J_{2r+xr^{\frac 13}+s}(2r)\,J_{2r+yr^{\frac 
13}+s}(2r)-\right.\\
\left. \sum_{s=1}^{N}
A(x+sr^{-\frac 13})A(y+sr^{-\frac 13})\right|=O(1)
\end{gathered}$$

because the number of summands is $N=O(r^{\frac 13})$ and $A(x)$ is bounded on subsets of $\mathbb{R}$ which are bounded from below. Note that

$$r^{-\frac 13} \sum_{s=1}^{N}
A(x+sr^{-\frac 13})A(x+sr^{-\frac 13})$$

is a Riemann integral sum for the integral

$$\int\limits_{0}^{M-m+1} A(x+t)A(y+t)\,dt,$$

and it converges to this integral as $r\to+\infty$. Since the absolute value of the second term in the right-hand side of [\[e49\]](#e49){reference-type="eqref" reference="e49"} does not exceed $\delta r^{-\frac 13}$ by the choice of $N$, we get

$$\left|r^{\frac 13}\mathsf{J}\left(2r+xr^{\frac 13},2r+yr^{\frac 13},{r^2} 
\right)-\int\limits_{0}^{M-m+1} A(x+t)A(y+t)dt\right|\le \delta+o(1)$$

as $r\to+\infty$, and this estimate is uniform on compact sets. Now let $\delta\to 
0$ and $M\to+\infty$. By [\[e42\]](#e42){reference-type="eqref" reference="e42"} the integral [\[e48\]](#e48){reference-type="eqref" reference="e48"} converges uniformly in $x$ and $y$ on compact sets and we obtain the claim of the proposition. ◻
:::

::: proof
*Proof of Proposition [\[p44\]](#p44){reference-type="ref" reference="p44"}.* It is clear that Proposition [\[p41\]](#p41){reference-type="ref" reference="p41"} implies the convergence of $[\mathsf{J}_r]_a$ to $[\mathsf{A}]_a$ in the weak operator topology. Therefore, by Proposition [\[p56\]](#p56){reference-type="ref" reference="p56"}, it remains to prove that $\operatorname{tr}[\mathsf{J}_r]_a\to\operatorname{tr}[\mathsf{A}]_a$ as $r\to+\infty$. We have

$$\operatorname{tr}[\mathsf{J}_r]_a=\sum_{k=[2r+ar^{\frac13}]}^\infty\mathsf{J}(k,k;{r^2})+o(1)\,,$$

where the $o(1)$ correction comes from the fact that $a$ may not be a number of the form $\frac{k-2r}{r^{1/3}}$, $k\in\mathbb{Z}$. By [\[e47\]](#e47){reference-type="eqref" reference="e47"} we have

$$\label{e403}
\sum_{k=[2r+ar^{\frac13}]}^\infty\mathsf{J}(k,k;{r^2})
=\sum_{l=1}^\infty l\left(J_{[2r+ar^{\frac13}]+l}(2r)\right)^2 \,.$$

Similarly,

$$\label{e404}
\operatorname{tr}[\mathsf{A}]_a=\int_a^{\infty}\mathsf{A}(s,s)ds=\int_0^\infty t(A(a+t))^2dt\,.$$

Since we already established the uniform convergence of kernels on compact sets, it is enough to show that the both [\[e403\]](#e403){reference-type="eqref" reference="e403"} and [\[e404\]](#e404){reference-type="eqref" reference="e404"} go to zero as $a\to+\infty$ and $r\to+\infty$. For the Airy kernel this is clear from [\[e42\]](#e42){reference-type="eqref" reference="e42"}. For the kernel $\mathsf{J}_r$ it is equivalent to the following statement: for any $\delta>0$ there exists $M_0>0$ such that for all $M>M_0$ and large enough $r$ we have

$$\label{e410}
\left|\sum_{l=1}^\infty l \, J_{2r+Mr^{\frac 13}+l}^2(2r)\right|<\delta \,.$$

We shall employ Lemma [\[l46\]](#l46){reference-type="ref" reference="l46"} for $A=M$. Again, we split the sum in [\[e410\]](#e410){reference-type="eqref" reference="e410"} in two parts

$${\sum}_1=\sum_{l\le \varepsilon r}\,, \quad  
{\sum}_2=\sum_{l> \varepsilon r}\,.$$

For the first sum Lemma [\[l46\]](#l46){reference-type="ref" reference="l46"} gives

$${\sum}_1\le 
c_1r^{-\frac 23}\exp\left(-c_2M^{\frac 32}\right)\sum_{l\le [\varepsilon 
r]}l\, q^l\,,$$

where

$$q=\exp\left(-c_2M^{\frac 12}r^{-\frac 13}\right)\,, \quad 0<q<1\,,$$

and the $c_i$'s are some positive constants that do not depend on $M$. Since $\sum l\, q^l = q (1-q)^{-2}$ we obtain

$${\sum}_1 \le 
c_1r^{-\frac 23}\exp\left(-c_2M^{\frac 32}\right) \, \frac{q}{(1-q)^2} \le
c_3\frac{\exp\left(-c_2M^{\frac 32}\right)}{M} \,.$$

This can be made arbitrarily small by taking $M$ sufficiently large.

For the other part of the sum we have the estimate

$${\sum}_2 \le
\sum_{l> \varepsilon r}l \exp(-c_4(r+l))$$

which, evidently, goes to zero as $r\to+\infty$. ◻
:::

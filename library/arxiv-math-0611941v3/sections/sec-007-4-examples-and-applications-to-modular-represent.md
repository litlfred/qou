---
doc_id: arxiv-math-0611941v3
doc_title: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR"
section_id: sec-007-4-examples-and-applications-to-modular-represent
section_title: "Examples and applications to modular representations"
section_number: 4
pages: 11-15
source_pdf: 0611941v3.pdf
source_sha256: bf6f2d55c7adee51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.782
latex_coverage_ratio: 0.984
doc_brief: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR — Let H be the one-parameter Hecke algebra associated to a ﬁnite Weyl group W, deﬁned over a ground ring in which “bad” primes for W are invertible."
---
[]{#secApp label="secApp"}

Throughout this section, we assume that Lusztig's conjectures on Hecke algebras with unequal parameters hold; see §[\[sub24\]](#sub24){reference-type="ref" reference="sub24"}. (Recall that this is the case, for example, if the weight function $L$ is a positive multiple of the length function.) We now discuss examples and applications of Theorem [\[mainthm\]](#mainthm){reference-type="ref" reference="mainthm"}.

::: example
[]{#expdim1 label="expdim1"} Assume that $L(s)>0$ for all $s \in S$ and that $\lambda \in \Lambda$ is such that $\dim E^\lambda=d_\lambda=1$. Then there exists a group homomorphism $\eta \colon W \rightarrow\{\pm 1\}$ and a weight function $m \colon W \rightarrow {\mathbb{Z}}$ such that $T_w$ acts on $E_v^\lambda$ via the $A$-algebra homomorphism $$\mu^\lambda\colon{\mathcal{H}}\rightarrow A,\qquad T_w\mapsto\eta(w)v^{m(w)}.$$ By [@Lusztig03 Prop. 20.6], the corresponding representation of $J$ is given by $$t_w \mapsto \left\{\begin{array}{cl}   (-1)^{l(w)}\,\hat{n}_w
\hat{n}_{w^{-1}}\, \eta(w) & \qquad \mbox{if ${\mathbf{a}}_\lambda+m(w)=0$},\\ 
0 & \qquad \mbox{otherwise}.  \end{array}\right.$$ (Note that a factor $\hat{n}_w\hat{n}_{w^{-1}}$ should be inserted into the formula in [@Lusztig03 20.6].) Clearly, we can take $B^\lambda=(1)$ in this case. Hence, the unique element of the cellular basis corresponding to $\lambda$ is given by $$C_{1,1}^\lambda=\sum_{\genfrac{}{}{0pt}{}{w \in W}{{\mathbf{a}}_\lambda+m(w)=0}} 
(-1)^{l(w)}\,\eta(w)\, c_w^\dagger.$$ For example, if $E^\lambda$ is the unit representation, we have $\eta(w)=1$ and $m(w)=L(w)$ for all $w \in W$; furthermore, ${\mathbf{a}}_\lambda=0$ and so $C_{1,1}^\lambda=c_1^\dagger$ (since $L(w)>0$ for all $w\neq 1$).

If $E^\lambda$ is the sign representation, we have $\eta(w)=(-1)^{l(w)}$ and $m(w)=-L(w)$ for all $w \in W$. Furthermore, ${\mathbf{a}}_\lambda=L(w_0)$ where $w_0\in W$ is the longest element; see [@Lusztig03 20.18]. Since $L(w)<L(w_0)$ for all $w\neq w_0$, we obtain $C_{1,1}^\lambda=
c_{w_0}^\dagger$ in this case.
:::

::: example
[]{#expirred label="expirred"} Assume that there are no $L$-bad primes for $W$, that is, we have $f_\lambda=1$ for all $\lambda \in \Lambda$. Then we claim that there are signs $\delta_w=\pm 1$ ($w\in W$) such that $$\{\delta_w\, c_w^\dagger\mid w \in W\} \qquad \mbox{is a cellular basis}.$$ This is seen as follows. Let $\Gamma$ be a left cell of $W$ and $[\Gamma]=\langle t_x \mid x \in \Gamma\rangle_{\mathbb{Q}}\subseteq J_{{\mathbb{Q}}}$. Then $[\Gamma]$ is a simple left ideal of $J_{\mathbb{Q}}$; see [@Lusztig03 Chap. 21] and [@myert05 Cor. 4.8]. Hence $[\Gamma]$ affords an irreducible representation of $J_{\mathbb{Q}}$, and all irreducible representations arise in this way. So, for any $\lambda \in \Lambda$, we can choose a left cell $\Gamma^\lambda$ such that $[\Gamma^\lambda]\cong 
E_\spadesuit^\lambda$. Let us write $$\Gamma^\lambda=\{x_{\mathfrak{s}}\mid {\mathfrak{s}}\in M(\lambda)\} \qquad \mbox{for
$\lambda \in \Lambda$}.$$ Then $\{t_{x_{\mathfrak{s}}} \mid {\mathfrak{s}}\in M(\lambda)\}$ is a basis of $[\Gamma^\lambda]$ and the corresponding matrix coefficients are $$\rho^\lambda_{{\mathfrak{s}}{\mathfrak{t}}}(t_w)=\gamma_{w,x_{\mathfrak{t}},x_{{\mathfrak{s}}}^{-1}}
\qquad \mbox{for $w \in W$ and ${\mathfrak{s}},{\mathfrak{t}}\in M(\lambda)$}.$$ By **(P7)** in [@Lusztig03 14.2] and [@Lusztig03 Prop. 13.9], we have $$\gamma_{w,x_{\mathfrak{t}},x_{{\mathfrak{s}}}^{-1}}=\gamma_{x_{{\mathfrak{t}}}^{-1},w^{-1},x_{\mathfrak{s}}}=
\gamma_{w^{-1}, x_{\mathfrak{s}},x_{{\mathfrak{t}}}^{-1}}.$$ This implies that $\rho^\lambda (t_{w^{-1}})=\rho^\lambda(t_w)^{\text{tr}}$ for all $w \in W$. Thus, if we take for $B^\lambda$ the identity matrix of size $d_\lambda$, then the conditions in Proposition [\[lem1\]](#lem1){reference-type="ref" reference="lem1"} are satisfied. Furthermore, for fixed ${\mathfrak{s}},{\mathfrak{t}}\in M(\lambda)$, the Schur relations now read: $$\sum_{y \in W} \bigl(\gamma_{y,x_{\mathfrak{t}},x_{\mathfrak{s}}^{-1}}\bigr)^2=\sum_{y \in W} 
\rho_{{\mathfrak{s}}{\mathfrak{t}}}^\lambda(t_y)\,\rho_{{\mathfrak{t}}{\mathfrak{s}}}^\lambda(t_{y^{-1}})=f_\lambda=1.$$ We deduce that there is a unique $w=w_\lambda({\mathfrak{s}},{\mathfrak{t}})\in W$ such that $\gamma_{w,x_{\mathfrak{t}},x_{\mathfrak{s}}^{-1}}\neq 0$; in fact, we have $\gamma_{w,x_{\mathfrak{t}},
x_{\mathfrak{s}}^{-1}}= \pm 1$. Now the formula in Theorem [\[mainthm\]](#mainthm){reference-type="ref" reference="mainthm"} reads $$\begin{aligned}
C_{{\mathfrak{s}},{\mathfrak{t}}}^\lambda&=\sum_{y \in W} \hat{n}_y\hat{n}_{y^{-1}}\,
\gamma_{y^{-1},x_{\mathfrak{s}},x_{\mathfrak{t}}^{-1}}\, c_y^\dagger= \sum_{y \in W} 
\hat{n}_y\hat{n}_{y^{-1}}\,\gamma_{y,x_{\mathfrak{t}},x_{\mathfrak{s}}^{-1}}\,
c_y^\dagger\\ &=\hat{n}_w\hat{n}_{w^{-1}}\,\gamma_{w,x_{\mathfrak{t}},x_{\mathfrak{s}}^{-1}}\, 
c_w^\dagger=\delta_w\, c_w^\dagger,
\end{aligned}$$ where $w=w_\lambda({\mathfrak{s}},{\mathfrak{t}})$ and $\delta_w=\pm 1$. Thus, $\{\delta_w\,c_w^\dagger \mid w \in W\}$ is a cellular basis, as claimed.

The above assumptions are satisfied for $W$ of type $A_n$ where $L$ is a positive multiple of the length function; see [@Lusztig03 22.4]. Thanks to a geometric interpretation of the basis $\{c_w\}$, we know that $h_{x,y,z}\in {{\mathbb{Z}}}_{\geqslant 0}[v,v^{-1}]$ for all $x,y,z\in W$; see [@Lusztig03 Chap. 15] and the references there. Hence we also have $\hat{n}_x\geqslant 0$ and $\gamma_{x,y,z}\geqslant 0$ for all $x,y,z\in W$. So, in this case, $\{c_w^\dagger\mid w\in W\}$ is a cellular basis of ${\mathcal{H}}$, as originally pointed out by Graham--Lehrer [@GrLe Example 1.2]. Note that another cellular structure in type $A_n$ was constructed by Murphy [@Mu1], [@Mu2], using purely combinatorial methods. The exact relation between the two cellular structures is determined in [@mymurph].
:::

::: example
[]{#expb2 label="expb2"} Let $W$ be the Weyl group of type $B_2$ where $S=\{s_1,s_2\}$ and $(s_1s_2)^4=1$. Let $L\colon W \rightarrow{\mathbb{Z}}$ be any weight function such that $L(s_i)>0$ for $i=1,2$. If $L(s_1)\neq
L(s_2)$, then there are no $L$-bad primes for $W$. Furthermore, by [@GeIa06], [@myert06], Lusztig's conjectures hold in this case. (More generally, they hold for a certain class of weight functions in type $B_n$ for any $n \geqslant 2$.) Hence, in this case, $\{\delta_w
c_w^\dagger \mid w \in W\}$ is a cellular basis by Example [\[expirred\]](#expirred){reference-type="ref" reference="expirred"}. By [@myert06 Cor. 6.4], we actually have $\delta_w=1$ for all $w\in W$.

Now assume that $L(s_1)=L(s_2)=1$ ("equal parameter case"). Then $2$ is the only bad prime. We have ${\operatorname{Irr}}(W)=\{{\bf 1},\varepsilon_1,\varepsilon_2,
\varepsilon,r\}$ where ${\bf 1}$ is the unit representation, $\varepsilon$ is the sign representation, $\varepsilon_1$, $\varepsilon_2$ have dimension one, and $r$ has dimension two. The ${\mathbf{a}}$-invariants are ${\mathbf{a}}_{\bf 1}=0$, ${\mathbf{a}}_{\varepsilon_1}={\mathbf{a}}_{\varepsilon_2}={\mathbf{a}}_r=1$ and ${\mathbf{a}}_{\varepsilon}=4$. A cellular basis as in Theorem [\[mainthm\]](#mainthm){reference-type="ref" reference="mainthm"} is given as follows: $$\begin{aligned}
{2}
C_{1,1}^{\bf 1}&=c_1^\dagger, \qquad\qquad &
C_{1,1}^r &= c_{s_1}^\dagger+c_{s_1s_2s_1}^\dagger,\\
C_{1,1}^\varepsilon&=c_{w_0}^\dagger, \qquad\qquad &
C_{1,2}^r &= -2c_{s_1s_2}^\dagger, \\ C_{1,1}^{\varepsilon_1}&=
c_{s_2}^\dagger-c_{s_2s_1s_2}^\dagger,\qquad\qquad &C_{2,1}^r &= 
-2c_{s_2s_1}^\dagger, \\ C_{1,1}^{\varepsilon_2}&=c_{s_1}^\dagger-
c_{s_1s_2s_1}^\dagger,\qquad\qquad &C_{2,2}^r &= 
2c_{s_2}^\dagger+2c_{s_2s_1s_2}^\dagger.
\end{aligned}$$ Indeed, by Example [\[expdim1\]](#expdim1){reference-type="ref" reference="expdim1"}, we already know that $c_1^\dagger$ and $c_{w_0}^\dagger$ belong to the cellular basis. Now consider the two further one-dimensional representations. We fix the notation such that $\varepsilon_1(T_{s_1})=\varepsilon_2(T_{s_2})=v$ and $\varepsilon_1
(T_{s_1})=\varepsilon_2(T_{s_2})=-v^{-1}$. Using the formula in Example [\[expdim1\]](#expdim1){reference-type="ref" reference="expdim1"}, we obtain the above expressions for $C_{1,1}^{\varepsilon_1}$ and $C_{1,1}^{\varepsilon_2}$. Finally, consider the two-dimensional representation $r$. We have to determine a corresponding representation of $J$ such that the conditions in Proposition [\[lem1\]](#lem1){reference-type="ref" reference="lem1"} hold. Now, the basis elements $\{c_w\}$ are explicitly determined in [@Lusztig03 Prop. 7.3]. From this, one easily deduces the left cells. They are given by $$\{1\},\quad\{s_1,s_2s_1,s_1s_2s_1\},\quad\{s_2,s_1s_2,s_2s_1s_2\},
\quad\{w_0=s_1s_2s_1s_2\};$$ see [@Lusztig03 8.7]. Furthermore, one finds the following relations in $J$. We have $t_1^2=t_1$ and $t_1t_x=0$ for $x\neq 1$; we have $t_{w_0}^2
=t_{w_0}$ and $t_{w_0}t_x=0$ for $x \neq w_0$. Furthermore, $$\begin{gathered}
t_{s_1}^2=t_{s_1},\qquad t_{s_1}t_{s_1s_2}=t_{s_1s_2},\qquad 
t_{s_1}t_{s_1s_2s_1}=t_{s_1s_2s_1},\\
t_{s_2}^2=t_{s_2},\qquad t_{s_2}t_{s_2s_1}=t_{s_2s_1},\qquad t_{s_2}
t_{s_2s_1s_2}= t_{s_2s_1s_2},\\ 
t_{s_1s_2}t_{s_2s_1}=t_{s_1}+ t_{s_1s_2s_1},\qquad t_{s_1s_2}
t_{s_2s_1s_2}=t_{s_1s_2},\\
t_{s_2s_1}t_{s_1s_2}=t_{s_2}+ t_{s_2s_1s_2},\qquad 
t_{s_2s_1}t_{s_1s_2s_1}=t_{s_2s_1},\\
t_{s_1s_2s_1}t_{s_1s_2s_1}=t_{s_1},\qquad t_{s_2s_1s_2}t_{s_2s_1s_2}=t_{s_2}.
\end{gathered}$$ All other products $t_xt_y$ are either zero or can be deduced from the above list using the formulas $\gamma_{x,y,z}=\gamma_{y^{-1},x^{-1},z^{-1}}$ (see [@Lusztig03 Prop. 13.9]) and $\gamma_{x,y,z}=\gamma_{y,z,x}$ (see **(P7)** in [@Lusztig03 14.2]). Note also that, by **(P8)** in [@Lusztig03 14.2], we have $\gamma_{x,y,z}=0$ unless $x \sim_{{\mathcal{L}}}
y^{-1}$, $y \sim_{{\mathcal{L}}} z^{-1}$ and $z \sim_{{\mathcal{L}}} x^{-1}$. Now one readily checks that the following assignments define an irreducible two-dimensional representation of $J_{\mathbb{Q}}$: $$\begin{gathered}
t_{1} \mapsto \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix},\quad
t_{s_1} \mapsto \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix},\quad
t_{s_2s_1} \mapsto \begin{bmatrix} 0 & 0 \\ -1 & 0 \end{bmatrix},\quad
t_{s_1s_2s_1} \mapsto \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix},\\
t_{s_2} \mapsto \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix},\quad
t_{s_1s_2} \mapsto \begin{bmatrix} 0 & -2 \\ 0 & 0 \end{bmatrix},\quad
t_{s_2s_1s_2} \mapsto \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix},\quad
t_{w_0} \mapsto \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}.
\end{gathered}$$ Finally, taking for $B^\lambda$ the diagonal matrix with diagonal entries $1$ and $2$, we see that all the conditions in Proposition [\[lem1\]](#lem1){reference-type="ref" reference="lem1"} are satisfied. This yields the expressions for the basis elements $C_{{\mathfrak{s}},{\mathfrak{t}}}^r$ where $1 \leqslant{\mathfrak{s}},{\mathfrak{t}}\leqslant 2$.
:::

::: example
[]{#expcanbas label="expcanbas"} Following Graham--Lehrer [@GrLe], we define *cell representations* of ${\mathcal{H}}$ as follows. Fix $\lambda \in \Lambda$ and let $W(\lambda)$ be a free $A$-module with basis $\{C_{\mathfrak{s}}\mid {\mathfrak{s}}\in M(\lambda)\}$. Then $W(\lambda)$ is an ${\mathcal{H}}$-module with action given by $$h.C_{\mathfrak{s}}=\sum_{{\mathfrak{s}}'\in M(\lambda)} r_h({\mathfrak{s}}',{\mathfrak{s}})\, C_{{\mathfrak{s}}'} \qquad 
\mbox{for $h \in {\mathcal{H}}$ and ${\mathfrak{s}}\in M(\lambda)$}.$$ There is a symmetric bilinear form $g^\lambda \colon W(\lambda) \times 
W(\lambda) \rightarrow A$ defined by $$g^\lambda(C_{\mathfrak{s}},C_{\mathfrak{t}})=r_h({\mathfrak{s}},{\mathfrak{s}}) \qquad \mbox{where ${\mathfrak{s}},{\mathfrak{t}}\in
M(\lambda)$ and $h=C_{{\mathfrak{s}}, {\mathfrak{t}}}^\lambda$};$$ see [@GrLe Def. 2.3]. We have $g^\lambda(h.C_{\mathfrak{s}},C_{\mathfrak{t}})=g^\lambda(C_{\mathfrak{s}},h^*.C_{\mathfrak{t}})$ for all ${\mathfrak{s}},{\mathfrak{t}}\in M(\lambda)$ and $h \in {\mathcal{H}}$; see [@GrLe Prop. 2.4]. Using the formula for $r_h({\mathfrak{s}}',{\mathfrak{s}})$ in the proof of Theorem [\[mainthm\]](#mainthm){reference-type="ref" reference="mainthm"}, and a computation analogous to that in the proof of [@Lusztig03 Prop. 20.6], it is straightforward to check that $$v^{{\mathbf{a}}_\lambda}\, g^\lambda(C_{\mathfrak{s}},C_{\mathfrak{t}})\equiv f_\lambda\,\beta_{{\mathfrak{s}}
{\mathfrak{t}}}^\lambda \quad \bmod vR[v].$$ In particular, we can see from this expression that the determinant of the Gram matrix of $g^\lambda$ is non-zero. (This fact also follows from the general theory of cellular algebras, since ${\mathcal{H}}_K$ is known to be split semisimple.)

Now let $K$ be the field of fractions of $A$; we write ${\mathcal{H}}_K=
K\otimes_A {\mathcal{H}}$ and $W_K(\lambda)=K\otimes_A W(\lambda)$. Since $g^\lambda$ induces a non-degenerate form on $W_K(\lambda)$ for each $\lambda \in \Lambda$, we have $${\operatorname{Irr}}({\mathcal{H}}_K)=\{W_K(\lambda) \mid \lambda \in \Lambda\}; \qquad
\mbox{see \protect{\cite[Theorem~3.8]{GrLe}}}.$$ In fact, by the formula for $r_h({\mathfrak{s}}',{\mathfrak{s}})$ in the proof of Theorem [\[mainthm\]](#mainthm){reference-type="ref" reference="mainthm"}, we see that the action of ${\mathcal{H}}$ on $W(\lambda)$ is obtained by pulling back the action of $J$ on $E^\lambda_\spadesuit$ via Lusztig's homomorphism $\phi \colon {\mathcal{H}}\rightarrow J_A$. This shows that $W_K(\lambda)\cong E_v^\lambda$; see [@Lusztig03 20.2, 20.3].

Now let $\theta \colon A \rightarrow k$ be any ring homomorphism where $k$ is a field. By extension of scalars, we obtain a $k$-algebra ${\mathcal{H}}_k=k 
\otimes_A {\mathcal{H}}$ and cell representations $W_k(\lambda)=k \otimes_A 
W(\lambda)$ ($\lambda \in \Lambda$), which may no longer be irreducible. Denoting by $g_k^\lambda$ the induced bilinear form on $W_k(\lambda)$, we set $L^\lambda=W_k(\lambda)/\mbox{rad}(g_k^\lambda)$. Then, by [@GrLe Theorem 3.4], each $L^\lambda$ is either $0$ or an absolutely irreducible representation of ${\mathcal{H}}_k$, and we have $${\operatorname{Irr}}({\mathcal{H}}_k)=\{L^\mu \mid \mu \in \Lambda^\circ\} \qquad \mbox{where}
\qquad \Lambda^\circ=\{\lambda \in \Lambda \mid L^\lambda \neq 0\}.$$ Denote by $[W_k(\lambda):L^\mu]$ the multiplicity of $L^\mu$ as a composition factor of $W_k(\lambda)$. Then $$\left\{\begin{array}{l} \quad [W_k(\mu):L^\mu]=1 \quad \mbox{for any
$\mu\in \Lambda^\circ$},\\[1mm] \quad [W_k(\lambda):L^\mu]=0 \quad 
\mbox{unless $\lambda \preceq \mu$ (i.e., $\lambda=\mu$ or ${\mathbf{a}}_\mu<
{\mathbf{a}}_\lambda$)}; \end{array}\right.  \tag{$\Delta$}$$ see [@GrLe Prop. 3.6]. Thus, the decomposition matrix $$D=\bigl([W_k(\lambda):L^\mu]\bigr)_{\lambda \in \Lambda,\mu \in 
\Lambda^\circ}$$ has a lower unitriangular shape, if the rows and columns are ordered according to increasing ${\mathbf{a}}$-value.

The relations ($\Delta$) show that the subset $\Lambda^\circ \subseteq
\Lambda$ defines a "canonical basic set" in the sense of [@mylaus Def. 4.13], which itself is an axiomatization of the results obtained earlier by Rouquier and the author [@mykl], [@GeRo2]. Note that the definition of "canonical basic sets" only requires the invariants ${\mathbf{a}}_\lambda$ (with respect to $L$) and the general set-up of Brauer's theory of *decomposition numbers* for associative algebras. Explicit descriptions of these "basic sets" are now known in all cases; see the survey [@mylaus] and the references there. In [@Jac2], [@GeJa], the existence of such basic sets for type $B_n$ and any $L$ (where $k$ has characteristic $0$) has been established *without* assuming Lusztig's conjectures on Hecke algebras with unequal parameters.
:::

::: example
[]{#expbn label="expbn"} Assume that $W$ is of type $B_n$ ($n\geqslant 2$) with diagram and weight function given by

::: center
::: picture
(250,30) ( 0, 10)$B_n$ ( 40, 10) ( 44, 7)(1,0)33 ( 44, 13)(1,0)33 ( 81, 10) ( 86, 10)(1,0)29 (120, 10) (125, 10)(1,0)20 (155, 7)$\cdot$ (165, 7)$\cdot$ (175, 7)$\cdot$ (185, 10)(1,0)20 (210, 10) ( 38, 22)$b$ ( 78, 22)$a$ (118, 22)$a$ (208, 22)$a$
:::
:::

where $a,b$ are non-negative integers. Then we have two cellular structures on ${\mathcal{H}}$: the one given by Theorem [\[mainthm\]](#mainthm){reference-type="ref" reference="mainthm"}, and the one given by Dipper--James--Murphy [@DJM3] (or, alternatively, by Graham--Lehrer [@GrLe §5]). In both cases, $\Lambda$ is the set of all pairs of partitions $(\lambda,\mu)$ such that $|\lambda|+|\mu|=n$. The partial order on $\Lambda$ that we use here is defined in terms of the ${\mathbf{a}}$-function; it heavily depends on the weight function $L$, i.e., on the integers $a$ and $b$. The partial order used by Dipper--James--Murphy (or Graham--Lehrer) is defined in purely combinatorial terms: it does not depend at all on the weight function $L$. Small examples show that the two partial orders indeed are different. Hence, in general, the cellular structure that we construct will be essentially different from the one constructed by Dipper--James--Murphy (or Graham--Lehrer). These differences can be seen explicitly in the descriptions of the sets $\Lambda^\circ \subseteq\Lambda$ parametrizing the irreducible representations of non-semisimple specialisations of ${\mathcal{H}}$, as discussed in [@GeJa]. By [@GeJa Theorem 2.8], the two parametrizations coincide if $b>(n-1)a>0$. Thus, one may expect that the two cellular structures are equivalent under this condition; see Iancu--Pallikaros [@IaPa] for a further discussion of this question.
:::

I wish to thank the referees for some useful comments and for pointing out the reference [@kor2] to me.

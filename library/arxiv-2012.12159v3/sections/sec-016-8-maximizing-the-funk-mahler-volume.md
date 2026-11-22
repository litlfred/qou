---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-016-8-maximizing-the-funk-mahler-volume
section_title: "Maximizing the Funk-Mahler volume"
section_number: 8
pages: 26-34
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.964
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
---
[]{#sec:inequalities label="sec:inequalities"}

Let us introduce for convenience $\rho=1-e^{-r}$, and the modified Funk-Mahler volumes $$\widetilde M_\rho(K,q):=r^nM_{r}(K,q)=\int_{z\in q+\rho (K-q)}|K^z|dz,\quad \widetilde M_\rho(K)=\inf_{q\in \mathop{\mathrm{int}}(K)}\widetilde M_\rho(K, q).$$

::: Lemma
Let $B\subset\mathbb{R}^n$ be an ellipsoid. Then $$\widetilde M_\rho(B)=n\omega_n^2\int_0^\rho\frac{t^{n-1}dt}{(1-t^2)^{\frac{n+1}{2}}}.$$
:::

By Lemmas [\[lem:mahler_convex\]](#lem:mahler_convex){reference-type="ref" reference="lem:mahler_convex"} and [\[lem:volume_ellipsoid\]](#lem:volume_ellipsoid){reference-type="ref" reference="lem:volume_ellipsoid"}, $$\widetilde M_\rho(B)=\widetilde M_\rho(B^n,0)=\int_{\rho B}|B^z|dz=\omega_n\int_{\rho B}\frac{dz}{(1-|z|^2)^{\frac{n+1}{2}}}=n\omega_n^2  \int_0^\rho\frac{t^{n-1}dt}{(1-t^2)^{\frac{n+1}{2}}}.$$

In light of the discussion in section [\[sec:every_scale\]](#sec:every_scale){reference-type="ref" reference="sec:every_scale"}, and inspired by the Blaschke-Santaló and the centro-affine isoperimetric inequalities, we propose a unified inequality containing both of the above as limiting cases.

::: Conjecture
[]{#conj:bodies label="conj:bodies"} Fix any $0\leq \rho<1$, and let $K\in\mathcal K(\mathbb{R}^n)$ have $0$ as its centroid.

1.  $\widetilde M_\rho(K,0)\leq \widetilde M_\rho(B^n)$.

2.  If $\widetilde M_\rho(K,0)= \widetilde M_\rho(B^n)$ then $K$ is an ellipsoid.
:::

This is not to say that $\widetilde M_\rho(K)=\widetilde M_\rho(K,0)$: as $\rho\to 0$, $\widetilde M_\rho(K,q)$ attains its minimum close to the Santaló point of $K$, which generally differs from the centroid.

We will prove the conjecture in the restricted class of unconditional convex bodies. To this end, we must expand our discussion to include log-concave functions. We write $f_q(\bullet)=f(q+\bullet)$.

::: Definition
For $f:\mathbb{R}^n\to \mathbb{R}_+$ a Borel function, put $\phi(x)=-\log f(x):\mathbb{R}^n\to \mathbb{R}\cup\{+\infty\}$. Define for $\rho\in\mathbb C$ the Funk-Mahler volumes around $0$ $$\begin{aligned}
\widetilde M_\rho(f,0)&:=\frac{1}{n!}\displaystyle\int_{z\in\mathbb{R}^n} e^{-\phi(\frac{z}{\rho})}\displaystyle\int_{\xi\in \mathbb{R}^n} e^{-\mathcal L\phi_z(\xi)} d\xi dz\\&=\frac{1}{n!}\rho^n\displaystyle\int_{\mathbb{R}^n\times \mathbb{R}^n} e^{-\phi(x)-\mathcal L \phi (\xi)+\rho\langle x,\xi\rangle}dxd\xi,
\end{aligned}$$ whenever the integral converges. Define also $$\widetilde M_\rho(f, q):=\widetilde M_\rho(f_q,0), \quad \widetilde M_\rho(f):=\inf_{q\in \mathbb{R}^n} \widetilde M_\rho(f, q).$$
:::

As $\rho\to 0$, $$\widetilde M_\rho(f,0)\sim \frac 1{n!} \rho^n \int_{\mathbb{R}^n\times \mathbb{R}^n} e^{-\phi(z)-\mathcal L \phi(\xi)}dxd\xi,$$ which is the functional Mahler product.

::: Lemma
[]{#lem:functional_invariance label="lem:functional_invariance"} It holds that $\widetilde M_\rho(f,0)=\widetilde M_\rho(\lambda f\circ A,0)$ for any $\lambda> 0$ and $A\in\mathop{\mathrm{GL}}_n(\mathbb{R})$. Furthermore, $\widetilde M_\rho(f,q)$ is a convex function of $q$, and strictly convex where finite.
:::

The first statement is immediate from definition by the $\mathop{\mathrm{GL}}$-equivariance of the Legendre transform, and since $\mathcal L(\phi+c)=\mathcal L\phi -c$.

For the second, observe that $$\widetilde M_\rho(f,q)=\frac{1}{n!}\int_{\mathbb{R}^n\times\mathbb{R}^n} e^{-\phi(\frac{w}{\rho})+\langle \xi,w\rangle-\mathcal L\phi(\xi)}e^{(1-\rho)\langle \xi,q\rangle}dwd\xi,$$ and note that $t\mapsto e^{(1-\rho)t}$ is strictly convex.

The functional Funk-Mahler volumes generalize those previously introduced for convex bodies, as follows.

::: Lemma
[]{#lem:body_vs_function label="lem:body_vs_function"} $\widetilde M_\rho(\mathbbm 1_K, 0)=\widetilde M_\rho(K ,0)$.
:::

Recall that $\mathcal L(-\log \mathbbm 1_K)(\xi)=h_K(\xi)=\|\xi\|_{K^o}$. Thus $$\widetilde M_\rho(\mathbbm 1_K, 0)=\frac{1}{n!}\int_{\rho K\times\mathbb{R}^n}e^{-\|\xi\|_{K^z}}dzd\xi=\frac{1}{n!}\int_{\rho K}dz \int_0^\infty r^{n-1}e^{-r}dr\int_{\partial K^z}d\mu_{K^z},$$ where $d\xi=r^{n-1}drd\mu_{K^z}$. Thus $$\widetilde M_\rho(\mathbbm 1_K, 0)= \frac{1}{n!}(n-1)!n\int_{\rho K} |K^z|dz=\widetilde M_\rho(K, 0). \qedhere$$

Using this representation, let us exhibit a curious property of the Funk-Mahler volume of a convex body, which at present we only formally establish for zonoids.

::: Proposition
[]{#prop:to_the_infinity_and_beyond label="prop:to_the_infinity_and_beyond"} Assume $0\in \mathop{\mathrm{int}}(K)$. There is then a continuous extension of $\widetilde M_\rho(K, 0)$ to $\rho\in[0,1)\times i\mathbb{R}$, which is analytic in $(0,1)\times i\mathbb{R}$.\
Furthermore if $K$ is a zonoid, then $$\lim_{t\to \pm\infty} \widetilde M_{it}(K,0)=i^n\frac{(2\pi)^n}{n!}.$$
:::

For the first statement, put $\rho=s+it$, write $$\widetilde M_{\rho}(K,0)= \widetilde M_{\rho}(\mathbbm 1_K,0)=\frac{(s+it)^n}{n!}\int_{K\times\mathbb{R}^n} e^{-h_K(\xi)+s\langle x,\xi\rangle +it \langle x,\xi\rangle}dxd\xi,$$ and note that

$$\frac{1}{n!}\int_{K\times\mathbb{R}^n} e^{-h_K(\xi)+s\langle x,\xi\rangle }dxd\xi =\frac{1}{s^n}\widetilde M_s(K,0)<\infty$$ for $0\leq s<1$.

For the second statement, let $\mathcal F(f)(y)=\int_{\mathbb{R}^n}f(x)e^{-i\langle x, y\rangle }dx$ be the Fourier transform. Write $$\begin{aligned}
\widetilde M_{it}(K,0)&=\frac{i^n}{n!} t^n\int_{\mathbb{R}^n\times\mathbb{R}^n}\mathbbm 1_K(x) e^{-h_K(\xi)}e^{it\langle x, \xi\rangle}dxd\xi\\&=\frac{i^n}{n!}\int_{\mathbb{R}^n} \mathbbm 1_K(\frac{x}{t})\mathcal F(e^{-h_K})(-x)dx\\&=\frac{i^n}{n!}\int_{\mathbb{R}^n}e^{-h_K(\xi)}\int_{tK}e^{i\langle x,\xi\rangle} dxd\xi ,
\end{aligned}$$ and note that $\mathcal F(e^{-h_K})\in L^1(\mathbb{R}^n)$ when $K$ is a zonoid. Thus as $t\to\pm \infty$, $$\widetilde M_{it}(K,0)\to \frac{i^n}{n!}\int_{\mathbb{R}^n}\mathcal F(e^{-h_K})=\frac{i^n}{n!}(2\pi)^ne^{-h_K(0)}=i^n\frac{(2\pi)^n}{n!}.$$

Motivated by Conjecture [\[conj:bodies\]](#conj:bodies){reference-type="ref" reference="conj:bodies"}, and inspired by the results of [@lehec], we boldly put forward the following

::: Conjecture
[]{#conj:functional_general label="conj:functional_general"} Consider two Borel functions $\phi,\psi:\mathbb{R}^n\to \mathbb{R}\cup\{+\infty\}$ such that for all $x,\xi\in\mathbb{R}^n$ one has $\phi(x)+\psi(\xi)\geq \langle x, \xi\rangle$. Assume also $\int xe^{-\phi(x)}dx=0$. Then for all $0\leq \rho<1$, $$\label{eq:general_inequality} \int_{\mathbb{R}^n\times\mathbb{R}^n}e^{-\phi(x)-\psi(\xi)+\rho\langle x,\xi\rangle}dxd\xi\leq (2\pi)^n(1-\rho^2)^{-\frac n 2}.$$ Equality is attained uniquely, up to equality a.e., by the pairs of functions $$\label{eq:pairs}\phi(x)=\frac 12 \langle Ax, x\rangle +c, \quad \psi(\xi)=\mathcal L\phi(\xi)=\frac 12 \langle A^{-1}x, x\rangle -c,$$ for some $A>0$ and $c\in\mathbb{R}$.
:::

We remark that here and in the following, one may restrict attention to dual pairs of convex functions $\phi, \psi=\mathcal L\phi$, without loss of generality. In all that follows, we take *a.e.-uniqueness* to mean uniqueness up to equality a.e.

Let us check the trivial statement in the conjecture.

::: Lemma
Pairs $\phi,\psi$ as in [\[eq:pairs\]](#eq:pairs){reference-type="eqref" reference="eq:pairs"} give equality in [\[eq:general_inequality\]](#eq:general_inequality){reference-type="eqref" reference="eq:general_inequality"}.
:::

Taking $q(x)=\frac12 |x|^2$, $$\mathcal Lq_z(\xi)=\frac{|\xi|^2}{2}-\langle \xi,z\rangle,$$ and so $$\begin{aligned}
&\int_{\mathbb{R}^n\times\mathbb{R}^n} e^{-\frac{|z|^2}{2\rho^2}-\frac{|\xi|^2}{2}+\langle \xi, z\rangle}d\xi dz=\rho^n\int e^{-\frac12 (|w|^2+|\xi|^2-2\rho\langle w,\xi\rangle )}d\xi dw
    \\&=\rho^n\int e^{-\frac12 (|w-\rho\xi|^2+(1-\rho^2)|\xi|^2)}d\xi dw =\int e^{-\frac12 |w|^2}dw\int e^{-\frac12 (1-\rho^2)|\xi|^2} d\xi \\&=(2\pi)^n\rho^n(1-\rho^2)^{-\frac{n}{2}}.
\end{aligned}$$ By Lemma [\[lem:functional_invariance\]](#lem:functional_invariance){reference-type="ref" reference="lem:functional_invariance"}, we get equality for all pairs as claimed.

An immediate corollary is a functional version of Conjecture [\[conj:bodies\]](#conj:bodies){reference-type="ref" reference="conj:bodies"}, as follows.

::: Conjecture
[]{#conj:functional_santalo label="conj:functional_santalo"} Let $f:\mathbb{R}^n\to \mathbb{R}_+$ be an integrable Borel function, and assume also that $\int x f(x)dx=0$. Then for all $0\leq \rho<1$, $$\widetilde M_\rho(f,0)\leq \frac{1}{n!}(2\pi)^n\rho^n(1-\rho^2)^{-\frac n 2}.$$ Equality is attained uniquely by multiples of gaussians: $f(x)=\lambda e^{-\frac 12 \langle Ax, x\rangle}$.
:::

::: Remark
Note that the implication Conjecture [\[conj:functional_general\]](#conj:functional_general){reference-type="ref" reference="conj:functional_general"} $\Rightarrow$ Conjecture [\[conj:functional_santalo\]](#conj:functional_santalo){reference-type="ref" reference="conj:functional_santalo"} is valid separately for each $n$, and also separately for any family of functions with certain symmetry, such as even or unconditional functions.
:::

We now prove Conjecture [\[conj:functional_general\]](#conj:functional_general){reference-type="ref" reference="conj:functional_general"} under the extra assumption of unconditionality. Recall that $\phi$ is unconditional if $\phi(x_1,\dots, x_n)=\phi(|x_1|,\dots, |x_n|)$.

::: Theorem
[]{#thm:functional_unconditional label="thm:functional_unconditional"} Consider two unconditional Borel functions $\phi,\psi:\mathbb{R}^n\to \mathbb{R}\cup\{+\infty\}$ such that for all $x,\xi\in\mathbb{R}^n$ one has $\phi(x)+\psi(\xi)\geq \langle x, \xi\rangle$. Then for all $0\leq \rho<1$, $$\int_{\mathbb{R}^n\times\mathbb{R}^n}e^{-\phi(x)-\psi(\xi)+\rho\langle x,\xi\rangle}dxd\xi\leq (2\pi)^n(1-\rho^2)^{-\frac n 2}.$$ Equality is attained a.e.-uniquely by Legendre-dual pairs $$\phi(x)=\frac 12 \langle Ax, x\rangle +c, \quad \psi(\xi)=\mathcal L\phi(\xi)=\frac 12 \langle A^{-1}x, x\rangle -c.$$
:::

Since $\phi(x)=\phi(-x)$, the claimed inequality is equivalent to $$\label{eq:ineq1} I:=\int_{\mathbb{R}^n\times\mathbb{R}^n} e^{-\phi(x)-\psi(\xi)}\cosh(\rho \langle x, \xi\rangle)d\xi dx\leq (2\pi)^n(1-\rho^2)^{-n/2}.$$

The left hand side can be rewritten as $$\begin{aligned}
J&=\sum_{j=0}^\infty \frac{\rho^{2j}}{(2j)!}\int_{\mathbb{R}^n\times\mathbb{R}^n}e^{-\phi(x)-\psi(\xi)}\langle x, \xi\rangle^{2j}dxd\xi\\&=\sum_{j=0}^\infty\frac{\rho^{2j}}{(2j)!}\sum_{|I|=2j}{2j\choose I}\int_{\mathbb{R}^n}x^{I}e^{-\phi(x)}dx\int_{\mathbb{R}^n}\xi^{I}e^{-\psi(\xi)}d\xi,\nonumber
\end{aligned}$$ where the last sum is over all $n$-tuples $I=(i_1,\dots, i_n)$ of non-negative integers such that $|I|:=\sum_{\nu=1}^n i_\nu =2j$, and we use the notation $x^I:=\prod_{\nu=1}^n x_\nu^{i_\nu}$, and $${2j\choose I}:=\frac{(2j)!}{i_1!\cdots i_n!}$$ for the multinomial coefficient.

Observe that by unconditionality, if $I$ contains an odd index then the corresponding integrals vanish. Therefore, $$\begin{aligned}
\label{eq:eq1} J&= \sum_{j=0}^\infty\frac{\rho^{2j}}{(2j)!}\sum_{|I|=j}{2j\choose 2I}\int_{\mathbb{R}^n}x^{2I}e^{-\phi(x)}dx\int_{\mathbb{R}^n}\xi^{2I}e^{-\psi(\xi)}d\xi\\&=
    4^{n}\sum_{j=0}^\infty\frac{\rho^{2j}}{(2j)!}\sum_{|I|=j}{2j\choose 2I}\int_{\mathbb{R}^n_+}x^{2I}e^{-\phi(x)}dx\int_{\mathbb{R}^n_+}\xi^{2I}e^{-\psi(\xi)}d\xi. \nonumber
\end{aligned}$$

Making the change of coordinates $x=e^u:=(e^{u_i})_{i=1}^n$, $\xi=e^v=(e^{v_i})$, we may write $$\label{eq:eq2}\int_{\mathbb{R}_+^n}e^{-\phi(x)}x^{2I}dx\int_{\mathbb{R}_+^n}e^{-\psi(\xi)}\xi^{2I}d\xi=\int_{\mathbb{R}^n} f(u)du\int_{\mathbb{R}^n} g(v)dv,$$ where $f(u)=e^{-\phi(e^u)}e^{\langle 2I+1, u\rangle}$, $g(v)=e^{-\psi(e^v)}e^{\langle 2I+1, v\rangle}$, and $I+c:=(i_\nu+c)_{\nu=1}^n$.

Denote $$h(w)=e^{-\frac12 |e^w|^2}e^{\langle 2I+1, w\rangle},\quad w\in \mathbb{R}^n,$$ where $|e^w|=\sqrt{\sum_{i=1}^n e^{2w_i}}$. Since $\phi(x)+\psi(\xi)\geq  \langle x, \xi\rangle$, we immediately find that $$f(u)g(v)\leq h\left(\frac{u+v}{2}\right)^2,$$ and by the Prekopa-Leindler inequality we have $$\begin{aligned}
 \int_{\mathbb{R}^n} f\int_{\mathbb{R}^n} g&\leq \left(\int_{\mathbb{R}^n} h\right)^2=\left(\int_0^\infty e^{-\frac{|p|^2}{2}}p^{2I}dp\right)^2=\prod_{\nu=1}^n\left(\int_0^\infty e^{-\frac{t^2}{2}} t^{2i_\nu}dt\right)^2\\&=\left( \frac{\sqrt{2\pi}}{2}\right)^{2n} \prod_{\nu=1}^n ((2i_\nu-1)!!)^2=\frac{(2\pi)^n}{4^n} \prod_{\nu=1}^n ((2i_\nu-1)!!)^2.
\end{aligned}$$ Combined with [\[eq:ineq1\]](#eq:ineq1){reference-type="eqref" reference="eq:ineq1"}, [\[eq:eq1\]](#eq:eq1){reference-type="eqref" reference="eq:eq1"}, [\[eq:eq2\]](#eq:eq2){reference-type="eqref" reference="eq:eq2"}, it remains to verify that

$$\sum_{j=0}^\infty \frac{\rho^{2j}}{(2j)!}\sum_{|I|=j}{2j\choose 2I}\prod_{\nu=1}^n ((2i_\nu-1)!!)^2 =(1-\rho^2)^{-n/2},$$ or equivalently

$$\sum_{j=0}^\infty \rho^{2j}\sum_{|I|=j}{2j\choose 2I}\prod_{\nu=1}^n \frac{(2i_\nu-1)!!}{(2i_\nu)!!} =(1-\rho^2)^{-n/2}.$$ By Newton's binomial formula, $$(1-\rho^2)^{-\frac12}=\sum_{i=0}^\infty{-1/2 \choose i}(-1)^i\rho^{2i}=\sum_{i=0}^\infty\frac{(2i-1)!!}{2^i i!}\rho^{2i}=\sum_{i=0}^\infty\frac{(2i-1)!!}{(2i)!!}\rho^{2i},$$ and it remains to raise both sides to power $n$.

For equality, we must have an equality at each application of Prekopa-Leindler, which is characterized in [@dubuc]. Namely for each $I$, one has a.e. equalities $f=\lambda h(\bullet + C)$, $g=\lambda^{-1}h(\bullet - C)$. Already for a single multi-index $I$ this forces the existence of a diagonal matrix $A$ and $c\in\mathbb{R}$ such that a.e. one has $$\phi(x)=\frac 12 \langle Ax, x\rangle +c,\quad \psi(\xi)=\frac 12 \langle A^{-1}x, x\rangle -c.$$

By the previous discussion, we immediately get

::: Corollary
For all unconditional Borel functions $f:\mathbb{R}^n\to \mathbb{R}_+$ it holds that $$\widetilde M_\rho(f,0)\leq \frac{1}{n!}(2\pi)^n\rho^n(1-\rho^2)^{-\frac n 2},$$ with equality attained a.e.-uniquely by $f(x)=\lambda e^{-\frac12 \langle Ax, x\rangle}$ with some diagonal matrix $A>0$ and scalar $\lambda>0$.
:::

Follows directly from Theorem [\[thm:functional_unconditional\]](#thm:functional_unconditional){reference-type="ref" reference="thm:functional_unconditional"}, since $\widetilde M_\rho(f,0)=\widetilde M_\rho(f)$ by unconditionality and the second part of Lemma [\[lem:functional_invariance\]](#lem:functional_invariance){reference-type="ref" reference="lem:functional_invariance"}.

In particular, we proved a functional inequality of independent interest.

::: Corollary
[]{#cor:even_moments label="cor:even_moments"} Consider an unconditional Borel function $f=e^{-\phi}:\mathbb{R}^n\to \mathbb{R}_+$. Then $$I_{2j}(f):=\int_{\mathbb{R}^n\times\mathbb{R}^n}\langle x,\xi\rangle ^{2j}e^{-\phi(x)-\mathcal L\phi(\xi)}dx d\xi\leq (2\pi)^n \frac{(n-2+2j)!!}{(n-2)!!(2j-1)!!}.$$ Equality is attained a.e.-uniquely by multiples of gaussians $f(x)=\lambda e^{-\frac 12 \langle Ax, x\rangle}$, for some diagonal $A>0$ and scalar $\lambda>0$.
:::

The case of $j=0$ is the Blaschke-Santaló inequality for unconditional functions. The case of $j=1$ was established previously in [@huang_li]. Denote $\psi=\mathcal L\phi$. In the proof of Theorem [\[thm:functional_unconditional\]](#thm:functional_unconditional){reference-type="ref" reference="thm:functional_unconditional"}, we have seen that $I_{2j}(e^{-\phi})$ is maximized a.e.-uniquely by multiples of gaussians. The maximal value $I_{2j}(G)$ can be computed directly, or alternatively it can be deduced from Theorem [\[thm:functional_unconditional\]](#thm:functional_unconditional){reference-type="ref" reference="thm:functional_unconditional"} as follows. We have $$\sum_{j=0}^\infty\frac{\rho^{2j}}{(2j)!}I_{2j}(G)= (2\pi)^n(1-\rho^2)^{-n/2},$$ and by Newton's binomial $$(1-\rho^2)^{-\frac n2}=\sum_{j=0}^\infty{-n/2 \choose j}(-1)^j\rho^{2j}=\sum_{i=0}^\infty\frac{(n+2j-2)!!}{(n-2)!!(2j)!! }\rho^{2j}.$$ Consequently, $$I_{2j}(G)=(2\pi)^n(2j)!\frac{(n+2j-2)!!}{(n-2)!!(2j)!! }=(2\pi)^n\frac{(n-2+2j)!!}{(n-2)!!(2j-1)!!}.$$

We can now deduce the corresponding inequalities for unconditional convex bodies. Define $$I_{2j}(K):=\int_{K\times K^o} \langle x,\xi\rangle^{2j}dxd\xi.$$ First, we prove two simple relations.

::: Lemma
For any convex body $K\in\mathcal K_0(\mathbb{R}^n)$, $$\label{eq:gaussian_body} I_{2j}(K)=\frac{1}{((n+2j)!!)^2} \left(\frac 2\pi \right)^{\frac12(1-(-1)^n)}I_{2j}(e^{-\frac12 \|x\|_K^2}).$$ If $K=-K$ then $$\label{eq:mahler_to_moments}\widetilde M_\rho(K)= \sum_{j=0}^\infty {n+2j \choose n}I_{2j}(K)\rho^{n+2j}.$$
:::

We will use the change of variables $x=tp$, $\xi=s\eta$, with $p\in\partial K, \eta\in \partial K^o$. We have $dx=r^{n-1}drd\mu_K(p), d\xi =s^{n-1}dsd\mu_{K^o}(\eta)$.

We may write

$$\begin{aligned}
I_{2j}(e^{-\frac12 \|x\|_K^2})&=\int_{\mathbb{R}^n\times \mathbb{R}^n}\langle x, \xi\rangle ^{2j}e^{-\frac{\|x\|^2_K}{2}}e^{-\frac{\|\xi\|^2_{K^o}}{2}}dxd\xi\\&=\int_{[0,\infty)^2}e^{-\frac {r^2}{2}-\frac{s^2}{2}}r^{n+2j-1}s^{n+2j-1}drds\int_{\partial K\times\partial K^o}\langle p, \eta\rangle ^{2j}d\mu_K(p)d\mu_{K^o}(\eta)
    \\&=\left(\int_0^\infty r^{n+2j-1} e^{-r^2/2}dr\right)^2\int_{\partial K\times\partial K^o}\langle p, \eta\rangle ^{2j}d\mu_K(p)d\mu_{K^o}(\eta)\\
    &=2^{n+2j-2}\Gamma(\frac{n}{2}+j)^2\int_{\partial K\times\partial K^o}\langle p, \eta\rangle ^{2j}d\mu_K(p)d\mu_{K^o}(\eta).
\end{aligned}$$ On the other hand, $$\begin{aligned}
    I_{2j}(K)&=\int_{K\times K^o}\langle x, \xi\rangle^{2j}dxd\xi\\&=\int_{\partial K\times \partial K^o} \langle p, \eta\rangle ^{2j}d\mu_K(p)d\mu_{K^o}(\eta)\int_{[0,1]^2}r^{n+2j-1}s^{n+2j-1}drds\\&=\frac{1}{(n+2j)^2}\int_{\partial K\times \partial K^o} \langle p, \eta\rangle ^{2j}d\mu_K(p)d\mu_{K^o}(\eta),
    
\end{aligned}$$ and it remains to combine the two equalities to find $$\begin{aligned}
 I_{2j}(K)&=\frac{1}{2^{n+2j-2}(n+2j)^2\Gamma(\frac n 2+j )^2}I_{2j}(e^{-\frac12\|x\|^2_K})\\&=\frac{1}{((n+2j)!!)^2} \left(\frac 2\pi \right)^{\frac12(1-(-1)^n)}I_{2j}(e^{-\frac12 \|x\|_K^2}).
\end{aligned}$$

Now assume $K=-K$. By Lemmas [\[lem:body_vs_function\]](#lem:body_vs_function){reference-type="ref" reference="lem:body_vs_function"} and [\[lem:mahler_convex\]](#lem:mahler_convex){reference-type="ref" reference="lem:mahler_convex"}, $$\begin{aligned}
    \widetilde M_\rho(K)=\widetilde M_\rho(K,0)=\widetilde M_\rho(\mathbbm 1_K, 0)=&\frac{\rho^n}{n!}\int_{K\times\mathbb{R}^n}e^{-\|\xi\|_{K^o}+\rho\langle x,\xi\rangle}dxd\xi\\&=\frac{\rho^n}{n!}\int_{K\times\mathbb{R}^n}e^{-\|\xi\|_{K^o}}\cosh(\rho\langle x,\xi\rangle)dxd\xi
    \\&=\sum_{j=0}^\infty \frac{1}{n!(2j)!}\rho^{n+2j}\int_{K\times\mathbb{R}^n}\langle x, \xi\rangle^{2j}e^{-\|\xi\|_{K^o}}dxd\xi.
\end{aligned}$$ We may write $$\begin{aligned}
I_{2j}(K)=\int_{K\times K^o}\langle x,\xi\rangle^{2j}dxd\xi&=\int_{K\times\partial K^o}\langle x,\eta\rangle^{2j}dxd\mu_{K^o}(\eta)\int_0^1s^{2j+n-1}ds\\&=\frac{1}{n+2j}\int_{K\times\partial K^o}\langle x,\eta\rangle^{2j}dxd\mu_{K^o}(\eta).
\end{aligned}$$ Therefore, $$\begin{aligned}
\int_{K\times\mathbb{R}^n}\langle x, \xi\rangle^{2j}e^{-\|\xi\|_{K^o}}dxd\xi &=\int_{K\times [0,\infty)\times \partial K^o} s^{2j+n-1}e^{-s}\langle x,\eta\rangle ^{2j}dxds d\mu_{K^o}(\eta)\\&=(2j+n-1)!\int_{K\times\partial K^o}\langle x, \eta\rangle^{2j}dxd\mu_{K^o}(\eta)\\&=(2j+n)!I_{2j}(K),
\end{aligned}$$ and so $$\widetilde M_\rho(K) = \sum_{j=0}^\infty \frac{(n+2j)!}{n!(2j)!}\rho^{n+2j}I_{2j}(K).$$

::: Corollary
[]{#cor:bodies_moments label="cor:bodies_moments"} For $K\subset \mathbb{R}^n$ convex and unconditional, $$I_{2j}(K):=\int_{K\times K^o} \langle x,\xi\rangle^{2j}dxd\xi\leq \frac{(2\pi)^n}{n+2j}\frac{1}{ (n+2j)!!(n-2)!!(2j-1)!!} \left(\frac2\pi\right)^{\frac{1-(-1)^n}{2} }.$$ Equality is attained uniquely by ellipsoids.
:::

We apply Corollary [\[cor:even_moments\]](#cor:even_moments){reference-type="ref" reference="cor:even_moments"} to $f(x)=e^{-\phi(x)}=e^{-\frac12 \|x\|_K^2}$. By eq. [\[eq:gaussian_body\]](#eq:gaussian_body){reference-type="eqref" reference="eq:gaussian_body"}, $I_{2j}(K)$ is uniquely maximized by ellipsoids, and the maximal value is readily computed.

::: Corollary
[]{#cor:bodies_mahler label="cor:bodies_mahler"} For any $0\leq  r<\infty$, and $K\subset \mathbb{R}^n$ convex and unconditional, $M_r(K)\leq  M_r(B^n)$. Equality is attained uniquely by ellipsoids.
:::

We only need to note that by Corollary [\[cor:bodies_moments\]](#cor:bodies_moments){reference-type="ref" reference="cor:bodies_moments"}, each summand of [\[eq:mahler_to_moments\]](#eq:mahler_to_moments){reference-type="eqref" reference="eq:mahler_to_moments"} is uniquely maximized by ellipsoids.

*Proof of Corollary [\[cor:entropy\]](#cor:entropy){reference-type="ref" reference="cor:entropy"}*. Since $d^H=\frac12(d^F+d^{RF})\geq \frac12d^F$, it follows that $B^H_r(q, K)\subset B^F_{2r}(q, K)$. Write $c_n$ for a constant depending only on $n$ which may change between occurrences. By Proposition [\[prop:centro_affine\]](#prop:centro_affine){reference-type="ref" reference="prop:centro_affine"} we have $\mathop{\mathrm{vol}}^F(B^F_R(q,B^n))\leq c_ne^{\frac{n-1}{2}R }$. Using the Rogers-Shephard inequality as in the proof of Corollary [\[cor:hilbert_volume_sec3\]](#cor:hilbert_volume_sec3){reference-type="ref" reference="cor:hilbert_volume_sec3"}, and applying Corollary [\[cor:bodies_mahler\]](#cor:bodies_mahler){reference-type="ref" reference="cor:bodies_mahler"}, we find $$\begin{aligned}
 \mathop{\mathrm{vol}}_K^H(B_r^H(q,K))&\leq c_n \mathop{\mathrm{vol}}_K^F(B_r^H(q,K))\leq c_n\mathop{\mathrm{vol}}_K^F(B_{2r}^F(q,K))\leq  c_n\mathop{\mathrm{vol}}_K^F(B_{2r}^F(q,B^n))\\&\leq c_ne^{\frac{n-1}{2}2r}=c_ne^{(n-1)r},
\end{aligned}$$ completing the proof. 0◻

Using the same methods as before, we can also show the following.

::: Theorem
Let $f=e^{-\phi}:\mathbb{R}^n_+\to \mathbb{R}_+$ be a Borel function. Then

-   For all $j\geq 0$, $$I^+_j(f):=\int_{\mathbb{R}_+^n\times\mathbb{R}_+^n}\langle x,\xi\rangle^{j} e^{-\phi(x)-\mathcal L\phi(\xi)}dx d\xi\leq I^+_j(e^{-\frac{|x|^2}{2}}).$$

-   If $n=1$, $$I_{2j+1}^+(f)=\int_0^\infty x^{2j+1} e^{-\phi(x)}dx  \int_0^\infty \xi^{2j+1}e^{-\mathcal L\phi(\xi)} d\xi\leq (2j)!!^2.$$

-   For all $0\leq \rho<1$, $$\int_{\mathbb{R}_+\times\mathbb{R}_+}e^{-\phi(x)-\mathcal L\phi (\xi)}\sinh (\rho x\xi)dxd\xi\leq\frac{1}{\sqrt{1-\rho^2}}\arctan\frac{\rho}{\sqrt{1-\rho^2}}.$$

Equality in all cases is a.e.-uniquely attained by $\lambda e^{-\frac12 \langle Ax, x\rangle}$, where $A>0$ is diagonal and $\lambda>0$.
:::

The first two inequalities can be obtained by trivially adjusting the proof of Theorem [\[thm:functional_unconditional\]](#thm:functional_unconditional){reference-type="ref" reference="thm:functional_unconditional"}. For the last inequality, we should show that $$\sum_{j=0}^\infty\frac{(2j)!!^2}{(2j+1)!}\rho^{2j+1}=\sum_{j=0}^\infty\frac{(2j)!!}{(2j+1)!!}\rho^{2j+1}=\frac{1}{\sqrt{1-\rho^2}}\arctan\frac{\rho}{\sqrt{1-\rho^2}}.$$ This can be done by observing that $$\frac{(2j)!!}{(2j+1)!!}=\int_0^{\pi/2}\sin^{2j}tdt,$$ and so $$\begin{aligned}
\sum_{j=0}^\infty\frac{(2j)!!}{(2j+1)!!}\rho^{2j+1}&=\int_{0}^{\frac \pi 2}(\rho\sin t)^{2j+1}dt=\int_0^{\frac \pi 2}\frac{\rho \sin t}{1-\rho^2\sin^2t}dt\\&=\int_0^1 \frac{2\rho ds}{s^2+2(1-2\rho^2)s +1}\\&=\frac{1}{\sqrt{1-\rho^2}}\left(\arctan \frac{\sqrt{1-\rho^2}}{\rho}-\arctan \frac{1-2\rho^2}{2\rho \sqrt{1-\rho^2}}\right)\\&=\frac{1}{\sqrt{1-\rho^2}}\arctan \frac{\rho}{\sqrt{1-\rho^2}}.
\end{aligned}$$ Equality cases are settled using [@dubuc] as in Theorem [\[thm:functional_unconditional\]](#thm:functional_unconditional){reference-type="ref" reference="thm:functional_unconditional"}. As a sidenote, the discussion above suggests an extension of the centro-affine surface area to functions.

::: Definition
Let $f:\mathbb{R}^n\to[0,\infty)$ be a Borel function. Its centro-affine surface area is $$\begin{aligned}
\Omega_n(f)&:=\frac{1}{n!}\limsup_{\rho\to1^-} (1-\rho^2)^{n/2}\displaystyle\int_{\mathbb{R}^n\times \mathbb{R}^n} e^{-\phi(x)-\mathcal L \phi (\xi)+\rho\langle x,\xi\rangle}dxd\xi.
\end{aligned}$$
:::

Evidently, $\Omega_n(f)=\Omega_n(\lambda f\circ A)$ for any $\lambda> 0$ and $A\in\mathop{\mathrm{GL}}_n(\mathbb{R})$.

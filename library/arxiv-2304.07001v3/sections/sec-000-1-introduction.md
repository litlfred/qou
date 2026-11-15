---
doc_id: arxiv-2304.07001v3
doc_title: "RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-7
source_pdf: 2304.07001v3.pdf
source_sha256: b6c0d7f50b6407f1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.71
latex_coverage_ratio: 0.967
doc_brief: "RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES — We prove resurgence properties for the Borel transform of a formal power series associated to elements in the Habiro ring that come from radial"
---
The modern theory of resurgence began with the voluminous works of Écalle in 1981 [@e1; @e2] and 1985 [@e3]. This theory now plays a vital rôle in a remarkable number of diverse areas, to name just a few examples: nonlinear systems of ODEs and difference equations [@costin1; @kamimoto], algebraic combinatorics [@cfmt1; @cfmt2], enumerative combinatorics and quantum field theory [@BD; @MY], period integrals and string theory scattering amplitudes [@dk], wall-crossing phenomena [@ks] and matrix models [@mm]. In this paper, we are interested in a conjecture due to Costin and Garoufalidis [@cg] which connects resurgence and quantum topology. For other such interactions, see [@am; @ggm; @ggm2; @ggmw; @fw] and the references therein.

Let us recall the general setup from [@cg]. For further details, see [@costin2; @dp; @bm; @ms] or [@Sauzin Section 2] for an excellent concise review of the basic notions of resurgence and alien calculus. A formal power series $$\label{fps}
\mathcal{F}(x)=\sum_{n=0}^{\infty} a_n x^{-n} \in \mathbb{C}[[1/x]]$$ is called Gevrey-1 if there exists positive real numbers $A$, $B$ such that $$| a_n | \leq AB^n n!$$ for all $n \geq 0$. Consider a Gevrey-1 formal power series given by ([\[fps\]](#fps){reference-type="ref" reference="fps"}) and its Borel transform $\mathcal{B}: \mathbb{C}[[1/x]] \longrightarrow \mathbb{C}[[p]]$ defined by $$\label{borel}
\mathcal{B} \Biggl( \sum_{n=0}^{\infty} a_n x^{-n} \Biggr) = a_0\delta+\sum_{n=1}^{\infty} a_{n} \frac{p^{n-1}}{(n-1)!} =: a_0\delta + G(p)$$ where $\delta$ is a formal symbol that has Laplace transform given by the constant function $1$. For simplicity, we write $\mathcal{B}[\mathcal{F}](p)$ for the transform [\[borel\]](#borel){reference-type="eqref" reference="borel"}. Here, $G(p)$ has a positive radius of convergence as it arose from a Gevrey-1 power series. In a standard abuse of notation, $G(p)$ denotes the formal power series in ([\[borel\]](#borel){reference-type="ref" reference="borel"}) (and is also commonly referred to in the literature as the Borel transform of $\mathcal{F}(x)$) and the analytic continuation of the associated germ at the origin. In addition, $G(p)$ is called a *resurgent function* if it is endlessly analytically continuable [@ms]. This property means $G(p)$ extends to a (possibly multi-valued) holomorphic function along unbounded paths that need only circumvent a discrete set of singularities. In the present work, we consider the case where $G(p)$ defines a multi-valued function on $\mathbb{C} \setminus \mathcal{N}$, with $\mathcal{N}$ a discrete set of singularities lying on the ray $\mathbb{R}_{>0}$, e.g., $\mathcal{N} = \left \{ \frac{n^2\pi^2}{6}:n\in\mathbb{Z}_{>0} \right \}$.

Assuming $G(p)$ satisfies suitable growth conditions, the left and right Borel resummations of $\mathcal{F}(x)$ are defined as $$\begin{aligned}
S^{+}[\mathcal{F}](x) =\int_{\gamma_l}e^{-px} \mathcal{B}[\mathcal{F}](p) \,dp
\end{aligned}$$ and $$\begin{aligned}
S^{-}[\mathcal{F}](x) =\int_{\gamma_r}e^{-px}  \mathcal{B}[\mathcal{F}](p) \, dp
\end{aligned}$$ where $x \in \mathbb{C}$ and $\gamma_l$ and $\gamma_r$ are contours in $\mathbb{C} \setminus \mathcal{N}$ from $0$ to $\infty$ that turn left (respectively, right) at each singularity in $\mathcal{N}$ (see Figure [1](#fig:fig1){reference-type="ref" reference="fig:fig1"}). In addition, the left and right Borel resummations give analytic functions on a sector of opening angle $\pi$ in the complex $x$-plane.

<figure id="fig:fig1">

<figcaption>A singularity set <span class="math inline">𝒩 ⊂ ℂ</span> and the contours <span class="math inline"><em>γ</em><sub><em>l</em></sub></span> and <span class="math inline"><em>γ</em><sub><em>r</em></sub></span>.</figcaption>
</figure>

Following [@cg Sections 4.2--4.3], the median resummation of $\mathcal{F}$ is given by $$\label{smed}
S^{\textbf{med}}(x) = S^{\textbf{med}}[\mathcal{F}](x) := \frac{1}{2} \Bigl( S^{+}[\mathcal{F}](x) + S^{-}[\mathcal{F}](x) \Bigr).$$ In general, care is required when defining median summations, see [@hlss Section 2]. Under favorable circumstances, for example when $G(p)$ is the Borel transform of a formal (Gevrey-1) solution in powers of $1/x$ to a linear differential equation, each of $\mathcal{S}^{\pm}[\mathcal{F}](x)$ (and thus, of course, $S^{\textbf{med}}(x)$) is a well-defined homomorphic solution. This is one incarnation of the terminology "resummation".

In this paper, we will study the median resummation of the Borel transform for certain formal power series associated to knots.

Let $K$ be a knot and $J_N(K; q)$ be the usual colored Jones polynomial, normalized to be 1 for the unknot. If $N=2$, then we recover the Jones polynomial [@Jones]. As a knot invariant, the colored Jones polynomial is of fundamental importance in several open problems in quantum topology (see, e.g., [@garoufalidis-AJ; @garoufalidis-slope; @kal-tran; @my; @z]). We now recall the Habiro ring [@habiro] $$\displaystyle \mathcal{H} := \varprojlim_{n} \mathbb{Z}[q] / \langle (q)_n \rangle$$ where $$(a)_n = (a;q)_n := \prod_{k=1}^{n} (1-aq^{k-1})$$ is the standard $q$-Pochhammer symbol. Every element of $\mathcal{H}$ may be written as $$\sum_{n=0}^{\infty} b_n(q) (q)_n$$ where $b_n(q) \in \mathbb{Z}[q]$. Given $K$, there exists an element $\Phi_{K}(q) \in \mathcal{H}$ called the Kashaev invariant [@Kashaev:6j] which matches $J_N(K; q)$ (up to a prefactor) when $q=\zeta_N := e^{\frac{2 \pi i}{N}}$ [@hl Theorem 2]. To illustrate, for the trefoil knot $K=3_1$, we have [@habiro1; @thang] $$\label{cjp31}
J_{N}(3_1; q) = q^{1-N} \sum_{n=0}^{\infty} q^{-nN} (q^{1-N})_n.$$ In this case, the Kontsevich-Zagier series [@z] $$\label{kz}
\Phi_{3_1}(q) := \sum_{n=0}^{\infty} (q)_n \in \mathcal{H}$$ gives the Kashaev invariant for the trefoil [@Kashaev:6j] and so from [\[cjp31\]](#cjp31){reference-type="eqref" reference="cjp31"} and [\[kz\]](#kz){reference-type="eqref" reference="kz"}, we observe $$\Phi_{3_1}(\zeta_N) \zeta_N = J_N(3_1; \zeta_N).$$ Now, a crucial aspect of the computations in [@cg] is the "strange identity\" $$\label{strid}
\Phi_{3_1}(q) ``=" -\frac{1}{2} \sum_{n=1}^{\infty} n \Bigl( \frac{12}{n} \Bigr) q^{\frac{n^2 - 1}{24}}$$ where $``="$ means that both sides agree to infinite order at any root of unity and $\bigl( \frac{12}{*} \bigr)$ is the quadratic character of conductor $12$. More precisely, replacing $q$ by the product of a root of unity and $e^{-x}$, then letting $x \to 0^{+}$, the right-hand side has an asymptotic expansion as a power series in $x$ and this power series is given by the left-hand side at $q$. For further details, see [@akl; @z1]. If $q=e^{2 \pi i x}$, $x \in \mathbb{H}$, then ([\[strid\]](#strid){reference-type="ref" reference="strid"}) implies for $0 \neq \alpha \in \mathbb{Q}$ $$\label{rational}
e^{\frac{\pi i \alpha}{12}} \Phi_{3_1}(e^{2 \pi i \alpha}) = -\frac{1}{2} \sum_{n=1}^{\infty} n \Bigl( \frac{12}{n} \Bigr) e^{\frac{n^2 \pi i \alpha}{12}}$$ where the right-hand side of ([\[rational\]](#rational){reference-type="ref" reference="rational"}) is interpreted as the radial limit $x \to \alpha$. The significance of "identities\" akin to ([\[strid\]](#strid){reference-type="ref" reference="strid"}) is evident in various applications, e.g., asymptotics and congruences for Fishburn and generalized Fishburn numbers modulo prime powers [@ak; @akl; @as; @Be; @an; @gjko; @straub; @z1], the quantum modularity of $\Phi_{3_1}(q)$ [@go; @z] and expressing WRT invariants of Brieskorn homology spheres in terms of limiting values of Eichler integrals [@hikamiWRT1; @hikamiWRT2; @hikamiWRT3]. For a recent advance using the "Bailey machinery\" which not only recovers ([\[strid\]](#strid){reference-type="ref" reference="strid"}), but produces a wealth of new examples, see [@lovejoy].

Elements of $\mathcal{H}$ can also be formally expanded around any root of unity. Therefore, we let $$\label{habel}
F_{K}(x) := \Phi_{K}(e^{-\frac{1}{x}})\in\mathbb{C}[\![1/x]\!].$$ To emphasize the dependence on $K$, we denote the Borel transform of $F_{K}(x)$ by $G_{K}(p)$ and its conjecturally well-defined median resummation by $S_{K}^{\textbf{med}}(x)$. Finally, we use the notation $\stackrel{.}{=}$ to denote equality up to a prefactor which depends on $K$. We can now state the main conjecture from [@cg] (slightly edited for clarity) which is part of a larger program to understand the analytic continuation of invariants of "knotted objects\" arising in Chern-Simons theory [@g; @gl].

::: conjecture
[]{#cgconj label="cgconj"} For every knot $K$,

-   $F_K(x)$ has a resurgent Borel transform $G_{K}(p)$.\

-   $S^{\textbf{med}}_{K}(x)$ is an analytic function defined on $\Re(x) > 0$ with radial limits at the points $\frac{1}{2\pi i} \mathbb{Q}$ of its natural boundary.\

-   If $(2)$ is true, then consider the radial limit $$S_{K}^{\bf{med}}\left( -\frac{1}{2 \pi i \alpha} \right)  := \lim_{x \to -\frac{1}{2 \pi i \alpha}} S_{K}^{\bf{med}}(x)$$ where $\Re(x) > 0$. For $0 \neq \alpha \in\mathbb{Q}$, we have $S_{K}^{\textbf{med}}\left(-\frac{1}{2 \pi i \alpha}\right) \stackrel{.}{=} \Phi_{K}(e^{2\pi i \alpha})$.
:::

In [@cg Theorem 2.5, Theorem 3.1], Conjecture [\[cgconj\]](#cgconj){reference-type="ref" reference="cgconj"} (1) and (2) were proven for $K=3_1$. Here, $$F_{3_1}(x) = e^{-\frac{1}{24x}} \sum_{n=0}^{\infty} (e^{-\frac{1}{x}})_n$$ where an adjustment of ([\[habel\]](#habel){reference-type="ref" reference="habel"}) has been made. The Borel transform $G_{3_1}(p)$ of $F_{3_1}(x)$ is explicitly given by [@cg Theorem 3.1] $$\label{g31}
G_{3_1}(p) = \frac{3 \pi}{2\sqrt{2}} \sum_{n=1}^{\infty} \frac{n \bigl( \frac{12}{n} \bigr)}{\bigl (-p + \frac{n^2 \pi^2}{6} \bigr)^{5/2}}.$$ Moreover, a close inspection of the proofs of Theorems 2.5 and 3.1 in [@cg] reveals that it is actually ([\[strid\]](#strid){reference-type="ref" reference="strid"}) and the periodic function $\bigl( \frac{12}{*} \bigr)$ which determine the analytic nature of $G_{3_1}(p)$ and $S^{\textbf{med}}_{3_1}(x)$. Our main goal in this paper is to prove resurgence properties for formal power series associated to elements in $\mathcal{H}$ that satisfy a general type of strange identity motivated by ([\[strid\]](#strid){reference-type="ref" reference="strid"}). Here, we emphasize the importance of periodic functions. Before stating our main result, we introduce some notation.

Let $M \geq 2$ be an integer and $k_1, k_2 \in \mathbb{Z}$ with $0 < k_1 < k_2 < \frac{M}{2}$. Let $0\neq c\in\mathbb{R}$ and $f$ be the function $$\begin{aligned}
\label{ggen}
f(n):=\begin{cases}
c &\text{if $n\equiv k_1,M-k_1\pmod{M}$,} \\
-c &\text{if $n\equiv k_2,M-k_2\pmod{M}$,}\\
0 &\text{otherwise.}
\end{cases} 
\end{aligned}$$ Note that under the conditions on $k_1$ and $k_2$, $f$ is a well-defined even function of period $M$ with mean value zero. For integers $a \geq 0$ and $b>0$, consider the partial theta series $$\label{pts}
\theta_{a,b,f}^{(\nu)}(q):=\sum_{n=0}^{\infty} n^\nu f(n)q^{\frac{n^2-a}{b}}$$ where $q=e^{2\pi i x}$, $x \in \mathbb{H}$, and $\nu \in \{0, 1\}$. For $\ell \in \mathbb{Z}$, set $$\label{ftilde}
\tilde{f}(\ell) := (-1)^{\ell} \sin\left(\frac{(k_2-k_1)\ell\pi}{M}\right)\sin\left(\frac{(M-k_1-k_2)\ell\pi}{M}\right).$$ Suppose there exists $$\Phi_{f}(q) := \sum_{n=0}^{\infty} A_{n,f}(q) (q)_n \in \mathcal{H}$$ where $A_{n,f}(q) \in \mathbb{Z}[q]$ such that $$\label{Hstrange}
 \Phi_{f}(q) ``=" \theta_{a,b,f}^{(1)}(q).$$ Finally, define $$\label{gen-expansions2}
\mathcal{F}_{f} \left( x \right) := e^{-\frac{a}{bx}} {\Phi}_f(e^{-\frac{1}{x}})=\sum_{n=0}^\infty\dfrac{C_{n,f}}{n!}\left(\frac{1}{bx}\right)^n\,.$$ The asymptotics of the partial theta series $\theta_{a,b,f}^{(1)}(q)$ around $q=1$, which by the strange identity in [\[Hstrange\]](#Hstrange){reference-type="eqref" reference="Hstrange"} gives the expansion of $\Phi_f(q)$, can be computed by $L$-values. By standard calculations using the Mellin transform (see, e.g., [@akl; @gjko; @z]), we find that $$\begin{aligned}
\label{Cnf}
C_{n,f}=(-1)^nL(-2n-1,f)
\end{aligned}$$ where $$\begin{aligned}
 L(s,f) :=\sum_{n=1}^\infty\dfrac{f(n)}{n^s}
\end{aligned}$$ is the $L$-series associated to $f$. In particular, using [@akl Lemma 3.2], we obtain that $$\begin{aligned}
\label{CnfBer}
C_{n,f}=(-1)^{n+1} \dfrac{M^{2n+1}}{2n+2} \sum_{m=1}^M f(m)B_{2n+2}\left(\dfrac{m}{M}\right)
\end{aligned}$$ where for $k\geq 0$, $B_k(x)$ denotes the $k$th Bernoulli polynomial. By ([\[gen-expansions2\]](#gen-expansions2){reference-type="ref" reference="gen-expansions2"}) and [\[CnfBer\]](#CnfBer){reference-type="eqref" reference="CnfBer"}, we have $$\label{F}
\mathcal{F}_{f} \left( \frac{1}{x} \right)  = \sum_{n=0}^{\infty} \frac{(-1)^{n+1} M^{2n+1}}{(2n+2) n!} \sum_{m=1}^{M} f(m) B_{2n+2}\left(\dfrac{m}{M}\right) \left(\frac{x}{b}\right)^n.$$ We will denote the Borel transform of $\mathcal{F}_f(x)$ by $G_f(p)$. Here, we write $S_{f}^{\bf{med}}(x)$ for $S^{\textbf{med}}(x)$, $$S_{f}^{\bf{med}}\left( -\frac{1}{2 \pi i \alpha} \right)  := \lim_{x \to -\frac{1}{2 \pi i \alpha}} S_{f}^{\bf{med}}(x),$$ $\theta_{a,b,f}^{(\nu)}(x)$ for $\theta_{a,b,f}^{(\nu)}(q)=\theta_{a,b,f}^{(\nu)}(e^{2\pi i x})$ and $\displaystyle \theta_{a,b,f}^{(\nu)}(\alpha) := \lim_{x \to \alpha} \theta_{a,b,f}^{(\nu)}(x)$ where $0 \neq \alpha \in \mathbb{Q}$. Our main result is now the following.

::: theorem
[]{#main label="main"} For $f$ given by [\[ggen\]](#ggen){reference-type="eqref" reference="ggen"} and $\mathcal{F}_f(x)$ as in [\[F\]](#F){reference-type="eqref" reference="F"}, we have the following:

-   $\mathcal{F}_f(x)$ has a resurgent Borel transform $G_f(p)$.\

-   $S_f^{\textbf{med}}(x)$ is an analytic function defined on $\Re(x) > 0$ with radial limits at the points $\frac{1}{2\pi i} \mathbb{Q}$ of its natural boundary.\

-   For $0 \neq \alpha\in\mathbb{Q}$, we have $$\label{eq:smed.form}
    S^{\textbf{med}}_f\left(-\dfrac{1}{2\pi i\alpha}\right)=\frac{c b e^{\pi i/4}}{M\pi (i\alpha)^{3/2}}\int_0^{+i\infty} \frac{\theta_{0,4M^2,\tilde{f}}^{(0)}(bp)}{\big(\frac{1}{\alpha}+ p\big)^{3/2}} dp+\left(\frac{b}{i\alpha}\right)^{3/2}\frac{\sqrt{2} c}{M^2}\theta^{(1)}_{0,4M^2,\tilde{f}}\left(-\frac{b}{\alpha}\right).$$
:::

::: remark
The proof of Theorem [\[main\]](#main){reference-type="ref" reference="main"} demonstrates resurgence properties for the normalized partial theta series $e^{-\frac{a}{bx}} \theta_{a,b,f}^{(1)}(e^{-\frac{1}{x}})$ without assuming [\[Hstrange\]](#Hstrange){reference-type="eqref" reference="Hstrange"}. Our results and those in the announcement [@hlss] appear to be related; however, we give a proof that can be used to prove Conjecture 1.1 for our cases of interest (see Corollary [\[cor\]](#cor){reference-type="ref" reference="cor"}).
:::

We give two applications of Theorem [\[main\]](#main){reference-type="ref" reference="main"}. The first result explicitly computes [\[eq:smed.form\]](#eq:smed.form){reference-type="eqref" reference="eq:smed.form"} in the following situation. For coprime positive integers $s$ and $t$, $1\le m\le t-1$ and $1\le n\le s-1$, let $\chi_{s,t}^{(n,m)}(k)$ be the periodic function obtained by choosing $c=1$, $M=2st$, $k_1= | nt-ms |$ and $k_2 = nt+ms$ in [\[ggen\]](#ggen){reference-type="eqref" reference="ggen"}, i.e., $$\begin{aligned}
\label{pf}
\chi_{s,t}^{(n,m)}(k)=\begin{cases}
1 & \text{if $k\equiv \pm(nt-ms)\pmod{2st}$},\\
-1& \text{if $k\equiv \pm(nt+ms)\pmod{2st}$},\\
0 &\text{otherwise}.
\end{cases}
\end{aligned}$$ For coprime odd integers $s$, $t$, define the sets $$\begin{aligned}
 \label{d1}
\mathscr{D}_1(s, t)&:=\left\{(n, m): 1\le n\le \frac{s-1}{2}, 1\le m\le t-1\right\}
\end{aligned}$$ and $$\begin{aligned}
 \label{d2}
\mathscr{D}_2(s, t)&:=\left\{(n, m): 1\le n\le s-1, 1\le m\le \frac{t-1}{2}\right\}.
\end{aligned}$$ There is a bijection between $\mathscr{D}_1(s, t)$ and $\mathscr{D}_2(s, t)$ (see Lemma [\[scha\]](#scha){reference-type="ref" reference="scha"} and [\[bi\]](#bi){reference-type="eqref" reference="bi"}). For $s$ and $t$ coprime and of opposite parities, we consider $$\begin{aligned}
\mathscr{D}_3(s, t):=
\begin{cases}
\left\{(n, m): 1\le n\le \frac{s-1}{2}, 1\le m\le t-1\right\} & \text{if $s\equiv 1\!\!\!\pmod{2}$},\\
\left\{(n, m): 1\le n\le s-1, 1\le m\le \frac{t-1}{2}\right\} & \text{if $s\equiv 0\!\!\!\pmod{2}$}.
\end{cases}
\end{aligned}$$ Finally, define the set $\mathscr{D}(s, t)$ of pairs which yield distinct characters in ([\[pf\]](#pf){reference-type="ref" reference="pf"}) as follows: $$\begin{aligned}
 \label{d}
\mathscr{D}(s, t):=
\begin{cases}
\mathscr{D}_1(s, t)\quad \text{or}\quad \mathscr{D}_2(s, t) & \text{if $s\equiv t\equiv 1\!\!\!\pmod{2}$},\\
\mathscr{D}_3(s, t) & \text{if $s\not\equiv t\!\!\!\pmod{2}$}.
\end{cases}    
\end{aligned}$$ One sees that $D(s, t):=|\mathscr{D}(s, t)|=\frac{(s-1)(t-1)}{2}$.

::: theorem
[]{#main2 label="main2"} Let $s$ and $t$ be coprime positive integers and $(n,m) \in \mathscr{D}(s,t)$. For $0 \neq \alpha \in \mathbb{Q}$, we have $$S_{\chi_{s,t}^{(n,m)}}^{\bf{med}}\left(-\frac{1}{2\pi i\alpha}\right) = \theta_{0,4st,\chi_{s,t}^{(n,m)}}^{(1)}(\alpha).$$
:::

The second result verifies Conjecture [\[cgconj\]](#cgconj){reference-type="ref" reference="cgconj"} for two families of torus knots.

::: corollary
[]{#cor label="cor"} Let $u,k\in\mathbb{Z}_{\geq 1}$. Conjecture [\[cgconj\]](#cgconj){reference-type="ref" reference="cgconj"} is true for the families of torus knots $T(2, 2u+1)$ and $T(3, 2^k)$.
:::

Corollary [\[cor\]](#cor){reference-type="ref" reference="cor"} generalizes Theorems 2.5 and 3.1 in [@cg] and upon taking either $u=1$ or $k=1$ confirms Conjecture [\[cgconj\]](#cgconj){reference-type="ref" reference="cgconj"} for the trefoil knot $3_1 = T(2,3)=T(3,2)$.

The paper is organized as follows. In Section [1](#sec:proof-main-thm){reference-type="ref" reference="sec:proof-main-thm"}, we prove Theorem [\[main\]](#main){reference-type="ref" reference="main"} by first providing an explicit evaluation of $G_{f}(p)$ in [\[BT\]](#BT){reference-type="eqref" reference="BT"}, which generalizes [\[g31\]](#g31){reference-type="eqref" reference="g31"}, and then computing $S_{f}^{\textbf{med}}(x)$ directly via a careful contour deformation argument. In Section [2](#sec:torus){reference-type="ref" reference="sec:torus"}, we prove Theorem [\[main2\]](#main2){reference-type="ref" reference="main2"} and Corollary [\[cor\]](#cor){reference-type="ref" reference="cor"}. In Section [\[sec:remarks\]](#sec:remarks){reference-type="ref" reference="sec:remarks"}, we make some concluding remarks.

# Proof of Theorem [\[main\]](#main){reference-type="ref" reference="main"} {#sec:proof-main-thm}

::: proof
*Proof of Theorem [\[main\]](#main){reference-type="ref" reference="main"}.* The Borel transform of $\mathcal{F}_f(1/x)$ from [\[F\]](#F){reference-type="eqref" reference="F"} is given by $$\mathcal{B}[\mathcal{F}_{f}](p) = C_M \delta + G_f(p)$$ where $$C_M = -\frac{M}{2} \sum_{m=1}^{M} f(m) B_{2}\left(\dfrac{m}{M}\right)$$ and $$\label{gfp}
\begin{aligned}
G_f(p) & = \sum_{n=1}^{\infty} \frac{(-1)^{n+1} M^{2n+1}}{(2n+2) n!} \sum_{m=1}^{M} f(m) B_{2n+2}\left(\dfrac{m}{M}\right) \frac{p^{n-1}}{(n-1)! b^n} \\
& = M \sum_{n=0}^{\infty} \sum_{m=1}^{M} \frac{(-1)^n f(m) B_{2n+4}\left(\dfrac{m}{M}\right)}{(2n+4)!} \frac{(2n+3)!}{n! (n+1)!} \left( \frac{M^2}{b} \right)^{n+1} p^n.
\end{aligned}$$ From the generating function $$\begin{aligned}
\label{Berpolygen}
\dfrac{xe^{xt}}{e^x-1}=\sum_{n=0}^\infty\dfrac{B_n(t)}{n!}x^n, 
\end{aligned}$$ where $|x|<2\pi$, we deduce $$\begin{aligned}
 \label{b}
\sum_{n=0}^{\infty} \dfrac{B_{2n}(t)}{(2n)!}x^{2n}=\dfrac{x}{2}\left(\dfrac{e^{xt}}{e^x-1}-\dfrac{e^{-xt}}{e^{-x}-1}\right)=\dfrac{x(e^{xt}+e^{-(t-1)x})}{2(e^{x}-1)}.\label{evenBer}   
\end{aligned}$$ Assuming $|y|<\frac{2\pi}{M}$, $x=iMy$, and taking $t=\frac{m}{M}$, where $1\leq m\leq M$, we use ([\[b\]](#b){reference-type="ref" reference="b"}) to obtain $$\begin{aligned}
 \label{yep}
\dfrac{1}{My}\sum_{m=1}^Mf(m)\sum_{n=0}^\infty\dfrac{B_{2n+2}\left(\frac{m}{M}\right)}{(2n+2)!}\left(iMy\right)^{2n+2}&=\dfrac{i}{2(e^{iMy}-1)}\sum_{m=1}^{M} f(m)\left(e^{imy}+e^{-i(m-M)y} \right) \notag \\
&=-2c\cdot\dfrac{\sin\left(\frac{(k_2-k_1)y}{2}\right)\sin\left(\frac{(M-k_1-k_2)y}{2}\right)}{\sin\left(\frac{My}{2}\right)}.
\end{aligned}$$ If we let $y=\sqrt{p}$ in ([\[yep\]](#yep){reference-type="ref" reference="yep"}), then $$\begin{aligned}
\notag g_{1,f}(p)&:=M^{3} \sum_{n=0}^{\infty}\sum_{m=1}^M f(m)\dfrac{B_{2n+4}\left(\frac{m}{M}\right)}{(2n+4)!}\,  (-M^2p)^{n}\\
&= \frac{1}{Mp^2}\sum_{n=0}^{\infty}\sum_{m=1}^M f(m)\dfrac{B_{2n+2}\left(\frac{m}{M}\right)}{(2n+2)!}\,  (-M^2p)^{n+1} - \frac{C_M}{p}\notag\\
&\label{f1}= -\dfrac{1}{p^{3/2}}\left(2c\cdot\dfrac{\sin\left(\frac{(k_2-k_1)\sqrt{p}}{2}\right)\sin\left(\frac{(M-k_1-k_2)\sqrt{p}}{2}\right)}{\sin\left(\frac{M\sqrt{p}}{2}\right)} + C_M\sqrt{p}\right).
\end{aligned}$$ We conclude $$\begin{aligned}
G_f(p)=(g_{1,f}\circledast g_{2,f})(p)    
\end{aligned}$$ where $g_{1,f}$ was computed in [\[f1\]](#f1){reference-type="eqref" reference="f1"} and $$\begin{aligned}
g_{2,f}(p)&:=\sum_{n=0}^{\infty} \dfrac{(2n+3)!}{n!(n+1)!}\Big(\dfrac{1}{b}\Big)^{n+1} p^{n} =\dfrac{1}{b}\dfrac{6}{ \left(1-4\frac{p}{b} \right)^{5/2}} 
\end{aligned}$$ and $\circledast$ denotes the Hadamard product of two formal power series $$\begin{aligned}
\Biggl( \sum_{n=0}^{\infty} a_n p^n \Biggr) \circledast \Biggl( \sum_{n=0}^{\infty} b_n p^n \Biggr) := \sum_{n=0}^{\infty} a_n b_n p^n.
\end{aligned}$$ It now follows that $$\begin{aligned}
\label{int}
G_f(p)=\dfrac{1}{2\pi i}\int_{-\gamma} g_{1,f}(s)g_{2,f}\left(\frac{p}{s}\right)\dfrac{ds}{s}    
\end{aligned}$$ where $\gamma$ is a circle with center at the origin and a small radius oriented clockwise (see Figure [2](#fig:fig2){reference-type="ref" reference="fig:fig2"}).

<figure id="fig:fig2">

<figcaption>Contour deformation of <span class="math inline"><em>γ</em><sub><em>R</em></sub> − <em>γ</em></span></figcaption>
</figure>

Now, we consider the poles of $g_{1,f}(s)$. Note that there is no pole at $s=0$. By [\[f1\]](#f1){reference-type="eqref" reference="f1"}, they are supported where $p=\frac{4\ell^2\pi^2}{M^2}$, $\ell \in \mathbb{Z}$. However, $$\begin{aligned}
\sin\left(\frac{(k_2-k_1)\sqrt{p}}{2}\right)\sin\left(\frac{(M-k_1-k_2)\sqrt{p}}{2}\right)=0
\end{aligned}$$ when $p=\dfrac{4k^2\pi^2}{(k_2-k_1)^2}$ or $p=\dfrac{4k^2\pi^2}{(M-k_2-k_1)^2}$ for $k\in\mathbb{Z}$. Thus, if for some $k, \ell\in\mathbb{Z}$ $$\begin{aligned}
\ell=\dfrac{Mk}{k_2-k_1} \quad\text{or}\quad \ell=\dfrac{Mk}{M-k_2-k_1}
\end{aligned}$$ which is true if and only if $$\begin{aligned}
 \label{coml}
\ell = \dfrac{\frac{M}{\text{gcd}(M, \, k_2-k_1)}k}{\frac{(k_2-k_1)}{\text{gcd}(M,\, k_2-k_1)}}\quad\text{or}\quad \ell=\dfrac{\frac{M}{\text{gcd}(M,\, M-k_2-k_1)}k}{\frac{(M-k_2-k_1)}{\text{gcd}(M,\, M-k_2-k_1)}},
\end{aligned}$$ then $g_{1,f}(s)$ does not have poles at $p=\frac{4\ell^2\pi^2}{M^2}$. Thus, the set of poles of $g_{1,f}(s)$ is given by $$\begin{aligned}
\label{sing}
\mathcal{N}_{1,f}=\left\{\frac{4\ell^2\pi^2}{M^2} :  \ell\in\mathbb{N}, \frac{M}{\text{gcd}(M,k_2-k_1)}\nmid\ell\; \; \text{or} \;\; \frac{M}{\text{gcd}(M,M-k_2-k_1)}\nmid\ell\right\}. 
\end{aligned}$$ We next carefully calculate the residues of the poles of the integrand [\[int\]](#int){reference-type="eqref" reference="int"} which are given by [\[sing\]](#sing){reference-type="eqref" reference="sing"}. Take a circle $\gamma_R$ with center at the origin and of large radius $R$ which encloses a finite number of points $N$ in $\mathcal{N}_{1,f}$. Thus,

$$\begin{aligned}
  \label{largeR}
& \dfrac{1}{2\pi i}\int_{\gamma_R \, \cup \, \gamma} g_{1,f}(s)g_{2,f}\left(\frac{p}{s}\right)\dfrac{ds}{s} = \sum_{\substack{p_i\in\mathcal{N}_{1,f}\\1\leq i\leq N}}\text{Res}_{s\to p_i}\left(\dfrac{g_{1,f}(s)g_{2,f}(\tfrac{p}{s})}{s}\right) \nonumber \\
&= \sideset{}{^N} \sum_{\ell \in \mathbb{N}} \dfrac{g_{2,f}\left(\frac{p M^2}{4\ell^2\pi^2}\right)}{\left(\frac{4\ell^2\pi^2}{M^2}\right)}\nonumber  \\
& \quad \quad \quad \quad \times \lim_{s\rightarrow \frac{4\ell^2\pi^2}{M^2}}\left(s-\frac{4\ell^2\pi^2}{M^2}\right)\left[-\dfrac{1}{s^{3/2}} \left(2c\cdot\dfrac{\sin\left(\frac{(k_2-k_1)\sqrt{s}}{2}\right)\sin\left(\frac{(M-k_1-k_2)\sqrt{s}}{2}\right)}{\sin\left(\frac{M\sqrt{s}}{2}\right)} + C_M\sqrt{s}\right)\right] \nonumber \\
&=-\dfrac{3\pi c}{bM^2}\sideset{}{^N}\sum_{\ell\in\mathbb{N}}\dfrac{\ell \tilde{f}(\ell)}{\left(\frac{\ell^2\pi^2}{M^2}-\frac{p}{b}\right)^{5/2}} 
\end{aligned}$$

where $\sideset{}{^N}\sum$ means that $\ell$ runs over the first $N$ elements $\frac{4\ell^2\pi^2}{M^2}$ of $\mathcal{N}_{1,f}$ and $\tilde{f}(\ell)$ is given by ([\[ftilde\]](#ftilde){reference-type="ref" reference="ftilde"}). It follows that $$\begin{aligned}
 \label{lim}
\left|\int_{\gamma_R}g_{1,f}(s)g_{2,f}\left(\frac{p}{s}\right)\dfrac{ds}{s}\right|\rightarrow 0 
\end{aligned}$$ as $R\to\infty$. Thus, [\[int\]](#int){reference-type="eqref" reference="int"}, [\[largeR\]](#largeR){reference-type="eqref" reference="largeR"}, [\[lim\]](#lim){reference-type="eqref" reference="lim"} and the contour deformation given in Figure [2](#fig:fig2){reference-type="ref" reference="fig:fig2"} imply that $$\begin{aligned}
 \label{BT}
G_f(p)=\dfrac{3\pi c}{M^2b} \sum_{\ell =1}^{\infty} \dfrac{\ell \tilde{f}(\ell)}{\left(\frac{\ell^2\pi^2}{M^2}-\frac{p}{b}\right)^{5/2}}.    
\end{aligned}$$

The set of poles of $G_f(p)$ is then $$\begin{aligned}
 \label{poles}
\mathcal{N}:=\left\{\frac{b\ell^2\pi^2}{M^2} : \ell\in\mathbb{N}, \frac{M}{\text{gcd}(M,k_2-k_1)}\nmid\ell\;\text{or}\;\frac{M}{\text{gcd}(M,M-k_2-k_1)}\nmid\ell\right\}. 
\end{aligned}$$ Since $G_f(p)$ has two branches, by considering the cut complex plane $\mathbb{C}\setminus \mathcal{N}$, it can be made analytic in this region. This implies (1). We now compute $S^{\pm}[\mathcal{F}_f](x)$: $$\begin{aligned}
\label{eq:lateral_BL}
S^{\pm}[\mathcal{F}_f](x)=\int_0^{e^{\pm i\theta}\infty}e^{-px}\mathcal{B}[\mathcal{F}_f](p) \, dp&= C_M + \frac{3\pi c}{M^2b}\sum_{\ell =1}^{\infty} \ell \tilde{f}(\ell)\int_0^{e^{\pm i\theta}\infty} \frac{e^{-px}}{\Big(\frac{\ell^2\pi^2}{M^2}-\frac{p}{b}\Big)^{5/2}} dp
\end{aligned}$$ where the integral $\int_0^{e^{+ i\theta}\infty}$ agrees with $\int_0^{+i\infty}$ if $\Im (x)>0$ and the integral $\int_0^{e^{- i\theta}\infty}$ agrees with $\int_0^{-i\infty}$ if $\Im (x)<0$. To prove the first part of (2), we start with the following formula, valid for $\Re(x)>0$: $$\label{errorf}
\int_{\gamma}\dfrac{e^{-px}}{(1-p)^{\frac{5}{2}}} \, dp=-\dfrac{4}{3}+\dfrac{8}{3}\sqrt{\pi} \mathcal{E}(\sqrt{x})$$ where $\gamma=[0,e^{i\theta} \infty) \cup [0,e^{-i\theta}\infty)$ and $$\begin{aligned}
\mathcal{E}(y):=\dfrac{2y^3e^{-y^2}}{\sqrt{\pi}}\int_0^ye^{t^2}dt-\dfrac{y^2}{\sqrt{\pi}}.    
\end{aligned}$$ From ([\[smed\]](#smed){reference-type="ref" reference="smed"}) and [\[eq:lateral_BL\]](#eq:lateral_BL){reference-type="eqref" reference="eq:lateral_BL"}, we have $$\begin{aligned}
\label{Smed}
S^{\textbf{med}}_f(x) &= C_M + \frac{1}{2} \frac{3\pi c}{M^2b}\sum_{\ell =1}^{\infty} \ell \tilde{f}(\ell) \int_{\gamma} \frac{e^{-px}}{\Big(\frac{\ell^2\pi^2}{M^2}-\frac{p}{b}\Big)^{5/2}}dp\notag\\
&= C_M + b\left(\dfrac{M}{\pi}\right)^3\dfrac{3\pi c}{2 M^2 b} \sum_{\ell =1}^{\infty} \dfrac{\tilde{f}(\ell)}{\ell} \int_{\gamma}\dfrac{e^{-\frac{bp\ell^2\pi^2 x}{M^2}}}{\left(1-p\right)^{5/2}} \, dp
\end{aligned}$$ where we have made the change of variable $p\rightarrow \frac{bp\ell^2\pi^2}{M^2}$. Thus, [\[errorf\]](#errorf){reference-type="eqref" reference="errorf"} and [\[Smed\]](#Smed){reference-type="eqref" reference="Smed"} imply $$\begin{aligned}
S^{\textbf{med}}_f(x) &= C_M + \dfrac{3Mc}{2 \pi^2} \sum_{\ell =1}^{\infty} \dfrac{\tilde{f}(\ell)}{\ell} \left\{-\dfrac{4}{3}+\dfrac{8}{3}\sqrt{\pi} \mathcal{E}\left(\dfrac{\ell\pi}{M}\sqrt{bx}\right)\right\}\notag\\
&=\dfrac{4Mc}{\pi^{3/2}} \sum_{\ell =1}^{\infty} \dfrac{\tilde{f}(\ell)}{\ell} \, \mathcal{E}\left(\dfrac{\ell\pi}{M}\sqrt{bx}\right)
\end{aligned}$$ where one can check that $$\label{cm}
C_M = \frac{2Mc}{\pi^2} \sum_{\ell=1}^{\infty} \frac{\tilde{f}(\ell)}{\ell^2}.$$ This implies that $S_f^{\textbf{med}}(x)$ is analytic on $\Re(x) > 0$.

To prove the existence of the radial limit and part (3), we begin with rewriting the integral on the right-hand side of [\[eq:lateral_BL\]](#eq:lateral_BL){reference-type="eqref" reference="eq:lateral_BL"} as an integral of the partial theta function $\theta_{0,4M^2,\tilde{f}}^{(0)}(x)$. This requires some attention due to the branch cut singularity of the resulting square root. Integration by parts yields $$\begin{aligned}
 \label{parts}
 \int_0^{e^{\pm i\theta}\infty} \frac{e^{-px}}{\Big(\frac{\ell^2\pi^2}{M^2}-\frac{p}{b}\Big)^{5/2}} dp&=
\left [ \frac{2b}{3}\frac{e^{-px}}{\Big(\frac{\ell^2\pi^2}{M^2}-\frac{p}{b}\Big)^{3/2}} \right ]_0^{e^{\pm i\theta}\infty}+\frac{2bx}{3}\int_0^{e^{\pm i\theta}\infty} \frac{e^{-px}}{\Big(\frac{\ell^2\pi^2}{M^2}-\frac{p}{b}\Big)^{3/2}} dp \notag \\
&=\frac{2b}{3} \left [-\frac{M^3}{\ell^3\pi^3}+x\int_0^{xe^{\pm i\theta}\infty} \frac{e^{-\frac{\ell^2\pi^2 b}{M^2}p}}{\Big(\frac{\ell^2\pi^2}{M^2}-\frac{\ell^2\pi^2}{M^2x}p\Big)^{3/2}} d\left( \frac{\ell^2\pi^2b}{M^2x}p \right) \right ] \notag \\
&= -\frac{2bM^3}{3\ell^3\pi^3} + \frac{2b^2 M}{3 \ell \pi} \int_0^{xe^{\pm i\theta}\infty} \frac{e^{-\frac{\ell^2\pi^2b}{M^2}p}}{\Big(1-\frac{p}{x}\Big)^{3/2}} dp.
\end{aligned}$$ The change of coordinate $x \rightarrow -\frac{1}{2\pi i\alpha}$ where $0 \neq \alpha \in \mathbb{C}$ to ([\[parts\]](#parts){reference-type="ref" reference="parts"}) yields $$\begin{aligned}
 \label{change}
 -\frac{2bM^3}{3\ell^3\pi^3}  + \frac{2b^2 M}{3 \ell \pi} \int_0^{xe^{\pm i\theta}\infty} \frac{e^{-\frac{\ell^2\pi^2b}{M^2}p}}{\Big(1-\frac{p}{x}\Big)^{3/2}} dp 
&=-\frac{2bM^3}{3\ell^3\pi^3} + \frac{2b^2 M}{3 \ell \pi} \int_0^{-\frac{1}{2\pi i\alpha}e^{\pm i\theta}\infty} \frac{e^{2\pi i\frac{\ell^2 2\pi i b}{4M^2}p}}{\big(1+2\pi i p\alpha\big)^{3/2}} dp \notag \\
&=-\frac{2bM^3}{3\ell^3\pi^3} + \frac{b^2M}{3i\ell \pi^2} \int_0^{-\frac{1}{\alpha}e^{\pm i\theta}\infty} \frac{e^{2\pi i\frac{\ell^2  b}{4M^2}p}}{\big(1+ p\alpha\big)^{3/2}} dp.
\end{aligned}$$ Now $(1+p\alpha)^{3/2}$ has a branch cut at $p=-1/\alpha$, hence we distinguish between $\Re(\alpha)>0$ and $\Re(\alpha)<0$ (see Figure [3](#fig:branch){reference-type="ref" reference="fig:branch"}). If $\Re(\alpha)>0$, then $(1+p\alpha)^{3/2}=\alpha^{3/2}(1/\alpha+p)^{3/2}$, and the integral at angle $-i\theta$ will not change sign as the path is not crossing the branch cut, i.e., $\int_0^{-\frac{1}{\alpha}e^{ -i\theta}\infty}=\int_0^{+i\infty}$. If $\Re(\alpha)<0$, then $(1+p\alpha)^{3/2}=\alpha^{3/2}(1/\alpha+p)^{3/2}$, but the integral at angle $+i\theta$ will change sign as the path is crossing the branch cut, i.e., $\int_0^{-\frac{1}{\alpha}e^{+i\theta}\infty}=-\int_0^{+i\infty}$.

<figure id="fig:branch">

<figcaption>Branch cut of <span class="math inline">(1+<em>p</em><em>α</em>)<sup>3/2</sup></span>. On the left for <span class="math inline">ℜ(<em>α</em>) &lt; 0</span> and on the right for <span class="math inline">ℜ(<em>α</em>) &gt; 0</span>.</figcaption>
</figure>

By [\[eq:lateral_BL\]](#eq:lateral_BL){reference-type="eqref" reference="eq:lateral_BL"}, [\[cm\]](#cm){reference-type="eqref" reference="cm"} and [\[change\]](#change){reference-type="eqref" reference="change"}, we have for $\alpha\in\mathbb{Q}_{>0}$ $$\begin{aligned}
\int_0^{e^{-i\theta}\infty} e^{\frac{p}{2\pi i\alpha}}\, \mathcal{B}[\mathcal{F}_f](p) \,dp &=-i\frac{c b }{M\pi}\sum_{\ell =1}^{\infty}\tilde{f}(\ell) \int_0^{-\frac{1}{\alpha}e^{- i\theta}\infty} \frac{e^{2\pi i\frac{\ell^2  b}{4M^2}p}}{\big(1+ p\alpha\big)^{3/2}} dp \nonumber \\
&=-i\frac{ c b }{M\pi \alpha^{3/2}}\sum_{\ell =1}^{\infty} \tilde{f}(\ell) \int_0^{+i\infty} \frac{e^{2\pi i\frac{\ell^2  b}{4M^2}p}}{\big(1/\alpha+ p\big)^{3/2}} dp \nonumber \\
&=-i\frac{c b }{M\pi \alpha^{3/2}}\int_0^{+i\infty} \frac{\theta_{0,4M^2,\tilde{f}}^{(0)}(bp)}{\big(1/\alpha+ p\big)^{3/2}} dp
\end{aligned}$$ while for $\alpha\in\mathbb{Q}_{<0}$, we obtain $$\begin{aligned}
\int_0^{e^{+ i\theta}\infty} e^{\frac{p}{2\pi i\alpha}}\, \mathcal{B}[\mathcal{F}_f](p) \,dp &=-i\frac{c b }{M\pi}\sum_{\ell =1}^{\infty} \tilde{f}(\ell) \int_0^{-\frac{1}{\alpha}e^{+i\theta}\infty} \frac{e^{2\pi i\frac{\ell^2  b}{4M^2}p}}{\big(1+ p\alpha\big)^{3/2}} dp \nonumber \\
&= i\frac{c b }{M\pi \alpha^{3/2}} \sum_{\ell=1}^{\infty} \tilde{f}(\ell) \int_0^{+i\infty} \frac{e^{2\pi i\frac{\ell^2  b}{4M^2}p}}{\big(1/\alpha+ p\big)^{3/2}} dp \nonumber \\
&=i\frac{c b }{M\pi \alpha^{3/2}}\int_0^{+i\infty} \frac{\theta_{0,4M^2,\tilde{f}}^{(0)}(bp)}{\big(1/\alpha+ p\big)^{3/2}} dp.
\end{aligned}$$ We now compute the discontinuity $\mathrm{disc}^0(x)$ across the positive real axis: $$\label{disc}
\begin{aligned}
\mathrm{disc}^0(x) &:= S^{+}[\mathcal{F}_f](x) - S^{-}[\mathcal{F}_f](x)  \\
&=\frac{3\pi c}{M^2b}\sum_{\ell =1}^{\infty} \ell \tilde{f}(\ell) \left[\int_0^{e^{+i\theta}\infty}\frac{e^{-px}}{\big(\frac{\ell^2\pi^2}{M^2}-\frac{p}{b}\big)^{5/2}}dp - \int_0^{e^{-i\theta}\infty}\frac{e^{-px}}{\big(\frac{\ell^2\pi^2}{M^2}-\frac{p}{b}\big)^{5/2}}dp\right] \\
&= \frac{3\pi c}{M^2b}\sum_{\ell =1}^{\infty} \ell \tilde{f}(\ell) \int_{\mathcal{C}} \frac{e^{-px}}{\big(\frac{\ell^2\pi^2}{M^2}-\frac{p}{b}\big)^{5/2}}dp \\
&= \frac{3\pi cb^{3/2}}{M^2}\sum_{\ell =1}^{\infty} \ell \tilde{f}(\ell) e^{-\frac{\ell^2\pi^2 b}{M^2}x} \int_{\mathcal{C}_{\ell}} \frac{e^{-px}}{(-p)^{5/2}}\, dp \\
&=\frac{3\pi cb^{3/2}\,}{M^2} \sum_{\ell =1}^{\infty} \ell \tilde{f}(\ell) e^{-\frac{\ell^2\pi^2 b}{M^2}x} \int_{\mathcal{C}_{\ell}} \frac{e^{-px}}{(-xp)^{5/2}}\, d(xp) x^{3/2} \\
&=\frac{2\pi i}{\Gamma\big(\frac{5}{2}\big)}x^{3/2}\frac{3\pi cb^{3/2}}{M^2} \sum_{\ell =1}^{\infty}  \ell \tilde{f}(\ell) e^{-\frac{\ell^2\pi^2 b}{M^2}x} \\
&=2i\, (2b \pi x)^{3/2}\frac{ \sqrt{2} c }{M^2} \sum_{\ell=1}^{\infty}  \ell \tilde{f}(\ell) e^{-\frac{\ell^2\pi^2 b}{M^2}x} \\
& = 2i\, (2b \pi x)^{3/2}\frac{ \sqrt{2} c }{M^2} \theta^{(1)}_{0,4M^2,\tilde{f}}(2\pi ix). 
\end{aligned}$$ Here, $\mathcal{C}_\ell=\mathcal{C}-\tfrac{\ell^2\pi^2b}{M^2}$ where $\mathcal{C}$ is the Hankel contour enclosing the branch point singularity arising from the second line in [\[disc\]](#disc){reference-type="eqref" reference="disc"}, as in Figure [4](#fig:Hankel){reference-type="ref" reference="fig:Hankel"}. The radial limit $x \to -\frac{1}{2\pi i\alpha}$ of the partial theta series appearing in the last line of [\[disc\]](#disc){reference-type="eqref" reference="disc"} exists by [@akl Proposition 3.1] and so $$\mathrm{disc}^0\Big(-\frac{1}{2\pi i\alpha}\Big) = 2i\, \Big(\frac{ib}{\alpha} \Big)^{3/2}\frac{ \sqrt{2} c }{M^2}\, \theta_{0,4M^2,\tilde{f}}^{(1)}\left(-\frac{b}{\alpha}\right).$$

<figure id="fig:Hankel">

<figcaption>The Hankel contour <span class="math inline">𝒞</span> for the discontinuity <span class="math inline">disc<sup>0</sup>(<em>x</em>)</span>.</figcaption>
</figure>

In addition, the radial limit $x \to -\frac{1}{2\pi i\alpha}$ also exists for $S^{\pm}[\mathcal{F}_f](x)$ since they are analytic functions on the half-planes $\Re(e^{\pm i\theta}x)>0$, respectively (see the change of coordinates after [\[parts\]](#parts){reference-type="eqref" reference="parts"}). Thus, the second part of (2) follows. Summarizing, we find that $${S}^{\mathbf{med}}_f\left(-\frac{1}{2\pi i\alpha}\right)
=\begin{cases}
S^{+}\left(-\dfrac{1}{2\pi i\alpha}\right)+\, \Big(\dfrac{b}{\alpha} \Big)^{3/2} e^{\pi i/4}\dfrac{ \sqrt{2} c }{M^2}\, \theta_{0,4M^2,\tilde{f}}^{(1)}\left(-\frac{b}{\alpha}\right)
 & \text{if $\alpha\in\mathbb{Q}_{>0}$}, \\
&\\
S^{-}\left(-\dfrac{1}{2\pi i\alpha}\right)-\, \Big(\dfrac{b}{\alpha} \Big)^{3/2} e^{\pi i/4} \dfrac{ \sqrt{2} c }{M^2}\, \theta_{0,4M^2,\tilde{f}}^{(1)}\left(-\frac{b}{\alpha}\right)
& \text{if $\alpha\in\mathbb{Q}_{<0}$}
\end{cases}$$ with $${S}^\pm\left(-\frac{1}{2\pi i\alpha}\right)=\mp i\frac{c b}{M\pi \alpha^{3/2}}\int_0^{+i\infty} \frac{\theta_{0,4M^2,\tilde{f}}^{(0)}(bp)}{\big(1/\alpha+ p\big)^{3/2}} dp.$$ Finally, noticing that $(i\alpha)^{-3/2}=\mp e^{\pi i/4}\alpha^{-3/2}$ depending on the sign of $\alpha$ and on our choice of the branch of the square root, part (3) follows. ◻
:::

# Proof of Theorem [\[main2\]](#main2){reference-type="ref" reference="main2"} and Corollary [\[cor\]](#cor){reference-type="ref" reference="cor"} {#sec:torus}

In order to prove Theorem [\[main2\]](#main2){reference-type="ref" reference="main2"} and Corollary [\[cor\]](#cor){reference-type="ref" reference="cor"}, we require some general preliminaries. Recall the periodic function $\chi_{s,t}^{(n,m)}(k)$ given by [\[pf\]](#pf){reference-type="eqref" reference="pf"}.

::: lemma
[]{#scha label="scha"} For all $k\in\mathbb{Z}$, $1\le m\le t-1$ and $1\le n\le s-1$, we have $$\begin{aligned}
\chi_{s,t}^{(n,m)}(k)=\chi_{s,t}^{(s-n,t-m)}(k).    
\end{aligned}$$
:::

::: proof
*Proof.* By replacing $n\rightarrow s-n$ and $m\rightarrow t-m$, we see that $$\label{sym}
\begin{aligned}
\pm ((s-n)t-(t-m)s)&=\pm(ms-nt)=\mp(nt-ms)\,,\\
\pm ((s-n)t+(t-m)s)&=\pm(2st-ms-nt)\equiv \mp(nt+ms)\pmod{2st}\,,     
\end{aligned}$$ and thus the result follows from [\[sym\]](#sym){reference-type="eqref" reference="sym"}. ◻
:::

In view of Lemma [\[scha\]](#scha){reference-type="ref" reference="scha"}, the map $$\begin{aligned}
 \label{bi}
(n, m)\xrightarrow[]{} \begin{cases}
(n, m)& \text{if $1\le n\le \frac{s-1}{2}, \quad 1\le m\le \frac{t-1}{2}$},\\
(s-n, t-m) &\text{otherwise}.
\end{cases}    
\end{aligned}$$ is a bijection between the pairs defined by $\mathscr{D}_1(s, t)$ and $\mathscr{D}_2(s, t)$ in [\[d1\]](#d1){reference-type="eqref" reference="d1"} and [\[d2\]](#d2){reference-type="eqref" reference="d2"}, respectively.

::: lemma
[]{#distinct label="distinct"} Let $s$ and $t$ be coprime positive integers and $\mathscr{D}(s,t)$ be the set given by ([\[d\]](#d){reference-type="ref" reference="d"}). Then the integers in the set $$\label{set1}
\mathscr{S} = \{\pm(nt\pm ms): (n,m)\in\mathscr{D}(s,t)\}$$ are distinct and thus $| \mathscr{S} | = 2(s-1)(t-1)$.
:::

::: proof
*Proof.* We assume that $s$ and $t$ are coprime odd integers. A similar argument applies when $s$ and $t$ are of opposite parities. Let us consider two integers of the forms $n_1t+m_1s$ and $n_2t+m_2s$ where $-\frac{s-1}{2}\le n_1, n_2\leq \frac{s-1}{2}$ and $-(t-1)\le m_1, m_2\leq t-1$. Then $$\begin{aligned}
\label{liceq}
n_1t+m_1s=n_2t+m_2s\iff (n_1-n_2)t+(m_1-m_2)s=0.    
\end{aligned}$$ Since $s$ and $t$ are coprime, [\[liceq\]](#liceq){reference-type="eqref" reference="liceq"} implies that $s\mid (n_1-n_2)$, which yields $|n_1-n_2|\ge s$. On the other hand, since $-\frac{s-1}{2}\le n_1, n_2\leq \frac{s-1}{2}$, we obtain $-(s-1)\leq n_1-n_2\leq s-1$, or equivalently, $|n_1-n_2|\le s-1$, a contradiction. This shows that $n_1=n_2$ and thus [\[liceq\]](#liceq){reference-type="eqref" reference="liceq"} implies that $m_1=m_2$. ◻
:::

Define $$\begin{aligned}
S_{n, \, m}^{n',\,m'}=\sqrt{\dfrac{8}{st}}(-1)^{nm'+mn'+1}\sin\left(\frac{nn't}{s}\pi\right)\sin\left(\frac{mm's}{t}\pi\right).    
\end{aligned}$$

::: proposition
[]{#gentor label="gentor"} For all $k\in\mathbb{Z}$, and $(n, m)\in \mathscr{D}(s, t)$, we have $$\label{keyform}
\tilde{\chi}_{s,t}^{(n,m)}(k)=-\sqrt{\dfrac{st}{8}}\sum_{(n',\,m')\in \mathscr{D}(s, t)} S_{n, \, m}^{n',\,m'} \chi_{s,t}^{(n',\,m')}(k).$$
:::

::: proof
*Proof.* We assume that $nt - ms > 0$. A similar argument holds for $nt - ms < 0$. By [\[ftilde\]](#ftilde){reference-type="eqref" reference="ftilde"}, we have $$\begin{aligned}
 \label{tilchiano}
\tilde{\chi}_{s,t}^{(n,m)}(k)&=(-1)^k\sin\left(\dfrac{(nt+ms- |nt-ms|)k\pi}{2st}\right)\sin\left(\dfrac{(2st- |nt-ms| - (nt+ms))k\pi}{2st}\right) \nonumber \\   
& =(-1)^k\sin\left(\dfrac{mk\pi}{t}\right)\sin\left(\dfrac{(s-n)k\pi}{s}\right) \nonumber \\
& =-\sin\left(\frac{mk\pi}{t}\right)\sin\left(\frac{nk\pi}{s}\right).
\end{aligned}$$ Clearly, the support of $\tilde{\chi}_{s,t}^{(n,m)}$ is contained within the set of integers $k$ such that $s\nmid k$ and $t\nmid k$. By inclusion-exclusion, the total number of integers between $0$ and $2st-1$ which are either multiples of $s$ or $t$ is $2s+2t-2$. By Lemma [\[distinct\]](#distinct){reference-type="ref" reference="distinct"}, the number of distinct integers $k=\pm(m's\pm n't)$ between $0$ and $2st-1$, where $(n',m')\in \mathscr{D}(s, t)$ is $2(s-1)(t-1)$. Since $\tilde{\chi}_{s,t}^{(n,m)}$ has period $2st$, this implies that the support of $\tilde{\chi}_{s,t}^{(n,m)}$ is contained in the following set of distinct integers $$\label{intgen}
\mathscr{T} = \{ \pm(m's\pm n't)\pmod{2st} \, : \, (n',m')\in\mathscr{D}(s,t)\}.$$ Thus it suffices to prove [\[keyform\]](#keyform){reference-type="eqref" reference="keyform"} for integers in $\mathscr{T}$. From [\[tilchiano\]](#tilchiano){reference-type="eqref" reference="tilchiano"}, we have $$\begin{aligned}
\label{tilchigenlin}
\tilde{\chi}_{s,t}^{(n,m)}(\pm(m's\pm n't))&=-\sin\left(\frac{\pm m(m's\pm n't)\pi}{t}\right)\sin\left(\frac{\pm n(m's\pm n't)\pi}{s}\right)\notag\\
&=-\sin\left(\pm mn'\pi+ \frac{mm's}{t}\pi\right)\sin\left( nm'\pi\pm \frac{ nn't}{s}\pi\right) \notag \\
&=\pm(-1)^{mn'+nm'+1}\sin\left(\frac{mm's}{t}\pi\right)\sin\left(\frac{nn't}{s}\pi\right) \notag\\
&=(-1)^{mn'+nm'}\sin\left(\frac{mm's}{t}\pi\right)\sin\left(\frac{nn't}{s}\pi\right)\chi_{s,t}^{(n',m')}(\pm(m's\pm n't))
\end{aligned}$$ where in the last step we use that the sign $\pm$ depends on the sign of $(m's\pm n't)$, and it is $-\chi_{s,t}^{(n',m')}(\pm(m's\pm n't))$. Since the integers in $\mathscr{T}$ are distinct, then from [\[tilchigenlin\]](#tilchigenlin){reference-type="eqref" reference="tilchigenlin"} we find: $$\begin{aligned}
\label{classgen}
\tilde{\chi}_{s,t}^{(n,m)}(\pm(m's\pm n't))=-\sqrt{\dfrac{st}{8}}\sum_{(n'',\,m'')\in\mathscr{D}(s,t)}S_{n, \, m}^{n'',\,m''}\chi_{s,t}^{(n'',\,m'')}(\pm(m's\pm n't)).    
\end{aligned}$$ It follows from [\[classgen\]](#classgen){reference-type="eqref" reference="classgen"} that [\[keyform\]](#keyform){reference-type="eqref" reference="keyform"} is true for integers $k$ given by [\[intgen\]](#intgen){reference-type="eqref" reference="intgen"}, which are non-multiples of $s$ or $t$ and between $0$ and $2st-1$. It remains to show that [\[keyform\]](#keyform){reference-type="eqref" reference="keyform"} remains true when $k$ is a multiple of $s$ or $t$. Without loss of generality, we assume that $k$ is a multiple of $s$. Then [\[tilchiano\]](#tilchiano){reference-type="eqref" reference="tilchiano"} implies that $\tilde{\chi}_{s,t}^{(n,m)}(k)=0$. Thus, it suffices to show that $\chi_{s,t}^{(n',\,m')}(k)=0$ for all $(n', m')\in\mathscr{D}(s, t)$. To this end, we note that since $s$ and $t$ are coprime, $s\mid \pm (n't\pm m's)$ if and only if $s\mid n'$, which implies that $n'\ge s$, a contradiction. Thus, for $(n', m')\in\mathscr{D}(s, t)$, it follows $\pm(n't\pm m's)\not\equiv 0\pmod{s}$. Hence $k\neq \pm(n't\pm m's)$, and $\chi_{s,t}^{(n',m')}(k)=0$. ◻
:::

Finally, we recall two key properties for the non-holomorphic Eichler integral $$\widehat{\Phi}^{(n,m)}(z) := \sqrt{\frac{sti}{8\pi^2}} \int_{\bar{z}}^{+i \infty} \frac{\theta_{0,4st,\chi_{s,t}^{(n,m)}}^{(0)}(\tau)}{(\tau - z)^{3/2}} d\tau$$ where $z \in \mathbb{H}^{-}$ [@HK1 Eqn. (16)]. For $z \in \mathbb{H}^{-}$ and $\alpha \in \mathbb{Q}$, consider the period function $$r^{(n,m)}(z; \alpha) := \sqrt{\frac{sti}{8\pi^2}} \int_{\alpha}^{+i \infty} \frac{\theta_{0,4st,\chi_{s,t}^{(n,m)}}^{(0)}(\tau)}{(\tau - z)^{3/2}} d\tau\,,$$ as defined in [@HK1 Eqn. (18)]. Then, we have $$\label{HKlast1}
\widehat{\Phi}^{(n,m)}(z) + \left(\frac{1}{iz}\right)^{3/2} \sum_{(n',\,m')\in\mathscr{D}(s,t)} S_{n, m}^{n', \,m'} \widehat{\Phi}^{(n',\,m')}\left(-\frac{1}{z}\right) = r^{(n,m)}(z;0)$$ and $$\label{HKlast2}
\widehat{\Phi}^{(n,m)}(\alpha) =  -\frac{1}{2} \theta_{0,4st,\chi_{s,t}^{(n,m)}}^{(1)}(\alpha)$$ where [\[HKlast1\]](#HKlast1){reference-type="eqref" reference="HKlast1"} is [@HK1 Eqn. (17)] and [\[HKlast2\]](#HKlast2){reference-type="eqref" reference="HKlast2"} is [@HK1 below Eqn. (19)].

::: proof
*Proof of Theorem [\[main2\]](#main2){reference-type="ref" reference="main2"}.* By Proposition [\[gentor\]](#gentor){reference-type="ref" reference="gentor"}, we have $$\label{eq:gentor}
\theta_{0, 4(2st)^2, \tilde{\chi}_{s,t}^{(n,m)}}^{(\nu)}(4st z) = -\sqrt{\dfrac{st}{8}} \sum_{(n',m')\in\mathscr{D}(s,t)} S_{n, m}^{n', m'} \theta_{0, 4st, \chi_{s,t}^{(n',m')}}^{(\nu)}(z).$$ Also, [@HK1 Eqn. (10)] states $$\label{transgen}
\theta_{0,4st,\chi_{s,t}^{(n',m')}}^{(0)}(z) = \sqrt{\frac{i}{z}} \sum_{(n',\,m')\in\mathscr{D}(s,t)} S_{n, m}^{n', \,m'}\theta_{0,4st,\chi_{s,t}^{(n',m')}}^{(0)}\left(-\frac{1}{z} \right)\,.$$ Applying Theorem [\[main\]](#main){reference-type="ref" reference="main"} part (3) and [\[eq:gentor\]](#eq:gentor){reference-type="eqref" reference="eq:gentor"} gives $$\begin{gathered}
 \label{compgen}
\displaystyle S_{\chi_{s,t}^{(n,m)}}^{\bf{med}} \left(-\frac{1}{2 \pi i \alpha} \right)  = -\frac{2e^{\pi i/4}}{ \pi (i \alpha)^{3/2}}\sqrt{\dfrac{st}{8}}  \int_{0}^{+ i\infty} \frac{\sum_{(n',m')\in\mathscr{D}(s,t)} S_{n, m}^{n', m'}\theta_{0, 4st, \chi_{s,t}^{(n',m')}}^{(0)}(p)}{\left( \frac{1}{\alpha} + p \right)^{3/2}} \, dp \\
 - \frac{1}{(i \alpha)^{3/2}}\sum_{(n',m')\in\mathscr{D}(s,t)} S_{n, m}^{n', m'}\theta_{0, 4st, \chi_{s,t}^{(n',m')}}^{(1)}\left(-\dfrac{1}{\alpha}\right).
 
\end{gathered}$$ Then, by [\[transgen\]](#transgen){reference-type="eqref" reference="transgen"}, we rewrite [\[compgen\]](#compgen){reference-type="eqref" reference="compgen"} as follows: $$\begin{gathered}
 \label{almost}
\displaystyle S_{\chi_{s,t}^{(n,m)}}^{\bf{med}} \left(-\frac{1}{2 \pi i \alpha} \right) = -\frac{2e^{\pi i/4}}{ \pi (i \alpha)^{3/2}}\sqrt{\dfrac{sti}{8}}  \int_{0}^{+ i \infty} \frac{\theta_{0, 4st, \chi_{s,t}^{(n,m)}}^{(0)}(-1/p)}{\sqrt{p} \left(\frac{1}{\alpha} + p \right)^{3/2}} \, dp \\
 - (i \alpha)^{-3/2} \sum_{(n',m')\in\mathscr{D}(s,t)} S_{n, m}^{n', m'}\theta_{0, 4st, \chi_{s,t}^{(n',m')}}^{(1)}\left(-\dfrac{1}{\alpha}\right).
\end{gathered}$$ We now perform the change of coordinates $p \to -1/p$ to the integral in [\[almost\]](#almost){reference-type="eqref" reference="almost"} and simplify to obtain $$\begin{aligned}
\frac{2e^{\pi i/4}}{ \pi (i \alpha)^{3/2}}\sqrt{\dfrac{sti}{8}}\int_{0}^{+ i \infty} \frac{\theta_{0, 4st, \chi_{s,t}^{(n,m)}}^{(0)}(-1/p)}{\sqrt{p}\left(\frac{1}{\alpha} + p \right)^{3/2}} \, dp
=2\sqrt{\dfrac{sti}{8\pi^2}}\int_{0}^{+ i \infty} \frac{\theta_{0, 4st, \chi_{s,t}^{(n,m)}}^{(0)}(p)}{\left(p - \alpha \right)^{3/2}} \, dp\,.
\end{aligned}$$ Then, going back to [\[almost\]](#almost){reference-type="eqref" reference="almost"} we find $$\label{lastgen}
\begin{aligned}
\displaystyle S_{\chi_{s,t}^{(n,m)}}^{\bf{med}} \left(-\frac{1}{2 \pi i \alpha} \right) &= -2\sqrt{\dfrac{sti}{8\pi^2}}\int_{0}^{+ i \infty} \frac{\theta_{0, 4st, \chi_{s,t}^{(n,m)}}^{(0)}(p)}{\left(p - \alpha \right)^{3/2}} \, dp \\
&\qquad - (i \alpha)^{-3/2} \sum_{(n',m')\in\mathscr{D}(s,t)} S_{n, m}^{n', m'}\theta_{0, 4st, \chi_{s,t}^{(n',m')}}^{(1)}\left(-\dfrac{1}{\alpha}\right) \\
& = \theta_{0, 4st, \chi_{s,t}^{(n,m)}}^{(1)}(\alpha)
\end{aligned}$$ where the last line of ([\[lastgen\]](#lastgen){reference-type="ref" reference="lastgen"}) follows from [\[HKlast1\]](#HKlast1){reference-type="eqref" reference="HKlast1"} and [\[HKlast2\]](#HKlast2){reference-type="eqref" reference="HKlast2"}. This proves the result. ◻
:::

::: proof
*Proof of Corollary [\[cor\]](#cor){reference-type="ref" reference="cor"}.* Let $u \in \mathbb{Z}_{\geq 1}$. For $0 \leq \ell \leq u-1$, define $$\begin{aligned}
 \label{xm}
X_u^{(\ell)}(q):=\sum_{k_1,k_2,\dotsc,k_u=0}^\infty (q)_{k_u} q^{k_1^2+\cdots+k_{u-1}^2+k_{\ell+1}+\cdots+k_{u-1}}\prod_{i=1}^{u-1}\begin{bmatrix} k_{i+1} + \delta_{i,\ell} \\ k_{i} \end{bmatrix}
\end{aligned}$$ where $\delta_{i,\ell}$ is the characteristic function; see [@hikami2 Eqn. (11)]. The expression $X_u^{(\ell)}(q)$ matches the $N$th colored Jones polynomial for $T(2, 2u+1)$ when $\ell = 0$ and $q=\zeta_N$ and is an element of $\mathcal{H}$; see [@hikami2 Proposition 16]. Take $s=2$, $t=2u+1$, $n=1$ and $m=\ell + 1$ in [\[pf\]](#pf){reference-type="eqref" reference="pf"}. Then Hikami's strange identity [@hikami2 Eqn. (15)][^1] reads $$\begin{aligned}
\label{strangehikami}
X_u^{(\ell)}(q)``=" -\frac{1}{2}\theta^{(1)}_{(2u-2\ell-1)^2, 2(8u+4), \chi_{2, 2u+1}^{(1, \ell +1)}}(q).
\end{aligned}$$ Claims (1) and (2) of Conjecture [\[cgconj\]](#cgconj){reference-type="ref" reference="cgconj"} follow from Theorem [\[main\]](#main){reference-type="ref" reference="main"} parts (1) and (2), namely the formal series $\mathcal{F}_{\chi_{2, 2u+1}^{(1, \ell + 1)}}(x)$ has a resurgent Borel transform and its median resummation is an analytic function for $\Re(x)>0$ with radial limits at points $\frac{1}{2\pi i}\mathbb{Q}$. In particular, this is true for $$F_{T(2,2u+1)}(x) = \mathcal{F}_{\chi_{2, 2u+1}^{(1,1)}}(x)\,.$$ Then, part (3) of Conjecture [\[cgconj\]](#cgconj){reference-type="ref" reference="cgconj"} follows by Theorem [\[main2\]](#main2){reference-type="ref" reference="main2"} applying [\[strangehikami\]](#strangehikami){reference-type="eqref" reference="strangehikami"} for $\ell=0$. In fact, we can prove a stronger result: $$S^{\bf med}_{\chi_{2, 2u+1}^{(1, \ell + 1)}}\left(-\frac{1}{2\pi i\alpha}\right) \stackrel{.}{=} \mathcal{F}_{\chi_{2, 2u+1}^{(1,\ell+1)}}(e^{2\pi i \alpha})$$ for every $0\neq\alpha\in\mathbb{Q}$ and $0\leq\ell\leq u-1$.

Let $k\in\mathbb{Z}_{\geq 1}$ and $\mathfrak{F}_k(q)$ denote the element in $\mathcal{H}$ that matches the $N$th colored Jones polynomial for $T(3, 2^k)$ at a root of unity $q=e^{\frac{2\pi i}{N}}$ (see [@Be Eqn. (1.8)] for an explicit $q$-hypergeometric expression). Choose $s=3$, $t=2^k$, $n=2$ and $m=1$ in [\[pf\]](#pf){reference-type="eqref" reference="pf"}. Then the strange identity $$\label{str2}
\mathfrak{F}_k(q)``=" -\frac{1}{2}\theta^{(1)}_{(2^{k+1} - 3)^2, 3\cdot 2^{k+2}, \chi_{3, 2^{k}}^{(2,1)}}(q)$$ was proved in [@Be Theorem 2.4][^2]. Claims (1) and (2) of Conjecture [\[cgconj\]](#cgconj){reference-type="ref" reference="cgconj"} follow from Theorem [\[main\]](#main){reference-type="ref" reference="main"} parts (1) and (2), namely the formal series $$F_{T(3,2^k)}(x) = \mathcal{F}_{\chi_{3, 2^{k}}^{(2,1)}}(x)$$ has a resurgent Borel transform and its median resummation is an analytic function for $\Re(x)>0$ with radial limits at points $\frac{1}{2\pi i}\mathbb{Q}$. Then, part (3) of Conjecture [\[cgconj\]](#cgconj){reference-type="ref" reference="cgconj"} follows by Theorem [\[main2\]](#main2){reference-type="ref" reference="main2"} applying [\[str2\]](#str2){reference-type="eqref" reference="str2"}. ◻
:::

[^1]: Taking $u=1$ and $\ell = 0$ in ([\[xm\]](#xm){reference-type="ref" reference="xm"}) and ([\[strangehikami\]](#strangehikami){reference-type="ref" reference="strangehikami"}) yields ([\[strid\]](#strid){reference-type="ref" reference="strid"}).

[^2]: Taking $k=1$ in ([\[str2\]](#str2){reference-type="ref" reference="str2"}) gives ([\[strid\]](#strid){reference-type="ref" reference="strid"}).

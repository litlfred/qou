---
doc_id: arxiv-2304.07001v3
doc_title: "RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-7
source_pdf: 2304.07001v3.pdf
source_sha256: b6c0d7f50b6407f1
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.96
doc_brief: "RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES — We prove resurgence properties for the Borel transform of a f ormal power series associated to elements in the Habiro ring that come from radi al"
---
The modern theory of resurgence began with the voluminous works of Écalle in 1981 [@e1; @e2] and 1985 [@e3]. This theory now plays a vital rôle in a remarkable number of diverse areas, to name just a few examples: nonlinear systems of ODEs and difference equations [@costin1; @kamimoto], algebraic combinatorics [@cfmt1; @cfmt2], enumerative combinatorics and quantum field theory [@BD; @MY], period integrals and string theory scattering amplitudes [@dk], wall-crossing phenomena [@ks] and matrix models [@mm]. In this paper, we are interested in a conjecture due to Costin and Garoufalidis [@cg] which connects resurgence and quantum topology. For other such interactions, see [@am; @ggm; @ggm2; @ggmw; @fw] and the references therein.

Let us recall the general setup from [@cg]. For further details, see [@costin2; @dp; @bm; @ms] or [@Sauzin Section 2] for an excellent concise review of the basic notions of resurgence and alien calculus. A formal power series $$\begin{equation}
 \label{fps}
\mathcal{F}(x)=\sum_{n=0}^{\infty} a_n x^{-n} \in \mathbb{C}[[1/x]]
\end{equation}$$ is called Gevrey-1 if there exists positive real numbers $A$, $B$ such that $$\begin{equation*}
| a_n | \leq AB^n n!
\end{equation*}$$ for all $n \geq 0$. Consider a Gevrey-1 formal power series given by ([\[fps\]](#fps){reference-type="ref" reference="fps"}) and its Borel transform $\mathcal{B}: \mathbb{C}[[1/x]] \longrightarrow \mathbb{C}[[p]]$ defined by $$\begin{equation}
 \label{borel}
\mathcal{B} \Biggl( \sum_{n=0}^{\infty} a_n x^{-n} \Biggr) = a_0\delta+\sum_{n=1}^{\infty} a_{n} \frac{p^{n-1}}{(n-1)!} =: a_0\delta + G(p)
\end{equation}$$ where $\delta$ is a formal symbol that has Laplace transform given by the constant function $1$. For simplicity, we write $\mathcal{B}[\mathcal{F}](p)$ for the transform [\[borel\]](#borel){reference-type="eqref" reference="borel"}. Here, $G(p)$ has a positive radius of convergence as it arose from a Gevrey-1 power series. In a standard abuse of notation, $G(p)$ denotes the formal power series in ([\[borel\]](#borel){reference-type="ref" reference="borel"}) (and is also commonly referred to in the literature as the Borel transform of $\mathcal{F}(x)$) and the analytic continuation of the associated germ at the origin. In addition, $G(p)$ is called a *resurgent function* if it is endlessly analytically continuable [@ms]. This property means $G(p)$ extends to a (possibly multi-valued) holomorphic function along unbounded paths that need only circumvent a discrete set of singularities. In the present work, we consider the case where $G(p)$ defines a multi-valued function on $\mathbb{C} \setminus \mathcal{N}$, with $\mathcal{N}$ a discrete set of singularities lying on the ray $\mathbb{R}_{>0}$, e.g., $\mathcal{N} = \left \{ \frac{n^2\pi^2}{6}:n\in\mathbb{Z}_{>0} \right \}$.

Assuming $G(p)$ satisfies suitable growth conditions, the left and right Borel resummations of $\mathcal{F}(x)$ are defined as $$\begin{eqnarray*}
S^{+}[\mathcal{F}](x) =\int_{\gamma_l}e^{-px} \mathcal{B}[\mathcal{F}](p) \,dp
\end{eqnarray*}$$ and $$\begin{eqnarray*}
S^{-}[\mathcal{F}](x) =\int_{\gamma_r}e^{-px}  \mathcal{B}[\mathcal{F}](p) \, dp
\end{eqnarray*}$$ where $x \in \mathbb{C}$ and $\gamma_l$ and $\gamma_r$ are contours in $\mathbb{C} \setminus \mathcal{N}$ from $0$ to $\infty$ that turn left (respectively, right) at each singularity in $\mathcal{N}$ (see Figure [1](#fig:fig1){reference-type="ref" reference="fig:fig1"}). In addition, the left and right Borel resummations give analytic functions on a sector of opening angle $\pi$ in the complex $x$-plane.

<figure id="fig:fig1" data-latex-placement="ht">

<figcaption>A singularity set <span class="math inline">𝒩 ⊂ ℂ</span> and the contours <span class="math inline"><em>γ</em><sub><em>l</em></sub></span> and <span class="math inline"><em>γ</em><sub><em>r</em></sub></span>.</figcaption>
</figure>

Following [@cg Sections 4.2--4.3], the median resummation of $\mathcal{F}$ is given by $$\begin{equation}
 \label{smed}
S^{\textbf{med}}(x) = S^{\textbf{med}}[\mathcal{F}](x) := \frac{1}{2} \Bigl( S^{+}[\mathcal{F}](x) + S^{-}[\mathcal{F}](x) \Bigr).
\end{equation}$$ In general, care is required when defining median summations, see [@hlss Section 2]. Under favorable circumstances, for example when $G(p)$ is the Borel transform of a formal (Gevrey-1) solution in powers of $1/x$ to a linear differential equation, each of $\mathcal{S}^{\pm}[\mathcal{F}](x)$ (and thus, of course, $S^{\textbf{med}}(x)$) is a well-defined homomorphic solution. This is one incarnation of the terminology "resummation".

In this paper, we will study the median resummation of the Borel transform for certain formal power series associated to knots.

Let $K$ be a knot and $J_N(K; q)$ be the usual colored Jones polynomial, normalized to be 1 for the unknot. If $N=2$, then we recover the Jones polynomial [@Jones]. As a knot invariant, the colored Jones polynomial is of fundamental importance in several open problems in quantum topology (see, e.g., [@garoufalidis-AJ; @garoufalidis-slope; @kal-tran; @my; @z]). We now recall the Habiro ring [@habiro] $$\begin{equation*}
\displaystyle \mathcal{H} := \varprojlim_{n} \mathbb{Z}[q] / \langle (q)_n \rangle
\end{equation*}$$ where $$\begin{equation*}
(a)_n = (a;q)_n := \prod_{k=1}^{n} (1-aq^{k-1})
\end{equation*}$$ is the standard $q$-Pochhammer symbol. Every element of $\mathcal{H}$ may be written as $$\begin{equation*}
\sum_{n=0}^{\infty} b_n(q) (q)_n
\end{equation*}$$ where $b_n(q) \in \mathbb{Z}[q]$. Given $K$, there exists an element $\Phi_{K}(q) \in \mathcal{H}$ called the Kashaev invariant [@Kashaev:6j] which matches $J_N(K; q)$ (up to a prefactor) when $q=\zeta_N := e^{\frac{2 \pi i}{N}}$ [@hl Theorem 2]. To illustrate, for the trefoil knot $K=3_1$, we have [@habiro1; @thang] $$\begin{equation}
\label{cjp31}
J_{N}(3_1; q) = q^{1-N} \sum_{n=0}^{\infty} q^{-nN} (q^{1-N})_n.
\end{equation}$$ In this case, the Kontsevich-Zagier series [@z] $$\begin{equation}
 \label{kz}
\Phi_{3_1}(q) := \sum_{n=0}^{\infty} (q)_n \in \mathcal{H}
\end{equation}$$ gives the Kashaev invariant for the trefoil [@Kashaev:6j] and so from [\[cjp31\]](#cjp31){reference-type="eqref" reference="cjp31"} and [\[kz\]](#kz){reference-type="eqref" reference="kz"}, we observe $$\begin{equation*}
\Phi_{3_1}(\zeta_N) \zeta_N = J_N(3_1; \zeta_N).
\end{equation*}$$ Now, a crucial aspect of the computations in [@cg] is the "strange identity\" $$\begin{equation}
 \label{strid}
\Phi_{3_1}(q) ``=" -\frac{1}{2} \sum_{n=1}^{\infty} n \Bigl( \frac{12}{n} \Bigr) q^{\frac{n^2 - 1}{24}}
\end{equation}$$ where $``="$ means that both sides agree to infinite order at any root of unity and $\bigl( \frac{12}{*} \bigr)$ is the quadratic character of conductor $12$. More precisely, replacing $q$ by the product of a root of unity and $e^{-x}$, then letting $x \to 0^{+}$, the right-hand side has an asymptotic expansion as a power series in $x$ and this power series is given by the left-hand side at $q$. For further details, see [@akl; @z1]. If $q=e^{2 \pi i x}$, $x \in \mathbb{H}$, then ([\[strid\]](#strid){reference-type="ref" reference="strid"}) implies for $0 \neq \alpha \in \mathbb{Q}$ $$\begin{equation}
 \label{rational}
e^{\frac{\pi i \alpha}{12}} \Phi_{3_1}(e^{2 \pi i \alpha}) = -\frac{1}{2} \sum_{n=1}^{\infty} n \Bigl( \frac{12}{n} \Bigr) e^{\frac{n^2 \pi i \alpha}{12}}
\end{equation}$$ where the right-hand side of ([\[rational\]](#rational){reference-type="ref" reference="rational"}) is interpreted as the radial limit $x \to \alpha$. The significance of "identities\" akin to ([\[strid\]](#strid){reference-type="ref" reference="strid"}) is evident in various applications, e.g., asymptotics and congruences for Fishburn and generalized Fishburn numbers modulo prime powers [@ak; @akl; @as; @Be; @an; @gjko; @straub; @z1], the quantum modularity of $\Phi_{3_1}(q)$ [@go; @z] and expressing WRT invariants of Brieskorn homology spheres in terms of limiting values of Eichler integrals [@hikamiWRT1; @hikamiWRT2; @hikamiWRT3]. For a recent advance using the "Bailey machinery\" which not only recovers ([\[strid\]](#strid){reference-type="ref" reference="strid"}), but produces a wealth of new examples, see [@lovejoy].

Elements of $\mathcal{H}$ can also be formally expanded around any root of unity. Therefore, we let $$\begin{equation}
 \label{habel}
F_{K}(x) := \Phi_{K}(e^{-\frac{1}{x}})\in\mathbb{C}[\![1/x]\!].
\end{equation}$$ To emphasize the dependence on $K$, we denote the Borel transform of $F_{K}(x)$ by $G_{K}(p)$ and its conjecturally well-defined median resummation by $S_{K}^{\textbf{med}}(x)$. Finally, we use the notation $\stackrel{.}{=}$ to denote equality up to a prefactor which depends on $K$. We can now state the main conjecture from [@cg] (slightly edited for clarity) which is part of a larger program to understand the analytic continuation of invariants of "knotted objects\" arising in Chern-Simons theory [@g; @gl].

::: conjecture
[]{#cgconj label="cgconj"} For every knot $K$,

- $F_K(x)$ has a resurgent Borel transform $G_{K}(p)$.\

- $S^{\textbf{med}}_{K}(x)$ is an analytic function defined on $\Re(x) > 0$ with radial limits at the points $\frac{1}{2\pi i} \mathbb{Q}$ of its natural boundary.\

- If $(2)$ is true, then consider the radial limit $$\begin{equation*}
  S_{K}^{\bf{med}}\left( -\frac{1}{2 \pi i \alpha} \right)  := \lim_{x \to -\frac{1}{2 \pi i \alpha}} S_{K}^{\bf{med}}(x)
  \end{equation*}$$ where $\Re(x) > 0$. For $0 \neq \alpha \in\mathbb{Q}$, we have $S_{K}^{\textbf{med}}\left(-\frac{1}{2 \pi i \alpha}\right) \stackrel{.}{=} \Phi_{K}(e^{2\pi i \alpha})$.
:::

In [@cg Theorem 2.5, Theorem 3.1], Conjecture [\[cgconj\]](#cgconj){reference-type="ref" reference="cgconj"} (1) and (2) were proven for $K=3_1$. Here, $$\begin{equation*}
F_{3_1}(x) = e^{-\frac{1}{24x}} \sum_{n=0}^{\infty} (e^{-\frac{1}{x}})_n
\end{equation*}$$ where an adjustment of ([\[habel\]](#habel){reference-type="ref" reference="habel"}) has been made. The Borel transform $G_{3_1}(p)$ of $F_{3_1}(x)$ is explicitly given by [@cg Theorem 3.1] $$\begin{equation}
 \label{g31}
G_{3_1}(p) = \frac{3 \pi}{2\sqrt{2}} \sum_{n=1}^{\infty} \frac{n \bigl( \frac{12}{n} \bigr)}{\bigl (-p + \frac{n^2 \pi^2}{6} \bigr)^{5/2}}.
\end{equation}$$ Moreover, a close inspection of the proofs of Theorems 2.5 and 3.1 in [@cg] reveals that it is actually ([\[strid\]](#strid){reference-type="ref" reference="strid"}) and the periodic function $\bigl( \frac{12}{*} \bigr)$ which determine the analytic nature of $G_{3_1}(p)$ and $S^{\textbf{med}}_{3_1}(x)$. Our main goal in this paper is to prove resurgence properties for formal power series associated to elements in $\mathcal{H}$ that satisfy a general type of strange identity motivated by ([\[strid\]](#strid){reference-type="ref" reference="strid"}). Here, we emphasize the importance of periodic functions. Before stating our main result, we introduce some notation.

Let $M \geq 2$ be an integer and $k_1, k_2 \in \mathbb{Z}$ with $0 < k_1 < k_2 < \frac{M}{2}$. Let $0\neq c\in\mathbb{R}$ and $f$ be the function $$\begin{eqnarray}
\label{ggen}
f(n):=\begin{cases}
c &\text{if $n\equiv k_1,M-k_1\pmod{M}$,} \\
-c &\text{if $n\equiv k_2,M-k_2\pmod{M}$,}\\
0 &\text{otherwise.}
\end{cases}
\end{eqnarray}$$ Note that under the conditions on $k_1$ and $k_2$, $f$ is a well-defined even function of period $M$ with mean value zero. For integers $a \geq 0$ and $b>0$, consider the partial theta series $$\begin{equation}
 \label{pts}
\theta_{a,b,f}^{(\nu)}(q):=\sum_{n=0}^{\infty} n^\nu f(n)q^{\frac{n^2-a}{b}}
\end{equation}$$ where $q=e^{2\pi i x}$, $x \in \mathbb{H}$, and $\nu \in \{0, 1\}$. For $\ell \in \mathbb{Z}$, set $$\begin{equation}
 \label{ftilde}
\tilde{f}(\ell) := (-1)^{\ell} \sin\left(\frac{(k_2-k_1)\ell\pi}{M}\right)\sin\left(\frac{(M-k_1-k_2)\ell\pi}{M}\right).
\end{equation}$$ Suppose there exists $$\begin{equation*}
\Phi_{f}(q) := \sum_{n=0}^{\infty} A_{n,f}(q) (q)_n \in \mathcal{H}
\end{equation*}$$ where $A_{n,f}(q) \in \mathbb{Z}[q]$ such that $$\begin{equation}
 \label{Hstrange}
 \Phi_{f}(q) ``=" \theta_{a,b,f}^{(1)}(q).
\end{equation}$$ Finally, define $$\begin{equation}
 \label{gen-expansions2}
\mathcal{F}_{f} \left( x \right) := e^{-\frac{a}{bx}} {\Phi}_f(e^{-\frac{1}{x}})=\sum_{n=0}^\infty\dfrac{C_{n,f}}{n!}\left(\frac{1}{bx}\right)^n\,.
\end{equation}$$ The asymptotics of the partial theta series $\theta_{a,b,f}^{(1)}(q)$ around $q=1$, which by the strange identity in [\[Hstrange\]](#Hstrange){reference-type="eqref" reference="Hstrange"} gives the expansion of $\Phi_f(q)$, can be computed by $L$-values. By standard calculations using the Mellin transform (see, e.g., [@akl; @gjko; @z]), we find that $$\begin{eqnarray*}
\label{Cnf}
C_{n,f}=(-1)^nL(-2n-1,f)
\end{eqnarray*}$$ where $$\begin{eqnarray*}
 L(s,f) :=\sum_{n=1}^\infty\dfrac{f(n)}{n^s}
\end{eqnarray*}$$ is the $L$-series associated to $f$. In particular, using [@akl Lemma 3.2], we obtain that $$\begin{eqnarray}
\label{CnfBer}
C_{n,f}=(-1)^{n+1} \dfrac{M^{2n+1}}{2n+2} \sum_{m=1}^M f(m)B_{2n+2}\left(\dfrac{m}{M}\right)
\end{eqnarray}$$ where for $k\geq 0$, $B_k(x)$ denotes the $k$th Bernoulli polynomial. By ([\[gen-expansions2\]](#gen-expansions2){reference-type="ref" reference="gen-expansions2"}) and [\[CnfBer\]](#CnfBer){reference-type="eqref" reference="CnfBer"}, we have $$\begin{equation}
 \label{F}
\mathcal{F}_{f} \left( \frac{1}{x} \right)  = \sum_{n=0}^{\infty} \frac{(-1)^{n+1} M^{2n+1}}{(2n+2) n!} \sum_{m=1}^{M} f(m) B_{2n+2}\left(\dfrac{m}{M}\right) \left(\frac{x}{b}\right)^n.
\end{equation}$$ We will denote the Borel transform of $\mathcal{F}_f(x)$ by $G_f(p)$. Here, we write $S_{f}^{\bf{med}}(x)$ for $S^{\textbf{med}}(x)$, $$\begin{equation*}
S_{f}^{\bf{med}}\left( -\frac{1}{2 \pi i \alpha} \right)  := \lim_{x \to -\frac{1}{2 \pi i \alpha}} S_{f}^{\bf{med}}(x),
\end{equation*}$$ $\theta_{a,b,f}^{(\nu)}(x)$ for $\theta_{a,b,f}^{(\nu)}(q)=\theta_{a,b,f}^{(\nu)}(e^{2\pi i x})$ and $\displaystyle \theta_{a,b,f}^{(\nu)}(\alpha) := \lim_{x \to \alpha} \theta_{a,b,f}^{(\nu)}(x)$ where $0 \neq \alpha \in \mathbb{Q}$. Our main result is now the following.

::: theorem
[]{#main label="main"} For $f$ given by [\[ggen\]](#ggen){reference-type="eqref" reference="ggen"} and $\mathcal{F}_f(x)$ as in [\[F\]](#F){reference-type="eqref" reference="F"}, we have the following:

- $\mathcal{F}_f(x)$ has a resurgent Borel transform $G_f(p)$.\

- $S_f^{\textbf{med}}(x)$ is an analytic function defined on $\Re(x) > 0$ with radial limits at the points $\frac{1}{2\pi i} \mathbb{Q}$ of its natural boundary.\

- For $0 \neq \alpha\in\mathbb{Q}$, we have $$\begin{equation}
  \label{eq:smed.form}
  S^{\textbf{med}}_f\left(-\dfrac{1}{2\pi i\alpha}\right)=\frac{c b e^{\pi i/4}}{M\pi (i\alpha)^{3/2}}\int_0^{+i\infty} \frac{\theta_{0,4M^2,\tilde{f}}^{(0)}(bp)}{\big(\frac{1}{\alpha}+ p\big)^{3/2}} dp+\left(\frac{b}{i\alpha}\right)^{3/2}\frac{\sqrt{2} c}{M^2}\theta^{(1)}_{0,4M^2,\tilde{f}}\left(-\frac{b}{\alpha}\right).
  \end{equation}$$
:::

::: remark
The proof of Theorem [\[main\]](#main){reference-type="ref" reference="main"} demonstrates resurgence properties for the normalized partial theta series $e^{-\frac{a}{bx}} \theta_{a,b,f}^{(1)}(e^{-\frac{1}{x}})$ without assuming [\[Hstrange\]](#Hstrange){reference-type="eqref" reference="Hstrange"}. Our results and those in the announcement [@hlss] appear to be related; however, we give a proof that can be used to prove Conjecture 1.1 for our cases of interest (see Corollary [\[cor\]](#cor){reference-type="ref" reference="cor"}).
:::

We give two applications of Theorem [\[main\]](#main){reference-type="ref" reference="main"}. The first result explicitly computes [\[eq:smed.form\]](#eq:smed.form){reference-type="eqref" reference="eq:smed.form"} in the following situation. For coprime positive integers $s$ and $t$, $1\le m\le t-1$ and $1\le n\le s-1$, let $\chi_{s,t}^{(n,m)}(k)$ be the periodic function obtained by choosing $c=1$, $M=2st$, $k_1= | nt-ms |$ and $k_2 = nt+ms$ in [\[ggen\]](#ggen){reference-type="eqref" reference="ggen"}, i.e., $$\begin{align}
\label{pf}
\chi_{s,t}^{(n,m)}(k)=\begin{cases}
1 & \text{if $k\equiv \pm(nt-ms)\pmod{2st}$},\\
-1& \text{if $k\equiv \pm(nt+ms)\pmod{2st}$},\\
0 &\text{otherwise}.
\end{cases}
\end{align}$$ For coprime odd integers $s$, $t$, define the sets $$\begin{align}
 \label{d1}
\mathscr{D}_1(s, t)&:=\left\{(n, m): 1\le n\le \frac{s-1}{2}, 1\le m\le t-1\right\}
\end{align}$$ and $$\begin{align}
 \label{d2}
\mathscr{D}_2(s, t)&:=\left\{(n, m): 1\le n\le s-1, 1\le m\le \frac{t-1}{2}\right\}.
\end{align}$$ There is a bijection between $\mathscr{D}_1(s, t)$ and $\mathscr{D}_2(s, t)$ (see Lemma [\[scha\]](#scha){reference-type="ref" reference="scha"} and [\[bi\]](#bi){reference-type="eqref" reference="bi"}). For $s$ and $t$ coprime and of opposite parities, we consider $$\begin{align*}
\mathscr{D}_3(s, t):=
\begin{cases}
\left\{(n, m): 1\le n\le \frac{s-1}{2}, 1\le m\le t-1\right\} & \text{if $s\equiv 1\!\!\!\pmod{2}$},\\
\left\{(n, m): 1\le n\le s-1, 1\le m\le \frac{t-1}{2}\right\} & \text{if $s\equiv 0\!\!\!\pmod{2}$}.
\end{cases}
\end{align*}$$ Finally, define the set $\mathscr{D}(s, t)$ of pairs which yield distinct characters in ([\[pf\]](#pf){reference-type="ref" reference="pf"}) as follows: $$\begin{align}
 \label{d}
\mathscr{D}(s, t):=
\begin{cases}
\mathscr{D}_1(s, t)\quad \text{or}\quad \mathscr{D}_2(s, t) & \text{if $s\equiv t\equiv 1\!\!\!\pmod{2}$},\\
\mathscr{D}_3(s, t) & \text{if $s\not\equiv t\!\!\!\pmod{2}$}.
\end{cases}
\end{align}$$ One sees that $D(s, t):=|\mathscr{D}(s, t)|=\frac{(s-1)(t-1)}{2}$.

::: theorem
[]{#main2 label="main2"} Let $s$ and $t$ be coprime positive integers and $(n,m) \in \mathscr{D}(s,t)$. For $0 \neq \alpha \in \mathbb{Q}$, we have $$\begin{equation}
S_{\chi_{s,t}^{(n,m)}}^{\bf{med}}\left(-\frac{1}{2\pi i\alpha}\right) = \theta_{0,4st,\chi_{s,t}^{(n,m)}}^{(1)}(\alpha).
\end{equation}$$
:::

The second result verifies Conjecture [\[cgconj\]](#cgconj){reference-type="ref" reference="cgconj"} for two families of torus knots.

::: corollary
[]{#cor label="cor"} Let $u,k\in\mathbb{Z}_{\geq 1}$. Conjecture [\[cgconj\]](#cgconj){reference-type="ref" reference="cgconj"} is true for the families of torus knots $T(2, 2u+1)$ and $T(3, 2^k)$.
:::

Corollary [\[cor\]](#cor){reference-type="ref" reference="cor"} generalizes Theorems 2.5 and 3.1 in [@cg] and upon taking either $u=1$ or $k=1$ confirms Conjecture [\[cgconj\]](#cgconj){reference-type="ref" reference="cgconj"} for the trefoil knot $3_1 = T(2,3)=T(3,2)$.

The paper is organized as follows. In Section [\[sec:proof-main-thm\]](#sec:proof-main-thm){reference-type="ref" reference="sec:proof-main-thm"}, we prove Theorem [\[main\]](#main){reference-type="ref" reference="main"} by first providing an explicit evaluation of $G_{f}(p)$ in [\[BT\]](#BT){reference-type="eqref" reference="BT"}, which generalizes [\[g31\]](#g31){reference-type="eqref" reference="g31"}, and then computing $S_{f}^{\textbf{med}}(x)$ directly via a careful contour deformation argument. In Section [\[sec:torus\]](#sec:torus){reference-type="ref" reference="sec:torus"}, we prove Theorem [\[main2\]](#main2){reference-type="ref" reference="main2"} and Corollary [\[cor\]](#cor){reference-type="ref" reference="cor"}. In Section [\[sec:remarks\]](#sec:remarks){reference-type="ref" reference="sec:remarks"}, we make some concluding remarks.

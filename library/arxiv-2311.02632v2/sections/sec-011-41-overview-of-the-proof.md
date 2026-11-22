---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE"
section_id: sec-011-41-overview-of-the-proof
section_title: "Overview of the proof"
section_number: 4.1
pages: 21-29
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.988
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
In this section, we will investigate the multiplicity $m_1$ of the first eigenvalue $\la_1$ of the Laplacian on the Fricke-Macbeath surface $\X=\Gamma\backslash\disk$. Specifically, we will prove the following:

::: theorem
[]{#thm:mult7 label="thm:mult7"} The multiplicity of the first eigenvalue $\la_1$ of the Fricke-Macbeath surface is 7, and $\la_1\in [1.23, 1.26]$.
:::

To achieve this, we begin with the following key lemma:

::: lemma
[]{#prop:mult7 label="prop:mult7"} The multiplicity of the first eigenvalue $\la_1$ is at least 7.
:::

::: proof
*Proof.* By [@FBP23 Lemma 9.2], no 1-dimensional subrepresentation of $\Aut(\X)$ can occur in the eigenspace $V_{\la_1}$ associated to $\la_1$. From the character table of $\Aut(\X)$ given in Table [\[table:character_table\]](#table:character_table){reference-type="ref" reference="table:character_table"}, we know that $\Aut(X)$ has irreducible representations of dimensions 1,7,8, and 9. As a result, $V_{\la_1}$ contains a direct summand with a dimension of at least 7. ◻
:::

Our main tool for the proof of Theorem [\[thm:mult7\]](#thm:mult7){reference-type="ref" reference="thm:mult7"} is the Selberg trace formula [\[eq:STF1\]](#eq:STF1){reference-type="eqref" reference="eq:STF1"}. Following the notation in [@FBP21] for the Selberg trace formula, we define $$\begin{aligned}
\calS &= \sum_{n=0}^{\infty} h(r_{n}),\\
\calI &= 2(g(X)-1)\int_0^\infty r h(r) \tanh (\pi r)\, dr,\\
\calG &= \frac{1}{\sqrt{2\pi}}\sum_{\{\gamma\} \in \calC(\Gamma)} \frac{\La(\gamma)}{2 \sinh(\ell(\gamma)/2)} g(\ell(\gamma)),\\
\end{aligned}$$ so that the Selberg trace formula is compactly expressed as $\mathcal{S} = \mathcal{I} + \mathcal{G}$. Here, $g(X)$ denotes the genus of a surface $X$, which is 7 in our case. We have also utilized the relation $\mathrm{area}(X) = 4\pi (g(X) - 1)$ and the even nature of the function $h$ to refine the expression for $\mathcal{I}$.

For our proof of Theorem [\[thm:mult7\]](#thm:mult7){reference-type="ref" reference="thm:mult7"}, we will divide the interval $[0,1.26]$ into four subintervals and establish the following:

-   $\la_1 \notin [0, 0.25]$ ()

-   $\la_1 \notin [0.25, 1]$ ()

-   $\la_1 \notin [1, 1.23]$ ()

-   $\la_1 \in [1.23, 1.26]$ () and its multiplicity is 7 ()

We will choose suitable test functions $h,g$ to derive the desired conclusions. These test functions have a particular form with many adjustable parameters. Hence the challenge in applying the Selberg trace formula lies in finding the optimal parameters for these test functions.

In subsections [0.1](#subsec:subinterval1){reference-type="ref" reference="subsec:subinterval1"} and [0.2](#subsec:subinterval2){reference-type="ref" reference="subsec:subinterval2"}, $h(\xi)$ will be given as a linear combination of functions of the form $\left(\frac{\sin(\delta \xi / 2)}{\delta \xi / 2}\right)^{4}\cos(n \delta \xi)$ for some fixed $\delta\in \R$ with $n\in \Z$. Such $h$ is an entire function and satisfies the decay properties as given in [\[eq:hdecay\]](#eq:hdecay){reference-type="eqref" reference="eq:hdecay"}. Its Fourier transform $g$ is an even function with compact support. Such $h,g$ form an admissible transform pair. These type of functions were used in [@MR2338122 Section 4] and [@MR4186122 Section 5] to verify the Selberg eigenvalue conjecture for many congruence subgroups of small conductor.

In subsections [0.3](#subsec:subinterval3){reference-type="ref" reference="subsec:subinterval3"} and [\[subsec:subinterval4\]](#subsec:subinterval4){reference-type="ref" reference="subsec:subinterval4"}, we will use test functions involving the *Hermite polynomials* $\{H_n\}_{n\in \Z_{\geq 0}}$. They are orthogonal polynomials with weight $e^{-x^2}$ on the real line $\R = (-\infty, \infty)$. They can be also defined by the Rodrigues formula $$H_n(x) = (-1)^n e^{x^2} \frac{d^n}{dx^n}(e^{-x^2}).$$ For even and odd values of $n$, $H_n$ is respectively even and odd, satisfying the relation: $$H_n(-x) = (-1)^n H_n(x).$$ They have a close relationship with certain Laguerre polynomials $\{L_n^{(\alpha)}(x)\}$. More specifically, the Hermite polynomials of even order satisfies $$H_{2n}(x) = (-1)^n 4^{n} n! L_n^{(-1/2)}(x^2).$$ Let $h_n(x) = H_n(x) e^{-x^2/2}$. They are eigenfunctions of the Fourier transform with eigenvalues $\pm 1, \pm \i$. In particular, we have $\what{h_{2n}}(\xi) = (-1)^n h_{2n}(\xi)$.

Our test functions $h,g$ will of the form: $$\begin{aligned}
g(x) &= \left(\sum_{n=0}^N s_n L_n^{(-1/2)}(x^2) \right) e^{-x^2/2} =: u(x^2) e^{-x^2/2}, \notag \\
h(\xi) &=  \left(\sum_{n=0}^N (-1)^n s_n L_n^{(-1/2)}(\xi^2) \right) e^{-\xi^2/2} =: v(\xi^2) e^{-\xi^2/2}. \label{eq:gh_hermite}
\end{aligned}$$ The rational numbers $\{s_n\}$ in [\[eq:gh_hermite\]](#eq:gh_hermite){reference-type="eqref" reference="eq:gh_hermite"} are what we specify in concrete applications. In this instance, $h$ is an even entire function that exhibits rapid decay, readily meeting the criteria set by [\[eq:hdecay\]](#eq:hdecay){reference-type="eqref" reference="eq:hdecay"}. Thus, $h$ and $g$ together make up an admissible transform pair. Note that $u$ and $v$ are polynomials with rational coefficients.

These test functions were used in the sphere packing problem [@MR1973059 Section 7]. They were first used to study the spectrum of hyperbolic surfaces in [@FBP21]. They prove particularly valuable when constructing test functions that satisfy some sign conditions for both $h$ and its Fourier transform.

## Proof of $\la_1 \notin [0, 0.25]$ {#subsec:subinterval1}

::: prop
[]{#prop:subinterval1 label="prop:subinterval1"} There is no eigenvalue in the interval $(0,1/4]$.
:::

::: proof
*Proof.* We choose the test function

$$h(r)=\left(\frac{\sin r}{r}\right)^{4}.$$ Then its Fourier transform $g$ is explicitly given by $$\begin{aligned}
g(u) = 
\frac{1}{192} \Big[ &(u-4)^3 \sgn(u-4)  - 4 (u-2)^3 \sgn(u-2) +6 u^3 \sgn(u)  \\
&- 4 (u+2)^3 \sgn(u+2) + (u+4)^3 \sgn(u+4) \Big].
\end{aligned}$$ Note that $g$ is supported in the interval $[-4,4]$. Given that $\sys(\X) > 5$, the hyperbolic classes do not contribute to $\calG$, resulting in $\calG = 0$. Thus, the trace formula can be simply expressed as $\calS = \calI$.

Let us find an upper bound for $\calS$. We put $\eps=10^{-3}$ and $L=1000$ and split the integral for $\calI$ as $$\begin{aligned}
\calI_1 & = 2(g(\X)-1)\int_0^{\eps} r h(r) \tanh(\pi r) \,dr\\
\calI_2 &= 2(g(\X)-1)\int_{\eps}^{L} r h(r) \tanh(\pi r) \,dr\\
\calI_3 & = 2(g(\X)-1)\int_{L}^{\infty}  r h(r) \tanh(\pi r) \,dr
\end{aligned}$$ Using the inequality $\sin(x) \leq x - \frac{x^3}{6} + \frac{x^5}{120}$ for $x\geq 0$, we can check that $h(r)\leq (1 - r^2/6 + r^4/120)^4 \leq 1-\frac{2 r^2}{3}+\frac{r^4}{5}$ for $r\leq 1$. Also note that $\tanh(\pi r) = \frac{e^{2 \pi  r}-1}{e^{2 \pi  r}+1} \leq 1$. Thus, $$\label{eq:upper_bound_I1}
\calI_1 \leq 2(g(\X)-1) \int_0^{\eps} r \left(1-\frac{2 r^2}{3}+\frac{r^4}{5}\right)\,dr
< 6\times 10^{-6}.$$ For the second term, we employ interval arithmetic to obtain the following: $$\calI_2 = 2(g(\X)-1)\int_{\eps}^{L} r h(r) \tanh(\pi r) \,dr < 7.8684.$$ Since the function $h(r)$ is bounded by $1/r^4$, $$\calI_3 \leq 2(g(\X)-1) \int_{L}^\infty r \frac{1}{r^4} \,dr  = \frac{g-1}{L^2} =  6\times 10^{-6}.$$ Note also that $h(r_0) = h(i/2) = 16 \sinh\left(\frac{1}{2}\right)^4 > 1.1797$. We can deduce that $$\label{upper_bound_I}
\calS-h(r_0) = \calI-h(r_0) =  \calI_1+\calI_2+\calI_3-h(r_0)<6.7.$$ See the Sage [@sagemath] notebook `subinterval1.ipynb` for the necessary numerical calculations.

Assume that $0\leq \la_1 \leq 1/4$. Then $r_1 = i\nu_1$ for some $0\leq \nu_1 \leq 1/2$. Because its multiplicity must be at least 7 (Lemma [\[prop:mult7\]](#prop:mult7){reference-type="ref" reference="prop:mult7"}), $h(i\nu)=\frac{\left(e^{\nu }-e^{-\nu }\right)^4}{16 \nu ^4}\geq 1$ for $0\leq \nu \leq 1/2$, and $h(r)>0$ for all $r\in \R$, we have $$\calS-h(r_0) = \sum_{n=1}^{\infty} h(r_n) \geq 7.$$ This contradicts the bound [\[upper_bound_I\]](#upper_bound_I){reference-type="eqref" reference="upper_bound_I"} for $\calS$. ◻
:::

## Proof of $\la_1 \notin [0.25, 1]$ {#subsec:subinterval2}

Consider the function $f$ given by $$\label{eqn:hsqrth}
f(r)=\left(\frac{\sin(\delta r / 2)}{\delta r / 2}\right)^{2} \sum_{n=0}^{M-1} x_{n} \cos(\delta n r),$$ where $M=15$ and $\delta = 1/5$. The coefficients $x_i$ are given by: $$\begin{aligned}
x_{0} & = 0.10495, & x_{5} & = 0.16480, & x_{10} & = 0.06400, \\
x_{1} & = 0.20797, & x_{6} & = 0.14688, & x_{11} & = 0.04416, \\
x_{2} & = 0.20226, & x_{7} & = 0.12715, & x_{12} & = 0.02632, \\
x_{3} & = 0.19294, & x_{8} & = 0.10628, & x_{13} & = 0.01154, \\
x_{4} & = 0.18032, & x_{9} & = 0.08497, & x_{14} & = 0.00046.
\end{aligned}$$

We select the test function $h$ to be the square of $f$: $$\begin{aligned}
h(r) & = f(r)^{2} \label{eqn:hfsquare} \\
     & = \left(\frac{\sin(\delta r / 2)}{\delta r / 2}\right)^{4} \sum_{{i=0}}^{{M-1}} \sum_{{j=0}}^{{M-1}}     
     \cos(i \delta r) \cos(j \delta r) x_{i} x_{j} \nonumber \\
     & = \left(\frac{\sin(\delta r / 2)}{\delta r / 2}\right)^{4}\sum_{{i=0}}^{{M-1}} \sum_{{j=0}}^{{M-1}}     
     \frac{1}{2} \left[ \cos((i-j) \delta r) + \cos((i+j) \delta r) \right]x_{i} x_{j}. \nonumber
\end{aligned}$$

::: prop
[]{#prop:upper_bound_II label="prop:upper_bound_II"} For the test function $h$ in [\[eqn:hfsquare\]](#eqn:hfsquare){reference-type="eqref" reference="eqn:hfsquare"}, we have $\calS-h(r_0)<7$.
:::

::: proof
*Proof.* Let $h_{ij}(r) : =\frac{1}{2} \left(\frac{\sin(\delta r / 2)}{\delta r / 2}\right)^{4}
     \left[ \cos((i-j) \delta r) + \cos((i+j) \delta r) \right]$. Then $$h(r) = \sum_{{i=0}}^{{M-1}} \sum_{{j=0}}^{{M-1}}h_{ij}(r)x_i x_j.$$

Then we obtain the following expression from [\[eqn:hfsquare\]](#eqn:hfsquare){reference-type="eqref" reference="eqn:hfsquare"}: $$\label{eq:calS}
\mathcal{S} = \sum_{n=0}^{\infty} h(r_n) = \sum_{i=0}^{M-1} \sum_{j=0}^{M-1} a_{ij} x_{i} x_{j},$$ where $a_{ij} =  \sum_{n=0}^{\infty} h_{ij}(r_n)$.

For fixed $\delta$ and $j$, introduce the following function with respect to the variable $r$: $$h(r, \delta, j) = \left(\frac{\sin(\delta r / 2)}{\delta r / 2}\right)^{4}\cos(j \delta r)$$ and its Fourier transform, which is a function of $u$: $$\begin{aligned}
g(u, \delta, j) = \frac{1}{24 \delta^4} (&6 (u - j \delta)^3 \text{sgn}(u - j \delta) + (u - 2\delta - j \delta)^3 \text{sgn}(u - 2\delta - j \delta) \\
&- 4 (u - \delta - j \delta)^3 \text{sgn}(u - \delta - j \delta) \\
&- 4 (u + \delta - j \delta)^3 \text{sgn}(u + \delta - j \delta) + (u + 2\delta - j \delta)^3 \text{sgn}(u + 2\delta - j \delta) \\
&+ 6 (u + j \delta)^3 \text{sgn}(u + j \delta) + (u - 2\delta + j \delta)^3 \text{sgn}(u - 2\delta + j \delta) \\
&- 4 (u - \delta + j \delta)^3 \text{sgn}(u - \delta + j \delta) - 4 (u + \delta + j \delta)^3 \text{sgn}(u + \delta + j \delta) \\
&+ (u + 2\delta + j \delta)^3 \text{sgn}(u + 2\delta + j \delta)).
\end{aligned}$$ For each $0\leq i\leq 2M-2 = 28$, we put $$\begin{aligned}
\calI_i & = 2(g(\X)-1)\int_0^\infty r h(r , \delta, i) \tanh(\pi r) \,dr,\\
\calG_i & = \sum_{\{\gamma\} \in \calC(\Gamma)} \frac{\La(\gamma)}{2 \sinh(\ell(\gamma)/2)}g(\ell(\gamma), \delta, i).
\end{aligned}$$ From the Selberg trace formula, we can write $$\label{eq:a_ij}
a_{ij} = \frac{1}{2}(\mathcal{I}_{|i-j|} + \mathcal{I}_{i+j} + \mathcal{G}_{|i-j|} + \mathcal{G}_{i+j}).$$

Note that each $g(u, \delta, j)$ has support in $[-(2+j)\delta, (2+j)\delta]$. For $0\leq j \leq 26$, $\calG_{j}=0$ because $\ell_0 =\sys(\X)$ is outside the support. Specifically, $(2+j)\delta\leq 28\cdot \frac{1}{5} <\ell_0 \approx 5.796$. For $j=27$ or $28$, only the conjugacy classes of the shortest length can contribute to the sum $\calG_j$. That is to say, $$\calG_{j} = \frac{252\ell_0}{2 \sinh(\ell_0/2)}g(\ell_0, \delta, j),\, j\in \{27, 28\}.$$

Let us consider $\calI_i = 2(g(\X)-1)\int_0^\infty r h(r , \delta, i) \tanh(\pi r) \,dr$. Put $\eps=10^{-3}$ and $L=10^5$. We intend to approximate $\calI_i$ by $$\calI_i' : = 2(g(\X)-1)\int_\eps^L r h(r , \delta, i) \tanh(\pi r) \,dr.$$ Let us find a bound for the deviation between $\calI_i$ and $\calI_i'$. As in [\[eq:upper_bound_I1\]](#eq:upper_bound_I1){reference-type="eqref" reference="eq:upper_bound_I1"}, we have $$\left|h(r, \delta, j)\right| \leq 1 - \frac{r^2 \delta^2}{6} + \frac{r^4 \delta^4}{80},\quad r\leq \frac{1}{\delta}.$$ From this, it follows that: $$2(g(\X)-1)\left|\int_0^\eps r h(r , \delta, i) \tanh(\pi r) \,dr\right| \leq 
2(g(\X)-1)\int_0^\eps r(1 - \frac{r^2 \delta^2}{6} + \frac{r^4 \delta^4}{80})  \,dr
<6\times 10^{-6}.$$ And using $|h(r,\delta, i)|\leq 1/r^4$, we obtain $$2(g(\X)-1)\left|\int_L^\infty r h(r , \delta, i) \tanh(\pi r) \,dr\right| \leq 
2(g(\X)-1)\int_L^\infty r(\frac{1}{\delta r/2})^4  \,dr
=6\times 10^{-6}.$$ Therefore, $$\left|\calI_i - \calI_i' \right|<1.2\times 10^{-5}.$$ In this way, we can estimate the values for $\calI_0,\dots, \calI_{28}$, $\calG_{27}$, and $\calG_{28}$ within a known error bound by utilizing interval arithmetic as detailed below: $$\begin{array}{c|c|c|c|c|c}
& \text{approximate value} & \text{error bound} & & \text{approximate value} & \text{error bound} \\
\hline
\calI_{0} & 831.2770 & 0.0000383 & \calI_{1} & -180.9242 & 0.0000419 \\
\calI_{2} & -110.5626 & 0.0000416 & \calI_{3} & -38.3114 & 0.0000548 \\
\calI_{4} & -20.5191 & 0.0000292 & \calI_{5} & -12.9689 & 0.0000616 \\
\calI_{6} & -9.0154 & 0.0000125 & \calI_{7} & -6.6722 & 0.0000182 \\
\calI_{8} & -5.1618 & 0.0000379 & \calI_{9} & -4.1264 & 0.0000124 \\
\calI_{10} & -3.3822 & 0.0000410 & \calI_{11} & -2.8265 & 0.0000515 \\
\calI_{12} & -2.3986 & 0.0000387 & \calI_{13} & -2.0604 & 0.0000594 \\
\calI_{14} & -1.7873 & 0.0000287 & \calI_{15} & -1.5626 & 0.0000498 \\
\calI_{16} & -1.3749 & 0.0000347 & \calI_{17} & -1.2160 & 0.0000273 \\
\calI_{18} & -1.0800 & 0.0000193 & \calI_{19} & -0.9625 & 0.0000470 \\
\calI_{20} & -0.8601 & 0.0000281 & \calI_{21} & -0.7704 & 0.0000150 \\
\calI_{22} & -0.6913 & 0.0000281 & \calI_{23} & -0.6213 & 0.0000201 \\
\calI_{24} & -0.5591 & 0.0000605 & \calI_{25} & -0.5036 & 0.0000570 \\
\calI_{26} & -0.4539 & 0.0000547 & \calI_{27} & -0.4095 & 0.0000170 \\
\calI_{28} & -0.3696 & 0.0000159 & & & \\
\hline
\calG_{27} & 0.0002 & 0.0000414 & \calG_{28} & 35.5542 & 0.0000587 \\
\end{array}$$ See the Sage notebook `subinterval2.ipynb` for the necessary numerical calculations.

By applying interval arithmetic to [\[eq:calS\]](#eq:calS){reference-type="eqref" reference="eq:calS"} and [\[eq:a_ij\]](#eq:a_ij){reference-type="eqref" reference="eq:a_ij"}, we finally obtain $$\calS- h(r_0) < 6.76,$$ thereby establishing the proposition. ◻
:::

::: lemma
[]{#lem:subinterval2 label="lem:subinterval2"} For $r\in [0,0.87]$, $h(r)\geq 1$.
:::

::: proof
*Proof.* For each $0\leq i\leq 14$, we have $x_i>0$ and the functions $\left(\frac{\sin(\delta r / 2)}{\delta r / 2}\right)^{2}$ and $\cos(i\delta r)$ are monotonically decreasing over the given interval since $i\delta = i/5 < \pi$. Thus, $f(r)$ in [\[eqn:hsqrth\]](#eqn:hsqrth){reference-type="eqref" reference="eqn:hsqrth"} is monotonically decreasing over $[0,0.87]$. Using interval arithmetic, we can check $f(0.87)\geq 1$; see the Sage notebook `subinterval2.ipynb` for the evaluation of $f(0.87)$. This implies $f(r)\geq 1$ for $r\in [0,0.87]$. ◻
:::

::: prop
[]{#prop:subinterval2 label="prop:subinterval2"} There is no eigenvalue in the interval $[1/4,1]$.
:::

::: proof
*Proof.* From , we know $\la_1\geq 1/4$. Therefore, $r_n\in \R$ for all $n\geq 1$. Assume that $0\leq r_1 \leq 0.87$. Then we have $\calS-h(r_0)=\sum_{n=1}^{\infty} h(r_n)\geq 7$ because the multiplicity of $\la_1$ is at least 7 (Lemma [\[prop:mult7\]](#prop:mult7){reference-type="ref" reference="prop:mult7"}), $h(r_1)\geq 1$ (Lemma [\[lem:subinterval2\]](#lem:subinterval2){reference-type="ref" reference="lem:subinterval2"}), and $h(r)=f(r)^2\geq 0$ for all $r\in \R$ [\[eqn:hfsquare\]](#eqn:hfsquare){reference-type="eqref" reference="eqn:hfsquare"}. This contradicts Proposition [\[prop:upper_bound_II\]](#prop:upper_bound_II){reference-type="ref" reference="prop:upper_bound_II"}.

Therefore, $r_1 > 0.87$ and $\la_1 = r_1^2+1/4>1.0069>1$. ◻
:::

## Proof of $\la_1\notin [1,1.23]$ {#subsec:subinterval3}

::: prop
[]{#prop:subinterval3 label="prop:subinterval3"} There is no eigenvalue in the interval $[1,1.23]$.
:::

::: proof
*Proof.* Let $a = 1$ and $b=1.23$. We define the test functions $h,g$ as in [\[eq:gh_hermite\]](#eq:gh_hermite){reference-type="eqref" reference="eq:gh_hermite"}. We choose the sequence of rational numbers $\{s_n\}_{n=0}^{17}$ such that the two polynomials $$\begin{aligned}
u(y) &= \sum_{n=0}^{17} s_n L_n^{(-1/2)}(y),\\
v(y) &= \sum_{n=0}^{17} (-1)^n s_n L_n^{(-1/2)}(y),
\end{aligned}$$ meet the following conditions:

-   $u(y)$ has a simple root at $33$ and a double root at $1937$.

-   $v(y)$ possesses double roots at 1.83, 4.94, 9.86, 15.35, 22.16, 32.22, 46.41 and additionally fulfills the condition $v(a-1/4) = 1$.

The above conditions produce a system of linear equations for the coefficients $\{s_n\}_{n=0}^{17}$. This system has a unique solution over the rationals.

For the necessary numerical computations in this proof, see the Sage notebook `subinterval3.ipynb`. We can confirm that both $u$ and $v$ have roots with the specified orders at the designated locations.

Recall that $\ff(x) = u(x^2) e^{-x^2/2}$ and $\hatf(\xi)=v(\xi^2) e^{-\xi^2/2}$. We need to ensure that they satisfy the following conditions:

1.  $\ff(x)\leq 0$ for every $x \geq \sys(\X)$.

2.  $\hatf(r(\la))\geq c=0.32388$ for every $\la \in [a, b]$.

3.  $\hatf(r(\la))\geq 0$ for every $\la \geq b$.

To count the number of zeros of a polynomial over a given interval, we can employ Sturm's theorem. This has been implemented in `PARI/GP` [@PARI2], and is also accessible through `Sage`.

\(1\) We can count the number of zeros of $u$ in $[33, \infty)$ to make sure that it does not change sign, and verify that $u''$ is negative at its unique double zero so that $u$ and hence $\ff$ is non-positive on $[\sqrt{33},\infty)$. Because $\sqrt{33}<5.75<\sys(\X)$, $\ff(x)\leq 0$ for $x \geq \sys(\X)$.

\(2\) We verify that $2v'-2v$ does not have a root between $a-1/4$ and $b-1/4$. This implies that $\hatf$ does not exhibit a critical point within the interval from $r(a)$ to $r(b)$ since the derivative of $\hatf$ is given by: $$\hatf'(\xi) = (2v'(\xi^2)-v(\xi^2)) e^{-\xi^2/2} \xi.$$ This implies that the minimum of $\hatf$ on the interval $[r(a),r(b)]$ is achieved at the endpoints. Using interval arithmetic, we can check that $\hatf(r(\la)) \geq  c$ for $\la\in [a, b]$. Note that $\hatf(r(a)) \approx 0.6872893$ and $\hatf(r(b)) \approx 0.3238802$.

\(3\) To demonstrate that $\hatf(r(\la)) \geq 0$ holds for all $\la \geq b$, it's necessary to confirm that $\hatf$ retains a consistent sign over the interval $[r(b), \infty)$. To this end, we apply Sturm's theorem to verify that $v$ has precisely $7$ distinct zeros, all of which are double zeros, in the interval $[b-1/4,\infty)$. Consequently, we deduce that $v$ does not change sign over $[b-1/4,\infty)$ and, hence, $\hatf\geq 0$ over the interval $[r(b),\infty)$ because $\hatf(r(b)) \geq c$.

With the above test functions $h,g$, we will establish the following inequalities: $$\mathcal{I} \leq 9.197, \quad \mathcal{G} \leq -0.10356, \quad -\hatf(r_0) \leq -6.854.$$

To find an upper bound for $\calI$, we separate the integral into two parts $\calI = \calI_1+\calI_2$ : $$\begin{aligned}
\calI_1 & = 2(g(\X)-1) \int_0^{100} r \hatf(r) \tanh(\pi r) dr,\\
\calI_2 & = 2(g(\X)-1) \int_{100}^\infty r \hatf(r) \tanh(\pi r) dr.
\end{aligned}$$ Using interval arithmetic, we can find $$\calI_1 \leq 9.1971.$$ For the remaining part, we have $$\calI_2 = 2(g(\X)-1) \int_{100}^\infty r \hatf(r) \tanh(\pi r) dr\leq 2(g(\X)-1) \int_{100}^\infty r \hatf(r)dr.$$ Observe that for any odd integer $k\geq 1$, the function $r^k e^{-\frac{r^2}{2}}$ has an antiderivative of the form of $e^{-\frac{r^2}{2}}$ multiplied by a polynomial in $r$. Consequently, the function $r \hatf(r) = r \, v(r^2) e^{-r^2/2}$ has an antiderivative of the form $V(r) = p(r)e^{-r^2/2}$, where $p$ is a polynomial. By evaluating it, we obtain the inequality $$\calI_2 \leq -2(g(\X)-1)V(100) \approx 1.747\times 10^{-2124}.$$ Thus, $\calI_2$ is so small as to be practically negligible in comparison to $\calI_1$.

Now we turn to $\calG$. Because $\ff(x)\leq 0$ for every $x \geq \sys(\X)$, $$\begin{aligned}
\calG & = \frac{1}{\sqrt{2\pi}}\sum_{\{\gamma\} \in \calC(\Gamma)} \frac{\La(\gamma)}{2 \sinh(\ell(\gamma)/2)} \ff(\ell(\gamma)) \\
& \leq \frac{1}{\sqrt{2\pi}}\sum_{\{\gamma\} \in P} \frac{\ell(\gamma)}{2\sinh(\ell(\gamma)/2)} \ff(\ell(\gamma)),
\end{aligned}$$ where $P$ is any subset of $\calC(\Gamma)$. By employing interval arithmetic to sum over conjugacy classes with the two shortest lengths described in , we obtain $$\calG \leq -0.10356.$$

Finally, we can verify that $\hatf(r_0)\geq 6.854$ using interval arithmetic.

Now we put these pieces together. Because $\hatf(r(\la))\geq 0$ for $\la \geq b$, the Selberg trace formula gives $$\calI+\calG = \calS  =  \sum_{n=1}^{\infty}\hatf(r_n)
\geq \hatf(r_0)+ \sum_{\substack{n=1 \\ \la_n\in [a,b]}}^{\infty}
\hatf(r_n).$$ From $\hatf(r(\la))\geq c$ for $\la\in [a,b]$, we obtain $$\calI+\calG - \hatf(r_0)  \geq  c m(a,b),$$ where $m(a,b)$ denote the number of eigenvalues of the Laplacian in the interval $[a,b]$ counting multiplicity. Therefore, $m(a,b)$ is less than or equal to $$\frac{1}{c}\left(\calI+\calG - \hatf(r_0) \right) \leq 6.9148<7.$$ From Lemma [\[prop:mult7\]](#prop:mult7){reference-type="ref" reference="prop:mult7"}, we can finish the proof of the proposition. ◻
:::

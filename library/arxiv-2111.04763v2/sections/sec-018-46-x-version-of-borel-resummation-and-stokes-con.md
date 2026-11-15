---
doc_id: arxiv-2111.04763v2
doc_title: "Resurgence of Chern-Simons theory at the trivial flat connection"
section_id: sec-018-46-x-version-of-borel-resummation-and-stokes-con
section_title: "x-version of Borel resummation and Stokes constants"
section_number: 4.6
pages: 48-52
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.921
doc_brief: "Resurgence of Chern-Simons theory at the trivial flat connection — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
[]{#sub.52borelx label="sub.52borelx"}

In this section we discuss the $x$-deformation version of Section [\[sub.52borel\]](#sub.52borel){reference-type="ref" reference="sub.52borel"}. The asymptotic series $\Phi^{(\sigma_j)}(\tau)$ for $j=0,1,2,3$ are extended to series $\Phi^{(\sigma_j)}(x;\tau)$ with coefficients in $\mathbb{Z}(x^{\pm 1})$. The series $\Phi^{(\sigma_j)}(x;\tau)$ for $j=1,2,3$ are defined in terms of perturbation theory of a deformed state-integral [@AK] and they have been computed with about 200 terms for many values of $x$ in [@GGM:peacock]. Let $\xi_j$ ($j=1,2,3$) be three roots to the equation $$(1-\xi)(1-x\xi)(1-x^{-1}\xi) = \xi^2,$$ ordered such that they reduce to [\[eq:xi\]](#eq:xi){reference-type="eqref" reference="eq:xi"} in the limit $x\rightarrow 1$. The series $\Phi^{(\sigma_j)}(\tau)$ ($j=1,2,3$) can be uniformly written as[^1] $$\Phi^{(\sigma_j)}(x;\tau) = \frac{{\rm e}^{\frac{3\pi{\rm i}}{4}}}{\sqrt{\delta_j(x)}}
    {\rm e}^{\frac{V_j(x)}{2\pi{\rm i}\tau}} \varphi^{(\sigma_j)}(x;\tau)$$ where $\delta_j(x) = \xi_j-s \xi_j^{-1}+2 \xi_j^{-2}$ and $$\label{Vx52}
  \begin{aligned}
    V_1(x) &=
      -\mathrm{Li}_2(\xi_1^{-1})-\mathrm{Li}_2(x\xi_1^{-1})-\mathrm{Li}_2(x^{-1}\xi_1^{-1})
      +\frac{1}{2}\log^2 x -\frac{1}{2}\log^2 \xi_1
      +\pi{\rm i}\log\xi_1+\frac{2\pi^2}{3},\\
    V_2(x) &=
      -\mathrm{Li}_2(\xi_2^{-1})-\mathrm{Li}_2(x\xi_2^{-1})-\mathrm{Li}_2(x^{-1}\xi_2^{-1})
      +\frac{1}{2}\log^2 x -\frac{1}{2}\log^2 \xi_2
      -\pi{\rm i}\log\xi_2+\frac{2\pi^2}{3},\\
    V_3(x) &=
      -\mathrm{Li}_2(\xi_3^{-1})-\mathrm{Li}_2(x\xi_3^{-1})-\mathrm{Li}_2(x^{-1}\xi_3^{-1})
      +\frac{1}{2}\log^2 x -\frac{1}{2}\log^2 \xi_3
      +3\pi{\rm i}\log\xi_3+\frac{2\pi^2}{3}.
  \end{aligned}$$ The power series $\varphi^{(\sigma_j)}(x;\tau)$ are $$\begin{aligned}
  \varphi^{(\sigma_j)}(x;\tfrac{\tau}{2\pi{\rm i}}) =
  &1 + \frac{\tau}{12\delta_j(x)}\big((-397 - 94 s - 114 s^2 + 390 s^3 - 278 s^4 + 81 s^5 - 10 s^6)\nonumber \\
  &+(-381 + 623 s - 124 s^2 - 328 s^3 + 268 s^4 - 81 s^5 + 10 s^6)
    \xi_j\nonumber \\
  &+(-270 + 137 s + 182 s^2 - 207 s^3 + 71 s^4 - 10 s^5) \xi_j^2
    \big)+\ldots
\end{aligned}$$ with $$s = s(x) = x^{-1}+1+x.$$

The additional series $\Phi^{(\sigma_0)}(x;\tau)$, as in Section [\[sub.41Phi0xq\]](#sub.41Phi0xq){reference-type="ref" reference="sub.41Phi0xq"}, can be computed either from the colored Jones polynomial or by using Habiro's expansion of the colored Jones polynomials. We find $$\Phi^{(\sigma_0)}(x;\tau) = \varphi^{(\sigma_0)}(x;\tau),$$ where the power series $\varphi^{(\sigma_0)}(x;\tau)$ reads $$\phi^{(\sigma_0)}(x;\tfrac{\tau}{2\pi{\rm i}}) = \frac{1}{2x+2x^{-1}-3}
  -\frac{(x^{1/2}-x^{-1/2})^2(5x+5x^{-1}-4)}{(2x+2x^{-1}-3)^3}\tau+\ldots,$$

<figure id="fg:52x_brplane">

<figcaption>Singularities of Borel transforms of <span class="math inline"><em>φ</em><sup>(<em>σ</em><sub><em>j</em></sub>)</sup>(<em>x</em>,<em>τ</em>)</span> for <span class="math inline"><em>j</em> = 0, 1, 2, 3</span> of the knot <span class="math inline"><strong>5</strong><sub>2</sub></span>.</figcaption>
</figure>

We are interested in the Stokes automorphisms in the upper half plane of the Borel resummation of the 4-vector $\Phi(x;\tau)$ of asymptotic series $$\Phi(x;\tau) =
  \begin{pmatrix}
    \Phi^{(\sigma_0)}(x;\tau)\\
    \Phi^{(\sigma_1)}(x;\tau)\\
    \Phi^{(\sigma_2)}(x;\tau)\\
    \Phi^{(\sigma_3)}(x;\tau)
  \end{pmatrix},$$ when $x$ is close to 1. The singular points of the Borel transform of $\Phi(x;\tau)$, collectively denoted as $\Lambda(x)$, are smooth functions of $x$ and they are equal to $\Lambda$ in [\[eq:Lmb52\]](#eq:Lmb52){reference-type="eqref" reference="eq:Lmb52"} in the limit $x\rightarrow 1$. When $x$ is slightly away from 1, each singular point $\iota_{i,j}^{(k)}$ in $\Lambda$ splits to a finite set of points located at $\iota_{i,j}^{(k,\ell)}:=\iota_{i,j}^{(k)}+\ell \log(x)$, $\ell\in\mathbb{Z}$. We illustrate this schematically in Fig. [1](#fg:52x_brplane){reference-type="ref" reference="fg:52x_brplane"}. The complex plane of $\tau$ is divided by rays passing through these singular points into infinitely many cones. We will then pick the cones $I$ and $II$ located slightly above the positive and negative real axes, and compute the global Stokes matrix from cone $I$ to cone $II$ defined by

$$\Delta(x,\tau) s_{II}(x,\tau) = \mathfrak{S}_{I\rightarrow II}(\tilde{x},\tilde{q})
  \Delta(x,\tau) s_{I}(x,\tau),
  \label{eq:SRRx}$$ where $$\Delta(x,\tau) =
  \mathrm{diag}\left(\tau^{1/2}\frac{x^{1/2}-x^{-1/2}}{\tilde{x}^{1/2}-\tilde{x}^{-1/2}},1,1,1\right).$$ The global Stokes matrix $\mathfrak{S}_{I\rightarrow II}(\tilde{x},\tilde{q})$ factorises uniquely into a product of local Stokes automorphisms associated to each of the singular points in the upper half plane, from which the individual Stokes constants can be read off.

The global Stokes matrix $\mathfrak{S}_{I\rightarrow II}(\tilde{x},\tilde{q})$ in [\[eq:SRRx\]](#eq:SRRx){reference-type="eqref" reference="eq:SRRx"} also has the block upper triangular form $$\begin{pmatrix}
    1&*&*&*\\
    0&*&*&*\\
    0&*&*&*\\
    0&*&*&*
  \end{pmatrix}.$$ The $3\times 3$ sub-matrices $\mathfrak{S}^{\text{red}}_{I\rightarrow II}$ in the right bottom have been worked out in [@GGM:peacock], and they are given by

$$\begin{align}
\mathfrak{S}^{\text{red}}_{I\rightarrow II}(\tilde{x},\tilde{q})
&=\frac{1}{2}
\begin{pmatrix}
0&1&0\\0&1&1\\-1&0&0
\end{pmatrix} \mathbf J^\mathrm{red}_{-1}(\tilde{x};\tilde{q}^{-1})^T
\begin{pmatrix}
1&0&0\\0&0&1\\0&1&0
\end{pmatrix} \mathbf J^\mathrm{red}_{-1}(\tilde{x};\tilde{q})
\begin{pmatrix}
 0&0&-1\\1&-\tilde{s}&0\\0&1&0
\end{pmatrix},
\quad
|\tilde{q}|<1,\label{eq:SRed12x}
\end{align}$$ where $$\tilde{s}= s(\tilde{x}),$$ and $\mathbf J^{\mathrm{red}}(x,q)$ is given by [\[Jred52x\]](#Jred52x){reference-type="eqref" reference="Jred52x"}. To calculate the first row of $\mathfrak{S}_{I\rightarrow II}(\tilde{x},\tilde{q})$, we use the additional holomorphic block $D_m(x,q)$.

::: conjecture
For every cone $R\subset \Lambda(x)$ and every $\tau \in R$, we have

$$D_0(x,q) = s_R(\Phi^{(\sigma_0)})(x;\tau) +
    \tau^{-1/2}\frac{\tilde{x}^{1/2}-\tilde{x}^{-1/2}}{x^{1/2}-x^{-1/2}}
    \sum_{j=1}^3 M_{R,j}(\tilde{x},\tilde{q})s_R(\Phi^{(\sigma_j)})(x;\tau),
    \label{eq:QMPhix}$$ where $M_{R,j}(\tilde{x},\tilde{q})$ ($j=1,2,3$) are $\tilde{q}$-series

with coefficients in $\mathbb{Z}(\tilde{x}^{\pm 1})$ depending on the cone $R$.
:::

We present $M_{R,j}(\tilde{x},\tilde{q})$ in terms of the row vector $M_R(\tilde{x},\tilde{q}) := (M_{R,1},M_{R,2},M_{R,3})(\tilde{x},\tilde{q})$, and it can be expressed in terms of a $3\times 3$ matrix $M^{(\sigma_0)}_R(\tilde{x},\tilde{q})$ $$M_R(\tilde{x},\tilde{q})
  = \left(\tilde{q}D_0(\tilde{x},\tilde{q}),\tilde{q}^2D_1(\tilde{x},\tilde{q}),\tilde{q}^3D_2(\tilde{x},\tilde{q})\right)
  M^{(\sigma_0)}_R(\tilde{x},\tilde{q}).
  \label{eq:MMs0}$$

::: conjecture
Equation [\[eq:QMPhi\]](#eq:QMPhi){reference-type="eqref" reference="eq:QMPhi"} holds in the cones $R=I,II$ where the $\tilde{q}$- series $M_{R,j}(\tilde{q})$ are given in terms of $M_R^{(0)}(\tilde{x},\tilde{q})$ through [\[eq:MMs0\]](#eq:MMs0){reference-type="eqref" reference="eq:MMs0"} which are as follows $$\begin{align}
    M^{(\sigma_0)}_{I}(\tilde{x},\tilde{q}) =
    &\begin{pmatrix}
       1&-1&-\tilde{s}\,\tilde{q}\\0&-1&-1+\tilde{s}\,\tilde{q}\\0&0&-\tilde{q}
     \end{pmatrix},\\
    M^{(\sigma_0)}_{II}(\tilde{x},\tilde{q}) =
    &\begin{pmatrix}
       -1&1&-\tilde{s}\,\tilde{q}\\-1&0&-1+\tilde{s}\,\tilde{q}\\0&0&-\tilde{q}
     \end{pmatrix}.
    
    
    
    
    
    
    
    
  \end{align}$$
:::

Eqs. [\[eq:QMPhix\]](#eq:QMPhix){reference-type="eqref" reference="eq:QMPhix"}, together with the reduced Stokes matrices $\mathfrak{S}^{\text{red}}_{I\rightarrow II}(\tilde{x},\tilde{q})$ for $\Phi^{(\sigma_j)}(x;\tau)$ ($j=1,2,3$), allow us to calculate entries in the first row of $\mathfrak{S}_{I\rightarrow
  II}(\tilde{x},\tilde{q})$ by $$\mathfrak{S}_{I\rightarrow II}(\tilde{x},\tilde{q})_{0,j} =
  M_{I,j}(\tilde{x},\tilde{q}) - \sum_{k=1}^3M_{II,k}(\tilde{x},\tilde{q})
  \mathfrak{S}^{\text{red}}_{I\rightarrow II}(\tilde{x},\tilde{q})_{k,j},\quad j=1,2,3.$$ In the following we list the first few terms of these $\tilde{q}$ -series. $$\begin{aligned}
    \mathfrak{S}_{I\rightarrow II}(\tilde{x},\tilde{q})_{0,1}=
    &-1+(1+\tilde{s}+\tilde{s}^2)\tilde{q}-(-2\tilde{s}-\tilde{s}^2+\tilde{s}^3)\tilde{q}^2-(1+\tilde{s}^4)\tilde{q}^3
      +O(\tilde{q}^4) ,\\
    \mathfrak{S}_{I\rightarrow II}(\tilde{x},\tilde{q})_{0,2}=
    &1-(1+2\tilde{s}+\tilde{s}^2)\tilde{q}+(-\tilde{s}-\tilde{s}^2+2\tilde{s}^3)\tilde{q}^2+(3\tilde{s}^2+\tilde{s}^3+\tilde{s}^4)\tilde{s}^3
      +O(\tilde{q}^4) ,\\
    \mathfrak{S}_{I\rightarrow II}(\tilde{x},\tilde{q})_{0,3}=
    &-\tilde{q}+(1+\tilde{s}^2)\tilde{q}^2+(3\tilde{s}+\tilde{s}^2)\tilde{q}^3+O(\tilde{q}^4).
  \end{aligned}$$

Finally, we can factorise the global Stokes matrices $\mathfrak{S}_{I\rightarrow II}(\tilde{x},\tilde{q})$

to obtain local Stokes matrices associated to individual singular points in $\Lambda$ and extract the associated Stokes constants. The Stokes constants for $\Phi^{(\sigma_j)}(x;\tau)$ ($j=1,2,3$) are already given in [@GGM:resurgent; @GGM:peacock]. We collect the Stokes contants for $\Phi^{(\sigma_0)}(x;\tau)$ in the generating series $$\mathsf{S}^+_{0,j}(\tilde{x},\tilde{q}) = \sum_{k\geq 0}\sum_{\ell}
  \mathcal{S}^{(k,\ell)}_{0,j}\tilde{x}^\ell\tilde{q}^k,
  
  
  \quad j=1,2,3.$$ And we find that $$\begin{aligned}
    \mathsf{S}^+_{0,1}(\tilde{x},\tilde{q}) =
    &-1+\tilde{q}+\tilde{s}\tilde{q}^2+(-2+3\tilde{s}^2)\tilde{q}^3+(2-\tilde{s}-2\tilde{s}^2+5\tilde{s}^3+2\tilde{s}^4)\tilde{q}^4
      +O(\tilde{q}^5),\\
    \mathsf{S}^+_{0,2}(\tilde{x},\tilde{q}) =
    &1-\tilde{q}-\tilde{s}\tilde{q}^2-(-2+3\tilde{s}^2)\tilde{q}^3+(2-\tilde{s}-2\tilde{s}^2+5\tilde{s}^3+2\tilde{s}^4)\tilde{q}^4
      +O(\tilde{q}^5),\\
    \mathsf{S}^+_{0,3}(\tilde{x},\tilde{q}) =
    &0.
  \end{aligned}$$

[^1]: The series $\Phi^{(\sigma_j)}(x;\tau)$ ($j=1,2,3$) are related to the series in [@GGM:resurgent; @GGM:peacock], which we will denote by $\Phi^{(\sigma_j)}_{\text{GGM}}(x;\tau)$, by a common prefactor $$\Phi^{(\sigma_j)}(x;\tau) = {\rm i}
        {\rm e}^{-\frac{\pi{\rm i}}{12}(\tau+\tau^{-1})-2\pi{\rm i}\tau}
        \Phi^{(\sigma_j)}_{\text{GGM}}(x;\tau),\quad j=1,2,3.$$ The Stokes constants associated to the Borel resummation of $\Phi^{(\sigma_j)}_{\text{GGM}}(\tau)$ are not changed.

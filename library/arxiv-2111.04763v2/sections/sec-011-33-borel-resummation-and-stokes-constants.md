---
doc_id: arxiv-2111.04763v2
doc_title: "Resurgence of Chern-Simons theory at the trivial flat connection"
section_id: sec-011-33-borel-resummation-and-stokes-constants
section_title: "Borel resummation and Stokes constants"
section_number: 3.3
pages: 27-33
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.763
latex_coverage_ratio: 0.716
doc_brief: "Resurgence of Chern-Simons theory at the trivial flat connection — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
[]{#sub.41borel label="sub.41borel"}

In this section we discuss the asymptotic expansion as $q = {\rm e}^{2\pi{\rm i}\tau}\rightarrow 1$ of the vector $G(q)$ of $q$-series and relate it to the vector $\Phi(\tau)$ of the asymptotic series, where $$G(q) =
  \begin{pmatrix}
    G^{(2)}(q) \\
    G^{(1)}(q) \\
    G^{(0)}(q)
  \end{pmatrix}, \qquad
  \Phi(\tau) =
  \begin{pmatrix}
    \Phi^{(\sigma_0)}(\tau)\\
    \Phi^{(\sigma_1)}(\tau)\\
    \Phi^{(\sigma_2)}(\tau)
  \end{pmatrix}
  \label{eq:Gq}$$ with $G^{(0)}(q), G^{(1)}(q)$ given in [\[G01\]](#G01){reference-type="eqref" reference="G01"}, and the additional series $G^{(2)}(q)$ given in [\[G2\]](#G2){reference-type="eqref" reference="G2"}.

The three power series $\Phi^{(\sigma_j)}(\tau)$, $j=0,1,2$ can be resummed by Borel resummation. On the other hand, according to the resurgence theory, the value of the Borel resummation of an asymptotic power series depends crucially on the argument of the expansion variable. If the Borel transform of the power series has a singular point located at $\iota$, the values of the Borel resummation of the power series whose expansion variable has an argument slightly greater and less than the angle $\theta = \arg \iota$ differ by an exponentially small quantity, called the Stokes discontinuity. Usually the difference is identical with the Borel resummation of another power series in the theory, a phenomenon called the Stokes automorphism.

![Singularities of the Borel transforms of $\varphi^{(\sigma_j)}(\tau)$ for $j=0,1,2$ of the knot $\mathbf{4}_1$.](41_brplane){#fg:41_brplane height="6cm"}

In the case of the power series $\Phi^{(\sigma_j)}(\tau)$, $j=0,1,2$, the singularities of the Borel transforms of $\Phi^{(\sigma_j)}(\tau)$, $j=1,2$ were already studied in [@GGM:resurgent; @GGM:peacock], and they are located at $$\Lambda^{(\sigma_j)} = \{ \iota_{j,i} +2\pi{\rm i}k\;|\; i=1,2,i\neq j,\,
  k\in\mathbb{Z}\}\cup
  \{2\pi{\rm i}k\;|\; k\in\mathbb{Z}_{\neq 0}\},\quad j=1,2,
  \label{eq:Lmb12}$$ as shown in the middle and the right panels of Fig. [1](#fg:41_brplane){reference-type="ref" reference="fg:41_brplane"}, while the singularities of the Borel transform of $\Phi^{(\sigma_0)}(\tau)$ are located at (see also [@Ga:resurgence Conj. 4]) $$\Lambda^{(\sigma_0)} = \{\iota_{0,i} +2\pi{\rm i}k\;|\; i=1,2,\,k\in\mathbb{Z}\},
  \label{eq:Lmb0}$$ as shown in the left panel of Fig. [1](#fg:41_brplane){reference-type="ref" reference="fg:41_brplane"}, where $$\iota_{j,i} = \frac{V(\sigma_j) - V(\sigma_i)}{2\pi{\rm i}},\quad
  i,j=0,1,2.$$ All the rays $\rho_\theta$ (Stokes rays) passing through the singularities in the union $$\Lambda = \cup_{j=0,1,2} \Lambda^{(\sigma_j)},
  \label{eq:Lmb}$$ form a peacock pattern, cf. Fig. [2](#fg:41_rays){reference-type="ref" reference="fg:41_rays"}, and they divide the complex plane of Borel transform into infinitely many cones. The Borel resummation of the vector $\Phi(\tau)$ is only well-defined within one of these cones.

Recall that the Borel transform $\widehat{\varphi}(\zeta)$ of a Gevrey-1 power series $\varphi(\tau)$ $$\varphi(\tau) = \sum_{n=0}^\infty a_n\tau^n,\quad a_n = O(C^n n!),$$ is defined by $$\widehat{\varphi}(\zeta) =\sum_{n=0}^\infty \frac{a_n}{n!}\zeta^n.$$ If it analytically continues to an $L^1$-analytic function along the ray $\rho_\theta:={\rm e}^{{\rm i}\theta}\mathbb{R}_+$ where $\theta = \arg\tau$, we define the Borel resummation by the Laplace integral $$s_\theta(\varphi)(\tau) =
  \int_0^\infty \widehat{\varphi}(\tau\zeta)
  {\rm e}^{-\zeta}{\rm d}\zeta =
  \frac{1}{\tau}\int_{\rho_\theta}
  \widehat{\varphi}(\zeta){\rm e}^{-\zeta/\tau}{\rm d}
  \zeta.
  \label{eq:svarphi}$$ The Borel resummation of the trans-series $\Phi(\tau) =
{\rm e}^{\frac{V}{2\pi{\rm i}\tau}}\varphi(\tau)$ is defined to be $$s_\theta(\Phi)(\tau) =
  {\rm e}^{\frac{V}{2\pi{\rm i}\tau}}s_\theta(\varphi)(\tau).
  \label{eq:sPhi}$$ In the following we will also use the notation $s_R(\Phi)(\tau)$ when the argument of $\tau$ is in the cone $R$ and it is a continuous function of $\tau$.

Coming back to the vector of $q$-series $G(q)$, we find that the asymptotic expansion of $G(q)$ when $q=e^{2\pi{\rm i}\tau}$ and $\tau \to 0$ in a cone $R$ can be expressed in terms of $\Phi(\tau)$. Moreover, this asymptotic expansion can be lifted to an exact identity between $q$-series $G^{(j)}(q)$ and linear combinations of Borel resummation of $\Phi^{(\sigma_j)}(\tau)$ multiplied by power series in $\tilde{q}= {\rm e}^{-2\pi{\rm i}\tau^{-1}}$ (thought of as exponentially small corrections) with integer coefficients. This is the content of the following conjecture.

::: conjecture
[]{#conj-exact-ra label="conj-exact-ra"} For every cone $R \subset \mathbbm C\setminus \Lambda$ and every $\tau \in R$, we have $$\Delta'(\tau) G(q) = M_R(\tilde{q}) \Delta(\tau)
    s_R(\Phi)(\tau),
    \label{eq:GMsPhi}$$ where $$\Delta'(\tau) = \mathrm{diag}(\tau^{3/2},\tau^{1/2},\tau^{-1/2}),\quad
    \Delta(\tau) = \mathrm{diag}(\tau^{3/2},1,1),$$ and $M_R(\tilde{q})$ is a $3\times 3$ matrix of $\tilde{q}$ (resp., $\tilde{q}^{-1}$)-series if $\mathrm{Im}\tau>0$ (resp., $\mathrm{Im}\tau<0$) with integer coefficients that depend on $R$.
:::

![Stokes rays and cones in the $\tau$-plane for the 3-vector $\Phi(\tau)$ of asymptotic series of the knot $\mathbf{4}_1$.](41_rays){#fg:41_rays height="8cm"}

As in [@GGM:resurgent; @GGM:peacock], we pick out in particular four of these cones, located slightly above and below the positive or the negative real axis, labeled in clockwise direction by $I,II,III,IV$ as indicated in Fig. [2](#fg:41_rays){reference-type="ref" reference="fg:41_rays"}. We work out the exact matrices $M_R(\tilde{q})$ in these four cones.

::: conjecture
[]{#conj-exact-regions label="conj-exact-regions"} Equation [\[eq:GMsPhi\]](#eq:GMsPhi){reference-type="eqref" reference="eq:GMsPhi"} holds in the cones $R=I,II,III,IV$ where the matrices $M_R(\tilde{q})$ are given in terms of $\mathbf J_{-1}(\tilde{q})$ as follows $$\begin{align}
      M_I(\tilde{q}) &=
      \mathbf J_{-1}(\tilde{q})
        \begin{pmatrix}
          1 & 0 & 0\\
          0 & 0 & -1\\
          0 & 1 & -1
        \end{pmatrix}, & |\tilde{q}|<1,
                  \label{eq:M1}\\
      M_{II}(\tilde{q}) &=
      \begin{pmatrix}
        1 & 0 & 0\\
        0 & -1& 0\\
        0 & 0 & 1
      \end{pmatrix}
                \mathbf J_{-1}(\tilde{q})
                \begin{pmatrix}
                  1&0&0\\
                  0&1&0\\
                  0&1&-1
                \end{pmatrix}, & |\tilde{q}|<1,
                         \label{eq:M2}\\
      M_{III}(\tilde{q}) &=
                     \begin{pmatrix}
        1 & 0 & 0\\
        0 & -1& 0\\
        0 & 0 & 1
      \end{pmatrix}
      \mathbf J_{-1}(\tilde{q})
        \begin{pmatrix}
          1&1&0\\
          0&-1&0\\
          0&2&1
        \end{pmatrix}, & |\tilde{q}|>1,
                         \label{eq:M3}\\      
      M_{IV}(\tilde{q}) &=
                    \mathbf J_{-1}(\tilde{q})
    \begin{pmatrix}
      1&0&1\\
      0&0&-1\\
      0&1&2
    \end{pmatrix}, & |\tilde{q}| >1.
           \label{eq:M4}
    \end{align}$$
:::

We now discuss the Stokes automorphism. To any singularity in the Borel plane located at $\iota_{i,j}^{(k)}:= \iota_{i,j}+2\pi{\rm i}k$, we can associate a local Stokes matrix $$\mathfrak{S}_{\iota_{i,j}^{(k)}}(\tilde{q}) = I + \mathcal{S}_{i,j}^{(k)}\tilde{q}^k
  E_{i,j},\quad  \mathcal{S}_{i,j}^{(k)}\in\mathbb{Z},$$ where $E_{i,j}$ is the elementary matrix with $(i,j)$-entry 1 ($i,j=0,1,2$) and all other entries zero, and $\mathcal{S}_{i,j}^{(k)}$ is the Stokes constant. Let us assume the *locality* condition that no two Borel singularities share the same argument, or if there are, their Stokes matrices commute. This is indeed the case in our example. Then for any ray of angle $\theta$, the Borel resummations of $\Phi(\tau)$ with $\tau$ whose argument is raised slight above ($\theta_+$) or lowered sightly below ($\theta_-$) $\theta$ are related by the following formula of Stokes automorphism $$\Delta(\tau) s_{\theta_+}(\Phi)(\tau) = \mathfrak{S}_{\theta}(\tilde{q})
  \Delta(\tau) s_{\theta_-}(\Phi)(\tau),\quad
  \mathfrak{S}_\theta(\tilde{q}) = \prod_{\arg\iota=\theta}\mathfrak{S}_\iota(\tilde{q}).$$ Because of the locality condition, we don't have to worry about the order of the product of local Stokes matrices.

More generally, consider two rays $\rho_{\theta^+}$ and $\rho_{\theta^-}$ whose arguments satsify $0<\theta^+-\theta^-\leq \pi$, we define the global Stokes automorphism $$\Delta(\tau)s_{\theta^+}(\Phi)(\tau) =
  \mathfrak{S}_{\theta^-\rightarrow \theta^+}(\tilde{q})
  \Delta(\tau)s_{\theta^-}(\Phi)(\tau),
  \label{eq:S-glob}$$ where both sides are analytically continued smoothly to the same value of $\tau$. The global Stokes matrix $\mathfrak{S}_{\theta^-\rightarrow\theta^+}(\tilde{q})$ satisfies the factorisation property [@GGM:resurgent; @GGM:peacock] $$\mathfrak{S}_{\theta^-\rightarrow\theta^+}(\tilde{q}) =
  \prod_{\theta^-<\theta<\theta^+}^{\leftarrow}
  \mathfrak{S}_{\theta}(\tilde{q}),
  \label{eq:S-fac}$$ where the ordered product is taken over all the local Stokes matrices whose arguments are sandwiched between $\theta^-,\theta^+$ and they are ordered with rising arguments from right to left.

Given [\[eq:GMsPhi\]](#eq:GMsPhi){reference-type="eqref" reference="eq:GMsPhi"} with explicit values of $M_R(\tilde{q})$ for $R=I,II,III,IV$, in general we can calculate the global Stokes matrix via $$\mathfrak{S}_{R\rightarrow R'}(\tilde{q}) = M_{R'}(\tilde{q})^{-1}\cdot M_{R}(\tilde{q}).
  \label{eq:SMM}$$ Here in the subscript of the global Stokes matrix on the left hand side, $R$ stands for any ray in the cone. For instance, we find that the global Stokes matrix from cone $I$ anti-clockwise to cone $II$ is $$\mathfrak{S}_{I\rightarrow II}(\tilde{q}) =
  \begin{pmatrix}
    1&0&0\\
    0&1&0\\
    0&1&-1
  \end{pmatrix}
  \mathbf J_{-1}(\tilde{q})^{-1}
  \begin{pmatrix}
    1&0&0\\
    0&-1&0\\
    0&0&1
  \end{pmatrix}
  \mathbf J_{-1}(\tilde{q})
  \begin{pmatrix}
    1&0&0\\
    0&0&-1\\
    0&1&-1
  \end{pmatrix},\quad |\tilde{q}|<1.\label{eq:S12}$$ This Stokes matrix has the block upper triangular form $$\begin{pmatrix}
    1&*&*\\
    0&*&*\\
    0&*&*
  \end{pmatrix}.\label{eq:1bd}$$ Let us note that this form implies that $\Phi^{(\sigma_j)}(\tau)$ ($j=1,2$) form a closed subset under Stokes automorphisms (this was called in [@GM:top-sting] a "minimal resurgent structure"). They are controled by the $2\times 2$ submatrix of $\mathfrak{S}_{I\rightarrow II}(\tilde{q})$ in the bottom right and one can verity that it is indeed the Stokes matrix in [@GGM:resurgent]. In addition we can also extract Stokes constants $\mathcal{S}_{0,j}^{(k)}$ ($j=1,2$, $k=1,2,\ldots$) responsible for Stokes automorphisms into $\Phi^{(\sigma_0)}(\tau)$ from Borel singularities in the upper half plane, and collect them in the generating series $$\mathsf{S}^+_{0,j}(\tilde{q}) = \sum_{k=1}^\infty
  \mathcal{S}_{0,j}^{(k)}\tilde{q}^k,\quad j=1,2.$$ We find $$\begin{aligned}
  \mathsf{S}_{0,1}^+(\tilde{q}) = \mathsf{S}_{0,2}^+(\tilde{q}) =
  &-G_0^{(2)}(\tilde{q}) - G_1^{(2)}(\tilde{q})
    +  \left(G_0^{(0)}(\tilde{q})+G_1^{(0)}(\tilde{q})\right)G_0^{(2)}(\tilde{q})
    /G_0^{(0)}(\tilde{q})\nonumber \\=
  &-\tilde{q}-2\tilde{q}^2-3\tilde{q}^3-7\tilde{q}^4-14\tilde{q}^5-34\tilde{q}^6+\ldots.
\end{aligned}$$

Similarly, we find that the global Stokes matrix from cone $III$ anti-clockwise to cone $IV$ is $$\mathfrak{S}_{III\rightarrow IV}(\tilde{q}) =
  \begin{pmatrix}
    1&0&0\\
    0&-1&1\\
    0&1&0
  \end{pmatrix}\cdot \mathbf J_{-1}(\tilde{q}^{-1})^{-1}\cdot
  \begin{pmatrix}
    1&0&0\\
    0&-1&0\\
    0&0&1
  \end{pmatrix}
  \cdot \mathbf J_{-1}(\tilde{q}^{-1})\cdot
  \begin{pmatrix}
    1&0&0\\
    0&1&0\\
    0&1&1
  \end{pmatrix},\quad |\tilde{q}|>1.\label{eq:S34}$$ It also has the form as [\[eq:1bd\]](#eq:1bd){reference-type="eqref" reference="eq:1bd"}, and the $2\times 2$ submatrix of $\mathfrak{S}_{III\rightarrow IV}(\tilde{q})$ in the bottom right is the Stokes matrix given in [@GGM:resurgent]. We also extract Stokes constants $\mathcal{S}_{0,j}^{(k)}$ ($j=1,2$, $k=-1,-2,\ldots$) responsible for Stokes automorphisms into $\Phi^{(\sigma_0)}(\tau)$ from Borel singularities in the lower half plane, and collect them in the generating series $$\mathsf{S}^-_{0,j}(\tilde{q}) = \sum_{k=-1}^{-\infty}
  \mathcal{S}_{0,j}^{(k)}\tilde{q}^k,\quad j=1,2.$$ We find $$\begin{aligned}
  \mathsf{S}_{0,2}^-(\tilde{q}) = -\mathsf{S}_{0,1}^-(\tilde{q}) = \mathsf{S}_{0,1}^+(\tilde{q}^{-1}).
\end{aligned}$$ We can also use [\[eq:SMM\]](#eq:SMM){reference-type="eqref" reference="eq:SMM"} to compute the global Stokes matrix $\mathfrak{S}_{IV\rightarrow I}(\tilde{q})$ and we find $$\mathfrak{S}_{IV\rightarrow I} = 
  \begin{pmatrix}
    1&0&1\\
    0&1&3\\
    0&0&1
  \end{pmatrix}.$$ Note that this can be identified as $\mathfrak{S}_{0}$ associated to the ray $\rho_0$ and it can be factorised as $$\mathfrak{S}_{0} = \mathfrak{S}_{\iota_{0,2}}\mathfrak{S}_{\iota_{1,2}},\quad
  \mathfrak{S}_{\iota_{0,2}} =
  \begin{pmatrix}
    1&0&1\\
    0&1&0\\
    0&0&1
  \end{pmatrix},\quad
  \mathfrak{S}_{\iota_{1,2}} =
  \begin{pmatrix}
    1&0&0\\
    0&1&3\\
    0&0&1
  \end{pmatrix}.$$ Since the local Stokes matrices $\mathfrak{S}_{\iota_{0,2}}$ and $\mathfrak{S}_{\iota_{1,2}}$ commute, the locality condition is satisfied. We read off the Stoke discontinuity formulas

$$\label{disc-pra}
\begin{aligned}
  &\text{disc}_0 \Phi^{(0)}(\tau) = \tau^{-3/2}s(\Phi^{(s_2)})(\tau),\\
  &\text{disc}_0 \Phi^{(1)}(\tau) = 3s(\Phi^{(s_2)})(\tau),
\end{aligned}$$ with $$\text{disc}_\theta\Phi(\tau) = s_{\theta_+}(\Phi)(\tau) - s_{\theta_-}(\Phi)(\tau),$$ and the second identity has already appeared in [@gh-res; @GGM:resurgent].

Finally, in order to compute the global Stokes matrix $\mathfrak{S}_{II\rightarrow III}(\tilde{q})$, we need to take into account that the odd powers of $\tau^{1/2}$ on both sides of [\[eq:GMsPhi\]](#eq:GMsPhi){reference-type="eqref" reference="eq:GMsPhi"} give rise to additional $-1$ factors when one crosses the branch cut at the negative real axis, and [\[eq:SMM\]](#eq:SMM){reference-type="eqref" reference="eq:SMM"} should be modified by $$\mathfrak{S}_{II\rightarrow III}(\tilde{q}) = \mathrm{diag}(1,-1,-1)
  M_{III}(\tilde{q})^{-1}\cdot M_{II}(\tilde{q}),$$ and we find $$\mathfrak{S}_{II\rightarrow III} = 
  \begin{pmatrix}
    1&1&0\\
    0&1&0\\
    0&-3&1
  \end{pmatrix}.$$ Similarly this can be identified as $\mathfrak{S}_{\pi}$ associated to the ray $\rho_{\pi}$ and it can be factorised as $$\mathfrak{S}_{\pi} = \mathfrak{S}_{\iota_{0,1}}\mathfrak{S}_{\iota_{2,1}},\quad
  \mathfrak{S}_{\iota_{0,1}} =
  \begin{pmatrix}
    1&1&0\\
    0&1&0\\
    0&0&1
  \end{pmatrix},\quad
  \mathfrak{S}_{\iota_{2,1}} =
  \begin{pmatrix}
    1&0&0\\
    0&1&0\\
    0&-3&1
  \end{pmatrix}.$$ Note that the local Stokes matrices $\mathfrak{S}_{\iota_{0,1}}$ and $\mathfrak{S}_{\iota_{2,1}}$ also commute. We read off the Stokes discontinuity formulas $$\label{disc-prb}
\begin{aligned}
  &\text{disc}_\pi \Phi^{(0)}(\tau) =
  \tau^{-3/2}s(\Phi^{(s_1)})(\tau),\\
  &\text{disc}_\pi \Phi^{(2)}(\tau) = -3s(\Phi^{(s_1)})(\tau),
\end{aligned}$$ where the second identity has already appeared in [@GGM:resurgent].

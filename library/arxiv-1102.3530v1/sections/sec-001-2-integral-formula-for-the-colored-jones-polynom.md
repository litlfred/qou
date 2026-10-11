---
doc_id: arxiv-1102.3530v1
doc_title: "The colored Jones polynomial, the Chern-Simons invariant, and the Reidemeister torsion"
section_id: sec-001-2-integral-formula-for-the-colored-jones-polynom
section_title: "Integral formula for the colored Jones polynomial"
section_number: 2
pages: 4-6
source_pdf: 1102.3530v1.pdf
source_sha256: ad3edab19f3dc404
doc_brief: "The colored Jones polynomial, the Chern-Simons invariant, and the Reidemeister torsion — W e show that from the asymptotic behavior of an evaluation of the colored Jones polynomial of the ﬁgure-eight"
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.899
---
[]{#sec:integral label="sec:integral"} In this section we use the quantum dilogarithm function to express the colored Jones polynomial of the figure-eight knot as an integral. We mainly follow [@Andersen/Hansen:JKNOT2006].

First of all we recall the following formula due to Habiro and Le (see for example [@Masbaum:ALGGT12003]). $$\label{eq:Habiro_Le}
\begin{split}
  J_N(E;q)
  &=
  \sum_{k=0}^{N-1}
  \prod_{l=1}^{k}
  \left(q^{(N-l)/2}-q^{-(N-l)/2}\right)
  \left(q^{(N+l)/2}-q^{-(N+l)/2}\right)
  \\
  &=
  \sum_{k=0}^{N-1}
  q^{-kN}
  \prod_{l=1}^{k}
  \left(1-q^{N-l}\right)
  \left(1-q^{N+l}\right).
\end{split}$$

For a complex number $\gamma$ with $\operatorname{Re}(\gamma)>0$, define the quantum dilogarithm $S_{\gamma}(z)$ as follows [@Faddeev:LETMP1995]: $$S_{\gamma}(z)
  :=
  \exp
  \left(
    \frac{1}{4}
    \int_{C_R}
    \frac{e^{zt}}{\sinh(\pi t)\sinh(\gamma t)}
    \frac{dt}{t}
  \right),$$ where $|\operatorname{Re}(z)|<\pi+\operatorname{Re}(\gamma)$ and $C_R$ is $(-\infty,-R]\cup\Omega_R\cup[R,\infty)$ with $\Omega_R:=\{R\exp(\sqrt{-1}(\pi-s))\mid0\le s\le\pi\}$ for $0<R<\min\{\pi/|\gamma|,1\}$. Note that the poles of the integrand are $0,\pm\sqrt{-1},\pm2\sqrt{-1},\dots$ and $\pm\pi\sqrt{-1}/\gamma,\pm2\pi\sqrt{-1}/\gamma,\dots$.

::: rem
Note that in [@Andersen/Hansen:JKNOT2006] it is assumed that $\gamma$ is real and $0<\gamma<1$ but we can define $S_{\gamma}(z)$ when $\operatorname{Re}(\gamma)>0$. See [@Dimofte/Gukov/Lenells/Zagier:CNTP2010 (3.21)]. (Our quantum dilogarithm $S_{\gamma}(z)$ is equal to $\Phi(z/(2\pi);\gamma/\pi)$ in [@Dimofte/Gukov/Lenells/Zagier:CNTP2010].) We give a proof of the analyticity of $S_{\gamma}$ in Lemma [\[lem:analyticity\]](#lem:analyticity){reference-type="ref" reference="lem:analyticity"}.
:::

The following formula is well known and its proof can be found in [@Andersen/Hansen:JKNOT2006 p. 530]. Note that they assume that $\gamma$ is real but their proof is also valid in our case.

::: lem
If $|\operatorname{Re}(z)|<\pi$, then we have $$\label{eq:S_gamma}
  \left(1+e^{\sqrt{-1}z}\right)S_{\gamma}(z+\gamma)
  =
  S_{\gamma}(z-\gamma).$$
:::

Putting $\gamma:=(2\pi-\sqrt{-1}u)/(2N)$ and $z:=\pi-\sqrt{-1}u-2l\gamma$ ($l=1,2,\dots,N-1$) in [\[eq:S_gamma\]](#eq:S_gamma){reference-type="eqref" reference="eq:S_gamma"}, we have $$\left(1+e^{\sqrt{-1}(\pi-\sqrt{-1}u-2l\gamma)}\right)
  S_{\gamma}(\pi-\sqrt{-1}u-2l\gamma+\gamma)
  =
  S_{\gamma}(\pi-\sqrt{-1}u-2l\gamma-\gamma).$$ So for $k=1,2,\dots,N-1$ we have $$\begin{split}
  \prod_{l=1}^{k}\bigl(1-\exp((N-l)\xi/N)\bigr)
  &=
  \prod_{l=1}^{k}
  \left(1+e^{\sqrt{-1}(\pi-\sqrt{-1}u-2\pi l/N+\sqrt{-1}ul/N)}\right)
  \\
  &=
  \prod_{l=1}^{k}
  \frac{S_{\gamma}(\pi-\sqrt{-1}u-(2l+1)\gamma)}
       {S_{\gamma}(\pi-\sqrt{-1}u-(2l-1)\gamma)}
  \\
  &=
  \frac{S_{\gamma}(\pi-\sqrt{-1}u-(2k+1)\gamma)}
       {S_{\gamma}(\pi-\sqrt{-1}u-\gamma)}.
\end{split}$$ Similarly we have $$\prod_{l=1}^{k}\bigl(1-\exp((N+l)\xi/N)\bigr)
  =
  \frac{S_{\gamma}(-\pi-\sqrt{-1}u+\gamma)}
       {S_{\gamma}(-\pi-\sqrt{-1}u+(2k+1)\gamma)}.$$ Therefore we have $$\begin{gathered}
  J_N\bigl(E;\exp(\xi/N)\bigr)
  \\
  =
  \frac{S_{\gamma}(-\pi-\sqrt{-1}u+\gamma)}{S_{\gamma}(\pi-\sqrt{-1}u-\gamma)}
  \sum_{k=0}^{N-1}
  \exp(-ku)
  \frac{S_{\gamma}(\pi-\sqrt{-1}u-(2k+1)\gamma)}
       {S_{\gamma}(-\pi-\sqrt{-1}u+(2k+1)\gamma)}.
\end{gathered}$$

Using $S_{\gamma}$ we define $$\label{eq:g_N_def}
  g_N(w)
  :=
  \exp(-Nuw)
  \frac{S_{\gamma}(\pi-\sqrt{-1}u+\sqrt{-1}\xi w)}
        {S_{\gamma}(-\pi-\sqrt{-1}u-\sqrt{-1}\xi w)}.$$ Since $S_{\gamma}(z)$ is defined for $|\operatorname{Re}(z)|<\pi+\operatorname{Re}(\gamma)$, the function $g_N(w)$ is defined for $w$ with $|\pi-\operatorname{Im}(\xi w)|<\pi+\operatorname{Re}(\gamma)=\pi+\pi/N$, that is, $w$ is in the strip $-(2\pi/u)\operatorname{Re}(w)-\pi/(Nu)<\operatorname{Im}(w)<-(2\pi/u)\operatorname{Re}(w)+2\pi/u+\pi/(Nu)$ (Figure [1](#fig:contour){reference-type="ref" reference="fig:contour"}).

![The function $g_N$ ($\Phi$, respectively) is defined between the two dotted (thick, respectively) lines. The dashed parallelogram indicates the contour $C_{+}(\varepsilon)\cup C_{-}(\varepsilon)$.](contour.eps){#fig:contour}

For $0<\varepsilon<1/(4N)$, let $C_{+}(\varepsilon)$ be the polygonal line that connects $1-\varepsilon$, $1-u/(2\pi)-\varepsilon+\sqrt{-1}$, $-u/(2\pi)+\varepsilon+\sqrt{-1}$, and $\varepsilon$, and $C_{-}(\varepsilon)$ be the polygonal line that connects $\varepsilon$, $u/(2\pi)-\sqrt{-1}$, $1+u/(2\pi)-\sqrt{-1}$, and $1-\varepsilon$. See Figure [1](#fig:contour){reference-type="ref" reference="fig:contour"}. Put $C(\varepsilon):=C_{-}(\varepsilon)\cup C_{+}(\varepsilon)$. Note that the domain of $g_N(w)$ contains $C(\varepsilon)$.

By the residue theorem we have $$\begin{gathered}
  J_N\bigl(E;\exp(\xi/N)\bigr)
  \\
  =
  \frac{S_{\gamma}(-\pi-\sqrt{-1}u+\gamma)}{S_{\gamma}(\pi-\sqrt{-1}u-\gamma)}
  \frac{\sqrt{-1}\exp(u/2)N}{2}
  \int_{C(\varepsilon)}
  \tan(N\pi w)
  g_N(w)
  dw
\end{gathered}$$ since the set of the poles of $\tan(N\pi w)$ inside $C(\varepsilon)$ is $\{(2k+1)/(2N)\mid k=0,1,2,\dots,N-1\}$ and the residue of each pole is $-1/(N\pi)$.

Putting $$G_{\pm}(N,\varepsilon)
  :=
  \int_{C_{\pm}(\varepsilon)}\tan(N\pi w)g_N(w)\,dw,$$ we have $$\label{eq:G}
  J_N\bigl(E;\exp(\xi/N)\bigr)
  =
  \frac{S_{\gamma}(-\pi-\sqrt{-1}u+\gamma)}{S_{\gamma}(\pi-\sqrt{-1}u-\gamma)}
  \frac{\sqrt{-1}\exp(u/2)N}{2}
  \bigl(G_{+}(N,\varepsilon)+G_{-}(N,\varepsilon)\bigr).$$

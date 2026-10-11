---
doc_id: arxiv-1102.3530v1
doc_title: "The colored Jones polynomial, the Chern-Simons invariant, and the Reidemeister torsion"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1102.3530v1.pdf
source_sha256: ad3edab19f3dc404
doc_brief: "The colored Jones polynomial, the Chern-Simons invariant, and the Reidemeister torsion — W e show that from the asymptotic behavior of an evaluation of the colored Jones polynomial of the ﬁgure-eight"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.987
---
Let $J_N(K;q)$ be the colored Jones polynomial of a knot $K$ in the three-sphere $S^3$ associated with the $N$-dimensional irreducible representation of $\mathfrak{sl}(2;\mathbb{C})$. We normalize it so that $J_N(\text{unknot};q)=1$. Note that $J_2(K;q)$ is the celebrated Jones polynomial [@Jones:BULAM385] after a suitable change of variable.

In 1995 Kashaev introduced a complex valued knot invariant for each natural number $N$ by using quantum dilogarithm [@Kashaev:MODPLA95] and observed that its asymptotic behavior for large $N$ determines the hyperbolic volume for several hyperbolic knots [@Kashaev:LETMP97]. He also conjectured that it is also true for any hyperbolic knot. Here a knot is called hyperbolic if its complement has a unique complete hyperbolic structure with finite volume. It is proved in 2001 by J. Murakami and the author that his invariant coincides with $J_N\bigl(K;\exp(2\pi\sqrt{-1}/N)\bigr)$ [@Murakami/Murakami:ACTAM12001]. We also generalized Kashaev's conjecture to the following volume conjecture.

::: conj
Let $K$ be a knot in $S^3$ and $\operatorname{Vol}(K)$ denote the simplicial volume of $S^3\setminus{K}$. Then the following equality would hold: $$\label{eq:VC}
  \lim_{N\to\infty}
  \frac{\log\left|J_N\bigl(K;\exp(2\pi\sqrt{-1}/N)\bigr)\right|}{N}
  =
  \frac{\operatorname{Vol}(K)}{2\pi}.$$
:::

See for example [@Murakami:Columbia] about recent developments of the conjecture and its generalizations.

As one of the generalizations Yokota and the author [@Murakami/Yokota:JREIA2007] proved that for the figure-eight knot the colored Jones polynomial knows much more. Actually we showed that if we perturb the parameter $2\pi\sqrt{-1}$ a little the corresponding limit determines the $\rm{SL}(2;\mathbb{C})$ Chern--Simons invariant associated with an irreducible representation of $\pi_1(S^3\setminus{K})$ to $\rm{SL}(2;\mathbb{C})$ in the sense of Kirk and Klassen [@Kirk/Klassen:COMMP93]. In fact we showed the following theorem.

::: thm
[]{#thm:Murakami/Yokota label="thm:Murakami/Yokota"} Let $E$ be the figure-eight knot. There exists a neighborhood $U\subset\mathbb{C}$ of $0$ such that if $u\in(U\setminus{\pi\sqrt{-1}\mathbb{Q}})\cup\{0\}$ then the following limit exists: $$\lim_{N\to\infty}
  \frac{\log J_N\bigl(K;\exp((u+2\pi\sqrt{-1}/N))\bigr)}{N}.$$ Moreover the limit determines the $\rm{SL}(2;\mathbb{C})$ Chern--Simons invariant associated with an irreducible representation of $\pi_1(S^3\setminus{E})$ to $\rm{SL}(2;\mathbb{C})$ which is determined by the parameter $u$.
:::

On the other hand, Andersen and Hansen [@Andersen/Hansen:JKNOT2006 Theorem 1] refined the volume conjecture for the figure-eight knot as follows.

::: thm
[]{#thm:Andersen/Hansen label="thm:Andersen/Hansen"} The following asymptotic equivalence holds: $$\begin{split}
  &J_N\bigl(E;\exp(2\pi\sqrt{-1}/N)\bigr)
  \\
  \underset{N\to\infty}{\sim}&
  \frac{1}{3^{1/4}}
  N^{3/2}
  \exp\left(\frac{N\operatorname{Vol}(E)}{2\pi}\right)
  \\
  =\hspace{3mm}&
  2\pi^{3/2}
  \left(\frac{2}{\sqrt{-3}}\right)^{1/2}
  \left(\frac{N}{2\pi\sqrt{-1}}\right)^{3/2}
  \exp\left(\frac{N}{2\pi\sqrt{-1}}\times\sqrt{-1}\operatorname{Vol}(E)\right).
\end{split}$$ Note that the twisted Reidemeister torsion and the Chern--Simons invariant associated with the unique complete hyperbolic structure of $S^3\setminus{E}$ are $2/\sqrt{-3}$ and $\sqrt{-1}\operatorname{Vol}(E)$ respectively.
:::

Note that we write $f(N)\underset{N\to\infty}{\sim}g(N)$ if and only if $\lim_{N\to\infty}f(N)/g(N)=1$ and that [\[eq:VC\]](#eq:VC){reference-type="eqref" reference="eq:VC"} follows from the equivalence relation above when $K$ is the figure-eight knot.

In this paper we refine Theorem [\[thm:Murakami/Yokota\]](#thm:Murakami/Yokota){reference-type="ref" reference="thm:Murakami/Yokota"} as Theorem [\[thm:Andersen/Hansen\]](#thm:Andersen/Hansen){reference-type="ref" reference="thm:Andersen/Hansen"} for the case where $u$ is real.

::: thm
[]{#thm:main label="thm:main"} Let $u$ be a real number with $0<u<\log((3+\sqrt{5})/2)=0.9624\dots$ and put $\xi:=2\pi\sqrt{-1}+u$. Then we have the following asymptotic equivalence of the colored Jones polynomial of the figure-eight knot $E$: $$\label{eq:main}
  J_N(E;\exp(\xi/N))
  \\
  \underset{N\to\infty}{\sim}
  \frac{\sqrt{-\pi}}{2\sinh(u/2)}
  T(u)^{1/2}
  \left(\frac{N}{\xi}\right)^{1/2}
  \exp\left(\frac{N}{\xi}S(u)\right),$$ where $$S(u)
  :=
  \operatorname{Li}_2(e^{u-\varphi(u)})-\operatorname{Li}_2(e^{u+\varphi(u)})-u\varphi(u)$$ and $$T(u)
  :=
  \frac{2}{\sqrt{(e^u+e^{-u}+1)(e^u+e^{-u}-3)}}.$$ Here $\varphi(u):=\operatorname{arccosh}(\cosh(u)-1/2)$ and $$\operatorname{Li}_2(z)
  :=
  -\int_{0}^{z}\frac{\log(1-x)}{x}\,dx$$ is the dilogarithm function.
:::

Note that $S(u)$ defines the $\rm{SL}(2;\mathbb{C})$ Chern--Simons invariant and $T(u)$ is the cohomological twisted Reidemeister torsion, both of which are associated with an irreducible representation of $\pi_1(S^3\setminus{E})$ into $SL(2;\mathbb{C})$ sending the meridian to an element with eigenvalues $\exp(u/2)$ and $\exp(-u/2)$. See Section [\[sec:interpretation\]](#sec:interpretation){reference-type="ref" reference="sec:interpretation"} for details.

::: rem
Since the figure-eight knot is amphicheiral, we have $J_N(E;q^{-1})=J_N(E;q)$. Thus if $u<0$ we have $$\begin{split}
  J_N\bigl(E;\exp((u+2\pi\sqrt{-1})/N)\bigr)
  &=
  J_N\bigl(E;\exp((-u-2\pi\sqrt{-1})/N)\bigr)
  \\
  &=
  \overline{J_N\bigl(E;\exp((-u+2\pi\sqrt{-1})/N)\bigr)},
\end{split}$$ where $\overline{z}$ denotes the complex conjugate of $z$. So if we prove Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} for $u>0$, we have a similar asymptotic equivalence for $u<0$. Details are left to the readers.
:::

Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} confirms the following conjecture in the case of the figure-eight knot for real $u$ with $0<u<\log((3+\sqrt{5})/2)$.

::: conj
Let $K$ be a hyperbolic knot. Then there exists a neighborhood $U\in\mathbb{C}$ of $0$ such that if $u\in U\setminus\pi\sqrt{-1}\mathbb{Q}$, we have the following asymptotic equivalence: $$J_N(K;\exp(\xi/N))
  \\
  \underset{N\to\infty}{\sim}
  \frac{\sqrt{-\pi}}{2\sinh(u/2)}
  T(K;u)^{1/2}
  \left(\frac{N}{\xi}\right)^{1/2}
  \exp\left(\frac{N}{\xi}S(K;u)\right),$$ where $\xi:=2\pi\sqrt{-1}+u$, $T(K;u)$ is the cohomological twisted Reidemeister torsion and $S(K;u)$ is the $\rm{SL}(2;\mathbb{C})$ Chern--Simons invariant, both of which are associated with an irreducible representation of $\pi_1(S^3\setminus{K})$ into $SL(2;\mathbb{C})$ sending the meridian to an element with eigenvalues $\exp(u/2)$ and $\exp(-u/2)$.
:::

For physical interpretations of this conjecture, see for example [@Gukov:COMMP2005; @Dimofte/Gukov:Columbia].

For torus knots we know the following result. Let $T(a,b)$ be the torus knot of type $(a,b)$ for positive coprime integers $a$ and $b$. It is known that the $\rm{SL}(2;\mathbb{C})$ character variety of $\pi_1(S^3\setminus{T(a,b)})$ has $(a-1)(b-1)/2$ components [@Klassen:TRAAM1991] (see also [@Munoz:REVMC2009]). Such components are indexed by a positive integer $k$ that is not a multiple of $a$ or $b$. See [@Hikami/Murakami:Bonn § 2] for details. Let $\rho_k$ be an irreducible representation in the component indexed by $k$, $S_k(u)$ be the Chern--Simons invariant associated with $\rho_k$ with $\exp(\pm u/2)$ the eigenvalues of the image of the meridian by $\rho_k$, and $T_k$ be the cohomological twisted Reidemeister torsion associated with $\rho_k$. Then we have the following formulas [@Hikami/Murakami:Bonn]: $$\begin{aligned}
  S_k(u)
  &:=
  \frac{-\bigl(2k\pi\sqrt{-1}-ab(2\pi\sqrt{-1}+u)\bigr)^2}{4ab}
  \\
  \intertext{and}
  T_k
  &:=
  \frac{16\sin^2(k\pi/a)\sin^2(k\pi/b)}{ab}.
\end{aligned}$$ Dubois and Kashaev [@Dubois/Kashaev:MATHA2007], and Hikami and the author [@Hikami/Murakami:Bonn] obtain the following asymptotic equivalences.

::: thm
For $u=0$ we have $$\begin{gathered}
  J_N\bigl(T(a,b);\exp(2\pi\sqrt{-1}/N)\bigr)
  \\
  \underset{N\to\infty}{\sim}
  \frac{\pi^{3/2}}{2ab}
  \left(\frac{N}{2\pi\sqrt{-1}}\right)^{3/2}
  \sum_{k=1}^{ab-1}
  (-1)^{k+1}k^2
  T_k^{1/2}
  \exp\left(\frac{N}{\xi}S_k(0)\right).
\end{gathered}$$ Note that since $T_k$ vanishes if $a$ or $b$ divides $k$, the summation is for all the irreducible components of the character variety.
:::

::: thm
Let $u$ be a complex number with $0<|u|<2\pi/(ab)$. Then we have $$J_N\bigl(T(a,b);\exp(\xi/N)\bigr)
  \underset{N\to\infty}{\sim}
  \frac{1}{\Delta(T(a,b);e^{u})}$$ when $\operatorname{Re}{u}>0$ and $$\begin{gathered}
  J_N\bigl(T(a,b);\exp(\xi/N)\bigr)
  \\
  \underset{N\to\infty}{\sim}
  \frac{1}{\Delta(T(a,b);e^u)}
  +
  \frac{
  \sqrt{-\pi}}{2\sinh(u/2)}
  \sum_{k=1}^{ab-1}
  (-1)^{k}
  T_k^{1/2}
  \left(\frac{N}{\xi}\right)^{1/2}
  \exp\left(\frac{N}{\xi}S_k(u)\right)
\end{gathered}$$ when $\operatorname{Re}{u}<0$, where $\xi:=u+2\pi\sqrt{-1}$ and $\Delta(T(a,b);t)$ is the Alexander polynomial.

See [@Hikami/Murakami:Bonn] for more details.
:::

The paper is organized as follows. In Section [\[sec:integral\]](#sec:integral){reference-type="ref" reference="sec:integral"} we give an integral formula for the colored Jones polynomial using the quantum dilogarithm. We study its asymptotic behavior by using the saddle point method to give a proof of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} in Section [\[sec:approximation\]](#sec:approximation){reference-type="ref" reference="sec:approximation"}. In Section [\[sec:interpretation\]](#sec:interpretation){reference-type="ref" reference="sec:interpretation"} we give topological interpretations of $S(u)$ and $T(u)$. Sections [\[sec:S_gamma\]](#sec:S_gamma){reference-type="ref" reference="sec:S_gamma"} to [\[sec:Phi_0\]](#sec:Phi_0){reference-type="ref" reference="sec:Phi_0"} are devoted to miscellaneous calculations.

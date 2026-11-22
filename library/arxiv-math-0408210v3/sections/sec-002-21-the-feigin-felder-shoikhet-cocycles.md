---
doc_id: arxiv-math-0408210v3
doc_title: "A simple algebraic proof of the algebraic index theorem"
section_id: sec-002-21-the-feigin-felder-shoikhet-cocycles
section_title: "The Feigin-Felder-Shoikhet cocycles"
section_number: 2.1
pages: 3-5
source_pdf: 0408210v3.pdf
source_sha256: 16d5ccb83a86954f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.984
doc_brief: "A simple algebraic proof of the algebraic index theorem — In math.QA/0311303 B. Feigin, G. Felder, and B."
---
First, we recall that for any associative algebra ${\cal A}$ with a unit over a field $K$ (of characteristic zero) we have a chain map $\phi^N$ from the Hochschild cochain complex $C^{\bullet}({\cal A},{\cal A}^*)$ with coefficients in the dual module ${\cal A}^*$ to the Lie algebra cochain complex $C^{\bullet}({\mathfrak{gl}}_N ({\cal A});
{\mathfrak{gl}}_N({\cal A})^{*})$ with coefficients in ${\mathfrak{gl}}_N({\cal A})^*$ $$\phi^N(\psi)(M_1\otimes a_1 ,\dots,M_k\otimes a_k)(M_0\otimes a_0)$$ $$\label{phi}
=\frac1{k!}\sum_{\nu\in S_k}(-)^{\nu}
\psi(a_{\nu(1)}\otimes \dots \otimes a_{\nu(k)})(a_0)\,tr(M_0 M_{\nu(1)}\dots
M_{\nu(k)})\,,$$ where $M_l\in {\mathfrak{gl}}_N(K)$, $a_l\in {\cal A}$, and $\psi\in C^k({\cal A}, {\cal A}^*)$ .

Let ${\cal V}$ be a $2n$-dimensional vector space (over ${\Bbb C}$) endowed with a symplectic form $B$. Let $\{y^1, \dots, y^{2n}\}$ be a basis in ${\cal V}$. We denote by $||B^{ij}||$, $(i,j=1, \dots , 2n)$ the matrix $$B^{ij} = B(y^i, y^j)$$ of the form $B$ in this basis. Let ${\varepsilon}$ be the completely antisymmetric Liouville tensor whose components ${\varepsilon}^{i_1\dots i_{2n}}$ are defined in the basis $\{ y^1, \dots, y^{2n}\}$ as follows $$\label{ve}
{\varepsilon}^{i_1 \dots i_{2n}} =
\frac{(-1)^n}{n!} \sum_{\nu\in S_{2n}}
(-)^{\nu} B^{i_{\nu(1)} i_{\nu(2)}} \dots
B^{i_{\nu(2n-1)} i_{\nu(2n)}}\,.$$

::: defi
[]{#fWa label="fWa"} The Weyl algebra ${\cal W}$ associated with the symplectic vector space ${\cal V}$ is the vector space ${\Bbb C}[[{\cal V}]](({\hbar}))$ of the formally completed symmetric algebra of ${\cal V}$ equipped with the following (associative) multiplication $$\label{circ}
(a \circ b)(y,{\hbar})=
\exp\left(\frac{{\hbar}}{2}B^{ij}\frac{{\partial}}{{\partial}y^i}\frac{{\partial}}{{\partial}z^j}
\right)a(y,{\hbar})b(z,{\hbar})|_{y=z}.$$
:::

One can easily see that the multiplication defined by ([\[circ\]](#circ){reference-type="ref" reference="circ"}) does not depend on the choice of a basis in ${\cal V}$. We view ${\cal W}$ as an algebra over the field ${\Bbb C}(({\hbar}))$ .

The Weyl algebra ${\cal W}$ is naturally filtered with respect to the degree of monomials $2[{\hbar}]+[y]$ where $[{\hbar}]$ is a degree in ${\hbar}$ and $[y]$ is a degree in $y$ $$\label{filtr}
\begin{array}{c}
\displaystyle
\dots \subset {\cal W}^1  \subset {\cal W}^0  \subset {\cal W}^{-1}
\dots \subset {\cal W}\,, \\[0.3cm]
\displaystyle
{\cal W}^m = \{ a = \sum_{2k+p\ge m}
{\hbar}^k a_{k; i_1 \dots i_p} y^{i_1} \dots y^{i_p}\}
\end{array}$$ This filtration defines the $2[{\hbar}]+[y]$-adic topology in ${\cal W}$.

In [@FFS] Feigin, Felder, and Shoikhet proposed an explicit expression for the $(2n)$th Hochschild (continuous) cocycle of the Weyl algebra ${\cal W}$ with coefficients in the dual module ${\cal W}^*$. Their formula is reminiscent of Kontsevich's construction of the structure maps of his celebrated formality quasi-isomorphism [@K]. However, unlike the integrals in Kontsevich's construction [@K] the coefficients entering the formula of Feigin, Felder, and Shoikhet are rational.

Following [@FFS] we start with the $2n$-th simplex $\Delta_{2n}=\{(u_1,\dots, u_{2n})\in{\Bbb R}^{2n}\, |\, 0\le u_1\dots \le u_{2n} \le 1\}$ with the standard orientation and denote by $B_{bc}$ the action of the form $B$ on the $b$-th and $c$-th components of ${\cal W}^{\otimes (2n+1)}$ $$B_{bc}(a_0\otimes\dots \otimes a_{2n})=$$ $$B^{ij} (a_0\otimes\dots\otimes\frac{{\partial}a_{b}}{{\partial}y^{i}}\otimes\dots
\otimes\frac{{\partial}a_c}{{\partial}y^{j}}\otimes\dots\otimes a_{2n})\,,
\qquad a_b \in {\cal W}\,.$$ Furthermore, we denote by $\pi_{2n}$ the action of the Liouville tensor ([\[ve\]](#ve){reference-type="ref" reference="ve"}) $$\pi_{2n}(a_0\otimes\dots \otimes a_{2n})=
{\varepsilon}^{i_1 \dots i_{2n}}
a_0\otimes\frac{{\partial}a_1}{{\partial}y^{i_1}}\otimes\dots
\otimes\frac{{\partial}a_{2n}}{{\partial}y^{i_{2n}}}.$$ Finally, if we denote by $\mu$ the natural projection from $({\cal W}^{\otimes (2n+1)})$ onto ${\Bbb C}(({\hbar}))$ $$\mu(a_0\otimes\dots\otimes a_{2n})=a_0(0)\dots a_{2n}(0)$$ the Feigin-Felder-Shoikhet formula of the $2n$-th Hochschild cocycle $\tau_{2n} \in C^{2n}({\cal W}, ({\cal W})^*)$ can be written as [@FFS] $$\label{tau}
\tau_{2n}({\alpha})(a_0)=
\mu_{2n}\Big( \int_{\Delta_{2n}}\prod_{0\le b\le c \le 2n}
e^{\frac{{\hbar}}{2}(2u_b-2u_c+1)B_{bc}}
\pi_{2n}(a_0\otimes {\alpha})du_1\wedge\dots\wedge du_{2n}\Big)\,,$$ where $a_0\in {\cal W}$, ${\alpha}\in {\cal W}^{\otimes (2n)}$, and $u_0=0$ . It is easy to see that the cocycle $\tau_{2n}$ does not depend on the choice of the basis $\{y^1, \dots, y^{2n}\}$ in ${\cal V}$ .

Applying  the  map  ([\[phi\]](#phi){reference-type="ref" reference="phi"})  to  ([\[tau\]](#tau){reference-type="ref" reference="tau"})  we  get  the  $2n$-th  cocycle  in  the  chain  complex  $C^{{\bullet}}({\mathfrak{gl}}_N({\cal W}), {\mathfrak{gl}}_N({\cal W})^*)$ of the Lie algebra ${\mathfrak{gl}}_N({\cal W})$ with values in the dual module $({\mathfrak{gl}}_N({\cal W}))^*$ $$\label{Te}
\Theta^N_{2n}=
\phi^N(\tau_{2n})\,:\, \wedge^{2n} ({\mathfrak{gl}}_N({\cal W})) \otimes
{\mathfrak{gl}}_N({\cal W}) \mapsto {\Bbb C}(({\hbar}))\,.$$ In [@FFS] it was shown that the latter cocycle satisfies remarkable properties which allow us to construct a trace density map for a quantum algebra of functions on any symplectic manifold. Before talking about these properties we recall a necessary construction of the Chern-Weil theory.

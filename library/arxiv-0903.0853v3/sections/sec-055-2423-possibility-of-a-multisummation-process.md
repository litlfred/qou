---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis"
section_id: sec-055-2423-possibility-of-a-multisummation-process
section_title: "Possibility of a multisummation process"
section_number: 24.2.3
pages: 129-132
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 0.976
---
No explicit algorithm is presently known to yield the solution of [\[equation:carre\]](#equation:carre){reference-type="eqref" reference="equation:carre"} in the spirit of theorem [\[theo:sommabilite\]](#theo:sommabilite){reference-type="ref" reference="theo:sommabilite"} with $\Lambda=[\lambda]+[\mu]$. A multisummation algorithm does exist in a very different setting, due to the third author. The following result shows its similarity to classical Borel-Laplace summation.

::: theo
[]{#thm:12sommable label="thm:12sommable"} In [\[equation:carre\]](#equation:carre){reference-type="eqref" reference="equation:carre"}, we have $L = (z \sigma_q- 1)(z^2 \sigma_q- 1)$ and the series $\hat Y$ is $(1,1/2)$-summable by the following process: $$\begin{aligned}
\hat f = \sum_{n\ge 0} a_n z^n \quad
&
\overset{{\mathcal{B}_{q,1}}}{\longrightarrow}
&
\varphi := \sum_{n\ge 0} a_n q^{-n(n-1)/2} \xi^n \\
&
\overset{{\mathcal A}^{*}_{q;1,1/2}}{\longrightarrow}
&
f^*_{1}
\overset{{\mathcal L}^{*}_{q;1/2}}{\longrightarrow}
f^*_{(1,1/2)}.
\end{aligned}$$
:::

For a basic introduction to this method and explanation of the notations above, see [@DRSZ], which contains further references to this work.

# From the Mock Theta functions to the $q$-Euler equation {#section:MockTheta}

Our source here is the famous 1935 paper "The final problem: an account of the Mock Theta Functions" by G. N. Watson, as reproduced, for instance, in [@Rama]. On page 330 of *loc. cit.*, seven "mock theta functions of order three" are considered. The first four are called $f,\phi,\psi,\chi$ (after Ramanujan who discovered them); the three last are called $\omega,\nu,\rho$ (after Watson who added[^1] them to the list). In the notation of Ramanujan and Watson, the unique variable of these analytic functions is written $q$ (this tradition goes back to Jacobi) and it is assumed there that $0 < \left |q \right |< 1$.\
In [@CZMTF], a new variable $x$ is added (this tradition goes back to Euler) and one puts: $$\label{not106}
s(\alpha,\beta;q,x) := \sum_{n \geq 0} a_{n} x^{n},$$ where: $$\begin{aligned}
a_{n} & := \dfrac{q^{n^{2}}}
{\left(\frac{q}{\alpha},\frac{q}{\beta};q\right)_{n}}
\left(\frac{1}{\alpha \beta}\right)^{n} \\
& =
\dfrac{(\alpha,\beta;q)_{\infty}}{(\alpha q^{-n},\beta q^{-n};q)_{\infty}} q^{-n} \\
& =
\dfrac{q^{n^{2}}}
{(\alpha - q) \cdots (\alpha - q^{n})(\beta - q) \cdots (\beta - q^{n})} \cdot
\end{aligned}$$ Note for further use that the second formula makes sense for all $n \in {\mathbf Z}$ and allows one to define another series: $$F(\alpha,\beta;q,x) := \sum_{n \in {\mathbf Z}} a_{n} x^{n},$$ []{#not107 label="not107"} so that $F(\alpha,\beta;q,x) = s(\alpha,\beta;q,x) + G(\alpha,\beta;q,x)$, where: $$G(\alpha,\beta;q,x) = \sum_{n < 0} a_{n} x^{n} = 
\sum_{n \geq 0} (\alpha,\beta;q)_{n} (q/x)^{n}.$$ The formula giving $s(\alpha,\beta;q,x)$ subsumes all seven mock theta functions, which can be respectively recovered by setting $(\alpha,\beta,x)$ to be one of the following: $(-1,-1,1)$, $({\text{i}},-{\text{i}},1)$, $(\sqrt{q},-\sqrt{q},1)$, $(j,j^{2},-q)$, $(1/q,1/q,1)$, $({\text{i}}/\sqrt{q},-{\text{i}}/\sqrt{q},1)$ and $(-j/q,-j^{2}/q,1)$. (Note that in all cases, among other multiplicative relations, $\alpha$ and $\beta$ map to torsion points of ${\mathbf{E}_{q}}$.)\
In the following, which is intended to motivate the study of the Stokes phenomenon, we follow recent work by the third author [@CZMTF], skipping most of the proofs. In [1.1](#subsection:functequafors){reference-type="ref" reference="subsection:functequafors"} and [\[subsection:backtoMockTheta\]](#subsection:backtoMockTheta){reference-type="ref" reference="subsection:backtoMockTheta"}, we use the conventions of *loc. cit.*. In particular, it is assumed (exceptionally) that $\left |q \right |< 1$ and we use the theta function: $$\theta(x;q) := \sum_{n \in {\mathbf Z}} q^{n(n-1)/2} x^{n} = (q,-x,-q/x;q)_{\infty}.$$ (See [\[eqn:tripleproduit\]](#eqn:tripleproduit){reference-type="eqref" reference="eqn:tripleproduit"} in the general notations of section [\[section:generalnotations\]](#section:generalnotations){reference-type="ref" reference="section:generalnotations"} and equation [\[eqn:deuxtriplesproduits\]](#eqn:deuxtriplesproduits){reference-type="eqref" reference="eqn:deuxtriplesproduits"} page .) In [\[subsection:backtoqEuler\]](#subsection:backtoqEuler){reference-type="ref" reference="subsection:backtoqEuler"}, we shall return to the general convention $\left |q \right |> 1$ of the present paper, and use the function ${\theta_{q}}$

## Functional equation for $s(\alpha,\beta;q,z)$ {#subsection:functequafors}

From the recurrence relation $(\alpha - q^{n+1}) (\beta - q^{n+1}) a_{n+1} = q^{2n+1} a_{n}$, one deduces that $s$, as a function of $x$, is solution of the second order non homogeneous $q$-difference equation: $$\label{eqn:NHCBHG}
\bigl((\sigma_q- \alpha)(\sigma_q- \beta) - q x \sigma_q^{2}\bigr) s = 
(1 - \alpha) (1 - \beta).$$ The recurrence relation actually remains valid for all $n \in {\mathbf Z}$, which implies that $F$ is solution of the corresponding homogeneous equation: $$\label{eqn:HCBHG}
\bigl((\sigma_q- \alpha)(\sigma_q- \beta) - q x \sigma_q^{2}\bigr) F = 0.$$ This, in turn, entails that $-G = s - F$ is a solution defined at infinity of [\[eqn:NHCBHG\]](#eqn:NHCBHG){reference-type="eqref" reference="eqn:NHCBHG"}.\
We shall assume now that $\alpha,\beta \neq 0$ and that $\beta/\alpha \not\in q^{{\mathbf Z}}$. One checks easily that the equation [\[eqn:HCBHG\]](#eqn:HCBHG){reference-type="eqref" reference="eqn:HCBHG"} is fuchsian at $0$ with exponents $\alpha,\beta$ (see for instance [@JSAIF]). Likewise, taking in account the general conventions of this paper (*i.e.* using the dilatation factor $q^{-1}$ in order to have a modulus $> 1$), we see that [\[eqn:HCBHG\]](#eqn:HCBHG){reference-type="eqref" reference="eqn:HCBHG"} is pure isoclinic at infinity, with slope $-1/2$; this will explain the appearance of $\theta(-,q^{2})$ in the following formulas. We define: $$M(\alpha,\beta;q,x) := 
\left(\frac{q}{\alpha},\frac{q}{\beta};q\right)_{\infty} F(\alpha,\beta;q,x).$$ This is another solution of [\[eqn:HCBHG\]](#eqn:HCBHG){reference-type="eqref" reference="eqn:HCBHG"}, with more symetries. It admits the following expansions: []{#not108 label="not108"} $$\begin{aligned}
M(\alpha,\beta;q,x) &= 
\theta(q \alpha \beta x;q^{2}) U_{\alpha/\beta}(x) - 
\dfrac{q}{\alpha} ~ \theta(\alpha \beta x;q^{2}) V_{\alpha/\beta}(x) \\
& =
\theta(q x/\alpha \beta;q^{2}) U_{\alpha/\beta}(1/x) - 
\dfrac{q}{\alpha} ~ \theta(q^{2} x/\alpha \beta;q^{2}) V_{\alpha/\beta}(1/x),
\end{aligned}$$ with the following definitions: []{#not109 label="not109"} $$\begin{aligned}
U_{\lambda}(x) & := 
\sum_{m \geq 0} q^{m^{2}} S_{2 m}(-q^{-2 m} \lambda;q) (q x/\lambda)^{m}, \\
V_{\lambda}(x) & := 
\sum_{m \geq 0} q^{m(m+1)} S_{2 m+1}(-q^{-2 m-1} \lambda;q) (q x/\lambda)^{m}, \\
S_{n}(x;q) & := 
\sum_{k=0}^{n} \dfrac{q^{k^{2}}}{(q;q)_{k} (q;q)_{n-k}} (-x)^{k}.
\end{aligned}$$ (The $S_{n}$ are the *Stieltjes-Wiegert polynomials*.)\

::: rema
The parameter $\lambda := \alpha/\beta$ is linked to monodromy. Indeed, the local Galois group of [\[eqn:HCBHG\]](#eqn:HCBHG){reference-type="eqref" reference="eqn:HCBHG"} at $0$ is the set of matrices $\begin{pmatrix} \gamma(\alpha) & 0 \\ 0 & \gamma(\beta) \end{pmatrix}$, where $\gamma$ runs through the group endomorphisms of ${\mathbf C}^{*}$ that send $q$ to $1$; and the local monodromy group is the rank $2$ free abelian subgroup with generators corresponding to two particular choices of $\gamma$ described in [@JSGAL].
:::

[^1]: At least, so says Watson in *loc. cit.*. However, this is questioned by G.E. Andrews and B.C. Berndt in their introduction to Ramanujan's Lost Notebook. The point is also discussed in detail in pp. 171-172 of the article by Andrews in [@Rama].

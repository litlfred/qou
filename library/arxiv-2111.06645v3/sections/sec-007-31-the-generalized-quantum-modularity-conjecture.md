---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-007-31-the-generalized-quantum-modularity-conjecture
section_title: "The generalized quantum modularity conjecture"
section_number: 3.1
pages: 15-16
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 1.0
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
[]{#sub.GQMC label="sub.GQMC"}

The function $J^{(K)}$ from $\mathbb Q/\mathbb Z$ to $\overline{\mathbb Q}$, which was originally defined as the Galois-equivariant extension of the Kashaev invariant $\langle K\rangle_N$, has now re-appeared as the constant term of one of a collection of formal power series indexed by the elements $\sigma$ of a finite set $\mathcal P_K$ associated to the knot. This suggests that we should look also at the constant terms of the other series as well, i.e., that we should study the functions (*generalized Kashaev invariants*) $$\begin{gathered}
\label{cherries}
J^{(K,\sigma)}\colon\ \mathbb Q/\mathbb Z\to \overline{\mathbb Q},\qquad J^{(K,\sigma)}(\alpha) := \Phi_\alpha^{(K,\sigma)}(0)
\end{gathered}$$ for all $\sigma\in\mathcal P_K$. These functions turn out to have beautiful arithmetic properties generalizing in a non-obvious way the Habiro-ring property of the original functions $J^{(K)}= J^{(K,\sigma_0)}$. These will be the subject of the subsequent paper [@GSZ:habiro] and, apart from a few numerical examples, will not be discussed further here. Instead, we will concentrate on the asymptotic properties of the new functions [\[cherries\]](#cherries){reference-type="eqref" reference="cherries"}. In particular, we can ask whether these functions satisfy an analogue of the quantum modularity conjecture for $J^{(K)}$. The answer turns out to be positive, but to involve a number of successive refinements arising from the numerical data. We will present the simplest version here and the strongest versions, which require more preparation, in Sections [\[sec.RQMC\]](#sec.RQMC){reference-type="ref" reference="sec.RQMC"} and [\[sec.Matrix\]](#sec.Matrix){reference-type="ref" reference="sec.Matrix"}.

We start once again with the simplest knot $K=4_1$. Here the function $J^{(K,\sigma_0)}(\alpha)=J^{(K)}(\alpha)$ is the one given by [\[J0for41\]](#J0for41){reference-type="eqref" reference="J0for41"} (with $\zeta_N$ replaced by $\mathbf{e}(\alpha)$) whereas the new functions $J^{(K,\sigma_1)}(\alpha)$ and $J^{(K,\sigma_2)}(\alpha)$ are given explicitly by $$\label{Def41J1}
J^{(K,\sigma_1)}(\alpha) = \frac1{\sqrt{c}\sqrt[4]{3}}
\sum_{Z^c = \zeta_6} \prod_{j=1}^c \bigl|1 - q^jZ\bigr|^{2j/c},
\qquad c=\mathrm{den}(\alpha),\quad q=\mathbf{e}(\alpha)$$ and $J^{(K,\sigma_2)}(\alpha) ={\rm i} J^{(K,\sigma_1)}(-\alpha)=\overline{J^{(K,\sigma_1)}(\alpha)}$. The original QMC says that $J^{(4_1)}\bigl(\frac{aX+b}{cX+d}\bigr)$ is asymptotically equal to for any matrix as $X$ tends to infinity with bounded denominator, where the "completion" $\widehat\Phi$ is defined by [\[DefPhih\]](#DefPhih){reference-type="eqref" reference="DefPhih"}. When we look at the corresponding asymptotics for the two new functions and for the two simple matrices and of $\mathrm{SL}_2(\mathbb Z)$, we see a similar behavior, but with two major differences: the "automorphy factor" $(cX+d)^{3/2}$ is no longer there, and there is a new exponential factor involving the complex volume. Explicitly, what we find experimentally is $$\label{nontweak1}
J^{(4_1,\sigma_1)}(-1/X)  \sim  {\rm e}^{v(K)/(\text{num}(X)\cdot\mathrm{den}(X))}
J^{(4_1,\sigma_1)}(X)  \widehat\Phi^{(4_1)}_0\left(\frac{2\pi {\rm i}}X\right)$$ (here "num" and "den" denote the numerator and denominator) and $$\label{nontweak2}
J^{(4_1,\sigma_1)}(X/(2X+1))  \sim {\rm e}^{v(K)/((X+\frac12)\cdot\mathrm{den}(X)^2)}
J^{(4_1,\sigma_1)}(X) \widehat\Phi^{(4_1)}_{1/2}\left(\frac{2\pi {\rm i}}{2(2X+1)}\right)$$ and similarly for $\Phi^{(\sigma_2)}$ but with $v(K)$ replaced by $v(K,\sigma_2)=-v(K)$. The two equations [\[nontweak1\]](#nontweak1){reference-type="eqref" reference="nontweak1"} and [\[nontweak2\]](#nontweak2){reference-type="eqref" reference="nontweak2"} can be written uniformly in the form $$J^{(4_1,\sigma_1)}(\gamma X)  \sim {\rm e}^{v(K) \lambda_\gamma(X)}
J^{(4_1,\sigma_1)}(X) \widehat\Phi^{(4_1)}_{a/c}\left(\frac{2\pi {\rm i}}{c(cX+d)}\right)$$ for $\gamma=\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr) \in \mathrm{SL}_2(\mathbb Z)$, where $\lambda_\gamma(x)$ is defined for $x = r/s \in \mathbb Q$ with $r$ and $s$ coprime by $$\label{tweakdef}
\lambda_\gamma(x) := \frac{1}{\mathrm{den}(x)^2\big(x-\gamma^{-1}(\infty)\big)} = \frac{c}{s(cr+ds)}
= \pm \frac c{\mathrm{den}(x)\mathrm{den}(\gamma x)} .$$

The experiments show that the same thing happens for other knots $K$ and all representations $\sigma$, i.e., we can formulate the *generalized quantum modularity conjecture* (GQMC) $$\label{GQMC}
(cX+d)^{-\kappa(\sigma)} {\rm e}^{-v(\sigma)  \lambda_\gamma(X)}

J^{(K,\sigma)}(\gamma X)  \sim  J^{(K,\sigma)}(X)
\widehat\Phi^{(K)}_{a/c}\left(\frac{2\pi {\rm i}}{c(cX+d)}\right) ,$$ as $X \to \infty$ with bounded denominator (as usual), and where $\gamma=\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr) \in \mathrm{SL}_2(\mathbb Z)$ with $c>0$, and where the *weight* $\kappa(\sigma)$ of the representation $\sigma\in\mathcal P_K$ is defined by $$\label{Defwsigma}
\kappa(\sigma) = \begin{cases} 3/2 & \text{if $\sigma=\sigma_0$,} \\
  0 & \text{otherwise.} \end{cases}$$ Notice that [\[GQMC\]](#GQMC){reference-type="eqref" reference="GQMC"} coincides with the original QMC when $\sigma=\sigma_0$ because in this case the factor ${\rm e}^{-v(\sigma)\lambda_\gamma(X)}$ on the left-hand side of [\[GQMC\]](#GQMC){reference-type="eqref" reference="GQMC"} is identically $1$. We also see that the two different definitions [\[DefPhih\]](#DefPhih){reference-type="eqref" reference="DefPhih"} and [\[DefPhi0h\]](#DefPhi0h){reference-type="eqref" reference="DefPhi0h"} of $\widehat\Phi^{(K,\sigma)}$ for $\sigma\ne\sigma_0$ and $\sigma=\sigma_0$ can now be written in a uniform way as $$\label{UnifPhih}
\widehat\Phi_\alpha^{(K,\sigma)}(h) =
 |c\hbar|^{\kappa(\sigma)} {\rm e}^{v(\sigma)/c^2\hbar} \Phi_\alpha^{(K,\sigma)}(h),
 \qquad c=\mathrm{den}(\alpha),\quad \hbar:=h/2\pi {\rm i},$$ which will also be convenient at many other points. Notice that the convention $\hbar=h/2\pi {\rm i}$ is almost, but not quite, the same as the one used in ordinary quantum mechanics, and also that the factor $2\pi {\rm i}$ relating $h$ and $\hbar$ is the same as that used in our two different normalizations $\mathbf V(\sigma)$ and $v(\sigma)=\mathbf V(\sigma)/2\pi {\rm i}$ of the volume, so that ${\rm e}^{v(\sigma)/c^2\hbar}={\rm e}^{\mathbf V(\sigma)/c^2h}$.

We end this subsection by proving a cocycle property of the arithmetic function $\lambda_\gamma(X)$ that will be needed in Section [\[sec.Matrix\]](#sec.Matrix){reference-type="ref" reference="sec.Matrix"}.

::: Lemma
[]{#lem.lambda label="lem.lambda"} For all $\gamma, \gamma'\in \mathrm{PSL}_2(\mathbb Z)$ and $x\in\mathbb Q\smallsetminus\big\{{\gamma'}^{-1}(\infty),{(\gamma\gamma')}^{-1}(\infty)\big\}$, we have $$\lambda_{\gamma\gamma'}(x) = \lambda_\gamma(\gamma' x) + \lambda_{\gamma'}(x) .$$
:::

::: proof
*Proof.* Let $\gamma=\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr)$, $\gamma'=\bigl(\smallmatrix a'&b'\\c'&d'\endsmallmatrix\bigr)$ and $\gamma \gamma'=\bigl(\smallmatrix a''&b''\\c''&d''\endsmallmatrix\bigr)$. Then $c''d'-c'd''=c$, and hence $$\lambda_{\gamma\gamma'}(x) - \lambda_{\gamma'}(x) = \frac{c''}{s(c''r+d''s)}+\frac{c'}{s(c'r+d's)}
 = \frac c{s(c'r+d's)(c''r+d''s)} = \lambda_\gamma(\gamma' x)$$ as required. A more enlightening way to say this is that $\lambda_\gamma(\gamma'(\infty))=C(\gamma\gamma',\gamma')$, where $$C(\gamma_1,\gamma_2):=\frac{c\big(\gamma_1\gamma_2^{-1}\big)}{c(\gamma_1)c(\gamma_2)}=\gamma_2^{-1}(\infty)-\gamma_1^{-1}(\infty),$$ which is a coboundary and hence a cocycle. ◻
:::

---
doc_id: arxiv-2404.03933v2
doc_title: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY"
section_id: sec-005-7-integral-formula-for-multiplicities
section_title: "Integral formula for multiplicities"
section_number: 7
pages: 18-21
source_pdf: 2404.03933v2.pdf
source_sha256: 48aff6e97e1f1267
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.91
doc_brief: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY — We study the decomposition of tensor powers of two dimensional irreducible rep- resentations of quantum sl2 at even roots of"
---
[]{#rec-int label="rec-int"}

## Characters of tilting and Weyl modules.

We define the character of an $U_q(\mathfrak{sl}_2)$-module $V$ as the Laurent polynomial (see section [\[modules\]](#modules){reference-type="ref" reference="modules"}) as $$\mathrm{ch}_V (x)=\sum_j \dim V_j x^j$$ Here the sum is taken over weight subspaces of $V$ and $i$ ranges over all possible weights that occur in $V$. We will treat $x$ either as a formal variable, or, as a variable $x=e^{i\theta}$ on a unit circle in the complex plane. Because our characters are Laurent polynomials both make sense.

Theorem [\[Weyl\]](#Weyl){reference-type="ref" reference="Weyl"} and Theorem [\[isomLW\]](#isomLW){reference-type="ref" reference="isomLW"} give the following identifications and relations: $$\begin{eqnarray*}
\mathrm{ch}_{L(k_0)}(x)=\mathrm{ch}_{W(k_0)}(x)=\mathrm{ch}_{T(k_0)}(x),& 0\leq k_0\leq l-1,\\
\mathrm{ch}_{W(k_1l+k_0)}(x)=\mathrm{ch}_{L(k_1l+k_0)}(x)+\mathrm{ch}_{L(k_1l-2-k_0)}(x),& 0\leq k_0\leq l-2,\,k_1\in\mathbb{Z}_{>0},\\
\mathrm{ch}_{T(k_1l+k_0)}(x)=\mathrm{ch}_{W(k_1l+k_0)}(x)+\mathrm{ch}_{W(k_1l-2-k_0)}(x),& 0\leq k_0\leq l-2,\,k_1\in\mathbb{Z}_{>0},\\
\mathrm{ch}_{L(k_1l+l-1)}(x)=\mathrm{ch}_{W(k_1l+l-1)}(x)=\mathrm{ch}_{T(k_1l+l-1)}(x),& k_1\in\mathbb{Z}_{>0}.
\end{eqnarray*}$$

::: lemma
[]{#fchar label="fchar"}Characters of tilting modules are: $$\begin{equation*}
\mathrm{ch}_{T(k_1l+k_0)}(x)=
\begin{cases}
\frac{x^{k_0+1}-x^{-(k_0+1)}}{x-x^{-1}},& \textit{if $0\leq k_0\leq l-1$ and $k_1=0$},\\
\frac{x^{(k_1+1)l}-x^{-(k_1+1)l}}{x-x^{-1}},& \textit{if $k_0=l-1$ and $k_1\in\mathbb{Z}_{>0}$},\\
(x^{k_0+1}+x^{-(k_0+1)})\frac{x^{k_1l}-x^{-k_1l}}{x-x^{-1}},& \textit{if $0\leq k_0\leq l-2$ and $k_1\in\mathbb{Z}_{>0}$}.
\end{cases}
\end{equation*}$$
:::

::: proof
*Proof.* Weight $k$ can be uniquely written as $k=k_1l+k_0$, where $0\leq k_0\leq l-1$ and $k_1\in\mathbb{Z}_{\geq 0}$. Characters for Weyl modules $W(k)$ are $$\begin{equation*}
    \mathrm{ch}_{W(k)}(x)=\frac{x^{k+1}-x^{-(k+1)}}{x-x^{-1}}.
\end{equation*}$$ From Theorem [\[tensor_pr\]](#tensor_pr){reference-type="ref" reference="tensor_pr"} we know, that $$\begin{equation}
\label{ch1}
    \mathrm{ch}_{L(k_1l+k_0)}(x)=\mathrm{ch}_{L(k_1l)}(x)\mathrm{ch}_{L(k_0)}(x),
\end{equation}$$ and for $0\leq k\leq l-2$ or $k=ml-1$, $m\in\mathbb{Z}_{>0}$ $$\begin{equation}
\label{ch2}
    \mathrm{ch}_{L(k)}(x)=\mathrm{ch}_{W(k)}(x)=\mathrm{ch}_{T(k)}(x).
\end{equation}$$ formulae ([\[ch1\]](#ch1){reference-type="ref" reference="ch1"}) and ([\[ch2\]](#ch2){reference-type="ref" reference="ch2"}) give $$\begin{equation*}
    \mathrm{ch}_{W((m+1)l-1)}(x)=\mathrm{ch}_{L(ml)}(x)\mathrm{ch}_{L(l-1)}(x)=\mathrm{ch}_{L(ml)}(x)\mathrm{ch}_{W(l-1)}(x),
\end{equation*}$$ which gives $$\begin{equation*}
    \mathrm{ch}_{L(ml)}(x)=\frac{\mathrm{ch}_{W((m+1)l-1)}(x)}{\mathrm{ch}_{W(l-1)}(x)}=\frac{x^{(m+1)l}-x^{-(m+1)l}}{x^l-x^{-l}}
\end{equation*}$$ and, concluding, we have $$\begin{equation*}
    \mathrm{ch}_{L(k_1l+k_0)}(x)=\frac{x^{k_0+1}-x^{-(k_0+1)}}{x-x^{-1}}\frac{x^{(k_1+1)l}-x^{-(k_1+1)l}}{x^l-x^{-l}}.
\end{equation*}$$ Note that this definition satisfies condition, given by short exact sequences in Theorem [\[Weyl\]](#Weyl){reference-type="ref" reference="Weyl"}, meaning that for $k_0\neq l-1$ we indeed have $$\begin{equation*}
    \mathrm{ch}_{W(k_1l+k_0)}(x)=\mathrm{ch}_{L(k_1l+k_0)}(x)+\mathrm{ch}_{L(k_1l-k_0-2)}(x).
\end{equation*}$$ Using exact sequences from Theorem [\[isomLW\]](#isomLW){reference-type="ref" reference="isomLW"}, we can derive characters for the rest of the tilting modules. Suppose $k_0\neq l-1, \ \ k_1\in\mathbb{Z}_{>0}$, then $$\begin{eqnarray*}
    \mathrm{ch}_{T(k_1l+k_0)}(x)=\mathrm{ch}_{W(k_1l+k_0)}(x)+\mathrm{ch}_{W(k_1l-k_0-2)}(x)=\\
    =(x^{k_0+1}+x^{-(k_0+1)})\frac{x^{k_1l}-x^{-k_1l}}{x-x^{-1}}\nonumber,
\end{eqnarray*}$$ which concludes the proof. ◻
:::

## Scalar product and orthogonality.

Consider the scalar product on functions on the unit circle which is the radial part of the Haar measure on $SU(2)$. For two functions $f, g: S^1=\{z=e^{i\theta}\}\to \mathbb{C}$ define $$\begin{equation}
\label{sp}
(f,g)=\frac{1}{4\pi}\int_0^{2\pi}\overline{f(e^{i\theta})}g(e^{i\theta})|e^{i\theta}-e^{-i\theta}|^2d\theta
\end{equation}$$ In particular it defines the scalar product on the space of Laurent polynomials in $x$ which are symmetric with respect to the Weyl reflection $x\mapsto x^{-1}$.

We will use the following notations for characters of irreducible representations $L(k)$, Weyl modules $W(k)$ and tilting modules $T(k)$. $$\begin{equation*}
\mathrm{ch}_{L(k_1l+k_0)}(x)=\chi^L_{k_1,k_0},\quad\mathrm{ch}_{W(k_1l+k_0)}(x)=\chi^W_{k_1,k_0},\quad\mathrm{ch}_{T(k_1l+k_0)}(x)=\chi^T_{k_1,k_0}.
\end{equation*}$$

Characters of Weyl modules form an orthonormal basis in the space $L^2(S^{1})$ with respect to the scalar product ([\[sp\]](#sp){reference-type="ref" reference="sp"}): $$\begin{eqnarray*}
(\chi^W_{k_1,k_0},\chi^W_{m_1,m_0})=\delta_{k_1,m_1}\delta_{m_0,k_0},
\end{eqnarray*}$$ Scalar products between characters of tilting modules and Weyl modules are: $$\begin{equation*}
(\chi^L_{k_1,k_0},\chi^T_{m_1,m_0})=
\begin{cases}
\delta_{l-2-k_0,m_0}(\delta_{k_1+1,m_1}-\delta_{0,m_1}),& \textit{if $k_0\neq l-1$, $k_1\in\mathbb{Z}_{>0}$},\\
\delta_{k_1,m_1}\delta_{k_0,m_0},& \textit{otherwise}.
\end{cases}
\end{equation*}$$

In order to find an integral formula for multiplicities, similar to the one that exists for compact Lie groups and is based on the orthogonality of characters of irreducible modules, let us find the basis orthogonal to the basis of characters of tiltling modules.

::: theorem
Functions $$\begin{equation*}
\eta_{k_1,k_0}=\frac{(x^{k_1l-1}+x^{-(k_1l-1)})(x^{k_0-l+1}-x^{-(k_0-l+1)})}{(x-x^{-1})(x^l-x^{-l})}.
\end{equation*}$$ form a basis orthogonal to the basis of characters of tilting modules: $$\begin{eqnarray*}
    (\chi^T_{m_1,m_0},\eta_{k_1,k_0})=\delta_{m_1,k_1}\delta_{m_0,k_0}
\end{eqnarray*}$$
:::

::: proof
*Proof.* It is easy to find the decomposition of $\eta_{k_1,k_0}$ in the basis of Weyl modules: $$\begin{equation*}
\eta_{k_1,k_0}=\sum_{j=0}^\infty (\chi^W_{k_1+2j,k_0}-\chi^W_{k_1+1+2j,l-2-k_0}).
\end{equation*}$$ Now let us use formulae expressing characters of tilting modules in terms of character of Weyl modules, the formula above and the orthogonality of characters of Weyl modules. For $k_0\neq l-1$ and $k_1\in\mathbb{Z}_{>0}$ we have $$\begin{eqnarray*}
(\chi^T_{m_1,m_0},\eta_{k_1,k_0})=\sum\limits_{j=0}^\infty((\chi^W_{m_1,m_0},\chi^W_{k_1+2j,k_0})+(\chi^W_{m_1-1,l-2-m_0},\chi^W_{k_1+2j,k_0})\\
-(\chi^W_{m_1,m_0},\chi^W_{k_1+1+2j,l-2-k_0})-(\chi^W_{m_1-1,l-2-m_0},\chi^W_{k_1+1+2j,l-2-k_0}))=\\
=\sum\limits_{j=k_1}^\infty(\delta_{m_1,k_1+2j}\delta_{m_0,k_0}+\delta_{m_1-1,k_1+2j}\delta_{l-2-m_0,k_0}-\\
-\delta_{m_1,k_1+1+2j}\delta_{m_0,l-2-k_0}-\delta_{m_1-1,k_1+1+2j}\delta_{l-2-m_0,l-2-k_0}).
\end{eqnarray*}$$ It is evident that this expression gives the right combination of Kroneker delta symbols: $$\begin{eqnarray*}
    (\chi^T_{m_1,m_0},\eta_{m_1,k_0})=\delta_{m_0,k_0},
\end{eqnarray*}$$ and for $k_1<m_1$, again, $0$. To resume, we have $$\begin{equation*}
    (\chi^T_{m_1,m_0},\eta_{k_1,k_0})=\delta_{m_0,k_0}\delta_{m_1,k_1},
\end{equation*}$$ ◻
:::

## Multiplicities {#integralchar}

Now we can use the basis $\eta_{k_1,k_0}$ to derive the integral formula for multiplicities of tilting modules.

The tensor product decomposition, implies the equality of characters: $$\begin{equation*}
(\mathrm{ch}_{T(1)}(x))^N=\sum_{0\leq k_0\leq l-1,\, k_1\in\mathbb{Z}_{\geq 0}}M^{(l)}_{k_1l+k_0}(N)\mathrm{ch}_{T(k_1l+k_0)}(x).
\end{equation*}$$ Now that we have found the orthogonal basis, we can use it to derive the following integral formula for the multiplicity $$\begin{equation*}
M^{(l)}_{k}(N)=\frac{1}{4\pi}\int_{0}^{2\pi}\overline{\eta_{k_1,k_0}(e^{i\theta})}(\mathrm{ch}_{T(1)}(e^{i\theta}))^N|e^{i\theta}-e^{-i\theta}|^2d\theta.
\end{equation*}$$

To compare this formula with Theorem [\[comb_coef\]](#comb_coef){reference-type="ref" reference="comb_coef"}, we use the definition of $\eta_{k_1,k_0}$, and decomposition into a sign-alternating sum of characters of Weyl modules. Using the orthogonality of Weyl characters we arrive to the expression $$\begin{equation*}
M^{(l)}_{k}(N)=\sum_{j=0}^\infty (F_{k_1l+2jl+k_0}^{(N)}-F_{k_1l+2(j+1)l-2-k_0}^{(N)}),
\end{equation*}$$ where $F^{(N)}_m$ are the same as in ([\[tkN\]](#tkN){reference-type="ref" reference="tkN"}). Clearly, this agrees with Theorem [\[comb_coef\]](#comb_coef){reference-type="ref" reference="comb_coef"}. Moreover the analytic derivation above is more or less a rephrasing of the algebraic proof of this theorem.

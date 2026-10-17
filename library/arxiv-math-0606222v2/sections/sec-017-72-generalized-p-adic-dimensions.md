---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-017-72-generalized-p-adic-dimensions
section_title: "Generalized p-adic dimensions"
section_number: 7.2
pages: 32-35
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
toc_source: outline
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.929
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
[]{#Genpdim label="Genpdim"}

In this subsection we consider the $p$-adic degeneration of the generalized quantum dimension $D_q(\lambda)$ and we relate it to the complex dimension of the $\mathcal{M}_{\mathbb{F}}$-spherical irreducible $\mathcal{K}_{\mathbb{F}}$-representation $V_\lambda^{\mathbb{F}}$ for non-Archimedean local fields $\mathbb{F}$ (see Section [\[local\]](#local){reference-type="ref" reference="local"}). Denote $\delta_{k,l}$ ($k,l\in\mathbb{Z}$) for the Kronecker delta function: it is one if $k=l$ and zero otherwise.

::: lem
[]{#specialq=0 label="specialq=0"} The functions $v_i(m;q)$, $w_{j,k}^{\pm}(m;q)$ [(]{.upright}see Lemma [\[explicitD\]](#explicitD){reference-type="ref" reference="explicitD"}[)]{.upright} for $m\in\mathbb{Z}_+$ are regular at $q=0$. If we write $v_i(m)=v_i(m;0)$ and $w_{j,k}^{\pm}(m)=w_{j,k}^{\pm}(m;0)$ for their constant terms, then $v_i(0)=w_{j,k}^{\pm}(0)=1$ and $$\begin{split}
v_i(m)&=\left(\frac{1-at^{n-i}}{1-bt^{n-i}}\right)t^{i-n}\bigl(1-(1-\delta_{m,1})abt^{n-i}\bigr),\\
w_{j,k}^{+}(m)&=\left(\frac{1-abt^{2n-j-k+1-\delta_{m,1}}}{1-abt^{2n-j-k-1}}\right)t,\\
w_{j,k}^{-}(m)&=\frac{1-t^{k-j+1}}{1-t^{k-j}}
\end{split}$$ for $m\geq 1$.
:::

::: proof
*Proof.* As an example, we compute $v_i(m)$ for $m\in\mathbb{Z}_{\geq 1}$ (the other computations are similar). To compute $v_i(1)$ we rewrite $v_i(1;q)$ as $$v_i(1;q)=\left(\frac{1-qabt^{2(n-i)}}{1-qt^{n-i}}\right)\left(\frac{1-at^{n-i}}{1-bt^{n-i}}\right)
\left(\frac{q-abt^{n-i}}{q-abt^{2(n-i)}}\right),$$ which yields $$v_i(1)=v_i(1;0)=\left(\frac{1-at^{n-i}}{1-bt^{n-i}}\right)t^{i-n}.$$ To compute $v_i(m)$ for $m\geq 2$ we write $v_i(m;q)$ as $$\begin{split}
v_i(m;q)=&\left(\frac{(1-q^{2m-1}abt^{2(n-i)})\bigl(qat^{n-i};q\bigr)_{m-1}\bigl(qabt^{n-i};q\bigr)_{m-2}}
{\bigl(qt^{n-i};q\bigr)_m\bigl(qbt^{n-i};q\bigr)_{m-1}}\right)\\
&\times \left(\frac{(1-at^{n-i})(1-abt^{n-i})}{(1-bt^{n-i})}\right)
\left(\frac{q-abt^{n-i}}{q-abt^{2(n-i)}}\right),
\end{split}$$ which yields $$v_i(m)=v_i(m;0)=\left(\frac{1-at^{n-i}}{1-bt^{n-i}}\right)t^{i-n}(1-abt^{n-i}),\qquad m\geq 2.$$ ◻
:::

::: prop
[]{#formula label="formula"} Let $\lambda\in\Lambda_n$. The generalized quantum dimension $D_q(\lambda)$ [(]{.upright}see [\[Dgeneralized\]](#Dgeneralized){reference-type="eqref" reference="Dgeneralized"}[)]{.upright} is regular at $q=0$. Writing $D_0(\lambda)=D_0(\lambda;a,b;t)$ for $D_q(\lambda;a,b;t)|_{q=0}$, we have $$D_0(\lambda)=a^{-|\lambda|}t^{-2(\rho,\lambda)}\prod_{i=1}^nv_i(\lambda_i)\prod_{1\leq j<k\leq n}
w_{j,k}^+(\lambda_j+\lambda_k)w_{j,k}^-(\lambda_j-\lambda_k),\qquad \lambda\in\Lambda_n.$$
:::

::: proof
*Proof.* This is immediate from Lemma [\[explicitD\]](#explicitD){reference-type="ref" reference="explicitD"} and the previous lemma. ◻
:::

::: eg
For $n=1$, so that $\Lambda_1=\mathbb{Z}_+$, we have $D_0(0)=1$ and $$D_0(\lambda)=a^{-\lambda}\left(\frac{1-a}{1-b}\right)\bigl(1-(1-\delta_{\lambda,1})ab\bigr),\qquad \lambda\geq 1.$$
:::

In contrast to the quantum case, the explicit expression for $D_0(\lambda)=D_0(\lambda;a,b;t)$ from Proposition [\[formula\]](#formula){reference-type="ref" reference="formula"} simplifies for all partitions $\lambda\in\Lambda_n$ as follows.

::: thm
[]{#padicformula label="padicformula"} For $\lambda\in\Lambda_n$ we have $$\label{padicfor}
D_0(\lambda)=a^{-|\lambda|}t^{-2(\rho,\lambda)}\bigg[{n \atop \partial\lambda'}
\bigg]_t \frac{\bigl(at^{n-\lambda_1'};t\bigr)_{\lambda_1'}\bigl(abt^{2n-\lambda_1'-\lambda_2'};t\bigr)_{\lambda_1'+\lambda_2'}}
{\bigl(bt^{n-\lambda_1'}, abt^{n-\lambda_1'-1};t\bigr)_{\lambda_1'}}
\left(\frac{1-abt^{2n-2\lambda_1'-1}}{1-abt^{2n-1}}\right).$$
:::

As remarked already in Subsection [\[repp\]](#repp){reference-type="ref" reference="repp"}, the generalized $p$-adic dimension formula [\[padicfor\]](#padicfor){reference-type="eqref" reference="padicfor"} combined with its representation theoretic interpretation [\[reldimD0\]](#reldimD0){reference-type="eqref" reference="reldimD0"} from [@OU1] leads to the explicit dimension formulas [\[padic-dimension\]](#padic-dimension){reference-type="eqref" reference="padic-dimension"} for the irreducible $\mathcal{M}_{\mathbb{F}}$-spherical $\mathcal{K}_{\mathbb{F}}$-representations $V_\lambda^{\mathbb{F}}$ ($\lambda\in\Lambda_n$).

::: cor
[]{#fundamentalcase label="fundamentalcase"} For $r=0,\ldots,n$ we have $$\label{Dpadic}
D_0(\omega_r)=
\frac{\bigl(t^{n+1-r}, at^{n-r}, abt^{2n-r};t\bigr)_r}
{\bigl(t, bt^{n-r}, abt^{n-r-1};t\bigr)_r}
\left(\frac{1-abt^{2n-2r-1}}{1-abt^{2n-1}}\right)a^{-r}t^{r(r+1-2n)}.$$
:::

::: proof
*Proof.* Follows either by specializing Theorem [\[padicformula\]](#padicformula){reference-type="ref" reference="padicformula"} to $\lambda=\omega_r$, or by taking $q=0$ in [\[fundamentalqformula\]](#fundamentalqformula){reference-type="eqref" reference="fundamentalqformula"}. ◻
:::

We next proceed to prove Theorem [\[padicformula\]](#padicformula){reference-type="ref" reference="padicformula"}, which is based on the expression for $D_0(\lambda)$ as given in Proposition [\[formula\]](#formula){reference-type="ref" reference="formula"}. We divide the proof into several elementary lemmas. Since the theorem is obviously correct for $\lambda=0$, we fix for the proof a nonzero partition $\lambda\in\Lambda_n$.

::: lem
[]{#el1 label="el1"} $$\prod_{i=1}^n v_{i}(\lambda_i)=t^{\frac{1}{2}\lambda_1'(\lambda_1'+1)-n\lambda_1'}
\frac{\bigl(at^{n-\lambda_1'};t\bigr)_{\lambda_1'}
\bigl(abt^{n-\lambda_2'};t\bigr)_{\lambda_2'}}{\bigl(bt^{n-\lambda_1'};t\bigr)_{\lambda_1'}}.$$
:::

::: proof
*Proof.* Using the explicit expression for $v_i$ (see Lemma [\[specialq=0\]](#specialq=0){reference-type="ref" reference="specialq=0"}), we have $$\begin{split}
\prod_{i=1}^n v_{i}(\lambda_i)&=\prod_{i=1}^{\lambda_2'}
\left(\frac{1-at^{n-i}}{1-bt^{n-i}}\right)t^{i-n}\bigl(1-abt^{n-i}\bigr)
\prod_{i=\lambda_2'+1}^{\lambda_1'}\left(\frac{1-at^{n-i}}{1-bt^{n-i}}\right)t^{i-n}\\
&=\prod_{i=1}^{\lambda_1'} \left(\frac{1-at^{n-i}}{1-bt^{n-i}}\right)t^{i-n}
\prod_{i=1}^{\lambda_2'}\left({1-abt^{n-i}}\right)\\
&=t^{\frac{1}{2}\lambda_1'(\lambda_1'+1)-n\lambda_1'}\frac{\bigl(at^{n-\lambda_1'};t\bigr)_{\lambda_1'}
\bigl(abt^{n-\lambda_2'};t\bigr)_{\lambda_2'}}{\bigl(bt^{n-\lambda_1'};t\bigr)_{\lambda_1'}},
\end{split}$$ as desired. ◻
:::

::: lem
[]{#el2 label="el2"} $$\prod_{1\leq j<k\leq n} w_{j,k}^-(\lambda_j-\lambda_k)=\bigg[{n
\atop \partial\lambda'}\bigg]_t.$$
:::

::: proof
*Proof.* Since $w_{j,k}^-(0)=1$ and $w_{j,k}^-(m)=\frac{1-t^{k-j+1}}{1-t^{k-j}}$ for $m\ne 0$ (see Lemma [\[specialq=0\]](#specialq=0){reference-type="ref" reference="specialq=0"}), the term $w_{j,k}^{-}(\lambda_j-\lambda_k)$ contributes to the product only if $\lambda_j \ne \lambda_k$. Hence $$\prod_{1\leq j<k\leq n} w_{j,k}^-(\lambda_j-\lambda_k)=A/B,$$ with $$\begin{split}
&A=\prod_{1\leq j<k\leq
n}\frac{1-t^{k-j+1}}{1-t^{k-j}}=\prod_{l=1}^{n}\frac{(1-t^{l+1})^{n-l}}{(1-t^{l})^{n-l}}=[n]_t! \\
&B=\prod_{\substack{1\leq j<k\leq n \\
\lambda_j =
\lambda_k}}\frac{1-t^{k-j+1}}{1-t^{k-j}}=\prod_{l\ge
0}\prod_{1\leq j<k\leq \lambda_l'-\lambda_{l+1}'}\frac{1-t^{k-j+1}}{1-t^{k-j}}=\prod_{l \ge 0}
[\lambda_l'-\lambda_{l+1}']_t!,
\end{split}$$ as desired. ◻
:::

::: lem
[]{#el3 label="el3"} $$\prod_{1\leq j<k\leq n} w_{j,k}^+(\lambda_j+\lambda_k)=t^{\frac{1}{2}\lambda_1'(\lambda_1'-1)+\lambda_1'(n-\lambda_1')}
\frac{(abt^{2n-\lambda_1'};t)_{\lambda_1'-1}}{(abt^{2n-2\lambda_1'};t)_{\lambda_1'-1}}
\frac{(abt^{2n-2\lambda_1'-1};t)_{\lambda_1'}(abt^{2n-\lambda_1'-\lambda_2'};t)_{\lambda_2'}}
{(abt^{n-\lambda_1'-1};t)_{\lambda_1'}(abt^{n-\lambda_2'};t)_{\lambda_2'}}.$$
:::

::: proof
*Proof.* The term $w_{j,k}^+(m)$ has three possible values depending on $m$ being $0$, $1$ or $\ge 2$ (see Lemma [\[specialq=0\]](#specialq=0){reference-type="ref" reference="specialq=0"}). We are hence led to consider the following sets $$\begin{split}
 X_1&=\{(j,k) \,|\, 1\leq j<k\leq n,\,\, \lambda_j+\lambda_k=1\}=
 \{(j,k) \,|\, \lambda_2' < j \le \lambda_1' < k \le n \}\\
X_2&=\{(j,k) \,|\, 1\leq j<k\leq n,\,\,  \lambda_j+\lambda_k \ge 2 \}=X_2^a\sqcup X_2^b,
\end{split}$$ where the disjoint subsets $X_2^a$ and $X_2^b$ are given by $$X_2^a=\{(j,k) \,|\, 1\leq j<k\leq \lambda_1'\},\qquad
X_2^b=\{(j,k) \,|\, 1\leq j\leq \lambda_2',\,\, \lambda_1'<k\leq n\}.$$ We then have $$\prod_{1\leq j<k\leq n} w_{j,k}^+(\lambda_j+\lambda_k) =
\Pi(X_1)\Pi(X_2^a)\Pi(X_2^b)$$ where we write $\Pi(X)=\prod_{(j,k)\in X} w_{j,k}^+(\lambda_j+\lambda_k)$ for a subset $X\subseteq \{(j,k) \, | \, 1\leq j<k\leq n \}$. We have $$\begin{split}
\Pi(X_1)&=t^{(n-\lambda_1')(\lambda_1'-\lambda_2')}\prod_{j=\lambda_2'+1}^{\lambda_1'}\prod_{k=\lambda_1'+1}^n
\left(\frac{1-abt^{2n-j-k}}{1-abt^{2n-j-k-1}}\right)\\
&=t^{(n-\lambda_1')(\lambda_1'-\lambda_2')}\prod_{j=\lambda_2'+1}^{\lambda_1'}
\left(\frac{1-abt^{2n-j-\lambda_1'-1}}{1-abt^{n-j-1}}\right)= t^{(n-\lambda_1')(\lambda_1'-\lambda_2')}
\frac{\bigl(abt^{2n-2\lambda_1'-1};t\bigr)_{\lambda_1'-\lambda_2'}}{\bigl(ab
t^{n-\lambda_1'-1};t\bigr)_{\lambda_1'-\lambda_2'}}.
\end{split}$$ Using the same notations and simplification arguments as in the proof of Proposition [\[lemref\]](#lemref){reference-type="ref" reference="lemref"}, we have $$\Pi(X_2^a)=t^{\frac{1}{2}\lambda_1'(\lambda_1'-1)}e_{\lambda_1'}(abt^{2n})
e_{\lambda_1'}(abt^{2n-1})=
t^{\frac{1}{2}\lambda_1'(\lambda_1'-1)}\frac{\bigl(abt^{2n-\lambda_1'};t\bigr)_{\lambda_1'-1}}
{\bigl(abt^{2n-2\lambda_1'};t\bigr)_{\lambda_1'-1}}.$$ By a similar computation as for $\Pi(X_1)$, we finally have $$\Pi(X_2^b)=t^{(n-\lambda_1')\lambda_2'}\,
\frac{\bigl(abt^{2n-\lambda_1'-\lambda_2'},
abt^{2n-\lambda_1'-\lambda_2'-1};t\bigr)_{\lambda_2'}}
{\bigl(abt^{n-\lambda_2'}, abt^{n-\lambda_2'-1};t\bigr)_{\lambda_2'}}.$$ Combining these expressions leads to the desired result. ◻
:::

We can now use Proposition [\[formula\]](#formula){reference-type="ref" reference="formula"}, Lemma [\[el1\]](#el1){reference-type="ref" reference="el1"}, Lemma [\[el2\]](#el2){reference-type="ref" reference="el2"} and Lemma [\[el3\]](#el3){reference-type="ref" reference="el3"} to obtain an explicit expression for the generalized $p$-adic dimension $D_0(\lambda)$. After straightforward simplifications, we arrive at the desired expression [\[padicfor\]](#padicfor){reference-type="eqref" reference="padicfor"} for $D_0(\lambda)$.

---
doc_id: arxiv-1203.4538v1
doc_title: "The exponential-logarithmic equivalence classes of surreal numbers"
section_id: sec-005-3-the-kappa-map
section_title: "The kappa map."
section_number: 3
pages: 7-9
source_pdf: 1203.4538v1.pdf
source_sha256: 5e44909e355c78d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.961
doc_brief: "The exponential-logarithmic equivalence classes of surreal numbers — 9 sections: Front matter; Introduction.; Preliminaries on surreal numbers."
---
[]{#sect:kappa label="sect:kappa"}

In this section we define and describe a new map $\kappa$, which takes naturally place between the Conway-Gonshor maps $\Omega$ and $\epsilon$ (see Remark [\[rem:gonshor\]](#rem:gonshor){reference-type="ref" reference="rem:gonshor"}). As in [@kuhl:ord-exp Remark 3.20], we introduce the notion of **exponential equivalence relation** for surreal numbers. Set $\exp^n$ and $\log^n$ for the $n$th iterate of the corresponding maps.

::: defn
[]{#defi:equiv-exp label="defi:equiv-exp"} We set :

-   the **exponential equivalence relation** to be:

    ::: center
    $\forall x,y\in\textbf{NO}^{\gg 1},\ x\sim_{\exp}y\Leftrightarrow \exists n\in\mathbb{N},\ \log^n(|x|)\leq |y|\leq\exp^n(|x|)$;\
    :::

-   the **exponential comparison relation** to be:

    ::: center
    $\forall x,y\in\textbf{NO}^{\gg 1},\ x\gg _{\exp}y\Leftrightarrow \forall n,\ \log^n(|x|)>|y|$.
    :::
:::

::: thm
[]{#theo:kappa-defi label="theo:kappa-defi"} The recursive formula $$\forall a\in\textbf{No},\ \kappa(a)=\kappa_a:=\langle \exp^n(0),\ \exp^n (\kappa_{a^L})\ |\ \log^n (\kappa_{a^R})\rangle$$ (where it is understood that $n\in\mathbb{N}$) defines a map

::: center
$\begin{array}{llcl}
\kappa: &\textbf{No}&\rightarrow&\textbf{No}\\
&a&\mapsto&\kappa(a):=\kappa_a
\end{array}$
:::

with values in $\textbf{No}_{>0}^{\gg 1}$ and such that:

\(i\)

:   for any $a,b\in\textbf{No}$, $a<b\Rightarrow\kappa_a\ll_{\exp}\kappa_b$;

\(ii\)

:   there is a uniformity property for this formula (i.e. the recursive formula does not depend on the choice of the cut for $a$).
:::

::: demo
We proceed by transfinite induction on the length of the surreals considered. For $l(a)=0$, i.e. $a=0=\langle \emptyset|\emptyset\rangle$, we have:

::: center
$\begin{array}{lcl}
\kappa_0&:=&\langle \exp^n(0)\ |\ \emptyset\rangle\\
&=&\langle n\ |\ \emptyset\rangle\textrm{ by cofinality}\\
&=&\omega.\\
\end{array}$
:::

We consider $a\in\textbf{No}$ with $l(a)>0$, and suppose that the theorem holds for any $b\in\textbf{No}$ with $l(b)<l(a)$. Consider a canonical representation $a=\langle a^L\ |\ a^R\rangle$ of $a$. By the induction hypothesis, since $\kappa_{a^L}>\mathbb{R}$ and $\kappa_{a^L}\ll_{\exp}\kappa_{a^R}$, for any $n\in\mathbb{N}$ we have $\exp^n(0)<\exp^n (\kappa_{a^L})<\log^n (\kappa_{a^R})$. Thus the recursive formula for $\kappa_a$ is well defined. Moreover, since $\exp^n(0)$ for $n\in\mathbb{N}$ is cofinal in $\mathbb{R}$ and is always part of the lower elements in the recursive formula, we have $\kappa_a>\mathbb{R}$, meaning that $\kappa_a\in\textbf{No}_{>0}^{\gg 1}$ for any $a\in\textbf{No}$.

\(i\) To show the property $a<b\Rightarrow\kappa_a\ll_{\exp}\kappa_b$, we proceed as in [@gonshor_surreal Theorems 3.1, 3.4 et 5.2] by induction on the natural sum of $l(a)$ and $l(b)$. So we consider $a<b$ in $\textbf{No}$. We denote by $c$ the common initial segment of $a$ and $b$. There are two cases. Either $c=a\textrm{ or }b$: in this case, the property follows directly from the recursive definition of $\kappa$, since $a=b^L$ or $b=a^R$ respectively. Or we have $a<c<b$ with $c<_sa$ and $c<_sb$. Then the natural sum of $a$ and $c$, and of $b$ and $c$, is less than the one of $a$ and $b$. By the induction hypothesis, we obtain that $\kappa_a\ll_{\exp}\kappa_c$ and $\kappa_c<_{\exp}\kappa_b$, so $\kappa_a\ll_{\exp}\kappa_b$.

\(ii\) Concerning the uniformity property, we refer to [@gonshor_surreal Theorems 3.2, 3.5, Corollary to Theorem 5.2 etc]. Let $a=\langle L\ |\ R\rangle\in\textbf{No}$. By Theorem [\[theo:cofin\]](#theo:cofin){reference-type="ref" reference="theo:cofin"} (3.), $(L,R)$ is cofinal in the canonical cut $(L_a,R_a)$ of $a$. By the preceding property, it implies that $(\kappa(L),\kappa(R))$ and $(\kappa(L_a),\kappa(R_a))$ are cofinals, and that $\kappa(L)\ll_{\exp}\kappa_a\ll_{\exp}\kappa(R)\Rightarrow\kappa(L)<\kappa_a<\kappa(R)$ (these inequalities concern elements in $\textbf{No}_{>0}^{\gg 1}$). So we can apply Theorem [\[theo:cofin\]](#theo:cofin){reference-type="ref" reference="theo:cofin"} (2.) to obtain $\kappa_a=\langle\kappa(L_a)\ |\ \kappa(R_a)\rangle = \langle\kappa(L)\ |\ \kappa(R)\rangle$.
:::

::: ex
We compute some particular values:

::: center
$\begin{array}{lcl}
\kappa_1&:=&\langle \exp^n(0),\ \exp^n(\omega)\ |\ \emptyset\rangle\\
&=&\langle \Omega^n(\omega)\ |\ \emptyset\rangle\textrm{ by cofinality}\\
&=&\epsilon_0\ ;\\
 \kappa_{-1}&:=&\langle \exp^n(0),\ |\ \log^n(\omega) \rangle\\
&=&\langle n\ |\ \omega^{\omega^{-n}}\rangle\textrm{ by cofinality}\\
&=&\omega^{\omega^{-\omega}}\ ;\\
\end{array}$
:::
:::

::: thm
[]{#theo:kappa-equivEL label="theo:kappa-equivEL"} A surreal number $b\in\textbf{No}$ is of the form $\kappa_a$ for some $a\in\textbf{No}$ if and only if $b$ is the representative of minimal length in an exponential equivalence class.
:::

::: demo
We got inspired by [@gonshor_surreal Theorem 5.3].\
Consider $a,b\in\textbf{No}$ such that $b\sim_{\exp}\kappa_a\Leftrightarrow  \exists n\in\mathbb{N},\ \log^n(x)\leq y\leq\exp^n(x)$. So we have $\exp^n(0)\ll_{\exp} b$ and $\exp^n (\kappa_{a^L})\ll_{\exp}b\ll_{\exp} \log^n (\kappa_{a^R})$ for any $n\in\mathbb{N}$. So $\kappa_a$ is an initial part of $b$.\
Conversely, we show by transfinite induction on $l(b)\in\textbf{On}$ that for any $b\in\textbf{No}_{>0}^{\gg 1}$, there exists $a\in\textbf{No}$ such that $b\sim_{\exp}\kappa_a$. First, by (ii) of Theorem [\[theo:kappa-defi\]](#theo:kappa-defi){reference-type="ref" reference="theo:kappa-defi"}, we note that $a$ is unique whenever it exists.\
One has $\omega=\kappa_0$.\
Consider $b=\langle L_b\ |\ R_b\rangle\in\textbf{No}_{>0}^{\gg 1}$ with $l(b)>\omega$ and suppose that for any $c\in\textbf{No}$ with $l(c)<l(b)$ the desired property holds. So, for any $c\in L_b\cup R_b$, we have $c\sim_{\exp} \kappa_d$ for some $d\in\textbf{No}$. Let $L:=\{d\in\textbf{No}\ |\ \exists c\in L_b,\ c\sim_{\exp}\kappa_d\}$ and $R:=\{d\in\textbf{No}\ |\ \exists c\in R_b,\ c\sim_{\exp}\kappa_d\}$. Suppose that $L\cap R\neq\emptyset$. We consider $d\in L\cap R$. So there exist $c_1\in L_b$ and $c_2\in R_b$ such that $c_1\sim_{\exp}\kappa_d$ and $c_2\sim_{\exp}\kappa_d$. Since $c_1<c<c_2$, it follows that $c\sim_{\exp}\kappa_d$.\
Suppose now that $L\cap R=\emptyset$. We have $L<R$ (if not we would have $d_1>d_2\Rightarrow\kappa_{d_1}\gg_{\exp}\kappa_{d_2}\Rightarrow c_1>c_2$ with $c_1\in L_b$ and $c_2\in R_b$). Note that, by definition, $\kappa(L)$, respectively $\kappa(R)$, is a complete set of representatives of the exponential-logarithmic equivalence classes containing the elements of $L_b\setminus\{0\}$, respectively of $R_b$. There are 3 different cases:\
$\bullet$ either there are $a\in L$ and $n\in\mathbb{N}$ such that $\exp^n(\kappa_a)\geq b$. Consider $c_1\in L_b$ such that $c_1\sim_{\exp}\kappa_a$. Thus $c_1<b\leq\exp^n(\kappa_a)$ and $c_1\sim_{\exp}\kappa_a\sim_{\exp}\exp^n(\kappa_d)$. So $b\sim_{\exp}\kappa_a$;\
$\bullet$ either there are $a\in R$ and $n\in\mathbb{N}$ such that $\log^n(\kappa_a)\leq b$. Simingly, we obtain $b\sim_{\exp}\kappa_a$ ;\
$\bullet$ or for any $d_1\in L$, $d_2\in R$ and $n\in\mathbb{N}$, we have $\exp^n(\kappa_{d_1})< b<\log^n(\kappa_{d_2})$. Consider $c_1\in L_b\setminus\{0\}$. There is $d_1\in L$ such that $c_1\sim_{\exp}\kappa_{d_1}$. In particular, $c_1\leq \exp^n(\kappa_{d_1})$ for some $n$. As before, for any $c_2\in R_b$, there exists $d_2\in R$ such that $c_2\geq \log^m(\kappa_{d_2})$. Theorem [\[theo:cofin\]](#theo:cofin){reference-type="ref" reference="theo:cofin"} (2.) applies, so $b=\langle \exp^n(0), \exp^n(\kappa_{d_1})\ |\ \log^n(\kappa_{d_2})\rangle=\kappa_a$ where we set $a:=\langle L\ |\ R\rangle$.
:::

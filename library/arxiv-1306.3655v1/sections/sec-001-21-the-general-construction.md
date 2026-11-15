---
doc_id: arxiv-1306.3655v1
doc_title: "The Murnaghan-Nakayama rule and some virtual S n characters"
section_id: sec-001-21-the-general-construction
section_title: "The general construction"
section_number: 2.1
pages: 2-7
source_pdf: 1306.3655v1.pdf
source_sha256: 45dd8bd55687ecce
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 1.0
doc_brief: "The Murnaghan-Nakayama rule and some virtual S n characters — We construct certain virtual characters for the symmetric groups, then compute a formula which calculates the values of these virtual"
---
[]{#section2.1 label="section2.1"}

::: defn
[]{#height1 label="height1"} 1.  Let $n\ge k$, $\nu\vdash k$, and $\eta\vdash n$. We shall assume that $n\ge 2k+2$. Assume $\nu \le\eta$ and that $S$ is a part of the rim of $\eta$ such that $\eta\setminus S=\nu$, then we write $\eta=\nu*S$. Let $h(S)$ denote the height of $S$.

.  Given such $\eta=\nu*S$, we say that \"$S$ covers $\nu$\" if $\nu'_1\le h(S)$. Otherwise $S$ covers only an upper part of $\nu$.

.  Given $\nu\vdash k,$ we start by constructing $\nu*S_1$. Here $S_1$ is the one row of length $n-k$, added to the first row of $\nu$. Clearly, $h(S_1)=1$. Continue and construct the sequence of partitions $\nu*S_1$, $~\nu*S_2$, $~\ldots ~,~\nu*S_{n-k}.$ Lemma [\[height2\]](#height2){reference-type="ref" reference="height2"} shows that $h(S_j)=j$ for $1\le j\le n-k$, and the process stops at $j=n-k$, namely after $n-k$ steps.

.  Define the virtual $S_n$ character $\psi_{\nu,n}$ as follows: $$\begin{aligned}
\label{psi1}
\psi_{\nu,n}:=\sum_{j=1}^{n-k} (-1)^{j+1}\chi^{\nu*S_j}.
\end{aligned}$$

5.  We say that $\nu*S$ *\"has a tail\"* if $\nu*S=\mu=(\mu_1,\mu_2,\ldots)$ where $\mu_1\ge \nu_1+1$.
:::

The following unique-decomposition lemma is crucial here.

::: lem
[]{#uniqueness1 label="uniqueness1"} Let $n\ge 2k+2$. For $i=1,2$ let $\nu^{(i)}\vdash k$, and let $S^{(i)}$ be a rim of $\nu^{(i)}*S^{(i)}$ of length $n-k$. $$\mbox {If}\quad\nu^{(1)}*S^{(1)}=\nu^{(2)}*S^{(2)}\quad\mbox{then}\quad \nu^{(1)}=\nu^{(2)}
\quad\mbox{and}\quad S^{(1)}=S^{(2)}.$$
:::

Note that Example [\[example1\]](#example1){reference-type="ref" reference="example1"} below shows that the condition $n\ge 2k +2$ is necessary.

::: proof
*Proof.* Denote $\eta=\nu^{(1)}*S^{(1)}=\nu^{(2)}*S^{(2)}$. There are three cases to consider.

Case 1: $S^{(1)}$ covers an upper part of $\nu^{(1)}$ (and has a North-East tail).

case 2: The conjugate of case 1.

Case 3: $S^{(1)}$ completely covers $\nu^{(1)}$ (and might have a North-East and/or South-East tails).

Case 1: Here the rim of $\nu^{(1)}*S^{(1)}$ contains $S^{(1)}$ and possibly an additional part which is a part of $\nu^{(1)}$. Assume $\eta=\nu^{(1)}*S^{(1)}=\nu^{(2)}*S^{(2)}$ with $\nu^{(1)}\ne \nu^{(2)}$. Then $\nu^{(2)}$ contains a cell of $S^{(1)}$. This cell splits $S^{(1)}$ into two parts: the North-East part of $S^{(1)}$ and the South-East part (which contains the South-East part of $S^{(1)}$). Let $\tilde S$ denote the South-East part of $S^{(1)}$ together with the lower part of the rim of $\nu^{(2)}$. We need to show that neither the North-East part of $S^{(1)}$, nor $\tilde S$ can be $S^{(2)}$.

The North-East part is properly contained in $S^{(1)}$ hence has length strictly less than $|S^{(1)}|=n-k$, thus this part cannot be $S^{(2)}$.

Since we are in case 1, the part $\tilde S$ is a part of $\nu^{(2)}$. But $\nu^{(2)}\vdash k$, hence $\tilde S$ is of length $|\tilde S|\le k<n-k$, hence this part cannot be $S^{(2)}$ either.

So case 1 is impossible. By conjugation, case 2 is also impossible.

Case 3. The argument here is similar: A cell of $\nu^{(2)}$ on $S^{(1)}$ splits the rim of $\nu^{(1)}*S^{(1)}$ (namely $S^{(1)}$) into two parts, each of length strictly less than $n-k$, hence neither can be $S^{(2)}$. Thus case 3 is also impossible, and the proof follows. ◻
:::

::: lem
[]{#height2 label="height2"} Let $\nu\vdash k$ and let $n\ge 2k+2.$ As in Definition [\[height1\]](#height1){reference-type="ref" reference="height1"}, construct the sequence of partitions $\nu*S_1$, $~\nu*S_2$, $~\ldots ~,~\nu*S_{n-k}$. Then $h(S_j)=j$ for $1\le j\le n-k$.
:::

Here also, Example [\[example1\]](#example1){reference-type="ref" reference="example1"} shows that the condition $n\ge 2k +2$ is necessary.

::: proof
*Proof.* Analogue to the height $h(S)$, we also define the width $w(S)$ (which is the height of the conjugate rim $S'$). By projecting $S$ on the axes (see also (1.7) in [@macdonald]), it follows that $$\begin{aligned}
\label{height.width}
|S|=h(S)+w(S)-1.
\end{aligned}$$

Note that $n-k\ge \nu_1+\nu'_1+1$. Indeed, $k\ge \nu_1+\nu'_1-1$, so $n-k\ge k+2
\ge \nu_1+\nu'_1+1$.

As in Definition [\[height1\]](#height1){reference-type="ref" reference="height1"}.2, construct the sequence $\nu*S_1, ~\nu*S_2,\ldots$. For the first $\nu_1'+1$ steps, by construction and induction, $h(S_j)=j,~1\le j\le \nu_1'+1$ (since $|S|=n-k$, while the number of boxes in $S$ except those in the first row of $\nu*S$ is $\le \nu_1+\nu'_1\le k$). After $\nu_1'+1$ steps, $\nu$ is \"covered\", with $\nu_1+\nu'_1+1$ out of the $n-k$ cells are covering $\nu$. Since $n-k\ge \nu_1+\nu'_1+1$, at that stage there still is a \"tail\" of added boxes in the first (i.e. top) row of $\nu*S_j,$ $j=\nu_1'+1$.

For the remaining steps we consider the conjugate construction. Then, applying [\[height.width\]](#height.width){reference-type="eqref" reference="height.width"} together with the above argument, the proof follows. ◻
:::

::: example
[]{#example1 label="example1"} **Counter examples** when $n\not\ge 2k+2$.

.  Let $k=3,~n=6,~\eta=(3,3),~\nu^{(1)}=(3), ~\nu^{(2)}=(2,1)$. Let $S^{(i)}$, $i=1,2$, satisfy $$(3,3)=\nu^{(1)}*S^{(1)}=\nu^{(2)}*S^{(2)}.$$ Then clearly $S^{(1)}\ne S^{(2)}$, as well as $\nu^{(1)}\ne \nu^{(2)}$.

2\.  Again let $k=3,~n=6$. Let $\nu=(3)$ and construct the sequence of partitions\
$\nu*S_1$, $~\nu*S_2$, $~\nu*S_3\ldots$ Then $h(S_2)=1\ne 2$.
:::

We proceed with the general case.

::: cor
[]{#height3 label="height3"} Let $\nu\vdash k$, and let $n\ge 2k+2$, then $$\psi_{\nu,n}=\sum_{S,\;\nu*S\vdash n}(-1)^{h(S)+1}\chi^{\nu*S}=\sum_{j=1}^{n-k}(-1)^{h(S_j)+1}\chi^{\nu*S_j}.$$
:::

::: proof
*Proof.* This follows from Equation [\[psi1\]](#psi1){reference-type="eqref" reference="psi1"} (which defines $\psi_{\nu,n}$) and from Lemma [\[height2\]](#height2){reference-type="ref" reference="height2"}. ◻
:::

# A formula for $\psi_{\nu,n}(\mu)$

Our aim is to prove the following formula.

::: thm
[]{#v4 label="v4"}

Let $\nu=(\nu_1,\nu_2,\ldots )\vdash k$, $n\ge 2k+2$ . Let $\mu=(\mu_1,\mu_2,\ldots )\vdash n$, and denote $\bar\mu=(\mu_2,\mu_3,\ldots)$, so $\mu_1=n-k$ if and only if $\bar\mu\vdash k$. Then

$$\begin{aligned}
\label{general.conjecture}
\psi_{\nu,n}(\mu)=\begin{cases}\chi^\nu(\bar\mu)\cdot(n-k) & if  ~\mu_1= n-k
\\
0 & if ~\mu_1\ne n-k\\
\end{cases}
\end{aligned}$$
:::

The proof is given below.

Let $n\ge 2k+2$ and let $\nu\vdash k$, so $(n-k,\nu)$ is a partition of $n$. Let $\lambda\vdash n$ and assume $\chi^\lambda_{(n-k,\nu)}\ne 0$, then, by the Murnaghan-Nakayama (M-N) rule, $\lambda$ can be written, probably in several ways, as $\lambda=\rho*S$ where $\rho\vdash k$, $S$ is part of the rim of $\lambda$ and $|S|=n-k$. By Lemma [\[uniqueness1\]](#uniqueness1){reference-type="ref" reference="uniqueness1"} this decomposition, with $|\rho|=k$, is unique, hence we can write $\lambda\leftrightarrow (\rho_\lambda ,S_\lambda).$ Again by the M-N rule,with $\lambda=\rho*S$, $$\begin{aligned}
\label{basic2}
\chi^\lambda_{(n-k,\nu)}=(-1)^{h(S)+1}\chi^{\rho}_\nu=
(-1)^{h(S_\lambda)+1}\chi^{\rho_\lambda}_\nu.
\end{aligned}$$

Lemma [\[uniqueness1\]](#uniqueness1){reference-type="ref" reference="uniqueness1"} allows us to prove the following formula.

::: prop
[]{#usemn label="usemn"} Let $\nu\vdash k$ and let $n\ge 2k+2$. Then $$\sum_{\lambda\vdash n}\chi^\lambda_{(n-k,\nu)}\chi^\lambda=\sum_{\rho\vdash k}
\chi^\rho_\nu \cdot \psi_{\rho,n}.$$
:::

::: proof
*Proof.* We just saw that $$\{\lambda\vdash n\}=\{\rho*S\vdash n\mid \rho\vdash k,~~|S|=n-k\}\cup
\{\lambda\vdash n\mid\chi^\lambda_{(n-k,\nu)}=0\},$$ and by Lemma [\[uniqueness1\]](#uniqueness1){reference-type="ref" reference="uniqueness1"} we have the bijection $$\{\rho*S\vdash n\mid \rho\vdash k,~~|S|=n-k\}\longleftrightarrow
\{(\rho,S)\mid \rho\vdash k,~~|S|=n-k\quad\mbox{and}\quad \rho*S\vdash n\}.$$ We denote $$A_{k,n}=\{(\rho,S)\mid \rho\vdash k,~~|S|=n-k\quad\mbox{and}\quad \rho*S\vdash n\}.$$ By [\[basic2\]](#basic2){reference-type="eqref" reference="basic2"} $$\sum_{\lambda\vdash n}\chi^\lambda_{(n-k,\nu)}\chi^\lambda=
\sum_{(\rho,S)\in A_{k,n}}(-1)^{h(S)+1}\chi^\rho_\nu\cdot\chi^\lambda=$$ $$\sum_{\rho\vdash k}~~\sum_{S,\;\rho*S\vdash n}(-1)^{h(S)+1}\chi^\rho_\nu\cdot\chi^{\rho*S}=$$ $$~~~~~~~~~~~~~
\sum_{\rho\vdash k}\chi^\rho_\nu~\sum_{S,\;\rho*S\vdash n}(-1)^{h(S)+1}\chi^{\rho*S}=
\sum_{\rho\vdash k}\chi^\rho_\nu\cdot\psi_{\rho,n}.$$ The last equality applied corollary [\[height3\]](#height3){reference-type="ref" reference="height3"}. ◻
:::

::: remark
[]{#u33 label="u33"}
:::

Let $d=|\{Par(k)\}|.$ Note that in matrix form, Proposition [\[usemn\]](#usemn){reference-type="ref" reference="usemn"} can be written as follows: $$\begin{aligned}
\label{usemn2}
\left[\chi^\rho_\nu\right]\left[ \psi_{\rho,n}\right]=
\left[\sum_{\lambda\vdash n}\chi^\lambda _{(n-k,\nu)}\cdot\chi^\lambda \right].
\end{aligned}$$ Here $\left[\chi^\rho_\nu\right]$ is the $d\times d$ character table of $S_k$, and $\left[ \psi_{\rho,n}\right]$ is a column of height $d$. Of course, the locations of the entries of both $\left[\chi^\rho_\nu\right]$ and $\left[ \psi_{\rho,n}\right]$ depend on how we order $Par(k)$. Applying [\[usemn2\]](#usemn2){reference-type="eqref" reference="usemn2"} on $\mu\vdash n$ we get $$\begin{aligned}
\label{usemn3}
\left[\chi^\rho_\nu\right]\left[ \psi_{\rho,n}(\mu)\right]
=\left[\sum_{\lambda\vdash n}\chi^\lambda _{(n-k,\nu)}\cdot\chi^\lambda_\mu \right]
\end{aligned}$$

Recall the classical column-orthogonality-relations for the $S_n$ characters.

::: thm
[]{#v5 label="v5"} (The column-orthogonality-relations) $$\begin{aligned}
\label{columns1}
\sum_{\lambda\vdash n}\chi^\lambda_\eta\chi^\lambda_\mu=\begin{cases}|Z_{S_n}(\eta)| & if ~\mu=\eta
\\
0 & if~ \mu\ne \eta,\\
\end{cases}
\end{aligned}$$ where $\lambda,\eta,\mu\vdash n$, and $Z_{S_n}(\eta)$ is the centralizer of $\eta$ in $S_n$ (i.e the centralizer of $\pi\in S_n$ with cycle structure $\eta$). Let $K=K^{(n)}=\left[ \chi_{\eta}^{\theta}\right]$ denote the character table of $S_n$, then  [\[columns1\]](#columns1){reference-type="eqref" reference="columns1"} can be written as $$\begin{aligned}
\label{columns2}
 KK^T=diag(|Z_{S_n}(\eta)|,\mid \eta\vdash n).
  
\end{aligned}$$
:::

Then numbers $|Z_{S_n}(\eta)|$ are calculated through the following well known formula.

::: thm
[]{#v1 label="v1"} Let $\eta\vdash n$, $\eta=(1^{m_1},2^{m_2},\ldots )$, and let $Z_{S_n}(\eta)$ denote the centralizer in $S_n$ of $\sigma\in S_n$ where $\eta$ is the cycle structure of $\sigma$. Then $$|Z_{S_n}(\sigma)|=|Z_{S_n}(\eta)|=\prod_i (i^{m_i}\cdot m_i!).$$
:::

::: remark
[]{#centralizer1 label="centralizer1"} Let $\nu\vdash k$, $n\ge 2k+2$. Then $(n-k,\nu)$ is a partition (of $n$), and $$|Z_{S_n}(n-k,\nu)|=|Z_{S_k}(\nu)|\cdot (n-k).$$
:::

This follows from Theorem [\[v1\]](#v1){reference-type="ref" reference="v1"} since $n-k$ is strictly larger than any component of $\nu$. Together with [\[columns1\]](#columns1){reference-type="eqref" reference="columns1"} this implies

::: cor
[]{#centralizer2 label="centralizer2"} Let $\nu\vdash k$, $n\ge 2k+2$, $\mu=(\mu_1,\mu_2,\ldots)\vdash n$ and let $\bar \mu=(\mu_2,\mu_3,\ldots)$. Then $$\begin{aligned}
\label{columns12}
\sum_{\lambda\vdash n}\chi^\lambda_{(n-k,\nu)}\chi^\lambda_\mu=
\begin{cases}|Z_{S_k}(\nu)|\cdot(n-k) & if ~\bar\mu=\nu
\\
0 & if~ \mu\ne \eta.\\
\end{cases}
\end{aligned}$$
:::

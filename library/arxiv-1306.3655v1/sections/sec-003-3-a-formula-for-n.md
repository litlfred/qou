---
doc_id: arxiv-1306.3655v1
doc_title: "The Murnaghan-Nakayama rule and some virtual S n characters"
section_id: sec-003-3-a-formula-for-n
section_title: "A formula for ,n()"
section_number: 3
pages: 5-7
source_pdf: 1306.3655v1.pdf
source_sha256: 45dd8bd55687ecce
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 1.0
doc_brief: "The Murnaghan-Nakayama rule and some virtual S n characters — We construct certain virtual characters for the symmetric groups, then compute a formula which calculates the values of these virtual"
---
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

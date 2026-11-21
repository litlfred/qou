---
doc_id: arxiv-1306.3655v1
doc_title: "The Murnaghan-Nakayama rule and some virtual S n characters"
section_id: sec-002-21-the-general-construction
section_title: "The general construction"
section_number: 2.1
pages: 2-5
source_pdf: 1306.3655v1.pdf
source_sha256: 45dd8bd55687ecce
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.992
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

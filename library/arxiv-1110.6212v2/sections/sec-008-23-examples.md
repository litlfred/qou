---
doc_id: arxiv-1110.6212v2
doc_title: "On calibrated representations and the Plancherel Theorem for aﬃne Hecke algebras"
section_id: sec-008-23-examples
section_title: "Examples"
section_number: 2.3
pages: 11-14
source_pdf: 1110.6212v2.pdf
source_sha256: 1923b6a0bfdc810f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.89
---
[]{#sect:examples label="sect:examples"}

Let us give some concrete examples of the construction from Theorem [\[thm:repmain\]](#thm:repmain){reference-type="ref" reference="thm:repmain"}. Most of these examples will arise in the Plancherel Theorems in the later parts of this paper (see Section [\[sect:plancherel\]](#sect:plancherel){reference-type="ref" reference="sect:plancherel"}). Of interest, we see in the third and fourth examples that some non-calibrated modules (in the single parameter case) can be constructed from calibrated modules (of multi-parameter algebras) by making an appropriate change of basis and taking a limit.

::: Example
[]{#ex:1 label="ex:1"} Let $\mathscr{H}$ be a $\tilde{C}_2$ Hecke algebra with $L=P$ and with parameters $q_1$ and $q_2$ (see Section [\[sect:C2P\]](#sect:C2P){reference-type="ref" reference="sect:C2P"}). Let $t\in\mathrm{Hom}(P,\mathbb{C}^{\times})$ be the character with $t^{\omega_1}=-q_1^{-1}$ and $t^{\omega_2}=q_1^{-1/2}$, so that $t^{\alpha_1^{\vee}}=q_1^{-1}$ and $t^{\alpha_2^{\vee}}=-1$. Thus $N(t)^{\vee}=\{\alpha_1^{\vee},\alpha_1^{\vee}+2\alpha_2^{\vee}\}$ and $D(t)=\emptyset$. Thus there are $4$ choices for subsets $J\subseteq N(t)$. Let $J_1^{\vee}=\emptyset$, $J_2^{\vee}=\{\alpha_1^{\vee}\}$, $J_3^{\vee}=\{\alpha_1^{\vee}+2\alpha_2^{\vee}\}$, and $J_4^{\vee}=\{\alpha_1^{\vee},\alpha_1^{\vee}+2\alpha_2^{\vee}\}$. We compute $F_{J_1}(t)=\{1,s_2\}$, $F_{J_2}(t)=\{s_1,s_2s_1\}$, $F_{J_3}(t)=\{s_1s_2,s_2s_1s_2\}$, and $F_{J_4}(t)=\{s_1s_2s_1,s_1s_2s_1s_2\}$, and so the calibration graph is as in Figure [1](#fig:calibex1){reference-type="ref" reference="fig:calibex1"}(a). Thus by Theorem [\[thm:repmain\]](#thm:repmain){reference-type="ref" reference="thm:repmain"} and Proposition [\[prop:quotient\]](#prop:quotient){reference-type="ref" reference="prop:quotient"} there are $4$ irreducible modules with central character $t$, each with dimension $2$. For example, the matrices for the module $M_{J_1}(t)$ with respect to the basis $\{e_t,e_{s_2t}\}$ are $\pi(T_1)=-q_1^{-1/2}I$, $\pi(x^{\omega_1})=-q_1^{-1}I$, and $$\begin{aligned}
\pi(T_2)&=\frac{q_2^{1/2}}{2}\begin{pmatrix}1-q_2^{-1}&1+q_2^{-1}\\
1+q_2^{-1}&1-q_2^{-1}\end{pmatrix}&\pi(x^{\omega_2})&=\mathrm{diag}(q_1^{-1/2},-q_1^{-1/2}).
\end{aligned}$$ Note that $\pi(x^{\alpha_1^{\vee}})=q_1^{-1}I$ and $\pi(x^{\alpha_2^{\vee}})=-I$, and it follows that the restriction $\pi|_{\mathscr{H}_Q}$ is not irreducible (indeed $\pi|_{\mathscr{H}_Q}$ is the direct sum of the representations $\pi^4$ and $\pi^5$ from Section [\[sect:C2Q\]](#sect:C2Q){reference-type="ref" reference="sect:C2Q"}). This does not contradict the irreducibility statement of Theorem [\[thm:repmain\]](#thm:repmain){reference-type="ref" reference="thm:repmain"}, because the calibration graph changes if we use the lattice $Q$ instead of $P$ (see Example [\[ex:2\]](#ex:2){reference-type="ref" reference="ex:2"}).
:::

::: Example
[]{#ex:2 label="ex:2"} Now let $\mathscr{H}$ be a $\tilde{C}_2$ Hecke algebra with $L=Q$. Let $t\in\mathrm{Hom}(Q,\mathbb{C}^{\times})$ be the character with $t^{\alpha_1^{\vee}}=q_1^{-1}$ and $t^{\alpha_2^{\vee}}=-1$ (note the similarity to Example [\[ex:1\]](#ex:1){reference-type="ref" reference="ex:1"}). Then $N(t)$ and $D(t)$ are as in Example [\[ex:1\]](#ex:1){reference-type="ref" reference="ex:1"}. Let $J_1,J_2,J_3,J_4$ be as in Example [\[ex:1\]](#ex:1){reference-type="ref" reference="ex:1"}, and then the sets $F_{J_i}(t)$ are as computed in Example [\[ex:1\]](#ex:1){reference-type="ref" reference="ex:1"}. However now $s_2t=t$, and so the calibration graph is as shown in Figure [1](#fig:calibex1){reference-type="ref" reference="fig:calibex1"}(b). Thus Theorem [\[thm:repmain\]](#thm:repmain){reference-type="ref" reference="thm:repmain"} constructs $2$ irreducible $1$-dimensional modules, and $1$ irreducible $2$-dimensional module with central character $t$.
:::

<figure id="fig:calibex1">

<figcaption>Calibration graphs for Examples <a href="#ex:1" data-reference-type="ref" data-reference="ex:1">[ex:1]</a> and <a href="#ex:2" data-reference-type="ref" data-reference="ex:2">[ex:2]</a></figcaption>
</figure>

::: Example
Let $\mathscr{H}$ be a $\tilde{G}_2$ Hecke algebra with $L=Q=P$ and with parameters $q_1$ and $q_2$ (see Section [\[sect:G2\]](#sect:G2){reference-type="ref" reference="sect:G2"}). Let $t\in\mathrm{Hom}(Q,\mathbb{C}^{\times})$ be the character with $t^{\alpha_1^{\vee}}=q_1$ and $t^{\alpha_2^{\vee}}=q_1^{-1/2}q_2^{1/2}$. If $q_1\neq q_2$ and $q_1\neq q_2^3$ then this character is regular, and we compute $N(t)^{\vee}=\{\alpha_1^{\vee},\alpha_1^{\vee}+2\alpha_2^{\vee}\}$. Thus there are $4$ choices for $J\subseteq N(t)$, and the connected components of the calibration graph are given by $\{wt\mid w\in F_J(t)\}$ for these choices of $J$. Consider the case $J^{\vee}=\{\alpha_1^{\vee}+2\alpha_2^{\vee}\}$. We compute $F_J(t)=\{s_2s_1s_2s_1,s_1s_2s_1s_2s_1,s_2s_1s_2s_1s_2s_1\}$. The matrices for $\pi=M_J(t)$ are $$\begin{aligned}
\pi(T_1)&=q_1^{\frac{1}{2}}\begin{pmatrix}
\frac{1-q_1^{-1}}{1- q_1^{\frac{1}{2}}q_2^{-\frac{3}{2}}}&
\frac{1- q_1^{-\frac{3}{2}}q_2^{\frac{3}{2}}}{1- q_1^{-\frac{1}{2}}q_2^{\frac{3}{2}}}&0\\
\frac{1- q_1^{-\frac{1}{2}}q_2^{-\frac{3}{2}}}{1- q_1^{\frac{1}{2}}q_2^{-\frac{3}{2}}}&
\frac{1-q_1^{-1}}{1- q_1^{-\frac{1}{2}}q_2^{\frac{3}{2}}}&0\\
0&0&-q_1^{-1}
\end{pmatrix}&
\pi(T_2)&=q_2^{\frac{1}{2}}\begin{pmatrix}
-q_2^{-1}&0&0\\
0&\frac{1-q_2^{-1}}{1- q_1^{\frac{1}{2}}q_2^{-\frac{1}{2}}}&
\frac{1- q_1^{\frac{1}{2}}q_2^{-\frac{3}{2}}}{1- q_1^{-\frac{1}{2}}q_2^{\frac{1}{2}}}\\
0&\frac{1- q_1^{-\frac{1}{2}}q_2^{-\frac{1}{2}}}{1- q_1^{\frac{1}{2}}q_2^{-\frac{1}{2}}}&\frac{1-q_2^{-1}}{1- q_1^{-\frac{1}{2}}q_2^{\frac{1}{2}}}
\end{pmatrix}\\
\pi(x^{\alpha_1^{\vee}})&=\mathrm{diag}( q_1^{-\frac{1}{2}}q_2^{\frac{3}{2}}, q_1^{\frac{1}{2}}q_2^{-\frac{3}{2}},q_1^{-1})&\pi(x^{\alpha_2^{\vee}})&=\mathrm{diag}(q_2^{-1}, q_1^{-\frac{1}{2}}q_2^{\frac{1}{2}}, q_1^{\frac{1}{2}}q_2^{-\frac{1}{2}})
\end{aligned}$$ The construction breaks down when $q_1=q_2$ or when $q_1=q_2^3$. These cases can be dealt with by a suitable change of basis in the module $M_J(t)$. Let $$\begin{aligned}
A&=\begin{pmatrix}
1&0&0\\
0&1&-q_1^{\frac{1}{2}}q_2^{-\frac{1}{2}}\\
0&-1&1\end{pmatrix}&B&=\begin{pmatrix}1&-q_1^{\frac{1}{2}}q_2^{-\frac{3}{2}}&0\\
-1&1&0\\
0&0&1-q_1^{\frac{1}{2}}q_2^{-\frac{3}{2}}
\end{pmatrix}.
\end{aligned}$$ After conjugating each representing matrix by $A$ (respectively $B$) it is observed that the resulting matrices are defined at $q_1=q_2$ (respectively $q_1=q_2^3$). Setting $q_1=q_2=q$ (respectively $q_1=q^3$ with $q_2=q$) gives a (non-calibrated) irreducible representation of the algebra $\mathscr{H}(q,q)$ (respectively the algebra $\mathscr{H}(q,q^3)$). For example, the matrices in the $q_1=q_2=q$ case become $$\begin{aligned}
\pi(T_1)&=q^{\frac{1}{2}}\begin{pmatrix}
1&\frac{3}{q-1}&\frac{3}{q-1}\\
\frac{q+1}{q}&\frac{2q+1}{q(q-1)}&\frac{3}{q-1}\\
-\frac{q+1}{q}&-\frac{3}{q-1}&-\frac{4q-1}{q(q-1)}\end{pmatrix}
&
\pi(T_2)&=q^{\frac{1}{2}}\begin{pmatrix}
-q^{-1}&0&0\\
0&1&0\\
0&-2q^{-1}&-q^{-1}\end{pmatrix}\\
\pi(x^{\alpha_1^{\vee}})&=\begin{pmatrix}
q&0&0\\
0&-2q^{-1}&-3q^{-1}\\
0&3q^{-1}&4q^{-1}\end{pmatrix}&
\pi(x^{\alpha_2^{\vee}})&=\begin{pmatrix}
q^{-1}&0&0\\
0&3&2\\
0&-2&-1\end{pmatrix}.
\end{aligned}$$
:::

::: Example
Let $\mathscr{H}$ be a $\tilde{C}_2$ affine Hecke algebra with either $L=Q$ or $L=P$ and with parameters $q_1$ and $q_2$ (see Sections [\[sect:C2Q\]](#sect:C2Q){reference-type="ref" reference="sect:C2Q"} and [\[sect:C2P\]](#sect:C2P){reference-type="ref" reference="sect:C2P"}). Let $t\in\mathrm{Hom}(L,\mathbb{C}^{\times})$ be a character with $t^{\alpha_1^{\vee}}=q_1^{-1}$ and $t^{\alpha_2^{\vee}}=q_2$. If $q_1\neq q_2$ and $q_1\neq q_2^2$ then the character $t$ is regular, since $t^{\alpha_1^{\vee}+\alpha_2^{\vee}}=q_1^{-1}q_2$ and $t^{\alpha_1^{\vee}+2\alpha_2^{\vee}}=q_1^{-1}q_2^2$. Thus we compute $N(t)=\{\alpha_1,\alpha_2\}$ and $D(t)=\emptyset$. There are $4$ choices for $J\subseteq N(t)$, namely $J_1=\emptyset$, $J_2=\{\alpha_1\}$, $J_3=\{\alpha_2\}$, and $J_4=\{\alpha_1,\alpha_2\}$. We compute $$\begin{aligned}
F_{J_1}(t)&=\{1\},&F_{J_2}(t)&=\{s_1,s_2s_1,s_1s_2s_1\},&F_{J_3}(t)&=\{s_2,s_1s_2,s_2s_1s_2\},&F_{J_4}(t)&=\{s_1s_2s_1s_2\}.
\end{aligned}$$ The sets $\{wt\mid w\in F_{J_i}(t)\}$ with $i=1,2,3,4$ are the connected components of the calibration graph of $t$. Thus there are $4$ irreducible modules $M_{J_i}(t)$ ($i=1,2,3,4$) with central character $t$, with dimensions $1,3,3,1$ respectively.

Consider the module $M_{J_3}(t)$ (this module will appear in the Plancherel Theorem for $\tilde{C}_2$). The matrices of $T_1,T_2,x^{\alpha_1^{\vee}}$ and $x^{\alpha_2^{\vee}}$ relative to the basis $e_{s_2t},e_{s_1s_2t},e_{s_2s_1s_2t}$ are $$\begin{aligned}
\pi(T_1)&=q_1^{\frac{1}{2}}\begin{pmatrix}
\frac{1-q_1^{-1}}{1-q_1q_2^{-2}}&
\frac{1-q_1^{-2}q_2^2}{1-q_1^{-1}q_2^2}&
0\\
\frac{1-q_2^{-2}}{1-q_1q_2^{-2}}&
\frac{1-q_1^{-1}}{1-q_1^{-1}q_2^2}&
0\\
0&0&-q_1^{-1}
\end{pmatrix}&
\pi(T_2)&=q_2^{\frac{1}{2}}
\begin{pmatrix}
-q_2^{-1}&0&0\\
0&
\frac{1-q_2^{-1}}{1-q_1q_2^{-1}}&
\frac{1-q_1^{-1}}{1-q_1^{-1}q_2}\\
0&
\frac{1-q_1q_2^{-2}}{1-q_1q_2^{-1}}&
\frac{1-q_2^{-1}}{1-q_1^{-1}q_2}
\end{pmatrix}\\
\pi(x^{\alpha_1^{\vee}})&=\mathrm{diag}(q_1^{-1}q_2^2,q_1q_2^{-2},q_1^{-1})&\pi(x^{\alpha_2^{\vee}})&=\mathrm{diag}(q_2^{-1},q_1^{-1}q_2,q_1q_2^{-1}).
\end{aligned}$$ If $L=P$ then $\omega_1=\alpha_1^{\vee}+\alpha_2^{\vee}$ and $\omega_2=\alpha_1^{\vee}/2+\alpha_2^{\vee}$. Thus there are $2$ characters $t\in\mathrm{Hom}(P,\mathbb{C}^{\times})$ with $t^{\alpha_1^{\vee}}=q_1^{-1}$ and $t^{\alpha_2^{\vee}}=q_2$, specifically $t^{\omega_1}=q_1^{-1}q_2$ and $t^{\omega_2}=\pm q_1^{-1/2}q_2$. The corresponding matrices for $x^{\omega_1}$ and $x^{\omega_2}$ are $$\begin{aligned}
\pi(x^{\omega_1})&=\mathrm{diag}(q_1^{-1}q_2,q_2^{-1},q_2^{-1})&\pi(x^{\omega_2})&=\pm\mathrm{diag}(q_1^{-1/2},q_1^{-1/2},q_1^{1/2}q_2^{-1}).
\end{aligned}$$ In the cases $q_1=q_2$ or $q_1=q_2^2$ an analogous computation to that in Example 2 can be used to construct (non-calibrated) irreducible representations of $\mathscr{H}(q,q)$ and $\mathscr{H}(q,q^2)$.
:::

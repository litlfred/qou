---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-016-6-invariance-of-the-3d-index-under-23-moves-and
section_title: "Invariance of the 3D index under 23 moves and 20 moves"
section_number: 6
pages: 18-21
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.981
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sec.23 label="sec.23"}

## Invariance under the $3\to 2$ move {#sub.3-2}

Consider two ideal triangulations $\mathcal T$ and $\widetilde{\mathcal T}$ with $N$ and $N+1$ tetrahedra, respectively, related by a $2-3$ move shown in Figure [1](#fig.23too){reference-type="ref" reference="fig.23too"}.

<figure id="fig.23too">
<div class="center">
<embed src="draws/23.pdf" />
</div>
<figcaption>A <span class="math inline">2 − 3</span> move.</figcaption>
</figure>

The above figure matches the conventions of [@DG Sec.3.6]. For a variable, matrix or vector $f$ associated to $\mathcal T$, we will denote by $\widetilde{f}$ the corresponding variable, matrix or vector associated to $\widetilde{\mathcal T}$. Let us use variables $(Z,Z',Z'')$ and $(\widetilde Z,\widetilde Z',\widetilde Z'')$ to denote the angles of $\mathcal T$ and and $\widetilde{\mathcal T}$ respectively, where $$Z := (X_1,X_2,Z_3,...,Z_N)\,,\qquad 
\tilde Z := (W_1,W_2,W_3,Z_3,...,Z_N)\,.$$ We fix a quad type assigning these variables to $\mathcal T$ and $\widetilde{\mathcal T}$ as in Figure [\[fig.23\]](#fig.23){reference-type="ref" reference="fig.23"}. When calculating the Neumann-Zagier matrices, we will assume that we keep the edge equation which comes from the internal edge of the 2-3 bipyramid.

There are nine linear relations among the shapes of the tetrahedra involved in the move; three come from adding dihedral angles on the equatorial edges of the bipyramid:

$$\label{eq.s3}
W_1'=X_1+X_2\,,\qquad W_2'=X_1'+X_2''\,,\qquad 
W_3'= X_1''+X_2'\,,$$

and six from the longitudinal edges:

$$\label{eq.s6}
\begin{array}{c@{\qquad}c@{\qquad}c}
X_1=W_2+W_3''\,,& X_1'=W_3+W_1''\,,&  X_1''=W_1+W_2''\,, \\[.2cm]
X_2 = W_2''+W_3\,,& X_2'=W_1''+W_2\,,& X_2''=W_3''+W_1\,.
\end{array}$$

Moreover, due to the central edge of the bipyramid, there is an extra gluing constraint in $\widetilde\mathcal T$:

$$\label{eq.glue3} 
W_1'+W_2'+W_3' = 2\pi i\,.$$

Let $\mathrm{GA}(\mathcal T)$ and $\mathrm{A}(\mathcal T)$ denote, respectively, the sets of generalized and strict angle structures of $\mathcal T$.

::: lemma
[]{#lem.mu.2.3 label="lem.mu.2.3"} Consider the map: $$\label{eq.3-2.angles}
\mu_{3\to 2} \colon \mathrm{GA}(\widetilde{\mathcal T}) \to \mathrm{GA}(\mathcal T),
\qquad
\mu_{3\to 2} (\widetilde Z,\widetilde Z',\widetilde Z'') = (Z,Z',Z'')$$ defined by Equations [\[eq.s6\]](#eq.s6){reference-type="eqref" reference="eq.s6"}. It induces a map $$\mu_{3\to 2} \colon \mathrm{A}(\widetilde{\mathcal T}) \to \mathrm{A}(\mathcal T)$$
:::

::: proof
*Proof.* To check that $\mu_{3 \to 2}$ is well-defined we need to show that $X_i+X_i'+X_i''=1$ is satisfied for $i=1,2$, assuming that Equation [\[eq.glue3\]](#eq.glue3){reference-type="eqref" reference="eq.glue3"} holds and $W_i+W_i'+W_i''=1$ for $i=1,2,3$. This is easy to check. If $(\widetilde Z,\widetilde Z',\widetilde Z'') \in \mathbb R_+^{3(N+1)}$ (where $\mathbb R_+$ is the set of positive real numbers), it is manifest from the definition that $(Z,Z',Z'') \in \mathbb R_+^{3N}$. In other words, $\mu_{3\to 2}$ sends strict angle structures on $\widetilde{\mathcal T}$ to those on $\mathcal T$. ◻
:::

This proves the first part of Proposition [\[prop.3.2.index\]](#prop.3.2.index){reference-type="ref" reference="prop.3.2.index"}. To prove the remaining part, we study how are the gluing equation matrices of $\mathcal T$ and $\widetilde{\mathcal T}$ related. Let $(\bar{\mathbf A}|\bar{\mathbf B}|\bar{\mathbf C})$ denote the matrix of exponents of the gluing equations of $\mathcal T$. We will use column notation and write $$\bar{\mathbf A} = (\bar a_1,\;\bar a_2,\;\bar a_i)\,,\quad 
\bar{\mathbf B} = (\bar b_1,\;\bar b_2,\;\bar b_i)\,,\quad
\bar{\mathbf C} = (\bar c_1,\;\bar c_2,\;\bar c_i)\,,$$ where $\bar a_i$ meaning $(\bar a_3,\bar a_4,...,\bar a_N)$ and similarly for $\bar b_i$ and $\bar c_i$. Eliminating the $Z'$ variables, we obtain $$\mathbf A = \bar{\mathbf A} - \bar{\mathbf B}, \qquad
\mathbf B = \bar{\mathbf C} - \bar{\mathbf B} \,.$$ In other words, $$\label{eq.a1b1}
(a_1, a_2, a_i)=(\bar a_1 - \bar b_1, \bar a_2 - \bar b_2, \bar a_i - \bar b_i)
\quad
(b_1, b_2, b_i)=(\bar c_1 - \bar b_1, \bar c_2 - \bar b_2, \bar c_i - \bar b_i)
\,.$$ To compute the corresponding matrices of $\widetilde{\mathcal T}$, use

$$\begin{aligned}
2 &= \bar a_1 X_1 + \bar a_2 X_2 + \bar a_i Z_i 
+ \bar b_1 X'_1 + \bar b_2 X'_2 + \bar b_i Z'_i +
\bar c_1 X''_1 + \bar c_2 X''_2 + \bar c_i Z''_i \\
&= \bar a_1 (W_2+W_3'') + \bar a_2 ( W_2''+W_3) + \bar a_i Z_i \\
&\quad + \bar b_1 (W_3+W_1'') + \bar b_2 (W_1''+W_2) + \bar b_i Z'_i  \\
&\quad + \bar c_1(W_1+W_2'') + \bar c_2 (W_3''+W_1) + \bar c_i Z''_i \,.
\end{aligned}$$ Collecting the coefficients of $\tilde Z, \tilde Z', \tilde Z''$ it follows that the matrix of exponents of the gluing equations of $\widetilde{\mathcal T}$ is given by $$\begin{aligned}
\widetilde{\bar{\mathbf A}} 
& = \begin{pmatrix} 0 & 0 & 0  & 0 \\ 
\bar c_1+\bar c_2 & \bar a_1 + \bar b_2 & \bar a_2 + \bar b_1 & \bar a_i 
\end{pmatrix}\,, \qquad
\widetilde{\bar{\mathbf B}}
=\begin{pmatrix} 1 & 1 & 1 & 0 \\ 
0 & 0 & 0 & \bar b_i 
\end{pmatrix}\,, 
\\
\widetilde{\bar{\mathbf C}}
&=\begin{pmatrix} 0 & 0 & 0 & 0 \\ 
\bar b_1+\bar b_2 & \bar a_2+\bar c_1 & \bar a_1+\bar c_2 & \bar c_i 
\end{pmatrix} \,.
\end{aligned}$$ Use a row operation via $P= \begin{pmatrix} 1 & 0 \\ \bar b_1 + \bar b_2 & \mathbf I \end{pmatrix}$ it follows that $$\begin{aligned}
P \widetilde{\bar{\mathbf A}} 
& = \begin{pmatrix} 0 & 0 & 0  & 0 \\ 
\bar c_1+\bar c_2 & \bar a_1 + \bar b_2 & \bar a_2 + \bar b_1 & \bar a_i 
\end{pmatrix}\,, \qquad
P \widetilde{\bar{\mathbf B}}
=\begin{pmatrix} 1 & 1 & 1 & 0 \\ 
\bar b_1+\bar b_2 & \bar b_1+\bar b_2 & \bar b_1+\bar b_2 & \bar b_i 
\end{pmatrix}\,, 
\\
P \widetilde{\bar{\mathbf C}}
&=\begin{pmatrix} 0 & 0 & 0 & 0 \\ 
\bar b_1+\bar b_2 & \bar a_2+\bar c_1 & \bar a_1+\bar c_2 & \bar c_i 
\end{pmatrix} \,.
\end{aligned}$$ Since $\widetilde{\mathbf A} =\widetilde{ \bar{\mathbf A}} - \widetilde{\bar{\mathbf B}}$ and $\widetilde{\mathbf B} =\widetilde{ \bar{\mathbf C}} -\widetilde{ \bar{\mathbf B}}$, the above combined with Equation [\[eq.a1b1\]](#eq.a1b1){reference-type="eqref" reference="eq.a1b1"} implies that

$$\label{eq.wtAB}
P \widetilde{\mathbf A} = \begin{pmatrix} -1 & -1 & -1  & 0 \\ 
b_1+b_2 & a_1 & a_2 & a_i \end{pmatrix}\,,\qquad P \widetilde{\mathbf B} 
=\begin{pmatrix} -1 & -1 & -1 & 0 \\ 0 & a_2+b_1 & a_1+b_2 & b_i 
\end{pmatrix}\,,$$ Since the 3D index is invariant under row operations (see Remark [\[rem.GLr\]](#rem.GLr){reference-type="ref" reference="rem.GLr"}), Equation [\[eq.wtAB\]](#eq.wtAB){reference-type="eqref" reference="eq.wtAB"} and the pentagon identity [\[eq.pentagon\]](#eq.pentagon){reference-type="eqref" reference="eq.pentagon"} concludes that $I_{\widetilde{\mathcal T}}=I_{\mathcal T}$. 0◻

## Invariance under the $2\to 3$ move {#sub.2-3}

In this section we will define what is a special angle structure on $\mathcal T$, and show the partial invariance of the 3D index under a $2\to 3$ move. We will use the same notation as in Section [0.1](#sub.3-2){reference-type="ref" reference="sub.3-2"}. To define a map $(Z,Z',Z'') \mapsto (\widetilde Z,\widetilde Z',\widetilde Z'')$, we need to solve for $W_i,W_i',W_i''$ for $i=1,2,3$ in terms of $X_i,X_i',X_i''$ for $i=1,2$ using Equations [\[eq.s3\]](#eq.s3){reference-type="eqref" reference="eq.s3"} and [\[eq.s6\]](#eq.s6){reference-type="eqref" reference="eq.s6"}. The answer involves one free variable (say, $W_1$) and it is given by

$$\label{eq.W1free}
\begin{align}
(W_1,W_2,W_3) &=
(W_1,W_1 + X_1 + X_2 + X_2''-1, W_1  + X_1 + X_2 + X_1' -1)
\\
(W_1',W_2',W_3')&=
(X_1 + X_2, X_1'-X_2-X_2''+1,-X_1-X_1'+X_2'+1)
\\
(W_1'',W_2'',W_3'')&= 
(-W_1 + 1 -X_1 -X_2, -W_1 -X_1 -X_1'+1, -W_1-X_2-X_2'+1) 
\end{align}$$ If $(Z,Z',Z'')$ is a strict angle structure on $\mathcal T$, then $(\widetilde Z,\widetilde Z',\widetilde Z'')$ is a strict angle structure if and only if Equations [\[eq.W1free\]](#eq.W1free){reference-type="eqref" reference="eq.W1free"} have a strictly positive solution. It is easy to see that this is equivalent to the following condition $$\label{eq.special.angle}
X_1 + X_2 < 1, \qquad X_1''+X_2' < 1, \qquad X_1'+ X_2'' < 1 \,.$$ These conditions are precisely equivalent to the $W_1', W_2', W_3' <1$, as follows by Equation [\[eq.s3\]](#eq.s3){reference-type="eqref" reference="eq.s3"}. I.e., a special strict angle structure is an angle structure such that all angles of the bipyramid are less than $1$.

::: definition
[]{#def.special.index label="def.special.index"} We will say that $(Z,Z',Z'')$ is a *special strict angle structure* on $\mathcal T$ if the inequality [\[eq.special.angle\]](#eq.special.angle){reference-type="eqref" reference="eq.special.angle"} is satisfied.
:::

Let $\mathrm{A}^{\mathrm{sp}}(\mathcal T)$ denote the set of special strict angle structures on $\mathcal T$. Then, we have a map (more precisely, a section of $\mu_{3 \to 2}$) $$\mu_{2\to 3} \colon \mathrm{A}^{\mathrm{sp}}(\mathcal T) \to A(\widetilde{\mathcal T}),
\qquad
\mu_{2\to 3}(Z,Z',Z'')=(\widetilde Z,\widetilde Z',\widetilde Z'') \,.$$ The conclusion is that if $\mathcal T$ admits a special strict angle structure, then so does $\widetilde{\mathcal T}$. In that case, $I_{\mathcal T}$ and $I_{\widetilde{\mathcal T}}$ both exist. An application of the pentagon identity as in Section [0.1](#sub.3-2){reference-type="ref" reference="sub.3-2"} implies that $I_{\mathcal T}=I_{\widetilde{\mathcal T}}$. 0◻

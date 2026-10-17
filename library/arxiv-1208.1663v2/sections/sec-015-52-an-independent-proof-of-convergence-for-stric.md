---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-015-52-an-independent-proof-of-convergence-for-stric
section_title: "An independent proof of convergence for strict index structures"
section_number: 5.2
pages: 16-21
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.986
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sub.independent.strict label="sub.independent.strict"}

Theorem [\[thm.IMconv\]](#thm.IMconv){reference-type="ref" reference="thm.IMconv"} implies that $I_{\mathbf M}$ converges when $\mathbf M$ admits a strict index structure. In this section we give an independent proof of this fact without using the restriction of the summand of the index to a ray.

::: proposition
[]{#prop.IMconv.strict label="prop.IMconv.strict"} If $\mathbf M$ supports a strict index structure, then $I_{\mathbf M}(m,e)(q) \in \mathbb Z((q^{1/2}))$ is convergent for all $m,e \in \mathbb Z^s$.
:::

The proof of proposition [\[prop.IMconv.strict\]](#prop.IMconv.strict){reference-type="ref" reference="prop.IMconv.strict"} requires some lemmas.

::: lemma
[]{#lem.Iconv label="lem.Iconv"} Fix positive real numbers $\alpha,\beta>0$ with $\alpha+\beta< 1/2$ and let $\gamma= \min\{\alpha,\beta,1/2-\alpha-\beta\}$. Then for all for all integers $m,e$ we have: $$\delta(I_{\Delta}(m,e) q^{-\beta m + \alpha e}) \geq \gamma\max\{|m|,|e|,|m+e|\} 

\,.$$
:::

::: proof
*Proof.* (of Lemma [\[lem.Iconv\]](#lem.Iconv){reference-type="ref" reference="lem.Iconv"}) Let $L_+(m,e)=\max\{|m|,|e|,|m+e|\}$. $L_+(m,e)$ is a piece-wise linear function given by Figure [1](#fig.Lplus){reference-type="ref" reference="fig.Lplus"}.

<figure id="fig.Lplus">
<div class="center">
<embed src="draws/Lplus.pdf" />
</div>
<figcaption>A piece-wise linear function <span class="math inline"><em>L</em><sub>+</sub></span>.</figcaption>
</figure>

With the notation of Lemma [\[lem.degID\]](#lem.degID){reference-type="ref" reference="lem.degID"}, we need to show that $$\label{eq.degDL}
\delta(m,e)-\beta m + \alpha e \geq \gamma L_+(m,e) \,.$$ First, consider the three rays of $\delta(m,e)$:

::: center
         ray         left hand side of [\[eq.degDL\]](#eq.degDL){reference-type="eqref" reference="eq.degDL"}   right hand side of [\[eq.degDL\]](#eq.degDL){reference-type="eqref" reference="eq.degDL"}
  ----------------- ------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------
   $m=0, e \geq 0$                                          $\alpha e$                                                                                 $\gamma e$
   $e=0, m \leq 0$                                          $-\beta m$                                                                                 $-\gamma m$
    $m=-e \geq 0$                                     $m(1/2-\alpha-\beta)$                                                                            $\gamma m$
:::

This proves inequality [\[eq.degDL\]](#eq.degDL){reference-type="eqref" reference="eq.degDL"} in the three rays and shows that the choice of $\gamma$ is optimal. Now, in the interior of each of the $6$ cones of linearity of $L_+$, $\delta(m,e) -\beta m + \alpha e$ is given by a quadratic polynomial of $m,e$. The degree $2$ (resp. $1$) part of this polynomial is always greater than or equal to $1/2 L_+(m,e)$ (resp. $(1/2-\gamma) L_+(m,e)$) by a case computation. For example, in the cone $m \geq 0, e \leq 0, e+m \geq 0$ with rays $\mathbb R_+(1,0)$ and $\mathbb R_+(1,-1)$ we have $\delta(m,e)=m(m+e)/2+m/2$ and $L_+(m,e)=m$ and $$\begin{aligned}
\delta(m,e)-\beta m + \alpha e &=& \frac{m(e+m)}{2}+\frac{m}{2}-\beta m+\alpha e
\\ & \geq & \frac{m}{2} + \frac{m}{2} -\beta m+\alpha e
\\ &= & (1-\beta-\alpha) m + \alpha(m+e) 
\\ & \geq & (1-\beta-\alpha) m \geq (1-\beta-\alpha) L_+(m,e) 
\end{aligned}$$ The other cases are similar. ◻
:::

The next lemma is well-known [@Ziegler].

::: lemma
[]{#lem.Pv label="lem.Pv"} Consider the convex polytope $P$ in $\mathbb R^r$ defined by $$P=\{ x \in \mathbb R^r \, | v_i \cdot x \leq c_i \quad i=1,\dots s \} \,$$ where $v_i \in \mathbb R^r$ and $c_i \in \mathbb R$ for $i=1,\dots,s$. Then $P$ is compact if and only if the linear span of the set $\{v_i| i=1,\dots,s\}$ is $\mathbb R^r$ and $0$ is a $\mathbb R_{\geq 0}$-linear combination of elements of $\{v_i| i=1,\dots,s\}$.
:::

::: proof
*Proof.* (of Proposition [\[prop.IMconv.strict\]](#prop.IMconv.strict){reference-type="ref" reference="prop.IMconv.strict"}) Let $a_i$ and $b_i$ for $i=1,\dots,s$ denote the columns of $(\mathbf A|\mathbf B)$. If $\mathbf M$ admits a strict index structure then there exist $\alpha_i, \gamma_i >0$ that satisfy $a_i + \gamma_i < 1$ for all $i$ such that $$\sum_{i=1}^s \alpha_i a_i + \gamma_i \beta_i = \nu \,.$$ It follows that $$I_{\mathbf M}(m,e)(q)=\sum_{k \in \mathbb Z^r}
\prod_{i=1}^s I(m_i-b_i \cdot k, e_i+a_i \cdot k)(q) 
q^{\frac{\beta_i}{2} b_i \cdot k + \frac{\alpha_i}{2} a_i \cdot k} \,.$$ Applying Lemma [\[lem.Iconv\]](#lem.Iconv){reference-type="ref" reference="lem.Iconv"}, it follows that for every $k \in \mathbb Z^d$, the degree of the summand is bounded below by $$\sum_{i=1}^s \left( \beta_i m_i - \alpha_i e_i \right)
+ \gamma' \sum_{i=1}^s \left( |-m_i+b_i \cdot k| +|e_i+a_i \cdot k| \right)  

\,.$$ Now, Lemma [\[lem.Pv\]](#lem.Pv){reference-type="ref" reference="lem.Pv"} and admissibility implies that for fixed $N_0$, there are finitely many $k \in \mathbb Z^d$ such that the above degree is less than $N_0$. Proposition [\[prop.IMconv.strict\]](#prop.IMconv.strict){reference-type="ref" reference="prop.IMconv.strict"} follows. ◻
:::

# Invariance of the 3D index under $2\leftrightarrow
3$ moves and $2\leftrightarrow 0$ moves {#sec.23}

## Invariance under the $3\to 2$ move {#sub.3-2}

Consider two ideal triangulations $\mathcal T$ and $\widetilde{\mathcal T}$ with $N$ and $N+1$ tetrahedra, respectively, related by a $2-3$ move shown in Figure [2](#fig.23too){reference-type="ref" reference="fig.23too"}.

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

In this section we will define what is a special angle structure on $\mathcal T$, and show the partial invariance of the 3D index under a $2\to 3$ move. We will use the same notation as in Section [1.1](#sub.3-2){reference-type="ref" reference="sub.3-2"}. To define a map $(Z,Z',Z'') \mapsto (\widetilde Z,\widetilde Z',\widetilde Z'')$, we need to solve for $W_i,W_i',W_i''$ for $i=1,2,3$ in terms of $X_i,X_i',X_i''$ for $i=1,2$ using Equations [\[eq.s3\]](#eq.s3){reference-type="eqref" reference="eq.s3"} and [\[eq.s6\]](#eq.s6){reference-type="eqref" reference="eq.s6"}. The answer involves one free variable (say, $W_1$) and it is given by

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
\mu_{2\to 3}(Z,Z',Z'')=(\widetilde Z,\widetilde Z',\widetilde Z'') \,.$$ The conclusion is that if $\mathcal T$ admits a special strict angle structure, then so does $\widetilde{\mathcal T}$. In that case, $I_{\mathcal T}$ and $I_{\widetilde{\mathcal T}}$ both exist. An application of the pentagon identity as in Section [1.1](#sub.3-2){reference-type="ref" reference="sub.3-2"} implies that $I_{\mathcal T}=I_{\widetilde{\mathcal T}}$. 0◻

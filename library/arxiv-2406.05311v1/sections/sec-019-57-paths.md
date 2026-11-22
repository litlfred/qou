---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-019-57-paths
section_title: "Paths"
section_number: 5.7
pages: 27-29
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.859
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
[]{#ss:Paths label="ss:Paths"} We turn our attention to nonzero paths and simply call them paths from now on. Thus a composition ${\mathbf v}={\mathbf v}_{a_r b_r}\dotsb{\mathbf v}_{a_1 b_1}$ is a if it is nonzero, its graph is a path with $a_1$ or $b_1$ an endpoint, and $\#(\{a_i,b_i\}\cap\{a_{i+1},b_{i+1}\})=1$ for all $i$.

::: remark
[]{#rem:yellow label="rem:yellow"} As in Figure [1](#fig:paths){reference-type="ref" reference="fig:paths"}, a yellow (shaded) area in the diagrammatic rendering of operators highlights an open segment that is contained in all quantum operator(s) and no classical operators. Such an operator can be cyclically shifted by powers of $\mathfrak o$ to a classical operator (see Figures [2](#fig:column-vs-classical-row){reference-type="ref" reference="fig:column-vs-classical-row"} and [3](#fig:column-vs-classical-column){reference-type="ref" reference="fig:column-vs-classical-column"}). Theorem [\[thm:quantum_path\]](#thm:quantum_path){reference-type="ref" reference="thm:quantum_path"} shows this is always the case for paths.$\diamond$
:::

<figure id="fig:paths">
<p><span class="math display">$$\begin{gathered}
        \valuediagram[scale=1.25, baseline=2ex]{{1,3},{3,4},{4,5},{5,7}}
        \qquad
        \valuediagram[scale=1.25, baseline=2ex]{{5,7},{4,5},{3,4},{1,3}}
        \label{Eq:classicalRowColumn}
        \\
        \valuediagram[scale=1.25, critical windows={(1,2)}, baseline=2ex]{{2,3}, {3,4}, {4,5}, {5,1}}
        \qquad
        \valuediagram[scale=1.25, critical windows={(4,5)}, baseline=2ex]{{5,1}, {1,2}, {2,3}, {3,4}}
        \qquad
        \valuediagram[scale=1.25, critical windows={(4,5)}, baseline=2ex]{{3,4}, {2,3}, {1,2}, {5,1}}
        \qquad
        \valuediagram[scale=1.25, critical windows={(1,2)}, baseline=2ex]{{5,1}, {4,5}, {3,4}, {2,3}}
        \label{Eq:InitialLemma}
        \\
        \valuediagram[scale=1.25, critical windows={(5,6)}, baseline=4ex]{{6,8},{8,9},{9,10},{10,1},{1,2},{2,3},{3,5}}
        \qquad
        \valuediagram[scale=1.25, critical windows={(3,5)}, baseline=4ex]{{2,3},{1,2},{10,1},{9,10},{7,9},{6,7},{5,6}}
        \label{Eq:quantumRowColumn}
    
\end{gathered}$$</span></p>
<figcaption>Some nonzero paths. Rows are on the left and columns are on the right.</figcaption>
</figure>

A composition ${\mathbf v}= {\mathbf v}_{a_r b_r}\dotsb{\mathbf v}_{a_1 b_1}$ of classical operators is a if $b_{i} = a_{i+1}$ for all $1 \leq i < r$. That is, if $a_1 < a_2 < a_3 < \cdots < a_{r-1} < a_{r} < b_{r}$ so that ${\mathbf v}={\mathbf v}_{a_rb_r}{\mathbf v}_{a_{r-1} a_r}\dotsb{\mathbf v}_{a_1a_2}$. If $u$ is a permutation whose first $r+1$ values are $a_1a_2\dotsc a_rb_r$, then ${\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_1 u\neq{\mathbf 0}$, so ${\mathbf v}\not\equiv{\mathbf 0}$.

A ${\mathbf v}= {\mathbf v}_{a_r b_r}\dotsb{\mathbf v}_{a_1 b_1}$ is a noncrossing composition of connected classical rows. Operators from different connected rows of ${\mathbf v}$ commute, by [\[Eq:monoid-relations\]](#Eq:monoid-relations){reference-type="eqref" reference="Eq:monoid-relations"}(i). By this we mean that commuting them gives an equivalent operator. Thus, replacing ${\mathbf v}$ by an equivalent operator, we may assume that $a_1<\dotsb<a_r$, when ${\mathbf v}$ is a classical row.

A is a composition of operators that can be cyclically shifted to a classical row. See Figure [2](#fig:column-vs-classical-row){reference-type="ref" reference="fig:column-vs-classical-row"}.

<figure id="fig:column-vs-classical-row">
<p><span class="math display">$$\begin{array}{c}
            \valuediagram[scale=1.25, critical windows={(4,5)}]{{5,9},{6,7},{7,8},{9,1},{1,2},{2,3},{3,4}}
        \end{array}
        \xrightarrow{~~\mathfrak o^5~}
        \begin{array}{c}
            \valuediagram[scale=1.25]{{1,5},{2,3},{3,4},{5,6},{6,7},{7,8},{8,9}}
        \end{array}$$</span></p>
<figcaption>The operator on the right is a <em>classical row</em> as it is the product of two noncrossing <em>connected classical rows</em>. The operator on the left is a <em>row</em> as it can be cyclically shifted to the classical row.</figcaption>
</figure>

A connected row is a particular instance of a path.

Similarly, a composition ${\mathbf v}= {\mathbf v}_{a_r b_r}\dotsb{\mathbf v}_{a_1 b_1}$ of classical operators is a if $b_{i} = a_{i-1}$ for all $1 < i \leq l$. That is, if $a_r < a_{r-1} < \cdots < a_2 < a_1 < b_1$ so that ${\mathbf v}={\mathbf v}_{a_ra_{r-1}}\dotsb{\mathbf v}_{a_2a_1}{\mathbf v}_{a_1b_1}$. If $u$ is a permutation whose first $r+1$ values are $a_ra_{r-1}\dotsc a_1b_1$, then ${\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_r u\neq{\mathbf 0}$, so ${\mathbf v}\not\equiv{\mathbf 0}$.

A ${\mathbf v}$ is a noncrossing composition of connected classical columns. As with rows, replacing ${\mathbf v}$ by an equivalent operator, we may assume that $a_1>\dotsb>a_r$. A is a composition that can be cyclically shifted to a classical column as in Figure [3](#fig:column-vs-classical-column){reference-type="ref" reference="fig:column-vs-classical-column"}. A connected column is an instance of a path. Note that if ${\mathbf v}$ is a column, then $\rho({\mathbf v})$ is a row.

<figure id="fig:column-vs-classical-column">
<p><span class="math display">$$\begin{array}{c}
            \valuediagram[scale=1.25, critical windows={(6,7)}]{{2,3},{1,2},{9,1},{8,9},{5,6},{4,5},{7,4}}
        \end{array}
        \xrightarrow{~~\mathfrak o^3~}
        \begin{array}{c}
            \valuediagram[scale=1.25]{{5,6},{4,5},{3,4},{2,3},{8,9},{7,8},{1,7}}
        \end{array}
        \equiv
        \begin{array}{c}
            \valuediagram[scale=1.25]{{8,9},{7,8},{5,6},{4,5},{3,4},{2,3},{1,7}}
        \end{array}$$</span></p>
<figcaption>The operator on the right is a <em>classical column</em> as it is the product of two noncrossing <em>connected classical columns</em>. The operator on the left is a <em>column</em> as it can be cyclically shifted to the classical column.</figcaption>
</figure>

::: theorem
[]{#thm:quantum_path label="thm:quantum_path"} Every path is either a row or a column and a path contains at most one quantum operator. Paths can be cyclically shifted to a classical row or to a classical column. The only path that can be shifted to both consists of a single operator.
:::

::: proof
*Proof.* We split the proof into four parts. Let ${\mathbf v}$ be a path, which is nonzero.

*(1) Paths consisting only of classical operators.* Suppose the path ${\mathbf v}= {\mathbf v}_{a_r b_r}\dotsb{\mathbf v}_{a_1 b_1}$ is a composition of classical operators (for all $i$, $a_i<b_i$). Then every pair of adjacent compositions ${\mathbf v}_{a_{i+1},b_{i+1}}{\mathbf v}_{a_i,b_i}$ is nonzero. Suppose that $a_1$ is an endpoint. As ${\mathbf v}\not\equiv{\mathbf 0}$, the relations [\[Eq:monoid-relations\]](#Eq:monoid-relations){reference-type="eqref" reference="Eq:monoid-relations"}(*ii*) imply that $a_{i+1}=b_i$ for all $i$. Similarly, if $b_1$ is an endpoint, then we must have $a_i=b_{i+1}$ for all $i$. Thus, ${\mathbf v}$ is either a connected classical row or a connected classical column. If ${\mathbf v}= {\mathbf v}_{a_r b_r}\dotsb{\mathbf v}_{a_1 b_1}$ with for example, $a_i<b_i$ and $a_{i+1}=b_i$ for all $i$, then we showed that ${\mathbf v}\not\equiv {\mathbf 0}$, and so ${\mathbf v}$ is a connected classical row. If instead $a_i=b_{i+1}$, then applying $\rho$ or $w_0$ shows that ${\mathbf v}$ is a connected classical column. Such paths are shown in [\[Eq:classicalRowColumn\]](#Eq:classicalRowColumn){reference-type="eqref" reference="Eq:classicalRowColumn"} in Figure [1](#fig:paths){reference-type="ref" reference="fig:paths"}.

*(2) Composition of a connected classical column/row with a quantum operator.* Suppose that the path ${\mathbf v}={\mathbf v}_{a_ra_{r-1}} \dotsb {\mathbf v}_{a_2 a_1}{\mathbf v}_{a_1b} \cdot {\color{BrickRed}{\mathbf v}_{ba}}$ is a composition of a connected classical column with single quantum operator ${\color{BrickRed}{\mathbf v}_{ba}}$. Then $a_r<a_{r-1}<\dotsb<a_2<a_1<b$, $a<b$, and $a\not\in\{a_r,\dotsc,a_2,a_1\}$. By Corollary [\[T\*vq=0\]](#T*vq=0){reference-type="ref" reference="T*vq=0"}, we must have $a < a_r < \dotsb < a_1 < b$. Such a path is illustrated in [\[Eq:InitialLemma\]](#Eq:InitialLemma){reference-type="eqref" reference="Eq:InitialLemma"} on the right in Figure [1](#fig:paths){reference-type="ref" reference="fig:paths"}.

Applying $\mathfrak o^{n{+}1{-}a_r}$ to ${\mathbf v}$ cyclically shifts it to a classical column. We illustrate this.

$$\valuediagram[scale=1., critical windows={(1,2)}]{{5,1}, {4,5}, {3,4}, {2,3}}
    \ \raisebox{5pt}{$\xrightarrow{\;\mathfrak o\;}$}\
     \valuediagram[scale=1., critical windows={(2,3)}]{{1,2}, {5,1}, {4,5}, {3,4}}
    \ \raisebox{5pt}{$\xrightarrow{\;\mathfrak o\;}$}\
     \valuediagram[scale=1., critical windows={(3,4)}]{{2,3}, {1,2}, {5,1}, {4,5}}
    \ \raisebox{5pt}{$\xrightarrow{\;\mathfrak o\;}$}\
     \valuediagram[scale=1., critical windows={(4,5)}]{{3,4}, {2,3}, {1,2}, {5,1}}
    \ \raisebox{5pt}{$\xrightarrow{\;\mathfrak o\;}$}\
     \valuediagram[scale=1.]{{4,5}, {3,4}, {2,3}, {1,2}}$$

If instead ${\mathbf v}={\mathbf v}_{a_ra_{r-1}} \dotsb {\mathbf v}_{a_2 a_1}{\mathbf v}_{a_1b} \cdot {\color{BrickRed}{\mathbf v}_{ba}}$ is the composition of a classical connected row and a quantum operator ${\color{BrickRed}{\mathbf v}_{ba}}$, then we may apply $w_0$ to convert it to the composition of a connected classical column and a quantum operator. As $w_0\mathfrak o=\mathfrak o^{n-1}w_0$, arguments for a column imply this for rows.

*(3) Paths may contain at most one quantum operator.* Suppose that ${\mathbf v}$ contains at least two quantum operators. By Figures  [\[fig:more-degree-2-zero-relations\]](#fig:more-degree-2-zero-relations){reference-type="ref" reference="fig:more-degree-2-zero-relations"} and [\[fig:touching-orbit\]](#fig:touching-orbit){reference-type="ref" reference="fig:touching-orbit"}, no two quantum operators are adjacent. Restrict ${\mathbf v}$ to two of its quantum operators and the classical operators between them. This segment remains a nonzero path. Applying $w_0$ if necessary, we may assume that the classical segment is a column, so that ${\mathbf v}$ has the form

$${\mathbf v}\ =\ {\color{BrickRed}{\mathbf v}_{b a_r}}\,{\mathbf v}_{a_r a_{r-1}}\dotsb {\mathbf v}_{a_2 a_1}\, {\color{BrickRed}{\mathbf v}_{a_1 c}} \,,\quad\mbox{where }\
    a_r<b\,, \ a_r<\dotsb<a_2<a_1\,,\ \mbox{ and }c<a_1 \,.$$

Applying Part *(2)* to the segment omitting ${\mathbf v}_{b a_r}$ shows that $c<a_r$. Applying $\rho$ and then $\omega_0$ to the segment omitting ${\mathbf v}_{a_1 c}$, Part *(2)* shows that $a_1<b$. Applying $\mathfrak o^{n+1-b}$ to ${\mathbf v}$ gives: $$\mathfrak o^{n+1-b}{\mathbf v}\ =\ {\mathbf v}_{\alpha_r 1}\,{\mathbf v}_{\alpha_r \alpha_{l-1}}\dotsb
   {\mathbf v}_{\alpha_2 \alpha_1}\, {\color{BrickRed}{\mathbf v}_{\alpha_1,\gamma}}\,,\quad\mbox{where }\
    1<\gamma<\alpha_r<\dotsb<\alpha_2<\alpha_1 \,.$$ $$\valuediagram[scale=1.25, xmin=1, xmax=9]
   {{6,2}, {5,6},{4,5},{3,4}, {8,3}}
   \quad \raisebox{10pt}{$\xrightarrow{\ \mathfrak o^{n+1-b}\ }$} \quad
   \valuediagram[scale=1.25, xmin=1, xmax=9]{{8,4}, {7,8},{6,7},{5,6}, {1,5}}$$ As $1<\gamma<\alpha_r$, this is zero by Corollary [\[T\*vq=0\]](#T*vq=0){reference-type="ref" reference="T*vq=0"} and Part *(2)*, thus ${\mathbf v}$ cannot contain two quantum operators.

*(4) Paths containing a single quantum operator.* Let ${\mathbf v}$ be a path containing a single quantum operator ${\mathbf v}_{ba}$ ($a<b$). Arguing as above, we may suppose ${\mathbf v}$ that takes the form $${\mathbf v}=
    {\mathbf v}_{b_m b_{m-1}} \cdots {\mathbf v}_{b_2 b_1} {\mathbf v}_{b_1 b}
    \, {\color{BrickRed}{\mathbf v}_{ba}}\, 
    {\mathbf v}_{a a_{l}} {\mathbf v}_{a_l a_{l-1}} \dotsb{\mathbf v}_{a_2 a_1}$$ with $a < a_l < \dotsb < a_{2} < a_1$ and $b_{m} < \cdots < b_{1} < b$. If $a_1<b_m$, then applying $\mathfrak o^{n{+}1{-}b_m}$ to ${\mathbf v}$ cyclically shifts it to a classical column, which completes the proof in this case. This is illustrated on the right in [\[Eq:quantumRowColumn\]](#Eq:quantumRowColumn){reference-type="eqref" reference="Eq:quantumRowColumn"} in Figure [1](#fig:paths){reference-type="ref" reference="fig:paths"}.

Suppose that $b_{m}\leq a_1$. Since the graph of ${\mathbf v}$ is a path, $b_{m}\not\in\{a_1,\dotsc,a_r\}$. We have $a<b_{m}$ by Part *(2)*, so there is some $i$ with $a_{i+1}<b_{m}<a_i$ (if $i=l$, then $a=a_{l+1}$). Then the cyclic shift $\mathfrak o^{n-b_{m}}{\mathbf v}$ is a path with two quantum operators coming from the shifts of ${\mathbf v}_{a_{i+1} a_i}$ and ${\mathbf v}_{b_m b_{m-1}}$, as illustrated by $$\valuediagram[baseline=2ex]  {{3,5},{2,3},{1,2}, {7,1}, {6,7},{4,6}}
   \xrightarrow{\;\mathfrak o\;}
  \valuediagram[baseline=2ex]  {{4,6},{3,4},{2,3},{1,2}, {7,1}, {5,7}}
   \xrightarrow{\;\mathfrak o\;}
  \valuediagram[baseline=2ex]  {{5,7},{4,5},{3,4},{2,3},{1,2},  {6,1}}
   \xrightarrow{\;\mathfrak o\;}
  \valuediagram[baseline=2ex]  {{6,1}, {5,6},{4,5},{3,4},{2,3}, {7,2}}\ .$$ But this is a contradiction, as a nonzero path has at most two quantum operators. ◻
:::

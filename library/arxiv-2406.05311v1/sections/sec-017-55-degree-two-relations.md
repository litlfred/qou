---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-017-55-degree-two-relations
section_title: "Degree two relations"
section_number: 5.5
pages: 23-26
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.9
latex_coverage_ratio: 0.823
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
[]{#S:degreeTwo label="S:degreeTwo"}

Given a composition ${\mathbf v}$ involving quantum operators, in Section [\[SS:monoid\]](#SS:monoid){reference-type="ref" reference="SS:monoid"} we developed the notions of equivalence to zero (${\mathbf v}\equiv{\mathbf 0}$), of ${\mathbf v}$ being nonzero (${\mathbf v}\not\equiv{\mathbf 0}$), and the notion of $(u,k)$-equivalence for nonzero compositions ${\mathbf v}$. We do not however have a notion of equivalence of operators similar to the stronger one of [@BS-Monoid] for classical operators.

By Theorem [\[Th:shape-equivalence\]](#Th:shape-equivalence){reference-type="ref" reference="Th:shape-equivalence"}, a composition ${\mathbf v}$ being equivalent to ${\mathbf 0}$ only depends upon its shape-equivalence class. Furthermore, if ${\mathbf v}$ is minimal and ${\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u=q^\alpha w$, then $(u,k)$-equivalence to ${\mathbf v}$ only depends on shape-equivalence (and not specifically on $u$ or $k$). Consequently, we will simply write $\equiv$ for equivalence to ${\mathbf 0}$ and $(u,k)$-equivalence of minimal compositions.

A composition ${\mathbf v}_{ab}{\mathbf v}_{cd}$ is minimal when $\{a,b\}\neq\{c,d\}$. We identify all relations among minimal compositions that preserve equivalence. These relations are depicted in Figures [1](#fig:crossing-operators){reference-type="ref" reference="fig:crossing-operators"},  [2](#fig:degree-2-nonzero-relations){reference-type="ref" reference="fig:degree-2-nonzero-relations"},  [3](#fig:more-degree-2-zero-relations){reference-type="ref" reference="fig:more-degree-2-zero-relations"}, and  [4](#fig:touching-orbit){reference-type="ref" reference="fig:touching-orbit"}. This uses the notion of crossing and noncrossing sets from Section [\[sec:classic-mn-rule\]](#sec:classic-mn-rule){reference-type="ref" reference="sec:classic-mn-rule"}.

::: lemma
[]{#Lem:Rel label="Lem:Rel"} The following describe all relations among minimal compositions of two left operators; those not of the form ${\mathbf v}_{ab} {\mathbf v}_{ba}$ or ${\mathbf v}_{ab} {\mathbf v}_{ab}$.

1.  If $\{a,b\}\cap\{c,d\}=\emptyset$, then the operators commute, ${{\mathbf v}}_{ab}{{\mathbf v}}_{cd} \equiv {{\mathbf v}}_{cd}{{\mathbf v}}_{ab}$.

    1.  []{#Rel:1:i label="Rel:1:i"} If $\{a,b\}$ and $\{c,d\}$ are crossing, then ${\mathbf v}_{ab}{\mathbf v}_{cd}  \equiv {\mathbf 0}$.

    2.  []{#Rel:1:ii label="Rel:1:ii"} If $a<d<c<b$ or $a>b>c>d$, then ${\mathbf v}_{cd}{\mathbf v}_{ab}$ and ${\mathbf v}_{ab}{\mathbf v}_{cd}$ are both zero, $$\valuediagram[scale=1.1]{{1,4},{3,2}}\equiv
                     \valuediagram[scale=1.1]{{2,1},{4,3}}\equiv
                     \valuediagram[scale=1.1]{{3,2},{1,4}}\equiv
                     \valuediagram[scale=1.1]{{4,3},{2,1}}\equiv {\mathbf 0}\,.$$

    3.  []{#Rel:1:iii label="Rel:1:iii"} In all other cases when $\{a,b\}$ and $\{c,d\}$ are noncrossing, ${\mathbf v}_{ab}{\mathbf v}_{cd}\equiv{\mathbf v}_{cd}{\mathbf v}_{ab}$, and both are nonzero.

2.  If $\#(\{a,b\}\cap\{c,d\})=1$, then the operators ${\mathbf v}_{ab}$ and ${\mathbf v}_{cd}$ do not commute.

    1.  []{#Rel:2:i label="Rel:2:i"} For $a<b<c$, each of the six compositions, ${\mathbf v}_{ba}{\mathbf v}_{ac}$, ${\mathbf v}_{cb}{\mathbf v}_{ba}$, ${\mathbf v}_{ac}{\mathbf v}_{cb}$, ${\mathbf v}_{ac}{\mathbf v}_{ba}$, ${\mathbf v}_{ba}{\mathbf v}_{cb}$, and ${\mathbf v}_{cb}{\mathbf v}_{ac}$ is equivalent to ${\mathbf 0}$.

    2.  []{#Rel:2:ii label="Rel:2:ii"} For any distinct $a,b,c$, both ${\mathbf v}_{ab}{\mathbf v}_{ac}$ and ${\mathbf v}_{ba}{\mathbf v}_{ca}$ are equivalent to ${\mathbf 0}$.

    3.  []{#Rel:2:iii label="Rel:2:iii"} The six remaining compositions with $\#(\{a,b\}\cap\{c,d\})=1$ are nonzero and pairwise inequivalent, and are depicted in Figure [5](#fig:nonzero-touching-operators){reference-type="ref" reference="fig:nonzero-touching-operators"}.
:::

::: remark
The composition ${\mathbf v}_{ab}{\mathbf v}_{ab}$ is zero. When $a<b$, this is by [\[Eq:monoid-relations\]](#Eq:monoid-relations){reference-type="eqref" reference="Eq:monoid-relations"}(*ii*). The case $a>b$ follows from this by cyclic shift (applying $\mathfrak o$) and Corollary [\[C:symmetries_bzero\]](#C:symmetries_bzero){reference-type="ref" reference="C:symmetries_bzero"}.

The composition ${\mathbf v}_{ab}{\mathbf v}_{ba}$ is nonzero and ${\mathbf v}_{ab}{\mathbf v}_{ba}\not\equiv {\mathbf v}_{ba}{\mathbf v}_{ab}$. If $a<b$, then ${\mathbf v}_{ab}{\mathbf v}_{ba}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u$ equals $q_k u$ if $u(k)=b$ and $u(k{+}1)=a$ and is ${\mathbf 0}$ otherwise. If $a>b$, then ${\mathbf v}_{ab}{\mathbf v}_{ba}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u$ equals $q_k u$ if $u(k)=a$ and $u(k{+}1)=b$ and is ${\mathbf 0}$ otherwise.$\diamond$
:::

::: proof
*Proof of Lemma [\[Lem:Rel\]](#Lem:Rel){reference-type="ref" reference="Lem:Rel"}.* Consider compositions ${\mathbf v}_{ab}{\mathbf v}_{cd}$ with $\{a,b\}\cap\{c,d\}=\emptyset$. Then $\{a,b\}$ and $\{c,d\}$ form an ordered partition of the four-element set $\{a,b,c,d\}$. There are $6=\binom{4}{2}$ such. Each operator may be either quantum or classical, there are 24 choices in all.

For (1)[\[Rel:1:i\]](#Rel:1:i){reference-type="ref" reference="Rel:1:i"}, the eight compositions ${\mathbf v}_{ab}{\mathbf v}_{cd}$ with $\{a,b\}$ and $\{c,d\}$ crossing are shown in Figure [1](#fig:crossing-operators){reference-type="ref" reference="fig:crossing-operators"}.

<figure id="fig:crossing-operators">
<p><span class="math display">$$\begin{array}{l@{\hskip1.25em}l@{\hskip1.25em}l@{\hskip1.25em}l}
        \valuediagram[scale=1.7]{{1,3},{2,4}} &amp; \valuediagram[scale=1.7]{{2,4},{3,1}}
      &amp; \valuediagram[scale=1.7]{{3,1},{4,2}} &amp; \valuediagram[scale=1.7]{{4,2},{1,3}}
            \\[10pt]
        \valuediagram[scale=1.7]{{2,4},{1,3}} &amp; \valuediagram[scale=1.7]{{3,1},{2,4}}
      &amp; \valuediagram[scale=1.7]{{4,2},{3,1}} &amp; \valuediagram[scale=1.7]{{1,3},{4,2}}
    \end{array}$$</span></p>
<figcaption>Crossing compositions of (1)(i). They all are equivalent to <span class="math inline"><strong>0</strong></span>.</figcaption>
</figure>

They form a single orbit under the joint action of $\mathfrak o$ and $\rho$. Both classical compositions (in the first column) are zero by [\[Eq:monoid-relations\]](#Eq:monoid-relations){reference-type="eqref" reference="Eq:monoid-relations"}(*ii*). Lemma [\[lemma:actions\]](#lemma:actions){reference-type="ref" reference="lemma:actions"} implies the rest are zero.

The four compositions in (1)[\[Rel:1:ii\]](#Rel:1:ii){reference-type="ref" reference="Rel:1:ii"} form a single orbit under $\mathfrak o$ by Lemma [\[lemma:actions\]](#lemma:actions){reference-type="ref" reference="lemma:actions"}, and it suffices to show that one is equivalent to ${\mathbf 0}$. As in Section [\[cohomology-ring-of-the-flag-manifold\]](#cohomology-ring-of-the-flag-manifold){reference-type="ref" reference="cohomology-ring-of-the-flag-manifold"}, write permutations in one-line notation, placing " $\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}$ " just after the $k$th position. Thus $52\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}6134\in S_6$ has $k=2$, and $(\dotsc a\dotsc \raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}b \dotsc)$ is a permutation $w$ with $w^{-1}(a)\leq k$ and $w(k{+}1)=b$.

Let $a<b<c<d$ be the values involved in the first composition in (1)(ii) of operators, $\valuediagram{{1,4},{3,2}}={\mathbf v}_{cb}{\mathbf v}_{ad}$, and suppose that $u\in S_n$ is such that ${\mathbf v}_{cb} {\mathbf v}_{ad}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u\neq{\mathbf 0}$. Then $u\lessdot_k (a,d)u$, and writing $v \vcentcolon= (a,d)u$, we have that $v$ has the form $(\dotsc d\dotsc \raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}\dotsc a \dotsc)$, with neither $b$ nor $c$ appearing between $d$ and $a$. Since ${\mathbf v}_{cb}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}v\neq{\mathbf 0}$, not only must $c$ be left of $\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}$ and $b$ right of $\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}$, but every value $e$ of $v$ at a position between those of $c$ and $b$ satisfies $b<e<c$. But this forces $c$ and $b$ to lie between $a$ and $d$ in $v$, a contradiction. Thus ${\mathbf v}_{cb} {\mathbf v}_{ad}\equiv{\mathbf 0}$.

Consider the remaining twelve $=24-8-4$ noncrossing compositions ${\mathbf v}_{ab}{\mathbf v}_{cd}$ in (1). If $a<b$ and $c<d$, so that the operators are classical, then by [\[Eq:monoid-relations\]](#Eq:monoid-relations){reference-type="eqref" reference="Eq:monoid-relations"}(*i*), they are nonzero and ${\mathbf v}_{ab}{\mathbf v}_{cd}\equiv{\mathbf v}_{cd}{\mathbf v}_{ab}$. These are on the left of the two top rows in Figure [2](#fig:degree-2-nonzero-relations){reference-type="ref" reference="fig:degree-2-nonzero-relations"}.

<figure id="fig:degree-2-nonzero-relations">
<p><span class="math display">$$\begin{array}{r@{\hskip5pt}c@{\hskip5pt}l@{\hskip3em}r@{\hskip5pt}c@{\hskip5pt}l}
      \valuediagram[scale=1.7]{{1,2},{3,4}} &amp; \raisebox{3pt}{$\equiv$} &amp; \valuediagram[scale=1.7]{{3,4},{1,2}} &amp;
      \valuediagram[scale=1.7]{{2,3},{4,1}} &amp; \raisebox{3pt}{$\equiv$} &amp; \valuediagram[scale=1.7]{{4,1},{2,3}}
      \\[3ex]
      \valuediagram[scale=1.7]{{1,4},{2,3}} &amp; \raisebox{3pt}{$\equiv$} &amp; \valuediagram[scale=1.7]{{2,3},{1,4}} &amp;
      \valuediagram[scale=1.7]{{2,1},{3,4}} &amp; \raisebox{3pt}{$\equiv$} &amp; \valuediagram[scale=1.7]{{3,4},{2,1}}
      \\[2ex]
      \valuediagram[scale=1.7]{{3,2},{4,1}} &amp; \raisebox{3pt}{$\equiv$} &amp; \valuediagram[scale=1.7]{{4,1},{3,2}} &amp;
      \valuediagram[scale=1.7]{{4,3},{1,2}} &amp; \raisebox{3pt}{$\equiv$} &amp; \valuediagram[scale=1.7]{{1,2},{4,3}}
   \end{array}$$</span></p>
<figcaption>Relations of Lemma <a href="#Lem:Rel" data-reference-type="ref" data-reference="Lem:Rel">[Lem:Rel]</a>(1)(iii).</figcaption>
</figure>

The two relations in the first row are mapped to each other by $\mathfrak o$, the four in the remaining rows form an orbit under $\mathfrak o$. As equivalence is preserved by $\mathfrak o$, this establishes (1)(iii).

For (2), there are 24 possibilities for ${\mathbf v}_{ab}{\mathbf v}_{cd}$: As $\#\{a,b,c,d\}=3$, the indices $\{a,b\}$ and $\{c,d\}$ are an ordered choice of two of the three subsets of $\{a,b,c,d\}$ of cardinality two. In each of these six, either operator may be quantum or classical, giving 24 choices in all. Note thay they do not commute as $(a,b)(c,d)\neq(c,d)(a,b)$ when $\#(\{a,b\}\cap\{c,d\})=1$.

Figure [3](#fig:more-degree-2-zero-relations){reference-type="ref" reference="fig:more-degree-2-zero-relations"} shows the six compositions in (2)(i).

<figure id="fig:more-degree-2-zero-relations">
<p><span class="math display">$$\valuediagram[scale=1.7]{{1,3},{2,1}}\quad
     \valuediagram[scale=1.7]{{2,1},{3,2}}\quad
     \valuediagram[scale=1.7]{{3,2},{1,3}}\qquad

     \valuediagram[scale=1.7]{{2,1},{1,3}}\quad
     \valuediagram[scale=1.7]{{3,2},{2,1}}\quad
     \valuediagram[scale=1.7]{{1,3},{3,2}}$$</span></p>
<figcaption>The six compositions in (2)(i) are all equivalent to <span class="math inline"><strong>0</strong></span>.</figcaption>
</figure>

They form an orbit under the joint action of $\mathfrak o$ and $\rho$. Consider the leftmost operator in Figure [3](#fig:more-degree-2-zero-relations){reference-type="ref" reference="fig:more-degree-2-zero-relations"}. Writing $a<b<c$ for its support, let $u\in S_n$ be such that ${\mathbf v}_{ac}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u\neq{\mathbf 0}$. Then $u\lessdot_k {\mathbf v}_{ac}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u=(a,c)u=\vcentcolon v$, so that $v=(\dotsc c\dotsc \raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}\dotsc a \dotsc)$, and $b$ is not between $a$ and $c$ in $v$. Since ${\mathbf v}_{ba}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}v\neq{\mathbf 0}$, $b$ must be left of $\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}$ and hence left of $c$. But then $c$ lies between $b$ and $a$, so that ${\mathbf v}_{ba}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}v ={\mathbf 0}$. Hence ${\mathbf v}_{ba}{\mathbf v}_{ac}={\mathbf 0}$.

The twelve compositions of (2)(ii) are shown in Figure [4](#fig:touching-orbit){reference-type="ref" reference="fig:touching-orbit"}.

<figure id="fig:touching-orbit">
<p><span class="math display">$$\begin{array}{ccccccc}
    \valuediagram[scale=1.7]{{1,3},{1,2}}&amp;
    \valuediagram[scale=1.7]{{2,1},{2,3}}&amp;
    \valuediagram[scale=1.7]{{3,2},{3,1}}&amp;&amp;
    \valuediagram[scale=1.7]{{1,2},{1,3}}&amp;
    \valuediagram[scale=1.7]{{2,3},{2,1}}&amp;
    \valuediagram[scale=1.7]{{3,1},{3,2}}\\[1ex]
    \valuediagram[scale=1.7]{{1,3},{2,3}}&amp;
    \valuediagram[scale=1.7]{{2,1},{3,1}}&amp;
    \valuediagram[scale=1.7]{{3,2},{1,2}}&amp;&amp;
    \valuediagram[scale=1.7]{{2,3},{1,3}}&amp;
    \valuediagram[scale=1.7]{{3,1},{2,1}}&amp;
    \valuediagram[scale=1.7]{{1,2},{3,2}}
  \end{array}$$</span></p>
<figcaption>The twelve compositions of (2)(ii) are all equivalent to <span class="math inline"><strong>0</strong></span>.</figcaption>
</figure>

They form a single orbit under the joint action of $\mathfrak o$, $w_0$, and $\rho$. As the classical compositions (first and fourth in each row) among them are zero by [\[Eq:monoid-relations\]](#Eq:monoid-relations){reference-type="eqref" reference="Eq:monoid-relations"}(*ii*), all twelve are zero by Lemma [\[lemma:actions\]](#lemma:actions){reference-type="ref" reference="lemma:actions"}.

The six remaining compositions in (2)(iii) are shown in Figure [5](#fig:nonzero-touching-operators){reference-type="ref" reference="fig:nonzero-touching-operators"}.

<figure id="fig:nonzero-touching-operators">

<figcaption>Remaining compositions of two operators.</figcaption>
</figure>

They form a single orbit under the joint action of $\mathfrak o$ and $\rho$. It suffices to show that one is nonzero and inequivalent to any of the others. To that end, note that ${\mathbf v}_{23} {\mathbf v}_{12}\mathop{\mathrm{{\scriptstyle \bullet}}}_1 1\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}23 = 3\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}12$. This represents the first composition in Figure [5](#fig:nonzero-touching-operators){reference-type="ref" reference="fig:nonzero-touching-operators"}. As ${\mathbf v}_{23}\mathop{\mathrm{{\scriptstyle \bullet}}}_2 1\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}23 = {\mathbf 0}$, ${\mathbf v}_{23} {\mathbf v}_{12}\not\equiv {\mathbf v}_{12}{\mathbf v}_{23}$, so the first and fourth are inequivalent. A composition of classical operators cannot be equivalent to a composition involving quantum operators, which completes the proof. ◻
:::

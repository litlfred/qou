---
doc_id: arxiv-0804.0917v1
doc_title: "Composition-Diamond Lemma for Modules ∗"
section_id: sec-002-composition-diamond-lemma-for-double-free-module
section_title: "Composition-Diamond lemma for ``double-free' modules"
section_number: null
pages: 4-7
source_pdf: 0804.0917v1.pdf
source_sha256: 887fbd8be47a2781
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.886
doc_brief: "Czechoslovak Mathematical Journal — 19 sections: Page 1; Page 2; Page 3"
duplicate_of: "czechmathj-60-2010-1-4"
---
Let $X,Y$ be sets and $mod_{k\langle X\rangle} \langle Y\rangle$ a free left $k\langle X\rangle$-module with the basis $Y$. Then $mod_{k\langle X\rangle} \langle Y\rangle=\oplus_{y\in Y} k\langle
X\rangle y$ is called a "double-free\" module.

We now define Gröbner-Shirshov basis in $mod_{k\langle
X\rangle} \langle Y\rangle$.

Suppose that $<$ is a monomial order on $X^*$, $<$ a well order on $Y$ and $X^*Y=\{uy|u\in X^*, \ y\in Y\}$. We define an order $``\prec"$ on $X^*Y$: for any $w_1=u_1y_1,w_2=u_2y_2\in X^*Y$, $$w_1\prec w_2\Leftrightarrow u_1<u_2 \ \ \mbox{ or } u_1=u_2, y_1<y_2
\ \ \ \  \ \  \  \ \ \  \ \  \  \ \ \ \  \ \  \  \ \ \  \ \  \  \ \
\ (*)$$ It is clear that the order $``\prec "$ is left compatible in the sense of $$w\prec w'\Rightarrow aw \prec aw' \ \mbox{ for any  } a\in X^*.$$

Let $S\subset
mod_{k\langle X\rangle} \langle Y\rangle$ with each $s\in S$ monic. We define the composition in $S$ only the inclusion composition which means $w=\bar{f}=a\bar{g}$, where $f,g\in S$.

If $(f,g)_w=f-ag=\sum \alpha_i a_i s_i$, where $\alpha_i\in k, \ a_i
\in X^*, \ s_i \in S$ and $a_i \overline{s}_i\prec w$, then this composition is called trivial modulo $(S,w)$ and denote it by $$(f,g)_w\equiv 0 \ mod(S,w).$$

::: definition
[]{#d3 label="d3"}([@ch]) Let $S\subset mod_{k\langle X\rangle} \langle Y\rangle$ be a non-empty set with each $s\in S$ monic. Let the order "$\prec$\" be as before. Then we call $S$ a Gröbner-Shirshov basis in the module $mod_{k\langle X\rangle} \langle Y\rangle$ if all the compositions in $S$ are trivial modulo $S$.
:::

The proof of the following lemma is essentially from [@ch]. For convenience, we give the detail.

::: lemma
[]{#l3.5 label="l3.5"} ([@ch], Composition-Diamond lemma for "double-free\" modules)[]{#l2 label="l2"} Let $S\subset mod_{k\langle X\rangle} \langle
Y\rangle$ be a non-empty set with each $s\in S$ monic and $``\prec"$ the order on $X^*Y$ as before. Then the following statements are equivalent:

1.   $S$ is a Gröbner-Shirshov basis in $mod_{k\langle X\rangle} \langle Y\rangle$.

2.   If  $0\neq
    f\in k\langle X\rangle S$, then $\overline{f}=a\overline{s}$ for some $a\in X^*, \ s\in S$.

3.   If  $0\neq f\in k\langle
    X\rangle S$, then $f=\sum \alpha_i a_i s_i$ with $a_1
    \overline{s}_1\succ a_2 \overline{s}_2\succ\cdots$, where each $\alpha_i\in k, \ a_i\in X^*, \ s_i\in S$.

4.   $Red(S)=\{w \in X^*Y|w\neq a\overline{s}, \ a\in X^*, \ s\in S\}$ is a $k$-linear basis for the factor $mod_{k\langle X\rangle} \langle
    Y|S\rangle=mod_{k\langle X\rangle} \langle Y\rangle /k\langle
    X\rangle S$.
:::

**Proof:** $(1)\Rightarrow (2)$. Suppose that $0\neq f\in
k\langle X\rangle S$. Then $f=\sum \alpha_i a_i s_i$ for some $\alpha_i\in k, \ a_i\in X^*, \ s_i\in S$. Let $w_i=a_i
\overline{s}_i$ and $w_1=w_2=\cdots=w_l\succ w_{l+1}\succeq \cdots$. We will prove that $\overline{f}=a\overline{s}$ for some $a\in X^*,
\ s\in S$, by using induction on $l$ and $w_1$. If $l=1$, then the result is clear. If $l>1$, then $a_1 \overline{s}_1=a_2
\overline{s}_2$. Thus, we may assume that $a_1=a_2 a, \
\overline{s}_2=a\overline{s}_1$ for some $a\in X^*$. Now, by (1), $$a_1 s_1-a_2 s_2=a_2 as_1-a_2 s_2=a_2(as_1-s_2)=a_2\sum \beta_j b_j
u_j=\sum \beta_j a_2b_j u_j,$$ where $\beta_j\in k, \ b_j\in X^*, \ u_j\in S$ and $b_j
\overline{u}_j\prec\overline{s}_2$. Therefore, $a_2 b_j
\overline{u}_j\prec w_1$. Now, by induction on $l$ and $w_1$, we have the result.

It is clear that $(2)$ is equivalent to $(2')$.

$(2)\Rightarrow (3)$. For any $0\neq f\in mod_{k\langle X\rangle}
\langle Y\rangle$, if $\bar{f}=u_1\in Red(S)$, then $f=\beta_1
u_1+\cdots$. If $\bar{f}\not\in Red(S)$, then $f=\alpha_1 a_1
s_1+\cdots$. It follows that we can express $f$ as $$f=\sum \alpha_i a_i s_i+\sum \beta_j u_j,$$ where $\alpha_i, \ \beta_j \in k, \ a_i\in X^*, \ s_i\in S \
\mbox{and} \ u_j\in Red(S)$. Then $Red(S)$ generates the factor module. Moreover, assume that $0\neq \sum \alpha_i a_i s_i=\sum
\beta_j u_j$, where $\ a_i\in X^*, \ s_i\in S, \ u_j\in Red(S), \
a_1 \overline{s}_1\succ a_2 \overline{s}_2\succ\cdots$ and $u_1\succ
u_2\succ\cdots$. Then $u_1=a_1 \overline{s}_1$, a contradiction. This shows that $Red(S)$ is a $k$-linear basis of the factor module.

$(3)\Rightarrow (1)$. For any $f, \ g\in S$, suppose that $w=\overline{f}=a\overline{g}$. Since $(f,g)_w\in k\langle X\rangle
S$, we get, by $(3)$, that $(f,g)_w=f-ag=\sum \alpha_i a_i s_i$, where $s_i\in S, \  a_i\in X^*$ and $a_i \overline{s_i}\preceq
\overline{(f,g)_w}\prec w$. Then, $S$ is a Gröbner-Shirshov basis in the module $mod_{k\langle X\rangle} \langle Y\rangle$.   $\square$\
: Let us view $k\langle X\rangle$ as free left $k\langle X\rangle$-module with one generator $I$. Then $mod_{k\langle X\rangle} \langle I\rangle=k\langle X\rangle
I=_{k\langle X\rangle}\!\!k\langle X\rangle$ is a cyclic $k\langle
X\rangle$-module. If $S\subset k\langle X\rangle$, then $k\langle
X\rangle S$ is a left ideal of $k\langle X\rangle$ (also a left $k\langle X\rangle$-submodule of $k\langle X\rangle I$). This implies that Lemma [\[l1\]](#l1){reference-type="ref" reference="l1"} is a special case of Lemma [\[l2\]](#l2){reference-type="ref" reference="l2"}.

  

Let $S\subset k\langle X\rangle$ and $A=k\langle X|S\rangle$ an associative algebra. Then, for any left $A$-module $_AM$, we can view $_AM$ as a $k\langle X\rangle$-module in a natural way: for any $f\in k\langle X\rangle, \ m\in M$, $$fm=(f+Id(S))m.$$ We note that $_AM$ is an epimorphic image of some free $A$-module. Then, we can assume that $_A M=mod_A \langle Y|T\rangle=mod_{A}
\langle Y\rangle/AT$, where $T\subset mod_{A} \langle Y\rangle$ and $mod_{A} \langle Y\rangle$ a free left $A$-module with the basis $Y$. Let $T_1=\{\sum f_iy_i\in mod_{k\langle X\rangle} \langle
Y\rangle|\sum (f_i+Id(S))y_i\in T\}$ and $R=SX^*Y\cup T_1$. Then, by the following Lemma [\[l3.6\]](#l3.6){reference-type="ref" reference="l3.6"}, we have, as $k\langle
X\rangle$-modules, $_A M\cong mod _{k\langle X\rangle}\!\langle
Y|R\rangle$.

::: lemma
([@ch])[]{#l3.6 label="l3.6"} Let the notations be as above. Then, as $k\langle X\rangle$-modules, $$\sigma: \ _A M\rightarrow mod _{k\langle X\rangle}\!\langle
Y|R\rangle, \ \ \sum (f_i+Id(S)) (y_i+AT)\mapsto\sum f_i
y_i+k\langle X\rangle R$$ is an isomorphism, where each $f_i\in k\langle X\rangle$.
:::

**Proof:** For any $\sum (f_i+Id(S)) (y_i+AT),\sum (g_i+Id(S))
(y_i+AT)\in_A\!M$, we have $$\begin{aligned}
&&\sum (f_i+Id(S)) (y_i+AT)=\sum (g_i+Id(S)) (y_i+AT)\ \ \ \mbox{ in } \ \ \ _A\!M \\
&\Leftrightarrow& \sum (f_i-g_i)y_i\in AT\ \ \ \mbox{ in } \ \ \ _A\!M \\
&\Leftrightarrow&  \sum (f_i-g_i)y_i\in k\langle X\rangle R\\
&\Leftrightarrow&  \sum f_i y_i+k\langle X\rangle R=\sum g_i
y_i+k\langle X\rangle R.
\end{aligned}$$ Hence, $\sigma$ is injective. It is easy to see that $\sigma$ is a surjective mapping and a $k\langle X\rangle$-module homomorphism.   $\square$

By using Lemma [\[l3.5\]](#l3.5){reference-type="ref" reference="l3.5"} and Lemma [\[l3.6\]](#l3.6){reference-type="ref" reference="l3.6"}, we know that if we want to find a $k$-linear basis for the module $_A M=mod_A \langle
Y|T\rangle$, where $A=k\langle X|S\rangle$, we only need to find a Gröbner-Shirshov basis for the module $mod_{k\langle X\rangle}
\langle Y|SX^*Y\cup T_1\rangle$, where $T_1=\{\sum f_iy_i\in
mod_{k\langle X\rangle} \langle Y\rangle|\sum (f_i+Id(S))y_i\in
T\}$.

  

The following theorem gives some relationships between the Gröbner-Shirshov bases (pairs) in free associative algebras and "double-free\" modules.

::: theorem
[]{#l3 label="l3"} Let $X, \ Y$ be well ordered sets, $<$ a monomial order on $X^*$, $\prec$ the order on $X^*Y$ as in $(*)$. Let $S,\ T\subset k\langle
X\rangle$ be monic sets. Then the following statements hold:

1.   $S\subset k\langle X\rangle$ is a Gröbner-Shirshov basis in $k\langle X\rangle$ with respect to the order $<$ if and only if $SX^*Y\subset mod_{k\langle
    X\rangle} \langle Y\rangle$ is a Gröbner-Shirshov basis in $mod_{k\langle X\rangle} \langle Y\rangle$ with respect to the order $\prec$.

2.   Let us view $k\langle X\rangle$ as free $k\langle X\rangle$-module with one generator $I$. Then, $(S,T)$ is a Gröbner-Shirshov pair for the $A$-module $M=A/A(T+Id(S))$, where $A=k\langle X|S\rangle$, if and only if $S$ is a Gröbner-Shirshov basis in the algebra $k\langle X\rangle$ with respect to the order $<$ and $(SX^*\cup T)I$ a Gröbner-Shirshov basis in the free module $mod_{k\langle
    X\rangle}\!\langle I\rangle$ with respect to the order $\prec$.
:::

**Proof:** (1) Suppose that $S$ is a Gröbner-Shirshov basis in $k\langle X\rangle$. We shall prove that all the compositions in $SX^*Y$ are trivial modulo $SX^*Y$. For any $f, \ g\in SX^*Y$, let $f=s_1 a_1 y, \ g=s_2 a_2 y , \ s_1,s_2\in S, \ a_1,a_2\in X^*, \
y\in Y$ and $w=\overline{f}=a\overline{g}$. Then $\overline{s}_1
a_1=a\overline{s}_2 a_2$. Since $S$ is a Gröbner-Shirshov basis in $k\langle X\rangle$, we have $$(f,g)_w=f-ag=s_1 a_1 y-as_2 a_2 y=(s_1 a_1-as_2 a_2)y=\sum (\alpha_i
u_i r_i v_i)y,$$ where $u_i, \ v_i\in X^*, \ r_i\in S$ and $u_i \overline{r}_i v_i
y\prec w$. So each composition is trivial modulo $SX^*Y$ and hence, $SX^*Y$ is a Gröbner-Shirshov basis in $mod_{k\langle X\rangle}
\langle Y\rangle$.

Conversely, assume that $SX^*Y$ is a Gröbner-Shirshov basis in the module $mod_{k\langle X\rangle} \langle Y\rangle$. For any $f, \
g\in S$ and $w=\overline{f}a=b\overline{g}$, we have $w_1=\overline{fay}=b\overline{gy}$ and $$(fay,bgy)_{w_1}=(fa-bg)y=\sum \alpha_i (a_i r_i) y,$$ where $\alpha_i\in k, \ r_i=s_i b_i, \ a_i,b_i\in X^*, \ s_i \in S$ and $a_i \overline{r}_i y\prec w_1$. Then, $$(f,g)_w=fa-bg=\sum \alpha_i a_is_i b_i$$ with $a_i \overline{s}_i b_i<w$. This shows that, each composition of intersection in $S$ is trivial modulo $S$. Similarly, each composition of inclusion in $S$ is trivial modulo $S$. Therefore, $S$ is a Gröbner-Shirshov basis in $k\langle X\rangle$.

\(2\) The results follow from the Definitions [\[d4\]](#d4){reference-type="ref" reference="d4"} and [\[d3\]](#d3){reference-type="ref" reference="d3"} directly.   $\square$

  

: By Theorem [\[l3\]](#l3){reference-type="ref" reference="l3"}, it is clear that the Theorem [\[t1\]](#t1){reference-type="ref" reference="t1"} follows from Lemma [\[l3.5\]](#l3.5){reference-type="ref" reference="l3.5"}.

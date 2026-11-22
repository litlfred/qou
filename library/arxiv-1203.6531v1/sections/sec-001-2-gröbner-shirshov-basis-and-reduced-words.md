---
doc_id: arxiv-1203.6531v1
doc_title: "Groebner-Shirshov basis and reduced words for affine Weyl group A_n"
section_id: sec-001-2-gröbner-shirshov-basis-and-reduced-words
section_title: "Gröbner-Shirshov Basis and Reduced Words"
section_number: 2
pages: 3-7
source_pdf: 1203.6531v1.pdf
source_sha256: 29541f28c1c62d8f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.826
doc_brief: "Groebner-Shirshov basis and reduced words for affine Weyl group A_n — Using Buchberger-Shirshov Algorithm and Composition-Diamond lemma we obtain the reduced Gr¨obner-Shirshov bases of f An and"
---
::: defn
The affine Weyl group $\widetilde{A_n}$ has a presentation with generators $S=\{r_0,r_1, \ldots,r_n\}$ and defining relations

$r_ir_i=1 \quad   0 \leq i \leq n$

$r_ir_j=r_jr_i \quad   0\leq i < j-1 < n \; \mathrm{and} \; (i,j) \neq (0,n)$

$r_ir_{i+1}r_i=r_{i+1}r_ir_{i+1} \quad 0 \leq i \leq n-1$

$r_0r_nr_0=r_nr_0r_n$.
:::

Identifying each relation $u=v$ by a polynomial $u-v$, we define

$f_{1}^{(i)}=r_ir_i-1 \quad   0 \leq i \leq n$

$f_{2}^{(i,j)}=r_ir_j-r_jr_i \quad   0\leq i < j-1 < n \; \mathrm{and} \; (i,j) \neq (0,n)$

$f_{3}^{(i)}=r_ir_{i+1}r_i-r_{i+1}r_ir_{i+1} \quad 0 \leq i \leq n-1$

$f_4=r_0r_nr_0-r_nr_0r_n$

Let us define

$$r_{ij}= \left\{
  \begin{array}{ll}
    r_ir_{i+1}\ldots r_j, & i<j; \\
    r_ir_{i-1}\ldots r_j, & i>j;\\
    r_i, & i=j; \\
    1, & i=1,j=0;\\
    1, & i=n,j=n+1.
  \end{array}
\right.$$

::: lem
[]{#gs label="gs"} Let $R=\{f_1,f_2,f_3,f_4\}$. A Grobner-Shirshov Basis of $\widetilde{A_n}$ with respect to deglex order with $r_0>r_1> \cdots >r_n$ contains the following polynomials.

$g_{1}^{(i,j)}=r_{ij}r_i-r_{i+1}r_{ij} \qquad 0 \leq i <j-1 < n$ with $(i,j)\neq (0,n)$

$g_{2}=r_{0n}r_0r_n-r_1r_{0n}r_0$

$g_{3}^{(j,k)}=r_0r_{nk}r_j-r_jr_0r_{nk} \qquad 2 \leq j<k-1<n$

$g_{4}^{(j)}=r_0r_{nj}r_{j+1}-r_jr_0r_{nj} \qquad 2 \leq j < n$

$g_{5}^{(k)}=r_0r_{nk}r_0-r_nr_0r_{nk} \qquad 2 \leq k <n$

$g_{6}^{(k,l)}=r_0r_{nk}r_{1l}r_{0l}-r_nr_0r_{nk}r_{1l}r_{0,l-1} \qquad 1\leq l <n, \;  2 \leq k\leq n$

$g_{7}^{(k,l)}=r_0r_{nk}r_{1l}r_0r_{nk}-r_1r_0r_{nk}r_{1l}r_0r_{n,k+1} \qquad 1 \leq l< k-1 <n$

$g_{8}^{(k,l)}=r_0r_{nk}r_{1l}r_0r_{n,k-1}-r_1r_0r_{nk}r_{1l}r_0r_{nk} \quad 3 \leq k\leq n, \quad k-1\leq l\leq n$

$g_{9}^{(j,k,l)}=r_0r_{nk}r_{1l}r_0r_{nj}r_{1l}-r_nr_0r_{nk}r_{1l}r_0r_{nj}r_{1,l-1}$\
$\qquad2\leq k\leq n-1, \quad k+1\leq j\leq n,\quad 1\leq l\leq j-2$

$g_{10}^{(j,k,l)}=r_0r_{nk}r_{1l}r_0r_{nj}r_{1,l+1}-r_nr_0r_{nk}r_{1l}r_0r_{nj}r_{1l}$\
$\qquad 2\leq k\leq n,\quad k\leq j\leq n,\quad j-1\leq l\leq n-1$
:::

::: proof
*Proof.* Let $R=\{f_1,f_2,f_3,f_4\}$. We apply the Buchberger-Shirshov algorithm to the $R$. We show every ELW in the below computations except ELW's of $f_2{(i,j)}$, the cummutativity relations. Notice that at this point we are not claiming that this is a Gröbner-Shirshov basis for $\widetilde{A}_n$.

$(f_{3}^{(i)},f_{2}^{(i,i+2)})=g_{1}^{(i,i+2)}.$

$(g_{1}^{(i,j-1)},f_{2}^{(i,j)})=g_{1}^{(i,j)} \quad \mathrm{for} \quad  j=i+3,\ldots,n.$

$(g_{1}^{(0,n-1)},f_{4})=g_{2}.$

$(f_{2}^{(0,j)},f_{2}^{(j,n)})=g_{3}^{(j,n)}.$

$(g_{3}^{(j,k+1)},f_{2}^{(j,k)})=g_{3}^{(j,k)}\quad \mathrm{for} \quad k=n-1,\ldots,j+2.$

$(f_{2}^{(0,n-1)},f_{3}^{(n-1)})=g_{4}^{(n-1)}.$

$(g_{3}^{(j,j+2)},f_{3}^{(j)})=g_{4}^{(j)} \quad  \mathrm{for} \quad j=n-2,...,2.$

$(f_{4},f_{2}^{(0,n-1)})=g_{5}^{(n-1)}.$

$(g_{5}^{(k+1)},f_{2}^{(0,k)})=g_{5}^{(k)} \quad  \mathrm{for} \quad k=n-2,\ldots,2 .$

$(f_{4},f_{3}^{(0)})=g_{6}^{(n,1)}$

$(g_{5}^{(k)},f_{3}^{(0)})=g_{6}^{(k,1)}\quad \mathrm{for} \quad k=n-1,\ldots,2.$

$(g_{6}^{(k,l-1)},f_{3}^{(l-1)})=g_{6}^{(k,l)}\quad \mathrm{for} \quad l=2,\ldots,n-1 .$

$(f_{3}^{(0)},f_4)=r_0r_nr_1r_0r_n-r_1r_0r_nr_1r_0=g_{7}^{(n,1)}.$

$(g_{1}^{(0,l)},f_{4})=g_{7}^{(n,l)} \quad \mathrm{for} \quad l=2,\ldots,k-2.$

::: flalign*
(g\_7\^(k+1,l),g\_3\^(k+1,k))& = r\_0r\_n,k+1r\_1lr\_kr\_0r\_nk-r\_1r\_0r\_n,k+1r\_1lr\_0r\_n,k+2r\_kr\_k+1\
&= g\_7\^(k,l)-r\_1r\_0r\_n,k+1r\_1lg\_3\^(k,k+2)r\_k+1 k=n-2,...,3.&
:::

::: flalign*
(g\_7\^(n,l),g\_3\^(n,n-1))& = r\_0r\_nr\_1lr\_nr\_0r\_n,n-1-r\_1r\_0r\_nr\_1lr\_0r\_n,n-1r\_n\
&= g\_7\^(n-1,l)-r\_1r\_0r\_nr\_1lf\_2\^(0,n-1)r\_n k=n-1.&
:::

::: flalign*
(g\_7\^(k,k-2),g\_4\^(k-1))&=r\_0r\_nkr\_1,k-1r\_0r\_n,k-1-r\_1r\_0r\_nkr\_1,k-2r\_0r\_n,k+1r\_k-1r\_k\
&=g\_8\^(k,k-1)-r\_1r\_0r\_nkr\_1,k-2g\_3\^(k-1,k+1)r\_n k=n-1,...,3.&
:::

::: flalign*
(g\_7\^(n,n-2),g\_4\^(n-1))&=r\_0r\_nr\_1,n-1r\_0r\_n,n-1-r\_1r\_0r\_nr\_1,n-2r\_0r\_n-1r\_n\
&=g\_8\^(n,n-1)-r\_1r\_0r\_nr\_1,n-2f\_2\^(0,n-1)r\_n k=n.&
:::

$(g_{2},g_{4}^{(n-1)})=r_{0,n-2}f_{3}^{(n-1)}r_{0}r_{n}r_{n-1}-r_{1}r_{0n}f_{2}^{(0,n-1)}r_{n}-r_{1}r_{0,n-2}f_{3}^{(n-1)}r_{0}r_{n}+g_8^{(n,n)}$

::: flalign*
(g\_8\^(k+1,l),g\_4\^(k-1))&=r\_0r\_n,k+1r\_1,k-2g\_1\^(k-1,l)r\_0r\_n,k-1-r\_1r\_0r\_n,k+1r\_1lg\_3\^(k-1,k+1)r\_k\
&-r\_1r\_0r\_n,k+1r\_1,k-2g\_1\^(k-1,l)r\_0r\_n,k+1r\_k+g\_8\^(k,l) l=k,...,n .&
:::

$(g_{6}^{(k,1)},f_{2}^{(1,n)})=g_{9}^{(k,n,1)}.$

$(g_{9}^{(k,j+1,1)},f_{2}^{(1,j)})=g_{9}^{(k,j,1)}\quad \mathrm{for} \quad j=n-1,\ldots,k+1.$

::: flalign*
(g\_9\^(k,j,l-1),f\_3\^(l-1))&=r_0r\_nkr\_1,l-1r_0r\_njr\_1,l-2r\_lr\_l-1r_l-r_nr_0r\_nkr\_1,l-1r_0r\_njr\_1,l-2r\_lr\_l-1\
&=g\_9\^(k,j,l) l=2,...,j-2.&
:::

::: flalign*
(g\_9\^(k,j+1,j-1),f\_3\^(j-1))=&r_0r\_nkr\_1,j-1r_0r\_n,j+1r\_1,j-2r\_jr\_j-1r\_j\
&-r\_nr\_0r\_nkr\_1,j-1r\_0r\_n,j+1r\_1,j-2r\_jr\_j-1\
&=g\_10\^(k,j,j-1) j=n-1,...,k.&\
:::

::: flalign*
(g\_6\^(k,n-1),f\_3\^(n-1))=& r_0r\_nkr\_1,n-1r\_0,n-2r\_nr\_n-1r\_n\
&-r\_nr_0r\_nkr\_1,n-1r\_0r\_nr\_1,n-1 = g\_10\^(k,n,n-1) .&
:::

::: flalign*
(g\_10\^(k,j,l-1),f\_3\^(l))=&r_0r\_nkr\_1,l-1r_0r\_njr\_1,l-1r\_l+1r\_lr\_l+1\
& -r_nr_0r\_nkr\_1,l-1r_0r\_njr\_1,l-1r\_lr\_l+1r_l\
=&r\_0r\_nkr\_1,l-1g\_4\^(l)r\_l-1,jr\_1,l+1-r\_nr\_0r\_nkr\_1,l-1g\_4\^(l)r\_l-1,jr\_1l\
&+g\_10\^(k,j,l) l=j-1,...,n-1.&
:::

In the above equation if $l=j$, then $r_{l-1,j}$ assumed to be the identity $1$. ◻
:::

Let $R'= R \cup \{g_1, \ldots, g_{10} \}.$ We want to find the properties of the elements of the set $Red(R') = \{w \in S^*|w \neq a\overline{f}b, a, b \in S^*, f \in R'\}$. If $w \in Red(R')$, then we call it a reduced word.

Notice that elements of $R'$ not containing $r_0$ is in fact a Gröbner-Shirshov basis for the Coxeter group $A_n$. The following lemma is just another way of expressing of the Lemma 3.2 of [@bokut1].

::: lem
[]{#ri label="ri"} Any reduced word not containing $r_{0}$ is in the form $$r=(r_{nj_{n}})^{\alpha_{n}}(r_{n-1,j_{n-1}})^{\alpha_{n-1}},\ldots,(r_{2j_{2}})^{\alpha_{2}},(r_{1j_{1}})^{\alpha_{1}}$$ where $i\leq j_{i}\leq n$ and $\alpha_{i}\in \{0,1\}$.
:::

After investigation of leading words of the elements of $G'$, we can claim the following results. For convenience we write $r_{0}r_{n,n+1}r_{1l}$ instead of $r_{0l}$ and $r_{0}r_{nk}r_{10}$ instead of $r_{0}r_{nk}$.

::: lem
[]{#r0 label="r0"} The following words are reduced.

\(i\) $w=r_{0}r_{nk}r_{1l}$ $2\leq k\leq n+1$, $0\leq l\leq n$

\(ii\) $$(r_0r_{nk}r_{1l})(r_0r_{np}r_{1q})=\left\{
                                            \begin{array}{ll}
                                              (k<p) \wedge (l>q), & \hbox{if} \; \; \; q-p <l-k<-1\\
                                              (k \leq p) \wedge (l>q), & \hbox{if} \; \; \; (q-p<-1) \wedge (l-k \geq -1)\\
                                              (k \leq p) \wedge (l \geq q), & \hbox{if} \; \; \;  l-k>q-p \geq -1
                                            \end{array}
                                          \right.$$
:::

::: lem
[]{#rir0 label="rir0"} Let $w$ be a reduced word starting with $r_i$ for $i=1,\ldots,n$ and let $t$ be a reduced word starting with $r_0$. Then $wt$ is also a reduced word.
:::

::: proof
*Proof.* The results follows from the following observation. Any leading word starting with $r_i$ for $i=1,\ldots,n$ in $G'$ do not contains $r_0$. ◻
:::

::: lem
[]{#lem8 label="lem8"} Let $w_{1},w_{2},\ldots w_{k},w_{k+1}$ be reduced words in the one of the forms given in the first three items of Lemma  [\[r0\]](#r0){reference-type="ref" reference="r0"}. If $w_{1}w_{2}\ldots w_{k}$ and $w_{2}w_{3}\ldots w_{k+1}$ are reduced, then $w_{1}w_{2}\ldots w_{k+1}$ is also reduced.
:::

::: proof
*Proof.* Let $w=w_{1}w_{2}\ldots w_{k+1}$. The only possible reduced subword of $w$ is in the form $rw_{2}w_{3}\ldots w_{k}s$ where $r$ and $s$ are subwords of $w_{1}$ and $w_{k+1}$, respectively. Since $w_{2}w_{3}\ldots w_{k}w_{k+1}$ is reduced word, $w_{2}w_{3}\ldots w_{k}s$ is also reduced word starting with $r_{0}$. Since $r$ is a subword of $w_{1}$, $r$ is also a reduced word not containing $r_{0}$. By Lemma  [\[rir0\]](#rir0){reference-type="ref" reference="rir0"}, $rw_{2}w_{3}\ldots w_{k}s$ is also reduced. Hence $w_{1}w_{2}\ldots w_{k+1}$ must be a reduced word. ◻
:::

::: defn
[]{#u label="u"} Let $a_{i}=r_{0}r_{nk}r_{1l}$ for $2\leq k\leq n+1$, $0\leq l\leq n$ and $l-k=i-2$.

Let $$u=(a_{n})^{m_{n}}(a_{n-1})^{m_{n-1}}\ldots (a_{1})^{m_{1}}$$ where $m_{i}\geq 0$ for $i=1,\ldots,n$. Furthermore, if $a_{i}=r_{0}r_{nk}r_{1l}$, then $a_{i+1}=r_{0}r_{n,k+1}r_{1l}$ or $a_{i-1}=r_{0}r_{nk}r_{1,l-1}$. Notice that the number of possible $u$'s is $2^{n-1}$. We call $a_i$'s the components of the word $u$.
:::

::: defn
Let $b_t=r_{0}r_{np}r_{1q}$ for $2\leq p\leq n+1$ and $0\leq q\leq n$ satisfying $q-p<-1$. There are $n!$ such words.

Let $$v^{(b_t)}=b_t (b_{t-1})^{\alpha_{t-1}}\cdots (b_{s})^{\alpha_s}$$ where $\alpha_{i}\in \{0,1\}$. Furthermore, if $b_{i}=r_{0}r_{np_i}r_{1q_i}$, then $b_{i-1}=r_{0}r_{np_{i-1}}r_{1q_{i-1}}$ for $p_i<p_{i-1}$ and $q_i>q_{i-1}$. If $p_i=n+1$ or $q_i=0$, then $\alpha_{j}=0$ for $j=s,\ldots,i-1$.

For the convenience, we define $1=r_0r_{n,\infty}r_{1,-1}$ and $v{(1)}=1$.
:::

::: proof
*Proof.* The result is easily follows from Lemma  [\[r0\]](#r0){reference-type="ref" reference="r0"} and Lemma [\[lem8\]](#lem8){reference-type="ref" reference="lem8"}. ◻
:::

Figure 1.1 shows every possible reduced words for $n=4$.

Let $$w_1=(r_0r_{42}r_{14})^{m_1}(r_0r_{42}r_{13})^{m_2}(r_0r_{43}r_{13})^{m_3}(r_0r_{4}r_{13})^{m_4}r_{01}$$ and $$w_2=(r_0r_{42}r_{14})^{m_1}(r_0r_{43}r_{14})^{m_2}(r_0r_{4}r_{14})^{m_3}(r_0r_{4}r_{13})^{m_4}r_{01}.$$ Then $w_1$ and $w_2$ are two reduced words in $\widetilde{A}_4$. If we take $m_2=m_3=0$ and $m_1=m_4=1$, then the subword $(r_0r_{42}r_{14})(r_0r_{4}r_{13})r_{01}$ is written twice. To avoid this situation, we define the arranged words.

<figure id="1">
<p><img src="4.png" style="width:4.86111in" alt="image" /><br />
</p>
<figcaption>1</figcaption>
</figure>

::: defn
[]{#arranged label="arranged"} Let $w=u v^{(b_t)}$ be a reduced word where $b_{t}=r_{0}r_{np}r_{1q}$ and $$u=(a_n)^{(m_n)}(a_{n-1})^{(m_{n-1})} \cdots (a_1)^{(m_1)}.$$

For $i=2,\ldots,n-1$ , let $m_i \geq 1$ if $a_{i+1}=r_{0}r_{nk}r_{1,l+1}$, $a_{i}=r_{0}r_{nk}r_{1l}$ and $a_{i-1}=r_{0}r_{n,k+1}r_{1l}$. If $a_2=r_{0}r_{nk}r_{1,l+1}, a_1=r_{0}r_{nk}r_{1l}$ and $p>k$, then let $m_1 \geq 1$. Then $w$ is called an arranged word and the components $a_i$ where $m_i \geq 1$ are called a marked component of $w$.
:::

::: thm
If all reduced words $w=u v^{(b_t)}$ are arranged, then each subword is written uniquely.
:::

::: proof
*Proof.* Let $w_1=u_1 v^{(b_t)}$ and $w_2=u_2v^{(b_t)}$ be two arranged word. Since the only possibility for $a_n=r_0r_{n2}r_{1n}$, the first components of them are the same. Let us assume that $a_n,a_{n-1},\ldots,a_j$ are common in $w_1$ and $w_2$. If the exponents of $a_i$ for $i=j,\ldots,n$ were $1$ and the others were $0$ in both $w_1$ and $w_2$, then the word $a_na_{n-1}\cdots a_j$ would be written twice.

Let us assume $a_j=r_0r_{nk}r_{1l}$. Moreover, let $a_{j-1}=r_0r_{n,k+1}r_{1l}$ in $w_1$ and $a_{j-1}=r_0r_{nk}r_{1,l-1}$ in $w_2$. Then there exits $s \geq l-1$ the components of $w_2$ between $j-1$ and $s+1$ are $$(r_{0}r_{nk}r_{1,l-1})(r_{0}r_{nk}r_{1,l-2})\cdots (r_{0}r_{nk}r_{1s})(r_{0}r_{n,k+1}r_{1s})$$ when $s-k>-1$. If $s-k=-1$, we have $$(r_{0}r_{nk}r_{1,l-1})(r_{0}r_{nk}r_{1,l-2})\cdots (r_{0}r_{nk}r_{1s})(r_{0}r_{np}r_{1q})$$

Therefore $r_0r_{nk}r_{1s}$ is a marked component in the first case. By Definition [\[u\]](#u){reference-type="ref" reference="u"}, $r_0r_{nk}r_{1l}$ can not be a component of $w_1$. The component of $w_1$ in the same position can be $r_0r_{n\overline{k}}r_{1 \overline{s}}$ where $\overline{k}> k$ and $\overline{s}<s$. Since $b_t$ is common in both words, $p \geq \overline{k} >k$. Therefore $r_0r_{nk}r_{1s}$ is also a marked component in the second case.Hence the word $(a_n)a_{n-1}\cdots (a_j)$ can be written only in $w_1$ not in $w_2$. ◻
:::

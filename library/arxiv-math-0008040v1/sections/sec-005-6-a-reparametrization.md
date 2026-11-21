---
doc_id: arxiv-math-0008040v1
doc_title: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A"
section_id: sec-005-6-a-reparametrization
section_title: "A Reparametrization"
section_number: 6
pages: 13-21
source_pdf: 0008040v1.pdf
source_sha256: a72319b55dbaf20b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.864
doc_brief: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A — Let U be the quantum group associated to a Lie algebra g of type An."
---
We will now use the rectangle combinatorics from the previous section to calculate the Lusztig parametrizations $c_j(\mathbf{j})$, $c_P(\mathbf{j})$ of the canonical basis elements arising in Theorem [\[natural\]](#natural){reference-type="ref" reference="natural"}; here $\mathbf{j}$ is fixed as the reduced expression $(n,n-1,n,n-2,n-1,n,\ldots ,1,2,\ldots ,n)$ for $w_0$.

::: definition
[]{#centralline label="centralline"} Suppose $P$ is a partial quiver and $D(P)$ is the diagram for $P$ as defined above. The rectangles $\rho(Y)$ for $Y$ a component of $P$ divide $D(P)$ into smaller rectangles, which we shall call boxes. (In the example near the start of Section [\[rectangles\]](#rectangles){reference-type="ref" reference="rectangles"}, there are $6$ boxes). We regard these boxes as appearing in diagonal rows, from top left to bottom right As we work our way down the diagonal rows of boxes, starting from the top right of $D(P)$, the number of boxes in each diagonal is at first odd, and then even, or is at first even, and then odd. We draw a central line $Z$ on $D(P)$ dividing these two sets of diagonal rows of boxes. In our example, the number of boxes in each row is $1$,$3$,$2$, so the central line is indicated by the dashed line in Figure [1](#centrallinef){reference-type="ref" reference="centrallinef"}.

<figure id="centrallinef">
<p>units &lt;0.8cm,0.8cm&gt; x from -9 to 3, y from -2 to 3</p>
<p>at -2.5 1</p>
<p>[c] at 0.5 0 [c] at 1 0.5 [c] at 1.5 1.0 [c] at 2 1.5</p>
<p>0 2 2 / 2 2.5 1.5 / 1.5 0.5 -0.5 / -0.5 0 0 /</p>
<p>[c] at 1 -0.5 [c] at 1.5 0 [c] at 2 0.5</p>
<p>0 1.5 1.5 / 1.5 2.5 0.5 / 0.5 1 -1 / -1 0 0 /</p>
<p>[c] at 0.5 1 [c] at 1 1.5</p>
<p>1 1 2 / 2 2.5 0.5 / 0.5 1.5 -0.5 /</p>
<p>2 2.5 -1.5 /</p>
<p>[c] at 2.8 1.5 [c] at -0.3 0 [c] at 2.8 0.5</p>
<figcaption>The central line in <span class="math inline"><em>D</em>(<em>L</em><em>R</em><em>L</em>−)</span>.<span id="centrallinef" label="centrallinef"></span></figcaption>
</figure>

Let $Y$ be a component of $P$, and define a set $S(Y)$ of positive roots as follows. The rectangle $\rho(Y)$ for $Y$ is divided into two parts by the central line. Let $\rho^*(Y)$ be the part of $\rho(Y)$ which is labelled. The root $\alpha_{ij}$ lies in $S(Y)$ if and only if the intersection of a diagonal row of $D(P)$ (see Definition [\[diagonalrow\]](#diagonalrow){reference-type="ref" reference="diagonalrow"}) with $\rho^*(Y)$ contains the numbers $i,i+1,\ldots ,j-1,$ in order, reading from top left to bottom right. Then $S(P)$ is defined to be the union of the sets $S(Y)$ for $Y$ a component of $P$. In our example, $S(L_1)=\{\alpha_1,\alpha_2,\alpha_3\}$, $S(R_1)=\{\alpha_4+\alpha_5\}$ and $S(L_2)=\{\alpha_1+\alpha_2+\alpha_3,
\alpha_2+\alpha_3+\alpha_4\}$, so $S(P)=\{\alpha_1,\alpha_2,\alpha_3,
\alpha_4+\alpha_5,\alpha_1+\alpha_2+\alpha_3,\alpha_2+\alpha_3+\alpha_4\}$.

Let $v(P)\in \mathbb{N}^k$ be defined as follows. The reduced expression $\bf j$ defines an ordering on the positive roots; we write $\beta^l=
s_{j_1}s_{j_2}\cdots s_{j_{l-1}}(\alpha_{j_l})$, for $l=1,2,\ldots ,k$. Then let $v(P)_l$ be equal to $1$ if $\beta^l\in S(P)$ and $0$ otherwise. So in the example above, $v(P)=(0,1,0,0,0,1,0,1,0,1,0,0,1,0,1)$.

If $j\in [1,n]$, we define $S(j)$ by specifying that the root $\alpha_{ij}$ lies in $S(j)$ if and only if there is a diagonal row of $D(j)$ containing the numbers $i,i+1,\ldots ,j-1,$ in order, reading from top left to bottom right. We define $v(j)$ in the same way as $v(P)$ is defined using $S(P)$.
:::

We know that, if $b\in {\bf B}$ and $i\in [1,n]$, then $\widetilde{F}_ib\equiv
b'\ ({\rm mod\ } vL')$ for some unique $b'\in {\bf B}$. With respect to our fixed reduced expression ${\bf j}$, this defines an action on $\mathbb{N}^k$, defined by $\widetilde{F}_i(\varphi_{\bf j}(b))=\varphi_{\bf j}(b')$. Using the identification in the last paragraph, this also induces an action on sets of positive roots, which we also denote by $\widetilde{F}_i$. Reineke, in [@reineke1 §1], describes the action of $\widetilde{F}_i$ on $\mathbb{N}^k$:

::: prop
(Reineke) []{#reineke label="reineke"}\
Suppose ${\bf v}=(v_1,v_2,\ldots ,v_k)\in \mathbb{N}^k$. Write, for $1\leq i<
j\leq n+1$, $v_{ij}=v_l$, where $\beta^l=\alpha_{ij}$. For such $i<j$, define $$f_{ij}=\sum_{l=j}^{n+1} v_{il}-\sum_{l=j+1}^{n+1} v_{i+1,l}.$$ Let $j_0$ be minimal so that $f_{ij_0}=\max_j f_{ij}$. Then $\widetilde{F}_i$ increases $v_{ij_0}$ by $1$, decreases $v_{i+1,j_0}$ by $1$ (unless $i+1=j_0$, when this latter effect does not occur), and leaves the other $v_{ij}$'s unchanged.
:::

**Definition:** Let $2\leq a\leq b\leq n$, and let $Q$ be a quiver. We define the *$(a,b)$-sub partial quiver* of $Q$ to be the partial quiver $P$ with $P\leq Q$, leftmost directed edge numbered $b$ and rightmost directed edge numbered $a$.

As conjectured by Carter, we have:

::: theorem
[]{#Scorrespondence label="Scorrespondence"} Let $Q$ be a quiver, with ${\bf i}\in \chi_n$ compatible with $Q$. Suppose that $(c,{\bf i})$ is a chamber of $Q$, with $P=P(c,{\bf i})$. Let ${\bf j}=(n,n-1,n,n-2,n-1,n,\ldots ,1,2,\ldots ,n)$. Let $b_P$ be the canonical basis element arising in Theorem [\[natural\]](#natural){reference-type="ref" reference="natural"}. Then the Lusztig parametrization $c_P(\mathbf{j})$ of $b_P$ is given by $v(P)$. Similarly the Lusztig parametrization $c_j(\mathbf{j})$ of $b_j$ is given by $v(j)$.
:::

We have to calculate $S_{\bf i}^{\bf j}(a(c,{\bf i}))$ or $S_{\bf i}^{\bf j}(a(j,{\bf i}))$, and thus we consider the corresponding monomial of root operators acting on $1$, $\widetilde{F}(P)=\widetilde{F}_{i_1}^{a_1}
\widetilde{F}_{i_2}^{a_2}\cdots \widetilde{F}_{i_k}^{a_k}\cdot 1$. Here $P=P(c,{\bf i})$ in the first case and $j$ in the second. Theorem [\[spanningmonomial\]](#spanningmonomial){reference-type="ref" reference="spanningmonomial"} gives a description of $\widetilde{F}(P)$ in terms of $D(P)$. Recall that $D(P)$ consists of a number of *diagonal rows* (see Definition [\[diagonalrow\]](#diagonalrow){reference-type="ref" reference="diagonalrow"}), where diagonal row number $1$ is the one which is at the top right of $D(P)$, diagonal row number $2$ is below this (down and to the left), and so on. We now make a claim.

Let $x$ be a position in $D(P)$ containing a number, $i$. Suppose $x$ is in (diagonal) row $a$. Let $r$ be the total number of rows in $D(P)$, and let $\widetilde{F}(s)$, $s=1,2,\ldots ,r$, be the part of $\widetilde{F}(P)$ arising from the $s$th row. Thus $\widetilde{F}(P)=\widetilde{F}(r)\widetilde{F}(r-1)
\cdots \widetilde{F}(1)\cdot 1$. For $s=1,2,\ldots ,r$, let $d_s$ be the number at the rightmost end of the $s$th row. Define $\widetilde{F}[x]:=\widetilde{F}_{i}^{\lambda_{i}}
\widetilde{F}_{i+1}^{\lambda_{i+1}}\cdots \widetilde{F}_{d_a}^{\lambda_{d_a}}
\widetilde{F}(a-1)\cdots \widetilde{F}(2)\widetilde{F}(1)\cdot 1$, where, if $j$ appears in row $a$, $\lambda_j$ is the multiplicity associated to it.

So $\widetilde{F}[x]$ is a final segment of $\widetilde{F}(P)$, arising from the first $a-1$ rows of the diagram, together with the part of the $a$th row to the right of $x$, including $x$. Let ${\bf c}\in \mathbb{N}^k$ be defined by $\widetilde{F}[x]\equiv F_{\bf i}^{\bf c}\ ({\rm mod\ } v{\cal L'})$. Note that there is no problem working here modulo $v{\cal L'}$. We shall have $\widetilde{F}[x]\equiv b\ ({\rm mod\ } v{\cal L'})$ for a unique $b\in {\bf B}$ from Kashiwara's approach, and $b\equiv F_{\bf i}^{\bf c}\ 
({\rm mod\ } v{\cal L'})$ for a unique ${\bf c} \in \mathbb{N}^k$ by Lusztig's approach and the comparison theorem [@lusztig3 §2.3].

Let $S(x)$ be the corresponding multiset of positive roots, obtained by using the ordering on the set of positive roots induced by $\bf j$. We claim that $S(x)$ is given by the union of the following two sets: The first, $S_1(x)$ is defined to be those roots in $S(P)$ arising from rows $1,2,\ldots ,a-1$, together with those roots in $S(P)$ arising from row $a$ of the form $\alpha_{s}+\alpha_{s+1}+\cdots +\alpha_t$ where $s\geq i$. The second, $S_2(x)$, is defined to be the set of roots of form $\alpha_{i}+\alpha_{i+1}+\cdots +\alpha_t$, where $\alpha_s+\alpha_{s+1}+
\cdots +\alpha_t$ is a root in $S(P)$ arising from row $a$ with $s<i$ (we call this procedure of passing from $\alpha_s+\alpha_{s+1}+\cdots +
\alpha_t$ to $\alpha_{i}+\alpha_{i+1}+\cdots +\alpha_t$, 'cutting off').

We will prove the claim by induction on $x$. Let us assume that for a given $x$ in $D(P)$, $S(x)$ is as described. Let $\bf c$ be as above, corresponding to $x$. Let $y$ be one position to the left of $x$ in the $a$th row of $D(P)$. We understand this to mean the rightmost element of the $(a+1)$st row of $D(P)$ if $x$ is the leftmost element of the $a$th row. In this case for the purposes of the argument below we actually take $x$ to be in the same row as $y$, immediately down and to the right of $y$, with corresponding (fictitious) label $1$ more than that of $y$ (i.e. actually just outside the diagram $D(P)$). Note that in this case, as we are assuming the claim to be true for $x$, we have $S_2(x)=\phi$. Suppose there is an $i$ in position $y$. Then there is an $i+1$ in position $x$. Suppose that $x$ and $y$ both lie in the $a$th row of $D(P)$. We will show that the claim is also true for $y$. The base case, when $x$ is taken to be one position to the right of (and below) the rightmost position of the first row, with $S(x)=\phi$, is trivially true. The Theorem will follow from the induction argument, as it is the claim for the case when $x$ is the leftmost position of the last row of the diagram.

We must show that the set of positive roots (defined by $\bf j$) corresponding to $\bf c'$, where $\widetilde{F}[y]=\widetilde{F}_i^{\lambda_i}
\widetilde{F}[x]\equiv F_{\bf i}^{\bf c'}\ ({\rm mod\ } v{\cal L'})$ is given by $S_1(y)\cup S_2(y)$, where $i$ is the number labelling position $y$. In the case where $y$ is the rightmost element of its row (numbered $a$), we take $\widetilde{F}[x]$ to be $\widetilde{F}(a-1)\cdots \widetilde{F}(2)\widetilde{F}(1)\cdot 1$. We define ${\bf c}\in \mathbb{N}^k$ by writing $c_{ij}=1$ if $\alpha_{ij}\in S(x)$ and $c_{ij}=0$ otherwise. We start with an important

::: lemma
[]{#bothequalone label="bothequalone"} If $l>i+1$ then we cannot have both $c_{il}=1$ and $c_{i+1,l}=1$.
:::

(of Lemma). First of all note that if $P=j\in [1,n]$, the Lemma is obvious, following easily from the structure of $D(P)$. So we can assume that $P$ is a partial quiver. Suppose, for a contradiction, that $c_{il}=c_{i+1,l}=1$. So $\beta_1:=\alpha_i+\alpha_{i+1}+\cdots +
\alpha_{l-1}$ and $\beta_2:=\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_{l-1}$ both lie in $S(x)$. We are assuming the claim to be true for $x$, so $S(x)=S_1(x)\cup
S_2(x)$. We shall see that the structure of $D(P)$ leads to a contradiction; to do this we consider various cases:\
Case (a) For $i=1,2$, if $\beta_i\in S_2(x)$, let $\gamma_i$ be the root in $S(P)$ which is 'cut off' to give $\beta_i$. Otherwise, let $\gamma_i=\beta_i$. Suppose that $\gamma_1,\gamma_2$ both come a rectangle for a component $Y$ of $P$ of type $L$ which is the $(a_1,b_1)$-sub partial quiver of $Q$. The set of positive roots in $S(P)$ arising from $Y$ is $\{\alpha_{1,n-b_1},\alpha_{2,n+1-b_1},\ldots ,\alpha_{s,n+s-1+b_1}\}$ (where the central line passes through the rectangle corresponding to $Y$ immediately below the row with leftmost number $s$). If $\alpha=\alpha_{pq}$ is any positive root, write $r(\alpha)=q-1$ and $l(\alpha)=p$. For each $\gamma$ in this list, $r(\gamma)$ is distinct, and since 'cutting off' a root $\gamma$ does not affect $r(\gamma)$, we conclude that this case cannot occur, since $r(\beta_1)=r(\beta_2)$.\
Case (b) Suppose that $\beta_1,\beta_2$ both come from a component of $P$ of type $R$, as in (a). We argue as in case (a) to see that this case cannot occur.\
Case (c) Suppose that $\beta_1$ and $\beta_2$ arise from distinct components of $P$ and that $\beta_1,\beta_2\in S_1(x)$. Let $h$ be the height of the roots in $S(P)$ arising from a component $Y$ of $P$. Then the height of the roots in $S(P)$ arising from the component of $P$ immediately to the right of $Y$ (if such exists) is $h+t$, where $t$ is the number of directed edges in $Y$. Thus, since $\mbox{ht}(\beta_1)=1+\mbox{ht}(\beta_2)$ (ht denotes height), for this case to occur, we must be in the situation where we have two components $Y$ and $Z$ of $P$, where $Z$ immediately follows $Y$, and $Y$ has precisely one directed edge. We assume that $Y$ is of type $L$ and $Z$ is of type $R$ (the argument in the other case is very similar). Suppose that $Z$ is the $(a_1,b_1)$-sub partial quiver of $Q$. The two rectangles $\rho(Y)$ and $\rho(Z)$ will appear in $D(P)$ as in Figure [2](#rhoyrhoz){reference-type="ref" reference="rhoyrhoz"},

<figure id="rhoyrhoz">
<p>units &lt;0.8cm,0.8cm&gt; x from -6.4 to 5, y from -4.5 to 5</p>
<p>0 4 4 / 0 4 -4 / 3 7 -1 / -1 4 -4 / 4 7 1 / 1 3 -3 /</p>
<p>2.5 6.5 -3.5 /</p>
<p>at 0.5 0 at 3 2.5 at 3 2.1 at 4 3.65 at 6.3 1 at 5.15 0.2 at 5.28 -0.2 at 3 -2.3 at 6.15 -0.8 at 6.28 -1.2 at 4 -3.65</p>
<p>[c] at -0.3 0 [c] at 7.3 1</p>
<figcaption>The rectangles <span class="math inline"><em>ρ</em>(<em>Y</em>)</span> and <span class="math inline"><em>ρ</em>(<em>Z</em>)</span>.<span id="rhoyrhoz" label="rhoyrhoz"></span></figcaption>
</figure>

where as usual, the dashed line indicates the central line in $D(P)$. Then the roots for $Y$ will be taken from above this line, and the roots for $Z$ from below, such roots $\alpha$ will have differing values of $r(\alpha)$ so we see that this case cannot occur.\
Case (d) Suppose we have $\beta_1,\beta_2\in S_2(x)$. Suppose first that $x$ lies above the central line. We know that the lines in $D(P)$ which are the bottom right edges of rectangles $\rho(Y)$ where $Y$ is a component of $P$ of type $L$ are all distinct and parallel. It follows that $r(\beta_1)\not=r(\beta_2)$, a contradiction. A similar argument holds if $x$ lies below the central line.\
Case (e) Suppose that $\beta_1\in S_1(x)$ and $\beta_2\in S_2(x)$. If $\beta_1$ arises from the $a$th row of $D(P)$, we can argue as in (d) (we will have again $r(\beta_1)\not= r(\beta_2)$, a contradiction). So assume that $\beta_1$ arises from the $b$th row, where $1\leq b<a$. We know that $\beta_2$ arises via cutting off from a root $\gamma_2\in S(P)$ which comes from the $a$th row of $D(P)$. Since $\mbox{ht}(\beta_2)<
\mbox{ht}(\gamma_2)$ and $\mbox{ht}(\beta_1)=1+\mbox{ht}(\beta_2)$, we have $\mbox{ht}(\beta_1)< \mbox{ht}(\gamma_2)$. Therefore, arguing as in (c), we see that $\beta_1$ comes from a component $X_1$ occurring to the left of that giving rise to $\gamma_2$ (and thus $\beta_2$). We call the latter $X_2$. Suppose that $X_1$ does not occur immediately to the left of $X_2$, or that $X_2$ is of type $R$. Then by the structure of $D(P)$, the bottom right lines $T_1$, $T_2$ delimiting the rectangles $\rho(X_1)$ and $\rho(X_2)$ are distinct. Indeed, the line for $\rho(X_2)$ occurs below and to the right of $\rho(X_1)$.

We know that there is an $l-1$ in the intersection of the $b$th row with $\rho(X_1)$, immediately to the left and above the line $T_1$. Similarly, there is an $l-1$ in the intersection of the $a$th row with $\rho(X_2)$, immediately to the left and above the line $T_2$, by the construction of $\beta_1,\beta_2$. The relative position of lines $T_1$ and $T_2$ tells us that the former $l-1$ lies strictly to the left of the latter, while the fact that $b<a$ tells us that the latter $l-1$ lies strictly to the left of the former, a contradiction. We are left with the case when $X_1$ immediately precedes $X_2$ and $X_2$ is of type $L$. In this case $T_1$ and $T_2$ coincide along part of their lengths. Now $X_1$ is of type $R$, so $\beta_1$ arises from a row below the central line, and $X_2$ is of type $L$, so $\beta_2$ arises from a row above the central line. It follows that $r(\beta_1)\not=r(\beta_2)$, a contradiction.\
Case (f) Suppose that $\beta_1\in S_2(x)$, $\beta_2\in S_1(x)$, and $\beta_1$ and $\beta_2$ arise from different components. If $\beta_2$ arises from the $a$th row, we can argue as in (d). So assume $\beta$ arises from the $b$th row, where $1\leq b<a$. Then $\beta_1$ arises via cutting off from a root $\gamma_1\in S(P)$ which comes from the $a$th row. Since $\mbox{ht}(\beta_1)<\mbox{ht}(\gamma_1)$ and $\mbox{ht}(\beta_1)=1+\mbox{ht}(\beta_2)$, we have $\mbox{ht}(\beta_2)<
\mbox{ht}(\gamma_1)$, and we can argue as in (e).

We have now covered all possible cases for $\beta_1,\beta_2\in S(x)$, and we see that the Lemma is proved. $\square$

We now investigate further the structure of $\bf c$. By assumption, for each $j,k$, $c_{jk}$ is equal to $0$ or $1$. The above shows that we cannot have both $c_{il}=c_{i+1,l}=1$ for $l>i+1$. We shall now pin down further the possible values for $c_{il}$ and $c_{i+1,l}$. We know that, for each $l>i+1$, $(c_{il},c_{i+1,l})=(0,0)$, $(0,1)$ or $(1,0)$. If we let $c_{i+1,i+1}:=1-c_{i,i+1},$ then this is also true for $l=i+1$. For $m=0,1,2,\ldots n-i$, write $a_m=c_{i,i+m+1}$ and $b_m=c_{i+1,i+m+1}$, so the pairs we are interested in are of form ${\bf x}_m=(a_m,b_m)$, $m=0,1,2,\ldots n-i$. We first need a Lemma describing the action of $\widetilde{F}_i$ in terms of these pairs, using Proposition [\[reineke\]](#reineke){reference-type="ref" reference="reineke"}:

::: lemma
[]{#applyreineke label="applyreineke"} Suppose $\bf c$ is as in the above, and we have written the pairs ${\bf x}_0,{\bf x}_1,\ldots ,{\bf x}_{n-i}$ as above, with each ${\bf x}_m$ equal to $(0,0)$, $(0,1)$ or $(1,0)$. Rewrite this sequence, replacing pairs of these types with $0$, '$-$' and '$+$', respectively. Cross out all $0$'s, except initial $0$'s. Cross out all non-initial pairs of symbols of form $+-$, and repeat until there are no such pairs of symbols in the sequence left. Use the following table of possible sequences to determine a symbol in the resulting sequence of symbols. This is defined to be the symbol that is indicated by a line above it. Every time a sequence of symbols appears in the list, as in $-,-,\ldots ,-$, this means that the symbol concerned must occur at least once.

\(i\) $0,-,-,\ldots ,\overline{-},+,+,\ldots ,+,$\
(ii) $0,-,-,\ldots ,\overline{-},$\
(iii) $\overline{0},+,+,\ldots ,+,$\
(iv) $\overline{0},$\
(v) $(+,-),-,-,\ldots ,\overline{-},+,+,\ldots ,+,$\
(vi) $(+,-),-,-,\ldots ,\overline{-},$\
(vii) $(\overline{+},-),+,+,\ldots ,+,$\
(viii) $\overline{+},-,$\
(ix) $-,-,\ldots ,\overline{-},+,+,\ldots ,+,$\
(x) $-,-,\ldots ,\overline{-},$\
(xi) $\overline{+},+,\ldots ,+$.

In this way, a symbol in the original sequence is determined, and therefore an ${\bf x}_m$. Then acting $\widetilde{F}_i$ has the following effect on $\bf c$. If ${\bf x}_m=(0,1)$ (i.e. a '$-$'), then $c_{i+1,i+m+1}=1$. This is changed to zero (having no effect if $m=0$), and $c_{i,i+m+1}$ is changed from zero to $1$, thus changing the corresponding symbol in the sequence from a '$-$' to a '$+$'. If ${\bf x}_m=(1,0)$ or $(0,0)$, then we must have $m=0$ (as no initial symbols are crossed out), and $\widetilde{F}_i$ has the effect of increasing $c_{i,i+1}$ by $1$.
:::

: We consider how the $f_{ij}$'s are related to the ${\bf x}_p$'s (see Proposition [\[reineke\]](#reineke){reference-type="ref" reference="reineke"} for the definition of the $f_{ij}$'s). For each $0\leq p\leq n-i$, write $\delta_p:=f_{i,i+p+2}-f_{i,i+p+1}$. A simple calculation shows us that $\delta_p=1$ if $({\bf x}_p,{\bf x}_{p+1})=(0,-)$ or $(-,-)$, that $\delta_p=-1$ if $({\bf x}_p,{\bf x}_{p+1})=(+,+)$ or $(+,0)$, and is zero in all other cases. Thus the sequence in the Lemma enables us to calculate the value of the $f_{ij}$'s, given the value of $f_{i,i+1}$ (for our fixed $i$). Recall that Proposition [\[reineke\]](#reineke){reference-type="ref" reference="reineke"} tells us that, in order to see how $\widetilde{F}_i$ acts, we need to calculate the smallest $j$ for which $f_{ij}$ is maximal; write $j_0$ for this value of $j$. It is easy to check that the crossing out routines described above never cross out the symbol corresponding to ${\bf x}_p$ where $i+p+1=j_0$. Thus recalculating this *after* doing the crossing out does not affect the final result. After crossing out is done, the only possible sequences are those as listed in the Lemma. It is then easy to check that $j_0$ is given by $j_0=i+p+1$ where $p$ is given by the rules in the Lemma in each case (i)-(xi). $\square$

To illustrate this Lemma we go back to our example (see Definition [\[diagonal\]](#diagonal){reference-type="ref" reference="diagonal"} and Definition [\[centralline\]](#centralline){reference-type="ref" reference="centralline"}). So $P=LRL-$ and $D(P)$ is as in Figure [1](#centrallinef){reference-type="ref" reference="centrallinef"}. Suppose $x$ is the position of the rightmost $4$ in $D(P)$, the last element in the third diagonal row of $D(P)$. Then $y$ is the leftmost $3$ in $D(P)$, the second element in the third diagonal row, so $i=3$. The set $S_1(x)$ is by assumption $\{\alpha_1,
\alpha_2,\alpha_1+\alpha_2+\alpha_3\}$, and $S_2(x)$ is $\{\alpha_4\}$. Thus $S(x)$ is the union of these two sets and ${\bf c}=(0,0,1,0,0,0,0,0,0,
1,0,0,1,0,1)$. We can write $\bf c$ as in Figure [3](#vectorc){reference-type="ref" reference="vectorc"}.

<figure id="vectorc">
<p>units &lt;0.75cm,0.75cm&gt; x from -4 to 5, y from 1 to 5.5</p>
<p>at 1 1 at 2 1 at 3 1 at 4 1 at 5 1 at 1.5 2 at 2.5 2 at 3.5 2 at 4.5 2 at 2 3 at 3 3 at 4 3 at 2.5 4 at 3.5 4 at 3 5</p>
<p>at 7 3</p>
<p>at 9 1 at 10 1 at 11 1 at 12 1 at 13 1 at 9.5 2 at 10.5 2 at 11.5 2 at 12.5 2 at 10 3 at 11 3 at 12 3 at 10.5 4 at 11.5 4 at 11 5</p>
<figcaption>The vector <span class="math inline">$\bf c$</span>.<span id="vectorc" label="vectorc"></span></figcaption>
</figure>

We have ${\bf x}_0=(c_{34},c_{44})=(0,1)$, ${\bf x}_1=(c_{35},c_{45})=(0,1)$, and ${\bf x}_2=(c_{36},c_{46})=(0,0)$ --- these are indicated by underlining in Figure [3](#vectorc){reference-type="ref" reference="vectorc"} (note that $c_{44}$ does not appear in the diagram). Thus the sequence of symbols as in Lemma [\[applyreineke\]](#applyreineke){reference-type="ref" reference="applyreineke"} is $(-,-,0)$. In the reduction step, we remove the final zero to get $(-,-)$ and see we are in case (x) of the Lemma, and that the final '$-$' is marked. This corresponds to ${\bf x}_1$ and the Lemma tells us that applying $\widetilde{F}_i$ changes $c_{35}$ from $0$ to $1$ and $c_{45}$ from $1$ to $0$. As a more complicated example, consider the sequence of symbols $(0,0,+,+,-,-,+,+,+,0,-,0,-,-,+,-,-,-,-,0,0)$. We first of all remove non-initial zeros to get $(0,+,+,-,-,+,+,+,-,-,-,+,-,-,-,-)$ and then remove $+,-$ pairs to get $(0,-,-,-)$ --- which is case (ii) of the Lemma. Thus the last '$-$' is indicated, corresponding to the last '$-$' of the original sequence.

We now begin the investigation as promised.

::: lemma
[]{#investigation label="investigation"} Suppose that ${\bf x}_j=(1,0)$. Then $c_{i,i+j+1}=1$, so that $\alpha_{i,i+j+1}\in S(x)$. Suppose that in fact $\alpha_{i,i+j+1}\in
S_1(x)$. Then there is $m>j$ so that ${\bf x}_{j+1}={\bf x}_{j+2}=\cdots =
{\bf x}_{m-1}=(0,0)$ and ${\bf x}_m=(0,1)$. Thus $c_{i+1,i+m+1}=1$, so $\alpha_{i+1,i+m+1}\in S(x)$; in fact $\alpha_{i+1,i+m+1}\in S_1(x)$.
:::

: Let $l=i+j+2$; we know that $\alpha_i+\alpha_{i+1}+
\cdots +\alpha_{l}\in S_1(x)$. So $\alpha_i+\alpha_{i+1}+ \cdots +\alpha_{l}\in S(P)$ and arises from the intersection of row $b$ of $D(P)$ with a rectangle $\rho$, where $b<a$ (since $\alpha_i$ appears in it). Thus if $P=j\in [1,n]$, we have a contradiction by the structure of $D(P)$ (which consists of only one rectangle); $i$ can appear at the start of one row in $D(P)$ only. So in this case the circumstances of the Lemma cannot occur. Therefore we can assume $P$ is a partial quiver and we define $X$ to be the component of $P$ corresponding to $\rho$. Suppose that row $b$ is not immediately above the central line in $D(P)$. Then row $b+1$ of $D(P)$ intersects $\rho,$ the rectangle for $X$. This is because $i$ occurs in row $a$, in position $y$, where $a>b$. If row $b$ were the bottom row in the rectangle for $X$, $i$ would appear in the left hand corner of this rectangle, and therefore in no later row in $D(P)$ (by the structure of $D(P)$), a contradiction. Thus the intersection of row $b+1$ with the rectangle for $X$ gives a root $\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_{l+1}\in S(P)$. Since $b+1\leq a$ and the label at position $x$ in $D(P)$ is $i+1$, this root lies in $S_1(x)$ (i.e. is not cut off), as required (with $m=j+1$).

So we are left in the case where row $b$ does lie immediately above the central line of $D(P)$. Then $X$ must be of type $L$. Suppose first that $X$ is the rightmost component of $P$. Then $i$ appears in the leftmost column (where a column is perpendicular to what we are calling a row) of $D(P)$, and also is immediately above the central line. The central line coincides with the bottom left delimiting line of the rectangle for $X$. Consider now the rectangle for the component $Y$ immediately to the left of $X$. This has bottom right delimiting line parallel to that for $X$, but length (from top left to bottom right) less than that for $X$. Thus its upper left delimiting line is down and to the right of that for $X$, and $i$ is in the left hand corner of the rectangle for $X$. Then all of the upper left delimiting lines for components other than $X$ appear down and to the right of that for $X$, so $i$ cannot appear below the central line. But as $b<a$, $x$ is below the central line, and therefore so is $y$, which is labelled $i$, and we have a contradiction. Thus there is a component immediately to the right of $X$ in $P$; we call this $Y$. Let $\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_t$ (some $t>l+1$) in $S(P)$ be the root arising from the intersection of the $(b+1)$st row of $D(P)$ with the rectangle for $Y$. Then as before $\alpha_{i+1}+
\alpha_{i+2}+\cdots +\alpha_t\in S_1(x)$. Put $m=t-i$, and we have $(a_m,b_m)=(c_{i,i+m+1},c_{i+1,i+m+1})=(0,1)$, as required. We now have to show that ${\bf x}_{j+1}={\bf x}_{j+2}=\cdots =
{\bf x}_{m-1}=(0,0)$. That is, we have to show that\
(a) $\alpha_i+\alpha_{i+1}+\cdots +\alpha_u\not\in S(x)$ for $l+1\leq u<t$, and\
(b) $\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_u\not\in S(x)$ for $l+1\leq u<t$.

We start with (a), and take $l+1\leq u<t$. Since all roots $\beta\in S_2(x)$ satisfy $l(\beta)=i+1$, we have $\alpha_i+\alpha_{i+1}+\cdots +\alpha_{u}\not \in S_2(x)$. Therefore, it is enough to show that $\alpha_i+\alpha_{i+1}+\cdots +\alpha_{u}\not\in S(P)$. But $\mbox{ht}(\alpha_i+\alpha_{i+1}+\cdots +\alpha_{u})$ is strictly between the heights of the roots in $S(P)$ arising from $X$ and $Y$, and so by our description of the heights of the roots in $S(P)$ in case (c) of the proof of Lemma [\[bothequalone\]](#bothequalone){reference-type="ref" reference="bothequalone"}, we see that $\alpha_i+\alpha_{i+1}+\cdots +\alpha_{u}\not\in S(P)$ and (a) holds.

For (b), we consider again $l+1\leq u<t$. If $u\not=l+1$, the argument used for (a) shows that $\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_{u}\not
\in S(P)$. But if $u=l+1$, then this root has the same height as roots in $S(P)$ arising from $X$. So if it were in $S(P)$, it would have arisen from the intersection of the rectangle for $X$ with row $b+1$ of $D(P)$. But this row is below the central line of $D(P)$, whence $\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_{l+1}$ does not arise in this way, and so does not lie in $S(P)$. Next, suppose that we had $\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_{u}\in S_2(x)$. Then, since $x$ must be below the central line, $u$ must be immediately to the upper left of the bottom right line delimiting a rectangle corresponding to a component $Z$ of $P$ of type $R$. Since $\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_{u}$ is assumed to be in $S_2(x)$, it must be the 'cut off' from a root $\gamma=\alpha_p+\alpha_{p+1}+
\cdots +\alpha_u\in S(P)$, $p\leq i$, where $\gamma$ arises from the rectangle corresponding to $Z$. Since $\mbox{ht}(\gamma)>\mbox{ht}(
\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_{l+1}),$ $Z$ must lie strictly to the right of $X$ in $P$. We know that $\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_{t}$ corresponds to the first line of the rectangle for $Y$ below the central line in $D(P)$, so $Z$ is strictly to the right of $Y$, as $u<t$. Thus the bottom right delimiting line for $Z$ is strictly down to the right of that for $Y$. Thus this $u$ lies to the right of the $u$ corresponding to the $\alpha_u$ in $\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_{t}$ (in the $(b+1)$st row of $D(P)$), and this $u$ lies below the central line. This is impossible, as all $u$'s in $D(P)$ to the right of the $u$ in the $(b+1)$st row (which is immediately below the central line), lie *above* the central line. Thus $\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_{u}\not\in S_2(x)$ and so it is not in $S$ for $l+1\leq u<t$. So we see (b) also holds, and the Lemma is proved. $\square$

Note that all roots in $S_2(x)$ have a corresponding ${\bf x}_j$ of form $(0,1)$. All roots in $S_1(x)$ arising from the $a$th row of $D(P)$ will be of form $\alpha_p+\alpha_{p+1}+\cdots +\alpha_l$, for $l\geq p\geq i+1$, so only if $p=i+1$ will they contribute to an ${\bf x}_j$; in this case we shall get a corresponding ${\bf x}_j$ of form $(0,1)$.

We can now apply Lemma [\[applyreineke\]](#applyreineke){reference-type="ref" reference="applyreineke"} in our situation. By Lemma [\[applyreineke\]](#applyreineke){reference-type="ref" reference="applyreineke"}, after the crossing out process, our sequence looks like $((+,-),-,-,\ldots ,-),$ $((0),-,-,\ldots ,-)$ or $((-),-,\ldots ,-)$. By Lemma [\[applyreineke\]](#applyreineke){reference-type="ref" reference="applyreineke"}, applying $\widetilde{F}_i$ will change the last minus to a plus, and repeated applications will change the final $\lambda_i$ minuses to pluses. By the proof of Lemma [\[investigation\]](#investigation){reference-type="ref" reference="investigation"}, it is clear that all of the $-$'s in the sequence, except for those in brackets, correspond to precisely those ${\bf x}_p$'s which correspond to roots of form $\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_l\in S_2(x)$. Suppose first that there is no edge of a rectangle between $x$ and $y$. By structure of $D(P)$, $\lambda_i$ is the number of roots in $S_2(x)$. Applying $\widetilde{F}_i$ $\lambda_i$ times thus replaces each root $\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_l\in S_2(x)$ by $\alpha_i+\alpha_{i+1}+\cdots +\alpha_l$ (see Lemma [\[applyreineke\]](#applyreineke){reference-type="ref" reference="applyreineke"}). Next, suppose that there is an edge which is the bottom right edge of a rectangle between $x$ and $y$. By the structure of $D(P)$, $\lambda_i$ is $1$ more than the number of roots in $S_2(x)$. Applying $\widetilde{F}_i$ $\lambda_i-1$ times thus replaces each root $\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_l\in S_2(x)$ by $\alpha_i+\alpha_{i+1}+\cdots +\alpha_l$ (see Lemma [\[applyreineke\]](#applyreineke){reference-type="ref" reference="applyreineke"}). We must have $c_{i,i+1}=0$, so that the initial symbol in our sequence is a '$-$', and we must have a sequence of form $(-),-,-,\ldots ,-$. From this we can conclude that applying $\widetilde{F}_i$ one more time changes this initial '$-$' (in brackets) into a '$+$', introducing the root $\alpha_i$ into $S(x)$. Finally, suppose there is an edge which is the top left edge of a rectangle between $x$ and $y$. By the structure of $D(P)$, $\lambda_i$ is $1$ less than the number of roots in $S_2(x)$. Applying $\widetilde{F}_i$ $\lambda_i$ times thus replaces each root $\alpha_{i+1}+\alpha_{i+2}+\cdots +\alpha_l\in S_2(x)$ by $\alpha_i+\alpha_{i+1}+\cdots +\alpha_l$ (see Lemma [\[applyreineke\]](#applyreineke){reference-type="ref" reference="applyreineke"}), except for the one with minimal value of $l$. Thus we see that in each case, applying $\widetilde{F}_i$ $\lambda_i$ times replaces $S(x)$ with $S(y)$, proving that our claim is also true for $y$, and we see it is true for all points in the diagram. It follows that Theorem [\[Scorrespondence\]](#Scorrespondence){reference-type="ref" reference="Scorrespondence"} is true. $\square$

\
Thanks are due to Professor R. W. Carter of the University of Warwick, whose help, ideas and discussions were invaluable. The research for this paper was carried out while the author was an EPSRC research assistant of Professor K. A. Brown at the University of Glasgow, Scotland. Part of the work was completed while the author was attending the programme 'Representation Theory of Algebraic Groups and Related Finite Groups' at the Isaac Newton Institute, Cambridge, in 1997. The author is grateful to the referee for some helpful comments on an earlier version of this manuscript. This paper was typeset in LaTeX.

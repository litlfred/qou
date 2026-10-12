---
doc_id: arxiv-2411.04021v1
doc_title: "On the Gram determinants of the Specht modules"
section_id: sec-001-preliminaries
section_title: "Preliminaries"
section_number: null
pages: 3-7
source_pdf: 2411.04021v1.pdf
source_sha256: f5b6980f08d25394
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.871
doc_brief: "On the Gram determinants of the Specht modules — For every partitionλ of a positive integern, letSλ be the corresponding Specht module of the symmetric group Sn, and let det(λ)∈ Z denote the Gram"
---
We fix a positive integer $n$. A *partition* is a sequence $\lambda=(a_1, \dots, a_m)$ of non-negative integers such that $a_1 \geq a_2 \geq \dots \geq a_m$. We identify partitions that only differ by a string of zeros at the end. We say that $\lambda$ is a partition of $n$ if $|\lambda|:= a_1+a_2+ \dots +a_m=n.$ We denote by $\mathscr{P}_n$ the set of partitions of $n$ and by $\mathscr{P}:= \bigcup_{i=0}^{\infty} \mathscr{P}_i$ the set of all partitions. If $\mu=(c_1, \dots, c_l)$ is another partition of $n$, we write $\lambda \trianglelefteq \mu$ and say that $\lambda$ proceeds $\mu$ in the *dominance (partial) order* if and only if $a_1 + \dots +a_i \leq c_1+ \dots +c_i$ for all $i \geq 1$. We denote $$[\lambda]=\{ (i,j) \mid (i,j) \in \mathbb Z \times \mathbb Z, 1 \leq i \leq m, 1 \leq j \leq a_m \}$$ to be the *Young diagram* of $\lambda$, which we can depict as a set of cells with $a_1$ cells in the first row, $a_2$ cells in the second row, and so on, see Figure [1](#Figure1){reference-type="ref" reference="Figure1"}. For a cell $c \in [\lambda]$, we denote the *hook length* $h_{\lambda}(c)$ to be the number of cells in the *hook* of $c$, i.e., the number of cells below and to the right of $c$, including itself. The *hook diagram* of $\lambda$ is the Young diagram, where each cell is filled with its hook length.

<figure id="Figure1" data-latex-placement="ht">
<div class="ytableau">
<p>9 &amp; *(lightgray) 8 &amp; *(lightgray) 7 &amp; *(lightgray) 5 &amp; *(lightgray) 3 &amp; *(lightgray) 2 &amp; *(lightgray) 1<br />
5 &amp; *(lightgray) 4 &amp; 3 &amp; 1<br />
3 &amp; *(lightgray) 2 &amp; 1</p>
</div>
<figcaption>Hook diagram of <span class="math inline">(7, 4, 3)</span>, with the hook of the cell <span class="math inline"><em>c</em> = (1, 2)</span> colored gray.</figcaption>
</figure>

Note that the entries of the first column of a hook diagram uniquely determine the underlying partition. Generalizing that observation, a *sequence of $\beta$-numbers* is a sequence $\beta=(b_1, \dots, b_m)$ of non-negative integers such that all its entries are distinct. For each such sequence, there is a unique $\sigma \in \mathfrak{S}_m$ such that $\beta=(b_{\sigma(1)}, \dots, b_{\sigma(m)})$ is a strictly decreasing sequence, i.e., $b_{\sigma(1)} > b_{\sigma(2)} > \dots > b_{\sigma(m)}$. We define the partition $$\mathrm{Part}(\beta) \coloneqq (b_{\sigma(1)}-m+1,b_{\sigma(2)}-m+2,\dots,b_{\sigma(m)}-m+m)$$ and say that $\beta$ is a sequence of $\beta$-numbers for $\mathrm{Part}(\beta)$. Moreover, we say that $\ell(\beta) \coloneqq m$ is the length of $\beta$ and define $|\beta|:= |\mathrm{Part}(\beta)|$.

Let $\mathscr{B}$ be the set of all sequences of $\beta$-numbers. We define the subsets $$\mathscr{B}_n:= \{ \beta \in \mathscr{B} \mid |\beta|=n \}$$ of the sequences of $\beta$-numbers of $n$ and $$\mathscr{B}(\lambda):= \{ \beta \in \mathscr{B} \mid \mathrm{Part}(\beta)=\lambda \}$$ of the sequences of $\beta$-numbers for the partition $\lambda$.

::: example
Let $\lambda=(7,4,3)$ as in Figure [1](#Figure1){reference-type="ref" reference="Figure1"}. The first column of its hook diagram consists of the sequence $(9,5,3)$, so $(9,5,3)$ is a sequence of $\beta$-numbers for $\lambda$. Further sequences of $\beta$-numbers for $\lambda$ include $(10,6,4,0)$, $(11,7,5,1,0)$ and $(1,0,6,8,12,2)$.
:::

Recall that there is a 1-to-1 correspondence between the partitions $\lambda$ of a positive integer $n$ and the irreducible characters $\chi_{\lambda}$ of the symmetric group $\mathfrak{S}_n$. The following well-known formula gives a convenient way to calculate the degree of each character.

::: proposition
(cf. [@james1981representation Theorem 2.3.21]) []{#DegreeSpechtModule label="DegreeSpechtModule"} Let $\lambda$ be a partition of $n$. Then $$f_{\lambda}:=\chi_{\lambda}(1)=\frac{n!}{\prod_{c \in [\lambda]} h_{\lambda}(c)}.$$ We further set $f_{(0)}:=1$. A partition is said to be odd (resp. even) if and only if $f_{\lambda}$ is odd (resp. even).
:::

We say that a partition $\lambda$ is *$q$-core* for some positive integer $q$ if there is no $c \in [\lambda]$ such that $q \mid h_{\lambda}(c)$. There is a unique partition $\mathrm{core}_q(\lambda)$, which is $q$-core, that can be constructed from $[\lambda]$ by successively removing hooks of cells with hook lengths a multiple of $q$, see also [@james1981representation Section 2.7]. This is where sequences of $\beta$-numbers come into play; removing a hook from a Young diagram corresponds to subtracting a multiple of a unit vector from a sequence of $\beta$-numbers for $\lambda$.

::: example
Let $\lambda=(7,4,3)$. Then $\lambda$ is not $8$-core, as $h_{\lambda}((1,2))=8$. Removing the corresponding hook, we end up with $\mathrm{core}_8(\lambda)=(3,2,1)$.
:::

We shall need a criterion on the parity of $f_{\lambda}$. Let $r$ be the non-negative integer such that $2^r \leq n <2^{r+1}$.

::: lemma
(cf. [@OddLattice Lemma 1]) []{#OddnessPartitions label="OddnessPartitions"} Let $\lambda$ be a partition of $n$. There exists at most one cell $c \in [\lambda]$ such that $h_{\lambda}(c)=2^r$. Moreover, $\lambda$ is odd if and only if such a cell exists and $\mathrm{core}_{2^r}(\lambda)$ is odd.
:::

Let $e_i=(0,0, \dots,0,1,0,\dots)$ be the sequence that has a $1$ in position $i$ and $0$ everywhere else.

::: corollary
[]{#OddnessBetaNumbers label="OddnessBetaNumbers"} Let $\lambda$ be a partition of $n$ and let $\beta_{\lambda} \in \mathscr{B}(\lambda)$. Then there is at most one index $i$ such that $\beta_{\lambda}-2^r e_i \in \mathscr{B}_{n-2^r}$. If such an index, say $j$, exists, then $\beta_{\lambda}-2^r e_j \in \mathscr{B}(\mathrm{core}_{2^r}(\lambda))$.
:::

::: definition
We define the function $D: \mathscr{P} \to \mathscr{P}$ such that for any partition $\lambda$ of $n$, we have $D(\lambda):=\mathrm{core}_{2^r}(\lambda)$. Moreover, we set $D((0)):=(0)$. Denote $D^0(\lambda):=\lambda$ and $D^{m}(\lambda):=D(D^{m-1}(\lambda))$ for any positive integer $m$. We define the *oddness rank* of the partition $\lambda$ by $$\mathrm{OddRank}(\lambda) = \min \{m \in \mathbb Z_{\geq 0} \mid D^{m+1}(\lambda)=D^m(\lambda)\}.$$
:::

::: corollary
Let $\lambda$ be a partition of $n$. Let $n= \sum_{i=0}^r a_i 2^i$ for $a_i \in \{0,1 \}$ be the decomposition of $n$ in binary. Then $\lambda$ is odd if and only if $\mathrm{OddRank}(\lambda)= \sum_{i=0}^r a_i.$
:::

We now define a distance function for the set of partitions, where the distance between two partitions is the minimum number of hooks that must be removed and added to transform one Young diagram into the other.

::: definition
1.  Let $m$ be a positive integer and let $\beta=(b_1,\dots, b_m), \beta'= (b_1',\dots, b_m')\in \mathbb Z^m$. Let $d_m: \mathbb Z^m \times \mathbb Z ^m \to \mathbb Z_{ \geq 0}$ be defined by $$d_m(\beta,\beta')= \# \{i \mid 1 \leq i \leq m, \ b_i \neq b_j' \ \text{for all} \ 1 \leq j \leq m\},$$ i.e., $d_m(\beta,\beta')$ is the number of mismatches of $\beta$ and $\beta'$.

2.  Let $\lambda, \mu$ be partitions. We choose the positive integer $m$ large enough such that there are sequences of $\beta$-numbers $\beta_{\lambda} \in \mathscr{B}(\lambda)$, $\beta_{\mu} \in \mathscr{B}(\mu)$ such that $\ell(\beta_{\lambda})=\ell(\beta_{\mu})=m$. We define the distance $d:\mathscr{P} \times \mathscr{P} \to \mathbb Z_{ \geq 0}$ by $$d(\lambda, \mu):=d_m(\beta_{\lambda},\beta_{\mu}).$$
:::

It is clear that the distance between two partitions is well-defined and that $(\mathscr{P},d)$ is a metric space. Note that for instance if $\lambda$ is a partition of $n$ with $\mathrm{OddRank}(\lambda)>0$, then $d(\lambda, D(\lambda))=1$.

The following definition covers the *odd branches* of a partition, which are the main objects we will work with in this paper.

::: definition
Let $\lambda$ be a partition of $n$.

1.  Let $\mu$ be another partition of $n$. We say that $\mu$ is a branch of $\lambda$ if $\lambda \trianglelefteq \mu$ and $d(\lambda, \mu)=2$. Let $\mathscr{P}_{\lambda}$ be the set of branches of $\lambda$.

2.  Let $\mu$ be a branch of $\lambda$ and let $\beta_{\lambda} \in \mathscr{B}(\lambda)$ (resp. $\beta_{\mu} \in \mathscr{B}(\mu)$) with $$\beta_{\lambda}=(b_1,b_2,b_3, \dots, b_m), \
    \beta_{\mu}=(b_1',b_2',b_3, \dots, b_m),$$ such that $b_1>b_2$, $b_1'>b_2'$. We define $$h_{\lambda}^1(\mu):=b_1-b_2'=b_1'-b_2, \
    h_{\lambda}^2(\mu):=b_2-b_2'=b_1'-b_1.$$ Note that there are two cells $c_1=(k,j), c_2 =(l,j) \in [\lambda]$ with $k<l$ such that $h_{\lambda}(c_i)=h_{\lambda}^i(\mu)$ for $i=1,2$. Also, $(b_1,b_2',b_3, \dots, b_m) \in \mathscr{B}$ and the associated partition corresponds to removing the hook of $c_2$ from the Young diagram of $\lambda$.

3.  We define $$\mathscr{P}_{\lambda}^{\mathrm{odd}}:=   \{ \mu \in \mathscr{P}_{\lambda} \mid  \mu \ \textit{is odd}  \}$$ to be the set of odd branches of $\lambda$.
:::

We are now ready to give the formula for the Gram determinant of a Specht module:

::: theorem
(cf. [@JamesMurphyFormula]) []{#James-Murphy Formula label="James-Murphy Formula"} Let $\lambda$ be a partition of $n$. The Gram determinant of the canonical bilinear form with respect to the standard basis of the Specht module $S^{\lambda}$ is given by $$\det(\lambda) :=\prod_{\mu \in \mathscr{P}_{\lambda}} \left( \frac{h_{\lambda}^1(\mu) }{h_{\lambda}^2(\mu)} \right)^{\varepsilon_{\mu} f_{\mu}} \in \mathbb{Z},$$ where $\varepsilon_{\mu} \in \{-1,1 \}$. For any prime $p$, we define the integer $a_{\lambda}^{(p)}$ such that $$\det(\lambda)=m \cdot p^{a_{\lambda}^{(p)}},$$ where $m$ is coprime to $p$.
:::

::: remark
[]{#RemarkDeterminantFormula label="RemarkDeterminantFormula"} We denote $(\mathbb{Q}^{\times})^2:= \{ x^2 \mid x \in \mathbb Q^{\times}  \}$ to be the set of invertible rational squares. Let $\lambda$ be an even partition of $n$ and let $\chi_{\lambda}$ be the character corresponding to $\lambda$. The orthogonal determinant $\det(\chi_{\lambda}) \in \mathbb{Q}^{\times}/(\mathbb{Q}^{\times})^2$ in the sense of [@NebeOrtDet] is defined to be the rational square class of the Gram determinant of any $\rho(\mathfrak{S}_n)$-invariant, non-degenerate, symmetric bilinear form of any rational representation $\rho$ affording the character $\chi_{\lambda}$. The obvious choice is the canonical bilinear form for the Specht module $S^{\lambda}$, and we arrive at $$\det(\chi_{\lambda})= \det(\lambda) \cdot (\mathbb{Q}^{\times})^2= \prod_{\mu \in \mathscr{P}_{\lambda}^{\mathrm{odd}}} \frac{h_{\lambda}^1(\mu) }{h_{\lambda}^2(\mu)}  \cdot (\mathbb{Q}^{\times})^2.$$
:::

::: example
[]{#Example21111331 label="Example21111331"} Let $\lambda=(2,1^{(5)})$ and let $\mu=(3,3,1)$ be two partitions of $7$. Clearly, $\lambda \trianglelefteq \mu$ in the dominance order.

We choose $\beta_{\lambda}:=(7,5,4,3,2,1)$ and $\beta_{\mu}=(8,7,4,2,1,0)$ for the sequences of $\beta$-numbers for $\lambda$ and $\mu$, respectively. Comparing the two sequences, we see that there are two mismatches, so $d(\lambda, \mu)=d_6(\beta_{\lambda}, \beta_{\mu})=2$. So $\mu$ is in fact a branch of $\lambda$; we calculate that $h_{\lambda}^1(\mu)=5$ and $h_{\lambda}^2(\mu)=3$.

It is easily seen that $\mu$ is odd; indeed, $D(\mu)=(3)$ and $f_{(3)}=1$, so the oddness follows by Lemma [\[OddnessPartitions\]](#OddnessPartitions){reference-type="ref" reference="OddnessPartitions"}. In particular, $\mu$ is an odd branch of $\lambda$. With the same reasoning we see that $\lambda$ is even, since $D(\lambda)=(2,1)$ and $(2,1)$ is $2$-core.

We further observe that $\mathscr{P}_{\lambda}^{\mathrm{odd}}= \{\mu, (7), (5,1,1), (3,1^{(4)}) \}$ and thus arrive at $$\det(\chi_{\lambda})= \frac{5}{3} \cdot \frac{7}{5} \cdot \frac{7}{3} \cdot \frac{7}{1} \cdot (\mathbb{Q}^{\times})^2= 7 \cdot (\mathbb{Q}^{\times})^2.$$
:::

<figure id="Figure2" data-latex-placement="ht">
<div class="ytableau">
<p>7 &amp; 1<br />
5<br />
4<br />
3<br />
2<br />
1</p>
</div>
<p>        </p>
<div class="ytableau">
<p>5 &amp; 3 &amp; 2<br />
4 &amp; 2 &amp; 1<br />
1</p>
</div>
<figcaption>Hook diagrams of <span class="math inline">(2, 1<sup>(5)</sup>)</span> and <span class="math inline">(3, 3, 1)</span>.</figcaption>
</figure>

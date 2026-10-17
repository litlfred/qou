---
doc_id: arxiv-2203.06568v4
doc_title: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-4
source_pdf: 2203.06568v4.pdf
source_sha256: 256fcfb588dac554
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.924
doc_brief: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra — We study the upper bounds for A(n, d), the maximum size of codewords with length n and Hamming distance at least d."
---
In coding theory, one of the classical problems is to determine $A(n, d)$, the maximum size of a binary $(n,d)$ code with length $n$ and minimum distance at least $d$. The (Hamming) distance distribution of a code is considered since the MacWilliams identities provide a linear relation between the distance distribution and its transform [@MS77]. With this linear relation, the maximum possible size of a code can be formulated as a linear programming problem. Delsarte showed that the transform of the distance distribution is nonnegative and used linear programming techniques to derive upper bounds on $A(n, d)$ [@Del73].

Schrijver considered the distance relations among triplets of codewords and derived positive-semidefinite relations based on the Terwilliger algebra of Hamming scheme [@Sch05]. Thus one can formulate a semidefinite program (SDP) on the maximum possible size of a code and derive a semidefinite programming bound on the size of a binary code. Several linear programming upper bounds on $A(n,d)$ are improved since Schrijver's semidefinite constraints imply Delsarte's linear inequalities [@Sch05] by diagonalizing certain positive semidefinite matrices derived from Schrijver's semidefinite constraints in the Bose-Mesner algebra.

This method was later extended to nonbinary codes by Gijswijt, Schrijver, and Tanaka [@GST06]. Gijswijt, Mittelmann, and Schrijver further studied the distance relations among quadruples of codewords and generalized Schrijver's SDP [@GMS12], called quadruple SDP, which improved many upper bounds for $A(n,d)$. Although an SDP based on the distance relations of $m$-tuple codewords for any $m$ is studied, an SDP based on quadruple distances has already many variables, leading to high computation complexity.

On the other hand, there are several known linear constraints for binary codes, including Delsarte's inequalities [@Del73], the ones derived by Best [@Bes80] and Mounits, Etzion and Litsyn [@MEL02], which can be used to strengthen linear programming or semidefinite programming bounds on $A(n,d)$. Moreover, Kim and Toan proved additional linear constraints on the variables of Schrijver's SDP and improved upper bounds on $A(18, 8)$ and $A(19, 8)$ [@KT13]. Then, $A(18, 8) = 64$ has later been settled by Östergård [@Ost19] by using a computer-aided search.

The $A(n,d)$ problem can be regarded as finding the maximum number of an independent set of a graph as follows. Let $E$ be a graph with $2^n$ vertices corresponding to all the binary vectors of length $n$. There is an edge between two binary vectors if their Hamming distance is less than $d$. Now an $(n,d)$ code corresponds to an independent set of $E$. Consequently, Delsarte's linear programming bound can be viewed an upper bound on the independent number of $E$. Moreover, this bound can be extended to serve as an upper bound on the independent number an arbitrary graph [@Sch79]. Based on this connection, Laurent gave a hierarchy for semidefinite programming bounds on $A(n, d)$ and proposed strengthened bounds [@Lau07], which improve bounds on $A(20, 8)$ and $A(25, 6)$.

Upper bounds for several related coding problems in various spaces can also be derived using semidefinite programming techniques. For instance, Bachoc and Vallentin studied SDPs for codes in Hamming balls, projective spaces and spherical codes (kissing number problems) [@Bac10; @BV08]. Barg and Yu also used semidefinite programming techniques to obtain better upper bounds for spherical two-distance sets and equiangular lines [@BY13; @BY14].

In this paper, we would like to study Schrijver's SDP and derive additional semidefinite constraints. One can define a split distance distribution of a code, and derive a split version of Delsarte's inequalities, which provide subtler linear constraints [@Sim95]. Recently, split Hamming weight distributions and their MacWilliams identities have been studied in various quantum codes [@LHL16; @LA18; @ALB20]. It has been demonstrated that linear programming bounds on quantum codes can be improved with additional constraints from split MacWilliams identities [@LA18].

Inspired by the effects of split distance or weight distributions in linear programming, we would like to study a similar notion in Schrijver's SDP. Consider a partition of the support of a code with two subsets. We define a split Terwilliger algebra with respect to the partition. Similar to the derivation of Schrijver's semidefinite constraints, we show that this split Terwilliger algebra can be block-diagonalized to derive finer positive-semidefinite constraints. Moreover, we show that these split Schrijver's semidefinite constraints also imply corresponding split Delsarte's inequalities, and hence they are natural generalizations of Schrijver's constraints. Together with Schrijver's semidefinite constraints and the known linear constraints in the literature, we have a strengthened SDP on $A(n,d)$. In particular, we improve the semidefinite programming bound on $A(18,4)$ to $6551$, while the previously known upper bound is $6552$, by linear programming with Delsarte's inequalities and Best's inequalities [@Bes80]. The number has not been updated since more than four decades ago [@BBMOS_1987; @Brouwer]. The numerical error of this SDP program can be pessimistically estimated from its dual SDP as suggested by Gijswijt [@Gij05]. Using this method, we are able to verify that $A(18,4) \leq 6551$.

One of our semidefinite constraint $R_{s}$ can be derived from the quadruple SDP. It is not clear whether the other semidefinite constraint on $R_{s}'$ obtained by a split Terwilliger algebra is included in the constraints of the quadruple SDP as well. However, in our experiment, we are able to improve the bound $A(18,4)$ over the quadruple SDP in [@GMS12].

All the results and proofs can be generalized to a split Terwilliger algebra on $m$ subsets of a partition with $m \leq n$ (called *$m$-split Terwilliger algebra*), from which we may derive more additional positive-semidefinite constraints. However, this $m$-split Terwilliger induces an SDP with $O((\frac{n}{m})^{3m})$ variables and may not be practical in implementation with large $m$.

Finally, we mention $m$-split Terwilliger algebras for the Hamming scheme, which might allow us to apply our method to other association schemes. To implement an SDP program, one of the key points is to block diagonalize the algebra in use and Gijswijt has developed a general method to handle this problem [@Gij09]. Gijswijt's method was refined and extended to nonbinary codes by Litjens, Polak and Schrijver [@LPS17]. Moreover, the method can be further generalized to the groups of the form $(G^{n_{1}} \rtimes S_{n_{1}}) \times \cdots \times (G^{n_{m}} \rtimes S_{n_{m}})$ with $\sum_{i = 1}^{m}n_{m} = n$ and $S_{n_{i}}$ are symmetric groups [@Pol19_1]. Together with those approaches, one can calculate the block diagonalization formula of split Terwilliger algebras in various types of codes, such as constant-weight codes and nonbinary codes with Hamming or Lee distances.

The paper is organized as follows. We introduce the Terwilliger algebra of the Hamming scheme and Schrijver's SDP. In Section [\[sec:split\]](#sec:split){reference-type="ref" reference="sec:split"} we define a split Terwilliger algebra and derive semidefinite constraints. Then we provide our SDP together with the linear constraints in the literature in Section [\[sec:SDP\]](#sec:SDP){reference-type="ref" reference="sec:SDP"}. A generalization of the method on $m$-split Terwilliger algebra is given in Section [\[sec:gener\]](#sec:gener){reference-type="ref" reference="sec:gener"}. Finally, we conclude our work in Section [\[sec:conslus\]](#sec:conslus){reference-type="ref" reference="sec:conslus"}.

# Terwilliger algebra and Schrijver's SDP

Let ${\cal P}$ be the power set of $\{1, \dots, n\}$. A binary code $C$ is a subset of ${\mathcal P}$. For $X,Y \in {\mathcal P}$, denote $$X\Delta Y= \{a\in\{1,\dots,n\}: a\in (X \setminus Y) \cup (Y \setminus X) \}.$$ Let $\lvert S \rvert$ denote the size of a set $S \in {\mathcal P}$. Hence the (Hamming) distance of $X$ and $Y \in {\mathcal P}$ is $\lvert X \Delta Y \rvert$. The distance distribution of the code $C$ is $$A_{j} = \frac{1}{\lvert C \rvert} \sum_{x \in C}\{ y \in C : \lvert x \Delta y \rvert = j\} \label{eq:dist_distriubtion}$$ for $j=0,\dots, n$. The minimum distance $d$ of $C$ is the minimum Hamming distance of two distinct elements in $C$ and hence $$d= \min\{j>0: A_j>0\}.$$ Note that for $\lvert C \rvert \leq 1$, its minimum distance is defined to be $\infty$. $C$ is said to be an $(n,d)$ code if $C$ has minimum distance $d$ and length $n$. See more details about codes in [@MS77].

We review the Terwilliger algebra of the Hamming scheme [@Ter92; @Ter93; @BBIT21]. Let $G$ be the group of all distance-preserving automorphisms of ${\cal P}$. Consider the action of $G$ on ${\cal P} \times {\cal P}$ defined by $g(X, Y) = (g X, g Y)$ for $g \in G$ and $(X, Y) \in {\cal P} \times {\cal P}$ with orbits ${\cal O}_{1}, \dots, {\cal O}_{m}$ for some $m$. For each ${\cal O}_{u}$, we define a $\lvert {\cal P} \rvert \times \lvert {\cal P} \rvert$ matrix $M_{{\cal O}_{u}}$, indexed by the elements in ${\mathcal P}$, as $$(M_{{\cal O}_{u}})_{X, Y} = \left\{
    \begin{aligned}
        &1, \text{ if } (X, Y) \in {\cal O}_{u};\\
        &0, \text{ otherwise.}
    \end{aligned} \right.$$ Observe that $(X, Y)$ and $(U, V)\in {\cal P} \times {\cal P}$ belong to the same orbit if and only if there is an automorphism $g\in G$ such that $gX = U$ and $gY = V$, that is, if and only if $\lvert X \rvert = \lvert U \rvert,$ $\lvert Y \rvert = \lvert V \rvert,$ $\lvert X \Delta Y \rvert = \lvert U \Delta V \rvert$. Thus, $M_{{\cal O}_{u}}$ can be rewritten as $$(M_{i, j}^{t})_{X, Y} = \left\{
    \begin{aligned}
        &1, \text{ if } \lvert X \rvert = i, \lvert Y \rvert = j, \lvert X \cap Y \rvert = t;\\
        &0, \text{ otherwise,}
    \end{aligned} \right.$$ where each orbit ${\cal O}_{u}$ is represented by some $(i,j,t)$ for $i, j, t \in \{0, \dots, n\}$ with $i+j-2t \in \{0, \dots, n\}$. Let ${\cal A}_{n}$ be the collection of all linear combinations of $\{M_{i, j}^{t}\}$ over the complex field $\mathbb{C}$. Then ${\cal A}_{n}$ is closed under matrix multiplication and adjoint. Moreover, ${\cal A}_{n}$ is a $\mathbb{C}^{*}$-algebra, called the *Terwilliger algebra* of the Hamming scheme. ${\cal A}_{n}$ is finitely generated with dimension $\binom{n+3}{3}$.

Schrijver described a block diagonal formula for the Terwilliger algebra of the Hamming scheme.

::: theorem
[@Sch05 Theorem 1] []{#thm:ter_blo label="thm:ter_blo"} There is an isomorphism from ${\cal A}_{n}$ to $\bigoplus_{k = 0}^{\lfloor \frac{n}{2} \rfloor} \mathbb{C}^{(n-2k+1) \times (n-2k+1)}$ that maps $A = \sum_{i, j, t}x_{i, j}^{t}M_{i, j}^{t} \in {\cal A}_{n}$ to $\bigoplus_{k = 0}^{\lfloor \frac{n}{2} \rfloor} B_{k}$, where $$B_{k} = \left( \sum_{t} \binom{n-2k}{i-k}^{-\frac{1}{2}} \binom{n-2k}{j-k}^{-\frac{1}{2}} \beta_{i, j, k}^{t} x_{i, j}^{t} \right)_{i, j = k}^{n-k}$$ with $$\beta_{i, j, k}^{t} = \sum_{u = 0}^{n} (-1)^{u-t} \binom{u}{t} \binom{n-2k}{u-k}\binom{n-k-u}{i-u}\binom{n-k-u}{j-u}.$$
:::

The formula says ${\cal A}_{n}$ as the direct sum of matrices. Therefore, we can represent the elements of ${\cal A}_{n}$ on a computer with a minimal memory.

Now, Schrijver's semidefinite constraints for a nontrivial code $C$ [@Sch05] can be derived as follows. Consider the action of $G$. Let $\Pi = \{\pi \in G \mid \emptyset \in \pi(C)\}$ and $\Pi' = \{\pi \in G \mid \emptyset \notin \pi(C)\}$. Let $\chi^{\pi(C)}$ be the incidence vector (as a column vector) of $\pi(C)$ indexed by ${\cal P}$. Define $\lvert {\cal P} \rvert \times \lvert {\cal P} \rvert$ matrices $$\begin{aligned}
    &R = \frac{1}{\lvert \Pi \rvert} \sum_{\pi \in \Pi} \chi^{\pi(C)} (\chi^{\pi(C)})^{T}, \\
    &R' = \frac{1}{\lvert \Pi' \rvert} \sum_{\pi \in \Pi'} \chi^{\pi(C)} (\chi^{\pi(C)})^{T}.
\end{aligned}$$ It is obvious that $R$ and $R'$ are positive semidefinite. Let $$x_{i, j}^{t} = \frac{1}{\lvert C \rvert \binom{n}{i-t, j-t, t}} \lambda_{i, j}^{t},$$ where

$\binom{n}{a, b, c} = \frac{n!}{a!b!c!}$ for $a, b, c \geq 0$ with $a+b+c \leq n$, and

$$\begin{aligned}
    \lambda_{i, j}^{t} = &\lvert \{ (X, Y, Z) \in C^{3} : \lvert X \Delta 
    Y \rvert = i, \lvert X \Delta Z \rvert = j, \lvert (X \Delta Y) \cap (X \Delta Z)\rvert = t\}\rvert,
\end{aligned}$$ for each $i, j, t \in \{0, \dots, n\}$ with $i-t \geq 0$, $j-t \geq 0$, and $i+j-2t \leq n$. $\lambda_{i, j}^{t}$ counts the number of triple codewords in $C$ satisfying certain distance relations. The following proposition says that $R,R'\in{\mathcal A}_n$.

::: proposition
[@Sch05 Proposition $1$] $$\begin{aligned}
        & R = \sum_{i, j, t} x_{i, j}^{t} M_{i, j}^{t} \text{ and }\\
        & R' = \frac{\lvert C \rvert}{2^{n}-\lvert C \rvert}\sum_{i, j, t}(x_{i+j-2t, 0}^{0}-x_{i, j}^{t})M_{i, j}^{t}.
    
\end{aligned}$$
:::

By Theorem [\[thm:ter_blo\]](#thm:ter_blo){reference-type="ref" reference="thm:ter_blo"}, $R$ and $R'$ are positive semidefinite if and only if for $k = 0, \dots, \lfloor \frac{n}{2} \rfloor$, the following matrices $$\begin{aligned}
    & \left( \sum_{t} \binom{n-2k}{i-k}^{-\frac{1}{2}} \binom{n-2k}{j-k}^{-\frac{1}{2}} \beta_{i, j, k}^{t} x_{i, j}^{t} \right)_{i, j = k}^{n-k}, \label{sdp_1}\\
    & \left( \sum_{t} \binom{n-2k}{i-k}^{-\frac{1}{2}} \binom{n-2k}{j-k}^{-\frac{1}{2}} \beta_{i, j, k}^{t} (x_{i+j-2t, 0}^{0}-x_{i, j}^{t}) \right)_{i, j = k}^{n-k} \label{sdp_2}
\end{aligned}$$ are positive semidefinite. Schrijver also showed that $x_{i,j}^t$ satisfy the following constraints.

::: proposition
[@Sch05] []{#pro:sch label="pro:sch"} Let $C$ be a code with length $n$ and minimum distance at least $d$. Then $x_{i, j}^{t}$'s corresponding to $C$ satisfy the following constraints: $$\begin{array}{cl}
            \mbox{(i)}     &  x_{0, 0}^{0} = 1;\\
            \text{(ii)}    & 0 \leq x_{i, j}^{t} \leq x_{i, 0}^{0};\\
            \text{(iii)}    & x_{i,0}^{0} + x_{j,0}^{0} \leq  1+x_{i, j}^{t};\\
            \text{(iv)}    & x_{i, j}^{t} = x_{i', j'}^{t'}  \mbox{ if } (i, j, i+j-2t) \mbox{ is a permutation of } (i', j', i'+j'-2t');\\
            \text{(v)}    & x_{i, j}^{t} = 0 \mbox{ if }\{i, j, i+j-2t\} \cap \{1, \dots, d-1\} \neq \emptyset;
        \end{array} \label{sdp_3}$$ Also, we have $$\lvert C \rvert = \sum_{i}\binom{n}{i}x_{i, 0}^{0}.$$
:::

Note that $\{\binom{n}{i}x_{i, 0}^{0}\}$ is the distance distribution of $C$. Constraints (i) and (iv) are from the definition directly. Consider $\lvert X \rvert = i$ and $\lvert Y \rvert = j$ and then we have $$\begin{aligned}
    &(R)_{X,X} = x_{i, i}^{i} = x_{i, 0}^{0}, \quad (R)_{X,Y} = x_{i, j}^{t}.
\end{aligned}$$ The first inequality of Constraint (ii) follows because of the non-negativity of $\lambda_{i,j}^t$ and the second inequality is because $R$ is positive semidefinite and a diagonal element of a positive semidefinite matrix would dominate its row entries. Constraint (iii) can be similarly derived from $(R)_{X,X}'\geq (R)_{X,Y}'$ and (iv). To see this, we consider $\lvert X \rvert = i$ and $\lvert Y \rvert =j'= i+j-2t$ at $t'= i-t$. Then $$\begin{aligned}
    &  (R')_{X, X} = x_{0, 0}^{0} - x_{i, 0}^{0}, \\
    & (R')_{X, Y} = x_{i+j'-2t', 0}^{0} - x_{i, j'}^{t'}= x_{j, 0}^{0} - x_{i, i+j-2t}^{i-t}= x_{j, 0}^{0} - x_{i, j}^{t},
\end{aligned}$$ where $x_{i, i+j-2t}^{i-t}=  x_{i, j}^{t}$ is because of (iv). Constraint (v) is the requirement from the minimum distance of the code. To sum up, Schrijver's SDP is as follows with variables $x_{i, j}^{t} \in\mathbb{R}$: $$\begin{aligned}
    {\rm maximize}&\sum_{i}\binom{n}{i}x_{i, 0}^{0}  \notag\\
    {\rm subject\ to\ }       &  \mbox{ positive semidefiniteness of }(\ref{sdp_1}) \mbox{ and } (\ref{sdp_2})\notag\\
    &(\ref{sdp_3}).    \notag
\end{aligned}$$

---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-011-44-higher-order-expansion-for-free-cumulants
section_title: "Higher order expansion for free cumulants"
section_number: 4.4
pages: 33-42
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.986
---
[]{#sec:evercrossing label="sec:evercrossing"}

In this section we present a method of enumerating all evercrossing partitions with a given genus. The main concept is to simplify a given evercrossing partition by a number of steps. After these simplifications we obtain an evercrossing pair partition (with some extra properties) which can be enumerated easily. By reversing the process of simplifications we shall therefore obtain all evercrossing partitions with a given genus.

### Simplification, step 1 {#subsec:simple1}

Let an evercrossing partition be given. In the first step we remove all its trivial blocks. For example, Figure [1](#fig:wynikstep1){reference-type="ref" reference="fig:wynikstep1"} depicts the outcome of this step performed on an evercrossing partition from Figure [\[fig:evercrossing\]](#fig:evercrossing){reference-type="ref" reference="fig:evercrossing"}. In fact we do not really care what are the labels of vertices and it would be a good idea not to write them down at all; in this example we do write them down for the reason of clarity.

<figure id="fig:wynikstep1">
<embed src="figure18.eps" />
<figcaption>Partition from Figure <a href="#fig:evercrossing" data-reference-type="ref" data-reference="fig:evercrossing">[fig:evercrossing]</a> after the first step of the simplification algorithm.</figcaption>
</figure>

### Simplification, step 2

In the second step of simplification, we consider the fat partition corresponding to the outcome of the first step (cf example on Figure [2](#fig:wynikstep2){reference-type="ref" reference="fig:wynikstep2"}). In other words, we perform the operation depicted on Figure [3](#fig:step2elementary){reference-type="ref" reference="fig:step2elementary"} on each of the blocks.

<figure id="fig:wynikstep2">
<embed src="figure19.eps" />
<figcaption>Partition from Figure <a href="#fig:evercrossing" data-reference-type="ref" data-reference="fig:evercrossing">[fig:evercrossing]</a> after the second step of the simplification algorithm.</figcaption>
</figure>

<figure id="fig:step2elementary">
<embed src="figure20.eps" />
<figcaption>Elementary operation of step 2 of the simplification algorithm: one of the blocks is replaced by its fat version.</figcaption>
</figure>

### Simplification, step 3 {#subsec:simple3}

The outcome of the second step is a pair partition. In the third step of the simplification algorithm we perform the operation depicted on Figure [4](#fig:step3){reference-type="ref" reference="fig:step3"}. To be precise: for $n\geq 2$ let $(p_1,\dots,p_n)$ and $(q_n,q_{n-1},\dots,q_1)$ be two sequences of consecutive vertices of this pair partition such that $p_k$ is connected with $q_k$. We remove all vertices $p_2,p_3,\dots,p_n,q_2,q_3,\dots,q_n$ and leave vertices $p_1$ and $q_1$ unchanged. We iterate this removal of vertices as long as it is possible (cf example on Figure [5](#fig:wynikstep3){reference-type="ref" reference="fig:wynikstep3"}).

![The elementary operation of step 3 of the simplification algorithm: a number of parallel lines is replaced by a single one.](figure21.eps){#fig:step3}

![The outcome of the step 3 of the simplifying algorithm for partition from Figure [\[fig:evercrossing\]](#fig:evercrossing){reference-type="ref" reference="fig:evercrossing"}.](figure22.eps){#fig:wynikstep3}

A careful reader might observe that after rotating the Figure [4](#fig:step3){reference-type="ref" reference="fig:step3"} upside--down the roles played by $p_1$, $q_1$ are interchanged with $q_n$ and $p_n$ therefore the above rule is not very precise which labels should be carried by the vertices of the surviving block; but in fact we do not really care about these labels. In particular, we do not care which of the labels is the smallest, therefore we identify pair partitions which are cyclic rotations of each other.

### Outcome of the simplification algorithm

::: theorem
[]{#theo:gorneszacowanie label="theo:gorneszacowanie"} The outcome of the simplification algorithm from Sections [0.0.1](#subsec:simple1){reference-type="ref" reference="subsec:simple1"}--[0.0.3](#subsec:simple3){reference-type="ref" reference="subsec:simple3"} is an evercrossing pair--partition which has the same genus and free index as the original partition.

Let $n$ denote the number of vertices of the outcome pair partition $\pi$. If $\mathop{\mathrm{genus}}_\pi\neq 0$ then $$n\leq 12 \mathop{\mathrm{genus}}_{\pi}-6. \label{eq:szacowanie}$$
:::

::: proof
*Proof.* In order to show that all three steps of the simplification algorithm preserve the genus of a partition, it is enough to notice that the surface without the boundary we constructed in Section [\[subsec:zaklejanie\]](#subsec:zaklejanie){reference-type="ref" reference="subsec:zaklejanie"} changes in each of the steps into a homeomorphic one.

We shall prove now that all three steps preserve the free index of a partition. Let $\pi$ be a partition of some set $X$, let $x\notin
X$, then $\pi'=\pi\cup \{ x \}$ is a partition of the set $X \cup
\{x\}$ which has an additional trivial block. Observe that every partition $\rho'\leq \pi'$ must have a form $\rho'=\rho \cup \big\{
\{x\} \big\}$ where $\rho\leq\pi$. Therefore $$I_{\pi'}=\sum_{\substack{ \rho'\in\mathop{\mathrm{NC}}(X \cup \{x\}) \\ \rho'\leq \pi'}} \mathop{\mathrm{Moeb}}_{\rho'} =
\sum_{\substack{ \rho\in\mathop{\mathrm{NC}}(X) \\ \rho\leq \pi}} \mathop{\mathrm{Moeb}}_{\rho} =
I_{\pi}.$$ It follows that two partitions which differ with one trivial block have the same free index and, by iterating, the first step preserves the free index.

The second and the third step can be divided into a number of elementary operations

(for the second step the elementary operation is the replacement of only one of the blocks of the original partition by the corresponding 'fat block', cf Figure [3](#fig:step2elementary){reference-type="ref" reference="fig:step2elementary"}, for the third step the elementary operation is the performance of only one operation from Figure [4](#fig:step3){reference-type="ref" reference="fig:step3"}). Our goal is to prove that every elementary operation preserves the free index. Let $\pi$ be a partition and let $\pi'$ be an outcome of one of the elementary operations performed on $\pi$. We can decompose $\pi=\sigma \cup
\tau$, $\pi'=\sigma'\cup\tau$ (we use the notations of Lemma [\[lem:fundamentalny\]](#lem:fundamentalny){reference-type="ref" reference="lem:fundamentalny"}), where $\tau\in\mathop{\mathrm{P}}(T)$ is the set of blocks of $\pi$ not changed by the elementary operation. One can easily check that for both elementary operations $\sigma\in\mathop{\mathrm{NC}}(S)$ and $\sigma'\in\mathop{\mathrm{NC}}(S')$ are non--crossing partitions, furthermore for every $\rho\in\mathop{\mathrm{P}}(T)$ we have that $(\sigma \wedge
\rho_{\mathop{\mathrm{comp}}})\in\mathop{\mathrm{NC}}(S)$ is trivial if and only if $(\sigma' \wedge
\rho_{\mathop{\mathrm{comp}}})\in\mathop{\mathrm{NC}}(S')$ is trivial. From Lemma [\[lem:fundamentalny\]](#lem:fundamentalny){reference-type="ref" reference="lem:fundamentalny"} applied to $\pi$ and $\pi'$ it follows that

$$I_{\pi}=\sum_{\substack{\rho\in\mathop{\mathrm{NC}}(T), \\ \rho\leq \tau,
\\ (\sigma \wedge \rho_{\mathop{\mathrm{comp}}}) \text{ is trivial}  }}
  \mathop{\mathrm{Moeb}}_{\rho}=
\sum_{\substack{\rho\in\mathop{\mathrm{NC}}(T), \\ \rho\leq \tau,
\\ (\sigma' \wedge \rho_{\mathop{\mathrm{comp}}}) \text{ is trivial}  }}
  \mathop{\mathrm{Moeb}}_{\rho}= I_{\pi'}$$

and hence both elementary operations preserve the free index.

Observe also, that the first and the third step of the algorithm preserve clearly the partition property of being evercrossing. It should be clear from the graphical interpretation that also the second step preserves this property; nevertheless we provide a more detailed proof below. Let a partition $\pi$ be an outcome of the first step of the algorithm. Any pair connected by $\pi_{\mathop{\mathrm{fat}}}$ must be of the form $(\pi_{s,t}', \pi_{s,t+1})$ (we use the notation from Section [\[subsec:fat\]](#subsec:fat){reference-type="ref" reference="subsec:fat"}). As an outcome of the first step of the simplification algorithm, $\pi$ contains no trivial blocks hence $\pi_{s,t}\neq \pi_{s,t+1}$. Since $\pi$ is evercrossing, there exist $b,d\in\pi_{u}$, $u\neq s$, such that $\pi_{s,t},b,\pi_{s,t+1},d$ are ordered up to a cyclic rotation. In other words: on the graphical representation on a circle, elements of the block $\pi_u$ are not all on the same side of the line which passes through $\pi_{s,t}$ and $\pi_{s,t+1}$. Therefore there must be some consequent elements $\pi_{u,v}$, $\pi_{u,v+1}$ of the block $\pi_u$ such that $\pi_{s,t},\pi_{u,v},\pi_{s,t+1},\pi_{u,v+1}$ are ordered up to a cyclic rotation. It is easy to see that $b=\pi_{u,v}'$ and $d=\pi_{s,t+1}$ are the vertices required by the property of $\pi_{\mathop{\mathrm{fat}}}$ to be evercrossing.

Let $\pi$ be the outcome of the simplification algorithm and such that $\mathop{\mathrm{genus}}_{\pi}\neq 0$. We keep notation from Section [\[subsec:zaklejanie\]](#subsec:zaklejanie){reference-type="ref" reference="subsec:zaklejanie"}, i.e. $r=\frac{n}{2}$ denotes the number of blocks of $\pi$ and $t$ denotes the number of cycles of $\pi_{\mathop{\mathrm{fat}}}\circ c$ (or, alternatively, the number of holes after gluing the first collection of discs). Observe that on the boundary of every hole there must be at least three intervals which touch some discs from the first collection (if some hole does not touch any discs then $\pi=\emptyset$ and $\mathop{\mathrm{genus}}_{\pi}=0$; if some hole touches only one disc we denote by $a$, $c$ the only two vertices which are on the boundary of the hole and clearly $(a,c)$ is a pair of vertices required for $\pi$ to be non--evercrossing; if some hole touches exactly two discs then it is possible to perform some simplifications of step 3; a careful reader might observe that it is possible and perfectly legal for a hole to touch some of the discs twice, cf the left--hand side partition on Figure [8](#fig:zwyczajninadzwyczajni){reference-type="ref" reference="fig:zwyczajninadzwyczajni"}). Since $\pi$ is a pair partition, every disc of the first collection touches the holes on exactly two intervals. It follows that $n= 2r \geq 3t$. Equation [\[eq:genus\]](#eq:genus){reference-type="eqref" reference="eq:genus"} implies that $$n \leq 12 \mathop{\mathrm{genus}}_{\pi}-6$$ which finishes the proof. ◻
:::

### Interpretation of the free index?

Free index of a partition is a quite strange combinatorial object. We can think that it measures how far a given partition is away from non--crossing partitions or how much it is evercrossing. Its particularly interesting feature appears in Theorem [\[theo:gorneszacowanie\]](#theo:gorneszacowanie){reference-type="ref" reference="theo:gorneszacowanie"}, namely that it is being preserved by a number of operations one can perform on a partition. The list of such operations is far from being complete and we leave it as an exercise to the reader to find at least one such operation which does not appear in the simplification algorithm. Suppose we have completed such a list of natural operations preserving free index; now we can treat them as analogues of Reidemeister moves in the knot theory and say that two partitions are isotopic when one can be obtained from another by a sequence of such elementary operations. Of course free index will be an invariant of the isotopy class but we should not expect that it will always be able to distinguish different isotopy classes. A question arises: is there some natural (geometric?) interpretation of such isotopy?

## The second main result: the second--order expansion of free cumulants and characters {#sec:secondorderexp}

### Evercrossing partitions with genus $1$

Theorem [\[theo:gorneszacowanie\]](#theo:gorneszacowanie){reference-type="ref" reference="theo:gorneszacowanie"} allows us to enumerate (in finite time) all possible outcomes of the simplifying algorithm for a fixed genus of the original evercrossing partition. By reversing all three steps of the simplifying algorithm we are able to write a number of "templates" which describe all evercrossing partitions with a prescribed genus. Let us have a look on an example.

::: theorem
[]{#theo:klasyfikacja label="theo:klasyfikacja"} Every evercrossing partition with genus $1$ must be either of the form depicted on Figure [6](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} (in this case it has the free index equal to $-1$) or Figure [7](#fig:gwiazdadawida){reference-type="ref" reference="fig:gwiazdadawida"} (in this case it has the free index equal to $-2$). On both figures only non--trivial blocks were shown.

<figure id="fig:krzyz">
<embed src="figure23.eps" />
<figcaption>General pattern of evercrossing partitions with genus <span class="math inline">1</span> and free index equal to <span class="math inline"> − 1</span> (only non–trivial blocks were shown).</figcaption>
</figure>

<figure id="fig:gwiazdadawida">
<embed src="figure24.eps" />
<figcaption>General pattern of evercrossing partitions with genus <span class="math inline">1</span> and free index equal to <span class="math inline"> − 2</span> (only non–trivial blocks were shown).</figcaption>
</figure>
:::

::: proof
*Proof.* Theorem [\[theo:gorneszacowanie\]](#theo:gorneszacowanie){reference-type="ref" reference="theo:gorneszacowanie"} implies that an outcome of the simplification algorithm obtained for an evercrossing partition with genus $1$ must have at most $6$ vertices. By direct inspection of all such pair partitions one can find that there are only two possible outcomes of the simplifying algorithm and they are depicted on Figure [8](#fig:zwyczajninadzwyczajni){reference-type="ref" reference="fig:zwyczajninadzwyczajni"}.

<figure id="fig:zwyczajninadzwyczajni">
<embed src="figure25.eps" />
<figcaption>The only two possible outcomes of the simplification algorithm for an evercrossing partition with genus <span class="math inline">1</span>. The pair partition on the left–hand side has free index equal to <span class="math inline"> − 1</span> and the pair partition on the right–hand side has free index equal to <span class="math inline"> − 2</span>.</figcaption>
</figure>

By reverting the third step of the simplifying algorithm we see that the outcome of the first two steps of the simplifying algorithm must be a pair partition either of the form from Figure [6](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} or Figure [7](#fig:gwiazdadawida){reference-type="ref" reference="fig:gwiazdadawida"}. For Figure [7](#fig:gwiazdadawida){reference-type="ref" reference="fig:gwiazdadawida"} we have to study $2^4$ cases now: each of the numbers $p,q,r$ can be either even or odd, we also have to guess which of the vertices carry primed and which carry non--primed labels (we have two possibilities); the case of Figure [6](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} is slightly simpler. For each of the $2^4$ cases we try to reverse the second step of the algorithm (and for most of the cases it is not possible; a less patient reader will find easily arguments which would allow to find only the few cases when it is possible). It turns out that after the first step of the simplification algorithm must be a pair partition either of the form depicted on Figure [6](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} or on Figure [7](#fig:gwiazdadawida){reference-type="ref" reference="fig:gwiazdadawida"}. Reverting the first step means that we are allowed to add any number of trivial blocks, which finishes the proof. ◻
:::

### Second--order asymptotics of free cumulants

We leave the proof of the following simple lemma to the reader.

::: lemma
[]{#lem:summertime label="lem:summertime"} For any $y,n\in{\mathbb{N}}$ there are $\binom{y-1}{n-1}$ solutions of the equation $x_1+\cdots+x_n=y$ if we require $x_1,\dots,x_n$ to be positive integers.
:::

::: theorem
[]{#theo:gagggag label="theo:gagggag"} For every $n\in{\mathbb{N}}$ we have $$\begin{gathered}
\label{eq:dukakao}
 R^{\mathop{\mathrm{JM}}}_{n}=
 \Sigma_{n-1}- \!\!\!\! \sum_{\substack{m_2,m_3,\dots\geq 0 \\
2m_2+3 m_3+4 m_4+\cdots=n-2}} \!\!\!\!
\frac{n (n-1) (n-2)}{24} \binom{m_2+m_3+\cdots}{m_2,m_3,\dots} \times \\
\prod_{s\geq 2} \big( (s-1) \big)^{m_s}
\Sigma_{\underbrace{1,\dots,1}_{m_2 \text{ times}},
\underbrace{2,\dots,2}_{m_3 \text{ times}},
\underbrace{3,\dots,3}_{m_4 \text{ times}},\dots} +\\
\text{(terms of degree at most $n-4$)}
  
\end{gathered}$$
:::

::: proof
*Proof.* The highest--order term in expansion [\[eq:kumulantypartycji2\]](#eq:kumulantypartycji2){reference-type="eqref" reference="eq:kumulantypartycji2"} was already found in Theorem [\[theo:pierwszystopien\]](#theo:pierwszystopien){reference-type="ref" reference="theo:pierwszystopien"}. The next highest--order terms correspond to evercrossing partitions with genus $1$. We shall calculate first the contribution of the partitions of the form depicted on Figure [6](#fig:krzyz){reference-type="ref" reference="fig:krzyz"}.

For the partition from Figure [6](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} the tuple $(k_1,\dots,k_{p+q-1})$ given by the algorithm from Section [\[subsec:pierwszawzmiankaofppsq\]](#subsec:pierwszawzmiankaofppsq){reference-type="ref" reference="subsec:pierwszawzmiankaofppsq"} is equal to $$\begin{gathered}
\label{eq:zlepyciagi}
\Big( \big( (a_{s+1}-a_{s})+(c_s-c_{s+1})-1 \big)_{s=1,2,\dots,p-1},\\
\big((b_1-a_p)+(c_p-b_q)+(d_q-c_1)+(a_1-d_1)\big)-3, \\
\big( (b_{s+1}-b_{s})+(d_s-d_{s+1})-1 \big)_{s=1,2,\dots,q-1} \Big).
\end{gathered}$$ Here and in the following, the subtraction is taken modulo $n$, i.e. $$y-x=\begin{cases} y-x & \text{if } y>x, \\ (y+n)-x & \text{if } y<x. \end{cases}$$ This subtraction has a natural interpretation as the number of elements between $x$ and $y$ going counterclockwise from $x$ to $y$.

Let $m_2,m_3,\dots$ be a sequence of nonnegative integers such that $2 m_2+3 m_3+\cdots=n-2$. We shall count now for how many different partitions of the form depicted on Figure [6](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} the tuple [\[eq:zlepyciagi\]](#eq:zlepyciagi){reference-type="eqref" reference="eq:zlepyciagi"} is equal (up to a permutation) to $$\label{eq:gromada}
(k_1',k_2',\dots,k_{p+q-1}')=(\underbrace{1,\dots,1}_{m_2\text{
times}}, \underbrace{2,\dots,2}_{m_3\text{ times}},
\underbrace{3,\dots,3}_{m_4\text{ times}}\dots).$$ Firstly, observe that all the numbers $(a_s),(b_s),(c_s),(d_s)$ are uniquely determined by $a_1$ and the collection of increments $$\begin{gathered}
\label{eq:increment} (a_{s+1}-a_s)_{s=1,\dots,p-1} , (b_1-a_p),
(b_{s+1}-b_s)_{s=1,\dots,q-1},\\  (c_p-b_q),
(c_s-c_{s+1})_{s=1,\dots,p-1},
              (d_q-c_1) , (d_s-d_{s+1})_{s=1,\dots,q-1}, (a_1-d_1),
\end{gathered}$$ where numbers [\[eq:increment\]](#eq:increment){reference-type="eqref" reference="eq:increment"} are positive integers the sum of which is equal to $n$.

Every partition of the form depicted on Figure [6](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} has free index equal to $(-1)$. There are $n$ choices of $a_1$. There are $\binom{m_2+m_3+\cdots}{m_2,m_3,\dots}$ different permutations of the tuple [\[eq:gromada\]](#eq:gromada){reference-type="eqref" reference="eq:gromada"}. We need to specify $1\leq p\leq
m_2+m_3+\cdots$. Now we count in how many different ways every of the numbers [\[eq:zlepyciagi\]](#eq:zlepyciagi){reference-type="eqref" reference="eq:zlepyciagi"} can be written as a sum of two specified elements of [\[eq:increment\]](#eq:increment){reference-type="eqref" reference="eq:increment"} minus $1$ except for one of the numbers [\[eq:zlepyciagi\]](#eq:zlepyciagi){reference-type="eqref" reference="eq:zlepyciagi"} which should be written as a sum of four specified elements of [\[eq:increment\]](#eq:increment){reference-type="eqref" reference="eq:increment"} minus $3$; the position of this exceptional number is specified by the index $p$. Finally, we have to take into account the symmetry factor $\frac{1}{4}$ of Figure [6](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} since for every partition of this form we can choose sequences $(a_s),(b_s),(c_s),(d_s)$ in four different ways corresponding to four cyclic rotations of the template. From Lemma [\[lem:summertime\]](#lem:summertime){reference-type="ref" reference="lem:summertime"} it follows that the contribution of partitions from Figure [6](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} to the summand $\Sigma_{\underbrace{1,\dots,1}_{m_2\text{ times}},
\underbrace{2,\dots,2}_{m_3\text{ times}},\dots}$ is equal to $$\label{eq:wkladkrzyza}(-1) \frac{1}{4} n
\binom{m_2+m_3+\cdots}{m_2,m_3,\dots} \sum_{1\leq p \leq
m_2+m_3+\cdots} \binom{k'_p+2}{3} \prod_{p'\neq p}
\binom{k'_{p'}}{1}.$$

By very similar considerations one can easily show that the contribution of partitions from Figure [7](#fig:gwiazdadawida){reference-type="ref" reference="fig:gwiazdadawida"} to the summand $\Sigma_{\underbrace{1,\dots,1}_{m_2\text{ times}},
\underbrace{2,\dots,2}_{m_3\text{ times}},\dots}$ is equal to $$\begin{gathered}
\label{eq:wkladgwiazdydawida}
(-2)\frac{1}{6} n \binom{m_2+m_3+\cdots}{m_2,m_3,\dots} \times \\
\sum_{1\leq p_1<p_2 \leq m_2+m_3+\cdots} \binom{k'_{p_1}+1}{2}
\binom{k'_{p_2}+1}{2} \prod_{p'\neq p_1,p_2} \binom{k'_{p'}}{1}.
\end{gathered}$$

By an application of Leibnitz rule we see that the sum of [\[eq:wkladkrzyza\]](#eq:wkladkrzyza){reference-type="eqref" reference="eq:wkladkrzyza"} and [\[eq:wkladgwiazdydawida\]](#eq:wkladgwiazdydawida){reference-type="eqref" reference="eq:wkladgwiazdydawida"} can be written in a compact form as $$\begin{gathered}
\frac{(-1) n}{24}

\times \\
\shoveright{\frac{d^2}{dx^2} \left( \sum_{s}  (s-1) z_s x^{-s}
\right)^
{m_2+m_3+\cdots}=} \\
[z_2^{m_2} z_3^{m_3} \cdots] \frac{(-1)n(n-1)(n-2)}{24}

\left( \sum_{s}  (s-1) z_s \right)^
{m_2+m_3+\cdots}=\\
\frac{(-1)n(n-1)(n-2)}{24} \binom{m_2+m_3+\cdots}{m_2,m_3,\dots}
1^{m_2} 2^{m_3} 3^{m_4} \cdots
\end{gathered}$$ which finishes the proof. ◻
:::

### Second--order expansion of characters

The following result was conjectured by Biane [@BianeCharacters].

::: theorem
[]{#theo:hahahauuau label="theo:hahahauuau"} For every $n\geq 2$ we have $$\begin{gathered}
\Sigma_{n-1}= R^{\mathop{\mathrm{JM}}}_{n}+\\ \!\!\!\!  \sum_{\substack{m_2,m_3,\dots\geq 0 \\
2m_2+3 m_3+\cdots=n-2}} \!\!\!\! \frac{1}{4} \binom{n}{3}
\binom{m_2+m_3+\cdots}{m_2,m_3,\dots} \prod_{s\geq 2} \big( (s-1)
R^{\mathop{\mathrm{JM}}}_s \big)^{m_s} +\\ \text{(terms of degree at most $n-4$)}.
\end{gathered}$$
:::

::: proof
*Proof.* In [\[eq:dukakao\]](#eq:dukakao){reference-type="eqref" reference="eq:dukakao"} we use [\[eq:eksplozjamozgu\]](#eq:eksplozjamozgu){reference-type="eqref" reference="eq:eksplozjamozgu"} to express $\Sigma_{\underbrace{1,\dots,1}_{m_2 \text{
times}},\underbrace{2,\dots,2}_{m_3 \text{ times}},\dots}$ in terms of $R^{\mathop{\mathrm{JM}}}_2,R^{\mathop{\mathrm{JM}}}_3,\dots$. ◻
:::

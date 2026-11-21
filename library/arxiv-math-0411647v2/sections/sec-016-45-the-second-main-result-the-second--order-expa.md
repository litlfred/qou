---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-016-45-the-second-main-result-the-second--order-expa
section_title: "The second main result: the second--order expansion of free cumulants and characters"
section_number: 4.5
pages: 37-42
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 0.99
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
[]{#sec:secondorderexp label="sec:secondorderexp"}

### Evercrossing partitions with genus $1$

Theorem [\[theo:gorneszacowanie\]](#theo:gorneszacowanie){reference-type="ref" reference="theo:gorneszacowanie"} allows us to enumerate (in finite time) all possible outcomes of the simplifying algorithm for a fixed genus of the original evercrossing partition. By reversing all three steps of the simplifying algorithm we are able to write a number of "templates" which describe all evercrossing partitions with a prescribed genus. Let us have a look on an example.

::: theorem
[]{#theo:klasyfikacja label="theo:klasyfikacja"} Every evercrossing partition with genus $1$ must be either of the form depicted on Figure [1](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} (in this case it has the free index equal to $-1$) or Figure [2](#fig:gwiazdadawida){reference-type="ref" reference="fig:gwiazdadawida"} (in this case it has the free index equal to $-2$). On both figures only non--trivial blocks were shown.

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
*Proof.* Theorem [\[theo:gorneszacowanie\]](#theo:gorneszacowanie){reference-type="ref" reference="theo:gorneszacowanie"} implies that an outcome of the simplification algorithm obtained for an evercrossing partition with genus $1$ must have at most $6$ vertices. By direct inspection of all such pair partitions one can find that there are only two possible outcomes of the simplifying algorithm and they are depicted on Figure [3](#fig:zwyczajninadzwyczajni){reference-type="ref" reference="fig:zwyczajninadzwyczajni"}.

<figure id="fig:zwyczajninadzwyczajni">
<embed src="figure25.eps" />
<figcaption>The only two possible outcomes of the simplification algorithm for an evercrossing partition with genus <span class="math inline">1</span>. The pair partition on the left–hand side has free index equal to <span class="math inline"> − 1</span> and the pair partition on the right–hand side has free index equal to <span class="math inline"> − 2</span>.</figcaption>
</figure>

By reverting the third step of the simplifying algorithm we see that the outcome of the first two steps of the simplifying algorithm must be a pair partition either of the form from Figure [1](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} or Figure [2](#fig:gwiazdadawida){reference-type="ref" reference="fig:gwiazdadawida"}. For Figure [2](#fig:gwiazdadawida){reference-type="ref" reference="fig:gwiazdadawida"} we have to study $2^4$ cases now: each of the numbers $p,q,r$ can be either even or odd, we also have to guess which of the vertices carry primed and which carry non--primed labels (we have two possibilities); the case of Figure [1](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} is slightly simpler. For each of the $2^4$ cases we try to reverse the second step of the algorithm (and for most of the cases it is not possible; a less patient reader will find easily arguments which would allow to find only the few cases when it is possible). It turns out that after the first step of the simplification algorithm must be a pair partition either of the form depicted on Figure [1](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} or on Figure [2](#fig:gwiazdadawida){reference-type="ref" reference="fig:gwiazdadawida"}. Reverting the first step means that we are allowed to add any number of trivial blocks, which finishes the proof. ◻
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
*Proof.* The highest--order term in expansion [\[eq:kumulantypartycji2\]](#eq:kumulantypartycji2){reference-type="eqref" reference="eq:kumulantypartycji2"} was already found in Theorem [\[theo:pierwszystopien\]](#theo:pierwszystopien){reference-type="ref" reference="theo:pierwszystopien"}. The next highest--order terms correspond to evercrossing partitions with genus $1$. We shall calculate first the contribution of the partitions of the form depicted on Figure [1](#fig:krzyz){reference-type="ref" reference="fig:krzyz"}.

For the partition from Figure [1](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} the tuple $(k_1,\dots,k_{p+q-1})$ given by the algorithm from Section [\[subsec:pierwszawzmiankaofppsq\]](#subsec:pierwszawzmiankaofppsq){reference-type="ref" reference="subsec:pierwszawzmiankaofppsq"} is equal to $$\begin{gathered}
\label{eq:zlepyciagi}
\Big( \big( (a_{s+1}-a_{s})+(c_s-c_{s+1})-1 \big)_{s=1,2,\dots,p-1},\\
\big((b_1-a_p)+(c_p-b_q)+(d_q-c_1)+(a_1-d_1)\big)-3, \\
\big( (b_{s+1}-b_{s})+(d_s-d_{s+1})-1 \big)_{s=1,2,\dots,q-1} \Big).
\end{gathered}$$ Here and in the following, the subtraction is taken modulo $n$, i.e. $$y-x=\begin{cases} y-x & \text{if } y>x, \\ (y+n)-x & \text{if } y<x. \end{cases}$$ This subtraction has a natural interpretation as the number of elements between $x$ and $y$ going counterclockwise from $x$ to $y$.

Let $m_2,m_3,\dots$ be a sequence of nonnegative integers such that $2 m_2+3 m_3+\cdots=n-2$. We shall count now for how many different partitions of the form depicted on Figure [1](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} the tuple [\[eq:zlepyciagi\]](#eq:zlepyciagi){reference-type="eqref" reference="eq:zlepyciagi"} is equal (up to a permutation) to $$\label{eq:gromada}
(k_1',k_2',\dots,k_{p+q-1}')=(\underbrace{1,\dots,1}_{m_2\text{
times}}, \underbrace{2,\dots,2}_{m_3\text{ times}},
\underbrace{3,\dots,3}_{m_4\text{ times}}\dots).$$ Firstly, observe that all the numbers $(a_s),(b_s),(c_s),(d_s)$ are uniquely determined by $a_1$ and the collection of increments $$\begin{gathered}
\label{eq:increment} (a_{s+1}-a_s)_{s=1,\dots,p-1} , (b_1-a_p),
(b_{s+1}-b_s)_{s=1,\dots,q-1},\\  (c_p-b_q),
(c_s-c_{s+1})_{s=1,\dots,p-1},
              (d_q-c_1) , (d_s-d_{s+1})_{s=1,\dots,q-1}, (a_1-d_1),
\end{gathered}$$ where numbers [\[eq:increment\]](#eq:increment){reference-type="eqref" reference="eq:increment"} are positive integers the sum of which is equal to $n$.

Every partition of the form depicted on Figure [1](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} has free index equal to $(-1)$. There are $n$ choices of $a_1$. There are $\binom{m_2+m_3+\cdots}{m_2,m_3,\dots}$ different permutations of the tuple [\[eq:gromada\]](#eq:gromada){reference-type="eqref" reference="eq:gromada"}. We need to specify $1\leq p\leq
m_2+m_3+\cdots$. Now we count in how many different ways every of the numbers [\[eq:zlepyciagi\]](#eq:zlepyciagi){reference-type="eqref" reference="eq:zlepyciagi"} can be written as a sum of two specified elements of [\[eq:increment\]](#eq:increment){reference-type="eqref" reference="eq:increment"} minus $1$ except for one of the numbers [\[eq:zlepyciagi\]](#eq:zlepyciagi){reference-type="eqref" reference="eq:zlepyciagi"} which should be written as a sum of four specified elements of [\[eq:increment\]](#eq:increment){reference-type="eqref" reference="eq:increment"} minus $3$; the position of this exceptional number is specified by the index $p$. Finally, we have to take into account the symmetry factor $\frac{1}{4}$ of Figure [1](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} since for every partition of this form we can choose sequences $(a_s),(b_s),(c_s),(d_s)$ in four different ways corresponding to four cyclic rotations of the template. From Lemma [\[lem:summertime\]](#lem:summertime){reference-type="ref" reference="lem:summertime"} it follows that the contribution of partitions from Figure [1](#fig:krzyz){reference-type="ref" reference="fig:krzyz"} to the summand $\Sigma_{\underbrace{1,\dots,1}_{m_2\text{ times}},
\underbrace{2,\dots,2}_{m_3\text{ times}},\dots}$ is equal to $$\label{eq:wkladkrzyza}(-1) \frac{1}{4} n
\binom{m_2+m_3+\cdots}{m_2,m_3,\dots} \sum_{1\leq p \leq
m_2+m_3+\cdots} \binom{k'_p+2}{3} \prod_{p'\neq p}
\binom{k'_{p'}}{1}.$$

By very similar considerations one can easily show that the contribution of partitions from Figure [2](#fig:gwiazdadawida){reference-type="ref" reference="fig:gwiazdadawida"} to the summand $\Sigma_{\underbrace{1,\dots,1}_{m_2\text{ times}},
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

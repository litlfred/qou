---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-010-54-an-additional-trace-when-ya2-1
section_title: "An additional trace when y=a2= 1"
section_number: 5.4
pages: 23-24
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.973
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
Let $S^{\dagger\dagger}  = S/(a^2-1,y-1) = S^{\dagger}/(a^2-y^2) = \overline{S}/(a^2-y)$,
and $BMW_n^{\dagger\dagger} = \WBMW_n \otimes_R S^{\dagger \dagger}$.

We first deal with the very special case $x = -2a$.
\begin{prop} \label{propTracesXm2a}
Let $(x_n)_{n \geq 1}$ denote a sequence with values in some $S^{\dagger\dagger}$-module
satisfying $(x+2a) M = 0$. Then there exists a Markov trace $(t_n^X)$ on $(\widetilde{BMW}_n)$
with values in $M$ such that, for every braid $g$, $t_n^X(g) = x_{\# \hat{g}}$, where
$\hat{g}$ denotes the closure of the braid $g$ and $\# L$ denotes the number of
components of the link $L$. Moreover, every Markov trace on $(\widetilde{BMW}_n)$ with
values in $M$ is of that form.
\end{prop}
\begin{proof}
We first note that the relations $(s_i-a)(s_i^2 + 2a s_i +1) = (s_i -a)(s_i+a)^2 = (s_i^2-1)(s_i+a) = 0$
hold true in $M$. Therefore, the action of $BMW_n^{\dagger\dagger}$ on $M$ factors
through the group algebra $\Q[a]/(a^2-1) \mathfrak{S}_n$ of the symmetric group. Moreover, the
natural map $H_n \otimes S^{\dagger\dagger}/(x+2a) \to \Q[a]/(a^2-1) \mathfrak{S}_n$, where $H_n$
is the cubic Hecke algebra defined by $(s_i^2-1)(s_i+a) = 0$, is clearly surjective, and $\mathcal{R}_1$
is easily checked to map to $0$. Therefore, the map $\widetilde{BMW}_n \otimes S^{\dagger\dagger}/(x+2a) \to \Q[a]/(a^2-1) \mathfrak{S}_n$
is surjective.

We show that there exists a Markov trace $(t_n^X)$ on $((\Q[a]/(a^2-1)) \mathfrak{S}_n)$
fulfilling the conditions of the statement. Since the formula
$t_n^X(g) = x_{\# \hat{g}}$ clearly defines an invariant of links, and therefore a Markov
trace on the tower of algebras of the braid groups, it is sufficient to prove that
$t_n^X$ vanishes on the defining ideal of $\Q[a]/(a^2-1) \mathfrak{S}_n$ for any given $n$.
This ideal is the linear span of the $A s_i^2 B - AB$ for $A,B$ two arbitrary braids on $n$
strands. Since the closures of $A s_i^2 B$ and $AB$ have the same number of components,
we indeed get that $(t_n^X)$ is a well-defined Markov trace on $(\widetilde{BMW}_n)$.
Since $t_n^X(1) = x_n$, the fact that all Markov traces are obtained this way is a consequence of proposition \ref{unicitetn1}.

\end{proof}

We can now state a general statement.
\begin{prop} {\ }  \label{propclassmarkovddagger3}
\begin{enumerate}
\item There exists a Markov trace $(t_n^{\dagger\dagger})$ on $\WBMW_n$ with values in $S^{\dagger\dagger}$, given by 
$t_n^{\dagger\dagger}(\beta) = a^n \psi_n(\beta)$, where $\psi_n : \WBMW_n \to S^{\dagger\dagger}$ is an algebra morphism
defined by $s_i \mapsto a$.
\item Let $t'_3$ be the composite of $t_3$ with $M \to M \otimes_R S^{\dagger\dagger}[ (a-x)^{-1},(2a-x)^{-1}]$.
 Then $(t'_3)$ is a linear combination of the composites of $t_3^H$, $t_3^K$, $t_3^{\dagger\dagger}$ 
 with
 coefficients inside $M \otimes_R S^{\dagger\dagger}[ (a-x)^{-1},(2a-x)^{-1}]$.
\end{enumerate}
\end{prop}
\begin{proof}
We first check that the $R$-algebra morphism $\psi_n : H_n \to S^{\dagger\dagger}$ defined by $s_i \mapsto a$
indeed factorizes through $\WBMW_n$, namely that $\psi_n(\mathcal{R}_1) = 0$, by direct calculation. Then
$t_n^{\dagger\dagger}(x) = a^n \psi_n(x)$ clearly defines a trace for every $n$, and we need to check
the Markov property, namely that $t_{n+1}^{\dagger\dagger}(x s_{n}^{\pm 1}) = t_n^{\dagger\dagger}(x)$
for all $x \in \WBMW_n$. This holds because 
$t_{n+1}^{\dagger\dagger}(x s_{n}^{\pm 1}) = a^{n+1} \psi_{n+1}(x s_{n}^{\pm 1})
= a^{n+1} \psi_{n+1}(x) a^{\pm 1}
= a^{n+1} \psi_{n}(x) a^{\pm 1} 
= a^{n+1} \psi_{n}(x) a
= a^{n+2} \psi_{n}(x)
= a^n \psi_n(x) = t_n^{\dagger\dagger}(x)$. This proves (i).
Note that $t_3^{\dagger\dagger}(1) = a^3$, $t_3^{\dagger\dagger}(s_1) = a^2=1$, $t_3^{\dagger\dagger}(s_1s_2) = a$,  
We know that $t_3'$ is uniquely determined by its value on $1,s_1,s_1s_2$. It has to be a linear
combination of $t_3^H$, $t_3^K$ and $t_3^{\dagger\dagger}$ if and only if 
$$
\Delta = \left| \begin{array}{ccc}  a^3 & a^2 & a \\ \delta_H^2 & \delta_H & 1 \\ \delta_K^2 & \delta_K & 1 \\ \end{array} \right| 
=a  \left| \begin{array}{ccc}  a^2 & a & 1 \\ \delta_H^2 & \delta_H & 1 \\ \delta_K^2 & \delta_K & 1 \\ \end{array} \right| 
$$
is invertible. Since $\delta_H = (y+1)/x = 2/x$, $\delta_K = \frac{2}{x} - a$, we get
$$
\Delta = \frac{2}{x^2}(2a-x)(a-x)
$$
whence the conclusion of (ii).

\end{proof}

We will show below (see corollary \ref{corclasstracesddagger}) that part (ii) actually holds true for every $n$, provided
that $x+2a$ is also assumed to be invertible.

We note that, when specialized to a field, $x=a, y=1,a^2=1$ imply $x \in \{-1,1 \}$, hence $\{ b,c \} = \{-j, -j^2 \}$ with $j = \exp(\frac{2 \ii \pi}{3})$
if $a=1$, and $\{ b,c \} = \{ j, j^2 \}$ if $a=-1$ ; likewise,
$x=2a, y=1,a^2=1$ imply $x \in \{-2,2 \}$, hence $b=c$, and $b,c \in \{-1,1 \}$,
hence either $a=b=c=1$ or $a=b=c=-1$.
In these four cases, we have $a = \pm bc$, and a possible additional trace on $\WBMW_n$ cannot factorize through
$BMW_n^{\pm}$, as is immediately checked on the 12-terms relation (note that,
by substracting a linear combination of the two ordinary traces,
we can assume in the first two cases that this trace satisfies $t_3(1) = t_3(s_1) = 0$, $t_3(s_1s_2) = 1$, while in the
latter cases we can assume $t_3(1) = 1$, $t_3(s_1) = t_3(s_1s_2)=0$).

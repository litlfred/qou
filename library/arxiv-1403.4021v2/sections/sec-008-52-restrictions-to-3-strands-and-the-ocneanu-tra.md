---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-008-52-restrictions-to-3-strands-and-the-ocneanu-tra
section_title: "Restrictions to 3 strands, and the Ocneanu trace"
section_number: 5.2
pages: 21-24
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.965
---
We recall that the notation $MT_3(M)$ was defined in section \ref{sectH3}. We note that
$$
t_3^H(1) = \left( \frac{y+1}{x} \right)^2 \ \  
t_3^H(s_1) =\frac{y+1}{x}  \ \  
t_3^H(s_1s_2) = 1 \ \  
$${}
and define additional elements $t_3^S$, $t_3^K$
of $MT_3(M)$ by
$$
t_3^S(1) = a^3,\ \ \ \ t_3^S(s_1) = t_3^S(s_1s_2) = 0, \ \ \ \ 
t_3^S((s_1s_2^{-1})^2)=  x^2(2a+x),
$$
{}
$$
t_3^K(1) = \delta_K^2,\ \ \ \ t_3^K(s_1) = \delta_K,\ \ \ \ t_3^K(s_1s_2) = 1,
\ \ \ \ \delta_K =  \frac{y^2 - ax+y}{xy}, 
$${}
$$
 t_3^K((s_1 s_2^{-1})^2) = x^3 y(y+1) + x^2(y^2 + 2a + \frac{a}{y}) - x(1+y) - (y + a + \frac{a}{y}).
$$
\begin{prop} \label{prop:MT3bmw} Let $t \in MT_3(M)$ factorizing through $\WBMW_3$.
\begin{enumerate}
\item  The trace $t$ is uniquely
determined by $t(1)$, $t(s_1)=t(s_2)$ and $t(s_1s_2)$. 
\item If $x(a^2-y^2)$ is invertible in $M$ then $t$ is  uniquely determined by $t(1)$ and $t(s_1s_2)$.
\item If $x^2(a^2-y)$ is invertible in $M$ then $t$ is  uniquely determined by $t(s_1)$ and $t(s_1s_2)$.
\item If $x(a^2-y^2)$ and $x^2(a^2-y)$ are invertible in $M$ then $t$ is uniquely determined by $t(s_1s_2)$.
\end{enumerate}
\end{prop}
\begin{proof} Let $t \in MT_3(M)$ factorizing though $\WBMW_3$. With the notations of proposition \ref{propMT3}
we write $t = \alpha e_1^* + \beta e_2^* + \gamma e_3^* + \delta e_4^*$. By direct calculation,
we check that the equation $t(\mathcal{R}_1s_1) = 0$ means
$$0=-{x}^{2} \left( {a}^{2}+ax+y \right) \alpha +
 {\frac {x \left( 2\, \left( y+1 \right) {a}^{3}+2\,x \left( y+1 \right) {a}^{2}+a \left( {x}^{2}+y \left( y+1
 \right)  \right) +yx \right) }{a}}\beta $${}$$+{\frac {- \left( y+1 \right) ^{2}{a}^{3}-x \left( y+1 \right) ^{2}{a}^{2}+a \left( -{x}^{2}-2\,{x}^{2}y+y \left( {y}^{
2}+y+1 \right)  \right) -yx \left( y+1 \right) }{a}} \gamma + {y}^{2} \delta
$$ 
and, since $y$ is invertible, this proves that $t$ is determined by $\alpha, \beta$ and $\gamma$,
meaning that $t$ is uniquely determined by $t(1)$, $t(s_1)$ and $t(s_1s_2)$, which proves (i).
Similarly, we get that $t(s_1^{-1}\mathcal{R}_1)=0$ reads
$$
(a^2-y^2) \left( x t(s_1) - (y+1) t(s_1s_2) \right) = 0
$$
and $t(\mathcal{R}_1)=0$ means
$$
x^2(a^2-y) t(1) = \frac{(a^2-y)(y+1) - x(y-1)a}{a} \left( x t(s_1) - (y+1) t(s_1s_2) \right) + \frac{x}{a}(y+1)(a^2-y) t(s_1)
$$
which easily implies (ii)-(iv).
\end{proof}

\begin{cor} Let $(t_n)$ be a Markov trace factoring through $(\WBMW_n)$ with values in $M$.
If  $x(a^2-y^2)$ and $x^2(a^2-y)$ are invertible in $M$ then $(t_n)$ is a multiple of $(t_n^H)$ composed
with some morphism $R \to M$.
\end{cor}
\begin{proof}
Immediate consequence of (iv) together with proposition \ref{prop:unicitetracegen}.
\end{proof}

Recall that $S^{\dagger} = S/(a^2-y) = R[x^{-1}]/(a^2-y)$ and $BMW_n^{\dagger} = \WBMW_n \otimes_R S^{\dagger}$.

\begin{prop} \label{propmarkovypas1} Let $t'_n$ be the composite of $t_n$ with $M \to M \otimes_R S^{\dagger}[ (y-1)^{-1}]$.
 Then $(t'_n)$ is a scalar multiple of the composite of $t_n^H$ with some morphism $R \to M$ and with $M \to M \otimes_R S^{\dagger}[ (y-1)^{-1}]$.
 \end{prop}
\begin{proof}
Inside $S^{\dagger}[(y-1)^{-1}]$ we have $a^2 -y^2 = y(1-y)$, hence by proposition \ref{prop:MT3bmw} (ii)
we have that $t'_3$ is uniquely determined by $t'_3(1)$ and $t'_3(s_1s_2)$,
and more precisely the equation $t'_3(s_1^{-1}\mathcal{R}_1)=0$ means
$t'(s_1) = \frac{y+1}{x} t'(s_1 s_2)$. Let $t_n^{\circ} = t'_n - t'_3(s_1s_2) t_n^H$.
Then $t_3^{\circ}(s_1s_2) = 0$ hence $t_3^{\circ}(s_1) = 0$ and therefore $t_3^{\circ} =  a^{-3}t_3^{\circ}(1) t_3^S$.
Let $\tau = t_4^{\circ} \circ \iota_3$, where $\iota_3 : \WBMW_3 \to \WBMW_4$ is the natural map. Again by
 \ref{prop:MT3bmw} (ii) we know that $\tau$ is uniquely determined by $\tau(1)$ and $\tau(s_1s_2)$. Moreover
 $\tau(s_1s_2) = t_4^{\circ}(s_1s_2) = t_4^{\circ}(s_2s_3) = t_3^{\circ}(s_2) = t_3^S(s_2) = 0$.
 It follows that $\tau(s_1) = 0$, since $\tau(s_1) = \frac{y+1}{x} \tau(s_1 s_2)$.
 But $\tau(s_1) =  t_4^{\circ}(s_1) =t_4^{\circ}(s_3) = t_3^{\circ}(1)$, hence $t_3(1) = 0$ and
 $t_3^{\circ} = 0$. We prove by induction on $n$ that $t_n^{\circ}(1) = 0$. Assume we
 know that $t_r^{\circ}(1) = 0$ for all $r \leq n$, and consider the composite $\tau$ of $t_{n+1}^{ \circ}$
 with the natural map $\WBMW_3 \to \WBMW_{n+1}$. We have $\tau(s_1s_2) = t_{n+1}^{\circ}(s_1 s_2)
 = t_{n+1}^{\circ}(s_{n-1} s_{n})= t_{n-1}^{\circ}(1) = 0$. It follows as before that $\tau(s_1) = 0$,
 hence $t_n^0(1) = t_{n+1}^0(s_n) = t_{n+1}^0(s_1) = \tau(s_1) = 0$. It follows that $t_n^{\circ}(1) = 0$,
 and the claim follows by induction because of proposition \ref{unicitetn1}.
\end{proof}




\subsection{The Kauffman trace}


Recall that we defined in \S \ref{secttwobmwagebras} two Markov traces $t_n^{\pm} : BMW_n^{\pm} \to S_{\pm}$. Using the Chinese
Remainder Theorem isomorphism $\overline{S} \simeq S_+ \oplus S_-$ they
can be patched together into a Markov trace $\overline{BMW}_n \otimes_{\overline{R}}  \overline{S} \to
\overline{S}$, which extends to a Markov trace $t_n^K : \WBMW_n \to \overline{S}$.


$$
\xymatrix{
  &\overline{BMW}_n\otimes_{\overline{R}}S_+ \ar[r]&  BMW_n^+ \ar[r]^{t_n^+} & S_+ \ar[dr] & \\
 \overline{BMW}_n\otimes_{\overline{R}} \overline{S} \ar[ur] \ar[dr] \ar@{.>}[rrrr]^{t_n^K}& & & & \overline{S} \\
  & \overline{BMW}_n\otimes_{\overline{R}}S_- \ar[r]& BMW_n^- \ar[r]_{t_n^-} & S_- \ar[ur] & \\
}
$$

Note that the value of $t_3^K((s_1 s_2^{-1})^2)$ define before indeed matches
this new definition, because of the
computation of the Kauffman invariant of the figure-eight knot we did in section \ref{secttwobmwagebras}.

\begin{prop} Let $t'_n$ be the composite of $t_n$ with $M \to M \otimes_R \overline{S}[ (a^2-y)^{-1}]$.
 Then $(t'_n)$ is a linear combination of the composites of $t_n^H$ and $t_n^K$ with some morphism $\overline{S} \to M \otimes_R \overline{S}[ (a^2-y)^{-1}]$.
\end{prop}
\begin{proof}
By proposition \ref{prop:unicitetracegen} we know that $t'_n$ is uniquely determined by $t'_1(1) = t'_3(s_1s_2)$ and $t'_2(1) = t'_3(s_1)$. It is thus
sufficient to show that $t_3^H$ and $t_3^K$ induce a basis of $( \overline{S}[ (a^2-y)^{-1}])^2$ under $t'_3 \mapsto (t'_3(s_1s_2),t'_3(s_1))$.
The corresponding $2 \times 2$ matrix has for determinant
$$
\left| \begin{array}{cc} \delta_H & 1 \\ \delta_K & 1 \end{array} \right| = \delta_H - \delta_K = \frac{a}{y} \in ( \overline{S}[ (a^2-y)^{-1}])^{\times}
$$
with $\delta_H = \frac{y+1}{x}$, and this concludes the proof.
\end{proof}


\begin{remark} It is well-known that both the Kauffman polynomial and
the HOMFLYPT polynomial both specialize to the Jones polynomial
(see e.g. \cite{LICKO} p. 180). It could have been expected that this coincidence would have appeared in the previous proposition.
It clearly does not, since any specialized value of the invariants defined by our
traces $t_n^H$ and $t_n^K$
cannot coincide on the 2-components unlink (we always have $\delta_H \neq \delta_K$).
What happens is that, according to \cite{LICKO} proposition 16.6, the trace $t_n^K$ provides the Jones
polynomial when specialized to $\alpha = -t^{\frac{-3}{4}}$, $q = t^{\frac{1}{4}}$, that
is $a = q^{-6}$, $b = -q^{-2} = -t^{\frac{-1}{2}}$, $c = -q^{-4} = -t^{-1}$ while, according to \cite{LICKO} proposition 16.5, $t_n^H$
provides the Jones polynomial when $\{b,c \}$ is specialized to $\{ - t^{\frac{1}{2}}, t^{\frac{3}{2}} \}$, and the
only value of $t$ for which these two parametrizations coincide is $t^{\frac{1}{2}} = -1$, in which
case we get $b+c = 0$, which is forbidden here.
\end{remark}


\subsection{An additional trace when $y=a^2= 1$}

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

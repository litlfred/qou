---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces"
section_id: sec-009-association-schemes
section_title: "Association schemes"
section_number: null
pages: 27-32
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.973
doc_brief: "Bounds for codes and designs in complex subspaces — We introduce the concepts of complex Grassmannian codes and designs."
---
\label{sec:assoc}

As Theorem \ref{thm:twothree} indicates, sets of Grassmannian subspaces which reach equality in the Delsarte bounds have a great deal of structure. In this section, we show that---much like spherical codes and spherical designs---these sets are often endowed with the structure of an association scheme. 

Let $S$ be an $f$-code with a finite number of distinct sets of principal angles $y = (y_1,\ldots,y_m)$. Denote the set of $y$'s that occur by $\scr{Y}$. For each $y \in \scr{Y}$, define a $|S| \times |S|$ matrix as follows:
\[
A_y(a,b) := \begin{cases}
1, & a,b \mbox{ have principal angles } y; \\
0, & \mbox{otherwise.}
           \end{cases}
\]
Each $A_y$ is a symmetric $\{0,1\}$-matrix. Furthermore, each pair $(a,b)$ has some principal angle $y$, so $\sum_{y \in \scr{Y}} A_y = J$, where $J$ is the all-ones matrix. If $y_0 := (1,\ldots,1)$ denotes the trivial principal angles set, then $A_0 := A_{y_0}$ is the identity matrix. We will call the $A_y$ matrices \defn{Schur idempotents}, as they are idempotent under Schur multiplication, defined as follows:
\[
(A \circ B)_{ij} := A_{ij} B_{ij}.
\]
Under certain conditions, these Schur idempotents form an association scheme. 

For each integer partition $\mu$ and corresponding zonal polynomial $Z_\mu$, define an $|S| \times |S|$ matrix as follows:
\[
E_{\mu}(a,b) := \frac{1}{|S|}Z_\mu(a,b).
\]
Each $E_\mu$ is also symmetric and in the span of $\{A_y\}_{y \in \scr{Y}}$:
\[
E_\mu = \frac{1}{|S|}\sum_{y \in \scr{Y}} Z_\mu(y) A_y.
\]
In particular, $E_0$ is a scalar multiple of $J$. When $\{A_y\}_{y \in \scr{Y}}$ forms an association scheme, the matrices $E_\mu$ are the scheme's idempotents.

\begin{lemma}
If $S$ is a $2t$-design, then $\{E_\mu\}_{\abs{\mu} \leq t, \len(\mu) \leq m}$ are a set of orthogonal idempotents.
\label{lem:orthogidem}
\end{lemma}

\begin{proof}
Suppose $\abs{\mu} = i$ and $\abs{\la} = j$, with $i,j \leq t$. Then
\begin{align*}
(E_\mu E_\la)_{a,b} & = \frac{1}{|S|^2}\sum_{c \in S} Z_\mu(a,c)Z_\la(c,b) \\
& = \frac{1}{|S|}\ip{Z_{\mu,a}}{Z_{\la,b}}_S.
\end{align*}
Since $Z_{\mu,a}$ and $Z_{\mu,b}$ are in $H_t$, their product is in $H_{2t}$. Now $S$ is a $2t$-design, so the average of $Z_{\mu,a}Z_{\la,b}$ over $S$ is the same as the average over $\gras{m}{n}$. But
\[
\ip{Z_{\mu,a}}{Z_{\la,b}} = \de_{\la,\mu}Z_\mu(a,b),
\]
and so we find that $E_\mu E_\la = \de_{\la,\mu}E_\mu$. \qed
\end{proof}

More generally, if $\abs{\mu} = i$ and $\abs{\la} = j$, and $S$ is a $(i+j)$-design, then $E_\mu$ and $E_\la$ are orthogonal. 

Now suppose $S$ is a $2t$-design. By the previous lemma $\{E_\mu\}_{\abs{\mu} \leq t}$ are linearly independent, and clearly the matrices $\{A_y\}_{y \in \scr{Y}}$ are also linearly independent. If $|\scr{Y}|$ equals the number of partitions of at most $t$ (into at most $m$ parts), then the span of $\{A_y\}_{y \in \scr{Y}}$ and $\{E_\mu\}_{\abs{\mu} \leq t}$ are the same. Since $\{E_\mu\}_{\abs{\mu} \leq t}$  is closed under multiplication, so too is the span of $\{A_y\}_{y \in \scr{Y}}$, and so we have an association scheme. 

\begin{corollary}
\label{cor:assoc}
Let $S$ be a $2t$-design in $\gras{m}{n}$ with principal angle set $\scr{Y}$. If $|\scr{Y}|$ is equal to the total number of partitions of $0,1,\ldots,t$ into at most $m$ parts, then $\{A_y\}_{y \in \scr{Y}}$ is an association scheme.
\end{corollary}

\begin{lemma}
Let $S$ be a $2t$-design in $\gras{m}{n}$ with principal angle set $\scr{Y}$ such that $|\scr{Y}|$ is the total number of partitions of $0,1,\ldots,t$ into at most $m$ parts. Then $\{E_\mu\}_{\abs{\mu} \leq t, \len(\mu) \leq m}$ are the idempotents of the scheme $\{A_y\}_{y \in \scr{Y}}$.
\end{lemma}

\begin{proof}
Since $E_\mu = \frac{1}{|S|}\sum_{y \in \scr{Y}} Z_\mu(y) A_y$, we see that the matrix $[Z_\mu(y)]$ is the transition matrix between the two bases of the association scheme and is therefore invertible. It follows that for each $y_i$ in $\scr{Y}$, some linear combination of the rows $Z_\mu$ forms a homogeneous degree-$t$ polynomial $g_i$ such that $g_i(y_j) = \de_{ij}$. (Conversely, if such $g_i$ polynomials exist, then $[Z_\mu(y)]$ is invertible.) Then
\begin{align*}
(A_iE_\mu)_{a,b} & = \frac{1}{|S|}\sum_{c: y(a,c) = y_i} Z_\mu(c,b) \\
& = \ip{g_{i,a}}{Z_{\mu,b}}_S \\
& = \ip{g_{i,a}}{Z_{\mu,b}}.
\end{align*}
Now write $g_i = \sum_{\abs{\la} \leq t} c_{i,\la} Z_\la$, so that
\[
\ip{g_{i,a}}{Z_{\mu,b}} = \sum_{\abs{\la} \leq t} c_{i,\la} \ip{Z_{\la,a}}{Z_{\mu,b}} = c_{i,\mu} Z_\mu(a,b). 
\]
Thus $A_iE_\mu = c_{i,\mu} E_\mu$ for some $c_{i,\mu}$. \qed
\end{proof}

By way of example, let $t = 1$, and suppose $S$ is a $2$-design with only one nontrivial principal angle set (and one trivial one, for a total of two). The number of partitions of at most $1$ is also two ($\mu = 0$ and $\mu = (1)$), so by Corollary \ref{cor:assoc} we have an association scheme. In this case the scheme is the trivial one, namely $\{I, J-I\}$.

As another example of an association scheme obtained from principal angles, consider the collection of subspaces in $\gras{n/2}{n}$ from Theorem \ref{thm:pauli}. This collection has four distinct sets of principal angles: 
\begin{align*}
y & = (1,\ldots,1) \quad (\text{trivial principal angles}), \\
y & = (0,\ldots,0) \quad (\text{angles between $a$ and $a^\perp$}), \\
y & = (\underbrace{1,\ldots,1}_{n/4},\underbrace{0,\ldots,0}_{n/4}), \\ 
y & = (\tfrac{1}{2},\ldots,\tfrac{1}{2}).
\end{align*}
While $|\scr{Y}| = 4$ is the number of partitions of at most $2$ ($\mu = 0$, $\mu = (1)$, $\mu = (1,1)$ and $\mu = (2)$), the hypotheses of Corollary \ref{cor:assoc} are not satisfied because the subspaces do not form a $4$-design. Nevertheless, it is easy to verify computationally that this collection does give a $3$-class association scheme.

We may define a coarser set of relations on an $f$-code $S$ using the sums of principal angles---the inner products of the projection matrices---instead of the principal angles themselves. Let $\scr{A}$ denote the set of nontrivial inner product values that occur in $S$, so $S$ is an $\scr{A}$-code. For $\al \in \scr{A}$ let $A'_\al$ be the $|S| \times |S|$ matrix defined as follows:
\[
A'_\al(a,b) := \begin{cases}
1, & \tr(P_aP_b) = \al, \\
0, & \mbox{otherwise.}
           \end{cases}
\]
Also define $A'_m := I$ for the identity relation. Clearly each $A'_\al$ is in the span of $\{A_y: y \in \scr{Y}\}$; in fact
\[
A'_\al = \sum_{y \in \scr{Y}:\; \sum y_i = \al} A_y.
\]
In particular, $A'_m = A_0 = I$, and if $0$ is in $\scr{A}$, then $A'_0 = A_{(0,\ldots,0)}$. As before, the matrices are Schur idempotents and sum to $J$. Next we need the corresponding idempotents. For each $i \in \{0,\ldots,t\}$, define $E'_i$ as follows:
\[
E'_i := \sum_{\abs{\mu} = i} E_\mu.
\]
This implies that $E'_0 = J/|S|$ and $E'_i(a,b) = (Z_i(a,b) - Z_{i-1}(a,b))/|S|$ for $i > 0$. As in Lemma \ref{lem:orthogidem}, if $S$ is a $2t$-design, then $\{E'_i: i \leq t\}$ is a set of orthogonal idempotents, and if $S$ is a $(2t-1)$-design, then $\{E'_i: i \leq t\}$ are linearly independent.

Clearly $E'_i$ is in the span of $\{A_y: y \in \scr{Y}\}$, since each $E_\mu$ is in that span. But suppose $Z_i(y)$ is the annihilator polynomial of some $i$-distance set, so it is a only function of $\sum_i y_i$: then in fact $E'_i$ is in the span of $\{A'_\al: \al \in \scr{A}\}$. If $Z_i(y)$ is an annihilator for sufficiently many $i$, then $\{E'_i: 0 \leq i \leq t\}$ and $\{A'_\al: \al \in \scr{A}\cup\{m\}\}$ span the same set, and that set is closed under multiplication.

\begin{corollary}
\label{cor:sumassoc}
Let $S$ be a $2t$-design that is also an $\scr{A}$-code in $\gras{m}{n}$. If $|\scr{A}| \leq t$, and $Z_i(y)$ is an annihilator polynomial for each $i \leq t$, then $\{A'_\al: \al \in \scr{A}\cup\{m\}\}$ is an association scheme.
\end{corollary}

In fact, these hypotheses can be weakened.

\begin{theorem}
\label{thm:weakscheme}
Let $S$ be a $(2t-2)$-design that is also an $\scr{A}$-code in $\gras{m}{n}$. If $|\scr{A}| = t$, and $Z_i(y)$ is an annihilator for each $0 \leq i \leq t-1$, then $\{A'_\al: \al \in \scr{A}\cup\{m\}\}$ is an association scheme.
\end{theorem}

\begin{proof}
Since $S$ is a $2(t-1)$-design, the idempotents $\{E'_i: 0 \leq i \leq t-1\}$ are linearly independent. We claim that $I$ is also linearly independent from $\{E'_i: 0 \leq i \leq t-1\}$. For, if $I = \sum_{i=0}^{t-1} c_iE'_i$, then the off-diagonal entries of $I$ are functions of a polynomial of degree at most $t-1$ in $\sum_j y_j$, namely 
\[
\frac{1}{|S|}\left(c_0 + \sum_{i=1}^{t-1}c_i(Z_i(y)-Z_{i-1}(y)) \right).
\] 
But all off-diagonal entries are $0$, implying that the polynomial has $t$ roots in $\sum_i y_i$, a contradition. So $\{E'_i: 0 \leq i \leq t-1\} \cup \{I\}$ is linearly independent and therefore spans $\{A'_\al: \al \in \scr{A}\cup\{m\}\}$. Since it is closed under multiplication, we have an association scheme. \qed
\end{proof}

By way of example, suppose $t=2$ in Theorem \ref{thm:weakscheme}. Note that $Z_0(y)$ and $Z_1(y)$ are always annihilators. It follows that if $S$ is a $2$-design, and the inner product set $\scr{A} = \{\tr(P_aP_b): a \neq b \in S\}$ contains exactly two distinct values, then $\{A'_\al: \al \in \scr{A}\cup\{m\}\}$ is a $2$-class association scheme. 

\begin{corollary}
Let $S$ be a $(2t-2)$-design and an $\scr{A}$-code in $\gras{m}{n}$ such that $|\scr{A}| = t$ and $Z_i(y)$ is an annihilator for $i \leq t-1$. Then the idempotents of the scheme $\{A'_\al: \al \in \scr{A}\cup\{m\}\}$ are $E'_0,\ldots,E'_{t-1}$, and $J - \sum_{i=0}^{t-1}E'_i$.
\end{corollary}

\begin{proof}
Let $f_\al$ denote the annihilator polynomial of $\scr{A}\backslash\{\al_0,\al\}$, normalized so that $f_\al(\al) = 1$. Then $f_\al$ is a polynomial of degree $t-1$ in $\sum_i y_i$, and the corresponding zonal polynomial $f_{\al,a}$ is in $H_{t-1}(n)$. Writing $P_i := Z_i - Z_{i-1} = \sum_{\abs{\mu} = i} Z_\mu$, we have
\begin{align*}
(A'_\al E'_i)_{a,b} & = \frac{1}{|S|}\sum_{\tr(P_aP_c) = \al} P_i(\tr(P_cP_b)) \\
& = \ip{f_{\al,a}}{P_{i,b}}_S - \frac{f_\al(m)}{|S|}P_i(\tr(P_aP_b)) \\
& = \ip{f_{\al,a}}{P_{i,b}} - \frac{f_\al(m)}{|S|}P_i(\tr(P_aP_b)).
\end{align*}
Now decomposing into its degrees as $f_\al = \sum_i c_{\al,i} P_i$, we get
\begin{align*}
(A'_\al E'_i)_{a,b} & = c_{\al,i}\ip{P_{i,a}}{P_{i,b}} - \frac{f_\al(m)}{|S|}P_i(\tr(P_aP_b)) \\
& = c_{\al,i}P_i(\tr(P_aP_b)) - \frac{f_\al(m)}{|S|}P_i(\tr(P_aP_b)) \\
& = (c_{\al,i}|S| - f_\al(m))(E'_i)_{a,b}.
\end{align*}
Thus $A'_\al E'_i = \la_{\al,i}E'_i$ for some constant $\la_{\al,i}$. \qed
\end{proof}

---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces"
section_id: sec-003-symmetric-spaces
section_title: "Symmetric spaces"
section_number: null
pages: 7-10
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.958
doc_brief: "Bounds for codes and designs in complex subspaces — We introduce the concepts of complex Grassmannian codes and designs."
---
\label{sec:symmetric}

The group $U(n)/U(m) \times U(n-m)$ is an example of a \defn{symmetric space}: a factor group $G/K$ such that $G$ is a connected semisimple Lie group and $K$ is the fixed point set of an involutive automorphism of $G$. In this section, we use results from Goodman and Wallach \cite{gw1} to explain how the decomposition of representations of $\gras{m}{n}$ follows from this structure.

Let $s_m$ denote the $m \times m$ matrix with backwards diagonal entries of $1$ and $0$ elsewhere:
\[
s_m := \left(\begin{matrix} 
0 & & 1 \\
& \iddots & \\
1 & & 0
                 \end{matrix} \right).
\]

Then $U(n,s_n)$ denotes the group of matrices which preserve the Hermitian form $(x,y) \mapsto x^*s_ny$: that is, $U(n,s_n)$ is the set of matrices $M$ such that $M^*s_nM = s_n$. This group is isomorphic the standard unitary group $U(n)$. Define
\[
J_{m,n} := \left(\begin{matrix} 
& & s_m \\
& I_{n-2m} & \\
s_m & &
                 \end{matrix} \right),
\]
and consider the involution $\th(M) := J_{m,n}MJ_{m,n}$ on $GL_n(\cx)$. The fixed points of $\th$ have the form 
\[
M = \left(\begin{matrix} 
a & b & c \\
d & e & ds_m \\
s_mcs_m & s_mb & s_mas_m 
                 \end{matrix} \right),
\]
so the fixed point set in $GL_n(\cx)$ is isomorphic to $GL_m(\cx) \times GL_{n-m}(\cx)$. 

\begin{lemma}
The fixed point set $K$ of $\th$ in $G = U(n,s_n)$ is isomorphic to $U(m) \times U(n-m)$. Therefore $\gras{m}{n}$ is a symmetric space.
\end{lemma}

\begin{proof}
For $a = (a_1,\ldots,a_m)$, let $\breve{a}$ denote the reversal of $a$, namely
\[
\breve{a} := s_ma = (a_m,\ldots,a_1).
\]
If $a$, $b$, and $c$ have length $m$, $n-2m$ and $m$ respectively, then we have $J_{m,n}(a,b,c)^T = (\breve{c},b,\breve{a})^T$. Therefore the $1$ and $-1$ eigenspaces of $J_{m,n}$ are $V_+ = \{(a,b,\breve{a})\}$ and $V_- = \{(a,0,-\breve{a})\}$ respectively. These spaces are orthogonal with respect to the form $(x,y) \mapsto x^*s_ny$. 

Now $K$ is the set of points in $U(n,s_n)$ which commute with $J_{m,n}$. So decomposing $\cx^n$ into $V_+ \oplus V_-$, we have that $K$ is the set of points in $U(n,s_n)$ which leave both $V_+$ and $V_-$ invariant. In other words, $K$ is the set of points which preserve the form $s_n$ on the subspaces $V_+$ and $V_-$. Thus 
\[
K \cong U(V_+,s_n|_{V_+}) \times U(V_-,s_n|_{V_-}) \cong U(n-m) \times U(m). \eqed
\]
\end{proof}

\begin{comment}
Let $P_{\pm}$ project on to $V_{\pm}$, so $J' = V_+ - V_-$. Then $K$ is the set of points in $U(n,s_n)$ that commute with both $V_+$ and $V_-$. Now $U(V_+,s_n|_{V_+})$ is the set of matrices that $(P_+Ma)^*s_n(P_+Mb) = a^*s_nb$ for all $a,b \in V_+$: that is, the matrices satisfying $P_+M^*P_+s_nP_+MP_+ = P_+s_nP_+$,  and similarly for $V_-$. Any $M \in U(n,s_n)$ commuting with $P_+$ satisfies this condition. Conversely, since $P_{\pm}$ commutes with $s_n$ and $P_\pm s_nP_\pm = \pm P_\pm$, we have that $U(V_\pm,s_n|_{V_\pm})$ is the set of $M$ satisfying $P_\pm M^*P_\pm MP_\pm = P_\pm$.  
\end{comment}

The fact that $K$ is the fixed point set of $\th$ in $G$ implies (\cite[Theorem 12.3.5]{gw1}) that $(G,K)$ is a \defn{spherical pair}: for every irreducible representation $V_\la$ of $G$, the subspace $V_\la^K$ of points fixed by $K$ satisfies $\dim V_\la^K \leq 1$. Those representations such that $V_\la^K$ has dimension exactly $1$ are called \defn{spherical representations}. The following theorem \cite[Theorem V.4.3]{hel} explains how those representation relate to $L^2(G/K)$.

\begin{theorem}
Let $G$ be a compact simply connected semisimple Lie group, and let $K \leq G$ be the fixed point group of an involutive automorphism of $G$. Further let $\hat{G}_K$ denote the set of equivalence classes of spherical representations $V_\la$ of $G$ with respect to $K$. Then $L^2(G/K)$ is a multiplicity-free representation of $G$, and
\[
L^2(G/K) \cong \bigoplus_{\la \in \hat{G}_K} V_\la.
\]
\end{theorem}


To describe which representations are spherical, we now consider diagonal subgroups of $G$ and $K$. For $d = (d_1,\ldots,d_n)$, let $\diag(d)$ denote the diagonal matrix with diagonal entries $d_1,\ldots,d_n$. Firstly, note that $\diag(d)$ is in $U(n,s_n)$ if and only if $d_{n+1-k} = 1/\bar{d_k}$, where $\bar{d_k}$ is the complex conjugate of $d_k$. In other words, if $\bar{d}^{-1}$ denotes the vector $(1/\bar{d_1},\ldots,1/\bar{d_k})$, then $\diag(d)$ is in $U(n,s_n)$ if and only if $\breve{d} = \bar{d}^{-1}$. Secondly, note that if $d = \diag(a,b,c)$ with $a$ and $c$ of length $m$, then $\th(d) = (\breve{c},b,\breve{a})$. It follows that the diagonal group 
\[
T := \{\diag(a_1,\ldots,a_m,c_{m+1},\ldots,c_{n-m},a_m,\ldots,a_1): \abs{a_i} = 1, \breve{c} = \bar{c}^{\,-1}\}
\]
is contained in $K$. In fact, it is a maximal Abelian subgroup of $K$: this is called a \defn{torus} of $K$. 

\begin{comment}
On the other hand, $A = \{\diag(a,c,\breve{c},\breve{a}^{-1}): c_i = \pm 1, a_i \in \re\}$ is a maximally Abelian subgroup of $G$ such that $\th(h) = h^{-1})$ for every $h \in A$: this is called the \defn{anisotropic} torus. 
\end{comment}

Recall that the irreducible representations of $G$ are indexed by the dominant weights $\la = (\la_1,\ldots,\la_n)$, where $\la_i \geq \la_{i+1}$ and $\la_i \in \ints$. Now the spherical representations of $G$ with respect to $K$ are indexed by those particular dominant weights such that $t^{\la} = 1$ for all $t = (t_1,\ldots,t_n)$ in the torus $T$ (see Goodman and Wallach \cite[p. 540]{gw1}). So a dominant weight $\la$ is spherical if it has the form
\[
\la = (\la_1,\ldots,\la_m,0,\ldots,0,-\la_m,\ldots,-\la_1)
\]
with $\la_1 \geq \ldots \geq \la_m \geq 0$ and $\la_i \in \ints$. In other words:

\begin{theorem}
The irreducible representations of $U(n)$ occurring in $L^2(\gras{m}{n})$ are in one-to-one correspondence with the integer partitions with at most $m$ parts.
\end{theorem}

For any partition $\mu$, we let $H_\mu(n)$, or simply $H_\mu$, denote the irreducible representation in $L^2(\gras{m}{n})$ isomorphic to $V_{(\mu,0,\ldots,0,-\breve{\mu})}$. The Weyl character formula (equation \eqref{eqn:weylchar}) now tells us the dimension of each $H_\mu$. The first few dimensions are:
\begin{align*}
\dim H_{(0)} = \dim V_{(0,\ldots,0)} & = 1 \\
\dim H_{(1)} = \dim V_{(1,0,\ldots,0,-1)}& = n^2 - 1 \\
\dim H_{(2)} & = \frac{n^2(n-1)(n+3)}{4} \\
\dim H_{(1,1)} & = \frac{n^2(n+1)(n-3)}{4} \\
\dim H_{(2,1)} & = \frac{(n^2-1)^2(n^2-9)}{9} \\
\dim H_{(k)} & = \binom{n+k-2}{k}^2\frac{n+2k-1}{n-1} \\
\dim H_{(\underbrace{\scriptstyle{1,\ldots,1}}_k)} & = \binom{n+1}{k}^2\frac{n-2k+1}{n+1} 
\end{align*}

If $m = 1$, then $\gras{m}{n}$ is the complex projective space $\cx P^{n-1}$, and only the spaces $H_{(k)}$ occur. In that case $H_{(k)}$ is isomorphic to the space $\Harm(k,k)$ of harmonic polynomials of homogeneous degree $k$ in both $z$ and $\bar{z}$, where $z = (z_1,\ldots,z_n)$ is a point on the unit sphere in $\cx^n$. Those harmonic polynomials were used by Delsarte, Goethals, and Seidel in their LP bounds for codes and designs the complex unit sphere \cite{dgs}.

We now record a few more representations of $U(n)$ we will need later. Given an nonincreasing sequence of nonnegative integers $\mu = (\mu_1,\mu_2,\ldots)$, we say $\mu$ has \defn{size} $k$ and write $\abs{\mu} = k$ if $\mu$ is a partition of $k$; that is, $\sum_i \mu_i = k$. We also say $\mu$ has \defn{length} $l$ and write $\len(\mu) = l$ if $\mu$ has $l$ nonzero entries. For example, $(2,1,0,\ldots)$ has size $3$ and length $2$. Then for fixed $\gras{m}{n}$, define $H_k = H_k(m,n)$ as follows:
\[
H_k(m,n) := \bigoplus_{\substack{\abs{\mu} \leq k \\ \len(\mu) \leq m}} H_\mu(n).
\]
For $k > 0$ this representation is reducible, and $H_{k-1}$ is contained in $H_k$. When $m=1$, $H_k$ is isomorphic to the space of homogeneous polynomials degree $k$ in both $z$ and $\bar{z}$ on the unit sphere in $\cx^n$. In the next section, we will see that $H_k$ is also the span of the
degree-$k$ symmetric polynomials on the principal angles between $a \in \gras{m}{n}$ and some fixed $b \in \gras{m}{n}$. Moreover, if $g$ and $h$ are polynomials in $H_k$ and $H_{k'}$ respectively, then $gh$ is in $H_{k+k'}$, and in fact $H_{k+k'}$ is spanned by polynomials of that form.

We also let $\Hom_k(n) \sbs L^2(\gras{m}{n})$ denote the space of polynomials which are homogeneous of degree $k$ in the entries of $P_a$, where $P_a$ is the projection matrix of $a \in \gras{m}{n}$. Since the constant function $P_a \mapsto \tr(P_a) = m$ is in $\Hom_1(n)$, it follows that $\Hom_{k-1}(n)$ can be embedded into $\Hom_k(n)$. Similarly for fixed $b$, the distance function $P_a \mapsto \tr(P_aP_b)$ is in $\Hom_1(n)$. The next section will also show that $H_k$ is a subspace of $\Hom_k$.

James and Constantine \cite{jc1} further investigated the irreducible subspaces of $L^2(\gras{m}{n})$, finding zonal polynomials for each irreducible representation. We describe those results in the next section.

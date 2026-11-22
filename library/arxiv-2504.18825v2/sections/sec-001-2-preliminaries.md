---
doc_id: arxiv-2504.18825v2
doc_title: "Murnaghan-Nakayama rule for the cyclotomic Hecke algebra and applications"
section_id: sec-001-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 7-12
source_pdf: 2504.18825v2.pdf
source_sha256: 829f97190cb1c8ad
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.958
doc_brief: "Murnaghan-Nakayama rule for the cyclotomic Hecke algebra and applications — We establish a Murnaghan–Nakayama rule for the irreducible characters of the cyclotomic Hecke algebra Hm,n(q, u) on Shoji’s"
---
\subsection{Multipartitions and corresponding symmetric functions}
The terminologies and notations about classical {\it partitions}, such as {\it length, weight, diagram}, etc, can be found in \cite[Chapter I]{Mac}. Now we introduce the corresponding notions and definitions in the context of {\em multipartitions}. A $m$-multipartition (resp. $m$-multicomposition) of $n$ is an ordered tuple $\bm{\la}=(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})$ of partitions (resp. compositions) $\la^{(i)}$ such that $|\bm{\la}|=\sum_{i=1}^{m}|\la^{(i)}|=n$. We denote by $\mathcal{P}_{n,m}$ the set of all $m$-multipartitions of $n$. Let $C_{n,m}$ denote the set of $m$-tuples of nonnegative integers summing to $n$, i.e., an element in $C_{n,m}$ has the form $(c_1, c_2, \cdots, c_m)$ with $c_i$ nonnegative integer such that $\sum_{i=1}^{m}c_i=n$. 
Occasionally, we will omit $m$, just say $\bla$ is a multipartition (or multicomposition), for short unless special emphasis. We usually write $\bm{\la}$ in bold to emphasize that $\bm{\la}$ is a multipartition. Define $l(\bm{\la})=\sum_{i\geq1}^ml(\la^{(i)})$. The {\it diagram} of the multipartition $\bm{\la}$ is naturally the sequence of the consecutive Young diagrams of $\la^{(i)}$, $i=1,2,\cdots,m$. Here is an example for a $5$-multipartition of $24$ with length $11$.
\begin{align}\label{e:la}
\big((3,2,1),(3,3,1,1),\varnothing,(2,2,2),(4)\big)=\left( \begin{array}{ccccc}
\begin{tikzpicture}[scale = 0.33]
  \begin{scope}
    \clip (0,0) -| (1,1) -| (2,2) -| (3,3) -- (0,3) -- (0,0);
    \draw [color=black!25] (0,0) grid (3,3);
  \end{scope}
  \draw [thick] (0,0) -| (1,1) -| (2,2) -| (3,3) -- (0,3) -- (0,0);
\end{tikzpicture},&
\begin{tikzpicture}[scale = 0.33]
  \begin{scope}
    \clip (0,0) -| (1,2) -| (3,4) -- (0,4) -- (0,0);
    \draw [color=black!25] (0,0) grid (3,4);
  \end{scope}
  \draw [thick] (0,0) -| (1,2) -| (3,4) -| (0,4) -- (0,0);
\end{tikzpicture},&
    \varnothing,&
    \begin{tikzpicture}[scale = 0.33]
  \begin{scope}
    \clip (0,0) -| (2,3) -- (0,3) -- (0,0);
    \draw [color=black!25] (0,0) grid (2,3);
  \end{scope}
  \draw [thick] (0,0) -| (2,3)  -- (0,3) -- (0,0);
\end{tikzpicture},&
\begin{tikzpicture}[scale = 0.33]
  \begin{scope}
    \clip (0,0) -| (4,1) -- (0,1) -- (0,0);
    \draw [color=black!25] (0,0) grid (4,1);
  \end{scope}
  \draw [thick] (0,0) -| (4,1) -- (0,1) -- (0,0);
\end{tikzpicture}
\end{array}  \right).
\end{align}





For two arbitrary multipartitions $\bm{\la},\bm{\mu}\in \mathcal{P}_{n,m}$, we say $\bm{\mu}\subset\bm{\la}$ if $\mu^{(i)}\subset\la^{(i)}$ for all $1\leq i\leq m$. We define the {\it $m$-multi skew diagram} of $\bm{\la}/\bm{\mu}$ (denoted by $\D(\bla/\bmu)$) as the sequence of the consecutive skew diagrams of $\la^{(i)}/\mu^{(i)}$. For instance, we choose $\bm{\la}$ in the above figure and $\bm{\mu}=((2,1,1),(2,1,1),\varnothing,(2,1),(2))$. Clearly, $\bmu\subset\bla$. The skew diagram of $\bla/\bmu$ is presented as below:
\begin{align}\label{e:la/mu}

\D(\bm{\la/\mu})=\left( \begin{array}{ccccc}
\begin{tikzpicture}[scale = 0.35]
  \begin{scope}
    \clip (0,0) -| (1,1) -| (2,2) -| (3,3) -- (0,3) -- (0,0);
    \draw [color=black!25] (0,0) grid (3,3);
  \end{scope}
  \draw [thick] (0,0) -| (1,1) -| (2,2) -| (3,3) -- (0,3) -- (0,0);
      \node [draw, circle, fill = white, inner sep = 1.5pt] at (1.5,1.5) { };
      \node [draw, circle, fill = white, inner sep = 1.5pt] at (2.5,2.5) { };
\end{tikzpicture},&
\begin{tikzpicture}[scale = 0.35]
  \begin{scope}
    \clip (0,0) -| (1,2) -| (3,4) -- (0,4) -- (0,0);
    \draw [color=black!25] (0,0) grid (3,4);
  \end{scope}
  \draw [thick] (0,0) -| (1,2) -| (3,4) -- (0,4) -- (0,0);
     \draw [thick, rounded corners] (1.5,2.5) -- (2.5,2.5) -- (2.5,3.5);
       \draw [color=black,fill=black,thick] (2.5,3.5) circle (.6ex); 
      \node [draw, circle, fill = white, inner sep = 1.5pt] at (0.5,0.5) { };
      \node [draw, circle, fill = white, inner sep = 1.5pt] at (1.5,2.5) { };
\end{tikzpicture},&
\varnothing,&
 \begin{tikzpicture}[scale = 0.35]
  \begin{scope}
    \clip (0,0) -| (2,3) -- (0,3) -- (0,0);
    \draw [color=black!25] (0,0) grid (2,3);
  \end{scope}
  \draw [thick] (0,0) -| (2,3)  -- (0,3) -- (0,0);
  \draw [thick, rounded corners] (0.5,0.5) -- (1.5,0.5) -- (1.5,1.5);
       \draw [color=black,fill=black,thick] (1.5,1.5) circle (.6ex); 
      \node [draw, circle, fill = white, inner sep = 1.5pt] at (0.5,0.5) { };
\end{tikzpicture},&
\begin{tikzpicture}[scale = 0.35]
  \begin{scope}
    \clip (0,0) -| (4,1) -- (0,1) -- (0,0);
    \draw [color=black!25] (0,0) grid (4,1);
  \end{scope}
  \draw [thick] (0,0) -| (4,1) -- (0,1) -- (0,0);
  \draw [thick, rounded corners] (2.5,0.5) -- (3.5,0.5);
       \draw [color=black,fill=black,thick] (3.5,0.5) circle (.6ex); 
      \node [draw, circle, fill = white, inner sep = 1.5pt] at (2.5,0.5) { };
\end{tikzpicture}
\end{array}  \right).
\end{align}

Let $\Lambda_{\mathbb{Q}}$ be the ring of symmetric functions in the $x_n$ ($n\in\mathbb N$) over $\mathbb{Q}$. As is well known, the ring $\Lambda_{\mathbb{Q}}$ has several linear bases indexed by partitions such as power sum functions $p_{\la}(x)$, elementary symmetric functions $e_{\la}(x)$, complete symmetric functions $h_{\la}(x)$ and Schur functions $s_{\la}(x)$, etc., and the reader 
is referred to \cite[Chap. I]{Mac} for their definitions. There exists the canonical Hall inner product on $\Lambda_{\mathbb{Q}}$ defined by:
\begin{align}\label{e:z}
\langle p_{\la}(x), p_{\mu}(x) \rangle=\delta_{\la,\mu}z_{\la},
\end{align}
where $z_{\lambda}=\prod_{i\geq 1}i^{m_i(\lambda)}m_i(\lambda)!$, under which the Schur functions forms an orthonormal basis. 

Let us consider the tensor product $\Lambda_{\mathbb{Q}}^{\otimes m}$. Now we extend these notions to the setting of $m$-multipartitions.
Let $x^{(i)}_j$ ($1\leq i\leq m$, $j\geq 1$) be $m$ sets of variables.  For each integer $k\geq 1$ and $1\leq i\leq m$, let
\begin{align}
p_{k}^{(i)}(x)=\sum_{j=1}^{m}\zeta^{-ij}p_{k}(x^{(j)}),
\end{align}
where $p_k(x^{(j)})$ are the ordinary $k$-th power sum symmetric functions in the variables $x^{(j)}_1,x^{(j)}_2,\cdots$, and throughout the paper $\zeta$ is a fixed primitive $m$-th root of unity. We define the power sum function $p_{\bm{\la}}$ associated with $m$-multipartition $\bm{\la}=(\la^{(1)},\la^{(2)},\cdots,\la^{(m)})$ by
\begin{align}\label{e:def-p}
p_{\bm{\la}}(x)=\prod_{i=1}^{m}\prod_{j=1}^{l(\la^{(i)})}p^{(i)}_{\la^{(i)}_j}(x).
\end{align}
Similarly, the Schur function $s_{\bm{\la}}(x)$ associated with $\bm{\la}$ is defined by
\begin{align}
s_{\bm{\la}}(x)=\prod_{i=1}^{m}s_{\la^{(i)}}(x^{(i)}),
\end{align}
where $s_{\la^{(i)}}(x^{(i)})$ denotes the ordinary Schur function associated with partition $\la^{(i)}$ in the variables $x^{(i)}_1,x^{(i)}_2,\cdots$. We refer to $s_{\bm{\la}}(x)$ as {\em multi-Schur functions}.

Clearly the tensor products of basis elements from a given basis of $\Lambda_{\mathbb{Q}}$ will form
a basis for the tensor product space $\Lambda_{\mathbb{Q}}^{\otimes m}$. In particular, $\{s_{\bm{\la}}\mid\bm{\la}\in \mathcal{P}_{n,m}\}$ forms a basis in $\Lambda_{\mathbb{Q}}^{\otimes m}$.
We canonically extend the inner product of $\Lambda_{\mathbb{Q}}$ to $\Lambda_{\mathbb{Q}}^{\otimes m}$. Namely,
\begin{align}\label{e:tensor}
\langle u_1\otimes\cdots\otimes u_m, v_1\otimes\cdots\otimes v_m \rangle_{\otimes}:=\prod_{i=1}^m\langle u_i,v_i \rangle
\end{align}
for any two sets of elements $\{u_i\}$, $\{v_i\}$ in $\Lambda_{\mathbb{Q}}$ and extend bilinearly.
Then we have
\begin{align}\label{e:orth}
\langle s_{\bm{\la}}, s_{\bm{\mu}} \rangle_{\otimes}=\delta_{\bm{\la}\bm{\mu}}.
\end{align}
This means $\{s_{\bm{\la}}\mid\bm{\la}\in \mathcal{P}_{n,m}\}$ forms an orthonormal basis in $\Lambda_{\mathbb{Q}}^{\otimes m}$.



\subsection{Frobenius-type formula for the cyclotomic Hecke algebra}\label{ss:Fro}
Let $\mathscr{W}_{m,n}$ be the complex reflection group of type $G(m, 1, n)$ (cf. \cite{ST}) (called complex reflection group for short), which is 
generated by $s_1,s_2,\cdots, s_n$ with the relations
\begin{align}
\begin{split}
&s_{1}^{m}=1, \quad s_{2}^2=\cdots=s^2_{n}=1,\\
&s_1s_2s_1s_2=s_2s_1s_2s_1,\\
&s_is_j=s_js_i, \quad\text{if $|i-j|>1$},\\
&s_is_{i+1}s_i=s_{i+1}s_is_{i+1}, \quad\text{for $2\leq i<n$}.
\end{split}
\end{align}
Denote by $\mathfrak{S}_n$ the symmetric group on $n$ letters. It is well-known that $\mathscr{W}_{m,n}=(\mathbb{Z}/m\mathbb{Z})^n \rtimes \mathfrak{S}_n$, where $s_2,\cdots, s_n$ are respectively the transpositions $(1,2), \cdots, (n-1,n)$ in $\mathfrak{S}_n$ and $s_1$ corresponds to the generator of the cyclic group. Several Murnaghan--Nakayama type rules for the complex reflection group $\mathscr{W}_{m,n}$ were
found in \cite{Osi, St, AK, GJ}.





Let $\mathbb{K}=\mathbb{C}(q,\bm{u})$ be the field of rational functions in indeterminates $q$ (called {\em Hecke parameter}) and $\bm{u}=(u_1,\cdots,u_m)$ (called {\em cyclotomic parameters}). The cyclotomic Hecke algebra $\mathscr{H}_{m,n}(q,\bm{u})$ \cite{AK,BM,C} (also called the Ariki-Koike algebra) associated to $\mathscr{W}_{m,n}$ is the unital associative $\mathbb{K}$-algebra generated by $g_1, g_2, \cdots, g_n$ and subject to relations\footnote{The presentation is slightly different from that in \cite{AK}. They are isomorphic by the substitutions: $g_i\rightarrow q^{-1}g_i$, $u_i\rightarrow q^{-1}u_i$ and $q^2\rightarrow q$.}
\begin{align}
\begin{split}
&(g_1-u_1)\cdots(g_1-u_m)=0,\\
&g_1g_2g_1g_2=g_2g_1g_2g_1,\\
&g_i^2=(q-q^{-1})g_i+1, \quad \text{for $2\leq i\leq n$},\\
&g_ig_j=g_jg_i, \quad \text{for $|i-j| > 1$},\\
&g_ig_{i+1}g_i = g_{i+1}g_ig_{i+1},\quad \text{for $2 \leq i < n$}.
\end{split}
\end{align}
It is known \cite{AK} that $\mathscr{H}_{m,n}(q,\bm{u})$ is a free $\mathbb{K}$-module of rank $n!m^n$. The algebra $\mathscr{H}_{m,n}(q,\bm{u})$ reduces to $\mathscr{W}_{m,n}$ by specializing $q=1$ and $\bm{u}=\bm{\zeta}=(1,\zeta,\cdots,\zeta^{m-1})$, i.e., $u_i=\zeta^{i-1}$, $i=1,2,\cdots,m$.


Let us recall the irreducible character table of $\mathscr{H}_{m,n}(q,\bm{u})$. It is well known that the set of conjugacy classes in $\mathscr{W}_{m,n}$ is parametrized by $\mathcal{P}_{n,m}$ \cite{AK}.
For a survey on the representation theory of $\mathscr{H}_{m,n}(q,\bm{u})$ and $q$-Schur algebras, see \cite{Mat}.

Let $A$ be the matrix of degree $m$ whose $(a,b)$-entry is $u^a_b$  for $0 \leq a\leq m-1$ and $1\leq b \leq m$. 

Its determinant $\Delta=\det A=\prod_{i>j}(u_i-u_j)$ is the Vandermonde determinant. Let $B=A^*$ be the adjoint matrix of $A$. We write $B=(v_{b,a}(\bm{u}))$, where $v_{b,a}(\bm{u})$ is a polynomial in $\bm{u}$. For $1 \leq a \leq m$, we define $F_b(X)$ as the generating polynomial of $v_{b, a}(\bm u)$ as follows:

\begin{align*}
F_b(X)=\sum_{0\leq a\leq m-1}v_{b,a}(\bm{u})X^a.
\end{align*}

Following \cite[Sec. 3.6]{Sho}, let $\mathscr{H}^{\natural}$ be the associative algebra over $\mathbb{K}$ generated by $g_2,\cdots, g_n$ and $\xi_{1},\cdots,\xi_{n}$ subject to the following relations:
\begin{align*}
&(g_i-q)(g_i + q^{-1})=0, \quad 2 \leq i \leq n;\quad (\xi_i-u_1)\cdots(\xi_i-u_m) = 0,\quad 1 \leq i \leq n;\\
&g_ig_{i+1}g_i = g_{i+1}g_ig_{i+1},\quad 2 \leq i < n;\quad g_ig_j = g_jg_i,\quad |i-j| \geq 2;\\
&\xi_i\xi_j = \xi_j\xi_i,\quad 1 \leq i, j \leq n;\quad g_j\xi_i = \xi_ig_j ,\quad i \neq j-1, j;\\
&g_j\xi_j = \xi_{j-1}g_j + \Delta^{-2}\sum_{a<b}(u_a-u_b)(q-q^{-1})F_a(\xi_{j-1})F_b(\xi_j),\quad 2\leq j\leq n;\\
&g_j\xi_{j-1} = \xi_{j}g_j-\Delta^{-2}\sum_{a<b}(u_a-u_b)(q-q^{-1})F_a(\xi_{j-1})F_b(\xi_j),\quad 2\leq j\leq n.
\end{align*}
Then $\mathscr{H}^{\natural}$ is isomorphic to $\mathscr{H}_{m,n}(q,\bm{u})$ owing to \cite[Theorem 3.7]{Sho}.

We define the {\it standard elements} $g(\bm{\mu})\in \mathscr{H}_{m,n}(q,\bm{u})$ as follows. Fix $m\ge 1$ and $n\ge 1$.  For any composition $\alpha=(\alpha_1,\ldots,\alpha_\ell)$ of $n$
(with $\alpha_k\ge 1$), set $b_0=0$ and $b_t=\alpha_1+\cdots+\alpha_t$ for $1\le t\le \ell$.
For each $t$, let $\mathscr{H}^{\natural}_{m,\alpha_t}$ be the cyclotomic Hecke algebra on
$\alpha_t$ letters (with generators $g_2,\ldots,g_{\alpha_t}$ and $\xi_1,\ldots,\xi_{\alpha_t}$),
and consider the block-embedding
\[
\iota_{\alpha}:\ 
\mathscr{H}^{\natural}_{m,\alpha_1}\otimes\cdots\otimes \mathscr{H}^{\natural}_{m,\alpha_\ell}
\ \hookrightarrow\ \mathscr{H}^{\natural}_{m,n}
\]
defined on generators by
\[
\iota_{\alpha}\big(g^{(t)}_{k}\big)=g_{b_{t-1}+k},\quad (2\le k\le \alpha_t),\qquad
\iota_{\alpha}\big(\xi^{(t)}_{k}\big)=\xi_{b_{t-1}+k},\quad (1\le k\le \alpha_t),
\]
where $g^{(t)}_{k},\xi^{(t)}_{k}$ denote the generators in the $t$-th tensor factor.
(Thus the images of different tensor factors commute, giving a single embedding.)

For $1\le i\le m$ and $r\ge 1$, define the $i$-cycle element in $\mathscr{H}^{\natural}_{m,r}$ by
\[
g_{r,i}:=\xi_r^{\,i-1}\,g_r g_{r-1}\cdots g_2,
\]
(with the convention $g_{1,i}:=\xi_1^{\,i-1}$).
Now for a partition $\mu=(\mu_1,\ldots,\mu_\ell)$ of $r$, define
\[
g(\mu,i):=\iota_{\mu}\big(g_{\mu_1,i}\otimes g_{\mu_2,i}\otimes\cdots\otimes g_{\mu_\ell,i}\big)
\ \in\ \mathscr{H}^{\natural}_{m,r},
\]
where $\iota_{\mu}$ stands for the above embedding with $\alpha=\mu$.

Finally, for a multipartition $\bm{\mu}=(\mu^{(1)},\ldots,\mu^{(m)})\in\mathcal{P}_{n,m}$, define
the standard element
\[
g(\bm{\mu}) := g(\mu^{(1)},1)\, g(\mu^{(2)},2)\cdots g(\mu^{(m)},m)\ \in\ \mathscr{H}^{\natural}_{m,n},
\]
and view it in $\mathscr{H}_{m,n}(q,\bm u)$ via the isomorphism
$\mathscr{H}^{\natural}\simeq \mathscr{H}_{m,n}(q,\bm u)$.













It was proved in \cite[Proposition 7.5]{Sho} that the characters $\chi^{\bm{\la}}$ of $\mathscr{H}_{m,n}(q,\bm{u})$ are determined completely by their values on $g(\bm{\mu})$ for all $\bm{\mu}\in \mathcal{P}_{n,m}$. For simplicity, we write $\chi^{\bm{\la}}_{\bm{\mu}}$ for $\chi^{\bm{\la}}(g(\bm{\mu}))$ in short. $\chi^{\bm{\la}}_{\bm{\mu}}$ forms the irreducible character table of $\mathscr{H}_{m,n}(q,\bm{u})$ when $\bm{\la}$ and $\bm{\mu}$ run over $\mathcal{P}_{n,m}$.

Recall the Hall-Littlewood function $q_{k}(x;t)$ defined by
\begin{align*}
q_0(x;t)&=1,\\
q_k(x;t)&=(1-t)\sum_{i\geq 1}x_i^k\prod_{j\neq i}\frac{x_i-tx_j}{x_i-x_j} \quad (k\geq 1).
\end{align*}
It is expedient to consider the generating function of $q_{k}(x;t)$:
\begin{align}\label{e:generating-q}
Q(z;t)=\sum_{k=0}^{\infty}q_{k}(x;t)z^k=\prod_{i}\frac{1-x_itz}{1-x_iz}.
\end{align}
Now we introduce a family of symmetric functions $q_{\bm{\mu}}(x;q,\bm{u})$ as follows. For each $1\leq i\leq m$, let
\begin{align*}
q^{(i)}_{n}(x;q,\bm{u})=\frac{q^n}{q-q^{-1}}\sum_{c\in C_{n,m}}u^i_c\prod_{j=1}^{m}q_{c_j}(x^{(j)};q^{-2}) \qquad\text{for $n\geq 1$,}
\end{align*}
where $c=(c_1,\cdots,c_m)$ runs through $C_{n, m}$, and $u_c$ denotes $u_k$ for the largest integer $k$ such that $c_k\neq 0$. For convention $q^{(i)}_{0}(x;q,\bm{u}):=\frac{1}{q-q^{-1}}$.
Then define $q_{\bm{\mu}}(x;q,\bm{u})$ by
\begin{align*}
q_{\bm{\mu}}(x;q,\bm{u})=\prod_{i=1}^m\prod_{j=1}^{l(\mu^{(i)})}q^{(i)}_{\mu_j^{(i)}}(x;q,\bm{u}).
\end{align*}

The Frobenius formula for the characters of the cyclotomic Hecke algebra can be stated as follows \cite[Theorem 6.14]{Sho}.
\begin{thm}\label{t:fro}
Let $\bm{\la},\bm{\mu}\in \mathcal{P}_{n,m}$, then the irreducible character $\chi^{\bm{\la}}_{\bm{\mu}}$ is determined by
\begin{align}\label{e:fro}
q_{\bm{\mu}}(x;q,\bm{u})=\sum_{\bm{\la}\in \mathcal{P}_{n,m}} \chi^{\bm{\la}}_{\bm{\mu}}s_{\bm{\la}}.
\end{align}
\end{thm}


\subsection{$\la$-ring theory} For the $\la$-ring theory, we mainly refer the reader to \cite{Knu}. A {\em pre-$\lambda$-ring} is a commutative ring $\R$ with identity $1$ endowed a series of operations $\lambda^i: \R\rightarrow \R$ for $i\in\mathbb{N}$, such that for all $r\in\R$, the formal power series
\begin{align}\label{E:c1}
\lambda_z(r)=\sum_{i=0}^{\infty}\lambda^i(r)z^i=\lambda^0(r)+\lambda^1(r)z+\lambda^2(r)z^2+\cdots
\end{align}
 satisfies 

\begin{align}\label{E:la1}
\lambda^0(r)=1,\quad \lambda^1(r)=r\quad \text{and}\quad \lambda_z(r+r')=\lambda_z(r)\lambda_z(r') \quad \text{for all $r,r'\in\R$}.
 
\end{align}
\eqref{E:la1} gives $\lambda_z(0)=1$ and $\lambda_z(r)=\lambda_z(-r)^{-1}$. A {\em $\la$-ring} is a pre-$\la$-ring attached more conditions involving expressions for $\la^i(xy)$ and $\la^i(\la^j(x))$. However, we will not delve further into the general theory of $\la$-ring here. See \cite[Chapter I]{Knu} for details.

Consider the ring of symmetric functions $\Lambda_{\mathbb{Q}}$, which is a free $\lambda$-ring on one generator, i.e., $\Lambda_{\mathbb{Q}}=\mathbb{Q}[e_1,e_2,\cdots]$ with $\lambda^i(e_1)=e_i$ where $e_i$ is the $i$-th elementary symmetric function. If we choose $x_1,x_2,\cdots$ as the variables. Then $\lambda^i(X)=e_i$. Here $X=e_1(x)=x_1+x_2+\cdots$. If we define $\sigma^i(r):=(-1)^i\lambda^i(-r)$ and
\begin{align*}
\sigma_z(r):=\sum_{i=0}^{\infty}\sigma^i(r)z^i=\sum_{i=0}^{\infty}
\lambda^i(-r)(-z)^i=\lambda_{-z}(-r).
\end{align*}
Then we have
\begin{align}
e_i(x)&=\lambda^i(X), \qquad\quad h_i(x)=\sigma^i(X),\\
E(x;z)&=\lambda_z(X),\qquad H(x;z)=\sigma_z(X),
\end{align}
where $E(x;z)$ and $H(x;z)$ are respectively the generating functions of $e_r(x)$ and $h_r(x)$ ($r$-th complete symmetric function) given by
\begin{align}\label{e:defe}
E(x;z):=\sum_{n\geq0}e_n(x)z^n&=\prod_{i\geq1}\left(\sum_{0\le j\le 1}(x_iz)^j\right)=\prod_{i\geq1}(1+x_iz),\\
\label{e:defh}
H(x;z):=\sum_{n\geq0}h_n(x)z^n&=\prod_{i\geq1}\left(\sum_{j\geq0}(x_iz)^j\right)=\prod_{i\geq1}\frac{1}{1-x_iz}.
\end{align}
Now we rewrite $q_{k}(x;t)$ by using the $\la$-ring notation. By \eqref{e:generating-q}, we have
\begin{align}
    Q(z;t)=\frac{\sigma_z(X)}{\sigma_z(tX)}=\sigma_z\big((1-t)X\big),
\end{align}
which further yields
\begin{align}\label{e:q-laring}
   q_{k}(x;t)=\sigma^k\big((1-t)X\big).
\end{align}

For any two partitions $\mu\subset\la$, we define the {\em skew Schur operation} $s^{\la/\mu}(X)$ in the $\la$-ring $\Lambda_{\mathbb{Q}}$ by
\begin{align}
    s^{\la/\mu}(X):=\det_{1\leq i,j\leq l(\la)}(\sigma^{\la_i-i-\mu_j+j}(X)).
\end{align}
We have the following properties of $s^{\la/\mu}(X)$:
\begin{align}\label{e:schurrule}
\begin{split}
s^{\la/\mu}(X+Y)&=\sum_{\mu\subset\nu\subset\la}s^{\la/\nu}(X)s^{\nu/\mu}(Y) \quad \text{(sum rule)}\\
s^{\la/\mu}(-X)&=(-1)^{|\la/\mu|}s^{\la^{t}/\mu^{t}}(X) \quad \text{(duality rule)}\\
s^{\la/\mu}(tX)&=t^{|\la/\mu|}s^{\la/\mu}(X) \quad \text{(homogeneity)}.
\end{split}
\end{align}
Here $\la^{t}$ is the {\it conjugate} of $\la$, obtained from $\la$ by transposing the diagram $\D(\la)$ along the main diagonal. These identities can be found in the literature, for instance \cite[p. 43, p. 72]{Mac}, \cite[(6.2)]{HR95}, etc.

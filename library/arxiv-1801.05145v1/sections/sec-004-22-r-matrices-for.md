---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-004-22-r-matrices-for
section_title: "R-matrices for"
section_number: 2.2
pages: 18-20
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.921
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
\hfill




  For $|\beta|=n$ and $1\le a<n$,  we define $\vphi_a\in R( \beta)$
by
\eqn&&\ba{l}
  \vphi_a e(\nu)=
\begin{cases}
  \bl\tau_ax_a-x_{a}\tau_a\br e(\nu)
  & \text{if $\nu_a=\nu_{a+1}$,} \\[2ex]
\tau_ae(\nu)& \text{otherwise.}
\end{cases}
 \ea \eneqn
They are called the {\em intertwiners}. Since $\{\vphi_a\}_{1\le a<n}$
satisfies the braid relation, $\vphi_w\seteq\vphi_{i_1}\cdots\vphi_{i_\ell}$
does not depend on the choice of reduced expression $w=s_{i_1}\cdots s_{i_\ell}$.


For $m,n\in\Z_{\ge0}$,
let us denote by $w[{m,n}]$ the element of $\sym_{m+n}$  defined by
\eqn
&&w[{m,n}](k)=\begin{cases}k+n&\text{if $1\le k\le m$,}\\
k-m&\text{if $m<k\le m+n$.}\end{cases}
\eneqn

Let $\beta,\gamma\in \rtl^+$ with $|\beta|=m$, $|\gamma|=n$,
 and let
$M$ be an $R(\beta)$-module and $N$ an $R(\gamma)$-module. Then the
map $M\tens N\to N\conv M$ given by
$u\tens v\longmapsto \vphi_{w[n,m]}(v\tens u)$
is  $R( \beta)\tens R(\gamma )$-linear, and  hence it extends
to an $R( \beta +\gamma)$-module  homomorphism
\eqn &&R_{M,N}\col
M\conv N\To N\conv M. \eneqn





\medskip
Assume that the \KLR\ $R(\beta)$ is symmetric.
Let $z$ be an indeterminate  which is homogeneous of degree $2$, and
let $\psi_z$ be the graded algebra homomorphism
\eqn
&&\psi_z\col R( \beta )\to \cor[z]\tens R( \beta )
\eneqn
given by
$$\psi_z(x_k)=x_k+z,\quad\psi_z(\tau_k)=\tau_k, \quad\psi_z(e(\nu))=e(\nu).$$

For an $R( \beta )$-module $M$, we denote by $M_z$
the $\bl\cor[z]\tens R( \beta )\br$-module
$\cor[z]\tens M$ with the action of $R( \beta )$ twisted by $\psi_z$.
Namely,
\eqn&&
\ba{l}
e(\nu)(a\tens u)=a\tens e(\nu)u,\\[1ex]
x_k(a\tens u)=(za)\tens u+a\tens (x_ku),\\[1ex]
\tau_k(a\tens u)=a\tens(\tau_k u)
\ea
\label{eq:spt1}
\eneqn
for  $\nu\in I^\beta$,  $a\in \cor[z]$ and $u\in M$.
 Note that the multiplication by $z$ on $\cor[z]$ induces  an  $R(\beta)$-module endomorphism on $M_z$.
 For $u\in M$, we sometimes denote by $u_z$ the corresponding element $1\tens u$ of
the $R( \beta )$-module  $M_z$.



For a non-zero $M\in R(\beta)\smod$
and a non-zero $N\in R(\gamma)\smod$,
\eq&&\parbox{70ex}{
let $s$ be the order of zero of $R_{M_z,N}\col  M_z\conv
N\To N\conv M_z$;
i.e., the largest non-negative integer such that the image of
$R_{M_z,N}$ is contained in $z^s(N\conv M_z)$.}
\label{def:s} \eneq
Note that such an $s$ exists because
$R_{M_z,N}$ does not vanish (\cite[Proposition 1.4.4 (iii)]{K^3}).
We denote by $\Rm_{M_z,N}$
the morphism $z^{-s}R_{M_z,N}$.

\Def Assume that $R(\beta)$ is symmetric.
For a non-zero $M\in R(\beta)\smod$
and a non-zero $N\in R(\gamma)\smod$,
let $s$ be an integer as in \eqref{def:s}.
We define $$\rmat{M,N}\col M\conv N\to N\conv M$$
by  $$\rmat{M,N} = \Rm_{M_z,N}\vert_{z=0},$$
and call it the {\em renormalized R-matrix}.
\edf


By the definition, the renormalized R-matrix
$\rmat{M,N}$ never vanishes.

We define also
$$\rmat{N,M}\col N\conv M\to M\conv N$$
by  $$\rmat{N,M} = \bl (-z)^{-t}R_{N,M_z}\br\vert_{z=0},$$
where $t$ is the order of zero of
$R_{N,M_z}$.

If $R(\beta)$ and $R(\gamma)$ are symmetric, then
$s$ coincides with the order of zero of
$R_{M,N_z}$, and $\bl z^{-s}R_{M_z,N}\br\vert_{z=0}=\bl (-z)^{-s}R_{M,N_z}\br\vert_{z=0}$
(see, \cite[(1.11)]{KKKO14}).

By the construction, if the composition
$(N_1 \conv \rmat{M,N_2}) \circ (\rmat{M,N_1} \conv N_2)$
for $M,N_1,N_2 \in R \smod$
doesn't vanish, then it is equal to $\rmat{M,N_1 \circ N_2}$.

\Def
A simple $R(\beta)$-module $M$ is called \emph{real} if $M \conv M$ is simple.
\edf

The  following lemma was used significantly in \cite{KKKO14}.
\Lemma[{\cite[Lemma 3.1]{KKKO14}}] \label{lem:simplicity}
Let $\beta_k\in\rtl^+$ and $M_k\in R(\beta_k)\smod$
$(k=1,2,3)$.
Let $X$ be an $R(\beta_1+\beta_2)$-submodule of $M_1\conv M_2$ and
$Y$ an $R(\beta_2+\beta_3)$-submodule of $M_2\conv M_3$
such that $X\conv M_3\subset M_1\conv Y$ as submodules of
$M_1\conv M_2\conv M_3$.
Then there exists an $R(\beta_2)$-submodule $N$ of $M_2$
such that
$X\subset M_1\conv N$ and $N\conv M_3\subset Y$.
\enlemma

One of the main results in \cite{KKKO14} is
\Th[{\cite[Theorem 3.2]{KKKO14}}] \label{thm:simplicity}
Let $\beta, \gamma \in \rootl^+$ and assume that $R(\beta)$ is symmetric.
Let $M$ be a real simple module in
$R(\beta) \smod$ and
$N$ a simple module in $R(\gamma) \smod$.
Then
\bnum
  \item $M \conv N$ and $N \conv M$ have simple socles and simple heads.
  \item Moreover, $\Im(\rmat{M,N})$ is equal to the head of $M \conv N$
and socle of $N \conv M$.
Similarly,
$\Im(\rmat{N,M})$ is equal to the head of $N \conv M$
and socle of $M \conv N$.
\end{enumerate}
\enth

We will use the following convention frequently.
\Def
For simple $R$-modules $M$ and $N$, we denote by  $M \hconv N$   the head of
$M \conv N$ and  by $M \sconv N$ the socle of $M \conv N$ .
\edf

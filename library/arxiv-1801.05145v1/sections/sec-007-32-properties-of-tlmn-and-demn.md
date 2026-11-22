---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-007-32-properties-of-tlmn-and-demn
section_title: "Properties of $\tL(M,N)$ and $\de(M,N)$"
section_number: 3.2
pages: 22-31
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.941
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
\Lemma \label{lem:even}
Let $M$ and $N$ be simple $R$-modules.
Then we have
\bnum
   \item $\Lambda(M,N)+\Lambda(N,M) \in 2 \Z_{\ge 0}.$
   \item If $\Lambda(M,N)+\Lambda(N,M) =2m$ for some $m \in \Z_{\ge 0}$, then
  \eqn
\Rm_{M_z,N} \circ \Rm_{N,M_z}=z^m \id_{N \conv M_z} \quad
\text{and} \quad
\Rm_{N,M_z} \circ \Rm_{M_z,N}=z^m \id_{M_z \conv N}
  \eneqn
  up to constant multiples.
\end{enumerate}
\enlemma
\Proof
By \cite[Proposition 1.6.2]{K^3}, the morphism
\eqn
\Rm_{N,M_z} \circ \Rm_{M_z,N} : M_z \circ N \to
M_z \circ N
\eneqn
is equal to $f(z) \id_{M_z \circ N}$ for some $0 \neq f(z) \in \cor[z]$.
Since $\Rm_{N,M_z} \circ \Rm_{M_z,N}$ is  homogeneous of degree $\Lambda(M,N)+\Lambda(N,M)$,
we have $f(z)=c z^{\frac{1}{2}(\Lambda(M,N)+\Lambda(N,M))}$ for some $c \in \cor^\times$.
\QED

\Def
For non-zero modules $M$ and $N$, we set
\eqn
\de(M,N) = \frac{1}{2}\bl\Lambda(M,N)+\Lambda(N,M)\br.
\eneqn
\edf
Note that if $M$ and $N$ are simple modules, then  we have
$\de(M,N) \in \Z_{\ge 0}$.
Note also that
if $M,N_1,N_2$ are simple modules, then we have
$\de(M,N_1 \conv N_2) =\de(M,N_1)+\de(M,N_2)$ by Lemma \ref{lem:composition} (ii).

\Lemma[\cite{KKKO14}] \label{lem:commute_equiv}
Let $M,N$ be simple modules and assume that one of them is real. Then the following conditions are equivalent.
\bnum
  \item $\de(M,N)=0$.
  \item $\rmat{M,N}$ and $\rmat{N,M}$ are inverse to each other up to a constant multiple.
  \item $M \conv N$ and $N \conv M$ are isomorphic up to a grading shift.
  \item $M \hconv N$ and $N \hconv M$ are isomorphic up to a grading shift.
  \item $M \conv N$ is simple.
\end{enumerate}
\enlemma
\Proof
By specializing the equations in Lemma \ref{lem:even} (ii) at $z=0$, we obtain that $\de(M,N)=0$ if and only if $\rmat{M,N} \circ \rmat{N,M} = \id_{N\conv M}$ and $\rmat{N,M} \circ \rmat{M,N} = \id_{M\conv N}$ up to non-zero constant multiples. Hence the conditions (i) and (ii) are equivalent.


The conditions  (ii), (iii), (iv), and (v) are equivalent by \cite[Theorem 3.2, Proposition 3.8, and Corollary 3.9]{KKKO14}.
\QED


\Def
Let $M,N$ be simple modules.
\bnum
  \item We say that $M$ and $N$ \emph{commute} if $\de(M,N)=0$.
  \item We say that $M$ and $N$  are \emph{simply-linked} if $\de(M,N)=1$.
\end{enumerate}
\edf

\Prop  \label{prop:real simple}
Let $M_1,\ldots, M_r$ be a commuting family of real simple modules.
Then the convolution product
\eqn
M_{1} \conv \cdots \conv M_{r}
\eneqn
is a real simple module.
\enprop
\Proof We shall first show the simplicity of the convolutions.
By induction on $r$, we may assume that $ M_{2} \conv \cdots \conv M_{r}$
is a simple module.
Then we have
\eqn
\de(M_{1}, M_{2} \conv \cdots \conv M_{r})

=\sum_{s=2}^r \de(M_{1},M_{s})=0
\eneqn
so that
$M_{1} \conv \cdots \conv M_{r}$ is simple by Lemma \ref{lem:commute_equiv}.

Since $(M_{1} \conv \cdots \conv M_{r}) \conv (M_{1} \conv \cdots \conv M_{r})$ is also simple,
$M_{1} \conv \cdots \conv M_{r}$ is real.
\QED



\begin{definition}
Let $M_1,\ldots,M_m$ be real
simple modules. Assume that they commute with each other. We set
\eqn
&&M_1\sodot M_2\seteq q^{\tLa(M_1,M_2)}M_1\conv M_2,\\
&&\sodot_{1 \le k \le m}M_k
\seteq(\cdots(M_1\sodot M_2)\cdots)\sodot M_{m-1})\sodot M_m\\
&&\hs{20ex}\simeq q^{\sum_{1 \le i <j\le m} \tLa(M_i,M_j)}M_1 \conv \cdots \conv M_m.
\eneqn
\end{definition}
It is invariant  under the permutations of $M_1,\ldots,M_m$.


\Lemma\label{lem:multipro}
Let $M_1,\ldots, M_m$ be real simple modules commuting with each other.
Then for any $\sigma\in\sym_m$, we have
$$\nconv_{1\le k\le m} M_k\simeq \nconv_{1\le k\le m} M_{\sigma(k)}\quad\text{in $R\gmod$.}$$
Moreover, if the $M_k$'s are self-dual,
then so is
$\nconv_{1\le k\le m} M_k$.
\enlemma
\Proof
It follows from Lemma~\ref{lem:selfdual} and
$q^{\tL(M_i,M_j)}M_i\conv M_j\simeq
q^{\tL(M_j,M_i)}M_j\conv M_i$.
\QED

\Prop \label{prop:inequalities}
Let $f:N_1 \to N_2$ be a morphism between non-zero
$R$-modules $N_1, N_2 $
and let $M$ be a non-zero $R$-module.
\bnum
\item
If $\Lambda(M,N_1)=\Lambda(M,N_2)$, then the following diagram is commutative:
  \eqn
  \xymatrix@C=5em{
  M\conv N_1 \ar[r]^{\rmat{M,N_1}} \ar[d]_{M \circ f} &
N_1 \conv M \ar[d]^{f \circ M} \\
  M\conv N_2 \ar[r]^{\rmat{M,N_2}}& 
N_2 \conv M.
  }\eneqn
\item If $\Lambda(M,N_1) < \Lambda(M,N_2)$, then the composition
  \eqn
  M \conv N_1 \To[M \circ f] M \conv N_2 \To[\rmat{M,N_2}] N_2 \conv M
  \eneqn
  vanishes.
 \item If $\Lambda(M,N_1) > \Lambda(M,N_2)$, then the composition
  \eqn
M \conv N_1 \To[\rmat{M,N_1}] N_1 \conv M \To[f \circ M] N_2 \conv M
  \eneqn
  vanishes.
 \item If $f$ is surjective, then we have
 \eqn
 \Lambda(M,N_1) \ge \Lambda(M,N_2) \quad \text{and} \quad
 \Lambda(N_1,M) \ge \Lambda(N_2,M)
 \eneqn
If $f$ is injective, then we have
\eqn
\Lambda(M,N_1) \le \Lambda(M,N_2) \quad \text{and}\quad
\Lambda(N_1,M) \le \Lambda(N_2,M)
\eneqn
\end{enumerate}

\enprop
\Proof

Let $s_i$  be the order of zero of $R_{M_z,N_i}$ for $i=1,2$.
Then we have  $\Lambda(M,N_1) - \Lambda(M,N_2)=2(s_2-s_1)$.

Set $m\seteq\min\{s_1,s_2\}$.
Then the following diagram is commutative:
  \eqn
  \xymatrix@C=10em{
  M_z\conv N_1 \ar[r]^{z^{-m}R_{M_z,N_1}} \ar[d]_{M_z \conv f} &  N_1 \conv M_z \ar[d]^{f \conv M_z} \\
  M_z\conv N_2 \ar[r]^{z^{-m}R_{M_z,N_2}}&  N_2 \conv M_z.
  }\eneqn


(i) If $s_1=s_2$, then by specializing $z=0$ in the above diagram,
we obtain the commutativity of the diagram in (i).

(ii) If $s_1 > s_2$, then we have
\eqn
z^{-m}R_{M_z,N_1}=z^{s_1-m} \bl z^{-s_1}R_{M_z,N_1}\br
\eneqn
so that $z^{-m}R_{M_z,N_1}|_{z=0}$ vanishes.
Hence
we have
\eqn
\rmat{M,N_2} \circ (M\conv f) = z^{-m}R_{M_z,N_2}|_{z=0} \circ (M\conv f) =0,
\eneqn
as desired. In particular, $f$ is not surjective.

(iii) Similarly, if $s_1 < s_2$, then we have
$
(f \conv M) \circ \rmat{M,N_1} =0,
$
and $f$ is not injective.

(iv) The statements for $\Lambda(M,N_1)$ and   $\Lambda(M, N_2)$ follow
from (ii) and (iii).
The other statements can be shown in a similar way.
\QED


\Prop\label{prop:rmat}
 Let $M$ and $N$ be simple modules.
We assume that one of them is real.
Then we have
$$\Hom_{R\smod}(M\conv N,N\conv M)=\cor\,\rmat{M,N}.$$

\enprop
\Proof
 Since the other case can be proved similarly, we assume that $M$ is real.
Let $f\cl M\conv N\to N\conv M$ be a morphism.
 Note that we have $\rmat{M,\,M\circ N}=M\conv \rmat{M,N}$ and $\rmat{M,\,N\circ M}=\rmat{M,N}\conv M$   by Lemma \ref{lem:composition} (ii) and by the fact that $\rmat{M,M}=\id_{M\conv M}$ up a constant multiple.
Thus, by Proposition \ref{prop:inequalities}, we have a commutative diagram (up to a constant multiple)
$$\xymatrix@C=10ex{
M\conv M\conv N\ar[r]^{M\circ \rmat{M,N}}\ar[d]_{M\circ f}
&M\conv N\conv M\ar[d]_{f\circ M}\\
M\conv N\conv M\ar[r]^{\rmat{M,N}\circ M}
&N\conv M\conv M
}$$
Hence we have
$$M\conv {\rm Im}(\rmat{M,N})\subset f^{-1}\bl {\rm Im}(\rmat{M,N})\br\conv M.$$
Hence there exists a submodule $K$ of $N$ such that
${\rm Im}(\rmat{M,N})\subset K\conv M$ and
$M\conv K\subset f^{-1}\bl{\rm Im}(\rmat{M,N})\br$ by Lemma \ref{lem:simplicity}.
Since $K\not=0$, we have $K=N$.
Hence
$f(M\conv N)\subset {\rm Im}(\rmat{M,N})$, which means that
$f$ factors as
$M\conv N\to \soc(N\conv M)\monoto N\conv M$.
It remains to remark that
$\Hom_{R\smod}\bl M\conv N,\soc(N\conv M)\br=\cor\,\rmat{M,N}$.
\QED


\Prop \label{pro:subquotient}
Let $L$, $M$ and $N$ be simple modules.
Then we have
\eq&&\ba{l}
\La(L,S)\le\La(L,M)+\La(L,N),\
\La(S,L)\le\La(M,L)+\La(N,L)\ \text{and}\\[1ex]
\de(S,L)\le\de(M,L)+\de(N,L)\ea\label{eq:LMN<}
\eneq
for any subquotient $S$ of $M\conv N$.
Moreover, when $L$ is real, the following conditions are equivalent.
\bni
\item $L$ commutes with $M$ and $N$.
\item Any simple subquotient $S$ of $M\conv N$ commutes with
$L$ and satisfies $\La(L,S)=\La(L,M)+\La(L,N)$.
\item Any simple subquotient $S$ of $M\conv N$ commutes with $L$ and satisfies
$\La(S,L)=\La(M,L)+\La(N,L)$.
\ee
\enprop
\Proof
The inequalities \eqref{eq:LMN<} are consequences of Proposition \ref{prop:inequalities}.
Let us show the equivalence
of (i)--(iii).

Let $M\conv N=K_0\supset K_1\supset \cdots\supset  K_\ell\supset K_{\ell+1}=0$ be a Jordan-H\"older series of $M\conv N$.
Then the renormalized R-matrix $\Rm_{L_z,M\circ N}=(M\conv\Rm_{L_z,N})\circ(\Rm_{L_z,M}\conv N)
\cl L_z\conv M\conv N\to M\conv N\conv L_z$
is homogeneous of degree $\La(L,M)+\La(L,N)$ and it sends $L_z\conv K_k$ to
$K_k\conv L_z$ for any $k\in\Z$. Hence
$f\seteq\rmat{L,M\circ N}=\Rm_{L_z,M\circ N}\vert_{z=0}$ sends
$L\conv K_k$ to $K_k\conv L$.

\medskip
\noi
First assume (i).
Then $f$ is an isomorphism.
Hence $f\vert_{L\circ K_k}\cl L\conv K_k\to K_k\conv L$ is injective.
By comparing their dimension, $f\vert_{L\circ K_k}$ is an isomorphism,
Hence $f\vert_{L\circ (K_k/K_{k+1})}$ is an isomorphism of homogeneous degree
$\La(L,M)+\La(L,N)$.
Hence we obtain (ii).

\medskip
\noi
Conversely, assume (ii).
Then,
$\Rm_{L_z,M\circ N}\vert_{L_z\conv (K_k/K_{k+1})}$ and $\Rm_{L_z,K_k/K_{k+1}}$
have the same homogeneous degree, and hence they should coincide.

It implies that $f\vert_{L\circ(K_k/K_{k+1})}=\rmat{L,K_k/K_{k+1}}$ is an isomorphism
for any $k$.
Therefore $f=(M\conv\rmat{L,N})\circ(\rmat{L,M}\conv N)$ is an isomorphism,
which implies that $\rmat{L,N}$ and $\rmat{L,M}$ are isomorphisms.
Thus we obtain (i).

\medskip
\noi
Similarly, (i) and (iii) are equivalent.
\QED

\Lemma \label{lem:LMN1}
Let $L$, $M$ and  $N$ be simple modules.
 We assume that $L$ is real and commutes with $M$.
Then the diagram
$$\xymatrix@C=10ex
{L\conv (M\conv N)\ar[r]^{\rmat{L,M\circ N}}\ar[d]
&(M\conv N)\conv L\ar[d]\\
L\conv (M\hconv N)\ar[r]^{\rmat{L,M\shconv N}}
&(M \hconv N)\conv L}
$$
commutes.
\enlemma
\Proof
Otherwise
the composition

$$
\xymatrix@C=8ex{
L\conv M\conv N\ar[r]^-\sim_-{\rmat{L,M}\circ N}
&M\conv L\conv N\ar[r]_-{M\circ\rmat{L,N}}&M\conv N\conv L
\ar[r]&
(M\hconv N)\conv L}
$$
vanishes by Proposition \ref{prop:inequalities}.
Hence we have
$$M\circ \Im(\rmat{L,N})\subset \Ker(M\conv N\to M\hconv N)\conv L.$$
Hence, by Lemma \ref{lem:simplicity}, there exists a submodule $K$ of $N$ such that
$$\text{$\Im(\rmat{L,N})\subset K\conv L$ and
$M\conv K\subset\Ker(M\conv N\to M\hconv N)$.}$$
The first inclusion implies $K\not=0$ and the second implies $K\not=N$,
which contradicts the simplicity of $N$.
\QED

The following lemma can be proved similarly.
\Lemma\label{lem:LMN2}
Let $L$, $M$ and  $N$ be simple modules.
We assume that $L$ is real and commutes with $N$.
Then the diagram
$$\xymatrix@C=10ex
{(M\conv N)\conv L\ar[r]^{\rmat{M\circ N,L}}\ar[d]
&L\conv(M\conv N)\ar[d]\\
(M\hconv N)\conv L\ar[r]^{\rmat{M\shconv N,L}}
&L\conv(M\hconv N)}
$$
 commutes. 
\enlemma

The following proposition follows from Lemma~\ref{lem:LMN1} and Lemma~\ref{lem:LMN2}.
\Prop \label{prop:Lambda decomp}
Let $L$, $M$ and  $N$ be simple modules. Assume that $L$ is real.
Then we have:
\bnum
\item
If $L$ and $M$ commute, then
$$\La(L,M\hconv N)=\La(L,M)+\La(L,N).$$

\item
If $L$ and $N$ commute, then
$$\La(M\hconv N,L)=\La(M,L)+\La(N,L).$$
\ee
\enprop






\Prop \label{prop:socNM}
Let $M$ be a real simple module and let $N$ be a module with a simple socle.
If the following diagram
$$\xymatrix@C=12ex
{\wb{\soc(N)\conv M}\ar[r]^{\rmat{\soc(N),M}}\ar@{>->}[d]
&\wb{M\conv\soc(N)}\ar@{>->}[d]\\
N\conv M\ar[r]^{\rmat{N,M}}&M\conv N
}
$$ commutes up to a non-zero constant multiple, then
$\soc\bl M\conv\soc(N)\br$ is
equal to the socle of $M\conv N$.
In particular, $M\conv N$ has a simple socle.
\enprop
\Proof
Let $S$ be an arbitrary simple submodule of $M\conv N$.
Then we have the following commutative diagram:
$$\xymatrix@C=12ex
{\wb{S\conv M_z}\ar[r]^{ R_{S\circ M_z} }  \ar@{>->}[d]
&\wb{M_z\conv S}\ar@{>->}[d]\\
M\conv N\conv M_z\ar[r]^{R_{M\circ N,M_z}}
&M\conv M\conv N.
}$$
 By multiplying $z^{-m}$, where  $m$ be the order of zero of $R_{M\conv N, M}$,  and
specializing at $z=0$,
we have a commutative diagram  (up to a constant multiple):
$$\xymatrix@C=12ex
{\wb{S\conv M}\ar[r] \ar@{>->}[d]
&\wb{M\conv S}\ar@{>->}[d]\\
M\conv N\conv M\ar[r]^{M\circ\rmat{N,M}}&M\conv M\conv N.
}$$


 Here, we use the fact that
$\rmat{M\conv N, M} = (\rmat{M,M} \conv N) \circ (M\conv \rmat{N,M})$ from Lemma \ref{lem:composition} and the fact that
$\rmat{M,M}$
is equal to $\id_{M\conv M}$ up to a non-zero constant multiple, because $M$ is a real simple module.

It follows that  $S\conv M\subset M\conv (\rmat{N,M})^{-1}(S)$.
Hence there exists a submodule $K$ of $N$ such that
$S\subset M\conv K$ and $K\conv M\subset (\rmat{N,M})^{-1}(S)$
by Lemma \ref{lem:simplicity}.
Hence $K\not=0$ and $\soc(N)\subset K$ by the assumption.
Hence $\rmat{N,M}\bl\soc(N)\conv M\br
\subset \rmat{N,M}\bl K\conv M\br\subset S$.
Since $\rmat{N,M}\bl\soc(N)\conv M\br$ is non-zero by the assumption, we have
$\rmat{N,M}\bl\soc(N)\conv M\br=S$.
Thus we obtain the desired result.
\QED


The following is a dual form of the preceding proposition.
\Prop\label{prop:hdMN}
Let $M$ be a real simple module.
Let $N$ be a module with a simple head.
If the following diagram
$$\xymatrix@C=12ex
{{M\conv N}\ar[r]^{\rmat{M,N}}\ar@{->>}[d]
&{N\conv M}\ar@{->>}[d]\\
M\conv \hd(N)\ar[r]^{\rmat{M,\hd(N)}}&\hd(N)\conv M
}
$$ commutes up to a non-zero constant multiple, then
$M\hconv \hd(N)$ is
equal to the simple head of $M\conv N$.
\enprop

\begin{prop} \label{prop:3simple}
Let $L$, $M$ and  $N$ be simple modules.
We assume that $L$ is real and
one of $M$ and $N$ is real.
\begin{enumerate}
\item[{\rm (i)}]
If $\La(L,M\hconv N)=\La(L,M)+\La(L,N)$,
then
$L\conv M\conv N$ has a simple head and
$N\conv M\conv L$ has a simple socle.
\item[{\rm (ii)}]
If $\La(M\hconv N,L)=\La(M,L)+\La(N,L)$,
then
$M\conv N\conv L$ has a simple head and
$L\conv N\conv M$ has a simple socle.
\item[{\rm (iii)}]
If $\de(L,M\hconv N)=\de(L,M)+\de(L,N)$,
then
$L\conv M\conv N$ and $M\conv N\conv L$  have  simple heads, and
$N\conv M\conv L$ and $L\conv N\conv M$ have  simple socles.
\end{enumerate}
\end{prop}

\begin{proof}
(i)\ Denote $k=\La(L,M\hconv N)=\La(L,M)+\La(M,N)$ and $m=\La( M,N)$. Then the diagram
$$\xymatrix@C=12ex@R=3ex
{{L\conv M\conv N}\ar[r]^{\rmat{L,M\circ N}}\ar@{->>}[d]
& q^{-k}{M\conv N\conv L}\ar@{->>}[d]
\\
\wb{L\conv (M\hconv N)}\ar[r]^{\rmat{L,M\shconv N}}\ar@{>->}[d]
&\wb{q^{-k}(M\hconv N)\conv L}\ar@{>->}[d]\\
q^{-m}L\conv N\conv M\ar[r]^{\rmat{L,N\circ M}}&q^{-k-m} N\conv M\conv L
}
$$
commutes. Hence
 Proposition \ref{prop:socNM} and Proposition \ref{prop:hdMN}  imply that $L\conv M\conv N$ has a simple head and $N\conv M\conv L$ has a simple socle.
(ii) are proved similarly.

\medskip\noindent
(iii)\ If $\de(L,M\hconv N)=\de(L,M)+\de(L,N)$,
then we have $\La(L,M\hconv N)=\La(L,M)+\La(L,N)$
and $\La(M\hconv N,L)=\La(M,L)+\La(N,L)$ by Proposition \ref{prop:inequalities}. Thus
 the statements in (iii) follow from (i) and (ii).
\end{proof}


\Prop\label{Prop: l2}
Let $M$ and $N$ be simple modules.
Assume that one of them is real and $\de(M,N)=1$.
Then we have an exact sequence
\eqn
&&0\to  M\sconv N \to M\conv N\to M\hconv N\to 0.
\eneqn
In particular, $M\conv N$ has length $2$.
\enprop
\Proof In the course of the proof, we ignore the grading.

Set $X=M_z\circ N$
and $Y=N\circ M_z$.
By $\Rm_{N,M_z}\cl Y\monoto X$ let us regard $Y$ as a submodule of $X$.
By the condition, we have
$\Rm_{N,M_z}\circ \Rm_{M_z,N}=z\id_X$ up to a constant multiple (see Lemma \ref{lem:even} (ii)),
and hence we have
$$zX\subset Y\subset X.$$

We have an exact sequence
$$ 0\To \dfrac{Y}{zX}\To\dfrac{X}{zX}\To\dfrac{X}{Y}\To0.$$
Since
$$M\conv N\simeq\dfrac{X}{zX}\epito \dfrac{X}{Y}\monoto \dfrac{z^{-1}Y}{Y}
\simeq N\conv M,$$
we have $\dfrac{X}{Y}\simeq M\hconv N$ by Proposition \ref{prop:rmat}.
Similarly,
$$N\conv M\simeq\dfrac{Y}{zY}\epito \dfrac{Y}{zX}\monoto \dfrac{X}{zX}
\simeq M\conv N$$
implies that
$\dfrac{Y}{zX}\simeq  M\sconv N $ by Proposition \ref{prop:rmat}.
\QED


\Lemma \label{lem:crde}
Let $M$ and $N$ be simple  modules.
Assume that one of them is real.
If there is an exact sequence
$$0\to q^mX\To M\circ N\To q^n Y\To 0$$
for self-dual simple modules $X$, $Y$ and
integers $m$, $n$, then we have
$$\de(M,N)=m-n.$$
\enlemma
\Proof
We may assume that $M$ and $N$ are self-dual without loss of generality.
Then we have
$n=-\tLa(M,N)$.
Since $q^mX\simeq q^{\La(N,M)}N\hconv M
\simeq q^{\La(N,M)-\tL(N,M)}\bl q^{\tL(N,M)}N\hconv M\br$, we have
$m=\La(N,M)-\tL(N,M)$.
Thus we obtain
$$m-n=\La(N,M)-\tL(N,M)+\tLa(M,N)=\de(M,N).$$
\QED


\Lemma\label{lem:short}
Let $M$ and $N$ be simple modules.
Assume that one of them is real.
If the equation
$$[M][N]=q^m[X]+q^n[Y]$$
holds in $K(R\gmod)$ for self-dual simple modules $X$, $Y$ and
integers $m$, $n$ such that $m\ge n$,
then we have
\bnum
\item $\de(M,N)=m-n>0$,
\item there exists an exact sequence
$$0\To q^mX\To M\conv N\To q^nY\To0,$$
\item
 $ q^mX$ is  the  socle of $M\conv N$ and $q^nY$ is
 the
head of
$M\conv N$.
\ee
\enlemma
\Proof
First note that $\de(M,N)>0$ since $M\conv N$ is not simple.
By the assumption,
there exists either an exact sequence
$$0\To q^mX\To M\conv N\To q^nY\To0,$$
or
$$0\To q^nY\To M\conv N\To q^mX\To0.$$
The  second sequence cannot exist by Lemma \ref{lem:crde}
because $\de(M,N)=n-m\le0$.
Hence the first sequence exists, and the assertion  (iii) follows from
 Theorem \ref{thm:simplicity}.
\QED





\Prop \label{prop:real}
Let $X,Y,M$ and $N$ be simple $R$-modules.
Assume that there is  an exact sequence
\eqn
0 \to X \to M \conv N \to Y \to 0,
\eneqn
$X \conv N$ and $Y \conv N$ are simple and $X \conv N \not\simeq Y \conv N$
as ungraded modules.
Then $N$ is a real simple module.
\enprop
\Proof
Assume that $N$ is not real.
Then $N \conv N$ is reducible and we have $\rmat{N,N} \neq c \id_{N \conv N}$ for any $c \in \cor$ by \cite[Corollary 3.3]{KKKO14}.
Note that $N \conv N$
is of length $2$, because $M\conv N \conv N$ is of length $2$.

Let $S$ be a simple  submodule of $N \conv N$.
Consider an exact sequence
$$0\To X\conv N\To M\conv N\conv N\To Y\conv N\To0.$$
Then we have
\eq (X \conv N) \cap (M\conv S) =0.
\label{eq:SN}
\eneq
Indeed, if $(X\conv N) \subset (M \conv S)$, then there exists a submodule $Z$ of $N$ such that
$X \subset M \conv Z$ and $Z \conv N \subset S$ by \cite[Lemma 3.1]{KKKO14}.
It contradicts the simplicity of $N$.
Thus \eqref{eq:SN} holds.

Note that \eqref{eq:SN} implies
$$M\conv S\simeq Y\conv N$$
since $Y \conv N$ is simple.

\medskip\noi
(a)\ Assume first
that $N \conv N$ is semisimple so that $N \conv N=S \oplus S'$ for some simple submodule
 $S'$ of $N \conv N$.
 Then
$M\conv S\simeq Y\conv N\simeq M\conv S'$.
Hence $M\conv S\simeq X\conv N\simeq M\conv S'$.
Therefore we obtain $X \conv N \simeq Y \conv N,$ which is a contradiction.

\medskip\noi
(b)\   Assume that $N \conv N$ is not semisimple so that $S$ is a unique non-zero proper submodule of
  $N \conv N$ and $(N \conv N) / S$ is a unique non-zero proper quotient of $N \conv N$.
  Without loss of generality, we may assume that $\cor$ is algebraically closed (\cite[Corollay 3.19]{KL09}).
  Let $x \in \cor$ be an eigenvalue of $\rmat{N,N}$.
 Since $\rmat{N,N} \not\in\cor\id_{N \conv N}$, we have
 $0  \subsetneq \Im(\rmat{N,N}-x \id_{N\conv N}) \subsetneq N\conv N$.
It follows that
\eqn
S = \Im(\rmat{N,N}-x \id_{N\conv N}) \simeq (N \conv N) /S,
\eneqn
and  hence we have an exact sequence
\eqn
0 \To M\conv S \To M \conv N \conv N \To M \conv \bl(N \conv N) /S\br  \To 0.
\eneqn
Since $M \conv N \conv N $ is of length $2$, we have
\eqn
X \conv N \simeq M \conv S \simeq M\conv\bl(N \conv N) /S\br\simeq  Y \conv N,
\eneqn
 which is a contradiction.
 \QED

 \Cor \label{cor:real}
Let $X,Y,N$ be simple $R$-modules and let $M$ be a real simple  $R$-module.
 If we have an exact sequence
\eqn
0 \to X \to M \conv N \to Y \to 0
\eneqn
and if $X \conv N$ and $Y \conv N$ are simple,
then $N$ is a real simple module.
\encor
\Proof
Since $M$ is real and $M \conv N$ is not simple, $X$ is not isomorphic to $Y$
as an ungraded module by Lemma \ref{lem:commute_equiv} (iv).
It follows that $X \conv N$ is not isomorphic to $Y \conv N$,
because $K(R\gmod)$ is a domain so that
$[X\conv N]=q^m [Y \conv N]$ for some $m \in \Z$ implies $[X]=q^m [Y]$.
Now the assertion follows from Proposition \ref{prop:real}.
\QED


\Lemma\label{lem:MN}
Let $\{M_i\}_{1\le i\le n}$ and $\{N_i\}_{1\le i\le n}$ be a pair of
commuting families of real simple modules.
We assume that
\bnam
 \item $\{M_i\hconv N_i\}_{1\le i\le n}$ is a commuting family of real simple
modules,
\item $M_i\hconv N_i$ commutes with $N_{j}$
for any $1\le i,j\le n$.
\ee

Then we have
$$(\conv_{1\le i\le n}M_i)\hconv (\conv_{1\le j\le n}N_j)
\simeq \conv_{1\le i\le n}(M_i\hconv N_i)\quad
\text{up to a grading shift.}
$$
\enlemma
\Proof
 Since $\conv_{1\le i\le n}(M_i\hconv N_i)$ is simple, it is enough to give
an epimorphism $(\conv_{1\le i\le n}M_i)\conv (\conv_{1\le j\le n}N_j)
\epito \conv_{1\le i\le n}(M_i\hconv N_i)$.
We shall show it by induction on $n$.
For $n>0$, we have
\eqn
&&(\conv_{1\le i\le n}M_i)\conv (\conv_{1\le j\le n}N_j)\simeq
(\conv_{1\le i\le n-1}M_i)\conv M_n\conv N_n\conv (\conv_{1\le j\le n-1}N_j)\\
&&\epito (\conv_{1\le i\le n-1}M_i)\conv (M_n\hconv N_n) \conv (\conv_{1\le j\le n-1}N_j) \\
&&\simeq (\conv_{1\le i\le n-1}M_i)\conv (\conv_{1\le j\le n-1}N_j) \conv  (M_n\hconv N_n)  \\
&&\epito (\conv_{1\le i\le n-1}(M_i \hconv N_i)) \conv  (M_n\hconv N_n),
\eneqn
as desired.
\QED

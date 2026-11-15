---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-017-52-twisted-alexander-polynomials-and-knot-concor
section_title: "Twisted Alexander polynomials and knot concordance"
section_number: 5.2
pages: 14-16
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.981
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:slice}

The first significant result in the study of slice knots is due to
Fox and Milnor \cite{FM66} who showed that if $K$ is a slice knot, then $\Delta_K \doteq f(t)f(t^{-1})$ for some $f(t)\in \mathbb{Z}[t^{\pm 1}]$.

In this section we will give an exposition and a slight generalization of the Kirk--Livingston \cite{KL99a} sliceness obstruction theorem, which generalizes the Fox--Milnor condition. Note that we will state this obstruction using a slightly different setup, but Theorem \ref{thm:slice} is
already contained in \cite{KL99a} and \cite{HKL08}.

Let $K$ be a knot, as above we  denote by $N_K$ the zero--framed surgery of $S^3$ along $K$.
Now suppose that $K$ has a  slice disk $D$. Note that $\partial (D^4\setminus \nu D)=N_K$.

Let $R$ be a ring with (possibly trivial) involution and as usual we extend the involution to $R[t^{\pm 1}]$ by $\overline{t}\mathrel{\mathop:}=t^{-1}$.
Let  $\alpha:\pi_1(N_K)\to \mbox{GL}(R[t^{\pm 1}],k)$ be a unitary  representation.
Assume that $\alpha$ has  the following two properties:
\begin{enumerate}
\item $\alpha$ factors through a representation $\pi_1(D^4\setminus \nu D)\to \mbox{GL}(k,R[t^{\pm 1}])$, and
\item the induced twisted modules $H_*(D^4\setminus \nu D;R[t^{\pm 1}]^k)$ are $R[t^{\pm 1}]$--torsion,
\end{enumerate}
then  using Poincar\'e duality for Reidemeister torsion (cf. \cite[Theorem~6.1]{KL99a}) one can show that  $\tau(N_K,\alpha)\doteq f(t)\overline{f(t)}$ for some $f(t)\in R(t)$. We refer to \cite[Corollary~5.3]{KL99a} for details.

\begin{remark}
Note that the canonical representation $\pi_1(N_K)\to \mbox{GL}(1,\mathbb{Z}[t^{\pm 1}])$ extends over any slice disk complement.
It can be shown that  $H_*(D^4\setminus \nu D;\mathbb{Z}[t^{\pm 1}])$ is $\mathbb{Z}[t^{\pm 1}]$--torsion. We can therefore recover the Fox--Milnor theorem from this discussion.
\end{remark}

Most of the ideas and techniques of finding  representations satisfying (1) and (2) go back to the seminal work of Casson and Gordon \cite{CG86}.
We follow the approach taken in \cite{Fr04} which is inspired by Letsche \cite{Let00} and Kirk--Livingston \cite{KL99a,HKL08}.


In the following let $K$ again be a knot in $S^3$.
We denote by $W_k$ the  cyclic $k$--fold branched cover of $K$.
Note that $H_1(W_k;\mathbb{Z})$ has a natural $\mathbb{Z}/k$--action, and we can therefore view $H_1(W_k;\mathbb{Z})$ as a $\mathbb{Z}[\mathbb{Z}/k]$--module.
If $H_1(W_k;\mathbb{Z})$ is finite, then there exists  a non--singular linking form
\[\lambda_k:H_1(W_k;\mathbb{Z})\times H_1(W_k;\mathbb{Z})\to \mathbb{Q}/\mathbb{Z}\]
with respect to which $\mathbb{Z}/k$ acts via isometries. We say that $M\subset H_1(W_k;\mathbb{Z})$ is a \emph{metabolizer} of the linking form
if $M$ is a $\mathbb{Z}[\mathbb{Z}/k]$--submodule of $H_1(W_k;\mathbb{Z})$ such that $\lambda_k(M,M)=0$ and such that $|M|^2=|H_1(W_k;\mathbb{Z})|$.
It is well--known that if $K$ is slice, then $\lambda_k$ has a metabolizer for any prime power $k$. We refer to \cite{Go78} for details.


Note that $H^1(N_K;\mathbb{Z})=\mathbb{Z}$, in particular $H^1(N_K;\mathbb{Z})$ has a unique generator (up to sign) which we denote by $\phi$.
We now consider the Alexander module  $H_1(N_K;\mathbb{Z}[t^{\pm 1}])$ which we denote by $H$.
Note that $H$ is isomorphic to the usual Alexander module of $K$.
It is well--known that given $k$ there exists a canonical isomorphism
$H/(t^k-1)\to H_1(W_k;\mathbb{Z})$ (cf. e.g. \cite[Corollary~2.4]{Fr04} for details).
Now let $\mu \in \pi_1(N_K)$ be an element  with $\phi(\mu)=1$.
Note that for any $g\in \pi$ we have $\phi(\mu^{-\phi(g)}g)=0$, in particular we can consider its image $[\mu^{-\phi(g)}g]$ in the abelianization $H_1(\ker(\phi))$, which we can identify with $H$.
Then we have a well--defined map
\[ \pi \to \mathbb{Z} \ltimes H \to \mathbb{Z} \ltimes H/(t^k-1) \]
where the first map is given by sending $g\in \pi$ to $(\phi(g),[\mu^{-\phi(g)}g])$. Here $n\in \mathbb{Z}$ acts on $H$ and on $H/(t^k-1)$ via multiplication by $t^n$.
We refer to \cite{Fr04} and \cite{BF08} for details.

Fix $k \in \mathbb{N}$.
Let  $\chi:H_1(W_k;\mathbb{Z})\to \mathbb{Z}/q\to S^1$ be a character. We denote the induced character $H\to H/(t^k-1)=H_1(W_k;\mathbb{Z})\to S^1$ by $\chi$ as well.
Let $\zeta_q$ be a primitive $q$--th root of unity.
Then it is straightforward  to verify that
 $$ \begin{array}{rcl} \alpha(k,\chi) :\pi \to  \mathbb{Z}\ltimes H/(t^{k}-1)& \to &\mbox{GL}(k,\mathbb{Z}[\zeta_q][t^{\pm 1}]) \\
    (j,h) &\mapsto &
\begin{pmatrix}
 0& \dots &0&t \\
 1&0& \dots &0 \\
\vdots &\ddots &  & \vdots\\
    0&\dots &1&0 \end{pmatrix}^j
\begin{pmatrix}
\chi(h) &0& \dots&0 \\
 0&\chi(th) & \dots& 0\\
\vdots&&\ddots & \vdots\\ 0&0&\dots &\chi(t^{k-1}h) \end{pmatrix} \end{array} $$
defines a unitary representation.
(Note the ``$t$'' in the upper right corner.)
Also note that $\alpha(k,\chi)$ is not a tensor representation (cf. \cite{HKL08}).

We can now formulate the following obstruction theorem which is well--known to the experts. It can be proved using the above discussion,
Proposition \ref{prop:deltataualpha}, various
well--known arguments going back to Casson and Gordon \cite{CG86} and \cite[Lemma~6.4]{KL99a}.

We also refer to Letsche \cite{Let00} and \cite{Fr04}  for more information.


\begin{theorem} \label{thm:slice}
Let $K$ be a slice knot. Then for any prime power $k$ there exists a metabolizer $M$ of $\lambda_k$
such that for any odd prime power $n$ and any  character $\chi:H_1(W_k;\mathbb{Z})\to \mathbb{Z}/n\to S^1$ vanishing on $M$ we have
\[ \Delta_{N_K}^{\alpha(k,\chi)}\doteq f(t)\overline{f(t)} \]
for some $f(t)\in Q(\mathbb{Z}[\zeta_n])[t^{\pm 1}]=\mathbb{Q}(\zeta_n)[t^{\pm 1}]$.
\end{theorem}


Note that  the original sliceness obstruction of Kirk and Livingston \cite[Theorem~6.2]{KL99a} (cf. also \cite[Theorem~8.1]{HKL08} and \cite[Theorem~5.4]{Liv09}) gives an obstruction in terms of twisted Alexander polynomials of
a cyclic cover of $S^3\setminus \nu K$ corresponding to one--dimensional representations. Using
Theorem \ref{thm:shapiro} and Lemma \ref{lem:zerosurgery} (cf. also \cite[Lemma~6.3]{KL99a}) one can show that the sliceness obstruction of Theorem \ref{thm:slice}
is equivalent to the original formulation by Kirk and Livingston.

\begin{remark}
In Theorem \ref{thm:slice} and later in Theorems \ref{thm:slicetensor} and \ref{thm:doublyslice} we restrict ourselves to characters of odd prime power.
Similar theorems also hold for characters of even prime power order, we refer to \cite[Lemma~6.4]{KL99a} and \cite[Section~5]{Liv09} for more information.
\end{remark}

Theorem \ref{thm:slice} can be somewhat generalized using tensor representations.
In the following let $k_1,\dots,k_n \in \mathbb{N}$. Assume we are given  characters $\chi_i:H_1(W_{k_i};\mathbb{Z})\to \mathbb{Z}/q\to S^1, i=1,\dots,n$
we also get a tensor representation
\[ \alpha(k_1,\chi_1)\otimes \dots \otimes \alpha(k_n,\chi_n)\to \mbox{GL}(k_1\cdot\dots \cdot k_n,\mathbb{Z}[\zeta_q][t^{\pm 1}]).\]
We refer to \cite[Proposition~4.6]{Fr04} for more information.

The following theorem can be proved by modifying the proof of Theorem \ref{thm:slice} along the lines of
\cite[Theorem~4.7]{Fr04}.


\begin{theorem} \label{thm:slicetensor}
Let $K$ be a slice knot. Let $q$ be an odd prime power and let $k_1,\dots,k_n$ be coprime prime powers.
Then there exist metabolizers $M_1,\dots,M_n$ of the linking forms $\lambda_{k_1},\dots,\lambda_{k_n}$
such that for any choice of  characters $\chi_i:H_1(W_{k_i};\mathbb{Z})\to \mathbb{Z}/q\to S^1,i=1,\dots,n$  vanishing on $M_i$ we have
\[ \Delta_{N_K}^{\alpha(k_1,\chi_1)\otimes \dots \otimes \alpha(k_n,\chi_n)}\doteq f(t)\overline{f(t)} \]
for some $f(t)\in Q(\mathbb{Z}[\zeta_q])[t^{\pm 1}]=\mathbb{Q}(\zeta_q)[t^{\pm 1}]$.
\end{theorem}

\begin{remark}
 It was first observed by Letsche \cite{Let00} that non--prime power dimensional representations can give rise to sliceness obstructions. It is shown in \cite{Fr03}
that Letsche's non--prime power representations are given by the tensor representations considered in Theorem \ref{thm:slicetensor}.
\end{remark}

The sliceness obstruction coming from twisted Alexander polynomials is in some sense less powerful than
the invariants of Casson and Gordon \cite{CG86} (cf. \cite[Section~6]{KL99a} for a careful discussion) and Cochran--Orr--Teichner \cite{COT03}.
But to date  twisted Alexander polynomials give the strongest sliceness obstruction for algebraically slice knots
that can be computed efficiently.
The Kirk--Livingston sliceness obstruction theorem  has been used by various authors to produce many interesting examples,
some of which we list below:
\begin{enumerate}
\item Kirk and Livingston \cite{KL99b} apply twisted Alexander polynomials to show that
some knots (e.g. $8_{17}$) are not concordant to their inverses. This shows in particular that
knots are not necessarily concordant to their mutants. In \cite{KL99b} it is also shown that in general a knot
is not even concordant to a positive mutant.
\item Tamulis \cite{Tam02} considered knots with at most ten crossings which have algebraic concordance order two.
Tamulis used twisted Alexander polynomials to show that all but one of these knots do not have order two in the knot concordance group.
\item
In \cite{HKL08} Herald, Kirk and Livingston consider all knots with up to twelve crossings.
Eighteen of these knots are algebraically slice but can not be shown to be slice using elementary methods.
In \cite{HKL08} twisted Alexander polynomials are used to show that sixteen of these knots are in fact not slice
and one knot is smoothly slice. Therefore among the knots with up to twelve crossings only the sliceness status of the knot $12_{a631}$ is unknown.
\item The concordance genus $g_c(K)$ of a knot $K$ is defined to be the minimal genus among all knots
concordant to $K$. Livingston \cite{Liv09} uses twisted Alexander polynomials to show that
the concordance genus of $10_{82}$ equals three, which is its ordinary genus.
\end{enumerate}

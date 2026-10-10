---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-015-52-twisted-alexander-polynomials-and-knot-concor
section_title: "Twisted Alexander polynomials and knot concordance"
section_number: 5.2
pages: 14-16
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
text_source: latex
latex_prose_ratio: 0.676
latex_coverage_ratio: 0.982
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexand er polynomials of a 3–manifold associated to a representation of its fundam ental group."
---
\label{section:conc}

We first recall the relevant definitions.
Let $L=L_1\cup \dots \cup L_m\subset S^3$ be an oriented $m$--component link.
We say that $L$ is (topologically) \emph{slice} if the components bound $m$ disjointly embedded locally flat disks in $D^4$.
Given two ordered oriented $m$--component links $K=K_1\cup \dots \cup K_m\subset S^3$ and $L=L_1\cup \dots \cup L_m\subset S^3$
we say that $K$ and $L$ are \emph{concordant} if there exist $m$ disjointly embedded locally flat cylinders $C_1,\dots,C_m$ in $S^3\times [0,1]$
such that $\partial C_i=K_i\times 0\, \cup \, -L_i\times 1$. (Given an oriented knot $K\subset S^3$ we write $-K=\overline{K}^*$, i.e. $-K$ is  the knot obtained from the mirror image of $K$ by reversing the orientation.) Note that two knots $K_1$ and $K_2$ are concordant
if and only if $K_1\# -K_2$ is slice, and a link is slice if and only if it is concordant to the unlink.



\subsection{Twisted Alexander polynomials of zero--surgeries}\label{section:zerosurgery}

Given a knot $K\subset S^3$ the zero--framed surgery $N_K$ of $S^3$ along $K$ is defined to be
\[ N_K =S^3\setminus \nu K \cup_{T} S^1\times D^2\]
where $T=\partial (S^3\setminus \nu K)$ and $T$ is glued to $S^1\times D^2$ by gluing the meridian to $S^1\times \mbox{pt}$.
The inclusion map induces an isomorphism $\mathbb{Z}\cong H_1(S^3\setminus \nu K;\mathbb{Z})\xrightarrow{\cong} H_1(N_K;\mathbb{Z})$.
It is well--known that understanding the zero--framed surgery $N_K$
is the key to determining whether $K$ is slice or not
(cf. e.g. \cite{COT03}, \cite[Proposition~3.1]{FT05}, \cite[Proposition~2.1]{CFT09}).
We therefore prefer to formulate the sliceness obstructions in terms of the twisted Alexander polynomials of the zero--framed surgery.
The following lemma, together with Proposition \ref{prop:taudelta}, relates the twisted invariants of the zero--framed surgery with the twisted invariants of the knot complement.
We refer to \cite[Lemma~6.3]{KL99a} and \cite[Section~VII]{Tu02a} for very similar statements.


\begin{lemma}\label{lem:zerosurgery}
Let $K \subset S^3$ be a knot. Denote its meridian by $\mu$.
Let  $\alpha:\pi_1(N_K)\to \mbox{GL}(k,R[t^{\pm 1}])$ be a representation
such that $\det(\alpha(\mu)-\mbox{id})\ne 0$.
We denote the inclusion induced representation $\alpha:\pi_1(S^3\setminus \nu K)\to \pi_1(N_K)\to \mbox{GL}(k,R[t^{\pm 1}])$ by $\alpha$ as well.
Then
\[ \tau(S^3\setminus \nu K,\alpha)=\tau(N_K,\alpha) \cdot \det(\alpha(\mu)-\mbox{id}).\]
\end{lemma}

\begin{proof}
The proof of the lemma is standard and well--known. We therefore give just a quick summary.
Consider the decomposition $ N_K = S^3\setminus \nu K \cup_{T} S$ as above, where $S = S^1 \times D^2$.


Using the Mayer--Vietoris theorem for torsion we obtain that
\[ \tau(N_K,\alpha) =\frac{\tau(S^3\setminus \nu K,\alpha)\cdot \tau(S,\alpha)} { \tau( T,\alpha)}.\]
It is well--known that the torsion of the torus is trivial (c.f. e.g \cite{KL99a})
and that the torsion of $S$ is given by
\[ \tau(S,\alpha) = \frac{1}{ \det(\alpha(\mu)-\mbox{id})}.\]
The lemma now follows immediately.
\end{proof}


























\subsection{Twisted Alexander polynomials and knot concordance}\label{section:slice}

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





\subsection{Ribbon knots  and doubly slice knots}\label{section:ds}


A knot $K$ is called \emph{homotopy ribbon} if there exists a slice disk $D$ such that
$\pi_1(N_K)\to \pi_1(D^4\setminus \nu D)$ is surjective. Note that if a knot is ribbon, then it is also homotopy ribbon.
It is an open conjecture whether every knot that is slice is also homotopy ribbon.

Let $K\subset S^3$ be a knot. Recall that there exists a non--singular hermitian pairing
\[ \lambda:H_1(N_K;\mathbb{Z}[t^{\pm 1}])\times H_1(N_K;\mathbb{Z}[t^{\pm 1}])\to \mathbb{Q}(t)/\mathbb{Z}[t^{\pm 1}] \] which is referred to as the \emph{Blanchfield pairing}.
We say that $M\subset H_1(N_K;\mathbb{Z}[t^{\pm 1}])$ is a \mbox{metabolizer} for the Blanchfield pairing if $M=M^{\perp}$, i.e. if $M$ satisfies
\[ M=\{ x\in H_1(N_K;\mathbb{Z}[t^{\pm 1}]) \, |\, \lambda(x,y)=0 \in \mathbb{Q}(t)/\mathbb{Z}[t^{\pm 1}] \mbox{ for all }y\in M\}.\]
If $K$ is slice, then there exists a metabolizer for the Blanchfield pairing.
Also recall from the previous section that for any $k$ there exists a canonical isomorphism $H_1(N_K;\mathbb{Z}[t^{\pm 1}])/(t^k-1)=H_1(L_k;\mathbb{Z})$.
If $M$ is a metabolizer for the Blanchfield pairing, then for any $k$ we have that $M/(t^k-1)\subset H_1(N_K;\mathbb{Z}[t^{\pm 1}])/(t^k-1)=H_1(L_k;\mathbb{Z})$
is a metabolizer for the linking form $\lambda_k$.
We refer to \cite{Bl57}, \cite{Ke75}, \cite[Section~7]{Go78}, \cite{Let00} and \cite[Section~2.3]{Fr04} for more information.


The proof of Theorem \ref{thm:slice}  can now be modified along well established lines (cf. e.g. \cite[Theorem~8.3]{Fr04}) to prove the following theorem:

\begin{theorem}\label{thm:ribbon}
Let $K\subset S^3$ be a ribbon knot, then there exists a metabolizer $M\subset H_1(N_K;\mathbb{Z}[t^{\pm 1}])$ for the Blanchfield pairing $\lambda$
such that for any $k$ and any non--trivial character $\chi:H_1(L_{k};\mathbb{Z})\to S^1$ of prime power vanishing on $M/(t^k-1)$ we have
\[ \Delta_{N_K}^{\alpha(k,\chi)}\doteq f(t)\overline{f(t)} \]
for some $f(t)\in Q(\mathbb{Z}[\zeta_q])[t^{\pm 1}]=\mathbb{Q}(\zeta_q)[t^{\pm 1}]$.
\end{theorem}

Using \cite[Proposition~4.6]{Fr04}  one can show that if a knot $K$ satisfies the ribbon obstruction of Theorem \ref{thm:ribbon}, then it also satisfies the
sliceness obstruction given by Theorem \ref{thm:slicetensor}.


A knot $K\subset S^3$ is called \emph{doubly slice} if there exists an unknotted locally flat
two--sphere $S
\subset S^4$ such that
$S\cap S^3=K$.
Note that a doubly slice knot is in particular slice.






The ordinary Alexander polynomial does not contain enough information to distinguish between slice and doubly slice knots.
On the other hand twisted Alexander polynomials can detect the difference.
The following theorem is well--known to the experts. It can be proved using the above ideas
of Kirk and Livingston combined with the results of Gilmer and Livingston \cite{GL83} (cf. also \cite[Section~8.2]{Fr04}).
Note that many of the ideas already go back to the original paper by Sumners \cite{Sum71}.

\begin{theorem} \label{thm:doublyslice}
Let $K$ be a doubly slice knot. Then for any prime power $k$ there exist
two metabolizers $M_1$ and $M_2$ of $\lambda_k$ with $M_1\cap M_2=\{0\}$
such that for any odd prime power $n$ and any  character $\chi:H_1(L_k;\mathbb{Z})\to \mathbb{Z}/n\to S^1$ which vanishes either on $M_1$ or on $M_2$
we have
\[ \Delta_{N_K}^{\alpha(k,\chi)}\doteq f(t)\overline{f(t)} \]
for some $f(t)\in Q(\mathbb{Z}[\zeta_n])[t^{\pm 1}]$.
\end{theorem}

It is also possible to state and prove an analogue of Theorem \ref{thm:slicetensor} for doubly slice knots.







\subsection{Twisted invariants and slice links}\label{section:slicelinks} \label{section:linkslice}


Kawauchi \cite[Theorems~A~and~B]{Ka78} showed that if $L$ is a slice link with more than one component, then the ordinary Alexander module  is necessarily non--torsion,
in particular the corresponding Reidemeister torsion is zero.
We will follow an idea of Turaev \cite[Section~5.1]{Tu86} to define a (twisted) invariant for links even if the (twisted) Alexander module is non--torsion.
This invariant will then give rise to a sliceness obstruction for links. We refer throughout this section to \cite{CF10} and \cite{Tu86} for details.

Let $L\subset S^3$ be an oriented $m$--component link.
Let $R\subset \mathbb{C}$ be a subring and let $\alpha:\pi(S^3\setminus \nu L)\to \mbox{GL}(k,R)$ be a unitary representation. Suppose that
$\psi:\pi_1(S^3\setminus \nu L)\to F$ is a homomorphism to a free abelian group which is non--trivial on each meridian of $L$.
Under these assumptions      we can endow $H_1(S^3\setminus \nu L;Q(R[F])^k)$ and $H_2(S^3\setminus \nu L;Q(R[F])^k)$
with dual bases and using these bases we can define
 the
Reidemeister torsion
\[ \tilde{\tau}^{\alpha\otimes \psi}(L)\in Q(F)^*/N(Q(F)^*),\]
here  $N(Q(F)^*)$ denotes the subgroup of norms of the multiplicative group $Q(F)^*$, i.e.
 $N(Q(F)^*)=\{ q\overline{q} \, |\, q\in Q(F)^*\}$. Reidemeister torsion
$\tilde{\tau}^{\alpha\otimes \psi}(L)$ viewed as an element in $Q(F)^*/N(Q(F)^*)$ is well--defined up to multiplication
by an element of the form $\pm df$ where $d\in \det(\alpha(\pi_1(S^3\setminus \nu L))), f\in F$.
The invariant $\tau^{\alpha\otimes \psi}(L)$ is the twisted version of an invariant first introduced by Turaev \cite[Section~5.1]{Tu86}.


For example, if $L$ is the $m$--component unlink in $S^3$ with meridians $\mu_1,\dots,\mu_m$,
then given $\alpha$ and $\psi$ as above we have
\[ \tilde{\tau}^{\alpha\otimes \psi}(L)=\pm df \cdot \prod\limits_{i=1}^m \det\big(\mbox{id}-\psi(\mu_i)\alpha(\mu_i)\big)^{-1} \, \in Q(F)^*/N(Q(F)^*)\]
with $d\in \det(\alpha(\pi_1(S^3\setminus \nu L))), f\in F$.





In \cite{CF10} the first author and Jae Choon Cha prove the following result.

\begin{proposition}\label{prop:slicelink}
Let $L$ be an $m$--component oriented slice link with meridians $\mu_1,\dots,\mu_m$.
 Let $R\subset \mathbb{C}$ be a subring closed under complex conjugation and let $\alpha:\pi_1(S^3\setminus \nu L)\to \mbox{GL}(k,R)$ be a representation which factors through a finite group of prime power order. Let
$\psi:H_1(S^3\setminus \nu L)\to F$ be an epimorphism onto a free abelian group which is non--trivial on each meridian of $L$.  Then
\[ \tilde{\tau}^{\alpha\otimes \psi}(L)=\pm
 df\cdot \prod\limits_{i=1}^m \det\big(\mbox{id}-\psi(\mu_i)\alpha(\mu_i)\big)^{-1} \, \in Q(F)^*/ N(Q(F))^* \]
 for some $d\in \det(\alpha(\pi_1(S^3\setminus \nu L)))$ and $f\in F$.
\end{proposition}



If $\alpha$ is the trivial representation over $\mathbb{Z}$, then it is shown in \cite[Theorem~5.1.1]{Tu86} that the torsion
is represented by the untwisted Alexander polynomial of $L$ corresponding to $\psi$.
Using this observation we see that Proposition \ref{prop:slicelink} generalizes earlier
results of Murasugi \cite{Mu67}, Kawauchi \cite{Ka77,Ka78} and Nakagawa \cite{Na78}. The approach taken in \cite{CF10}
is partly inspired by  Turaev's proof of the untwisted case (cf. \cite[Theorem~5.4.2]{Tu86}).

In \cite{CF10} we will in particular use the obstruction of Proposition \ref{prop:slicelink} to reprove that the Bing double of the Figure 8 knot is not slice.
This had first been shown by Cha \cite{Ch09}.

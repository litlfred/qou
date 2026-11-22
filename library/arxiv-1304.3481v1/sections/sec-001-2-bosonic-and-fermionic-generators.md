---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-Graded Colored Homology of Knots"
section_id: sec-001-2-bosonic-and-fermionic-generators
section_title: "Bosonic and Fermionic generators"
section_number: 2
pages: 7-19
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 0.977
doc_brief: "Quadruply-Graded Colored Homology of Knots — We conjecture the existence of four independent gradings in the colored HOMFLY homology."
---
\label{sec:bosonic}


\subsection{The algebra of BPS states and knot cobordisms}
\label{sec:geomphys}


While most of this paper is probably aimed at a more mathematical reader, here we offer a geometric
interpretation of some of our observations in the framework more familiar to physicists.
Therefore, the purpose of this section is twofold. First, it will help physicists to
understand better some of our observations (which, we believe, may go beyond the scope of the present
paper and are worth studying further in the context of BPS state counting).
Second, the physical interpretation / motivation provides further evidence
for the structures of knot homologies discussed in this paper.
In Section \ref{sec:inst-surf}
we also comment on the connection with the equivariant instanton counting in the presence of a surface operator.


We begin with a lightning review of the physical interpretation of knot homologies, in which
$\CH_{\text{knot}}$ is identified with a space of supersymmetric particles (the so-called BPS states) \cite{GSV,GukovRTN,fiveknots}:
\be
\CH_{\text{knot}} \; = \; \CH_{\text{BPS}} \,.
\label{HHBPS}
\ee
In particular, it will allow us to see bosonic and fermionic generators of homological knot invariants
and will also help us in section \ref{sec:inst-surf} to understand the limit $\a \to 0$.
As we shall see, the latter allows one
to focus on the ``bottom row'' of the superpolynomial
which turns out to have a very elegant and simple geometric interpretation in the physical framework.

In one of the duality frames, the physical system involves a compactification on a very particular (non-compact) Calabi-Yau 3-fold $X$
in the presence of five-branes supported on a Lagrangian submanifold $L_{K} \subset X$:
\bea
\text{space-time} & : & \qquad \R \times X \times M_4 \label{theoryB} \\
\text{M5-branes} & : &  \qquad \R \times L_K \times D \nonumber
\eea
Specifically, $X$ is the total space of the $\CO (-1) \oplus \CO (-1)$ bundle over $\cp^1$,
while the Lagrangian submanifold $L_K$ is determined by a knot $K \subset \mathbf{S}^3$, {\it cf.} \cite{OoguriV,Taubes,Koshkin}.
Furthermore, the number of five-branes in \eqref{theoryB} is equal to $|\lambda|$ (= the total number of boxes in the Young diagram $\lambda$),
whereas the K\"ahler modulus of $X$ is related to the variable $\a$ in the superpolynomial:

\begin{equation}
\a \; = \; \exp \left( - {\rm Vol} (\cp^1) \right) \,.
\label{NvolCP1}
\end{equation}

This summary was very telegraphic, of course, but the reader can always consult e.g. \cite{GS} for further details, references, and the outline of the relation between different ways of looking at this physical system \eqref{theoryB}.
As reviewed there, the system \eqref{theoryB} was studied in physics as well as in math literature from
many different angles, e.g. from the target space point of view \cite{GSV,GWalcher} that leads to a description of \eqref{HHBPS}
in terms of enumerative invariants of $(X,L_K)$, or from the viewpoint of the five-brane \cite{fiveknots}, or from the viewpoint
of the $\CN=2$ gauge theory on a 4-manifold $M_4$ with ramification \cite{DGH}.
However, only recently \cite{FGS2,FGSS} the system \eqref{theoryB} has been considered from
the viewpoint of the two-dimensional theory on $D$, that will be yet another
motivation for the discussion in Section~\ref{sec:inst-surf}.

Now we are ready to discuss the BPS states that contribute to the reduced and unreduced superpolynomials,
$\CP^{\lambda} (\a,q,t)$ and $\bar \CP^{\lambda} (\a,q,t)$, respectively.

As discussed e.g. in \cite{OoguriV,GSV,NagaoN}, there are two kinds of BPS particles that contribute to \eqref{HHBPS}
in the problem at hand: M2-branes supported on bordered surfaces embedded in $X$ with boundary on $L_K$,
and momentum modes ({\it a.k.a.} D0-branes).
The charge of the former is precisely the $\a$-grading, while the charge of the latter is the $q$-grading.
Both types of states can mix together (forming stable BPS particles that carry both charges) and both can carry
a non-trivial spin $j_3$, which becomes the third $t$-grading on \eqref{HHBPS}.
To summarize, the dictionary between three gradings on the colored HOMFLY homology
and the charges of the BPS particles is as follows:
\be
\begin{array}{rcll}
``\a-\text{grading}" & = & \beta \in H_2 (X,L_K) \cong \Z \; & \quad \text{(``winding number'')} \\[.2cm]
``q-\text{grading}" & = & n \in \Z \;  & \quad  \text{(``D0-brane charge'')} \\[.2cm]
``t-\text{grading}" & = & 2 j_3 \in \Z & \quad  \text{(spin)}
\end{array}
\label{aqtgradings}
\ee
Using this dictionary, we can identify every generator of \eqref{HHBPS} with the corresponding BPS particle.
For example, if we see a term $\a^m q^n t^k$ in the superpolynomial, the proper translation to the physics
language is
\be
\begin{array}{ccl}
\text{monomial} & \longleftrightarrow & \text{``a BPS particle with winding number } m \,, \\[.1cm]
\a^m q^n t^k \subset \CP^{\lambda} & & \; \; \; \text{D0-brane charge } n \,, \text{ and spin } \frac{k}{2} \text{ ''}
\end{array}
\ee
The particles that carry no winding number ($m=0$) are usually called simply D0-branes.

One well-known property of the BPS states in the present setup is that particles that carry non-trivial winding number $m=1$
are fermions, whereas D0-brane states (with $m=0$) are bosonic \cite{Refined,JafferisM}.
When translated to the language of knot homologies, this statement says that statistics of the generators
in the colored HOMFLY homology is correlated with the $\a$-grading!

Namely, the generators with trivial $\a$-grading are bosonic, whereas the generators with $\a$-grading equal to 1 are fermions.
This will play a key role in what follows.\\

\begin{figure}[htb]
\centering
\includegraphics[width=4.0in]{cobordism2}
\caption{A real isotropic knot cobordism $\Sigma \subset \R \times S^3$ defines a coassociative 4-manifold $L_{\Sigma} \subset \R \times T^* S^3$.}
\label{fig:cobordism2}
\end{figure}

Another useful lesson that we can learn from the connection with enumerative (BPS) invariants \eqref{HHBPS}--\eqref{theoryB}
is the behavior of colored HOMFLY homology with respect to cobordisms.
First, however, it is convenient to consider a dual brane system related to \eqref{theoryB}
by a geometric transition\footnote{sometimes also called ``large $N$ duality,'' which is somewhat of a misnomer
since the duality holds for all values of $N$, as long as one is careful with differentials and wall crossing \cite{DGR,GS}} \cite{GopakumarV,OoguriV}:
\bea
\text{space-time} & : & \qquad \R \times T^* W \times M_4 \nonumber \\
N~\text{M5-branes} & : & \qquad \R \times W \times D \label{theoryA} \\
|\lambda|~\text{M5-branes} & : &  \qquad \R \times L_K \times D \nonumber
\eea
where $W = S^3$ in most of our applications (or, its close cousin $W = \R^3$).
This system is relevant to $sl(N)$ homological knot invariants and has been studied from various points of view in \cite{AShakirov,IK,fiveknots}.
One advantage of the duality frame \eqref{theoryA} that will serve us well in building knot cobordisms is that the Lagrangian submanifold $L_K \subset T^* W$ can be defined simply as the conormal bundle to the knot $K \subset W$.

Now, it is easy to describe how knot cobordisms can be implemented in the physical setup.
Since the factor of $\R$ in \eqref{theoryB} and \eqref{theoryA} plays the role of the ``time'' direction,
one can replace $\R \times S^3$ by a general 4-manifold cobordism $V$ and replace $\R \times K$ embedded in it by
a more general knot cobordism $\Sigma \subset V$, as in Figure~\ref{fig:cobordism2}:
\bea
\text{space-time} & : & \qquad X_7 \times M_4 \nonumber \\
N~\text{M5-branes} & : & \qquad V \times D \label{theoryAcob} \\
|\lambda|~\text{M5-branes} & : &  \qquad L_{\Sigma} \times D \nonumber
\eea
Supersymmetry imposes certain constraints, which ensure that the physical setup here continues to
maintain the relation between supersymmetric configurations (BPS states) and functors on knot homologies.
Specifically, the 7-manifold $X_7$ must be a special holonomy manifold with holonomy group $G_2$,
while the 4-manifold $L_{\Sigma}$ must be a coassociative submanifold in $X_7$.
Both can be constructed in a fairly simple way, starting with the data of $V$ and $\Sigma$, respectively.
 
 
Just like $T^* W$ is a ``canonical'' Calabi-Yau 3-fold associated to a 3-manifold $W$, from a 4-manifold $V$
one can build a ``canonical'' $G_2$-holonomy manifold $X_7 = \Lambda^{2,+} (V)$ as the total space of the bundle of self-dual 2-forms.
This 7-manifold $X_7 = \Lambda^{2,+} (V)$ replaces $\R \times T^* W$ and reduces to it when $V = \R \times W$.
In what follows, we restrict our attention only to this case and, moreover, assume $W = S^3$.

Then, given a knot cobordism $\Sigma \subset V = \R \times S^3$,
we wish to construct a coassociative 4-manifold $L_{\Sigma} \subset \Lambda^{2,+} (V)$ with the property
\be
L_{\Sigma} \cap V = \Sigma
\ee
which is a suitable $G_2$-manifold version of the property $L_K \cap S^3 = K$ in \eqref{theoryA}.
By analogy with the conormal bundle construction of $L_K$, the desired coassociative 4-manifold $L_{\Sigma}$
can be defined as the subbundle of $\Lambda^{2,+} (V)$ over $\Sigma \hookrightarrow V$
such that restriction of the fiber to $\Sigma$ is trivial, provided that $\Sigma$ is a real isotropic minimal surface \cite{IKM,KMO}.
Details of this construction and its implications for functors on colored knot homologies will be discussed elsewhere.
Here, we simply point out that the existence of such geometric construction implies the existence of a map
\be
\CH^{\lambda} (\unknot) \otimes \CH^{\lambda} (K) \; \to \; \CH^{\lambda} (K)
\label{HHHunknot}
\ee
Indeed, applying geometric transition one more time to the setup \eqref{theoryAcob} with $V = \R \times S^3$ we get
a ``cobordism version'' of \eqref{theoryB}:
\bea
\text{space-time} & : & \qquad \R \times X \times M_4 \label{theoryBcob} \\
\text{M5-branes} & : &  \qquad \quad L_{\Sigma} \times D \nonumber
\eea
where $L_{\Sigma}$ is a coassociative 4-manifold in $\R \times X$.
When $\Sigma$ is a link cobordism from $K \bigsqcup \unknot$ to $K$,
the setup \eqref{theoryBcob} defines a functor on the space of refined open BPS states and, via \eqref{HHBPS},
leads to a functor \eqref{HHHunknot} on the colored HOMFLY homology.
 

\begin{figure}[htb]
\centering
\includegraphics[width=3in]{walls3}
\caption{Walls and chambers for the conifold $X$ in \eqref{theoryB}.}
\label{fig:walls}
\end{figure}
 
 
Note, that \eqref{HHHunknot} is very similar --- and, in fact, possibly related --- to the conjecture \cite{GS}
that $\CH^{\lambda} (K) = \CH_{\text{BPS}}^{\text{open}}$
is a module over the algebra of {\it closed} BPS states $\CH_{\text{BPS}}^{\text{closed}}$:
\be
\begin{array}{rcl}
\text{refined open BPS states}: &  & \CH_{\text{BPS}}^{\text{open}} \\
 & & \circlearrowleft \\
\text{refined closed BPS states}: &  & \CH_{\text{BPS}}^{\text{closed}}
\end{array}
\label{HHrep}
\ee
Even though we did not pursue the detailed comparison of
$\CA = \CH (\unknot)$ and the algebra $\CH_{\text{BPS}}^{\text{closed}}$ here,
it is worth mentioning that the two share some similarities.
For instance, much like $\CH (\unknot)$ has $sl(N)$ specializations indexed by $N$
and realized by the action of differentials $d_N$ (see below), the space $\CH_{\text{BPS}}^{\text{closed}}$
for the problem at hand also has an infinite set of chambers, conveniently labeled by $N$, see Figure \ref{fig:walls}.
Moreover, in the $N$-th chamber the space $\CH_{\text{BPS}}^{\text{closed}}$
has $N$ stable BPS objects \cite{NagaoN}: D0/D2 bound states of charge $(n,\beta) = (j,1)$, where $0 \le j < N$,
nicely matching the fact that $\CH^{sl(N), \tableau{1}} (\unknot)$ is also $N$-dimensional.



\subsection{Colored polynomials of the unknot}
\label{sec:unknot}

For a Young diagram $\lambda$ and a box $x$ in it we define the arm $a(x)$, leg $l(x)$, co-arm $a'(x)$ and co-leg $l'(x)$ by the Figure \ref{armlegs}. The hook-length of $x$ is defined as
$h(x)=a(x)+l(x)+1,$ and the content of $x$ is defined as $c(x)=a'(x)-l'(x)$.

Let $\lambda$ be a Young diagram with $k$ boxes, let $V_{\lambda}$ denote the irreducible representation of $S_k$ labelled by $\lambda$,
and let $U_{\lambda}=\mathbb{S}_{\lambda}(\C^{N})$ denote the irreducible representation of $sl(N)$ labelled by $\lambda$.
The $sl(N)$ quantum invariant of the $\lambda$-colored unknot coincides with the  character of the representation $U_{\lambda}$ and is given by (\ref{plambda}). This character is given by the hook formula:
$$\mbox{\rm ch} U_{\lambda}=\prod_{x\in \lambda}\frac{(1-q^{N+c(x)})}{(1-q^{h(x)})}.$$
If we substitute $A=q^{N}$, we get
\begin{equation}
\label{plambda}
P^{\lambda}(a,q)=\prod_{x\in \lambda}\frac{(1-A q^{c(x)})}{(1-q^{h(x)})}.
\end{equation}
Let $M_{\lambda}(q,t;p_i)$ be a Macdonald polynomial corresponding to a diagram $\lambda$. Recall that its evaluation can be computed by the formula \cite{macd19}:
\begin{equation}
\label{mstar}
M^{*}_{\lambda}(A,q,t)=M_{\lambda}\left(p_i=\frac{1-A^{i}}{1-t^{i}}\right)=\prod_{x\in\lambda}\frac{t^{l'(x)}-Aq^{a'(x)}}{1-q^{a(x)}t^{l(x)+1}}.
\end{equation}
Note that at $q=t$ the Macdonald polynomials degenerate to Schur polynomials and (\ref{mstar}) degenerates to the equation (\ref{plambda}).
In all approaches based on the refined BPS invariants the (unreduced) colored superpolynomials of the unknot
are given by the Macdonald dimensions
\be
\bar \CP^{\lambda} (\unknot) \; = \; M^*_{\lambda}(A,q,t) \,.
\label{mcdim}
\ee
In order to write these expressions with positive coefficients, one needs to convert to the variables
used e.g. in \cite{DGR}:
$$
A = -\a^2 t \,, \qquad
q = \q^2 \t^2 \,, \qquad
t = \q^2.
$$
The first few values of \eqref{mcdim} read as
\be
\bar \CP^{\tableau{1}} (\unknot) \; = \;
\frac{1 - A^{2}}{1 - t^{2}} =
\frac{1 + \a^2 \t}{1 - \q^2}
\ee
\be
\bar \CP^{\tableau{2}} (\unknot) \; = \;
\frac{(1 - A^{2})(1 - A^{2}q^{2})}{(1 - t^{2})(1 - q^{2} t^{2})}
= \frac{(1 + \a^2 \t) (1 + \a^2 \q^2 \t^3)}{(1 - \q^2) (1 - \q^4 \t^2)}
\ee
where we normalized by an overall powers of $A$, $q$, and $t$, so that
all expressions \eqref{mcdim} have the form of a power series $\bar \CP^{\lambda} (\unknot) = 1 + \ldots$.

\begin{figure}
\begin{tikzpicture}
\draw (0,0)--(0,5)--(1,5)--(1,4)--(3,4)--(3,2)--(5,2)--(5,0)--(0,0);
\draw (2,1)--(2,1.5)--(2.5,1.5)--(2.5,1)--(2,1);
\draw (2.25,1.25) node {$x$};
\draw [<->,>=stealth] (2.5,1.25)--(5,1.25);
\draw [<->,>=stealth] (0,1.25)--(2,1.25);
\draw [<->,>=stealth] (2.25,1.5)--(2.25,4);
\draw [<->,>=stealth] (2.25,0)--(2.25,1);
\draw (4,1) node {$a(x)$};
\draw (1,1) node {$a'(x)$};
\draw (1.9,2.8) node {$l(x)$};
\draw (2.8,0.5) node {$l'(x)$};
\end{tikzpicture}
\caption{Arm, leg, co-arm and co-leg}
\label{armlegs}
\end{figure}

{}From now on we will work in the variables $\a, \q, \t$. The variable $\t$ will be also denoted by $t_c$. The equation
(\ref{mcdim}) in these variables has a form:
\be
\label{mcdim1}
\bar \CP^{\lambda} (\unknot)=\prod_{x\in \lambda}\frac{1+\a^2\q^{2c(x)}t^{2a'(x)+1}}{1-\q^{2h(x)}\t^{2a(x)}}
\ee
Note that the right hand side is a polynomial in $\a$ and a series in $\q$ with all nonnegative coefficients. For $\lambda=S^r$, these answers match the stable homology of $(r,\infty)$ torus knots defined in \cite{DGR}.



\subsection{Schur-Weyl duality}

Following \cite{KRb}, let us model the fundamental representation of $sl(N)$ as $U_{\square}=\C[x]/(x^N).$
The Schur-Weyl duality (e.g. \cite{FH}) says that
$$U_{\square}^{\otimes k}=\bigoplus_{|\mu|=k}V_{\mu}\otimes U_{\mu},$$
or, equivalently,
\begin{equation}
\label{hom}
U_{\lambda}=\mbox{\rm Hom}_{S_k}(V_{\lambda},U_{\square}^{\otimes k})=\mbox{\rm Hom}_{S_k}(V_{\lambda},\C[x_1,\ldots,x_k]/I_{N}),
\end{equation}
where the ideal $I_N\subset \C[x_1,\ldots,x_k]$ is generated by $x_1^N,\ldots, x_k^N$. If $\lambda$ corresponds to the symmetric power of the fundamental representation, the construction
(\ref{hom}) gives the identity
$$S^{k}U_{\square}=(\C[x_1,\ldots,x_k]/I_{N})^{S_k}=\mathbb{C}[x_1,\ldots,x_k]^{S_k}/(I_{N})^{S_k}.$$
The symmetrized ideal $I_{N}^{S_k}$ is generated by $p_{N+s}=\sum x_i^{N+s}$ for $0\le s\le k-1$. If $\lambda$ corresponds to the exterior power of the fundamental representation, we have to study the anti-symmetric part of
$I_n$. One can check (\cite{GWalcher}) that $(I_N)^{\epsilon}$ is generated by $\Delta\cdot h_{N+1-j}, 1\le j\ge k$, where $h_i$ denote the complete symmetric polynomials, and $\Delta$ denotes the Vandermonde determinant. Therefore
$$\Lambda^{k}U_{\square}=(\mathbb{C}[x_1,\ldots,x_k]/I_{N})^{\epsilon}=\Delta \cdot (\C[x_1,\ldots,x_k])^{S_k}/(h_{N+1-j}).$$
Remark that the latter equation allows us to identify the exterior power with the cohomology of the Grassmannian:
$$\Lambda^{k}U_{\square}(sl(N))=\Delta\cdot H^{*}(Gr(k,N)),$$
since $h_{i}$ can be naturally identified with the Chern classes of the quotient bundle.

The setup of \cite{DGR} and \cite{GS} prescribes the knot homology to be obtained by a certain reduction procedure from the
``large $N$ limit''. Let us describe this construction for the case of unknot.
Given a Young diagram $\lambda$, there supposed to exist a triply graded space $\CH^{\lambda}$ modelling the $\lambda$-colored HOMFLY homology of the unknot. This space is equipped with the differentials $d_N$, and the homology of $\CH^{\lambda}$ with respect to $d_N$ should be isomorphic to the $sl(n)$ homology of the unknot colored by $\lambda$. Let us describe $\CH^{\lambda}$ along the lines of the above Schur-Weyl duality.
We start with the fundamental representation
$U_{\square}(sl(N))=\C[x]/(x^N).$
The corresponding triply graded space will be
$$\CH^{\square}=\Omega^{\bullet}(\C)=\C[x,dx],$$
and the differential comes from the Koszul complex:
$$d_{N}(x)=0,\quad d_{N}(dx)=x^{N}.$$
It is clear that $H^{*}(\CH^{\square}, d_N)\simeq U_{\square}(sl(N)).$
The $k$-th tensor power of this construction will give
$$\CH^{\square^{\otimes k}}=\Omega^{\bullet}(\C^{k})=\C[x_1,\ldots,x_k;dx_1,\ldots,dx_k],$$
and the differential is given by the formula
$d_N(x_i)=x_i^{N}$.
Therefore a natural candidate for $\CH^{\lambda}$ will be \cite{GWalcher}:
\begin{equation}
\label{hlambda}
\CH^{\lambda}:=\mbox{\rm Hom}_{S_k}\left(V_{\lambda},\Omega^{\bullet}(\C^{k})\right).
\end{equation}
Note that this space (as in the uncolored case) differs from the naive limit of $U_{\lambda}(sl(N)).$
It is naturally equipped with two gradings: $a$-grading is given by the degree of a differential form and $q$-grading is a standard
polynomial grading. In other words, the $(a,q)$-degree for $x_i$ equals to $q^{2i}$ and for $dx_i$ equals to $a^2$.

Let us check that the $(a,q)$-character of the space $\CH^{\lambda}$ agrees with the colored HOMFLY polynomial of the unknot. It follows from the results of \cite{KirPak} (see also \cite{Molch}) that the character of $\CH^{\lambda}$ equals 
\begin{equation}
\label{charUnknot}
\mbox{\rm ch}\CH^{\lambda}(a,q)=\prod_{(i,j)\in \lambda}\frac{(q^{i-1}+aq^{j-1})}{(1-q^{h(i,j)})}.
\end{equation}
Therefore
$\mbox{\rm ch}\CH^{\lambda}(a,q)=q^{\nu(\lambda)}P^{\lambda}(-a,q),$ where $\nu(\lambda)=\sum (i-1)\lambda_{i}.$
At $a=0$ the character (\ref{charUnknot})  degenerates to:
\begin{equation*}
P_{\text{bottom}}(\CH^{\lambda})=\prod_{(i,j)\in \lambda}\frac{q^{i-1}}{1-q^{h(i,j)}}.
\end{equation*}

For a symmetric representation we have
$$\CH^{S^{k}}=\left(\Omega^{\bullet}(\C^{k})\right)^{S_k}=\Omega^{\bullet}(\C^{k}/S_k)=\C[u_1,\ldots,u_k;du_1,\ldots,du_k],$$
where $u_i$ denote the elementary symmetric polynomials. Remark that the $(a,q)$-degree for $u_i$ equals to $q^{2i}$ and
for $du_i=\sum \frac{\partial u_i}{\partial x_j}dx_j$ equals to $a^2q^{2i-2}$. Therefore the bigraded Poincar\'e series $\CH^{S^{k}}$ has a form:
$$P(\CH^{S^{k}})=\prod_{i=1}^{k}\frac{1+a^2q^{2i-2}}{1-q^{2i}},$$
in agreement with (\ref{mcdim1}).


Let us describe the ``bottom'' $a=0$ part of the homology for $\lambda=\tableau{2 1}$.
The corresponding representation of $S_3$ is the standard two-dimensional representation.
We have to compute $\mbox{\rm Hom}_{S_k}\left(V_{\lambda},\C[x_1,x_2,x_3]\right)$.
Let $\mathfrak{a}\subset \C[x_1,x_2,x_3]$ denote the  ideal generated by the symmetric polynomials of
positive degree.
It is known that $\C[x_1,x_2,x_3]/\mathfrak{a}$ is isomorphic to the regular representation of $S_3$, and it contains two copies of $V_{\lambda}$
in gradings 1 and 2. These copies can be multiplied by arbitrary symmetric polynomials, so the character of the $a=0$ part of the homology
equals to
$$\frac{q+q^2}{ (1-q)(1-q^2)(1-q^3)}=\frac{q}{(1-q)^2(1-q^3)}.$$
This results agrees with the hook formula (\ref{plambda}) at $a=0$, since the hook-lengths for the boxes of our diagram are equal to 1, 1 and 3.


\subsection{Colored homology of the unknot}
\label{sec:alggrad}

Consider a free supercommutative algebra $\CA$ with even generators $u_1,\ldots,u_r$ and odd generators $\xi_1,\ldots,\xi_{s}$. Suppose that the algebra is graded such that
$\deg u_i=\alpha_{i},\ \deg \xi_i=\beta_{i}.$
It is clear that the Hilbert series of this algebra is given by the formula
\begin{equation}
\label{hilbert free}
H_{\alpha,\beta}(q)=\frac{\prod_{i=1}^{s}(1+q^{\beta_{i}})}{\prod_{i=1}^{r}(1-q^{\alpha_{i}})}.
\end{equation}
The similarity of this formula to (\ref{plambda}) and (\ref{mcdim1}) suggests the following construction.
We conjecture that the homology $\CH^{\lambda}$ of the unknot colored by the representation $\lambda$ is isomorphic to the
free graded supercommutative algebra $\CA$. To every box $x$ of $\lambda$ we associate an even generator $u_{x}$ and an odd generator $\xi_{x}$. The algebra has three gradings $q,a,t_{c}$ such that
$$(q,a,t_{c})[u_{x}]=(2h(x),0,2a(x)),\quad (q,a,t_{c})[\xi_{x}]=(2c(x),2,2a'(x)+1).$$
By (\ref{hilbert free}) and (\ref{mcdim1}) the Hilbert series of this algebra equals to
$$
\bar \CP^{\lambda}(\unknot)(a,q,t_{c})=\prod_{x\in \lambda}\frac{1+a^2q^{2c(x)}t^{2a'(x)+1}_{c}}{1-q^{2h(x)}t_{c}^{2a(x)}}.
$$

As we will mostly discuss the rectangle-shaped Young diagrams, let us fix some notations for them.
Let $\lambda$ be a rectangle with $R$ rows and $S$ columns. For a box $x=(i,j),\ 1\le i\le S, 1\le j\le R$ in it we have:
$$a(x)=S-i,\qquad l(x)=R-j,\qquad h(x)=R+S-i-j+1,$$
$$a'(x)=i-1,\qquad l'(x)=j-1.$$
To this box we associate a bosonic generator $u_{ij}$ and a fermionic generator $\xi_{ij}$ such that
$$(q,a,t_{c})[u_{ij}]=(2(R+S-i-j+1),0,2(S-i)),\quad (q,a,t_{c})[\xi_{ij}]=(2(i-j),2,2i-1).$$

We define a fourth grading using the mirror symmetry between $R\times S$ and $S\times R$ rectangles.
To write down the isomorphism $M_{\lambda} : \CH^{\lambda} \to \CH^{\lambda^t}$, one can define it on the level of generators.
We define
$$M_{\lambda} (u_{ij}):=u_{R-j+1,S-i+1},\quad M_{\lambda} (\xi_{ij}):=\xi_{ji}.$$

The correspondence between boxes is shown in Figure \ref{mirrorrect}.
Note that for bosonic generators we fix the southeast corner of the rectangle (marked with *) while
for the fermionic ones we fix the southwest corner.
We define the grading $t_{r}$ using the mirror symmetry relation $t_{r}(w)=t_{c}(M_{\lambda} (w))$, so
$$t_{r}(u_{ij})=2j-2,\qquad t_{r}(\xi_{ij})=2j-1.$$
Using the formula $$Q=\frac{q+t_{r}-t_{c}}{R},$$
we get
$$Q(u_{ij})=2,\quad Q(\xi_{ij})=0.$$

\begin{figure}
\begin{tikzpicture}
\draw (0,4)--(0,6)--(3,6)--(3,4)--(0,4);
\draw (1.2,5) node {$\bullet$};
\draw [<->,>=stealth] (0,5)--(1.1,5);
\draw [<->,>=stealth] (1.2,4)--(1.2,4.9);
\draw (0.6,5.2) node {$i$};
\draw (1.4,4.5) node {$j$};
\draw (2.8,4.2) node {*};

\draw [<->,>=stealth] (3.5,5)--(4.5,5);
\draw (4,5.2) node {$M$};

\draw (5,4)--(5,7)--(7,7)--(7,4)--(5,4);
\draw (6,5.8) node {$\bullet$};
\draw [<->,>=stealth] (6.1,5.8)--(7,5.8);
\draw [<->,>=stealth] (6,5.9)--(6,7);
\draw (5.9,6.4) node {$i$};
\draw (6.5,5.6) node {$j$};
\draw (6.8,4.2) node {*};


\draw (0,0)--(0,2)--(3,2)--(3,0)--(0,0);
\draw (1.2,1) node {$\bullet$};
\draw [<->,>=stealth] (0,1)--(1.1,1);
\draw [<->,>=stealth] (1.2,0)--(1.2,0.9);
\draw (0.6,1.2) node {$i$};
\draw (1.4,0.5) node {$j$};
\draw (0.2,0.2) node {*};

\draw [<->,>=stealth] (3.5,1)--(4.5,1);
\draw (4,1.2) node {$M$};

\draw (5,0)--(5,3)--(7,3)--(7,0)--(5,0);
\draw (6,1.2) node {$\bullet$};
\draw [<->,>=stealth] (5.9,1.2)--(5,1.2);
\draw [<->,>=stealth] (6,1.1)--(6,0);
\draw (5.9,0.5) node {$i$};
\draw (5.4,1.4) node {$j$};
\draw (5.2,0.2) node {*};

\end{tikzpicture}
\caption{Mirror symmetry for $u_{ij}$ (upper pair) and for $\xi_{ij}$ (lower pair).}
\label{mirrorrect}
\end{figure}




\subsection{Potentials and differentials: antisymmetric case}
\label{sec:potentanti}

It is known (\cite{DGR,Gornik,GWalcher,Lee}, see also Section \ref{sec:gradings}) that the reduction from HOMFLY homology to $sl(N)$ homology
is given by the following procedure. Let $\CH^{\lambda}(K)$ and $\CH^{sl(N),\lambda}(K)$
respectively denote the HOMLFY and $sl(N)$ homology of a knot $K$. There exists a differential $d_{N}$
of $(a,q)$-degree $(-1,N)$ such that
$$\CH^{sl(N), \lambda}(K)=H^{*}(\CH^{\lambda}(K),d_{N})$$
Remark that $d_{N}$ preserves the grading $Na+q$, and its Euler characteristic with respect to this grading equals
$P^{\lambda}(K;a=q^{N},q)=P^{sl(N), \lambda}(K).$

On the other hand, it is known that for some diagrams $\lambda$ one can construct a family of potentials
$W_{\lambda,N}(u_1,\ldots,u_d)$ such that $\CH^{sl(N), \lambda}(\unknot)$ coincides with the Jacobi ring $J=\C[u_i]/\left(\frac{\partial W_{\lambda,N}}{\partial u_i}\right)$.
More generally, $\CH^{sl(N), \lambda}(\unknot)$ is expected to coincide with the Hochschild homology of the category of the matrix factorizations of $W_{\lambda,N}$, that is, with the homology of the Koszul complex associated with the sequence of the partial derivatives of
$W_{\lambda,N}$. The latter homology contains the Jacobi ring $J$ and is equal to it if and only if $W_{\lambda,N}$ has only isolated singularities.
In other words, if the potentials $W_{\lambda,N}(u_1,\ldots,u_d)$ exist then one can consider the free supercommutative algebra $\CA$
with even generators $u_1,\ldots,u_d$,  odd generators $\xi_1,\ldots,\xi_{d}$ and the differential
$$d_{N}:\C[u_i,\xi_j]\to \C[u_i,\xi_j],\quad d_{N}(\xi_i)=\frac{\partial W_{\lambda,N}}{\partial u_i},\ d_{N}(u_i)=0.$$
This matches with the above construction of differentials, if one can identify $u_i$ and $\xi_i$ with the even and odd generators of
$\CH^{\lambda}$, so that $\C[u_i,\xi_j]=\CH^{\lambda}$.

The potential $W_{\Lambda^{k},N}$ was found in \cite{GWalcher}:
$$W_{\Lambda^{k},N}(u_1,\ldots,u_k)=\Coef_{N+1}\left[\ln (1+zu_1+\ldots+z^{k}u_k)\right].$$
It has an isolated singularity at the origin, and the Jacobi rings of $W_{\Lambda^{k},N}$ and $W_{\Lambda^{N-k},N}$ are isomorphic.
Moreover, one can check that up to some change of variables $(u_i)\to (v_i)$ the following identity holds:
\begin{equation}
\label{split of W}
W_{\Lambda^{k},2k-j}(u_1,\ldots,u_k)=W_{\Lambda^{k-j},2k-j}(v_1,\ldots,v_{k-j})+\frac{1}{2}\sum_{s=1}^{j}v_{k-j+s}v_{k+1-s}.
\end{equation}
For example, one can check that
$W_{\Lambda^{2},3}=-\frac{u_1^4}{4} + u_1^{2}u_2 - \frac{u_2^2}{2},W_{\Lambda^{1},3}=-\frac{u_1^{4}}{4},$
hence
$$W_{\Lambda^{2},3}=-W_{\Lambda^{1},3}-\frac{(u_2-u_1^2)^2}{2}.$$

\begin{remark}
Let us explain the construction of $v_{i}$ in general.
Consider supplementary variables $w_j$ defined by the equation
$$w_s=\Coef_j\left[\frac{1+zu_1+\ldots+z^{k}u_k}{1+zu_1+\ldots+z^{k-j}u_{k-j}}\right].$$
Clearly, $w_s=0$ for $s\le k-j$, and the change of variables
$$(u_1,\ldots,u_k)\to (u_1,\ldots, u_{k-j},w_{k-j+1},\ldots,w_{k})$$
is invertible. Now
$$W_{\Lambda^{k},2k-j}(u_1,\ldots,u_k)-W_{\Lambda^{k-j},2k-j}(u_1,\ldots,u_{k-j})=$$ $$\Coef_{2k-j+1}\ln\left[\frac{1+zu_1+\ldots+z^{k}u_k}{1+zu_1+\ldots+z^{k-j}u_{k-j}}\right]=$$
$$\Coef_{2k-j+1}\ln\left[(1+w_{k-j+1}z^{k-j+1}+\ldots+w_{k}z^{k}+\ldots)\right]=$$
$$\frac{1}{2}\sum_{s=1}^{j}w_{k-j+s}w_{k+1-s}+\ldots.$$
Since the quadratic part of this expression is non-degenerate, one can apply Morse lemma
with parameters and get rid of terms of higher degree in $w$'s.
See also \cite{GZV} for an alternative proof of this result and further discussions.
\end{remark}


The equation (\ref{split of W}) can be rewritten as $W_{\Lambda^{k},2k-j}=W_{\Lambda^{k-j},2k-j}+W'$, and we get the following diagram:
\begin{equation}
\begin{tabular}[c]{ccc}
$\CH^{\Lambda^{k}}$ & $\xrightarrow{d_{\Lambda^{k}\to \Lambda^{k-j}}}$ & $\CH^{\Lambda^{k-j}}$\cr
 $\vline$ & & $\vline$ \cr
${d_{2k-j}}$ & & ${d_{2k-j}}$\cr
 $\downarrow$ & & $\downarrow$ \cr
$\CH^{\Lambda^{k},2k-j}$ & $\xrightarrow{\qquad =\qquad}$ & $\CH^{\Lambda^{k-j},2k-j}$
\end{tabular}
\end{equation}

Here the colored differential $d_{\Lambda^{k}\to \Lambda^{k-j}}$ coincides with the one defined in \cite{GS}.
It is defined on HOMFLY homology colored by $\Lambda^{k}$, and its homology are isomorphic to the HOMFLY homology colored by $\Lambda^{k-j}$.
It corresponds to the ``remainder potential'' $W'=\frac{1}{2}\sum_{s=1}^{j}v_{k-j+s}v_{k+1-s}$ in (\ref{split of W}).
The corresponding Koszul complex is associated to the sequence of polynomials $v_{k-j+1},\ldots,v_{k}$:
$$d_{\Lambda^{k}\to \Lambda^{k-j}}(\xi_i)=v_{i+k-j},$$
and its homology is isomorphic to a free superpolynomial algebra generated by $v_1,\ldots,v_{k-j},\xi_{j+1},\ldots,\xi_n$.
We can easily see this differential on the picture with the bosonic and fermionic generators labeled by the boxes of a Young diagram.
Recall that their $q$-degrees are twice the contents and the hook-length of the boxes of $\Lambda^{k}$ respectively, as shown in Figure \ref{dlambda}. The differential $d_{\Lambda^{k}\to \Lambda^{k-j}}$ has $q$-degree $4k-2j$,
\be
(a,q) [d_{\Lambda^{k}\to \Lambda^{k-j}}] \; = \; (-2,4k-2j)
\ee

\begin{figure}
\begin{tikzpicture}
\draw (0,0)--(0,5)--(1,5)--(1,0)--(0,0);
\draw (0,4.5)--(1,4.5);
\draw (0,3)--(1,3);
\draw (0,2.5)--(1,2.5);
\draw (0,0.5)--(1,0.5);
\draw (-0.2,4.7) node {$2$};
\draw (-1,2.7) node {$2(k-j+1)$};
\draw (-0.3,0.3) node {$2k$};
\draw (0.5,4) node {$\vdots$};
\draw (0.5,1.5) node {$\vdots$};
\draw (0.5,4.7) node {$u_1$};
\draw (0.5,2.7) node {$u_{k-j+1}$};
\draw (0.5,0.3) node {$u_k$};
\draw (0.5,-1) node {$q(u_x)$};

\draw (4,0)--(4,5)--(5,5)--(5,0)--(4,0);
\draw (4,4.5)--(5,4.5);
\draw (4,3)--(5,3);
\draw (4,2.5)--(5,2.5);
\draw (4,0.5)--(5,0.5);
\draw (5.6,4.7) node {$2-2k$};
\draw (5.7,2.7) node {$2j-2k$};
\draw (5.3,0.3) node {$0$};
\draw (4.5,4) node {$\vdots$};
\draw (4.5,1.5) node {$\vdots$};
\draw (4.5,4.7) node {$\xi_1$};
\draw (4.5,2.7) node {$\xi_{j}$};
\draw (4.5,0.3) node {$\xi_k$};
\draw (4.5,-1) node {$q(\xi_x)$};

\draw [->,>=stealth] (3.8,4.7)--(1.2,2.7);
\draw (2.5,2.7) node {$\vdots$};
\draw [->,>=stealth] (3.8,2.7)--(1.2,0.3);
\end{tikzpicture}
\caption{Action of the differential $d_{\Lambda^{k}\to \Lambda^{k-j}}$ and the $q$-degrees of the generators $u_{x},\xi_{x}$.}
\label{dlambda}
\end{figure}



\subsection{Potentials and differentials: extension to $n\lambda$}
\label{sec:extension}

Let us first fix some notations. Let $\lambda=(\lambda_1,\ldots,\lambda_r)$ be a Young diagram. Then the boxes of
$n\lambda=(n\lambda_1,\ldots,n\lambda_r)$ are split into groups by $n$ boxes labelled by the boxes of $\lambda$.
If $x$ is a box of $\lambda$, then we label the corresponding boxes in $n\lambda$ by $x^{(1)},\ldots,x^{(n)}$.

For every $x$ in $\lambda$ we can also consider the generators $u_{x}$ and $\xi_{x}$ in
$\CH^{\lambda}$ and the generators  $u_{x}^{(i)}$ and $\xi_{x}^{(i)}$ in
$\CH^{n\lambda}$. For convenience, we can consider the generating functions
$$u_{x}(\tau)=\sum_{i=1}^{n-1} u_{x}^{(i)}\tau^{i-1},\ \xi_{x}(\tau)=\sum_{i=1}^{n-1} \xi_{x}^{(i)}\tau^{i-1}.$$

Suppose that the diagram $\lambda$ admits a potential $W_{\lambda,N}(u_1, \ldots, u_d)$. We conjecture that for all $n$
the diagrams $n\lambda$ admit potentials $W_{n\lambda,N}$ such that
\begin{equation}
\label{extension of W}
\hat{W}(\tau)=\sum_{n=1}^{\infty}\tau^{n-1}W_{n\lambda,N}=W_{\lambda,N}(u_1(\tau),\ldots,u_d(\tau)).
\end{equation}


Since $W_{\Lambda^{2},3}(u_1,u_2)=-\frac{u_1^4}{4} + u_1^{2}u_2 - \frac{u_2^2}{2}$, we have
$$W_{2\Lambda^{2},3}(u_{1}^{(1)},u_{1}^{(1)},u_{2}^{(1)},u_{2}^{(2)})=\Coef_{1}\left[-\frac{u_1(\tau)^4}{4} + u_1(\tau)^{2}u_2(\tau) - \frac{u_2(\tau)^2}{2}\right]=$$
$$=-\left(u_{1}^{(1)}\right)^{3}u_{1}^{(2)} + \left(u_{1}^{(1)}\right)^{2}u_{2}^{(2)}+ 2u_{1}^{(1)}u_{1}^{(2)}u_{2}^{(1)} - u_{2}^{(1)}u_{2}^{(2)}.$$
Remark that $u_{i}^{(j)}$ correspond to the boxes of the $2\times 2$ rectangle (see Figure \ref{2x2}), so that their $q$-degrees are equal to the hook-lengths:
$$q(u_{1}^{(1)})=q(u_1)=2,\ q(u_{1}^{(2)})=4,\ q(u_{2}^{(1)})=q(u_{2})=4,\ q(u_{2}^{(2)})=6.$$
The potential $W_{2\Lambda^{2},3}$ is homogeneous of $q$-degree 10.


\begin{figure}
\begin{tikzpicture}
\draw (0,0)--(0,2)--(2,2)--(2,0)--(0,0);
\draw (0,1)--(2,1);
\draw (1,0)--(1,2);
\draw (0.5,0.5) node {$u_{2}^{(2)}$};
\draw (1.5,0.5) node {$u_{2}^{(1)}$};
\draw (0.5,1.5) node {$u_{1}^{(2)}$};
\draw (1.5,1.5) node {$u_{1}^{(1)}$};

\draw (-2,0)--(-2,2)--(-1,2)--(-1,0)--(-2,0);
\draw (-2,1)--(-1,1);
\draw (-1.5,0.5) node {$u_2$};
\draw (-1.5,1.5) node {$u_1$};
\end{tikzpicture}
\caption{Bosonic generators for $\Lambda^2$ and $2\Lambda^2$.}
\label{2x2}
\end{figure}

\begin{figure}
\begin{tikzpicture}
\draw (0,0)--(0,2)--(2,2)--(2,0)--(0,0);
\draw (0,1)--(2,1);
\draw (1,0)--(1,2);
\draw (0.5,0.5) node {$\xi_{2}^{(1)}$};
\draw (1.5,0.5) node {$\xi_{2}^{(2)}$};
\draw (0.5,1.5) node {$\xi_{1}^{(1)}$};
\draw (1.5,1.5) node {$\xi_{1}^{(2)}$};

\draw (-2,0)--(-2,2)--(-1,2)--(-1,0)--(-2,0);
\draw (-2,1)--(-1,1);
\draw (-1.5,0.5) node {$\xi_2$};
\draw (-1.5,1.5) node {$\xi_1$};
\end{tikzpicture}
\caption{Fermionic generators for $\Lambda^2$ and $2\Lambda^2$.}
\label{2x2ferm}
\end{figure}

Moreover, suppose that we have some differential $D$ on $\CH^{\lambda}$ given by the formula
$D(\xi_l)=p_{l}(u_1,\ldots,u_d).$ Such a differential can be naturally extended to $n\lambda$ by the formula
\begin{equation}
\label{extension of D}
D_n(\xi_{l}^{(i)})=\Coef_{n-1-i}[p_{l}(u_1(\tau),\ldots,u_d(\tau))]
\end{equation}
Remark that equations (\ref{extension of W}) and (\ref{extension of D}) agree with each other.
Indeed, every potential $W$ induced a differential $D_{W}$ such that $D_{W}(\xi_l)=\frac{\partial W}{\partial u_l}$,
if we match a bosonic variable $u_l$ with the fermionic variable $\xi_l$. We can match $u_{l}^{(i)}$ with $\xi_{l}^{(i)}$
so that
$$\frac{\partial W_n}{\partial u_{l}^{(i)}}=\Coef_{n-1}\left[\frac{\partial \hat{W}}{\partial u_{l}}\frac{\partial u_{l}(\tau)}{\partial u_{l}^{(i)}}\right]=\Coef_{n-1-i}[p_{l}(u_1(\tau),\ldots,u_d(\tau))].$$


As an example of this construction, consider $\lambda=(1)$, so that $n\lambda=(n)=S^{n}$.
We have $W_{\lambda,N}=x^{N+1}$, and it was suggested in \cite{GOR} (see also \cite{GORS})
that
$$W_{S^{n},N}=\Coef_{n-1}(x^{(1)}+x^{(2)}\tau+\ldots+x^{(n)}\tau^{n-1})^{N+1}.$$
This differential differs form the one proposed in \cite{GWalcher}, but its homology agree with the known categorifications of the Jones-Wenzl projectors \cite{CHKrushkal,CKrushkal,Stroppel}.

As a more interesting example, let us compute the colored differential for the rectangular $R\times S$ diagram.
Such a diagram can be presented as $S\cdot \Lambda^{R}$, and, as such, admits an extension of the colored differential
$d_{\Lambda^{R}\to \Lambda^{j}}$. We have
$d_{\Lambda^{R}\to \Lambda^{j}}(\xi_{l})=u_{l-j},$
so
$$d_{R\times S\to j\times S}(\xi_{l}^{(m)})=u_{l-j}^{(m)}.$$





In Figure \ref{d22to21} we show the action of the differential $d_{2\Lambda^2\to 2\Lambda^1}$.
The left and right rectangles illustrate the $q$-degrees of the bosonic and fermionic generators respectively.
The differential has $q$-degree 6 (the same as $d_{\Lambda^2\to \Lambda^1}$), and its homology is a free graded supercommutative algebra
isomorphic to $\CH^{S^2}$.


\begin{figure}
\begin{tikzpicture}
\draw (0,0)--(0,2)--(2,2)--(2,0)--(0,0);
\draw (0,1)--(2,1);
\draw (1,0)--(1,2);
\draw (0.5,0.5) node {$6$};
\draw (1.5,0.5) node {$4$};
\draw (0.5,1.5) node {$4$};
\draw (1.5,1.5) node {$3$};

\draw (3,0)--(3,2)--(5,2)--(5,0)--(3,0);
\draw (3,1)--(5,1);
\draw (4,0)--(4,2);
\draw (3.5,0.5) node {$0$};
\draw (4.5,0.5) node {$2$};
\draw (3.5,1.5) node {$-2$};
\draw (4.5,1.5) node {$0$};

\draw [->,>=stealth] (3.1,1.5)--(1.9,0.5);
\draw [->,>=stealth] (4.2,1.5)--(0.8,0.5);

\draw (1,-0.5) node {$u_{x}$};
\draw (4,-0.5) node {$\xi_{x}$};
\end{tikzpicture}
\caption{Colored differential $d_{2\Lambda^2\to 2\Lambda^1}$.}
\label{d22to21}
\end{figure}

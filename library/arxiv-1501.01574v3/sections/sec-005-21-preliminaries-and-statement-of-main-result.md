---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-005-21-preliminaries-and-statement-of-main-result
section_title: "Preliminaries and statement of main result"
section_number: 2.1
pages: 4-6
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.994
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polynomial and the boundary slopes of knots under the operation of cabling."
---
Let $V$  be a standardly embedded solid torus in $S^3$ and let $V'\subset V$ a second standard solid torus 
that is concentric to $V$. On $\partial V'$  we choose a pair of meridian and canonical longitude  (which also determines such a pair on $\partial V$).  For coprime integers $p,q$, let  $T_{p,q}\subset \partial V'$ be a simple closed curve
of slope $p/q$; that is a $(p, q)$-torus knot.

Recall that for a knot  $K$, $n(K)$  denotes  a neighborhood of $K$.  Embed $V$ in $S^3$ by a  homeomorphism   $f: V\longrightarrow n(K)$
that preserves the canonical longitudes. The $(p,q)$-cable of $K$ is the image
$K_{p,q}:= f(T_{p, q})$.  
The space $C_{p, q}: =f(\overline{V\setminus n(T_{p, q})})$
is called a  $(p,q)$-\emph{cable space}.  The complement of  $K_{p,q}$, denoted by $\M$,
is obtained from the complement of $K$ by attaching $\C$.
The space $\C$ has two boundary components; the inner one $T_{-}=f( \partial n(T_{p, q}))=\partial\M$
and the outer one $T_{+}=f(\partial V)=\partial M_K$.



\begin{define}  \label{bdryslopes} For a knot $K\subset S^3$,  let $\langle \mu, \lambda \rangle$ be the canonical
meridian--longitude basis of $H_1 (\bdy n(K))$.  For a pair of integers $(a, b)$,  the ratio  $a/b \in
{\QQ}\cup \{ 1/0\}$ is called a \emph{boundary slope} of $K$ if there
is a properly embedded essential surface $(S, \bdy S) \subset (M_K,
\bdy n(K))$, such that  $\bdy S$ represents  $a \mu + b \lambda \in
H_1 (\bdy n(K))$. 
\end{define}


In Definition \ref{bdryslopes},  $a, b$  do not need to be coprime.
In fact if $d=\gcd(a, b)$ then we have a surface $S$ as above with $d$ boundary components.
To stress this point sometimes we will say that the \emph{total} slope of $\partial S$ is $a/b$.
Recall that every knot $K$ has finitely many boundary slopes and that
$bs_K$ denotes the set of boundary slopes of $K$.
The rest of the section is devoted to the proof of the following theorem.

\begin{theorem} 
 \label{main:bs} 
 (a)\ Let $K \subset S^3$  be a non-trivial knot and $(p, q)$ coprime  integers.
If $a/b$ is a boundary slope of $K$, then
$q^2 a/b$ is a boundary slope of ${K_{p,q}}$. 
\smallskip

\smallskip

(b)\ For every knot $K \subset S^3$ and $(p, q)$ coprime  integers,
we have 
 $$\left( q^2 bs_K \cup \{pq\} \right) \subset bs_{K_{p,q}}.$$
\end{theorem}

\smallskip



The reader is referred to 
\cite{Ha, hempel} for basic definitions and terminology. 
Let $(p, q)$ be coprime integers.
The cable space $\C$ is a Seifert fibered manifold over an annulus $B$, with one singular fiber of multiplicity $q$. 
In $\C$ there is an essential annulus $A$, that is vertical with respect to the fibration,  with $\bdy A \subset T_{-}$ and with boundary slope equal
to $pq$; this annulus is the \emph{cabling annulus}. 
There are two additional essential annuli in $\C$. One with both boundary components on $T_{-}$, each with slope
$p/q$. The other annulus 
 $A'$ has one component of $\bdy A'$ on $T_{-}$ with slope $pq$, and the second component of $\bdy A'$
on $T_{+}$ with slope $p/q$. See \cite{GL}. In particular, we have the following.
\begin{lemma} \label{cannulus} For any cable knot $\K$, $s=pq$ is a boundary slope in $\M$.

\end{lemma}


Recall that a properly embedded surface $S$ in a 3-manifold  $M$ with boundary, is \emph{essential}
if the map on $\pi_1$ induced by inclusion is injective. If $S$ is orientable
this is equivalent to saying that $S$ is \emph{incompressible} and \emph{ $\partial$-incompressible}
in $M$. If $S$ is non-orientable, then $S$ being essential is  equivalent 
to saying that  the surface $\widetilde{S}: =\partial(S\times I )$ is incompressible and $\partial$-incompressible 
in  $M$.

We need the following lemma, a proof of which is given, for example, in   \cite[Proposition 1.1]{KS}.

\begin{lemma} \label{basic} Let $M$ be a knot complement in $S^3$ and let $\Sigma$ be a properly embedded essential surface 
in $M$. Suppose that a path $\alpha \subset \Sigma$ that has its endpoints on $\partial \Sigma$ is homotopic relative endpoints in $M$
to a path in $\partial M$. Then $\alpha$ is homotopic relative endpoints in $\Sigma$ 
to a path in $\partial \Sigma$.

\end{lemma}

The complement $\M$ of the cable knot  $\K$ is obtained by gluing $\C$ and the complement of $K$
along the torus $T_+$.  If $K$ is a non-trivial knot,  then the  torus $T_{+}$ is essential in $\M$; that is a companion
of $\K$.

We will use $\M \cut T_{+}$ to denote the 3-manifold obtained by splitting
$\M$ along $T_{+}$. Also given a  properly embedded surface $S$ in $\M$ we will use $S\cut T_{+}$
to denote the image of $S$ in $\M \cut T_{+}$.


\begin{lemma}\label{components} Let $K \subset S^3$  be a non-trivial knot and $(p, q)$ coprime  integers.
Let $S$ be a properly embedded surface in $\M$. Suppose that each component of  $S \cut T_{+}$ is essential in the component of $\M \cut T_{+}$ it lies in. Then $S$ is essential in $\M$.

\end{lemma}

\begin{proof} Since $S$ may be non-orientable we will work with the orientable double
$\widetilde {S}= \partial (S \times I)$.  By way of contradiction, suppose that  
$\widetilde {S}$  is not $\pi_1$-injective. This means that $\widetilde {S}$  is either compressible or
$\partial$-compressible. Since $\partial \M$ consists of tori, incompressibility implies $\partial$-incompressibility
\cite{Ha}. Thus we may assume that there is a compression disk $(E, \partial E)\subset (\M, \widetilde {S})$. Since each component of $\widetilde {S}\cut T_{+}$ is incompressible, the intersection $E\cap T_{+}$
must be non-empty. Since $T_{+}$ is essential (and thus incompressible in $\M$) we may eliminate the closed components of $E\cap T_{+}$. Thus we may assume that each component of $E\cap T_{+}$
is an arc properly embedded in $E$. By further isotopy of $E$, during which $\partial E$  moves on
$\widetilde {S}$, we may assume that the intersection $E\cap T_{+}$ is minimal. Now let $\alpha$ be a component
of $E\cap T_{+}$ that is outermost on $E$: It cuts off a disc $E'\subset E$ whose interior contains no further intersections 
with $T_{+}$. Now $\partial E'$ consists of $\alpha$ and an arc $\beta$ that is properly embedded on a component,
say $\Sigma$,
of $\widetilde {S}\cut T_{+}$.  We can use  disk $E'$ to isotope  $\beta$, relatively $\partial \beta$,
on $T_{+}$; this isotopy takes place in  $\M \cut T_{+}$.
Since $\Sigma$ is essential in the component of $\M \cut T_{+}$ 
it lies in, we conclude that the arc $\beta$ may be isotopied on $\Sigma$, relatively $\partial \beta$,
to an arc on $\partial \Sigma$.  This follows from Lemma \ref{basic}. But this isotopy will reduce the components of the intersection  $E\cap T_{+}$, contradicting our assumption of minimality. Thus  $\widetilde {S}$
must be incompressible and therefore, by above discussion,  essential  in $\M$.
\end{proof}

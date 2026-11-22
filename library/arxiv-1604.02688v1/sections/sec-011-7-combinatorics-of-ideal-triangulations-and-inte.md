---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-011-7-combinatorics-of-ideal-triangulations-and-inte
section_title: "Combinatorics of ideal triangulations and integer normal surface theory"
section_number: 7
pages: 16-19
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.963
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
\label{ZNST}

The work of Kang-Rubinstein and Luo-Tillmann, described above, shows that 
the edge solutions and tetrahedral solutions 
span the real vector space $N(\T;\R) \subset \R^{3n}$ of closed normal 
classes, and that these together with the 
peripheral curve solutions span the real vector space 
$Q(\T;\R) \subset \R^{3n}$ of all $Q$-normal classes.
However, over the integers the situation is more subtle --- the integer 
linear combinations of edge and tetrahedral solutions generally give only 
a finite index submodule of $N(\T;\Z)$ and the integer linear combinations 
of edge, tetrahedral and peripheral curve solutions  give a finite index 
submodule of $Q(\T;\Z)$. In this section we give a precise 
description of these integer classes. It turns out that this is a 
consequence of the results of Neumann  \cite{N} on combinatorics of ideal 
triangulations.

We regard a $Q$-normal class  as a linear combination of quads in 
$\T$ satisfying the $Q$-matching equations of Tollefson \cite{To}. 
Explicitly, let $\Z E \cong \Z^n$ and $\Z\quads \cong \Z^{3n}$ 
denote the free $\Z$-modules with bases given by the (unoriented) edge 
classes and quad types in $\T$ respectively. Given a quad $q_\sigma$ in an 
oriented tetrahedron $\sigma$ of $\T$ we associate a sign $\pm 1$ to each 
of the edges of $\sigma$ meeting $q_\sigma$ as shown in 
figure \ref{twisted_octagon}. (These signs give the shear parameters 
along the edges as explained in Section \ref{spun_normal_construction}.)
Adding these contributions gives a linear map 
\be
\label{Qmatching_map}
F: \Z\quads \to \Z E
\ee
whose kernel is the submodule $Q(\T;\Z)$ of $Q$-normal classes.

\begin{figure}[htpb]
\begin{center}
\includegraphics[width=0.26\textwidth]{figures/quadWithOrientation} 
\hspace{1cm}
\includegraphics[width=0.26\textwidth]{figures/twistedSquare} 
\hspace{1cm}
\includegraphics[width=0.26\textwidth]{figures/twistedOctagon}
\end{center}
\caption{Each quad can be replaced by a twisted square or twisted octagon.}
\label{twisted_octagon}
\end{figure}

Kang-Rubinstein \cite{KR1} observed that for each edge class  in $\T$, the 
sum of all quad types facing the edges in this class gives an 
``edge solution''  in $Q(\T;\Z)$; this gives a linear map 

\be 
\label{edge_solution_map}
G: \Z E \to \Z\quads 
\ee 
with image contained in $Q(\T;\Z)$.
Further, the sum of the three quad types in a tetrahedron in $\T$ gives a 
``tetrahedral solution'' in $Q(\T;\Z)$. We let 
$\EE,\TT \subset Q(\T;\Z) \subset \Z\quads$ denote the $\Z$-submodules 
spanned by the edge solutions and tetrahedral solutions respectively, and 
let $Q_0(\T;\Z)$ denote the submodule $\EE+\TT  \subset Q(\T;\Z)$.

Next we associate two important homology (or cohomology) classes with any 
$Q$-normal class. First observe that any quadrilateral in a tetrahedron can 
be replaced by a `twisted square' meeting the same edges, or by a 
`twisted octagon' in the corresponding truncated tetrahedron with its 
four external edges oriented as shown in Figure \ref{twisted_octagon} 
(compare \cite[Figures 9, 10]{N}). Note that the arrow on each external 
edge goes from an internal edge labelled $+1$ to an internal edge labelled $-1$.

Each spun normal class $S \in Q(\T;\Z)$ is a linear combination of quads, so 
we can replace this by a linear combination $S'$ of twisted octagons. It 
follows from the $Q$-matching equations that  $S'$ represents a mod 2 
homology class $[S]_2 \in H_2(M,\bd M; \Z/2\Z)$. Here and throughout the 
paper, we will use $[~]_2$ to indicate a $\Z/2\Z$ homology (or co-homology) 
class. Further, the boundary edges of $S'$, oriented as above, represent 
a homology class $[\bd S] \in H_1(M;\Z)$. In particular, the kernel of the 
boundary map $S \mapsto [\bd S]$ is precisely the  submodule 
$N(\T;\Z) \subset Q(\T;\Z)$ of {\em  closed} normal classes. 

When $S$ gives an embedded spun normal surface,  $[\bd S]$ agrees with 
boundary map defined by Tillmann in \cite{Ti} (up to sign), and describes 
the boundary components of the spun normal surface and the direction of 
spiralling of the spun normal surface around $\bd M$.  (With the 
orientation convention given in Figure \ref{twisted_octagon}, the ends of 
a spun normal surface spiral up into the cusp to the {\em right} of the 
oriented boundary curve, as viewed from the cusp.)

Since $S'$ gives a 2-chain mod 2 whose boundary represents the reduction of 
$[\bd S]$ mod 2, it follows that 
$$
([S]_2,[\bd S]) \in \{ (a,b) \in  H_2(M,\bd M;\Z/2\Z) \times H_1(\bd M;\Z) : 
\bd_* a =   b \bmod 2  \}
$$
where $\bd_*: H_2(M,\bd M;\Z/2\Z) \to H_1(\bd M;\Z/2\Z) $ is the connecting 
homomorphism in the long exact sequence of the pair $(M, \bd M)$.   
Hence, $[\bd S] \in {\mathcal K} =\Ker(H_1(\bd M;\Z) \to H_1(M;\Z/2\Z))$, 
by the long exact sequence of the pair $(M,\bd M)$ with $\Z/2\Z$ coefficients.

\begin{thm} 
\label{ZQNT_struct_thm}
The homomorphism 
$$
H:  Q(\T;\Z) \to H_2(M,\bd M;\Z/2\Z) \times H_1(\bd M;\Z),~ S 
\mapsto ([S]_2,[\bd S])
$$
has image 
$$
\Im H =\{ (a,b) \in H_2(M,\bd M;\Z/2\Z) \times  H_1(\bd M;\Z) :  
\bd_* a =  b \bmod 2 \}
$$
and kernel
$$
\Ker H = Q_0(\T;\Z) = \EE + \TT.
$$
In particular, the homomorphism
$$
H_0:  N(\T;\Z) \to  H_2(M,\bd M;\Z/2\Z),~ S \mapsto [S]_2
$$
has image
$$
\Im H_0 = \Ker( H_2(M,\bd M;\Z/2\Z) \to H_2(\bd M;\Z/2\Z)) 
=  \Im ( H_2(M;\Z/2\Z) \to H_2(M,\bd M;\Z/2\Z) )
$$
and kernel
$$
\Ker H_0 =Q_0(\T;\Z)= \EE + \TT.
$$
\end{thm}

\begin{proof} 
This essentially follows from Neumann \cite[Theorem 5.1]{N} together with 
Poincar\'e duality. To match Neumann's notation from sections 4--6 
of \cite{N} we let $K$ denote the oriented pseudo-manifold given by the 
triangulation $\T$ with its ideal vertices included.
Thus $K$ is homeomorphic to the end compactification $\hat M$ of the 
$\text{int} M$, obtained by collapsing each component of  $\bd M$
to a separate point. Truncating the corners of the tetrahedra in $K$ gives 
a cell complex $K_0$ homeomorphic to $M$ with boundary
$\bd K_0$ homeomorphic to $\bd M$. 

Let  $C_0 =\Z V \cong \Z^r , C_1=\Z E \cong \Z^n ,  
\overline{J}=\Z \quads \cong\Z^{3n}$  be the free $\Z$-modules 
with bases given by the cusps, (unoriented) edge classes, and quad types 
in $\T$ respectively, and let $\EE, \TT\subset \Z \quads$ denote the 
$\Z$-submodules spanned by the edge solutions and  tetrahedral solutions
respectively.  Then Neumann defines a chain complex
$$
0 \to C_0  \xrightarrow{\alpha} C_1  \xrightarrow{\beta}  J  
\xrightarrow{\beta^*}  C_1  \xrightarrow{\alpha^*}  C_0 \to 0
$$
where $J= \Z \quads/\TT \cong \Z^{2n}$, $\alpha$ gives the sum of all 
edges incident to a vertex, $\alpha^*$ is a map that associates to an 
edge the sum of its endpoints, and $\beta$ and $\beta^*$ are defined so 
that the following diagram commutes:

\begin{center}
\begin{tabular}{c}
\xymatrix{
& \overline{J}= \Z\quads \ar[dd]_\pi \ar[dr]^F &\\
C_ 1= \Z\EE  \ar[ur]^G \ar[dr]_\beta & & C_ 1= \Z\EE\\
&J=\Z\quads/\TT \ar[ur]_{\beta^*} & 
}
\end{tabular}
\end{center}

Here, $\pi: \Z\quads  \rightarrow  \Z\quads/\TT$ is the quotient map.

To relate this  to integer  $Q$-normal surface theory we observe that 
$\Ker \beta^* = Q(\T;\Z)/\TT$ and $\Im \beta = (\EE + \TT)/\TT$.

Now Neumann's Theorem 5.1 gives an isomorphism from 
$\Ker \beta^*/\Im \beta = Q(\T;\Z)/(\EE + \TT)$ to
$$
\{ (f,g) \in  H^1(M;\Z/2\Z) \times H^1(\bd M;\Z)  :   i^* f =  g \bmod 2 \}
$$
where 
$i^*: H^1(M;\Z/2\Z) \to H^1(\bd M;\Z/2\Z) $ is induced by the inclusion 
map $i: \bd M \to M$. In other words, this is the set of pairs
$(f,g)$ with $f \in \Hom(H_1(M),\Z/2\Z)$, $g \in \Hom(H_1(\bd M),\Z)$, 
such that $f(\gamma) =g(\gamma) \bmod 2$  for all $ \gamma \in H_1(\bd M)$,
where we write  $H_1(\bd M)= H_1(\bd M; \Z)$ and $H_1(M)= H_1(M; \Z)$. 

Now we have a commutative diagram
$$
\begin{CD}
H^1(M,\bd M;\Z/2\Z) @>j^*>> H^1(M;\Z/2\Z) @>i^*>> H^1(\bd M;\Z/2\Z) \\
@VV\cong V                      @VV\cong V     @VV\cong V          \\
H_2(M;\Z/2\Z) @>j_*>> H_2(M,\bd M; \Z/2\Z)  @>\bd_*>>   H_1(\bd M; \Z/2\Z)
\end{CD}
$$
where the vertical maps are the isomorphisms given by Poincar\'e duality.
This gives an isomorphism 
$$
Q(\T;\Z)/(\EE + \TT) \cong \{ (a,b) \in  H_2(M,\bd M;\Z/2\Z) 
\times H_1(\bd M;\Z) : \bd_* a =   b\bmod 2  \}
$$
where 
$\bd_*: H_2(M,\bd M;\Z/2\Z) \to H_1(\bd M;\Z/2\Z) $ is the connecting 
homomorphism in the long exact sequence of the pair $(M, \bd M)$. 
A careful examination of Neumann's work shows that this isomorphism
is given by the homology map $H :S \mapsto ([S]_2,[\bd S])$ defined above.  
\end{proof}

\begin{rmk} 
Using Poincar\'e duality and the Mayer-Vietoris sequence it follows that
\begin{align*}
\Im H_0 &= \Im ( H_2(M;\Z/2\Z) \to H_2(M,\bd M;\Z/2\Z)) \\ 
&\cong \Ker (H^1(M;\Z/2\Z) \to H^1(\bd M; \Z/2\Z)) \cong H^1(\hat M; \Z/2\Z).
\end{align*}
where $\hat M$ is the pseudo-manifold given by the triangulation $\T$ 
with its ideal vertices included; thus $\hat M$ is homeomorphic to $M$ with 
a cone attached over each boundary torus.
\end{rmk}

\begin{rmk}
When $M$ has no non-peripheral $\Z/2\Z$ homology (for example, if $M$ is 
a knot or link exterior in a $\Z/2\Z$ homology sphere), then 
$Q_0(\T;\Z) = N(\T;Z)$  consists of all closed normal classes.
Further, ${\mathcal K} =\Ker(H_1(\bd M;\Z) \to H_1(M;\Z/2\Z))$ is a 
subgroup of index $2^r$ in $H_1(\bd M;\Z)$ where $r$ is the number of 
components of $\bd M$.

In general, $Q_0(\T;\Z)$ is a finite index submodule of $N(\T;Z)$, and for 
any normal surface class $S \in N(\T;Z)$
its ``double'' $2S$ lies in $Q_0(\T;\Z)$.
\end{rmk}

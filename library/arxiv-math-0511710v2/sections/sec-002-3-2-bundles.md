---
doc_id: arxiv-math-0511710v2
doc_title: "Higher gauge theory"
section_id: sec-002-3-2-bundles
section_title: "2-Bundles"
section_number: 3
pages: 13-19
source_pdf: 0511710v2.pdf
source_sha256: f88f50d459080490
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.942
doc_brief: "Higher gauge theory — Just as gauge theory describes the parallel transport of point particles using connections on bundles, higher gauge theory describes the parallel transport of 1-dimensional"
---
\label{section: 2-Bundles}

In differential geometry an
ordinary bundle consists of two smooth spaces, the {\bf total space}
$E$ and the {\bf base space} $B$, together with a {\bf projection map} 
\[
  E \stackto{p} B
  \,.
\]
To categorify the theory of bundles, we start by replacing smooth spaces by 
smooth 2-spaces:

\begin{definition} \et
  \label{2-bundle}
  A {\bf 2-bundle} consists of
  \begin{itemize}
    \item
      a smooth 2-space $E$ (the {\bf total 2-space}),
    \item
      a smooth 2-space $B$ (the {\bf base 2-space}),
    \item
      a smooth map $p \maps E \to B$ 
      (the {\bf projection}).
  \end{itemize}
\end{definition} 

In gauge theory we are interested in \emph{locally trivial} 2-bundles. 
Ordinarily, a locally trivial
bundle with fiber $F$ is a bundle $E \stackto{p} B$ together with an open
cover $U_i$ of $B$, such that the restriction of $E$ to any of the $U_i$ 
is equipped with an isomorphism to the trivial bundle $U_i \times F \to U_i$. 
To categorify this, we would need to define a `2-cover' of the base 2-space 
$B$.  This is actually a rather tricky issue, since forming the `union' of 
2-spaces requires knowing how to compose a morphism in one 2-space
with a morphism in another.  While this issue can be addressed, we prefer 
to avoid it here by assuming that $B$ is just an ordinary smooth space,
regarded as a smooth 2-space with only identity morphisms.

We can now state the definition of a
locally trivial 2-bundle.  First note that we can restrict a
2-bundle $E \stackto{p} B$ to any subspace $U \subseteq B$
to obtain a 2-bundle which we denote by $E|_U \stackto{p} U$.  Then:

\begin{definition} \et
\label{2-bundle with local trivialization}
Given a smooth 2-space $F$, we define a {\bf locally trivial 2-bundle 
with fiber $F$} to be a 2-bundle $E \stackto{p} B$ and an open cover 
$\{U_i\}$ of the base space $B$ 
equipped with equivalences 
  \[
    E|_{\twoU_i} \stackto{t_i} \twoU_i \times \twoF
  \]
called {\bf local trivializations} such that these diagrams: 
\[ 
\xymatrix @!0
{ E|_{\twoU_i}
 \ar [dddrr]_{p}
  \ar[rrrr]^{t_i} 
  & &  & &
  U_i \times F
  \ar[dddll]^{}
  \\ \\ &  \\ & &
   U_i 
 }
\]
commute for all $i \in I$.
\end{definition}
Readers wise in the ways of categorification \cite{BaezDolan:1998} may 
ask why we did not require that these diagrams commute {\it up to 
natural isomorphism}.  The reason is that $U_i$, as an ordinary space, has
only identity morphisms when we regard it as a 2-space.  Thus, for
this diagram to commute up to natural isomorphism, it must commute
`on the nose'. 

Readers less wise in the ways of categorification may find the
above definition painfully abstract.  So, let us translate it
into data that specify how to build a locally trivial 2-bundle
from trivial ones over the patches $U_i$.  For this, 
we need to extract \emph{transition functions} from the local 
trivializations.

So, suppose $E \stackto{p} B$ is a locally trivial 2-bundle with 
fiber $F$.  This means that $B$ is equipped with an 
open cover $U$ and for each open set $U_i$ in the cover
we have a local trivialization 
\[   t_i \maps  E|_{U_i} \to \twoU_i \times \twoF \]
which is an equivalence.  This means
that $t_i$ is equipped with a specified map
\[   \bar t_i  \maps \twoU_i \times \twoF \to E|_{\twoU_i} \]
together with invertible 2-maps
\[  
\begin{array}{ccl}
   \tau_i \maps \bar t_i t_i &\To& 1  \\
   \bar \tau_i \maps t_i \bar t_i &\To& 1   
\end{array}
\] 
In particular, this means that $\bar t_i$ is also an equivalence.

Now consider a double intersection $U_{ij} = U_i \cap U_j$.
The composite of equivalences is again an equivalence, so
we get an {\bf autoequivalence}
\[
t_j \bar t_i
\maps U_{ij}\times \twoF \to U_{ij}\times \twoF
\]
that is, an equivalence from this 2-space to itself.
By the commutative
diagram in \refdef{2-bundle with local trivialization}, this
autoequivalence 
must act trivially on the $U_{ij}$ factor, so 
\[
  t_j \bar t_i(x,f) = (x,f g_{ij}(x)) 
\]
for some smooth function $g_{ij}$ from $U_{ij}$ to the 
smooth space of autoequivalences of the fiber $F$.  
Note that we write these autoequivalences as acting on 
$F$ from the right, as customary in the theory of bundles.
We call the functions $g_{ij}$ {\bf transition functions}, since they
are just categorified versions of the usual transition functions 
for locally trivial bundles.  

In fact, for any smooth 2-space $F$ there is a smooth 2-space $\AUT(F)$ 
whose objects are autoequivalences of $F$ and whose morphisms are 
invertible 2-maps between these.  The transition functions are maps
\[     g_{ij} \maps U_{ij} \to \Ob(\AUT(F))  .\]
The 2-space $\AUT(F)$ is a kind of 2-group, with composition of
autoequivalences giving the product.  However, is not the sort of
2-group we have been considering here, because it does not have
`strict inverses': the group laws involving inverses do not hold as
equations, but only up to specified isomorphisms that satisfy
coherence laws of their own.  So, $\AUT(F)$ is a `coherent' smooth
2-group in the sense of Baez and Lauda \cite{BaezLauda:2003}.

Next, consider a triple intersection $U_{ijk} = U_i \cap U_j \cap U_k$.
In an ordinary locally trivial bundle the transition functions satisfy 
the equation $g_{ij} g_{jk} = g_{ik}$, but in a locally trivial 
2-bundle this holds {\it only up to isomorphism}.  In other
words, there is a smooth map 
\[    h_{ijk} \maps U_{ijk} \to \Mor(\AUT(F))  \]
such that for any $x \in U_{ijk}$, 
\[    h_{ijk}(x) \maps g_{ij}(x) g_{jk}(x) \stackto{\sim} g_{ik}(x) . \]
To see this, note that there is an invertible 2-map
\[ t_k \tau_j \bar t_i \, \maps \,
t_k \bar t_j t_j \bar t_i \To t_k \bar t_i  \]
defined by horizontally composing $\tau_j$ with $t_k$ on the left
and $\bar t_i$ on the right.   Since
\[   t_k \bar t_j t_j \bar t_i(x,f) = (x,fg_{ij}(x)g_{jk}(x)) \]
while
\[     t_k \bar t_i(x,f) = (x, f g_{ik}(x))  \]
we have
\[ t_k \tau_j \bar t_i (x,f) \maps 
(x, fg_{ij}(x)g_{jk}(x)) \to (x,fg_{ik}(x)).\]
Since this morphism must be the identity on the first factor,
we have
\[ t_k \tau_j \bar t_i (x,f) = (1_x, f h_{ijk}(x)) \]
where $h_{ijk}(x) \maps g_{ij}(x) g_{jk}(x) \to g_{ik}(x)$ depends
smoothly on $x$. 

Similarly, in a locally trivial bundle we have
$g_{ii} = 1$, 
but in a locally trivial 2-bundle there is a smooth map
\[    k_i \maps U_i \to \Mor(\AUT(F))  \]
such that for any $x \in U_i$,
\[    k_i(x) \maps g_{ii}(x) \to 1  .\]
To see this, recall that there is an invertible 2-map
\[     \bar\tau_i \maps t_i \bar t_i \To 1 . \]
Since
\[   t_i \bar t_i(x,f) = (x, f g_{ii}(x)) \]
we have
\[ \bar \tau_i (x,f) \maps (x, f g_{ii}(x)) 
\to (x,f) , \]
and since this morphism must be the identity on the first factor,
we have
\[ \bar \tau_i (x,f) = (1_x, f k_i(x)) \]
where $k_i(x) \maps g_{ii}(x) \to 1$ depends smoothly on $x$. 

In short, the transition functions $g_{ij}$ for a locally trivial 2-bundle
satisfy the usual cocycle conditions up to specified isomorphisms
$h_{ijk}$ and $k_i$, which we call {\bf higher transition functions}.
These, in turn, satisfy some cocycle conditions of their own: 

\begin{theorem} \et 
\label{2-bundle cocycle conditions} 
Suppose $E \stackto{p} B$ is a locally trivial 2-bundle, 
and define the transition functions 
$g_{ij}, h_{ijk}$, and $k_i$ as above.  Then:

\begin{itemize}
\item
$h$ makes this diagram,
called the {\bf associative law},
commute for any $x \in U_{ijkl}$:
\[
\xy
 (0,20)*+{g_{ij}(x)\, g_{kl}(x) \, g_{lm}(x) }="T";
 (-20,0)*+{g_{il}(x)\, g_{lm}(x)}="L";
 (20,0)*+{g_{ij}(x)\, g_{jm}(x)}="R";
 (0,-20)*+{g_{im}(x)}="B";
 (-7,0)*{}="ML";
 (7,0)*{}="MR";
     {\ar^{g_{ij}(x) \, h_{jkl}(x)} "T";"R"};
     {\ar_{h_{ijk}(x) \, g_{kl}(x)} "T";"L"};
     {\ar^{h_{ijl}(x)} "R";"B"};
     {\ar_{h_{ikl}(x)} "L";"B"};

\endxy
\]

\item 
$k$ makes these diagrams, 
called the {\bf left and right unit laws}, 
commute for any $x \in U_{ij}$:
\[
\xy
  (-36,5)*+{g_{ii}(x) \, g_{ij}(x) }="L";
  (0,5)*+{1 \, g_{ij}(x)}="M";

  (0,-18)*+{g_{ij}(x)}="B";
  (-5,2)*{}="TL";
  (5,2)*{}="TR";
  (10,-4)*{}="BR";
  (-10,-4)*{}="BL";
     {\ar^{k_i(x) \, g_{ij}(x)} "L";"M"};

     {\ar^{=} "M";"B"};
     {\ar_{h_{iij}(x)} "L";"B"};



\endxy
\qquad
\xy

  (0,5)*+{g_{ij}(x) \, 1}="M";
  (36,5)*+{g_{ij}(x) \, g_{jj}(x)}="R";
  (0,-18)*+{g_{ij}(x)}="B";
  (-5,2)*{}="TL";
  (5,2)*{}="TR";
  (10,-4)*{}="BR";
  (-10,-4)*{}="BL";

     {\ar_{g_{ij}(x) \, k_j(x)} "R";"M"};
     {\ar_{=} "M";"B"};

     {\ar^{h_{ijj}(x)} "R";"B"};


\endxy
\]
\end{itemize}
\end{theorem}

\Proof  
Checking that these diagrams commute is a straightforward 
computation using the definitions of $g,h$, and $k$ in 
terms of $t,\bar t$, $\tau$ and $\bar \tau$.  
\endofproof

The associative law and unit laws are analogous to those which hold 
in a monoid.  They also have simplicial interpretations.  
In a locally trivial bundle, the transition functions
give a commuting triangle for any triple intersection:
\begin{center}
  \begin{picture}(100,85)
  \includegraphics{triangle.eps}
  \put(-80,40){$g_{ij}$}
  \put(-24,40){$g_{jk}$}
  \put(-50,-7){$g_{ik}$}
  \end{picture}
\end{center}
\vskip 2em 
In a locally trivial 2-bundle, such triangles commute only
up to isomorphism:
\begin{center}
 \begin{picture}(100,85)
  \includegraphics{triangle_filled.eps}
  \put(-120,0){}
  \put(-60,80){}
  \put(2,0){}
  \put(-80,40){$g_{ij}$}
  \put(-24,40){$g_{jk}$}
  \put(-50,-7){$g_{ik}$}
  \put(-70,24){$h_{ijk}$}
  \end{picture}
  \vskip 1em
\end{center}
However, the associative law says that for each quadruple 
intersection, this tetrahedron commutes:
\begin{eqnarray*}
\begin{picture}(140,160)
  \includegraphics{tetrahedron.eps}
  \put(-127,46){${}_{g_{ij}}$}
  \put(-53,46){${}_{g_{jk}}$}
  \put(-90,-3){$g_{ik}$}
  \put(-137,80){$g_{il}$}
  \put(-41,80){$g_{kl}$}
  \put(-82,105){${}_{g_{jl}}$}

  \put(-80,22){$h_{ijk}$}
  \put(-82,47){$h_{ikl}$}
  \put(-68,85){${}_{h_{jkl}}$}
  \put(-112,85){${}_{h_{ijl}}$}
\end{picture}
\end{eqnarray*}

\vskip 1em \noindent

\noindent
We can also visualize the left and right unit laws simplicially,
but they involve degenerate tetrahedra:

\begin{center}
\begin{picture}(230,180)
\includegraphics{unitcoherence.eps}
\put(0,0){}
\put(-45,-6){$g_{ij}$}
\put(-190,-6){$g_{ij}$}
\put(-45,100){$g_{ij}$}
\put(-190,100){$g_{ij}$}
\put(-20,145){$g_{ij}$}
\put(-161,145){$g_{ij}$}
\put(-71,35){$g_{ij}$}
\put(-215,35){$g_{ij}$}
\put(-75,145){$g_{ii}$}
\put(-224,145){$g_{ii}$}
\put(-200,144){$k_i$}
\put(-193,129){$1$}
\put(-176,122){$1$}
\put(-117,130){$=$}
\put(-55,120){$h_{iij}$}
\put(-117,20){$=$}
\put(-16,35){$g_{jj}$}
\put(-149,35){$g_{jj}$}
\put(-172,39){$k_j$}
\put(-175,20){$1$}
\put(-194,15){$1$}
\put(-52,13){$h_{ijj}$}
\end{picture}
\end{center}

We are now almost in a position to define $\twogroup$-2-bundles 
for any smooth 2-group $\twogroup$; we only need to understand
how a 2-group can `act' on a 2-space.  For simplicity we only
consider the case of a strict action:

\begin{definition} \et 
A {\bf (strict) action} of a smooth 2-group 
$\twogroup$ on a smooth 2-space $F$ is a smooth homomorphism
\[    \alpha \maps \twogroup \to \AUT(F) , \]
that is, a smooth map that preserves products and inverses.
\end{definition}

\noindent
Note in particular that every smooth 2-group has an action on itself
via right multiplication.

\begin{definition} \et
For any smooth 2-group $\twogroup$, we say a locally trivial
2-bundle $E \to M$ has $\twogroup$ as its {\bf structure 
2-group} when the transition functions $g_{ij}$, $h_{ijk}$, and 
$k_i$ factor through an action $\twogroup \to \AUT(F)$.  In this case we 
also say $P$ is a {\bf $\twogroup$-2-bundle}.
If furthermore $F = \twogroup$ and $\twogroup$ acts on $F$ by right
multiplication, we say $P$ is a {\bf principal $\twogroup$-2-bundle}.  
\end{definition}

For a principal $\twogroup$-2-bundle we can think of the transition 
functions as taking values in the groups $\Ob(\twogroup)$ and 
$\Mor(\twogroup)$.  The reader familiar with 
gerbes will note that these functions, satisfying the equations they do, 
reduce to the usual sort of cocycle defining an 
\emph{abelian gerbe} when $k_i = 1$ and $\twogroup$ has
the special form described in Example \ref{crossed.1}.  Similarly, 
they reduce to a cocycle defining a \emph{nonabelian gerbe}
when $k_i = 1$ and $\twogroup$ has the form described in 
Example \ref{crossed.2}.  Thus there is a close relation between
principal 2-bundles and gerbes, much like that between principal
bundles and sheaves of groups.

The equation $k_i = 1$ arises because gerbes 
are often defined using {\v C}ech cocycles that are antisymmetric 
in the indices $i,j,k,\dots,$ in the sense that group-valued functions 
go to their inverses upon an odd permutation of these indices.  Thus in 
this context $g_{ii} = 1$, and one implicitly assumes $k_i = 1$.    
In fact, Bartels \cite{Bartels:2004} has shown that every 
$\twogroup$-2-bundle is equivalent to one with $k_i = 1$.  To 
state this result, he first needed to define a 2-category of 
$\twogroup$-2-bundles.  This 2-category is equivalent to the 
2-category of abelian or nonabelian gerbes when $\twogroup$ has 
one of the two special forms mentioned above.

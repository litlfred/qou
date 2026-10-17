---
doc_id: arxiv-1608.07234v3
doc_title: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS"
section_id: sec-003-4-iwahori-hecke-algebra
section_title: "Iwahori-Hecke algebra"
section_number: 4
pages: 26-31
source_pdf: 1608.07234v3.pdf
source_sha256: 311730670d2fdcb7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.833
latex_coverage_ratio: 0.943
doc_brief: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS — We describe a graded extension of the usual Hecke algebra: it acts in a graded fashion on the cohomology of an arithmetic group Γ."
---
\label{IHA}
 In this section, we collect a few important facts about Iwahori--Hecke algebras. 
In particular, we discuss the structure of the Iwahori--Hecke algebra at a Taylor--Wiles prime (\S \ref{Iwahori}), the
relation between modules over the (usual, i.e. non-derived) Iwahori-Hecke algebra
and modules over the (usual) spherical Hecke algebras (\S \ref{IwahoriHecke})
and finally briefly discuss a localization result for the derived Iwahori-Hecke algebra
(\S \ref{dhLocalization}). 

 These results are presumably well-known to experts
but they help us polish our presentation of the Taylor-Wiles method -- indeed similar ideas appear in the paper of Khare and Thorne \cite{KT}.



\subsection{} 
 
 We continue with the notation of the prior section (\S \ref{BasicNotn}). 
 In particular, $G_v$ is the $F_v$-points of a reductive split group. 
 
 In this section, we will also make use of the affine Weyl group $\tilde{W}$ attached to $\mathbf{G}$; by definition
  \index{$\tilde{W}$} 
 this is the semidirect product $X_*  \rtimes W$  where $X_*$ is the cocharacter group of  the maximal torus $\mathbf{A}$,
 and $W$ is the Weyl group of $\mathbf{A}$. 
 
 Let $S$ be the ring $\Z/\ell^r$, for a prime $\ell$; this will be the coefficient ring for all our Hecke algebras and derived Hecke algebras.    We suppose that $q_v \equiv 1$ modulo $\ell^r$
 and that $\ell$ doesn't divide the order of the Weyl group.  

{\color{\changecolor} Let $I_v$ be an Iwahori subgroup of $G_v$ contained inside $K_v$ and in good position with reference to $\mathbf{A}$.  By this we mean that $I_v$ stabilizes
a chamber of the building that lies inside the apartment defined by $\mathbf{A}$. 
 An explicit choice of such an $I_v$ can be obtained from an integral model $\mathcal{B}$ of a Borel subgroup containing $\mathbf{A}$:
$$ I_v = \mbox{preimage of $\mathcal{B}(\mathbf{F}_v)$ inside $\mathcal{G}(\mathcal{O}_v)$,}$$
and the other such $I_v$s are $W$-conjugate to this one. }

It will be helpful to keep in mind that the index $[K_v:I_v] \equiv |W|$ modulo $\ell^r$, in particular, this index is invertible in $S$.
  Take the Haar measure on $G_v$ which assigns $I_v$ mass $1$.

  


 
\subsection{The structure of the Iwahori algebra} \label{Iwahori}   
   {\color{\changecolor} Let $\mathrm{H}_I$ be the Hecke algebra for $I_v$.
   We will understand this to be defined as
   $$ \mathrm{H}_I  := \Hom_{SG_v}(S[G_v/I_v], S[G_v/I_v]).$$

This is identified with the 
set of
 $S$-valued and finitely supported functions $f$  on $I_v \backslash G_v/I_v$. Namely, 
 identifying such functions with measures (multiplying by the Haar measure on $G_v$, thought
 of as valued in $S$), each such 
function $f$ acts by right convolution on $S[G_v/I_v]$, and therefore defines an element of $\mathrm{H}_I$. 
\index{$\mathrm{H}_K$} \index{$\mathrm{H}_{IK}$} \index{$\mathrm{H}_{KI}$} \index{$\mathrm{H}_{II}$} 
Therefore, in the text, we will often produce elements of $\mathrm{H}_I$ by describing
the associated bi-invariant function. 

{\em Warning:} the resulting identification
\begin{equation} \label{left right sequel} \mathrm{H}_I \simeq \left(\mbox{functions on $I_v \backslash G_v/I_v$} \right)\end{equation}
is an anti-isomorphism of algebras if we equip the right-hand side with the convolution product.  
When we multiply elements of $\mathrm{H}_I$, we will always understand the multiplication to be that of $\mathrm{H}_I$,
not the multiplication induced from the right hand side of \eqref{left right sequel}. 

We similarly define 
\begin{eqnarray*} \label{HKIdef} \mathrm{H}_K  =  \Hom_{SG_v}(S[G_v/K_v], S[G_v/K_v]), \\
 \mathrm{H}_{IK} = \Hom_{SG_v} (S[G_v/K_v], S[G_v/I_v]), \\ 
  \mathrm{H}_{IK} = \Hom_{SG_v} (S[G_v/I_v], S[G_v/K_v]).
\end{eqnarray*}

If $V$ is any $G$-representation, the algebra  $ \Hom_{SG_v}(S[G_v/K_v], S[G_v/K_v])$ 
acts on the right on $V^{K_v} = \Hom_{G_v}(S[G_v/K_v], V)$. Similarly, elements $\mathrm{H}_{IK}$
induces endomorphisms  $V^{I_v} \rightarrow V^{K_v}$. 
Indeed a useful mnemonic for    the subscript ``$IK$''  is that,  acting as explained above,   $\mathrm{H}_{IK}$ goes from $I$-invariants to $K$-invariants, and so on.
Also   $\mathrm{H}_{IK}, \mathrm{H}_{KI}$  are bimodules for $\mathrm{H}_K$ and $\mathrm{H}_I$. 


As before, each of these can be identified with a space of functions. Thus, for example, 
 \begin{eqnarray} \label{leftright2} \mathrm{H}_{IK} \simeq \mbox{functions on $K_v \backslash G_v/I_v$},    \end{eqnarray}
 and similarly for $\mathrm{H}_{IK}, \mathrm{H}_K$. 
As before, these identifications  arise  from the right convolution action of the functions
  on $S[G_v/K_v]$ or $S[G_v/I_v]$.  
  
 Note that, somewhat contrary to what the notation might suggest,  an element of $\mathrm{H}_{IK}$
  considered as a function is {\em left} $K_v$-invariant and {\em right} $I_v$-invariant.         Again, we will use these identifications such as \eqref{leftright2} without comment to produce
  elements inside the various Hecke algebras. The same warning applies here: the identifications do not preserve multiplication; the order
  must be switched, just as \eqref{left right sequel} is an anti-automorphism.  To avoid confusion here, our convention is that products are always to be understood
  in the sense of the $\mathrm{H}_I, \mathrm{H}_K$, etc., and {\em not} via convolution of functions. 
 

  

  

  
  
It is useful later to define  
\begin{equation} \label{eK definition} e_K = \frac{1_{K_v}}{\mathrm{measure}(K_v)}.\end{equation}
Considered as an element of $\mathrm{H}_I$ it  is idempotent. 
When  considered as an element of $\mathrm{H}_{IK}$, it carries the identity coset of $S[G_v/K_v]$ to 
  $\sum_{k \in K/I} k I_v \in S[G_v/I_v]$, and when considered as an element of $\mathrm{H}_{KI}$, carries the identity coset of $S[G_v/I_v]$
  to $\frac{1}{[K_v:I_v]} eK_v \in S[G_v/K_v]$. In particular, $e_K \in \mathrm{H}_{IK}$ induces the co-restriction  map $V^{I_v} \rightarrow V^{K_v}$,
  and $e_K \in \mathrm{H}_{KI}$ induces the map $V^{K_v} \rightarrow V^{I_v}$ which is the natural inclusion divided by the index $[K_v:I_v]$. 
   }
  
  
 











 \begin{comment}
\begin{remark}
There are some confusing left/right issues  that arise here. 

 If $V$ is any $G$-representation, 
 the algebras $\mathrm{H}_K$, considered as convolution algebras of measures,
act on the {\em left} on  $V^{K_v}$.    Correspondingly the  map \eqref{left right} is not an algebra identification, but rather
an anti-homomorphism: it identifies one side with the opposite algebra of the other.
As a final point of confusion, the induced actions of the two sides of \eqref{left right} on $V^{K_v}$ do not coincide,
but rather they differ by a factor of $[K_v:I_v]$. 

{\color{\changecolor} 
By and large,  these issues are not very important to the kind of computation we do. 
However, there are a small number of places where these may become confusing. These \index{$\Hop$ $\Hop_K$ $\Hop_{KI}$ $\Hop_{IK}$}
are the places where we must simultaneously work with ordinary and derived Hecke algebras.
Our derived Hecke algebras are defined analogously to the right-hand side of \eqref{left right};
as discussed in the remark of \S \ref{Arithmeticmanifolds}, they act on the right on cohomology.
As such, their definition does not line up with $\mathrm{H}_K$.
 

Therefore, at  certain points where these issues need clarity, we will adopt the notation
$$ \Hop_K :=  \Hom_{SG_v}(S[G_v/K_v], S[G_v/K_v]),$$
an algebra that is identified with the opposite algebra of $\mathrm{H}_K$ by means of \eqref{left right};
it acts on the {\em right} of $V^{K_v}$ for any $G$-representation $V$.
Similarly, we define $\Hop_K, \Hop_{KI}, \Hop_{IK}, \Hop_I$ e.g. 
$\Hop_{IK} = \Hom_{SG_v}(S[G_v/K_v], S[G_v/I_v])$; it is identified with $\mathrm{H}_{IK}$, but (for example)
$\Hop_{K}$ acts on $\Hop_{IK}$ on the right, whereas $\mathrm{H}_K$ acts on $\mathrm{H}_{IK}$ on the left. }




 





\end{remark}
  
 
  
{\color{blue} In debugging this the following diagram is useful in understanding what we have called either $\mathrm{H}_{AB}$ or $\mathrm{H}_{AB}^{\mathrm{op}}$: 
{\small   \begin{equation}
 \xymatrix{
 \mathrm{measures}(B \backslash G/A)  \ar[r]\ar[d]  &  \Hom(S[G/B], S[G/A]) \ar[d]^{\times \mu(A)/\mu(B)} \ar[r]^s & \mbox{Functions}^G(G/A \times G/B) \ar[d]^{T(e,y)} \ar[dr]^{T(x,e)} . \\
\mathrm{measures}(B \backslash G/A) \ar[r]  &  \Hom(V^A, V^B) &  \mbox{functions}(A \backslash G/B)  & \mbox{functions}(B \backslash G/A)   \\
  }
\end{equation}}
The map at the top sends $\mu$ to the map sending $eB \mapsto \sum_{g \in G/A} \mu(B g) [gA]$, 
whereas the map at the bottom sends $\mu$ to the map sending $v$ to $\mu \star v$, which corresponds instead to the element $\sum_{g \in G/A} \mu(gA) [gA]$. 
The inverse of $s$ sends the function $T(x,y)$ to the map $g \in S[G/B] \mapsto Tg(x) = \sum T(x,y) g(y)$;
thus $eB$ is sent to $\sum_{x} T(x, e) \cdot [xA]$. 
In particular it sends $T$ onto the measure given by $\mu(Bx) = T(x, e)$; visibly $T(x, e)$ defines a function on $B \backslash G/A$. 

Added later: in particular, if $\mu$ is supported on the double coset $BgA$, the associated function $T$ is supported on the $B$-orbit
of $gA \times eB$.


{\em The isolated veritcal arrow sends $T$ to $T(e, gA)$   will never be used. In our identifications used for the derived Hecke algebra,
see \S \ref{doublecoset}, we use the identification given by $T(x,e)$, i.e. the vertical arrow. This corresponds to evaluating the homorphism $S[G/B] \rightarrow S[G/A]$
on $eB$ as we just saw.} 

 

Therefore, the diagram doesn't commute, but only after insertion of the $\times \mu(A)/\mu(B)$ factor.  When it comes to actions on cohomology, our convention is that we are using the ``top'' map.   
Now we'll use the following cases:
\begin{itemize}
\item $A=K, B=I$ -- we want the inclusion $V^K \hookrightarrow V^I$, which comes from $e_K$ at the bottom left, but so also from 
the map $S[G/I] \rightarrow S[G/K]$ taking $eI$ to $eK$, which corresponds to the measure $|W| e_K$ at the top left.  This corresponds to the pullback in cohomology. 

\item $A=I, B=K$: we want the pushforward $V^I \rightarrow V^K$,  which comes from $|W| e_K$ at the bottom left, and so from  $e_K$ at the top left.  Equivalently,
it comes from the map $S[G/K] \rightarrow S[G/I]$ that takes $eK$ to $\sum_{k \in K/I} kI$.  This correponds to the pushforward in cohomology. 
\end{itemize}

From the point of view of the bottom map the inclusion $V^K \hookrightarrow V^I$ corresponds to $e_K$, and the pushforward $V^I \rightarrow V^K$
corresponds to $|W| e_K$. However, using the top map, the roles are reversed, and these correspond to $|W| e_K$ and $e_K$ respectively. 

The products go like this:
{\tiny    \begin{equation}
 \xymatrix{
 \underbrace{ \mathrm{meas}(C \backslash G/B)}_{\mu \in H_{BC}} \times  \underbrace{\mathrm{meas}( B \backslash G/A)}_{\nu \in H_{AB}} \ar[r]\ar[dd]  &
  \Hom(V^B, V^C) \times \Hom(V^A, V^B) \ar[dd]   &  
 \ar[l] 
  \underbrace{ \Hom(S[G/B], S[G/A])}_{\nu'} \times  \underbrace{ \Hom(S[G/C], S[G/B]) }_{\mu'} \ar[d]^{\mapsto \nu' \circ \mu'}    \\
&&    \mathrm{Fun}(G/A \times G/B) \times \mathrm{Fun}(G/B \times G/C) \ar[d]^{\sum_{y} \nu'(x,y) \mu'(y,z)}  \\ 
  \underbrace{  \mathrm{meas}(C \backslash G/A)   }_{\mu * \nu} \ar[r]  &  \Hom(V^A, V^C)      & \ar[l] \mathrm{Fun}(G/A \times G/C) 
   }
\end{equation} }


 
 
 
Roughly speaking, the map from measures on $B \backslash G/A$ to functions on $G/A \times G/B$
sends a measure $\mu$ to the function given by $(x,y) \mapsto \mu(y^{-1} x)$. 
}
\end{comment}

 









 
Because $q$ is congruent to $1$ modulo $\ell^r$, the structure of $\mathrm{H}_I$ is very simple.
 It is isomorphic simply to the group algebra 
 of the affine Weyl group:
 \begin{equation} \label{affineweyl} \mathrm{H}_I \simeq S[\tilde{W}] \end{equation}
An explicit anti-isomorphism sends the characteristic function of $I_v w I_v$ to the
 element $w$, for $w \in \tilde{W}$; in particular $e_K$ is sent
 to $\frac{1}{|W|} \sum_{w \in W} w$, the sum over the usual Weyl group. 
 
This follows from the standard presentation of the Iwahori-Hecke algebra (for a reference
with complex coefficients, see \cite[Theorem 4.2]{ChrissGinzburg}); the key point
is that the relation $(T_s-q)(T_s+1)$ simplifies to $T_s^2=1$ when $q=1$ in the coefficients.  
 Actually it is also possible to verify $\mathrm{H}_I$ is isomorphic to $S[\tilde{W}]$ by using torus localization,
although we omit the details.







\subsection{Central element and discriminant} \label{Zdis} 
Every element of $S[X_*]^W$ is central  in $S[\tilde{W}]$. Therefore, \eqref{affineweyl} yields 
a  natural map (indeed an isomorphism) from $Z := S[X_*]^W$ to the center of $\mathrm{H}_I$.  
 
Then $\mathrm{H}_I, \mathrm{H}_K$ have structures of $Z$-algebra and $\mathrm{H}_{IK}, \mathrm{H}_{KI}$
have structure of $Z$-module, all of which are compatible in the obvious way. 

For example, the  ring homomorphism $Z \rightarrow \mathrm{H}_K$
is given by $z \mapsto e_K z e_K = e_K z$. In fact this is a ring {\em isomorphism}, as follows easily from the explicit presentation.
Then e.g. $\mathrm{H}_{IK}$ has two structures of $Z$-module, one via $Z \rightarrow \mathrm{H}_I$ and one via
$Z \rightarrow \mathrm{H}_K$, and the ``compatibility'' is that these two structures coincide. 
 























\subsection{Iwahori Hecke algebra} \label{IwahoriHecke}
  
 {\color{\changecolor}  The next statement 
 asserts that the bimodules $\mathrm{H}_{KI}, \mathrm{H}_{IK}$ give
 equivalences of categories, at least over the open subset of $\Spec(Z)$
 where the ``$W$-covering'' $\Spec \ S[X_*] \rightarrow \Spec  \ S[X_*]^W$ is {\'e}tale. }
  \footnote{{\color{\changecolor} 
I am grateful to Peter Schneider for correcting an error. In an earlier version of this paper, this Lemma was formulated
over a larger open subset of $\Spec \ Z$, but one step in the proof was not correct in this greater generality.}}
     
\begin{lemma} \label{IHequivalence}
Let $\mathfrak{m}$ be a maximal ideal of $Z$ 
over which the map $Z \rightarrow S[X_*]$ is {\'e}tale,
and write $Z'$ for the localization of $Z$ at $\mathfrak{m}$. 
 
 
  
   Write $\mathrm{H}_K' = \mathrm{H}_K \otimes_{Z} Z'$ and define similarly
$\mathrm{H}_I', \mathrm{H}_{IK}', \mathrm{H}_{KI}'$. 
Then the bimodules $\mathrm{H}_{IK}'$ and $\mathrm{H}_{KI}'$
induce inverse equivalences of categories between $\mathrm{H}_K'$ modules and $\mathrm{H}_I'$ modules. \end{lemma}  
This is probably well-known in characteristic zero at least.





\proof   (Sketch). 


Let's show, for example, that the natural map induced by multiplication  

\begin{equation} \label{targetmap}
  \mathrm{H}_{IK} \otimes_{\mathrm{H}_K}  \mathrm{H}_{KI}
 \rightarrow \mathrm{H}_I \end{equation}


yields an isomorphism after localization at $\mathfrak{m}$. 
In what follows, we denote such localization with a prime: $S[X_*]' = S[X_*] \otimes_Z Z'$. 

Note that  $\mathrm{H}_I$  is  free of rank $w$ as a right module over $S[X_*]$  (clear from \eqref{affineweyl}) 
and, being finite {\'e}tale, $S[X_*]'$ is
\locally
free as a right module over $Z'$
of rank $w$.





 So $\mathrm{H}_I'$ is \locally free of rank $w^2$ over $Z'$.
Similarly, $\mathrm{H}_{IK}'$ and $\mathrm{H}_{KI}'$ are \locally free of rank $w$
and  $\mathrm{H}_K'$ is  locally free of rank $1$ as a $Z'$-module.  The
obstruction to \eqref{targetmap} being an isomorphism then given   by the vanishing of a suitable determinant;
it is enough, therefore, to  show that
\eqref{targetmap} is onto after reducing modulo the  maximal ideal $\mathfrak{m}'$ of $Z'$.

  


We can extend


the natural homomorphism $Z' \rightarrow Z'/\mathfrak{m}'$
to a homomorphism $\chi: S[X_*]' \rightarrow k$, 
  with $k$ an algebraically closed field containing the finite field $Z'/\mathfrak{m}'$. 
   Note that $k$ has characteristic $\ell$, and that $\chi$ is not fixed by any element of $W$.
      
 
 

Now  a homomorphism from $X_* \rightarrow k^{\times}$
is the same as
an unramified $k$-valued character $\chi$ of the maximal torus $A_v$;
so we may identify $\chi$ to a character of $A_v$. 
We form the corresponding induced representation $V= V_{\chi}$. 
Its elements consist of locally constant $k$-valued functions on $G_{v}$
that transform according to $\chi$ on a Borel subgroup containing $A_v$. 
Now
$V^{I_v}$ is a $k$-vector space of rank $w$, and $V^{K_v}$ is a $k$-vector space of rank $1$,
and $Z$ acts on these spaces via the character $\chi$ (as follows, e.g.
from \eqref{explicit00} below).   

We now show that the natural maps
$$\mathrm{H}_{ab} \otimes_Z  k \rightarrow \Hom(V^a, V^b)$$
are isomorphisms for $a$ and $b$ belonging to $\{I, K\}$; that implies the 
desired claim, that is to say, that \eqref{targetmap} is onto after reducing modulo $\mathfrak{m}$.

Because the two sides have the same rank it is enough to check surjectivity. 
In fact, it's enough to show surjectivity in the case of 
$\mathrm{H}_{II}$ and to show that all the other maps are nonzero (because then, for example, the image for $\mathrm{H}_{IK}$ would be a nonzero subspace
of $\Hom(V^{I_v}, V^{K_v})$ which is stable under $\Hom(V^{I_v}, V^{I_v})$.) 
 The other maps are clearly nonzero: the element $e_K$ induces a nonzero map
in each of the cases $IK, KI, KK$. So we are reduced to seeing that 
\begin{equation} \label{moo} \mathrm{H}_{I} \twoheadrightarrow \Hom(V^{I_v}, V^{I_v}).\end{equation}

But there's a standard basis for $V^{I_v}$ indexed by the Weyl group:  $v_w \ (w \in W)$, whose restriction to $K$ 
is the characteristic function of the Bruhat cell  indexed by $w$. 
 The group algebra of $W$, inside $\mathrm{H}_I$, acts by permuting the elements $v_w$. 
Also the element $\lambda \in X_* $, considered again inside $\mathrm{H}_I$, acts by  \begin{equation} \label{explicit00}  \lambda \cdot v_w = \langle w \chi, \lambda \rangle v_w.\end{equation}
In other words, as a representation of $\tilde{W}$, this is the representation
induced from the generic character $\chi$, and so clearly irreducible.  The surjectivity of \eqref{moo} follows. 
 \qed	
 

  
 
\subsection{Localization for the derived Iwahori--Hecke algebra} \label{dhLocalization}
It will later on be helpful to make use of localization for the {\em derived} Iwahori--Hecke algebra.  

We define the derived Iwahori Hecke algebra as per the recipe of \S \ref{sec:dha}, i.e.
$$ \mathscr{H}_I := \Ext_{SG_v}^*(S[G_v/I_v], S[G_v/I_v]).$$
As before this  is isomorphic to the algebra of functions  $h$ that associate to $(x,y) \in G_v/I_v \times G_v/I_v$
a class $h(x,y) \in H^*(G_{xy}, S)$, with the product as described in \S \ref{desc2}.
  In a similar way, we get derived versions
$\mathscr{H}_{IK},\mathscr{H}_{KI}$ of the bimodules $\mathrm{H}_{KI}, \mathrm{H}_{IK}$ defined earlier. 


 Now, we can consider  ``restriction to $\tilde{W}$, '' i.e.
\begin{equation} \label{Tau1}  h_1  \in \mathscr{H}_{II} \longrightarrow  h_1' \in  \mbox{ functions $\tilde{W} \times \tilde{W} \rightarrow H^*(T,S)$} \end{equation}
where $T$ is as in 
\S \ref{BasicNotn}
 and we identify $w \in \tilde{W}$ with $wI \in G_v/I_v$; and 
\begin{equation} \label{Tau2}  h_2 \in \mathscr{H}_{IK} \longrightarrow  h_2' \in \mbox{ functions $\tilde{W} \times X_* \rightarrow H^*(T,S)$} \end{equation} where here we identify $x \in X_*$ with the associated coset $xK_v$; and we used the fact that $T$ stabilizes pointwise both  $\tilde{W} \cdot I_v$ and $X_* \cdot K_v$ to restrict cohomology classes to $T$. 
 Finally we have a similar map for $\mathscr{H}_{KI}$.
 
 
 Note that the right-hand side of \eqref{Tau1} has an algebra structure,   at least  restricting to functions supported on finitely many $\tilde{W}$-orbits,
 by means of the formula $H_1 H_2 (x,y)=
 \sum_{z \in \tilde{W}} H_1(x,z) \cup H_2(z,y)$ (where all of $x,y,z$ all belong to $\tilde{W}$). 
  This algebra acts on the right-hand side of \eqref{Tau2}, by means 
  of the same formula, but $H_2$ now belongs to the right-hand side of \eqref{Tau2}, 
  and therefore $y$ is now taken to belong to $X_*$. 
  
  
 
 \begin{lemma}
Under our current notation and assumptions,
(see \S \ref{BasicNotn}), 
the map \eqref{Tau1} is an algebra morphism.
 Similarly, the map \eqref{Tau2}  
 is compatible with the  map \eqref{Tau1} and the product $\mathscr{H}_{II} \times \mathscr{H}_{IK} \rightarrow \mathscr{H}_{IK}$;
similarly for $\mathscr{H}_{KI}$.
 \end{lemma}
 
 \proof 
 
 We want to show that (where $h_1,h_2 \in \mathscr{H}_{II}$)
  $$ \mathrm{Res}(h_1 h_2) = h_1'  h_2',$$
 where $\mathrm{Res}$ means to restrict all $G_v/I_v$ arguments to $\tilde{W}$ and restrict cohomology classes to $T$; 
we also want similar statements for the $\mathscr{H}_{II}$-action on $\mathscr{H}_{KI}$ and $\mathscr{H}_{IK}$. 
 
 By precisely the same argument as in \S \ref{Satake algebra proof}, we are reduced to the following claim:
 








 
 \begin{quote} 
{\em Claim:}   
Let $y'$ belong to either $G_v/K_v$ or $G_v/I_v$. Let $\Gamma$ be an $\ell$-Sylow of $A_v \cap K_v$. 
Let $\Gamma_{y'}$ be the stabilizer of $y'$ in $\Gamma$.
Then
 the corestriction $H^*(\Gamma_{y'}, S) \rightarrow H^*(\Gamma, S)$ vanishes, 
 unless $y' \in X_* \subset G_v/K_v$ or $y' \in \tilde{W} \subset G_v/I_v$.  \end{quote}
 

 
 
 
We repeat
the reasoning of Lemma \ref{splitness}:  let $\mathbf{S}$ be the algebraic double centralizer 
 of  $\Gamma_{y'}$.  As before, $\Gamma_{y'} \subset \Gamma$ gives $\mathbf{S} \subset \mathbf{A}$. 
 
Let $\mathbf{S}^0$ be the identity component of $\mathbf{S}$. By Lemma  \ref{doublecentralizer},  the component group of $\mathbf{S}$ is prime-to-$\ell$. Therefore,  
$\Gamma_{y'}$ lies inside $\mathbf{S}^0$. Let $\Gamma_{y'}^* \subset \mathbf{S}^0(F_v)^{\circ}$ be an $\ell$-Sylow of the maximal compact subgroup.  Thus $\Gamma_{y'} \subset \Gamma_{y'}^*$.



Choose a complement $\mathbf{S}' \subset \mathbf{A}$ to $\mathbf{S}^0$, i.e. a subtorus
with the property that $\mathbf{S}^0 \times \mathbf{S}' \rightarrow \mathbf{A}$ is an isomorphism.  
Then $\Gamma_{y'}^* \subset \mathbf{S}^0(F_v)^{\circ}$ is an $\ell$-Sylow,
and $\Gamma \subset \mathbf{A}(F_v)^{\circ}$ is an $\ell$-Sylow. 
Therefore $$\Gamma = \Gamma_{y'}^* \times \Gamma'$$
where $\Gamma'$ is the $\ell$-Sylow of $\mathbf{S}'(F_v)^{\circ}$. 

If $\mathbf{S}'$ were trivial, then $\mathbf{S}^0 = \mathbf{A}$.
In that case  $y'$ lies in the fixed set of $\mathbf{A}(F_v)^{\circ}$. 
In the case where $y' \in G_v/K_v$ this was proved in
  \S \ref{doublecentralizer}. However, the proof of this assertion also applies word for word
to establish the same assertion in the case $y' \in G_v/I_v$. 
 
The fixed set of  $\mathbf{A}(F_v)^{\circ}$
 on $G_v/K_v$ is $X_*$, as before, and the fixed set  of  $\mathbf{A}(F_v)^{\circ}$
on $G_v/I_v$ is precisely $\tilde{W} I_v \subset G_v/I_v$.\footnote{Here is a proof of the latter claim: 
if $gI_v$ is fixed, then   $g K_v \in X_* K_v$, and modifying $g$ by an element
of $\mathbf{A}(F_v)$, we can suppose $g \in K_v$. We are reduced to computing
the $\mathbf{A}(F_v)^{\circ}$-fixed points on $K_v/I_v$, which amount to the torus fixed points on a flag variety over $\mathbf{F}_v$ --
using Lemma \ref{nontriv} to avoid problems with small residue field, these fixed points are precisely the $wI_v$ with $w \in W$, as desired.}

 
Otherwise, $\mathbf{S}'$ is not trivial, the corestriction $\Gamma_{y'}^* \rightarrow \Gamma$
vanishes as before, and so the corestriction $\Gamma_{y'} \rightarrow \Gamma$ vanishes too. 
 \qed

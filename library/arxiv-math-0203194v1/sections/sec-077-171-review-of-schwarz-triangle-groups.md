---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-077-171-review-of-schwarz-triangle-groups
section_title: "Review of Schwarz triangle groups."
section_number: 17.1
pages: 179-183
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.994
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::5.1}

\begin{para}\label{para::5.1.1} A {\it Schwarz orbifold} is a complex orbifold
 of the form 
 \begin{equation*}
  \mathcal{S}(e_0,e_1,e_\infty)=(\P^1; (0,
   e_0), (1,e_1), (\infty, e_{\infty})).
 \end{equation*}
 It is uniformizable. The universal orbifold-covering is $\P^1, \A^1$ or 
 the open unit disk $\matheur{D}$ according to whether $\sum  \frac{1}{e_i}$ is
 $>1,\;=1,\;$ or $<1$ respectively.

 \noindent We fix a base-point $\ovl{s}$ (which can be a tangential
 base-point).
 
\medskip\noindent The {\it Schwarz triangle group\footnote{in conformity
 with the previous chapter, we do 
 not allow the $e_i$'s to be infinite. Thus we restrict our attention to
 the so-called cocompact triangle groups.}} $\Delta(e_0,e_1,e_\infty)$
 may be defined as $\pi_1^{\mathrm{orb}}(\mathcal{S}(e_0,e_1,e_\infty),s)$.

\noindent As an abstract group, it has generators 
$\gamma_0,\gamma_1, \gamma_\infty$ and relations
 $\gamma_0^{e_0}=\gamma_1^{e_1}=\gamma_\infty^{e_\infty}= \Pi \gamma_i = 
1$. A permutation of $e_0,e_1,e_\infty)$ does not change the group, only
 the orbifold by a homography interchanging 
 $0,1$ and $\infty$.  
\end{para}

\begin{para}\label{para::5.1.2} The uniformizing differential equation is
 fuchsian with singularities at $0,1,\infty$, and Riemann scheme 
\begin{equation*}
\begin{pmatrix}
 0 &  1 & \infty \\
 &&&\\
 \frac{1}{2}(1+\frac{1}{e_0})& \frac{1}{2}(1+\frac{1}{e_{1}})&
 \frac{-1}{2}(1+\frac{1}{e_{\infty}}) \\ 
 &&& \\
 \frac{1}{2}(1-\frac{1}{e_0})& \frac{1}{2}(1-\frac{1}{e_{1}})&
 \frac{-1}{2}(1-\frac{1}{e_{\infty}})
\end{pmatrix} .
\end{equation*}

 \medskip Multiplying solutions of this equation by  
\begin{equation*}
 z^{\frac{1}{2}(-1+\frac{1}{e_0})}(z-1)^{\frac{1}{2}(-1+\frac{1}{e_1})}
\end{equation*}
transforms this equation into a (projectively equivalent) differential equation of hypergeometric type
\begin{equation*}
 HGDE(a,b,c)\;\;\;\;\;\;\;\;\;\;\;\;\;\; z(z-1)y''+(c-(a+b+1)z)y'-ab y=0,  
\end{equation*}
with $1-c=\frac{1}{e_0},\;c-a-b=\frac{1}{e_1},\; \pm(a-b)=\frac{1}{e_\infty}$, whose Riemann scheme is    
 \begin{equation*}
  \begin{pmatrix}
   0 &  1 & \infty \\
   &&&\\
   0& 0& \frac{1}{2}(1-\frac{1}{e_0}-\frac{1}{e_1}+\frac{1}{e_{\infty}}) \\
   &&&\\
   \frac{1}{e_0}&\frac{1}{e_{1}}&
   \frac{1}{2}(1-\frac{1}{e_0}-\frac{1}{e_1}-\frac{1}{e_{\infty}})
  \end{pmatrix} .
 \end{equation*}
 The triangle group $\Delta(e_0,e_1,e_\infty)$ may thus be interpreted
 as the {\it projective monodromy group pointed at $\ovl{s}$ of this
 hypergeometric differential equation}.
\end{para}

\begin{para}\label{para::5.1.3} The quotient $\tau$ of a suitable basis of
 solutions of $ HGDE(a,b,c)$ sends the upper half-plane bijectively 
onto a curvilinear triangle $\mathcal{T}$ with vertices
 $\tau(0),\tau(1),\tau(\infty)$ and respective angles 
$\pi/e_0,\pi/e_1,\pi/e_\infty$. By the Schwarz reflection principle, the
 map $\tau$ can be extended to the lower half-plane 
through each of the ``segments'' $]0,1[$, $]1,\infty[$, $]\infty,0[$ by
 conformal reflections $s_\infty,s_0,s_1$ respectively. The products 
$\gamma_0=s_1s_\infty,\,\gamma_1=s_\infty s_0,\,\gamma_\infty=s_0s_1 $
 give the standard generators of $\Delta(e_0,e_1,e_\infty)$. By
 repeating these reflections, the occuring curvilinear triangles do not
 overlap (except on their edges) and provide a tiling of the universal
orbifold-covering ($\P^1, \A^1$ or $\matheur{D}$).
\end{para}

\begin{para}\label{para::5.1.4} A similar situation arises for any
 hypergeometric differential equation with rational parameters
 $(a,b,c)$.  However, if some of the differences of the exponents
$1-c,c-a-b,a-b$ is not the inverse of an integer, the triangles which
occur by iterating Schwarz reflections may overlap. Moreover, if the
local projective monodromies are of respective order $e_0, e_1,
e_\infty$ at $0,1,\infty$, the global projective monodromy group need
not be $\Delta(e_0,e_1,e_\infty)$. This is related to the fact that a
homomorphic image of $\Delta(e_0,e_1,e_\infty)$ which preserves the
order of $\gamma_0,\gamma_1,\gamma_\infty$ need not be isomorphic to
$\Delta(e_0,e_1,e_\infty)$ (\cf \cite{greenberg81:_homom_psl} for a
detailed discussion 
of homomorphic images of triangle groups\footnote{we are indebted to
M. Kapovich for this reference.}).
\end{para}

\begin{para}\label{para::5.1.5} The case $\sum  \frac{1}{e_i}>1$ (universal
 covering $\P^1$) corresponds to the Schwarz list of $HGDE$ with finite
 (projective) monodromy groups: the list of triples
 $(e_0,e_1,e_\infty)$ is, up to permutation:

 \medskip
 $(2,2,n)$ corresponding to a dihedral group,

 $(2,3,3)$ corresponding to the tetrahedral group,

$(2,3,4)$ corresponding to the octahedral group,

 $(2,3,5)$ corresponding to the icosahedral group.
 
 \medskip In the case $\sum  \frac{1}{e_i}=1$ (universal covering $\A^1$), there is a global orbifold chart given by an elliptic curve with complex
 multiplication. There are three possibilities for $(e_0,e_1,e_\infty)$, up to permutation:
 $(2,3,6)$,
 $(2,4,4)$,
 $(3,3,3)$.
 
 \medskip All the other triples belong to the ``hyperbolic case'':
 $\Delta(e_0,e_1,e_\infty)$ is a fuchsian group.
 
 For more detail on these topics, we refer to the  good treatises
 \cite{f2}, \cite{ntatg}, \cite{hfml}.

\end{para}

\begin{para}\label{para::5.1.6} As was remarked by J. Wolfart, Belyi's
 criterion for algebraic curves to be defined over $\ovl{\Q}$ can be
 expressed in terms of Schwarz orbifolds as follows:

 a complex projective curve $\ovl{S}$ is defined over $\ovl{\Q}$ if and
 only if it is the base of an orbifold-covering $(\ovl{S}, (Z_i,e_i))$
 of some Schwarz orbifold.
\end{para}



\subsection{$p$-adic Schwarz orbifolds and triangle groups.}\label{sub::5.2}

\begin{para}\label{para::5.2.1} A {\it $p$-adic Schwarz orbifold} is an
 orbifold over some complete subfield $K$ of $\C_p$  of the form 
\begin{equation*}
\mathcal{S}(e_0,e_1,e_\infty)=(\P^1, (0, e_0), (1,e_1), (\infty, e_{\infty})).
\end{equation*}
\noindent Up to replacing $K$ by a finite extension, it is uniformizable
 (\cf example in \ref{para::4.4.4}). However, there is no universal
 orbifold-covering (\ref{para::4.4.4}).
 
We want our $p$-adic triangle groups to be {\it discrete}
groups of fractional linear $p$-adic transformations. Thus it is not
 possible in general to define them as orbifold 
fundamental groups, but only as appropriate discrete quotients. This
 leads us to imitate the alternative definition \ref{para::5.1.2} 
of triangle groups as projective hypergeometric monodromy groups. 
\end{para}

\begin{para}\label{para::5.2.2} Let $e_0, e_1, e_\infty$ be integers $>1$, and
 define  
\begin{equation*}
 a=
 \frac{1}{2}\Bigl(1-\frac{1}{e_0}-\frac{1}{e_1}+\frac{1}{e_{\infty}}\Bigr),\,
 b=
 \frac{1}{2}\Bigl(1-\frac{1}{e_0}-\frac{1}{e_1}-\frac{1}{e_{\infty}}\Bigr),\, 
 c= 1- \frac{1}{e_0}.
\end{equation*} 
 We now consider the hypergeometric differential equation 
$HGDE(a,b,c)$ as a $p$-adic differential equation.
\end{para}

\begin{dfn}\label{def::5.2.3} Assume that $ HGDE(a,b,c) $ is in the
 image of the \'etale Riemann-Hilbert functor, 
\ie the \'etale sheaf of germs
 of solutions is locally constant on $\P^1_{\C_p}\setminus\{0,1,\infty\}$
 (\cf \ref{thm::3.4.6}).  If the corresponding projective monodromy group
\begin{equation*}
\Im\bigl[\pi_1^{\mathrm{et}}(\P^1\setminus\{0,1,\infty\},\ovl{s})\to
 PGL_2(\C_p)\bigr]
\end{equation*} is discrete and finitely generated, it is then called
a {\rm $p$-adic triangle group}, and denoted by
$\Delta_p(e_0,e_1,e_\infty)$.

\medskip
In the sequel, we say that ``{\it $\Delta_p(e_0,e_1,e_\infty)$ exists}''
to express that the assumptions of \ref{def::5.2.3} are 
fulfilled (this depends on the four numbers $p,e_0,e_1,e_\infty$).

\end{dfn}

\begin{pro}\label{pro::5.2.4}
 \begin{enumerate}
  \renewcommand{\theenumi}{\alph{enumi}}
  \item If $\Delta_p(e_0,e_1,e_\infty)$ exists,
	there exists a finite Galois covering 
	$\phi:\,\ovl{S}' \to \P^1$ ramified above $\{0,1,\infty\}$, such that
	the pull-back of $ HGDE(a,b,c) $ by $\phi$ has a full 
	set of multivalued analytic solutions over
	$S'=\phi^{-1}(\P^1\setminus\{0,1,\infty\})$.
  \item If $\Delta_p(e_0,e_1,e_\infty)$ exists, the homomorphism
	\begin{equation*}
	 \Im[\pi_1^{\mathrm{et}}(\P^1\setminus\{0,1,\infty\},\ovl{s})\to
	 PGL_2(\C_p)]
	\end{equation*}
	factors through a surjective homomorphism 
	\begin{equation*}
	 \pi_1^{\mathrm{orb}}(\mathcal{S}(e_0,e_1,e_\infty)) \to
	  \Delta_p(e_0,e_1,e_\infty). 
	\end{equation*}
  \item Conversely, if the projective connection attached to $HGDE(a,b,c)$
	comes from a projective representation
	\begin{equation*}
	 \pi_1^{\mathrm{orb}}(\mathcal{S}) \to  PGL_2(\C_p)
	\end{equation*}
	with discrete image, this image is a $p$-adic triangle group
	$\Delta_p(e_0,e_1,e_\infty)$.
  \item Every $p$-adic triangle group
	$\Delta_p(e_0,e_1,e_\infty)$ is a discontinuous subgroup of
	$PGL_2(K)$ for some finite extension $K$ of $\Q_p$.
 \end{enumerate}
\end{pro}

\begin{proof}
  (a) Because the Wronskian of $ HGDE(a,b,c) $ is algebraic, the
 determinant of the representation  
 $\rho:\,\pi_1^{\mathrm{et}}(\P^1_{\C_p} \setminus
 \{0,1,\infty\},\ovl{s})\to 
 GL_2(\C_p)$ factors through a finite representation of
 $\pi_1^{\mathrm{temp}}(\P^1_{\C_p}\setminus\{0,1,\infty\},\ovl{s})$.
 Under the assumptions of \ref{def::5.2.3}, $\Im\,\ovl{\rho}$ is
 finitely 
 generated, and it follows that $\Im \,\rho$ is finitely generated. By
 \ref{pro::3.5.10}, one derives that $\rho$ factors through
 $\pi_1^{\mathrm{temp}}(\P^1\setminus\{0,1,\infty\},\ovl{s})$. This
 implies a), \cf \ref{para::3.5.6} (where a concrete description
 of the monodromy is 
 also given).

   (b) We have just seen that $\rho$ factors through
 $\pi_1^{\mathrm{temp}}(\P^1_{\C_p}\setminus\{0,1,\infty\},\ovl{s})$. To
 check that the associated projective representation factors through 
 $\pi_1^{\mathrm{orb}}(\mathcal{S}(e_0,e_1,e_\infty))$ is a matter of
 projective local monodromy --- or more plainly, of difference of
 exponents --- at $0,1,\infty$ (\cf 4.5); this is clear.

  (c) Again because the Wronskian of $HGDE(a,b,c)$ is algebraic, the
 fact that the projective connection attached to $HGDE(a,b,c)$ comes
 from a projective representation of
 $\pi_1^{\mathrm{temp}}(\P^1\setminus\{0,1,\infty\},\ovl{s})$ implies
 that $ HGDE(a,b,c) $ itself comes from a representation of
 $\pi_1^{\mathrm{temp}}(\P^1\setminus\{0,1,\infty\},\ovl{s})$ (\cf the
 discussion in \ref{para::3.5.13}). By \ref{pro::3.5.10}, the
 image is finitely generated, and 
 the assertion follows.

  (d) If $\Delta_p(e_0,e_1,e_\infty)$ exists, there exists a finite
 Galois global orbifold chart $\ovl{S}'\to \P^1$ such that pull-back of
 $ HGDE(a,b,c) $ on the universal topological covering
 $\widetilde{\ovl{S}'}$ becomes trivial (as a connection). Notice that
 $\ovl{S}'$ is a projective curve defined over some number field, and a
 fortiori over some finite extension $K/\Q_p$.  Up to replacing $K$ by a
 finite extension, we may assume that $\widetilde{\ovl{S}'}$ is also
 defined over $K$ (and that the image in $\ovl{S}'$ of some geometric
 point above $\ovl{s}$ is $K$-rational). Thus $\rho$ factors through a
 representation of
 $\pi_1^{\mathrm{temp}}(\P^1_K\setminus\{0,1,\infty\},\ovl{s})\to
 GL_2(K)$, which makes clear that $\Delta_p(e_0,e_1,e_\infty)\subset
 PGL_2(K)$. Since $K$ is locally compact, any discrete subgroup of
 $PGL_2(K)$ is discontinuous \cite[1.6.4]{sgamc}.
\end{proof}

\medskip\noindent{\it Remark.} By (b), if $\Delta_p(e_0,e_1,e_\infty)$
exists, there {\it exists} a finite Galois global 
orbifold chart $\phi:\,\ovl{S}' \to \P^1$ such that the quotient of two
non-proportional solutions of $ HGDE(a,b,c) $ 
defines a multivalued meromorphic function on $\ovl{S}'$. However, one
should not believe that {\it any} finite Galois 
global orbifold chart $\phi:\,\ovl{S}' \to \P^1$ has this property.

\noindent Indeed, we shall see below that the diadic triangle group
$\Delta_2(4,4,4)$ exists. The Fermat curve $F_4$ over 
$\C_2$ provides a finite Galois global orbifold chart, with
$\pi_1^{\mathrm{top}}(F_4)=1$ (because $F_4$ has tree-like reduction). 
But the corresponding projective hypergeometric connection does not
become trivial over $F_4$, since $\Delta(4,4,4)$ is 
infinite.  

\begin{para}\label{para::5.2.5} The case $\sum \frac{1}{e_i}>1$ corresponds
 to the list of $p$-adic $HGDE$ with finite (projective) monodromy
 groups. This is the same as the Schwarz list: $(2,2,n)$, $(2,3,3)$,
$(2,3,4)$, $(2,3,5)$, up to permutation, and yields finite $p$-adic
triangle groups for every $p$ which are isomorphic to the corresponding
finite Schwarz triangle groups.

\medskip\noindent On the other hand, there is {\it no $p$-adic triangle
 group with $\sum  \frac{1}{e_i}=1$}. Indeed, there is a global
 algebraic orbifold chart given by an elliptic curve with complex
 multiplication.  Viewed over $\C_p$, these have good reduction, and it
 follows from \ref{para::4.5.6} and \ref{para::2.3.2} that the orbifold
 fundamental group is 
 compact. Any discrete representation would then be finite, and it would
 follow that the corresponding $HGDE$ has a basis of algebraic
 solutions. This is an algebraic property, which can be translated back
 over $\C$. One finds that such a $HGDE$ would belong to the Schwarz
 list, a contradiction.

\medskip In the sequel, we restrict our attention to the ``hyperbolic
 case'' $\sum  \frac{1}{e_i}<1$. It is not clear a 
 priori that there exists any hyperbolic $p$-adic triangle group.
\end{para}

---
doc_id: arxiv-1608.07234v3
doc_title: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS"
section_id: sec-008-9-some-very-poor-evidence-for-the-main-conjectur
section_title: "Some very poor evidence for the main conjecture: Tori and the trivial representation"
section_number: 9
pages: 74-76
source_pdf: 1608.07234v3.pdf
source_sha256: 311730670d2fdcb7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.903
doc_brief: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS — We describe a graded extension of the usual Hecke algebra: it acts in a graded fashion on the cohomology of an arithmetic group Γ."
---
\label{pisspoor}
 
 We verify that the main conjecture  (Conjecture \ref{mainconjecture})
  holds in the case when $\mathbf{G}$ is an anisotropic torus.  This is straightforward,  but still slightly comforting. 
  
  One may also verify that  a certain analogous statement to Conjecture \ref{mainconjecture}
  holds in the situation studied in  \S \ref{Quillen},
but there we do not understand the situation clearly at present --  hopefully it will eventually prove to be a specialization
 of the general conjecture to the nontempered case.
    
  
\subsection{Setup} \label{tori}

Let $\mathbf{T}$ be an anisotropic $F$-torus; let $\mathcal{O}$ be the ring of integers of $F$. 
Let us fix a finite set of places $\ramprimes$ such that $\mathbf{T}$ admits a smooth model over $\mathcal{O}[\frac{1}{\ramprimes}]$. 
We assume it contains all places $\wp$ above the rational prime $p$. 



  The associated symmetric space 
$$ \mathcal{S} =  \mathbf{T}(F \otimes \R)/\mbox{maximal compact}$$
has  $q,\delta$ invariants (see \eqref{qdef}):
$$ q= 0 , \delta = \dim(\mathcal{S}).$$ 


The arithmetic manifold $Y(K)$ associated to a level structure $K$  is
a disjoint union of copies of $\mathcal{S}/\Delta$, where 
  $\Delta$ is a congruence subgroup of $\mathbf{T}(\mathcal{O})$. 
Moreover  the quotient $ \mathcal{S}/\Delta$ is a union of compact tori, and thus 
the rank of $\Delta$, i.e. $\dim_{\Q} (\Delta \otimes \Q)$, equals $\delta$.  
  We will suppose that $K$ is chosen so small that $\Delta$ is free of $p$-torsion.
 



\subsection{Galois cohomology}

Let $M$ be the motive associated to the first homology group $H_1(\mathbf{T})$ of $\mathbf{T}$. 

Let $X_*(\mathbf{T})$ be the co-character group of $\mathbf{T}$. It carries an action of $\Gal(\overline{F}/F)$. 
Coming from $X_* \otimes_{\Z} \mathbb{G}_m \stackrel{\sim}{\rightarrow} \mathbf{T}$, we get  an isomorphism of $\Gal(\overline{F}/F)$-modules 
$$M_p := \mbox{$p$-adic realization of $M$} = X_*(\mathbf{T}) \otimes_{\Z} \Z_{p}(1) \simeq \varprojlim \mathbf{T}[p^n],$$
the $p$-adic Tate module of $\mathbf{T}$. 
Computing with the Kummer sequence,
\begin{equation} \label{cococo} H^1(\mathcal{O}[\frac{1}{\ramprimes}] ,  M_p) \simeq \mathbf{T}(\mathcal{O}[\frac{1}{\ramprimes}]) \otimes \Z_p.  \end{equation}
Inside the left-hand side, we can consider those classes  that are crystalline at $p$ and 
 unramified at {\em all primes away from $p$, including primes in $S$.} We will denote this subgroup by $H^1_{f, \mathrm{ur}}(F, M_p)$. \footnote{For a precise
 definition we refer to \cite{BK}: the group we have called $H^1_{f, \mathrm{ur}}$  is the group denoted by $H^1_{f, U}$ in \cite[Definition 5.1]{BK} with $U$ taken to be all finite places. This group is often 
simply written $H^1_f(F, -)$ in the literature.}

 The subgroup on the right-hand side corresponding to $H^1_{f, \mathrm{ur}}(F, M_p)$, call it
$$ \Delta' \subset  \mathbf{T}(\mathcal{O}[\frac{1}{\ramprimes}]) \otimes \Z_p,$$ 
 is  commensurable to the image of  $\Delta \otimes \Z_p$ in the right-hand side of \eqref{cococo}.
{\color{\changecolor} Indeed, the constraint that a point $t \in  \mathbf{T}(\mathcal{O}[\frac{1}{\ramprimes}])$
have cohomology class in $H^1_{f, \mathrm{ur}}$ is equivalent
to forcing $t$ to belong to a suitable open compact subgroup of $\mathbf{T}(F_v)$
for each $v \in S$; see   \cite[Theorem 2.3.1]{HK} for this statement in the trickier case when $v$ is above $p$.} 




We suppose (shrinking $\Delta$ a little if necessary) that $\Delta \otimes \Z_p \subset \Delta'$.
  
Also, the {\em motivic} cohomology $H^1_{\mot}(M, \Q(1))$
is identified with  with the $\mathbf{T}(\Q) \otimes \Q$,  as we may see by first passing to an extension that trivializes the torus $\mathbf{T}$. Presumably
the following is valid, but I did not try to check it:

\begin{quote} {\em Assumption:} The subgroup of ``integral classes'' $H^1_{\mot}(M_{\Z}, \Q(1))$ (see discussion after \eqref{saxophone}) is identified  with the image of $\Delta \otimes \Q$ inside $\mathbf{T}(\Q) \otimes \Q$. 
\end{quote}

Now a cohomological automorphic form $\Pi$ for $\mathbf{T}$ is trivial on the connected component of $\mathbf{T}(F \otimes \R)$, i.e.
they are the {\em finite order}  id{\`e}le class characters of $\mathbf{T}$.   
However, the associated co-adjoint motive (see \S \ref{sec:MV}) doesn't depend on which idele class character: we have simply 
$$ \left(\mbox{ coadjoint motive for $\Pi$}  \right) (1) \simeq M,$$
the motive $M$ described above. \footnote{
 Indeed, the the $\Z_{p}$-linear dual of $\hat{T}$ is identified with 
$$ \Lie(T^{\vee})^{\vee} \simeq \left( \Lie(\mathbf{G}_m) \otimes X_*(T^{\vee}) \right)^{\vee} \simeq X^*(T^{\vee})  \otimes \Z_p \simeq X_*(\mathbf{T}) \otimes \Z_{p}$$
where we have fixed an isomorphism $\Z \simeq \Lie(\mathbf{G}_m)$.  }


 


















Now let us examine Conjecture \ref{mainconjecture} in this case. Put 
$$\mathsf{V} = H^1_{f, \mathrm{ur}}(F,  M_p)^{\vee},$$
where $M_p$ is the $p$-adic etale realization, and $\vee$ denotes $\Z_p$-linear dual; thus $\mathsf{V} = \Hom(\Delta',\Z_p)$. 
The notation $H^1_{f, \mathrm{ur}}$ was defined after \eqref{cococo}. 
 
 
There is a natural action of $\mathsf{V}$ on $H^*(Y, \Z_p)$,
obtained from the maps
\begin{equation} \label{frow} \mathsf{V} = H^1(\Delta', \Z_p) \rightarrow H^1(\Delta, \Z_p). \end{equation}
Moreover, motivic cohomology gives a lattice in $\mathsf{V} \otimes \Q = H^1(\Delta', \Q_p)$
(the classes which are $\Q$-valued on $\Delta \subset \Delta'$)
and obviously this lattice indeed preserves $H^*(Y, \Q)$, in the
$\Q$-linear extension of the action of $\mathsf{V}$. 


The only point to be discussed is that the action \eqref{frow} is indeed that 
resulting from the  same formalism as \S \ref{reciprocity}.  We describe this only briefly. 


Let $v$ be a finite place not belonging to $S$, so that $\mathbf{T}$ extends to a smooth torus over $\mathcal{O}_v$. 
As usual we have an injection, 
 $$  \Hom(\mathbf{T}(\mathcal{O}_v), \Z/p^n) \hookrightarrow \mbox{ derived Hecke algebra at $v$,}$$
 and thus an action of  the left-hand group on the cohomology
 of $H^*(Y,\Z/p^n)$; explicitly, this action is obtained by pulling back cohomology classes via $\Delta \rightarrow \mathbf{T}(\mathcal{O}_v)$, and cup product. 
 By just the same procedure as  that described  in \eqref{fqndef}, we can construct a map  











 $$ \Hom(\mathbf{T}(\mathcal{O}_v), \Z/p^n)  \rightarrow \underbrace{ \mathsf{V}/p^n}_{\simeq \Hom(\Delta',\Z/p^n)} ,$$
and one verifies this is the  map induced by $\Delta' \rightarrow \mathbf{T}(\mathcal{O}_v) \otimes \Z_p$. 
 Then the action of $\mathsf{V}/p^n$  on $H^*(Y, \Z/p^n)$ is compatible with the ``derived Hecke'' action of $\Hom(\mathbf{T}(\mathcal{O}_v), \Z/p^n) $ for all $v$;
 and in fact this compatibility determines the action of $\mathsf{V}/p^n$.

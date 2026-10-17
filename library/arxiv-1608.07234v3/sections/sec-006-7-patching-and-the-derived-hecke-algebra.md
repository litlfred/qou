---
doc_id: arxiv-1608.07234v3
doc_title: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS"
section_id: sec-006-7-patching-and-the-derived-hecke-algebra
section_title: "Patching and the derived Hecke algebra"
section_number: 7
pages: 50-55
source_pdf: 1608.07234v3.pdf
source_sha256: 311730670d2fdcb7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.913
latex_coverage_ratio: 0.893
---
\label{Patching2}


We continue with the notation  and assumptions of the previous section \S \ref{Patching}; see in particular
\S  \ref{Sec:assumptions} and \S \ref{GaloisAss}. 
That section was primarily setup, and now we get down to proving that the global derived Hecke algebra is ``big enough,''
in the sense discussed around 
\eqref{bigenough}. 
The main result is
Theorem \ref{mindegreeproof}. 

We use the patching of the Taylor--Wiles method; more specifically, we use the 
version of that method  that was discovered \cite{CG} by Calegari and Geraghty,
which applies to situations where the same Hecke eigensystem occurs in multiple degrees.
We also use heavily the presentation of the Calegari--Geraghty method 
given by Khare and Thorne \cite{KT}. 

\subsection{Deformation rings and chain complexes at level $Q_n$.}  \label{Qnchain}

 Fix now a Taylor-Wiles datum $Q_n$ of level $n$. 
  (We will   abusively use $Q_n$ both to denote the Taylor-Wiles datum and simply the set of primes associated to that datum.)
  
  Recall the definition of $Y_1^*(Q_n)$ from \S \ref{TWprimes stuff}: it is the fiber-product of coverings $Y_1(q, n) \rightarrow Y(1)$
  over $q \in Q_n$. 
 We now collect together various results about the homology of $Y_1^*(Q_n)$, which are essentially the same
 results as those already discussed for $Y_1(q,n)$, but using all the primes in $Q_n$ instead of just $\{q\}$. 
 
 
 \begin{lemma} The homology $H_j(Y_1^*(Q_n), \Z_p)_{\mathfrak{m}}$
  vanishes for $j \notin [\BWq, \BWq+\delta]$. 
 \end{lemma} 
 \proof As in Lemma \ref{vanishing lemma BW}. \qed
 
 Just as in \eqref{bigsplit}, this homology group is split (by ``$U$-operators'') into summands
 indexed by collections $\Frob^T_q \in T^{\vee}(k) \ \ (q \in Q_n)$, where each $\Frob^T_q$
 is conjugate to the Frobenius at $q$. 
  In particular, since the Taylor--Wiles datum is equipped (\S \ref{TWprimes stuff}) with a specific choice of such a $\Frob_q^T$ for each $q \in Q_n$, we
  can consider  the summand 
\begin{equation} \label{Weylsplitting}  H_*(Y_1^*(Q_n), \Z_p)_{\mathfrak{m},\Frob^T_{Q_n}}  \subset H_*(Y_1^*(Q_n), \Z_p)_{\mathfrak{m}}  \end{equation}
indexed by  these prescribed lifts. 

  Recall  from \eqref{idontcare}  that $Y_1^*(Q_n) \rightarrow Y_0(Q_n)$ is Galois, with Galois group $T_n$.  \index{$R_n$} \index{$R_{Q_n}$} 
Let us introduce notation for the deformation rings of interest to us: let 
 $$R_{Q_n} = \mbox{universal deformation ring at level $\ramprimes \coprod Q_n$,}$$
 \begin{equation} \label{RnRn}  R_n = \mbox{ quotient of $R_{Q_n}$ classifying   deformations of inertial level $\leq n$ at primes in $Q_n$}
 \end{equation}
  For example,  in the case when $Q_n = \{q\}$ this was the ring $R^{\univ,\leq n}_{\ramprimes \cup \{q\}}$ discussed around \eqref{Rndef}.  
 
  By the discussion  of  \eqref{rgh}  and after, we get a morphism
   $\mathbf{A}(\mathbf{F}_{q_i})/p^n \rightarrow R_n^{\times}$, and therefore we get (see \eqref{idontcare}): 
 $$T_n \rightarrow R_n^{\times}$$
 What we know (local-global compatibility, assumed in \S \ref{Lgcompat})  is that the natural action of $T_n$  (deck transformations) on homology of $Y_1^*(Q_n)$ 
is compatible with its action via $T_n \rightarrow R_n^{\times}$.  
 To say differently, we get a map \begin{equation} \label{Sndef} S_n := \Z/p^n[T_n] \rightarrow R_n/p^n, \end{equation}  and the natural action of $S_n$ on the $\Z/p^n$ homology of $Y_1^*(Q_n)$ is compatible
 with that via the map to $R_n/p^n$.   
 
  
  Now consider the complex of singular chains   $$ \widetilde{C}_n = \Chains(Y_1^*(Q_n); \Z/p^n)$$
  with $\Z/p^n$ coefficients.  We think of it as a complex of $S_n$ modules, because of the action of $T_n$ by deck transformations on $Y_1^*(Q_n)$.   It is quasi-isomorphic to a bounded complex of finite free $S_n$-modules
  and we have canonical identifications:
  
 \begin{equation} \label{id1} H_* \widetilde{C}_n \simeq H_*(Y_1^*(Q_n), \Z/p^n)\end{equation}
\begin{equation} \label{id2} H^*\Hom_{S_n}(\widetilde{C}_n, \Z/p^n) \simeq H^*(Y_0(Q_n), \Z/p^n)\end{equation}
\begin{equation} \label{id0} H_*( \widetilde{C_n} \otimes_{S_n} \Z/p^n) \simeq  H_*(Y_0(Q_n), \Z/p^n).\end{equation}

  Note that $\widetilde{C}_n$ is a free $S_n$-module, with basis given by the characteristic functions of an arbitrarily chosen set of representatives
  for $T_n$-orbits on singular simplices. 
  Therefore, the homology  of $\Hom_{S_n}(\widetilde{C}_n, \Z/p^n)$ computes the homomorphisms from $\widetilde{C}_n$ to $\Z/p^n$
  in the derived category of $S_n$-modules. 
  By composition of homomorphisms in this derived category, we get a map
 \begin{equation} \label{above} \underbrace{H^*  \left( \Hom_{S_n}(\widetilde{C}_n, \Z/p^n) \right) }_{\simeq H^*(Y_0(Q_n),\Z/p^n)} \times  \underbrace{ \Ext^*_{S_n}(\Z/p^n, \Z/p^n) }_{\simeq H^*(T_n,\Z/p^n)} \rightarrow  \underbrace{ H^* \left( \Hom_{S_n}(\widetilde{C}_n, \Z/p^n)\right) }_{\simeq H^*(Y_0(Q_n),\Z/p^n)} \end{equation}
   With respect to the identifications noted underneath the respective terms, this is precisely the ``natural'' action of $H^*(T_n, \Z/p^n)$ on $H^*(Y_0(Q_n), \Z/p^n)$.
  This natural action arises thus: 
   the covering $Y_1^*(Q_n) \rightarrow Y_0(Q_n)$ has covering group $T_n$, i.e. can be regarded as a map
\begin{equation} \label{BTmap} Y_0(Q_n) \rightarrow \mathrm{B}T_n\end{equation} 
   from $Y_0(Q_n)$ to the classifying space of $T_n$; this allows one to pull back cohomology classes from $T_n$ and take cup product. 
      The coincidence of \eqref{above} and this ``natural action'' is a general fact; for lack of a reference we sketch a proof in \S \ref{sec:remedialtopology}. 
 
 


It is possible to ``cut down'' $\widetilde{C}_n$ in a fashion that corresponds to  the summand
  \eqref{Weylsplitting}, as is explained in \cite{KT} (see Lemma 2.12 thereof,  and surrounding discussion).  
  This can be done compatibly for $Y_0(Q_n)$ and $Y_1^*(Q_n)$ and thus one gets 
  a perfect complex $C_n$ of $S_n$-modules, equipped with identifications 
that are analogous to \eqref{id1} and \eqref{id2}: 
 \begin{equation} \label{id3} H_*(C_n; \Z/p^n) \simeq H_*(Y_1^*(Q_n), \Z/p^n)_{\mathfrak{m}, \Frob^T}, \end{equation} 
\begin{equation} \label{id4} H^*(\Hom_{S_n}(C_n, \Z/p^n)) \simeq H^*(Y_0(Q_n), \Z/p^n)_{\mathfrak{m}, \Frob^T}\end{equation}
  and again the action of $\Ext^*_{S_n}(\Z/p^n , \Z/p^n)$ on the latter group corresponds to the natural action    by pulling back cohomology classes via \eqref{BTmap}.\footnote{As a sanity check on this, note that the action of $H^*(T_n, \Z/p^n)$ on $H^*(Y_0(Q_n), \Z/p^n)$ indeed
  does preserve the splitting into  summands of the type \eqref{Weylsplitting}; one can see this directly  
  by seeing that $H^*(T_n, \Z/p^n)$, considered inside the  derived Iwahori-Hecke algebra, commutes   with the ``positive subalgebra'' used to define the splitting \eqref{Weylsplitting}.}









 



 




\subsection{Extracting the limit}  \label{extraction}    Now we ``pass to the limit'' as per Taylor--Wiles and  Calegari--Geraghty.
 The idea is roughly speaking to extract, by a compactness argument, a subsequence of $n$ along which
the $C_n, S_n, R_n$ are compatible, and then get limits $\Cinf, \Sinf, \Rinf$ by an inverse limit. Usually in modularity lifting
one is only concerned with the limit of the process; but in our case we also want to remember
some facts about how this relates to the $C_n, S_n, R_n$. 
A discussion of this process which emphasizes exactly what we need is given in \cite[\S 13]{GV}, see in particular Theorem 13.1 therein.

 
 We choose a sequence of Taylor-Wiles data $Q_n$ with  $n \rightarrow \infty$.  
 After replacing the $Q_n$ by a suitable subsequence and then reindexing  -- that is to say, 
 replacing $Q_i$ by $Q_{n_i}$ for some $n_i > i$, and then regarding $Q_{n_i}$ as a set of Taylor--Wiles primes of level  $i$ -- 
 we can arrange that we  can ``pass to the limit.''
After having done this, we obtain at last the following data:   
  
\begin{itemize}
 
\item[(a)] A sequence of Taylor--Wiles data $Q_n$ of level $n$.

 Recall to this we have associated coverings $Y_1^*(Q_n) \rightarrow  Y_0(Q_n) \rightarrow Y(1)$,
as in \S \ref{TWprimes stuff}, and the Galois group of the former map is called $T_n$; also \eqref{Sndef} we set $S_n = \Z/p^n[T_n]$, the group algebra of $T_n$. 

\item[(b)] With $\Sinf = \Z_p[[x_1, \dots, x_R]]$ as in
\S \ref{sec:diamond}, 
a complex $\Cinf$ of finite free $\Sinf$-modules, 
equipped with 
a quasi-isomorphism \begin{equation} \label{Descent} \Cinf \otimes_{\Sinf} S_n  \simeq C_n,\end{equation}   
where $C_n$ is as described in \S \ref{Qnchain}: a version of the chain complex of $Y_1^*(Q_n)$ with $\Z/p^n$ coefficients,
but localized at $\mathfrak{m}$ and $\Frob^T$. 











\medskip
\item[(c)]  
 A quotient $\usbR_n$ of $R_n$,   \index{$\usbR_n$} 
defined as follows:

Recall   from \eqref{RnRn} the definition of $R_n$; a quotient of the crystalline deformation ring
at level  $\ramprimes \coprod Q_n$.  We set \begin{equation} \label{goef} \usbR_n = R_n/(p^n, \mathfrak{m}^{K(n)})\end{equation}
for a certain explicit function $K(n)$, chosen so that  e.g.  action of $R_n$ on $H_*(C_n)$  
automatically factors through $\usbR_n$.  We can and will assume $K(n) \geq 2n$.   (The main function of $K(n)$ is to make $\usbR_n$ Artinian, 
while still retaining enough information about all of $R_n$ for our purposes.) 

\item[(d)]

 A ``limit deformation ring'' $\Rinf \simeq \Z_p[[x_1, \dots, x_{R-\delta}]]$  equipped with 
maps  $\Sinf \rightarrow \Rinf$ and maps $\Rinf \rightarrow \usbR_n, \Rinf \twoheadrightarrow \defring$   which are compatible,
in the sense that this diagram commutes: 
    \begin{equation} \label{SinftySn}
 \xymatrix{
\Sinf  \ar[r] \ar[d] &   \Rinf  \ar[d] \ar[r]  & \defring   \ar[d] \\
S_n   \ar[r]   &   \usbR_n   \ar[r] & \defring/  (p^n, \mathfrak{m}^{K(n)}) }
\end{equation}

(Recall here that $\defring$ is the deformation ring of $\rhobar$, with crystalline conditions imposed, without adding any level, 
cf. \S \ref{GaloisAss}). 

Moreover, the composite $\Sinf \rightarrow \Rinf \rightarrow \defring$ factors through 
the augmentation $\Sinf \rightarrow \Z_p$; and also the  left-hand square induces an isomorphism
 \begin{equation} \label{second-iso}  \Rinf \otimes_{\Sinf} S_n \simeq  \usbR_n \end{equation}
 
 
\item[(e)] An  action of $\Rinf$ on $H_*(\Cinf)$, compatible with the $\Sinf$ action,
and with the maps $H_*(\Cinf) \rightarrow H_*(C_n)$, where
$\Rinf$ acts on $H_*(C_n)$ via $\Rinf \rightarrow  \usbR_n$. 

 

\item[(f)]   An identification of  \begin{equation} \label{logstructure} H^*(\Hom_{\Sinf}(\Cinf, \Z_p)) \stackrel{\sim}{\longrightarrow} H^*(Y(1), \Z_p)_{\mathfrak{m}},\end{equation}   
compatible under \eqref{Descent} with 
the identification $H^*(\Hom_{S_n}(C_n, \Z/p^n)) \simeq H^*(Y(1), \Z/p^n)_{\mathfrak{m}}$
that is the composition of \eqref{id4} with the pushforward. (This is described in dual form in \cite[Theorem 13.1(d)]{GV} but one gets
similarly this result, and the statement about compatibility is just a matter of looking at the definition of the map \eqref{logstructure}. 
\begin{comment} \footnote{COMMENT: This is only described in dual form in the quoted reference,
so we briefly describe it.  We have identifications of $H^*(Y(1), \Z_p)_{\mathfrak{m}} $ with 
\begin{eqnarray*}  \varprojlim_n H^*(Y(1), \Z/p^n)_{\mathfrak{m}}    \stackrel{\eqref{doubleprojremark}}{\simeq }  \varprojlim_n H^*(Y_0(Q_n), \Z/p^n)_{\mathfrak{m}, \Frob_Q} 
  \stackrel{\eqref{id4}}{ \simeq} \varprojlim_n  H^* \Hom_{S_n}(C_n, \Z/p^n)   \\  \stackrel{\eqref{Descent}}{=} \varprojlim_n H^* \Hom_{\Sinf}(\Cinf, \Z/p^n) 
 = H^* \varprojlim \Hom_{\Sinf}(\Cinf, \Z/p^n) =  H^* \Hom_{\Sinf} (\Cinf, \Z_p).  \end{eqnarray*}
Here, the structure of inverse system on the second and third terms is determined by their isomorphisms with the first term;
the fact that this is compatible with the natural structure of inverse system on $ \Hom_{\Sinf}(\Cinf, \Z/p^n) $
is part of the way the limit process is set up. In fact, \cite[\S 13.9(iv)]{GV}
says that the various maps   $C_n \otimes_{S_n} \Z/p^n \rightarrow C_*(Y(1),  \Z/p^n)_{\mathfrak{m}}$
are compatible with one another, and so the various maps 
$\Cinf \otimes_{\Sinf} \Z/p^n \rightarrow C_*(Y(1), \Z/p^n)_{\mathfrak{m}}$ 
are all compatible with reference to the isomorphisms
$C_*(Y(1), \Z/p^{n+1})_{\mathfrak{m}} \underline{\otimes}_{\Z/p^{n+1}} \Z/p^n \simeq C_*(Y(1), \Z/p^n)_{\mathfrak{m}}$
in the derived category of $\Z/p^n$-modules.  Now if $h \in H^*(Y(1), \Z/p^{n+1})$ is a cohomology class,
considered as a homomorphism $C_*(Y(1), \Z/p^n) \stackrel{f_h}{ \rightarrow} \Z/p^{n+1}[?]$ in the derived category of $\Z/p^{n+1}$-modules,
then the image $\bar{h} \in H^*(Y(1), \Z/p^n)$ is  represented by the derived tensor product $f_h \underline{\otimes} \Z/p^n$. 
The claim follows from this. 
}
\end{comment}

  

\item[(g)]

(These last results use heavily the formal smoothness, assumption (e) from  \S \ref{GaloisAss}):
 $\Cinf$  has homology only in degree $q$, and its homology there $H_q(\Cinf)$ is free   as $\Rinf$-module. Moreover, one has 
an ``$R=T$ result''
\begin{equation} \label{first-iso} \Rinf \otimes_{\Sinf} \Z_p \simeq \defring \simeq \mbox{ image of $\mathbb{T}_{K_0} $ in  $\End \ H_q(Y(1), \Z_p)_{\mathfrak{m}}$}. \end{equation}

 \end{itemize}
 
 
  
 
\subsection{The structure of $\Sinf \rightarrow \Rinf$} \label{SR} 
 
 The limit process has given a map of rings $\Sinf \rightarrow \Rinf$, 
 where $\Sinf$ and $\Rinf$ are formal power series rings that represent, roughly speaking,
 ``limits'' of the rings $S_n, R_n$ as $n \rightarrow \infty$. 
  
As in \eqref{Zplift}, the  representation $\Pi$ gives a lift $\rho$ to $\Z_p$ of the residual representation $\rhobar$;
 this corresponds to an augmentation $\defring \rightarrow \Z_p$.  
Thus we also get an augmentation $$f: \Rinf \rightarrow \Z_p,$$
and the pullback of this to $\Sinf$ is the natural augmentation of $\Sinf \rightarrow \Z_p$ ((d) of \S \ref{extraction}).
In particular, the kernel of $f$ on $\Sinf$ is precisely the ideal
$\Iinf$. 
 
 
 Our assumptions imply that the map $\Sinf \rightarrow \Rinf$ is surjective.
 Indeed, because $\Sinf$ is complete for the $\Iinf$-adic topology
 it is enough to verify that $\Sinf/\Iinf \rightarrow \Rinf/\Iinf \Rinf$
 is surjective.  But
 $\Rinf/\Iinf$ is a Hecke ring by \eqref{first-iso} and so isomorphic to $\Z_p$
 by \eqref{nocong0}. 
  Note in particular that this also means that $\Iinf \Rinf$ is precisely the kernel of $f$. 
 
 
 The following easy  lemma is now useful for explicit computations. 
 
 \begin{lemma} \label{straightening} We can choose generators  $x_i, y_j$ for $\Sinf, \Rinf$, i.e.
  $$\Sinf = \Z_p[[x_1, \dots, x_R]],  \ \ \Rinf = \Z_p[[y_1, \dots, y_{R-\delta}]]$$ 
 such that the $x_i, y_j$s lie in the kernel of the compatible augmentations 
 $$\Sinf \rightarrow \Rinf \rightarrow \Z_p,$$  and 
the map $\Sinf \rightarrow \Rinf$  is given by $x_i \mapsto y_i$ for $i \leq R-\delta$ and $x_i \mapsto 0 $ for $i > R-\delta$. 
 \end{lemma}

\proof 
  
 
 Write $f: \Rinf \rightarrow \Z_p$ for the augmentation. 
  Abstractly, $\Rinf \simeq \Z_p[[u_1, \dots, u_{R-{\delta}}]]$ where all the $u_i$ lie in the maximal ideal.  
Set  $y_i = u_i - f(u_i) \in  \ker(\Rinf \rightarrow \Z_p)$. Then still $\Rinf \simeq \Z_p[[y_1, \dots, y_{R-\delta}]]$. 
We have noted above that $\Jinf := \Iinf \Rinf$ is precisely the kernel of the augmentation $\Rinf \rightarrow \Z_p$; thus, 
  the $y_i$ freely span as $\Z_p$-module the quotient $\Jinf/\Jinf^2$.  
 
 Lift the $y_i$ to $x_1, \dots, x_r \in \ker(\Sinf \rightarrow \Z_p)$. 
Necessarily the $x_i$  span a saturated\footnote{Here we say that a submodule $Q$ of a free $\Z_p$-module $Q'$ is saturated if the quotient
$Q'/Q$ is torsion-free.} $\Z_p$-submodule of rank $s$ inside $\Iinf/\Iinf^2 \simeq \Z_p^s$; 
they are $\Z_p$- independent because any linear relation $\sum a_i x_i \in \Iinf^2$ (with $a_i \in \Z_p$) 
would give rise to a corresponding linear relation in $\Rinf$, a contradiction. Similarly, they are saturated because 
given $x'$  and $(a_1 \dots, a_r)$ with $\gcd(a_1, \dots, a_r) =1$ and  $p x' = \sum a_i x_i + \Iinf^2$, we would get a corresponding relation in $\Rinf$, again a contradiction. 

Now  extend  the $x_i$ to a full $\Z_p$-basis
$x_{r+1}, \dots, x_s$ for $\Iinf/\Iinf^2$.  Each $x_j$ for $j > r$
is sent under $\Sinf \rightarrow \Rinf$ an element of $\Jinf \subset \Rinf$, which means that it can be written
as a formal polynomial  $P_j(y_1, \dots, y_r)$ in  $y_1, \dots, y_r$, with no constant term; so  replacing $x_j$ by $x_j - P_j(x_1, \dots, x_r)$ we may  suppose that $x_j \mapsto 0$ in $\Rinf$. 
\qed 














 















 

 
















 
 
 
 













Now we come to the main theorem of the section.  

\begin{theorem}  \label{mindegreeproof} 
Let assumptions be as in \S \ref{Sec:assumptions}
and \S \ref{GaloisAss}. 
The cohomology  $H^*(Y(1), \Z_p)_{\mathfrak{m}}$
  is generated, as a module over the strict global derived Hecke algebra (see \S \ref{limit} and \S \ref{Hecke:resplace} for definition with $\Z_p$ coefficients), by its minimal degree component $H^{\BWq}(Y(1), \Z_p)_{\mathfrak{m}}$.
 \end{theorem}
 
 
 \proof 









We use the setup of the Taylor--Wiles limit process (\S \ref{extraction}), beginning   with the fact that the natural map 
\begin{equation} \label{cyclicity2}H^{\BWq}(\Hom_{\Sinf}(\Cinf, \Z_p)) \otimes \Ext^j_{\Sinf}(\Z_p, \Z_p) \twoheadrightarrow   H^{\BWq+j}(\Hom_{\Sinf}(\Cinf, \Z_p))    \end{equation}
is a surjection for all $j$: by   (g) of \S \ref{extraction} and Lemma \ref{straightening}, 
we can choose coordinates so that $\Sinf \simeq \Z_p[[x_1, \dots, x_R]]$,
and the complex $\Cinf$ is quasi-isomorphic to {\color{\changecolor} a sum of copies of } $\Sinf/(x_{R}, \dots, x_{R-\delta+1})$
concentrated in a single degree.   So   the surjectivity of \eqref{cyclicity2} follows from the ``Koszul algebra'' computations in \S \ref{AppendixB} of the Appendix. 


   Examine now the diagram, where all the maps are the obvious ones;





{\small     \begin{equation} \label{previousstory}
 \xymatrix{
 H^{\BWq}(\Hom_{\Sinf}(\Cinf, \Z_p))^{} \ar[d]^{=} & \times  &    \Ext^{i}_{\Sinf}(\Z_p, \Z_p)  \ar[d]  \ar[r] &  H^{\BWq+i}(\Hom_{\Sinf}(\Cinf, \Z_p)) \ar[d]^V \\
  H^{\BWq}(\Hom_{\Sinf}(\Cinf, \Z_p))   \ar[d]^{V}  & \times&  \Ext^{i}_{\Sinf}(\Z_p, \Z/p^n)    \ar[r]&   H^{\BWq+i}(\Hom_{\Sinf}(\Cinf,  \Z/p^n))\ar[d]^{=}\\
  H^{\BWq}(\Hom_{\Sinf}(\Cinf, \Z/p^n))^{}   & \times & \left( \Ext^{i}_{\Sinf}(\Z/p^n, \Z/p^n) \right) \ar[r]   \ar[u]^U  &  H^{\BWq+i}(\Hom_{\Sinf}(\Cinf, \Z/p^n))   \\
 H^{\BWq}(\Hom_{S_n}(\Cinf \otimes_{\Sinf} S_n, \Z/p^n))^{} \ar[u]^{f, \sim} & \times  &   \left( \Ext^{i}_{S_n}(\Z/p^n, \Z/p^n) \right) \ar[r]^{\mathfrak{Q} \ \  \ \ \ \ \ } \ar[u]^{U'} &  \ar[u]^{\sim} H^{\BWq+i}(\Hom_{S_n}(\Cinf \otimes_{\Sinf} S_n, \Z/p^n)). \\
  }
  \end{equation}
  }
Here, the middle square ``commutes'' in the sense that the image of $(x, Uy)$ is the same as the image
  of $(Vx, y)$, i.e. $U, V$ are adjoint for the pairing.  The top and bottom squares commute.   
  All this is obvious, except for perhaps the bottom square which involves change of rings, so let us talk through it: 
The map $\Sinf \rightarrow S_n$ induces a forgetful map $T$
from the derived category of
$S_n$-modules to the derived category of $\Sinf$-modules.  
Take $$\alpha \in H^{\BWq}(\Hom_{S_n}(\Cinf \otimes_{\Sinf} S_n, \Z/p^n)), \ \ \beta \in   \Ext^{i}_{S_n}(\Z/p^n, \Z/p^n).$$ 
We can regard $\alpha$ as a map $\Cinf \otimes_{\Sinf} S_n \rightarrow \Z/p^n[q]$
and $\beta$ as a map $\Z/p^n[q] \rightarrow \Z/p^n[q+i]$,  both in the derived category of $S_n$-modules.
Applying the functor $T$, we see that $T \beta \cdot T\alpha  = T(\beta \alpha)$. On the other hand,
$T \alpha$ is  simply the morphism
$\Cinf \otimes_{\Sinf} S_n \rightarrow \Z/p^n[q]$ considered as a map of $\Sinf$-modules.
If we pre-compose with $\gamma: \Cinf \rightarrow \Cinf \otimes_{\Sinf} S_n$, considered
as a map of $\Sinf$-modules, we get $f(\alpha)$. 
 Similarly, $  T(\beta \alpha) \gamma  = f(\beta \alpha) \cdot \gamma$.
So $T \beta . f(\alpha) = f(\beta \alpha)$: that is the  commutativity of the bottom square.
 



























  
  
  
  
 
  
  
  
 












     
    
It follows  from the Lemma of \S \ref{sec:diamond}  that the composite $U \circ U'$ is surjective.  
  Also the map $V$ is surjective (because the cohomology of $\Hom_{\Sinf}(\Cinf, \Z_p)$ is torsion-free, by \eqref{logstructure} and
  assumption 7(a) of \S \ref{Sec:assumptions}). 
    Tracing through the above diagram, this is enough to show that the image of  $\mathfrak{Q}$ generates the codomain of $\mathfrak{Q}$. 


Now,  recall  from \eqref{Descent} the quasi-isomorphism $\Cinf \otimes_{\Sinf} S_n  \simeq C_n$; 
    we have therefore shown that 
   $   H^*(\Hom_{S_n}(C_n, \Z/p^n))$  is generated  by $ H^{\BWq}(\Hom_{S_n}(C_n, \Z/p^n))$ as a module   over $\Ext^*_{S_n}(\Z/p^n, \Z/p^n) $.
   As in the discussion after \eqref{above}, this  is equivalent to saying that
 $H^*(Y_0(Q_n), \Z/p^n)_{\mathfrak{m},\Frob^T}$ is generated by  its degree $q$ component as a $H^*(T_n, \Z/p^n)$-module, i.e.  
\begin{equation} \label{bencumber}H^{\BWq}(Y_0(Q_n), \Z/p^n)_{\mathfrak{m}, \Frob^T} \otimes H^*(T_n,\Z/p^n) \twoheadrightarrow H^*(Y_0(Q_n),\Z/p^n)_{\mathfrak{m}, \Frob^T}.\end{equation}
   
      

 



















































\label{randompageref}
In what follows, let us write $\mathscr{H}_I, \mathscr{H}_K$ for the tensor product \index{$\mathscr{H}_I$} \index{$\mathscr{H}_K$} 
of (derived) Iwahori-Hecke algebras  $\mathscr{H}_{I,q}$ and derived Hecke algebra $\mathscr{H}_{q}$  over  $q \in Q_n$;
and write $\mathrm{H}_K, \mathrm{H}_{KI}, \mathrm{H}_{IK}, \mathrm{H}_I$ for the (non-derived) algebras and bimodules
of \S \ref{Morita}, but tensoring over all $q \in Q_n$.  All of these will be taken with $\Z/p^n$ coefficients. 
 
Note that the action of $H^*(T_ n, \Z/p^n)$  on $H^*(Y_0(Q_n), \Z/p^n)$ factors through the action of $\mathscr{H}_I$ (e.g. see the Remark in \S \ref{sec:concrete}). 
  So $H^*(Y_0(Q_n), \Z/p^n)_{\mathfrak{m}, \Frob^T}$ is    generated in degree  $\BWq$ over  $\mathscr{H}_I$. 
  Taking the sum over all possible lifts $\Frob^T$,  as in \eqref{bigsplit}, we see that
  $H^*(Y_0^*(Q_n), \Z/p^n)_{\mathfrak{m}}$
  is also generated in degree $q$ over the derived $\mathscr{H}_I$.   
  
  
  Now,  each of the following maps are surjective:
  
  
\begin{eqnarray*}
H^{\BWq}(Y(1),\Z/p^n)_{\mathfrak{m}} \otimes \mathrm{H}_{KI} \twoheadrightarrow H^{\BWq}(Y_0(Q_n), \Z/p^n)_{\mathfrak{m}}, \\    H^{\BWq}(Y_0(Q_n), \Z/p^n)_{\mathfrak{m}} \otimes \mathscr{H}_I^j \twoheadrightarrow   H^{\BWq+j}(Y_0(Q_n), \Z/p^n)_{\mathfrak{m}},\\
H^{\BWq+j}(Y_0(Q_n) , \Z/p^n)_{\mathfrak{m}}\otimes \mathrm{H}_{IK} \twoheadrightarrow H^{\BWq+j}(Y(1),\Z/p^n)_{\mathfrak{m}}, \end{eqnarray*}
where the second statement is what we just proved, 
whereas the first and third statement come from Lemma \ref{needaref}.
Also there is a map  $\left( \mathrm{H}_{KI}  \otimes \mathscr{H}_I^j  \otimes \mathrm{H}_{IK} \right)  \rightarrow \mathscr{H}_K^j$ compatible with the respective actions, just arising  
from composition of Exts. We get  
$$   H^{\BWq}(Y(1), \Z/p^n)_{\mathfrak{m}}  \otimes  \mathscr{H}_K^j 
\twoheadrightarrow H^{\BWq+j}(Y(1), \Z/p^n)_{\mathfrak{m}}. $$

Passing to the limit (as in  the discussion of \S \ref{limit})    concludes the proof.  \qed

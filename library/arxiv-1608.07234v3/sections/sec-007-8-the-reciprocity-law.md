---
doc_id: arxiv-1608.07234v3
doc_title: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS"
section_id: sec-007-8-the-reciprocity-law
section_title: "The reciprocity law"
section_number: 8
pages: 55-74
source_pdf: 1608.07234v3.pdf
source_sha256: 311730670d2fdcb7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 0.896
doc_brief: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS — We describe a graded extension of the usual Hecke algebra: it acts in a graded fashion on the cohomology of an arithmetic group Γ."
---
\label{reciprocity} 


In \S \ref{Patching2} we proved, conditional under assumptions (\S \ref{Sec:assumptions}, \S \ref{GaloisAss}) on the existence of Galois representations attached to modular forms
and other assumptions that simplify the integral situation (\S \ref{Sec:assumptions}), 
that the global derived Hecke algebra is ``big enough,'' in the sense discussed around \eqref{bigenough}.  


We now turn to the question mentioned in \S \ref{reindexing}: 
we index elements of this global derived Hecke algebra by means of a certain dual Selmer group.
This is achieved in Theorem \ref{maintheorem}.  
This Theorem is not an end in itself; rather, it just gives the correct language for us to formulate the central conjecture of the paper, 
Conjecture \ref{mainconjecture}.
 
 
 
\subsection{The coadjoint representations}

We are interested in the co-adjoint representation, i.e. the dual of the 
representation of $G^{\vee}$ on its Lie algebra $\mathfrak{g}^{\vee}$.  
Denoting by $\dualLiedual$ the $\Z$-dual to this Lie algebra, we obtain  \index{$\Ad^*$} 
$$\Ad^*: G^{\vee} \rightarrow GL(\dualLiedual)$$ 
which we regard as a morphism of algebraic groups over $\Z$. 
\footnote{Why the {\em coadjoint} representation rather than the adjoint? They are isomorphic
for $G$ semisimple, at least away from small characteristic. However, canonically what comes up for us is the coadjoint;
for example,  when one works with tori, as in \S \ref{tori}, the difference is important. }
 

In particular given a representation $\sigma: G_{\Q} \rightarrow G^{\vee}(R)$ we denote by   
$\Ad^* \sigma: G_{\Q} \rightarrow \GL(R \otimes_{\Z} \dualLiedual)$ 
the composition of $\sigma$ with the co-adjoint representation.  
When $\sigma$ is valued in $\Z_p$, we will write
$\Ad ^* \sigma_n$ for the reduction of $\Ad ^* \sigma$ modulo $p^n$.  



\subsection{Galois cohomology} 

We will freely use the theory of Fontaine and Laffaille which (in good circumstances) parameterizes
crystalline representations of $\Gal(\overline{\Q_p}/\Q_p)$, even with torsion coefficients. For a summary, see \S 4 of \cite{BK}. 

Fix once and for all the interval $[-\frac{p-3}{2}, \frac{p-3}{2}] \subset \mathbb{N}$ of Hodge weights. 
We will say that a  representation   of $\Gal(\overline{\Q_p}/\Q_p)$  on a finitely generated $\Z_p$-module is  ``crystalline''
if it is isomorphic to a subquotient of a crystalline representation with Hodge weights in $[-\frac{p-3}{2}, \frac{p-3}{2}]$. 
This indexing of Hodge weights is useful for  adjoint representations  which have weights symmetric around $0$.

Recall that for any $p$-torsion  crystalline $M$   \index{$H^1_f$}
we can define
$$  H^1_f(\Q_p, M) \subset H^1(\Q_p, M) $$
which classifies those extensions $M \rightarrow  ? \rightarrow 1$ which are crystalline;
it is in fact a submodule and it is identified (by Fontaine-Laffaille theory) with a corresponding Ext-group in the category
of filtered Dieudonn{\'e} modules. In particular,  this allows one to check that
$H^1_f$ is isomorphic to the cokernel of the map 
\begin{equation} \label{kitty}
\mathrm{F}^0 D(M) \stackrel{1 - \mathrm{Frob}}{\rightarrow} D(M),\end{equation}
where $D(M)$ is the associated filtered Dieudonn{\'e} module. 
Also, the kernel of  $1-\mathrm{Frob}$  in \eqref{kitty} is isomorphic to $H^0(\Q_p, M)$. In particular, for $M$ finite we have 
\begin{equation} \label{goo-goo} \# H^1_f(\Q_p, M) = \frac{ | D(M)|}{|F^0 D(M)|} \cdot \# H^0(\Q_p, M),\end{equation} 
 which can be effectively 
 used to compute the size of $H^1_f$ (note: the size of $D(M)$ and $M$ coincide).
 
We will need to know that the subspaces $H^1_f(\Q_p, M)$ and $H^1_f(\Q_p, M^*)$
(with $M^* := \Hom(M, \mu_{p^{\infty}})$ are each other's annihilators \index{$M^*$, dual of a  Galois module}
under the local duality pairing $H^1(\Q_p, M) \times H^1(\Q_p, M^*) \simeq \Q/\Z$. 
This follows from the fact they annihilate each other  (their product would come from an $\Ext^2$
in the category of Fontaine--Laffaille modules, but the relevant $\Ext^2$ vanishes by \cite[Lemma 4.4]{BK})  and a size computation
using \eqref{goo-goo}.


\subsection{Selmer groups}

Let $\Q_{\ramprimes}$ 
be the largest extension of $\Q$ unramified outside 
$\ramprimes$, and let $M$ be a module for the Galois group of $\Q_{\ramprimes}/\Q$;
thus $M$ defines an {\'e}tale sheaf on $\Z[\frac{1}{\ramprimes}]$. 
We write

$$H^1(\Z[\frac{1}{S}], M) \supset H^1_f(\Z[\frac{1}{S}], M)$$
for (respectively) the {\'e}tale cohomology of $M$ (equivalently the group cohomology
of $\Gal(\Q_{\ramprimes}/\Q)$ with coefficients in $M$),
and the subset of this group consisting of classes that are crystalline at $p$, i.e. classes
whose image in $H^1(\Q_p, M)$ lies in the subgroup $H^1_f(\Q_p, M)$ defined above.

Note that we impose {\em no} local condition on  classes in $H^1_f(\Z[\frac{1}{S}], M)$ except  for the crystalline condition  at $p$. 
 
 We will write $H^1_f(\Q, M)$ for the usual Bloch--Kato Selmer group: this is 
the subgroup of classes in $H^1(\Gal(\overline{\Q}/\Q), M)$ which
are unramified away from $p$, {\em and} crystalline at $p$.
In general, we have an inclusion $H^1_f(\Q, M) \subset H^1_f(\Z[\frac{1}{S}], M)$;
the former is more restrictive, requiring that the cohomology class be unramified
at places of $\ramprimes - \{p\}$. However, in our applications, 
$M$ will be a module such that $H^1(\Q_v, M)$ vanishes for $v \in \ramprimes - \{p\}$,
and so $H^1_f(\Q, M) = H^1_f(\Z[\frac{1}{S}], M)$. 
 




\subsection{}  \label{mMain}

We will follow the notation of the previous section, described in \S \ref{Sec:assumptions};
in particular, we have an arithmetic manifold $Y(1) =Y(K_0)$, an automorphic
representation $\Pi$,  corresponding to a maximal ideal $\mathfrak{m}$ of the Hecke algebra;
and an associated Galois representation $\rho: G_{\Q} \rightarrow G^{\vee}(\Z_p)$. 
We let $\ramprimes$ be the set of ramified primes for $\rho$ or $K_0$, together with $p$.
 
\index{$\Vinf$} 
 Put  \begin{equation} \label{Vdef} \mathsf{V} :=   H^1_f(\Z[\frac{1}{\ramprimes}], \Ad^* \rho(1))^{\vee},\end{equation}
where  we wrote  $-^{\vee}$ for $\Hom(-, \Z_p)$. 
We will prove in Lemma \ref{DeltaDimensional} that both the $H^1_f$ above and  $\mathsf{V}$   are (under our assumptions)   free $\Z_p$-modules of rank $\delta$.


We will produce an action of $\mathsf{V}$ on   $H^*(Y(K), \Z_p)_{\mathfrak{m}}$.
To explain it, fix $\mathbf{A}$   a maximal torus of $\mathbf{G}$ and
let $q$ be a Taylor--Wiles prime of level $n$, 
equipped with an element of $T^{\vee}(k)$ conjugate to  Frobenius at $q$. 
Let $$T_q = \mathbf{A}(\F_q)/p^n.$$  \index{$T_q$} 
From this data we  will construct: \index{$\iota_{q,n}$} 
\begin{itemize}
\item[-] 
A natural embedding (\S \ref{Vnaction})  of  
 \begin{equation} \label{iotaqndef1} \iota_{q,n}: H^1(T_q,\Z/p^n) \hookrightarrow \left( \mathscr{H}^{(1)}_{q,\Z/p^n}\right)_{\mathfrak{m}} \end{equation} into the  degree $1$ component $ \mathscr{H}^{(1)}$ of the  local, full level,  derived Hecke algebra
$\mathscr{H}_{q, \Z/p^n}  $. (More precisely, we will use its completion at the maximal ideal $\mathfrak{m}$).   
\item[-]  A map \begin{equation} \label{fqndef} f_{q,n}: H^1(T_q, \Z/p^n) \rightarrow \mathsf{V}/p^n, \end{equation} \index{$f_{q,n}$}
We have already explained, in a special case, the constrution of $f_{q,n}$ in \eqref{padef}.
We briefly outline the general case: 
Given $\alpha \in H^1(T_q, \Z/p^n)$,
we obtain, by \eqref{brst}, an element  $\alpha'$ in the quotient of $H^1(\Q_q, \Ad \rho_n)$
by unramified classes;  now,  we associate to $\alpha$
the functional  sending $\beta \in H^1_f(\Z[\frac{1}{\ramprimes}], \Ad^* \rho(1))$ 
to the local pairing $\langle \alpha' , \beta_q \rangle_q  \in \Z/p^n$, where $\beta_q$ is the restriction of $\beta$ to $H^1(\Q_q, \Ad^* \rho(1))$. 
\end{itemize} 

 
Finally recall that under our assumptions (7(a) of \S \ref{Sec:assumptions}) , $H^*(Y(1), \Z_p)_{\mathfrak{m}}$ is torsion-free;
its reduction modulo $p^n$ coincides with  $H^*(Y(1), \Z/p^n)_{\mathfrak{m}}$.
\begin{theorem} \label{maintheorem}
Let notation and assumptions be as established in \S \ref{Patching}
(in particular \S \ref{Sec:assumptions},  \S \ref{GaloisAss}). 
Let $\Vinf$ be as in \eqref{Vdef}. 


 
There  exists a function $a: \mathbf{Z}_{\geq 1} \rightarrow \mathbf{Z}_{\geq 1}$ and 
an action of $\Vinf$ on $H^*(Y(1), \Z_p)_{\mathfrak{m}}$ 
by endomorphisms of degree $+1$ 
with the  following property:

(*) For any $n \geq 1$ and any  prime $q \equiv 1$ modulo $p^{a(n)}$,
equipped with a strongly regular  element  of $T^{\vee}(k)$ conjugate to 
$\rhobar(\mathrm{Frob}_q)$, 
 the two actions of $H^1(T_q, \Z/p^{n})$  on $H^*(Y(1), \Z/p^{n})_{\mathfrak{m}}$ coincide:
one via $f_{q,n}$  and one via $\iota_{q,n}$.
 
The property (*) uniquely characterizes the $\Vinf$ action (this is true for any function $a$). 
 
 In particular, the {\color{\changecolor} strict} global derived Hecke algebra
 contains $\mathsf{V}$, and so also the exterior algebra freely generated by $\mathsf{V}$
(the induced map from $\wedge^* \mathsf{V}$ 
 to endomorphisms of    $H^*(Y(1), \Z_p)_{\mathfrak{m}}$ is injective). 
 \end{theorem}




 Note that the
 uniqueness part of the statement is straightforward, because the condition pins down the action of $\mathsf{V}/p^r$ for arbitrarily large $r$:
by Chebotarev, 
  the images $f_{q,n}(H^1(T_q, \Z/p^n))$ generate $\mathsf{V}/p^n$ even when restricted to primes $q \equiv 1$ modulo $p^{a(n)}$;
  this basically  follows from the existence of Taylor--Wiles data (see in particular  \eqref{tsnvsurj}). 


{\color{\changecolor}  Finally,   under a further ``multiplicity one'' assumption, this result is sufficient to force the whole
derived Hecke algebra to be graded commutative.  We separate this result
from the main analysis because it is inessential to our main goals and it requires this additional multiplicity one assumption.

Before we state the proposition, we note that, by the argument of \eqref{removing w}
together with \cite[Lemma 6.20]{KT}, the action of global Hecke algebra $\gHecke$ 
on cohomology induces an action of $\gHecke$ on 
  on $H^*(Y(1), \Z_p)_{\mathfrak{m}}$.


\begin{prop} \label{P853}
  If   $H^{\BWq}(Y(1), \Z_p)_{\mathfrak{m}}  = \Z_p$,
then the 
image of the full global derived Hecke algebra $\gHecke$ inside $\End \ H^*(Y(1), \Z_p)_{\mathfrak{m}}$ in fact precisely coincides with the exterior algebra generated by $\mathsf{V}$,
and in particular the global derived Hecke algebra (acting on $\mathfrak{m}$-part of cohomology) is graded commutative.
 
This same conclusion of graded commutativity holds, more generally, when there exists a semisimple  $\Q_p$-algebra $\mathsf{S}$ of   (degree-preserving) endomorphisms of $H^*(Y(1), \Q_p)$
 commuting with $\gHecke$ and such that $H^{\BWq}(Y(1), \Z_p)_{\mathfrak{m}} \otimes \Q_p$ has multiplicity one as a $\mathsf{S}$-module.   \end{prop}}
 

 
 \begin{remark}
 \begin{itemize}
\item[-] {\color{\changecolor}  A natural choice for the commuting subalgebra $\mathsf{S}$ in Proposition \ref{P853} is
  the $\Z_p$-algebra generated by the local underived Hecke algebras at all primes that are not good.
  However, the multiplicity one condition is only realistic  when there is a  {\em unique} tempered representation $\pi_{\infty}$ of $\mathbf{G}(\R)$ with nontrivial $(\mathfrak{g}, \mathrm{K})$-cohomology.
  If this uniqueness condition is satisfied, then we would likely expect the multiplicity one condition to be valid in the great majority of cases. 
 






 

Under the assumptions we are currently working (simply connected group, and working over $\Q$) only $\SL_{2n+1}$
has this property. However, this unicity of $\pi_{\infty}$ in fact applies
whenever we work over a CM base field, or for $\PGL_n$ over $\Q$. \footnote{Note that, for $\PGL_n$ with $n$ even, 
one should enlarge $\mathsf{S}$ using the action of the component group of the archimedean maximal compact.} 
The analysis of \S \ref{Patching} -- \S \ref{reciprocity}
would extend to those cases with only some  notational changes.   } 
 
 
 
 

\item[-] That we get an {\em integral} isomorphism of $\gHecke$ and $\wedge^* \Vinf$, in the first statement of the Proposition, is an artifact of our simplifying hypotheses. We don't expect $\gHecke$
to be an integral exterior algebra in general, but corresponding statements should remain valid $\otimes \Q$. 
 
 In general,
 we would expect the $\gHecke$ to be $\mathbb{T} \otimes \wedge^* \mathsf{V}$, where $\mathbb{T}$
 is the usual Hecke algebra,   after tensoring with $\Q$. But here our assumptions mean that $\mathbb{T}$ is just $\Z_p$,
 and moreover that the conclusion is true integrally.
\end{itemize}
\end{remark}

\medskip







\subsection{Formulation of the conjecture}
We are now ready to state the conjecture, the formulation of which is the main point of this paper. 
(Although the trip was fun too.) 

The formulation of the conjecture itself rests on the conjecture of Langlands that associates  
to $\Pi$ a motive, or more precisely a system of motives indexed by representations of the dual group. 
 Unfortunately it is difficult to find a comprehensive account of this conjecture in print;  the reader may consult
the brief remarks in \cite{Langlands} or the appendix of \cite{PV}.  


Continue with notation as in Theorem \ref{maintheorem}.   
As in    the discussion of \S \ref{sec:MV} and \S \ref{reindexing},
let $M_{\coad}$ be the motive  with $\Q$ coefficients associated to $\Pi$ and the co-adjoint representation of $G^{\vee}$, if it  exists. {\em A priori},
one may not always be able to descend the coefficients of $M_{\coad}$ to $\Q$, although we expect this is possible in most if not all cases.  (See discussion
in \cite[Appendix, A.3]{PV}).  In what follows we assume that $M_{\coad}$ can indeed be descended to $\Q$ coefficients; if not 
one can simply reformulate the conjecture by replacing $\Q$ by a field extension. 


Thus there is an identification of Galois modules
$$ \mbox{ {\'e}tale realization of $M_{\coad}$}  \simeq \Ad^* \rho  \otimes \Q_p$$
 and there is 
 a regulator map   from the motivic cohomology 
 $$H^1_{\mot}(\Q, M_{\coad,\Z}(1)) \longrightarrow H^1_f(\Z[\frac{1}{S}], \Ad^* \rho(1)) \otimes  \Q_p.$$
  As in \S \ref{motivic chi}, the motivic cohomology group on the left-hand side has been restricted
to classes that extend to an integral model.
  We assume that this regulator map is an isomorphism.\footnote{
  In general, the appropriate conjecture is that the regulator, taken to the group of classes that are crystalline at $p$
  {\em and unramified at all primes in $S$}, is an isomorphism. However, by virtue of our assumptions in 
  \S \ref{GaloisAss}, part (e), it is not necessary to explicitly impose ``unramified at primes in $S$.''}
 Let $\mathsf{V}_{\Q_p} = \mathsf{V} \otimes  \Q_p$,
 and let $\mathsf{V}_{\Q}$ be those classes in $\mathsf{V}_{\Q_p}$
 whose pairing with  motivic cohomology
 lies in $\Q$. 
 
 Write $H^*(Y(1), -)_{\Pi}$ for the 
Hecke eigenspace for the character $\mathbb{T}_{K_0} \rightarrow \mathbf{Z}$
 associated with $\Pi$ (see \eqref{oort}).   Our assumptions imply that $H^*(Y(1), \Z_p)_{\Pi}
 = H^*(Y(1), \Z_p)_{\mathfrak{m}}$. 

\begin{conjecture}     \label{mainconjecture} 
 Notation as above. With reference to the action
 $$ \wedge^* \mathsf{V}_{\Q_p} \acts H^*(Y(1), \Q_p)_{\Pi}$$
 furnished by Theorem \ref{maintheorem}, the action of $\mathsf{V}_{\Q}$
 preserves $H^*(Y(1), \Q)_{\Pi}$. 
\end{conjecture} 



  Some rather scant evidence is discussed in the next section  (\S \ref{pisspoor}).   As we have mentioned in the introduction, 
  much more compelling is that we have been able
to obtain numerical evidence for a coherent analog of the conjecture, in a joint work with Michael Harris. 


 
 
  
 
Recall  (\S \ref{GaloisAss}) 
we assume that 





\begin{equation} \label{recall} H^0(\Q_p, \Ad \rhobar) = H^2(\Q_p, \Ad \rhobar) = 0\end{equation} 
which implies the same conclusions for $\Ad^* \rhobar(1)$. 
In  particular,  $H^1(\Q_p, \Ad^* \rho(1))$ is torsion-free and surjects
 onto $H^1(\Q_p, \Ad^* \rhobar(1))$. 
  Finally, $H^1_f(\Q_p, \Ad^* \rho(1))$ is a saturated submodule of $H^1(\Q_p, \Ad^* \rho(1))$ and we have an equality of ranks
 $$\mathrm{rank}_{\Z_p} H^1_f(\Q_p, \Ad^* \rho(1)) = \mathrm{rank}_{\mathbf{F}_p} H^1_f(\Q_p, \Ad^* \rhobar(1)),$$
 as follows from explicit computation. In particular, $H^1_f(\Q_p,\Ad^* \rho(1))$ surjects onto $H^1_f(\Q_p, \Ad^* \rhobar(1))$.  
Also   observe that, because of the assumed ``big image'' (\S \ref{GaloisAss} assumption (b)) of $\rhobar$, we have 
\begin{equation} \label{h00} H^0(\Z[\frac{1}{\ramprimes}], \Ad^* \rhobar(1)) = 0,\end{equation}
  and so $H^1(\Z[\frac{1}{\ramprimes}], \Ad^* \rho(1))$ is torsion-free. 

 \begin{lemma} \label{DeltaDimensional}  Both $ H^1_f(\Z[\frac{1}{\ramprimes}], \Ad^* \rho(1))$ and $\mathsf{V}$ are  free  $\Z_p$-modules of rank $\delta$.
 \end{lemma}
 \proof  
 
 First of all, because the Taylor--Wiles method in this case implies an $R=T$ theorem (see \eqref{first-iso})
 and  we are assuming   that the Hecke algebra is isomorphic to $\Z_p$  (see \eqref{nocong0}) we get from a tangent space computation that
 $H^1_f ( \Z[\frac{1}{\ramprimes}], \Ad \rhobar ) = 0.$
 We now apply Tate global duality to this statement. It implies  both the surjectivity of
\begin{equation} \label{sarge} H^1(\Z[\frac{1}{\ramprimes}], \Ad ^*  \rhobar(1)) \twoheadrightarrow \frac{ H^1(\Q_p, \Ad^* \rhobar (1)) }{ H^1_f(\Q_p, \Ad^* \rhobar (1)) }, \end{equation}
and  the injectivity  of
\begin{equation} \label{Vanishing} H^2(\Z[\frac{1}{\ramprimes}],\Ad^* \rhobar(1))  \hookrightarrow \underbrace{ \prod_{v \in \ramprimes} H^2(\Q_v, \Ad^* \rhobar(1)) }_{=0 \mathrm{  \ by  \ \S \ref{GaloisAss}}} \end{equation}
  so in fact $ H^2(\Z[\frac{1}{\ramprimes}],\Ad^* \rhobar(1))=0$. 
 

The surjectivity \eqref{sarge} holds also for $\Ad^* \rho(1)$, not just the mod $p$ reduction.
This follows because $H^1(\Z[\frac{1}{\ramprimes}], \Ad^* \rho(1))$ surjects onto  $H^1(\Z[\frac{1}{\ramprimes}], \Ad^* \rhobar(1))$, by \eqref{Vanishing};
and the induced map
$$\frac{ H^1(\Q_p, \Ad^* \rho (1)) }{ H^1_f(\Q_p, \Ad^* \rho (1)) }/p  \rightarrow \frac{ H^1(\Q_p, \Ad^* \rhobar (1)) }{ H^1_f(\Q_p, \Ad^* \rhobar (1)) } $$
is an isomorphism. 




 
 
The Euler characteristic formula, taken together with \eqref{h00}, \eqref{sarge} and \eqref{Vanishing}, allows one to compute  \begin{equation}
\label{EC} \dim H^1_f(\Z[\frac{1}{\ramprimes}], \Ad^* \rhobar \ (1)) = \delta.\end{equation}
Now examine  the short exact sequences  
 
 \begin{equation} \label{feeling_groovy1}
 \xymatrix{
H^1(\Z[\frac{1}{\ramprimes}], \Ad^*  \rho (1)) \ar[r]^{p}\ar[d]^j   & H^1(\Z[\frac{1}{\ramprimes}], \Ad^* \rho  (1))\ar[d]   \ar[r]  &H^1(\Z[\frac{1}{\ramprimes}], \Ad^* \rhobar (1))   \ar[d] \\
\frac{H^1(\Q_p,\Ad^* \rho (1))}{H^1_f (\Q_p, \Ad^* \rho(1))} \ar[r]^{p}   & \frac{H^1(\Q_p,\Ad^* \rho  (1))}{H^1_f(\Q_p,\Ad^* \rho  (1))} \ar[r] &\frac{H^1(\Q_p,\Ad^* \rhobar (1))}{H^1(\Q_p,\Ad^* \rhobar (1))} \\
 }
 \end{equation} 
 Since we have seen that $j$ is onto, 
 it follows that the induced maps of vertical kernels is a short exact sequence;
that and \eqref{EC} imply that
 $$ H^1_f(\Z[\frac{1}{\ramprimes}], \Ad^* \rho(1)) \simeq \Z_p^{\delta},$$
 as claimed. 
   \qed 
 
 


\subsection{ Cohomological vanishing in the  Taylor--Wiles method} \label{TWrecall} 
In  the Taylor--Wiles method we choose a set of primes $Q$ such that, with $SQ=  \ramprimes \cup Q$, we have the following properties:
\begin{itemize}
\item[(a)]  $Q$ is a Taylor--Wiles datum of some level, and
\item[(b)]  The map $H^1(\Z[\frac{1}{SQ}], \Ad \rhobar) \rightarrow \frac{H^1(\Q_p, \Ad \rhobar)}{H^1_f(\Q_p, \Ad \rhobar)}$ is surjective,
and the map $H^2(\Z[\frac{1}{SQ}], \Ad  \rhobar) \rightarrow \prod_{v \in Q} H^2(\Q_p, \Ad \rhobar )$ is injective. 


\end{itemize} 
(Recall that our local assumptions at $S$ mean there is no local cohomology there: \S \ref{GaloisAss}, assumption (e)). 






Observe also that if $Q$ is such a set of primes, and $Q'$ is a further set satisfying (a) and (b), then certainly $Q \cup Q'$ satisfies (a) and (b) too.
Indeed, the cohomological criteria of (b) are equivalent to asking that \begin{equation} \label{dual-inj} H^1_f(\Z[\frac{1}{SQ}], \Ad^* \rhobar \ (1)) \rightarrow \prod_{v \in Q} H^1(\Q_v, \Ad^* \rhobar(1))\end{equation}  is injective,  and this  is stable under enlarging $Q$ (it is equivalent to the same injectivity on $H^1_f(\Z[\frac{1}{S}], -)$,
since anything in the kernel would be unramified at $Q$). 

Now, if we choose a system of such data $Q_n$ of level $n$, we can 
(by passing to a subsequence and reindexing, e.g. as in \cite[\S 13.10]{GV}) achieve 
a new sequence $Q_n$ which satisfy the ``limit properties'' of \S \ref{extraction}.  

\begin{Definition} \label{TWconvgt}  \index{convergent (Taylor--Wiles data)}  
A sequence of Taylor--Wiles data $Q_n$ of level $n$ is called {\em convergent} if:
\begin{itemize} \item[-] $Q_n$ have  the cohomological properties stated in (b) above and, 
\item[-] One can pass to the limit in the sense of \S \ref{extraction}, i.e. there exists data $\Rinf, \Sinf, \Cinf, f_n, g_n$ etc. 
satisfying all the properties enumerated in \S \ref{extraction}.
\end{itemize}
 \end{Definition}
 
 In particular, any sequence of Taylor--Wiles data has a convergent subsequence, after reindexing the subsequence.

 


\subsection{The tangent spaces to $R$ and $S$} \label{tangentRS}
As in \S \ref{SR} both $\Rinf$ and $\Sinf$ are augmented to $\Z_p$:
$$ \Sinf \rightarrow \Rinf \rightarrow \Z_p,$$
and the composite $\Sinf \rightarrow \Z_p$ is the standard augmentation of $\Sinf$. 
 The kernel of these augmentations are denoted by $\Jinf \subset \Rinf$ and $\Iinf \subset \Sinf$. 
 
 
  First of all, we set let $\mathfrak{t}_{\Rinf}$ be the ``tangent space'' to $\Rinf$  {\em over $\Z_p$}, that is to say \index{$\mathfrak{t}_{\Rinf}$}
$$\mathfrak{t}_{\Rinf} \simeq \Hom_{*}(\Rinf, \Z_p[\varepsilon]/\varepsilon^2),$$ 
where the subscript $*$ means that the homomorphism lifts the natural augmentation $\Rinf \rightarrow \Z_p$.   Equivalently, $\Rinf$ is the derivations of $\Rinf/\Z_p$ into $\Z_p$, 
or the $\Z_p$-linear dual of $\Jinf/\Jinf^2$. 

We can make exactly the same definition for $\Sinf$.  The surjection $\Sinf \twoheadrightarrow \Rinf$ induces 
a surjection $\Iinf/\Iinf^2 \twoheadrightarrow \Jinf/\Jinf^2$ and thus 
 a natural injection $\mathfrak{t}_{\Rinf} \rightarrow \mathfrak{t}_{\Sinf}$ with saturated image (i.e. split). 
We write  $\Winf$ for the cokernel of the map on tangent spaces, so we have an exact sequence 
\begin{equation} \label{Vdef2}  \mathfrak{t}_{\Rinf} \hookrightarrow \mathfrak{t}_{\Sinf}  \twoheadrightarrow \Winf.  \end{equation} 
 Then $\Winf$ is a free $\Z_p$-module of rank $\delta$.
 
 

 
\subsection{Tangent spaces to $\usbR_n$ and $S_n$}  \label{tnRnSn}
 
 We suppose now that $Q_n$ are a convergent sequence (\S \ref{TWrecall}) of Taylor--Wiles data.  
  
Recall that $\Sinf, \Rinf$ are defined as ``limits,'' roughly speaking,
of rings $S_n \rightarrow \usbR_n$ that occur at level $Q_n$ in the Taylor--Wiles process.
We recall that $\usbR_n$ is not the full (crystalline at $p$) deformation ring  $R_{Q_n}$ at level $Q_n$, but is a ``very deep'' Artinian quotient of 
it. 

 These rings are also compatibly  augmented over $\Z/p^n$, i.e.
$$S_ n  \longrightarrow   \usbR_n \longrightarrow \Z/p^n$$
(see the bottom row of  \eqref{SinftySn}, and compose with the reduction of the map $\defring \rightarrow \Z_p$
which arises from our fixed automorphic representation $\Pi$). 

  
 


\begin{lemma}
The map  $R_{Q_n} \rightarrow \usbR_n$ 
induces an isomorphism  upon applying $\Hom_*(-, \Z/p^n[\varepsilon]/\varepsilon^2)$, 
where $\Hom_*$ means that the map lifts the natural augmentations to $\Z/p^n$. 
\end{lemma}
\proof
Write $A :=   \Z/p^n[\varepsilon]/\varepsilon^2$. 
A map $R_{Q_n} \rightarrow  A$ gives rise to a deformation 
 $\widetilde{\rho}_n: G_{\Q} \rightarrow G^{\vee}(\Z/p^n)$
 that lifts the modulo $p^n$ reduction of $\rho$.   


We want to show that $R_{Q_n} \rightarrow A$ must factor through  $\usbR_n$. 
To do so we must show (see \eqref{goef})  that
the map dies on the $K(n)$th power of the maximal ideal $\mathfrak{m}_{R_{Q_n}}$,
and also that $\rho_n$ automatically has inertial level $\leq n$ at primes in $Q_n$ (see page \pageref{inertial level} for definition). 

Note that the maximal ideal $(p, \varepsilon)$ of $\Z/p^n[\varepsilon]/\varepsilon^2$
satisfies $(p, \varepsilon)^{n+1} = 0$. Since $K(n)  \geq n+1$ by assumption,  we only need verify that $\widetilde{\rho}_n$ has inertial level $\leq n$
at all Taylor--Wiles primes. 
After suitably conjugating, we can suppose $\widetilde{\rho}_n|\Q_q$
to have image in $T^{\vee}$ (see Lemma \ref{TWdeflem}).  Restricted to inertia it takes image inside 
 the kernel of $T^{\vee}(\Z/p^n[\varepsilon]/\varepsilon^2) \rightarrow T^{\vee}(\Z/p^n)$; 
 this group has exponent $p^n$, and  so $\widetilde{\rho}_n$ has inertial conductor $\leq n$. 
\qed 






We also define $$\mathfrak{t}_{R_n} = \Hom_*(R_{Q_n}, \Z/p^n[\varepsilon]/\varepsilon^2).$$ 
  \index{$\mathfrak{t}_{R_n}$}    It doesn't matter whether we use $R_{Q_n}$ or $\usbR_n$ in this definition, as we just showed.
  Similarly we define $$\mathfrak{t}_{S_n} = \Hom_*(S_n, \Z/p^n[\varepsilon]/\varepsilon^2).$$  There is a natural map $\mathfrak{t}_{R_n} \rightarrow \mathfrak{t}_{S_n}$
  induced by $S_n \rightarrow \usbR_n$.  \index{$\mathfrak{t}_{S_n}$} 

Finally define  \index{$W_n$} 
\begin{equation} \label{Wndef} W_n = \mathrm{cokernel} \left( \mathfrak{t}_{R_n} \rightarrow \mathfrak{t}_{S_n}\right). 
\end{equation}


 

 

The maps $\Rinf \rightarrow \usbR_n$ and $\Sinf \rightarrow S_n$ give rise to an isomorphism 
of short exact sequences as below: 
 
 \begin{equation} \label{feeling_groovy2}
 \xymatrix{
 0 \ar[r] & \mathfrak{t}_{R_n} \ar[r]\ar[d]^{\alpha, \sim}  & \mathfrak{t}_{S_n} \ar[d]^{\beta,\sim}  \ar[r]  & W_n   \ar[d]^{\gamma, \sim} \ar[r] & 0  \\
 0 \ar[r] & \mathfrak{t}_{\Rinf}/p^n \ar[r]    &\mathfrak{t}_{\Sinf}/p^n  \ar[r] & \Winf/p^n  \ar[r] &0 \\
 }
 \end{equation} 
 
This requires some explanation.   

First of all,  we explain the maps.  Note first of all
that there is a natural map  $\mathfrak{t}_S/p^n \simeq \Hom_{*}(\Sinf, \Z/p^n[\varepsilon]/\varepsilon^2)$,
which is an isomorphism. Similarly for $\Rinf$. 
 This means that there are maps 
\begin{equation} \label{gogo}   \alpha: \mathfrak{t}_{S_n} \rightarrow \mathfrak{t}_{\Sinf}/p^n,   \beta:  \mathfrak{t}_{R_n} \rightarrow \mathfrak{t}_{\Rinf}/p^n\end{equation} 
that are induced by the projections $\Sinf \rightarrow S_n$ and $\Rinf \rightarrow \usbR_n$.
This explains $\alpha, \beta$; and the map $\gamma$ is the induced map on cokernels.  

Next we see that $\alpha, \beta, \gamma$ are isomorphisms. 

For $S$ this is the assertion that homomorphism $\Sinf \rightarrow \Z/p^n[\varepsilon]/\varepsilon^2$ 
factors through $S_n$. Indeed,  referring to the coordinate presentation \eqref{explicit} and \eqref{Sinfdef},  each element $x_i$ must go to   $a\varepsilon$ for some $a \in \Z/p^n$, 
and then $(1+x_i)^{p^n}$ is carried to $(1+a \varepsilon)^{p^n} = 1$. 
For $R$, we use the fact \eqref{second-iso}    that   we can identify $\usbR_n$ with $\Rinf\otimes_{\Sinf} S_n$. 
As above, any homomorphism $\Sinf \rightarrow \Z/p^n[\varepsilon]/\varepsilon^2$  (lifting the augmentation) factors through
$S_n$,  and in particular any homomorphism $\Rinf \rightarrow \Z/p^n$, lifting the natural one,
factors  through $\usbR_n$. 

Now, the bottom row is exact, by definition and the freeness of $\Winf$. The top row
is exact at the left because the  vertical maps $\alpha, \beta$ are isomorphisms,
and exact at the right by definition. 
Then it follows that $\gamma$ is an isomorphism too. 

This concludes the explanation of diagram \eqref{feeling_groovy2}.



\subsection{Tangent spaces  to $S_n$ reinterpreted}
Let us reinterpret the tangent space to $S_n$ in a few different  (canonical) ways. 

\label{DDR REF1}


By \eqref{coocoo} we have an isomorphism








\begin{equation}\label{ExtT} \mathfrak{t}_{S_n} \simeq \Ext^1_{S_n}(\Z/p^n, \Z/p^n)\end{equation} 

Now $S_n$ was, by definition (\S \ref{sec:diamond}) , the $\Z/p^n$- group algebra of the group $T_n$; thus, from the above equation,  we get a canonical isomorphism
\begin{equation} \label{tsnTn}\mathfrak{t}_{S_n} \simeq H^1(T_n, \Z/p^n).\end{equation}
 
 Next we connect $\mathfrak{t}_{S_n}$ to Galois cohomology. Recall from  Lemma \ref{TWdeflem}
  that, for any $q \in Q_n$, a deformation of $\rho|G_{q}$
can be conjugated to lie in the torus, and in particular factors through the profinite completion of $\Q_q^{\times}$. 
Now we can identify $H^1(G_q, \Ad \ \rho_n)$
with the set of lifts  of $\rho_n$ to $G^{\vee}(\Z/p^n[\varepsilon]/\varepsilon^2)$, modulo conjugacy. 
This lift sends tame inertia to the kernel of reduction modulo $\varepsilon$. 
In particular, having fixed an element of $T^{\vee}(k)$ conjugate to $\rhobar(\mathrm{Frob}_q)$, we get a canonical isomorphism 
\begin{equation} \label{TqH} \frac{ H^1(\Q_q, \Ad \rho_n)}{H^1_{\ur}(\Q_q, \Ad \rho_n) } \simeq 
\mathrm{Hom}\left( \ \mathbf{F}_q^{\times},  
\mathrm{Lie}(T^{\vee}) \otimes \Z/p^n\right)\end{equation}
Identifying the the Lie algebra
with $X_*(T^{\vee})$, we get 
\begin{equation}   \label{brst}
 \frac{ H^1(\Q_q, \Ad \rho_n)}{H^1_{\ur}(\Q_q, \Ad \rho_n) }  \simeq \Hom(\mathbf{F}_q^{\times}/p^n,  \Z/p^n) \otimes X_*(T^{\vee})  \simeq \Hom(\underbrace{X_*(\mathbf{A}) \otimes \mathbf{F}_q^{\times}/p^n}_{\mathbf{A}(\mathbf{F}_q)/p^n}, \Z/p^n)\end{equation} 
(here the subscript ``ur'' means unramified) and thus, from \eqref{idontcare} and  \eqref{tsnTn} 
\begin{equation} \label{tSn Galois} \mathfrak{t}_{S_n} \simeq  \bigoplus_{q \in Q_n}  \frac{ H^1(\Q_q, \Ad \rho_n)}{H^1_{\ur}(\Q_q, \Ad \rho_n)} \end{equation} 
where we emphasize that the isomorphism depends on the choice of  an element of $T^{\vee}(k)$ conjugate to Frobenius at $q$, for each $q \in Q_n$. 
 
  


  There is an isomorphism similar to \eqref{ExtT} for
 $\mathfrak{t}_{\Sinf}$; in particular,
 $ \mathfrak{t}_{\Sinf} \simeq \Ext^1_{\Sinf}(\Z_p, \Z_p)$
 and more usefully
$$ \mathfrak{t}_{\Sinf}/p^n \simeq \Ext^1_{\Sinf}(\Z_p, \Z/p^n)$$

 
The composite
 \begin{equation} \label{compositemap} \Ext^1_{S_n}(\Z/p^n, \Z/p^n)  {\longrightarrow} \Ext^1_{\Sinf}(\Z/p^n, \Z/p^n) \rightarrow \Ext^1_{\Sinf}(\Z_p, \Z/p^n).\end{equation}













gives the natural identification  -- map $\beta$ from \eqref{feeling_groovy2}
 -- of $\Ext^1_{S_n}(\Z/p^n, \Z/p^n) = \mathfrak{t}_{S_n}$
 with $ \Ext^1_{\Sinf}(\Z_p, \Z/p^n) = \mathfrak{t}_{\Sinf}/p^n$.
 
 
 





\subsection{$V_n$ and Galois cohomology} \label{Vnhstar}

\label{DDR REF2}

  We  exhibit now a canonical surjection 
\begin{equation} \label{tsnvsurj}  \mathfrak{t}_{S_n} \twoheadrightarrow \Vinf/p^n\end{equation}
In fact, this surjection uses no more than the fact that $Q_n$ is a Taylor--Wiles datum. If we suppose
that $Q_n$ are a convergent sequence (\S \ref{TWrecall}) of Taylor--Wiles data,   we will see that this actually descends to an isomorphism
\begin{equation} \label{brrr} W_n  \simeq \Vinf/p^n,\end{equation}
    i.e. $W_n$ (defined in \eqref{Wndef})  is isomorphic to $ \Hom( H^1_f(\Z[\frac{1}{S}], \Ad^* \rho \ (1)  ), \Z/p^n)$.     
     
  
 
  As before, let $SQ_n$ be the union of the set $\ramprimes$ with the set $Q_n$.   Examine: 
  \begin{equation}
 \xymatrix{
 \Hom_{*}(R_{Q_n}, \Z/p^n[\varepsilon]/\varepsilon^2) \ar[r] \ar[d]^{\sim} & \Hom_{*}(S_n, \Z/p^n[\varepsilon]/\varepsilon^2) \ar[r]\ar[d]^{\sim} &  W_n \ar[d]^{=}\\ 
  H^1_f(\Z[\frac{1}{SQ_n}], \Ad \rho_n)  \ar[r]^{\varphi} &     \prod_{v \in Q_n} \frac{H^1(\Q_v, \Ad \rho_n)}{H^1_{\mathrm{ur}}(\Q_v, \Ad \rho_n)}   \ar[r] &  W_n.
 
 }
 \end{equation} 
 The first  vertical map is just the computation of tangent spaces  to deformation rings (working over $\Z/p^n$ rather than a field),  the second vertical map 
 is \eqref{tSn Galois}, and $\varphi$ is restriction in Galois cohomology.
 
 There is now a natural pairing :\begin{equation} \label{pairing}  H^1_f(\Z[\frac{1}{\ramprimes}], \ \Ad^* \rho_n \ (1)) \times W_n \longrightarrow \Z/p^n \end{equation}
which, we emphasize again, depends on the choice of toral elements conjugate to Frobenius at each prime in $Q_n$. 
To  be explicit,  
an element of $W_n$ is represented by a collection
 $$(\beta_v) \in  \prod_{v \in Q_n} \frac{H^1(\Q_v, \Ad \rho_n)}{H^1_{\mathrm{ur}}(\Q_v, \Ad \rho_n)},$$  modulo $\mathrm{image}(\varphi)$;  
to pair $\alpha \in H^1_f(\Z[\frac{1}{\ramprimes}], \Ad ^* \rho_n(1))$ with  $(\beta_v)_{v \in Q_n}$ 
 we take the sum of local pairings
\begin{equation} \label{abovemoo}   (\alpha, (\beta_v)_{v \in Q_n}) \mapsto \sum (\alpha_v, \beta_v)_v\end{equation}
where the local pairing is defined by restricting $\alpha$ to $\Q_v$ and using local reciprocity. 
This pairing \eqref{abovemoo} is well-defined because each $\alpha_v$, i.e. the restriction of $\alpha$ to $\Q_v$,  is actually unramified.   Moreover, if the collection $(\beta_v)$ come from a class in $H^1_f(\Z[\frac{1}{SQ_n}], \Ad \rho_n)$, 
the value of \eqref{abovemoo} is zero by global reciprocity: our local assumptions means that the local pairings
for $v \in \ramprimes$ vanishes.   Thus the pairing \eqref{abovemoo} descends to the quotient of
$\prod_{v \in Q_n} H^1$ by $\mathrm{image}(\varphi)$. 
 This concludes our discussion of \eqref{pairing}. 
 
We have also seen (\S  \ref{tnRnSn},  and similar arguments to Lemma \ref{DeltaDimensional}) that both $W_n$ and $H^1_f(\Z[\frac{1}{\ramprimes}], \Ad^*  \rho_n \ (1))$ are free $\Z/p^n$-modules of dimension $\delta$. 
Let us check that     \eqref{pairing} is a perfect pairing of $\Z/p^n$ modules, i.e.
the map
$$ W_n \rightarrow H^1_f(\Z[\frac{1}{\ramprimes}], \Ad^* \rho_n (1))^{\vee}$$
is an isomorphism, where $\vee$ means homomorphisms to $\Z/p^n$.   Since both sides have the same size, it is enough to check that the map  
is surjective, and thus enough to show that the induced map
\begin{equation} \label{lunytunes} \mathfrak{t}_{S_n} \rightarrow H^1_f(\Z[\frac{1}{\ramprimes}], \Ad^* \rhobar \ (1))^{\vee}\end{equation} 
is surjective, where $\vee$ now means homomorphisms to $\Z/p$. 

  Now the Taylor-Wiles set $Q_n$ is chosen \eqref{dual-inj} so that 
 $ H^1_f(\Z[\frac{1}{\ramprimes}],  \Ad^* \rhobar \ (1)) \hookrightarrow \prod_{v \in Q_n} H^1(\Q_v, \Ad^* \rhobar(1))$.
 The image of this map consists of classes unramified at $Q_n$, so we also have
  $$H^1_f(\Z[\frac{1}{\ramprimes}], \Ad^* \rhobar\ (1)) \hookrightarrow \prod_{v \in Q_n} H^1(\Q_v, \Ad^* \rhobar(1))^{\mathrm{ur}}$$
When we dualize this, and apply local duality at primes in $Q_n$,  we get the surjectivity of \eqref{lunytunes}. 

 

























 

 
\subsection{The injection $H^1(T_q) \hookrightarrow \mathscr{H}_q^{(1)}$} \label{Vnaction}  
 
 
 In this section, we suppose that $Q_n$ is a Taylor--Wiles datum of level $n$, but do not assume  that it is part of a convergent sequence (\S \ref{TWrecall}) of Taylor--Wiles data. 
 Let $q \in Q_n$, thus equipped with $\Frob_q^T \in T^{\vee}(k)$.   We will work exclusively with $S=\Z/p^n$ coefficients. 
   As before, $\mathscr{H}_q$ denotes the local derived Hecke algebra at $q$, and $\mathscr{H}_q^{(1)}$ denotes its degree $1$ component. 
   Let
   $T_q = \mathbf{A}(\F_q)/p^n.$ 
   
 
 We are going to describe the map \eqref{iotaqndef1}, which is necessary for the formulation of the Theorem. 
More precisely, we are going to describe a map \begin{equation} \label{thetaref} \theta: H^1(T_q) \rightarrow  \left( \mathscr{H}_q^{(1)}\right)_{\mathfrak{m}},\end{equation}
  where the subscript means that we complete at the ideal of the Hecke algebra  (i.e., the degree zero component of $\mathscr{H}_q$) 
 corresponding to $\mathfrak{m}$. 
 
 The easiest way to think about $\theta$ is probably through  the following property: 
for each $\alpha \in H^1(T_q)$, the action of $\theta(\alpha)$ on $H^*(Y(1), \Z/p^n)_{\mathfrak{m}}$ is thus: 
   \begin{equation}  \label{explicit-action} \mbox{Pullback to $Y_0(q)$, project
 to $\Frob^T_q$-eigenspace,  cup with  $\alpha$,  pushdown to $Y(1)$. } \end{equation} 
 where the projection is done
 with reference to the splitting 
 of Corollary \ref{MoritaCor}.  
 
  The formal definition of the map $\theta$ is given in
\eqref{embedH1T}, and the validity of \eqref{explicit-action} will follow from the Lemma below.

  
 
 \medskip
 
 The Satake isomorphism of \S \ref{Satake} gives
 $$\mathscr{H}_q \stackrel{\sim}{\longrightarrow}  \left(  S[X_*] \otimes  H^*(\mathbf{A}(\F_q) ) \right)^W$$
 and in particular with $\Z/p^n$ coefficients the map $H^1(T_q) \rightarrow H^1(\mathbf{A}(\F_q))$ is an isomorphism, so 
  $$\mathscr{H}_q ^{(1)}\stackrel{\sim}{\longrightarrow}  \left(  S[X_*] \otimes  H^1(T_q ) \right)^W$$

 
 Now $\Frob_q^T \in T^{\vee}(k)$ gives a map $X_*(\mathbf{A}) = X^*(T^{\vee}) \rightarrow k^{\times}$, 
 i.e. it gives rise to a character $\chi_{\Frob_q^T}: S[X_*] \rightarrow k$.  The pullback of this to $S[X_*]^W$
 defines the maximal ideal $\mathfrak{m}$ (using the Satake isomorphism). 
 Let us denote by $\widetilde{\mathfrak{m}}$ the extension of the ideal $\mathfrak{m}$ back to $S[X_*]$;
 we caution that it is  no longer maximal, and rather it cuts out $\Frob_q^T$ together with all its $W$-conjugates. 
 We have an identification of completions
\begin{equation} \label{wsplit} S[X_*]_{\widetilde{\mathfrak{m}}} \cong \bigoplus_{w \in W} S[X_*]_{w \chi},\end{equation}
where we have denoted by $S[X_*]_{w\chi}$ the completion of $S[X_*]$ at the maximal ideal
that is the kernel of $w \chi$.

Next 
the natural inclusion  
\begin{equation} \label{inc}   \left( S[X_*] \otimes H^*(T_q) \right) ^{W} \hookrightarrow S[X_*] \otimes H^*(T_q) \end{equation}
induces the first map of  
\begin{equation} \label{composite iso}  \left( S[X_*] \otimes H^*(T_q) \right) ^{W}_{\mathfrak{m}} \stackrel{\eqref{inc}}{   \rightarrow}   S[X_*]_{\widetilde{\mathfrak{m}}} \otimes H^*(T_q) \stackrel{\eqref{wsplit}}{\rightarrow}  S[X_*]_{\chi} \otimes H^*(T_q). \end{equation}  
The composite map of \eqref{composite iso} is an isomorphism, and thus by composing with the Satake isomorphism we get an isomorphism
\begin{equation} \label{ciso2} \left( \mathscr{H}_q^{(1)} \right)_{\mathfrak{m}} \stackrel{\sim}{\rightarrow} S[X_*]_{\chi} \otimes H^1(T_q). \end{equation} 
 
 
 We then define the map $\theta: H^1(T_q) \rightarrow \left( \mathscr{H}_{q}^{(1)}\right)_{\mathfrak{m}} $ by the rule  
\begin{equation} \label{embedH1T} \theta:  h \in H^1(T_q) \mapsto 1 \otimes h \in S[X_*]_{\chi} \otimes H^1(T_q) \stackrel{\eqref{ciso2}^{-1}}{\longrightarrow}  \left( \mathscr{H}_{q}^{(1)}\right)_{\mathfrak{m}} \end{equation} 
where the superscript $1$ refers to cohomological degree, and the final map is the inverse of \eqref{ciso2}.
   Note that this embedding depends on the choice of $\Frob^T_q$; if we 
replace $\Frob^T_q$ by $w \Frob^T_q$ then the embedding is modified by means of the natural action of $w$ on $T_q$. 


This concludes the description of the map $H^1(T_q) \rightarrow \mathscr{H}_q^{(1)}$.  We now want    to justify \eqref{explicit-action}.     For this
we will describe an explicit preimage of $\theta(\alpha)$ under the map  
\begin{equation} \label{blastfromthepast} \left( \mathrm{H}_{KI}  \otimes \mathscr{H}_I  \otimes \mathrm{H}_{IK} \right)  \rightarrow   \mathscr{H}_K \end{equation}
in the case of the group $\G(\Q_q)$, where notation is as before (see, e.g. the proof of Theorem \ref{mindegreeproof});



note that $\mathscr{H}_K$ coincides
with what was previously called $\mathscr{H}_q$. 
Observe that everything here is a compatibly a module under the center of $\mathrm{H}_{II}$,   which 
is identified (\S 
\ref{Zdis})
with $S[X_*]^W$. In particular, it makes sense to complete at $\mathfrak{m}$. 


Now let $e_{\lambda} \in \mathrm{H}_{II}$ correspond to the characteristic function of $I_q \lambda  I_q$, where $\lambda \in X_*$.
Then $\lambda \mapsto e_{\lambda}$ defines an embedding $S[X_*] \rightarrow \mathrm{H}_{II}$, and, completing,
an embedding
\begin{equation} \label{completed embedding} S[X_*]_{\widetilde{\mathfrak{m}}} \rightarrow (\mathrm{H}_{II})_{\mathfrak{m}} \end{equation}

As before (\S \ref{Iwahori}) we let $e_K$ be   the characteristic function of $K_q$, divided by its measure; 
if we write $e_w$ for the characteristic function of $I_q w I_q$, we have $e_K = \frac{1}{|W|} \sum_{w \in W} e_w$. 
It can be considered, as in \S \ref{Iwahori}, as an element of $\mathrm{H}_{KI}$ or $\mathrm{H}_{IK}$. 

Also $|W|   e_K e_{\lambda}   \in \mathrm{H}_{KI}$ 
{\color{\changecolor} (i.e.  the product of $|W| e_K \in \mathrm{H}_{KI}$ with $e_{\lambda} \in \mathrm{H}_{II}$)} corresponds to the characteristic function of $I_q \lambda K_q$.  

\begin{lemma} \label{Theta explicit}
 Let $\Theta  \in  S[X_*]_{\widetilde{\mathfrak{m}}}$
 be chosen so that it projects under \eqref{wsplit} to the identity in $S[X_*]_{\chi}$
 and to zero in all $S[X_*]_{w \chi}$, for $w \in W$ not the identity.  
We use the same letter for its image $\Theta \in  (\mathrm{H}_{II})_{\mathfrak{m}}$
 under \eqref{completed embedding}. 
 
 
For $h \in H^1(T_q)$ let $\langle h \rangle$ be the associated element of $\mathscr{H}_{I}^{(1)}$, i.e.
$\langle h \rangle$ is supported on the identity double coset of $I$, and 
the associated cohomology class is obtained from $h$ by means of the restriction isomorphism
$H^1(I) \stackrel{\sim}{\rightarrow} H^1(T_q)$. 

  
Then the $\mathfrak{m}$-completion of
 \eqref{blastfromthepast} sends  $|W|  e_K \Theta \otimes \langle h  \rangle \otimes  e_K$  to $\theta(h)$.
  \end{lemma}
  
  
  {\color{\changecolor} As above, the product $e_K \Theta$ is understood as the product of $e_K \in \mathrm{H}_{KI}$ with $\Theta \in \mathrm{H}_{II}$. }
   In words, this amounts precisely to the description \eqref{explicit-action}   for $\theta$,  taking into account that $\Theta$ realizes
 precisely the  projection onto the $\Frob_q^T$ component for the splitting \eqref{bigsplit}.  
  
 \proof 
 
 
 
 
  
Consider the map (no completions, at the moment)    
\begin{equation} \label{compo}  \left( \mathrm{H}_{KI}  \otimes \mathscr{H}_I^{(1)}  \otimes \mathrm{H}_{IK}  \right)  \rightarrow   \mathscr{H}_K^{(1)} \rightarrow \left(  S[X_*] \otimes  H^1(T_q ) \right)^W\end{equation} 
  We show it sends $A := e_{K} e_{\lambda} \otimes \langle h \rangle  \otimes e_K$, for $\lambda$ dominant,   to the ``$W$-average'' of $\lambda \otimes h$,
i.e. $ |W|^{-1} \sum_{w \in W} w \cdot (\lambda \otimes h)$.
  
   The claimed result will follow easily from this: Consider an element $\Theta' = \sum c_{\lambda} \lambda \in S[X_*]$
 with the property that $c_{\lambda}$ is nonzero only for $\lambda$ dominant, and also $\Theta \equiv \Theta'$ modulo some high power of $\widetilde{\mathfrak{m}}$. 
Our claim implies that  $|W|   e_K \Theta'  \otimes \langle h \rangle \otimes e_K$ is sent to the  sum of Weyl translates of $\sum c_{\lambda} (\lambda \otimes h)$. 
The image of $\sum c_{\lambda} (\lambda \otimes h)$ in $\bigoplus_{w \in W} S[X_*]_{w \chi} \otimes H^1(T_q)$  is
 very close to  $1 \otimes h$ in the $w=1$ factor, and very close  to zero in the other factors; 
 after summing over $W$, its projection  
 to the $w=1$ factor remains very close  to $1 \otimes h$.
  Here ``very close'' is taken in the topology
 of the complete local rings $S[X_*]_{w \chi}$. 
In other words, $\theta(h)$ and the image of $|W|   e_K \Theta'  \otimes \langle h \rangle \otimes  e_K$ 
 under \eqref{blastfromthepast}  and \eqref{ciso2} are very close;
 in the limit, this  shows the desired result. 
 
 We will now consider  everything in the ``function model'' of \S \ref{desc2}. 
 Let $a_1 \in \mathrm{H}_{KI}, a_2 \in \mathrm{H}_{IK}$ be the images of $e_K e_{\lambda} , e_K$ in the function model. Then 
 $a_1$ corresponds to  the function sending $(xK, yI)$ to $|W|^{-1}$ precisely when $I y^{-1} x K= I \lambda K$, 
 
 
 
 equivalently $K x^{-1} y I = K \lambdabar I$, where we write $\lambdabar \in X_*$ for the negative of $\lambda$.
 Also $a_2$ 
 corresponds to  the function $(xI, yK)$ which is $1$ exactly when $xK = yK$.   
\begin{comment} { \color{\changecolor} Explanation: at the measure level, $e_K e_{\lambda}$ is a measure supported on $K \lambda I$ of total mass equal to the total mass of $I \lambda I$.
 Now the measure of $K \lambda I$ and the measure of $I \lambda I$ differ by $W$, so as a function it has value $|W|^{-1}$ everwyhere.} \end{comment}
 Moreover, the function $\langle h \rangle$ is supported on the diagonal in $G/I$ and sends $(I, I)$ to $h \in H^1(T_q) \simeq H^1(I)$. 
  
 The second map of \eqref{compo} is  given by restricting arguments to the torus,
 and restricting cohomology classes to $T_q$. 
   We can compute this restriction using the ``localization'' results of \S \ref{dhLocalization};
   these results assert that  restriction to the torus actually preserves multiplication. 
   
  \begin{comment}
 {  \color{blue} { 
   
   
   
 $$A (\mu K,  K) = \sum_{  y \in   \tilde{W}} a_1(\mu K,yI) \langle h \rangle (yI,yI)  a_2(yI,  K)$$
 The first term is nonzero only 
 for those $y$ satisfying $I y^{-1} \mu K=I \lambda K$, i.e.
 $y^{-1} \mu \in \tilde{W} \in I \lambda K$. 
 This implies that $y^{-1} \mu = \lambda w$ with $w \in W$,
 i.e. $y = \mu w^{-1} \lambda^{-1}  = w \cdot (w \mu -\lambda)$. 
 
So this equals 
 $$ = |W|^{-1} \sum_{w \in W} \langle h \rangle ( \dots)  \underbrace{ a_2(   \mu w^{-1} \lambda^{-1} I,   K) }_{=a_2(w^{-1} \lambda^{-1} I, \mu^{-1} K) $$
 The final term is nonzero (and equals $1$) exactly when $w^{-1} \lambda^{-1} K  = \mu^{-1} K$.   Now both $\lambda, \mu$ are dominnat. 
 Thus  this only happens if $\lambda = \mu$ and $w \in W_{\mu}$: 
\begin{equation} \label{Derived} A(K,  \mubar K) =   |W|^{-1} \delta_{\lambda \mu}  \sum_{w \in W_{\mu}} \langle h \rangle (w \lambdabar I, w \lambdabar I) \end{equation} 
   On the right, $\langle h \rangle (w \lambda I, w \lambda I) \in H^1(T_q)$
equals   $w \cdot h \in H^1(T_q)$.  

   }}
   
 \end{comment}
   
   
   
We restrict to the torus. Suppose that $\mu \in X_*$  is  dominant, with negative $\mubar \in X_*$.  We compute: 

 $$A (K,\mubar K) = \sum_{  y \in   \tilde{W}} a_1(K,yI) \langle h \rangle (yI,yI)  a_2(yI, \mubar K)$$
 The first term is nonzero only 
 for those $y$ satisfying $K y I = K \lambdabar I$, i.e. $y \in \tilde{W} \cap K  \lambdabar I$. 
This implies that
  $y = w \lambdabar$, with $w \in W$. 
So this equals 
 $$ = |W|^{-1} \sum_{w \in W} \langle h \rangle (w \lambdabar I, w \lambdabar I) a_2(w \lambdabar I, \mubar K)  $$
 The final term is nonzero (and equals $1$) exactly when $\mubar K  =  w \lambdabar K$.    Recall  that both $\lambda$ and $\mu$ are dominant.
  Thus  this only happens if $\lambda = \mu$ and $w \in W_{\mu}$: 
\begin{equation} \label{Derived} A(K,  \mubar K) =   |W|^{-1} \delta_{\lambda \mu}  \sum_{w \in W_{\mu}} \langle h \rangle (w \lambdabar I, w \lambdabar I) \end{equation} 
   On the right, $\langle h \rangle (w \lambda I, w \lambda I) \in H^1(T_q)$
equals   $w \cdot h \in H^1(T_q)$.  

Now, the image of $A$ under the derived Satake map
is the $W$-invariant element of the derived Hecke algebra of the torus
defined by
  $$\mu \mapsto \mbox{restriction to $T_q$ of }A(\mu K,   K).$$
As we have just computed,   for $\mu$ dominant, $A(\mu K, K) = A(K, \mubar K)$   is nonvanishing only when $\mu=\lambda$, where its value is $|W|^{-1} \sum_{w \in W_{\mu}} wh$. 
Therefore the image of $A$ under \eqref{compo} is the $W$-average of $\lambda \otimes h$ as claimed. 
\qed 



\subsection{Producing an action of $\Vinf/p^n$ on the cohomology at level $1$} \label{tSnaction} 
Let $Q_n$ be a convergent sequence of Taylor--Wiles data (\S \ref{TWrecall}). For each integer $n$ we 
will produce an action of $\Vinf/p^n$
on   automorphic cohomology $H^*(Y(1), \Z/p^n)_{\mathfrak{m}}$. 
 {\em A priori} these actions will not be guaranteed to be compatible with one another; later
 we will see at least that they ``converge as $n \rightarrow \infty$'' to give an action of $\Vinf$ on $H^*(Y(1), \Z_p)_{\mathfrak{m}}$. 

More exactly, we
begin by constructing an action of $\mathfrak{t}_{S_n}$, then prove (the Lemma below)
that it factors through $W_n$, and finally we have identified $W_n \simeq \Vinf/p^n$ in \eqref{brrr}. 
This gives the desired action, and we will discuss the ``convergence as $n \rightarrow \infty$'' in the next section.

Thus, let $Q_n$ be a convergent sequence of Taylor--Wiles data.  

 
We have   \begin{equation} \label{embed} \mathfrak{t}_{S_n} \stackrel{\eqref{tsnTn}}{\cong} H^1(T_n, \Z/p^n) \stackrel{\eqref{thetaref}}{\hookrightarrow} \mbox{degree $1$ component of }\otimes_{q \in Q_n}  \left(  \mathscr{H}_q\right)_{\mathfrak{m}} ,\end{equation}
where   the Hecke algebras are taken with $\Z/p^n$ coefficients. The composite embedding will be denoted
\begin{equation} \label{iotaQndef}  \iota_{Q_n}: \mathfrak{t}_{S_n} \rightarrow  \otimes_{q \in Q_n} \left(  \mathscr{H}_q\right)_{\mathfrak{m}}.\end{equation}

This gives rise to an  action of $ \mathfrak{t}_{S_n}$
by degree $+1$ endomorphisms of  automorphic cohomology
$H^*(Y(1), \Z/p^n)_{\mathfrak{m}}$, whose explicit description is essentially that already given in 
\eqref{explicit-action}, just replacing the role of one prime by many.  




 

The embedding \eqref{tsnTn} and so also this action depends on the choice of elements $\Frob_q^T \in T^{\vee}(k)$ for each prime $q \in Q_n$. 
Should we modify $\Frob_q^T$ by an element $w_q \in W$, the Weyl group, the action of $\mathfrak{t}_{S_n}$
is also modified (see  comments after \eqref{embedH1T})  by the action of $w_q$  in the obvious way.  
 
 \begin{lemma} 
   \label{Vnfactor}
   Let $Q_n$ be a convergent sequence of Taylor--Wiles data, as in Definition \ref{TWconvgt}.    
   Then, for each $n$, 
the action of $\mathfrak{t}_{S_n}$ on $H^*(Y(1), \Z/p^n)_{\mathfrak{m}}$  (via $\iota_{Q_n}$)  is trivial on the image of $\mathfrak{t}_{R_n}$, and thus  factors through the map $\mathfrak{t}_{S_n} \rightarrow  W_n$. 
  \end{lemma}
  
  \proof 
 Consider the diagrams \eqref{previousstory} of our previous story, now with identifications with $\mathfrak{t}_S$ and $\mathfrak{t}_{S_n}$ included: 
 \begin{equation} \label{BigDog}
 \xymatrix{
 H^*(\Hom_{\Sinf}(\Cinf, \Z_p))^{} \ar[d]^{=} & \times  &   \protect\overbrace{ \Ext^1_{\Sinf}(\Z_p, \Z_p) }^{\mathfrak{t}_{\Sinf}}\owns \tilde{v} \ar[d]  \ar[r] &  H^*(\Hom_{\Sinf}(\Cinf, \Z_p)) \ar[d] \\ 
   \tilde{x} \in H^*(\Hom_{\Sinf}(\Cinf, \Z_p))   \ar[d]^{V}  &  \times&  \Ext^1_S(\Z_p, \Z/p^n)     \owns  v \ar[r]  &   H^*(\Hom_{\Sinf}(\Cinf,  \Z/p^n))\ar[d]^{=}  \\
x \in  H^*(\Hom_{\Sinf}(\Cinf, \Z/p^n))^{}   & \times & \left( \Ext^1_{\Sinf}(\Z/p^n, \Z/p^n) \right) \ar[r]   \ar[u]^U  &  H^*(\Hom_{\Sinf}(\Cinf, \Z/p^n))   \\
 H^*(\Hom_{S_n}(\Cinf \otimes_{\Sinf} S_n, \Z/p^n))^{} \ar[u]^{\sim} & \times  &  \protect\underbrace{ \left( \Ext^1_{S_n}(\Z/p^n, \Z/p^n) \right) }_{\mathfrak{t}_{S_n}} \ar[r] \ar[u] &  \ar[u]^{\sim} H^*(\Hom_{S_n}(\Cinf \otimes_{\Sinf} S_n, \Z/p^n)). \\
  }
  \end{equation}
  

  
     
   In particular,   let $x \in  H^*(\Hom_{S_n}(\Cinf \otimes_{\Sinf} S_n, \Z/p^n)) $ be liftable to $\tilde{x} \in  H^*(\Hom_{\Sinf}(\Cinf, \Z_p))$;
   let $v \in \mathfrak{t}_{S_n} \simeq \mathfrak{t}_{\Sinf/p^n}$ be lifted to $\tilde{v} \in \mathfrak{t}_S$. Then the image of $(x,v)$
   in the bottom row is obtained from projecting the image of $(\tilde{x}, \tilde{v})$ at the top row. 
   



   Let us recall from \S \ref{extraction} part (g)  that $\mathsf{C}$ is quasi-isomorphic to $\mathsf{R}$ as an $\mathsf{S}$-module in a single degree.  
   Thus we can explicitly compute what goes on in the top row. This explicit computation
   (see Lemma  \ref{KoszulExtComputation} in Appendix \S \ref{AppendixB}) shows that 
   any element   $\tilde{v} \in \mathfrak{t}_{\Sinf}$
that lies in the image of $\mathfrak{t}_{\Rinf}$  acts {\em trivially}  on $H^*(\Hom_{\Sinf}(\Cinf, \Z_p))$.

 For later use, note that these  explicit computations also show that 
\begin{equation} \label{watney} \mbox{ $H^*(\Hom_{\Sinf}(\Cinf, \Z_p))$ 
is free over
$\wedge^* \mathfrak{t}_{\Sinf}/\mathfrak{t}_{\Rinf}$.} \end{equation}

From 
\eqref{feeling_groovy2}
it then follows that 
 $\mathrm{image}(\mathfrak{t}_{R_n} \rightarrow \mathfrak{t}_{S_n})$  
acts trivially on  $$H^*(\Hom_{S_n}(\Cinf \otimes_{\Sinf} S_n, \Z/p^n)) \simeq H^*(Y_0(Q_n), \Z/p^n)_{\mathfrak{m}, \Frob^T},$$
where the action of $\mathfrak{t}_{S_n} = H^1(T_n, \Z/p^n)$  is by cup product, as in \eqref{bencumber}. 

By \eqref{explicit-action} this means that the action of $\iota_{Q_n}(\mathfrak{t}_{S_n})$
on $H^*(Y(1), \Z/p^n)_{\mathfrak{m}}$   is trivial on  $\mathrm{image}(\mathfrak{t}_{R_n} \rightarrow \mathfrak{t}_{S_n})$. 
 Thus, this action of $\mathfrak{t}_{S_n}$ on $H^*(Y(1), \Z/p^n)_{\mathfrak{m}}$ factors  
   through $W_n$ as claimed.  \qed   
   
   
  

\subsection{Summary} \label{Strictsequence}
Let us summarize more carefully what we have said to date:

For any Taylor--Wiles datum $Q_n$ we have an action of $\mathfrak{t}_{S_n} = \Hom(T_n, \Z/p^n)$ on $H^*(Y(1), \Z/p^n)_{\mathfrak{m}}$  
constructed via an embedding $$\iota_{Q_n}:\Hom(T_n, \Z/p^n) \hookrightarrow \mbox{derived Hecke algebra} $$
 (see \eqref{embed}). 
On the other hand, we have a  surjective morphism  (see \S \ref{Vnhstar}) 
$$ f_{Q_n}: \Hom(T_n, \Z/p^n) \twoheadrightarrow \Vinf/p^n.$$ 
 These constructions, for a given $n$, depend only on $Q_n$; they do not involve the Taylor--Wiles limit process.


\begin{Definition} \label{strictdef}  \index{strict Taylor--Wiles datum}
We say that a Taylor--Wiles datum $Q_n$ of level $n$ is {\em strict of level $n$} (or just {\em strict})
if the map   
$$ \mathfrak{t}_{S_n} \stackrel{ \iota_{Q_n}}{\longrightarrow} \End \ H^*(Y(1), \Z/p^n)_{\mathfrak{m}} $$
   factors through $f_{Q_n}$. Thus, a strict Taylor-Wiles datum of level $n$
gives rise to an action of $\Vinf/p^n$ on $H^*(Y(1), \Z/p^n)_{\mathfrak{m}}$.  
\end{Definition}

What we have proved, then, amounts to the following:
\begin{lemma}  \label{Convergent implies strict} 
If the $Q_n$ are a convergent sequence of Taylor--Wiles data (Definition \ref{TWconvgt}), then 
each $Q_n$ is strict, in the sense of Definition \ref{strictdef}. 
\end{lemma}


Note we do not know that the resulting actions  of $\Vinf/p^n$ are compatible for different $n$, in any sense. 
 

 
 
 

\subsection{Dependence of our construction on  choices} \label{obstructions}
We now study dependence on choices.  Using the results of this \S, we will conclude the proof of  Theorem  \ref{maintheorem}
in \S \ref{finalesec}. 

First we discuss a minor point,  the choice of $\Frob_q^T$s: 
Suppose we choose two different such choices for a given set $Q_n$,   differing by the action of $w \in W_s$.  (Recall from 
\S \ref{TWprimes stuff} that $W_s$ is just a product of copies of the Weyl group, one copy for each prime in $Q_n$). 
Then  the actions of $\mathfrak{t}_{S_n} $ on cohomology differ
by the action of $w \in W_s$ (comment after \eqref{embedH1T}). 



Also, $w : \mathfrak{t}_{S_n} \rightarrow \mathfrak{t}_{S_n}$  is compatible with the pairings previously constructed, i.e. 
this diagram commutes
 \begin{equation} \xymatrix{
\mathfrak{t}_{S_n}  \ar[d]^{w} & \times  & H^1_f(\Z[\frac{1}{S}], \ \Ad^* \rho_n \ (1))  \ar[d]^{=}   \ar[r]^{ \ \ \qquad \Frob_q^T}  & \Z/p^n  \\ 
\mathfrak{t}_{S_n} & \times  & H^1_f(\Z[\frac{1}{S}], \ \Ad^* \rho_n \ (1))    \ar[r]^{\ \ \qquad w \Frob_q^T} & \Z/p^n  \\ 
  } \end{equation}
 This shows that the action of $\Vinf/p^n$ on $H^*(Y(1), \Z/p^n)_{\mathfrak{m}}$
 did not depend on the choice of $\Frob_q^T$s for $q \in Q_n$. 


We now discuss the more serious issue of choice of Taylor--Wiles data. 
 
 \begin{lemma}  \label{EqualityOfTwo}
Given  two sequences $Q_n, Q_n'$ of {\em strict} Taylor--Wiles data, 
there is a subsequence $\mathcal{J}$ of  the integers with following property:

For each $k \geq 1$,  there is $j_0$ such that, for  each $j \in \mathcal{J}, j \geq j_0$,  the  two actions $\Vinf$ on $H^*(Y(1),  \Z/p^{k})_{\mathfrak{m}}$
-- arising from reducing modulo $p^k$ the ``$Q_{j}$-action" and the ``$Q_{j}'$-action"  -- coincide with one another.\footnote{Recall that we are supposing that $H^*(Y(1), \Z_p)$ is
free over $\Z_p$.}  


\end{lemma}

 \proof 
 It will be convenient to relabel the sequences of strict Taylor--Wiles data as $Q_n^{(1)},  Q_n^{(2)}$.  It will be harmless to suppose that  the sets of primes underlying 
  $Q_n^{(1)}$ and $Q_n^{(2)}$ are disjoint (otherwise, we can  e.g. just compare both of them with a third set, disjoint from both of them). 


   
We will compare them both to $Q_n := Q_n^{(1)} \coprod Q_n^{(2)}$  (with the obvious choice of $\Frob_q^T$ for $q \in Q_n$). 
  Of course $Q_n$ is bigger than either $Q_n^{(1)}$ or $Q_n^{(2)}$. However it still a
  sequence of Taylor--Wiles data.   
  Let $T_n, T_n^{(1)}, T_n^{(2)}$ be the analogues of $T_n$ for $Q_n, Q_n^{(1)}, Q_n^{(2)}$ respectively;
  then $T_n = T_n^{(1)} \times T_n^{(2)}$,
  and correspondingly $\mathfrak{t}_{S_n} = \mathfrak{t}_{S_n}^{(1)} \oplus \mathfrak{t}_{S_n}^{(2)}$,
  where $\mathfrak{t}_{S_n} = \Hom(T_n, \Z/p^n)$, etc. 
  
  
  
 We have a diagram 
 \begin{equation} \label{tvlift} 
 \xymatrix{
\mathfrak{t}_{S_n}^{(1)} \ar[r] \ar[rd]^{\alpha^{(1)}}   &     \mathfrak{t}_{S_n}  \ar[d]^{\alpha}     &  \mathfrak{t}_{S_n}^{(2)} \ar[ld]^{\alpha^{(2)}} \ar[l].\\
  & H^1_f(\Z[\frac{1}{S}], \Ad^* \rho_n(1))^{\vee}  & 
 }
 \end{equation} 
 where all the $\alpha$-maps are as in   \S \ref{Vnhstar}.

 
 The upper maps are compatible for the actions on cohomology previously defined (\S \ref{tSnaction}),
 and everything maps compatibly to the bottom group $H^1_f(\Z[\frac{1}{S}], \Ad^* \rho_n(1))^{\vee} $. Moreover the  action of $\mathfrak{t}_{S_n}^{(1)}$ and $\mathfrak{t}_{S_n}^{(2)}$ on  
mod $p^n$ cohomology factors through the bottom row  by the assumed strictness. However, we do not know that the action of $\mathfrak{t}_{S_n}$ factors through $\alpha$.

   
   


 


What is missing is control of the deformation ring after adding level $Q_n$. To obtain this,  we must run now the Taylor--Wiles limit process for $Q_n$. That involves passing   to a subsequence. 
In other words, all we are guaranteed is that there is a subsequence $n_j$ such 
that $(Q_{n_j}, j)$ form a  convergent sequence  of Taylor--Wiles  data of level $j$. 
It is possible that $n_j$ is very much larger than $j$. Our prior analysis of convergent data (Lemma \ref{Convergent implies strict})  implies
that the action of $\Hom(T_{n_j}, \Z/p^j)$  on mod $p^j$ cohomology of $Y(1)$
factors through $\Vinf/p^j$, or to say it explicitly: 

 \begin{quote} (*)  The action of  $\mathfrak{t}_{S_{n_j}}$   
on $H^*(Y(1), \Z/p^j)_{\mathfrak{m}}$, 
via its embedding $\iota_{Q_{n_j}}$  into the derived Hecke algebra,  followed by reduction to $\Z/p^j$ coefficients, 
factors through the map
$$ f_{Q_{n_j}} :  \mathfrak{t}_{S_{n_j}} \rightarrow H^1_f(\Z[\frac{1}{\ramprimes}], \Ad^* \rho_j(1))^{\vee}.$$
\end{quote}
 
The proof  of the Lemma easily follows. We take $\mathcal{J}$ to be the subsequence of $n_j$s.  Let $k$ be as in the Lemma.
Take $n= n_j$, for any $j \geq k$,  and take $w^{(i)} \in \mathfrak{t}_{S_n}^{(i)}$ that have the same image in  $H^1_f(\Z[\frac{1}{S}], \Ad^* \rho_n(1))^{\vee}$.  

The images of $w^{(i)}$ in $\mathfrak{t}_{S_n}$ have the same image in $H^1_f(\Z[\frac{1}{S}], \Ad^* \rho_j(1))^{\vee}$, 
 (we are using the fact that the map  $H^1(\Z[\frac{1}{S}], \Ad \rho_n(1)) \rightarrow H^1(\Z[\frac{1}{S}], \Ad \rho_j (1))$ is surjective, by discussion  before \eqref{h00}) and therefore they act the same way on mod $p^k$ cohomology by  (*) above. 
 \qed 
 
 
 
\subsection{Conclusion of the proof of  Theorem \ref{maintheorem}. } \label{finalesec}  
 
 \label{DDR REF3} 
 Let us call a sequence of Taylor--Wiles data $Q_n$ of level $n$ (where we do not 
 require $n$ to vary through all the integers, but possibly some subsequence thereof)
 {\em $\Vinf$-convergent} if: \index{$\Vinf$-convergent} 
 \begin{itemize} 
 \item Each $Q_n$ is strict (Definition \ref{strictdef}) thus giving an action of $\Vinf$ on $H^*(Y(1), \Z/p^n)_{\mathfrak{m}}$. 
 \item The actions  converge to  an action of of $\Vinf$ on $H^*(Y(1), \Z_p)_{\mathfrak{m}}$.
In other words, if we fix $k$,  the action of $\Vinf$ on $H^*(Y(1), \Z/p^k)_{\mathfrak{m}}$ 
 arising from reducing the $Q_n$-action   is eventually constant.
 
 \end{itemize}
 
 
 
 


















By Lemma \ref{Convergent implies strict} and passing to a further subsequence,
we see that $\Vinf$-convergent sequences exist. 
By Lemma \ref{EqualityOfTwo}, if $Q, Q'$ are two $\Vinf$-convergent sequences, 
  the resulting actions of $\Vinf$ on cohomology coincide.  
Thus at this point we have defined an action of $\Vinf$ on cohomology that is independent of choices, namely,
the action arising from any $\Vinf$-convergent sequence. 
This 
  action has the following property: 























 \begin{quote}  $(\dagger)$:  For any sequence $Q_n$ of Taylor--Wiles data,  
there is a subsequence $Q_{n_r}$ 
 such that  (for every $r$) the following two actions of $\mathfrak{t}_{S_{n_r}}$ on  $H^*(Y(1), \Z/p^r)_{\mathfrak{m}}$ coincide:
 
 \begin{itemize}
\item  The action via $\iota: \mathfrak{t}_{S_{n_r}} \rightarrow \mbox{ derived Hecke algebra with $\Z/p^r$ coefficients}$ (see \eqref{iotaQndef}). 
 \item The action obtained from the $\Vinf$-action, via   $f: \mathfrak{t}_{S_{n_r}} \twoheadrightarrow \Vinf/p^r$
(see   \eqref{tsnvsurj} ). 
\end{itemize} 
   \end{quote}  
  To see this, we first pass from $Q_n$ to a convergent subsequence 
  $(Q_{m_r}, r)$, where we regard $Q_{m_r}$ as having level $r$;
by Lemma \ref{Convergent implies strict} this means 
that  $Q_{m_r}$ is
  a strict datum of level $r$. We then pass to a further  subsequence $m_r'$
  to extract a $\Vinf$-convergent sequence; this gives the assertions above,
  but with $\Z/p^r$ and $\Vinf/p^r$ replaced by $\Z/p^{k(r)}, \Vinf/p^{k(r)}$
  where $k(r) \rightarrow \infty$ with $r$. Passing to a further subsequence gives the desired result. 
  
   
  
 

 

 
 
 
  
 \proof (of Theorem \ref{maintheorem}, using $(\dagger)$): 
We have already constructed an action of $\Vinf$; let us prove, by contradiction, that it has property (*)
from the Theorem. 
Suppose that there is an integer $A$ and an infinite sequence of primes $q_n \equiv 1$ modulo $ p^n$
such that the pullback of the action via $ f_{q_n,A}: H^1(T_q, \Z/p^A) \rightarrow \Vinf/p^A$ 
fails to coincide with the action of $H^1(T_q, \Z/p^A)$ via the  embedding $\iota_{q_n, A}$ into the derived Hecke algebra with $\Z/p^A$ coefficients. 
We can choose a Taylor--Wiles system $Q_n$  containing $q_n$ and then get a contradiction to $(\dagger)$
as soon as $r > A$.  This proves (*). 
 
Now let us show that the image of $\wedge^* \Vinf$  in endomorphisms
of cohomology coincides with the global derived Hecke algebra.

 
Refer to the diagram \eqref{BigDog}, constructed with a   convergent sequence of Taylor--Wiles data $Q_n$. 
We will only use a subsequence of $n$s which is $\Vinf$-convergent. 
Consider for $n \geq k$ the map
\begin{equation} \label{Banjo} \Winf   = \mathfrak{t}_{S}/\mathfrak{t}_R  \stackrel{\eqref{feeling_groovy2}}{\longrightarrow} \mathfrak{t}_{S_n}/\mathfrak{t}_{R_n} 
\stackrel{\eqref{tsnvsurj}}{ \longrightarrow} \Vinf/p^k. \end{equation}
By \eqref{feeling_groovy2} and the discussion after \eqref{tsnvsurj}, 
the composite actually gives an isomorphism \begin{equation} \label{Banjo2} \Winf/p^k \simeq \Vinf/p^k.\end{equation}  
\label{DDR REF4} For fixed $k$ and large $n$, the map \eqref{Banjo} is independent of $n$: Choose $\tilde{v} \in \mathfrak{t}_S$. Let $v_n, v_m$
 be its image in $\mathfrak{t}_{S_n}, \mathfrak{t}_{S_m}$.
 As we saw in the diagram \eqref{BigDog}, the actions of $v_n, v_m$ on mod $p^k$ cohomology must coincide, 
 because both can be computed by means of the lift $\tilde{v}$. 
For this we are implicitly using  \eqref{logstructure} to see that  the composite map
{\small  \begin{equation}
 H^*(\Hom_{\Sinf}(\Cinf, \Z_p)) \rightarrow 
 H^*(\Hom_{S_n}(\Cinf \otimes_{\Sinf} S_n, \Z/p^n))   \stackrel{\sim}{ \rightarrow}
  H^*(Y(1), \Z/p^n)_{\mathfrak{m}}  
 \rightarrow   H^*(Y(1), \Z/p^k)_{\mathfrak{m}}
  \end{equation}}
is {\em independent of $n$}, for $n \geq k$.







 So the images of $v_n, v_m$ in $\Vinf/p^k$ have the same actions on mod $p^k$ cohomology. 
The $\Vinf/p^k$ action on mod $p^k$ cohomology is faithful (by \eqref{Banjo2} and \eqref{watney}) so this forces  the image of $v_n, v_m$
in $\Vinf/p^k$ to coincide as claimed.  
  
Therefore, passing to the limit over $n$, we get a map $\Winf/p^k \rightarrow \Vinf/p^k$, 
which is easily seen to be compatible as we increase $k$; thus the inverse limit over $k$
defines an isomorphism \begin{equation} \label{bo} \Winf  \stackrel{\sim}{\rightarrow} \Vinf.\end{equation}


Next, referring to \eqref{BigDog} the action of $\Ext_{\Sinf}^*(\Sinf/\Iinf, \Sinf/\Iinf) \simeq \wedge^* \mathfrak{t}_S$
on $H^*(\Hom_{\Sinf}(\Cinf,  \Z_p))$ certainly factors through $\wedge^*  \Winf $;
this action of $\wedge^* \Winf$ on $H^*(\Hom_{\Sinf}(\Cinf, \Z_p))$  is compatible
under the identifications  \eqref{logstructure} and  \eqref{bo} with the action of $\wedge^* \Vinf$ on  $H^*(Y(1), \Z_p)_{\mathfrak{m}}$. 

  Therefore, by \eqref{watney},  $\Vinf$ freely generates an exterior algebra inside $\mathrm{End}(H^*)$, and $H^*$ is freely generated over $\wedge^* \Vinf$
  by $H^{\BWq}(Y(1), \Z_p)_{\mathfrak{m}}$, its minimal degree component. 
 On the other hand, the image of $\wedge^* \Vinf$ in $\mathrm{End}(H^*)$ is contained in the global derived Hecke algebra --
 the action of an element $\Vinf$ is, by definition, a limit of actions of elements in the derived Hecke algebra.  Indeed,
 $\Vinf$ lies inside the strict global derived Hecke algebra. 
  \qed 


\subsection{Proof of Proposition \ref{P853}} \label{P853proof}

 {\color{\changecolor} . In our current situation, we have an inclusion
\begin{equation} \label{xyyzzww} \wedge^* \mathsf{V} \subset \gHecke\end{equation}
and we have seen that $H^*(Y(1), \Z_p)_{\mathfrak{m}}$
 is generated by its lowest nonvanishing degree $H^{\BWq}$ as a  
 $\wedge^* \mathsf{V}$-module.  
 If we know that $H^*(Y(1), \Z_p)_{\mathfrak{m}} = \Z_p$, 
 we argue that \eqref{xyyzzww} is an equality
 just as in the corresponding argument after  \eqref{inclusions BHH}.
 
 If we are given $\mathsf{S}$ as in the statement of the Proposition, 
 let $\mathsf{M} = H^{\BWq}(Y(1), \Z_p)_{\mathfrak{m}} \otimes_{\Z_p} \Q_p$
 as a $\mathsf{S}$-module. It is semisimple by assumption, and the natural map
 $$ \mathsf{M} \otimes \wedge^* \mathsf{V}_{\Q_p}      \rightarrow H^*(Y(1), \Z_p)_{\mathfrak{m}} \otimes \Q_p$$
 is now an isomorphism of $\mathsf{S} \otimes \wedge^* \mathsf{V}_{\Q_p}$ modules. 
 However,
$$\mbox{(graded) commutant of $\mathsf{S} \otimes \wedge^* \mathsf{V}_{\Q_p}$   on $\mathsf{M} \otimes \wedge^* \mathsf{V}_{\Q_p}$} =   \mathsf{S}' \otimes  \wedge^* \mathsf{V}_{\Q_p},$$
as can be verified by computing in steps:  the commutant of $\mathsf{S}$ alone
 equals $  \mathsf{S}' \otimes \mathrm{End}(\wedge^* \mathsf{V}_{\Q_p})$,
 and then inside here the (graded) commutant of $\wedge^* \mathsf{V}_{\Q_p}$   is $\mathsf{S}' \otimes \wedge^* \mathsf{V}_{\Q_p} $.  
 

Since this commutant contains  the image of $\gHecke$
acting on $\Q_p$-cohomology, the latter is also graded commutative, since $\mathsf{S}'$ is commutative by the multiplicity one hypothesis.   Note that the action on $\Q_p$ cohomology
is faithful because of our torsion freeness assumption, see 7(a) of  \S \ref{Sec:assumptions}.












  }
\qed




 
\subsection{The action of Hecke operators}  \label{Galoisindexingproofs}
 To conclude, let us translate what we have proved into a more concrete   assertion about the action of a derived Hecke operator. 
 
 Let $q$ be a unramified prime for $\rho$,  with $q \equiv 1$ modulo $p^n$, and such that
 $\rhobar(\Frob_q)$ is conjugate to a strongly regular element of $T^{\vee}(k)$. Let $\nu \in X_*(\mathbf{A})^+$ be strictly dominant 
and let
  $$\alpha \in H^1(\mathbf{A}(\F_q), \Z/p^n).$$ 
  To this we can associate in a natural way (see below) a derived Hecke operator $T_{q, \nu, \alpha}$
  as well as an element $[q, \nu, \alpha] \in \Vinf/p^n$; we will prove
  that the actions of these are compatible (see Lemma below), 
 justifying the assertions made in \S \ref{Galoisindexing}. 


First of all,
a small piece of linear algebra. Let $k$ be a field.  Suppose given a  fixed character $\psi \in X^*(T^{\vee})$. 
Let $g \in G^{\vee}(k)$ be regular semisimple, with centralizer $Z_g$; 
this data allows us to construct a homomorphism of $k$-vector spaces
$$e_{\psi,g}: \mathrm{Lie}(T^{\vee}) \rightarrow \Lie(Z_g),$$ 
$$ e_{\psi,g}:  \sum_{\phi: T^{\vee} \stackrel{\sim}{\rightarrow} Z_g} \langle \psi, \phi^{-1}(g) \rangle \cdot d\phi$$
where the sum is taken over all conjugations of $T^{\vee}$ to $Z_g$ over $\bar{k}$;
the morphism is nonetheless defined over $k$. 

{\em Example:}   if $G^{\vee}=\SL_2$, take $T^{\vee}, B^{\vee}$ in the standard way to be the diagonal subgroup and upper triangular matrices, and take $\psi: \left( \begin{array}{cc} x & 0 \\ 0 & x^{-1} \end{array} \right) \mapsto x$.  Then $e_{\psi, g}$ sends $  \left( \begin{array}{cc} 1 & 0 \\ 0 & -1 \end{array} \right) \in \Lie(T^{\vee})$ 
to the element  $  2g - \mathrm{trace}(g) \in M_2(k)$: it's enough to check this for $g \in T^{\vee}$, where the result is clear. 



\medskip

Let $q, \nu, \alpha$ be as described at the start of this subsection. We can then construct a class 
  $$ [q, \nu, \alpha] \in \Vinf/p^n$$
  in the following way:  regarding $\nu$ as a character of
  $T^{\vee}$,  and use the linear algebra construction mentioned with $k = \Q_p$ to make the first map of   \begin{equation} \label{cheeseboard} \mathrm{Lie}(T^{\vee}) \stackrel{e_{\nu, \Frob_q}}{\longrightarrow } \Lie(Z_{\rho(\Frob_q)}) \hookrightarrow \Lie(G^{\vee})\end{equation}
  (at first we get this $\otimes \Q_p$ but then it preserves the integral structures, with reference to the natural $\Z_p$-models of the three groups above). 
  The resulting embedding $\mathrm{Lie}(T^{\vee}) \rightarrow  \Ad \rho$
    is a morphism of $\Gal(\overline{\Q_q}/\Q_q)$-modules,
  where $\mathrm{Lie}(T^{\vee})$ is taken to have the trivial action. 
 
  
As before, we may identify
  $$H^1(\mathbf{A}(\F_q), \Z/p^n) = H^1(X_*(\mathbf{A}) \otimes \F_q^{\times} , \Z/p^n) = \Hom(\F_q^{\times}, X_*(T^{\vee}) /p^n)$$
and so from $\alpha$ we obtain a class  
$$\alpha' \in   \frac{ H^1(\Q_q, \Lie(T^{\vee})/p^n)}{H^1_{\ur}(\Q_q, \Lie(T^{\vee})/p^n)}.$$
   Here $\Lie(T^{\vee})$ is taken as a trivial Galois module.
We can then form 
$$\mbox{pushforward of } \alpha' \mbox{via \eqref{cheeseboard}}  \in   \frac{ H^1(\Q_q, \Ad \rho_n)}{H^1_{\ur}(\Q_q, \Ad \rho_n)}. $$ 
  and, as usual, this can be paired with  $H^1_f(\Z[\frac{1}{S}], \Ad^* \rho (1))$ by means of local reciprocity.
  In this way we obtain a functional $H^1_f(\Z[\frac{1}{S}], \Ad^* \rho (1)) \rightarrow \Z/p^n$, which we denote as
$$[q, \nu, \alpha] \in \Vinf/p^n.$$ 
  
  \begin{lemma} \label{reciprocity law}
Let $q, \nu, \alpha$ be as above.   Let $[q, \nu, \alpha] \in \Vinf/p^n$ be as defined above. 

  
Let $T_{q, \nu,\alpha}$ be the derived Hecke operator with $\Z/p^n$ coefficients which is 
supported on the $G_q$-orbit of $(\nu K_q, K_q)$ and 
whose value at $(\nu K_q, K_q)$
which corresponds to $\alpha$ under the   cohomology isomorphism $H^*(K_q \cap \nu K_q \nu^{-1}, \Z/p^n) \cong H^*(\mathbf{A}(\F_q), \Z/p^n)$. 

Then $T_{q,\nu,\alpha}$ corresponds to $[q, \nu,\alpha] \in \Vinf/p^n$, in the following asymptotic sense:

 There is $N_0(m)$ such that  for  $q ,\nu, \alpha$ as above with 
 $q \equiv 1$ modulo $p^{N_0(m)}$, 
 the actions of  $T_{q, \nu, \alpha}$ and $[q, \nu,\alpha]$
 on $H^*(Y(1), \Z/p^m)_{\mathfrak{m}}$ coincide. 
\end{lemma}
  \proof
Under the derived Satake isomorphism, $T_{q,\nu, \alpha}$ is sent to  
$$\sum_{w} w \nu\otimes w \alpha
\in \left(S[X_*] \otimes H^1(\mathbf{A}(\F_q))\right)^W.$$   

With notation as in \S \ref{Vnaction}, 
let $\Theta_{\nu} \in S[X_*]_{\mathfrak{m}}^W$ be  defined
so that its image under $S[X_*]_{\mathfrak{m}}^W \hookrightarrow S[X_*]_{\tilde{\mathfrak{m}}} \rightarrow S[X_*]_{\chi}$
is equal to $\nu$. Here, we regard $\nu \in X_* \hookrightarrow S[X_*]$. 



 
 Then, after completing at $\mathfrak{m}$, we have an equality
  $$\mathrm{Satake}(T_{q,\nu,\alpha}) =   \sum_{w \in W}  \Theta_{w \nu} \cdot  \mbox{Satake}(\theta(w \alpha)) \in (S[X_*] \otimes H^1(\mathbf{A}(\F_q)))^W_{\mathfrak{m}}$$
 where $\theta$ is as in \eqref{embedH1T}.  (We can check this using the isomorphism  \eqref{composite iso}:
 it gives an isomorphism of the target group with  $S[X_*]_{\chi} \otimes H^1(T_q)$,
 under which $\theta(w \alpha)$ is, by its very definition,  sent to $1 \otimes w \alpha$; under the same isomorphism $\Theta_{w \nu}$ 
 is sent to $w \nu \otimes 1$, and the result follows.) 
 

  
 

As before we have fixed $\Frob^T_q \in T^{\vee}(\F_p)$ an element conjugate to $\rhobar(\Frob_q)$;
fix a lift $t_q \in T^{\vee}(\Z_p)$ that is conjugate to $\rho(\Frob_q)$. 
Then  $ \Theta_{w \nu}$  (more exactly, its preimage under Satake) acts on $H^*(Y(1), \Z_p)_{\mathfrak{m}}$
by  $\langle w \nu, t_q \rangle$ (this makes sense: $w \nu \in X^*(T^{\vee})$ and $t_q \in T^{\vee}(\Z_p)$, so they can be paired to get an element of $\Z_p^{\times}$).   Using Theorem \ref{maintheorem}, we see that the action of $T_{q,\nu, \alpha}$ on $H^*(Y(1), \Z_p)_{\mathfrak{m}}$
corresponds (in the sense  of the lemma statement) to the element
$$ \sum_{w \in W} \langle w \nu, t_q \rangle \cdot f_{q,n}(w \alpha)  =  \sum_{w \in W} \langle \nu, w^{-1} t_q \rangle \ \  f_{q,n}(w \alpha) \in  \Vinf/p^n.$$
Winding through the definitions, this element of $\Vinf/p^n$ is  exactly $[q, \nu, \alpha]$. \qed

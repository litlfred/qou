---
doc_id: arxiv-1608.07234v3
doc_title: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS"
section_id: sec-002-3-torus-localization-and-satake-isomorphism
section_title: "Torus localization and Satake isomorphism"
section_number: 3
pages: 21-26
source_pdf: 1608.07234v3.pdf
source_sha256: 311730670d2fdcb7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.897
doc_brief: "DERIVED HECKE ALGEBRA AND COHOMOLOGY OF ARITHMETIC GROUPS — We describe a graded extension of the usual Hecke algebra: it acts in a graded fashion on the cohomology of an arithmetic group Γ."
---
\label{Satake} 
  
   Our main goal here is to prove a version of the Satake isomorphism that applies to the derived Hecke algebra. Namely, 
take $m =\ell^r$  a prime power.   Suppose $q \equiv 1$ modulo $\ell^r$. We show  
   (see \eqref{dSatake} for the precise statement) 
\begin{eqnarray*} \mbox{derived Hecke algebra for  split $q$-adic group with $\Z/\ell^r$-coefficients} \\  \cong  \left(\mbox{derived Hecke algebra for maximal torus with $\Z/\ell^r$ coefficients}\right)^{W} \end{eqnarray*}
where the $W$ superscript means Weyl-fixed, and we also require that $\ell$ does not divide the order of $W$. 

For example,   if $q \equiv 1$ modulo $\ell$, the derived Hecke algebra of $\PGL_2(\Q_q)$ with coefficients in $\Z/\ell$  is isomorphic to 
   $$ \Z/\ell[x_0, x_0^{-1},  y_1, z_2]^{\Z/2}$$
  where $x_0, y_1, z_2$ have (respectively) degree $0,1,2$, and the action of $\Z/2$ switches $x_0^{\pm 1}$ and negates $y_1, z_2$. 
    
 A consequence of our results is that (under our assumptions on $q, m$)  the derived Hecke algebra is graded commutative. We do not know
 if this is valid without any assumption on $q$ and  the coefficient ring $S$.  Recall, however, that $q \equiv 1$  in $S$ is precisely the case where the Hecke algebra is largest, by 
 the discussion of \S \ref{doublecoset}, and understanding this case will be enough for our global analysis. 
 
 
  
\subsection{}
  
  
 
  It is a curious fact that, in characteristic dividing $q_v-1$, 
  the Iwahori-Hecke algebra of a split $F_v$-group is isomorphic to the group algebra of  its affine  Weyl group.   
  A related interesting phenomenon is that, under the same assumptions,
  the Satake isomorphism
  $$ \mbox{ Hecke algebra} \longrightarrow \mbox{Hecke algebra of torus}$$
  is given simply by {\em restriction} (!) 
  
These points  can be explained by
  ``torus localization,'' as we now explain.  Using that method we will derive our 
 Satake isomorphism  below.  Of  course this is a little bit cheap,
 but it turns out to be exactly what we need anyway.
  
 
 
 
    

  
  
  
  I am very grateful to David Treumann for conversations about this material.  In particular,
I learned about localization in the context of local geometric Langlands   from his paper {\em Smith theory and geometric Hecke algebras} \cite{Treumann}.
  















 
  
  
\subsection{} \label{BasicNotn}
  In this section and the next, $\mathbf{G}$ will be a {\em split group over
  the nonarchimedean local field $F_v$}.
  The coefficient ring for all our Hecke algebras will be taken to be 
  $S= \Z/\ell^r$,  for a prime $\ell$ and $r \geq 1$. 
We shall  suppose that $\ell^r$ divides $(q_v - 1)$, where $q_v$ is the cardinality
  of the residue field $\mathbf{F}_v$.      We also assume that $\ell$ is relatively prime to the order of the Weyl group of $\GG$. 
  



  We fix other notations as follows: Let $\mathcal{G}$ be a split group over $\mathcal{O}_v$ \index{$\mathcal{G}$} \index{$\mathcal{A}$} \index{$\mathcal{B}$}
  whose generic fiber is identified with $\mathbf{G}$. Let $K_v = \mathcal{G}(\mathcal{O}_v)$,
  a maximal compact subgroup of $G_v = \mathbf{G}(F_v)$. 
  Let $\mathbf{A}$ be a maximal torus in $\mathbf{G}$, and $\mathbf{B}$ a Borel subgroup of $\mathbf{G}$ containing $\mathbf{A}$; we suppose them to\index{$G_v$} \index{$A_v$} \index{$B_v$} 
 extend to a torus $\mathcal{A}$ and Borel $\mathcal{B}$  inside $\mathcal{G}$.  We write $A_v, B_v$ for the $F_v$-points
  of $\mathbf{A},\mathbf{B}$.    We shall use the notation $\mathbf{A}(F_v)^{\circ}$ for the   maximal compact subgroup of $\mathbf{A}(F_v)$,
  and similar notation whenever the maximal compact subgroup is unique.  \index{$\mathbf{A}(F_v)^{\circ}$}
  
  Let $W$ be the Weyl group for $\mathbf{A}$.  
We write $X_*= X_*(\mathbf{A})$ for the co-character group of $\mathbf{A}$. \index{$X_*$} 
  We identify $X_*$ with $A_v/A_v\cap K_v \subset G_v/K_v$  by means of the map
\begin{equation} \label{IWidentification} \chi \in X_* = \Hom(\mathbb{G}_m, \mathbf{A}) \longrightarrow \chi(\varpi_v),\end{equation}
  with $\varpi_v$ a uniformizer. 
 
 We write for short
 $ T =\mathcal{A}(\mathbf{F}_v).$
  The reduction map $A_v \cap K_v \rightarrow  T$ splits uniquely, and so we obtain
  a ``Teichm{\"u}ller'' lift
\begin{equation} \label{teich}  T \hookrightarrow A_v \cap K_v. \end{equation}
This induces a cohomology isomorphism, with $\Z/\ell^r$ coefficients.     \index{$T$}
   
   We have a Cartan decomposition
$$G_v = K_v \cdot A_v \cdot K_v  $$
The $A_v$ component of this decomposition is 
  unique up to the action of the Weyl group $W$.
  
  \begin{theorem} \label{DHA:Satake}  
Let notations be as above; in particular the coefficient ring is always $S=\Z/\ell^r$, where $\ell^r$ divides $q_v-1$,
and $\ell$ does not divide the order of the Weyl group. 



Then restriction (in the model of \S  \ref{desc2}) defines an isomorphism
   \begin{equation} \label{dSatake} \mbox{ derived Hecke algebra for $(G_v, K_v)$} 
\stackrel{\sim}{\longrightarrow} \mbox{ derived Hecke algebra for $(A_v, A_v \cap K_v)$ }^W.
  \end{equation}

  \end{theorem}
  
  Let us explicate what we mean by ``restriction.''
As per \S \ref{desc2}, an  element $h$ of the left-hand side  is an association:
$$ (x,y) \in (G_v/K_v)^2 \rightsquigarrow h(x,y) \in H^*(G_{xy}, S),$$
and  its image  $h'$ on the right-hand side is obtained
  by restricting to $A_v/(A_v \cap K_v) \hookrightarrow G_v/K_v$
  and pulling back cohomology classes under the inclusion $A_{xy} \hookrightarrow G_{xy}$. 
  The element $h'$ is clearly $A_v$-invariant, and it is also $W$-invariant:
  $$  [w]^* h'(wx, wy) =   h(x,y)$$
because of the $G$-invariance of $h$. 
 
Because $A_{xy} = A_v \cap K_v$ for each $x,y$, and the  the (Teichm{\"u}ller) inclusion \eqref{teich}
$T \hookrightarrow A_v \cap K_v$ induces a cohomology isomorphism,
we can regard $h'$  as a function $X_* \times X_* \longrightarrow H^*(T,S)$.
We will often regard $h'$ as such without explicit comment.  
The multiplication in this model is usual convolution in the $X_*$ variable, together with multiplication in $H^*(T, S)$. 
 We may therefore identify the right-hand side of \eqref{dSatake} with   \begin{equation}  \label{alterpres} \left( S[X_*] \otimes H^*(T, S) \right)^W,\end{equation}
  just as in \eqref{TTspin}, i.e. restrict to $X_* \times \{0\}$ and identify functions on $X_*$ with the group algebra in the obvious way.
  
    
\subsection{} \label{surj}
  
  A useful corollary to this result is the following (although even easier, as it does not use the algebra structure):
  The induced map
$$\mbox{derived Hecke algebra  over $\Z/\ell^n$} \rightarrow \mbox{ derived Hecke algebra  over  $\Z/\ell^m$ }$$
  is a {\em surjection} for $n > m$, under our assumption that $\ell^n$ divides $q_v-1$. 
  (We used this in the discussion  of \S \ref{limit}). 
  
  In fact, we're reduced to checking the same fact when $C$ is a cyclic group of order divisible by $\ell^n$, i.e.
  $$H^*(C, \Z/\ell^n) \rightarrow H^*(C, \Z/\ell^m)$$
  is surjective.  This follows from a straightforward computation.
  
  
  
  
  
  
    
















































\subsection{Some useful Lemmas}
 
\begin{lemma} \label{nontriv}
Any nontrivial root  $\alpha$ of $\mathbf{A}$ on $\mathbf{G}$ is nontrivial
on the $\ell$-Sylow of $A_v \cap K_v$. In particular, $\alpha$ induces a nontrivial
character  $\mathcal{A}(\mathbf{F}_v) \rightarrow \mathbf{F}_v^{\times}$. 
\end{lemma}
\proof
This is just a matter of checking the residue characteristic is forced to be big enough:
if the claim is not true,  the root $\alpha$ would be divisible 
 by $\ell^r$ in $X^*(\mathbf{A})$;  but roots are divisible at most by $2$ because $\langle \alpha, \alpha^{\vee} \rangle =2$, 
 and $\ell > 2$ because it's prime to the order of the Weyl group.
 \qed

 \begin{lemma}\label{finitefields} 
Use notation as above; in particular $\mathbf{F}_v$ is a finite field of cardinality $q_v \equiv 1$ modulo $\ell^r$,
and the order of the Weyl group is not divisible by $\ell$. 

Then the restriction map from the cohomology $H^*(\mathcal{G}(\mathbf{F}_v), \Z/\ell^r)$    to Weyl-fixed cohomology of the torus $H^*(\mathcal{A}(\mathbf{F}_v), \Z/\ell^r)^W$
is an isomorphism.
\end{lemma}

\proof   Write for short  (and just for this proof) $G, A,B$ for the $\mathbf{F}_v$-points of $\mathcal{G}, \mathcal{A}, \mathcal{B}$.

 Consider the composite of restrictions 
\begin{equation} \label{sequence} H^*(G,  \Z/\ell^r)  \rightarrow H^*(B, \Z/\ell^r) \stackrel{\sim}{ \rightarrow} H^*(A, \Z/\ell^r).\end{equation}
The second map is an isomorphism and its inverse is specified by corestriction. 
Therefore we can transport the $W$-action on $H^*(A)$  to a $W$-action on $H^*(B, \Z/\ell^r)$; explicitly the action of $w$ is
\begin{equation} \label{w} \mathrm{Cores}^B_A \circ  [w]_A \circ \mathrm{Res}^{B}_A .\end{equation} 
where $[w]_A$ is pullback of cohomology classes under $\Ad(w^{-1}): A \rightarrow A$. 

We will now show that $\mathrm{Res}^G_B \circ \mathrm{Cores}^{G}_B = \sum_{w \in W} w$,
where the $w$-action on $H^*(B)$ is that just defined. 
Since $\mathrm{Cores}^{G}_B \mathrm{Res}^G_B = |W|$, which is invertible in $\Z/\ell^r$,
we see that $\mathrm{Res}^G_B$ is injective and $\mathrm{Cores}^G_B$ is surjective; so 
  $\mathrm{Res}^G_B$ is an isomorphism onto the $W$-invariants on $H^*(B, \Z/\ell^r)$,
  which implies the Lemma.  
   
  
  
By the  usual formula \cite[Proposition 9.5]{Brown}, using the Weyl group $W$ as a system of representatives for double cosets,
the composite equals
$$\sum_{w \in W}  \mathrm{Cores}_{w  B w^{-1} \cap B}^B  \cdot \Ad(w^{-1})^* \cdot \mathrm{Res}^{B}_{B \cap w^{-1} B w}  $$
But $w^{-1} B w \cap B$ contains  $A$, and  $[w B w^{-1} \cap B: A] =1$ modulo $\ell^r$.  So we can rewrite the $w$-term as 
$$ \mathrm{Cores}_{w  B w^{-1} \cap B}^B  \cdot \Ad(w^{-1})^* \cdot  \mathrm{Cores}_{A}^{B \cap w^{-1} B w }  \mathrm{Res}^{B}_{A} = \Cores_{A}^{B} \cdot [w]_A \cdot \Res^B_A  $$
which is exactly the $W$-action on $H^*(B)$, by  \eqref{w}. \qed 

\begin{lemma}\label{ff2}  Let $G_1, G_2$ be finite groups. Suppose that $G_1 \hookrightarrow G_1 \times G_2$ is the natural inclusion, and $M$ is a module for $G_1 \times G_2$
 killed by  the order $\# G_2$ of $G_2$. Then the corestriction map $H^*(G_1, M) \rightarrow H^*(G_1 \times G_2, M)$
 is zero. 
 \end{lemma}
 \proof Indeed, the composite $H^*(G_1 \times G_2) \stackrel{Res}{\rightarrow} H^*(G_1) \stackrel{Cores}{\rightarrow} H^*(G_1 \times G_2)$
 is multiplication by the order  of $G_2$, and is therefore zero with $M$ coefficients; but the first $\mathrm{Res}$ is surjective
 because $G_1 \rightarrow G_1 \times G_2$ is split. 
\qed  


\begin{lemma}  \label{doublecentralizer} 
 Let $\Gamma \subset G_v$ be a finite $\ell$-subgroup.
 Let $\mathbf{S}$ be the double centralizer of $\Gamma$,
 considered as an algebraic $F_v$-subgroup of $\mathbf{G}$.
 Then:
   \begin{itemize}
  \item[(a)] $\mathbf{S}$ 
 has component group of prime-to-$\ell$ order, 
 \item[(b)]   the maximal compact subgroup $\mathbf{S}(F_v)^{\circ}$ of its $F_v$-points fixes
 every point of $G_v/K_v$ that is fixed by $\Gamma$. 
 \end{itemize} 
  
  \end{lemma}
\proof  Let $x \in G_v/K_v$ be fixed by $\Gamma$. Conjugating $\Gamma$ by $G_v$ we may suppose that $x=K_v$, the identity coset
 in $G_v/K_v$. 

 Now, the quotient of  the orders of $\mathcal{G}$ and $\mathcal{A}$
 over the finite field $\mathbf{F}_v$ is congruent to $|W|$ modulo $\ell$, because of our assumption $\ell$ divides $q-1$. Therefore there is an $\ell$-Sylow of $K_v$ contained in $A_v \cap K_v$.




Thus, further conjugating $\Gamma$ by $K_v$ we can further assume that 
 that $\Gamma \subset \mathbf{A}(F_v) \cap K_v$.   The centralizer $\mathbf{Z}(\Gamma)$ of $\Gamma$ is then a subgroup containing $\mathbf{A}$.
  The double centralizer $\mathbf{S}$ is  thus contained in $\mathbf{A}$ and, of course, it contains $\Gamma$. 
  
  
  
Because $\mathbf{S} \subset \mathbf{A}$, the maximal compact subgroup 
 of $\mathbf{S}(F_v)$ is contained in the maximal compact $\mathbf{A}(F_v) \cap K_v$ of $\mathbf{A}$; the latter fixes $x$. This
 proves (b). 
  
  To verify the assertion about the component group of $\mathbf{S}$, we first verify that $\mathbf{Z}(\Gamma)$ is connected. 
  Note that $\mathbf{S}$ is contained in $\mathbf{Z}(\Gamma)$ by the analysis above, so it is in fact the center of $\mathbf{Z}(\Gamma)$. 
  Then we are reduced to the following assertion: 
 for any reductive group $\mathbf{Z}$, the component group of the center of $\mathbf{Z}$
  is only divisible by primes dividing the order of the Weyl group. Replacing $\mathbf{Z}$ by  
  its quotient by the connected center, we can check the same assertion for $\mathbf{Z}$ semisimple;
  so it is enough to check for $\mathbf{Z}$ simply connected semisimple. There it is obvious case by case. 
   
  To see that $\mathbf{Z}=\mathbf{Z}(\Gamma)  $ is connected, we can reason as follows:  $\mathbf{A}$ is a maximal split
  torus  within  $\mathbf{Z}$, so any element of $\mathbf{Z}/\mathbf{Z}^0$ has a representative in $\mathbf{Z}$  that belongs to the normalizer of $\mathbf{A}$.
  Here $\mathbf{Z}^0$ denotes the connected component.
  So it is enough to show that any  $\overline{F_v}$-point $n$ in the normalizer of $\mathbf{A}$ that belongs to $\ZZ$ actually belongs to $\ZZ^0$.
  Let $w \in \Aut(\mathbf{A})$ be the  element of the Weyl group of $\mathbf{A}$ corresponding to such an $n$. 
  Fix $\gamma \in \Gamma$. Since $n$ centralizes $\Gamma$, we see that 
  $w$ fixes $\gamma$. 
Write $N$ for the $\ell$-part of $q-1$. So $\gamma \in \mathbf{A}[N] \simeq X_* \otimes \mu_{N}$;
  fixing a primitive $N$th root, we can identify $\mathbf{A}[N]$ with $X_*/N$. 
  Since the order of $w$ is relatively prime to $\ell$, we see -- by taking invariants in $X_* \rightarrow X_* \rightarrow X_*/N$ --
  that $\gamma$ actually lies in the image of some $w$-fixed character $\mathbb{G}_m \rightarrow \TT$.   
 
  Applying this reasoning for each $\gamma \in \Gamma$,
  we see that $w$ actually  centralizes a subtorus of $\TT$ containing $\Gamma$. But the centralizer of that torus
  is a connected group, thus contained in $\mathbf{Z}^0$.  We conclude that $\mathbf{Z}$ is connected, as we claimed. 
  \qed 










 
 
  
 \begin{lemma} \label{splitness}  Suppose $z \in G_v/K_v$ does not belong to the image of $X_*$
 (where the map  $X_* {\hookrightarrow}  G_v/K_v$ was  defined in
\eqref{IWidentification}). 
 
 Let $\Gamma$ be an $\ell$-Sylow of $A_v \cap K_v$; 
 thus $\Gamma$ is an $\ell$-Sylow subgroup of $G_{xy}$.
 Let $\Gamma_z$ be the stabilizer of $z$ in $\Gamma$.  
 
 Then the corestriction map  $H^*(\Gamma_z) \rightarrow H^*(\Gamma)$ is zero with $\Z/\ell^r$ coefficients.


\end{lemma}



 
 
 \proof  
 




 
 Note that the centralizer  and so also the double centralizer of $\Gamma$ is simply $\mathbf{A}$. (Any root of $\mathbf{A}$ is nontrivial on the $\ell$-Sylow of $A_v \cap K_v$,  by Lemma \ref{nontriv}, so the connected centralizer is $\mathbf{A}$; 
the centralizer cannot be larger than $\mathbf{A}$ because any element of the Weyl group acts nontrivially on $\Gamma \simeq X_*(\mathbf{A})/\ell^r$). 
 

 
 
Let $\mathbf{S}$ be the double centralizer of   $\Gamma_z$. 
  Since $\Gamma_z \subset \Gamma$
we also have $\mathbf{S} \subset \mathbf{A}$. 

 Let $\mathbf{S}^0$ be the identity component of $\mathbf{S}$; it is a split torus.  Because ((a) of \S \ref{doublecentralizer}) the component group of $\mathbf{S}$ is prime-to-$\ell$, we see that 
$\Gamma_z$ lies inside $\mathbf{S}^0$, and thus inside the maximal compact subgroup of $\mathbf{S}^0(F_v)$.
Let $\Gamma_z^*$ be the $\ell$-Sylow of $\mathbf{S}^0(F_v)$. Thus $\Gamma_z \subset \Gamma_z^*$. 




  
 
Choose a complement $\mathbf{S}' \subset \mathbf{A}$ to $\mathbf{S}^0$, i.e. a subtorus  
with the property that $\mathbf{S}^0 \times \mathbf{S}' \rightarrow \mathbf{A}$ is an isomorphism.  

Now $\Gamma \subset \mathbf{A}(F_v)^{\circ}$ is an $\ell$-Sylow by computation of orders, so
therefore $$\Gamma = \Gamma_z^* \times \Gamma'$$
where $\Gamma'$ is the $\ell$-Sylow of $\mathbf{S}'(F_v)^{\circ}$. 

If $\mathbf{S}'$ were trivial, then $\mathbf{S}^0 = \mathbf{A}$;   in that case,  by (b) of \S \ref{doublecentralizer}, 
$z$ lies in the fixed set of $\mathbf{A}(F_v)^{\circ}$, which is none other\footnote{ Let $\mathbf{N}$ be the unipotent radical of the Borel $\mathbf{B} \supset \mathbf{A}$. 
If $\mathbf{A}(F_v)^{\circ} x K_v = x K_v$, we have  $x^{-1} \mathbf{A}(F_v)^{\circ} x \subset K_v$.
By using the Iwasawa decomposition, it is enough to check that if this inclusion holds
 for some $x=n \in \mathbf{N}(F_v)$, then in fact $n \in K_v$.   
 In that case we have $n^{-1}  a  n \in K_v$   for all $a \in \mathbf{A}(F_v)^{\circ}$,
 and in particular $n^{-1} ( \Ad(a) n) \in K_v$ for all such $a$.
 
Choose a generic positive element $\lambda \in X_*(\mathbf{A})$, giving an enumeration of the positive roots $\alpha_1, \dots, \alpha_s$
so that $\langle \alpha_i, \lambda \rangle$ is increasing. 
For each such root
 we have a root subspace $u_{i}: \mathbf{G}_a \rightarrow
 N$, and the product map  $u_s(x_s) u_{s-1}(x_{s-1}) \dots u_1(x_1)$, 
 from $\mathbf{G}_a^s \rightarrow \mathbf{N}$, 
extends to an isomorphism
 of  schemes    over $\mathcal{O}_v$. In this ordering, the commutator
$[u_{i}, u_j]$ involves only $u_{k}$ with $k > \max(i,j)$. 
 
Let $x_1$ be the $\alpha_1$ coordinate of $n$. We have $(\alpha_1(a)-1) x_1 \in \mathcal{O}_v$
 for all $a \in \mathbf{A}(F_v)^{\circ}$, which implies $x_1 \in \mathcal{O}_v$, cf.  second paragraph of the proof of Lemma 
\ref{splitness}. Adjust $n$ on the right by $u_{1}(-x_1)$
 to arrange that $x_1$ is trivial. Now proceed the same way for the $\alpha_2, \alpha_3, \dots$ coordinate. 
 } than 
$$X_* \subset G_v/K_v,$$
which contradicts our assumption. Therefore, $\mathbf{S}'$ is nontrivial. We see at once that the order of $\Gamma'$ is divisible
by the $\ell$-part of $q-1$.

Thus, by Lemma \ref{ff2}, the corestriction from $\Gamma_z^*$ to $\Gamma$ is zero with $\Z/\ell^r$ coefficients. 
The corestriction from $\Gamma_z$ to $\Gamma$ factors through this one, so it is zero too. 












 
  
  \qed

  
  
 

\subsection{Proof of Theorem   \ref{DHA:Satake}}\label{Satake algebra proof}
Throughout the proof, as in the statement of the theorem, we take coefficients in $S = \Z/\ell^r$. Accordingly, we drop explicit
mention of the coefficients from the notation. 
 
 
 Recall the explicit description of the Satake map, using the identification
 \eqref{alterpres} of the toral derived Hecke algebra: 
 
 Given an assignment
 $(x,y) \in G_v/K_v \mapsto h(x,y) \in H^*(G_{xy})$, we associate
 to it the  function  $X_* \times X_* \longrightarrow H^*(T)$, given by 
 $$h': (x,y) \in (A_v/A_v \cap K_v)^2 \mapsto \mathrm{Res}^{G_{xy}}_{T} h(x,y) \in H^*(T)$$
 
 
 
 We must show that  the rule
 $h \mapsto h'$ gives  an isomorphism
   \begin{equation} \mbox{ derived Hecke algebra for $(G_v, K_v)$} 
  \simeq \mbox{ derived Hecke algebra for $(A_v, A_v \cap K_v)$ }^W.
  \end{equation}
 
  
 


We  first verify that $h \mapsto h'$ is bijective. Each element of  the derived Hecke algebra  for $(G_v, K_v)$ is  uniquely of the form $\sum h_{a, \alpha}$
  where $a \in X_*^+$ and $\alpha \in H^*(K_v \cap \Ad(a) K_v)$, with notation as in \S \ref{doublecoset}. 
The intersection of $K_v a K_v$ with $X_*$
  is precisely given by the $W$-orbit of $a$ by uniqueness of the Cartan decomposition. 
  So the map $h \mapsto h'$ sends $h_{a, \alpha}$ to the  function $h'_{a, \alpha}$ on $X_* \times X_*$
  characterized by $W$-invariance and:  
   \begin{itemize}
  \item[(i)]$h_{z,\alpha}(x,e) = 0$ unless    $x \in W a$; 
  \item[(ii)]  $h_{z,\alpha}$ sends   $ (a, e) $ to  the image of $\alpha \in H^*(K_v \cap \Ad(a) K_v) \rightarrow H^*(T)$. 
  \end{itemize}
    It is enough, then, to show that each element of  $\mbox{ derived Hecke algebra for $(A_v, A_v \cap K_v)$ }^W$
  is uniquely a sum of such elements $h'_{a,\alpha}$.  This comes down to the fact that the map
\begin{equation} \label{isogn} H^*(K_v \cap \Ad(a) K_v) \longrightarrow  H^*(T)^{W_a} \end{equation}
  is an isomorphism, where $W_a$ is the stabilizer of $a$ in the Weyl group. 
  But, if we write $M$ for the Levi subgroup of $\mathcal{G}$
  that centralizes $a$, then $K_v \cap \Ad(a) K_v$ is, modulo a pro-$p$-group,
  the $k$-points $M(k)$, and $W_a$ is identified with the Weyl group of $M$. 
  So \eqref{isogn} follows from Lemma \ref{finitefields}. 
 
     

To show that  $h \mapsto h'$ preserves multiplication, we compute $(h_1 h_2)'(x,z)$; it equals  the restriction, from $G_{xz}$ to $T$, of
 $$ \sum_{O \subset G_v/K_v} \sum_{y \in O} h_1(x,y) \cup h_2(y,z).$$
the sum being grouped, as before, over orbits $O$ of $G_{xz}$ on such $y$. 
Recall that the inner sum  is understood by computing the cup-product $h_1(x,y) \cup h_2(y,z)$ for a single $y \in O$, 
and then corestricting from $G_{xyz}$ to $G_{xz}$.  
Therefore,

$$(h_1 h_2)'(x,z)  = \sum_{O}  \underbrace{ \mathrm{Res}^{G_{xz}}_T \mathrm{Cores}^{G_{xz}}_{G_{xyz}} h_1(x,y) \cup h_2(y,z) }_{:= H(O)}$$
and as usual we can express $H(O)$ a sum over
 $T$-orbits on $G_{xz}/G_{xyz}$, that is to say, as a sum of $T$ orbits  $O' \subset O$:
\begin{equation} \label{yuk}  H(O) =\sum_{O'} \mathrm{Cores}^{T}_{T_{y'}} \mathrm{Res}^{G_{xyz}}_{T_{y'}} (\dots )\end{equation}
where we have chosen a representative $y' \in O'$ for each $T$-orbit $O'$ upon $O$; and
  the  injection $T_{y'} \rightarrow G_{xyz}$ that defines the restriction map is induced by an element of $G_{xz}$
conjugating $y'$ to $y$. 

We saw  in Lemma \ref{splitness} that the corestriction map vanishes unless $y'$ actually belongs to $X_*$. 
(Indeed, writing $\Gamma$ for the unique $\ell$-Sylow of  the abelian group $T$, 
then $\Gamma_{y'}$ is an $\ell$-Sylow of $T_{y'}$,
and the corestriction map induced by $\Gamma_{y'} \rightarrow T_{y'}$ is surjective on cohomology.)

In the case when $y' \in X_*$, we have  $T_{y'} = T$ in which case $O' = \{y'\}$. We conclude that 
$$H(O) =\sum_{y' \in O \cap X_*}  \mathrm{Res}^{G_{xyz}}_{T}(h_1(x,y) \cup h_2(y,z))

$$

and finally adding up all $O$ we get
\begin{eqnarray*}(h_1 h_2)'(x,z) &=& \sum_{y \in X_*}  \mathrm{Res}^{G_{xyz}}_{T} (h_1(x,y) \cup h_2(y,z) ) \\ 
 &=& \sum_{y \in X_*}  \mathrm{Res}^{G_{xy}}_{T}  h_1(x,y) \cup  \mathrm{Res}^{G_{yz}}_{T}  h_2(y,z)  =   h_1' h_2' (x,z).\end{eqnarray*}
This concludes the proof of the theorem.

---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-016-8-examples-and-applications
section_title: "Examples and Applications"
section_number: 8
pages: 21-23
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
text_source: latex
latex_prose_ratio: 0.653
latex_coverage_ratio: 0.969
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
\subsection{Examples}
We now examine three examples.  The first two consider minimal categorifications of the adjoint representation, while the third studies the categorification of the $n$-fold tensor product of the standard representation of $\fsl_n$.  For ease of presentation, we ignore gradings and consider non-quantum categorical representations.

\begin{example}
Let's consider the first non-trivial example of Theorem \ref{thm:mincat}: the minimal categorification of the adjoint representation of $\fsl_2$.  We can model this as follows:
$$
\begin{tikzcd}
\kk\mmod \arrow[rr, bend left, "ind"] &  & R\mmod \arrow[rr, bend left,"res"] \arrow[ll, bend left, "res"] &  & \kk\mmod \arrow[ll, bend left, "ind"]
\end{tikzcd}
$$
where $R=\kk[x]/(x^2)$ \cite[Example 5.17]{CR}.  Here $\kk\mmod$ is the $\pm2$ weight category, and $R\mmod$ is the zero weight category.  The arrows describe the $\sE,\sF$ functors (we omit the higher structure). 

Consider the Rickard complex $\Theta=\Theta\bone_0:D^b(R\mmod) \to D^b(R\mmod)$.  For $M\in R\mmod$, we have:
\begin{align*}
\Theta(M)=R\otimes_\kk M \to M,
\end{align*}
where the differential is given by the action map, and $M$ is in  cohomological degree $0$.  It's an exercise to verify that $\Theta(M)$ is quasi-isomorphic to $M'[1]$, where $M'$ is the twist of $M$ by the automorphism of $R$ given by $a+bx \mapsto a-bx$.  This shows that $\Theta[-1]$ is the t-exact equivalence $M\mapsto M'$.
\end{example}

\begin{example}
More generally, one can consider the minimal categorification of the adjoint representation of a simple simply-laced Lie algebra $\fg$.  This was studied by Khovanov and Huerfano in \cite{HuerKh}, who used zigzag algebras to model this category.  

For a weight $\alpha$ of the adjoint representation of $\fg$, the weight  category $\cC_\alpha$ is taken to be $\kk\mmod$ as long as $\alpha\neq 0$.  However, the zero weight  category is more interesting:  $\cC_0 := A \mmod$, where $A$ is the zigzag algebra associated to the Dynkin diagram $I$ of $\fg$ (cf. \cite{HuerKh} for the precise definition).  

The isomorphism classes of indecomposable projective left $A$-modules $\{P_i\}$ and the isomorphism classes of indecomposable projective right $A$-modules $\{Q_{i}\}$ are both indexed by $i \in I$.  Tensoring with these modules defines functors 
\begin{align*}
	&\sE_i: \cC_0 \longrightarrow \cC_{\alpha_i}, \quad M \mapsto Q_{i} \otimes_{A} M, \\
	&\sE_i : \cC_{-\alpha_i} \longrightarrow \cC_0, \quad  V \mapsto  P_i\otimes_\kk V.
\end{align*}
The functors $\sF_i$ are defined analogously and are biadjoint to the $\sE_i$.

The Rickard complex
$\Theta_i \bone_0$ is given by tensoring with the complex
$$
	P_i\otimes_\kk Q_i \rightarrow A
$$
of $(A,A)$-bimodules, where the differential is given by the multiplication in $A$, and $A$ sits in cohomological degree zero.  These functors are autoequivalences of the derived category $D^b(\cC_0)$.  

By Theorem \ref{thm:mincat}  $\Theta_{w_0}\bone_0[-n]$ is t-exact, where $n+1$ is the Coxeter number of $\fg$.  
This auto-equivalence can be explicitly described as follows: the automorphism of the Dynkin diagram $\tau:I\to I$ induces an automorphism $\psi$ of $A$.  Then we claim that $\Theta_{w_0}\bone_0[-n]$ is the abelian autoequivalence of $A\mmod$ defined by twisting with $\psi$.  Indeed, since $\Theta_{w_0}\bone_0[-n]$ is an abelian autoequivalence, it is determined up to isomorphism by its action on simple objects.  Moreover, the action on simple objects can be read off from the action of $W$ on the Grothendieck group of $A \mmod$ as follows: $[A \mmod]_\ZZ$ is isomorphic to the Cartain subalgebra by mapping $[L_i]$ ($L_i$ is the simple head of $P_i$) to the simple root vector $H_i$.  And on the root vectors we have that $w_0\cdot H_i = -H_{\tau(i)}$ 
\end{example}


\begin{example}\label{ex:catO}
Let $\fg=\fsl_n$ and consider the $n$-fold tensor power of the standard representation $V^{\otimes n}$.  Categorifications of $V^{\otimes n}$ have been well-studied, and a model $\cC$ for this categorical representation can be constructed using the BGG category $\cO$ of $\fg$ \cite{Sussan2007, MS09}.  In this model, the principal block $\cO_0 \subset \cO$ appears as the zero weight category of $\cC$, and the Rickard complexes acting on $D^b(\cO_0)$ are the well-known shuffling functors.

By Theorem \ref{thm:perveq} $\Theta_{w_0}\bone_0:D^b(\cO_0)\to D^b(\cO_0)$ is a perverse equivalence with respect to an isotypic filtration.  In fact, this recovers the type A case of a theorem of the third named author \cite{LosCacti}, using completely different methods (in \cite{LosCacti} the perversity of $\Theta_{w_0}$ is proved using the theory of W-algebras).  We can interpret the filtration of $\cO_0$ arising from our perspective concretely using the Robinson-Schensted correspondence .  

Recall that the simple objects in $\cO_0$ are the irreducible highest weight representations $L(w), w \in S_n$, where $L(w)$ has highest weight $w\rho-\rho$ ($\rho$ is the half-sum of positive roots of $\fsl_n$). 

We view a partition $\lambda$ of $n$  simultaneously as a dominant integral weight for $\fsl_n$, and as an index for the irreducible Specht module $S^\lambda$ of the symmetric group $S_n$. Let $\SYT(\lambda)$ denote the set of standard Young tableau of shape $\lambda$, and let $d(\lambda)=|\SYT(\lambda)|$.  Recall that $d(\lambda)=\dim S^\lambda$.  


Choose an ordering of the partitions of $n$, $\lambda_1,\hdots,\lambda_r$, so that if $\lambda_i \prec \lambda_j$ in the dominance order, then $i<j$.  Note that the dominance order on partitions of $n$ is equivalent to the positive root ordering on partitions (thought of as weights for $\fsl_n$).
By Remark \ref{rem:isofilts} there is an isotypic filtration on $\cC$,
$
0 \subset \cC_1 \subset \cdots\subset \cC_N=\cC,
$
where  $\cC_i/\cC_{i-1}$ is an isotypic categorification of type $\lambda_i$.  Then  $\Theta_{w_0}$ is a perverse equivalence with respect to the filtration $\cO_{0,i} = \cO_0\cap \cC_i$ and the perversity function $p(i)=ht(\lambda_i)$.


We would like now to define the categories $\cO_{0,i}$ more explicitly using the Robinson-Schensted correspondence, which recall is a bijection \cite{Sagan}:
\begin{align*}
\mathsf{RS}:S_n \longrightarrow \bigsqcup_{j=1}^r\SYT(\lambda_j)\times\SYT(\lambda_j), \; w \mapsto (P(w),Q(w)).
\end{align*}
We will use a crystal analogue of classical Schur-Weyl duality.  This is given by a crystal isomorphism: 
\begin{align}\label{eq:crystalSW}
\bB(\varpi_1)^{\otimes n} \longrightarrow \bigsqcup_{j=1}^r \bB(\lambda_j)\times\SYT(\lambda_j).
\end{align}

Now, recall that for a partition $\la$ of $n$, the underlying set of the crystal $\bB(\la)$ can be chosen to be the set of semistandard Young tableaux of shape $\la$ with entries $1,\hdots,n$, and the weight zero subset of $\bB(\la)$ is precisely $\SYT(\la)$.  
The essential point is that the isomorphism \eqref{eq:crystalSW} can be chosen so that it restricts to the map $\mathsf{RS}$ on the elements of weight zero (\cite[Theorem 3.5]{Shimozono}). (Note that  the elements of weight zero in $\bB(\varpi_1)^{\otimes n}$ are naturally identified with permutations of $1,\hdots,n$.)

This shows that as an element of the crystal $\bB(\varpi_1)^{\otimes n}$, $[L(w)]$ is in a connected component whose highest weight is the shape of $Q(w)$ (or equivalently $P(w)$).   
Therefore, following Remark \ref{rem:JHfromCrystal}, we can construct the isotypic filtration be defining  $\cO_{0,i}$ to be  the Serre subcategory of $\cO_0$ generated by $L(w)$ such that the shape of $Q(w)$ is among $\la_1,\hdots,\la_i$.






























\end{example}

\subsection{Type A combinatorics}\label{sec:typeA}

In this final section, we specialise to type A and discuss  the combinatorics of Kazhdan-Lusztig bases and standard Young tableaux from the vantage of perverse equivalences.   

Set  $I=A_{n-1}=\{1,\hdots,n-1\}$.
We continue with the notation in Example \ref{ex:catO} and view a partition $\lambda \vdash n$ simultaneously as a dominant integral highest weight for $\fsl_n$, and as an index of the Specht module $S^\lambda$. Recall that by Schur-Weyl duality, $L(\lambda)_0$ is isomorphic to $S^\lambda$.  The Kazhdan-Lusztig basis of the Hecke algebra naturally descends to a basis of $S^\la$, which we denote $\{C_T\}$ indexed by   $T\in\SYT(\lambda)$.  For further details we recommend the exposition in \cite{Rhoad}.  

Consider the  minimal categorification $\cL(\lambda)$, and in particular its zero weight category $\cL(\lambda)_0$.  For convenience, we forget the grading and work in the non-quantum setting.  The simple objects $L(T)  \in \cL(\lambda)_0$ are indexed by $T\in \SYT(\lambda)$, and hence a perverse equivalence $\sF:D^b( \cL(\lambda)_0) \to D^b( \cL(\lambda)_0)$ induces a bijection $\varphi_\sF:\SYT(\lambda) \to \SYT(\lambda)$.  

The bijection $\varphi_I$ studied in the previous section specialises to the well-known Sch\"utzenberger involution on standard Young tableau, otherwise known as the ``evacuation operator'' $e$ \cite{Sagan}.  Indeed, by Theorem \ref{thm:agree} $\varphi_I$ recovers the cactus group action on the crystal $\Irr(\cC)$ by generalised Sch\"utzenberger involutions.  The Sch\"utzenberger involution is well-known to agree with the evacuation operator \cite[Theorem A1.2.10]{StanleyII}).  Note that this is elementary: it follows directly from the fact that the evacuation operator satisfies the properties of Definition \ref{def:genSchutz} on standard Young tableaux.

The promotion operator $j:\SYT(\lambda)\to \SYT(\lambda)$ is another important function in algebraic combinatorics, which is closely connected to the RSK correspondence and related ideas such as jeu de taquin.  
Letting $J=\{1,\hdots,n-2\}\subset I$, we can express promotion in terms of the Sch\"utzenberger involution: $j=\varphi_I\varphi_{J}$.
We refer the reader to \cite{Sagan} for a detailed exposition.  We can now see easily that promotion also arises from a perverse equivalence:

\begin{Proposition}\label{prop:promo}
Let $c_n=(1,2,\hdots,n)\in S_n$ be the long cycle.  Then $$\Theta_{c_n}:D^b( \cL(\lambda)_0) \to D^b( \cL(\lambda)_0)$$ is a perverse equivalence whose associated bijection is the promotion operator: $\varphi_{\Theta_{c_n}}=j$.
\end{Proposition}

\begin{proof}
Notice that $c_n=w_0w_0^J$ for $J$ as above. 

Now recall that $\Theta_{w_0}$ is (up to shift) a t-exact  autoequivalence of $D^b( \cL(\lambda)_0)$ (Theorem \ref{thm:mincat}).  Since $\Theta_{w_0^J}$ is a perverse equivalence (Theorem \ref{thm:perveq}),  its inverse is too.  Therefore $\Theta_{c_n}\cong\Theta_{w_0}\Theta_{w_0^J}^{-1}$ is also a perverse autoequivalence. 
By Lemma \ref{lem:texactperv} we have that $\varphi_{\Theta_{c_n}}=\varphi_I\varphi_J$, and hence we recover the promotion operator.
\end{proof}

We can also use this set-up to extract information about the action of $S_n$ on the Kazhdan-Lusztig basis of $S(\lambda)$.  This is based on the following elementary lemma:

\begin{Lemma}\label{lem:KLact}
Let $w \in S_n, \lambda \vdash n$ and suppose $\Theta_w :D^b(\cL(\lambda)_0) \to D^b(\cL(\lambda)_0)$ is t-exact up to shift. 
Then for any $T \in \SYT(\lambda)$, $w\cdot C_T=\pm C_{S}$, where $S=\varphi_{\Theta_w}(T)$.
\end{Lemma}

\begin{proof}
Since $\Theta_w$ is t-exact up to shift, we have: 
\begin{align*}
[\Theta_{w}(L(T))]=\pm [L(S)].
\end{align*}
The result now follows since the isomorphism $[\cL(\lambda)_0]_\CC \cong S^\lambda, L(T) \mapsto C_T$, is $S_n$-equivariant, and  by \cite[Proposition 10]{BauqWeyl}, the action of the braid group $B=B_n$ on $L(\lambda)_0$  factors through $S_n$.
\end{proof}

Applying this lemma to Theorem \ref{thm:mincat} we obtain a result of Berenstein-Zelevinsky and Stembridge:

\begin{Corollary}\cite{BZ96, Stem96} 
The action of the longest element  on the Kazhdan-Lusztig basis recovers the Sch\"utzenberger evacuation operator, i.e. for $w_0 \in S_n, \lambda \vdash n$ and $T\in \SYT(\lambda)$, we have that 
$w_0\cdot C_T =\pm C_{e(T)}$.
\end{Corollary}

Similarly we can prove a result of Rhoades regarding the action of the long cycle  $c_n=(1,2,\hdots,n)$ on the Kazhdan-Lusztig basis.  Note that in the statement below the significance of $\lambda$ being rectangular  is that the restriction of $S(\lambda)$ to $S_{n-1}$ in this case remains irreducible. 

\begin{Proposition}(cf. \cite[Proposition 3.5]{Rhoad})
Let $\lambda=(a^b)\vdash n$ be a rectangular partition.  Then for any $T \in \SYT(\lambda)$, the action of the long cycle on the Kazhdan-Lusztig basis element $C_T$ recovers the promotion operator:
$$
c_n\cdot C_T=\pm C_{j(T)}.
$$ 
\end{Proposition}

\begin{proof}
As above, set $J=\{1,\hdots,n-2\} \subset I$.  Recall that, since $\cL(\la)$ is a simple categorification, we know  $\Theta_{w_0}:D^b( \cL(\lambda)_0) \to D^b( \cL(\lambda)_0)$ is t-exact up to shift by Theorem \ref{thm:mincat}. However, $L(\la)|_{\fsl_{n-1}}$ is no longer simple, so a priori we only know that $\Theta_{w_0^J}:D^b( \cL(\lambda)_0) \to D^b( \cL(\lambda)_0)$ is perverse, but not necessarily t-exact up to shift.
We first prove that $\Theta_{w_0^J}$ is indeed t-exact up to shift.  

Consider the set of functors which are monomials in the Chevalley functors indexed by $J$:
\begin{align*}
\bM=\{\sG_{j_1}\cdots \sG_{j_s}\;|\; \sG \in \{\sE,\sF \},\;  j_\ell \in J \}.
\end{align*}
Let $\cC$ be the abelian category generated by $\{\sM(X)\;|\; X \in \cL(\lambda)_0,\sM \in \bM\}$, that is, $\cC$ is the category closed under subobjects and quotients of objects of the form $\sM(X)$.  Since the Chevalley functors are exact, it is easy to see that $\cC$ is a categorical representation of $U_q(\fsl_{n-1})$.  

Let $\nu \vdash (n-1)$ be the (unique) partition obtained from $\lambda$ by removing a box.  We claim that $\cC$ is a categorification of $L(\nu)$.  Note that this is  a categorification of the fact that $L(\nu) \cong U_q(\fsl_{n-1})\cdot L(\lambda)_0$.  Indeed, it is clear that $[\cC]_\CC$ contains $L(\nu)$.  On the other hand, if $\cC_\mu\neq0$ then $\mu$ is in the root lattice of $\fsl_{n-1}$, and $L(\nu)$ is the unique constituent of $L(\lambda)|_{\fsl_{n-1}}$ whose weights are in the root lattice.  

Now observe that $\cC_0=\cL(\lambda)_0$. Hence, by Corollary \ref{cor:mainthm} it follows that $\Theta_{w_0^J}:D^b( \cL(\lambda)_0) \to D^b( \cL(\lambda)_0)$ is t-exact up to shift.  Since $\Theta_{w_0}$ is also t-exact up to shift, it follows that $\Theta_{c_n}$ is too.  The result now follows by Proposition \ref{prop:promo} and Lemma \ref{lem:KLact}.
\end{proof}




































\maketitle

---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-024-82-type-a-combinatorics
section_title: "Type A combinatorics"
section_number: 8.2
pages: 23-24
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.967
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
\label{sec:typeA}

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

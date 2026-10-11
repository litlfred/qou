---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-006-33-crystals
section_title: "Crystals"
section_number: 3.3
pages: 7-9
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.931
---
We recall the definition of a crystal. 

\begin{Definition} [\cite{Kash90}] A \textbf{$\fg$-crystal} is a finite set $\bB$ together with maps:
	$$\tilde{e}_i,\tilde{f}_i:\bB \rightarrow \bB\sqcup \{0\}, \quad \eps_i,\phi_i : \bB\rightarrow \ZZ, \quad \wt: \bB \rightarrow X$$
	for all $i \in I$, such that:
	\begin{enumerate}
		\item for any $b,b' \in \bB$, $\tilde{e}_i(b)=b'$ if and only if $b=\tilde{f}_i(b')$ ,
		\item for all $b \in \bB$, if $\tilde{e}_i(b) \in \bB$ then $\wt(\tilde{e}_i(b))=\wt(b)+\alpha_i$, and if $\tilde{f}_i(b) \in \bB$ then $\wt(\tilde{f}_i(b))=\wt(b)-\alpha_i$,
		\item for all $b \in \bB$, $\eps_i(b)=\max\{n \in \ZZ~:~\tilde{e}^n_i(b) \neq 0\}$, $\phi_i(b)=\max\{n \in \ZZ~:~\tilde{f}^n_i(b)\neq 0\}$,
		\item for all $b \in \bB$, $\phi_i(b)-\eps_i(b)=\left\langle \wt(b),h_i\right\rangle$.
	\end{enumerate}
\end{Definition}

Any $U_q(\fg)$-representation $V$ has a corresponding $\fg$-crystal $\bB=\bB_V$.  The underlying set of $\bB$ is in natural bijection with a particular basis of $V$ (the ``global crystal basis'' or ``canonical basis'').  The maps $\tilde{e}_i,\tilde{f}_i$ are related to the raising and lowering Chevalley operators; vaguely speaking they encode information about the leading terms of the Chevalley operators acting on this basis. In particular, for an integral dominant weight $\la$, the canonical basis $\bB(\la)$ of $L(\la)$ carries a natural crystal structure \cite{GL92}.

The crystal  of $V$ naturally arises via categorical representation theory. Namely, as we describe in the next proposition, if $\cC$ is a categorification of $V$, then $\Irr(\cC)$ carries a crystal structure isomorphic to $\bB_V$. This follows  from \cite[Proposition 5.20]{CR} and \cite{LV}, and is explained in detail in \cite{BDcryst}.  

\begin{Proposition}(\cite[Theorem 4.31]{BDcryst})\label{prop:cryst}
	The set $\Irr(\cC)$ together with:
	\begin{itemize}
	 \item Kashiwara operators defined as $\widetilde{\sE}_i(X)=\operatorname{soc}{\sE_i(X)}$, $\widetilde{\sF}_i(X)=\operatorname{soc}{\sF_i(X)}$ for $X \in \Irr(\cC)$, 
	 \item $\wt(X) = \mu$ for $X \in \cC_\mu$, and
	 \item $\varepsilon(X)=max\{ n \;|\; \sE_i^n(X)\neq 0\}$, and $\varphi(X)=max\{ n \;|\; \sF_i^n(X)\neq 0\}$,
	 \end{itemize}
	  is a $\fg$-crystal isomorphic to the crystal $\bB=\bB_V$.
\end{Proposition}






\subsection{Jordan-H\"older series}
A categorification of a simple representation (respectively an isotypic representation)  is called  a \textbf{simple categorification} (respectively an \textbf{isotypic categorification}).
There is a  distinguished  categorification of $L(\lambda)$ called the \textbf{minimal categorification} and denoted $\cL(\lambda)$ \cite{CR,Rou2KM,KLI,Webmerged,KK}. It  is characterized by the fact that $\cL(\lambda)_{\lambda}\cong \cL(\lambda)_{w_0(\lambda)} \cong \kk\mmod_{\ZZ}$.  We let $\kk_{low} \in \cL(\lambda)_{w_0(\lambda)}, \kk_{high}\in \cL(\lambda)_{\lambda}$ be the generators.  








The Jordan-H\"older Theorem for categorical representations will play an important role in our work.  
This was originally developed by Rouquier for additive categorifications \cite{Rou2KM}, and in this section we transfer these results to the abelian setting.
To set this up, recall that given finite abelian $\kk$-linear categories $\cA,\cB$ the \textbf{Deligne tensor product} $\cA \otimes_\kk \cB$  is universal for the functor assigning to every such abelian category $\cC$ the category of bilinear bifunctors $\cA \times \cB \to \cC$ right exact in both variables \cite[Definition 1.11.1]{EGNO}.  The tensor product is again a finite abelian $\kk$-linear category, and there is a bifunctor $\cA \times \cB \to \cA \otimes_\kk \cB, (X,Y) \mapsto X\otimes Y$.  This construction enjoys the following properties: 
\begin{enumerate}
\item The tensor product is unique up to unique equivalence,
\item for finite $\kk$-algebras $A,B$ we have that $(A\mmod)\otimes_\kk (B\mmod) \cong (A\otimes_\kk B)\mmod$, and
\item $\Hom_{\cA \otimes_\kk \cB}(X_1\otimes Y_1, X_2\otimes Y_2) \cong \Hom_\cA(X_1,Y_1)\otimes\Hom_\cB(X_2,Y_2)$.
\end{enumerate}

Let $\cC$ be a categorical representation, and let $\cA$ be a finite $\kk$-linear abelian category.  We can endow $\cC \otimes_\kk\cA$ with a structure of a categorical representation, by setting $(\cC \otimes_\kk\cA)_\mu=\cC_\mu \otimes_\kk\cA$, defining Chevalley functors $\sE_i\bone_\mu \otimes \bone_\cA$, etc.  If $\cC$ is a simple categorification, then clearly  $\cC \otimes_\kk\cA$ is an isotypic categorification.  Conversely, we have:  

\begin{Lemma}\label{lem:isocat}
Let $\cC$ be an isotypic categorification of type $\lambda \in X_+$.  Then there exists an abelian category $\cA$ such that $\cC \cong \cL(\lambda)\otimes_\kk \cA$.  
\end{Lemma}


\begin{proof}
Since $\cC$ is an isotypic categorification, so is $\cC\proj$.  By Rouquier's Jordan-H\"older series for additive categorifications \cite[Theorem 5.8]{Rou2KM}, there exists an additive $\kk$-linear category $\cM$ such that 
\begin{align*}
\cC\proj\cong (\cL(\lambda)\proj \otimes_\kk \cM)^i.
\end{align*}
Note that no filtration appears here since, in the notation of \cite{Rou2KM}, $(\cC\proj)_{-\lambda}^{lw}=(\cC\proj)_{-\lambda}$.

Let $\{P_i\}$ (respectively $\{Q_j\}$) be a complete list of the projective indecomposable objects of $\cL(\lambda)$ (respectively $\cM$).  Let $P=\bigoplus_{i,j}P_i\otimes Q_j$, and let $B=\End_\cC(P)^{op}$.  By Morita theory, $B\mmod\cong \cC$.  On the other hand,
\begin{align*}
B\cong \End_{\cL(\lambda)}(\bigoplus_i P_i)^{op} \otimes \End_\cM(\bigoplus_j Q_j)^{op}.
\end{align*}
Since $\cL(\lambda)\cong \End_{\cL(\lambda)}(\bigoplus_i P_i)^{op}\mmod$ we have the desired result with $\cA=\End_\cM(\bigoplus_j Q_j)^{op}\mmod$.
\end{proof}

\begin{Theorem}\label{thm:JH}
Let $\cC$ be a categorical representation of $U_q(\fg)$.  Then there exists a filtration by Serre subcategories
\begin{align}\label{eq:JHfiltration}
0=\cC_0 \subset \cC_1\subset \cdots\subset \cC_n=\cC, 
\end{align}
such that for each $i$: $\cC_i$ is a subrepresentation of $\cC$, 
$\cC_{i}/\cC_{i-1}$ is a simple categorification of type $\lambda_i\in X_+$, and the list of highest weights is weakly increasing so that $\la_i \prec \la_j \Longrightarrow i<j$. 
\end{Theorem}

\begin{proof}
The $\fg$-crystal $\Irr(\cC)$ is isomorphic to a finite direct sum of irreducible crystals $\bB(\la)$ for various $\la$, i.e. we have an isomorphism
$$
\Irr(\cC) \cong \bigoplus_{\la\in X_+} \bB(\la)^{\oplus m_\la},
$$
where $m_\la \geq 0$ and only finitely many are nonzero.

Define $M=\{ \la \in X_+ \;|\; m_\la\neq0\}$, and let $\la \in M$. We claim that there exists a highest weight simple object $L \in \cC_\la$.  Indeed, otherwise for any simple object $L\in \cC_\la$ there exists $i\in I$ such that $\sE_i(X) \neq 0$.  This implies that $\soc(\sE_i(X))\neq 0$, and by Proposition \ref{prop:cryst} we conclude that $\Irr(\cC)$ has no highest weight elements of weight $\la$,  a contradiction.  

Now take $\la \in M$  which is minimal with respect to $\preceq$, and let $L \in \cC_\la$ be a highest weight object.
 Let $\cC_1$ be the Serre subcategory of $\cC$ generated by objects
\begin{align}\label{eq:Serregens}
\{\sF_{i_1}\cdots \sF_{i_\ell}(L)\;|\; i_j\in I, \ell \geq 0\}.
\end{align}
By the exactness and bi-adjunction of the Chevalley functors, $\cC_1$ is  a subrepresentation of $\cC$.  Moreover it categorifies $L(\lambda)$.  Indeed, by our choice of $\lambda$ there cannot be any highest weight objects with weight $\prec\lambda$ occuring in $\cC_1$, and by construction the only simple object in  $(\cC_1)_\lambda$ is $L$.  

Next consider the categorical representation $\cC/\cC_1$ and repeat this construction.  This produces a Serre subcategory $\cC_2' \subset \cC/\cC_1$ which is again a simple categorification.  Let $\pi:\cC \to \cC/\cC_1$ be the natural quotient functor, and define $\cC_2=\pi^{-1}(\cC_2')$.  Clearly, we have that $\cC_1\subset \cC_2$, $\cC_2$ is Serre, it is a subrepresentation, and $\cC_2/\cC_1 \cong \cC_2'$ is a simple categorification.  

Iterating this process produces a filtration of $\cC$ such that each composition factor is a simple categorification, and the highest weights of the subquotients are weakly increasing.
\end{proof}
















































\begin{Remark}\label{rem:isofilts}
Note that the construction in the proof of Theorem \ref{thm:JH} can produce also an isotypic filtration with similar properties.  Namely, if $\la_1,\hdots,\la_N$ is a list of the \textit{distinct} isotypic types appearing in $[\cC]_{\CC(q)}$, and we choose any ordering of this list so that $\lambda_i \prec \lambda_j \Longrightarrow i <j$, then there is a filtration $0=\cC'_0 \subset \cC'_1\subset \cdots\subset \cC'_N=\cC$ such that $\cC'_{k}/\cC'_{k-1}$ categorifies the isotypic component of $[\cC]_{\CC(q)}$ of highest weight $\lambda_k$.  To construct this isotypic filtration, consider the  Jordan-H\"older filtration  from the theorem.  From the proof of Theorem \ref{thm:JH}, it's easy to see that one can ensure that the subquotients which categorify the same simple representations appear in sequence.  Assuming then that our Jordan-H\"older filtration satisfies this property, a coarsening of it is  the desired isotypic filtration.
\end{Remark}


\begin{Remark}\label{rem:JHfromCrystal}
Note that one can read off the isotypic filtration of $\cC$  from the crystal structure on $\Irr(\cC)$.  Indeed, suppose that $\Irr(\cC)$ decomposes into  components 
$$
\Irr(\cC)=\bX(\la_1) \sqcup \cdots \sqcup \bX(\la_N),
$$
where $\la_1,\hdots,\la_N \in X_+$ are distinct dominant integral weights, and $\bX(\la_i)$ is a disjoint union of copies of $\bB(\la_i)$.  Further, we arrange the weights  as above so that  $\la_i \prec \la_j \Longrightarrow i < j$.  Let $\cC_i$ be the Serre subcategory of $\cC$ generated by simple objects $L$ such that $[L] \in \bX(\la_j)$, where $j \leq i$.  Then it follows from Remark \ref{rem:isofilts} that $\{0\} \subset \cC_1 \subset \cC_2 \subset \cdots \subset \cC_N$ is an isotypic filtration of $\cC$.
\end{Remark}

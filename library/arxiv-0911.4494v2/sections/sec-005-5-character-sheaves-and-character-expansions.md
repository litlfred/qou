---
doc_id: arxiv-0911.4494v2
doc_title: "The geometry of Markov traces"
section_id: sec-005-5-character-sheaves-and-character-expansions
section_title: "Character sheaves and character expansions"
section_number: 5
pages: 9-11
source_pdf: 0911.4494v2.pdf
source_sha256: 1ba1c79686b12d98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.955
doc_brief: "The geometry of Markov traces — We give a geometric interpretation of the Jones-Ocneanu trace on the Hecke algebra, using the equivariant cohomology of sheaves on SLn."
---
Any trace on a semi-simple algebra can be
expanded as a direct sum of the traces on irreducible representations,
i.e. as a sum of irreducible characters.  A formula for this was given
in type A by Ocneanu \cite{Wenzl}, in type B by Orellana
\cite{Orellana}, and in arbitrary type by Gomi \cite{Gomi}.  Using
our geometric perspective, we can give a much simpler proof than that
of \cite{Gomi}, which depended on case-by-case analysis.








Our proof is founded on the fact that the expansion of the Hecke
algebra as a sum of matrix algebras has a geometric manifestation:
given a simple perverse sheaf $\IC_w$, we can apply the ``averaging''
functor $\ind^{\GD}_{\BD}\colon D^b_{\BD}\!(G)\to D^b_{\GD}\!(G)$.
Since $G/B$ is projective, each summand
of $\iIC_w=\ind^{\GD}_{\BD}\IC_w$ is a shift of a simple perverse
sheaf by the Decomposition Theorem.
\begin{defi}
  A simple perverse sheaf in $D^b_{\GD}\!(G)$ is called a {\bf
    unipotent character sheaf} if it appears as a summand of $\iIC_w$
  for some $w$.  Following \cite[\S 5.2]{MSp}, we let $\widehat G(1)$
  denote the set of unipotent character sheaves.
\end{defi}

We choose our normalization so that each $\cV \in \widehat G(1)$
extends a local system of weight 0 in degree 0. Let $\widehat W$ denote the set of irreducible characters of $W$. For each
$\chi \in \widehat W$ there exists a unipotent character sheaf
$\cV_{\chi} \in G(1)$ whose restriction to the regular semi-simple
elements of $G$ is a local system with monodromy given by
$\chi$. Let us denote by $\widehat{ G}(1)_{ex}$ those
character sheaves in $\widehat G(1)$ which are not isomorphic to a character sheaf of the form
$\cV_{\chi}$ for $\chi \in \widehat W$.

Since induction is adjoint to restriction, we have a natural isomorphism
\begin{equation} \label{eq:ind-res}
  \hc_{\GD}\!(G;\iIC_w)\cong \hc_{\BD}\!(G;\IC_w).
\end{equation}
One might hope that the decomposition of $\iIC_w$ into simple character sheaves categorifies the formula expressing the trace of $C^{\prime}_w$ in terms of  the irreducible characters of the Hecke algebra. If this were the case then, by \eqref{eq:ind-res} we could write the weights of our trace in terms of the mixed Poincar\'e polynomials of simple character sheaves. We will see below that this is true after performing Lusztig's Fourier transform.

For $\cV\in \widehat G(1)$, we let $P_\cV(q,t)$ denote the
$G_\Delta$-equivariant mixed Poincar\'e polynomial of $\cV$.  Let
$\{\chi^{\prime} ,\chi\}$ be the matrix coefficients of Lusztig's Fourier transform.
\begin{prop}\label{weight}
 The weight $\varpi_\chi$ of the
  character $\chi$ in $\Tr$ is
  \begin{equation*}
    \varpi_\chi=\sum_{\chi^{\prime} \in \widehat W }
    \{\chi^{\prime},\chi\}\cdot P_{\cV_{\chi^{\prime}}}(q,t)
  \end{equation*}
\end{prop}
\begin{proof}


















For the course of the proof consider $\mathscr S$ the split Grothendieck group of $D^b_{G_{\Delta}}(G)$. If $\F \in D^b_{G_{\Delta}}(G)$ we denote by $[\F]$ its class in $\mathscr S$ and, given a polynomial $a = a_i q^{\nicefrac{i}{2}} \in \mathbb{Z}[q^{\pm \nicefrac{1}{2}}]$ we set
\[
a \cdot [\F] := \sum_i a_i [\F \langle -i \rangle ] \in \mathscr S.
\]
In this notation, combining Lusztig's formula \cite[14.11]{LusCSIII} and \cite[23.1]{LusCSV} we obtain
\begin{equation} \label{lus-Kw}
[\iIC_w] = \sum_{\chi, \chi^{\prime} \in \widehat W} \chi_q (C_w^{\prime}) \{ \chi^{\prime}, \chi \} \cdot [\cV_{\chi'}]  +  \sum_{\cV \in \widehat{ G}(1)_{ex}} a_{\cV} \cdot  [\cV].
\end{equation}
Some remarks are in order about why our formula is equivalent to Lusztig's:
\begin{itemize}
  \item  Firstly, note that for Lusztig's objects $\bar K_{w}$ we have $\bar
  K_{w} \langle \ell(w)\rangle \cong \iIC_w$ and Lusztig normalizes
  character sheaves so as to be perverse.  
\item Secondly, note that
  \cite[14.11]{LusCSIII} is an equality after forgetting mixed
  structures, however this can be lifted to the mixed setting by using
  the fact that $\iIC_w$ is pure of weight zero. 
\item Thirdly, the sign
  $\epsilon_{\cV_{\chi}}$ (see \cite[13.10]{LusCSIII}) is equal to
  $(-1)^{\dim G}$ as $A_{\chi}$ occurs as a direct summand of the
  Springer sheaf $\iIC_{\id}$.
\end{itemize}


We show in Proposition \ref{formal} below that the $G_{\Delta}$-equivariant cohomology of any $\cV \in \widehat G(1)_{ex}$ is zero. Hence, applying hypercohomology to \eqref{lus-Kw} we obtain (note also \eqref{shifttwist})
\[
\Tr(C^{\prime}_w) =P_{\IC_w}(q,t)=P_{\iIC_w}(q,t)
=\sum_{\chi\in \widehat W} \chi_q(

C_w^{\prime} )\Big(\sum_{\chi^{\prime} \in \widehat
   W}\{\chi^{\prime},\chi\} \cdot P_{\cV_{\chi^{\prime}}}(q,t)\Big)
   \]
   and the proposition follows.
\end{proof}







































Thus,
the primary point remaining to us is the computation of the mixed
Poincar\'e polynomial $P_\cV(q,t)$.  Our first step is to show that a
number of character sheaves have trivial cohomology.

If $L\subset G$ is the Levi of a parabolic, then there are adjoint
{\bf parabolic restriction} and {\bf parabolic induction} functors
\begin{equation*}
  \xy
(0,0)*{D^b_{L_\Delta}(L)}="A";
(40,0)*{D^b_{\GD}\!(G)}="B";
{\ar@/_12pt/_{\Ind^G_L} "A";"B"};
{\ar@/_12pt/_{\Res^G_L} "B";"A"};
\endxy
\end{equation*}
relating the conjugation-equivariant derived categories of these groups, defined by Lusztig \cite{LusCSI}.  These functors are different from the usual restriction and induction functors on equivariant derived categories, which we write uncapitalized.

For each character sheaf $\cV$, there is up to conjugacy a unique minimal Levi $L_\cV$ such that $\cV$ is a summand of $\Ind^G_L\cV'$ where $\cV'$ is a strongly cuspidal character sheaf on $L$.  This is also the minimal Levi for which $\Res^G_L\cV\neq 0$.

In the equivariant derived category $D_{\GD}\!(G)$, these Levi subgroups index a block decomposition of the category generated by character sheaves.   That is,
\begin{prop}\label{block}
  If $\cV,\cW$ are character sheaves and
  $\Ext_{\GD}^\bullet(\cV,\cW)\neq \{0\}$, then $L_\cV$ is conjugate to $L_\cW$.   

In particular, if $L_\cV\neq T$, then $\hc_{\GD}\!(G;\cV)=\{0\}$ and $P_\cV(q,t)=0$.
\end{prop}
\begin{proof}
  This was proved in the non-equivariant situation by Lusztig in
  \cite[7.2]{LusCSII}, and the equivariant result follows immediately from the existence of the spectral sequence
  \[
  E_2^{p,q} = \Ext^q(\cV,\cW) \otimes H_{\GD}^{p}(pt) \Rightarrow \Ext_{\GD}^{p+q}(\cV,\cW). \qedhere
  \] \end{proof}

One simple corollary of Proposition \ref{block} is that:

\begin{thm}\label{formal}
  Any unipotent character sheaf is $\GD$-equivariantly formal.
\end{thm}
\begin{proof}
If $\cV$ is induced from a cuspidal sheaf on a non-abelian Levi, then by Proposition \ref{block}, $\hc_{G_\Delta}(\cV)=0$, so $\cV$ is equivariantly formal.

On the other hand, every character sheaf not covered by the
previous assertion is a summand of $\IndGT$, which is equivariantly formal, since $\IC_{1}=\Qlb_B$ is.
\end{proof}

This allows us to answer definitively a question answered positively for type A in a previous paper of the authors \cite{WW}.

\begin{cor}
  For any $G$ and any $w\in W$, the sheaf $\IC_w$ is
  $\BD$-equivariantly formal.
\end{cor}
We thank Hailong Dao for help with the following proof. 
\begin{proof}
The sheaf $\iIC_w$ is equivariantly formal, since it is a sum of unipotent character sheaves.  
Thus the cohomology $H^*_{\BD}(\IC_w)=H^*_{\GD}(\iIC_w)$ is free as a module over $H^*(B\GD)$; we wish to conclude that it is free as a module over the larger ring $H^*(B\BD)$. 

This follows from standard arguments in commutative algebra: since $\Spec H^*(B\BD)$ is smooth, it suffices to show that the depth of the stalk at each point is the dimension of the variety.  On the other hand, this follows immediately from Proposition 1.2.16 in \cite{BH}, and the fact that both $H^*(B\BD)$ and $H^*(B\GD)$ are smooth and thus Cohen-Macaulay.
\end{proof}

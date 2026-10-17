---
doc_id: arxiv-0911.4494v2
doc_title: "The geometry of Markov traces"
section_id: sec-006-6-character-sheaves-and-molien-series
section_title: "Character sheaves and Molien series"
section_number: 6
pages: 11-13
source_pdf: 0911.4494v2.pdf
source_sha256: 1ba1c79686b12d98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.916
latex_coverage_ratio: 0.931
doc_brief: "The geometry of Markov traces — We give a geometric interpretation of the Jones-Ocneanu trace on the Hecke algebra, using the equivariant cohomology of sheaves on SLn."
---
\label{sec:char-sheav-moli}

Proposition \ref{block} shows that in equation (\ref{weight}), we need only sum over the sheaves
that appear as summands of $\IndGT$, since the trivial local system is
the only unipotent character sheaf on $T$.  Let us give a more careful description of these sheaves.

Consider the variety $\tG=G_\Delta\times_{B_\Delta}B$ and let
$c:G_\Delta\times_{B_\Delta}B\to G$ be the map induced by
$(g,t)\mapsto gtg^{-1}$.  A unipotent character sheaf is induced from $T$ if and only if it is a summand of $\IndGT=c_*\underline{\Qlb}_{\tG}$.

It is known that the map $\tG\to G$ is small, and so the sheaf $\IndGT$ is the intermediate extension of a local system on the regular semi-simple locus $G_{reg}$, since $\tG_{reg}\to G_{reg}$ is a Galois covering with Galois group $W$.  Because intermediate extension preserves endomorphism rings, 
\[
\End(\IndGT)=\End_{\Qlb W}(\Qlb W)=\Qlb W.
\] 
Thus, the isomorphism types of simple summands which appear are in canonical bijection with simple representations of $W$. Given an irreducible character $\nu \in \widehat W$ recall that we denote by $\cV_{\nu}$ the corresponding unipotent character sheaf.

Set $\ft^* = X(T) \otimes_{\mathbb{Z}} \Qlb$, where $X(T)$ denotes the lattice of characters of $T$. Note that $\ft*$ is a $W$-module in a natural way, and set $E = \Sym^\bullet(\ft^*)\otimes
\wedge^\bullet\ft^*$, which we may view as a $W$-module with the tensor product action. We have a canonical identification $E \cong H^*_{T_\Delta}(T)$.
The geometric realization of this algebra equips it with a bigrading by degree and weight as in Section \ref{sec:categorified-trace}. Given an irreducible character $\nu \in \widehat W$ the graded dimension
\[
M_\nu(q,t)=\sum_{i,j}q^{i/2}t^{j-i}\dim\Hom_W(V_\nu,E)^{i,j}
\]
is called the {\bf Molien series} of $\nu$.
\begin{prop}
\begin{math}
     \displaystyle H^\bullet_{G_\Delta}(\cV_\nu)= \Hom_W( V_{\nu}, E).
\end{math}
\end{prop}


\begin{proof}
Because $K_1 = c_* \Qlb_{\widetilde{G}}$ we have canonical isomorphisms
\begin{equation} \label{eq:E1}
H^\bullet_{\GD}(\IndGT)\cong H^\bullet_G(\widetilde{G}) \cong H^\bullet_{\BD}(B)\cong H^{\bullet}_T(pt) \otimes H^{\bullet}(T) \cong E.
\end{equation}
The $W$-action on $\IndGT$ induces a $W$-action on $E$ such that with this induced action 
\[
H^\bullet_{\GD}(\cV_\nu,E)= \Hom_W (V_\nu, E).
\]  
Thus, we need only check that the induced $W$-action on $E$ via the the isomorphisms \eqref{eq:E1} is the natural action.  Since $W$ acts by algebra homomorphisms, it suffices to check this on $H^1$ and on pure classes in $H^2$. To this end, note that the restriction map
\begin{equation} \label{eq:reg-restrict}
H^\bullet_G(\widetilde{G}) \to H^\bullet_G(\widetilde{G}_{reg})
\end{equation}
is $W$-equivariant, where the $W$-action on $H_G(\widetilde{G}_{reg})$ is induced by the deck transformations of the covering $\widetilde{G}_{reg} \to G_{reg}$. We claim that the restriction map \eqref{eq:reg-restrict} is an injection on $H^1$ and an isomorphism on the subspace of pure classes.

We may identify $\widetilde{G}_{reg} = G/T \times T_{reg}$. Under this identification the $W$-action by deck transformations is given by $w \cdot (gT, t) = (g\dot{w}^{-1}T, \dot{w}t\dot{w}^{-1})$. Furthermore the $G$-action on $T_{reg}$ is trivial and hence
\begin{equation} \label{eq:E2}
H^\bullet_G(\widetilde{G}_{reg}) = H^\bullet_G(G/T) \otimes H^{\bullet}(T_{reg}) \cong H^\bullet_T(pt) \otimes H^{\bullet}(T_{reg}).
\end{equation}
It is straightforward to check that under the isomorphisms \eqref{eq:E1} and \eqref{eq:E2} the restriction map \eqref{eq:reg-restrict} is the tensor product of the identity on $H_T^{\bullet}(pt)$ and the restriction map $H^\bullet(T) \to H^\bullet(T_{reg})$ on ordinary cohomology.

Now $T_{reg}$ is obtained from the smooth variety $T$ by removing a divisor, and so $H^{\bullet}(T) \to H^{\bullet}(T_{reg})$ is injective on $H^1$ and there are no pure classes in positive degree in either group. Hence the pure classes in both \eqref{eq:E1} and \eqref{eq:E2} consists of the image of $H^{\bullet}_T(pt)$. It follows that \eqref{eq:reg-restrict} is injective on $H^1$ and an isomorphism on pure classes as claimed.

Finally, given the above description of the action of $W$ on $G/T \times T_{reg}$ one may conclude that the induced action of $W$ on \eqref{eq:E2} is the tensor product of the natural action of $W$ on $H_T(\pt) = \Sym^\bullet(\ft^*)$ and action induced by conjugation on $H^\bullet(T_{reg})$. The proposition then follows.
\excise{
For the latter, this follows by \cite[Theorem 7.2.2]{CG97}; for the former, a theorem of Ginzburg  \cite[Theorem 8.1]{Ginzburg-character} shows that the category of perverse sheaves Serre generated by $\IndGT$ is equivalent to the representations of the smash product $\Qlb[W]\# \Sym^\bullet \ft$ sending $\IndGT$ to $\Qlb[W]$ with trivial $\Sym^\bullet \ft$-action.  Thus, we have that \[H^1(\IndGT)=\Ext^1_{\mathsf{Perv}}(\Qlb_{G},\IndGT)=\Ext^1_{\Qlb[W]\#\Sym^\bullet h}(\Qlb,\Qlb[W])=\Ext^1_{\Sym^\bullet \ft}(\Qlb,\Qlb)=\wedge^\bullet\ft^*\] with the natural $W$-action. 
}
\end{proof}

This geometric realization of the Molien series allows us to arrive at
the main theorem of \cite{Gomi} by a very different route.
\begin{cor}\label{final}
  For all characters $\nu\in \widehat W$, we have
  $M_\nu(q,t)=P_{\cV_\nu}(q,t)$. In particular, by Proposition
  \ref{weight}, it follows that

  \begin{equation*}
    
    \Tr(x)=\sum_{\chi\in\widehat W}\chi_q(x)\cdot\{\chi,\nu\}\cdot M_\nu(q,t).
  \end{equation*}
\end{cor}



\begin{remark}\label{smash}
  The above identification of the cohomology of a character sheaf with a multiplicity space reflects a deeper fact about the structure of $\GD$-equivariant sheaves on $G$: by an extension of the arguments above, one can construct a natural isomorphism $\Ext^\bullet_{G_{\Delta}}(\IndGT)\cong \Qlb[W]\#E$ as bigraded algebras. This provides an equivariant version of a theorem of Ginzburg \cite[Theorem 8.1]{Ginzburg-character}. \end{remark}

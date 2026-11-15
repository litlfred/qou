---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-021-72-the-cactus-group-action-arising-from-rickard
section_title: "The cactus group action arising from Rickard complexes"
section_number: 7.2
pages: 18-20
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.938
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
We now explain how  cactus group actions arise from categorical representations, analogous to the construction of the crystal on $\Irr(\cC)$ in Proposition \ref{prop:cryst}.

Let $\cC$ be a categorical representation of $U_q(\fg)$.  For any weight $\mu \in X$, by Theorem \ref{thm:perveq} $\Theta_{w_0}\bone_\mu:D^b(\cC_\mu) \to D^b(\cC_{w_0(\mu)})$ is a perverse equivalence, and hence it induces a bijection $\varphi_I1_\mu:\Irr(\cC_\mu) \to \Irr(\cC_{w_0(\mu)})$.  By varying $\mu$  we obtain a bijection 
$
\varphi_I:\Irr(\cC) \to \Irr(\cC).
$  

Now let $J\subseteq I$ be a connected subdiagram, and let $\fg_J \subset \fg$ be the corresponding subalgebra.  By restriction, $\cC$ is also a categorical representation of $U_q(\fg_J)$, and hence by the above discussion we also obtain a bijection $
\varphi_J:\Irr(\cC) \to \Irr(\cC).
$


We will prove that this family of bijections defines an action of the cactus group $\Irr(\cC)$.  First we need the following technical result.  The important point here is just that there exists an integer $n$ such that 
$\st^2_{w_0}\sone_\mu=\pm q^n\sone_\mu$.

\begin{Lemma}\label{lem:fulltwist}
Let $\lambda\in X_+, \mu \in X$, and let $\mu-w_0(\lambda)=\sum_{r=1}^\ell \alpha_{i_r}$, where $i_r\in I$.  Set $j_r=\tau(i_r)$ and 
define $n(\la,\mu)\in\ZZ$ by 
    $$
    n(\la,\mu)=2\left(\sum_{r=1}^\ell \la_{j_r}+1-\sum_{1\leq r\leq s\leq \ell}a_{j_rj_s}+(\la,\rho)\right)
    $$
    Then on  $L(\lambda)_\mu$ we have \begin{align}\label{eq:fulltwist}\st^2_{w_0}\sone_\mu=(-1)^{\langle 2\lambda ,\rho^\vee \rangle}q^{n(\la,\mu)}\sone_\mu.\end{align}
\end{Lemma}

\begin{proof}
We will prove the  claim by induction on $ht(\mu-w_0(\la))$.  For $\mu=w_0(\la)$, we have that $\ell=0$ so  $n(\la,\mu)=(\la,\rho)$.  By \cite[Equation (7)]{KT}  $\st_{w_0}(v_\la)=(-1)^{\langle \lambda ,\rho^\vee \rangle}q^{(\la,\rho)}v_\la^{low}$, which, combined with Lemma \ref{lemma:KT}, implies that $\st_{w_0}^2(v_\la^{low})=(-1)^{\langle \lambda ,\rho^\vee \rangle}q^{(\la,\rho)}v_\la^{low}$.  Since $\dim(L(\la)_{w_0(\la)})=1$, this proves the base case.  

Now choose any $\mu$ and suppose (\ref{eq:fulltwist}) holds for any weight $\mu'$ such that $ht(\mu'-w_0(\la))<ht(\mu-w_0(\la))$.  Consider  $v=E_{j_1}\cdots  E_{j_\ell}v_\la^{low} \in L(\la)_\mu$.  First note that by \cite[Lemma 5.4]{KT} we have that
\begin{align}\label{lem:ftcomm}
\st_{w_0}^2E_i=q^2K_i^{-2}E_i\st_{w_0}^2.
\end{align}
Setting $v'=E_{j_2}\cdots  E_{j_\ell}v_\la^{low}$, by induction we have
\begin{align*}
\st_{w_0}^2v &= q^2K_{j_1}^{-2}E_{j_1}\st_{w_0}^2v' \\
&= (q^2K_{j_1}^{-2}E_{j_1})(-1)^{\langle \lambda ,\rho^\vee \rangle}q^{n(\la,\mu-\alpha_{j_1})}v' \\
&= (-1)^{\langle \lambda ,\rho^\vee \rangle}q^{2+n(\la,\mu-\alpha_{j_1})-2(\mu,\alpha_{j_1})}v
\end{align*}
One checks easily that $n(\la,\mu)=2+n(\la,\mu-\alpha_{j_1})-2(\mu,\alpha_{j_1})$, proving that $\st_{w_0}^2v=(-1)^{\langle \lambda ,\rho^\vee \rangle}q^{n(\la,\mu)}v$.  Since this holds for any vector of the form $E_{j_1}\cdots  E_{j_\ell}v_\la^{low}$ in $L(\la)_\mu$, this completes the inductive step.
\end{proof}



\begin{Theorem}\label{thm:cactus}
The assignment $c_J \mapsto \varphi_J$ defines an action of $C$ on $\Irr(\cC)$.
\end{Theorem}

\begin{proof} We need to show that the bijections $\varphi_J$ satisfy the cactus group relations. 










\textit{Relation (i)}: Without loss of generality we may assume $J=I$.   Fix a weight $\mu$.  Our aim is to show that 
\begin{equation}
\label{eq:rel1}
\varphi_I \varphi_I1_\mu=\Id_{\Irr(\cC_\mu)}.
\end{equation}



Since the filtration of $\cC_{w_0(\mu)}$ which we use in the perversity data of $\Theta_{w_0}\bone_\mu$, agrees with the filtration of $\cC_{w_0(\mu)}$ which we use in the perversity data of $\Theta_{w_0}\bone_{w_0(\mu)}$, by Lemma \ref{lem:pervcomp} the composition $\Theta_{w_0} \Theta_{w_0}\bone_\mu$ is a perverse autoequivalence of $D^b(\cC_\mu)$. 

The  functor $[\langle 2\lambda ,\rho^\vee \rangle]\langle n(\lambda,\mu)\rangle$ is also a perverse autoequivalence of $D^b(\cC_\mu)$.   By Lemma \ref{lem:fulltwist} these two perverse equivalences induce the same map on Grothendieck groups, and hence by Lemma \ref{lem:LosLem} they also induce the same bijection.  Since the bijection induced by $[\langle 2\lambda ,\rho^\vee \rangle]\langle n(\lambda,\mu)\rangle$ is the identity, this proves  relation (i).















\textit{Relation (ii)}:  Let $J,K \subset I$ be disjoint subdiagrams with no connecting edges.  Our aim is to show that
\begin{align}\label{eq:rel2}
\varphi_J\varphi_K1_\mu = \varphi_K \varphi_J1_\mu.
\end{align}
We prove a slightly more general statement, namely that for any categorical representation $\cC$ of $U_q(\fg_J \times\fg_K)$, relation (\ref{eq:rel2}) holds.

Note that $\Theta_J\Theta_K\bone_\mu\cong \Theta_K\Theta_J\bone_\mu$ are isomorphic perverse equivalences, so they induce the same bijections.  It remains to show that
\begin{align}\label{eq:rel2again}
\varphi_{\Theta_J\Theta_K\bone_\mu} =\varphi_J\circ\varphi_K 1_\mu.
\end{align}

Consider first the case when $\cC$ categorifies an simple representation of $U_q(\fg_J\times\fg_K)$.  A minimal categorification of $U_q(\fg_J\times\fg_K)$ is of the form $\cL(\lambda)\otimes_\kk\cL(\mu)$, where $\lambda$ is a highest weight for $\fg_J$ and $\mu$ is a highest weight for $\fg_K$.  Hence by Lemma \ref{lem:isocat}, a simple categorification of $U_q(\fg_J\times\fg_K)$ is of the form $\cL(\lambda)\otimes_\kk\cL(\mu)\otimes_\kk\cA$ for some abelian category $\cA$.  

This implies that as a categorical representation of $U_q(\fg_J)$ (respectively $U_q(\fg_K)$), $\cC$  categorifies an isotypic representation.  
By Corollary \ref{cor:mainthm} $\Theta_J\bone_{w_0^K(\mu)}$ and $\Theta_K\bone_\mu$ are t-exact up shift on isotypics categorifications.  Hence Equation (\ref{eq:rel2again}) follows by Lemma \ref{lem:pervcomp}.

Now consider a Jordan-H\"older filtration (Theorem \ref{thm:JH}):
\begin{align*}
0=\cC_0\subset \cdots\subset \cC_n=\cC,
\end{align*}
where for every $i$, $\cC_i$ is a  subrepresentation of $\cC$, and $\cC_i/\cC_{i-1}$ is a simple categorification of $U_q(\fg_J\times\fg_K)$.  Equation (\ref{eq:rel2again}) now follows by an easy induction on $i$.
Indeed the base case when $i=1$ holds by the paragraph above, and the inductive step by Lemma \ref{lem:quot}.












\textit{Relation (iii)}: We need to show that $\varphi_J\varphi_K1_\mu=\varphi_K\varphi_{\tau_K(J)}1_\mu$, where $J\subset K$.  Again, we may assume that $K=I$.  Note that we have an isomorphism at the level of functors:
\begin{align*}
\Theta_{w_0}^{-1}\Theta_{w_0^J}\Theta_{w_0}\bone_\mu \cong \Theta_{w_0^{\tau_K(J)}}\bone_\mu,
\end{align*}
which lifts the corresponding relation in $B$.  Since this is an isomorphism of perverse equivalences, they must induce the same bijections by Lemma \ref{lem:LosLem}.  

It remains to show that 
\begin{align}\label{eq:compo}
\varphi_{\Theta_{w_0}^{-1}\Theta_{w_0^J}\Theta_{w_0}\bone_\mu} =\varphi_I^{-1}\circ \varphi_J\circ \varphi_I.
\end{align}
When $\cC$ is a simple categorification, by Corollary \ref{cor:mainthm} $\Theta_{w_0}\bone_\mu$ is t-exact (up to shift).  Hence Equation (\ref{eq:compo}) follows by Lemma \ref{lem:texactperv}.  Now apply the same reasoning as in the proof of Relation (ii) to deduce equation (\ref{eq:compo}) in the general case.  


  





\end{proof}

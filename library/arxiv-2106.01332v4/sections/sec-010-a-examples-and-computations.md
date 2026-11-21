---
doc_id: arxiv-2106.01332v4
doc_title: "Braided matter interactions in quantum gravity via 1 -handle attachment"
section_id: sec-010-a-examples-and-computations
section_title: "A Examples and Computations"
section_number: null
pages: 11-13
source_pdf: 2106.01332v4.pdf
source_sha256: 44c19a99624997bf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 1.0
doc_brief: "Braided matter interactions in quantum gravity via 1 -handle attachment — 14 sections: Front matter; I Introduction; II A topological model of composit"
---
The computation of twists in Theorem~\ref{thm:invariant} suggests that the invariant $KL_n$ distinguishes, in general, the particles of Bilson-Thompson model, in the sense that two braided networks that are identical, except for two regions that enclose one of the particles of Figure~\ref{helonmodel} or Figure~\ref{bosons}, generally have different values of $KL_n$. Of course, in order to give a specific statement of this sort, regarding what particles are distinguished, one needs to fix the values of $q$ (i.e. $A$) and $n$. It is not the scope of the present article to fix values for them, but we rather are contented with showing that the theory is nontrivial. \\

We observe that no isotopy invariant of braided networks is suitable to distinguish $Z^0$ and $\gamma$ bosons, as they differ by an application of the framed Reidemeister move I which, by construction, is preserved by any isotopy invariant of braided networks. \\

By means of example we show that the invariant $KL_4$ does change when we replace a boson $\gamma$ by a boson $W^+$, so that the algebraic setting detects the topological non-equivalence of different bosons. Setting $n=4$, means that each ribbon edge is represented by parallel lines whose total sum does not exceed $6$. Since the two networks are assumed to be identical outside the region enclosing the two particles $W^+$ and $\gamma$, we can substantially compute the invariant $KL_4$ of $W^+$ and $\gamma$ as depicted in Figure~\ref{bosons}, as the computation of $KL_4$ would give identical values, when computing the rest of the braided network. We rewrite the twists of $W^+$ using the computation performed in the proof of Theorem~\ref{thm:invariant}. The computations are identical for each colouring, with the only difference being that one needs to take into account the number of strands in the twists. For example, trinions all coloured with two strands (the triple $\{2,2,2\}$ is $q$-admissible), gives us an overall factor of $A^{18}$ and the braids of $W^+$ are replaced by $R^2\otimes R^2\otimes R^2$, two consecutive crossings that braid the edges of each ribbon. We perform now smoothing of each crossing and utilize the definition of the Kauffman bracket polynomial. Observe that performing the two smoothings on a ribbon produces two diagrams, one with a straight ribbon and an extra factor of $A^2$, and one with the ribbon removed and a factor of $1-A^{-4}$. The computation is therefore reduced simply to the product of these factors. We denote by $|^i$ the braid with $i$ straight ribbons, where $i = 0,1,2,3$. We obtain that the braid $W^+$ can be replaced in the braided network by the sum of terms 
\begin{equation}\label{eqn:bosonW}
   W^+ = -A^{24}\cdot |^6 - A^{18}\cdot [A^2(1-A^{-4}) + 2A^4(1-A^{-4})]\cdot |^4 - A^{18}[(1-A^{-4}) + 2A^2(1-A^{-4})^2]\cdot |^2 - A^{18}(1-A^{-4})^3\cdot  |^0.
\end{equation}

By definition, we have that the evaluation with the boson $\gamma$, with the same colour, is simply $|^6$, which appears up to a factor in Equation~(\ref{eqn:bosonW}). When computing $KL_4$ of $W^+$, the terms with lower powers of $|$ disappear, since they contain turnbacks that are annihilated by the Jones-Wenzl projectors. In general, considering all colourings, $KL_4$ distinguishes the two bosons, as previously claimed. We remark that in the previous computation we have pairs of ribbons or single ribbons, instead of triples representing framed braids. In general, this is a middle step of a computation and, therefore, it is not to be considered as a physically meaningful configuration of a braided network.\\

It has been pointed out, in \cite{BT2}, that in order to introduce a nontrivial dynamics for braided particles, it is necessary to consider moves such that (what we have here called) braided networks do not constitute noiseless subsystems. In practice, what the authors of the article \cite{BT2} have realized, is that it is not enough to consider braided networks as arising from triangulations of manifolds and only local moves that are derived from Pachner moves. A natural question to ask, is whether performing surgery on manifolds to introduce dynamics represents an example of such a paradigm. We argue that this is indeed the case, and that the invariant $KL_n$ shows this. In fact, (very tedious) computations show that there are cases where the interaction/decay of two particles in a braided network, obtained via surgery as described above, produces another braided network whose $KL_n$ invariant is different from the initial one. Applying Theorem~\ref{thm:invariant} it follows that initial and final state are not isotopy equivalent and, therefore, the topology of the system has been changed during surgery, giving an affirmative answer to the previous question.  \\

We briefly describe the computations related to electron/positron annihilation producing one virtual photon. Recall that, in the setting of the present article, virtual means that the photon produced in the process lives on the handle that mediates the interaction. We set $n = 4$, and consider the colouring where all edges are assigned value $2$ (the remaining colours are computed in the same way). Let us indicate the value associated to this colouring by $KL^2_4(\mathcal N)$. Suppose that $e^+$ and $e^-$ are right-handed. First, observe that the value of two braided networks that are identical outside two regions containing $e^+$ and $e^-$ differ by a multiplication of a (Laurent) polynomial $f(A^{\pm 1})$, where $A$ refers to the positron, and $A^{-1}$ refers to the electron. Therefore, to compute $KL^2_4(\mathcal N)$, for a braided network $\mathcal N$ containing a positron and an electron, we can perform the computation of $KL^2_4(e^-)$ for the electron, and obtain the contribution of $e^+$ simply by changing the variable $A^{-1}$ to its inverse $A$. This computation can be simplified as follows. One first uses the formula obtained in Theorem~\ref{thm:invariant} to rewrite the twisting of each ribbon as composition of two negative crossings. This produces an overall factor of $-A^{-18}$ multiplying the braid corresponding to $e^-$. Now, we obtain a braid in pure twist form by applying two rotations of trinions \cite{BT2009}. We remark, here, that we can perform this operation by means only of framed Reidemeister moves, without twisting the vertex, or using the IH move, since the number of twists is even (due to the orientability assumption discussed above) \cite{Matsuzaki}. No overall multiplying factor is introduced during this process. We can also see this by applying Proposition~3 in Section 4.2 of \cite{KL}, since two opposite rotations would be utilized. In pure twist form, the right handed electron $e^-$ can be written as $[0,-2,-1]$, see table at page 12 of \cite{BT2009}. Now, we use the computation for the composition of two negative crossings $R^{-2} = A^{-2} \cdot |^2 + (1-A^4)\cdot |^0$, as obtained in Theorem~\ref{thm:invariant}, to complete the computation. This requires three iterations to give the result 
\begin{equation}\label{eqn:e-}
 KL^2_4(e^-) = -A^{-24}\cdot KL^2_4( |^6) + A^{-18}Q(A)\cdot KL^2_4(|^4) + A^{-18}P(A)(1-A^4)\cdot KL^2_4(|^2),   
\end{equation}
 where 
 \begin{equation}\label{def:PQ}
     P(A) := A^{-18}[2A^{-2}(1-A^4) - (1-A^4)(-A^2-A^{-2})],\ \  Q(A) := A^{-22}(1-A^4) - P(A)A^{-2}.
 \end{equation}
 
  As previously observed, we also have 
 \begin{equation}\label{eqn:e+}
  KL^2_4(e^+) = -A^{24}\cdot KL^2_4(|^6) + A^{18}Q(A^{-1})\cdot KL^2_4(|^4) + A^{18}P(A^{-1})(1-A^{-4})\cdot KL^2_4(|^2),  
 \end{equation}
 where the polynomials $P$ and $Q$ are defined in Equation~(\ref{def:PQ}).
  Let $\mathcal N$ be a braided network containing $e^-$ and $e^+$ and suppose that, via surgery on the base manifold, $\mathcal N$ undergoes an annihilation of $e^-$ and $e^+$ on an attached handle (over which a virtual boson is exchanged). Let us denote by $\mathcal N'$ the braided network obtained after surgery, and by $\hat{\mathcal N}$ the network obtianed from $\mathcal N$ by removing $e^+$ and $e^-$ and replacing them with two particles $\gamma$. From the computations giving Equation~(\ref{eqn:e-}) and Equation~(\ref{eqn:e+}) we have that 
\begin{equation}\label{eqn:annihilation}
 KL^2_4(\mathcal N) = KL^2_4(\hat{\mathcal N}) + KL^2_4(\text{ terms\ containing}\ \ Q(A^\pm), P(A^\pm))\,.   
\end{equation}
 
 The extra terms in Equation~(\ref{eqn:annihilation}) correspond to the braids with two ribbons, or a single ribbon, after the smoothings of $e^\pm$, and their coefficients do not generally vanish identically, but their contribution to $KL_4$ evaluations are trivial, since they contain turnbacks annihilated by the Jones-Wenzl projector. Summing the contributions due to the other $q$-admissible colourings, we see directly that the surgery corresponding to annihilation electron/positron changes the isotopy class of the braided network since, in general, we have that $KL_4(\hat{\mathcal N})$ is different from $KL_4(\mathcal N')$.

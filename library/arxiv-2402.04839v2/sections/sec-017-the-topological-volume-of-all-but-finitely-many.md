---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-017-the-topological-volume-of-all-but-finitely-many
section_title: "The topological volume of all but finitely many lens spaces"
section_number: null
pages: 19-21
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.991
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
Agol~\cite{agol-2cusped} showed that $W$ and $P$ are the minimal volume orientable hyperbolic 3-manifolds with two cusps. This property is key for the following:

\begin{reptheorem}{prop:lens-space-limit}
For all but finitely many homeomorphism types of lens spaces $L(p,q)$ ($p>q\geq 1$ coprime), the volume minimising link in $L(p,q)$ has complement one of $W(\frac{p'}{q'}, \infty)$ or $P(\frac{p''}{q''}, \infty)$, where the filling slopes $\frac{p'}{q'}$ and $\frac{p''}{q''}$ can be determined from an efficiently computable finite set. For $P$ this means that we fill along the unknotted component.
\end{reptheorem}

Throughout, the surgery coefficient $\frac{1}{0}$ is the filling with the infinity slope, while we do not write any slope if we leave one boundary component unfilled.

\begin{proof}
First note that, by \Cref{prop:isometry}, we can assume without loss of generality that we fill along the first cusp of both $W$ and $P$. Since the first cusp is an unknot (in $S^3$), it follows from the classification of lens spaces, that all Dehn fillings of $W$ or $P$ yielding a knot in $L(p,q)$ must have filling coefficients obtained from the following operations
\begin{align}
  (p,q) &\mapsto (p,q+np), & \forall n \in \mathbb{Z} \label{lenspace_1}\\
  (p,q) &\mapsto (p,q^*), & q^*q \equiv 1 \mod p \label{lenspace_2}\\
  (p,q) &\mapsto (-p,q), (p,-q).  \label{lenspace_3}
\end{align}
The volume functions ($\vol_W-\Delta \vol_W(p,q)$, for $\vol_W(p,q)$ from Equation \ref{eq:DvolP} and the correspondingly for $P$) derived by Hodgson and Masai in \cite{Hodgson_Masai} exclude all but finitely many fillings slopes satisfying \Cref{lenspace_1,lenspace_2,lenspace_3} from being volume minimising. 
Since these functions are strictly monotonically increasing with respect to their near-elliptical level sets (cf. \Cref{sec:dehnsurgeryspace}), this is a straightforward calculation.

With this setup, suppose to the contrary that there are infinitely many homeomorphism types of lens spaces $L(p_i,q_i)$, $p_i > q_i \geq 1$, with the property that some volume minimising link complement $M_i \subset L(p_i,q_i)$ is not homeomorphic with a Dehn filling on $P$ or $W.$ We may assume that $p_i^2 + q_i^2$ is sufficiently large, such that $W$ and $P$ have filling slopes resulting in hyperbolic knots in $L(p,q)$.

Hence for all $\frac{p'_i}{q'_i}$ obtained from $\frac{p_i}{q_i}$ by \Cref{lenspace_1,lenspace_2,lenspace_3} and with $W(\frac{p'_i}{q'_i})$, $P(\frac{p'_i}{q'_i})$ hyperbolic, we have $\volh(M_i) \le \volh(W(\frac{p'_i}{q'_i})),\volh(P(\frac{p'_i}{q'_i})) < \volh(W) = \volh(P)$. According to \cite{agol-2cusped}, $W$ and $P$ are the minimal volume orientable hyperbolic 3-manifolds with two cusps. Hence each $M_i$ has exactly one cusp.
Then $\{ \volh(M_i)\}$ is a set of volumes of hyperbolic manifolds with one cusp and bounded above by $\volh(W) = \volh(P).$ 

If this is a finite set, then there is $v_0\in \{ \volh(M_i)\}$ with the property that infinitely many of the manifolds $M_i$ have volume equal to $v_0.$ But then infinitely many lens spaces have the same volume, contradicting \Cref{pro:finiteness}.

Hence $\{ \volh(M_i)\}$ is an infinite set. But the first accumulation point for volumes of hyperbolic manifolds with one cusp is $\volh(W).$ However, a manifold with volume arbitrarily close to this value is obtained by Dehn surgery on either $P$ or $W$, a contradiction to our assumption.

This proves that all but finitely many lens spaces $L(p,q)$ have volume minimiser a Dehn filling on $P$ or $W.$ 
\end{proof}

\begin{corollary}
The sequence $(\;\volt(L(p,q))\;)_{(p,q)}$ converges, as $p^2+q^2\to\infty$, to the volume of the Whitehead link complement. \qed
\end{corollary}

\begin{corollary}
\label{cor:p-1}
The topological volume of the lens space $L(p,q)$ is realised by a knot, i.e.\ $h(L(p,q))=1$. Moreover, for $|p|$ sufficiently large, the minimiser of $L(p,1)$ is unique and the complement is a tunnel number one once-punctured torus bundle.
\end{corollary}

\begin{proof}
	Every lens space $L(p, q)$ is obtained as a $(-p/q)$-filling of the first component of (say) $P$. By performing an $n$-fold Rolfsen twist on that component we can change the surgery coefficient to $-p/(q+np)$. Thus we can assume that the filling slope is sufficiently large so that by Thurston's hyperbolic Dehn surgery theorem~\cite{Thurston_book} the other component of $P$ yields a hyperbolic knot in $L(p,q)$. But this implies that $\volt(L(p,q))<\vol(P)$. By Agol~\cite{agol-2cusped} any hyperbolic manifold with volume less than $\vol(P)$ has at most one cusp and thus the minimiser is a knot in $L(p,q)$.
  
  For the second statement, observe that $q$ must be within $\pm 1$ of a multiple of $p$ (see \Cref{lenspace_1,lenspace_2,lenspace_3}). Inserting this into the first terms of \Cref{eq:DvolW,eq:DvolP}, we can see that---for $p$ sufficiently large---the minimiser must be obtained by filling slope $(p, -1)$ on $W$ (setting $p\geq 0$ without loss): For $(p,\pm 1)$, the function $\Delta \vol_P (p,q)$ converges to $\frac{\pi^2}{2p^2}$ plus lower order terms, while $\Delta \vol_W (p,q)$ converges to $\frac{2\pi^2}{p^2}$ plus lower order terms; and we have $\Delta \vol_W (p,-1) = \frac{2\pi^2}{p^2 -4p + 1}$ while $\Delta \vol_W (p,1) = \frac{2\pi^2}{p^2 +4p + 1}$. And thus, the unique minimiser is given by an integer filling of the Whitehead link. These are known to be once-punctured torus bundles with tunnel number $1$~\cite[Theorem~1.3]{torus_bundles}.
\end{proof}

\begin{corollary}\label{cor:L4-is-special}
The lens space $L(4,1)$ has as a minimiser a one-cusped manifold of volume at most $\volh(m034)\approx 3.166$ and which is not obtained by Dehn filling $W$ or $P.$
\end{corollary}

\begin{proof}
The filling coefficients for $W$ and $P$ to obtain a knot in lens space $L(4,1)$ are precisely $(\pm 4, 2m+1)$, for $m \in \mathbb{Z}$. Of those, only $W((4,-1))$ and $P((4,1))$ are not hyperbolic: The former contains a splitting Klein bottle, the latter is a solid torus. The other cases can be verified to be hyperbolic using the $6$-theorem \cite{agol-bounds,lackenby-6} together with Snappy.

Using the volume bounds from \cite{FuterKalfagianniPurcell} for sufficiently large slopes together with direct computations using SnapPy for short slopes, we see that of the hyperbolic filling slopes, the smallest volume ones are $W((4,1))$ and $W((4,-3))$ with a volume of $\approx 3.17729$.  On the other hand, we have $\volt(L(4,1)) \le \volh(m034) \approx 3.166.$ 
\end{proof}

\begin{remark}
It is important to note that we require both the Whitehead link $W$ and its sister $P$ for \Cref{prop:lens-space-limit} to hold: The volume minimiser for $L(p,1)$, $p$ sufficiently large, is uniquely realised as filling $W(p,-1)$, as shown in \Cref{cor:p-1}. On the other hand, it can be deduced from \Cref{tab:complete} that $L(13,3)$ has minimiser $m011$ and $L(19,7)$ and $L(18,5)$ both have minimiser $m016$. But according to \Cref{tab:whichone}, these can only be obtained by Dehn fillings of $P$, but not of $W$. 
\end{remark}

We conclude this section with a question that is analogous to the third question in~\cite[\S 9]{Hodgson_Masai}.
\begin{question}
\label{q:largest}
What is the largest volume less than $\volh(W)$ of a one-cusped hyperbolic 3--manifold that does not arise from Dehn filling on $W=m129$ or $P=m125$? 
\end{question}

An answer to \Cref{q:largest} would allow us to give a quantitative version of \Cref{prop:lens-space-limit}.

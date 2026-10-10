---
doc_id: arxiv-2501.00914v2
doc_title: "L-SPACES AND KNOT TRACES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
text_source: latex
latex_prose_ratio: 0.639
latex_coverage_ratio: 0.828
doc_brief: "L-SPACES AND KNOT TRACES — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
Given a knot $K\subset S^3$ and an integer $n$, the \emph{$n$-trace} $X_n(K)$ is the smooth, oriented 4-manifold with boundary obtained from $B^4$ by attaching an $n$-framed 2-handle along $K\subset \partial B^4$. We say that $X_n(K)$ \emph{detects}  $K$ if its oriented diffeomorphism type determines $K$ --- that is, if \[X_n(J)\cong X_n(K) \] implies that $J=K$. In this paper, we propose and study the following question:

\begin{question}
\label{ques:traces}
For which knots $K\subset S^3$ and  integers $n$ does $X_n(K)$ detect $K$?
\end{question}

The $n$-trace  $X_n(K)$ is far from detecting $K$ in general \cite{akbulut-traces,lickorish-shake,AJOT}. This is prominently illustrated in Piccirillo's proof that the Conway knot is not slice, a key part of which involves finding a different knot with the same $0$-trace  \cite{piccirillo-conway}.

One way to prove that $X_n(K)$ detects $K$ is to show that its boundary $S^3_n(K)$, which is the result of $n$-framed Dehn surgery on $K$, does --- in other words, that $n$ is a \emph{characterizing slope} for $K$. A lot of effort has gone into  understanding  characterizing slopes for knots. Building on work by Lackenby  \cite{lackenby-characterizing} and McCoy \cite{mccoy-torus}, Sorya recently proved that for any knot $K$ all rational numbers with sufficiently large denominator are characterizing slopes, and if $K$ is composite then all non-integers are characterizing \cite{sorya}; see also \cite{sorya-wakelin}.  Deciding whether a given \emph{integer} characterizes a certain knot seems to be much harder in general, and this is especially true for the integer $n=0$. 

On this last point, Gabai proved in 1987 that $0$ is a characterizing slope for the unknot, figure-8, and trefoils in  \cite{gabai-foliations3}, and these were the only knots known to be characterized by their $0$-surgeries until we showed in 2022 that every \emph{nearly fibered} genus-1 knot is as well \cite{bs-nonfibered,bs-0-characterizing}. But it is still open, for example,  whether $0$ is a characterizing slope even for the torus knot $T_{2,5}$.

By contrast, our main result says that the $0$-trace detects every L-space knot:
\begin{theorem}
\label{thm:main}
If $K$ is an L-space knot then $X_0(K)$ detects $K$.
\end{theorem}

Here, $K\subset S^3$ is an \emph{L-space knot} if some positive Dehn surgery on $K$ is a Heegaard Floer L-space, meaning a rational homology 3-sphere $Y$ such that 
\[\dim \hfhat(Y) = |H_1(Y;\Z)|.\]
This class of knots includes all positive torus knots, as well as any other knot with a positive lens space surgery, like the $(-2,3,7)$-pretzel knot.

Theorem \ref{thm:main} follows from a combination of two results which may each be of independent interest. The first  says that any single trace detects \emph{whether} a given knot is an L-space knot:

\begin{theorem} \label{thm:lspace-detection-main}
If $K$ is an L-space knot and $X_n(J) \cong X_n(K)$, then $J$ is also an L-space knot and has the same genus as $K$. 
\end{theorem}

The $n=0$ case, which suffices for Theorem~\ref{thm:main}, can be deduced from our work in \cite{bs-fibered-sqp}, which in turn was inspired by our proof in \cite{bs-lspace} that \emph{instanton} L-space knots are fibered.  The general case builds on this but is considerably more involved; it further relies on results by Hayden--Mark--Piccirillo \cite{hayden-mark-piccirillo}, which also enable us to prove in Theorem \ref{thm:trace-determines-hfhat-restated} that any trace $X_n(K)$ with $n\geq 0$  determines the $\Z/2\Z$-graded Heegaard Floer homology of each positive rational surgery on $K$.

The second and more surprising ingredient in Theorem \ref{thm:main} is our result that if two L-space knots have the same 0-surgery then they are the same:
\begin{theorem} \label{thm:main-lspace-zero}
If $J$ and $K$ are L-space knots such that $S^3_0(J) \cong S^3_0(K)$, then $J=K$.
\end{theorem}
Theorem~\ref{thm:main-lspace-zero} relies on a deep relationship between the symplectic Floer homology of a surface diffeomorphism and the Heegaard Floer homology of its mapping torus, established via a combination of  work by Lee--Taubes \cite{lee-taubes} and Kutluhan--Lee--Taubes \cite{klt1}.

We used this relationship in joint work with Hu \cite{bhs-cinquefoil} to prove that if $K$ is a genus-2 hyperbolic L-space knot then the pseudo-Anosov representative of its monodromy has no fixed points, en route to proving  that Khovanov homology detects the cinquefoils; this was later used to prove that $T_{2,5}$ is the only  genus-2 L-space knot \cite{frw-cinquefoil}.     In \cite{ni-monodromy,ni-fixed}, Ni extended our argument to show  that the monodromy of \emph{any} nontrivial fibered knot  $K \subset S^3$ is freely isotopic to a map with at most
\begin{equation*}\label{eqn:dimminus1} \dim \hfkhat(K,g(K)-1) - 1 \end{equation*}
fixed points; see also Ghiggini--Spano \cite{ghiggini-spano}.  This is particularly useful when \[\dim \hfkhat(K,g(K)-1)=1,\] which holds, for instance, whenever $K$ is an L-space knot; more generally, we  call such  knots \emph{ffpf}, since they are fibered with fixed-point-free monodromy. Theorem \ref{thm:main-lspace-zero} is then a special case of our stronger result, Theorem~\ref{thm:zero-surgery-fpf}, which says  that no two ffpf knots have the same 0-surgery.

Our proof of Theorem \ref{thm:zero-surgery-fpf} goes very roughly as follows: suppose that $K$ is an ffpf knot with fiber surface  $\Sigma$ and monodromy $h$.  Let $\hat\Sigma$ be the closed surface obtained by capping  off $\Sigma$  with a disk, and let $\hat h$ be the \emph{closed  monodromy} obtained by extending $h$ by the identity over this  disk, so that $S^3_0(K)$ is the mapping torus of $\hat h$. The ffpf condition further implies  \cite{ni-exceptional} that $h$ is   \emph{veering}.  
We combine this with Ni's results about fixed points to argue that the canonical Nielsen--Thurston form of $\hat h$  has  a unique fixed point at the center of the capping disk. Removing the fiber over this fixed point then recovers the knot complement $S^3\setminus K$. 

Now let $J$ be another ffpf knot with closed monodromy $\hat g$ such  that \[S^3_0(J)\cong S^3_0(K).\] Since this manifold has a unique fibration, $\hat g$ is conjugate to $\hat h$. We  then use the rigidity of pseudo-Anosovs within their mapping classes \cite{flp} to show that the conjugating homeomorphism identifies the unique fixed points of the Nielsen--Thurston forms of $\hat g$ and $\hat h$. It follows that \[S^3\setminus J\cong S^3\setminus K,\]  and hence that $J=K$ by \cite{gordon-luecke-complement}. 


\subsection{Nonzero traces}
We  consider detection by nonzero traces as well, and prove several results that are in stark contrast with what is known about characterizing slopes. For instance, all rational surgeries characterize the trefoils  \cite{osz-characterizing}, but if $K$ is a positive torus knot besides the right-handed trefoil, then it is  unknown whether \emph{any} integer $n\leq 0$ is a characterizing slope for $K$. On the other hand, we use Theorem \ref{thm:lspace-detection-main} to prove the following:

\begin{theorem}
\label{thm:negtracetorus}
If $K$ is a positive torus knot and $n\leq 0$, then $X_n(K)$ detects $K$.
\end{theorem}

This leaves open the question of whether every trace detects each torus knot, which by Theorem \ref{thm:negtracetorus} is equivalent to asking whether every \emph{positive} trace detects each \emph{positive} torus knot. We expect this to be true for torus knots of the form $T_{2,2g+1}$, and  prove the following  result in that direction. Together with Theorem \ref{thm:negtracetorus}, this result implies  that if knot Floer homology detects $T_{2,2g+1}$ then  so does every trace; this knot Floer result  is   known  to hold when $|g| \leq 2$ \cite{osz-genus,ghiggini,frw-cinquefoil}.

\begin{theorem} \label{thm:positive-trace-t2n-main}
Suppose for some knot $K$ and  positive integers $n$ and $g$ that $X_n(K) \cong X_n(T_{2,2g+1}).$  Then either $K = T_{2,2g+1},$ or $1 \leq n \leq 4g-1$ and $K$ is a hyperbolic knot such that \[\hfkhat(K) \cong \hfkhat(T_{2,2g+1})\] as bigraded vector spaces.
\end{theorem}


We remark that not every positive integer is a characterizing slope for each positive torus knot, not even for torus knots of the form $T_{2,2g+1}$. For example, \[S^3_{21}(T_{4,5}) \cong S^3_{21}(T_{2,11}).\] In Appendix~\ref{sec:torus-pairs}, we describe infinitely many new pairs of distinct positive torus knots $(K,J)$  such that $S^3_n(K) \cong S^3_n(J)$ for some integer $n>0$, generalizing a family discovered by Ni--Zhang \cite{ni-zhang-torus-1} which includes the example above. On the other hand, Proposition~\ref{prop:compare-torus-surgeries} guarantees in this case that $g(K) \neq g(J)$, and then Theorem~\ref{thm:lspace-detection-main} implies that these knots are distinguished by their $n$-traces.










\subsection{Questions} Our results  above and their  comparisons with results about characterizing slopes raise many natural questions; we record a few of these here. The first asks whether we can upgrade our main result, Theorem \ref{thm:main}, to a statement about characterizing slopes:

\begin{question}
Is $0$ a characterizing slope for every L-space knot?
\end{question}

An affirmative answer   would follow from Theorem \ref{thm:main-lspace-zero} if one could show that  $0$-surgery, like the $0$-trace, detects whether a given knot is an L-space knot.

The class of ffpf knots contains but is much broader than the class of all nontrivial L-space knots, leading to the question below. Note that an affirmative answer would follow from Theorem \ref{thm:zero-surgery-fpf} if one could show that the 0-trace detects whether a knot is ffpf.

\begin{question}
Does the $0$-trace detect every ffpf knot?
\end{question}

One of the most important results on characterizing slopes is Lackenby's proof \cite{lackenby-characterizing} that every knot has one. On the other hand, Baker--Motegi showed in \cite{baker-motegi} that the knot $8_6$ has no \emph{integral} characterizing slope, which inspired the following question in the original version of this paper:

\begin{question}
Is every knot detected by at least one of its traces?
\end{question}

This question has since been answered in the negative by Baker--Kegel--Motegi in \cite{baker-kegel-motegi}.



Finally, our proof of Theorem \ref{thm:main} relies crucially on the fact that L-space knots are fibered with veering, fixed-point-free monodromy, as this guarantees that the closed monodromy has a unique fixed point such that the complement of the fiber over this fixed point recovers the knot complement. It is natural to ask whether there is an analogue of the ffpf condition for \emph{non-fibered} knots which guarantees something similar, for example:

\begin{question}
\label{ques:nonfibered}
Is there a condition on the knot Floer homology of a non-fibered hyperbolic knot $K\subset S^3$ which guarantees that there is  a pseudo-Anosov flow on $S^3_0(K)$ with exactly one orbit which generates the first homology of this surgery and whose complement recovers $S^3\setminus K$?
\end{question}

In \cite{baldwin-velavick}, Baldwin--Vela-Vick proved that if $K\subset S^3$ is a nontrivial fibered knot then \[\dim \hfkhat(K,g(K)-1) \geq \dim \hfkhat(K,g(K)) = 1.\] The ffpf condition is that this inequality is an \emph{equality}. So, perhaps the condition sought in Question \ref{ques:nonfibered} for a non-fibered knot $K$ is also that \[\dim \hfkhat(K,g(K)-1) = \dim \hfkhat(K,g(K)).\]
As noted in \cite{baldwin-velavick}, it is conjectured that the first is always greater than or equal to the second for non-fibered knots as well; this is still open.






\subsection{Conventions} We will only consider Heegaard Floer homology with coefficients in $\F = \Z/2\Z$. We will use $\cong$ to indicate orientation-preserving diffeomorphism throughout.

\subsection{Organization}  In \S\ref{sec:veering}, we review and prove some facts about surface diffeomorphisms and their dynamics, which we then  apply to prove Theorem~\ref{thm:zero-surgery-fpf} and consequently Theorem \ref{thm:main-lspace-zero}. In \S\ref{sec:large-surgeries}, we prove Theorem~\ref{thm:trace-large-surgery}, which says that if $n\geq 0$  then $X_n(K)$ determines the Heegaard Floer homology of large surgeries on $K$. It follows that the $0$-trace detects whether a  knot is an L-space knot, which together with Theorem \ref{thm:main-lspace-zero} implies our main result, Theorem~\ref{thm:main}. In \S\ref{sec:rational-surgeries}, we combine Theorem~\ref{thm:trace-large-surgery} with results from \cite{hayden-mark-piccirillo} to prove in Theorem~\ref{thm:trace-determines-hfhat-restated} that any trace $X_n(K)$  determines the Heegaard Floer homology of many or all rational surgeries on $K$; this quickly implies Theorem~\ref{thm:lspace-detection-main} as well.

The remainder of the paper is devoted to applying these results to nonzero traces of torus knots. In \S\ref{sec:torus-surgeries}, we prove Theorem~\ref{thm:negtracetorus} by combining Theorem~\ref{thm:lspace-detection-main} with   results about characterizing slopes for torus knots.  In \S\ref{sec:t2n-positive}, we focus on the torus knots $T_{2,2g+1}$,   proving Theorem~\ref{thm:positive-trace-t2n-main}. Finally, we describe in  Appendix~\ref{sec:torus-pairs} new infinite families of distinct positive torus knots with diffeomorphic $n$-surgeries. As explained above, the corresponding $n$-traces are not diffeomorphic, providing another illustration of the difference between trace detection and characterizing slopes.


\subsection{Acknowledgements} We thank Matt Hedden and Tye Lidman for helpful conversations, and the referee for a very careful reading and lots of detailed feedback on the original version of this paper.

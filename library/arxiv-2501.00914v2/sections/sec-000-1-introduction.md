---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.976
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
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

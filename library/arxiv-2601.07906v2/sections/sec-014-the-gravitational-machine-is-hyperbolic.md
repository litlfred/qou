---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-014-the-gravitational-machine-is-hyperbolic
section_title: "The gravitational machine is hyperbolic"
section_number: null
pages: 52-58
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 1.0
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
\label{subsec:machine is hyperbolic}
In this section, we prove one of the important results of this paper: 
that the gravitational machine maps hyperbolic manifolds to hyperbolic manifolds.  
This will follow from a rather nice interaction between topology and the conditions imposed on the statistical ensemble. It will turn out that the conditions \ref{cond:no Omega loops 2}, \ref{cond:no parallel rings 2} and \ref{cond:no Wilson line self gluing} on the gluing are precisely what is topologically needed to stay in the class of hyperbolic manifolds. The following section is somewhat mathematical, but central to our argument, which is why it is included in the main text. The reader that trusts us on this point can however jump to section~\ref{subsec:what 3-manifolds are generated}.

The proof proceeds by induction. Namely, suppose $M \in \mathcal{M}$ is hyperbolic. Then we will prove that after applying any of the moves \ref{move:disconnected sum}-\ref{move:gluing}, the resulting manifold $\widetilde{M}$ is also hyperbolic. Since our initial set of manifolds was the set of handlebodies (which are hyperbolic), we conclude that $\mathcal{M}$ only contains hyperbolic manifolds. 

\paragraph{Thurston's theorem.} To prove the induction step, we will examine the homotopy groups of the manifolds produced by the gravitational machine. The main workhorse in the proof is Thurston's hyperbolization theorem, which gives a topological criterion that decides whether a topological 3-manifold admits a hyperbolic structure. More precisely, it can be stated as \cite{Thurston:1982}:
\emph{
\begin{quote}
    The interior of a compact 3-manifold $M$ with nonempty boundary has a hyperbolic structure if and only if $M$ is prime, homotopically atoroidal and not homeomorphic to $(T^2\times [0,1])/\ZZ_2$. 
\end{quote}}
\noindent Let us clarify the terminology used in this theorem. Assuming that the closure of $M$ is \emph{compact} is a relatively weak finiteness condition, ensuring that the hyperbolic manifold is not too wild, for example it does not have infinitely many boundary components. 
A \emph{prime} manifold is a manifold that cannot be written as a non-trivial connected sum, meaning that $M=M_1 \# M_2$ implies that $M_1=\mathrm{S}^3$ or $M_2=\mathrm{S}^3$. Prime is implied and essentially equivalent to being \emph{irreducible}, which is the condition that the second homotopy group is trivial, $\pi_2(M) =0$.\footnote{The only manifold that is prime, but not irreducible is $\mathrm{S}^2 \times \mathrm{S}^1$, which is not hyperbolic.} Thus we will in the following replace prime by irreducible. \emph{Homotopically atoroidal} means that every map of $T^2$ to $M$ which acts injectively on the fundamental groups is homotopic to $\partial M$. This condition is equivalent to the condition that any subgroup of $\pi_1(M)$ isomorphic to $\mathbb{Z}\times \mathbb{Z}$ is conjugate to a subgroup of $\pi_1(\partial M)$.
We will in the following take atoroidal to mean homotopically atoroidal.\footnote{
In the literature, there are two similar but distinct notions of atoroidal 3-manifolds: homotopically atoroidal and geometrically atoroidal. A manifold is geometrically atoroidal if every \emph{embedded} torus with injective $\pi_1$ in $M$ is isotopic to a component of $\partial M$. In contrast, a manifold is homotopically atoroidal if every \emph{immersed} torus, including those with self-intersections, with injective $\pi_1$ is homotopic to a component of $\partial M$. The definition of homotopically atoroidal implies geometrically atoroidal, but the converse does not hold. There are irreducible geometrically atoroidal 3-manifolds $M$ that satisfy $\mathbb{Z}\times \mathbb{Z} \subset \pi_1(M)$, where the $\mathbb{Z}\times \mathbb{Z}$ factor is carried by an immersed torus that cannot be homotoped to $\partial M$. Notable examples include $\Sigma_{0,3}\times$S$^1$ (the product of a 3-punctured sphere with S$^1$), and the complement in S$^3$ of any torus knot. See e.g.~\cite{thurston1986hyperbolic} for more details.} 

We also need the notion of an \emph{incompressible surface}. These are surfaces $S\subset M$ whose fundamental group injects into the fundamental group of the 3-manifold. An incompressible surface is called \emph{boundary parallel} if it can be isotoped into a boundary component of $M$; otherwise, it is called \emph{essential}. Thurston's hyperbolization theorem implies that hyperbolic 3-manifolds do not contain essential tori. Connecting to the 3d gravity vocabulary, we note that a regular neighborhood of an essential torus is topologically a torus wormhole $T^2\times I$, showing that any bulk topology containing a torus wormhole is automatically off-shell. 

As an example of the above criteria, consider the complement in S$^3$ of the following handlebody-knot (to be discussed in section~\ref{subsec:handlebody-knots}), called $\mathbf{5}_4$ in table \ref{table:handlebodyknots}:
\begin{equation}
\label{eq:54}
\vcenter{\hbox{
\begin{tikzpicture}
\draw[line width=7pt,black]
(0.28, 0.22) to[out = 135, in =180]
(0.95,1.65) to[out =0, in = 90]
(1.9,0.1) to[out=270, in=-35]
(0.53,-1.46);
\draw[line width=7pt, black] 
(0.22,-1.14) to[out=135, in=225]
(0.38, 0.1) to[out =  45, in =-45]
(0.56,1.32);
\draw[line width=7pt, black]
(0.3, 1.5) to[out=145, in = 0]
(-0.25, 1.65);
\draw[line width=7pt, black]
(-0.25,-1.45) to[out = 0, in =-50, looseness=1.6]
(0.5,0);
\draw[line width=1pt, black, fill = black!15] 
(-0.2, 1.545) to[out=180,in = 100] 
(-0.37,0.8) to[out = {100+180}, in = 90]
(-0.27,0.1) to[out = 270, in = 80]
(-0.37,-0.8)
to[out = 260, in = 180]
(-0.2, -1.345) --
(-0.2, -1.555) to[out=180,in=0]
(-1.2,-1.555) to[out = 180, in = 270]
(-2.2, 0.1) to[out = 90, in = 180]
(-1.2,1.755) to[out = 0, in = 180]
(-0.2,1.755) -- 
(-0.2, 1.545);
\draw[line width=5pt,black!15]
(0.28, 0.22) to[out = 135, in =180]
(0.95,1.65) to[out =0, in = 90]
(1.9,0.1) to[out=270, in=-35](0.53,-1.46);
\draw[line width=5pt, black!15] 
(0.22,-1.14) to[out=135, in=225]
(0.38, 0.1) to[out =  45, in =-45]
(0.56,1.32);
\draw[line width=5pt, black!15]
(0.3, 1.5) to[out=145, in = 0]
(-0.25, 1.65);
\draw[line width=5pt, black!15]
(-0.25,-1.45) to[out = 0, in =-50, looseness=1.6]
(0.5,0);
\draw[dashed] (-0.27,0.1) arc (0:180:0.965 and 0.5);
\draw[very thick,wilsonred]
(0.28, 0.22) to[out = 135, in =180]
(0.95,1.65) to[out =0, in = 90]
(1.9,0.1) to[out=270, in=-35]
(0.53,-1.46);
\draw[very thick, wilsonred] 
(0.22,-1.14) to[out=135, in=225]
(0.38, 0.1) to[out =  45, in =-45]
(0.56,1.32);
\draw[very thick, wilsonred]
(0.3, 1.5) to[out=145, in = 0]
(-0.53, 1.65) to[out = 180, in =90]
(-1.9, 0.74) to[out=270, in =225]
(-0.83, 0.05);
\draw[very thick, wilsonred]
(-0.68, 0.25) to[out = 55, in = -90]
(-0.53, 1.65);
\draw[very thick, wilsonred]
(-0.53,-1.45) to[out = 90, in =35, looseness=1.5] 
(-1.55,0.2);
\draw[very thick, wilsonred]
(-1.72,0.05) to[out=235, in = 90]
(-1.9, -0. 57) to[out=270, in =180]
(-0.25,-1.45) to[out = 0, in =-50, looseness=1.6]
(0.5,0);
\draw (-0.27,0.1) arc (0:-180:0.965 and 0.5);
\end{tikzpicture}
}}.
\end{equation}
The handlebody-knot (in red) has a complement in $\mathrm{S}^3$ with a genus-2 boundary, but it is not atoroidal. In the figure above, the essential torus is highlighted in gray. Thus, by Thurston's theorem the $\mathbf{5}_4$-complement does not carry a hyperbolic metric. 

\paragraph{Proving hyperbolicity.} We now come back to the proof that the gravitational machine does not map out of the space of hyperbolic 3-manifolds. Since we only cut and paste manifolds one-by-one, the procedure does not change the compactness properties of $M$. Taking the disconnected union of manifolds (move \ref{move:disconnected sum}) as well as performing crossing transformations (move \ref{move:crossing}) do not map us out of hyperbolicity. For the latter statement, we use Mostow rigidity \cite{Sullivan} which ensures that a hyperbolic structure in the bulk either exists for \emph{all} boundary moduli or for none of them. In particular, in the canonical picture crossing transformations act on the boundary moduli, which do not affect hyperbolicity of the bulk manifold.

Moreover, the non-hyperbolic exceptional manifold $(T^2 \times [0,1])/\ZZ_2$ is not generated by the machine. The $\ZZ_2$ quotient flips the interval and corresponds to the covering transformation of $T^2$ such that $T^2/\ZZ_2$ is a Klein bottle. This exceptional manifold does have a genus-1 boundary, but it is not one of the $\mathrm{PSL}(2,\ZZ)$ family of Euclidean black holes, and these are the only manifolds the machine generates at genus 1. This follows directly from conditions \ref{cond:no parallel rings 2} and \ref{cond:no Wilson line self gluing}. Namely, at genus 1, there is a single Wilson line, so self-gluing is not permitted. The only available operation is the cylinder surgery of two BTZ black holes, $M_1$ and $M_2$. This either produces again a single BTZ black hole (for the trivial Dehn filling) or it introduces parallel rings, which are not allowed by condition \ref{cond:no parallel rings 2}.

Thus, it only remains to prove that the cylinder surgery operation, i.e.~move \ref{move:gluing}, keeps $M$ irreducible and atoroidal. For irreducibility, we will use a simple geometric argument known as the innermost/outermost curve argument. Our proof that the manifold stays atoroidal is entirely group-theoretic and requires some input from geometric group theory that we review in appendix~\ref{app:Bass-Serre theory}. By induction, it will follow that any manifold produced by the gravitational machine is hyperbolic.

\paragraph{Irreducible.} Let $M$ be the manifold before gluing and $\widetilde{M}=M \#_{P_1 \sim P_2}$ the manifold after gluing. For the irreducibility part of the proof, it doesn't matter whether we are gluing two disconnected components of $M$ or the same component to itself. As the induction hypothesis, we assume that $M$ is hyperbolic.

Recall that to define cylinder surgery, we had to excise the interiors of a pair of 2-punctured spheres in $M$. This does not change the homotopy groups of $M$. Thus, we will not distinguish between $M$ and $M$ with the balls removed. In particular, we will write $\partial M= \Sigma \cup \Sigma_{0,2} \sqcup \Sigma_{0,2}$, where $\Sigma$ is the original boundary of $M$ and $\Sigma_{0,2} \sqcup \Sigma_{0,2}$ is the disjoint union of two 2-punctured spheres. In $\widetilde{M}$, these 2-punctured spheres get identified.
We will only use the $\Omega$-loop condition \ref{cond:no Omega loops 2}, which says that neither $m_1$ nor $m_2$ is contractible in $M$. It also implies that a power $m_i^n$ for $n \in \ZZ \setminus \{0\}$ is not contractible. Otherwise, $\pi_1(M)$ would have torsion, which is impossible for hyperbolic manifolds. In other words, the inclusion $\pi_1(\Sigma_{0,2}) \hookrightarrow \pi_1(M)$ is an injection, for both of the boundary components $\Sigma_{0,2}$.

As a proof by contradiction, suppose that $\pi_2(\widetilde{M})\ne 0$. Choose a non-trivial element in $\pi_2(\widetilde{M})$, which can be represented by an embedded 2-sphere $S$.\footnote{For this one formally uses the sphere theorem of 3-manifolds, saying that any element of $\pi_2(M)$ may always be represented as a properly embedded sphere.} 
W.l.o.g., assume that $S$ intersects the 2-punctured sphere $\Sigma_{0,2}$ transversely in a number of curves $C_i$, with $i=1,\dots,n$. We choose the representative and the non-trivial element in $\pi_2(\widetilde{M})$ such that the number of connected components $n$ of the intersection is minimal. This $n$ cannot be zero since then $S$ would lie entirely in $M$. But since $\pi_2(M)=0$ by hypothesis (for any connected component of $M$), this implies that $S$ is null-homotopic in $M$ and thus  in $\widetilde{M}$, contradicting non-triviality of $S$ in $\pi_2(\widetilde{M})$.

Now choose an innermost curve of the intersection, i.e.~a $C_i$ that bounds a disk on $S$. Then $[C_i]$ cannot be a non-trivial element of $\pi_1(\Sigma_{0,2})$. For if it were, the disk would define a null-homotopy of $[C_i]$ in one of the connected components of $M$, thus contradicting the injectivity assumption of the maps $\pi_1(\Sigma_{0,2}) \xhookrightarrow{\quad} \pi_1(M)$. Thus $C_i$ has to be a contractible curve on $\Sigma_{0,2}$. 
\begin{figure}
\begin{center}
\begin{tikzpicture}[scale=.7]
  \path[draw=wilsonred,very thick,cm={ 0.5,-0.0,-0.0,0.6,(-1.6, 4.0)}] (4.0, 
  21.2).. controls (7.0, 21.3) and (9.9, 21.3) .. (11.8, 20.9).. controls (13.6,
   20.5) and (14.3, 19.6) .. (14.4, 18.9).. controls (14.4, 18.2) and (13.8, 
  17.6) .. (12.8, 17.3).. controls (11.9, 17.0) and (10.7, 17.0) .. (9.9, 
  16.6).. controls (9.0, 16.3) and (8.4, 15.5) .. (8.6, 14.9).. controls (8.9, 
  14.3) and (10.1, 13.7) .. (11.1, 13.4).. controls (12.2, 13.1) and (13.2, 
  13.1) .. (13.8, 12.7).. controls (14.5, 12.3) and (14.8, 11.5) .. (14.5, 
  10.8).. controls (14.1, 10.2) and (13.1, 9.6) .. (11.3, 9.4).. controls (9.4, 
  9.2) and (6.7, 9.3) .. (4.0, 9.4);
  \path[draw=black, very thick, cm={ 0.5,-0.0,-0.0,0.6,(-1.6, 4.0)}] 
  (11.3, 23.1).. controls (10.8, 21.7) and (10.3, 20.4) .. (10.3, 19.1).. 
  controls (10.3, 17.8) and (10.8, 16.6) .. (10.9, 15.3).. controls (11.1, 14.0)
   and (11.0, 12.6) .. (11.0, 11.2).. controls (11.0, 9.9) and (11.1, 8.5) .. 
  (11.2, 7.2);
  \path[draw=wilsonred,very thick,cm={ 0.6,-0.0,-0.0,0.6,(5.1, 3.9)}] (4.0, 
  21.2).. controls (7.0, 21.3) and (9.9, 21.3) .. (11.8, 20.9).. controls (13.6,
   20.5) and (14.3, 19.6) .. (14.4, 18.5).. controls (14.4, 17.3) and (13.8, 
  15.9) .. (12.3, 15.7).. controls (10.8, 15.6) and (8.5, 16.8) .. (7.5, 16.6)..
   controls (6.5, 16.4) and (6.9, 14.8) .. (7.6, 14.6).. controls (8.3, 14.4) 
  and (9.5, 15.5) .. (10.6, 15.4).. controls (11.8, 15.4) and (13.0, 14.2) .. 
  (13.7, 13.3).. controls (14.5, 12.3) and (14.8, 11.5) .. (14.5, 10.8).. 
  controls (14.1, 10.2) and (13.1, 9.6) .. (11.3, 9.4).. controls (9.4, 9.2) and
   (6.7, 9.3) .. (4.0, 9.4);
  \path[draw=black,very thick,cm={ 0.6,-0.0,-0.0,0.6,(5.1, 3.9)}] (11.3,
   23.1).. controls (10.8, 21.7) and (10.3, 20.4) .. (10.3, 19.1).. controls 
  (10.3, 17.8) and (10.8, 16.6) .. (10.9, 15.3).. controls (11.1, 14.0) and 
  (11.0, 12.6) .. (11.0, 11.2).. controls (11.0, 9.9) and (11.1, 8.5) .. (11.2, 
  7.2);
  \path[draw=black,very thick,dashed] (11.2, 13) ellipse (2.3 and 3.5);
  \path[draw=black,very thick, dashed] (11.6, 13.25) ellipse (0.1 and 0.15);
  \path[draw=black, very thick, dashed] (3.8, 13.1) ellipse (0.6 and 1.0);
  \path[draw=black, very thick ,dashed] (3.6, 13.1) ellipse (2.1 and 3.5);
  \path[draw=wilsonred,very thick,cm={ 0.5,-0.0,-0.0,0.6,(13.1, 3.8)}] (4.0, 
  21.2).. controls (7.0, 21.3) and (9.9, 21.3) .. (11.8, 20.9).. controls (13.6,
   20.5) and (14.3, 19.6) .. (14.4, 18.9).. controls (14.4, 18.2) and (13.8, 
  17.6) .. (13.2, 17.2).. controls (12.7, 16.9) and (12.3, 16.8) .. (12.1, 
  16.4).. controls (11.8, 16.0) and (11.6, 15.3) .. (11.7, 14.7).. controls 
  (11.8, 14.2) and (12.2, 13.9) .. (12.6, 13.6).. controls (13.1, 13.4) and 
  (13.6, 13.2) .. (14.1, 12.8).. controls (14.5, 12.3) and (14.8, 11.5) .. 
  (14.5, 10.8).. controls (14.1, 10.2) and (13.1, 9.6) .. (11.3, 9.4).. controls
   (9.4, 9.2) and (6.7, 9.3) .. (4.0, 9.4);
  \path[draw=black,very thick,cm={ 0.5,-0.0,-0.0,0.6,(13.1, 3.8)}] 
  (11.3, 23.1).. controls (10.8, 21.7) and (10.3, 20.4) .. (10.3, 19.1).. 
  controls (10.3, 17.8) and (10.8, 16.6) .. (10.9, 15.3).. controls (11.1, 14.0)
   and (11.0, 12.6) .. (11.0, 11.2).. controls (11.0, 9.9) and (11.1, 8.5) .. 
  (11.2, 7.2);
  \path[draw=black,very thick, dashed] (18.3, 12.9) ellipse (2.1 and 3.5);
  \path[draw=wilsonred,very thick,shift={(0.4, -0.1)}] (17.6, 
  13.3).. controls (17.8, 13.2) and (18.0, 12.9) .. (18.0, 12.6).. controls 
  (18.0, 12.3) and (17.9, 12.0) .. (17.7, 12.0).. controls (17.5, 11.9) and 
  (17.3, 12.0) .. (17.1, 12.3).. controls (17.0, 12.5) and (16.9, 12.8) .. 
  (17.0, 13.0).. controls (17.1, 13.2) and (17.4, 13.4) .. (17.6, 13.3) -- cycle;
  \draw[->, very thick] (6.9, 12.7) to 
  (7.9, 12.7);
  \draw[->, very thick] (14.6, 12.7) to
   (15.6, 12.7);
  \node at (2.4, 17.4){$M_1$};
  \node at (5.4, 17.4){$M_2$};
  \node at (10.4, 17.4){$M_1$};
  \node at (12.9, 17.4){$M_2$};
  \node at (19.9, 17.4){$M_2$};
  \node at (17.1, 17.4){$M_1$};
  \node at (5.3, 9.5){$S$};
  \node at (13.2, 9.5){$S$};
  \node at (17.5, 11.5){$S_1$};
  \node at (20.3, 9.5){$S_2$};
  \node at (4.8, 12.8){$C_i$};
  \node at (11.9, 13.8){$C_i$};
\end{tikzpicture}
\end{center}
\caption{Pinching the innermost curve leads to two surfaces with fewer intersections with the boundary $\partial M_1=\partial M_2$.} \label{fig:pinching curve}
\end{figure}
Since $C_i$ is contractible on $\Sigma_{0,2}$ and doesn't contain any other intersection curves in its interior, we can isotope it to a point. This pinches the 2-sphere $S$ along the curve $C_i$ and we obtain two 2-spheres $S_1$ and $S_2$ connected at a single point. If we separate them, at least one of the 2-spheres still defines a non-trivial element of $\pi_2(\widetilde{M})$ by the definition of $\pi_2$. See figure~\ref{fig:pinching curve} for an illustration of this procedure. Say $[S_1]$ is non-trivial. However, the number of intersections with $\Sigma_{0,2}$ of $S_1$ is at most $n-1$ since we removed the curve $C_i$. This contradicts the assumption that we chose $n$ minimal. Thus we have arrived at a contradiction and conclude that $\pi_2(\widetilde{M})=0$.

\paragraph{Computing $\pi_1$.} Next, we want to show that the gluing move \ref{move:gluing} also preserves the fact that the manifold $M$ is atoroidal. This can be checked by computing $\pi_1(\widetilde{M})$. The computation differs depending on whether we glue disconnected components or the same connected component to itself.

For gluing two disconnected components $M_1 \#_{P_1\sim P_2} M_2$, this is a standard application of the Seifert-Van-Kampen theorem. Before gluing, we have $M = M_1\sqcup M_2$, with $M_1 \cap M_2 \cong \Sigma_{0,2}$ with fundamental group $\pi_1(\Sigma_{0,2}) \cong \ZZ$. The theorem tells us that after gluing, the fundamental group has the form of an amalgamated product,
\be 
\pi_1(\widetilde{M})=\pi_1(M_1) *_\ZZ \pi_1(M_2)\,. \label{eq:amalgamated product}
\ee
Let us recall what amalgamation means. Suppose, for $i=1,2$, that $\pi_1(M_i)$ is generated by a set $S_i$ with some relations $R_i$, i.e.~has the presentation $\pi_1(M_i)=\langle S_i \, | \, R_i \rangle$. Then the free product $\pi_1(M_1)*\pi_1(M_2)$ has the presentation $\langle S_1,\, S_2 \, | \, R_1,\, R_2 \rangle$, so we are not imposing any further relations than the ones already present in the two factors. In particular, we are not imposing that generators in $S_1$ and $S_2$ commute (which would be the case in the direct product). With amalgamation, denoted by the subscript $*_H$, we are additionally identifying a joint subgroup $H$ in $\pi_1(M_i)$, in this case $\pi_1(\Sigma_{0,2})$, i.e.~we are adding the additional relations $\iota_1(g)=\iota_2(g)$ for all $g$ in the subgroup, where $\iota_i: H \hookrightarrow \pi_1(M_i)$ are the inclusions. In our case, we hence add the additional relation $m_1=m_2$.\footnote{In the above constructions, we have to choose a basepoint. We choose a basepoint for $\pi_1(M_i,x_i)$ in the respective boundary $ x_i\in \Sigma_{0,2} \subset M_i$, so that $x_1$ and $x_2$ get identified after identifying the two boundaries.} 

When writing the amalgamated product \eqref{eq:amalgamated product}, we used the fact that $\ZZ$ is naturally a subgroup of $\pi_1(M_1)$ and $\pi_1(M_2)$, i.e.~that the inclusion is injective according to \ref{cond:no Omega loops 2}. The amalgamated product can be viewed as a group-theoretic analogue of the cylinder surgery, where we `glue' two groups along a common subgroup.

In case that we are performing a self-gluing $\widetilde{M} = M\#_{ P_1\sim P_2}$, a similar presentation of the fundamental group exists. Let $M$ be the original manifold before gluing. Let $m_1$ and $m_2$ be (based) loops around the two Wilson lines that are to be identified, so that the fundamental group of $M$ has the presentation:
\be 
\pi_1(M)=\big \langle S,m_1,m_2 \, | \, R \big \rangle
\ee
for some relations $R$. Then $\pi_1(\widetilde{M})$ takes the form of a so-called HNN extension \cite{HNN_extension}. This means that $\pi_1(\widetilde{M})$ is obtained by adding a new generator $t$ together with the relation $m_2=t m_1 t^{-1}$, i.e.
\be 
\pi_1(\widetilde{M})=\big \langle S,m_1,m_2,t \, | \, R,\, m_2=t m_1 t^{-1} \big \rangle\,. \label{eq:fundamental group self-gluing}
\ee
The generator $t$ is usually called the stable letter. 
Geometrically, it corresponds to the loop through the `wormhole' $\Sigma_{0,2}\times I$, while the self-gluing identifies $m_1$ with the conjugated loop $t m_2 t^{-1}$ that also runs through the wormhole. Notice that the choice of $m_1$ and $m_2$ is only well-defined up to conjugation, but the resulting groups are isomorphic.\footnote{This can be derived using the groupoid version of the Seifert-van-Kampen theorem. For a more down-to-earth explanation, see \cite[chapter 5]{Wall1979}.} 

In writing down the HNN extension \eqref{eq:fundamental group self-gluing}, we again made use of the injectivity of the inclusions of $\pi_1(\Sigma_{0,2})$ in $\pi_1(\widetilde{M})$. More generally, the HNN extension identifies two isomorphic subgroups $H$ and $H'$ of $\pi_1(M)$, usually denoted by $\pi_1(M)*_{H\sim H'}$. Thus it provides the group-theoretic analogue of the self-gluing $M\#_{ P_1\sim P_2}$. More details on the underlying geometric group theory can be found in appendix~\ref{app:Bass-Serre theory}.

\paragraph{Malnormality.} We now establish two further properties of the amalgamated product and the HNN extension in our case, which will let us conclude that they do not have $\ZZ \times \ZZ$ subgroups. Let us write $G_i=\pi_1(M_i)$ in the disconnected case and $G_1=\pi_1(M)$ in the connected case, and let $H_i =\langle m_i \rangle  \cong \ZZ$, $i=1,\, 2$ for the joint isomorphic subgroups that we are identifying. W.l.o.g., we can assume that $m_1$ is primitive by condition \ref{cond:no parallel rings 2}.
For the case of a connected gluing, the condition \ref{cond:no Wilson line self gluing} that a Wilson line cannot be glued to itself states that
\be 
H_1 \cap g H_2 g^{-1}=\{1\}, \quad \text{for all } g \in G_1\,. \label{eq:H1 H2 intersection condition}
\ee
We next claim that $H_1 \subset G_1$ is a \emph{malnormal} subgroup in both the disconnected and the connected case. This means that 
\be 
 H_1 \cap g H_1 g^{-1}  =\{1\}, \quad \text{for all } g \in G_1 \setminus H_1 \,.\label{eq:malnormality}
\ee
To show this, assume that $g m_1^k g^{-1}=m_1^\ell$ for $k,\, \ell \in \ZZ \setminus \{0\}$. Since $m_1$ is primitive, the left-hand side is a $k$-th power of a primitive element and the right-hand side is an $\ell$-th power of a primitive element. Thus, they can only be equal if $|k|=|\ell|$. Furthermore, since $m_1$ is primitive, we only have to analyze $g m_1 g^{-1}=m_1$ and $g m_1 g^{-1}=m_1^{-1}$. In either case, $[m_1,g^2]=1$. Since $G_1$ does not have $\ZZ \times \ZZ$ subgroups by the induction hypothesis, $m_1$ and $g^2$ have to lie in the same infinite cyclic subgroup, which is necessarily generated by $m_1$, since it is primitive. Thus $g^2=m_1^n$ for some $n$. Since $m_1$ is again primitive, it follows that $n$ has to be even and since the group is torsion-free we can take the square root of the relation to conclude that $g \in H_1 =\langle m_1 \rangle$. This establishes \eqref{eq:malnormality}.

\paragraph{Atoroidal.} We can now finish the argument quickly by using geometric group theory \cite{SerreTrees}. We give some more mathematical  background on this theory in appendix~\ref{app:Bass-Serre theory}. Let us first treat the amalgamated product case, where we have the following theorem \cite{Karrass:1971}.\footnote{We will actually need a small generalization that is for example explained in \cite{mathoverflow_amalgamatedproduct}. In \cite{Karrass:1971}, it is assumed that $H$ is malnormal in $G_1$ \emph{and} $G_2$. We explain the derivation of this more general version in appendix~\ref{app:Bass-Serre theory}.} Consider an amalgamated product $G=G_1*_H G_2$. Assume that $H$ is malnormal in $G_1$. Let $g \in G$. Then the centralizer $\mathcal{C}(g)$ in $G$ is either infinite cyclic or $\mathcal{C}(g)$ is conjugate to $G_1$ or $G_2$.

We set everything up such that we can apply the theorem. Centralizers in $G_1$ and $G_2$ are all infinite cyclic groups (since $G_i$ does not have torsion or $\ZZ \times \ZZ$ subgroups). Thus, in both possibilities in the above theorem, the centralizer is an infinite cyclic group. Thus $G$ does not have $\ZZ \times \ZZ$ subgroups.

We have a similar theorem for the HNN extension. Consider an HNN extension $G=G_1 *_{H_1 \sim H_2}$. It states: if $H_1$ does not intersect any of the conjugates of $H_2$ and is malnormal in $G_1$, then the centralizer $\mathcal{C}(g)$ of $g \in G$ is either infinite cyclic or $\mathcal{C}(g)$ is conjugate to $G_1$. The assumptions of this theorem are guaranteed by \eqref{eq:H1 H2 intersection condition} and \eqref{eq:malnormality}. Since $G_1$ does not have $\ZZ \times \ZZ$ subgroups by the induction hypothesis, it follows that also $G$ does not have $\ZZ \times \ZZ$ subgroups.

Thus in both gluing types, we do not get $\ZZ \times \ZZ$ subgroups of $\pi_1(\widetilde{M})$, and hence $\widetilde{M}$ is homotopically atoroidal. Using Thurston's theorem, this concludes our proof that the operations of the machine preserve hyperbolicity.

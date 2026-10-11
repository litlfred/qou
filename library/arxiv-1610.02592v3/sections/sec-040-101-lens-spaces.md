---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-040-101-lens-spaces
section_title: "Lens spaces"
section_number: 10.1
pages: 311-318
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.836
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
We introduce some of the simplest 3-manifolds, the lens spaces. These manifolds (and many more) are easily described using an important three-dimensional construction, called \emph{Dehn filling}.\index{Dehn filling}

\subsection{Dehn filling} \label{Dehn:filling:subsection}
If a 3-manifold $M$ has a spherical boundary component, we can cap it off with a ball. If $M$ has a toric boundary component, there is no canonical way to cap it off: the simplest object that we can attach to it is a solid torus $D\times S^1$, but the resulting manifold depends on the gluing map. This operation is called a \emph{Dehn filling} and we now study it in detail.

Let $M$ be a 3-manifold and $T\subset \partial M$ be a boundary torus component. 
\begin{defn}
A \emph{Dehn filling} of $M$ along $T$ is the operation of gluing a solid torus $D\times S^1$ to $M$ via a diffeomorphism $\varphi\colon \partial D\times S^1 \to T$. 
\end{defn}

The closed curve $\partial D \times \{x\}$ is glued to some simple closed curve $\gamma\subset T$, see Figure \ref{DF:fig}. The result of this operation is a new manifold $M^{\rm fill}$, which has one boundary component less than $M$.

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{DF-BW}{DF}}
\nota{The Dehn filling $M^{\rm fill}$ of a 3-manifold $M$ is determined by the unoriented simple closed curve $\gamma \subset T$ to which a meridian $\partial D$ of the solid torus is attached.}
\label{DF:fig}
\end{center}
\end{figure}

\begin{lemma} \label{pq:lemma}
The manifold $M^{\rm fill}$ depends only on the isotopy class of the unoriented curve $\gamma$.
\end{lemma}
\begin{proof}
Decompose $S^1$ into two closed segments $S^1 = I\cup J$ with coinciding endpoints. The attaching of $D\times S^1$ may be seen as the attaching of a 2-handle $D\times I$ along $\partial D \times I$, followed by the attaching of a 3-handle $D\times J$ along its full boundary. 

If we change $\gamma$ by an isotopy, the attaching map of the 2-handle changes by an isotopy and hence gives the same manifold. The attaching map of the 3-handle is irrelevant by Proposition \ref{cap:prop}.
\end{proof}

We say that the Dehn filling \emph{kills} the curve $\gamma$, since this is what really happens on fundamental groups, as we now see. 

The \emph{normaliser} of an element $g\in G$ in a group $G$ is the smallest normal subgroup $N(g) \triangleleft G$ containing $g$. The normaliser depends only on the conjugacy class of $g^{\pm 1}$, hence  the subgroup $N(\gamma)\triangleleft \pi_1(M)$ makes sense without fixing a basepoint or an orientation for $\gamma$.\index{normaliser}

\begin{prop} 
We have
$$\pi_1(M^{\rm fill}) = \pi_1(M) /_{N(\gamma)}.$$
\end{prop}
\begin{proof}
The Dehn filling decomposes into the attachment of a 2-handle over $\gamma$ and of a 3-handle. By Van Kampen, the first operation kills $N(\gamma)$,
and the second leaves the fundamental group unaffected.
\end{proof}

Let a \emph{slope} on a torus $T$ be the isotopy class $\gamma$ of an unoriented homotopically non-trivial simple closed curve.\index{slope} The set of slopes on $T$ was indicated by $\calS$ in Chapter \ref{Teichmuller:chapter}. If we fix a basis $(m, l)$ for $H_1(T,\matZ)=\pi_1(T)$, every slope may be written as $\gamma = \pm (pm + ql)$ for some coprime pair $(p,q)$. Therefore we get a 1-1 correspondence
$$\calS \longleftrightarrow \matQ\cup \{\infty\}$$
by sending $\gamma$ to $\frac pq$. If $T$ is a boundary component of $M$, every number $\frac pq$ determines a Dehn filling of $M$ that kills the corresponding slope $\gamma$. 

Different values of $\frac pq$ typically produce non-diffeomorphic manifolds $M^{\rm fill}$: this is not always true - a notable exception is described in the next section - but it holds in ``generic'' cases.

\subsection{Lens spaces}
The simplest manifold that can be Dehn-filled is the solid torus $M=D\times S^1$ itself. The oriented \emph{meridian} $m=S^1 \times \{y\}$ and \emph{longitude} $l=\{x\}\times S^1$ form a basis for $H_1(\partial M,\matZ)$.\index{meridian and longitude}

\begin{defn} The \emph{lens space} $L(p,q)$ is the result of a Dehn filling of $M=D\times S^1$ that kills the slope $qm+pl$.\index{lens space}
\end{defn}

A lens space is a three-manifold that decomposes into two solid tori. We have already encountered lens spaces in the more geometric setting of Section \ref{lens:subsection}, and we will soon prove that the two definitions are coherent. Since $L(p,q)=L(-p,-q)$ we usually suppose $p\geqslant 0$.

\begin{ex}
We have $\pi_1\big(L(p,q)\big) = \matZ/_{p\matZ}$. 
\end{ex}

\begin{prop}
We have $L(0,1) = S^2\times S^1$ and $L(1,0) = S^3$.
\end{prop}
\begin{proof}
The lens space $L(0,1)$ is obtained by killing $m$, that is by mirroring $D\times S^1$ along its boundary. The lens space $L(1,0)$ is $S^3$ because the complement of a standard solid torus in $S^3$ is another solid torus, with the roles of $m$ and $l$ exchanged (exercise).
\end{proof}

\begin{ex} \label{fill:T:ex}
Every Dehn filling of one component of the product $T\times [0,1]$ is diffeomorphic to $D\times S^1$. Therefore by Dehn-filling both components of $T\times [0,1]$ we get a lens space.
\end{ex}

The solid torus $D\times S^1$ has a non-trivial self-diffeomorphism 
$$(x, e^{i\theta}) \longmapsto (xe^{i\theta}, e^{i\theta})$$
called a \emph{twist} along the disc $D\times \{y\}$. The solid torus can also be \emph{mirrored} via the map
$$(x,e^{i\theta}) \longmapsto (x,e^{-i\theta}).$$

\begin{ex} \label{pqpq:ex}
We have $L(p,q)\isom L(p,q')$ if $q' \equiv \pm q^{\pm 1}$ (mod $p$).
\end{ex}
\begin{proof}[Hint]
Twist, mirror, and exchange the two solid tori giving $L(p,q)$.
\end{proof}

\begin{rem}
The meridian $m$ of the solid torus $M=D\times S^1$ may be defined intrinsically as the unique slope in $\partial M$ that is homotopically trivial in $M$. The longitude $l$ is \emph{not} intrinsically determined: a twist sends $l$ to $m+l$. The solid torus contains infinitely many non-isotopic longitudes, and there is no intrinsic way to choose one of them.
\end{rem}

\subsection{Equivalence of the two definitions}
When $p>0$, we have defined the lens space $L(p,q)$ in two different ways: as the $(q,p)$-Dehn filling of the solid torus, and as an elliptic manifold in Section \ref{lens:subsection}. In the latter description we set
$$\omega = e^{\frac{2\pi i}p}, \qquad f(z,w) = (\omega z, \omega^qw)$$ 
and define $L(p,q)$ as $S^3/_\Gamma$ where $\Gamma = \langle f \rangle$ is generated by $f$. We now show that the two definitions produce the same manifolds.

\begin{prop}
The manifold $S^3/_{\langle f \rangle}$ is the $(q,p)$-Dehn filling of the solid torus.
\end{prop}
\begin{proof}
The isometry $f$ preserves the central torus 
$$T = \big\{(z,w)\ \big|\ |z|=|w| = \tfrac {\sqrt 2}2 \big\}$$
that divides $S^3$ into two solid tori
\begin{align*}
N^1 & = \big\{(z,w)\ \big|\ |z| \leqslant \tfrac {\sqrt 2}2,\ |w| = \sqrt{1-|z|^2}\big\}, \\
N^2 & = \big\{(z,w)\ \big|\ |w| \leqslant \tfrac {\sqrt 2}2,\ |z| = \sqrt{1-|w|^2}\big\}.
\end{align*}
Identify $T$ with $S^1\times S^1 = \matR^2/_{\matZ^2}$ in the obvious way, so that  $H_1(T) = \matZ \times \matZ$. The meridians of $N^1$ and $N^2$ are $(1,0)$ and $(0,1)$. The isometry $f$ act on $T$ as a translation of vector $v=\big(\frac 1p, \frac qp\big)$. The quotient $T/_{\langle f\rangle}$ is again a torus, with fundamental domain the parallelogram generated by $v$ and $w=(0,1)$.

The quotients $N^1/_{\langle f \rangle}$, and $N^2/_{\langle f \rangle}$ are again solid tori. Therefore $S^3/_{\langle f \rangle}$ is also a union of two solid tori. Their meridians are the projections of the horizontal and vertical lines in $\matR^2$ to $T/_{\langle f \rangle} = \matR^2/_{\langle v,w \rangle}$. In the basis $(v,w)$ these meridians are $pv -qw$ and $w$ respectively. Therefore $S^3/_{\langle f\rangle}$ is a $(-q,p)$-Dehn filling on the solid torus, which is diffeomorphic to the $(q,p)$-Dehn filling by mirroring the solid torus.
\end{proof}

\begin{cor}
We have $L(1,0) = S^3$ and $L(2,1) = \matRP^3$.
\end{cor}
\begin{proof}
We have $f = \id$ and $f=-\id$, correspondingly.
\end{proof}

\subsection{Classification of lens spaces}
Which lens spaces are diffeomorphic? It is not so easy to answer this question, because many lens spaces like $L(5,1)$ and $L(5,2)$ have the same homotopy and homology groups, while there is no evident diffeomorphism between them. 
A complete answer was given by Reidemeister in 1935, who could distinguish lens spaces using a new invariant, now known as the \emph{Reidemeister torsion}.\index{Reidemeister torsion} More topological proofs were discovered in th 1980s by Bonahon and Hodgson. We follow here Hatcher \cite{H}.

\begin{teo} \label{Lpq:teo}
The lens spaces $L(p,q)$ and $L(p',q')$ are diffeomorphic $\Longleftrightarrow$ $p=p'$ and $q' \equiv \pm q^{\pm 1}$ (mod $p$).
\end{teo}
\begin{proof}
We may suppose $p>1$.
Exercise \ref{pqpq:ex} furnishes one implication, so we start with a lens space $L(p,q)$ and we prove that there is (up to isotopy) only one torus $T$ dividing $L(p,q)$ into two solid tori: this fact then implies that one can recover $p$ and $q$ intrinsically from $L(p,q)$, up to the stated ambiguity for $q$ (which depends on the chosen longitudes and orientations, and changes by switching the solid tori). So we suppose that there is another torus $T'$.

Let $\Sigma$ be the core circle of one solid torus adjacent to $T'$. If we can isotope $\Sigma$ inside the torus $T$, we are done: in that case $T'$ is isotopic to the boundary of a small tubular neighbourhood of $\Sigma$, hence both $T$ and $T'$ are cut into two annuli $T = A_1 \cup A_2$ and $T' = A_1' \cup A_2'$ such that $\Sigma \subset A_1$, all four annuli share the same boundaries, and $A_2$ is contained in the large outside solid torus bounded by $T'$; the annulus $A_2$ is incompressible in this solid torus by Proposition \ref{pi1:prop} (otherwise $\Sigma$ would be homotopically trivial, contradicting $p>1$) and hence $\partial$-parallel by Proposition \ref{incompressible:solid:torus:prop}, so it is isotopic to either $A_1'$ or $A_2'$, suppose to $A_2'$; since $A_1$ is clearly isotopic to $A_1'$ we conclude that $T$ and $T'$ are isotopic.

Our aim is now to prove that $\Sigma$ can be isotoped inside $T$. To this purpose we construct two different objects from $T'$ and $T$, a \emph{spine} $\Delta$ and a \emph{foliation} $\calF$. The spine $\Delta\subset M$ is built by adding to $\Sigma$ the meridian $D$ of the other solid torus incident to $T'$, enlarged so that $\partial D$ is glued along $\Sigma$ like a degree-$p$ covering. Note that $M\setminus \Delta$ is an open ball.

We construct the foliation $\calF$ of $M$ by subdividing each solid torus bounded by $T$ into concentric tori, with a central singular circle in each. We represent $\calF$ as the level sets of a map $f\colon L(p,q) \to [0,1]$ where the singular circles are the extreme levels $f^{-1}(0)$ and $f^{-1}(1)$.

We now put $\Delta$ in some good position with respect to $\calF$. We first perturb $\Sigma$ so that it is disjoint from the singular circles of $\calF$ and $f|_\Sigma$ is a Morse function with singular points in distinct levels. At every local maximum (minimum) of $f|_\Sigma$ we isotope $\Delta$ so that the $p$ sheets of $\Delta$ lie above (below) $\Sigma$ as in Figure \ref{sheets_above:fig}. Finally, we require $\Delta$ to be transverse to the two singular circles of $\calF$ and $f|_{\Delta \setminus \Sigma}$ to be a Morse function, with critical points at distinct levels (also distinct from those of the critical points of $f|_\Sigma$).

\begin{figure}
\begin{center}
\includegraphics[width = 3 cm] {sheets_above}
\nota{We require the $p$ sheets of the spine $\Delta$ to lie above every local maximum for $f|_\Sigma$.}
\label{sheets_above:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{lens_singular-BW}{lens_singular}}
\nota{The singular points in $D$ can be centres (top left), saddles (top right) and half-saddles (bottom).}
\label{lens_singular:fig}
\end{center}
\end{figure}

The foliation $\calF$ induces a singular foliation on $\Delta$ that pulls back to $D$ via the map $D\to \Delta$. There are three types of singular points in the foliation, shown in Figure \ref{lens_singular:fig}: centres, saddles, and half-saddles.

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{lens_leaves-BW}{lens_leaves}}
\nota{A singular leaf exiting from a singular point may be of one of these kinds. The dots in (e) indicate that there might be another half-saddle at the other endpoint: this is because there are half-saddles at the same level (precisely $p$ for every local maximum or minimum for $f|_\Sigma$).}
\label{lens_leaves:fig}
\end{center}
\end{figure}

A leaf in $D$ incident to a singular point is \emph{singular}. Since we minimised the critical points that may stay at the same level, the singular leaves exiting from a singular point may be only of the six possible kinds shown in Figure \ref{lens_leaves:fig}.  
The saddles and half-saddles of type (a) and (e) are called \emph{essential}, and the others \emph{inessential}.
In (a) the singular leaves divide $D$ into four \emph{quarter discs}, and in (e) they cut off two or more \emph{half discs}.

Among all possible good configurations of $\Delta$, we pick one that minimises first the number of critical points in $f|_\Sigma$, and second the number of essential saddles.

Let $D' \subset D$ be a quarter or half-disc not containing any smaller quarter or half-disc. Define $\alpha = D' \cap \partial D$. Suppose first that $D'$ is a half-disc and both endpoints of $\alpha$ are singular. The singular disc $D'$ can contain some singular point of type (b), and it certainly contains one singular point of type (f), see Figure \ref{lens_leaves1:fig}-(left). (It contains no other singular point except these.) The image of $D'$ in $\Delta$ is shown in Figure \ref{lens_leaves1:fig}-(right). In this case we can slide $\alpha$ along $D'$ to the \iftoggle{BW}{light grey}{green} arc shown in the figure which lies entirely in a level torus of $f$. If we could do this for all the arcs of $\partial D$ cut by singular points, we would happily isotope $\Sigma$ inside a torus level and hence into $T$, and we would be done.

There are however two other cases to consider, and both will be excluded by our minimality assumption on $\Delta$. One is that $D'$ may be a half-disc with only one singular endpoint for $\alpha$, as in Figure \ref{lens_leaves2:fig}. In that case we can isotope $\alpha$ to the \iftoggle{BW}{light grey}{green} curve through $D'$, dragging the spine $\Delta$ behind. In the new configuration $f|_\Sigma$ has strictly less critical points, a contradiction.

\begin{figure}
\begin{center}
\includegraphics[width = 8.5 cm] {\iftoggle{BW}{lens_leaves1-BW}{lens_leaves1}}
\nota{The disc $D'$ is a half-disc and $\alpha$ is incident to two singular points.}
\label{lens_leaves1:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 8.5 cm] {\iftoggle{BW}{lens_leaves2-BW}{lens_leaves2}}
\nota{The disc $D'$ is a half-disc and $\alpha$ is incident to one singular point.}
\label{lens_leaves2:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{lens_leaves3-BW}{lens_leaves3}}
\nota{The disc $D'$ is a quarter disc.}
\label{lens_leaves3:fig}
\end{center}
\end{figure}

In the last case $D'$ is a quarter disc as in Figure \ref{lens_leaves3:fig} and we can isotope $\alpha$ to the \iftoggle{BW}{light grey}{green} curve dragging $\Sigma$ as above, but more carefully: we enlarge the other $p-1$ sheets of $\Delta$ by parallel copies of $D'$. In the new configuration the number of critical points in $f|_\Sigma$ is unchanged, but there are strictly fewer essential saddles: at least one is destroyed and no new one is created. (Note that many inessential saddles may be created.) This is also excluded.
\end{proof}

We have discovered, in particular, that there are closed three-manifolds like $L(5,1)$ and $L(5,2)$ that are not diffeomorphic, although their fundamental groups are both isomorphic to $\matZ/_{5\matZ}$; the two manifolds are both covered by $S^3$, so they also have isomorphic higher homotopy groups.

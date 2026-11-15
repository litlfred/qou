---
doc_id: arxiv-2106.01332v4
doc_title: "Braided matter interactions in quantum gravity via 1 -handle attachment"
section_id: sec-006-v-ribbon-networks-embedded-into-3-manifolds
section_title: "V Ribbon networks embedded into 3-manifolds"
section_number: null
pages: 6-8
source_pdf: 2106.01332v4.pdf
source_sha256: 44c19a99624997bf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 1.0
doc_brief: "Braided matter interactions in quantum gravity via 1 -handle attachment — 14 sections: Front matter; I Introduction; II A topological model of composit"
---
We suppose that particle systems constitute {\it ribbon graphs} in which vertices are thickened to be (homeomorphic to) two dimensional disks (or rectangles), and edges are thickened to ribbons. These objects are embedded in a 3-dimensional ground space, which is taken to be a 3-manifold, and they are also referred to as {\it fat graphs} in the literature. See for instance \cite{Igusa,MP}.   \\

Ribbon graphs are formally defined as oriented surfaces decomposed into two families of rectangular surfaces, i.e. embeddings of the square $[0,1]\times [0,1]$ in the base 3-dimensional manifold, called ``{\it coupons}'' and ``{\it ribbons}'', and a family of ``{\it annuli}'', i.e. embeddings of the cylinder $S^1\times [0,1]$. We will think of coupons as vertices of a graph, thickened into rectangles or, equivalently a $2$-dimensional closed ball, while ribbons will constitute the connecting edges of a graph, thickened to rectangles. Annuli determine the components of framed links, and will therefore be given with a trivialization of the normal bundle, which is described by an integer corresponding to the twisting. Moreover, it is assumed that coupons, ribbons and annuli do not self-intersect, but coupons and ribbons are allowed to meet at one side of the boundary of the rectangular surface. Figure~\ref{fig:ribbongraph} shows a portion of ribbon graph where a central coupon, rectangular and corresponding to a ``fat vertex'' of the graph, is connected to ribbon edges on top and bottom. This is the fundamental unit of a ribbon network considered below, as we can concatenate them by joining their ribbons. \\

\begin{figure}
    \centering
    \begin{tikzpicture}
		
		\draw (0,2) -- (1,0);
		\draw (0.2,2) -- (1.2,0);
		\draw (0,2)--(0.2,2);
		
		\draw (1.5,2) -- (1.5,0);
		\draw (1.7,2) -- (1.7,0);
		\draw (1.5,2)--(1.7,2);
		
		\draw (3,2) -- (2,0);
		\draw (3.2,2) -- (2.2,0);
		\draw (3,2)--(3.2,2);
		
		\draw[dashed] (0.5, 1.8) -- (1.4,1.8); 
		\draw[dashed] (1.8,1.8) -- (2.7,1.8);
		
		\draw (0,0) -- (3.2,0);
		\draw (0,-1) -- (3.2,-1);
		\draw (0,0) -- (0,-1);
		\draw (3.2,0) -- (3.2,-1);
		
		\draw (1,-1) -- (0,-3);
		\draw (1.2,-1) -- (0.2,-3);
        \draw (0,-3)--(0.2,-3);
		
		\draw (1.5,-1) -- (1.5,-3);
		\draw (1.7,-1) -- (1.7,-3);
		\draw (1.5,-3)--(1.7,-3);
		
		\draw (2,-1) -- (3, -3);
		\draw (2.2,-1) -- (3.2,-3);
		\draw (3,-3)--(3.2,-3);
		
		\draw[dashed] (0.5, -2.8) -- (1.4, -2.8);
		\draw [dashed] (1.8,-2.8) -- (2.7,-2.8);
		
			\end{tikzpicture}
    \caption{Example of ribbon graph. The top ribbons and bottom ribbons have one side connected to the central rectangular coupon, homeomorphic to a disk}
    \label{fig:ribbongraph}
\end{figure}

\begin{figure}
    \centering
    \begin{tikzpicture}
		\draw (0,3) -- (3,0);
		\draw (0.3,3) -- (3.3,0);
		
		\draw (3,3) -- (1.8,1.8);
		\draw (1.3,1.3) -- (0,0);
		
		\draw (3.3,3) -- (2,1.7);
		\draw (1.5,1.2) -- (0.3,0);
		
		\draw (0,3) -- (0.3,3);
		\draw (3,3) -- (3.3,3);
		\draw (0,0) -- (0.3,0);
		\draw (3,0) -- (3.3,0);
		
				\end{tikzpicture}
    \caption{A positive crossing of two ribbons, oriented downward}
    \label{fig:crossing}
\end{figure}
Two ribbon graphs are said to be equivalent if there exists an isotopy that transforms one into the other. Equivalence of ribbon graphs is conveniently expressed in combinatorial terms by considering diagrams of ribbon graphs, i.e. projections on the plane. In terms of their diagrams, two ribbon graphs are equivalent if and only if there exists a finite sequence of plane isotopies and moves of type:
\begin{itemize}
    \item 
    Oriented framed Reidemeister moves;
    \item 
    Ribbons can slide above and below coupons;
    \item
    Opposite crossings cancel, after orientation turning is applied;
    \item
    Coupons can be rotated with surface parallel to the plane, so that the attached ribbons spiral around the coupons.
\end{itemize}
This combinatorial moves correspond to the generators of the category of ribbon graphs in \cite{RT}, relations ${\rm rel}_1$ to ${\rm rel}_{13}$. \\

In analogy with spin networks in quantum gravity, we call {\it ribbon networks} the elements of an appropriate subclass of ribbon graphs (introduced below) considered in this article. We assume that our ribbon networks are embedded into $3$-manifolds. A $3$-manifold $M$ is thought of as a temporal fragment of space-time, in the sense that it represents the spatial coordinates at a fixed time. A network embedded in $M$ represents a physical system at time $t_0$. Figure~\ref{fig:embeddednetwork} illustrates a portion of a trivalent network embedded into a $3$-manifold corresponding to an arbitrary braid $B$ of Bilson-Thompson's model.\\ 

\begin{figure}
    \centering
    \begin{tikzpicture}
					\draw[rounded corners=40pt](6,-2)--(4,-1)--(2,-3)--(-2,-2)--(-4,0)--(-2,2)--(2.5,3.5)--(3.8,1)--(7,2)--(9.5,1.8)--(12,0)
					--(8,-3)--(6,-2);
					
					\draw[rounded corners=30] (6,0)--(7.25,-0.5)--(8.5,0); 
					\draw[rounded corners=30] (6.3,0)--(7.25,0.5)--(8.2,0);
					
					\draw (0,0)--(1.4,0);
					\draw (0,0.2)--(0.2,0.2);
					\draw (0.4,0.2)--(0.6,0.2);
					\draw (0.8,0.2)--(1,0.2);
					\draw (1.2,0.2)--(1.4,0.2);
					
					\draw (0.2,0.2)--(0.2,0.4);
					\draw (0.4,0.2)--(0.4,0.4);
					\draw (0.6,0.2)--(0.6,0.4);
					\draw (0.8,0.2)--(0.8,0.4);
					\draw (1,0.2)--(1,0.4);
					\draw (1.2,0.2)-- (1.2,0.4);
					
					\draw (0.2,2)--(1.2,2);
					\draw (0.2,1.5)--(0.2,2);
					\draw (1.2,1.5)--(1.2,2);
					
					\draw (0.2,1.5)--(0,1.5);
					\draw (1,1.5)--(1.4,1.5);
					\draw (0,0.4)--(0.2,0.4);
					\draw (1,0.4)--(1.4,0.4);
					\draw (0,0.4)--(0,1.5);
					\draw (1.4,0.4)--(1.4,1.5);
					\draw (0.2,0.4)--(1,0.4);
					\draw (0.2,1.5)--(1,1.5);
					
					\draw (0.4,1.5)--(0.4,1.7);
					\draw (0.6,1.5)--(0.6,1.7);
					\draw (0.8,1.5)--(0.8,1.7);
					\draw (1,1.5)--(1,1.7);
					\draw (0.4,1.7)--(0.6,1.7);
				    \draw (0.8,1.7)--(1,1.7);
					
					\draw[dashed] (0,0)--(-0.7,0);
					\draw[dashed] (0,0.2)--(-0.7,0.2);
					
					\draw[dashed] (1.4,0)--(2.1,0);
					\draw[dashed] (1.4,0.2)--(2.1,0.2);
					
					 \node (a)  at (60:1.3) {$B$};
					\end{tikzpicture}
    \caption{Fragment of trivalent ribbon network embedded in a $3$-manifold. The box named ``$B$'' corresponds to a braid of Bilson-Thompson model}
    \label{fig:embeddednetwork}
\end{figure}

 We take our ``admissible'' ribbon networks to be closed trivalent ribbon graphs, i.e. ribbon networks with no open edges whose vertices have three incident edges. We allow, moreover, disconnected annuli, i.e. loops, knotted with the rest of a ribbon network. In other words, an admissible ribbon network is a compact (not necessarily connected) surface with boundary whose corresponding spine is a trivalent graph embedded in $3$-space. A vertex coupon is represented as in Figure~\ref{fig:trinion}, and will be called a {\it trinion}. We consider isotopy classes of braided networks, and therefore do not distinguish between representatives of the same class. An isotopy class is determined combinatorially by a slightly modified version of the moves described above. In fact, the set of moves relating diagrams of isotopic surfaces with boundary embedded in a $3$-manifold has been determined in \cite{Matsuzaki} in both the oriented and non-oriented case. Since Bilson-Thompson's framed braids are all oriented, it is reasonable to require that our ribbon graphs, and hence ribbon networks, are all taken to be oriented. In the oriented case, Matsuzaki's moves \cite{Matsuzaki} correspond to the framed Reidemeister moves, as given for example in \cite{Ohtsuki}, Figure~1.8, slide of trinions over and underneath ribbons, and Ishii's IH move in \cite{Ishii}. In fact, the latter move has been considered in \cite{BT2} under the name of exchange move. We remark that using Matsuzaki's moves, in principle, the procedure of trading braiding for twists discussed in \cite{BT2009} is not allowed, as the oriented moves do not include vertex twists. Roughly speaking, we always look at one side of the ribbons, without allowing half-twists. This is consistent with the constructions found in this article, as a consequence of restricting ourselves to oriented surfaces.\footnote{As appeared in Bilson-Thompson's work, full twists are compositions of two half-twists, either positive or negative. In the present context, what is meant by a full twist is a loop with (positive or negative) self-crossing (also called {\it kink}), as in Matsuzaki's moves.} We will see below that it is useful to derive a relation between self-crossing twists and composition of half-twists in order to simplify computations. We will use this relation as a computational tool, although no isolated half-twist appears in our framework. \\

\begin{figure}
    \centering
    \begin{tikzpicture}
 	\draw[rounded corners=20pt](-1,1)--(0,-1)--(0,-2);
 	\draw[rounded corners=20pt](1,1)--(0.5,0)--(0,1); 
 	\draw[rounded corners=20pt](1,-2)--(1,-1)--(2,1);
 	\draw (-1,1)--(0,1);
 	\draw (1,1)--(2,1);
 	\draw (0,-2)--(1,-2);
 	\end{tikzpicture}
    \caption{A trivalent vertex is represented by a trinion}
    \label{fig:trinion}
\end{figure}
	
Lastly, recall that each $3$-manifold arises from surgery on a framed link embedded in the $3$-sphere $\mathbb S^3$, see for instance \cite{Lick}. This result, known in the literature as Lickorish-Wallace Theorem, allows us to represent a $3$-manifold $\mathcal M^3$ by a framed link $\mathcal L$ whose $\mathbb S^3$-surgery produces $\mathcal M_{\mathcal L}^3$. Using the definition of braided network, a framed link $\mathcal L$ is indeed a (possibly part of) braided network. We can therefore represent both base $3$-space and braided matter by means of braided networks as the disjoint union of a framed link $\mathcal L$ representing $\mathcal M_{\mathcal L}^3$, the $3$-dimensional base space, and matter embedded in $\mathcal M^3$ is encoded in an embedded surface with non-trivial number of trinions. In other words, space-time and matter are considered on the same footing.\\

The set of diagrammatic moves relating two framed links that correspond to diffeomorphic $3$-manifolds were obtained by Kirby \cite{Kir}, and are referred to as {\it Kirby's Calculus}. A braided network $\mathcal N$, therefore, is presented as union $\mathcal N = \Gamma\cup \mathcal L$ of a trivalent surface with boundary $\Gamma$ and a framed link $\mathcal L$, where $\mathcal L$ represents (via Lickorish-Wallace Theorem and link surgery) the base $3$-space $\mathcal M^3_{\mathcal L}$, and $\Gamma$ gives the braided matter embedded in $\mathcal M^3_{\mathcal L}$.

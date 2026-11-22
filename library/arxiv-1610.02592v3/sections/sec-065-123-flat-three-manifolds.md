---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-065-123-flat-three-manifolds
section_title: "Flat three-manifolds"
section_number: 12.3
pages: 388-391
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.817
latex_coverage_ratio: 0.984
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We now turn to flat three-manifolds. In dimension two, every orientation-preserving isometry of $\matR^2$ is a translation, and this easily implies that every flat orientable closed surface is a torus. In dimension three we also have \emph{rototranslations}, which produce more orientable manifolds. 

We now classify all the closed flat orientable three-manifolds up to diffeomorphism and prove the following.
\begin{teo} \label{main:flat:teo}
A closed orientable 3-manifold $M$ admits a flat metric if and only if it is a Seifert manifold with $e=\chi=0$.
\end{teo}
There are six such manifolds, listed in Table \ref{seven:table}. 


\subsection{Classification}
Every closed flat 3-manifold is isometric to $\matR^3/_\Gamma$ for some crystallographic group $\Gamma< \Iso(\matR^3)$ acting freely, see Section \ref{crystallographic:subsection}.

\begin{ex}
Every element in $\Gamma$ is either a translation or a rototranslation (defined in Example \ref{rototranslation:example}).
\end{ex}

We prove one half of Theorem \ref{main:flat:teo}.

\begin{prop} \label{flat:to:Seifert:prop}
Every closed orientable flat 3-manifold is a Seifert manifold with $e=\chi=0$.
\end{prop}
\begin{proof}
We have $M=\matR^3/_\Gamma$. Recall the exact sequence
$$0 \longrightarrow H \longrightarrow \Gamma \longrightarrow r(\Gamma) \longrightarrow 0$$
where $H \triangleleft \Gamma$ is the translation subgroup and $r(\Gamma)<SO(3)$ is finite by Proposition \ref{finite:image:r:prop}. We now prove that $\Gamma$ preserves a foliation of $\matR^3$ into parallel lines that projects to a Seifert structure on $M$.

If $r(\Gamma)$ is trivial, then $\Gamma = H$ consists of translations and preserves many foliations into parallel lines that project to a Seifert structure on the quotient 3-torus $M$. If $r(\Gamma)$ is non-trivial, it is isomorphic to $C_n$, $D_{2m}$, $T_{12}$, $O_{24}$, or $I_{60}$. If $r(\Gamma) = C_n$ or $D_{2m}$, it has a common fixed vector line $l\subset \matR^3$ and $\Gamma$ preserves the foliation of lines parallel to $l$.

If $r(\Gamma) = T_{12}, O_{24}$, or $I_{60}$ we obtain a contradiction as follows. In all cases we have $T_{12}\subset r(\Gamma)$. The group $T_{12}$ consists of the identity, the $\pi$-rotations along the three coordinate axis, and the $\pm\frac {2\pi}3$-rotations along the axis spanned by $(1,1,1), (1,-1,-1), (-1,1,-1)$, and $(1,-1,-1)$. 

Pick a rototranslation $h\in \Gamma$ with axis $l$ parallel to $(1,1,1)$, and up to conjugating $\Gamma$ by a translation we may suppose that $l$ contains the origin $0\in\matR^3$. We have $h(0) = (d,d,d)$ for some $d\neq 0$. Since $h^3$ is a translation we get $(3d,3d,3d) \in H$. 

The group $\Gamma$ and hence $T_{12}$ acts on $H$ via conjugation. Therefore $H$ is $T_{12}$-symmetric and $(3d,-3d,-3d)\in H$ using the $\pi$-rotation along the first axis. Hence $t=(6d,0,0) = (3d,3d,3d) + (3d,-3d,-3d) \in H$. The composition $t\circ h^2$ has a fixed point, because it sends $0$ to $(2d,2d,2d)-(6d,0,0) = (-4d,2d,2d)$ which is orthogonal to $l$: a contradiction.

In all cases $M$ has a Seifert structure. By Bieberbach's Theorem (stated as Corollary \ref{Bieberbach:cor}) the manifold $M$ is finitely covered by the 3-torus, and hence $\chi=e=0$ by Proposition \ref{cover:Seifert:prop}.
\end{proof}

We now prove the other half.

\begin{figure}
\begin{center}
\includegraphics[width = 10 cm] {flat.pdf}
\nota{The six closed orientable flat 3-manifolds, up to diffeomorphism. Each is constructed by pairing isometrically the faces of a polyhedron in $\matR^3$ according to the labels. When a face has no label, it is simply paired to its opposite by a translation. The polyhedra shown here are three cubes, two prisms with regular hexagonal basis, and one parallelepiped made of two cubes.}
\label{flat:fig}
\end{center}
\end{figure}

\begin{prop}
Every closed Seifert manifold $M$ with $e=\chi = 0$ admits a flat metric.
\end{prop}
\begin{proof}
There are six such Seifert manifolds up to diffeomorphism, listed in Table \ref{seven:table}. We build a flat metric for each in Figure \ref{flat:fig}.

The figure shows six flat manifolds, constructed by identifying isometrically the faces of a polyhedron in $\matR^3$. The reader is invited to check that each construction gives indeed a flat manifold, by verifying that the flat metric extends to the edges and to the vertices.

In all cases the foliation by parallel horizontal lines (orthogonal to the $P$ faces) descends to a Seifert fibration on the flat manifold. By looking at these lines one checks that the base surface of the fibration is respectively
$$T,\ (S^2,2,2,2,2),\ (S^2,2,4,4),\ (S^2,2,3,6),\ (S^2,3,3,3),\ (\matRP^2,2,2).$$
These orbifolds are obtained respectively from the figures by considering: the square torus, its quotient via a $\pi$-rotation, via a $\frac{\pi}4$-rotation, the quotient of a hexagon torus by a $\frac \pi 3$-rotation, by a $\frac{2\pi}3$-rotation, and the quotient of a Klein bottle via a $\pi$-rotation.

These flat Seifert manifolds have $e=0$ by Proposition \ref{flat:to:Seifert:prop}, and hence they are precisely those listed in Table \ref{seven:table}.
\end{proof}

We have proved Theorem \ref{main:flat:teo}.

\begin{figure}
\begin{center}
\includegraphics[width = 2.5 cm] {\iftoggle{BW}{HW-BW}{HW}}
\nota{The Hantsche-Wendt manifold $M=\matR^3/_\Gamma$. The group $\Gamma$ is generated by three rototranslations along the three \iftoggle{BW}{grey}{red} axis shown, each of angle $\pi$ and with unit displacement (this is a unit cube). A fundamental domain for $\Gamma$ is made of two unit cubes as in Figure \ref{flat:fig}-(bottom, right).}
\label{HW:fig}
\end{center}
\end{figure}

\begin{rem}
The rotational image $r(\Gamma) < SO(3)$ of $\Gamma$ for the six flat manifolds $M=\matR^3/_\Gamma$ constructed in Figure \ref{flat:fig} is respectively $\{e\}$, $C_2$, $C_4$, $C_6$, $C_3$, and the dihedral $D_4 = C_2\times C_2$. The sixth manifold is called the \emph{Hantzsche-Wendt manifold}: the group $\Gamma$ is generated by three rototranslations as in Figure \ref{HW:fig}.\index{three-manifold!Hantzsche-Wendt manifold}
\end{rem}

In contrast with the hyperbolic case, a finite-volume complete flat manifold is necessarily closed (see Proposition \ref{finite:volume:flat:prop}). The Seifert manifolds with boundary and $\chi=0$ are diffeomorphic to the bundles $T\times I$ and $K\timtil I$. Their interiors $T\times \matR$ and $K\timtil \matR$ may be given an \emph{infinite}-volume complete flat structure. The lack of a finite-volume complete flat structure for $K\timtil \matR$ is a reason for preferring the geometric decomposition to the canonical torus decomposition, see Section \ref{geometric:decomposition:subsection}.

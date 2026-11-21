---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-034-65-mapping-class-group
section_title: "Mapping class group"
section_number: 6.5
pages: 193-199
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.857
latex_coverage_ratio: 0.875
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
\label{MCG:section}
We have just proved that two self-diffeomorphisms of $S_g$ are homotopic if and only if they are isotopic. We have also seen that when $g=0$ there are only two self-diffeomorphisms up to isotopy: the identity and a reflection. Do we get a more complicated picture when $g\geqslant 1$? Yes, we get an interesting group, called the \emph{mapping class group} of $S_g$. The group is naturally defined on all finite-type surfaces $S_{g,b,p}$.\index{group!mapping class group}


\subsection{Definition}
Recall that the finite-type orientable surface $S_{g,b,p}$ has genus $g$, it has $b$ boundary components, and $p$ punctures. 
\begin{defn}
The \emph{mapping class group} of $S_{g,b,p}$ is the group
$$\MCG(S_{g,b,p}) = \Diffeo^+(S_{g,b,p})/_\sim$$
where $\Diffeo^+(S_{g,b,p})$ indicates the group of all orientation-preserving diffeomorphisms $S_{g,b,p}\to S_{g,b,p}$ that fix pointwise the boundary and $\varphi\sim\psi$ if $\varphi$ and $\psi$ are connected by an isotopy that fixes the boundary pointwise at every level.
\end{defn}

\begin{example}
The groups $\MCG(S^2)$ and $\MCG(D^2)$ are trivial by Theorems \ref{Smale:teo} and \ref{S2:omotopi:teo}.
\end{example}

The group $\MCG(S_{g,b,p})$ acts on $H_1(S_{g,b,p}, \matZ)$ since homotopic functions induce the same maps in homology. We get a group homomorphism 
$$\MCG(S_{g,b,p}) \longrightarrow \Aut^+\big(H_1(S_{g,b,p}, \matZ)\big) = \Aut^+ \big(\matZ^{n}\big) = \SL_{n}(\matZ)$$
with $n=2g+ \max\{b+p-1,0\}$. This homomorphism is neither injective nor surjective in general. Its kernel is called the \emph{Torelli group} of $S_{g,b,p}$.\index{group!Torelli group} 

The mapping class group of a sphere is trivial, so we look at the torus.


\subsection{The torus}
The mapping class group of the torus is a familiar group of $2\times 2$ matrices.

\begin{prop} \label{Torelli:toro:prop}
The Torelli group of the torus $T$ is trivial and
$$\MCG(T) \Isom \Aut^+(H_1(T)) = \SLZ.$$
\end{prop}
\begin{proof}
Fix a meridian $m$ and longitude $l$ of $T$. A diffeomorphism $\varphi$ of $T$ that acts trivially on $H_1(T) = \pi_1(T) = \matZ^2$ sends $m$ and $l$ to two simple closed curves $\varphi(m)$ and $\varphi(l)$ homotopic and hence isotopic to $m$ and $l$: the proof of Theorem \ref{omotopi:isotopi:teo} shows that $\varphi$ is isotopic to the identity. Therefore the Torelli group is trivial.

A matrix $A\in\SLZ$ acts linearly on $\matR^2$ preserving the orientation and the lattice $\matZ^2$ and hence descends to a self-diffeomorphism of $T=\matR^2/_{\matZ^2}$. This shows that the map $\MCG(T) \to \Aut^+(H_1(T)) = \SL_2(\matZ)$ is surjective.
\end{proof}

The mapping class group of a surface $S_g$ of genus $g\geqslant 2$ is not isomorphic to a familiar group of matrices, at least as far as we know: indeed (except some low-genus cases) it is still unknown whether $\MCG(S_{g,b,p})$ is \emph{linear}, \emph{i.e.}~isomorphic to a subgroup of $\GL(n,\matC)$ for some integer $n$.

For the moment we content ourselves with a concrete description of some particularly simple elements of $\MCG(S_{g,b,p})$ called \emph{Dehn twists}.


\subsection{Dehn twists} \label{Dehn:twist:subsection}
Let $\gamma$ be a non-trivial simple closed curve in the interior of $S_{g,b,p}$. The \emph{Dehn twist} along $\gamma$ is the element $T_\gamma \in \MCG(S_{g,b,p})$ defined as follows.\index{Dehn twist}

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{Dehn_twist-BW}{Dehn_twist}}
\nota{A Dehn twist along a curve $\gamma$ maps a transverse arc $\mu$ onto an arc which makes a complete left turn.}
\label{Dehn_twist:fig}
\end{center}
\end{figure}

Pick a tubular neighbourhood of $\gamma$ orientation-preservingly diffeomorphic to $S^1\times [-1,1]$ where $\gamma$ lies as $S^1\times\{0\}$. Let $f\colon[-1, 1] \to \matR$ be a smooth function which is zero in $\left[-1, -\frac 1 2\right]$ and $2\pi$ on $\left[\frac 1 2,1\right]$. Let 
$$T_\gamma\colon S_{g,b,p} \longrightarrow S_{g,b,p}$$ 
be the diffeomorphism that acts on the tubular neighbourhood as $T_\gamma(e^{i\alpha},t) = (e^{i(\alpha+f(t))},t)$ and on its complementary set in $S_{g,b,p}$ as the identity. We may visualise $T_\gamma$ by noting that it gives a complete left turn to any arc $\mu$ that intersects $\gamma$ as in Figure \ref{Dehn_twist:fig}. 

\begin{prop} The element $T_\gamma \in \MCG(S_{g,b,p})$ is well-defined and depends only on the isotopy class of $\gamma$.
\end{prop}
\begin{proof}
In the definition of $T_\gamma$ we have chosen a tubular neighbourhood for $\gamma$ and a smooth function $f$. Tubular neighbourhoods are ambiently isotopic, and functions with fixed extremes are isotopic too: these facts imply easily that the isotopy class of $T_\gamma$ is well-defined and depends only on the isotopy class of $\gamma$.
\end{proof}

\begin{oss} To define $T_\gamma$ we needed the orientation of $S_{g,b,p}$, but not an orientation for $\gamma$. A bit surprisingly, if we change the orientation of $\gamma$ the element $T_\gamma$ remains unaffected. 

The inverse $T_\gamma^{-1}$ transforms every curve $\mu$ crossing $\gamma$ via a complete \emph{right}-turn and is sometimes called a \emph{negative Dehn twist}.
\end{oss}

We construct some examples in the torus $T$.
Let $m$ and $l$ be some fixed meridian and longitude on the oriented $T$ forming a positive basis, so that $m\cdot l = +1$ and we get an identification $\MCG(T) = \SLZ$.

\begin{prop}
The Dehn twists $T_m$ and $T_l$ are
$$T_m=\begin{pmatrix} 1 & {-1} \\ 0 & 1 \end{pmatrix}, \qquad T_l = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}.$$
\end{prop}
\begin{proof}
In homology we find
$$T_m(m) = m, \quad T_m(l) = l-m, \qquad T_l(l) = l, \quad T_l(m) =m+l.$$
The proof is complete.
\end{proof}

By Exercise \ref{one:non-sep:ex} there is a unique non-separating simple closed curve $\gamma$ in $S_g$ up to self-diffeomorphism for every $g\geq 1$. Therefore the Dehn twists $T_\gamma$ along non-separating curves in $S_g$ are all conjugate in $\MCG(S_g)$. In the torus case these can be easily identified algebraically.

\begin{cor}
An element $A\in \SL_2(\matZ) = \MCG(T)$ is a (positive or negative) Dehn twist $\Longleftrightarrow$ it is primitive and $\tr A = 2$.
\end{cor}
\begin{proof}
Every such matrix in $\SL_2(\matZ)$ is conjugate to $\matr 1 {\pm 1} 0 1$. 
\end{proof}

\begin{ex} The Dehn twists $T_m$ and $T_l$ generate $\MCG(T)$.
\end{ex}

We have seen that Dehn twists generate $\MCG(T)$, while many elements $A\in \MCG(T)$ are neither Dehn twists nor powers of Dehn twists (those with $\tr A \neq 2$). These two facts extend to higher-genus surfaces $S_g$; we start by generalising the first.


\subsection{Dehn twists generate}
Dehn twists are basic elements in the mapping class group, and we now prove that they generate the whole group. We restrict ourselves for simplicity to compact surfaces $S_{g,b}$.

\begin{teo} \label{twists:generate:teo}
The group $\MCG(S_{g,b})$ is generated by Dehn twists.
\end{teo}

To prove the theorem we will need some preliminary facts. We say that two non-separating simple closed curves in the interior of $S_{g,b}$ are \emph{related} if there is a combination of isotopies and Dehn twists transforming the first into the second.

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{related-BW}{related}}
\nota{Two curves $\alpha$ \iftoggle{BW}{}{(red) }and $\beta$ \iftoggle{BW}{}{(green) }intersecting in one point are related: we get $\alpha = T_\beta(T_\alpha(\beta))$.}
\label{related:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{related2-BW}{related2}}
\nota{Pick two consecutive points in $\alpha$ \iftoggle{BW}{}{(green) }that intersect $\beta$\iftoggle{BW}{}{ (red)}. We can find a third non-separating curve $\gamma$ \iftoggle{BW}{}{(blue) }intersecting $\alpha$ and $\beta$ in $<k$ points. There are two cases (1) and (2): in (1) the curve $\gamma$ intersects $\beta$ in one point and is hence non-separating, in (2) we have two possibilities $\gamma_1, \gamma_2$, and one is certainly non-separating since $\beta$ is.}
\label{related2:fig}
\end{center}
\end{figure}

\begin{lemma}
The non-separating curves in $S_{g,b}$ are all related.
\end{lemma}
\begin{proof}
Let $\alpha$ and $\beta$ be two non-separating curves. 
Up to isotopy they intersect transversely into some $k$ points.
If $k=1$ they are related by a couple of Dehn twists as shown in Figure \ref{related:fig}. If $k=0$, since they are both non-separating, one sees easily that there is another curve $\gamma$ with $i(\alpha,\gamma) = i(\beta,\gamma)=1$: hence $\alpha$ and $\beta$ are both related to $\gamma$, so they are related themselves. If $k\geqslant 2$ we can find a curve $\gamma$ intersecting $\alpha$ and $\beta$ transversely into $<k$ points as shown in Figure \ref{related2:fig} and we proceed by induction on $k$.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{related3-BW}{related3}}
\nota{The arcs $\alpha$ \iftoggle{BW}{}{(red) }and $\beta$ \iftoggle{BW}{}{(green) }intersect at their endpoints and maybe at some $k$ interior points. If $k=0$ and they are oriented as in (1), a Dehn twist along $\gamma$ transforms $\beta$ into $\alpha$. If they are oriented as in (2), a negative Dehn twist along $\gamma$ transforms this configuration into (1). If $k>0$ we look at the first intersection point in $\alpha$. If the orientations are coherent as in (3) a Dehn twist along $\gamma$ decreases $k$. It the orientations are not coherent we change them as in (2).}
\label{related3:fig}
\end{center}
\end{figure}

We now consider $S_{g,b}$ with $b\geqslant 2$ and fix two points $p,q$ in two distinct boundary components of $S_{g,b}$. We consider all the properly embedded arcs in $S_{g,b}$ with endpoints at $p$ and $q$. As above, we say that two such arcs are \emph{related} if there is a combination of Dehn twists and isotopies transforming the first into the second.

\begin{lemma}
The arcs in $S_{g,b}$ with endpoints at $p$ and $q$ are all related.
\end{lemma}
\begin{proof}
Pick two arcs $\alpha$ and $\beta$ and put them into transverse position: they intersect at their endpoints $p$ and $q$ and maybe transversely at some $k$ other points. Figure \ref{related3:fig} shows that after isotopies and Dehn twists we get $\alpha = \beta$.
\end{proof}

We can finally prove Theorem \ref{twists:generate:teo}.
\begin{proof}[Proof of Theorem \ref{twists:generate:teo}]
Let $\varphi$ be a self-diffeomorphism of $S_{g,b}$ fixing pointwise the boundary. We prove that $\varphi$ is generated by isotopies and Dehn twists.

We first prove the case $g=0$ by induction on $b$. We know that $\MCG(S_{0,1})$ is trivial, so we suppose $b\geqslant 2$. Let $p,q$ be points in distinct boundary components of $S_{0,b}$, and $\alpha$ be an arc connecting them. All the arcs with endpoints in $p$ and $q$ are related, and hence $\alpha$ and $\varphi(\alpha)$ are. Therefore up to composing with Dehn twists and isotopies we may suppose that $\varphi$ is the identity of $\alpha$ and hence also on a tubular neighbourhood of $\alpha$. We cut $S_{0,b}$ along $\alpha$ and get $S_{0,b-1}$, with $\varphi$ transformed into a self-diffeomorphism of $S_{0,b-1}$. By induction on $b$ the new $\varphi$ is generated by Dehn twists and isotopies, so the original $\varphi$ also is.

We prove the case $g>0$ by induction on $g$. Let $\alpha$ be a non-separating simple closed curve. Since these are all related, up to isotopies and Dehn twists we may suppose that $\varphi$ is the identity on $\alpha$; as above we can cut $S_{g,b}$ along $\alpha$, get $S_{g-1,b+2}$ and conclude by induction on $g$. 
\end{proof}


\subsection{Action on simple closed curves}
We now show that every element $\varphi\in\MCG(S_g)$ is determined by the way it permutes the (isotopy classes of) simple closed curves in $S_g$.

\begin{prop} \label{action:curves:prop}
The action of $\varphi\in\MCG(S_g)$ on the isotopy classes of simple closed curves is faithful.
\end{prop}
\begin{proof}
The proof of Theorem \ref{omotopi:isotopi:teo} shows that if $\varphi$ fixes the isotopy classes of two essential multicurves $\mu$ and $\eta$ as in Figure \ref{multicurva_decomposizione:fig} then it is isotopic to the identity.
\end{proof}

Recall that every simple closed curve is oriented by assumption: if we considered \emph{unoriented} simple closed curves the proposition would be false, because in low genus there are some $\varphi$ that send every curve to its inverse: this happens for instance with the map $-I \in \SLZ = \MCG(T)$. 


\subsection{References}
The main source for this chapter is the book of Farb -- Margalit \cite{FM}, which contains a lot more information on the mapping class group of surfaces. We have also consulted Benedetti -- Petronio \cite{BP} and Thurson's notes \cite{Th} and book \cite{Th_book}, in particular for Smale's Theorem, that was originally proved in \cite{Sma}.


\chapter{Teichm\"uller space} \label{Teichmuller:chapter}
We have discovered in Chapter \ref{surfaces:chapter} that every surface $S_g$ of genus $g\geqslant 2$ can be equipped with a hyperbolic metric, and we have already noticed that this metric is not unique: this chapter is entirely devoted to studying this non-uniqueness phenomenon.

It turns out that $S_g$ admits a continuous family of non-equivalent hyperbolic metrics, that form altogether a nice topological space called the \emph{Teichm\"uller space} of $S_g$. We prove in his chapter that the Teichm\"uller space of $S_g$ is homeomorphic to an open ball of dimension $6g-6$. To prove this fact we will introduce and study concepts like \emph{length functions}, \emph{earthquakes}, and \emph{Fenchel--Nielsen coordinates}. The simple closed curves and their geodesic representatives will play a fundamental role in all the discussion.

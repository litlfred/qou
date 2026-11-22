---
doc_id: arxiv-2106.01332v4
doc_title: "Braided matter interactions in quantum gravity via 1 -handle attachment"
section_id: sec-007-a-surgery-on-3-manifolds
section_title: "A Surgery on 3-manifolds"
section_number: null
pages: 8-9
source_pdf: 2106.01332v4.pdf
source_sha256: 44c19a99624997bf
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Braided matter interactions in quantum gravity via 1 -handle attachment — 14 sections: Front matter; I Introduction; II A topological model of composit"
---
\label{Surgery}

A cobordism is an ordered triple of manifolds \cite{Kos}, written $\{X_0,Y,X_1\}$, such that $\partial Y = X_0\bigsqcup X_1$. If the manifolds are taken to be oriented, one assumes further that the orientations of $X_i$ and the orientations induced on them by that of $Y$ coincide. \\

Recall first, the definition of handle attachment, which we hereby provide. Let $X$ be a manifold of dimension $n$, and let $\psi$ be an embedding of $\partial B^p\times B^{n-p}$ in $\partial X$, where $B^k$ indicates the standard $k$-dimensional closed ball. We say that we attach a $p$-handle to $X$ when we attach a copy of $B^p\times B^{n-p}$ along the image $\psi(\partial B^p\times B^{n-p})$. The notion of handle attachment is closely related to that of surgery on a manifold. Suppose that we have an embedding of the $k$-dimensional sphere $\phi: \mathbb S^k \longrightarrow M$, into the $n$-dimensional manifold $M$. A framing of $\phi(\mathbb S^k)$ is a (continuous) section of the normal bundle of $\phi(\mathbb S^k)$. An embedded sphere, along with a framing of its image, determine a map $\psi: \mathbb S^k\times \mathbb B^{n-k}\longrightarrow M$ up to isotopy. A $k$-surgry on $\psi$ consists of removing $\psi(\mathbb S^k\times \mathbb B^{n-k})$ from $M$, and replacing it by a copy of $\mathbb B^{k+1}\times \mathbb S^{n-k-1}$ via the map $\psi$. It is known (\cite{Kos,4Manifolds}) that a $k$-handle attachment on a $(n+1)$-dimensional manifold with boundary is equivalent to a $(k-1)$-surgery on the $n$-dimensional boundary. We will therefore, sometimes, improperly use the two names interchangeably.  \\

Let now $X$ be a manifold and consider the cylinder $X\times I$, where $I:= [0,1]$ is the closed unit interval, and let us indicate by $X_i$ the copy $X\times \{i\}$ of $X$ in $X\times I$, with $i=0,1$. We attach a $p$-handle to the boundary of $X\times I$ along a copy of $\partial B^p\times B^{n-p}\hookrightarrow X_1$. It is a known results that the manifold so obtained, is a cobordism $Y$ between $X$ identified with the copy $X_0$ of $X\times I$, and $X_1$ with surgery along the attaching sphere of the $p$-handle. We say that such a cobordism arising from attaching a handle to a given manifold is an {\it elementary cobordism}. \\

Recall, further, that given two cobordisms $\{X_0,Y,X_1\}$ and $\{X'_0,Y',X'_1\}$ where we have a diffeomorphism $X_1 \cong X'_0$ (and compatible orientations in the orientable setting), we can construct a ``composition'' cobordim $\{X_0,Y\bigcup_{X_1}Y',X'_1\}$, obtained by gluing $Y$ and $Y'$ along their (diffeomorphic) common boundary for a given choice of diffeomorphism. This operation of composition of cobordisms can clearly be repeated. We have the following traditional result, proof of which can be found in \cite{Kos}, Chapter $7$. 

\begin{theorem}\label{thm:cobordism}
Let $\mathcal C = \{X_0,Y,X_1\}$ be a cobordism. Then $\mathcal C$ can be obtained as:
$$
\mathcal C = \mathcal C_1 \cup \cdots \cup\mathcal C_t,
$$
for elementary cobordisms $\mathcal C_i = \{X^i_0,Y^i,X_1^i\}$, $i=1,\ldots , t$. 
\end{theorem}

In fact, in our setting we are not interested in all types of elementary cobordisms and, consequently, general types of cobordisms. We restrict ourselves to handles attachment of degree 1 to $4$-manifolds with $3$-dimensional boundary, according to certain specific rules which we now describe. Firstly, observe that if $M$ is a $3$-dimensional manifold, then $\partial B^p\times B^{4-p} = \partial B^1\times B^3$, which is diffeomorphic to two $3$-dimensional closed balls. Then, the $1$-handle attached to $M\times I$ following the procedure described above, is a copy of $B^1\times B^3$, i.e. a cylinder whose section is a $3$-dimensional ball.

---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-008-25-ray-diagram
section_title: "Ray diagram"
section_number: 2.5
pages: 5-6
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
\label{raydiagram}
Let $(\Gamma,Z,\Omega)$ be a BPS structure.  The support property implies that in any bounded region of $\bC$ there are only finitely many points of the form $Z(\gamma)$ with $\gamma\in \Gamma$ an active class. It also implies that all such points are nonzero.
\begin{figure}
\begin{tikzpicture}[scale=0.4]


\draw (5,0) circle [radius=0.1];
\draw[->] (5.1,0.1) -- (8,2);
\draw[->] (4.9,0.1) -- (3,2);
\draw[->](5,0.1)--(5,4);
\draw[->] (10-5.1,-0.1) -- (10-8,-2);
\draw[->] (10-4.9,-0.1) -- (10-3,-2);
\draw[->](10-5,-0.1)--(10-5,-4);
\draw (9.4,2) node { $\scriptstyle Z(\gamma_1)$};
\draw (1.75,2) node {$\scriptstyle Z(\gamma_2)$};
\draw (3.8,4) node {$\scriptstyle Z(\gamma_3)$};
\draw (10-9.4,-2) node { $\scriptstyle -Z(\gamma_1)$};
\draw (10-1.75,-2) node {$\scriptstyle -Z(\gamma_2)$};
\draw (10-3.8,-4) node {$\scriptstyle -Z(\gamma_3)$};

\draw[fill] (8.05,2.05) circle [radius=0.05];
\draw[fill] (2.95,2.05) circle [radius=0.05];
\draw[fill] (4.95,4.05) circle [radius=0.05];
\draw[fill] (10-8.05,-2.05) circle [radius=0.05];
\draw[fill] (10-2.95,-2.05) circle [radius=0.05];
\draw[fill] (10-4.95,-4.05) circle [radius=0.05];
\end{tikzpicture}
\caption{The ray diagram associated to a BPS structure.
\label{fig}}
\end{figure}


By a ray in $\bC^*$ we mean a subset of the form
$\ell=\bR_{>0}\cdot z$ for some $z\in \bC^*$.
Such a ray  will be called active if it contains a point $Z(\gamma)$ for some active class $\gamma\in \Gamma$.  Taken together the active rays form a  picture as in Figure \ref{fig}, which we call the ray diagram of the BPS structure. In general there will be countably many active rays.
We define the height of an active ray $\ell\subset \bC^*$ to be \[\height(\ell)=\inf\big\{|Z(\gamma)|: \gamma \in \Gamma\text{ such that } Z(\gamma)\in \ell\text{ and } \Omega(\gamma)\neq 0\big\}.\]Non-active rays are considered to have infinite height. The support property  ensures that for any $H>0$ there are only finitely many rays of height $<H$.

Associated to any ray $\ell\subset \bC^*$ is a formal sum of twisted characters
\begin{equation}
\label{hamiltonian}\DT(\ell)=-\hspace{-.8em}\sum_{\gamma\in \Gamma: Z(\gamma)\in \ell} \DT(\gamma) \cdot x_\gamma.\end{equation}

Naively, we would like to view  $\DT(\ell)$  as a well-defined holomorphic function on the twisted torus $\bT$, and consider the associated time 1 Hamiltonian flow as a Poisson automorphism
\[\bS(\ell)\in \Aut(\bT).\]
We refer to this as the BPS automorphism associated to the ray $\ell$;
making good sense of it is one of the main technical problems we shall need to deal with.

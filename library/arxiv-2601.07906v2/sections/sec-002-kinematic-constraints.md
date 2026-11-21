---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-002-kinematic-constraints
section_title: "Kinematic constraints"
section_number: null
pages: 11-13
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.942
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
First, we state the constraints that we will impose on each member of the ensemble---that is, not just on average. For each $i$, we demand the spin $J_i$ to be an integer, as is appropriate for a bosonic CFT$_2$. Note that although this is a natural property to demand, it was not imposed in the original ensemble of \cite{Chandra:2022bqq}. In our case, spin quantization will follow as a special case of the stronger constraint of crossing symmetry and modular invariance that we impose in section \ref{sec:crossing}. 

Next, the OPE coefficients must satisfy the following properties under complex conjugation and permutation of the indices (here $\sigma \in S_3$): 
\begin{equation}\label{eq:OPEpermutation}
    C_{ijk}^* = C_{kji}, \quad C_{\sigma(i)\sigma(j)\sigma(k)} = \text{sgn}(\sigma)^{J_i + J_j + J_k}C_{ijk}\,.
\end{equation}
Combining these constraints implies that $C_{ijk}$ is purely real when the sum of spins is even, and purely imaginary when odd. When two operators coincide, the second constraint also implies that $C_{jjk} = (-1)^{J_k}C_{jjk}$, hence the OPE coefficient $C_{jjk}$ can only be nonzero if $J_k$ is even (and moreover $C_{jjk}$ is real). Lastly, we impose the selection rule when one of the operators is the identity, $
    C_{ij\mathds{1}} = \delta_{ij},$
where $\delta_{ij}$ is the Kronecker delta.

To account for the structure of descendant states, we can expand any genus-$g$ partition function into Virasoro conformal blocks \cite{Belavin:1984vu}. Loosely speaking, the blocks resum all contributions to the partition function from descendants, so that the remaining sums are only over primary states and OPE coefficients. More precisely, the conformal block decomposition requires us to pick a channel $\mathcal{C}$, so that\vspace{1mm}
\begin{equation}\label{eq:block_decomposition}
    \overline{Z[\Sigma_g;\Omega,\bar\Omega]} = \int \d^{3g-3} h \,\d^{3g-3} \bar h\,\,\overline{\prod_{e_i\in \Gamma_\mathcal{C}}\!\!\rho(h_i,\bar h_i)\!\prod_{v_{ijk}\in \Gamma_\mathcal{C}}\!\!\!C_{ijk}} \,\,\mathcal{F}_g^{\,\mathcal{C}}(\bm{h};\Omega) \bar{\mathcal{F}}_g^{\,\mathcal{C}}(\bar{\bm{h}};\bar\Omega).
\end{equation}
Let us explain the notation used. $\mathcal{F}_g^{\,\mathcal{C}}$ denotes the genus-$g$ Virasoro conformal block in the channel $\mathcal{C}$. The choice of channel involves a pair-of-pants decomposition of the surface $\Sigma_g$, which gives a set of $3g-3$ moduli, to which we collectively refer as $\Omega$. Similarly, the right-moving conformal block $\bar{\mathcal{F}}_g^{\,\mathcal{C}}$ depends on $3g-3$ independent right-moving moduli $\bar\Omega$. The pair-of-pants decomposition defines a dual trivalent graph $\Gamma_{\mathcal{C}}$, whose edges are labeled by the conformal weights $\bm{h} = (h_1,\dots, h_{3g-3})$ and $\bar{\bm{h}} = (\bar h_1,\dots, \bar h_{3g-3})$, and whose vertices are labeled by the OPE coefficients $C_{ijk}$. This graph specifies the products appearing in the average \eqref{eq:block_decomposition}: each edge $e_i$ contributes a factor of the density of states and each vertex $v_{ijk}$ a factor of $C_{ijk}$, where the pattern of OPE indices is determined by the topology of the graph $\Gamma_{\mathcal{C}}$.

In equation \eqref{eq:block_decomposition}, we used linearity to write the average of $Z[\Sigma_g]$ in terms of the average of the primary data encoded in the $\rho(h_i,\bar h_i)$'s and the OPE coefficients. Recall that this average is defined with respect to the measure $\mu(\{h_i,\bar h_i,C_{ijk}\})$. After averaging, we expect the moment $\overline{\prod \rho \prod C}$ to be a smooth function of the conformal weights $\bm{h},\bar{\bm{h}}$, at least for the states above the black hole threshold---more generally, it is a distribution, with discrete support on the light spectrum and continuous support on the heavy spectrum.
In section \ref{sec:3}, we will see how these moments are related to gravitational partition functions in the bulk.

As an example of the above formalism, let us draw the `sunset' and `dumbbell' channels for the genus-2 partition function, with the corresponding index structures:
\begin{equation}\label{eq:genus2graphs}
     \vcenter{\hbox{
    \begin{tikzpicture}[yscale=-0.65,xscale=0.65]
        \draw[very thick, wilsonred] (0,0) ellipse (1.5 and 1);
        \draw[very thick, wilsonred] (0,1) -- (0,-1);
        \node at (-1.2,0) {$i$};
        \node at (0.25,0) {$j$};
        \node at (1.2,0) {$k$};
    \end{tikzpicture}
    }}
    \rightarrow\, C_{ijk}C_{kji}, \quad \vcenter{\hbox{
    \begin{tikzpicture}[yscale=-0.75,xscale=0.75]
        \draw[very thick, wilsonred] (-1,0) circle (0.5 and 0.5);
        \draw[very thick, wilsonred] (1,0) circle (0.5 and 0.5);
        \draw[very thick, wilsonred] (-0.5,0) -- (0.5,0);
        \node at (-1,-0.2) {$i$};
        \node at (0,0.3)  {$j$};
        \node at (1,-0.2)  {$k$};
    \end{tikzpicture}
    }}
\rightarrow \, C_{iij}C_{jkk}.
\end{equation}
We read the cyclic ordering of the indices of the structure constants in a counter-clockwise sense of the three outgoing lines at each vertex.
There are of course also the same diagrams where some of the indices are permuted.
At genus 3, we have the following inequivalent graph topologies:
\be 
\vcenter{\hbox{\begin{tikzpicture}[scale=.5]
    \draw[very thick, wilsonred] (0,0) to (1,0);
    \draw[very thick, wilsonred] (2,0) to (3,0);
    \draw[very thick, wilsonred] (1.5,0) circle (.5);
    \draw[very thick, wilsonred] (-.5,0) circle (.5);
    \draw[very thick, wilsonred] (3.5,0) circle (.5);
\end{tikzpicture}}}\ , \quad  \vcenter{\hbox{\begin{tikzpicture}[scale=.5]
    \draw[very thick, wilsonred] (1,0) circle (1);
    \draw[very thick, wilsonred] (2,0) to (3,0);
    \draw[very thick, wilsonred] (1,-1) to (1,1);
    \draw[very thick, wilsonred] (3.5,0) circle (.5);
\end{tikzpicture}}}
\ , \quad  \vcenter{\hbox{\begin{tikzpicture}[scale=.5]
    \draw[very thick, wilsonred] (0,0) circle (1);
    \draw[very thick, wilsonred] (0,0) to (1,0);
    \draw[very thick, wilsonred] (0,0) to (-.5,.866);
    \draw[very thick, wilsonred] (0,0) to (-.5,-.866);
\end{tikzpicture}}}\ , \quad 
\vcenter{\hbox{\begin{tikzpicture}[scale=.5]
    \draw[very thick, wilsonred] (-1,1) to (1,1);
    \draw[very thick, wilsonred] (-1,-1) to (1,-1);
    \draw[very thick, wilsonred, bend left=40] (-1,-1) to (-1,1);
    \draw[very thick, wilsonred, bend right=40] (-1,-1) to (-1,1);
    \draw[very thick, wilsonred, bend left=40] (1,-1) to (1,1);
    \draw[very thick, wilsonred, bend right=40] (1,-1) to (1,1);
\end{tikzpicture}}}
\ , \quad 
\vcenter{\hbox{\begin{tikzpicture}[scale=.5]
    \draw[very thick, wilsonred] (0,0) to (1,0);
    \draw[very thick, wilsonred] (0,0) to (-.5,.866);
    \draw[very thick, wilsonred] (0,0) to (-.5,-.866);
    \draw[very thick, wilsonred] (1.5,0) circle (.5);
    \draw[very thick, wilsonred] (-.75,-1.3) circle (.5);
    \draw[very thick, wilsonred] (-.75,1.3) circle (.5);
\end{tikzpicture}}}\  \label{eq:genus3graphs}
\ee
where the first diagram corresponds to the index structure $C_{112} C_{234} C_{345} C_{566}$, the second to $C_{123}C_{124} C_{345}C_{566}$, and so forth.
In general, at genus $g$ we get $2g-2$ OPE coefficients, giving $(3(2g-2)-1)!!$ pairwise index contractions (many of which are related by graph automorphisms).

Note that these are all diagrams that can be drawn on the level of index structures of the OPE coefficients. However, the conformal blocks encode more data than just the graph topology: they are fully specified by the pair-of-pants decomposition and the braiding phases at each vertex of the dual graph (see the figures in \cite{Eberhardt:2023mrq} for the complete graphical representations of the blocks). There are an infinite number of such channels (where the trivalent graphs can be knotted), which are obtained from the basic graphs in \eqref{eq:genus2graphs} and \eqref{eq:genus3graphs} by acting with crossing transformations, also called Moore-Seiberg moves \cite{HatcherThurston1980, LegoTeichmuller,Moore:1988qv}. These crossing transformations will be the topic of the next subsection.

---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-004-typicality-and-index-contractions
section_title: "Typicality and index contractions"
section_number: null
pages: 16-21
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.981
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
\label{sec:typicality}
In the previous subsection, we have stated the requirements of crossing symmetry and modular invariance on the moments of CFT data, which were clearly based on the same requirements as in the regular CFT bootstrap. Now we will state an additional assumption on the ensemble, to which we refer as \emph{typicality}, which has its origin in the theory of quantum chaos.

In chaotic many-body quantum systems, the Eigenstate Thermalization Hypothesis (ETH) is a statistical ansatz to model the matrix elements of simple operators $\mathcal{O}_{ij} = \bra{E_i}\mathcal{O}\ket{E_j}$ in high-energy eigenstates \cite{Deutsch1991,Srednicki1994,Foini:2018sdb,Pappalardi:2022aaz,Jafferis:2022uhu}.  Instead of giving the exact, microscopic matrix elements $\mathcal{O}_{ij}$, the ETH posits a smoothly varying envelope for the diagonal matrix elements, and exponentially small erratic noise in the off-diagonal matrix elements that can effectively be treated as random variables.  As shown in \cite{Foini:2018sdb}, the statistics of these random variables are approximately Gaussian, but important non-Gaussianities can contribute at leading order to higher point thermal correlators \cite{Murthy:2019fgs} (in particular out-of-time-ordered ones). The structure of these non-Gaussian moments is fixed by assuming local unitary invariance in narrow microcanonical windows around high energy eigenstates:
\begin{equation}\label{eq:typicality}
    \overline{\mathcal{O}^U \cdots \mathcal{O}^U}\approx \overline{\mathcal{O}\cdots\mathcal{O}}\,.
\end{equation}
Here $\mathcal{O}^U = U\mathcal{O}U^\dagger$, with $U$ a block-diagonal unitary matrix. This block-diagonal structure is such that $U$ acts non-trivially in small microcanonical windows (that nevertheless contain many energy levels), so as to keep the overall band structure of the Hamiltonian intact. In the context of ETH, the assumption \eqref{eq:typicality} is referred to as typicality. Just like level repulsion, the intuition behind typicality stems from random matrix universality: if the Hamiltonian in a narrow energy band resembles a random matrix, then the relative basis change between the eigenbasis of simple operators and that of the Hamiltonian should be a random unitary. By averaging \eqref{eq:typicality} over $U$ in the unitary group, we immediately infer the index structure for the moments $\overline{\mathcal{O}_{a_1b_1}\cdots \mathcal{O}_{a_nb_n}}$ evaluated in energy eigenstates. Namely, for the moment to be non-zero, each index $a_i$ should be paired with an index $a_j$, and each $b_k$ with some $b_l$. Diagrammatically, the allowed index contractions are visualized by cyclic, cactus and non-cactus diagrams (see \cite{Pappalardi:2022aaz}). 

This statistical approach to chaos and thermalization, formalized in the ETH, is of course very similar to our point of view on OPE statistics and, in fact, a sharp analogy can be made for OPE coefficients of 1 light and 2 heavy operators \cite{deBoer:2024mqg,Belin:2021ryy}. More generally, for theories with a gravitational dual, $C_{ijk}$ can be treated as a random variable as long as at least one index is in the heavy part of the spectrum \cite{Belin:2020hea,Chandra:2022bqq}. 

If the statistics of these random variables were assumed to be Gaussian,\footnote{Here, by Gaussian we mean that the probability distribution $\mu(\{h_i,\bar h_i,C_{ijk}\})$ for the heavy OPE coefficients is the form $\exp(-\sum_{i,j,k} f(h_i,\bar h_i,h_j,\bar h_j, h_k,\bar h_k)|C_{ijk}|^2)$, where $f$ is some smooth function of the conformal weights.} the index structure of some statistical moment of OPE coefficients would be entirely fixed by Wick contractions. Although this Gaussian ansatz reproduces many bulk computations \cite{Chandra:2022bqq}, non-Gaussianities are necessary to match the ensemble prediction with gravitational calculations of multiboundary wormhole topologies \cite{deBoer:2024mqg,Collier:2024mgv} and topologies with higher-genus boundaries \cite{Belin:2021ryy, Collier:2023fwi, Hartman:2025ula}. Apart from bulk considerations, these non-Gaussianities are also necessary in order to satisfy the full crossing symmetry requirements discussed in the previous section \cite{Belin:2021ryy,Anous:2021caj}. Hence, we can no longer resort to Wick contractions.

This means we need a different principle to fix the index structure of a given moment of OPE coefficients. As in the ETH, the full index structure can be fixed by appealing to a version of typicality, now tailored to 2d CFT.\footnote{This notion of typicality has also been discussed in \cite{Belin:2021ryy,Belin:2021ibv,deBoer:2024mqg}.} We will focus on theories with a gap up to the black hole threshold, so we are interested in moments of $C_{ijk}$ where all indices correspond to heavy primaries (when one or more indices is the vacuum state, the index structure is trivially fixed by the selection rule $C_{ij\mathds{1}} = \delta_{ij}$). For these moments, typicality is the assumption that the average is approximately invariant under orthogonal transformations in microcanonical windows:
\begin{equation}\label{eq:typicalityCFT}
     \overline{C^T_{i_1i_2i_3}\cdots C^T_{i_{n-2}i_{n-1}i_n}}\,\approx\,\overline{C_{i_1i_2i_3}\cdots C_{i_{n-2}i_{n-1}i_n}} , \quad C^T_{ijk} \coloneqq \sum_{a,b,c} T_{ia}T_{jb}T_{kc} C_{abc}\,.
\end{equation}
Here $T$ is a block-diagonal orthogonal matrix, with each block acting in a microcanonical Hilbert space of dimension $\e^{S(\Delta_i)}$ centered at energy $\Delta_i$ with fixed spin $J_i$. The fact that $T$ is real orthogonal, instead of unitary, follows from the reality condition \eqref{eq:OPEpermutation} (see also section 2 of \cite{Jafferis:2025vyp}). As before, the typicality assumption fixes the index structure by taking the Haar average over the local rotations $T$: the moment of structure constants in \eqref{eq:typicalityCFT} is non-zero only if all indices are repeated pairwise. For example, for the second moment, typicality implies the following structure: 
\begin{multline}\label{eq:genus2typicality}
    \overline{C_{123}C^*_{1'2'3'}} = \sum_{\sigma \in S_3}\delta_{1\sigma(1')}\delta_{2\sigma(2')}\delta_{3\sigma(3')} \,(\text{sgn}(\sigma))^{J_1+J_2+J_3} \,\mathcal{G}_S\!\left[\vcenter{\hbox{
    \begin{tikzpicture}[yscale=-0.5,xscale=0.5]
        \draw[very thick, wilsonred] (0,0) ellipse (1.5 and 1);
        \draw[very thick, wilsonred] (0,1) -- (0,-1);
        \node at (-1.2,0) {\footnotesize $1$};
        \node at (0.29,0) {\footnotesize $2$};
        \node at (1.2,0) {\footnotesize $3$};
    \end{tikzpicture}
    }}\right] \\ 
    + \sum_{\tau,\sigma \in A_3} \delta_{\tau(1)\sigma(1')}\delta_{\tau(2) \tau(3)}\delta_{\sigma(2')\sigma(3')} \,\mathcal{G}_D\!\left[\vcenter{\hbox{
    \begin{tikzpicture}[yscale=-0.85,xscale=0.85]
        \draw[very thick, wilsonred] (-1,0) circle (0.5 and 0.5);
        \draw[very thick, wilsonred] (1,0) circle (0.5 and 0.5);
        \draw[very thick, wilsonred] (-0.5,0) -- (0.5,0);
        \node at (-1,-0.15) {\scriptsize $\tau(2)$};
        \node at (0,0.3)  {\scriptsize $\tau(1)$};
        \node at (1,-0.15)  {\scriptsize $\sigma(2')$};
    \end{tikzpicture}
    }}\right]\,.
\end{multline}
This is a sum over all pairings of 6 indices, with in total $(6-1)!! = 15$ terms, where we have split the sum into the two distinct contraction patterns that can appear for two OPE coefficients (recall eq.~\eqref{eq:genus2graphs}). The first sum, corresponding to the `sunset' contraction $C_{123}C_{123}^*$, is over the symmetric group $S_3$, with sign factors that account for the permutation property \eqref{eq:OPEpermutation}. The function $\mathcal{G}_S$ is a real-valued, totally symmetric smooth function of the conformal weights $h_{1,2,3},\bar h_{1,2,3}$, whose functional form will be discussed below. The second term is a double sum over the alternating group $A_3 = \{\text{Id},(123),(132)\}$, corresponding to the contractions of `dumbbell' type $C_{\tau(1)\tau(2)\tau(2)}C_{\tau(1)\sigma(2')\sigma(2')}$. The real function $\mathcal{G}_D$ also depends smoothly on the weights $\{h_{a},\bar h_{a}\}_{a\in\{\tau(1),\tau(2),\sigma(2')\}}$ in the heavy regime and vanishes when $J_{\tau(1)}$ is odd.\footnote{In each term of \eqref{eq:genus2typicality}, $\mathcal{G}_D$ is the same function, but evaluated on different conformal weights, as specified by the even permutations $\tau$ and $\sigma$.} Because the functions multiplying the Kronecker delta's are smooth, they are approximately constant over a narrow microcanonical window in which $T$ acts, which explains why the structure \eqref{eq:genus2typicality} indeed obeys the typicality condition \eqref{eq:typicalityCFT}.

For the higher statistical moments, the index structure is similarly fixed to be a sum over pairwise index contractions. Because each OPE coefficient has three indices, this automatically implies that all odd moments vanish.\footnote{The fact that odd moments vanish also already follows from the fact that the canonical normalization of the CFT operator $\mathcal{O}_i$
is unchanged under $\mathcal{O}_i\to-\mathcal{O}_i$, so there is no canonical definition of the overall sign of a moment containing an odd number of appearances of $\mathcal{O}_i$. Let us also remark that the statement that odd moments vanish holds in the `pure' gravity ensemble, where all non-vacuum states are above the black hole threshold. If we allow states in the conical defect regime, we can get non-vanishing odd moments: for a contribution to the cubic moment, see \cite{deBoer:2024mqg}.} The non-zero index contractions can be visualized again by trivalent graphs $\Gamma$, such as the ones depicted in \eqref{eq:genus3graphs}, so that the general ansatz compatible with typicality is\vspace{1mm}
\begin{equation}\label{eq:generaltypicality}
    \overline{C_{i_1i_2i_3}\cdots C_{i_{n-2}i_{n-1}i_n}} = \sum_{\text{pairings } P} \delta^P_{i_1\cdots i_n} \,\mathrm{sgn}(P)\,\mathcal{G}_{\Gamma}\big[\{h_a,\bar h_a\}_{e_a\in \Gamma}\big]\,.
\end{equation}
The sum is over the set of partitions of $n$ elements into $n/2$ pairs (where $n$ is even). To each pairing $P$ we associate a trivalent graph $\Gamma$ (really an equivalence class up to relabellings of the edges) and a product of Kronecker delta's $\delta^P\coloneqq \prod_{(a,b)\in P}\delta_{i_ai_b}$. We define the sign of $P$ by labeling the edges of $\Gamma$ and choosing an orientation for each vertex; then we define $\mathrm{sgn}(P) \coloneqq \prod_{v_{abc}\in \Gamma}\mathrm{sgn}(v_{abc})^{J_{i_a}+J_{i_b}+J_{i_c}} $ where $\mathrm{sgn}(v_{abc})$ is 1 if the index labels $abc$ are ordered clockwise; and $-1$ if they are ordered anti-clockwise. When two index labels coincide, we also define $\mathrm{sgn}(v_{abb}) = 1$. These $\pm$ signs are necessary for compatibility of the ansatz with the permutation property \eqref{eq:OPEpermutation} of the OPE coefficients.


There are a few things to note about the ansatz \eqref{eq:generaltypicality} predicted by typicality. First, there are more allowed contractions in \eqref{eq:generaltypicality} than in the ETH. This is because the Haar average is taken over orthogonal matrices, whereas in `standard' ETH the average is over the unitary group.\footnote{Straightforward extensions of the ETH to the GOE have also been discussed, see \cite{DAlessio:2015qtq}.} Hence, the ETH ansatz for $\mathcal{O}_{a_ib_i}$ always pairs an $a_i$-index with an $a_j$-index, and $b_i$ with $b_j$, while in the CFT case \eqref{eq:generaltypicality} any index can be paired to any other index. This means that, for example, the analog of the dumbbell contraction $\overline{C_{122}C_{133}}$ is absent in ETH, because in ETH the connected part of $\overline{\mathcal{O}_{22}\mathcal{O}_{33}}$ is zero for $E_2\neq E_3$.

Second, the non-zero contraction patterns in \eqref{eq:generaltypicality} are naturally encoded in averages of genus-$g$ partition functions $Z[\Sigma_g]$, expanded in Virasoro conformal blocks as in \eqref{eq:block_decomposition}. However, as explained in the previous section, although the sum over pairings is finite (with $(2n-1)!!$ terms), there is an infinite number of conformal blocks. So, for each graph topology $\Gamma$, the function $\mathcal{G}_{\Gamma}$ can itself be an infinite sum of contributions. In gravity, these contributions consist of bulk topologies with a boundary given by a marked Riemann surface, schematically $\mathcal{G}_\Gamma = \sum_{M_\Gamma} Z_\text{grav}[M_\Gamma]$, as will be explained in section \ref{sec:3}. However, so far we have not assumed a bulk dual, and hence the functions $\mathcal{G}_\Gamma$ only need to be sufficiently smooth for \eqref{eq:generaltypicality} to obey the typicality assumption \eqref{eq:typicalityCFT}.

Third, in the literature on OPE statistics it is customary, by a slight abuse of notation (also perpetrated by some of the present authors), to refer to the functions $\mathcal{G}_\Gamma$ by the corresponding moment $\overline{\prod_{v_{ijk}\in \Gamma}C_{ijk}}$. For example, we could write
\begin{equation}
    \overline{C_{123}C_{123}^*} = \mathcal{G}_S(h_{1,2,3},\bar h_{1,2,3})\,.
\end{equation}
This is not an abuse of notation as long as all indices are different, because only a single term in the sum of \eqref{eq:genus2typicality} will be non-zero. However, when some indices coincide, this is no longer entirely correct: for example,  $\overline{C_{122}C_{122}}$ receives contributions from both the sunset and dumbbell contractions, $\mathcal{G}_S$ and $\mathcal{G}_D$ (see below). This observation may seem like a minor detail, but it is at the root of answering our question why non-handlebodies appear in the sum over topologies! Saving a full explanation of this fact for section \ref{sec:minimal completion}, let us now briefly discuss the structure of the ansatz \eqref{eq:generaltypicality} when a subset of the indices is repeated.

\paragraph{Implications of typicality for repeated indices.} Typicality implies that moments of OPE coefficients are non-zero only when all indices are paired. This includes contractions in which indices are repeated \emph{more than once}. For example, for the OPE variance, the typicality ansatz \eqref{eq:typicalityCFT} for $\mathcal{O}_1\neq \mathcal{O}_2$ reads:\vspace{1mm}
\begin{equation}\label{eq:repeated indices a}
    \overline{C_{122}C_{122}} = \left(1+(-1)^{J_1}\right) \mathcal{G}_S\!\left[\vcenter{\hbox{
    \begin{tikzpicture}[yscale=-0.5,xscale=0.5]
        \draw[very thick, wilsonred] (0,0) ellipse (1.5 and 1);
        \draw[very thick, wilsonred] (0,1) -- (0,-1);
        \node at (-1.2,0) {\footnotesize $1$};
        \node at (0.29,0) {\footnotesize $2$};
        \node at (1.2,0) {\footnotesize $2$};
    \end{tikzpicture}
    }}\right] + \mathcal{G}_D\!\left[\vcenter{\hbox{
    \begin{tikzpicture}[yscale=-0.85,xscale=0.85]
        \draw[very thick, wilsonred] (-1,0) circle (0.5 and 0.5);
        \draw[very thick, wilsonred] (1,0) circle (0.5 and 0.5);
        \draw[very thick, wilsonred] (-0.5,0) -- (0.5,0);
        \node at (-1,-0.15) {\footnotesize $2$};
        \node at (0,0.3)  {\footnotesize $1$};
        \node at (1,-0.15)  {\footnotesize $2$};
    \end{tikzpicture}
    }}\right]\,.\vspace{1mm}
\end{equation}
Note that the factor $\left(1+(-1)^{J_1}\right)$ in the first term projects onto even spin $J_1$, in accordance with the fact that $C_{122}$ vanishes when $J_1$ is odd.\footnote{The function $\mathcal{G}_D$ is non-zero only for even $J_1$, which follows from \eqref{eq:OPEpermutation} and \eqref{eq:genus2typicality} evaluated on the dumbbell contraction $\overline{C_{122}C_{133}}$ with $\mathcal{O}_2 \neq \mathcal{O}_3$.} 

Similarly, when all indices coincide, all contractions contribute:
\begin{equation}\label{eq:repeated indices b}
    \overline{C_{111}C_{111}} = 3\left(1+(-1)^{J_1}\right) \mathcal{G}_S\!\left[\vcenter{\hbox{
    \begin{tikzpicture}[yscale=-0.5,xscale=0.5]
        \draw[very thick, wilsonred] (0,0) ellipse (1.5 and 1);
        \draw[very thick, wilsonred] (0,1) -- (0,-1);
        \node at (-1.2,0) {\footnotesize $1$};
        \node at (0.29,0) {\footnotesize $1$};
        \node at (1.2,0) {\footnotesize $1$};
    \end{tikzpicture}
    }}\right] + 9\,\mathcal{G}_D\!\left[\vcenter{\hbox{
    \begin{tikzpicture}[yscale=-0.85,xscale=0.85]
        \draw[very thick, wilsonred] (-1,0) circle (0.5 and 0.5);
        \draw[very thick, wilsonred] (1,0) circle (0.5 and 0.5);
        \draw[very thick, wilsonred] (-0.5,0) -- (0.5,0);
        \node at (-1,-0.15) {\footnotesize $1$};
        \node at (0,0.3)  {\footnotesize $1$};
        \node at (1,-0.15)  {\footnotesize $1$};
    \end{tikzpicture}
    }}\right]\,.
\end{equation}
These combinatorial factors (or `degeneracies') in the statistical moments of OPE coefficients will be important when we match to gravity in sections \ref{sec:minimal completion} and \ref{sec:5}. 
An entirely analogous observation holds for higher moments of OPE coefficients: when a subset of indices coincide, there are more terms in the ansatz \eqref{eq:generaltypicality} that can contribute, which can originate from different graph topologies.

One interesting point to observe here is that index repetition is not a notion that is invariant under crossing. For example, consider the contribution to $\overline{C_{113}C_{223}}$ from the index contraction $\delta_{12}$. Let us rewrite the discrete Kronicker delta using the continuous Dirac delta $\delta^2(h_1-h_2) \equiv \delta(h_1-h_2)\delta(\bar h_1-\bar h_2)$, multiplied by appropriate densities of states $\rho_i\equiv \rho(h_i,\bar h_i)$. Under the one-point S-transform, this index contraction gets mapped to:
\begin{equation}\label{eq:repeated indices and crossing}
   \int \d h_1\d \bar h_1 \, \delta^2(h_1-h_2)\,\overline{\rho_2\rho_3C_{113}C_{223}} \,|\mathbb{S}_{h_1h_4}[h_3]|^2 =  \overline{\rho_2\rho_3C_{223}C_{223}}\,|\sker{h_2}{h_4}{h_3}|^2.
\end{equation}
By the crossing equation \eqref{eq:S1invariance}, the RHS now contributes to $\overline{\rho_2\rho_{3}\rho_4C_{223}C_{443}}$, and is non-zero even when $h_2$ and $h_{4}$ do not coincide. So we see that crossing symmetry relates moments with repeated pairs of indices to moments with distinct (non-repeated) pairs of indices. This interplay between crossing symmetry and typicality will be at the heart of the mechanism that, on the bulk side, will be responsible for generating a large class of non-handlebodies in the sum over topologies.

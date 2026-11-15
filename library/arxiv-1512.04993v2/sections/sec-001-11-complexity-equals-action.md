---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-001-11-complexity-equals-action
section_title: "Complexity equals action"
section_number: 1.1
pages: 7-9
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.98
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
\label{subsec:CA}

Here we define  CA-duality  within the context of holographic duality. The setup of CA-duality and the relationship between CV-duality and CA-duality is illustrated in Fig.~\ref{fig:CVduality}. Choosing times $t_L , t_R$ on the left and right AdS boundaries of
 the eternal AdS-Schwarzschild black hole determines a state $\ket{\psi(t_L,t_R)}$,
\beq
\ket{\psi(t_L,t_R)} = e^{-i (H_L t_L + H_R t_R)} \TFD,
\eeq
where $\TFD = Z^{-1/2} \sum_\alpha e^{-\frac{\beta E_\alpha}{2} } \ket{E_\alpha}_L\ket{E_\alpha}_R$ is the thermofield double (TFD) state which purifies the thermal state of one side.\footnote{Note that with our conventions, time on both sides of Fig.~\ref{fig:CVduality} increases upwards.}

CV-duality proposes that the complexity of $\ket{\psi(t_L,t_R)}$ is computed from the volume $V$ of a $(D-1)$-dimensional maximal volume slice anchored at $t_L$ and $t_R$,
\beq
\CC(\ket{\psi(t_L,t_R)})
 \sim
\frac{V(t_L,t_R)}{G \ell},
\label{old}
\eeq
where $G$ is Newton's constant and $\ell$ is another length scale (the AdS radius for large black holes and the Schwarzschild radius for small black holes). This yields a complexity which grows linearly with time and is proportional to temperature $T$ and entropy $S$, a result that roughly matches CFT expectations.

The prescription Eq.~\ref{old} has a degree of arbitrariness. First of all the choice of foliation by maximal slices is not  unique. Moreover these slices do not foliate the entire geometry behind the horizon. Another unattractive feature is the introduction of the length scale $\ell$ which varies from case to case. The proposal of this paper remedies
 these unsatisfactory elements while retaining all the benefits of CV-duality.

To motivate the CA proposal we note that the geometry of the $D$-dimensional world volume $\CW$ behind the horizon is roughly that of a $D$-dimensional tube of length $t_L+t_R.$  The (\emph{D}-1)-dimensional cross section of the tube has spatial area $GS$ and time duration $\sim \ell_{\text{AdS}}.$ The world volume of the tube is defined to be $|\CW|$.
 Since $V(t_L,t_R) \sim G S (t_L + t_R)$ the volume formula may be expressed as
\beq
\frac{V(t_L,t_R)}{G \ell_{\text{AdS}}} \sim \frac{|\CW(t_L,t_R)|}{G \lads^2}.
\eeq
Since the cosmological constant $\Lambda$ is proportional to $-1 / \lads^2$, the second expression is roughly the classical action of the world volume $\CW$. This clue leads to CA-duality which we now define.

Consider again the eternal black hole geometry (the extension to other geometries is straightforward) and pick times $t_L$ and $t_R$. Define the Wheeler-DeWitt (WDW) patch $\CW(t_L,t_R)$ to be the union of all spacelike surfaces anchored at $t_L$ and $t_R$. The WDW patch is equivalent to the spacetime region sandwiched between forward and backward light rays sent from the boundary at $t_L$ and $t_R$. $\CW$ is also the spacetime region determined by the data on the maximal slice (or any other spacelike slice within $\CW$) and is naturally associated with the boundary state, e.g. \cite{transhorizon}. Note that $\CW$ is not a causal patch so no single observer is able to monitor all of $\CW$; this is consistent with the complexity not being a conventional quantum mechanical observable.

Let $\CA_\CW$ be the action obtained by integrating the bulk Lagrangian over $\CW$ and including suitable boundary terms on $\partial \CW$ (see \S\ref{sec:bh}). The complexity $\CC$  (defined more fully just below) is roughly the minimum number of gates from a universal set necessary to produce the state of interest from a simple state. CA-duality states that
\beq
\boxed{
\CC(\ket{\psi(t_L,t_R)}) = \frac{\CA_\CW}{\pi \hbar}.} \label{eq:Boxed-CA}
\eeq
The factor of $\pi$ is arbitrarily chosen so that an increase of complexity by one unit advances the phase of $e^{i \CA_\CW/\hbar}$ from one to minus one.
At present we do not assign a physical meaning to this factor of $\pi$, it is only a convention to normalize the complexity.  We speculate in Appendix~\ref{sec:boundapp} that there is a more universal continuum version of complexity where the prefactor can be unambiguously defined.

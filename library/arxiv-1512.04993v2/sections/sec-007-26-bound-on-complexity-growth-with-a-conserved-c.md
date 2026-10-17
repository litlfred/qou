---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-007-26-bound-on-complexity-growth-with-a-conserved-c
section_title: "Bound on complexity growth with a conserved charge"
section_number: 2.6
pages: 14-16
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.995
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
\label{sec:conserved-charge}

The bound Eq.~\ref{C-bound} is general, but if the system carries conserved quantum numbers such as charge $Q$ or angular momentum $J$, a tighter bound might be possible. Intuitively this is because conserved charges provide a barrier to rapid complexification since some energy is tied up in noncomputing degrees of freedom. We first motivate the bound using the charged TFD state and then present the bound.

To define the charged version of the TFD state we introduce a chemical potential $\mu$. We may think of the chemical potential as an electrostatic potential that is positive on one side of the black hole and negative on the other. The TFD state is given by
\beq
| \textrm{TFD}_{\mu} \rangle = Z^{-1/2} \sum_\alpha e^{-{\beta (E_\alpha +\mu Q_\alpha     )}/{2} } \ket{E_\alpha, Q_\alpha }_L\ket{E_\alpha, -Q_\alpha}_R
\label{TFDQ}
\eeq
The time evolution of the state is modified by the chemical potential,
\beq
\ket{\psi(t_L,t_R)} = e^{-i (H_L + \mu Q_L)t_L }  e^{-i (H_R - \mu Q_R)t_R }
| \textrm{TFD}_{\mu} \rangle .
\eeq
(Here $H_L$ and $H_R$ are the $\mu = 0$ Hamiltonians.)
By the same argument that lead to the $\mu =0$ bound, the complexification bound becomes
\beq
\boxed{\frac{d\CC}{dt} \leq  \frac{2}{\pi \hbar} \left[(M - \mu Q) - (M - \mu Q)_{\text{gs}}\right]} \,\,\, \text{(charged black holes),}
\label{CQ-bound}
\eeq
where the subscript $gs$ indicates the state of lowest $(M-\mu Q)$ for a given chemical potential $\mu$.\footnote{$M-\mu Q$ is natural when viewing $\mu$ as an electrostatic potential which modifies the total energy. For another perspective on the proposed bound, note that the complexity of $e^{i  \mu Q t}$ oscillates in time with period $2\pi/\mu$ because $Q$ has integer spectrum. We believe that the combination $M - \mu Q$ serves to remove this rapidly oscillating portion of the complexity.} For rotating black holes the bound becomes
\beq
\boxed{\frac{d\CC}{dt} \leq  \frac{2}{\pi \hbar} \left[(M - \Omega J) - (M - \Omega J)_{\text{gs}}\right]}  \,\,\, \text{(rotating black holes)},
\label{CR-bound}
\eeq
where the role of the chemical potential is played by the angular velocity
$\Omega$.

Bounds of the type Eq.~\ref{CQ-bound} and Eq.~\ref{CR-bound} can be understood using the thermodynamic relation,
\be
d(M-\mu Q) = TdS
\label{thermo-relation}
\ee
or its integrated form,
\be
\left[(M - \mu Q) - (M - \mu Q)_{\text{gs}}\right]= \int_\textrm{gs}^S T dS.
\label{integrated-thermo}
\ee
In other words $\left[(M - \mu Q) - (M - \mu Q)_{\text{gs}}\right]$ is the heat content or internal energy relative to the ground state at fixed $\mu.$  One way to state our hypothesis that black holes are the fastest computers is that they efficiently use all of their internal energy to complexify.\footnote{In earlier work the integral in Eq.~\ref{integrated-thermo} was replaced by the simpler expression $TS.$ Generally the two are approximately the same, but in \S\ref{sec:testingwithbh} we will encounter a case in which they are not. This is the case of near-extremal large charged AdS black holes.} In other words black holes saturate the bound
\be
\frac{d\CC}{dt} \leq \int_\textrm{gs}^S T dS.
\ee

For rotating black holes in $D=3$ we find that the bound is saturated. For charged black holes the situation is more complicated. Assuming the true ground state is empty AdS or the extremal black hole at fixed chemical potential as appropriate, we can show that the bound is sometimes saturated but generally \textit{violated}. However, proper evaluation of the bound raises a difficult dynamical question, specifically the nature of the ground state at nonzero chemical potential. The nature of the ground state depends on the full operator content of the conformal field theory and hence requires a proper UV completion of Einstein-Maxwell theory. At least we must specify the light charged degrees of freedom.

In some cases supersymmetry provides additional constraints and the bound seems to be saturated. More generally the bound appears to be either qualitatively valid, up to an order one factor, or badly violated but in a situation where the true ground state is probably drastically different from the extremal black hole. We find the uncharged bound of Eq.~\ref{C-bound} is always obeyed.

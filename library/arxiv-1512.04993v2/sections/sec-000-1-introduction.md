---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 4-7
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.995
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
According to the holographic principle all physics is encoded at the boundaries of spacetime.  A good deal is known in the context of AdS/CFT about this encoding as long as we restrict our attention to the region outside horizons. Very much less is known about the holographic encoding  of physics behind black hole horizons. The  purpose of this paper is to explore a proposal for how properties of the black hole interior are represented on the holographic boundary. We propose that the quantum complexity of the boundary state is equal to the classical action of a spacetime region that extends deep inside the horizon. This region---which we call the Wheeler-DeWitt patch---is defined as the bulk domain of dependence of a bulk Cauchy slice anchored at the boundary state. For the case of one- and two-sided black holes in Anti-de Sitter space, the geometry is shown in Fig.~\ref{fig:CVduality}. Quantum complexity $\CC$ is the minimum number of elementary operations (quantum gates) needed to produce the boundary state of interest from a reference state. Calling the action of the Wheeler-DeWitt patch $\CA$, our proposal is \cite{Brown:2015bva}
\be
\CC = \frac{\CA}{\pi \hbar}.
\label{eq:CAformula}
\ee

\begin{figure}
\label{fig:CVduality}
\centering
\includegraphics[width=.9\textwidth]{fig-CVvsCA.pdf}

\caption{The Penrose diagrams for two-sided eternal black holes (left) and one-sided black holes that form from collapsing shock waves (right). The two-sided black hole is dual to an entangled state of two CFTs that live on the left and right boundaries; the one-sided black hole is dual to a single CFT. The (old) complexity/volume conjecture related the complexity of the entangled CFT state to the volume of the maximal spatial slice anchored at the CFT state. Our (new) complexity/action conjecture relates the complexity of the CFT state to the action of the Wheeler-DeWitt patch.}
\end{figure}

Quantum complexity entered black hole physics to help quantify the difficulty of decoding Hawking radiation \cite{haydenharlow}, but it appears to also shed light on physics behind the horizon. It was observed that black hole interiors grow in time long after local equilibrium is reached \cite{hartmanmaldacena}. The complexity of the plasma dual to the black hole is also expected to increase long after local thermal equilibrium is reached, so it was proposed that the two growths are dual descriptions of the same phenomenon  \cite{Cgeodesicduality,Susskind:2014rva}. In this paper we will characterize the size of the black hole interior by its action. This action conjecture subsumes a previous conjecture \cite{complexityshocks} that characterized the size of the black hole interior by its spatial volume.

The original complexity/volume  or ``CV'' duality \cite{complexityshocks} stated that the complexity of the boundary state is proportional to  the spatial volume $V$ of a maximal slice behind the horizon,
\beq
\CC \sim \frac{V}{G \ell},
\label{CV--duality}
\eeq
where  $\ell$ is a length scale that has to be chosen appropriately for the configuration (typically either the AdS radius or the radius of the black hole).

 CV-duality had a number of nice features. The maximal volume slice is a relatively robust geometric object that naturally grows at a rate roughly proportional to the temperature $T$ times the entropy $S$ of the black hole. CV-duality works because $TS$ provides a rough estimate for the rate of complexification of a strongly coupled conformal plasma. Shock wave geometries dual to the insertion of a simple operator in the distant past  provide additional tests of CV-duality. For these shock wave geometries it was found that the maximal volume slice had cancellations that precisely match cancellations expected in the complexity \cite{complexityshocks,localshocks, Susskind:2014jwa}. Finally, various tensor network constructions qualitatively agreed with the holographic results \cite{complexityshocks,localshocks}. (For additional work on the CV-duality, see also \cite{Alishahiha:2015rta,Barbon:2015ria,Barbon:2015soa}.)

However,  CV-duality has a number of unsatisfactory elements. First we must choose by hand a length scale $\ell$, depending on the situation. Further, it is also not clear why the maximal volume slice should play a preferred role. The conjecture that complexity equals action  (``CA-duality") inherits all the nice features of CV-duality and none of the unsatisfactory elements.

One virtue of CA-duality is that it associates with the boundary state the entire Wheeler-DeWitt patch, and doesn't single out a special spacelike slice. Another virtue is that it is not necessary to introduce an arbitrary length scale; as a consequence, the prefactor of the complexity could  potentially have physical meaning. CA-duality reproduces the results of CV-duality for small and large AdS black holes without the need to choose different lengths in the two cases. Once the constant in Eq.~\ref{eq:CAformula} has been fixed by considering any particular black hole, the conjecture then makes unambiguous predictions with no further free parameters for black holes of any size, for black holes in any number of dimensions,  for black holes that are charged or rotating, and for states that are not black holes. The CA-duality passes all the same shock wave tests as were passed by CV-duality.

We work in the context of AdS/CFT and assume a familiarity with those notions; we also assume familiarity with notions of quantum information including quantum circuits, see e.g. \cite{complexityreview1,complexityreview2}. CA-duality is a quantum-classical duality, insofar as it relates a highly quantum theory on the boundary (where the complexity is defined) to a highly classical theory in the bulk (where the action is defined). 



In order to use CA-duality we will need to identify a set of weakly interacting semiclassical bulk degrees of freedom, to consider states that are semiclassical with respect to those degrees of freedom, and  to assume the existence of a unique real-valued semiclassical effective action for those degrees of freedom. In this paper we will generally be considering semiclassical bulk states of the Einstein-Maxwell system.


When studying states with growing complexity we will always restrict to times less than $O(e^S)$. Beyond this time the complexity is expected to saturate and fluctuate (and eventually decrease at times of order the quantum recurrence time $O(e^{e^S})$).

The paper is structured as follows:

In \S\ref{subsec:CA} we more precisely define our conjecture.

In \S\ref{sec:infobound} we review bounds on information processing and conjecture that black holes are the fastest computers in nature.

In \S\ref{sec:bh} we examine a number of different types of black holes and compute the growth of the action of the Wheeler-DeWitt (WDW) patch with time.

In \S\ref{sec:testingwithbh} we use our conjecture to compare the rate of growth of action of black holes with a conjectured quantum mechanical bound on complexity growth inspired by a conjectured bound of Lloyd's \cite{lloyd2000ultimate}. We find precise agreement for uncharged and rotating black holes. For charged black holes, the situation appears more complicated, but these complications result from  dynamical issues associated with the production of hair, and we have no controlled examples that violate our bound.



In \S\ref{sec:staticshells} we test our conjectures with an analysis of black holes surrounded by static shells of inert matter. We find our conjectures pass.

In \S\ref{sec:shockwaves} we test our conjectures with an analysis of black holes perturbed by shock waves. We show that CA-duality passes this test, for much the same reason that CV-duality did. We find that the geometry of the Einstein-Rosen bridge of shock wave states matches the geometry of the minimal tensor network that describes such products of precursors. In general, the CA-calculations turn out to be significantly simpler than the CV calculations. We also discuss {complexity growth with} finite-energy {perturbations}.

In \S\ref{sec:tensornetworks} we will provide a tensor network computation of complexification. 
Using tensor network renormalization group techniques, we will show that the growth of complexity is independent of the UV cutoff.



In \S\ref{sec:discussion} we review the main implications of CA-duality presented in this work, comment on a number of extensions and puzzles raised by our work, and discuss some open questions.

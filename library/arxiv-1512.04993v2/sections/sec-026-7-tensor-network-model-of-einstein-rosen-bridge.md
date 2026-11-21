---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-026-7-tensor-network-model-of-einstein-rosen-bridge
section_title: "Tensor network model of Einstein-Rosen bridge growth"
section_number: 7
pages: 43-47
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.9
latex_coverage_ratio: 0.997
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
\label{sec:tensornetworks}

In this section we will perform a nontrivial test of our conjecture using tensor networks. Tensor networks provide a microscopic account of complexity growth, and we will show that this microscopic account  agrees with the results from CA-duality. Further, as the case with shock waves in \S\ref{sec:shockwaves}, this derivation highlights that the complexity growth is dual to the \emph{minimal} quantum circuit that builds the state.


The tensor-network model serves several purposes. It justifies the reduction of the UV Hilbert space of the CFT to a number of active qubits that is not UV sensitive and instead scales like the entropy; it gives a concrete model of complexity along the lines discussed in Appendix~\ref{sec:boundapp}; it shows that the growth of complexity is roughly given by $TS$; it justifies the Hartman-Maldacena proposal \cite{hartmanmaldacena}; and it further supports our speculation that there is an effective low-energy notion of complexity that the action is calculating. We first discuss the tensor network picture for one side of the two-sided black hole; then we discuss the tensor network for the two-sided black hole and  examine its time development.\footnote{For additional work on the relationship between tensor networks and geometry, see also \cite{entrenholo,Swingle:2012wq,vidal_tns_geo,Pastawski:2015qua,Czech:2015qta,Czech:2015xna,Yang:2015uoa,Casini:2015zua}.}

Recall that a CFT is expected to have no long range entanglement on scales longer than the inverse temperature $1/T$. The basic picture is that the ground state renormalization group (RG) circuit remains a good description of the finite temperature RG circuit on scales shorter than $1/T$; at longer scales the state becomes trivial (unentangled). The RG circuit will typically differ from the ground state circuit as the scale $1/T$ is approached, but for simplicity we model the physics using the ground state circuit and a sharp cutoff at scale $1/T$.

The finite temperature state of the CFT is then
\beq
\rho(L,T) = V^k \rho(L/2^k,\Lambda_0)\( V^\dagger\)^k
\eeq
where $V$ is one circuit layer implementing coarse graining by a factor of $2$, $\Lambda_0$ is some UV energy scale [$\rho(L',T=\Lambda_0)$  has only cutoff-scale correlations], and $k = \log_2(\Lambda_0/T)$ is the RG depth. The system size is denoted by the argument $L$ in $\rho(L,T)$ and the number of lattice sites is $(L\Lambda_0)^{D-2}$ (recall that the CFT lives in $D-1$ spacetime dimensions; $D$ is the bulk spacetime dimension).

That was the description of one side of the black hole, but what about the two-sided black hole that purifies $\rho(L,T)$? Let the thermofield double state which purifies $\rho(L,T)$ be $\ket{\text{TFD}(L,T)}$. The RG circuit for the thermofield double state may then be written
\beq
\ket{\text{TFD}(L,T)} = V^k \otimes \(V^*\)^k \ket{\text{TFD}(L/2^k,\Lambda_0)}
\eeq
where $V^*$ appears because $\rho(L,T)$ and $\ket{\text{TFD}(L,T)}$ are related by a partial transpose on the second factor. The state $\ket{\text{TFD}(L',\Lambda_0)}$ roughly consists of $ (L' \Lambda_0)^{D-2}$ EPR pairs shared between the two sides of the thermofield double.

(In fact, this cannot be quite right because the spectrum of $\rho(L,T)$ is not completely degenerate---the thermofield double state is not perfectly maximally entangled---so some spread of the eigenvalues of the reduced state is necessary. However this is not an essential part of the story.)

Now we time evolve the TFD state with the Hamiltonian $H \otimes I + I \otimes H$. This can be represented by a tensor network where we act on the  thermofield double state with $U(t)\otimes U(t)$, where $U(t) = e^{- i  Ht}$ is time evolution with respect to the UV Hamiltonian $H$. Let us ask about the complexity of the resulting state. A naive estimate is \beq
\CC_{\text{naive}} = \CC_{\text{RG}} + c  \Lambda_0 (L\Lambda_0)^{D-2} t,
\eeq
but in fact this UV divergent expression is only an upper bound. A much more efficient circuit can be found by first renormalizing the operator $U(t)$, see Figs. \ref{fig:HM1} and \ref{fig:HM2}.

\begin{figure}
\centering
\includegraphics[width=.7\textwidth]{HM1.pdf}
\caption{Step 1: the time evolution acting on the UV degrees of freedom is renormalized into a time evolution acting on the IR degrees of freedom. The orange connection is the Einstein-Rosen bridge, the red region is the RG network, and the blue parts represent time evolution.}
\label{fig:HM1}
\end{figure}

\begin{figure}
\centering
\includegraphics[width=.7\textwidth]{HM2.pdf}
\caption{Step 2: the IR time evolution is ``rotated" from vertical to horizontal and becomes a part of the Einstein-Rosen bridge. The orange connection is the Einstein-Rosen bridge, the red regions are the RG networks, and the blue parts represent time evolution.}
\label{fig:HM2}
\end{figure}


To compute this renormalization it is useful to work with an infinitesimal time step: $U(\delta t) = I - i (\delta t)H$. The crucial piece of physics is that $H$ is a scaling operator with dimension $\Delta_H = 1$ (because it is the integral of the energy density which has dimension $D-1$). Hence we have
\beq
H^{(L)} V = V 2^{-\Delta_H} H^{(L/2)},
\eeq
where $V$ is one layer of the RG circuit,\footnote{This equation can in principle contain another term, call it $\CO$, on the RHS. This term must have the property that $V^\dagger \CO = 0$ and represents a high-energy contribution not captured by acting with $H^{(L/2)}$ and then $V$. It can nevertheless be argued to be irrelevant for the complexity growth. To fully show that the effective IR time evolution is approximately unitary one would have to examine this correction term more carefully.} and the parenthetical superscript indicates the size of the system. By definition we have $I^{(L)} V = V I^{(L/2)}$. It follows that for one RG step
\beq
\(I^{(L)} -i \delta t H^{(L)} \) V = V \(I^{(L/2)} - i \delta t 2^{-\Delta_H} H^{(L/2)} \)
\eeq
and that for $k$ RG steps
\beq
\(I^{(L)} -i \delta t H^{(L)}\) V^k = V^k \(I^{(L/2^k)} - i \delta t 2^{-\Delta_H k} H^{(L/2^k)}\).
\eeq
Thus time evolution at the UV scale for time $t$ can be traded for time evolution at a longer scale for time $ 2^{-\Delta_H k}t$. Alternatively, if the UV Hamiltonian $H_L$ has microscopic energy scale $\Lambda_0$ and acts on $(L\Lambda_0)^{D-2}$ sites, we may obtain the same action from a renormalized Hamiltonian with UV scale $\Lambda_0/2^k$ acting on $(L\Lambda_0/2^k)^{D-2}$ sites.

If the number of RG steps is $k= \log_2(\Lambda_0/T)$ then the scale of the renormalized Hamiltonian is $\Lambda_0/2^k = T$ and the number of sites on which it acts is $(L\Lambda_0/2^k)^{D-2} = (LT)^{D-2}$. Evolving for total time $t$, the complexity is now upper bounded by
\beq
\CC \leq \CC_{\text{RG}} + c \, T (LT)^{D-2} t \sim \CC_{\text{RG}} +   T S(T) t.
\eeq
This is illustrated in Fig.~\ref{fig:HM1}. The tensor network analysis therefore gives qualitatively the same result as we independently derived using CA-duality.



\subsubsection{Complexity per gate is $O(c)$}

Implicit in the above analysis was the assumption that the complexity per gate in the tensor network is roughly $c$ for a CFT$_2$ (with the obvious generalization to higher dimensions). This is not a trivial assertion; for example, it was proposed \cite{Swingle:2012wq} that random tensors make a good starting point for thinking about the entanglement properties of holographic field theories. However, with high probability a random tensor would be of at least scrambling complexity $O(c \log c)$ and possibly (depending on the ensemble from which the tensor is drawn) of much higher complexity. Recently random tensors have been further advanced \cite{Yang:2015uoa,RandomModelHolgraphy,Hosur:2015ylk} as toy models of holography and have been shown to satisfactorily model the entanglement structure of the field theory in terms of bulk minimal surfaces. However here we argue that such models do not correctly capture the complexity properties of the holographic field theory.

Let us justify this claim. First, note that each line in the tensor network should be understood as consisting of $O(c)$ degrees of freedom bundled together. In other words, every site of the lattice theory has $O(c)$ degrees of freedom, so if, for example, the field theory consists of a large-$N$ SU$(N)$ gauge theory, then each lattice site consists of a large-$N$ matrix quantum mechanics (coupled to the other sites) and we expect $c \sim N^2$.

It is easiest to first analyze the part of the network corresponding to conventional time evolution (the wormhole part). Implementing one layer of gates in the circuit corresponds to evolving with our properly normalized local Hamiltonian for a time of order the inverse temperature. Since the local Hamiltonian acts on $O(c)$ degrees of freedom per site and we evolve for a time of order $\beta$, the complexity of the resulting tensor is also $O(c)$. This implies that the rate of increase in complexity is proportional to the product of the central charge $c$, the number of thermal cells $(L T)^{D-2}$, and the temperature $T$. This combines to give $ST$.

Now let us analyze the RG part of the network (the part outside the horizon). Suppose we are performing a $2\rightarrow 1$ RG procedure in one boundary spatial dimension ($D=3$) by mapping the ground state on $L$ sites to the ground state on $L/2$ sites. This mapping is accomplished by some unitary transformation acting on the local degrees of freedom. Existence of a smooth continuum limit suggests that this unitary is the exponential of a local Hermitian generator. In other words, the RG generator should share the rough characteristics of an ordinary local Hamiltonian acting on the system.

The basic point is then that to achieve scrambling complexity   $O(c \log c)$ for the local gates, we would have to run the local evolution for a time $O(\log c)$. However, because the local generator also couples neighboring sites, correlations will be generated at scale $O(\log c)$. This is unphysical---correlations of $O(\log c)$ are not compatible with bulk locality on the AdS scale. Hence the RG transformation must correspond to running a local generator for a RG time of order one. This implies that the complexity of the gates in the RG transformation are $O(c)$ as claimed.





\section{Discussion}
\label{sec:discussion}

There is no doubt that the interior of a black hole grows with time until some kind of nonperturbative quantum effect saturates the growth, probably at an exponential time. Moreover there is no doubt that the complexity of the dual gauge theory state grows long after it has relaxed to thermal equilibrium. Identifying these growth phenomena is the basis for the complexity-geometry duality. In this paper we have proposed a new form of this duality that eliminates some of the less attractive aspects of CV-duality. The resulting CA-duality says that
 the complexity of a boundary state is dual to the action of the corresponding Wheeler-DeWitt patch in the bulk.

 In this section we will consider some of the implications of CA-duality as well as a sample of open questions for future work.

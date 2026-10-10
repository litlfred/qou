---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-015-12-the-growth-of-wormholes
section_title: "The Growth of Wormholes"
section_number: 12
pages: 35-40
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
text_source: latex
latex_prose_ratio: 0.716
latex_coverage_ratio: 1.0
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
Wormholes or Einstein-Rosen bridges grow with time.
To illustrate this fact we  examine the Penrose diagram \ref{Foliated-BTZ2} of an AdS ``eternal" black hole, or what is really two entangled black holes connected by an Einstein-Rosen bridge.
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{Foliated-BTZ2.pdf}
\caption{Penrose diagram for an AdS eternal black hole. The diagram is foliated by maximal slices. The darker blue portions of the slices represent the wormhole behind the horizons.
The volume of the slices ``bounces," decreasing in the lower part of the diagram, and increasing in the upper part. }
\label{Foliated-BTZ2}
\end{center}
\end{figure}


\bn
I've also drawn a space-like foliation that I'll define precisely in a moment.
One can see that the spatial size of each slice varies as we move up and down the diagram. In particular if we focus on the portion of the slices behind the horizons---the darker blue segments---it is evident that a kind of bounce occurs. The slice at $t=0$ has vanishing length, which then increases symmetrically, both into the future and the past. At first sight I found this very puzzling. It reminded me of something I had thought about long before while I was a student trying to understand the second law of thermodynamics.

Imagine a gas of a large number of classical molecules in a sealed box. At $t=0$ the molecules are all at rest and are confined to a extremely small volume near the center of the box. The entropy of this configuration is very small.
If we now evolve the state into the future the forces between molecules will act to spread their velocities and their positions. The  second law of thermodynamics will push the system to thermal equilibrium, filling the box uniformly, at least to the naked eye. The entropy will increase to the maximum value consistent with the energy. That much is obvious.

If, at $t=0$, instead of running the system into the future we run it back in time,  exactly the same thing will happen but in reverse. The entire history, past to future, will consist of a bounce. The gas will start in apparent equilibrium in the far past, spontaneously  begin to contract and collect near the center of the box, and then expand back out into the full volume. The entropy will decrease from its large initial equilibrium value to approximately zero, and then bounce back.


Why do we never see such 2nd-law-violating  phenomena? One answer is that they are very unstable;
 any minute ``butterfly" perturbation    will quickly reverse the decrease of entropy  and start it increasing. Nevertheless the unperturbed entropy-bounce is a genuine  solution of the classical equations of motion.



My first reaction  to the time-symmetrical  bounce in figure \ref{Foliated-BTZ2} was that it must be some similar phenomenon---a very fine-tuned entropy-bounce. But this cannot be right. The  black holes on both sides of the Penrose diagram are in perfect thermal equilibrium throughout the entire history. It cannot be entropy that bounced, nor can  the second law of thermodynamics be responsible for the  tendency for the wormhole to grow. These paradoxical  facts puzzled me for more than thirty years.

Before resolving the paradox I will define the slicing precisely. At each time (vertical height in the diagram) we  imagine anchoring a space-like surface on the two boundaries. The surface can then be interpolated  in a coordinate invariant way by choosing the slice of \it  maximum spatial volume.\rm  \ These maximal slices are the blue lines and the portion of them behind the horizons is the darker blue segments. We will identify this portion behind the horizons with the wormhole.
It is clear from figure \ref{Foliated-BTZ2} that the spatial volume of the wormhole bounces. It  goes to infinity as the anchoring time goes to $\pm \infty,$ and passes through zero at $t=0.$ 

Because the slices and their volumes are defined in a coordinate invariant manner, according to the standard AdS/CFT lore  there must be a holographic description of the wormhole volume: some property of the quantum state of the dual pair of CFTs at time $t$. Whatever that quantity is it should be minimal  in the thermofield double, and should increase into both the future and the past. Classically it should increase indefinitely but for reasons I will explain, quantum mechanics necessarily bounds the growth.  The 30 year puzzle for me was: What kind of quantity---if not entropy---can behave this way?

This problem is not special to the two-sided black hole. It also occurs in the theory of a single un-entangled black hole. Figure \ref{one-sided} shows the Penrose diagram for a one-sided black AdS hole formed by collapse.
 
 
 \begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{one-sided.pdf}
\caption{One sided AdS black hole formed by collapse.}
\label{one-sided}
\end{center}
\end{figure}

In figure \ref{one-sided-foli} the same history is shown foliated by maximal slices anchored at the boundary. 
 \begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{one-sided-foli.pdf}
\caption{One sided AdS black hole foliated by maximal slices. The dark portions of the slices represents the region behind the horizon, i.e., the bridge to nowhere.}
\label{one-sided-foli}
\end{center}
\end{figure}


In the one-sided case there is no bounce, only  a growth that begins when the horizon forms. In the remote past the slices do not penetrate behind the horizon at all, so we assign them zero volume. At some time the maximal slice intersects the point at which the horizon forms at $r=0.$ From then on the portion of the maximal slice behind the horizon grows as  a function of anchoring time.




In this one-sided case the black hole is not in perfect thermal equilibrium throughout its history. The entropy starts zero or very small, and then  quickly saturates at the equilibrium value. This takes a very short time\footnote{About a millisecond for a solar mass black hole.}, but the increase of the volume of the dark blue slices behind the horizon goes on indefinitely, at least classically. Evidently some feature of the quantum state evolves long after the system has come to thermal equilibrium.



As a matter of terminology, the portion of each slice behind the horizon in figure \ref{Foliated-BTZ2} is the instantaneous Einstein-Rosen bridge or wormhole connecting the two horizons. The growth phenomenon we are interested in is the growth of the wormhole.  In figures \ref{one-sided} and \ref{one-sided-foli} there are not two sides to connect, but there is a growing region behind the horizon that Ying Zhao and I called the ``bridge-to-nowhere." Both the ERB and the bridge-to-nowhere grow in similar manner.

One point to note is that the maximal surfaces do not foliate the entire geometry. As the anchoring time goes to infinity the maximal surfaces tend to an asymptotic maximal surface that lies somewhat below the singularity. Figure \ref{no-fol} shows the regions that are not covered by the foliation.

To reiterate, the important virtue of maximal slicing is that it is defined in a coordinate-independent manner.



 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.2]{no-fol.pdf}
\caption{The grey areas are not covered by the maximal-slice foliation.}
\label{no-fol}
\end{center}
\end{figure}



\subsection{Properties of Growth}

Let's review some facts about  the growth of wormhole volume that follow from the black hole geometry. First of all, except for an early transient, lasting about a thermal time, the growth  is linear with time. In the two-sided case the rate of growth of the volume satisfies,
\be 
\frac{dV(t)}{dt} \sim l_{ads}A T 
\label{Vdot}
\ee
where $t$ is the anchoring time, $A$ is the horizon area, $T$ is the black hole temperature, and $\l$ is the AdS length scale. This is not hard to show using the AdS black hole metric but an easier argument is just dimensional analysis. 
In the one-sided case the asymptotic  rate of growth is half that of the two-sided case.

Let's define a geometric quantity $C$ (yes, we will eventually identify it with complexity, but not yet),
\be 
C \equiv \frac{V}{G\l}
\label{CV}
\ee
Then \ref{Vdot} gives
\be 
\frac{dC}{dt}=\frac{A}{G}T
\ee
and using the Hawking-Bekenstein area-entropy relation
\be  
\frac{dC}{dt}=ST
\label{dCdt=ST1}
\ee
In a little while we will see that this is  the expected rate of growth of complexity for a circuit with $K\sim S$ qubits. 

\subsection{Rindler Time and CV}

The standard architecture for quantum circuits (explained in Lecture I) is illustrated in figure \ref{cirkuit}.
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.4]{cirkuit.pdf}
\caption{}
\label{cirkuit}
\end{center}
\end{figure}
We assume that the circuit comes equipped with a clock, and in each time-step $K/2$ gates act. For sub-exponential time the number of gates in a circuit corresponds to the complexity\footnote{This is the no-collisions assumption discussed at length in Lecture I. It is expected to be correct for sub-exponential time.} $\CC$ of the unitary operator prepared by the circuit satisfies,
\be 
\frac{d\CC}{\d\t} = \frac{K}{2}
\ee
or, assuming $K\sim S$,
\be 
\frac{d\CC}{\d\t} \sim S.
\label{dC-dtau=S}
\ee


If  black holes can be viewed as quantum circuits one may ask what the time-coordinate $\tau$ corresponds to on the black hole side. One hint is that since complexity and entropy are dimensionless, $\tau$ is also dimensionless. The ordinary Schwarzschild coordinate $t$ of a black hole has dimensions of time and therefore cannot be the same as $\t.$ There is however a universal dimensionless time for all non-extremal black holes, namely the Rindler time. The near-horizon geometry has the universal form,
\be 
ds^2 = -\rho^2 d\tau^2 + d\rho^2 +r(\rho)^2 d\Omega^2
\ee
where $\rho$ is proper distance from the horizon and $\tau $ is a hyperbolic boost angle. 
The natural candidate for the circuit time for a black hole is the Rindler time. For now let's accept this identification but 
later, in section \ref{Sec: Lyap and Rind} I will give a precise quantitative argument for identifying circuit time with Rindler time.

Thus I will therefore use the 
 same symbol $\t$ for circuit time, and for Rindler time. We may therefore assume that in the context of  black hole evolution the complexity grows according to \ref{dC-dtau=S} with $\tau$ being Rindler time.

An asymptotic   observer at infinity sees  rate of computation  red-shifted. It is a universal fact for all non-extremal black holes, that the asymptotic time $t$ is related to Rindler time by 
\be 
\t = \frac{2\pi t}{\beta} = 2\pi Tt.
\ee



It follows that the rate of computation as seen from infinity, is
\be 
\frac{d\CC}{dt}  
= ST.
\ee
Compare this with \ref{dCdt=ST1} and one sees that  the quantity $C$ is in fact the complexity $\CC.$ Accordingly \ref{CV} may be written in the form,
\be 
\CC =\frac{V}{G \l }.
\label{CV-dualtiy}
\ee
This formula connecting  complexity and the volume of the the wormhole is the called
 CV  correspondence. It is one of two versions of the complexity-geometry correspondence, the other being  complexity-action formulation. Time will not permit me to go over the CA correspondence, but there are many papers that you can consult.

\bn

Let me summarize and emphasize two points:
\begin{enumerate}
\item Circuit time, measured in steps, corresponds to the Rindler time of a black hole. 
Now repeat and memorize: 

 
\it
Circuit time, measured in steps, corresponds to the Rindler time of a black hole. \rm

\bn 

\item Complexity is proportional to the wormhole volume through
\ref{CV-dualtiy}
\end{enumerate}


Of course this latter point is a conjecture; it was not derived from  first-principles. The argument is due to Sherlock Holmes; I quote the great detective:  ``When you have excluded the impossible whatever remains, however improbable, must be the truth." We  can and will subject item 2 to rigorous testing.

---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-012-9-the-second-law-of-quantum-complexity
section_title: "The Second Law of Quantum Complexity"
section_number: 9
pages: 26-30
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.997
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
I'm not sure why complexity theorists never remarked on the similarity of quantum complexity and classical entropy, or the existence of a second law of complexity\footnote{There is a very interesting paper by Zurek  in which he argues that that the classical entopy of a system is the ensemble average of the Kolmogorov algorithmic complexity of states in phase space. [W. Zurek,  Phys.\ Rev.\ A {\bf 40}, 4731 (1989)] The idea is very similar to the connection between quantum-computational-complexity and entropy described by Brown et.al in  \url{https://arxiv.org/pdf/1701.0110.pdf}}. 
 Just to be clear, although ensemble-averaged complexity is a kind of entropy it is NOT conventional entropy. The conventional entropy of a system of $K$ qubits is bounded by $K\log{2}$, the logarithm of the maximum number of mutually orthogonal vectors in the Hilbert space. By contrast the maximum  complexity is exponential in $K$.  Maximum complexity $\sim 4^K\log{1/\epsilon}$, the number of $\epsilon$-balls in $\suk.$ 

The quantity $4^K \log{}1/\epsilon$ 
does have an interpretation in terms of the entropy of a classical \it auxiliary \rm system 
$\CA$ associated with the quantum system of $K$ qubits. We may think of it as the maximum entropy of a classical system with $4^K$ classical degrees of freedom.  The auxiliary  system is just the classical $4^K$ collection of coordinates\footnote{Stictly speaking, $4^K-1$.} that describe the evolving time-evolution operator $U(t).$ Figure \ref{motion} illustrates the auxiliary system.  Quantities describing the auxiliary system will carry a subscript $\CA.$



For now let us consider a simplified version of the quantum evolution of a system at high temperature. We envision an
ensemble of fictitious particles moving on $\suk$. The particles are  random walkers which all start at the origin of $\suk$ (the identitiy operator) at some initial time. The dynamics is discrete: at each step the position is updated by applying a depth-one circuit. This means the particles execute random walks on the graph
that I just explained.


At each vertex the decision for the next step is made randomly. I will allow the possibility of back-steps along the previous edge. 
Initially the probability is concentrated at the origin and the entropy of the fictitious system is zero.

After one time-step the particle is at the first level of the tree on one of the leaves, as in figure \ref{spider}. The fictitious entropy is $\log{d}$ and the complexity is $\frac{K}{2}.$ In the next step the particle has a probability $\sim 1/d$ to back-track, but for large $d$ that is negligible. With probability close to one the particle moves outward to the next level where the complexity is 
$K.$ and the auxiliary  entropy $S_{\CA}$ is $\log{d^2} = 2\log{d}.$
\bn

After $n$ steps the particle, with high probability, will be at the $n^{th}$ level, the auxiliary entropy will be $S_{\CA} = n\log{d}$,  and the complexity will be
$nK/2.$
Evidently the complexity and fictitious entropy of the auxiliary system  are related,
\be 
S_{\CA} \approx  \CC  \  \log{K}
\label{CsimS}
\ee

This identification is dependent on the negative curvature and high dimensionality of complexity space. These two ingredients are what insure that collisions are rare and that we can identify the level of the tree with the minimum distance from the origin at $I$. In other words, up to a factor $K/2$ we may identify the depth with complexity.

Of course it is not rigorously true that there are no collisions. It's just that collisions are rare for sub-exponential time. We can be reasonably sure that almost all leaves  (vertices) have complexity proportional to their level, but it is much harder to know that a given leaf has not had collisions in the  past. It's for this reason that we identify the entropy $S_{\CA}$ with the ensemble averaged complexity.

The second law of complexity is just the second law of thermodynamics---the overwhelming statistical likelihood that entropy will increase---applied to the ensemble average of complexity. The reason why complexity almost always increases when it is less than maximum is the same as why classical entropy  almost always increases when it is less than maximum---the number of states exponentially increases with increasing entropy/complexity.

Let us follow a particular member of the ensemble. As long as it is not an exponential number of steps from $I$ the complexity will simply reflect the exponentially growing number of states as we mover outward from the origin. It will with very high probability increase linearly with time. 
However once $\CC \sim 4^K$ the particle will have reached the maximum distance on the graph and the complexity will stop increasing. Complexity equilibrium will have been achieved. The number of states with  maximum complexity is so vast, that the particles will get lost among them and remain at maximum complexity for a recurrence time. The recurrence time for the classical system $\CA$  will be $t_{recur} = \exp{S_{\CA}}$ which is doubly exponential in $K,$.
\be
t_{recur} \sim e^{4^K}
\ee

Thus we expect a singly  exponential time $\sim 4^K$ during which complexity linearly grows, after which it remains approximately constant at its maximum. But then, on gigantically long time scales $\sim \exp\exp K$ it will recur to small values, and $U(t)$ will return to the neighborhood of the identity.

 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{2nd-law.pdf}
\caption{Evolution of complexity with time. The ragged red curve is the evolution for a specific instance of an ensemble. The smooth curve is the ensemble average.}
\label{2nd-law}
\end{center}
\end{figure}


The transition from linear growth to complexity equilibrium is very sudden.

 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{cut.pdf}
\caption{The left panel shows a (red) trajectory beginning at the identity and proceeding outward along toward greater complexity. It eventually reaches maximum complexity. The middle panel follows the evolution as it doubles back to a slightly less-than-maximal complexity. At this point the minimal path jumps to the green path. In the third panel the trajectory continues to maximal complexity and then jumps again. }
\label{cut}
\end{center}
\end{figure}

\bn
It is interesting to see how this behavior can be understood in terms of circuit graphs. We can get an idea by looking at figure \ref{cut}. The figure shows the evolution of the $\CA$ auxiliary system moving according to some ``dynamical" rule that mocks up Hamiltonian evolution starting with $U(0) = I.$ The trajectory moves outward and until collisions occur the complexity increases linearly with time. The complexity is proportional to the graph distance from $I$. That's shown as  the red trajectory in the left panel.

Once the trajectory reaches maximum complexity it keeps going, but it has no choice but to visit previously visited sites. With overwhelming probability it will jump to another almost maximally complex state. That is shown in the middle panel. 

But now, there is a shorter path to the end of the red trajectory. It is shown in green. The complexity is \bf NOT \rm the length of the red trajectory but rather the length of the green trajectory. Thus the complexity does not increase and may even decrease a bit.

From there the dynamical red trajectory continues. With overwhelming likelihood it moves outward because the overwhelming number of branches reach outward. It soon reaches the next point where it has to loop around. A new green trajectory forms that is quite different than the previous one, but also has close-to-maximal complexity. That is the reason why the top of the curve in figure \ref{2nd-law} is a bit ragged.

Eventually the auxiliary particle will find its way back to low complexity and the cycle will repeat but this takes a quantum-recurrence time, $\exp \exp K$.

Note that the transition from linearly increasing complexity to equilibrium at the top of the curve is sudden. It's similar to a first order phase transition where another local minimum crosses over and becomes the global minimum.

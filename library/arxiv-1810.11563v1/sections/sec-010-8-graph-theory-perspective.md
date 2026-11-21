---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-010-8-graph-theory-perspective
section_title: "Graph Theory Perspective"
section_number: 8
pages: 17-21
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.996
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
Circuits can be usefully described using graph theory\footnote{See also Henry Lin, ``Caley Graphs and Complexity Geometry",  \url{https://arxiv.org/pdf/1808.06620.pdf}.}. I'll call a graph  describing a circuit a \it circuit graph.\rm 




Let's begin at the identity and act with a circuit of depth one, in other words a circuit of a single step with $K/2$ gates. For simplicity let's assume the allowed gate set is a single non-symmetric two-qubit gate. A choice must be made of how the $K$ qubits are paired. Each pairing will lead to a different unitary. I'll call the number of possible choices $d$ (an odd choice of notation but it corresponds with standard graph-theory notation). It's an easy combinatoric exercise to compute $d$,
\be 
d \sim \frac{K!}{\left(  K/2 \right)!}  \sim \left(  \frac{2K}{e}   \right)^{\frac{K}{2}}
\ee

Let's visualize this by a decision-tree embedded in $\suk$. At the central vertex is the identity operator. The branches (or edges) correspond to the $d$ choices. 

 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{spider.pdf}
\caption{Vertex with $d=8$.}
\label{spider}
\end{center}
\end{figure}

The number of branches or edges $d$ at a vertex is called the degree of that vertex. In our construction every internal vertex has degree $\frac{K!}{\left(  K/2 \right)!}$. A graph in which every vertex has degree $d$ is called d-regular. But so far the circuit graph is not d-regular because the outer boundary vertices have a single edge.
The leaves of the graph are unitary operators in $\suk.$

\bn




Now let's grow the circuit depth by adding another step. I'm going to make one restriction of a technical nature. For large $K$ it makes no difference but it simplifies things. I will assume that when I add a step the choice of pairings is not the same as in the previous step. This  implies that the next layer of the tree has 
$$\frac{K!}{\left(  K/2 \right)!}-1$$
new branches. This is shown in figure \ref{ssspider}
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{ssspider.pdf}
\caption{Regular tree with degree 8, depth 2.}
\label{ssspider}
\end{center}
\end{figure}

Now comes an important assumption which underlies everything I will say. Each endpoint (leaf) of the tree represents a unitary operator. I will assume that the probability of two leaves being the same unitary is vanishingly small. Basically the reason is the extremely high dimension of the space of unitaries. If two leaves represent the same unitary to within $\epsilon$ I will say that a collision occurred. My provisional assumption is that collisions are so rare that they can be ignored.

This no-collision assumption  must eventually break down as the tree grows outward and we will calculate when that happens. But for now let's ignore collisions.

Assuming no-collisions, the number of unitaries that have been reached at depth $D$  is,
\be 
\#unitaries=d^D \approx \left(  \frac{2K}{e}   \right)^{\frac{DK}{2}}
\ee

The number of gates in a circuit of depth $D$ is $DK/2$. Assuming 
no-collisions, the path to each leaf is the minimal path, implying that the number of gates is the complexity. Thus we can write,

\bea 
\#unitaries \it \eq \left(  \frac{2K}{e}   \right)^{\CC} \cr \cr
 &\sim & e^{\CC \log{K}}
 \label{N=expC}
 \eea
Let me rephrase this formula in the following way:

\bn
\it The sub-volume of $\suk$ that corresponds to unitaries of complexity $\CC$ grows exponentially with $\CC.$ \rm

\bn
It says a number of things. First of all if we think of complexity as the distance from the origin (the unit operator ) then it says that the volume grows exponentially with radius---a characteristic of hyperbolic spaces of negative curvature. This may seem surprising: with the usual bi-invariant metric $\suk$ is positively curved. But we are talking about a different metric, relative complexity. This negative curvature is a symptom of chaos and in my opinion it, not fast scrambling, is the general signature of quantum chaos.

Equation \ref{N=expC} suggests something else. In classical statistical mechanics the volume of phase space associated with an ensemble of states of a given entropy is exponential in the entropy. The exponential growth of volume in $\suk$ associated with a given complexity is the basis for a deep analogy between complexity and entropy, including a \it Second Law of Complexity. \rm \  It can be summarized by the slogan:  Complexity is the entropy of the auxiliary system $\CA.$


\bn

One more point about the circuit graph and its embedding in $SU(2^K)$. Figures \ref{spider} and \ref{ssspider} are very schematic. It is difficult to accurately convey the actual properties of the embedding with pictures given the fact that the space is extremely high dimensional. One thing to keep in mind is that with the usual bi-invariant metric, \Suk \ is small in the sense that the largest distance is $\pi/2.$ A single one-step circuit will move $U$ about that distance. So although the tree abstractly grows outward from the center as in the left panel of figure \ref{two-views}, the embedding in \Suk \ looks more like the right panel. 
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.2]{two-views.pdf}
\caption{Two views of the circuit tree. On the left is an abstract decision tree. The complexity of the unitary leaf grows linearly  with the number of steps from the identity at the center. Relative complexity is proportional to the number of steps between leaves. On the right the tree is embedded in \Suk \ with the usual inner product metric.}
\label{two-views}
\end{center}
\end{figure}
The epsilon balls get filled in by the growing circuit in a very fractal manner which is related to the fact mentioned earlier that complexity is discontinuous as $\epsilon\to 0.$



\bn

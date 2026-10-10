---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-007-8-graph-theory-perspective
section_title: "Graph Theory Perspective"
section_number: 8
pages: 17-21
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
text_source: latex
latex_prose_ratio: 0.61
latex_coverage_ratio: 0.992
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

\subsection{Collisions and Loops}

Each vertex of the tree represents a unitary operator and for that reason we can think of the tree as being embedded in $SU(2^K).$ 
Suppose a collision does occur. This means that two leaves of the tree are located at the same point is $\suk.$ We can represent this by drawing the two leaves as a single leaf as in figure \ref{collision}. 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.4]{collision.pdf}
\caption{Two paths collide on the same epsilon-ball.}
\label{collision}
\end{center}
\end{figure}

The figure illustrates the fact that collisions induce loops in the graph. This allows us to translate the rarity of collisions into graph-theoretic terms. No collisions at all would mean no loops, i.e., exact tree-ness. But as we will see, eventually for very large depth, collisions must happen. This means that very large loops must occur. The correct formulation, which we will come back to, is that small loops must be absent or very rare. 

\bn

 Since the number of epsilon-regulated unitaries is finite we will eventually
 run out of room on $\suk$.  That happens when the number of leaves (as given by \ref{N=expC}) is equal to the total number of epsilon-balls as given in
  \ref{V-in-e-balls}. This determines the maximum possible complexity.
 
 
\be 
\left(  \frac{2K}{e}   \right)^{\CC_{max}} = \left(  \frac{2^K}{\epsilon^2} \right)^{4^K/2}
\ee
or



\be 
\CC_{max} = 4^K \left[\frac{1}{2} +\frac{|\log{\epsilon}|}{\log{K}}
\right]
\ee
Again, strong dependence on $K$, weak dependence on $\epsilon.$
\bn
Roughly  $$\CC_{max} \sim 4^K.$$

Apart from a factor of $K$ which is swamped by the exponential, this is also the depth at which collisions must occur. In other words it is the maximum radius at which the tree stops being tree-like. Finally it is also the largest distance  between nodes of the tree---the diameter of the graph.

We can now state the no-collision assumption more precisely. 

\bn

\it 

Loops smaller than $4^K$ are absent or very rare.\rm  

\bn
In graph-theoretic terms, the girth of the graph is $\sim 4^K.$

\bn
Another point follows from the fact that the total number of unitaries is $\sim   e^{4^K}$. We may identify this with the number of vertices in the graph. This implies that the diameter of the graph is logarithmic in the number of vertices.

\bn

\subsubsection*{The breakdown of no-collisions}
Let's consider what happens when the tree-ness breaks down.
Up to that point the graph is a d-regular tree similar to figure \ref{bethe} except with much higher degree.
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{bethe.pdf}
\caption{Regular tree with degree 3}
\label{bethe}
\end{center}
\end{figure}


\bn
But once we reach $\CC_{max}$ the graph can not continue to grow. Collisions occur and loops must form. The graph must double back on itself and revisit previously visited epsilon-balls\footnote{If we follow an epsilon ball from the identity it will not in general perfectly coincide with an epsilon ball after executing a loop. There is a bit of sloppiness but it doesn't seem to be important. Note that if $\epsilon $  is decreased the maximum complexity increases and the graph becomes bigger.}. We show a couple of possible loops that might form in figure \ref{bethe-2}.
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{bethe-2.pdf}
\caption{Graph ceases being a tree and doubles back. Since a group-space is homogeneous the structure must look the same from every vertex. The shortest loops (girth of graph) is of order $4^K.$ Thus the red loop is too short. The loops must look more like the blue loop.}
\label{bethe-2}
\end{center}
\end{figure}

Now we know that any loop which passes through the central node must be very big, namely of length $\sim 4^K.$  But because the space $\suk$ is a group space, every point on the graph is the same as every other point. Thus it must be that loops passing through any point must be equally long. It is clear from the figure that loop containing the red segment is much shorter and should not occur, but the loop containing the blue segment is long and may occur. 




\bn
Let me summarize the conjectured properties of circuit graphs generated by iterating one-step circuits: 

\begin{enumerate}
\item The degree is the same for all vertices and is given by
\be 
\rm degree \it = \frac{K!}{\left(  K/2 \right)!}  \sim \left(  \frac{2K}{e}   \right)^{\frac{K}{2}}.
\ee
This is much smaller than the number of vertices. The graph can be said to be sparse.

\item The number of vertices in the graph is of order $e^{4^K}.$

\item  The greatest distance between vertices (diameter)  is $\CC_{max} \sim 4^K$. The diameter is therefore logarithmic in the number of vertices.

\item Loops of length less than $4^K$ are rare or absent.

\item The graph is homogenous and from any point looks tree-like out to distances of order the diameter.

\end{enumerate}

These properties are very familiar to graph theorists. They are the properties of a good \it expander \rm graph.  Graphs of this type are discrete analogs of finiite negatively curved geometries such as the hyperbolic plane, with identifications that render it compact\footnote{The relation between complexity and such geometries was described in Brown, Susskind and Zhao, \url{https://arxiv.org/pdf/1608.02612.pdf}.} 








\begin{figure}[H]
\begin{center}
\includegraphics[scale=.2]{expander.pdf}
\caption{50-vertex, (almost) regular $d=4$ expander. Generated by some AI optimization  protocol.} 
\label{expander}
\end{center}
\end{figure}


 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.2]{expander2.pdf}
\caption{120 vertex, regular  $d=4$ Ramanujan-expander. Quoting Donetti, et al.:
``Some remarks on its topological properties are in order. The average distance 3.714 is relatively small (i.e. one
reaches any of the 120 nodes starting from any arbitrary origin in less than four steps, on average."  Note: $\log{120}=4.78749174278$. Not too different from  3.714.  The authors then go on to say, ``The clustering coefficient vanishes,
reflecting the absence of short loops (triangles), and the minimum loop size is large, equal to 6, and identical for
all the nodes. In a nutshell: the network homogeneity is remarkable; all nodes look alike, forming rather intricate,
decentralized structure, with delta-peak distributed topological properties."}   
\label{expander2}
\end{center}
\end{figure}



\bn

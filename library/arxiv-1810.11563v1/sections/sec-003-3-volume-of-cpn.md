---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-003-3-volume-of-cpn
section_title: "Volume of CP(N)"
section_number: 3
pages: 6-7
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 1.0
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
To do any kind of rigorous counting of points in a continuous space  we have to coarse-grain the space. An example is counting states in classical statistical mechanics where we coarse grain, replacing points by little balls of radius $\epsilon.$ This allows us to count states, for example to define entropy,
\be
S=\log{(\#states)}
\label{entropy}
\ee
 at the cost an additive term, $\Delta\log{\epsilon}$, $\Delta$ being the dimension of the phase space. In order to count states in $CP(2^K-1)$ or unitary operators in $\suk$ we have to do something similar. 




 The space of normalized states with phase modded out is the projective space $CP{(2^K-1)}$.
  Let's calculate its volume using the usual Fubini-Study metric. The answer is not hard to guess: it is the volume of the sphere of the same dimension divided by $2\pi.$ The volume of $CP(N)$ is, 
 \be 
V[CP(N)] = \frac{\pi^N}{N!} \approx \left(  \frac{e \pi}{N}   \right)^N
\ee




As I said, in order to count states we need to regulate the geometry. The simplest way to do that is to replace points by small balls of radius $\epsilon.$
The volume of an epsilon-ball of dimension $2N$ is
\be 
V[B(2N)] =\frac{\pi^N}{N!} \epsilon^{2N} \approx  \left(  \frac{e \pi}{N}   \right)^N\epsilon^{2N}.
\ee



The obvious thing to do is to divide the volume of $CP(N) $ by the volume of an epsilon-ball. The result is very simple. The
number of an epsilon-balls in $CP(N)$ is  $\epsilon^{-2N}.$

Next we replace $N$ by $2^K-1$. We identify the number of states with
 the number of epsilon-balls in $CP(2^K).$ 
\be 
\#states =\left( \frac{1}{\epsilon}\right)^{2(2^K -1)}
\ee
or
\be 
\log{(\#states}) =  2(2^K-1) \log{(1/\epsilon})
\label{balls-in-CP}
\ee



For $K=4$ and $\epsilon = 1/2$ this gives $1,073,741,824$ $\epsilon$-balls.

Equation \ref{balls-in-CP} shows the same pattern as  \ref{logstates}. It grows rapidly with $K$ like $2^K$, and is only logarithmically sensitive to the cutoff parameter.

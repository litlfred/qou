---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-020-121-properties-of-growth
section_title: "Properties of Growth"
section_number: 12.1
pages: 40-41
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.94
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
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

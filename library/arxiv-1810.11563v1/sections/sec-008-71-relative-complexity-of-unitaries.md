---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-008-71-relative-complexity-of-unitaries
section_title: "Relative Complexity of Unitaries"
section_number: 7.1
pages: 14-16
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.903
latex_coverage_ratio: 0.962
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
The standard inner product metric for unitaries is similar to the inner product metric for states. In fact if we think of unitaries as the wave functions of maximally entangled systems then it is the inner product for such states. The inner product distance between $U$ and $V$ is,
\be 
d(UV) = \arccos \   |\Tr U^{\dag}V|
\ee
where $\Tr$ means the normalized trace defined so that $\Tr I =1.$
For the same reasons that I discussed earlier, the inner product distance is not a useful measure of how difficult it is to go from $U$ to $V$ by small steps. A much better measure is relative complexity.\\


\bn
Given two  unitaries the relative complexity $\CC(U,V)$ is defined  as the minimum number of gates (in the allowed gate set)  satisfying,
\be 
U = g_n g_{n-1}....g_1 V
\label{uggggv}
\ee
to within tolerance $\epsilon.$ The relative complexity of $U$ and the identity may be defined to be the complexity of $U$.
\be 
\CC(U) \equiv \CC(U,I).
\ee


Figure \ref{relative-C} shows how the relative complexity can be thought of in terms of a discrete curve from $V$ to $U$.
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{relative-C.pdf}
\caption{Relative-C}
\label{relative-C}
\end{center}
\end{figure}


\bn
Because the curve defining $\CC(U,V)$ is the shortest such path, we can think of it as a geodesic, but NOT a geodesic with respect to the inner product metric. It is a geodesic with respect to  relative complexity. The geometry defined by relative complexity is very different from the geometry defined by the inner product distance.


\bn
\bf Relative complexity is a metric \rm

\bn

Relative complexity satisfies the four defining conditions to be a metric.

\begin{enumerate}
\item $\CC \geq 0.$
\item $\CC(U,V)= 0 \ \rm iff \it \ U=V $
\item  $\CC(U,V) = \CC(V,U)$
\item  $\CC(U,V) \leq \CC(V,W) + \CC(W,V)$ \ \ \ \rm (Triangle \ Inequality)
\end{enumerate}



In fact it is a particular kind of metric called  \it right-invariant.\rm  

\bn
Suppose that 
\be 
U=(g_n g_{n-1}.......g_1) \  V
\label{U=ggggV2}
\ee
Then for any $W$ it follows that,
\be 
UW=( g_n g_{n-1}.......g_1) \  VW.
\label{U=ggggV3}
\ee
In other words the relative complexity of $U$ and $V$ is the same as that of $UW$ and $VW.$ 
\be 
\CC(U,V) = \CC(UW,VW) \ \ \ \ \ \ \rm (all  \it W)
\ee
This is what it means for $\CC$ to be  right-invariant.



\bn
On the other hand if we multiply from the left,
\be
WU=(W g_n g_{n-1}.......g_1W^{\dag}) \  WV.
\label{U=ggggV4}
\ee
But $(W g_n g_{n-1}.......g_1W^{\dag})$ 
generally is not a product of $n$ allowed gates. Therefore $\CC$ is not left-invariant\footnote{The usual inner-product metric is both left and right invariant. It is called bi-invariant.}.







\bn
It should be obvious from these remarks that quantum complexity is really a branch of geometry---right-invariant geometry\footnote{See Dowling, Nielsen  \url{https://arxiv.org/pdf/quant-ph/0701004.pdf} }

Most of the mathematical literature on the subject is about left-invariant geometry but of course this is just a matter of convention.

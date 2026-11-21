---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-001-11-random-partitions-as-point-processes
section_title: "Random partitions as point processes"
section_number: 1.1
pages: 1-2
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
toc_source: outline
text_source: latex
latex_prose_ratio: 0.867
latex_coverage_ratio: 1.0
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
The aim of this article is to study deformations of discrete determinantal point processes describing distributions or limit distributions on partitions, namely the poissonized Plancherel measure, the $z$-measures and its limiting Gamma process (see e.g. [@boo], [@johanssonplancherel], [@infinitewedge], [@bodist], [@bogamma] and [@bomarkov]). Recall that a partition $\lambda=(\lambda_1 \geq \lambda_2 \geq ...)$ is a finite non-increasing sequence of non-negative integers, and that it can be identified with a Young diagram ([@macdonald]). The set of all partitions will be denoted by $\mathbb{Y}$. As it is usual, for a partition $\lambda \in \mathbb{Y}$, we define its length $l(\lambda)$ as being the index of its last non-zero entry $$\begin{aligned}
l(\lambda):=\max \{i, \hspace{0.1cm} \lambda_i \neq 0 , \hspace{0.1cm} i=1,2,... \},
\end{aligned}$$ and denote its size by $|\lambda|$ $$\begin{aligned}
|\lambda|:= \sum_{i \geq 1} \lambda_i.
\end{aligned}$$ A Young diagram $\lambda \in \mathbb{Y}$ can be seen as a subset of $\mathbb{Z}$ via the map $\lambda \mapsto \{ \lambda_i - i , i=1,2,... \}$ or some shifted version of it. More precisely, when we consider partitions $\lambda \in \mathbb{Y}$ with fixed length $N$, it is convenient to consider the finite set of positive integers $$\begin{aligned}
\{\lambda_i -i+N, \hspace{0.1cm} i=1,...,N\},
\end{aligned}$$ while when the lengths may vary, it is convenient to consider the infinite sets $$\begin{aligned}
\{ \lambda_i - i , \hspace{0.1cm} i=1,2,... \} \text{ or }\{ \lambda_i - i +1/2, \hspace{0.1cm} i=1,2,... \},
\end{aligned}$$ the latter providing a more symmetric picture. In any case, the pushforward of a probability measure on $\mathbb{Y}$ by one of these maps is thus a point process on a discrete subset of $\mathbb{R}$. In the cases we deal with, namely the poissonized Plancherel measure, the $z$-measures and its limiting process with the Gamma kernel, these point processes are determinantal point processes, see definition [\[defdpp\]](#defdpp){reference-type="ref" reference="defdpp"} below.

---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-002-our-results
section_title: "Our results"
section_number: null
pages: 3-4
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
text_source: latex
latex_prose_ratio: 0.86
latex_coverage_ratio: 0.7
doc_brief: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant — Previous work of the author and N."
---
[]{#sec:Our results label="sec:Our results"}

Let $K$ be an oriented, framed knot in $S^{3}$ and $\rho$ a decorated representation of $K$, which is a representation $\rho \colon
\pi_{1}(\comp{K}) \to \slg$ along with a choice of eigenspace for the image of the peripheral subgroup under $\rho$. In particular this choice distinguishes an eigenvalue $m$ of the meridians of $K$. A is a complex number $\mu$ with $e^{\tu \mu} = m$. The main result of [@McPhailSnyderVolume] is the definition of a sequence of invariants $$\qinv{K, \rho, \mu} \in \mathbb{C}$$ for integers $N\ge 2$. We can view them as a quantization of the $\slg$ Chern-Simons invariant, as a geometric twist of the Kashaev [@Kashaev1995] and ADO [@Akutsu1992] invariants, or as a candidate mathematical realization of $\slg$ Chern-Simons theory. The construction makes sense (and our results do too) for links and tangles as well but for simplicity we restrict to the case of knots.

Let $D$ be an open knot diagram of $K$ (i.ea $1$-$1$ tangle diagram whose closure is $K$). Let $E$ be the set of internal segments (edges) of $D$. Using quantum dilogarithms we define an $\actq{D,
\mu}{} \colon \mathbb{C}^{E} \to \mathbb{C}$ so that $$t \mapsto e^{ N\actq{D, \mu}{t} } \colon  \mathbb{C}^{E} \to \mathbb{C}$$ is a meromorphic function. Given the choice of some additional gauge data $u$ called a the invariant of [@McPhailSnyderVolume] is by definition a state sum $$\qinv{K, \rho, \mu}
  =
  \frac{1}{N^{\operatorname{cr}(D)}}
  \sum_{n \in \nset{N}^{E}}
  e^{ N\actq{D, \mu}{(\beta + n)/N} }$$ where $\nset{N} = \left\{ \def\given{\ \middle| \ }  0, 1, \dots, N- 1 \right\}$ and $\operatorname{cr}(D)$ is the crossing number of $D$. The vector $\beta \in \mathbb{C}^{E}$ encodes $(\rho, u)$. For a vector $k \in \mathbb{Z}^{E}$ with integer entries a is $$\label{eq:state integral intro}
  \stint{D, \mu, \beta}{k}
  \mathrel{:=}
  \int_{[0,1]^{E}}
  \exp \mathopen{}\left[ N( \actq{D, \mu}{\beta/N+ t} - \tu k \cdot t )
  \right]
  \dif t$$ In [\[sec:State integrals big\]](#sec:State integrals big){reference-type="ref" reference="sec:State integrals big"} we prove ([\[main result\]](#main result){reference-type="ref" reference="main result"}) that $\qinv{}$ is given by the sum over all state integrals: $$\label{eq:state integral sum intro}
  \qinv{K, \rho, \mu}
  =
  N^{(|E| - 1)/2}
  \sum_{k \in \mathbb{Z}^{E}}
  \stint{D, \mu, \beta}{k}$$ The main technical difficulty is ensuring the contour of integration avoids the poles of $e^{N\actq{D, \mu}{}}$. We discuss the required algebraic condition in [\[sec:Gauge
transformations and admissibility\]](#sec:Gauge
transformations and admissibility){reference-type="ref" reference="sec:Gauge
transformations and admissibility"}. Once this is handled using the methods of [@McphailSnyder2024octahedralcoordinateswirtingerpresentation] re-writing the sum in terms of the integrals is an elementary application of Fourier series. In particular the convergence of the infinite sum is automatic.

As $N\to \infty$ the functions $\actq{D , \mu}{}$ to a function $\act{D}{}$ that we interpret as the Chern-Simons action. In the literature $\act{D}{}$ is frequently called the [@arXiv:math/0009165] and denoted $V$. The critical points of $\actq{D}{}$ are boundary-parabolic representations of $K$ and the critical values are their Chern-Simons invariants. As such [\[main result\]](#main result){reference-type="ref" reference="main result"} accomplishes [\[step 1\]](#step 1){reference-type="ref" reference="step 1"} towards proving a volume conjecture for $\qinv{}$. We state this precisely, explain how the sum over $\mathbb{Z}^{E}$ is natural, and discuss barriers to [\[step 2\]](#step 2){reference-type="ref" reference="step 2"} in [\[sec:Formal asymptotics\]](#sec:Formal asymptotics){reference-type="ref" reference="sec:Formal asymptotics"}.

---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-001-11-random-partitions-as-point-processes
section_title: "Random partitions as point processes"
section_number: 1.1
pages: 1-4
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
toc_source: outline
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 1.0
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

## Determinantal point processes and Christoffel deformations

A specific and important class of determinantal point processes are the so called *orthogonal polynomial ensembles*, see e.g. the survey [@konig] and references therein. They are $N$-points random configurations for some fixed deterministic $N$ governed by the kernel of the orthogonal projection onto the first $N$ polynomials in the Hilbert space $L^2(\mathbb{R},\mu)$ for some measure $\mu$ with finite moments of all orders. This kernel is namely the $N$-th Christoffel-Darboux kernel of the polynomials orthogonal with respect to $\mu$. For example, the classical G.U.E. from random matrix theory is the orthogonal polynomial ensemble with the Gaussian weight on $\mathbb{R}$, and is thus described by the Hermite polynomials, see e.g. [@konig] and references therein.\

Multiplying the weight $\mu$ by a squared polynomial having its roots in $\mathbb{R}$ leads to the so-called Christoffel deformation of the system and an explicit description of the new family of orthogonal polynomials as well as the corresponding deformed point process.

## Background and motivations: characteristic polynomials and Palm measures

We prove in this note that the multiplicative structure of Christoffel deformations of orthogonal polynomial ensembles carries on to more general determinantal point processes. Our method is essentially by approximation of the models in consideration by orthogonal polynomial ensembles. However, since from [@bufetovconditional] we know that any determinantal point process on the real line is approximated by orthogonal polynomial ensemble in a particular sense, we hope to establish the existence and the explicit descritption of Christoffel deformations of determinantal point processes in full generality in a future work; this method has already been fruitful in order to prove the Giambelli compatibility of determinantal point processes in [@bufetovlazag].\
Besides being a natural deformation of a point process, there are two directions in which Christoffel deformations have applications: characteristic polynomials and Palm measures. Let us also mention that Christoffel deformations have been considered in [@bufetovqiupickrell] in order to describe the ergodic decomposition of inifinite Hua-Pickrell measures.\
The study of charcteristic polynomials of random matrices has connections with number theory, see for example [@keatingsnaith] or the more recent paper [@chhaibinajnudel]. In [@baikdeiftstrahov], explicit formulas for averages of products and ratios of characteristic polynomials of random matrices are obtained by the formalism of Christoffel deformations.

There are lots of studies of averages or more generally moments of characteristic polynomials in the continuous setting. For the discrete one, in [@giambelli], the authors develop the notion of *Giambelli compatible point processes* which provides a suitable formalism in the study of characteristic polynomials of general point processes. Among others, the authors show that the $z$-measures are Giambelli compatible, which means that characteristic polynomials of these processes are well defined and involve determinantal formulas.

Rather than directly studying characteristic polynomials, from which determinantal formulas for the correlations can be obtained (see [@fyodorovstrahov1], [@fyodorovstrahov2], [@borodinstrahov], and [@giambelli]), we go the reverse way and study Christoffel deformations of determinantal processes. Direct information on the characteristic polynomials of our processes of interest can be obtained from formulas from [@baikdeiftstrahov], [@fyodorovstrahov1] or [@fyodorovstrahov2]. For instance, our results concerning the Charlier ensemble were used in [@bertolaruzza] in order to compute the characteristic polynomial of the discrete Bessel point process (which describes the poissonized Plancherel measure, see section [\[sec3\]](#sec3){reference-type="ref" reference="sec3"} below) and in connection with the Gromov-Witten theory of $\mathbb{P}^1$ ([@bertolaruzza], Proposition 1.4).\
On the other hand, the formalism of Christoffel deformations of orthogonal polynomial ensembles englobes the theory of Palm measures of the latter, see Proposition [\[proppalm\]](#proppalm){reference-type="ref" reference="proppalm"} below. Roughly speaking, the Palm measure of a given point process is the same point process conditioned to have particles at specific points. Our results thus provide new explicit and simple formulas for the Palm measures of the examples we are intersted in.

An eloquent example is the one of the Totally Asymmetric Exclusion Process (TASEP) with initial wedge condition, which we now informally describe. We put independent exponential clock at each site $x \in \mathbb{Z}$, and at time $t=0$, we put particles on the whole semi-axis $\mathbb{Z}_{< 0}$. When a clock ring, the correponding particle moves to the site directly to the right of it, if this site is not occupied, and do not move else. A picture of this process at any time $t \geq 0$ is precisely the image of the poissonized Plancherel measure with parameter $t$ by the map $$\begin{aligned}
\lambda \mapsto \{ \lambda_i - i , \hspace{0.1cm} i=1,2,... \},
\end{aligned}$$ see for example [@borodingorin] and references therein. Theorem [\[thmpalmbessel\]](#thmpalmbessel){reference-type="ref" reference="thmpalmbessel"} thus gives a description of the TASEP with \"frozen\" sites, i.e. sites which must always be occupied, see Theorem [\[thmpalmbessel\]](#thmpalmbessel){reference-type="ref" reference="thmpalmbessel"} and remark [\[remtasep\]](#remtasep){reference-type="ref" reference="remtasep"} below.

In Theorem [\[thmpalmzmeas\]](#thmpalmzmeas){reference-type="ref" reference="thmpalmzmeas"}, we give new and compact formulas for the Palm measures of the $z$-measures.\
Our results also connect with those of [@bufetovbessel] and [@bufetovolshanski] (see also [@bufetovquasisymmetries]). In these papers, the author shows that conditioning at different points leads to equivalent point processes and that the Radon-Nikodym derivatives are explicitly given by regularized multiplicative functionals, analogous to the one given by Christoffel deformations.\

The $z$-measures on partitions were introduced in [@bodist] in order to describe the harmonic analysis of the infinite symmetric group. One of their interset indeed lies in the fact that they constitute a coherent system of measures on the Young graph. However, we were not able to prove whether the Christoffel deformations of the $z$-measures we introduce constitute a coherent system or not, but we believe that the study of their characteristic polynomial and conditional measures is of interest.

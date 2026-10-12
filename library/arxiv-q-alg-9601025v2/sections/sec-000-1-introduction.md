---
doc_id: arxiv-q-alg-9601025v2
doc_title: "arXiv:q-alg/9601025v2 25 Mar 1996"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 9601025v2.pdf
source_sha256: 369b0a1a92ce67a8
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 1.0
---
Many known knot and link invariants, including Alexander [@A] and Jones [@J] polynomials, can be obtained from $R$-matrices, solutions to the Yang-Baxter equation (YBE) [@Y; @B1]. Remarkably, many $R$-matrices in turn appear in quantum 3-dimensional Chern-Simons (CS) theory as partition functions of a 3-manifold with boundary, and with properly chosen Wilson lines [@W1]. The corresponding knot invariant acquires an interpretation in terms of a meanvalue of a Wilson loop. Note, that the quantum CS theory is an example of the topological quantum field theory (TQFT) defined axiomatically in [@At].

Thurston in his theory of hyperbolic 3-manifolds [@Th] introduces the notion of a hyperbolic knot: a knot that has a complement that can be given a metric of negative constant curvature. The volume of the complement in this metric appears to be a topological invariant, called the hyperbolic volume of a knot [@Th; @AHW; @Ad]. In principle, there should exist a quantum generalization of this invariant for the following reason.

Consider Euclidean quantum 2+1 gravity with a negative cosmological constant, which is the CS theory with a non-compact gauge group [@W2], and calculate the partition function of a hyperbolic knot's complement. The result would be a topological invariant, and the classical limit in the leading order would reproduce the hyperbolic volume of the complement. Unfortunately, quantum 2+1 gravity in its present formulation can not yet be used as a computational tool for this invariant.

The hyperbolic volume of ideal tetrahedra in three-dimensional hyperbolic space can be expressed in terms of Lobachevsky's function, which is the imaginary part of Euler's dilogarithm [@M]. Therefore, it is natural to expect, that the quantum dilogarithm of [@FK; @F1; @F2] can lead to a generalized (deformed) notion of the hyperbolic volume.

In [@K1; @K2] a link invariant, depending on a positive integer parameter $N$, has been defined via 3-dimensional interpretation of the cyclic quantum dilogarithm [@FK; @BR], see also [@BB; @KMS]. The construction can be considered as an example of the simplicial (combinatorial) version of the 3-dimensional TQFT [@TV]. In this paper we argue that this invariant is in fact a quantum generalization of the hyperbolic volume invariant. Namely, let $\langle L\rangle$ be the value of the invariant on a hyperbolic knot or link $L$ in three-sphere. We study the "classical" limit $N\to \infty$ of this invariant on particular examples of $L$, and show that for hyperbolic knots its absolute value grows exponentially, with the growth rate being given by the hyperbolic volume of the knot complement: []{#main label="main"} 2\|L\|\~N V(L), N, where $V(L)$ is the hyperbolic volume of $L$'s complement in $S^3$. Formula ([\[main\]](#main){reference-type="ref" reference="main"}) is in agreement with the expected classical limit of Euclidean quantum 2+1 gravity with a negative cosmological constant [@W2]. It is thus possible that the simplicial TQFT, defined in terms of the cyclic quantum dilogarithm, can be associated with quantum 2+1 dimensional gravity.

# The quantum invariant for three hyperbolic knots {#sec1}

Let $\omega$ be a primitive $N$-th root of unity. Throughout this paper we will work with the following choice for this root: =(2i/N). The result of calculation of the link invariant from papers [@K1; @K2] for three simplest hyperbolic knots reads: []{#4_1 label="4_1"} \_1=\_k\|()\_k\|\^2,(\"figure-eight\" knot), []{#5_2 label="5_2"} \_2=\_kl\^-k(l+1), []{#6_1 label="6_1"} \_1=\_k+lm \^(m-k-l)(m-k+1), where the summation variables run over $\{0,\ldots,N-1\}$; ()\_k=\_j=1\^k(1-\^j),k=0,...,N-1; and the asterisk means the complex conjugation. Strictly speaking only $N$-th powers of these quantities are invariants.

Note that the simplest case $N=2$ is related to a particular value of the Alexander polynomial $\Delta_L(t)$: \|L\|=\_L(-1),N=2. In the next section we study another extreme case $N\to\infty$.

---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
toc_source: outline
doc_brief: "KPZ limit theorems — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
Introduction
The KPZ universality is concerned with, among others, one-dimensional interacting particle systems, 1+1
random growth, and two-dimensional directed polymers. These models deﬁne height functions h(x, t), two-
dimensional random ﬁelds, where x represents the one-dimensional spatial position and t the time.
A
height function encodes the integrated current for interacting particle systems, the height for random growth
models, and the free energy for directed polymer models. See Section 2 for an example. The KPZ universality
conjecture is that for a large class of models, the scaled height function
hT (γ, τ) = h(γT 2/3, τT) −c(T)
T 1/3
(1.1)
converges, up to scaling factors, to a model-independent universal 2d random ﬁeld, which is called the KPZ
ﬁxed point. Here c(T) is a non-random term determined by the macroscopic limit of the height function.
Since the height, position, and time scale as T 1/3, T 2/3, and T, respectively, we say that (1.1) is a 1:2:3 scaled
height function. We also say that a KPZ limit theorem holds if a 1:2:3 scaled height function converges in
any suitable sense for the problem at hand.
Several physics papers [45,50,59,89] conjectured the 1:2:3 scale for various models in the mid-1980s. One
of them is the paper [59] of Kardar, Parisi, and Zhang on a nonlinear stochastic partial diﬀerential equation,
now called the KPZ equation, from which the term KPZ universality is derived. These papers were followed
by extensive research in the physics community. However, it remained unknown, even on a conjectural level,
what the limit should be.
The situation changed in 1999 with the publication of the paper [6] by Baik, Deift, and Johansson, in
which the authors considered the longest increasing subsequence problem of random permutations. This
problem is equivalent to the zero-temperature free energy of a directed polymer model. The paper proved
that the one-point distribution of an analog of the height function converges in distribution. See Theorem
3.1 below. Moreover, the authors found the limiting distribution explicitly, which turned out to be the
Tracy-Widom distribution from random matrix theory. This connection between the KPZ universality and
∗Department of Mathematics, University of Michigan, Ann Arbor, MI, 48109, USA, baik@umich.edu
1
arXiv:2206.14086v3  [math.PR]  20 Jul 2022
· · ·
· · ·

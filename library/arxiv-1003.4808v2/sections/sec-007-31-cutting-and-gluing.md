---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-007-31-cutting-and-gluing
section_title: "Cutting and gluing"
section_number: 3.1
pages: 15-17
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 1.0
doc_brief: "Quantum Field Theory and the Volume Conjecture — 15 sections: Front matter; Preliminaries; The many dimensions of the volume"
---
[]{#sec:cut label="sec:cut"}

In its more mathematical incarnation, a 3-dimensional TQFT can be thought of as a functor $Z$ that assigns

$$\begin{array}{c@{\qquad}c@{\qquad}c}
 \text{closed 3-manifold $M$} & \leadsto & \text{number $Z(M)$} \\
 \text{closed 2-manifold $\Sigma$} &\leadsto & \text{vector space $Z(\Sigma)$} \\
 \text{closed 1-manifold $S^1$} &\leadsto & \text{category $Z(S^1)$} \\
 \text{point $p$} &\leadsto & \text{2-category $Z(p)$}\,.
\end{array}$$

For our applications to Chern-Simons theory, we will really only need the top two levels $Z(M)$ and $Z(\Sigma)$. The finer structure of categories and 2-categories has recently been explored in *e.g.* [@Freed-TQFT].

![Hilbert space assigned to a surface $\Sigma$ and partition function assigned to a three-manifold $M$ in TQFT.](TQFT){#fig:TQFT width="5.5in"}

If a 3-manifold $M$ has a boundary $\Sigma = \partial M$, the object $Z(M)$ is no longer a number, but an element of the vector space $Z(\Sigma)$ assigned to the boundary, as shown in Figure [1](#fig:TQFT){reference-type="ref" reference="fig:TQFT"}. This vector space is in fact a Hilbert space, so let us denote it as ${\cal H}_\Sigma = Z(\Sigma)$. At the top two levels, the TQFT must then satisfy the following axioms of Atiyah and Segal (*cf.* [@atiyah-1990]).

1.  A change of orientation $\Sigma\to - \Sigma$ dualizes the Hilbert space, ${\cal H}_{-\Sigma}={\cal H}_\Sigma^*$ .

2.  For a boundary consisting of multiplet disjoint components, ${\cal H}_{\Sigma_1 \sqcup \Sigma_2} = {\cal H}_{\Sigma_1}\otimes{\cal H}_{\Sigma_2}\,.$

3.  Using the first two axioms, we see that for a manifold $M$ with $\partial M = (-\Sigma_1)\sqcup\Sigma_2$ one obtains a map $Z(M)\,:\;{\cal H}_{\Sigma_1}\to{\cal H}_{\Sigma_2}$. Then, given a 3-manifold $N$ that can be written as $N = M_1\cup_{\Sigma_2} M_2$, with $\partial M_1 = (-\Sigma_1)\sqcup \Sigma_2$ and $\partial M_2 = (-\Sigma_2)\sqcup \Sigma_3$ as illustrated below, the functoriality property $Z(N) = Z(M_2)\circ Z(M_1)$ must hold.\
    $$\includegraphics[width=3.5in]{TQFTf} \nonumber$$

4.  For the empty boundary, ${\cal H}_{\Sigma=\oslash}={\mathbb{C}}$ .

5.  For $M=\Sigma\times I$, the map $Z(M)\,:{\cal H}_\Sigma\overset{\rm id}{\to}{\cal H}_\Sigma$ is just the identity.

Using these axioms, the partition function $Z(M)$ of any three-manifold, with or without boundary, may be constructed by cutting the manifold into pieces and taking inner products in boundary Hilbert spaces to glue the pieces back together. For this purpose, it is often convenient to know how the mapping class group of a surface $\Sigma$ acts on ${\cal H}_\Sigma$, in order to properly identify the Hilbert spaces on two sides of a gluing.

There are many examples of three-dimensional TQFT, differing essentially in the definitions of the boundary Hilbert spaces ${\cal H}(\Sigma)$, as well as the action of the mapping class groups on these spaces. In the case of Chern-Simons theory with gauge group $G$ (whether compact or complex), ${\cal H}_\Sigma$ is a quantization of the space ${\cal M}_{{\rm flat}} (G;\Sigma)$ of flat $G$-connections on $\Sigma$:

$${\cal M}_{{\rm flat}} (G;\Sigma) = \left\{\begin{array}{r|l}
  \text{connections ${\cal A}$ on principal} & \multirow{2}{*}{$F_{\cal A}=0$} \\
  \text{$G$-bundle over $\Sigma$} &
  \end{array}\right\}\Big/ \text{gauge equivalence}\,.$$

(Recall that a connection is flat if the curvature $F_{\cal A}=d{\cal A}+{\cal A}\wedge {\cal A}$ vanishes.) The precise meaning of the quantization used to obtain ${\cal H}_\Sigma$ from ${\cal M}_{{\rm flat}} (G;\Sigma)$ will be the subject of Section [\[sec:quant\]](#sec:quant){reference-type="ref" reference="sec:quant"}. It depends on the level $k=i\pi\hbar^{-1}$ (or coupling constant) of Chern-Simons theory, the only adjustable parameter in the TQFT.

In Chern-Simons theory, one is also interested in colored knots or links embedded in 3-manifolds. Suppose for the moment that we have compact Chern-Simons theory with gauge group $G$ and level $k\in {\mathbb{Z}}$. The intersection of a knot and a boundary surface $\Sigma$ shows up as a puncture on $\Sigma$ and TQFT would assign the boundary $S^1$ surrounding this puncture in $\Sigma$ the category of representations of the affine Lie algebra $\widehat{\frak g}_{k}$,

$$Z(S^1) \sim \text{reps of $\widehat{\frak g}_k$}\,.$$

The definition of the Hilbert space ${\cal H}(\Sigma)$ of a multiple-punctured $\Sigma$ would then have to be altered to include the space of homomorphisms between such representations. For our purposes, however, the complication of knots can be conveniently avoided by *excising the knots and trading representations that color the knots for boundary conditions on knot complements*.

This trick was already mentioned in Section [\[sec:links\]](#sec:links){reference-type="ref" reference="sec:links"}. In the language of TQFT, it can be described the following way. Suppose that we have a knot $K$ colored by representation $R_\lambda$ inside the closed manifold $M$. We cut out a tubular neighborhood $N_K$ of the knot, so that

$$M = (M\backslash N_K)\cup_{T^2}N_K\,,\qquad N_K\simeq D^2\times S^1\,.$$

Of course, $M\backslash N_K\simeq M\backslash K$ is just the knot complement, and $N$ is topologically a 2-disk times $S^1$ that contains the knot running through its center. The partition functions $Z(M\backslash K;u;\hbar)$ and $Z(N_K;R_\lambda;\hbar)$ are both vectors in the boundary Hilbert space ${\cal H}_{T^2}$; therefore, by TQFT,

$$Z(K\subset M;R_\lambda;\hbar) = \langle\, Z(M\backslash K;u;\hbar) \,,\, Z(N_K;R_\lambda;\hbar)\,\rangle_{{\cal H}_{T^2}}\in{\mathbb{C}}\,.$$

As we will see in the next section, the Hilbert space ${\cal H}_{T^2}$ can be understood as a space of functions of the variable $u$ that describes the holonomy of flat connections around the meridian of $T^2$ (as in Figure [\[fig:lm\]](#fig:lm){reference-type="ref" reference="fig:lm"}a). The crucial fact, then, is that the vector $Z(N;R_\lambda;\hbar)\in {\cal H}_{T^2}$ is only supported on the part of this space with

$$e^u = {\rm Hol}(\mu) = \exp\left(i\pi \frac{\lambda^*+\rho^*}{k} \right)\,. \label{holagain}$$

In other words, $Z(N;R_\lambda;\hbar)$ acts like a delta-function $\delta(u-i\pi \frac{\lambda^*+\rho^*}{k})$. Therefore, coloring by $R_\lambda$ is equivalent to restricting $Z(M\backslash K)$ to an appropriate one-dimensional subspace of ${\cal H}_{T^2}$:

$$Z(K\subset M;R_\lambda;\hbar)
= Z(M\backslash K;u;\hbar)\big|_{u=i\pi \frac{\lambda^*+\rho^*}{k}} \, \in\, {\mathbb{C}}\,. \label{uR}$$\
Our plan now is to give a complete description of ${\cal H}_{T^2}$ and to explain how the elements $Z(M\backslash K) \in {\cal H}_{T^2}$ may be calculated for knot complements, in the case of Chern-Simons theory with both compact and complex gauge groups. (The extension to links is straightforward and will not be mentioned explicitly hereafter.) This will first require a brief discussion of quantization.

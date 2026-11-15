---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-017-24-explicit-matrices
section_title: "Explicit matrices"
section_number: 2.4
pages: 13-15
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.916
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:explicit matrices label="sub:explicit matrices"}

Although the definition of $\mathfrak{z}$ and $\mathrm{FHilb}_n(\mathbb{C}^2)$ is given by allowing the Borel subgroup to vary, to keep the presentation explicit we will henceforth fix it to be $B=B_0$. Therefore, points of the flag Hilbert scheme will be triples: $$\label{eqn:triple matrices}
X = \left( \begin{array}{cccc}
x_1 & 0 & 0 & 0 \\
* & x_2 & 0 & 0 \\
* & * & ... & 0 \\
* & * & * & x_{n} \end{array} \right), \quad Y = \left( \begin{array}{cccc}
y_1 & 0 & 0 & 0 \\
* & y_2 & 0 & 0 \\
* & * & ... & 0 \\
* & * & * & y_{n} \end{array} \right), \quad v = \left( \begin{array}{cccc}
1 \\
0 \\
0 \\
0 \end{array} \right)$$ such that $[X,Y]=0$, and the vectors $\{X^aY^bv\}_{a,b\geq 0}$ generate the space $V$. This latter condition implies that the first entry of $v$ must be non-zero, so we may use the $B=B_0$ action to fix $v$ as in equation [\[eqn:triple matrices\]](#eqn:triple matrices){reference-type="eqref" reference="eqn:triple matrices"}. Therefore, we will abuse notation and re-write [\[eqn:def flag hilbert\]](#eqn:def flag hilbert){reference-type="eqref" reference="eqn:def flag hilbert"} as: $$\label{eqn:defflaghilbert1}
\mathrm{FHilb}_n(\mathbb{C}^2) = \Big\{(X,Y,v), \ X,Y \text{ lower triangular}, \ [X,Y]=0, \ v \text{ cyclic} \Big\}/B$$ In this language, the map: $$\mathrm{FHilb}_n(\mathbb{C}^2) \stackrel{\rho}\longrightarrow \mathbb{C}^{2n}$$ is given by taking the joint eigenvalues of the matrices $X$ and $Y$. Therefore, we conclude that: $$\label{eqn:defflaghilbert2}
\mathrm{FHilb}_n(\mathbb{C}) = \Big\{(X,Y,v) \text{ as in \eqref{eqn:defflaghilbert1}}, \ \ \ Y \text{ strictly lower triangular} \Big\}$$ $$\label{eqn:defflaghilbert3}
\mathrm{FHilb}_n(\mathrm{point}) = \Big\{(X,Y,v) \text{ as in \eqref{eqn:defflaghilbert1}}, \ X , Y \text{ strictly lower triangular} \Big\}$$ We may use the descriptions [\[eqn:defflaghilbert1\]](#eqn:defflaghilbert1){reference-type="eqref" reference="eqn:defflaghilbert1"}--[\[eqn:defflaghilbert3\]](#eqn:defflaghilbert3){reference-type="eqref" reference="eqn:defflaghilbert3"} to obtain the following estimates of the dimensions of flag Hilbert schemes: $$\dim \mathrm{FHilb}_n(\mathbb{C}^2) \geq \dim \left(\text{affine space of }(X,Y,v)\right) - \#\left(\text{equations }[X,Y]=0\right) - \dim B =$$ $$\label{eqn:expdim1}
= n^2+2n - \frac {n(n-1)}2 - \frac {n(n+1)}2 = 2n \ =: \ \mathrm{exp \ dim \ }\mathrm{FHilb}_n(\mathbb{C}^2)$$ The right hand side stands for "expected (or virtual) dimension\". Similarly, we have: $$\label{eqn:expdim2}
\dim \mathrm{FHilb}_n(\mathbb{C}) \geq n \ =: \ \mathrm{exp \ dim \ }\mathrm{FHilb}_n(\mathbb{C})$$ $$\label{eqn:expdim3}
\dim \mathrm{FHilb}_n(\mathrm{point}) \geq n-1 \ =: \ \mathrm{exp \ dim \ }\mathrm{FHilb}_n(\mathrm{point})$$ The reason why the expected dimension in [\[eqn:expdim3\]](#eqn:expdim3){reference-type="eqref" reference="eqn:expdim3"} is $n-1$ rather than 0 is that when $X$ and $Y$ are both strictly lower triangular matrices, the commutator $[X,Y]=0$ is not only strictly lower triangular, but has the first sub-diagonal equal to zero by default. Therefore, the first sub-diagonal entries are $n-1$ equations that need not be placed on $\mathrm{FHilb}_n(\mathrm{point})$.

::: example
[]{#ex:not lci label="ex:not lci"}

If the inequalities in [\[eqn:expdim1\]](#eqn:expdim1){reference-type="eqref" reference="eqn:expdim1"}--[\[eqn:expdim3\]](#eqn:expdim3){reference-type="eqref" reference="eqn:expdim3"} were equalities, then we would conclude that flag Hilbert schemes were local complete intersections. However, this is not the case. We give an example of how the bound in [\[eqn:expdim3\]](#eqn:expdim3){reference-type="eqref" reference="eqn:expdim3"} can fail, which we learned from Ian Grojnowski. Let $n=10$, and consider the affine space of matrices $X,Y$ which are lower triangular, and have zero blocks of sizes $1,2,3$ and $4$ on the diagonal: $$\label{eqn:big matrix}
X,Y = \left( \begin{array}{cccccccccc}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
* & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
* & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
* & * & * & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
* & * & * & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
* & * & * & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
* & * & * & * & * & * & 0 & 0 & 0 & 0 \\
* & * & * & * & * & * & 0 & 0 & 0 & 0 \\
* & * & * & * & * & * & 0 & 0 & 0 & 0 \\
* & * & * & * & * & * & 0 & 0 & 0 & 0 \\
\end{array} \right)$$ The dimension of the affine space consisting of triples $(X,Y,v)$ equals $35+35+10 = 80$. Since the commutator $[X,Y]=0$ must have the $2\times 1$, $3\times 2$ and $4\times 3$ blocks under the diagonal equal to zero by default, the number of equations we need to impose is only $15$. Taking into account the fact that the Borel subgroup has dimension $55$, we conclude that: $$\dim \mathrm{FHilb}_{10}(\mathrm{point}) \geq 80 - 15 - 55 = 10 > 9 = \mathrm{exp \ dim \ }\mathrm{FHilb}_{10}(\mathrm{point})$$ We may translate this example in terms of flags of ideals inside $\mathbb{C}[x,y]$. Let $d=4$, $n = \binom{d+1}{2}$, and $\mathfrak{m} \subset \mathbb{C}[x,y]$ be the maximal ideal of the origin, and let us consider the locus of flags: $$L = (I_0\supset I_1\supset \ldots \supset I_{n}) \subset \mathrm{FHilb}_{n}(\mathrm{point})$$ such that: $$\label{eqn:weird ideal}
I_{\binom{k+1}{2}}=\mathfrak{m}^{k},\quad k = 0,\ldots,d.$$ By the defining property of the maximal ideal $\mathfrak{m}$, for each $k \in \{0,...,d-1\}$ the flag of ideals: $$\mathfrak{m}^{k}\supset I_{\binom{k+1}{2}+1}\supset \ldots I_{\binom{k+2}{2}-1} \supset \mathfrak{m}^{k+1}$$ can be chosen as an arbitrary complete flag of vector subspaces in $\mathfrak{m}^{k}/\mathfrak{m}^{k+1}\simeq \mathbb{C}^{k+1}$. Since the dimension of the corresponding flag variety is $\binom{k+1}{2}$, we conclude that: $$\dim L = \sum_{k=0}^{d-1}\binom{k+1}{2}=\binom{d+1}{3} \gg n-1 = \mathrm{exp \ dim \ }\mathrm{FHilb}_n(\mathrm{point})$$ as $d$ becomes large (although the inequality is strict as soon as $d\geq 4$). This construction also shows that the stratum $L$ is non-empty, since there always exist flags of ideals with the property [\[eqn:weird ideal\]](#eqn:weird ideal){reference-type="eqref" reference="eqn:weird ideal"}, something which was not immediately apparent from the matrix construction [\[eqn:big matrix\]](#eqn:big matrix){reference-type="eqref" reference="eqn:big matrix"}.
:::

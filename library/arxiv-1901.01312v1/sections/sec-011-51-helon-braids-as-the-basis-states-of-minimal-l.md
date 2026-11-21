---
doc_id: arxiv-1901.01312v1
doc_title: "Braided fermions from Hurwitz algebras"
section_id: sec-011-51-helon-braids-as-the-basis-states-of-minimal-l
section_title: "Helon braids as the basis states of minimal left ideals of $C\ell(6)$"
section_number: 5.1
pages: 6-7
source_pdf: 1901.01312v1.pdf
source_sha256: a480da38283622d6
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 1.0
doc_brief: "Braided fermions from Hurwitz algebras — Some curious structural similarities between a recent braid- and Hurwitz algebraic description of the unbroken internal symmetries for a single generations of"
---
[]{#braidedbasiststates label="braidedbasiststates"}

In [@Bilson-Thompson2009] it was shown that braiding of ribbons and twisting of ribbons within three strand ribbon braids are interchangeable, and that any orientable[^1] ribbon braid can always be written as a vector $[a,b,c]$ where $a,b,c$ are all integers or all half integers, specifying the number of twists on each ribbon. This vector is a topological invariant. In particular, the generators of $B^c_3$ can be written as twist vectors as follows: $$\begin{aligned}
\label{braidgenerators}
\sigma_1\rightarrow \left[ 1/2,1/2,-1/2\right] ,\qquad \sigma_2\rightarrow \left[ -1/2,1/2,1/2\right],\qquad \sigma_3\rightarrow \left[ 1/2,-1/2,1/2\right],
\end{aligned}$$ with the inverse braid generators giving the negatives of these twist vectors. Care must be taken to account for the permutations induced by braidings when systematically exchanging braiding for twisting [@Bilson-Thompson2009]. It can likewise be shown that any orientable ribbon braid may be manipulated such that all the twisting of the ribbons is removed, exchanged for braiding [@gresnigt2018knotted]. One may write this as $[0,0,0]B=B[0,0,0]$ where $B\in B_3^c$.

Because the ribbon braids in the Helon model are orientable, they can be written purely as braid words in $B_3^c$. Letting $B=(\sigma_2^{-1}\sigma_1)$, we have for example $$\begin{aligned}
\nonumber\nu &\rightarrow&  [0,0,0]B,\;\;e^+\rightarrow  [1,1,1]B=[0,0,0](\sigma_2\sigma_3)(\sigma_3\sigma_1)(\sigma_1\sigma_2)B,\\
\bar{d}^r &\rightarrow & [0,0,1]B=[0,0,0](\sigma_1\sigma_2)B,\;\;u^r \rightarrow  [0,1,1]B=[0,0,0](\sigma_2\sigma_3)(\sigma_3\sigma_1)B.
\label{positivestates}
\end{aligned}$$ If one now makes the identifications $$\begin{aligned}
\label{alphadagger}
(\sigma_1\sigma_2)\mapsto\alpha_1^{\dagger},\;\;(\sigma_3\sigma_1)\mapsto\alpha_2^{\dagger},\;\;(\sigma_2\sigma_3)\mapsto\alpha_3^{\dagger},\;\;\textrm{together\;with}\;\; \sigma_2^{-1}\sigma_1\mapsto\omega\omega^{\dagger},
\end{aligned}$$ and substitutes into the braid only representations of fermions, such as in equation ([\[positivestates\]](#positivestates){reference-type="ref" reference="positivestates"}), then the minimal left ideal $S^u$ of $C\ell(6)$, as in eqn., ([\[ideal\]](#ideal){reference-type="ref" reference="ideal"}) is recovered[^2]. One may similarly reconstruct the second ideal for antiparticles in a similar manner. More details of this construction are given in [@gresnigt2018braids].

Notice that if one is only concerned with the unbroken symmetries, and hence ignores the underlying braiding in Helon model braids (that is, ignore $\sigma_2^{-1}\sigma_1$ and instead take $\omega\omega^{\dagger}=I$ where $I$ is the identity braid), then one of the ideals consist entirely of positive braids (that is braid words made up of only braid generators), and the other ideal consists of negative braids made up entirely of inverse braid generators.

[^1]: Orientable here meaning that the surface bounded by the ribbon braid is orientable.

[^2]: The action of the basis states in the ideal is on the identity $[0,0,0]$ from left to right. Thus for example, $$\begin{aligned}
    \nonumber u^g &\rightarrow & [1,1,0](\sigma_2^{-1}\sigma_1)=[0,0,0](\sigma_1\sigma_2)(\sigma_2\sigma_3)(\sigma_2^{-1}\sigma_1)=[0,0,0]\alpha_1\alpha_3\omega^{\dagger}\omega.
    \end{aligned}$$

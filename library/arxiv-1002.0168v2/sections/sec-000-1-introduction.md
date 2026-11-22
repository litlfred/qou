---
doc_id: arxiv-1002.0168v2
doc_title: "Non-cyclotomic fusion categories Introduction"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1002.0168v2.pdf
source_sha256: c95d5d193d57b097
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.996
doc_brief: "Non-cyclotomic fusion categories Introduction — Etingof, Nikshych and Ostrik ask in [7, §2] if every fusion category can be completely deﬁned over a cyclotomic ﬁeld."
---
In [@MR2183279 §2], Etingof, Nikshych and Ostrik ask if every fusion category over the complex numbers can be defined over a cyclotomic field. More precisely, does every fusion category over $\Complex$ have a complete rational form over a cyclotomic field? (See Section [\[sec:background\]](#sec:background){reference-type="ref" reference="sec:background"} for definitions and examples of the key notions "rational form\" and "complete rational form.\")

Their question is motivated by the following results.

-   The representation category of any finite group has a complete rational form over a cyclotomic field. (This is a classical result of Brauer's, see [@MR0450380 §12.3].)

-   The semisimplified representation category of any quantum group at a root of unity has a complete rational form over a cyclotomic field. (This follows from the usual construction of Weyl modules.)

-   The Frobenius-Perron dimension of any object in a fusion category is a cyclotomic integer [@MR2183279].

-   The global dimension of a fusion category is a cyclotomic integer [@MR2183279].

-   The entries of the $S$-matrix of a modular category lie in a cyclotomic field [@MR1266785; @MR1120140].

We answer this question in the negative.

::: thm
[]{#thm:noncyclotomic label="thm:noncyclotomic"} The principal even part of the Haagerup subfactor and the principal even part of the extended Haagerup subfactor are fusion categories which do not have a complete rational form over any cyclotomic field.
:::

We hope that this result will eventually allow a more robust technique for establishing the "exotic\" nature of these fusion categories. No construction that preserves cyclotomicity can produce these fusion categories starting from groups or quantum groups. Alternately this result might suggest new techniques for constructing these fusion categories.

Let $\cH_0$ and $\cH_1$ be the Haagerup [@MR1686551; @0902.1294] and extended Haagerup [@0909.4099] subfactors which are the unique subfactors with the following principal graph pairs. $$\begin{aligned}
\Gamma(\cH_0) & = \left \{ \mathfig{0.25}{haagerup}, \mathfig{0.25}{dual-haagerup} \right \} \\
\Gamma(\cH_1) & = \left \{ \mathfig{0.4}{EH}, \mathfig{0.4}{dual-EH} \right \}
\end{aligned}$$

Given a subfactor $A \subset B$ there are two tensor categories $\cS^p$ and $\cS^d$ (consisting of certain $A$-$A$ bimodules and certain $B$-$B$ bimodules respectively) called the principal even part and dual even part. If the subfactor is finite depth then $\cS^p$ and $\cS^d$ are fusion categories over $\Complex$. We will be looking at the fusion categories $\cH_\ell^p$ and $\cH_\ell^d$ for $\ell \in \{0,1\}$.

Denote by $D_0 = \frac{5+\sqrt{13}}{2} \simeq 4.30278$ and $D_1 = \frac{8}{3}+\frac{2}{3} \operatorname{Re} \sqrt[3]{\frac{13}{2} \left(-5-3 i \sqrt{3}\right)} \simeq 4.3772$ the Jones indices of $\cH_0$ and $\cH_1$. Fix $$\begin{aligned}
\lambda_0 & = i \sqrt{\frac{-1+\sqrt{13}}{6}} \simeq 0.658983 i \\
\intertext{and}
\lambda_1& = \sqrt{-\frac{1}{5}+2 \operatorname{Re} \sqrt[3]{\frac{117-  65 i \sqrt{3}}{2250}}} \simeq 0.648585 i.
\end{aligned}$$

Let $\zeta_m$ denote the primitive $m$th root of unity $\exp(2\pi i/m)$. Note that $$\begin{aligned}
D_0 & = 2 -\zeta_{13}^{2} -\zeta_{13}^5 -\zeta_{13}^6 -\zeta_{13}^7-\zeta_{13}^8-\zeta_{13}^{11}\\
D_1 & = 3+ \zeta_{13}^2  + \zeta_{13}^3 + \zeta_{13}^{10} +  \zeta_{13}^{11}
\end{aligned}$$ so $D_\ell \in \Rational(\zeta_{13})$ while $\lambda_\ell$ is not cyclotomic. In fact, $\Rational(\lambda_\ell)$ is not Galois. The Galois group of the Galois closure of $\Rational(\lambda_0)$ is the dihedral group of order $8$, and the Galois group of the Galois closure of $\Rational(\lambda_1)$ is $\Integer/2\Integer \wr \Integer/3\Integer \cong \Integer/2\Integer \times A_4$.

::: thm
[]{#thm:detailed label="thm:detailed"} The following statements hold for $\ell = 0,1$.

1.  []{#pa:construct label="pa:construct"} The even parts $\cH_\ell^p$ and $\cH_\ell^d$ each have a (possibly incomplete) rational form over $\Rational(D_\ell)$.

2.  []{#pa:dualprojs label="pa:dualprojs"} The dual even part $\cH_\ell^d$ has a complete rational form over $k$ if and only if $D_\ell \in k$.

3.  []{#pa:principalprojs label="pa:principalprojs"} The principal even part $\cH_\ell^p$ has a complete rational form over $k$ if and only if $\lambda_\ell \in k$.

4.  []{#pa:center label="pa:center"} The Drinfel'd center $Z(\cH_0^p) \cong Z(\cH_0^d)$ has a complete rational form over $k$ as a ribbon fusion category if and only if $\zeta_{39} \in k$.
:::

Theorem [\[thm:noncyclotomic\]](#thm:noncyclotomic){reference-type="ref" reference="thm:noncyclotomic"} follows immediately from part [\[pa:principalprojs\]](#pa:principalprojs){reference-type="ref" reference="pa:principalprojs"} of Theorem [\[thm:detailed\]](#thm:detailed){reference-type="ref" reference="thm:detailed"}. Part 4 is of interest because it means these results do not exclude the possibility that every braided fusion category is defined over a cyclotomic field. We prove part [\[pa:construct\]](#pa:construct){reference-type="ref" reference="pa:construct"} and the "if\" direction of parts [\[pa:dualprojs\]](#pa:dualprojs){reference-type="ref" reference="pa:dualprojs"} and [\[pa:principalprojs\]](#pa:principalprojs){reference-type="ref" reference="pa:principalprojs"} in Section [\[sec:construction\]](#sec:construction){reference-type="ref" reference="sec:construction"}. We prove the "only if\" direction of parts [\[pa:dualprojs\]](#pa:dualprojs){reference-type="ref" reference="pa:dualprojs"} and [\[pa:principalprojs\]](#pa:principalprojs){reference-type="ref" reference="pa:principalprojs"} in Section [\[sec:noncyclotomic\]](#sec:noncyclotomic){reference-type="ref" reference="sec:noncyclotomic"}. We prove part [\[pa:center\]](#pa:center){reference-type="ref" reference="pa:center"} in Section [\[sec:center\]](#sec:center){reference-type="ref" reference="sec:center"}.

The main technique in this paper is to show that, in the context of fusion categories associated to 3-supertransitive subfactors, the (correctly normalized) "twisted moments\" of any $\Rational$-linear combination of projections gives an element of the base field of any complete rational form. These twisted moments can be computed using techniques from Jones's preprint [@quadratic]. In the construction of the Haagerup subfactor by Peters [@0902.1294], the moments and twisted moments of the "generator\" are the only scalars needed to define the subfactor. The $\lambda_\ell$ above are $\Rational(D_\ell)$ multiples of the third twisted moments of $\frac{1}{2}\left(\id_P-\id_Q\right)$ (where $P$ and $Q$ are the two simple objects immediately after the branch).

There is a third subfactor with index in the interval $(2, 3+\sqrt{3})$ called the Asaeda-Haagerup subfactor [@MR1686551]. Our techniques do not give an obstruction to cyclotomicity for either of the fusion categories coming from the Asaeda-Haagerup subfactor, because the analogous moments and twisted moments are cyclotomic. However, since there is not yet a construction of the Asaeda-Haagerup planar algebra following the Jones-Peters approach [@quadratic; @0902.1294; @0909.4099], the lack of obstruction does not guarantee that the even parts of the Asaeda-Haagerup subfactor are cyclotomic.

The authors would like to thank Emily Peters for teaching us about the Haagerup planar algebra and Pavel Etingof for encouraging us to write this paper. We'd like to thank Victor Ostrik, Ben Webster, and Pasquale Zito for suggesting arguments which we used to improve Section [\[sec:center\]](#sec:center){reference-type="ref" reference="sec:center"}. (For Pasquale Zito's suggestions, see Math Overflow <http://mathoverflow.net/questions/17641/>.) In addition we would also like to thank Stephen Bigelow, Vaughan Jones, Dmitri Nikshych, and Dylan Thurston for helpful conversations. Scott Morrison was at the Miller Institute for Basic Research at UC Berkeley during this work, and Noah Snyder was supported by an NSF Postdoctoral Fellowship at Columbia University.

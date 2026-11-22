---
doc_id: arxiv-2203.06568v4
doc_title: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra"
section_id: sec-011-conclusion
section_title: "Conclusion"
section_number: null
pages: 14-15
source_pdf: 2203.06568v4.pdf
source_sha256: 256fcfb588dac554
toc_source: outline
text_source: latex
latex_prose_ratio: 0.769
latex_coverage_ratio: 0.994
doc_brief: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra — We study the upper bounds for A(n, d), the maximum size of codewords with length n and Hamming distance at least d."
---
[]{#sec:conslus label="sec:conslus"} In conclusion, we have derived generalized Schrijver semidefinite constraints by considering the split of Terwilliger algebra. Our split semidefinite constraints are a natural generalization of Schrijver's constraints since they also implied the generalized Delsarte inequalities.

By implementing a $2$-split SDP, we have improved the upper bounds for $A(18, 4)$ and $A(19, 4)$. The MATLAB programs of the SDPs in this paper can be found at:

::: center
<https://github.com/PinChiehTseng/Split_SDP_solution>
:::

We have confirmed that $A(18,4)\leq 6551$ by showing that an upper bound on the numerical error is small enough. As for $A(19,4)$, we obtain $A(19,4)\leq 13087.5$ using $n_{1} = 9$. The currently best known bound for $A(19,4)$ is $13104$. As for the error estimate, we obtained an upper bound on the numerical error as large as $215.7376$. Since this estimate is over pessimistic, it provides no information about out result. Since the solver normally returned without any warning, we believed this figure is correct. More accurate solvers could be considered.

Our split approach can be extended to other related problems. For example, one may consider an arbitrary finite field or $k$-distance SDP for arbitrary $k$. Notice that the method described in [@GMS12] with $\lvert S \rvert = 2$ has been applied to improve upper bounds for constant weight codes. Moreover, the algebra considered in [@Pol19_2] is of the form $\bigotimes_{i} \mathcal{A}_{n_{i}}$ with $\sum_{i}n_{i} = n$. The constraint $R_{s}$ for constant weight codes has been studied. We can have a similar application by adding the constraint $R'_{s}$, which potentially opens a way to strengthen the upper bounds for constant weight codes. As for the upper bounds on the size of a set with few distances or intersecting families of subsets [@MN11; @BM11], we may directly apply our method to those problems. Moreover, as Schrijver's SDP has been extended to the maximum size problem of a code in the fold of $n$-cube by Hou et al. [@HHGY20], we might have a similar extension. The idea of isometry groups might be applied to spherical codes as well.

As an example of association schemes, our method corresponds to a special case of the $m$-split property of the Hamming scheme. Thus, our method may be extended to other association schemes, which share this $m$-split property. It is an interesting research direction.

Finally, it has been shown that certain polynomial symmetric properties can be exploited to obtain additional matrix inequalities and hence improve the semidefinite programming bounds for the kissing number problem [@caluza2018improving]. It is unknown whether a similar ideas could be applied to the case of binary codes to obtain better bounds for $A(n,d)$.

# ACKNOWLEDGEMENT

We would like to thank Dion Gijswijt, Alexander Schrijver, and Hajime Tanaka for helpful discussions. We would also like to thank the anonymous referees for their valuable comments.

PCT and CYL were supported by the Ministry of Science and Technology (MOST) in Taiwan under Grant MOST110-2628-E-A49-007. WHY was supported by MOST under Grant109-2628-M-008-002-MY4.

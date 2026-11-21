---
doc_id: arxiv-0803.1227v1
doc_title: "Linear programming bounds for unitary space time codes"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 0803.1227v1.pdf
source_sha256: cf72e0fcdc7f3ddf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.994
doc_brief: "Linear programming bounds for unitary space time codes — The linear programming method is applied to the space Un(C) of uni- tary matrices in order to obtain bounds for codes relative to the"
---
Nowadays breakthrough of wireless communications has provided new and nice problems to the field of coding theory. Indeed strategic issues of MIMO communications has lead to consider coding in Grassmann and Stiefel manifolds, and also in unitary groups [@TSE]. Codes in unitary groups are useful in the context of non-coherent flat Rayleigh channel as shown in [@MARZETTA]. The performance of a unitary space-time code $\Code$ is measured (see [@ROSEN]) by two functions namely the diversity sum $\Sigma \Nu$ and the diversity product $\Pi \Nu$ : $$\begin{aligned}
 \Sigma \Nu := \frac{1}{2\sqrt{n}} \min \left \{ ||x-y||\ :
 \ x\ne y \in \Code   \right\},
 
\end{aligned}$$ $$\begin{aligned}
 \Pi \Nu := \frac{1}{2} \min \left \{ |\det(x-y)|^{\frac 1 n}\ :
 \ x\ne y \in \Code \right\}.
 
\end{aligned}$$ Here $||A||$ denotes the standard Euclidean norm of complex matrices: $||A||^2=\trace(AA^*)=\sum|A_{i,j}|^2$. A standard problem is, given a number $N$ of points in $\U_n(\C)$, to maximize the value of $\Sigma \Nu$ or of $\Pi \Nu$. Many authors have addressed this question, narrowing gaps between bounds and explicit constructions (see [@ROSEN], [@AB], [@RECITE], [@SHOKRO]). The linear programming method, which was initially developed by Philippe Delsarte in the framework of association schemes [@DELSARTE], and is a powerful method to deal with such questions, has not been applied to unitary codes before. Delsarte method was successfully adapted to the compact two-point homogeneous spaces by Kabatiansky and Levenshtein [@LEVEN] and recently to more general situations like the Grassmann codes [@CHRISTINE1], the permutation codes [@TARNANEN], the ordered codes [@BARG], [@BIERBRAUER]. Most of the situations mentioned above fit into a common framework, namely a compact group $G$ acts homogeneously on the underlying space $X$, and the representation theory of $G$ constructs a certain family of orthogonal polynomials naturally attached to $X$. Standard methods of harmonic analysis show that these polynomials hold the desired positivity property that allows for Delsarte linear programming method. This general framework is recalled in Section II, and we show in Section III that unitary codes can be treated likewise, the Schur polynomials being the associated family of orthogonal polynomials. Section IV and V present the results, both numerical and analytic, obtained by the implementation of this method. It turns out that we improve all previously known bounds concerning the diversity sum and the diversity product. Moreover it is worth pointing out that the mathod can easily be extended to more complex situations, for example a diversity function involving both $\Sigma \Nu$ and $\Pi \Nu$.\

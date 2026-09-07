---
doc_id: arxiv-0803.1227v1
doc_title: "Linear programming bounds for unitary space time codes"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 0803.1227v1.pdf
source_sha256: cf72e0fcdc7f3ddf
doc_brief: "Linear programming bounds for unitary space time codes — The linear programming method is applied to the space Un(C) of uni- tary matrices in order to obtain bounds for codes relative to the"
---
Nowadays breakthrough of wireless communications has provided n ew and nice
problems to the ﬁeld of coding theory. Indeed strategic issues of M IMO commu-
nications has lead to consider coding in Grassmann and Stiefel manifo lds, and
also in unitary groups [13]. Codes in unitary groups are useful in the c ontext
of non-coherent ﬂat Rayleigh channel as shown in [6]. The performa nce of a
unitary space-time code V is measured (see [7]) by two functions namely the
diversity sum Σ V and the diversity product Π V :
Σ V := 1
2√n min {||x − y|| : x ⁄= y ∈ V} ,
Π V := 1
2 min
{
| det(x − y)|
1
n : x ⁄= y ∈ V
}
.
Here ||A|| denotes the standard Euclidean norm of complex matrices: ||A||2 =
Trace(AA∗) = ∑ |Ai,j |2. A standard problem is, given a number N of points
in Un(C), to maximize the value of Σ V or of Π V. Many authors have addressed
this question, narrowing gaps between bounds and explicit constru ctions (see
[7], [8], [10], [11]). The linear programming method, which was initially devel-
oped by Philippe Delsarte in the framework of association schemes [4 ], and is a
powerful method to deal with such questions, has not been applied to unitary
codes before. Delsarte method was successfully adapted to the c ompact two-
point homogeneous spaces by Kabatiansky and Levenshtein [9] and recently to
more general situations like the Grassmann codes [1], the permutat ion codes
[12], the ordered codes [2], [3]. Most of the situations mentioned abov e ﬁt into a
1
common framework, namely a compact group G acts homogeneously on the un-
derlying space X, and the representation theory of G constructs a certain family
of orthogonal polynomials naturally attached to X. Standard methods of har-
monic analysis show that these polynomials hold the desired positivity p roperty
that allows for Delsarte linear programming method. This general fr amework
is recalled in Section II, and we show in Section III that unitary codes can be
treated likewise, the Schur polynomials being the associated family of orthog-
onal polynomials. Section IV and V present the results, both numer ical and
analytic, obtained by the implementation of this method. It turns ou t that we
improve all previously known bounds concerning the diversity sum an d the di-
versity product. Moreover it is worth pointing out that the mathod can easily
be extended to more complex situations, for example a diversity fun ction in-
volving both Σ V and Π V.
2 The linear programming method on homoge-
neous spaces

---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
Borel transform [1] is an important tool in the study of non-perturbative phenomena. It is used to extract
information from divergent series which typically arise in perturbative expansions. Non-perturbative partition
functions depend on extra parameters, like the choice of integration contour, this dependence seems to disappear
in perturbative expansion, but is in fact traded for divergence of the series. New parameters appear as an
ambiguity in the Borel transform. All this is well seen already in the simplest example of the exponential Borel
transform
X
r
r!·qr =
Z ∞
0
X
r
(qx)re−xdx =
Z ∞
0
e−xdx
1−qx (1)
Now, it is clear that the r.h.s. depends on the integration contour, and there is an ambiguity
I
x=q−1
e−xdx
1−qx = 2πi
q e−1/q (2)
so that the sum of divergent series is defined modulo this “instantonic” term.
This standard argument, lying in the base of entire ”resurgence theory” [2] is, however, technically based
on exponential functions, and their Gamma and, more general, hypergeometric generalizations. They have, of
course, a straightforward q (“quantum”) and t deformations [3–5], but this is not the only important direction
to look at. In modern integrability theory [6], which is a crucially important part of non-perturbative physics,
an important role is played by combinatorial generalizations of the factorial, like the quantitydR, which extends
the factorial from integers to partitions (Young diagrams). It seems important to look at the versions of
Borel transform that deal with such additional combinatorial structure, hence, the name combinatorial Borel
transform. Surprisingly or not, exponentials still show up in the combinatorial Borel transforms, through
Cauchy identities [7], thus most probably this is not the last step. However, it can prove sufficient for the needs
of integrability theory, at least.
1mironov@lpi.ru; mironov@itep.ru
2morozov@itep.ru
1
arXiv:2302.05903v2  [hep-th]  30 Jun 2023
P
rarqr
?
Borel 6Γ-average
⟨qr⟩ =qrar
br
P
rbrqr
=
=
Sr{0} = br
cr
P
rarqr
P
rcrqrSr{¯p}
6⟨Sr{¯p}⟩¯p = ar
cr
--
--
6?CBT ⟨SR{¯p}⟩¯p = aR
cR
P
RaRq|R|SR{p} =F{p}
X
R
cRq|R|SR{p}SR{¯p}
generalization
Figure 1: A picture, illustrating the concept of the combinatorial Borel transform (CBT) of the series. First, we introduce into
the original series an auxiliary function Sr{¯p} such that its average over ¯p with an appropriate measure can change the coefficients
in a desired way: say, ar = r!−→br = 1 in (1) or, more general, ar = dm
r = (r!)−m−→br = ardr = dm+1
r = (r!)−m−1. For
traditional applications, the main point is that the underlined sum can converge better than the original one in the left upper corner
due to Sr{0} = br
cr
∼ 1
r! , but for us this is just one application of many. Then, we extend the summation domain {r}−→{ R} and
introduce an additional auxiliary function SR{p} so that the sum in the box is easily calculated, for instance, with the help of the
Cauchy identity. As an additional bonus, this converts the Cauchy relations into ineteresting formulas for the series F{p} at the
right upper corner, which can a priori look non-trivial, but are actually the ¯p averages of simple identities. Technically, what we
do is a substitution of the Gamma-function average ⟨qr⟩−→ qrΓ(r + 1) =r!·qr which inverts the left vertical arrow in the usual
Borel transform, by a smoother and richer Gaussian average, at the price of extending the sum over integers r to that over all
integer partitions (Young diagrams) R. Such generalization is not unique, which opens a way to obtain a whole class of formulas
by slight changes of the Gaussian measure.
As to possible techniques which could provide a route to the combinatorial Borel transforms, in [8] it was
suggested to consider an interpolation between two different kinds of sums over all Young diagrams
X
R
q|R| =
Y
k=1
1
1−qk (3)
and
X
R
q|R|SR{p}SR{¯p} = exp
 X
k
qkpk ¯pk
k
!
(4)
by taking a specially adjusted average of the Schur functions over the power sums pk. The emphasis, however,
can be put not so much on averaging, but on coexistence of generating functions differing by the non-trivial
combinatorial weights dR. It is a common place to consider such families differing by the number of factorials
in the weights: these are just related by the standard exponential Borel transform. It is an interesting direction
to study a more tricky combinatorial difference. The goal of the present paper is to exploit this idea and extend
it further in various directions.
The paper is organized as follows. In section 2, we explain the basic of our approach, and demonstrate how
the averaging method works for evaluating sums. In section 3, we extend the method to reproduce multiple
combinatorial sums. In section 4, we discuss evaluating bilinear averages in parallel with the property of strong
superintegrability in matrix models. Section 5 contains short notes on relations of the sums considered in the
paper with the Ramanujan sums. At last, section 6 discusses the cases when the sums are divergent, while
section 7 contains some concluding remarks.
Notation. We use the notation SR{pk} for the Schur functions, which are symmetric functions of xi, and
are graded polynomials of power sums pk :=P
ixk
i . They are labeled by partitions, or, equivalently, by Young
diagrams R with lR parts: R1≥ R2≥ ... ≥ RlR. The corresponding skew Schur functions labeled by two
partitions R and Q∈ R are denoted as SR/Q{pk}, while the Macdonald polynomials are denoted through
MR{pk}. We also denote R∨ the conjugate partition (Young diagram).
Our main quantity in this paper is dR,
dR =
QlR
i<j (Ri−i−Rj +j)
QlR
i=1 (lR +Ri−i)!
(5)
which is equal to SR{δk,1} in terms of Schur functions, and is equal to dimR/|R|!, where dimR is the dimension
of representation R of the symmetric group S|R|.|R| =PlR
i Ri is here the size of partition R with lR parts.
The theory of symmetric functions can be found in [7], and the theory of symmetric groups, in [10].
We also use notation P
R for the sum over all partitions R including the empty set, while P
R⊢m means
summing over all partitions of integer m.
2

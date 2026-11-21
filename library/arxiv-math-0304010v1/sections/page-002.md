---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-002
section_title: "Page 2"
section_number: null
pages: 2-2
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
§0. Introduction
Main result. Let Yn denote the set of partitions of n (n = 1, 2, . . .). We identify
partitions and Young diagrams, so that elements of Yn become Young diagrams
with n boxes. We view each λ ∈Yn as a plane shape, of area n, inside the ﬁrst
quadrant R2
+, with coordinates r, s (the row and column coordinates).
In new
coordinates x = s −r, y = r + s, the boundary ∂λ of the shape λ ⊂R2
+ may be
viewed as the graph of a continuous piece–wise linear function, which we denote as
y = λ(x). Note that λ′(x) = ±1, and λ(x) coincides with |x| for suﬃciently large
values of |x|. The area of the shape |x| ≤y ≤λ(x) equals 2n.
Further, we equip the ﬁnite set Yn with a probability measure Mn called the
Plancherel measure. The measure Mn has important representation theoretic and
combinatorial interpretations. By deﬁnition, the weight Mn(λ) assigned to a di-
agram λ ∈Yn equals dim2 λ/n!, where dim λ is the dimension of the irreducible
representation (of the symmetric group Sn) indexed by λ. Equivalently, dim λ is
the number of standard tableaux of shape λ.
Viewing λ’s as points of the probability space (Yn , Mn), we view λ( · )’s as
random functions, and we aim to describe their asymptotics as n →∞. Informally,
the main result can be stated as follows:
1
√n λ(√n x)
∼
Ω(x) +
2
√n ∆(x),
n →∞,
(0.1)
where Ω(x) is a certain ﬁxed curve and ∆(x) is a generalized Gaussian process on
the interval [−2, 2] (Ωand ∆are speciﬁed below).
The left–hand side (denoted as ¯λ(x) in the sequel) is a rescaled version of the
function y = λ(x). The graph of ¯λ( · ) is obtained from that of λ( · ) by shrinking
both the x–axis and the y–axis in √n times. The purpose of this procedure is to
put the random ensembles with diﬀerent n’s on the same scale (note that the area
of the shape |x| ≤y ≤¯λ(x) equals 2 for any n).
The ﬁrst term in the right–hand side of (0.1) corresponds to the law of large
numbers. It follows from (0.1) that in the large n limit, the random scaled polygonal
lines y = ¯λ(x) concentrate near the ﬁxed curve y = Ω(x). In the initial scale, this
means that, for large n, the “typical” functions y = λ(x) look like the function
y = √n Ω( 1
√nx).
The second term in the right–hand side of (0.1) governs the ﬂuctuations of the
random functions ¯λ around the curve Ω, which corresponds to the central limit
theorem.
We see that the ﬂuctuations of the scaled functions are of order
1
√n.
That is, in the initial picture for the shape λ ⊂R2
+, the random ﬂuctuations of the
boundary line ∂λ need no scaling along the main diagonal, as n →∞.
Description of Ωand ∆. The function Ω(x) is given by two diﬀerent expressions
depending on whether x is in the interval [−2, 2]:
Ω(x) =
 2
π(x arcsin x
2 +
√
4 −x2),
|x| ≤2,
|x|,
|x| ≥2.
(0.2)
Note that Ω′(x) =
2
π arcsin x
2 inside [−2, 2]. The critical points ±2 have an im-
portant meaning: for “typical” (with respect to the Plancherel measure) diagrams
λ ∈Yn, the length of the ﬁrst row and of the ﬁrst column is approximately 2√n.
2

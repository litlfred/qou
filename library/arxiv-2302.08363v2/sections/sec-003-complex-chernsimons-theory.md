---
doc_id: arxiv-2302.08363v2
doc_title: "Prepared for submission to JHEP On the structure of trans-series in quantum field theory"
section_id: sec-003-complex-chernsimons-theory
section_title: "Complex Chern–Simons theory"
section_number: null
pages: 9-11
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
doc_brief: "On the structure of trans-series in quantum field theory — Many observables in quantum field theory can be expressed in terms of trans-series, in which one adds to the perturbative series a typically"
---
Complex Chern–Simons (CS) theory is an ideal arena to study trans-series, since as a QFT it is
essentially solvable, and at the same time it leads to highly non-trivial perturbative series. The
mathematical program of applying resurgence in complex CS theory was pioneered in [38], and
applied in e.g. [39, 40].
– 8 –
In this section we will illustrate our considerations with the resurgent results for parti-
tion functions on the complements of knots, presented in [41, 42]. This observable admits a
non-perturbative definition through the so-called state integral invariant [43–45], which can be
calculated by a finite-dimensional integral. The coupling constant will be denoted by τ and is a
complex variable. The partition function depends on an additional complex variable, the holon-
omy around the knot, but we will set it to zero for simplicity. In this case, the partition function
is known to be an analytic function of τ on C\(−∞, 0].
For concreteness, we will consider the complement of the famous figure-eight knot. Its state-
integral invariant is explicitly known, and we would like to express it as a trans-series. The
building blocks of the trans-series are the perturbative expansions around non-trivial saddle
points or instantons in complex CS theory. In this case, there are two of them, corresponding to
the so-called geometric connection and its complex conjugate. We will denote the perturbative
series attached to these saddle-points byφg,c(τ), whereg(c) refers to the geometric (respectively,
conjugate) connection. They can be computed explicitly up to the very high order, and their
very first terms read as
φg(τ) =
X
k≥0
akτk = 3−1/4

1 + 11π√
3· 36τ + 697π2
7776 τ 2 +···

, φ c(τ) =φg(−τ). (4.1)
The partition function (or Andersen–Kashaev invariant) will be denoted by I(τ). As shown in
[41], it can be expressed as the lateral Borel resummation of a trans-series involving the above
perturbative series. Not surprisingly, this expression depends on the region of the τ plane which
we consider. When τ is slightly above the positive real axis, one simply finds
I(τ) =−2i e− V
2πτs(φc)(τ), (4.2)
where V = 2.029883... is the volume of the figure-eight knot, and it is the classical action of the
conjugate connection in complex CS theory. In (4.2), the resummation is along the direction set
by the argument of τ. However, as we move to the region slightly above the negative real axis,
we find the expression
I(τ) =−2i e− V
2πτs (φc) (τ)M1(˜q) + 2 e
V
2πτs (φg) (τ)M2(˜q). (4.3)
Here,
˜q = e− 2πi
τ , (4.4)
and the resummation is also along the direction set by the argument of τ. M1,2(˜q) are power
series in ˜q. Their very first terms read
M1(q) = 1− 8q− 9q2 + 18q3 + 46q4 +O(q5),
M2(q) =−9q− 3q2 + 39q3 + 69q4 +O(q5),
(4.5)
and their exact expressions were conjectured in [41]. We will not need them here, but we note
that they are convergent power series with radius of convergence R = 1.
The result (4.3) has a very clear physical interpretation. The terms ˜ qn exp(±V/(2πτ )) cor-
respond to contributions of complex instantons, whose actions are of the form
∓V
2π + 2πin, n ∈ Z>0. (4.6)
– 9 –
The additional term 2πin is due to the multivaluedness of the CS action. Therefore, the expression
(4.3) can be regarded as a multi-instanton expansion in which we sum over an infinite number of
exponentially small corrections (which in fact arise as Borel singularities of the series φg,c(τ), see
[41] for a detailed explanation). In terms of the formalism we set in section 2, we have a slightly
more general trans-series than (2.2). Let us denote
M1(q) =
X
n≥0
µ1,nqn, M 2(q) =
X
n≥0
µ2,nqn. (4.7)
Then, we can write the underlying trans-series as
Φ(τ) =−2i e− V
2πτ
X
ℓ≥0
˜qℓφc,ℓ(τ) + 2 e
V
2πτ
X
ℓ≥1
˜qℓφg,ℓ(τ), (4.8)
where
φc,ℓ(τ) =µ1,ℓφc(τ), φ g,ℓ(τ) =µ2,ℓφg(τ). (4.9)
Due to the presence of two different actions, we have two different functions Gn(y) to consider,
and they are given by
G1
n(y) = (−1)nan
X
ℓ≥0
µ1,ℓyℓ = (−1)nanM1(y), G2
n(y) =an
X
ℓ≥0
µ2,ℓyℓ =anM2(y), (4.10)
where in this case y = ˜q. Therefore, it is clear that the convergence of the series M1,2(q) defined
in (4.7) guarantees the convergence of the partial series, and it is obvious from (4.10) that the
radius of convergence ofGi
n(y), i = 1, 2 are the same, for all n.
Although we have focused on a particular example, the resulting structure seems to be typical
of many trans-series in complex CS theory: the partial series are given by convergent ˜q series. As
we have pointed out, this makes it possible to have a simple resurgent structure without further
resummations.

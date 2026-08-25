---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-013-24-ron-y-donagi
section_title: "RON Y. DONAGI"
section_number: 24
pages: 24-26
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
doc_brief: "Seiberg-Witten Integrable Systems — 17 sections: RON Y. DONAGI; Introduction; References"
---
A number of special cases of this construction are well known . When D = 0,
we get Hitchin’s system [ Hi] on T ∗M. When E has genus 0, we get the polynomial
matrices system studied in [ AHH] and [ B]. For more details and examples, see
[Mn] or [ DM1].
For the SYM theory with adjoint matter, we take E to be the elliptic curve
whoseτ parameter (in the halfplane H) is the coupling constant of the theory. We
are looking for a 1-parameter family of integrable systems ( parametrized by mass
m), each having an ( n − 1)-dimensional base and ( n − 1)-dimensional ﬁbers. One
checks easily that dim(Xa) equals the dimension of the adjoint orbit of a; so we are
looking for orbits of the smallest possible dimension 2( n − 1). There is essentially
only one 1-parameter family of possibilities: D consists of a single point ∞ ∈ E, and
a is the conjugacy class of the diagonal matrix with eigenvalu esm(1, 1,..., 1, 1−n).
This conjugacy class consists of all diagonalizable SL(n) matrices A with
rank(A −m ·Id) ≤ 1.
(As m → 0 there is one further, nilpotent, orbit of the right dimensi on: the con-
jugacy class of the elementary matrix e12. But this turns out to give a trivial
integrable system, i.e. the same as for a = 0: all the spectral curves are completely
reducible).
Our system can be described rather explicitly. The moduli sp ace of degree 0,
rank n vector bundles on E can be identiﬁed with the symmetric product SnE:
each equivalence class contains a unique decomposable bund le V = ⊕n
i=1Li, with
Li = OE(qi − ∞) ∈ Pic0E. The moduli of SL(n)-bundles is the ﬁber over 0 of the
Abel-Jacobi map SnE →E. It is a projective space
{q1 + · · · +qn|
∑
qi =n∞} = PH 0(E, O(n∞)) ≈ Pn−1.
In terms of the decomposition V = ⊕Li, any Higgs ﬁeld ϕ on V can be written as
a matrix with entries
ϕij ∈ Γ(Lj ⊗L−1
i (∞)).
Let A := Res ∞ϕ. Its diagonal elements are all zeroes, and A −m ·Id has rank
≤ 1, so A is conjugate, via a diagonal matrix, to m timese = Σ i⁄=jeij. This means
that each (V,ϕ ) in our system is equivalent to a pair ( V,ϕ ) with Res ∞(ϕij) = m
for i ⁄= j. For a given V , this condition uniquely determines the ϕij (as long as
Li ⁄=Li). The remaining free parameters are the coordinates qi ofV = ⊕O(qi − ∞)
and the diagonal entries pi = ϕii. Away from the diagonals qi = qj, these ( qi,p i)
can be identiﬁed with the canonical coordinates on T ∗M.
The spectral curves
The family of spectral curves Cb, for the fundamental, n-dimensional repre-
sentation of SL(n), can be described as a linear system on the compactiﬁcation
S = P(ωE(∞) ⊕ OE) of the surface S, or on various birationally equivalent sur-
faces. More precisely, it forms an aﬃne open subspace of this linear system, the
complement consisting of curves which contain the section a t inﬁnity, Z∞ :=S −S,
with some multiplicity k > 0. By removing this multiple component, we recover
the spectral curves for the analogous problem with n replaced by n −k. (If A is an
endomorphism of a vector space V , and W is an invariant subspace, then
rankW (A −m ·Id) ≤ rankV (A −m ·Id),
so the conjugacy class restricts correctly.)
SEIBERG-WITTEN INTEGRABLE SYSTEMS 25
We can write down an explicit equation
pn(t) = tn + Σ n
k=2fktn−k = 0
for the spectral curves. Here t is a coordinate on the ﬁbers of ωE(∞), and fk ∈
Γ( OE(k∞)). (We identify OE ≈ ωE). Once we have such a pn for each n, the
previous remark and the tracelessness condition imply that the general spectral
curve has equation
Cu :pn + Σ n−2
ℓ=0uℓpℓ = 0,
with arbitrary constants uℓ which can therefore be interpreted as coordinates on
the quantum moduli-space, the base of the integrable system .
The condition on pn which speciﬁes the right conjugacy class at inﬁnity is that
when we substitute t =t′ +ξ−1, where ξ is a local coordinate on E at ∞, we get a
function of t′ and ξ with at most ﬁrst order poles in ξ. Write the equation of E in
Weierstrass form,
E :y2 =x3 +bx −c.
The local coordinate ξ determines a sequence xk,k = 2, 3,... , of rational functions
on E which are regular on E − ∞ and such that near ∞,
xk −ξ−k =O(ξ−1).
We may as well use the local coordinate ξ = x−1/2, and then the xk can be read
oﬀ the Taylor expansions:
y =ξ−3(1 +bξ4 −cξ6)1/2 =ξ−3(1 +b
2ξ4 −c
2ξ6 −b2
8ξ8 +bc
4ξ10 − 2c2 −b3
16 ξ12 +... )
and
y−1 =ξ3(1+bξ4−cξ6)−1/2 =ξ3(1−b
2ξ4+c
2ξ6+ 3b2
8 ξ8− 3bc
4 ξ10+ 6c2 − 5b3
16 ξ12+... ).
Explicitly, we get:
x2 =x
x3 =y
x4 =x2
x5 =xy
x6 =x3
x7 =x2y − b
2y
x8 =x4
x9 =x3y − b
2xy + c
2y
x10 =x5
x11 =x4y − b
2x2y + c
2xy + 3b2
8 y
x12 =x6,

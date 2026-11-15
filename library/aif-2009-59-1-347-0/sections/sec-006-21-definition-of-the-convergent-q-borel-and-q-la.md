---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-006-21-definition-of-the-convergent-q-borel-and-q-la
section_title: "Definition of the convergent q-Borel and q-Laplace transform"
section_number: 2.1
pages: 14-16
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
toc_source: outline
doc_brief: "On q-summation and confluence — 28 sections: Front matter; Introduction; Part 1. Convergent q-Borel and q-L"
---
transform
Definition 2.1. — Let C{x} be the ring of the germs of analytic func-
tions in the neighborhood of x = 0.
(1) We call (convergent) q-Borel transform the map Bq given by:
Bq :
xC {x} →C{ξ},
X
n⩾0
anxn+1 7→
X
n⩾0
an
[n]!q
ξn.
(2) The (convergent) q-Laplace transform Lq is deﬁned by
Lq = B−1
q
:
C{ξ} →xC {x} ,
X
n⩾0
anξn 7→
X
n⩾0
an[n]!
qxn+1.
Remark 2.2. —
Notice that the q-Euler series Eq(x), considered in the
previous section, converges for |x| < 1 −q. Therefore a function f(x) is
analytic on an open disc {|x| < R}, for some R ∈(0, ∞), if and only if its
q-Borel transform Bqf(ξ) is analytic for |ξ| < R/(1 −q).
Calling Bq and Lq q-Borel and q-Laplace transform is somehow an abuse
of language: they don’t transform convergent series in divergent series and
vice versa. Nevertheless they have interesting properties and we will show
that they play a role in the understanding of the conﬂuence in the irregular
case. In fact, when q →1, they tend coeﬃcientwise to the usual Borel and
Laplace transforms, that we will denote B1 and L1 respectively.
TOME 59 (2009), FASCICULE 1
360
Lucia DI VIZIO & Changgui ZHANG
Let us denote by eq(x) the generating function associated to the sequence
(
1
[n]!q )n⩾0, so that it follows: eq(x) =
1
((1−q)x;q)∞. An important property of
Bq and Lq is that they can be expressed both as continuous and discrete
integrals:
Proposition 2.3. — Let f ∈xC{x} and φ ∈C{ξ} such that Bqf = φ.
Then:
φ(ξ) =
1
2πi
Z
|x|=R
f(x)
((1 −q) ξ
x; q)∞
dx
x2 =
1
2πi
Z
|x|=R
f(x)eq (ξ/x) dx
x2 ,
f(x) = −1
2πi
Z
|ξ|=ρ
φ(ξ)Eq

−x
ξ

dξ,
where the radii R and ρ are assumed to be chosen suﬃciently small, inde-
pendently of the variables ξ and x, respectively.
Proof. — The ﬁrst equality is a consequence of the identity
1
(x; q)∞
=
X
n⩾0
1
(q; q)n
xn
and of the residue theorem. Taking into account (1.1), the second equality
is an application of the residue theorem.
□
Corollary 2.4. — Let f and φ be as in Proposition 2.3. Then:
φ(ξ) = (q; q)∞
Z ξ
0
f((1 −q)x)
( qx
ξ ; q)∞
θ′(−x
ξ ) dqx,
(2.1)
f(x) =
Z
x
1−q
0
(1 −q)qξ
x
; q

∞
φ(ξ)dqξ =
Z
x
1−q
0
eq (qx/ξ)−1 φ(ξ)dqξ.
Remark 2.5. —
Notice that Formula (2.1) generalizes (1.4) and can be
obtained by direct calculations. We give an alternative proof below.
Proof. — Taking the derivative with respect to x of the functional equa-
tion
θ(qnx) = x−nq−n(n−1)/2θ(x)
and setting x = −1, we obtain
θ′(−qn) = (−1)nq−n(n+1)/2θ′(−1) = (−1)nq−n(n+1)/2(q; q)3
∞.
The residues formula and Equation (1.1) imply that
φ(ξ) = (1 −q)ξ
(q; q)∞
X
n⩾0
(−1)n f((1 −q)ξqn)
(q; q)n
qn(n+3)/2
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE
361
and that
f(x) = x
X
n⩾0
qn(qn+1; q)∞φ
 qnx
1 −q

.
This ends the proof.
□

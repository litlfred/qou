---
doc_id: s0894-0347-08-00618-8
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8"
section_id: sec-014-41-symmetric-homogenization-via-gårding-hyperbol
section_title: "Symmetric homogenization via Gårding hyperbolic polynomials"
section_number: 4.1
pages: 21-24
source_pdf: S0894-0347-08-00618-8.pdf
source_sha256: 7c0b2ca41992b21c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8 — 24 sections: Front matter; Introduction; A plethora of negative dependence"
---
following theorem shows that the symmetric homogenization (cf. §2.3) of any
strongly Rayleigh measure is again strongly Rayleigh, so that strongly Rayleigh
measures belong to the class PHR (Deﬁnition 2.6).
Theorem 4.2. If µ ∈Pn is strongly Rayleigh, then so is its symmetric homoge-
nization µsh ∈P2n.
The proof of Theorem 4.2 makes use of the theory of hyperbolic polynomials
that has its origins in partial diﬀerential equations and was developed by Petrovsky,
G˚arding, H¨ormander, Atiyah and Bott [3, 37, 43]. Recently, hyperbolic polynomi-
als have proved to be quite useful in other areas of mathematics such as convex
optimization [4, 36], complex analysis [7], matrix theory and combinatorics [34, 35].
542
J. BORCEA, P. BR¨AND´EN, AND T. M. LIGGETT
Let e ∈Rn. A homogeneous polynomial p ∈R[z1, . . . , zn] is said to be (G˚arding)
hyperbolic with respect to e if p(e)̸ = 0 and for all x ∈Rn the univariate polynomial
t 
→p(x + te) has only real zeros. Recall that the homogenization of a polynomial
f(z1, . . . , zn) = 
α∈Nn a(α)zα ∈C[z1, . . . , zn] of degree d is given by
fH(z1, . . . , zn+1) = zd
n+1f(z1/zn+1, . . . , zn/zn+1).
Recall the characterization of real stable polynomials given in Proposition 3.1
(1). The relationship between real stable polynomials and hyperbolic polynomials
is made explicit by the following result; see [9, Proposition 1].
Proposition 4.3. Let f ∈R[z1, . . . , zn]. Then f is real stable if and only if fH is
hyperbolic with respect to all vectors e ∈Rn+1 of the form e = (e1, . . . , en, 0), where
ei > 0 for 1 ≤i ≤n.
Let p be hyperbolic with respect to e ∈Rn. The cone
Ce(p) = {x ∈Rn : p(x + te)̸ = 0, t ≥0}
is called the hyperbolicity cone of p. The following fundamental properties of the
hyperbolicity cone are due to G˚arding [37]; see also [3, 36, 43].
Proposition 4.4. Let p ∈R[z1, . . . , zn] be hyperbolic with respect to e ∈Rn. Then
(a) Ce(p) is convex;
(b) Ce(p) is equal to the connected component of the set {x ∈Rn : p(x)̸ = 0}
that contains e;
(c) (s, t) 
→p(x + su + te) is real stable for any x ∈Rn and u ∈Ce(p);
(d) p is hyperbolic with respect to any u ∈Ce(p) and Cu(p) = Ce(p).
Below are examples of hyperbolic polynomials and their hyperbolicity cones:
(I) The polynomial p(z1, . . . , zn) = z1z2 · · · zn is hyperbolic with respect to the
direction e = (1, . . . , 1) ∈Rn, and the hyperbolicity cone is the positive
orthant Ce(p) = Rn
+.
(II) The (principal) symbol of the hyperbolic wave equation, i.e., the polynomial
p(z1, . . . , zn) = z2
1 −
n

j=2
z2
j ,
is hyperbolic with respect to the direction e = (1, 0, . . . , 0) ∈Rn, and the
hyperbolicity cone is the Lorentz cone
Ce(p) =

z ∈Rn :

z2
2 + · · · + z2n ≤z1

.
(III) Let zij, 1 ≤i ≤j ≤n, be n(n + 1)/2 diﬀerent variables and let X =
(xij)n
i,j=1 be the matrix with entries
xij =

zij if i ≤j,
zji if i > j.
The polynomial (in n(n + 1)/2 variables) p(z11, . . . , znn) = det(X) is hy-
perbolic with respect to the n × n identity matrix I, and the hyperbolicity
cone is the cone of positive deﬁnite n × n matrices.
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS
543
(IV) Let A1, . . . , Am be symmetric n×n matrices and let e = (e1, . . . , em) ∈Rm
be such that e1A1 + · · · + emAm is positive deﬁnite. Then the polynomial
p(z1, . . . , zm) = det
⎛
⎝
m

j=1
zjAj
⎞
⎠
is hyperbolic with respect to e, and the hyperbolicity cone is given by
Ce(p) =
⎧
⎨
⎩x ∈Rm :
n

j=1
xjAj is positive deﬁnite
⎫
⎬
⎭.
Theorem 4.5. Suppose that all the coeﬃcients of f ∈R[z1, . . . , zn] are non-
negative. The following are equivalent:
(1) fH is stable;
(2) f is stable;
(3) fH is hyperbolic with respect to some vector e with ei ≥0; 1 ≤i ≤n + 1;
(4) fH is hyperbolic with respect to any vector e with ei > 0, 1 ≤i ≤n + 1.
Proof. By the fact that the stability property is closed under setting variables equal
to real numbers (Proposition 3.1) and Proposition 4.3, we have that (1) ⇒(2) ⇒
(3). Now if (3) holds, then since f has all non-negative coeﬃcients it follows from
Proposition 4.4 (b) that Ce(fH) contains the cone Rn+1
+
, which by Proposition 4.4
(d) proves (4). Finally, (4) ⇒(1) by Proposition 3.1.
□
Let f ∈C[z1, . . . , zn] be a polynomial of degree di in zi, 1 ≤i ≤n.
The
polarization π(f) of f is the unique polynomial in n
i=1 di variables zij, 1 ≤i ≤n,
1 ≤j ≤di, satisfying:
(i) π(f) is multi-aﬃne;
(ii) π(f) is symmetric in the variables zi1, . . . zidi for 1 ≤i ≤n;
(iii) if we let zij = zi for all i, j in π(f), we recover f.
Recall that a circular region in C is either an open or closed aﬃne half-plane or
the open or closed interior or exterior of a circle. The famous Grace-Walsh-Szeg¨o
coincidence theorem [32, 66, 74] is stated next. For a proof of the following version
we refer to [19, Theorem 2.12].
Theorem 4.6 (Grace-Walsh-Szeg¨o). Let f ∈C[z1, . . . , zn] be symmetric and multi-
aﬃne and let C be a circular region containing the points ζ1, . . . , ζn. Suppose that
either f has total degree n or C is convex (or both). Then there exists at least one
point ζ ∈C such that f(ζ1, . . . , ζn) = f(ζ, . . . , ζ).
From the Grace-Walsh-Szeg¨o coincidence theorem we deduce:
Corollary 4.7. Let f ∈C[z1, . . . , zn]. Then f is stable if and only if π(f) is stable.
Proof. If π(f) is stable, then so is f since the latter is recovered from π(f) by
setting variables equal as in (iii) above. Now suppose that π(f) is not stable. Then
there are numbers ζij ∈{z ∈C : Im(z) > 0}, 1 ≤i ≤n, 1 ≤j ≤di, such that
π(f)(ζ) = 0, where ζ = (ζ11, . . . , ζ1d1, . . . , ζn1, . . . , ζndn). By successively applying
the Grace-Walsh-Szeg¨o coincidence theorem we see that there is a vector ζ′ =
(ζ′
11, . . . , ζ′
1d1, . . . , ζ′
n1, . . . , ζ′
ndn) with coordinates in {z ∈C : Im(z) > 0} for which
ζ′
ij = ζ′
kℓwhenever i = k and π(f)(ζ′) = π(f)(ζ) = 0. Hence f(ζ′
11, ζ′
21, . . . , ζ′
n1) =
π(f)(ζ′) = 0, so f is not stable either.
□
544
J. BORCEA, P. BR¨AND´EN, AND T. M. LIGGETT
We now have all the tools to prove Theorem 4.2.
Proof of Theorem 4.2. Let g be the generating polynomial of µ ∈Pn and suppose
that g is stable of degree d. Then so is the homogenization gH of g by Proposi-
tion 4.3. Now straightforward computations show that the generating polynomial
of the symmetric homogenization µsh ∈P2n is given by π(zn−d
n+1gH), so the theorem
follows from Corollary 4.7.
□

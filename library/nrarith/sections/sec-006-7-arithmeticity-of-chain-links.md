---
doc_id: nrarith
doc_title: "Arithmetic of Hyperbolic Manifolds"
section_id: sec-006-7-arithmeticity-of-chain-links
section_title: "Arithmeticity of chain links"
section_number: 7
pages: 29-30
source_pdf: nrarith.pdf
source_sha256: 085ec9541ddc6cd4
toc_source: inferred
doc_brief: "Arithmetic of hyperbolic manifolds (Neumann–Reid) — survey of arithmetic Kleinian groups: an arithmetic M = H³/Γ is determined up to commensurability by its invariant trace field and quaternion…"
---
Proof of part (iii) of Theorem 5.1. Recall that C(p, s) is a cover of W ′(p, s) and if
W ′(p, s) is hyperbolic, then it is double branched covered by W(p, q) with s = 2q. We
claim that the geodesic γ(p, s) added by hyperbolic Dehn ﬁlling W ′ to form W ′(p, s)
has length
ℓ0(γ(p, s)) = −d
s Re(u) = d
2p Re(v),
d = gcd(p, s),
(7.1)
where u and v are as in equations (6.4) and (6.5). Indeed, if ℓ(γ(p, s)) is the complex
length of the added geodesic then, by equation (6.5) and by [Th] or [NZ], we have
equations
pu + sv
2 = 2πi
p′u + s′ v
2 = ℓ(γ(p, s)),
where p′ and s′ are integers satisfying ps′ −sp′ = d. Multiplying the ﬁrst of these two
equations by s′ and the second by s and subtracting gives du = 2πis′ −sℓ(γ(p, s)),
from which the ﬁrst equality of (7.1) follows by taking real part; the second equality
follows similarly.
The computations that we now describe were computer-aided, so we omit some details.
We wish to ﬁnd the (p, s) for which ℓ0(γ(p, s)) ≥0.431277313 (cf. Corollary 4.7). We
use equations (7.1). First, by plotting level curves in the (p + s, s)-plane for Re(u)
and Re(v) one ﬁnds that the conditions | Re(u)| ≥0.43 and | Re(v)/2| ≥0.43 force
(p + s, s) to lie in a bounded domain (which lies entirely within the circle of radius 15).
It is then quick to verify that the (p, s) for which ℓ0(γ(p, s)) ≥0.431277313 are those
with (|p + s|, |s|) or (|s|, |p + s|) in {(n, 0) : 3 ≤n ≤14} ∪{(n, n) : 3 ≤n ≤
7} ∪{(3, 1), (3, 2), (4, 2)}. Thus, only in these cases might W ′(p, s) be arithmetic.
The table of Theorem 4.6 of possible short geodesic lengths in cusped arithmetic
orbifolds now eliminates all cases but those of part (iii) of Theorem 5.1, namely (|p +
s|, |s|) or (|s|, |p + s|) equal to one of (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 2),
(4, 4), (6, 0). (We could also have eliminated all but these and (6, 6) by the observation
that a cusped arithmetic orbifold can have torsion only of order 2, 3, 4, or 6, since the
trace of the square of the torsion element must be in some Od.)
To show that the above cases do give arithmetic orbifolds we use the characterization
of arithmeticity in Proposition 4.4. We must thus verify that in these cases the invariant
trace ﬁeld k(π1W ′(p, s)) is Q(
√
−d) with d respectively 7, 1, 3, 1, 3, 7, 2, 15,
and that W ′(p, s) has integral traces. By Theorem 6.2 and the proof of Theorem 6.3
we must check that z and 4/z lie in the appropriate Od. This is evident from Table 2,
which includes also the non-arithmetic case (6, 6).
Table 2. z and 4/z
{|p + s|, |s|}
z
4/z
{3, 0}
−3+√−7
2
−3−√−7
2
{3, 1}
−1 + √−1
2 −2√−1
{3, 2}
−1+√−3
2
−2 −2√−3
{3, 3}
+√−1
−4√−1
{4, 0}
−1 + √−3
−1 −√−3
{4, 2}
−1+√−7
2
−1 −√−7
{4, 4}
+√−2
−2√−2
{6, 0}
−1+√−15
2
−1−√−15
2
{6, 6}
+√−3
−4√−3
3
It is remarkable that the arithmetic W ′(p, s) are picked out exactly by Theorem 4.6.
We had conjectured the following alternate characterization of the arithmetic cases, and
T. Chinburg showed us a proof, which we sketch.
Proposition 7.1. k(π1W ′(p, s)) is a quadratic imaginary ﬁeld if and only if (p, s) is
one of the arithmetic cases above or (|p + s|, |s|) = (6, 6) (for which W ′(p, s) does not
have integral traces).
Sketch Proof. Suppose Q(z) is imaginary quadratic. Since z = x −x−1, x has degree
at most 4 over Q. If p = 0 or p+4q = 0 then equation (6.7) shows that x, respectively
(x + 1)/(x −1), is a root of unity of degree at most 4 over Q. This gives ﬁnitely many
cases to check. If neither p nor p + 4q is zero, then the proof of Theorem 6.3 shows that
z is an algebraic integer divisor of 4 in an imaginary quadratic number ﬁeld. This again
gives ﬁnitely many cases to check.
We have computed the minimal polynomial for the generating element z of
k(π1W ′(p, s)) whenever |p + s| and |s| are at most 13.
The degree is always at
most max{|p+s|, |s|}−1, as is not hard to prove, but is often smaller, as Table 3 shows.

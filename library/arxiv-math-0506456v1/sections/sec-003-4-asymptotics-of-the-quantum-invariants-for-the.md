---
doc_id: arxiv-math-0506456v1
doc_title: "Journal of Knot Theory and Its Ramiﬁcations c© W orld Scientiﬁc Publishing Company ASYMPTOTICS OF THE QUANTUM INV ARIANTS FOR SURGERIES ON THE FIGURE 8 KNOT JØRGEN ELLEGAARD ANDERS"
section_id: sec-003-4-asymptotics-of-the-quantum-invariants-for-the
section_title: "Asymptotics of the quantum invariants for the ﬁgure 8 knot"
section_number: 4
pages: 3-5
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
The AEC, Conjecture 1, however oﬀers in a sense a converse point of view, where
one seeks to derive the ﬁnal output of perturbation theory afte r all cancellations
have been made (i.e. collect all terms with the same Chern–Simons valu e). This
seems actually rather reasonable in this case, since the exact invar iant is known
explicitly.
The AEC was proved by Andersen in [1] in the case of mapping tori of ﬁ nite
order diﬀeomorphisms of orientable surfaces of genus at least two using the gauge-
theoretic approach to the quantum invariants. Later on the AEC w as proved by
Hansen in [9] for all Seifert manifolds with orientable base by suppleme nting the
work of Rozansky [31] with the required analytic estimates. In [10] t he AEC is
futher proved for the Seifert manifolds with nonorientable base of even genus.
Using the approach of Reshetikhin and Turaev to the quantum invar iants, the
AEC has not yet been proved for any hyperbolic 3–manifold. It is the refore partic-
ular interesting to consider surgeries on the ﬁgure 8 knot. Let Mp/q be the manifold
obtained by (rational) Dehn surgery on the ﬁgure 8 knot with surge ry coeﬃcient
p/q. Then Mp/q has a hyperbolic structure if and only if |p|> 4 or |q|> 1, see e.g.
[25, Theorem 10.5.10] or [33]. (It is well-known that for |q| = 1 and |p| ∈ { 1, 2, 3}
Mp/q is a Seifert manifold, and M±4 are obtained by gluing together the comple-
ment of the trefoil knot and the non-trivial I–bundle over the Klein bottle, see e.g.
[15, p. 95]. The manifold M0 is a mapping torus of a torus, see Appendix C.) We
use here the convention of Rolfsen for surgery coeﬃcients, cf. [3 0, Chap. 9]. In
particular Dehn surgery on a knot K in S3 with surgery coeﬃcient f ∈ Z is equal
to the boundary of the compact 4–manifold obtained by attaching a 2–handle to
the 4–ball using the knot K with framing f , see [30, p. 261]. As usual Mp/q is given
the orientation induced by the standard right-handed orientation of S3.
The advantage of working with surgeries on the ﬁgure 8 knot K is that the
(normalized) colored Jones polynomial J ′
K(λ) is known explicitly. In fact
J ′
K(λ) =
λ−1∑
m=0
ξ−mλ
m∏
l=1
(1 −ξλ−l)(1 −ξλ+l),
where ξ = exp(2πi/r) (and the product is 1 for m = 0). The colors λ are here di-
mensions of irreducible representations of the quantum group ass ociated to sl2(C)
and the root of unity ξ, so λ = 1, 2,...,r . By the above expression for J ′
K(λ) we
have an explicit formula for the quantum invariant τr(Mp/q) (see formula (2.17)).
Although this formula is completely explicit, it is not clear from it what th e leading
order large r asymptotics of τr(Mp/q) is. In order to study this asymptotics, we ob-
serve (generalizing from Kashaev’s work) that the product in the e xpression for the
colored Jones polynomial can be expressed in terms of a quotient of two evaluations
of Faddeev’s quantum dilogarithm Sγ (γ =π/r):
J ′
K(λ) =
λ−1∑
m=0
ξ−mλ
(1 −ξλ)
Sγ(−π + 2γ(λ −m) −γ)
Sγ(−π + 2γ(λ +m) +γ). (1.1)
4 Asymptotics of the quantum invariants for the ﬁgure 8 knot
This follows directly from the functional equation
(1 +e
√−1ζ)Sγ(ζ +γ) = Sγ(ζ −γ)
which Faddeev’sSγ satisﬁes. Recall that for Re( ζ)<π +γ we have the expression
Sγ(ζ) = exp
(1
4
∫
CR
eζz
sinh(πz) sinh(γz )z dz
)
,
which together with the functional equation determines Sγ as a meromorphic func-
tion on C. For the so-called top color, i.e. λ = r, we obtain the sligthly simpler
expression
J ′
K (r) = r
r−1∑
m=0
Sγ(π − (2m + 1)γ)
Sγ(−π + (2m + 1)γ).
Then we simply use the residue formula to convert this expression int o a contour
integral
J ′
K(r) =
∫
Cr
tan(πrx)˜gr(x)dx,
where Cr is contained in the strip {z ∈ C | 0< Re(z)< 1} and encloses (m + 1
2 )/r
for m = 0,...,r − 1, and ˜gr is a holomorphic function in this strip expressed in
terms of the above quotient of Sγ functions (see formula (3.21)).
Similarly we get for the quantum invariant with the use of (1.1) and the residue
theorem, now a double contour integral, since the quantum invarian t also involves
a sum over colors:
τr(Mp/q) =
∫
Cr×Cr
cot(πrx) tan(πry) ˜fp,q,r (x,y )dxdy, (1.2)
where ˜fp,q,r is holomorphic on the double strip {z ∈ C | 0< Re(z)< 1}2 and given
by some expression involving quotients of evaluations of Sγ functions, and where
we furthermore require of Cr that it also encloses k/r for k = 1,...,r − 1.
From this it is clear that we need to understand the small γ asymptotics of Sγ.
We have that
Sγ(ζ) = exp
( 1
2√−1γ Li2(−e
√−1ζ) +Iγ(ζ)
)
,
where Li 2 is Euler’s dilogarithm function, and where we have certain analytic est i-
mates on Iγ(ζ) (see Lemma 3).
Let us ﬁrst explain how we use this to give a proof of the volume conje cture of
Murakami and Murakami [24] for the ﬁgure 8 knot, namely that
lim
r→∞
2πLog(J ′
K(r))
r = Vol(K),
where the right-hand side is the hyperbolic volume of the ﬁgure 8 kno t, i.e. the hy-
perbolic volume of the complement S3 \K. The basic idea in analyzing the above

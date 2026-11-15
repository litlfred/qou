---
doc_id: ant-v14-n7-s-p07
doc_title: "Nonvanishing of hyperelliptic zeta functions over finite fields"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: ant-v14-n7-s-p07.pdf
source_sha256: c5a749ef6be194fd
toc_source: undetermined
doc_brief: "Nonvanishing of hyperelliptic zeta functions over finite fields — 16 sections: Page 1; Page 2; Page 3"
---
Nonvanishing of hyperelliptic zeta functions over ﬁnite ﬁelds
1899
because the form in which we present the proof here is conducive to proving the explicit bounds for
the stable range obtained in Proposition 2.7 below. It would be interesting to address the questions of
explicit bounds for the stable range in the more general situations considered by [loc. cit.], where the
group-theoretic part of the proof of Proposition 2.7 would presumably be more complicated.
When a = 1 and n is odd, Proposition 2.1 is essentially Theorem 8.8 of [Ellenberg et al. 2016], and
indeed the proof here is a modiﬁcation of the proof of that theorem.
The reader may note that [Ellenberg et al. 2016, Theorem 8.8] requires not only that q is not a multiple
of ℓbut that q is not congruent to 1 modulo ℓ. We face no such restriction here. That’s because [loc. cit.,
Theorem 8.8] computes arbitrary moments of the Cohen–Lenstra distribution, whereas we are only
studying the analogue of the average size of the ℓ-part of the class group. In the language of [loc. cit.,
Theorem 8.8], we are only considering the case A = Z/ℓZ. The difference is as follows. In the proof, we
will end up estimating the number of Fq-points on a moduli space over Fp, and the result will depend
on that space having just one geometrically irreducible component deﬁned over Fq. In the more general
setting treated in [loc. cit., Theorem 8.8], that space has many geometric components, all but one of which
have ﬁelds of deﬁnition containing µℓ; so when q is congruent to 1 mod ℓthere are multiple Fq-rational
components. In the case treated here, the moduli space in question is geometrically irreducible, so this
issue does not arise.
Proof. We begin by observing that P
f ∈Qn,q ma( f ) can be interpreted as the number of Fq-rational points
of a certain moduli space.
To this end we brieﬂy recall the setup of [Ellenberg et al. 2016, Section 7].
Let k be a ﬁeld, let G be a ﬁnite group with trivial center, denote by e the identity element of G, and
let c be a conjugacy-closed subset of G\e. By a tame G-cover of P1 with monodromy type c we mean a
triple (X, f, φ) where
• X is a smooth proper geometrically connected curve X/k;
• f : X →P1 is a tamely ramiﬁed ﬁnite cover;
• The image of tame inertia at each branch point of f excepting ∞lies in c;
• f is Galois with group G; that is, Aut( f ) acts transitively on the geometric ﬁbers of f and φ is an
automorphism from G to Aut( f ).
Here by an isomorphism between two covers f : X →P1 and f ′ : X′ →P1 we mean a morphism
ψ : X →X
′ with f ′ ◦ψ = f , not a pair (ψ, ι) with ι a nontrivial automorphism of P1 and f ′ ◦ψ = ι ◦f .
In other words, our P1 is “labeled”.
Then, as in [Ellenberg et al. 2016, Section 7] (more or less immediate from a theorem of Romagny and
Wewers [2006]), there is a scheme Hnc
G,n over Z[1/|G|] whose k-points (as long as k has characteristic
prime to |G|) are in bijection with the isomorphism classes of tame G-covers of P1 which have n branch

---
doc_id: arxiv-0906.1500v4
doc_title: "TWISTED ALEXANDER INV ARIANT AND NON–ABELIAN REIDEMEISTER TORSION FOR HYPERBOLIC THREE–DIMENSIONAL MANIFOLDS WITH CUSPS"
section_id: sec-001-l-jeﬀrey-and-j-weitsman-jw93-and-j-park-par97-fu
section_title: "Jeﬀrey and J. Weitsman [JW93] and J. Park [Par97]. Furthermore , J. Porti [Por97]"
section_number: L
pages: 1-3
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
doc_brief: "TWISTED ALEXANDER INVARIANT AND NON–ABELIAN REIDEMEISTER TORSION FOR HYPERBOLIC THREE–DIMENSIONAL MANIFOLDS WITH CUSPS — W e study a computational method of the hyperbolic Reidemeister torsion (also"
---
applied the Reidemeister torsion twisted by the adjoint representa tion to the study of
three–dimensional hyperbolic manifolds eventually with cusps via SL 2(C)-character va-
rieties.
Let M be a hyperbolic three–dimensional manifold with cusps. We consider t he char-
acter variety X(M ) of M , which is in a sense the “algebraic quotient” of the represen-
tation space Hom
(
π1(M ), SL2(C)
)
under the action by conjugation. This set has the
structure of a complex algebraic aﬃne set as it is proved in [CS83, LM8 5]). The geo-
metric component of X(M ) is the connected component which contains the discrete and
faithful representation of the complete hyperbolic structure.
The construction of the hyperbolic torsion uses SL 2(C)-representations whose con-
jugacy classes lie in the geometric component. In general, it is not ea sy to compute
the hyperbolic torsion directly from the deﬁnition because the twist ed complex involved
for the computation is not acyclic is that case. But for hyperbolic kn ot exteriors, we
can carry out the computation of the hyperbolic torsion by using th e derivative of the
twisted Alexander invariant given by second author’s work [Yam08]. Such formula gives
a link between the hyperbolic torsion, which is a “non–acyclic” Reideme ister torsion,
and another one which has the advantage to be computed using an a cyclic complex. We
call this procedure the derivative formula of the twisted Alexander invariant and we use
Date: November 13, 2018.
2000 Mathematics Subject Classiﬁcation. Primary: 57M25, Secondary: 57M27.
Key words and phrases. Reidemeister torsion; Twisted Alexander invariant; Chara cter variety;
Three–dimensional hyperbolic manifold; Homology orienta tion.
1
the terminology non–abelian Reidemeister torsion instead of the hyperbolic Reidemeister
torsion following author’s previous works [Dub05, DHY09].
This paper provides the generalized framework to compute the non –abelian Reidemeis-
ter torsion of a hyperbolic three–dimensional manifold with cusps by using the derivative
of the twisted Alexander invariant with multivariables. We proceed fr om the technical
conditions required by our framework to the computation procedu re of the non–abelian
Reidemeister torsion. Our framework requires the following three k inds of assumptions:
• topological conditions on the hyperbolic three–dimensional manifold M whose
boundary consists in the disjoint union of b two–dimensional tori:
∂M =
b⋃
ℓ=1
T 2
ℓ ;
• conditions on the surjective homomorphism
ϕ : π1(M ) → Zn = ⟨t1, . . . , tn | titj = tjti (∀ i, j) ⟩
which gives the variables of the twisted Alexander invariant and;
• conditions on an irreducible SL 2(C)-character ρ : π1(M ) → SL2(C) which lies in
the geometric component of the character variety.
These assumptions are referred to as the symbols ( AM ), ( Aϕ) and ( Aρ). Under these
assumptions, we show the following four results:
• the non–abelian Reidemeister torsion TM
λ (ρ) and the twisted Alexander invariant
∆ ϕ⊗Ad◦ρ
M (t1, . . . , tn) are well–deﬁned;
• the derivative of the twisted Alexander invariant with multivariables g ives the
non–abelian Reidemeister torsion. More precisely, we have:
lim
t1,...,tn− →1
∆ ϕ⊗Ad◦ρ
M (t1, . . . , tn)
∏ b
ℓ=1
(
t
a(ℓ)
1
1 · · ·ta(ℓ)
n
n − 1
) = (−1)b · TM
λ (ρ).
Here b denotes the number of tori components of the boundary ∂M of M and
ϕ
(
π1(T 2
ℓ )
)
=
⟨
t
a(ℓ)
1
1 · · · ta(ℓ)
n
n
⟩
for some positive integers a(ℓ)
1 , . . . , a(ℓ)
n ;
• under some technical conditions on the representations ϕ and ρ, we prove that
the twisted Alexander invariant ∆ ϕ⊗Ad◦ρ
M (t1, . . . , tn), which a priori lies in the
fraction ﬁeld C(t1, . . . , tn), is in fact contained in C[t±1
1 , . . . , t±1
n ] (up to a factor
tm1
1 · · · tmn
n for some integers m1, . . . , mn), and;
• we give the computation example of the non–abelian Reidemeister tor sion for
the Whitehead link exterior by using this generalized formula.
The advantage of our generalization of the derivative formula lies in t he fact that
we can obtain a sequences of hyperbolic knot exteriors by Dehn ﬁlling a hyperbolic
link exterior with some solid tori. Since twist knots are obtained by Deh n ﬁlling the
Whitehead link exterior, the computations result of the non–abelian Reidemeister torsion
for the Whitehead link exterior is useful to observe the asymptotic behavior of the non–
abelian Reidemeister torsions for the twist knot exteriors, as obse rved in [DHY09] by V.
Huynh and the authors.
It is expected that the twisted Alexander invariant in our framewor k has other prop-
erties than the derivative formula. We also prove a duality formula (w ith sign) for
the twisted Alexander invariant which can be compared with the well–k nown symme-
try property of the usual Alexander polynomial. More precisely, if M is a link exterior
M = EL = S3 \ N (L), then the polynomial torsion of EL satisﬁes the following formula:
∆ ϕ⊗Ad◦ρ
EL (t−1) = ( −1)b∆ ϕ⊗Ad◦ρ
EL (t).
2
Organization
The outline of the paper is as follows. Section 2 deals with some reviews on the sign–
determined Reidemeister torsion for a manifold and on the multiplicativ e property of
Reidemeister torsions (the Multiplicativity Lemma) which is the main too l for computing
Reidemeister torsions by using a cut and past argument. In Section 3, we set down
technical assumptions used in the whole of this paper, prove that a certain twisted
homology vanishes and then give the deﬁnition of the twisted Alexand er invariant for a
hyperbolic manifold with boundary. Section 4 presents some example s of computations of
the twisted Alexander invariant for the ﬁgure eight knot exterior a nd for the Whitehead
link exterior. Section 5 gives a reduction of the number of variables in the twisted
Alexander invariant when we change coeﬃcients in the twisted chain c omplex in the
deﬁnition of the torsion. Section 6 is devoted to the derivative form ula which gives a
bridge joining the twisted Alexander invariant and the non–abelian Re idemeister torsion
in the adjoint representation associated with an SL 2(C)-representation in the geometric
component. In Section 7, we prove that the twisted Alexander inva riant is generically
a polynomial by using a cut and paste argument and the multiplicative p roperty of
Reidemeister torsions (see Theorem 5). The symmetry properties (with sign) of this
polynomial torsion are investigated in Section 8 (see Theorem 14).

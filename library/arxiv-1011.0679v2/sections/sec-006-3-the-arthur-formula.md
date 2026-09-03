---
doc_id: arxiv-1011.0679v2
doc_title: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS"
section_id: sec-006-3-the-arthur-formula
section_title: "The Arthur formula"
section_number: 3
pages: 14-17
source_pdf: 1011.0679v2.pdf
source_sha256: 6fa4bbcf4e908373
---
In this section we prove the Arthur formula for the Euler–Poi ncar´ e pairing (30)
of representations of aﬃne Hecke algebras. In view of Lemma 2 .2 little is lost if we
restrict EPH to tempered representations, so we do that until further not ice. One
of the main results of [OpSo1] says that
(32) Ext n
S(π,π ′) ∼= Extn
H(π,π ′) n ∈ Z≥0
for all π,π ′ ∈ Modf (S), and hence
(33) EPS (π,π ′) :=
∑
n≥0
(−1)n dimC Extn
S(π,π ′) equals EPH(π,π ′).
We remark that corresponding statement for reductive p-adic groups is a deep the-
orem of Meyer [Mey].
It is clear from the deﬁnition (30) that EPH(π,π ′) = 0 if π andπ′ admit diﬀerent
Z(H)-characters. With (33) we can strengthen this to EPH(π,π ′) = 0 whenever
π and π′ admit diﬀerent Z(S)-characters. This is really stronger, because Z(S) is
larger than the closure of Z(H) in S.
We ﬁx ξ = (P,δ,t ) ∈ Ξ un. As Ξ un has the structure of a smooth manifold (with
components of diﬀerent dimensions) we can consider its tange nt space Tξ(Ξ un) at
ξ. The isotropy group Wξ acts linearly on Tξ(Ξ un) and for w ∈ W ξ we denote the
determinant of the corresponding linear map by det( w)Tξ(Ξ un). Since the connected
component of ξ in Ξ un is diﬀeomorphic to T P
un, we have
Tξ(Ξ un) ∼= Lie(T P
un) ∼=iaP ∼=i(a/aP ).
The expression det(1 −w)Tξ(Ξ un) = det(1 −w)aP is analogous to the Weyl denomi-
nator and to d(r) in Theorem 1. Notice that
det(1 −w)Tξ(Ξ un) ≥ 0
because Tξ(Ξ un) is a real representation of the ﬁnite group Wξ. Clearly det(1 −
w)Tξ(Ξ un) ⁄= 0 if and only if w acts without ﬁxed points on Tξ(Ξ un) \ {0}, in which
case we say that w is elliptic in Wξ.
Given π ∈ Modf,un,Wξ(S), Theorem 1.5.d produces a representation E−1
ξ (π) =
HomH(π,π (ξ)) of C[Rξ,κ ξ]. Explicitly, this means
(34) E−1
ξ (π)(w1)E−1
ξ (π)(w2)E−1
ξ (π)(w1w2)−1 =κξ(w1,w 2) for all w1,w 2 ∈ W ξ,
A variation on (34) shows that the dual space E−1
ξ (π)∗ is a representation of C[Rξ,κ −1
ξ ].
Ifπ′ ∈ Modf,un,Wξ(S), then E−1
ξ (π)∗ ⊗E−1
ξ (π′) is a representation of C[Rξ, 1], that
is, of the group Rξ. Its trace is
(35) tr E−1
ξ (π)∗⊗E−1
ξ (π′)(r) = trE−1
ξ (π)(r) trE−1
ξ (π′)(r).
It is an elementary result in homological algebra that, for t he purpose of comput-
ing Euler–Poincar´ e-pairings, one may replace any module b y its semisimpliﬁcation.
Hence in the next theorem it suﬃces to compute EPH(π,π ′) for π,π ′ ∈ Modf,Wξ(S)
irreducible. Recall that irreducible tempered modules are unitarizable [DeOp1,
Corollary 3.23]. In particular Theorem 1.5.d applies to π and π′.
A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS 15
Theorem 3.1. Letπ,π ′ ∈ Modf,Wξ(S) be irreducible tempered H-modules. Denote
byρ :=E−1
ξ (π) andρ′ :=E−1
ξ (π′) the irreducible modules of C[Rξ,κ ξ] corresponding
to π and π′ respectively (according to Theorem 1.5). Then we have:
EPH(π,π ′) = |Rξ|−1 ∑
r∈Rξ
det(1 −r)Tξ(Ξ un)trρ(r) trρ′(r).
Proof. Our strategy is to consider π andπ′ as modules over various algebras A, such
that the extension groups Ext n
A(π,π ′) for diﬀerent A’s are all isomorphic.
Writeξ = (P,δ,t ). By (33), (21) and (22) we may replace H ﬁrst by S and then
by
(36)
(
C ∞(T P
un) ⊗ EndC(C[W P ] ⊗Vδ)
) WP,δ.
Let Uξ ⊂T P
un be a nonempty open ball around t such that
Uξ ∩wUξ =
{
Uξ if w ∈ W ξ
∅ if w ∈ W P,δ \ Wξ.
The localization of (36) at Uξ is
C ∞(Uξ)Wξ ⊗C∞(T Pun)WP,δ
(
C ∞(T P
un) ⊗ EndC(C[W P ] ⊗Vδ)
) WP,δ
∼=
(
C ∞(Uξ) ⊗ EndC(C[W P ] ⊗Vδ)
) Wξ.
(37)
As localization is an exact functor, this preserves the Ext- groups, up to a natural
isomorphism. The action of Wξ on C ∞(Uξ) ⊗ EndC(C[W P ] ⊗Vδ) is still deﬁned by
(20), so for w ∈ W ξ and t′ ∈Uξ
(38) ( w ·f )(t′) = π(w,P,δ,w −1t′)f (w−1t′)π(w,P,δ,w −1t′)−1.
LetVξ be the vector space C[W P ] ⊗Vδ endowed with the H-representationπ(ξ). It
is also a projective Wξ-representation, so we can deﬁne a Wξ-action on C ∞(Uξ) ⊗
EndC(Vξ) by
(39) ( w ·f )(t′) = π(w,ξ )f (w−1t′)π(w,ξ )−1.
The diﬀerence between (38) and (39) is that π(w,P,δ,w −1t′) depends on t′, while
π(w,ξ ) does not. Since Uξ is Wξ-equivariantly contractible to t, we are in the right
position to apply [Sol1, Lemma 7]. Its proof, and in particul ar [Sol1, (20)] shows
that the algebra (37), with the Wξ-action (38), is isomorphic to
(40)
(
C ∞(Uξ) ⊗ EndC(Vξ)
) Wξ,
with respect to the Wξ-action (39). By Theorem 1.5.a the elements of W (Rξ) do
not really act on End C(Vξ), only on C ∞(Uξ). Moreover by (29) W (Rξ) is normal in
Wξ and Wξ/W (Rξ) ∼= Rξ, so we can rewrite (40) as
(41)
(
C ∞(Uξ)W (Rξ) ⊗ EndC(Vξ)
) Rξ.
Using suitable coordinates on Uξ, we can identify it as a Wξ-representation with
Tξ(Ξ un). By Chevalley’s Theorem [Che, Hum] the algebra O(Tξ(Ξ un))W (Rξ) is a
free polynomial algebra on dim T P
un generators. With [Bie, Theorem 3] or [Schw]
one can extend Chevalley’s Theorem to smooth functions. Exp licitly, this means
that Uξ/W (Rξ) is a manifold with corners such that
(42) C ∞(Uξ)W (Rξ) ∼=C ∞(
Uξ/W (Rξ)
) ∼=C ∞(
Rdim T P
un
)
.
16 ERIC OPDAM AND MAARTEN SOLLEVELD
We insert (42) in (41) to obtain
(43)
(
C ∞(
Uξ/W (Rξ)
)
⊗ EndC(Vξ)
) Rξ.
Let κξ : Rξ × Rξ → C× be the cocycle from Theorem 1.5.b and let R∗
ξ be a Schur
extension of Rξ (also known as a representation group, see [CuRe, Section 53 ]).
There is a central idempotent p ∈ C[R∗
ξ] such that
C[Rξ,κ ξ] ∼=pC[R∗
ξ]
as algebras and as C[Rξ]-bimodules. By Theorem 1.5.c every irreducible represen-
tation of C[Rξ,κ ξ] appears at least once in Vξ, so by Theorem 4.1.a (43) is Morita
equivalent to
(44)
(
C ∞(
Uξ/W (Rξ)
)
⊗ EndC(pC[R∗
ξ])
) R∗
ξ.
Under this Morita equivalence π corresponds to a representation π1 of (44) such
that
ρ := Hom H(π,π (ξ)) ∼= Hom(
C∞
(
Uξ/W (Rξ)
)
⊗EndC(Vξ)
) Rξ (π,π (ξ))
∼= Hom(
C∞
(
Uξ/W (Rξ)
)
⊗EndC(pC[R∗
ξ ])
) R∗
ξ (π1,p C[R∗
ξ]),(45)
as R∗
ξ-representations. Since p is central and by Theorem 4.1.b, (44) is isomorphic
to
(46) p
(
C ∞(
Uξ/W (Rξ)
)
⊗ EndC(C[R∗
ξ])
) R∗
ξ ∼=p
(
C ∞(Uξ/W (Rξ)) ⋊ R∗
ξ
)
.
This is a direct summand of C ∞(Uξ/W (Rξ))⋊R∗
ξ , so we can consider the Ext-groups
of π1 and π′
1 just as well with respect to C ∞(Uξ/W (Rξ)) ⋊ R∗
ξ. More precisely, by
Theorem 4.1.c and (45) we get
(47) Ext n
H(π,π ′) ∼= Extn
C∞(Uξ/W (Rξ))⋊R∗
ξ
(π2,π ′
2),
where π2 admits the C ∞(Uξ/W (Rξ))-character R∗
ξt and π2
⏐⏐
R∗
ξ
∼= ρ∗, and similarly
for π′
2 and ρ′.
Now that we took enough reduction steps, we can resort to more direct calcu-
lations. The simple structure of C ∞(Uξ/W (Rξ)) ⋊ R∗
ξ allows one to construct an
analogue of the Koszul resolution, which was used in [OpSo1, Theorem 3.2.c] to
show that
(48) EPC∞(Uξ/W (Rξ))⋊R∗
ξ
(π2,π ′
2) = eR∗
ξ (π2,π ′
2) = eR∗
ξ (ρ∗,ρ ′∗).
Following [Ree], eR∗
ξ denotes the elliptic pairing of R∗
ξ-representations, with respect
to the representation of R∗
ξ on the tangent space Tt(Uξ/W (Rξ)) of Uξ/W (Rξ) at t.
Of course this is imprecise, as the orbifold Uξ/W (Rξ) has a corner at t. To make
more sense of it, one uses (42) and reinterprets Tt(Uξ/W (Rξ)) as the tangent space
of Rdim T P
un at 0. These identiﬁcations can be made Rξ-equivariantly, soT0
(
Rdim T P
un
)
becomes a Rξ-representation.
According to [Ree, Section 2], the right hand side of (48) equ als
|R∗
ξ|−1 ∑
r∈R∗
ξ
det(1 −r)Tt(Uξ/W (Rξ))trπ2(r)trπ′
2
(r) =
|R∗
ξ|−1 ∑
r∈R∗
ξ
det(1 −r)Tt(Uξ/W (Rξ))trρ(r)trρ′(r).
(49)
A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS 17
Notice that this formula does not use the entire action of R∗
ξ onTt(Uξ/W (Rξ)), only
det(1 −r)Tt(Uξ/W (Rξ)). This determinant is zero whenever r ∈ R∗
ξ ﬁxes a nonzero
vector inTt(Uξ/W (Rξ)). Suppose that Rξ is nonempty. Then R∨
ξ is a nonempty root
system in aP and RR∨
ξ can be identiﬁed with a subspace of Tt(Uξ). Every r ∈ R∗
ξ
ﬁxes ∑
α∈R+
ξ
α∨ ∈ aP \ {0}, so r ﬁxes nonzero vectors of Tt(Uξ) and Tt(Uξ/W (Rξ)).
We conclude that
det(1 −r)Tt(Uξ/W (Rξ)) = 0 = det(1 −r)Tt(Uξ)
whenever Rξ is nonempty. Therefore we may always replace Tt(Uξ/W (Rξ)) by
Tt(Uξ) = Tξ(Ξ un) in (49). So by (47), (48) and (49)
(50) EPH(π,π ′) = |R∗
ξ|−1 ∑
r∈R∗
ξ
det(1 −r)Tξ(Ξ un)trρ(r)trρ′(r).
Finally we want to reduce from R∗
ξ to Rξ. The action of R∗
ξ on Tξ(Ξ un) is deﬁned
via the quotient map R∗
ξ → Rξ, so that is no problem. We noted in (35) that ρ ⊗ρ′∗
is a Rξ-representation with trace
trρ⊗ρ′∗(r) = tr ρ(r)trρ′(r).
Hence any two elements of R∗
ξ with the same image in Rξ give the same contribution
to (50). Furthermore EPH is symmetric by Theorem 2.1.b, so
EPH(π,π ′) = EPH(π′,π ) = |Rξ|−1 ∑
r∈Rξ
det(1 −r)Tξ(Ξ un)trρ′(r)trρ(r). ✷
Remark 3.2. The proof of Theorem 3.1 relies on three deep results: the Knapp –
Stein linear independence theorem (Theorem 1.5), the isomor phism Ext∗
H ∼= Ext∗
S
for tempered representations (32) and the Plancherel isomorphism for S (21). Since
these three theorems are also known for all reductive p-adic groups (as we indicated in
some remarks) the proof of Theorem 3.1 applies equally well to the Euler–Poincar´ e
pairing for admissible tempered representations of reduct ive p-adic groups. This
proves Theorem 2.

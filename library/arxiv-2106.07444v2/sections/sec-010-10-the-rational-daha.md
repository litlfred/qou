---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-010-10-the-rational-daha
section_title: "The Rational DAHA"
section_number: 10
pages: 64-71
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the W eyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
10.1. As in the previous section, we do not assume that W is crystallographic. Let
Ref(W ) ⊆W be the subset of elements that act on V by reﬂections, cf. §A.10. We
continue to assume that VW = 0.
We write ⟨−, −⟩ : V × V∨ → QW for the evaluation pairing. For each reﬂection
t ∈ Ref(W ), we ﬁx nonzero vectors αt ∈ V and α∨
t ∈ V∨ such that
(1) ⟨αt, −⟩ = 0 is the hyperplane of V∨ ﬁxed by t.
(2) ⟨−,α ∨
t ⟩ = 0 is the hyperplane of V ﬁxed by t.
(3) ⟨αt,α ∨
t ⟩ = 2.
In the literature, the vectors αt and α∨
t are called roots and coroots even when
W is not crystallographic. Condition (3) will ensure that in w hat follows, our
constructions do not depend on the exact choices of αt,α ∨
t .
For anyν ∈ C, the rational Cherednik algebra or rational DAHA of slope
ν is the C-algebra
Drat
ν = C[W ] ⋉ (Sym(V) ⊗ Sym(V∨))⟨
yx −xy − ⟨x,y ⟩ +ν
∑
t∈Ref(W )
⟨x,α ∨⟩⟨α,y ⟩t :x ∈ V, y∈ V∨
⟩ .
Note that Drat
ν contains AW = C[W ] ⋉ Sym(V) as a subalgebra, regardless of ν.
Remark 10.1.1. Ifν = 0, then the deﬁning relations of Drat
ν simplify to [x,y ] = ⟨x,y ⟩
for all x andy. This shows that Drat
0 is isomorphic to C[W ] ⋉ D(V), the semidirect
product of C[W ] with the Weyl algebra of V.
10.2. Like the universal enveloping algebra of a semisimple Lie algebra, Drat
ν ad-
mits a triangular decomposition in the sense of Poincaré–Bi rkhoﬀ–Witt. It therefore
admits an analogue of the Bernstein–Gelfand–Gelfand categ ory O, which we will
denote by Oν [GGOR].
Any Drat
ν -moduleM ∈ Oν can be viewed as a W -equivariant quasicoherent sheaf
on V∨ = Spec Sym(V). The support of M is the W -stable subvariety of V∨ that
forms its support as a sheaf. Let Otor
ν ⊆ Oν be the Serre subcategory of modules
that are torsion over Sym( V∨) ⊆ Drat
ν . By [ GGOR, Lem. 5.1], Otor
ν is also the full
subcategory of Oν of modules supported on the discriminant locus of V∨, i.e., the
common complement of the reﬂection hyperplanes of the W -action.
The Verma modules in Oν are indexed by the set ˆW . For all φ ∈ ˆW , we write
∆ν (φ) for the corresponding Verma module of Drat
ν , and we write Lν(φ) for its
simple quotient. Explicitly, ∆ ν(φ) can be constructed by inﬂating φ from C[W ]
up to AW , then tensoring up to Drat
ν . In the literature, ∆ ν(1) is known as the
polynomial module and Lν(1) as the simple spherical module.
Like the Weyl algebra of V, the rational Cherednik algebra contains a canonical
“Euler element” h. For the precise deﬁnition, see [ E07, Ch. 11]. It commutes with
the subalgebra C[W ] ⊆ Drat
ν , and its action on any object of Oν is locally ﬁnite.
Thus, each object M ∈ O is endowed with a decomposition into ﬁnite-dimensional,
W -stable h-eigenspaces. On all Drat
ν -modules that we will need, the eigenvalues
will be half-integers. We deﬁne the q-graded character of such a module M to
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 65
be
[M ]q =
∑
n
q
n
2M n
2 ∈R(W )( (q
1
2 ) )
where M n
2 ⊆M is the h-eigenspace of eigenvalue n
2 . By [ E07, Ch. 11],
[∆ν (φ)]q = q
r
2 −νc(φ)φ · [Sym(V)]q(29)
for all φ ∈ ˆW , where we set [Sym( V)]q =∑
i qi Symi(V) as in Sections 7-8 and
§A.6 of Appendix A.
The basic problem in the representation theory of Drat
ν is to understand how the
graded characters [∆ ν (φ)]q, which are explicit, can be used to express the graded
characters [Lν(φ)]q, which are initially mysterious. The problem is highly sens itive
to the value of ν. When ν /∈ Q, category O is semisimple and [ Lν(φ)]q = [∆ν (φ)]q.
When ν ∈ Q, category O is no longer semisimple: It grows more complex as the
denominator of ν grows smaller.
10.3. Let ζ
1
2 =eπiν . We draw freely upon the notation in § A.11, so that
HW (ζ
1
2 ) = HW ⊗Z[q± 1
2 ] QW (ζ
1
2 )
and dζ :R+(HW (q
1
2 )) →R+(HW (ζ
1
2 )) is the decomposition map that corresponds
to the specialization q
1
2 ↦→ζ
1
2 . Let Mod(HW (ζ
1
2 )) be the category of HW (ζ
1
2 )-
modules, and for each φ ∈ ˆW , let
φζ = dζ(φq) ∈ Mod(HW (ζ
1
2 )).
In [ GGOR], Ginzburg, Guay, Opdam, and Rouquier introduced the Knizhnik–
Zamolodchikov (KZ) functor , an exact monoidal functor
KZ : Oν → Mod(HW (ζ
1
2 )).
The following facts comprise [ GGOR, Thm. 5.14, Cor. 5.18, Thm. 6.8]:
Theorem 10.3.1 (Ginzburg–Guay–Opdam–Rouquier). For all ν ∈ C,
(1) KZ induces an equivalence Oν/Otor
ν ≃ Mod(HW (ζ
1
2 )).
(2) KZ induces an isomorphism between the (vertical) center of Oν , i.e., the
algebra of endomorphisms of its unit object, and the center o f HW (ζ
1
2 ).
(3) KZ(∆ν (φ)) = φζ.
10.4. As preparation for the proofs of Corollary 11 and Theorem 12, we introduce
some subsets of Q depending on ν. It will be convenient to write {di}i∈I(W ) for
the multiset of invariant degrees of W . For any slope ν ∈ C, let
Iν (W ) = {i ∈I(W ) : ν ∈ 1
di
Z}.
Concretely, if n is the denominator of ν in lowest terms, then Iν (W ) is the set of
indices i such that n divides the invariant degree di.
Deﬁnition 10.4.1. If ν ∈ Q and ζ =e2πiν , then we say that ν is:
(1) A singular slope iﬀ |Iν (W )| ≥ 1.
66 MINH-TÂM QUANG TRINH
(2) A regular slope iﬀ W contains a ζ-regular element.
(3) A regular elliptic slope iﬀ W contains a ζ-regular element w such that
Vw = 0. (Recall that we assume VW = 0.)
(4) A cuspidal slope iﬀ |Iν (W )| = 1.
We say that an integer n> 0 is a singular number , etc., iﬀ it is the denominator
in lowest terms of a singular slope, etc.
Lemma 10.4.2. There is a chain of implications:
cuspidal =⇒ regular elliptic =⇒ regular =⇒ singular.
Proof. It is tautological that regular elliptic implies regular. T hat regular implies
singular follows from [ S74, Thm. 4.2(iii)]. That cuspidal implies regular elliptic is
[BE, Rem. 3.28]. □
Example 10.4.3. In typeAr, the invariant degrees are 2, 3, 4,...,r +1. An integer
is regular if and only if it is a divisor of either r orr +1 [ S74, §5.1]. The only regular
elliptic number is the Coxeter number r + 1 [ VV, Ex. 1.1.2].
Example 10.4.4. In type BCr, the invariant degrees are 2, 4, 6,..., 2r. An integer
is regular, resp. regular elliptic, if and only if it is a divisor of 2 r [S74, §5.2], resp.
an even divisor of 2 r [VV, Ex. 1.1.2]. To demonstrate: In type BC5:
• The singular numbers are 1 , 2, 3, 4, 5, 6, 8, 10.
• The regular numbers are 1 , 2, 5, 10.
• The regular elliptic numbers are 2 , 10.
• The only cuspidal number is 10, the Coxeter number.
This is a minimal example where each implication in Lemma 10.4.2 is strict.
Throughout the rest of this section, we assume ν ∈ Q and set ζ
1
2 = eπiν . We
form the virtual Drat
ν -module
Ων =
⨁
φ∈ ˆW
Degφ(e2πiν )∆ν(φ).
We can immediately prove part (1) of Theorem 12, stating that Lν(1) occurs in Ω ν
with multiplicity one. Indeed, we have D1(q) = 1, and for any ν, the only Verma
module that contains Lν(1) as a constituent is ∆ ν (1).
10.5. Singular Slopes. We prove part (2) of Theorem 12, stating that if ν is
singular, then Ων ∈ Otor
ν .
Lemma 10.5.1. We have
∑
φ∈ ˆW
Dφ(q)φq(σw) =
{
s(1q) w = 1
0 w ⁄= 1
in QW (q
1
2 ).
Proof. IfW ≃W1 ×W2, then Dφ1×φ2(q) = Dφ1(q) ·Dφ2(q) for all φi ∈ ˆWi. So we
can assume that W is irreducible. After checking the non-crystallographic t ypes by
hand, we can further assume that W is crystallographic.
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 67
Henceforth, we will use the notations and hypotheses of Sect ion 8. Recall that
by (23), we have
R1 ≃
⨁
φ∈ ˆW
V
⊕Degφ(q)
φ,q
asHW (q
1
2 )-modules, where Vφ,q is a free HW (q
1
2 )-module that admits the character
φq. From ( 21), we deduce that:
(1) σ1 acts on R1 by the identity operator. Its trace is |BF |.
(2) If w ⁄= 1, then σw acts on R1 by an operator with zeros along the diagonal.
Since |BF | = s(1q)|q=q, we are done. □
By Theorem 10.3.1(1), it remains to show that the HW (ζ
1
2 )-module KZ(Ων ) is
the zero module. By Theorem 10.3.1(3), we have
KZ(Ων ) =
∑
φ∈ ˆW
Degφ(ζ)φζ.
This coincides with the image of the virtual HW (q
1
2 )-module∑
φ Degφ(q)φq under
the decomposition map from § A.11. So by Lemma 10.5.1, it remains to show
s(1q)|q1/2=ζ1/2 = 0.
This follows from the Bott–Solomon formula [ Sol]
s(1q) =
∏
i∈I(W )
1 − qdi
1 − q(30)
together with the deﬁnition of singular slope.
10.6. Regular Slopes. We prove Corollary 11, stating that if β is periodic of slope
ν, then [Ω ν ] = ( q
1
2 )r−|β| · ⟨β⟩ 0
q. On the one hand,
(−q− 1
2 )|β|⟨β⟩ 0
q = ⟨β⟩ q ·ε[Sym(V)]q
=ε
∑
φ∈ ˆW
qνc(φ)Degφ(ζ)φ · [Sym(V)]q
by Theorems 5 and 10. On the other hand,
∑
φ∈ ˆW
Degφ(ζ)[∆ν (φ)]q = q
r
2
∑
φ∈ ˆW
q−νc(φ)Degφ(ζ)φ · [Sym(V)]q
= q
r
2ε
∑
φ∈ ˆW
qνc(φ)Degεφ(ζ)φ · [Sym(V)]q
by (29) and the identity c(εφ) = −c(φ). Since |β| =ν|π|, it remains to check:
Lemma 10.6.1. If ν ∈ Q is a regular slope and ζ =e2πiν , then
Degεψ(ζ) = ( −1)ν|π|Degψ(ζ)
for all ψ ∈ ˆW .
68 MINH-TÂM QUANG TRINH
Proof. Pick aζ-regular elementw ∈W . By the discussion in Section 9 and Lemma-
Postulate A.9.1(3),
Degεψ(ζ) =
∑
φ∈ ˆW
{φ,εψ }φ(w)
=
∑
φ∈ ˆW
{φ,ψ }(εφ)(w)
=ε(w)Degψ(ζ).
Finally,ε(w) = ( −1)ν|π| because |w| = |σw| = (ν − ⌊ν⌋)|π|. □
10.7. Regular Elliptic Slopes. We prove part (3) of Theorem 12, stating that if
ν is regular elliptic, ν >0, and W is a Weyl group, then [Ω ν ]q ∈R(W )[q± 1
2 ].
Writeν = m
n , where m,n > 0. Since 1
n is also a regular elliptic slope, we can
pick a e
2πi
n -regular element w ∈W such that Vw = 0. By Proposition 9.3.4, σm
w is
periodic of slope ν, so by Corollary 11,
[Ων ]q ∈ ⟨σw⟩ 0
q ·R(W )[q± 1
2 ].
But W is a Weyl group, so by Theorem 9, the condition Vw = 0 implies that
⟨σw⟩ 0
q ∈R(W )[q].
10.8. Cuspidal Slopes. We prove part (4) of Theorem 12, stating that if ν is
cuspidal and positive, then
[Ων ]q =
∑
ψ∈ ˆW1
[Lν(ψ)]q,
where ˆW1 ⊆ ˆW is the set of elements of greatest a-value within their ζ-blocks,
among the ζ-blocks of HW of defect 1 in the sense of § A.11.
Lemma 10.8.1. Ifζ
1
2 =eπiν , then the ζ-defect of the principal ζ-block of HW (q
1
2 )
equals |Iν (W )|.
Proof. The Bott–Solomon formula ( 30) can be rewritten
s(1q) =
∏
n≥1
Φn(q)|{i∈I(W ) :n divides di}|,
where Φn is the minimal polynomial of e
2πi
n over QW . □
Lemma 10.8.2. Theζ-defect of any ζ-block ofHW (q
1
2 ) is bounded above by Iν(W ).
Equality holds if and only if Degφ(ζ) ⁄= 0. Moreover, if |Iν (W )| ≤ 1, then there are
two kinds of blocks:
(1) Any block of defect 0 is a singleton. For φ in such a block, Degφ(ζ) = 0 .
(2) Any block of defect 1 is a line of characters ordered by a-value. If
{φ0>φ 1> · · ·>φ n−1}
is such a block, then Degφk (ζ) = ( −1)k for all k.
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 69
Proof. The only claim that does not follow from Theorem A.12.1 and Lemma 10.8.1
is the claim about generic degrees in case (2). Recall that, b y deﬁnition,
Degφk (ζ) = s(1q)
s(φk,q)
⏐⏐⏐⏐
q1/2→ζ1/2
.
By work of Broué, such ratios of Schur elements at roots of uni ty are Morita in-
variants of the block ideal [ Br, §3.7]. (Strictly speaking, Broué worked with group
algebras, not Iwahori–Hecke algebras, but see the footnote on [ CM, 286].) Thus,
by Theorem A.12.1(2), these ratios match the corresponding ratios for the Bra uer
tree algebra of type An−1. In this way, we reduce to the setting where W = Sn
and ν = 1
n . Here, we have φk = Λk(V), so it remains to show that
DegΛ k(V)(e
2πi
n ) = ( −1)k.
Let w be an e
2πi
n -regular element of W . By [ J, Rem. 3.7], the right-hand side
above equals tr(w | Λk(V )). By Lemma-Postulate A.9.1(2) and Theorem 9.3.2, the
left-hand side also equals tr( w | Λk(V )). □
We return to the proof of Theorem 12(5). Since ν is cuspidal, Theorem 12(3)
and Lemma 10.8.2 together imply:
[Ων ]q =
∑
Γ= {φΓ
k }k
∑
k
(−1)k[∆ν (φΓ
k )]q,
where the outer sum runs over ζ-blocks of HW (q
1
2 ) of defect 1. To conclude, we
claim that the inner sum on the right-hand side simpliﬁes to [ Lν(φΓ
0 )]q, where φΓ
0
is the element of greatest a-value in the block Γ. Indeed, this follows from the
theorem below, itself a corollary of Theorem 10.3.1(2).
Theorem 10.8.3. Suppose that {φ0 > φ1 > · · ·> φn−1} is a ζ-block of HW (q
1
2 ),
ordered by a-value. Then, in Oν, there is a “Bernstein–Gelfand–Gelfand” resolution
of Lν(φ0) of the form
∆ν (φn−1) → · · · → ∆ν(φ1) → ∆ν(φ0) →Lν(φ0) → 0.
In particular, we have
[Lν(φ0)]q =
∑
0≤k≤n−1
(−1)k[∆ν (φk)]q
in R(W )[ [q] ].
Remark 10.8.4. We believe that the ﬁrst appearance of this theorem in the lit erature
is [ R08, Thm. 5.15]. The type A case was used much earlier, in [ BEG-2].
10.9. Cuspidal Slopes, cont. We prove Corollary 13.
There are only two cases where W is an irreducible Coxeter group, ν is a cuspidal
slope, and there is a ζ-block of HW (q
1
2 ) of defect 1 besides the principal block.
Namely, W must be of type E8 or type H4 and the denominator of ν in lowest
terms must be 15.
In these cases, there is one other ζ-block of defect 1 and its element of greatest
a-value is the character of V, assuming as before that VW = 0. We refer to these
70 MINH-TÂM QUANG TRINH
as the two exceptional cases for ( W,ν ). Parts (3)-(4) of Theorem 12 now imply
the following stronger form of Corollary 13:
Corollary 10.9.1. If W is irreducible and ν is cuspidal, then:
[Ων ]q =
{
[Lν(1)]q + [Lν(V)]q (W,ν ) is exceptional
[Lν(1)]q else(31)
in R(W )[q]. In particular, the right-hand side is ﬁnite-dimensional.
Remark 10.9.2. This statement also recovers the observation of Bezrukavni kov–
Etingof [ BE, Rem. 3.31] that for irreducible W and cuspidal ν, the only ﬁnite-
dimensional simple Drat
ν -modules are those appearing on the right-hand side of
(31).
Remark 10.9.3. If W ≃W1 ×W2 and V ≃ V1 ⊕ V2, such that Vi is a realization
of Wi for i = 1, 2, then:
• |Iν (W )| = |Iν (W1)|+|Iν (W2)|, where the right-hand side is deﬁned in terms
of V1 and V2 rather than V.
• Category O for the rational Cherednik algebra of W is the tensor product
of the corresponding categories for W1 and W2.
So the above result can be generalized to any pair ( W,ν ) such that ν is cuspidal
with respect to each irredcible factor of W .
10.10. To conclude this section, we explain how to deduce [ GORS, Thm. 1.1] from
Corollaries 13 and 7.4.6.
For W = Sn, we have r = n − 1 and |π| = n(n − 1). Let si ∈ Sn be the
transposition (i i+ 1). Then the (positive) ( m,n ) torus knot is the link closure of
β = (σs1 · · ·σsn−1)m ∈ Br +
W,
a periodic braid of slope m
n . Since n is the Coxeter number of Sn, it is a cuspidal
number for Sn. Corollary 13 gives
[Lν (1)]q = [Ων ]q = (q
1
2 )r−|β| · ⟨β⟩ 0
q.
Since |β| −n + 1 = m
n |π| − (n − 1) = (m − 1)(n − 1), Corollary 7.4.6 gives
[ ˆβ]a,q =a(m−1)(n−1) ∑
0≤i≤n−1
(−a2)i(Λi(V), [Lν (1)]q)W.
This is [ GORS, Thm. 1.1].
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 71

---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-038-31-vanishing-theorems-revisited-45
section_title: "Vanishing theorems revisited 45"
section_number: 3.1
pages: 53-54
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
Let B be an arbitrary variety over the ﬁeldk, and let f : Y−→B be a
torsor under the torusT. By remark 4.8(a) in loc. cit. there exists an´etale
coveringB′−→B (not necessarily ﬁnite) over which our torsor admits a
trivialization.
Y×B B′ ∼= //
##GGGGGGGGG T×k B′
{{xxxxxxxxx
B′
Let us denote byi :Yb = f−1(b)−→Y the ﬁbre over some chosen geometric
pointb∈ B(k). In what follows we ﬁx a base pointy∈Yb(k) and denote the
group of all continuous characters of the tame fundamental groupπt
1(Yb,y)
as above byΠ(Yb), and similarly forΠ(Y). Since Yb is isomorphic to the
torusT, the character groupΠ(Yb) can be identiﬁed with the set of closed
points of a scheme as explained above. In particular, it makes sense to speak
about its irreducible components.
LEMMA 3.2. In the above setting, for every perverse sheaf P∈ P(Y)
there exists a subset U⊆ Π(Yb) which meets every irreducible component
and has the property that the forget support morphism
R f!(Pχ)−→R f∗(Pχ)
is an isomorphism for all charactersχ∈ Π(Y) with pull-back i∗(χ)∈U.
Proof.Let g : B′−→B be an ´etale covering which trivializes the given
torsor in the sense that the pull-backY′ = Y×B B′ is isomorphic overB′
to the trivial torsorT×k B′. Choosing a geometric pointb′∈ B′(k) with
imageg(b′) =b, we have a commutative diagram
Yb
i′
//

i
%%
Y′
f′

g′
// Y
f

Spec(k) b′
//
b
99B′ g // B
where the two squares are Cartesian. Sinceg is an´etale covering, the forget
support morphismR f!(Pχ)−→R f∗(Pχ) is an isomorphism iff its pull-back
underg∗ is an isomorphism. For the pull-backP′ = g′∗(P) and χ′ = g′∗(χ)
46 Chapter 3 – Perverse sheaves on semiabelian varieties
we have a commutative diagram
g∗(R f!(Pχ)) //
∼=

g∗(R f∗(Pχ))
∼=

R f′
!(P′
χ′) // R f′∗(P′
χ′)
where the vertical arrows are isomorphisms due to the smooth base change
theorem [38, th. I.7.3]. Furthermore, by constructioni′∗(χ′) =i∗(χ). Hence
it will be enough to prove the lemma in the case of the trivial torsor, and this
has been done in [41, cor. 2.3.2]. □
Let us now return to our semiabelian varietyX. For later reference it will
be convenient to reformulate the observation in theorem 3.1 in the following
equivalent way.
COROLLARY 3.3. Suppose that A= X/T satisﬁes axiom GV(A), and
let K∈ D(X) be a constructible sheaf complex. For all degrees r∈ Z and a
generic characterχ∈ Π(X) then
Hr
c(X,Kχ)∼= Hr(X,Kχ)∼= H0(X, pHr(K)χ),
where the ﬁrst isomorphism is induced by the forget support morphism.
Proof.For the perverse cohomology groupsPr = pHr(K) and χ∈ Π(X)
we have(Pr)χ = pHr(Kχ) since twisting byχ is a t-exact functor for the
perverset-structure. Only ﬁnitely manyPr are non-zero, so for genericχ
and allr theorem 3.1 says that the hypercohomology groupsHsc(X,(Pr)χ)
and Hs(X,(Pr)χ) will be isomorphic to each other via the forget support
morphism, and vanish for alls⁄= 0. Then the spectral sequences
Ers
2 = Hs(X,(Pr)χ) =⇒ Hr+s(X,Kχ)
Ers
2 = Hs
c(X,(Pr)χ) =⇒ Hr+s
c (X,Kχ)
degenerate, and our claim follows since the forget support map between the
limit terms is induced from the one between theE2-terms. □

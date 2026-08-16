---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-061-44-degenerations-of-abelian-varieties-83
section_title: "Degenerations of abelian varieties 83"
section_number: 4.4
pages: 91-93
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
in lemma 4.11. We choose the points such that the corresponding ppav and
its theta divisor have the form
Xs = X1×X2 resp. Θs = ( Θ1×X2)∪(X1×Θ2),
where forα∈{ 1,2} the Xα are general complex ppav’s of dimensiongα
with a symmetric theta divisorΘα. In particular, like for any divisor with
two components which intersect each other transversally along a smooth
subvariety, we have an exact sequence
0−→δΘ1×Θ2−→ΛΘs[g−1]−→δΘ1×X2⊕δX1×Θ2−→0
of perverse sheaves. Restricting this short exact sequence to the open dense
subset
V = Xs\Sing(ΘS)⊂ Xs
we get a monomorphism
δΘ1×Θ2|V ↪→ ΛΘs[g−1]|V = sp(δΘη)|V
of perverse sheaves, where the last equality holds by the formula for the
specialization in corollary 4.10. Now by the last statement in lemma 4.11
we can assume that the singular locusSing(ΘS) is a proper closed subset
of Sing(Θs) = Θ1×Θ2, and in this case the open dense subsetV will have
non-empty intersection withΘ1×Θ2. Then via intermediate extension it
follows from the above that the semisimpliﬁcation ofsp(δΘη) contains a
direct summandδΘ1×Θ2. By the properties of the monodromy ﬁltration
in section 4.3 the same then a fortiori holds for the semisimpliﬁcation of
the perverse sheaf of nearby cyclesΨ(δΘη). This being said, our claim
follows from the elementary observation that the Tannaka groupG(δΘ1×Θ2)
is isogenous toG(δΘ1)×G(δΘ2).
For part (2) lets∈ Ag,n(C) be a point which corresponds to a general
ppav Xs with a vanishing theta null, and letS ↪→ Ag,n be a general curve
which passes throughs but is otherwise contained in the open stratumU0
and has the properties in lemma 4.11. For the special ﬁbre with a vanishing
theta null we know from [26] with the correction given in [53, rem. 4.5],
or alternatively also from theorem 4.2 of loc. cit., that the theta divisorΘs
has an isolated ordinary double pointe as its only singularity. Hence the
Picard-Lefschetz formula [32, exp. XV , th. 3.4] says that
χ(Θs) = χ(Θη) + (−1)g = (−1)g−1· (g!−1)
because the generic theta divisorΘη is smooth of dimensiong−1 with
Euler characteristic(−1)g−1· g! by the Gauss-Bonnet theorem. Now the
perverse intersection cohomology sheaf near an ordinary double point can
84 Chapter 4 – The Tannaka group of the theta divisor
be controlled explicitly, indeed lemma 4.16 below gives an exact sequence
of perverse sheaves
0−→ κg−→ ΛΘs[g−1]−→ δΘs−→0
for the skyscraper sheaf
κg =
{
δe(−g−2
2 ) if g is even,
0 if g is odd.
Hence it follows that
χ(δΘs) = χ(ΛΘs[g−1])−χ(κg) =
{
g!−2 if g is even,
g!−1 if g is odd.
On the other hand, by remark 4.7 we can assume that the nearby cycles
for our degeneration coincide with the unipotent nearby cycles. Then from
the formula for the specialization in corollary 4.10 one deduces that the
semisimpliﬁcation of the nearby cycles must have the form
Ψ(δΘη)ss = δΘs⊕γ
for some perverse skyscraper sheafγ supported on the singular pointe of
the special ﬁbre. Looking at the above Euler characteristics, one sees that
this skyscraper sheafγ must have rank two ifg is even, resp. rank one ifg
is odd. Now take a Levi splitting
Gs = G(δΘs) ↪→ G(Ψ(δΘη)),
and letW be the irreducible representation ofGs which corresponds to the
simple perverse sheafδΘs. In lemma 4.13 below we will see as a general
fact about irreducible theta divisors that the restriction ofW to the connected
componentH = G0s⊆ Gs remains irreducible, so our claim follows.
For part (3) consider the locusJ⊂ Ag,n of Jacobian varieties of smooth
projective curves of genusg. If a stratumUi⊆U has codimension at most
one in the open subsetU, then the closureUi⊆ Ag,n has codimension at
most one inAg,n. In this case it has been observed in [83, cor. (0.7)] that
the intersectionJ∩Ui is nonempty and hence of codimension at most one
in J. We can then ﬁnd a pointt∈Ui(C) which corresponds to the Jacobian
variety of a non-hyperelliptic smooth curve (indeed the hyperelliptic locus
has codimension greater than one inJ for g≥ 4). Now consider in the
closureUi a curve which meets the Jacobian locusJ in the chosen pointt
and is otherwise contained in the open dense subsetUi⊂Ui. Deﬁne
ϕ : S−→ Ag,n
to be the normalization of this curve, and chooses∈ S(C) to be any point
withϕ(s) =t. ThenXS→ S is a family of ppav’s whose geometric generic
ﬁbreXη is a ppav in the stratumUi and whose special ﬁbreXs is the Jacobian

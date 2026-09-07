---
doc_id: arxiv-2501.00914v2
doc_title: "L-SPACES AND KNOT TRACES"
section_id: sec-007-21-surface-homeomorphisms-and-fibered-knots
section_title: "Surface homeomorphisms and fibered knots"
section_number: 2.1
pages: 5-8
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
doc_brief: "L-SPACES AND KNOT TRACES — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
compact oriented surface with possibly empty boundary. By Thurston’s classification [Thu88],his
isotopic rel boundary to a mapφ: Σ→Σ such that
•there exists a possibly emptyreducing systemΓ⊂Σ consisting of a finite disjoint union of
simple closed curves which is fixed setwise byφ;
•ifSis a component of Σ\Γ andnis the smallest positive integer such thatφ n(S) =S,
thenφ n|S is freely isotopic to a periodic or pseudo-Anosov map. Whenn= 1,we refer to
this map andSas a periodic or pseudo-Anosov component ofhor Σ\Γ, accordingly.
We will assume that Γ is minimal with respect to inclusion, in which case it is unique up to isotopy
[BLM83, Theorem C] and is called thecanonical reducing systemforh. We refer to the pair (φ,Γ)
as theNielsen–Thurston formofh.
We will focus hereafter on the Nielsen–Thurston forms of monodromies of fibered knots inS3 and
their associatedclosed monodromies; we spend some time below establishing notation, terminology,
and some preliminary results specific to that setting.
LetK⊂S 3 be a fibered knot with fiber surface Σ and monodromy
h: Σ→Σ.
Then Σ has one boundary component andhrestricts to the identity on∂Σ. Following [HKM07],
his said to beright-veeringif for every properly embedded arcα⊂Σ, eitherαandh(α) are
isotopic rel boundary, orh(α) is to the right ofαnear each endpoint after these arcs are isotoped
to intersect minimally. We say simply thathisveeringif eitherhorh −1 is right-veering.
Let (φ,Γ) be the Nielsen–Thurston form ofh. The suspension of Γ in the mapping torus ofφ
is a collection of incompressible tori in the knot complementS 3\ν(K). The complement of these
tori consists of Seifert fibered pieces swept out by the periodic components of Σ\Γ, and hyperbolic
pieces swept out by the pseudo-Anosov components [Thu98].
Let Σ0 be the component of Σ\Γ containing∂Σ; we call this theoutermostcomponent of Σ\Γ.
Note thatφfixes Σ 0 setwise, and its restriction to Σ 0 is freely isotopic to a map
φ0 : Σ0→Σ 0
which is either periodic or pseudo-Anosov. Thefractional Dehn twist coefficient[HKM07]
c(h)∈Q
records the amount of twisting near∂Σ in this free isotopy, giving a measure of how veeringhis.
(Ifφ 0 is pseudo-Anosov, then 1/c(h) is thedegeneracy slope[GO89] of the suspension flow ofφ 0.)
When the outermost component is pseudo-Anosov, we have the following [HKM07,§3]:
Theorem 2.1.Ifφ 0 is pseudo-Anosov, thenhis veering if and only ifc(h)̸= 0.
Moreover, using work of Gabai [Gab97], Kazez–Roberts showed [KR13, Theorem 4.5] that these
twist coefficients are highly constrained for monodromies of fibered knots inS 3:
Proposition 2.2.IfK⊂S 3 is a fibered knot with monodromyh, then|c(h)|<1.
It follows from the discussion above thatKis hyperbolic if and only if the outermost mapφ 0 is
pseudo-Anosov and Γ =∅. In the periodic case, we have the following, cf. [Bud06, Theorem 2]:
Proposition 2.3.Ifφ 0 is periodic, then either
•Γ =∅andKis a(p,q)-torus knot, or
•Γ̸=∅and either
6 JOHN A. BALDWIN AND STEVEN SIVEK
–Kis a composite knot andΣ 0 is a planar surface, or
–Kis a(p,q)-cable knot of some other knot inS 3 andΣ 0 has genusg(T p,q).
In each case above,q≥2andgcd(p,q) = 1.
Proof.The first case is due to Seifert [Sei33]; the second is a special case of [KR13, Proposition 4.2].
The statement of that proposition did not include the case whereKis composite, but the proof
allows for the possibility that a closed orbit in the mapping torus ofϕ 0 is a meridian ofK. In this
case, Kazez–Roberts show thatc(h) = 0, which implies thatϕ 0 restricts to the identity on∂Σ⊂Σ 0.
It then follows from [BNS25, Lemma 2.6], which is really an application of [JG93, Lemma 1.1], that
ϕ0 is the identity on all of Σ0. But then the outermost piece of the JSJ decomposition ofS 3\ν(K),
given by the mapping torus ofϕ 0, is simplyY 0 = Σ0×S 1. From here, [Bud06] says that Σ 0 must
be a planar surface with at least three boundary components, and thatKis a connected sum of
the nontrivial knots whose complements are the connected components of (S 3\ν(K))\Y 0.□
Let ˆΣ = Σ∪Dbe the closed surface obtained by capping off the fiber ofKwith a disk, and let
ˆh: ˆΣ→ ˆΣ
be the map obtained by extending the monodromyhby the identity over the capping diskD. We
call ˆhtheclosed monodromyofK; note that its mapping torus isS 3
0(K). Let
ˆΣ0 = Σ0∪D.
Let ( ˆφ,ˆΓ) be the Nielsen–Thurston form of ˆh. The Nielsen–Thurston forms ofhand ˆhcan be very
different in general (for instance, they can be freely isotopic to pseudo-Anosov and periodic maps,
respectively), but this is ruled out under some mild hypotheses:
Theorem 2.4.If the monodromyhis veering andΣ 0 is not a pair of pants, then
• ˆΓ⊂Γandφagrees withˆφonΣ\Σ 0 = ˆΣ\ ˆΣ0;
•ifφ 0 is periodic, then the pseudo-Anosov components ofΣ\Γand ˆΣ\ ˆΓare equal;
•ifφ 0 is pseudo-Anosov, then ˆΓ = Γand the restriction ofˆφto ˆΣ0 is freely isotopic to a
pseudo-Anosov mapˆφ0 which agrees withφ 0 onΣ 0 and fixes one pointpinD.
In brief, the hypothesis thathis veering guarantees that ifφ 0 is pseudo-Anosov then its stable
and unstable invariant foliations have at least two prongs on∂Σ. This implies that Σ 0 caps off to
a pseudo-Anosov component with one additional fixed point in the capping disk while the other
components are unchanged. The hypothesis that Σ 0 is not a pair of pants guarantees that ifφ 0
is periodic then capping off preserves all pseudo-Anosov components. This theorem will be crucial
for understanding the fixed points of the pseudo-Anosov components of the closed monodromies of
L-space knots and more generally ffpf knots in our proof of Theorem 2.10.
Proof of Theorem 2.4.We first show thatφ 0 extends to a map
ˆφ0 : ˆΣ0→ ˆΣ0
of the same type (periodic or pseudo-Anosov) asφ 0. Ifφ 0 is periodic, then it rotates∂Σ by some
rational multiple of 2π, and we simply extend this rotation radially across the diskDto define ˆφ 0.
Now suppose thatφ 0 is pseudo-Anosov. By definition, this means that there is a pair of transverse
singular measured foliations (Fs,µs) and (Fu,µu) of Σ0, called thestableandunstablefoliations of
φ0, such that
φ0(Fs,µs) = (Fs,λ−1µs) andφ 0(Fu,µu) = (Fu,λµu),
L-SPACES AND KNOT TRACES 7
for some real numberλ>1. The interior singularities of these foliations have at least 3prongs, and
each of these foliations has some numbern≥1 ofboundary prongsending on∂Σ⊂∂Σ 0. Sinceφ 0
preserves the boundary prongs, the fractional Dehn twist coefficient ofhis given by
c(h) =k/n
for some integerk; see [HKM07,§3.2]. Sincehis veering, Theorem 2.1 says thatk̸= 0. Meanwhile,
Proposition 2.2 implies that|k|< n. It follows thatn≥2. In this case,φ 0 extends to a pseudo-
Anosov homeomorphism ˆφ0 of ˆΣ0, andF s andF u extend to stable and unstable foliations ˆFs and
ˆFu for ˆφ0 in which thenboundary prongs extend tonprongs meeting at pointpinD. The point
pis a singularity of these two foliations whenn≥3, and a smooth point whenn= 2; see Figure 1.
Note thatpis the unique fixed point of ˆφ 0 inD.
(For the reader interested in more details about how one extends the foliations and transverse
measures over the diskD, we take the following easy way out: a pseudo-Anosov homeomorphism of a
surface with boundary is, by definition, a map which restricts on the complement of the boundary to
a pseudo-Anosov map of the corresponding punctured surface. Capping off a boundary component
from this point of view corresponds simply to filling in the corresponding puncture with a point.)
Figure 1.The transverse foliations ˆFs and ˆFu onD, in the cases whereF s and
Fu each haven= 2,3,4 boundary prongs. Whenn= 2 the pointpat the center is
a smooth point of each foliation, while forn≥3 it is ann-pronged singular point.
It follows in either case that Γ is a reducing system for ˆhas well, and thus contains ˆΓ. Moreover,
ˆφis the extension ofφby the identity overD, and in particular agrees withφon
Σ\Σ 0 = ˆΣ\ ˆΣ0,
proving the first item of the theorem. For the other items, we analyze the difference Γ\ ˆΓ.
We first claim that Γ\ ˆΓ consists of components of∂ ˆΣ0. Indeed, ˆφfixes Γ and thus∂ ˆΣ0 setwise.
It follows that ˆΓ∪∂ ˆΣ0⊂Γ is also a reducing system for ˆh,and hence forhas well. But then the
minimality of Γ⊂Σ as the canonical reducing system forhimplies that
Γ = ˆΓ∪∂ ˆΣ0,
which proves our claim about Γ\ ˆΓ.
We next claim that every component of Γ is homotopically essential in ˆΣ, and that no two
components of Γ are freely homotopic in ˆΣ. Indeed, the analogous conditions hold for Γ⊂Σ by
the minimality of this reducing system, and the only way this fails upon capping off is if ˆΣ0 is a
disk or an annulus; equivalently, if Σ 0 is an annulus or a pair of pants. Minimality of Γ⊂Σ rules
out the first possibility, while the second is excluded by the hypotheses of the theorem.
8 JOHN A. BALDWIN AND STEVEN SIVEK
We now use these two claims to prove the rest of the theorem. The third item follows from what
we have already established if we can show that ˆΓ = Γ whenφ 0 is pseudo-Anosov, or equivalently
if we can show that ˆΓ̸= Γ implies that Σ 0 is not a pseudo-Anosov component of Σ\Γ.
Let us therefore assume that ˆΓ̸= Γ. Let ˆΣ1 be the component of ˆΣ\ ˆΓ containing ˆΣ0. By the
first claim, this must be a proper containment, and we can write
ˆΣ1 = ˆΣ0∪S 1∪···∪S k,
whereS 1,...,S m are some components of Σ\Γ adjacent to Σ 0. For the third item in the theorem,
it suffices to show that Σ 0 is not a pseudo-Anosov component, as discussed; for the second item, it
suffices to show that none of theS j are pseudo-Anosov components. We prove both at once.
EachS j shares some boundary componentγwith ˆΣ0. Some power ( ˆφ)n restricts to a map on ˆΣ1
which is freely isotopic either to the identity or to a pseudo-Anosov map. Since ˆφfixes Γ setwise
andγis a component of Γ, we can also assume that ( ˆφ) n fixesγ. But the second claim implies
thatγis homotopically essential and not boundary parallel in ˆΣ1,which means that ( ˆφ)n|ˆΣ1
is not
freely isotopic to a pseudo-Anosov map; it is therefore freely isotopic to the identity. But then ( ˆφ)n
restricts to maps on ˆΣ0 andS j which are both freely isotopic to the identity.
Now, the restrictions of ( ˆφ)n andφ n toS j agree sinceφ= ˆφoutside ofD. It follows thatφ n|Sj
is freely isotopic to the identity, and hence thatS j is a periodic component of Σ\Γ. We can also
conclude that Σ0 is a periodic component of Σ\Γ. Indeed, if it is not thenφ 0 is pseudo-Anosov, in
which case the same is true of ˆφ0, as we showed at the beginning of the proof. This would imply
that the restriction of ( ˆφ)n to ˆΣ0 is freely isotopic to a pseudo-Anosov map, but we have just shown
that it is freely isotopic to the identity, a contradiction. It follows that Σ 0 andS j are both periodic
components of Σ\Γ, completing the proof of the theorem.□
Corollary 2.5.IfK⊂S 3 is a fibered hyperbolic knot such thatS 3
0(K)is not hyperbolic, then its
monodromy is not veering.
Proof.The monodromyh: Σ→Σ ofKis freely isotopic to a pseudo-Anosov mapφ 0. In this case,
Σ0 = Σ is not a pair of pants, since it has connected boundary. Thenhis not veering; otherwise,
Theorem 2.4 would imply that ˆφ 0 is also pseudo-Anosov, which would imply thatS 3
0(K), the
mapping torus of ˆh, is hyperbolic.□

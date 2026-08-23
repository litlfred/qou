---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-059-44-degenerations-of-abelian-varieties-79
section_title: "Degenerations of abelian varieties 79"
section_number: 4.4
pages: 87-89
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
whereYη and Ys denote the generic resp. special ﬁbres of˜f. Note that Ys
can be naturally identiﬁed with the ﬁbref−1(s)⊂ Y. In the case of the
perverse intersection cohomology sheaf the passage between the global and
the local picture is provided by the following observation, where we now
denote byi : Ys = f−1(s) ↪→Y the global embedding.
COROLLARY 4.10. In the above situation,
sp(δYη) = i∗(δY[−1]).
Proof.Our smoothness assumption onf implies that the generic ﬁbreYη
is smooth so that the perverse intersection cohomology sheafδ = δYη is
the constant sheaf up to a degree shift. From this one easily deduces that
the intermediate extensionj!∗(δ[1]) which occurs in lemma 4.9 arises from
the perverse intersection cohomology sheafδY on the total spaceY via the
Henselization morphism˜Y−→Y. □
4.4. Degenerations of abelian varieties
To ﬁnd sufﬁciently large lower bounds on the general Tannaka group
in theorem 4.2 we consider certain families of ppav’s whose theta divisor
degenerates. To construct these we ﬁx an integern≥ 3 and work over the
moduli spaceAg,n of ppav’s of dimensiong with leveln structure. It has
been shown in chapter 7.3 of [80] that this moduli space is representable by
a smooth quasi-projective variety overQ. Analytically it can be written as
the quotient
Ag,n(C) = Hg/Γg(n)
of the Siegel upper half space by the action of the principal congruence
subgroupΓg(n) =ker(Sp2g(Z)−→Sp2g(Z/nZ)). Recall that forn≥ 3 this
action is free, which again explains why in this case the moduli space is
smooth. We denote by
p : X = Hg×Cg/ Γg(n)⋉ Z2g // Ag,n
the universal abelian scheme and byΘ⊂ X the divisor which is deﬁned
on the universal coveringHg×Cg by the zero locus of the Riemann theta
functionϑ(τ,z). Thus for each point τ∈ Ag,n(C) the ﬁbre Xτ = p−1(τ)
is a complex ppav withΘτ = Θ∩Xτ as a symmetric theta divisor. More
generally, for any complex algebraic varietyS with a morphismS−→Ag,n
we denote by
XS = X×Ag,n S and ΘS = Θ×Ag,n S
80 Chapter 4 – The Tannaka group of the theta divisor
the corresponding abelian scheme resp. its relative theta divisor. For the
construction of families of ppav’s with degenerating theta divisors we will
use the following general observation.
LEMMA 4.11. For every point s∈ Ag,n(C) there is a smooth complex
quasi-projective curve S↪→ Ag,n, passing through the point s in a general
tangent direction, such that
(a) the generic ﬁbre of the familyΘS→S is smooth,
(b) the singular loci of the total space and of the special ﬁbre of this
family satisfy
Sing(ΘS)⊆ Sing(Θs).
If the theta divisorΘs contains a singular point of precise multiplicity two,
then the inclusion in part (b) is strict for a suitable choice of S.
Proof.Since the moduli spaceAg,n is smooth and quasi-projective, for
any s∈ Ag,n(C) we can ﬁnd a smooth quasi-projective curveS ↪→ Ag,n
passing through the points in a general tangent direction. We can assume
that our general curveS is not contained in the locus of ppav’s with singular
theta divisor, indeed by [4] this locus is itself a divisor inAg,n. So after
shrinkingS we can assume that for allt∈ S(C)\{s} the theta divisorΘt
is smooth. Then property(a) is clearly satisﬁed, and property(b) easily
follows from the fact that the total spaceΘS is given locally in the smooth
varietyXS as the zero locus of a single analytic function.
Explicitly, let∆⊂ S be an analytic coordinate disk with coordinatew
centered at the given points, and consider a local lifth : ∆→ Hg of the
embedding∆ ↪→ S ↪→ Ag,n. On the universal covering the divisorΘS is
described as the locus
{(w,z)∈ ∆×Cg| F(w,z) =0}⊂ ∆×Cg
where the analytic functionF(w,z) = ϑ(h(w),z) vanishes. If a point(w,z)
on this locus deﬁnes a singular point of the relative theta divisorΘS, then
the gradient ofF must vanish at this point. For the gradient in the variablez
this implies
0 = ( ∇zF)(w,z) = ( ∇zϑ)(τ,z) for τ = h(w).
Hence(τ,z) deﬁnes a singular point of the ﬁbreΘt wheret∈ S(C) denotes
the image of the pointτ. By our choice of the curve S the only singular
ﬁbre Θt is the one over the pointt = s, hence claim(b) follows.
This being said, if some point(τ,z)∈ Hg×Cg deﬁnes a singular point
of the theta divisorΘs with precise multiplicity two, then by deﬁnition the

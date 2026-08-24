---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-448-1-ss-restricted-to-s-notice
section_title: "(S,s ), restricted to S). Notice"
section_number: 1
pages: 166-168
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp — 580 sections: INTRODUCTION; INTRODUCTION; INTRODUCTION"
---
that the derivation d
dz extends canonically to O( ˜S).
Proposition 4.3.3. There is a unique diﬀerential equation of the form
y′′−qy = 0, q ∈ C(S),
the uniformizing diﬀerential equation , such that τ is the quotient of two
solutions inO( ˜S) of this diﬀerential equation. It is fuchsian and has singu-
larities only at Z ={ζ0,... ,ζ n}. The monodromy group pointed at s is a
discrete ﬁnitely generated subgroup of SL2(C) whose image in PSL 2(C) is
πorb
1 (S,s ).
If S = P1 and ζn =∞, the exponents are rational numbers given by the
(23)in some cases, it will be more convenient to work with h instead of D.
(24)in the case ˜S = P1, it is only meromorphic a priori. But in that case S = P1 and
the covering P1 → P1 is ﬁnite. It will be convenient to normalize things so that ∞ lies
above ∞ and z is the standard coordinate on P1. With this choice, τ has no pole.
4. NON-ARCHIMEDEAN ORBIFOLDS. 163
Riemann scheme:





ζ0 ... ζ n−1 ζn =∞
1
2 (1 + 1
e0
) ... 1
2 (1 + 1
en−1
) −1
2 (1 + 1
en )
1
2 (1− 1
e0
) ... 1
2 (1− 1
en−1
) −1
2 (1− 1
en )






.
cf. loc. cit.
Proof. Existence: q is nothing but the Schwarz derivative
{τ,z} =
(dτ
dz
)1/2 d2
dz2
[(dτ
dz
)−1/2]
,
which is single-valued on S. A basis of solutions of the uniformizing diﬀer-
ential equation is given by ( dτ
dz )−1/2 andτ.( dτ
dz )−1/2. The fact that q∈ C(S)
follows immediately from the invariance of the Schwarz deri vative under
homographic transformations.
Unicity: this is a purely algebraic fact: q is determined by the projective
connection attached to the diﬀerential equation y′′−qy = 0.
The determination of the Riemann scheme comes from this expr ession
and the fact that around ζi<n (resp. around∞) τ is given by z−ζi↦→
ci.(z−ζi)1/ei +h.o.t. (resp. 1/z↦→cn/zen +h.o.t.).
Remarks 4.3.4. (i) The case of three singularities will be detailed in the ne xt
section. In the case of more than three singularities, it is e xtremely diﬃcult
in general to write down explicitly the uniformizing diﬀere ntial equations.
(ii) In [ Y o87], an extension of the theory of uniformizing diﬀerential
equations to higher dimensions is developed. Its practical scope seems lim-
ited however to the case when ˜S is a symmetric domain.
(iii) The projective equivalence class of the uniformizing diﬀerential
equation is a variant of what is called the Schwarz structure or canonical
indigenous P1-bundle over S, cf. [Gun67], [ Moc96].
4.4. Non-archimedean orbifolds.
4.4.1. We now work over a complete non-archimedean ﬁeld K. The deﬁni-
tion of orbifolds is parallel to the one which we have selecte d in the com-
plex situation. Being mainly interested in orbifolds which are quotients of
manifolds by ﬁnite groups, it is natural to replace everywhe re ´ etale (= topo-
logical) coverings in the complex case by temperate ´ etale coverings in the
non-archimedean context.
A K-orbifold S = (
S, (Zi,e i)) consists in
– a normal K-analytic space S (in the sense of Berkovich),
– a locally ﬁnite collection of irreducible divisors ( Zi),
– a positive integer ei attached to each Zi.
It is assumed that S is covered by so-called orbifold charts , i.e. morphisms
W
φ
− →V ⊂S where
164 III. p-ADIC ORBIFOLDS AND MONODROMY.
– W is a K-manifold,
– φ is a (ramiﬁed) covering in the sense of 1.2.3 ( i.e. V is covered by
open subsets U such that ∐ Vj =φ−1U→U and the restriction of φ
to every Vj is ﬁnite),
– except for a closed subset Σ of codimension 2 in V , φ restricts to a
temperate ´ etale covering aboveV\ (V∩⋃ Zi), and is ramiﬁed with
index ei aboveZi.
Here again, we may and shall assume that that Σ is contained in ⋃ Zi∪
S
sing
and set Z =⋃ Zi∪S
sing
, S =S\Z (which is a K-manifold).
Remarks 4.4.2. (i) At this point, because the notion of orbifold is local, it
would not change if we had modiﬁed the deﬁnition of orbifold c harts by
replacing ‘temperate ´ etale’ by ‘ﬁnite ´ etale’ or by ‘´ etal e’. In contrast, we
insist that orbifold charts are deﬁned in terms of temperate coverings.
(ii) Since we only prescribe the ramiﬁcation indices and not the rami-
ﬁcation groups, this notion of orbifold is only reasonable i n the tame case,
i.e. when char(K) ∤ ei. We shall be mostly interested in the characteristic
0 case.
(iii) If dim S = 1, then S =S\⋃ Zi.

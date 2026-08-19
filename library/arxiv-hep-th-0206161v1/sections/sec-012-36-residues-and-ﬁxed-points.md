---
doc_id: arxiv-hep-th-0206161v1
doc_title: "SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING Nikita A. Nekrasov 1"
section_id: sec-012-36-residues-and-ﬁxed-points
section_title: "Residues and ﬁxed points"
section_number: 3.6
pages: 19-21
source_pdf: 0206161v1.pdf
source_sha256: 9530c40215baa02d
doc_brief: "SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING Nikita A. Nekrasov 1 — 26 sections: Introduction; (1 .3); (α±"
---
The poles in the integral (3.10) correspond to the ﬁxed point s of the action of the
groups G × T2 on the resolved moduli space ˜Mk,N . Physically they correspond to the
U (N ) (noncommutative) instantons which split as a sum of U (1) noncommutative instan-
tons corresponding to N commutingU (1) subgroups of U (N ). The instanton charge kl is
the charge of the U (1) instanton in the l’th subgroup. Moreover, these abelian instantons
are of special nature – they are ﬁxed by the group of space rota tions. If they were com-
mutative (and therefore point-like) they had to sit on top of each other, and the space of
such point-like conﬁgurations would have been rather singu lar. Fortunately, upon the non-
commutative deformation the singularities are resolved. T he instantons cannot sit quite
18
on top of each other. Instead, they try to get as close to each o ther as the uncertainty
principle lets them. The resulting abelian conﬁgurations w ere classiﬁed (in the language
of torsion free sheaves) by H. Nakajima [30].
Now let us ﬁx a conﬁguration ⃗Y and consider the corresponding contribution to the in-
tegral over instanton moduli. It is given by the residue of th e integral (3.10) corresponding
to (3.19):
R⃗Y = 1
(ǫ1ǫ2)k
∏
l
ν l, 1
∏
α=1
kl,α∏
β=1
Sl(ǫ1(α − 1) +ǫ2(β − 1))
(ǫ(ℓ(s) + 1) −ǫ2h(s))(ǫ2h(s) −ǫℓ(s)) ×
∏
l<m
ν l, 1
∏
α=1
km, 1∏
β=1
( (
alm +ǫ1(α −νm,β) +ǫ2(1 −β)
)
(alm +ǫ1α +ǫ2(kl,α + 1 −β))
(alm +ǫ1α +ǫ2(1 −β)) (alm +ǫ1(α −νm,β) +ǫ2(kl,α + 1 −β))
) 2
(3.20)
where we have used the following notations: alm =al −am,
Sl(x) = Q(al +x)∏
m⁄=l(x +alm)(x +ǫ +alm), S l(x) = Q(al +x)∏
m⁄=l(x +alm)2, (3.21)
and
ℓ(s) = kl,α −β, h (s) = kl,α +νl,β −α −β + 1 (3 .22)
Now, if we set ǫ1 = ¯h = −ǫ2 the formula (3.20) can be further simpliﬁed. After some
reshuﬄing of the factors it becomes exactly the formula for t he term in the sum (1.8),
corresponding to the partition {kl,i}.
Remark. The expressions (3.20)(1.6)(1.8) are the typical localiza tion formulae for the
instanton integrals. They commonly appear in the two dimens ional sigma model instanton
calculations, on the so-called A side. The Seiberg-Witten p repotential [3] is the typical
type B expression. In is not easy to recognize in the type A exp ression the mirror manifold,
and its periods. To illustrate this point, we suggest to look at the generating function of
the number of holomorphic curves of genus zero in the Calabi- Yau quintic, computed using
localization [17]. It requires some extra work to map it to th e mirror calculation, yet it
can be done [18]. In this paper we shall not complete the story in the sense that we
shall not prove directly that our “type A” expression can be c omputed on the “B side”
involving Seiberg-Witten curves. We shall, however, prese nt a conjecture, which connects
our calculation to its mirror counterpart (that is, we shall deﬁne the mirror computation).
We shall also make some explicit checks for low instanton num bers (up to ﬁve) to
make sure we have computed the right thing.
19

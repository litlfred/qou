---
doc_id: arxiv-1112.5179v1
doc_title: "Prepared for submission to JHEP 3-Manifolds and 3d Indices Tudor Dimofte1,2 Davide Gaiotto 1 Sergei Gukov 3,4 1Institute for Advanced Study, Einstein Dr., Princeton, NJ 08540, USA "
section_id: sec-001-2-actions-on-the-3d-index
section_title: "Actions on the 3d index"
section_number: 2
pages: 7-11
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices Tudor Dimofte1,2 Davide Gaiotto 1 Sergei Gukov 3,4 1Institute for Advanced Study, Einstein Dr., Princeton, NJ 08540, USA 2Trinity College, Cambridge CB2 1TQ, UK — We"
---
Let us consider a 3d N = 2 SCFT T with ﬂavor symmetry U(1)N. The generalized super-
symmetric index was deﬁned in [17], following [13–16, 43], as a trace
IT (m;q,ζ ) = Tr Hm(−1)Fe−β(E−R−j3)q
E+j3
2 ζe (2.1)
over a superselection sector of the Hilbert space of the 3d theory on S2. Speciﬁcally, the
Hilbert space Hm is labelled by the magnetic ﬂux m = (m1,...,m N)∈ ZN on S2 for N
backgroundU(1) gauge ﬁelds coupled to the ﬂavor symmetry,
mi :=
∫
S2
Fi
2π. (2.2)
By standard arguments [44], the index (2.1) receives contributions only from states with
energyE =R +j3, where R is the R-charge of a state 3 andj3 is the spin on S2, with respect
to a ﬁxed, chosen axis. With this in mind, we can write the index more simply as
IT (m;q,ζ ) = Tr Hm(−1)Fq
R
2 +j3ζe (2.3)
3Although we consider superconformal theories here, R does not have to be the same as the R-charge that
enters into the superconformal algebra, cf. [15].
– 6 –
The fugacity ζ measures the ﬂavor charge e∈ ZN of states, and we use a shorthand notation
ζe =ζe1
1 ··· ζeN
N .
It is also often convenient to work with the index at ﬁxed magnetic ﬂux m and at ﬁxed
electric charge e. We therefore collect e and m into a symplectic charge vector
γ =
(m
e
)
(2.4)
and deﬁne
IT (γ;q) ≡ IT (m,e ;q) := TrHm,e(−1)Fq
R
2 +j3. (2.5)
Thus,IT (m;q,ζ ) =
∑
e∈ZN
IT (m,e ;q)ζe, or converselyIT (m,e ;q) =
∮ dNζ
(2πi)Nζe+1IT (m;q,ζ ),
where ζe+1 =ζe1+1
1 ··· ζeN+1
N and integration is done on the unit circle.
We note that even though the theoryT is superconformal, the R-charge used to calculate
the index need not coincide with the superconformal R-charge. The index is typically com-
puted from a UV description of the theory, by a deformed Lagrangian on S2 that preserves a
half of the usual superconformal symmetries no matter how R is deﬁned [15, 45]. The powers
ofq produced by such a calculation could be unconstrained. However, if the UV theory ﬂows
to a IR SCFT whose R-symmetry is not accidental, there will be a R-symmetry redeﬁnition
that makes the powers of q nonnegative. This is because the quantity E +j3 in (2.1) (and
so R
2 +j3 when restricted to E =R +j3) is nonnegative in superconformal theories, cf. [46].
Conversely, the absence of a such redeﬁnition — which we have yet to encounter in class R
— would signal a breakdown of the naive expectations for the RG ﬂow of the UV theory. 4
Finally, we should comment on the precise meaning of ( −1)F in the trace. The most
natural choice would be ( −1)2j3, but it is not the choice that is (implicitly) made in the
literature on the reﬁned index: in the presence of odd magnetic ﬂux, the angular momentum
on S2 of a particle of odd electric charge is shifted by a half-integral amount, but no extra
(−1) sign is usually inserted compared to the index in even ﬂux sectors. This is equivalent to
a deﬁnition
(−1)F = (−1)2j3+e·m. (2.6)
The diﬀerence between the two conventions is fairly minimal: it is just an overall sign change
(−1)e·m ofIT (m,e ;q), or a redeﬁnition of the fugacity ζ→ (−1)mζ inIT (m;q,ζ ). In this
paper we will stick to the modiﬁed form of F , mostly for reasons of notational convenience
and backwards compatibility. We will return to some of these subtleties in later sections.
2.1 The Sp(2N, Z) action
In [22], an Sp(2N, Z) action on 3d SCFT’s with N U(1) ﬂavor symmetries was introduced. 5
The index (2.5) in the charge basis transforms very transparently under this action. Namely,
4This is a possibly more reﬁned version of the requirement of positive monopole operator dimensions used
to discuss the IR behavior of N = 4 gauge theories [47].
5We refer the reader to [22], as well as [19], for details of Sp(2N, Z) transformations on SCFT’s. Our
notation here closely follows that in [19].
– 7 –
for g∈Sp(2N, Z), we have6
Ig◦T (gγ ;q) =IT (γ;q). (2.7)
For simplicity, we can illustrate the action (2.7) forN = 1 (i.e. a singleU(1) ﬂavor symmetry)
by looking at the action of the two generators T and S of Sp(2, Z)≃SL(2, Z).
A T transformation simply adds one unit of Chern-Simons coupling for the background
U(1) gauge ﬁeld. The eﬀect of the CS coupling for the ﬂavor symmetry background gauge
ﬁeld is simply to shift the ﬂavor charge of a state by an amount proportional to the magnetic
ﬂux. Therefore
IT◦T (m,e +m;q) =IT (e,m ;q), (2.8)
which is compatible with the matrix representing T ,
T :
(m
e
)
↦→
(1 0
1 1
)(m
e
)
. (2.9)
An S transformation makes the background gauge ﬁeld dynamical, and adds a super-
symmetric FI term for it. This eﬀectively couples the resulting theory to a background U(1)
for a new ﬂavor symmetry, whose conserved current is the magnetic ﬂux of the old, now
gauged, ﬂavor symmetry. Thus, the new electric charge is the old magnetic ﬂux. Gauging
the old ﬂavor symmetry also means that we should project onto states of zero gauge charge.
However, turning on a magnetic ﬂux m′ for the new ﬂavor symmetry shifts the gauge charge
of a state by m′, so in eﬀect we project onto states of gauge charge −m′. Altogether we ﬁnd
IS◦T (−e,m ;q) =IT (m,e ;q), (2.10)
which is compatible with the matrix representing S,
S :
(m
e
)
↦→
(0− 1
1 0
)(m
e
)
. (2.11)
From these matrix representations, it is easy to check that I(ST )3◦T (γ;q) = IT (γ;q), and
IS2◦T (γ;q) = IT (−γ;q), as expected from the group relations ( ST )3 = id. and S2 = C,
where C acts as charge conjugation.
TheT andS transformations (2.8)–(2.10) could also be written in a “fugacity” basis for
the index (2.3). We ﬁnd
IT◦T (m;q,ζ ) =ζmIT (m;q,ζ ), (2.12)
IS◦T (m′;q,ζ′) =
∑
m∈Z
∮ dζ
2πiζ ζ′mζm′
IT (m;q,ζ ), (2.13)
with the integration done, as usual, on the unit circle. In this form, it is easier to see that
the transformations agree with the general rules of [15, 17] for gauging ﬂavor symmetries and
adding Chern-Simons terms to the index.
6Note that the Sp(2N, Z) transformation acts non-trivially on the ( −1)e·m factor we included in the deﬁ-
nition of the fermion number. We will return to this in Section 2.2.
– 8 –
2.2 Aﬃne shifts
As mentioned above, the R-charge used in the index does not need to coincide with the R-
charge that appears in the superconformal algebra. We can take R to be any R-symmetry
charge. If we redeﬁne the R-charge by a ﬂavor symmetry, then diﬀerent choices are related
byR→R−αe·e for some vector αe. Under such a shift, the index varies accordingly as
IT (m,e ;q)→q− 1
2αe·eIT (m,e ;q). (2.14)
There is also a certain degree of latitude in choosing the R-charge of the vacuum in a non-
trivial ﬂux sector of the theory. It is thus natural to also consider redeﬁnitionsR→R+αm·m,
under which
IT (m,e ;q)→q
1
2αm·mIT (m,e ;q). (2.15)
Altogether, we can collect
α =
(αe
αm
)
, (2.16)
and write
IσR(α)◦T (γ;q) =q
1
2⟨α,γ⟩IT (γ;q) (2.17)
where σR(α)◦T denotes the theory with the new R-charge R +⟨α,γ⟩. Here the symplectic
product⟨α,γ⟩ equals αm·m−αe·e.
Similar shifts can happen in the deﬁnition of the fermion number charge F . This would
not be the case if we had deﬁned ( −1)F = (−1)2j3, as j3 is a generator in a non-Abelian
symmetry group. But the symplectic group acts on ( −1)e·m in a rather interesting way.
Indeed, s(γ) = (−1)e·m is a “quadratic reﬁnement of the charge lattice”, i.e. a Z2-valued
function of charges with the property
s(γ)s(γ′) =s(γ +γ′)(−1)⟨γ,γ′⟩. (2.18)
Any two such reﬁnements diﬀer by a factor of the form ( −1)⟨α,γ⟩ for some α. Thus, we will
just introduce a fermion-number shift operation
IσF (α)◦T (γ;q) = (−1)⟨α,γ⟩IT (γ;q) (2.19)
that modiﬁes the choice of quadratic reﬁnement used in F . Note that [ σF (α)]2 = 1 for any
α. Such shifts in the deﬁnition of R and F are often important when comparing mirror
descriptions of the same theory. In particular, a symplectic transformation will change the
choice of quadratic reﬁnement from s(γ) tos(gγ), which will have to be brought back to s(γ)
by a fermion number shift.
In the following, we will often ﬁnd that R and F shifts happen simultaneously, with the
same parameter α. This is ultimately due to the fact that the UV description of the theories
– 9 –
often have a natural R-charge assignment such that (−1)F = (−1)R, i.e. (−1)R+2j3+e·m = 1
when acting on all the chiral ﬁelds in the Lagrangian. 7
Mathematically, the shifts in R and F generate an abelian group of translations Z2N×
(Z2)2N that acts on the index. This abelian group can naturally be combined with the
symplectic group Sp(2N, Z) to generate an aﬃne symplectic group Sp(2N, Z) ⋉ (Z× Z2)2N.
One can check that the expected group relations are satisﬁed. For example, taking N =
1, if we denote the generators of unit electric and magnetic shifts by σR
e, σF
e and σR
m, σF
m,
respectively, then
SσR
e =σR
mS, Sσ R
m = (σR
e )−1S, (2.20a)
T−1(σR
e )−1TσR
e =σR
m, Tσ R
m =σR
mT, (2.20b)
and similarly for σF
e,m. The abelian ( Z× Z2)2N subgroup of the aﬃne symplectic group does
act in the obvious way by translations on the vector (m,e ). However, we will see momentarily
that there exists another object, a certain algebra of operators associated with the index, on
which this abelian subgroup is represented by translations.

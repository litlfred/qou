---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-050-a-proof-of-saitos-theorem
section_title: "A Proof of Saito’s theorem"
section_number: null
pages: 100-110
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
Proof of Saito’s theorem
Let us recall the statement of the theorem. The proof we present here is adapted
from an unpublished version of [Sai94].
Theorem A.0.1. Let R be a k-algebra, and χ : B[Γ] →R an R-character. Assume
that χ is irreducible, that is χ(∆α,β) ∈R× for some α, β ∈Γ, and let A, B ∈SL2(R)
such that Tr A = χ(Yα), Tr B = χ(Yβ), Tr AB = χ(Yαβ). Then there exists a unique
representation ρ : Γ →SL2(R) whose character is χ and such that ρ(α) = A,
ρ(β) = B.
In the sequel we will denote by φ : Γ →R the map φ(γ) = χ(Yγ).We ﬁrst introduce
the following deﬁnition :
Deﬁnition A.0.2. An R-valued form is a map h : Γ →R such that ∀γ, δ ∈
Γ, h(γδ) + h(γδ−1) = φ(γ)h(δ). A form will be called homogeneous if h(e) = 0.
Remark A.0.3. By the trace formula, the map φ is a (non-homogeneous) form. If
h is a homogeneous form, then clearly h(γ) + h(γ−1) = 0, hence
h(γδ) + h(δγ) = φ(γ)h(δ) + φ(δ)h(γ)
(A.1)
Lemma A.0.4. Let h be a homogeneous form, denote by Vh = {γ ∈Γ : h(γ) = 0}.
Then the following holds :
1. ∀γ ∈Vh, ∀n ∈Z, γn ∈Vh.
2. ∀δ ∈Vh, ∀γ ∈Γ, h(γδ) = h(δ−1γ).
3. If δ1, . . . , δm ∈Vh such that δiδj ∈Vh for any i < j, then for any permutation
σ ∈Sm and any γ ∈Γ, h(δ1 . . . δmγ) = h(δσ(1) . . . δσ(m)γ).
99
Proof.
1. By deﬁnition h(γn) = h(γγn−1) = φ(γ)h(γn−1) −h(γn−2) = 0 by
induction.
2. We have h(γδ) = φ(γ)h(δ)−h(γ−1δ) but h(δ) = 0 and h(γ−1δ)+h(δ−1γ) = 0,
hence h(γδ) = h(δ−1γ).
3. We ﬁrst remark that Equation (A.1) implies that if δi, δj, δiδj ∈Vh, so is
δjδi, hence all the δiδj lie in Vh. It is enough to show the result for σ =

i
i + 1

a transposition. Applying successively item 2 one ﬁnd h(δ1 . . . δnγ)
= h(δi+2 . . . δmγδ−1
1 . . . δ−1
i+1). Then we apply again item 2 with (δi+1δi)−1 and
we obtain the equality h(δ1 . . . δm) = h(δi+1δiδi+2 . . . δmγδ−1
1 . . . δ−1
i−1), ﬁnally
we conclude by applying item 2 again for getting back with δi−1, . . . δ1 on the
left hand-side.
Lemma A.0.5. Let h be a homogeneous form, with h(α) = h(β) = h(αβ) = 0.
Then for any γ ∈Γ, φ(∆α,β)h(γ) = 0.
Proof. For any γ ∈Γ, let us compute φ(α)h(γ) = h(αγ) + h(α−1γ) hence
φ(α)2h(γ) = φ(α)(h(αγ + h(α−1γ)) = h(α2γ) + h(α−2γ) + 2h(γ)
In the very same way,
φ(β)2h(γ) = h(β2γ) + h(β−2γ) + 2h(γ)
and
φ(αβ)2h(γ) = h((αβ)2γ) + h((αβ)−2γ) + 2h(γ)
Now
φ(α)φ(β)φ(αβ)h(γ) = φ(αβ)φ(β)(h(αγ) + h(α−1γ))
= φ(βα)(hβαγ) + h(βα−1γ) + h(β−1αγ) + h(β−1α−1γ))
= h((βα)2γ) + h(γ) + h(βαβα−1γ) + h(α−2γ)
+ h(α2γ) + h(β−1α−1β−1αγ) + h(γ) + h((αβ)−2γ)
Finally we obtain
φ(∆α,β)h(γ) = φ(α)2h(γ) + φ(β)2h(γ) + φ(αβ)2h(γ) −φ(α)φ(β)φ(αβ)h(γ) −4h(γ)
= h(β2γ) −h(βαβα−1γ) + h(β−2γ) −h(β−1α−1β−1αγ) + h((αβ)2γ)
100
−h((βα)2γ)
and using Item 3 of Lemma A.0.4 we easily see that the latter is zero, and the lemma
is proved.
Before we start with the proof of Saito’s theorem, we prove the following lemma
that will be used in the sequel. We ﬁx the notations for this lemma and for the
proof of the theorem, we ﬁx α, β ∈Γ satisfying the hypotheses of the theorem.
For any γ ∈Γ, we deﬁne the vector Tγ =

φ(γ)
φ(αγ)
φ(βγ)
φ(αβγ)

and the
matrix M =






φ(e)
φ(α)
φ(β)
φ(αβ)
φ(α)
φ(α)2
φ(α)φ(β)
φ(α)φ(αβ)
φ(β)
φ(β)φ(α)
φ(β)2
φ(β)φ(αβ)
φ(αβ)
φ(αβ)φ(α)
φ(αβ)φ(β)
φ(αβ)2






. A computation gives
det(M) = −φ(∆α,β)2 hence M ∈GL4(R) in the following. We will denote by T t
γ the
column-vector transpose of Tγ.
Lemma A.0.6. Assume that φ(∆α,β) ∈R×, then for any γ, δ ∈Γ, φ(γδ) = TγM −1T t
δ.
Proof. For δ ∈Γ, we deﬁne Hδ : Γ →R by Hδ(γ) = φ(γδ) −TγM −1T t
δ. Then Hδ is
a form since Hδ(γη) + Hδ(γ−1η) = φ(γηδ) + φ(γ−1ηδ) −(Tγη + Tγ−1η)M −1T t
δ, and
the trace relation φ(γγ′) + φ(γ−1γ′) = φ(γ)φ(γ′) implies that Hδ(γη) + Hδ(γ−1η) =
φ(γ)φ(ηδ) + φ(γ)TηM −1T t
δ = φ(γ)Hδ(η).
Moreover, from






Te
Tα
Tβ
Tαβ






= M we deduce that Hδ(e) = Hδ(α) = Hδ(β) = Hδ(αβ) =
0, that is Hδ is homogeneous and satisﬁes the hypothesis of Lemma A.0.5, hence for
any γ ∈Γ, φ(∆α,β)Hδ(γ) = 0 and we conclude that Hδ(γ) = 0 for all δ ∈Γ, thus
the lemma is proved.
Proof of Saito’s Theorem. Let us deﬁne
ρ : Γ →M2(R)
γ 7→

Id
A
B
AB

M −1T t
γ
Here we consider the vector M −1T t
γ’s entries to be 2 × 2 scalar matrices. We need
to check that the map we deﬁned does satisfy all the requirements of the theorem.
101
1.

ρ(e)
ρ(α)
ρ(β)
ρ(αβ)

=

Id
A
B
AB

M −1 
T t
e
T t
α
T t
β
T t
αβ

but
the right hand matrix is exactly the matrix M, hence ρ(e) = Id, ρ(α) =
A, ρ(β) = B, ρ(αβ) = AB.
2. For any γ ∈Γ,






Tr(ρ(γ))
Tr(Aρ(γ))
Tr(Bρ(γ))
Tr(ABρ(γ))






= T t
γ since by deﬁnition, we have Tr(ρ(γ)) =

Tr Id
Tr A
Tr B
Tr AB

M −1T t
γ and thus the left hand side term is pre-
cisely






Tr I
Tr A
Tr B
Tr AB
Tr A
Tr A2
Tr AB
Tr A2B
Tr B
Tr AB
Tr B2
Tr AB2
Tr AB
Tr A2B
Tr AB2
Tr(AB)2






M −1T t
γ but item 1 implies that
the matrix






Tr I
Tr A
Tr B
Tr AB
Tr A
Tr A2
Tr AB
Tr A2B
Tr B
Tr AB
Tr B2
Tr AB2
Tr AB
Tr A2B
Tr AB2
Tr(AB)2






is nothing but M.
3. Let us prove that for any γδ ∈Γ, ρ(γδ) = ρ(γ)ρ(δ). Let C =






Tr ρ(γ)ρ(δ)
Tr Aρ(γ)ρ(δ)
Tr Bρ(γ)ρ(δ)
Tr ABρ(γ)ρ(δ)






.
Then






ρ(γ)ρ(δ)
Aρ(γ)ρ(δ)
Bρ(γ)ρ(δ)
ABρ(γ)ρ(δ)






=






ρ(γ)
Aρ(γ)
Bρ(γ)
ABρ(γ)






ρ(δ) =






ρ(γ)
Aρ(γ)
Bρ(γ)
ABρ(γ)







I
A
B
AB

M −1T t
δ =






ρ(γ)
ρ(γ)A
ρ(γ)B
ρ(γ)AB
Aρ(γ)
Aρ(γ)A
Aρ(γ)B
Aρ(γ)AB
Bρ(γ)
Bρ(γ)A
Bρ(γ)B
Bρ(γ)AB
ABρ(γ)
ABρ(γ)A
ABρ(γ)B
ABρ(γ)AB






M −1T t
δ.
Using item 2 and the trace relation we can compute the traces of the previous
matrix, for instance
Tr(ABρ(γ)B) = Tr(AB) Tr(ρ(γ)B) −Tr(B−1A−1ρ(γ)B)
= φ(αβ)φ(γβ) −Tr(A−1ρ(γ))
= φ(αβγβ) + φ(αγ−1) −Tr(Aρ(γ−1)
= φ(αβγβ)
102
We obtain C =






φ(γ)
φ(γα)
φ(γβ)
φ(γαβ)
φ(αγ)
φ(αγα)
φ(αγβ)
φ(αγαβ)
φ(βγ)
φ(βγα)
φ(βγβ)
φ(βγαβ)
φ(αβγ)
φ(αβγα)
φ(αβγβ)
φ(αβγαβ)






M −1T t
δ.
But from Lemma A.0.6 we know that φ(γδ) = TγM −1T t
δ and so C =






φ(γδ)
φ(αγδ)
φ(βγδ)
φ(αβγδ)






and from the ﬁrst item, C =






Tr(ρ(γδ))
Tr(Aρ(γδ))
Tr(Bρ(γδ))
Tr(ABρ(γδ))






.
Let then X = ρ(γδ) −ρ(γ)ρ(δ), then the latter equality is equivalent to
Tr(X) = Tr(AX) = Tr(BX) = Tr(ABX) = 0. We observe that M is a
Gramm matrix for {I, A, B, AB} with respect to the non-degenerate bilinear
form (M, N) 7→Tr(MN). As det(M) ∈R× we know that {I, A, B, AB} is a
basis of M2(R), and so X = 0, which proves that ρ is a group homomorphism.
4. A direct computation shows that Tγ2 = φ(γ)Tγ +Te = 0, in particular ρ(γ)2−
Tr(ρ(γ))ρ(γ) + ρ(e) = 1 and det(ρ(γ)) = 1 for any γ ∈G.
5. Finally, we prove the unicity as follows : for any representation ρ′ that satisﬁes
the statement of the theorem, we have






Tr(ρ(γ))
Tr(Aρ(γ))
Tr(Bρ(γ))
Tr(ABρ(γ))






=






Tr(ρ′(γ))
Tr(Aρ′(γ))
Tr(Bρ′(γ))
Tr(ABρ′(γ))






for any γ ∈Γ, hence ρ = ρ′ and the theorem is proved.
103
104
Bibliographie
[Ben16]
Leo Benard :
Singularities of the reidemeister torsion form on the
character variety. arXiv preprint : 1612.06237, 2016.
[Ben17]
Leo Benard : Torsion function on character varieties. ArXiv e-prints :
1711.08781, 2017.
[Ber94]
Robert W. Berger : Report on the torsion of the diﬀerential module of
an algebraic curve. In Algebraic geometry and its applications. Collec-
tions of papers from Shreeram S. Abhyankar’s 60th birthday conference
held at Purdue University, West Lafayette, IN, USA, June 1-4, 1990,
pages 285–303. New York : Springer-Verlag, 1994.
[Bro82]
Kenneth S. Brown : Cohomology of groups. Graduate Texts in Mathe-
matics, 87. New York-Heidelberg-Berlin : Springer-Verlag, 1982.
[Bur67]
Gerhard Burde : Darstellungen von Knotengruppen. Math. Ann., 173:
24–33, 1967.
[BV13]
Nicolas Bergeron et Akshay Venkatesh : The asymptotic growth of
torsion homology for arithmetic groups. J. Inst. Math. Jussieu, 12(2):
391–447, 2013.
[BZ92]
Jean-Michel Bismut et Weiping Zhang : An extension of a theorem by
Cheeger and Müller. With an appendix by François Laudenbach. Paris :
Société Mathématique de France, 1992.
[BZH14]
Gerhard Burde, Heiner Zieschang et Michael Heusener : Knots. 3rd
fully revised and extented edition. Berlin : Walter de Gruyter, 3rd fully
revised and extented edition édition, 2014.
[CCG+94] Daryl Cooper, Marc Culler, Henri Gillet, Darren D Long et Pe-
ter B Shalen :
Plane curves associated to character varieties of 3-
manifolds. Inventiones mathematicae, 118(1):47–84, 1994.
[Che77]
JeﬀCheeger : Analytic torsion and Reidemeister torsion. Proc. Natl.
Acad. Sci. USA, 74:2651–2654, 1977.
105
[CS83]
Marc Culler et Peter B Shalen : Varieties of group representations
and splittings of 3-manifolds. Annals of Mathematics, pages 109–146,
1983.
[CS84]
Marc Culler et Peter B Shalen : Bounded, separating, incompressible
surfaces in knot manifolds.
Inventiones mathematicae, 75(3):537–545,
1984.
[deR67]
Georges deRham : Introduction aux polynômes d’un nœud. Enseign.
Math. (2), 13:187–194, 1967.
[DFJ12]
Nathan M. Dunfield, Stefan Friedl et Nicholas Jackson : Twisted
Alexander polynomials of hyperbolic knots. Exp. Math., 21(4):329–352,
2012.
[DG16]
Jerome Dubois et Stavros Garoufalidis : Rationality of the SL(2, C)-
Reidemeister torsion in dimension 3. Topol. Proc., 47:115–134, 2016.
[DHY09]
Jérôme Dubois, Vu Huynh et Yoshikazu Yamaguchi : Non-abelian
Reidemeister torsion for twist knots.
J. Knot Theory Ramiﬁcations,
18(3):303–341, 2009.
[Dub06]
Jérôme Dubois : Non abelian twisted Reidemeister torsion for ﬁbered
knots. Can. Math. Bull., 49(1):55–71, 2006.
[Dun99]
Nathan M. Dunfield : Examples of non-trivial roots of unity at ideal
points of hyperbolic 3-manifolds. Topology, 38(2):457–465, 1999.
[FK91]
Charles D Frohman et Eric P Klassen : Deforming representations
of knot groups in su(2). Commentarii Mathematici Helvetici, 66(1):340–
361, 1991.
[Fra35]
Wolfgang Franz : Über die Torsion einer Überdeckung. J. Reine Angew.
Math., 173:245–254, 1935.
[Ful08]
William Fulton : Algebraic curves. An Introduction to Algebraic Geom,
2008.
[GKZ94]
I.M. Gelfand, M.M. Kapranov et A.V. Zelevinsky : Discriminants,
resultants, and multidimensional determinants. Boston, MA : Birkhäu-
ser, 1994.
[Gol84]
William M. Goldman : The symplectic nature of fundamental groups
of surfaces. Adv. Math., 54:200–225, 1984.
106
[HP15]
Michael Heusener et Joan Porti : Representations of knot groups into
SLn(C) and twisted Alexander polynomials. Pac. J. Math., 277(2):313–
354, 2015.
[HPSP01] Michael Heusener, Joan Porti et Eva Suárez-Peiró : Deformations
of reducible representations of 3-manifold groups into sl2(c). Journal fur
die Reine und Angewandte Mathematik, pages 191–228, 2001.
[HT85]
Allen E. Hatcher et William P. Thurston : Incompressible surfaces
in 2-bridge knot complements. Invent. Math., 79:225–246, 1985.
[Jac80]
William Jaco : Lectures on three-manifold topology. Conference Board
of the Mathematical Sciences. Regional Conference Series in Mathema-
tics, 43. Providence, R.I. : American Mathematical Society (AMS). XII,
1980.
[Kit94]
Teruaki Kitano : Reidemeister torsion of the ﬁgure-eight knot exterior
for SL(2, C)-representations. Osaka J. Math., 31(3):523–532, 1994.
[Kit96]
Teruaki Kitano : Twisted Alexander polynomial and Reidemeister tor-
sion. Pac. J. Math., 174(2):431–442, 1996.
[KP96]
Hanspeter Kraft et Claudio Procesi : Classical Invariant Theory, a
Primer. 1996.
[Le14]
Thang Le : Homology torsion growth and Mahler measure. Comment.
Math. Helv., 89(3):719–757, 2014.
[Liu06]
Qing Liu : Algebraic geometry and arithmetic curves. Transl. by Reinie
Erné. Oxford : Oxford University Press, 2006.
[LM85]
Alexander Lubotzky et Andy R. Magid : Varieties of representations
of ﬁnitely generated groups., volume 336. American Mathematical Society
(AMS), Providence, RI, 1985.
[Mar15]
Julien Marché : Character varieties in sl_2 and kauﬀman skein alge-
bras. arXiv preprint : 1510.09107, 2015.
[MFK93]
D. Mumford, J. Fogarty et F. Kirwan : Geometric invariant theory.
3rd enl. ed. Berlin : Springer-Verlag, 3rd enl. ed. édition, 1993.
[Mil66]
John W. Milnor : Whitehead torsion. Bull. Am. Math. Soc., 72:358–
426, 1966.
[MP12]
Pere Menal-Ferrer et Joan Porti : Twisted cohomology for hyper-
bolic three manifolds. Osaka J. Math., 49(3):741–769, 2012.
107
[Mul78]
Werner Muller : Analytic torsion and R-torsion of Riemannian mani-
folds. Adv. Math., 28:233–305, 1978.
[Mul93]
Werner Muller : Analytic torsion and R-torsion for unimodular repre-
sentations. J. Am. Math. Soc., 6(3):721–753, 1993.
[Oza00]
Makoto Ozawa : Synchronism of an incompressible non-free Seifert sur-
face for a knot and an algebraically split closed incompressible surface in
the knot complement. Proc. Am. Math. Soc., 128(3):919–922, 2000.
[Oza01]
Makoto Ozawa : Additivity of free genus of knots. Topology, 40(4):659–
665, 2001.
[Por97]
Joan Porti : Torsion de Reidemeister pour les variétés hyperboliques.,
volume 612. American Mathematical Society (AMS), Providence, RI,
1997.
[Por15]
Joan Porti : Reidemeister torsion, hyperbolic three-manifolds, and cha-
racter varieties. ArXiv e-prints, novembre 2015.
[Pro87]
Claudio Procesi : A formal inverse to the Cayley-Hamilton theorem.
J. Algebra, 107:63–74, 1987.
[Prz83]
Józef H. Przytycki : Incompressibility of surfaces after Dehn surgery.
Mich. Math. J., 30:289–308, 1983.
[PS00]
Józef H. Przytycki et Adam S. Sikora : On skein algebras and Sl2(C)-
character varieties. Topology, 39(1):115–148, 2000.
[Rei35]
Kurt Reidemeister : Homotopieringe und Linsenräume. Abh. Math.
Semin. Univ. Hamb., 11:102–109, 1935.
[Rol76]
Dale Rolfsen : Knots and links. Mathematical Lecture Series. 7. Ber-
keley, Ca. : Publish or Perish, Inc., 1976.
[RS71]
D.B. Ray et I.M. Singer : R-torsion and the Laplacian on Riemannian
manifolds. Adv. Math., 7:145–210, 1971.
[Sai94]
Kyoji Saito : Character variety of representations of a ﬁnitely generated
group in sl2. 1994.
[SB77]
Jean-Pierre Serre et Hyman Bass : Arbres, amalgames, sl2 ; astérisque
46. 1977.
[Sha02]
Peter B. Shalen : Representations of 3-manifold groups. In Handbook
of geometric topology, pages 955–1044. Amsterdam : Elsevier, 2002.
108
[Til03]
Stephen Tillmann : Finding hyperbolic structures of and surfaces in
3-manifolds. 2003.
[Wei64]
Andre Weil : Remarks on the cohomology of groups. Annals of Mathe-
matics, 80(1):149–157, 1964.
109

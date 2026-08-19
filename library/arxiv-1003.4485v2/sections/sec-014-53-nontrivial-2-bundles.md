---
doc_id: arxiv-1003.4485v2
doc_title: "email: baez@math.ucr.edu huerta@math.ucr.edu"
section_id: sec-014-53-nontrivial-2-bundles
section_title: "Nontrivial 2-Bundles"
section_number: 5.3
pages: 47-60
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describ e parallel trans- port for particles and strings in terms of 2-connections on 2 -bundles."
---
So far we have implicitly been looking at 2-connections on trivial 2-bun dles.
This is ﬁne locally. But there are also interesting issues involving nontr ivial
2-bundles, which become crucial when we work globally.
A careful treatment of 2-bundles would require some work, and th e reader
interested in this topic would do well to start with Moerdijk’s introduc tory
paper on ‘stacks’ and ‘gerbes’ [72]. Here we take a less sophisticate d approach:
we simply describe how to build a principal 2-bundle and put a 2-connec tion
on it. Since we do not say when two principal 2-bundles built this way ar e the
‘same’, our treatment is incomplete. The reader can ﬁnd more details elsewhere
[18, 19, 25, 28, 29, 30, 88]. We warn the reader that almost every p aper in the
literature uses diﬀerent notation, sign conventions, and so forth .
First recall ordinary gauge theory: suppose G is a Lie group and M a man-
ifold. In this case we can build a principal G-bundle over M using transition
functions. First, write M as the union of open sets or patches Ui ⊆ M :
M =
⋃
i
Ui.
Then, choose a smooth transition function on each double intersection of
patches:
gij: Ui ∩ Uj → G.
These transition functions give gauge transformations. We can bu ild a principal
G-bundle over all of M by gluing together trivial bundles over the patches with
the help of these gauge transformations. However, this procedu re will only
47
succeed if the transition functions satisfy a consistency condition on each triple
intersection:
gij(x)gjk (x) = gik(x)
for all x ∈ Ui ∩ Uj ∩ Uk. This equation is called a cocycle condition . We can
visualize it as a triangle:
•
• • gik
/d111/d111
gjk
/d88/d88✶✶✶✶✶✶✶✶✶✶✶✶
gij
/d6/d6✌✌✌✌✌✌✌✌✌✌✌✌
where we suppress the variable x for the sake of readability. The idea is that
this triangle should ‘commute’: the direct way of identifying points in th e trivial
bundle in the ith patch to points in the trivial bundle over the kth patch should
match the indirect way which proceeds via the jth patch.
A similar but more elaborate recipe works for higher gauge theory. N ow let
G be a Lie 2-group with crossed module ( G, H, t, α). To build a G-2-bundle, we
start by choosing transition functions on double intersections of p atches:
gij: Ui ∩ Uj → G
However, now it makes sense to replace the equation in the cocycle c ondition
by a 2-morphism! So, for each triple intersection we choose 2-morp hisms in G:
γijk (x): gij(x) gjk (x) ⇒ gik(x)
depending smoothly on x ∈ Ui ∩ Uj ∩ Uk. We can again visualize these as
triangles:
•
• • gik
/d111/d111
gjk
/d88/d88✶✶✶✶✶✶✶✶✶✶✶✶
gij
/d6/d6✌✌✌✌✌✌✌✌✌✌✌✌
γijk
/d11/d19
But now we demand that these 2-morphisms themselves obey a cocy cle condition
on quadruple intersections of patches. As we ascend the ladder of higher gauge
theory, triangles become tetrahedra and then higher-dimensiona l simplexes. In
48
this case, the cocycle condition says that this tetrahedron commu tes:
•
••
•
gkl
/d79/d79
gjk/d111/d111
gij
/d15/d15
gil
/d111/d111
gik
/d127/d127
gjl
/d95/d95❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄
γijl
/d17/d25✰✰✰✰✰✰
✰✰✰✰✰✰
γjkl/d123/d3 ⑧⑧⑧⑧⑧⑧
⑧⑧⑧⑧⑧⑧
γijk /d27/d35
γikl
/d5/d13
By saying that this tetrahedron ‘commutes’, we mean that the comp osite of the
front two sides equals the composite of the back two sides:
•
••
•
gkl
/d79/d79
gjk/d111/d111
gij
/d15/d15
gil
/d111/d111
gjl
/d95/d95❄❄❄❄❄❄❄❄❄❄❄❄❄❄γijl
/d16/d24✭✭✭✭
✭✭✭✭
γjkl
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
=
•
••
•
gkl
/d79/d79
gjk/d111/d111
gij
/d15/d15
gil
/d111/d111/d127/d127⑧⑧⑧⑧⑧⑧⑧⑧⑧⑧⑧⑧⑧⑧gik
γijk
/d27/d35❄❄❄❄
❄❄❄❄
γikl
/d6/d14 ✖✖✖✖
✖✖✖✖
We need whiskering to compose the 2-morphisms in this diagram, as ex plained
near the end of Section 3. So in equations, the tetrahedral cocyc le condition
says that:
γijl · (gij ◦ γjkl ) = γikl · (γijk ◦ gkl)
where · stands for vertical composition and ◦ stands for whiskering.
We can describe this cocycle condition in a more down-to-earth mann er if
we use Theorem 2, which says that a 2-morphism
γijk : gij gjk ⇒ gik
is the same as an element hijk ∈ H such that
t(hijk ) gij gjk = gik.
This theorem also gives formulas for vertical and horizontal compo sition in
terms of the groups G and H. Since whiskering by a morphism is horizontal
composition with its identity 2-morphism, we can also express whisker ing in
these terms. So, a little calculation—a wonderful exercise for the w ould-be
higher gauge theorist—shows that:
hijl α(gij)(hjkl ) = hikl hijk
where α is the action of G on H.
There is no need to have gii = 1 in this formalism; we should really choose
a 2-morphism from gii to 1. However, without loss of generality, we can assume
49
that gii = 1 and set this 2-morphism equal to the identity. We can also assume
that hijk = 1 whenever two or more of the indices i, j, k are equal. The reason
is that Bartels [25] has shown that any principal 2-bundle is equivalen t to one
for which these simplifying assumptions hold. We will make these assum ptions
in what follows. For the full story without these assumptions, see S chreiber and
Waldorf [88].
Now consider connections. Again, it helps to begin by reviewing the st ory
for ordinary gauge theory. Suppose we have a manifold M written as a union
of patches Ui, and suppose we have principal G-bundle over M built using
transition functions gij. To put a connection on this bundle, we ﬁrst put a
connection on the trivial bundle over each patch: that is, for each i, we choose
a g-valued 1-form Ai on Ui. But then we must check to see if these ﬁt together
to give a well-deﬁned connection on all of M . For this, we need the gauge
transform of the connection on the jth patch to equal the connection on the ith
patch:
Ai = gijAj g−1
ij + gijdg−1
ij
on each double intersection Ui ∩ Uj.
The story is similar for 2-connections. Suppose we have a principal G-2-
bundle over M built using transition functions gij and hijk as described above.
To equip this 2-bundle with a 2-connection, we ﬁrst put a 2-connect ion on the
trivial 2-bundle over each patch. So, on each open set Ui we choose a g-valued
1-form Ai and an h-valued 2-form Bi with t(Bi) = Fi. But then we must ﬁt
these together to get a 2-connection on all of M .
For this, we should follow the ideas from Section 5.1 on how gauge tran sfor-
mations work in higher gauge theory. So, we choose an h-valued 1-form aij on
each double intersection Ui ∩ Uj, and require that
Ai = gijAj g−1
ij + gij dg−1
ij + t(aij)
Bi = α(gij)(Bj ) + α(Ai) ∧ aij + daij − aij ∧ aij.
These equations say that the 2-connection ( Ai, Bi) is a gauge-transformed ver-
sion of ( Aj , Bj). The appearance of Ai on the right-hand side of the second
equation is not a typo! Finally, the 1-forms aij must obey a consistency condi-
tion on triple intersections:
h−1
ijk α(Ai)(hijk ) + h−1
ijk dhijk + α(gij)(ajk ) + aij = h−1
ijk aik hijk (2)
Where does this consistency condition come from? Indeed, what do es it even
mean? We have not yet deﬁned ‘ h−1α(A)(h)’ when A ∈ g and h is an element
of the group H.
We could systematically derive this condition from a more conceptual ap-
proach to 2-connections [16, 88], but it will be marginally less stressf ul to mo-
tivate it as follows. For every triple intersection Ui ∩ Uj ∩ Uk we have three
50
equations relating Ai, Aj and Ak:
Ai = gijAjg−1
ij + gij dg−1
ij + t(aij)
Aj = gjk Akg−1
jk + gjk dg−1
jk + t(ajk )
Ak = gkiAig−1
ki + gki dg−1
ki + t(aki)
The ﬁrst equation expresses Ai in terms of Aj. We can substitute the second
equation in the ﬁrst to get a formula for Ai in terms of Ak. Then we can use
the third equation to get a formula for Ai in terms of itself! We would like to be
able to simplify this formula to get simply Ai = Ai. The consistency condition,
Equation (2), ensures that we can do this.
This calculation is a bit of a workout; let us see how it goes. We begin by
doing the substitutions:
Ai = gijAjg−1
ij + gij dg−1
ij + t(aij)
= gij
(
gjk Akg−1
jk + gjk dg−1
jk + t(ajk )
)
g−1
ij + gij dg−1
ij + t(aij)
= gij
(
gjk
(
gkiAig−1
ki + gkidg−1
ki + t(aki)
)
g−1
jk + gjk dg−1
jk + t(ajk )
)
g−1
ij +
gij dg−1
ij + t(aij).
Then we do a bit of simpliﬁcation:
Ai = gijgjkgkiAi(gijgjkgki)−1 + gijgjkgkid(gijgjkgki)−1 +
gijgjkt(aki)(gijgjk)−1 + gijt(ajk )g−1
ij + t(aij).
Since t(hijk ) gij gjk = gik and by our assumptions g−1
ik = gki, we have
gijgjkgki = t(hijk )−1
so
0 = t(hijk )−1 Ai t(hijk ) − Ai + t(hijk )−1 dt(hijk ) +
t(hijk )−1gikt(aki)g−1
ik t(hijk ) + gijt(ajk )g−1
ij + t(aij). (3)
Now, if G is a matrix group, we can freely multiply group elements and Lie
algebra elements. Then for any h ∈ H and A ∈ g we have
t(h)−1At(h) − A = t(h)−1[A, t(h)]. (4)
This will allow us to simplify the ﬁrst two terms in Equation (3). Moreove r, for
any g ∈ G, h ∈ H we have
t(h−1α(g)h) = t(h)−1t(α(g)(h)) = t(h)−1gt(h)g−1.
Taking g = exp(sA) for A ∈ g and diﬀerentiating this equation with respect to
s at s = 0, we get
t(h−1α(A)(h)) = t(h)−1At(h) − A (5)
51
where on the left side α means the derivative of the map α: G × H → H with
respect to its ﬁrst argument, while t is the derivative of t. Here are we extending
our previous deﬁnitions of α and t. Combining Equations (4) and (5) we see
that
t(h)−1[A, t(h)] = t
(
h−1α(A)(h)
)
.
In fact this result holds even when G is a non-matrix Lie group, as long as we
carefully make sense of both sides.
Using this result, we can rewrite Equation (3) as follows:
0 = t(h−1
ijk α(Ai)(hijk )) + t(hijk )−1 dt(hijk ) +
t(hijk )−1gik t(aki) g−1
ik t(hijk ) + gij t(ajk ) g−1
ij + t(aij)
Each term in the above equation is t applied to an h-valued 1-form. Writing
down all these h-valued 1-forms, we see that the above equation will be true if
this condition holds:
0 = h−1
ijk α(Ai)(hijk ) + h−1
ijk dhijk + h−1
ijk α(gik)(aki)hijk + α(gij)(ajk ) + aij
This is our consistency condition in disguise! To remove the disguise, le t us
simplify it a bit further. When i = j this condition reduces to
aik + α(gik)(aki) = 0 .
Reinserting this result we obtain
0 = h−1
ijk α(Ai)(hijk ) + h−1
ijk dhijk − h−1
ijk aik hijk + α(gij)(ajk ) + aij
Voil` a! This is clearly equivalent to the consistency condition we stated in the
ﬁrst place, Equation (2):
h−1
ijk α(Ai)(hijk ) + h−1
ijk dhijk + α(gij)(ajk ) + aij = h−1
ijk aik hijk
Now let us consider some examples. Recall from Section 4.1 that bU(1 ) is
2-group with one morphism and U(1) as its group of 2-morphisms. A U(1)
gerbe is principal bU(1)-2-bundle. Let’s look at principal U(1)-bundles an d
then U(1) gerbes, to get a feel for how they are similar and how the y diﬀer.
To build a principal U(1)-bundle with a connection on it, we choose tra nsi-
tion functions
gij: Ui ∩ Uj → U(1)
such that
gijgjk = gik
on each triple intersection. To put a connection on this bundle, we th en choose
a 1-form Ai on each patch such that
Ai = Aj + gijdg−1
ij
52
on each double intersection Ui ∩ Uj. The curvature of this connection is then
Fi = dAi
on the ith patch. Note that Fi = Fj on Ui ∩ Uj, so we get a well-deﬁned
curvature 2-form F on all of M .
To build a U(1) gerbe, we choose transition functions hijk : Ui ∩ Uj ∩ Uk →
U(1) such that
hjkl hijl = hiklhijk
on each quadruple intersection. Remember, the 2-group bU(1) ha s only one
morphism, the identity, so the transition functions gij are trivial and can be
ignored. To put a 2-connection on this gerbe, we must ﬁrst choose a 2-form Bi
on each patch. Then we must choose a 1-forms aij on each double intersection.
We require that
Bi = Bj + daij
on each double intersection, and
aij + ajk = aik + hijk dh−1
ijk
on each triple intersection. The 2-curvature of this 2-connection is then
Zi = dBi
on the ith patch. Note that Zi = Zj on Ui ∩ Uj, so we get a well-deﬁned
2-curvature 3-form Z on all of M .
There is a nice link between U(1) gerbes and cohomology, which in fact is
the reason they were invented in the ﬁrst place. For any principal U (1)-bundle
with connection, the curvature F is integral:
∫
Σ
F ∈ 2πZ
for any closed surface Σ mapped into M . In addition, F is closed:
dF = 0.
Conversely, any closed, integral 2-form F on M is the curvature of some con-
nection on a principal U(1)-bundle over M . Two diﬀerent connections on the
same bundle have curvature 2-forms that diﬀer by an exact 2-for m, so we get
a well-deﬁned element of the de Rham cohomology H 2(M, R) from a principal
U(1)-bundle. This idea can be reﬁned further, and the upshot is th at principal
U(1)-bundles over M are classiﬁed by the cohomology group H 2(M, Z).
Similarly, for any U(1) gerbe, the curvature 3-form Z is closed and integral,
where the latter term now means that
∫
Y
Z ∈ 2πZ
53
for any closed 3-manifold Y mapped into M . Conversely, any such 3-form is the
2-curvature of some 2-connection on a U(1) gerbe over M —and in fact, U(1)
gerbes over M are classiﬁed by H 3(M, Z).
This is just the beginning of a longer tale: namely, the story of chara cteristic
classes in higher gauge theory [18, 83]. Indeed, though higher gaug e theory is
only in its infancy, there is much more to say. But our story ends her e. We
invite the reader to go further.
Acknowledgements
This paper is based on JH’s notes of lectures given by JB at the 2nd Sc hool and
Workshop on Quantum Gravity and Quantum Geometry, held as part of the
2010 Corfu Summer Institute. We thank George Zoupanos, Harald Grosse, and
everyone else involved with the Corfu Summer Institute for making o ur stay
a pleasant and productive one. We thank Urs Schreiber for many dis cussions
of higher gauge theory, and thank Tim van Beek, David Roberts and Elliot
Schneider for catching some errors. This research was partially su pported by
an FQXi grant.
References
[1] P. Aschieri, L. Cantini, and B. Jurˇ co, Nonabelian bundle gerbes, their
diﬀerential geometry and gauge theory, Comm. Math. Phys. 254 (2005),
367–400. Also available as arXiv:hep-th/0312154.
[2] P. Aschieri and B. Jurˇ co, Gerbes, M5-brane anomalies and E8 gauge theory,
JHEP 10 (2004) 068. Also available as arXiv:hep-th/0409200.
[3] A. Ashtekar and J. Lewandowski, Diﬀerential geometry on the s pace of
connections via graphs and projective limits, J. Geom. Phys. 17 (1995),
191–230. Also available as arXiv:hep-th/9412073.
[4] J. Baez, Four-dimensional BF theory as a topological quantum ﬁeld theory,
Lett. Math. Phys. 38 (1996), 129–143.
[5] J. Baez, Spin foam models, Class. Quantum Grav. 15 (1998), 1827–1858.
Also available as arXiv:gr-qc/9709052.
J. Baez, An introduction to spin foam models of BF theory and quan-
tum gravity, in Geometry and Quantum Physics , eds. H. Gausterer and H.
Grosse, Springer, Berlin, 2000, pp. 25–93.
[6] J. Baez, A. Baratin, L. Freidel and D. Wise, Inﬁnite-dimensional represen-
tations of 2-groups. Available as arXiv:0812.4969.
[7] J. Baez and A. Crans, Higher dimensional algebra VI: Lie 2-algebr as, The-
ory and Applications of Categories 12 (2004), 492–538. Also available as
arXiv:math/0307263.
54
[8] J. Baez, A. Crans, U. Schreiber and D. Stevenson From loop gro ups to 2-
groups, HHA 9 (2007), 101–135. Also available as arXiv:math.QA/0504123.
[9] J. Baez, A. Crans and D. Wise, Exotic statistics for strings in 4d BF
theory, Adv. Theor. Math. Phys. 11 (2007), 707–749. Also available as
arXiv:gr-qc/0603085.
[10] J. Baez, A. Hoﬀnung, C. Rogers, Categoriﬁed symplectic geom etry and the
classical string, Comm. Math. Phys. 293 (2010), 701–715. Also available
as arXiv:0808.0246.
[11] J. Baez and J. Huerta, Division algebras and supersymmetry II . Available
as arXiv:1003.3436.
[12] J. Baez and A. Lauda, A prehistory of n-categorical physics. Available as
arXiv:0908.2469.
[13] J. Baez and A. Lauda, Higher dimensional algebra V: 2-groups, The-
ory and Applications of Categories 12 (2004), 423–491. Also available as
arXiv:math/0307200.
[14] J. Baez and A. Perez, Quantization of strings and branes coup led to
BF theory, Adv. Theor. Math. Phys. 11 (2007), 1–19. Also available as
arXiv:gr-qc/0605087.
[15] J. Baez and C. Rogers, Categoriﬁed symplectic geometry and t he string Lie
2-algebra, to appear in Homology, Homotopy and Applications . Available
as arXiv:0901.4721.
[16] J. Baez and U. Schreiber, Higher gauge theory, in Categories in Al-
gebra, Geometry and Mathematical Physics , eds. A. Davydov et al,
Contemp. Math. 431, AMS, Providence, 2007, pp. 7–30. Also availa ble
arXiv:math/0511710.
[17] J. Baez and S. Sawin, Functional integration on spaces of conn ections, J.
Funct. Analysis 150 (1997), 1-26. Also available as arXiv:q-alg/9507023.
[18] J. Baez and D. Stevenson, The classifying space of a topologica l 2-group,
in Algebraic Topology: The Abel Symposium 2007 , eds. Nils Baas, Eric
Friedlander, Bjørn Jahren and Paul Arne Østvær, Springer, Berlin , 2009.
[19] I. Bakovic and B. Jurˇ co, The classifying topos of a topological bicategory.
Available as arXiv:0902.1750.
[20] A. P. Balachandran, F. Lizzi and G. Sparano, A new approach t o strings
and superstrings, Nucl. Phys. B277 (1986), 359-387.
[21] A. Baratin and L. Freidel, Hidden quantum gravity in 3d Feynman d i-
agrams, Class. Quant. Grav. 24 (2007), 1993–2026. Also available as
arXiv:gr-qc/0604016.
55
[22] A. Baratin and L. Freidel, Hidden quantum gravity in 4d Feynman d ia-
grams: emergence of spin foams, Class. Quant. Grav. 24 (2007), 2027–2060.
Also available as arXiv:hep-th/0611042.
[23] A. Baratin and D. Wise, 2-Group representations for spin foam s. Available
as arXiv:0910.1542.
[24] J. W. Barrett and M. Mackaay, Categorical representations of cate-
gorical groups, Th. Appl. Cat. 16 (2006), 529–557 Also available as
arXiv:math/0407463.
[25] T. Bartels, Higher gauge theory: 2-bundles. Available as
arXiv:math.CT/0410328.
[26] Jean B´ enabou, Introduction to bicategories, in Reports of the Midwest
Category Seminar , Springer, Berlin, 1967, pp. 1–77.
[27] F. Borceux, Handbook of Categorical Algebra 1: Basic Category Theory ,
Cambridge U. Press, Cambridge, 1994.
[28] L. Breen, Notes on 1- and 2-gerbes, in Towards Higher Categories , eds. J.
Baez and P. May, Springer, Berlin, 2009, pp. 193–235. Also available as
arXiv:math/0611317.
[29] L. Breen, Diﬀerential geometry of gerbes and diﬀerential for ms. Available
as arXiv:0802.1833.
[30] L. Breen and W. Messing, Diﬀerential geometry of gerbes, Adv. Math. 198
(2005), 732–846. Available as arXiv:math.AG/0106083.
[31] J.-L. Brylinski, Loop Spaces, Characteristic Classes and Geometric Quan-
tization, Birkh¨ auser, Boston, 1993.
[32] J.-L. Brylinski, Diﬀerentiable cohomology of gauge groups. Availa ble as
arXiv:math.DG/0011069.
[33] J.-L. Brylinski and D. A. McLaughlin, The geometry of degree-f our char-
acteristic classes and of line bundles on loop spaces I, Duke Math. J. 75
(1994), 603–638.
J.-L. Brylinski and D. A. McLaughlin, The geometry of degree-four char-
acteristic classes and of line bundles on loop spaces II, Duke Math. J. 83
(1996), 105–139.
[34] A. L. Carey, S. Johnson and M. K. Murray, Holonomy on D-bran es, Jour.
Geom. Phys. 52 (2004), 186–216. Also available as arXiv:hep-th/0204199.
[35] L. Crane, L. Kauﬀman and D. Yetter, State-sum invariants of 4-manifolds
I. Available as arXiv:hep-th/9409167.
[36] L. Crane and M. D. Sheppeard, 2-Categorical Poincar´ e repr esentations and
state sum applications, available as arXiv:math/0306440.
56
[37] L. Crane and D. Yetter, A categorical construction of 4d TQF Ts, in Quan-
tum Topology, eds. L. Kauﬀman and R. Baadhio, World Scientiﬁc, Singa-
pore, 1993, pp. 120-130. Also available as arXiv:hep-th/9301062.
[38] L. Crane and D. N. Yetter, Measurable categories and 2-grou ps, Appl. Cat.
Str. 13 (2005), 501–516. Also available as arXiv:math/0305176.
[39] T. DeDonder, Theorie Invariantive du Calcul des Variations , Gauthier–
Villars, Paris, 1935.
[40] C. DeWitt-Morette, A. Maheshwari, and B. Nelson, Path integr ation in
phase space, Gen. Relativity Gravitation 8 (1977), 581–593.
[41] L. Castellani, R. D’Auria and P. Fr´ e, Supergravity and Superstrings: A
Geometric Perspective , World Scientiﬁc, Singapore, 1991.
[42] M. J. Duﬀ, Supermembranes: the ﬁrst ﬁfteen weeks, Class. Quantum Grav.
5 (1988), 189–205. Also available at
⟨http://www-lib.kek.jp/cgi-bin/img index?8708425⟩.
[43] B. Eckmann and P. Hilton, Group-like structures in categories, Math. Ann.
145 (1962), 227-255.
[44] S. Eilenberg and S. Mac Lane, General theory of natural equiv alences,
Trans. Amer. Math. Soc. 58 (1945), 231–294.
[45] C. Ehresmann, Cat´ egories topologiques et cat´ egories diﬀer entiables, Coll.
G´ eom. Diﬀ. Globale (Bruxelles, 1958), Centre Belge Rech. Math. Louvain,
1959, pp. 137–150.
[46] C. Ehresmann, Cat´ egories structur´ ees,Ann. Ecole Norm. Sup. 80 (1963),
349–426.
[47] C. Ehresmann, Cat´ egories et Structures, Dunod, Paris, 1965.
[48] J. Elgueta, Representation theory of 2-groups on Kapranov and Voevod-
sky 2-vector spaces, Adv. Math. 213 (2007), 53–92. Also available as
arXiv:math/0408120.
[49] W. Fairbairn and A. Perez, Extended matter coupled to BF theory, Adv.
Theor. Math. Phys. D78:024013 (2008). Also available as arXiv:0709.4235.
[50] W. Fairbairn, K. Noui and F. Sardelli, Canonical analysis of algebr aic string
actions. Available as arXiv:0908.0953.
[51] M. Forrester-Barker, Group objects and internal categor ies, available as
arXiv:math.CT/0212065.
[52] D. S. Freed and E. Witten, Anomalies in string theory with D-Bran es, §6:
Additional remarks, Asian J. Math. 3 (1999) 819–852. Also available as
arXiv:hep-th/9907189.
57
[53] L. Freidel and D. Louapre: Ponzano–Regge model revisited. I : Gauge ﬁx-
ing, observables and interacting spinning particles, Class. Quant. Grav. 21
(2004), 5685–5726. Also available as arXiv:hep-th/0401076.
L. Freidel and D. Louapre: Ponzano–Regge model revisited. II: E quivalence
with Chern–Simons. Also available as arXiv:gr-qc/0410141.
L. Freidel and E. Livine: Ponzano–Regge model revisited. III: Fey nman
diagrams and eﬀective ﬁeld theory. Also available as arXiv:hep-th/05 02106.
[54] K. Gawedzki, Topological actions in two-dimensional quantum ﬁe ld theo-
ries, in Nonperturbative Quantum Field Theory , eds. G. t’Hooft, A. Jaﬀe,
G. Mack P. K. Mitter and R. Stora, Plenum, New York, 1988, pp. 101 –141.
[55] K. Gawedzki and N. Reis, WZW branes and gerbes, Rev. Math. Phys. 14
(2002), 1281–1334. Also available as arXiv:hep-th/0205233.
[56] E. Getzler, Lie theory for nilpotent L∞-algebras. Available as
arXiv:math/0404003.
[57] M. Gotay, J. Isenberg, J. Marsden, and R. Montgomery, Mom entum maps
and classical relativistic ﬁelds. Part I: covariant ﬁeld theory, availa ble as
arXiv:physics/9801019.
[58] F. Girelli and H. Pfeiﬀer, Higher gauge theory - diﬀerential vers us integral
formulation, Jour. Math. Phys. 45 (2004), 3949–3971. Also available as
arXiv:hep-th/0309173.
[59] F. Girelli, H. Pfeiﬀer and E. M. Popescu, Topological higher gauge theory -
from BF to BF CG theory, J. Math. Phys. 49:032503, 2008. Also available
as arXiv:0708.3051.
[60] V. Guillemin and S. Sternberg, Symplectic Techniques in Physics , Cam-
bridge U. Press, Cambridge, 1984.
[61] A. Henriques, Integrating L∞-algebras. Available as arXiv:math/0603563.
[62] M. Johnson, The combinatorics of n-categorical pasting, Jour. Pure Appl.
Alg. 62 (1989), 211–225.
[63] S. Lack, A 2-categories companion, in Towards Higher Categories , eds.
J. Baez and P. May, Springer, 2009, pp. 105–191. Also available as
arXiv:math/0702535.
[64] E. Lerman, Orbifolds as stacks?, available as arXiv:0806.4160.
[65] J. Lewandowski and T. Thiemann, Diﬀeomorphism invariant quan tum ﬁeld
theories of connections in terms of webs, Class. Quant. Grav. 16 (1999),
2299–2322. Also available as arXiv:gr-qc/9901015.
[66] S. Mac Lane and J. H. C. Whitehead, On the 3-type of a complex, Proc.
Nat. Acad. Sci. 36 (1950), 41–48.
58
[67] M. Mackaay and R. Picken, Holonomy and parallel transport for
Abelian gerbes, Adv. Math. 170 (2002), 287–339. Also available as
arXiv:math.DG/0007053.
[68] M. Markl, S. Schnider and J. Stasheﬀ, Operads in Algebra, Topology and
Physics, AMS, Providence, Rhode Island, 2002.
[69] J. F. Martins and R. Picken, On two-dimensional holonomy. Availa ble as
arXiv:0710.4310.
J. F. Martins and R. Picken, A cubical set approach to 2-bundles wit h
connection and Wilson surfaces. Available as arXiv:0808.3964.
[70] J. F. Martins and R. Picken, The fundamental Gray 3-groupoid of a smooth
manifold and local 3-dimensional holonomy based on a 2-crossed mod ule.
Available as arXiv:0907.2566
[71] J. Milnor, Remarks on inﬁnite dimensional Lie groups, Relativity, Groups
and Topology II, (Les Houches, 1983) , North-Holland, Amsterdam, 1984.
[72] I. Moerdijk, Introduction to the language of stacks and gerb es. Available
as arXiv:math.AT/0212266.
[73] M. Montesinos and A. Perez, Two-dimensional topological ﬁeld t heories
coupled to four-dimensional BF theory, Phys. Rev. D77:104020 (2008).
Also available as arXiv:0709.4235.
[74] M. K. Murray, Bundle gerbes, J. London Math. Soc. 54 (1996), 403–416.
Also available as arXiv:dg-ga/9407015.
M. K. Murray, An introduction to bundle gerbes. Available as
arXiv:0712.1651.
[75] M. K. Murray and D. Stevenson, Higgs ﬁelds, bundle gerbes and string
structures, Commun. Math. Phys. 243 (2003), 541–555. Also available as
arXiv:math.DG/0106179.
[76] H. Pfeiﬀer, Higher gauge theory and a non-Abelian generalizatio n of 2-
form electromagnetism, Ann. Phys. 308 (2003), 447–477. Also available
as arXiv:hep-th/0304074.
[77] A. J. Power, A 2-categorical pasting theorem, Jour. Alg. 129 (1990), 439-
445.
[78] A. Pressley and G. Segal, Loop Groups , Oxford U. Press, Oxford, 1986.
[79] D. Roberts and U. Schreiber, The inner automorphism 3-group of a strict
2-group. Also available as arXiv:0708.1741.
[80] C. Rovelli, Quantum Gravity, Cambridge U. Press, 2004. Also available at
⟨http://www.cpt.univ-mrs.fr/∼rovelli/book.pdf⟩.
59
[81] D. Roytenberg, On weak Lie 2-algebras. Available as arXiv:0712.3 461.
[82] H. Sati, Geometric and topological structures related to M-br anes. Avail-
able as arXiv:1001.5020.
[83] H. Sati, U. Schreiber and J. Stasheﬀ, L∞-algebras and applications to
string- and Chern–Simons n-transport. Available as arXiv:0801.3480.
[84] M. Schlessinger and J. Stasheﬀ, The Lie algebra structure of t angent coho-
mology and deformation theory, Jour. Pure App. Alg. 38 (1985), 313–322.
[85] C. Schommer-Pries, A ﬁnite-dimensional string 2-group. Availa ble as
arXiv:0911.2483.
[86] U. Schreiber, comments at the n-Category Caf´ e. Available at
⟨http://golem.ph.utexas.edu/category/2009/09/questions on ncurvature.html⟩.
[87] U. Schreiber and K. Waldorf, Parallel transport and functors , J. Homotopy
Relat. Struct. 4 (2009), 187–244. Also available as arXiv:0705.0452.
[88] U. Schreiber and K. Waldorf, Smooth functors vs. diﬀerential forms. Avail-
able as arXiv:0802.0663.
U. Schreiber and K. Waldorf, Connections on non-abelian gerbes an d their
holonomy. Available as arXiv:0808.1923.
[89] D. Stevenson, The Geometry of Bundle Gerbes , Ph.D. thesis, University of
Adelaide, 2000. Also available as arXiv:math.DG/0004117.
[90] S. Stolz and P. Teichner, What is an elliptic object?, in Topology, Geometry
and Quantum Field Theory: Proceedings of the 2002 Oxford Sympos ium in
Honour of the 60th Birthday of Graeme Segal , ed. U. Tillmann, Cambridge
U. Press, Cambridge, 2004.
[91] K. Waldorf, String connections and Chern–Simons theory. Ava ilable as
arXiv:0906.0117.
[92] H. Weyl, Geodesic ﬁelds in the calculus of variation for multiple integ rals,
Ann. Math. 36 (1935), 607–629.
[93] J. H. C. Whitehead, Note on a previous paper entitled ‘On adding r elations
to homotopy groups’, Ann. Math. 47 (1946), 806–810.
J. H. C. Whitehead, Combinatorial homotopy II, Bull. Amer. Math. Soc.
55 (1949), 453–496
[94] E. Witten, The index of the Dirac operator in loop space, in Elliptic Curves
and Modular Forms in Algebraic Topology , ed. P. S. Landweber, Lecture
Notes in Mathematics 1326, Springer, Berlin, 1988, pp. 161–181.
60

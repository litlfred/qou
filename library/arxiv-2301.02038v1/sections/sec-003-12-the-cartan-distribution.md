---
doc_id: arxiv-2301.02038v1
doc_title: "Vinogradov's Cohomological Geometry of Partial Differential Equations"
section_id: sec-003-12-the-cartan-distribution
section_title: "the Cartan distribution"
section_number: 1.2
pages: 6-10
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
doc_brief: "Vinogradov's Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a system of possibly non-li"
---
is the Cartan distribution . There are several equivalent ways to deﬁne it. The
one we present here will be also useful in deﬁning the prolong ation of a PDE in
the next subsection. We begin noticing that a section of the ﬁ bration J 1(P,n )→
J 0(P,n )∼
=P can be interpreted as an n-dimensional distribution on P . Now, for
every 1≤k≤∞ , the k-jet space is canonically equipped with a rank n distribution
along the projection Jk(P,n )→Jk−1(P,n ), i.e. a smooth map
C :Jk(P,n )−→J 1(
Jk−1(P,n ),n
)
such that the following diagram commutes
J 1(
Jk−1(P,n ),n
)
/d15/d15
Jk(P,n )
C
/d55/d55♥♥♥♥♥♥♥♥♥♥♥
/d47/d47Jk−1(P,n )
.
The Cartan distribution C is deﬁned as follows. For z =Nk
p∈Jk(P,n ), denote by
¯z =Nk−1
p ∈Jk−1(P,n ) its projection. Now put
Cz :=
(
Nk−1) 1
¯z =T¯z
(
Nk−1)
∈J 1(
Jk−1(P,n ),n
)
.
In other words Cz is the 1-jet at ¯z of the (k− 1)-jet prolongation of N . In local
coordinates
(1.3) C ∗(uα
I,j ) = uα
Ij, |I|≤ k− 1, j = 1,...,n,
where, in the left hand side, we denoted by (xi,uα
I,j ) the jet coordinates on the 1-jet
spaceJ 1(
Jk−1(P,n ),n
)
(corresponding to the coordinates (xi,uα
I ) onJk−1(P,n )),
and, in the right hand side, we are using concatenation of mul tiindexes.
Remark 1.5. The Cartan distribution C :Jk(P,n )−→J 1(
Jk−1(P,n ),n
)
is an
embedding that we often use to interpret the k-jet space Jk(P,n ) as a submanifold
in the jet space J 1(
Jk−1(P,n ),n
)
. More generally for any two non-negative integers
h,k , there is an embedding
Jh+k(P,n )֒→Jh(
Jk(P,n ),n
)
given by
Nh+k
p ↦→(Nk)h
p, p =Nk
p.
VINOGRADOV’S COHOMOLOGICAL GEOMETRY OF PDES 7
In the next subsection we will use this embedding to interpre t Jh+k(P,n ) as a
submanifold in Jh(
Jk(P,n ),n
)
.
Fork =∞, the Cartan distribution is a honest rank n distribution onJ ∞(P,n ),
and (1.3) shows that it is locally spanned by the total derivatives , i.e. the following
vector ﬁelds
Di := ∂
∂xi +
∑
|I|<∞
uα
Ii
∂
∂uα
I
, i = 1,...,n.
Dually, the annihilator C 0⊆T ∗J ∞(P,n ) is spanned by the Cartan forms
duα
I−uα
Iidxi, α = 1,...,m, |I|≤∞ .
Here, and in the rest of the paper, we adopt the Einstein summa tion conven-
tion over pairs of lowercase-uppercase indexes. We will not adopt the Einstein
convention for multiindexes.
Proposition 1.6. The Cartan distribution on J ∞(P,n ) is involutive, i.e. the
commutator of two sections of C lays in C as well. Additionally it detects ∞-jet
prolongations in the following sense: a submanifold S⊆J ∞(P,n ) is locally of the
form S = N ∞ for some n-dimensional submanifold N⊆ P if and only if it is an
n-dimensional integral submanifold of C .
So, morally, the∞-jet prolongation constructionN↦→N ∞ identiﬁes n-dimensional
submanifolds of P withn-dimensional integral submanifolds of C . In the following,
Cartan distribution will always mean the Cartan distribution on J ∞(P,n ) (unless
otherwise stated).
For their importance in the next section, we now discuss inﬁnitesimal sym-
metries of the Cartan distribution C , i.e. vector ﬁelds Y on J ∞(P,n ) such that
[Y, Γ( C )]⊆ Γ( C ). Denote by XC the Lie algebra of inﬁnitesimal symmetries of C
and notice that, by involutivity, Γ( C )⊆ XC is an ideal. We want to show that
the quotient Lie algebra XC/Γ( C ) identiﬁes with sections of an appropriate vector
bundleV →J ∞(P,n ). We ﬁrst deﬁne V . So let z =N ∞
p ∈J ∞(P,n ). The ﬁber of
V overz is then the m-dimensional vector space
Vz :=TpP/TpN.
In the following, we denote by π :J ∞(P,n )→P the projection. Now, let Y ∈ XC .
We deﬁne a section
Y of V as follows. For z =N ∞
p ∈J ∞(P,n ) put
Yz :=dπ(Yz) modTpN∈TpP/TpN =Vz.
Proposition 1.7. The assignment Y ↦→Y deﬁnes an R-linear surjection
XC → Γ(V ) with kernel given by Γ( C ). Hence there is a canonical short exact
sequence of vector spaces
0−→ Γ( C )−→ XC−→ Γ(V )−→ 0.
In particular, Γ(V ) inherits from XC a Lie bracket.
The Lie bracket on Γ(V ) is sometimes called the higher Jacobi bracket and
denoted by {−,−}. We conclude this section describing it in local coordinate s.
First notice that Γ(V ) is locally spanned by the sections vα deﬁned as follows. For
z =N ∞
p ∈J ∞(P,n ) put
vα|z := ∂
∂uα|p modTpN∈TpP/TpN =Vz.
8 F ABRIZIO PUGLIESE, GIOV ANNI SPARANO, AND LUCA VITAGLIANO
The isomorphism Γ(V )∼
= XC/Γ( C ) is now locally given by
χ↦→Зχ mod Γ( C )
where, for χ =χαvα∈ Γ(V ), we denoted by Зχ the (local) inﬁnitesimal symmetry
of C locally given by
(1.4) Зχ =
∑
|I|<∞
DIχα ∂
∂uα
I
,
and, for any multiindex i1··· ih,
Di1···ih :=Di1◦···◦ Dih.
We mention for the reader unfamiliar with the cyrillic alpha bet, that the script
З appearing in (1.4) is pronounced [e], like in se
t.
A vector ﬁeld of the form Зχ is sometimes called an evolutionary vector ﬁeld .
Notice that evolutionary vector ﬁelds are only locally deﬁn ed on∞-jets of subman-
ifolds (while one can give a coordinate free meaning to (1.4) on∞-jets of sections
of a ﬁbration, see e.g. [ 2, Chapter 4, Section 2.4] or [ 11, Section 3.9] ). It easily
follows from (1.4) that, if χ andψ are sections of V locally given by χ =χαvα and
ψ =ψβvβ, then their higher Jacobi bracket {χ,ψ} is the section locally given by
{χ,ψ} =
(
Зχψα− Зψχα)
vα =
∑
|I|<∞
(
DIχβ∂ψα
∂uβ
I
−DIψβ∂χα
∂uβ
I
)
vα.
1.3. diﬃeties. We now use jets to deﬁne PDEs and present their geometric
portraits: diﬃeties. Let P be a manifold of dimension n +m.
Definition 1.8. A system of k-th order partial diﬀerential equations imposed
on n-dimensional submanifolds of P , or simply a PDE, is a closed submanifold
E0 ⊆ Jk(P,n ) of the k-jet space. A solution of a PDE E0 ⊆ Jk(P,n ) is an n-
dimensional submanifold N⊆P such that Nk⊆ E0.
Remark 1.9. As a minimal regularity condition on a PDE E0⊆ Jk(P,n ) we
will always assume dim E0≥n so that the existence of solutions is not excluded a
priori by trivial dimensional reasons.
For a PDE E0⊆Jk(P,n ), locally, in jet coordinates, we have
(1.5) E0 :Fa(x,...,u I,... ) = 0, |I|≤ k,
for some local smooth functions Fa∈C∞(Jk(P,n )). If N⊆P is an n-dimensional
submanifold locally given by
N :uα =fα(x),
then N is a solution of E0 iﬀ
Fa
(
x,..., ∂|I|f
∂xI ,...
)
= 0.
This motivates Deﬁnition 1.8.
In Algebraic Geometry, given a system of algebraic equation s, it is natural to
take all their algebraic consequences. In other words, give n a subset of polynomials,
it is natural to consider the ideal that they span. Similarly , given a PDE (1.5), it
is natural (besides their smooth consequences) to take all t heir total derivatives,
this can be done in a coordinate free way via a construction kn own as prolongation
that we now describe. Let E0⊆Jk(P,n ) be a PDE, and let q = 0, 1,..., ∞.
VINOGRADOV’S COHOMOLOGICAL GEOMETRY OF PDES 9
Definition 1.10. The q-prolongation of E0 is the subset Eq⊆ Jk+q(P,n ) of
the (k +q)-jet space deﬁned by
(1.6) Eq :=Jq(E0,n )∩Jk+q(P,n ).
The∞-prolongation will be often denoted simply E .
Deﬁnition 1.10 requires some little explanations. As E0 is a submanifold in
Jk(P,n ), its jet space Jq(E0,n ) is a submanifold in the jet space Jq(Jk(P,n ),n )
as in Remark 1.4. The jet space Jk+q(P,n ) can be seen as a submanifold in
Jq(Jk(P,n ),n ) as well via the embedding in Remark 1.5. This explains the in-
tersection in (1.6). We stress that we will always understan d the prolongation Eq
as a subset in Jk+q(P,n ). If E0 is locally given by (1.5), then its q-prolongation is
locally given by
Eq :DJFa(x,...,u I,... ) = 0, |J|≤ q.
This shows that Eq encodes in a coordinate free way the total derivatives of E0 up
to order q, as desired.
Remark 1.11. For a generic E0⊆ Jk(P,n ) its q-th prolongation Eq is not a
submanifold in Jk+h(P,n ). When it is a submanifold, then it is clearly a PDE with
the same solutions as E0. In the following, we will always assume that the ∞-th
prolongation E = E∞ is a submanifold in J ∞(P,n ). This happens, e.g., when E0 is a
formally integrable PDE . Our assumptions are not a great loss of generality accord-
ing to Cartan-Kuranishi Prolongation Theorem which roughly states that, under
mild regularity conditions, every PDE becomes formally int egrable after ﬁnitely
many 1-prolongations.
Now on we concentrate on the ∞-prolongation E⊆J ∞(P,n ).
Proposition 1.12. Let E0⊆Jk(P,n ) be a PDE. Assume that its∞-prolongation
E⊆J ∞(P,n ) is a submanifold. Then the Cartan distribution restricts to E in the
sense that
Cz⊆TzE for all z∈ E.
Hence the restriction C : E → J 1(E,n ) is a well-deﬁned rank n involutive dis-
tribution on E . Additionally it detects solutions of E0 in the following sense: a
submanifoldS⊆ E is locally of the form S =N ∞ for some solution N of E0 if and
only if it is an n-dimensional integral submanifold of C .
The restriction of the Cartan distribution to the ∞-prolongation of a PDE will
be denoted by C as well and called the Cartan distribution .
Definition 1.13. A diﬃety (from the words diﬀerential equation and variety)
is a pair (E, C ) where E is the∞-prolongation of some PDE and C is the Cartan
distribution on E .
Proposition 1.12 now shows that a diﬃety (E, C ) contains most of the relevant
information about the PDE E0 deﬁning it.
We conclude this section brieﬂy discussing inﬁnitesimal symmetries of a PDE.
Let (E, C ) be the diﬃety corresponding to a PDE E0.
Definition 1.14. An inﬁnitesimal symmetry of E0 is a vector ﬁeld Y ∈ X(E )
such that [Y, Γ( C )]⊆ Γ( C ). A non-trivial inﬁnitesimal symmetry is an inﬁnitesimal
symmetry modulo trivial ones , i.e. sections of C .
10 F ABRIZIO PUGLIESE, GIOV ANNI SPARANO, AND LUCA VITAGLIAN O
Remark 1.15. The terminology “trivial, non-trivial symmetries” in Deﬁn ition
1.14 is motivated by the following facts. Let X be a section of the Cartan dis-
tribution on J ∞(P,n ) and let (E, C ) be any diﬃety, then X is tangent to E and
X|E is an inﬁnitesimal symmetry of E0. In other words, sections of the Cartan
distribution are inﬁnitesimal symmetries of all PDEs (regardless what is the PDE
we are considering).
There is an eﬃcient description of (non-trivial) inﬁnitesi mal symmetries in
local coordinates. Consider the vector bundle V → J ∞(P,n ) from the previous
subsection. Its sections are sometimes called generating sections of symmetries for
the following reasons. Take the restriction VE→ E of V to E . Sections of VE are
locally spanned by the restrictions vα|E , α = 1,...,m . Take a section χ∈ Γ(VE )
and let it be locally given by χ = χαvα|E for some local functions χα∈ C∞(E ).
Moreover, let ˜χ∈ Γ(V ) be an extension of χ, i.e. χ = ˜χ|E . Finally, let Y ∈ XC
be any inﬁnitesimal symmetry of the Cartan distribution on J ∞(P,n ) mapping to
˜χ under the projection XC → Γ(V ) (if we are working locally, we can take, e.g.,
the evolutionary vector ﬁeld З ˜χ). If E0 is locally given by (1.5), one can show that
Y is tangent to E if and only if locally χ is a solution of the following universal
linearization of E0:
ℓE (χ) = 0
where
ℓE : Γ(VE )→C∞(J ∞(P,n ))r, r = codim E0 = number of PDEs
is the locally deﬁned operator given by
ℓE (χ) =
(
ℓE (χ)1,...,ℓ E (χ)r
)
, ℓ E (χ)a := (З ˜χFa)|E = ∂Fa
∂uα
I
|EDI|Eχα.
and we used that all the total derivatives are tangent to E (a more intrinsic and
global interpretation of the universal linearization can b e provided for PDEs im-
posed on sections of a ﬁbration, particularly when E0 is speciﬁed as the zero locus of
a nonlinear diﬀerential operator , see e.g. [ 2, Chapter 4, Section 2.7] or [ 11, Section
3.9]) . In this case, the restriction Y|E is a inﬁnitesimal symmetry of E0
Proposition 1.16. The assignment χ↦→Y|E mod Γ( C ) establishes a bijection
between solutions of the universal linearization
ℓE (χ) = 0
of E0 and inﬁnitesimal symmetries of E0.
Remark 1.17. The universal linearization is a linear PDE imposed on secti ons
of the vector bundle VE→ E . As it only involves total derivatives, for any solution
N of E0, it can be pulled-back along the embedding j∞ :N→ E of Remark 1.3. If
we do so we get a new linear PDE for sections of the pull-back bu ndlej∞∗V . The
latter PDE is just the linearization of E0 around the solution N . This explain the
terminology “universal linearization”.

---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-585-663-in-elk98-table-2-one-ﬁnds-a-table-of-rationa
section_title: "In [ Elk98, Table 2], one ﬁnds a table of rational CM points z (ratio-"
section_number: 6.6.3
pages: 209-215
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki) — 606 sections: Analytic continuation"
---
nal points which correspond to abelian surfaces with comple x multiplication
by an order in M2(Q(
√
−d)) for some fundamental discriminant −d); with
the notation of loc. cit., they are given by z =B/(B−A) =±B/|C|. Some
of them are:
z d =−disc
−33/2272 d = 22.3.7
−53/37 d = 23.5
210/74 d = 3.17
−210/37 d = 19.
Notice that for the ﬁrst value of z, F ( 1
24, 7
24, 5
6 ;−33
2272 )3 converges. More-
over, since ( 22.7
3 ) = +1, it follows from I.4.6.4, I.5.3.9, that the triadic “pe ri-
ods” attached to the abelian surface A−33/2272 with complex multiplication
byM2(Q[
√
−d]) parametrized by z = 1, is algebraic (like the periods of A0).
By 5.6.3, it follows that the triadic number F ( 1
24, 7
24, 5
6 ;−33
2272 )3 is algebraic
(can one compute this algebraic number?).
On the other hand since Q(
√
−d)⁄= Q(√−3) in that case ( d = 2 2.3.7),
the real number F ( 1
24, 7
24, 5
6 ;−33
2272 ) is transcendental; this follows from Wol-
fart’s theorem [ W ol88] (whose proof has been recently completed by work
of Cohen-W¨ ustholz [CW01] and Edixhoven-Yafaev).
It can be proved, a contrario, that if the complex evaluation F ( 1
24, 7
24, 5
6 ;ξ)
is algebraic for some algebraic value ξ in the disc of convergence, then any p-
adic evaluation F ( 1
24, 7
24, 5
6 ;ξ)p which makes sense is also algebraic: indeed,
by [W ol88], [ CW01], such a ξ parametrizes a CM abelian surface by some
order in M2(Q[√−3]), and one concludes again using p-adic Betti lattices
as in I.5.3.
This is actually a very special case of a general, but conject ural, “prin-
ciple of global relations” for special values of solutions o f Gauss-Manin con-
nections, cf. [And95].
206 . p-ADIC ORBIFOLDS AND MONODROMY.
APPENDIX A
Rapid Course in p-adic Analysis.
By F. Kato
1. Introduction.
In this appendix, K always denotes a complete ﬁeld with respect to a
non-archimedean valuation|·| : K→ R≥0. The norm |·| is almost always
assumed to be non-trivial, unless otherwise stated.
Let us assume for a while that K is algebraically closed. We view the
ﬁeld K as an aﬃne space, as we do in complex analysis; K is a metrized
space with the metric induced from the valuation |·| . We can then follow
the lines of classical complex analysis and deﬁne convergen ce of power series,
Taylor and Laurent expansions, etc...
For instance let us deﬁne “holomorphic” functions to be K-valued func-
tions which are locally expressed by convergent power serie s(1) (cf. [Gou97,
Chap. 4]). This approach drives us however to several proble ms, which come
mainly from the fact that K with the metric topology is totally disconnected;
for example:
(i) for an open set U⊆K the ring of all such holomorphic functions on
U is huge. So is already the subring of all locally constant fun ctions.
(ii) It can be shown that the sheaf of germs of such functions s atisﬁes the
principle of unique continuation; but not in a satisfactory way. In
particular, Lemma 1.1.2 of Chapter I holds but is of no use, be cause
there is no non-empty connected open subset.
The trouble becomes more apparent when we think the local repre-
sentability by convergent power series in terms of coverings. In the complex
analytic situation, when we speak of the holomorphy of a func tionf deﬁned
over a connected open set U , we tacitly take a open covering {Ui}i∈I of U
consisting of suﬃciently small open neighborhoods such tha tf restricted on
each member Ui can be seen as evaluation of a power series convergent in
Ui. The point is that, since U is connected, members of {Ui} must have
overlaps so that the local properties can be transmitted to w hole U . But,
in the non-archimedean situation, such coverings may be reﬁ ned in such a
way that there are no overlap. This is why the analytic contin uation does
(1)The reader may wonder whether there is another approach by me ans of Cauchy-
Riemann type diﬀerential equations. This is unlikely becau se the diﬀerential calculus does
not go well, see [ Gou97, Chap. 4].
207
208 A. RAPID COURSE IN p-ADIC ANALYSIS.
not work well. So, for the sake of a reasonable analytic theor y, we have to
“limit” coverings so that we cannot take arbitrarily ﬁne reﬁ nements.
A ﬁrst method is due to Krasner. He introduced the so-called quasi-
connected sets and, on such subsets, deﬁned analytic functions as uniform
convergent limits of rational functions.
A more modern and systematic treatment was introduced by Tat e, with
the so-called Rigid Analysis . Let us brieﬂy view the main idea: we ﬁrst set
K{t1,... ,t n}
=
{ ∑
ν1,... ,νn≥0
aν1,... ,νntν1
1 ··· tνn
n ∈K[[t1,... ,t n]]
⏐
⏐
⏐
⏐
⏐
aν1,... ,νn→ 0 for
ν1 +··· +νn→∞
}
,
which is now called the Tate algebra overK. This is the ring of all functions
expressed by power series convergent on the closed disk D(0, 1+) = {z∈
K n|| zi|≤ 1}. The algebra K{t1,... ,t n} is endowed with the sup-norm
‖·‖, also called the Gauss norm . We list up some known properties (cf.
[BGR84, 5.2], [ FvdP81, II.3]):
(i) The ring K{t1,... ,t n} satisﬁes the Weierstrass Preparation Theo-
rem.
(ii) The ring K{t1,... ,t n} is Noetherian and factorial.
(iii) Every ideal of K{t1,... ,t n} is closed.
(iv) For any maximal ideal m ofK{t1,... ,t n}, the ﬁeld K{t1,... ,t n}/m
is a ﬁnite extension of K.
If, moreover, K is algebraically closed, the set of all maximal ideals, en-
dowed with the natural topology, coincides with D(0, 1+). So the situation is
analogous to classical algebraic geometry; D(0, 1+) to the aﬃne n-space, and
K{t1,... ,t n} to the coordinate ring. In fact, quotients A =K{t1,... ,t n}/I
by ideals I (called aﬃnoid algebras ), and their associated maximal spectra,
Spm(A), called aﬃnoids , forms the fundamental patches from which the
non-archimedean function theory will be developed. Althou gh the natural
metric topology on Spm( A) is terrible for the same reason as above, the
situation becomes much better as far as we deal only with thos e functions
coming from A. The trick is that, if the algebra A is integral, then we can
pretend that the space Spm( A) is “connected”; for example, the closed disk
D(0, 1+) is “connected” in this sense. So, basically according to th is point
of view, we can globalize the situation by gluing aﬃnoid patc hes to obtain
a reasonable theory of analytic functions. The actual recip e to do it is fur-
nished by the notion of Grothendieck topology, which censor s the plethora
of coverings. We will see this a little more precisely in what follows.
Remark 1.1. Although the rigid analysis seems to provide the reasonable
topological and analytical framework, one must not expect i t to be as nice
as the complex case. Firstly, in classical complex analysis , when we expand
a holomorphic function centered at a point inside its region of convergence,
the resulting Taylor expansion may have a diﬀerent region of convergence
2. RIGID ANALYTIC SPACES. 209
than the original one. This is a important method of analytic continuation.
But in the non-archimedean case, this never happens (cf. [ Gou97, 4.4]).
Secondly, the topological framework given as above is still not powerful
enough to handle paths. So it is hopeless to treat, for exampl e, fundamental
groups and monodromy in an intuitive way as in the classical c omplex case.
This diﬃculty is, in fact, remedied by Berkovich’ theory whi ch we shall see
later on.
2. Rigid analytic spaces.
Let K be as in the previous section; we do not assume in general that
K is algebraically closed.
As mentioned above, an aﬃnoid algebra A overK is a quotientK{t1,... ,t n}/I
for somen by an ideal I. Since I is closed, A has a norm|·| induced from the
sup-norm‖·‖of K{t1,... ,t n} (“residue norm” ). With the residue norm,
A is a Banach K-algebra. The norm |·| itself depends on the presentation
α : K{t1,... ,t n}/I ∼→ A, while the induced topology does not. So, strictly
speaking, we should write it like |·| α. Clearly, A is Noetherian and, for any
maximal ideal m of A, the residue ﬁeld A/m is a ﬁnite extension of K, and
hence, the valuation |·| of K naturally extends to that of it, denoted again
by|·| .
The associated aﬃnoid Spm(A) is the set of all maximal ideals of A. For
x∈ Spm(A) and f∈ A the value of f atx, denoted by f (x), is the class of f
in A/x. The set Spm( A) has the topology generated by the subsets of form
{x∈ Spm(A)|| f (x)|≤ 1} for f∈ A. But, as we pointed out above, this
topology is not very interesting since it makes Spm( A) totally disconnected.
So we should specify the reasonable family of “admissible” o pen sets (and
coverings), on which the function theory will be built.
Let A be an aﬃnoid algebra over K, and fi (i = 0,... ,n ) a collection
of elements in A which have no common zeros on Spm( A). The subspace
R ={x∈ Spm(A)||fi(x)|≤| f0(x)|, i = 1,... ,n}
can be identiﬁed with the aﬃnoid Spm( AR), where
AR = Aˆ⊗KK{t1,... ,t n}/(f1−t1f0,... ,f n−tnf0).
A subset of this form is called a rational subdomain. The identiﬁcation comes
as follows: We ﬁrst note that the morphism of aﬃnoids Spm( AR)→ Spm(A)
induced by A→ AR maps Spm(AR) toR. Then AR is the unique solution of
the following universal property (hence, it can be determin ed up to canonical
isomorphism): for any morphism of aﬃnoids φ : Spm( B)→ Spm(A) such
thatφ(Spm(B))⊂R, there exists a unique K-homomorphism AR→ B such
that the resulting diagram
210 A. RAPID COURSE IN p-ADIC ANALYSIS.
Spm(B) ✲φ
Spm(A)
Spm(AR)
♣♣♣♣♣♣❯ ✁
✁ ✕
is commutative.
Lemma 2.1. (1) If R and S are rational subdomains in Spm( A), then so is
R∩S.
(2) If R1 is a rational subdomain in Spm( A), and R2 is a rational sub-
domain in R1, then R2 is a rational subdomain in Spm( A).
Proof. (1) If R ={|fi(x)|≤| f0(x)|, i = 1,... ,n} and S ={|gj (x)|≤
|g0(x)|, j = 1,... ,m}, then one sees easily that R∩S ={|fi(x)gj (x)|≤
|f0(x)g0(x)|, i = 1,... ,n, j = 1,... ,m}.
(2) Exercise.
Corollary 2.2. Any subspace of the form
{|fi(x)|≤ 1,|gj (x)|≥ 1, i = 1,... ,n, j = 1,... ,m}
is a rational subdomain.
Proof. It is the intersection of rational subdomains {|fi(x)|≤ 1} for i =
1,... ,n and{1≤|gj(x)|} for j = 1,... ,m .
Example 2.3 (Rational subdomains of the unit polydisk) . Let us assume
thatK is algebraically closed. We consider rational subdomains o f the unit
polydisk D(0, 1+) = Spm(K{t1,... ,t n}).
(1) Closed polydisk: D(0,|π|+) ={x∈K n||xi|≤| πi|, i= 1,... ,n}, for
0⁄= πi∈ K,|πi|≤ 1, is a rational subdomain. The corresponding aﬃnoid
algebra is
K
{ t1
π1
,... , tn
πn
}
.
(2) Annulus: C(0,|π(1)|+,|π(2)|+) ={x∈K n|| π(1)
i |≤| xi|≤| π(2)
i |, i =
1,... ,n}, for 0 ⁄= π(j)
i ∈ K, |π(j)
i | ≤1, is a rational subdomain. The
corresponding aﬃnoid algebra is
K
{
π(1)
1
t1
,... , π(1)
n
tn
, t1
π(2)
1
,... , tn
π(2)
n
}
.
Let us next review the deﬁnition of Grothendieck topology (i n a narrow
sense). Let X be a topological space. A Grothendieck topology (G-topology,
in short) on X is a pair ( T, Cov) consisting of
• a collection T of open subsets in X,
• an assignment U↦→Cov(U ) for any U∈ T, where Cov(U ) is a collec-
tion of coverings by elements in T,

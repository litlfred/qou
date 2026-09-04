---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-026-polynomial-amoebas
section_title: "Polynomial amoebas"
section_number: null
pages: 159-165
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
doc_brief: "Analytic Combinatorics in Several Variables — 85 sections: Preface to the second edition; List of Symbols; Introduction"
---
sentation
f (w) =
( 1
2πi
)d ∑
η∈{a,b}d
sgn(η)
∫
Tη
f (z)
(z1− w1)··· (zd− wd)dz (6.2)
for allw∈ Relog−1(B′), where Tη = Relog−1(r) with rk = ak if ηk = a and
rk = bk ifηk = b. Since ak <|wk|< bk for all k, we have the series expansions
1
zk− wk
=

−
∑
n<0
zn
kw−n−1
k if|zk| =|ak|
∑
n≥0
z−n−1
k wn
k if|zk| =|bk|
.
In particular, each summand in (6.2) is a distinct Laurent series inw uniformly
converging on compact subsets and, taking the sgn(η) coeﬃcient into account,
we obtain the desired representation
f (w) =
∑
r∈Zd
( 1
(2πi)d
∫
Te(x)
f (z)z−r−1
)
wr
forw∈ B′. By independence of the Cauchy integral on the point x in B, this
holds for allx∈ B. □
Example 6.10. For d = 1, we obtain the classical representation
f (w) = 1
2πi
∫
γ2
f (z)
z− w dz
|               {z               }
f2(w)
− 1
2πi
∫
γ1
f (z)
z− w dz
|               {z               }
f1(w)
,
whereγ1 andγ2 are the inner and outer boundaries of an annulus A ={z : ea≤
|z|≤ eb}, the point w∈ A, and the analytic function f is represented by the
convergent series∑
n∈Z anzn on A. The function f2(w) is analytic on the disk of
radius eb while the function f1(1/w) is analytic on the disk of radius e−a, so
f2(w) = ∑
n≥0 anwn while f1(w) =−∑
n≤−1 anwn. ◁
6.2 Polynomial amoebas
If f (z) is a Laurent polynomial then the algebraic hypersurface or algebraic
variety deﬁned by f is the zero setV( f ) ={z∈Cd
∗ : f (z) = 0}. The amoeba
of f is the set
amoeba( f ) :=
{
Relogz :z∈Cd
∗ and f (z) = 0
}
⊂Rd
consisting of the image under Relog of the non-zero points in the algebraic
hypersurface deﬁned by f .
142 Laurent series, amoebas, and convex geometry
Amoebas provide a crucial tool for the study of convergent Laurent expan-
sions because they live in real space (which is much easier to picture than
complex space) and, as we will see in Theorem 6.18 below, the connected
components of amoeba( f )c = Rd\ amoeba( f ) are convex sets corresponding
to the convergent Laurent expansions of 1/ f (z).
Example 6.11. The amoebas of f (x, y) = 2− x−y and f (x, y) = (3−2x−y)(3−
x− 2y) are shown in Figure 6.1; note that the amoeba of a product is the union
of amoebas. Algorithms for drawing amoebas are discussed in Chapter 8. ◁
Figure 6.1 Left: amoeba(2− x−y) with the components of its complement.Right:
amoeba((3− 2x− y)(3− x− 2y)).
Exercise 6.2. Identify the convergent Laurent expansions corresponding to the
connected components B1, B2, and B3 of amoeba(2− x− y) shown on the left
side of Figure 6.1.
Exercise 6.3. Use the deﬁnition of an amoeba to transform the sketch of
amoeba(2− x− y) in Figure 6.1 into a sketch of amoeba(2− x− y2).
In order to study the connected components of amoeba( f )c, we introduce
some terminology.
Deﬁnition 6.12 (Newton polytopes). The convex hull hull(A) of a subset
A⊂ Rd is the smallest convex set in Rd containing A. The convex hull of A
equals the convex hull of its extreme points : those points x ∈ A which do
not lie in the interior of any line segment contained in A. A polytope P is the
convex hull of any ﬁnite set E⊂ Rd and the vertices of a polytope P are the
extreme points of hull(E). If f (z) is a Laurent polynomial then the support
of the Laurent polynomial f is the (ﬁnite) set of exponents of the monomials
6.2 Polynomial amoebas 143
appearing in f , and the Newton polytope N f of f is the convex hull of its
support,
N f := hull
{
r∈Zd : arzr is a non-zero monomial of f
}
.
We now ﬁx a Laurent polynomial f (z) = ∑
i aizi. The order map ν :
amoeba( f )c → Rd sends a point x ∈ amoeba( f )c to the vector ν(x) with
kth coordinate
ν(x)k = 1
2πi
∫
|zk|=exk
fzk(ex1,..., zk,..., exd)
f (ex1,..., zk,..., exd) dzk,
where (ex1,..., zk,..., exd) denotes the vectorz with z j = ex j for j, k.
Remark 6.13. Recall that if g is any univariate meromorphic function inside
and on a contour γ, with no zeros or poles on γ, then the classical argument
principle from complex analysis states that (counting with multiplicity) the
number of zeros of g insideγ minus the number of poles of g insideγ equals
1
2πi
∫
γ
g′(z)
g(z) dz.
In particular, 1
2πi
∫
γ
g′(z)
g(z) dz is an integer so the order map sends amoeba( f )c to
Zd.
Exercise 6.4. Use Cauchy’s residue theorem to prove the argument principle.
Exercise 6.5. Prove that for anyx∈ amoeba( f )c,
ν(x)k = 1
(2πi)d
∫
Relog−1(x)
zk fzk(z)
f (z)
dz
z1··· zd
.
Note that the order map is continuous, and hence constant on the connected
components of amoeba( f )c, so the order of a component of amoeba( f )c is
well deﬁned. The order map was introduced by Forsberg et al. [FPT00] as
a multivariate generalization of the argument principle. Our treatment of the
order map closely follows the arguments given in [FPT00].
Lemma 6.14. Ifx∈ amoeba( f )c ands∈ Zd\{ 0} thens·ν(x) equals the
number of zeros of as(w) = f (p1ws1,..., pdwsd) inside the unit circle|w| = 1
minus the order of the pole of as(w) at the origin, where p∈ Cd
∗ is any point
withx = Relog(p).
144 Laurent series, amoebas, and convex geometry
Proof The argument principle implies that the number of zeros of as(w) in-
side the unit circle minus the order of the pole of as(w) at the origin equals
1
2πi
∫
|w|=1
d
dw as(w)
as(w) dw.
By Exercise 6.16 below, the image of |w| = 1 under the change of variables
z = (p1ws1,..., pdwsd) is homotopic to the chain of integrations1γ1+··· +sdγd,
whereγk ={(p1,..., w,..., pd) :|w| =|pk|}. Thus, the diﬀerence of zeros and
poles is
d∑
k=1
sk
2πi
∫
γk
d
dw as(w)
as(w) dw =
d∑
k=1
sk
2πi
∫
|zk|=|pk|
fzk(p1,..., zk,..., pd)
f (p1,..., zk,..., pd) dzk
=
d∑
k=1
sk
2πi
∫
|zk|=exk
fzk(ex1,..., zk,..., exd)
f (ex1,..., zk,..., exd) dzk
=
d∑
k=1
skν(x)k
as claimed, where the ﬁrst equality follows from the chain rule, and the second
follows from the expression for the order map in Exercise 6.5. □
Lemma 6.14 is powerful as it allows us to characterize the order map using
the roots of a univariate polynomial; it forms the basis for all of the results
about the order map that we require.
Corollary 6.15. The image of amoeba( f )c under the order map lies in the
Newton polytope of f .
Exercise 6.6. Prove Corollary 6.15 by showing thats·ν(x)≤ max
n∈N f
(s·n) for
alls∈Zd\{ 0}.
Corollary 6.16. Ifx andx′ lie in distinct components of amoeba( f )c then
ν(x),ν(x′).
Proof Writingx′ =x + ts for somes∈Zd\{ 0} and t> 0, we have
s·ν(x′)
= # zeros of f (ex1+ts1ws1,..., exd+tsdwsd) inside|w| = 1 minus pole order at 0
= # zeros of f (ex1ws1,..., exdwsd) inside|w| = et minus pole order at 0
> # zeros of f (ex1ws1,..., exdwsd) inside|w| = 1 minus pole order at 0
=s·ν(x′),
where the inequality follows from the fact that there is at least one root of
6.2 Polynomial amoebas 145
f (ex1ws1,..., exdwsd) with 1 <|w| < et sincex andx′ lie in diﬀerent compo-
nents of amoeba( f )c. Thusν(x′),ν(x). □
Corollaries 6.15 and 6.16 imply that we can uniquely identify the Laurent
expansions of 1/ f (z) with integer points in the Newton polytope of f .
Figure 6.2 Left: The Newton polytope of (3 − 2x− y)(3− x− 2y) = 9− 9x−
9y + 2x2 + 5xy + 2y2. Right: Drawing of amoeba((3− 2x− y)(3− x− 2y)), whose
complement contains a connected component for each integer point of the Newton
polytope.
It is of great interest to know which elements ofN f∩Zd correspond to Lau-
rent expansions of 1/ f (z). In general this is a very diﬃcult question, however
in one important case we can be deﬁnitive.
Corollary 6.17. Ifv∈N f∩Zd and there existsx∈ amoeba( f )c such that
|avzv|>
⏐⏐⏐⏐ f (z)− avzv
⏐⏐⏐⏐
wheneverz∈ Te(x) then the Laurent series
1
f (z) = 1
avzv
∑
k≥0
(avzv− f (z)
avzv
)k
(6.3)
has domain of convergence Relog−1(B) for the component B ⊂ amoeba( f )c
with orderv. In particular, the vertices of N f are contained in the image of
amoeba( f )c under the order map.
Proof The Laurent series (6.3) converges in a neighborhood ofTe(x) as a ge-
ometric series with ratio less than one, meaning it has domain of convergence
Relog−1(B) for the component B⊂ amoeba( f )c containingx. Ifs is any vector
146 Laurent series, amoebas, and convex geometry
Figure 6.3 Sketch of amoeba(1− 4xy + x3 + y3).
inZd\{ 0}, then Rouch´e’s Theorem implies
s·ν(x) = # zeros− # poles of f (p1ws1,..., pdwsd) inside|w| = 1
= # zeros− # poles of avpvws·v inside|w| = 1
=s·v.
Since this holds for alls∈Zd\{ 0}, we see thatν(x) =v.
Ifv is a vertex ofN f then there existsr∈Rd such thatv·r >w·r for all
w,v in the support of f . Whenp = etr for t> 0 the term|avpv| =|av|et(v·r)
grows exponentially faster, as t→∞ , than|awpw| =|aw|et(w·r) for allw ,v
in the support of f . In particular, when t is suﬃciently large then p = etr
satisﬁes|avzv|>
⏐⏐⏐⏐ f (z)− avzv
⏐⏐⏐⏐ for allz∈ T(p). □
Summarizing our results, we have shown the following.
Theorem 6.18. The connected components of amoeba( f )c are convex subsets
of Rd in one-to-one correspondence with the convergent Laurent expansions
of 1/ f (z). The order map sends each component of amoeba( f )c to a diﬀerent
element ofN f∩Zd and every vertex ofN f lies in the image of amoeba( f )c.
Exercise 6.7. Figure 6.3 displays amoeba(1−4xy+x3+y3). Use Corollary 6.17
to prove algebraically that the amoeba complement contains a bounded com-
ponent and ﬁnd its order. Prove that for N≥ 0 the coeﬃcient of xNyN in the
Laurent expansion of F(x, y) = 1/(1− 4xy + x3 + y3) corresponding to the

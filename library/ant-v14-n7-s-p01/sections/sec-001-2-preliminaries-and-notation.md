---
doc_id: ant-v14-n7-s-p01
doc_title: "p-adic Asai L-functions of Bianchi modular forms David Loeﬄerand Chris Williams The Asai (or twisted tensor) L-function of a Bianchi modular form9 is the L-function attached to the"
section_id: sec-001-2-preliminaries-and-notation
section_title: "Preliminaries and notation"
section_number: 2
pages: 4-14
source_pdf: ant-v14-n7-s-p01.pdf
source_sha256: 976199bfca4ac086
doc_brief: "p-adic Asai L-functions of Bianchi modular forms David Loefflerand Chris Williams The Asai (or twisted tensor) L-function of a Bianchi modular form9 is the L-function attached to the tensor induction"
---
2A. Basic notation. We ﬁx notation for a general number ﬁeld K, which will either be Q or an imaginary
quadratic ﬁeld. (We’ll generally denote this imaginary quadratic ﬁeld by F to distinguish it from the
p-adic Asai L-functions of Bianchi modular forms 1673
rationals in the notation). Denote the ring of integers by OK , the adele ring by AK and the ﬁnite adeles
by A f
K . We let ˆOK:=ˆZ⊗Z OK be the ﬁnite integral adeles, and K×+ the totally positive elements of K×
(so that K×+= K× for K= F).
Let H:={ z∈ C: Im(z)> 0} be the usual upper half-plane, with GL2(R)+ (the group of 2× 2 matrices
of positive determinant) acting by Möbius transformations in the usual way; we extend this to all of
GL2(R) by letting
(−1
1
)
act via x+ iy↦→− x+ iy .
Deﬁne the upper half-space to be
H3:={(z, t)∈ C× R>0},
with GL2(C) acting via
( a
c
b
d
)
·(z, t)=
((az+ b)(cz+ d)+ a¯ct 2
|cz+ d|2+| c|2t2 , |ad− bc|t
|cz+ d|2+| c|2t2
)
.
We embed H in H3 via x+ iy↦→(x, y), which is compatible with the actions of GL 2(R) on both sides.
Throughout, p will denote a rational prime. Let F be an imaginary quadratic ﬁeld of discriminant−D,
with different D=(√−D), and ﬁx a choice of√−D in C. Let n⊂ OF be an ideal of F, divisible by
all the primes of F above p; this will be the level of our Bianchi modular form. We assume throughout
that n is small enough to ensure that the relevant locally symmetric space attached to n is smooth (see
Proposition 2.5). Let N be the natural number with (N)= Z∩ n as ideals in Z (noting that p| N).
For an integer n> 0 and a ring R, deﬁne V(r)
n (R) to be the space of homogeneous polynomials of
degree n in two variables X, Y with coefﬁcients in R, with GL2(R) acting on the right via( f|γ)( X, Y)=
f(a X+ bY, cX+ dY). Similarly, we write V(𝓁)
n (R) for the same space with GL2 acting on the left, so
(γ· f)(X, Y)= f(a X+ cY, bX+ dY).
2B. Locally symmetric spaces.
Deﬁnition 2.1. Let G be the algebraic group ResF/QGL2 over Q, and let G∗ be the subgroup G×D Gm,
where D:= ResF/QGm and the map G→ D is determinant.
(Compare [Lei et al. 2018, Deﬁnition 2.1.1] in the totally real case.)
Deﬁnition 2.2. We deﬁne locally symmetric spaces attached to the groups GL 2, G and G∗ as follows:
• If U⊂ GL2(A f
Q) is an open compact subgroup, we set
YQ(U):= GL2(Q)+\[GL2(A f
Q)× H]/U,
where GL2(Q)+ acts from the left on both factors in the usual way, and U acts on the right of
GL2(A f
Q).
• If U⊂ G(A f
Q)= GL2(A f
F) is open compact, we set
YF(U):= GL2(F)\[GL2(A f
F)× H3]/U.
1674 David Loeﬄer and Chris Williams
• If U⊂ G∗(A f
Q)=
{
g∈ GL2(A f
F): det(g)∈(A f
Q)×}
is open compact, we set
Y∗
F(U):= G∗(F)+\[G∗(A f
Q)× H3]/U,
where G∗(F)+={ g∈ G∗(F): det(g)> 0} is the intersection of G∗(F) with the identity component
of G∗(R).
Each of these spaces has ﬁnitely many connected components, each of which is the quotient of H or H3
by a discrete subgroup of PSL2(R) (resp. PGL2(C)). If U is sufﬁciently small, these discrete subgroups
act freely, so in particular the quotient is a manifold.
Deﬁnition 2.3. Let K be either Q or F, and m, n, a be ideals in OK . We deﬁne:
(i) UK(m, n):=
{
γ∈ GL2(ˆOK):γ≡ I mod
(m
n
m
n
)}
,
(ii) UK(m(a), n):=
{
γ∈ GL2(ˆOK):γ≡ I mod
(m
n
ma
n
)}
,
We write YK(m, n):= YK(U(m, n)) and similarly YK(m(a), n). We will be particularly interested
YK(m, n) for m=(1), which we abbreviate as YK,1(n).
In the case K= F, we write U∗
F(m, n), U∗
F(m(a), n), U∗
F,1(n) for the intersections of the above groups
with G∗.
Example 2.4. The following three locally symmetric spaces are of particular importance in the sequel,
so here we describe them explicitly (and record some of their other basic properties) for later reference.
(i) YQ,1(N) is the usual (open) modular curve of level 01(N). It has one connected component,
isomorphic to01(N)\H.
(ii) The space Y∗
F,1(n) also has a single connected component, isomorphic to 0∗
F,1(n)\H3, where
0∗
F,1(n):= G∗(F)+∩ U∗
F,1(n)=
{( a
c
b
d
)
∈ SL2(OF): c= 0, a= d= 1 mod n
}
.
(iii) Since det(UF,1(n))=ˆO×
F, the space YF,1(n) has h F connected components, where h F is the class
number of F. The identity component is isomorphic to 0F,1(n)\H3, where
0F,1(n):= GL2(F)∩ UF,1(n).
If N= n∩ Z, then there are natural maps
YQ,1(N) ι→ Y∗
F,1(n) → YF,1(n)
induced by the natural maps H↪→ H3 and GL2(A f
Q)↪→ G∗(A f
Q)↪→ G(A f
Q). The map ι is injective in
most cases:
Proposition 2.5. If n is divisible by some integer q> 4, then Y∗
F,1(n) is a smooth manifold, and
ι: YQ,1(N)↪→ Y∗
F,1(n)
is a closed immersion.
p-adic Asai L-functions of Bianchi modular forms 1675
Proof. First, the smoothness assertion. It sufﬁces to prove that 0∗
F,1(n) has no nontrivial torsion elements.
Since0∗
1(n) is a subgroup of SL2(OF), any torsion elementγ must have eigenvaluesζ,ζ−1 whereζ is a
(nontrivial) root of unity, deﬁned over an extension of F of degree at most 2. Since ζ+ζ−1= a+ d=
2 mod n, we conclude that n dividesζ+ζ−1− 2. A case-by-case check shows that this implies ζ has
order 2, 3, 4 or 6, and n must contain one of the integers 1, 2, 3.
Let us now prove the injectivity assertion. Let z, z′∈ H3 be such that γ z= z′, for some γ∈0∗
1(n).
Thenγ−1γ z= z, so eitherγ−1γ= id, orγ−1γ is a nontrivial torsion element in SL2(OF). Sinceγ is
upper-triangular modulo some integer q> 4, the same is true of γ and thus also ofγ−1γ ; but we have
just seen that0∗
F,1(q) has no torsion elements for q> 4.
We can therefore conclude that γ−1γ= id, in other words that γ∈0∗
F,1(n)∩ SL2(Z)=0Q,1(N).
Hence z= z′ as elements of YQ,1(N). □
Remark 2.6. Henceforth, we will always assume that n is divisible by such a q, or, more generally, is
small enough to avoid the possibility that these spaces are (nonsmooth) orbifolds.
In contrast, the composition ◦ι is never injective, since
(−1
0
0
1
)
∈01(n) preserves the image of H3 in
H, and acts on H by x+ iy↦→− x+ iy , so the points−x+ iy and x+ iy of YQ,1(N) (which are distinct
for generic x, y) are identiﬁed when mapped to YF,1(n). This failure of injectivity is a key reason for
introducing the space Y∗
F,1(n). In fact, one can see directly that:
Proposition 2.7. The map: Y∗
F,1(n)→ YF,1(n) has image equal to the identity component0F,1\H3. Its
ﬁbres are the orbits of the ﬁnite group
{(ϵ
0
0
1
)
:ϵ∈ O×
F
}
acting on0∗
F,1\H3.
2C. Hecke correspondences. We can deﬁne Hecke correspondences on the symmetric spaces YK,1(n),
for n an ideal of OK , as follows. Firstly, we have diamond operators⟨w⟩ for everyw∈(OK/n)×, which
deﬁne an action of (OK/n)× on YK,1(n); this even extends to an action of the narrow ray class group
modulo n, although we shall not use this.
Secondly, let a be a square-free ideal of OK . Consider the diagram
YK(1(a), n)
π2xx
π1
&&
YK,1(n) YK,1(n)
whereπ1 is the natural projection map, andπ2 is the “twisted” map given by the right-translation action of(ϖ
1
)
on GL2(A f
K), whereϖ∈ˆOK is any integral adèle which generates the ideal aˆOK . (If K= Q and
ϖ= a is the positive integer generatinga, then this mapπ2 corresponds to z↦→ z/a on H.) We then deﬁne
(Ta)∗:=(π2)∗◦(π1)∗,
(Ta)∗:=(π1)∗◦(π2)∗
as correspondences on YK,1(n). When a divides the level n, we denote these operators instead by (Ua)∗
and(Ua)∗. The deﬁnition may be extended to nonsquarefree a in the usual way.
1676 David Loeﬄer and Chris Williams
The same construction is valid for the more general symmetric spaces YK(m, n), but it is no longer
independent of the choice of generator ϖ of a (it depends on the class of ϖ modulo 1+ mˆOK ). We will
only use this in the case where a is generated by a positive integer a, in which case we of course take
ϖ= a. With this convention, the Hecke operators(Ta)∗ and(Ta)∗ for positive integers a also make sense
on the “hybrid” symmetric spaces Y∗
F,1(m, n).
Remark 2.8. The maps(Ta)∗ and(Ua)∗ are perhaps more familiar, as their action on automorphic forms
is given by simple formulae in terms of Fourier expansions, as we shall recall below. The lower-star
versions(Ta)∗ and(Ua)∗ are the transpose of the upper-star versions with respect to Poincaré duality; this
duality explains the key role played by (Up)∗ in our norm relation computations.
2D. Bianchi modular forms. We brieﬂy recall the deﬁnition of Bianchi modular forms; for further
details following our exact conventions, see [Williams 2017, §1; Ghate 1999] for a more general treatment.
As above, let F be an imaginary quadratic ﬁeld, and U an open compact subgroup of GL2(A f
F). Then,
for any k> 0, there is a ﬁnite-dimensional C-vector space Sk,k(U) of Bianchi cusp forms of weight(k, k)
and level U, which are functions
9: GL2(F)\GL2(AF)/U→ V(r)
2k+2(C)
transforming appropriately under right-translation by the group C×· SU2(C), and satisfying suitable
harmonicity and growth conditions.
These forms can be described by an appropriate analogue of q-expansions; see [Williams 2017, §1.2].
Let eF: AF/F→ C× denote the unique continuous character whose restriction to F⊗ R∼= C is
x∞↦−→e2πiTrF/Q(x∞),
and let W∞: C×→ V2k+2(C) be the real-analytic function deﬁned in [op. cit., 1.2.1(v)] (involving the
Bessel functions Kn).
Theorem 2.9. Let9 be a Bianchi modular form of weight(k, k) and level U. Then there is a Fourier–
Whittaker expansion
9
((y x
0 1
))
=| y|AF
∑
ζ∈F×
W f(ζ y f,9) W∞(ζ y∞)eF(ζ x),
where W f(−,9) , the “Kirillov function” of 9, is a locally constant function on (A f
F)×, with support
contained in a compact subset of A f
F.
If U= UF,1(n) for some n, then W f(−,9) is supported in D−1ˆOF. For m an ideal of OF, we deﬁne
a coefﬁcient c(m,9) as the value W f( y f,9) for any y f generating the fractional ideal D−1mˆOF; this is
independent of the choice of y f .
Exactly as for elliptic modular forms, the space Sk,k(UF,1(n)) has an action of (commuting) Hecke
operators(Tm)∗ for all ideals m; and if9 is an eigenvector for all these operators, normalised such that
p-adic Asai L-functions of Bianchi modular forms 1677
c(1,9)= 1, then the eigenvalue of the m-th Hecke operator on 9 is c(m,9) . Moreover, the space
Sk,k(UF,1(n)) is a direct sum of “new” and “old” parts, and the Hecke operators(Tm)∗ are simultaneously
diagonalisable on the new part.
2E. The Asai L-function. We now deﬁne the principal object of study in this paper, the Asai L-function
of a Bianchi eigenform.
The space Sk,k(UF,1(n)) has an action of diamond operators ⟨d⟩, for all d∈(OF/n)×; and on any
Hecke eigenform9 these act via a character ε9:(OF/n)×→ C×. Let ε9,Q denote the restriction of this
character to(Z/N Z)×.
Deﬁnition 2.10. Let 9 be a normalised eigenform in Sk,k(UF,1(n)), and χ a Dirichlet character of
conductor m. Deﬁne the Asai L-function of9 by
LAs(9,χ, s):= L(m N)(χ 2ε9,Q, 2s− 2k− 2)·
∑
n>1
(m,n)=1
c(nOF,9)χ( n)n−s,
where N= n∩ Z and L(m N)(−, s) is the Dirichlet L-function with its Euler factors at primes dividing
m N removed. Ifχ is trivial we write simply LAs(9, s).
This Dirichlet series is absolutely convergent for ℜ(s) sufﬁciently large, 1 and has meromorphic
continuation to all s∈ C. (This is proved in [Flicker 1988] or [Ghate 1999] for χ trivial, and the result
for generalχ can be proved similarly.) For s in the half-plane of convergence, it can be written as an
Euler product
LAs(9,χ, s)=
∏
𝓁 prime
LAs
𝓁 (9,χ, s),
where LAs
𝓁 (9,χ, s) depends only onχ(𝓁) and the Hecke and diamond eigenvalues of9 at the primes
above𝓁. If 𝓁| m then LAs
𝓁 (9,χ, s)= 1; if𝓁 ∤ m, then a case-by-case check shows that LAs
𝓁 (9,χ, s) has
the form P𝓁(9,𝓁−sχ(𝓁))−1, where P𝓁(9,−) is a polynomial of degree⩽ 4.
If9 is a new eigenform, and χ is trivial, then LAs(9,χ, s) coincides with the function denoted by
G(s, f) in [Ghate 1999].
Lemma 2.11. Suppose9 is a normalised eigenform of level n coprime to p, n′= n∏
p|p p, and9α
is a normalised eigenform of level n′ such that c(m,9α)= c(m,9) for all m coprime to p. Let α=
c(pOF,9α). Then we have
LAs(9α, s)=(1−αp−s)−1LAs,(p)(9, s),
and L As(9α,χ, s)= LAs(9,χ, s) for every nontrivialχ of p-power conductor. □
1Since the eigenvalues c(l,9) for l prime satisfy|c(l,9)|⩽ 2NF/Q(l)k/2+1 [Jacquet and Langlands 1970, §11], it sufﬁces
to takeℜ(s)> k+ 3. This bound is not optimal, but it sufﬁces for our purposes.
1678 David Loeﬄer and Chris Williams
2F. The primitive Asai L-function. The “imprimitive” Asai L-function of Deﬁnition 2.10 is closely
related to another L-function, the “primitive” Asai L-function. This is slightly more difﬁcult to deﬁne,
but in many ways more fundamental.
Automorphic construction: The Langlands L-group of G= ResF/Q GL2 is the semidirect product
LG=(GL2(C)×GL2(C))⋊Gal(Q/Q), with the Galois group acting on GL2×GL2 by permuting the fac-
tors via its quotient Gal(F/Q). There is a 4-dimensional representation of LG, the Asai representationr As,
whose restriction to GL2×GL2 is the tensor product map GL2×GL2→ GL4; see, e.g., [Flicker 1988, §0].
Remark 2.12. The representation r As of LG factors through the quotient LG∗, which explains the
prominent role the group G∗ plays in our constructions.
If5 is the automorphic representation of GL2(AF) generated by an eigenform9 as above, then for
each rational prime 𝓁, the local factors 5v for primes v|𝓁 of F determine (via the local Langlands
correspondence for GL2) a Weil–Deligne representation w5,𝓁 of Q𝓁 with values in LG. Moreover, a
Dirichlet characterχ modulo m determines uniquely a characterχA=∏
𝓁χ𝓁 of A×
Q/Q× such that for𝓁 ∤ m,
χ𝓁 is unramiﬁed and maps a uniformiser toχ(𝓁). We may interpretχ𝓁 also as a character of the Weil group
of Q𝓁, via the Artin reciprocity map (normalised to send uniformisers to geometric Frobenius elements).
Deﬁnition 2.13. We let LAs
𝓁 (5,χ, s) denote the local L-factor of the 4-dimensional Weil-Deligne rep-
resentation(r As◦w5,𝓁)⊗χ𝓁, where r As is the 4-dimensional tensor product representation of LG. We
deﬁne the primitive Asai L-function of5 by
LAs(5,χ, s)=
∏
𝓁 prime
LAs
𝓁 (5,χ, s).
Ifχ is trivial we write simply LAs
𝓁 (5, s) and LAs(5, s).
Remark 2.14. (i) Theorem 1.4 of [Ramakrishnan 2002] shows that LAs(5,χ, s) is an automorphic
L-function: more precisely, there exists an automorphic representation As(5) of GL4(AQ) such that
LAs(5,χ, s) coincides with the L-function of As(5)⊗χ, for every Dirichlet characterχ.
(ii) The L-factor LAs
𝓁 (5,χ, s) can also be deﬁned as the “lowest common denominator” of the values
of a local zeta-integral, as in [Flicker 1988]. This alternative deﬁnition is known to be equivalent to
Deﬁnition 2.13: if 𝓁 is split in F, this equivalence is one of the deﬁning properties of the local Langlands
correspondence (see condition (2) in the introduction of [Harris and Taylor 2001]); if𝓁 is inert or ramiﬁed
in F the equivalence is given by [Matringe 2010, Theorem 4.2].
Galois representations: This primitive L-function LAs(5,χ, s) can also be understood in terms of Galois
representations, as follows. As we shall see in the next section, for an eigenform 9 as above, the
coefﬁcients c(n,9) all lie in a number ﬁeld E⊂ C. If p is a prime of E, above some rational prime p,
there is a unique semisimple 2-dimensional Ep-linear representation Vp(5) of Gal(Q/F), unramiﬁed
outside np, on which geometric Frobenius at a prime l ∤ np of F has trace c(l,9) . Then we may form
p-adic Asai L-functions of Bianchi modular forms 1679
the tensor induction As Vp(5), which is a 4-dimensional representation of Gal(Q/Q), isomorphic as a
representation of Gal(Q/F) to the tensor product of Vp(5) and its Galois conjugate.
The local Euler factor at 𝓁 of this Galois representation is given by
L𝓁(As Vp(5)⊗χ, s):= det
(
1−𝓁−s Frob−1
𝓁 :(As Vp(5)⊗χ) I𝓁
)−1, (2-1)
where I𝓁 is the inertia group at𝓁, Frob𝓁 is an arithmetic Frobenius element, andp is any prime not dividing𝓁.
If Vp(5) satisﬁes local-global compatibility at the primes above𝓁 (which is expected, and known in many
cases by the results of [Mok 2014; Varma 2014]), then this local L-factor L𝓁(As Vp(5)⊗χ, s) coincides
with the automorphic local L-factor LAs
𝓁 (5,χ, s).
Relation to the imprimitive L-function: The imprimitive L-function LAs(9,χ, s) can be seen as an
“approximation” to the primitive L-function, in the following sense:
Proposition 2.15. We have
LAs(9,χ, s)= LAs(5,χ, s)
∏
𝓁|m N
C𝓁(9,χ, s),
where the local error termsC𝓁(9,χ, s) are polynomials in𝓁−s, of degree⩽ 4. In particular, the primitive
and imprimitive L-functions have the same local factors at all but ﬁnitely many primes.
Proof. The equality of the local factors for 𝓁 ∤ m N is Proposition 1 of [Ghate 1999]; so it remains to show
that if𝓁| m N, the ratio LAs
𝓁 (9,χ, s)/LAs
𝓁 (5,χ, s) is a polynomial in𝓁−s of degree⩽ 4.
If𝓁| m, then LAs
𝓁 (9,χ, s) is identically 1. The same holds if 5𝓁 is supercuspidal at some prime above
𝓁, since in this case c(nOF,9) is zero for every n divisible by𝓁. Since LAs
𝓁 (5,χ, s) is (by deﬁnition)
the reciprocal of a polynomial of degree⩽ 4, the result is automatic in these cases. This leaves the primes
𝓁 such that𝓁| N,𝓁 ∤ m, and the local factors of 5 at primes above𝓁 are principal series or special, which
can be veriﬁed in a case-by-case check. □
Perhaps surprisingly, the local error terms C𝓁(9,χ, s) at the primes𝓁| m N may be nontrivial, even if
χ= 1 and9 is the unique new eigenform generating5. In Galois-theoretic terms, this corresponds to
the fact that the inertia invariants of As Vp(5) at a prime𝓁 may be strictly larger than the tensor product
of the inertia invariants of Vp(5) at the primes above𝓁. However, there are some simple criteria that are
sufﬁcient to rule this out:
• If𝓁| m and𝓁 ∤ ND, then both LAs
𝓁 (9,χ, s) and LAs
𝓁 (5,χ, s) are identically 1, so in particular
C𝓁(9,χ, s)= 1.
• If𝓁 ∤ m,𝓁 is split in F, and only one of the two primes above 𝓁 divides n, then a direct computation
shows that C𝓁(9,χ, s)= 1 (compare [Kings et al. 2017, Remark 2.7.1] in the Rankin–Selberg case).
2G. The Coates–Perrin-Riou conjecture. In [Coates and Perrin-Riou 1989; Coates 1989], a general
conjecture is formulated predicting the existence of p-adic L-functions associated to any motive over Q
1680 David Loeﬄer and Chris Williams
whose L-function has at least one critical value. In this section, we shall explain what this conjecture
predicts for the (conjectural) Asai motive associated to a Bianchi eigenform.
Let us ﬁx an automorphic representation 5 of GL2(AF), generated by some Bianchi eigenform 9
of weight(k, k) with coefﬁcients in a number ﬁeld E. We shall assume (in this section only) that there
exists a Chow motive MAs(5) over Q, with coefﬁcients in E, whose L-function is LAs(5, s), and whose
p-adic realisation is As Vp(5), for every prime p of E. (Strictly speaking the conjectures are formulated
only for motives with coefﬁcients in Q, but the extension to general E is immediate.)
We shall apply the conjectures of [Coates 1989] to the motive M= MAs(5)(1). Note that M
has weight 2k, and its Hodge decomposition at ∞ is given by dim M(−1,2k+1)= dim M(2k+1,−1)= 1,
dim M(k,k)= 2. Moreover, complex conjugation acts as−1 on M(k,k), so d+(M)= 1 and d−(M)= 3.
Thus s= 0 is a critical value of L(M( j)(χ), s)= LAs(5,χ−1, s+ j), for integers 0⩽ j⩽ k and Dirichlet
charactersχ such that(−1) jχ(−1)= 1.2 We choose our square root of−1 (theρ of [op. cit.]) to be+i.
We shall also assume that p is unramiﬁed in F and5 has conductor coprime to p, and is ordinary at
the primes above p, so there is a unique eigenvalue α of Frob−1
p on As Vq(5), for q not dividing p, such
thatα is a unit at p. We shall takeχ to be a Dirichlet character of p-power conductor.
Proposition 2.16. In the notation of[Coates 1989], for( j,χ) as above we have
L(ρ)
∞(M( j)(χ))= 2(2πi)−1− j j!,
L(ρ)
p (M( j)(χ))=



(
1− p j
α
)
·
(
1− α
p1+ j
)−1
ifχ is trivial,
G(χ)
( p j
α
)r
ifχ has conductor p r> 1,
where
G(χ):=
∑
a∈(Z/pr)×
χ(a)e2πia/pr
. □
The conjecture of Coates and Perrin-Riou thus predicts that there should exist a nonzero constant M,
and a p-adic measureµ on Z×
p , such that
∫
Z×p
x jχ( x) dµ(x)= L(ρ)
p (M( j)(χ))· j!LAs,(p)(5,χ−1, j+ 1)
(2πi)(1+ j)M
,
for( j,χ) as above. Stated in this form, the conjecture is independent of the existence of the motive
MAs(5).
2H. The modular symbol attached to 9. The Bianchi modular forms we consider in this paper are
cohomological: they contribute to the cohomology of local systems on YF,1(n), as we shall now explain.
2These are all the critical values left of the centre of symmetry of the functional equation. Right of this line, we also have
critical values for k+ 1⩽ j⩽ 2k+ 2 with(−1) jχ(−1)=− 1.
p-adic Asai L-functions of Bianchi modular forms 1681
Deﬁnition 2.17. Let E be any ﬁeld extension of F, and let k> 0. We deﬁne the left E[GL2(F)]-module
Vkk(E):= V(𝓁)
k (E)⊗E V(𝓁)
k (E)σ , whereγ∈ GL2(F) acts in the usual way on the ﬁrst component and
via its complex conjugateγσ on the second component. Via this action, the space Vkk(E) gives rise to a
local system of E-vector spaces on YF,1(n), which we also denote by Vkk(E).
Theorem 2.18 (Eichler–Shimura–Harder). There is a canonical, Hecke-equivariant injection
Sk,k(UF,1(n))↪→ H1
c(YF,1(n), Vkk(C)).
Moreover, if9∈ Sk,k(UF,1(n)) is a normalised eigenform, this map induces isomorphisms of1-dimensional
C-vector spaces
Sk,k(UF,1(n))[9] ∼=−→H1
c(YF,1(n), Vkk(C))[9] ∼=−→H1(YF,1(n), Vkk(C))[9].
Proof. This was initially proved in [Harder 1987]. A treatment closer to our conventions is [Hida 1994],
where Proposition 3.1 gives an isomorphism between the cusp forms and cuspidal cohomology, the
injection of cuspidal cohomology into H1
c is explained at the start of §5, and the 1-dimensionality of each
of these spaces (hence the isomorphism) is explained in §8. □
If9∈ Sk,k(UF,1(n)), writeω9 for its image in H1
c(YF,1(n), Vkk(C)). This can be described concretely
as the class of a harmonic Vkk -valued differential form constructed from 9; for a summary of the
construction using our conventions, see [Williams 2017, §2.4].
We now consider integral structures at p. Let 9∈ Skk(UF,1(n)) be a normalised eigenform, E a
ﬁnite extension of F containing the Hecke eigenvalues of9, and P a prime of E above p. We write
R′= OF,(P) for the valuation ring of E at P, and R for its completion (so R is a ﬁnite-rank free
Zp-algebra). The same construction as before gives a ﬁnite-rank free R′-module Vkk(R′), with a left
action of GL2(OF,(p)), whose base-extension to E is Vkk(E).
IfˆOF,(p)=∏
v|p OF,v×∏′
v∤p Fv denotes the ring of ﬁnite adèles of F integral above p, the natural map
GL2(OF,(p))\[GL2(ˆOF,(p))× H3]/U→ YF(U)
is a bijection for any levelU (by the weak approximation theorem). ThusVkk(R′) gives a local system ofR′-
modules on YF(U) for any sufﬁciently smallU, whose base-extension to E is Vkk(E) as previously deﬁned.
Since every connected component of YF(U) is noncompact, its compactly supported cohomology
(with coefﬁcients in any locally constant sheaf) vanishes in degree 0. From the cohomology long exact
sequence associated to multiplication by a nonzero integer m, we conclude that its degree 1 compactly
supported cohomology with coefﬁcients in a torsion-free sheaf is torsion-free. Hence we can regard
H1
c(YF,1(n), Vkk(R′)) as an R′-lattice in H1
c(YF,1(n), Vkk(E)), preserved by the action of the Hecke
operators(Ta)∗,( Ua)∗.
Deﬁnition 2.19. We let
H1
c(YF,1(n), Vkk(R′))[9]
be the intersection of the 9-eigenspace H1
c(YF,1(n), Vkk(E))[9] with the lattice H1
c(YF,1(n), Vkk(R′)).
1682 David Loeﬄer and Chris Williams
Proposition 2.20. There exists a complex period 9∈ C×, uniquely determined up to multiplication
by(R′)×, such that the quotient
φ9:=ω9/9
is an R′-basis of H1
c(YF,1(n), Vkk(R′))[9].
Proof. Since compactly supported cohomology commutes with ﬂat base extension, it follows from the
Eichler–Shimura–Harder theorem that H1
c(YF,1(n), Vkk(E))[9] is one-dimensional over E. If φ9 is any
basis of this space, then it is also aC-basis of H1
c(YF,1(n), Vkk(C))[9], soω9 must be a C×-multiple ofφ9.
As R′ is a discrete valuation ring with ﬁeld of fractions E, the lattice H1
c(YF,1(n), Vkk(R′))[9] must be
free of rank 1 overR′. We can therefore chooseφ9 to be a generator of this module, and this determinesφ9
(and hence9) uniquely up to units in R′. □
Remarks. (i) Our normalisation of the period 9 is a little different from that used by Hida [1994, §8]:
we have used the lattice given by H1
c with integral coefﬁcients, while Hida uses the ordinary H1 with
integral coefﬁcients. Hence our φ9 may not map to an R′-basis of H1(YF,1(n), Vkk(R′))[9]. We expect
that the difference between these two R′-lattices “detects” congruences modulo P between 9 and
Eisenstein series, but we have not checked this.
(ii) There is a convenient explicit presentation for H1
c(YF,1(n), M), for very general local systems M,
using “modular symbols” (see [Barrera Salazar and Williams 2019, Lemma 8.4], generalising [Ash and
Stevens 1986, Proposition 4.2]). From this description the torsion-freeness of the cohomology, and its
compatibility with base-extension, is immediate.
The pullback φ∗
9:=∗(φ9) lies in H1
c(Y∗
F,1(n), Vkk(R′)). It is this class which we shall use in the
deﬁnition of our p-adic Asai L-function.

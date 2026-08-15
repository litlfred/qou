---
doc_id: arxiv-2412.04241v2
doc_title: "THE HABIRO RING OF A NUMBER FIELD"
section_id: sec-004-14-the-habiro-ring-of-a-number-field
section_title: "The Habiro ring of a number field"
section_number: 1.4
pages: 5-8
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
doc_brief: "THE HABIRO RING OF A NUMBER FIELD — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
the important property that vp(ζpm−ζm) > 0 for all positive integers m and all primes p,
and this will be more convenient for us.
For a ringR, the map ι motivates the notion of Galois invariantR-valued “functions near
roots of unity”. By this, we mean elements of the ring
PR =
 Y
ζ∈µ∞
R[ζ]JxK
Gal(Qab/Q)
∼=
Y
m≥1
R[ζm]JxK. (8)
(Here the fm suffice to expand F (q) around any root of unity, and not just around our
distinguished collection of roots of unity, using Galois invariance.) We will denote a typical
element of PR by f(q) = ( fm(x)), where q = ζm +x, rather than the more cumbersome
(fm(x))m≥1. We see that equation (6) now gives a map ι :H→P Z. Note that fm(x) are
formal series with no convergence properties assumed. In fact, in examples where R⊆ C
coming from perturbative knot invariants, the associated series will be factorially divergent
series over the complex numbers, whereas at the same time they are always p-adically con-
vergent on a disc of radius p−p/((p−1)(p−2)), as follows from [26, Thm.9.1, Thm.9.2]. The
series fm(x) are related to “functions near Q” defined in the previous work [26] and more
specifically the series Φα(h), where ζm +x =e2πiα−h/m and α∈ Q.
In [27] Habiro proved that the map (6) (and in fact, each of its factorsιm :HZ→ Z[ζm][ [x] ])
is injective and that its image consists of the collection of power seriesfm(x) = (ιmf)(x) that
arithmetically “glue”, generalising earlier work of Ohtsuki [39]. Let us explain how gluing
works. The map (6) satisfies the formal substitution property
fm(x +ζpm−ζm) = fpm(x) (9)
for all positive integers m and all prime numbers p. The only issue is that this equation
requires one to re-expand the left hand side, which is a power series in x, after shifting x to
x +ζpm−ζm. This is possible using the binomial theorem on x and ζpm−ζm if the shift
ζpm−ζm is small, and indeed it is in the completion Z[ζpm]∧
p of Z[ζpm], since ζpm−ζm has
positive p-valuation. Here R∧
p = lim←−nR/(pn), which is isomorphic to R⊗ Zp and will often
be denoted simply by Rp, denotes the p-completion of a ring R. Then, equation (9) holds
as an identity in the ring Z[ζpm]∧
p [ [x] ], and this compatibility property is what we meant by
“gluing”.
Summarising, an element f(q) of the Habiro ring can be identified with a collection of
power series (fm(x))m≥1∈Q
m≥1 Z[ζm][ [x] ] that satisfy the gluing property (9) for all primesp.
The gluing property implies that the entire collection ( fm(x))m≥1 is uniquely determined
by any one of its coordinate functions fm(x), indeed in many different ways, which of course
are consistent with each other. For instance f6(x) can be determined from f1(x) via the
chain f1(x)→ f3(x) = f1(x +ζ3− 1)→ f6(x) = f3(x +ζ6−ζ3) or via the chain f1(x)→
f2(x) =f1(x +ζ2− 1)→f6(x) =f2(x +ζ6−ζ2):
f1(x)
f3(x) =f1(x +ζ3− 1) f1(x +ζ2− 1) =f2(x)
f3(x +ζ6−ζ3) =f6(x) =f2(x +ζ6−ζ2)
. (10)
6 STA VROS GAROUF ALIDIS, PETER SCHOLZE, CAMPBELL WHEELER, AND DON ZAGIER
Notice, however, that the equalities here hold in different completions. We can phrase this
gluing using the language of p-adic power series and their corresponding functions. Namely,
an element of the Habiro ring consists of a collection of series fm(x)∈ Z[ζm][ [x] ] that satisfy
the following property. For every prime p, fm(x) is convergent on the open disc |x|p < 1
that containsζpm−ζm, and its re-expansion fm(x +ζpm−ζm), which is therefore defined but
a priori has potentially transcendental coefficients in Zp[ζpm], has algebraic coefficients (in
fact, in Z[ζpm]) and agrees withfpm(x). In other words, for each fixed prime p, the collection
of functions (fm(x)) can be used to define a singlep-adic analytic function on thedisconnected
domain{q∈ Cp||q|p = 1}, which is the union of the (not all distinct) open unit discs centred
at roots of unity. (Of course this set is totally disconnected anyway in the p-adic topology,
but here we mean that no two of the discs in question arep-adically close, so that the analytic
functions on them cannot be continued from one to the other.) The remarkable fact is that,
given these series come from something global, this “disconnectedness” disappears once we
start varying the prime p, in the sense that the small neighbourhoods of any two roots
of unity can be connected by neighbourhoods overlapping with respect to varying p-adic
metrics. It is this property that makes the Habiro ring work.
1.4. The Habiro ring of a number field. An abstract definition of the Habiro ring of a
number field was motivated by the ideas of q-de Rham cohomology in [43]. Our first task
is to give a power series realisation of this ring. As in the case of the Habiro ring, the
new definition involves OK-valued functions near the roots of unity, where OK is the ring
of integers of a number field K. However, there are two new features that emerge, both of
which already appeared in the numerical experiments described in Section 1.2, namely:
• one has to invert the primes dividing some integer ∆,
• the gluing now involves a Frobenius twist.
Both features cause subtleties, as we will see shortly. If ∆̸= 1, the Habiro ring ofOK[1/∆]
is no longer an integral domain, while the twist makes it unclear how to construct elements
that glue in the required way. 1
We now give the promised definition. Let K be a number field with ring of integer OK
and ∆ a positive integer divisible by the discriminant of K.2 Below, we usually take ∆ to
also be divisible by 6. The Habiro ring 3HR associated to the finite ´ etale map
Z[1/∆]→R, R = OK[1/∆] (11)
is defined as follows:
Definition 1.1. The Habiro ringHR is the subset ofPR consisting of elements
f(q) = ( fm(x))m∈Z>0 ∈ PR (12)
1We remark that both problems disappear when K is abelian over Q. Indeed, in this case we can define
an R-module structure onHR from the embedding R→H R given bya7→ (φma)m, where φm =Q
pφvp(m)
p
is the product of lifts from Kp to K of the Frobenius automorphisms φp , which exists for fields K abelian
over Q. This embedding also gives a canonical isomorphism HR∼=HZ[1/∆]⊗ZR for such K.
2One could also let ∆ be a non-zero element of OK divisible by all prime ideals whose square divides the
discriminant, but for simplicity we will always choose ∆ in Z.
3Here, we use HR rather than the more accurate HZ[1/∆]→OK[1/∆]. We will also refer to this ring as the
Habiro ring of the field K, rather than of the ring R.
THE HABIRO RING OF A NUMBER FIELD 7
that satisfy the gluing property
fm(x +ζpm−ζm) = ( φpfpm)(x) ∈ R∧
p [ζpm]JxK (13)
for primes p and all positive integers m, where φp is the Frobenius endomorphism of R∧
p ,
lifted to an endomorphism of R∧
p [ζpm]JxK fixing both ζpm and x.
Note that if p divides ∆, the above equation is trivial since the completed ring is trivial. We
also defineHR|∆ to be the same ring where we restrict to m prime to ∆, and more generally
HR|γ to be the ring where we restrict to m prime to any positive integer γ.
Note that the two equations (9) and (13) are nearly identical, the crucial difference being
the presence ofφp in (13). The reason this was not seen in the previous case was thatφp = id
for R = Z[1/∆]. The Frobenius twist makes it unclear if there is any natural R-module
structure onHR, and moreover how to construct nontrivial elements in HR. However, one
can equivalently defineHR as a finite ´ etaleHZ[1/∆]-algebra by gluing the naive base changes
R[ζm][ [q−ζm] ] overZ[ζm][ [q−ζm] ] along Frobenius twists afterp-adic completion. This abstract
definition of the Habiro ring implies in particular that HR is a finitely generated projective
HZ[1/∆]-module of rank r = [ K : Q]. (This follows from the corresponding fact after p-
completion, which itself follows from the fact that Rp[ζm]JxK has rank r over Zp[ζm]JxK.)
There is another way to view these conditions involving p-completions. Specifically, we
have natural ring isomorphisms
(HR)p∼=
ncollections of R∧
p [ζm][ [x] ]-series form≥ 1 that
glue w.r.t. re-expansion in x7→x +ζmp−ζm
o
∼=
Y
m≥1
(m,p)=1
R∧
p [ζm][ [x] ]∼=HRp, (14)
because there are no gluing constraints between the expansions around different roots of
unity of order prime to p. Moreover, for every prime p, we have a commutative diagram
HR −→ HR∧p
∩ ∩
PR
φ
−→ PR∧p
, (15)
where the bottom map is the composite of the obvious inclusion with the Frobenius endo-
morphism φvp(m)
p acting on R∧
p [ζm][ [x] ], and the Habiro ring is the universal ring associated
to the combinations over p of these diagrams, i.e., if we combine all of the p-completionsR∧
p
into bR = lim←−NR/MR∼=Q
p primeR∧
p , thenH bR
∼=Q
pHR∧p andHR is the intersection in P bR
ofPR andH bR
∼=HZ[1/∆]⊗Z bR.
Remark 1.2. Note that the ringHR is not an integral domain, since the gluing property (13)
is nontrivial only for primesp not dividing ∆, otherwiseR∧
p = 0. Instead,HR is a product of
(in general infinitely many) integral domains indexed by the equivalence classes of N under
the equivalence relation generated by m∼∆ pm for primes p not dividing ∆. Among those
integral domains isHR|∆ (corresponding to the equivalence class of all positive integers prime
to ∆), whose elements are collections of power series at roots of unity of order prime to ∆
that satisfy the gluing condition (13) for all primes p not dividing ∆. It is still possible that
there is a definition ofHR whenR is equal toOK rather than toOK[1/∆] that is an integral
8 STA VROS GAROUF ALIDIS, PETER SCHOLZE, CAMPBELL WHEELER, AND DON ZAGIER
domain, although the definition could not be exactly along the lines of the definition for
OK[1/∆].

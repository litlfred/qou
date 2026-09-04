---
doc_id: arxiv-1110.6212v2
doc_title: "On calibrated representations and the Plancherel Theorem f or affine Hecke algebras James Parkinson ∗"
section_id: sec-001-12-parameter-systems
section_title: "Parameter systems"
section_number: 1.2
pages: 3-8
source_pdf: 1110.6212v2.pdf
source_sha256: 1923b6a0bfdc810f
doc_brief: "On calibrated representations and the Plancherel Theorem f or affine Hecke algebras James Parkinson ∗ — This paper has two main purposes."
---
Let q0, q1, . . . , qn ∈ C× be such that qi = qj whenever si and sj are conjugate in WQ. We call
the sequence ( qi) a parameter system. By [3, IV, §5, No.5, Prop 5] the product
qw = qi1 · · ·qiℓ (where w = si1 · · · siℓ ∈ WQ is reduced)
3
does not depend on the particular reduced expression for w. If α ∈ W0αi ∩ W0αj then si and sj
are conjugate in W0, and hence for α ∈ R0 we deﬁne
qα = qi if α ∈ W0αi.
Let C[L] = C-span {xλ | λ ∈ L} be the group algebra of L, with the group operation written
multiplicatively as xλxµ = xλ+µ. In the ﬁeld of fractions of C[L] let (for α ∈ R0)
cα(x) =



1 − q−1
α x−α∨
1 − x−α∨ if α ∈ R1
(1 − q−1/2
0 q−1/2
n x−α∨/2)(1 + q1/2
0 q−1/2
n x−α∨/2)
1 − x−α∨ if α ∈ R2.
(Note that if α ∈ R2 then 2 α ∈ R, and so (2 α)∨ = α∨/2 is in L.) Choose relatively prime
elements nα(x) and dα(x) in C[L] so that
cα(x) = nα(x)
dα(x) .
For example, α ∈ R2 and q1/2
n = q1/2
0 then nα(x) = 1 − q−1
n x−α∨/2 and dα(x) = 1 − x−α∨/2.
Similarly, let
c′
α(x) =



1 − q−1
α
1 − x−α∨ if α ∈ R1
1 − q−1
n + q−1/2
n (q1/2
0 − q−1/2
0 )x−α∨/2
1 − x−α∨ if α ∈ R2.
Then, with dα(x) as above,
c′
α(x) = n′
α(x)
dα(x)
for some n′
α(x) ∈ C[L] with n′
α(x) and dα(x) relatively prime.
Let
c(x) =
∏
α∈R+
0
cα(x), n (x) =
∏
α∈R+
0
nα(x), d (x) =
∏
α∈R+
0
dα(x).
The expression c(x) = n(x)/d(x) is the Macdonald c-function. We write ci(x), c′
i(x), ni(x),
n′
i(x), and di(x) for ni(x) for cαi(x), c′
αi(x), nαi(x), n′
αi(x), and dαi(x) (respectively).
1.3 Aﬃne Hecke algebras
Standard references for aﬃne Hecke algebras include [14], [ 15] and [17]. With the above notation,
the aﬃne Hecke algebra HL with parameters q0, . . . , qn is the algebra over C with vector space
basis {Tw | w ∈ WL} and relations
TuTv = Tuv if ℓ(uv) = ℓ(u) + ℓ(v)
T 2
i = 1 + ( q
1
2
i − q
− 1
2
i )Ti for all i = 0, 1, . . . , n,
where we write Ti = Tsi.
The above presentation is the Coxeter presentation of HL. There is a second important
presentation which exploits the semidirect product struct ure WL = L⋊W0. This is the Bernstein
4
presentation, given by (1.2)–(1.5) below. Each λ ∈ L can be written as λ = µ − ν with
µ, ν ∈ L ∩ P +, and we deﬁne
xλ = TtµT −1
tν .
It is not hard to see that this is well deﬁned, and in particula r xλ = Ttλ if λ is dominant.
It can be shown [15] that HL has vector space basis {Twxλ | λ ∈ L, w ∈ W0} and relations
T 2
i = 1 + ( q
1
2
i − q
− 1
2
i )Ti for i = 1, . . . , n (1.2)
TiTjTi · · · = TjTiTj · · · (mij factors) for 1 ≤ i < j ≤ n (1.3)
xλxµ = xλ+µ for all λ, µ ∈ L (1.4)
Tixλ − xsiλTi = q
1
2
i c′
i(x)(xλ − xsiλ) for 1 ≤ i ≤ n and λ ∈ L. (1.5)
Thus we see a copy of the group algebra C[L] of the lattice L inside of HL. The relation (1.5) is
the Bernstein relation. Since siλ = λ − ⟨λ, αi⟩α∨
i and ⟨λ, αi⟩ ∈ Z the “fraction” c′
i(x)(xλ − xsiλ)
that appears in the Bernstein relation is actually an elemen t of C[L].
It is well known (see, for example, [15, (4.2.10)]) that the c entre of HL is
C[L]W0 = {f ∈ C[L] | w · f = f for all w ∈ W0}.
This has powerful implications for the representation theo ry of HL. For example it forces
the irreducible representations to be ﬁnite dimensional (s ince the centre acts on irreducible
representations by scalars, and it is evident that HL is ﬁnite dimensional over C[L]W0).
It is natural to seek modiﬁcations τw of Tw which satisfy a “simpliﬁed Bernstein relation”
τwxλ = xwλτw for all w ∈ W0 and λ ∈ L. (1.6)
Deﬁne elements τ1, . . . , τn ∈ HL by
τi = di(x)Ti − q
1
2
i n′
i(x).
The Bernstein relation gives τixλ = xsiλτi, and it can be shown (see [23, Proposition 2.7] for
example) that for w ∈ W0 the product
τw = τi1 · · ·τiℓ is independent of the choice of reduced expression w = si1 · · ·siℓ.
Thus the elements τw, w ∈ W0, satisfy (1.6), and a direct calculation gives the useful fo rmula
τ 2
i = qi ni(x)ni(x−1) ∈ C[L]. (1.7)
1.4 Harmonic analysis for the aﬃne Hecke algebra
Suppose now that q0, q1, . . . , qn > 1. Deﬁne an involution ∗ on HL and the canonical trace
functional Tr : HL → C by
( ∑
w∈WL
cwTw
) ∗
=
∑
w∈WL
cwTw−1 and Tr
( ∑
w∈WL
cwTw
)
= c1.
An induction on ℓ(v) shows that Tr( TuT ∗
v ) = δu,v for all u, v ∈ WL, and so
Tr(h1h2) = Tr(h2h1) for all h1, h2 ∈ HL.
5
Thus ( h1, h2) = Tr(h1h∗
2) deﬁnes an Hermitian inner product on HL. Let ‖h‖2 =
√
(h, h). The
algebra HL acts on itself by left multiplication, and the correspondin g operator norm is
‖h‖ = sup{‖hx‖2 : x ∈ HL, ‖x‖2 ≤ 1}.
Let HL denote the completion of HL with respect to this norm. Thus HL is a non-commutative
C ∗-algebra. This algebra is ‘liminal’. Even better, all irred ucible representations of HL are ﬁnite
dimensional, and so by [7, §8.8] there exists a probability measure µ such that
Tr(h) =
∫
spec(HL)
χπ(h)dµ(π) for all h ∈ HL. (1.8)
The measure µ is the Plancherel measure. Only those representations of HL which extend to
the completion HL appear in the Plancherel Theorem. It is known [19, Corollary 6.2] that these
are the tempered representations of HL (see [19, §2.7] for the deﬁnition).
If t ∈ Hom(L, C×) we write tλ = t(λ). The Weyl group W0 acts on Hom( L, C×) by the
formula ( wt)λ = tw−1λ. Following [18], deﬁne a function Gt : HL → C by
Gt(h) =
∑
µ∈L
t−µTr(xµh) (1.9)
whenever the series converges. From [18] we have the followi ng (see also [19, (3.9)]).
Theorem 1.1. The series Gt(h) is absolutely convergent for all h ∈ HL whenever |tα∨
i | < q −1
i
for (R, i) ⁄= (BCn, n) and |tα∨
n | < q −1
0 q−1
n for (R, i) = ( BCn, n). Moreover,
Gt(h) = gt(h)
qw0c(t)c(t−1)d(t) (1.10)
where for each ﬁxed h the function gt(h) has a analytic continuation in the t-variable to Hom(L, C×).
Moreover, gt(h) satisﬁes
1. gt(h) is a polynomial in {tλ | λ ∈ L} (for ﬁxed h ∈ HL),
2. gt(1) = d(t) for all t ∈ Hom(L, C×), and
3. gt(xλhxµ) = tλ+µgt(h) for all λ, µ ∈ L and all h ∈ HL.
Remark 1.2. (a) Note that tλgt(τw) = gt(τwxλ) = gt(xwλτw) = twλgt(τw), and so if wt ⁄= t
then
gt(τwxλ) = δw,1tλd(t).
Then by condition 1 in the theorem this formula holds for all t ∈ Hom(L, C×).
(b) The three conditions in the theorem completely determin e gt(h). For example consider
the ˜A2 case. It is suﬃcient to calculate gt(Tw) for each w ∈ W0, because gt(Twxλ) = tλgt(Tw).
Write Q = q
1
2 − q− 1
2 . Applying gt to the Bernstein relation T1xα∨
1 = x−α∨
1 T1 + Q(1 + xα∨
1 ) gives
gt(T1) = Q(1 − t−α∨
1 )−1d(t) = Q(1 − t−α∨
2 )(1 − t−α∨
1 −α∨
2 ).
Similarly, gt(T2) = Q(1 − t−α∨
1 )(1 − t−α∨
1 −α∨
2 ), gt(T1T2) = gt(T2T1) = Q2(1 − t−α∨
1 −α∨
2 ), and
gt(T1T2T1) = Q3 + Q(1 − t−α∨
1 )(1 − t−α∨
2 ), making (1.10) completely explicit in type ˜A2.
6
Let
ft(h) = gt(h)
d(t) . (1.11)
Note that ft(h) may have poles at points where tα∨
= 1 for some α ∈ R0. Fix a Z-basis
λ1, . . . , λn of L. From (1.9) and (1.10) we have
Tr(h) = 1
qw0
∫
a1T
· · ·
∫
anT
ft(h)
c(t)c(t−1) dt1 · · ·dtn (1.12)
where ti = tλi, dti is Haar measure on the circle group T, and where a1, . . . , an > 0 are chosen
such that if t ∈ Hom(L, C×) with |tλi| = ai for each i then |tα∨
i | < q −1
i (if ( R, i) ⁄= ( BCn, n))
and |tα∨
n | < q −1
0 q−1
n (if ( R, i) = ( BCn, n)). Formula (1.12) appears in [19, Theorem 3.7], and is
the starting point of the Plancherel Theorem.
2 Representations of aﬃne Hecke algebras
Let M be a ﬁnite dimensional HL-module. For each t ∈ Hom(L, C×) let
Mt = {v ∈ M | xλ · v = tλv for all λ ∈ L}
M gen
t = {v ∈ M | for each λ ∈ L there is a k > 0 such that ( xλ − tλ)k · v = 0}
be the t-weight space and the generalised t-weight space respectively. Each ﬁnite dimensional
HL-module M decomposes into a direct sum of generalised t-weight spaces
M =
⨁
t∈supp(M )
M gen
t
where supp( M ) = {t ∈ Hom(L, C×) | M gen
t ⁄= 0} is the support of M .
A ﬁnite dimensional HL-module M is calibrated if
M gen
t = Mt for all t ∈ supp(M ).
(In the literature this is also refereed to as tame). The main purpose of the ﬁrst half of this paper
is to construct calibrated irreducible representations of general aﬃne Hecke algebras. We suspect
that a complete classiﬁcation of calibrated representatio ns along the lines of the 1-parameter
case is possible (perhaps with some restrictions like Wt = W(t)), although such a classiﬁcation
requires detailed information about the representation th eory of rank 2 (multi-parameter) aﬃne
Hecke algebras, and this would take us beyond the scope of the present paper. Thus the focus
of this paper is on construction, and the question of classiﬁ cation will be pursued in later work.
The elements τi ∈ HL, considered as operators on a representation, are often cal led inter-
twining operators because of the following fundamental and important fact.
Lemma 2.1. Let 1 ≤ i ≤ n. Let M be a ﬁnite dimensional HL-module, and suppose that
t ∈ supp(M ). Then as operators,
τi : M gen
t → M gen
sit and τi : M gen
sit → M gen
t .
Moreover, ni(t)ni(t−1) ⁄= 0 if and only if each operator is bijective.
7
Proof. Let m ∈ M gen
t . By (1.6) we compute
(xλ − (sit)λ)kτi · m = τi(xsiλ − tsiλ)k · m = 0
for suﬃciently large k. Thus τi · m ∈ M gen
sit . For the ﬁnal claim, note that by (1.7) the operator
τ 2
i : M gen
t → M gen
t is given by τ 2
i · m = qini(t)ni(t−1)m.
By Schur’s Lemma (see [29]) the centre C[L]W0 of HL acts on an irreducible module M by
scalars. It follows that there exists t ∈ Hom(L, C×) such that
p(x) · v = p(t)v for all p(x) ∈ C[L]W0 and all v ∈ M .
The element t is only deﬁned up to W0 orbits. The orbit W0t is called the central character
of M , although as is customary we will usually refer to any t′ ∈ W0t as ‘the’ central character
of M . A central character t ∈ Hom(L, C×) is called regular if tα∨
⁄= 1 for all α ∈ R0.

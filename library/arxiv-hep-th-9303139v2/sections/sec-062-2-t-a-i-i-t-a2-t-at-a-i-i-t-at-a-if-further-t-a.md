---
doc_id: arxiv-hep-th-9303139v2
doc_title: "ITFA 93-10 March 1993 A.Morozov"
section_id: sec-062-2-t-a-i-i-t-a2-t-at-a-i-i-t-at-a-if-further-t-a
section_title: "((T a ⊗I + I ⊗T a)2 −T aT a ⊗I −I ⊗T aT a).) If further, T a ⊗T a"
section_number: 2
pages: 81-92
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
doc_brief: "ITFA 93-10 March 1993 A.Morozov — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
annihilates the product of two vacuum states:
(T a ⊗T a) | 0⟩⊗| 0⟩= 0,
(4.17)
then the same equation holds for all A:
(T a ⊗T a) | OA⟩⊗| OA⟩= 0.
(4.18)
Condition (4.17) is trivially valid in our case:
X
n∈Z
ψn | 0⟩⊗˜ψn | 0⟩= 0,
(4.19)
since in every term in the sum one of the vacuum states is annihilated: the
ﬁrst one of n ≥0 and the second one if n < 0.31 Thus we obtain the relation
X
n∈Z
ψn | OA⟩⊗˜ψn | OA⟩= 0,
(4.20)
which can be now multiplied from the left by
⟨0 | ψ(∞)eHCartan(t) ⊗⟨0 | ˜ψ(∞)eHCartan(t′)
(t′
k do not need to coincide with tk) and after insertions of ψ-operators are
expressed as the shifts of times, we obtain:
X
n∈Z
D−
n τ{t | A} ⊗D+
n τ{t | A} = 0,
(4.21)
31 It is easy to verify directly that P
n ψn⊗˜ψn is indeed a Casimir operator in the tensor
product:
[P
n ψn ⊗˜ψn, I ⊗P
l,m Almψl ˜ψm + P
l,m Almψl ˜ψm ⊗I] =
= P
n

ψn ⊗P
m Anm ˜ψm −P
l Alnψl ⊗˜ψn

= P
l
P
m Alm(ψl ⊗˜ψm −ψl ⊗˜ψm) = 0.
78
where P
n≥0 D±
n z−n = exp

± P
k>0
1
kzk
∂
∂tk

. This is particular form of Hirota
equation [86], which is often used to deﬁne τ-functions, associated with inte-
grable hierarchies. If one takes (4.8) for the deﬁnition, as it is more natural to
do in the general ”theory of everything” and as we did above, eq.(4.21) is the
starting point for the path, leading to hierarchies in conventional form of dif-
ferential equations, the Lax and pseudodiﬀerential representations naturally
appearing on the way. We do not go along this path in these notes.
The last remark to be made, before we proceed to more detailed formu-
las, is that τ-functions can be considered as determinants Det¯∂of the ¯∂-
operators acting on ﬁelds with some complicated boundary conditions (like
ψ(z) ∼exp
P
k>0 tkz−k
in the simplest case of t-dependencies). Entire A-
dependence is usually described in this context as that on the point of the
”universal module space”, which once appeared in the study of string models
on Riemann surface of arbitrary genus [87]. From this point of view more
general τ-functions are sections of the bundles over universal module space,
associated with conformal models, more sophisticated then just the theory of
free fermions (and b, c-systems). The WZNW model is, of course, the most
important example to be studied in this context.
The crucial feature of all the quantites, associated in this way to confor-
mal models is applicability of Wick theorem, reducing multipoint correlation
functions to pair correlators. In the free fermion case this is just a conse-
quence of quadratic form of Lagrangian, in generic situation this follows from
existence of holomorphic operator algebra, which allows to deﬁne the corre-
lators by ﬁxation of monodromy properties, dictated by pairwise collision
of points. Wick theorem is the concrete source of determinant formulas for
tau-functions, which are used in order to establish their relations with matrix
models and other branches of string theory.
After this discussion of the context where free-fermion τ-functions can and
do appear, we turn now to more detailed and exact formulas, relevant in this
particular free-fermion case. They are mostly due to Japanese school [88],
though many other people contributed to this ﬁeld after it was established.
The only sophisticated part of the work with these formulas is accurate ac-
counting for the normal ordering routine which will be mostly unnecessary for
our purposes. We shall mostly follow the presentation of papers [89],[30],[36].
79
4.4
Basic determinant formula for the free-fermion cor-
relator
Let us consider the following matrix element:
τN{t, ¯t | G} = ⟨N | eH G e
¯
H | N⟩
(4.22)
where
ψ(z) =
X
n∈Z
ψnzndz1/2;
˜ψ(z) =
X
n∈Z
˜ψnz−n−1dz1/2;
G = exp

X
m,n∈Z
Amnψm ˜ψn

;
H =
X
k>0
tkJk,
¯H =
X
k>0
¯tkJ−k
J(z) = ψ(z) ˜ψ(z) =
X
n∈Z
Jnz−n−1dz;
Jn =
X
k
ψk ˜ψk+n;
[ ˜ψm, ψn]+ = δm,n;
[Jm, Jn] = mδm+n,0;
ψm | N⟩= 0,
m < N;
⟨N | ψm = 0,
m ≥N;
˜ψm | N⟩= 0,
m ≥N;
⟨N | ˜ψm = 0,
m < N;
Jm | N⟩= 0,
m > 0;
⟨N | Jm = 0,
m < 0.
(4.23)
The ”N-th vacuum” | N⟩is deﬁned as the Dirac sea, ﬁlled up to the level N:
| N⟩=
∞
Y
i=N
˜ψi | ∞⟩=
N−1
Y
i=−∞
ψi | −∞⟩;
⟨N |= ⟨∞|
∞
Y
i=N
ψi = ⟨−∞|
N−1
Y
i=−∞
˜ψi,
(4.24)
where the ”empty” (bare) and ”completely ﬁlled” vacua are deﬁned so that:
˜ψm | −∞⟩= 0,
⟨−∞| ψm = 0,
ψm | ∞⟩= 0,
⟨∞| ˜ψm = 0
(4.25)
for any m ∈Z. For the only reason that operators J, H, ¯H and G are
deﬁned so that they have usually ˜ψ at the very right and ψ at the very left,
80
we have also:
Jm | −∞⟩= 0,
⟨−∞| Jm = 0,
G±1 | −∞⟩=| −∞⟩;
⟨−∞| G±1 = ⟨−∞|;
e± ¯
H | −∞⟩=| −∞⟩;
⟨−∞| e±H = ⟨−∞| .
(4.26)
Now we can use all these formulas to rewrite our original correlator (4.22)
as:
⟨N | eH G e
¯
H | N⟩=
= ⟨−∞|


N−1
Y
i=−∞
˜ψi

eH G e
¯
H


N−1
Y
i=−∞
ψi

| −∞⟩=
= ⟨−∞| e−H


N−1
Y
i=−∞
˜ψi

eH G e
¯
H


N−1
Y
i=−∞
ψi

e−¯
H | −∞⟩=
= ⟨−∞|
N−1
Y
i=−∞
˜Ψi[t]
N−1
Y
j=−∞
ΨG
j [¯t] | −∞⟩=
= Det−∞<i,j<N⟨−∞| ˜Ψi[t]ΨG
j [¯t] | −∞⟩=
= Deti,j<0Hi+N,j+N.
(4.27)
The last two steps here were introduction of ”GL(∞)-rotated” fermions,
˜Ψi[t] ≡e−HψieH;
Ψj[¯t] ≡e
¯
Hψje−¯H;
ΨG
j [¯t] ≡GΨj[¯t]G−1,
(4.28)
and application of the Wick theorem to express multifermion correlation
function through pair correlators
Hij(t, ¯t) ≡⟨−∞| ˜Ψi[t]ΨG
j [¯t] | −∞⟩=
= ⟨−∞| ˜Ψi[t] G Ψj[¯t] | −∞⟩,
(4.29)
(once again the fact that G−1 | −∞⟩=| −∞⟩was used). The only non-trivial
dynamical information entered through applicability of the Wick theorem,
and for that it was crucial that all the operators eH, e ¯
H, G are quadratic
exponents, i.e. can only modify the shape of the propagator, but do not
destroy the quadratic form of the action (ﬁelds remain free). This is ex-
actly equivalent to the statement that ”heisenberg” operators Ψ[t] are just
”rotations” of ψ, i.e. that transformations (4.28) are linear.
81
We shall now describe these transformations in a little more explicit form.
Namely, their entire time-dependence can be encoded in terms of ”Shur poli-
nomials” Pn(t). These are deﬁned to have a very simple generating function
(which we already encountered many times in the theory of matrix models):
X
n≥0
Pn(t)zn = exp
 ∞
X
k=1
tkzk
!
(4.30)
(i.e. P0 = 1,
P1 = t1,
P2 = t2
1
2 + t2 etc.), and satisfy the relation
∂Pn
∂tk
= Pn−k.
(4.31)
Since
exp
 ∞
X
k=1
tkzk
!
=
Y
k>0

X
nk≥0
1
nk! tnk
k zknk

,
Shur polinomials can be also represented as
Pn(t) =
X
{nk}
P
k>0 knk=n

Y
k>0
1
nk! tnk
k

.
(4.32)
Now, since
e−BAeB = A + [A, B] + 1
2![[A, B], B] + 1
3![[[A, B], B], B] + . . .
and
[ ˜ψi, Jk] = ˜ψi+k,
[[ ˜ψi, Jk1], Jk2] = ˜ψi+k1+k2, . . . ,
we have for every ﬁxed k:
e−tkJk ˜ψietkJk =
X
nk≥0
tnk
k
nk!
˜ψi+knk.
82
It remains to note that all the harmonics of J in H = P
k>0 tkJk commute
with each other, to obtain:
˜Ψi(t) = e−H ˜ψieH =

Y
k>0
e−tkJk

˜ψi

Y
k>0
etkJk

=
=
X
n≥0
˜ψi+n






X
{nk}
P
k>0 knk=n

Y
k>0
1
nk! tnk
k








(4.32)
=
=
X
n≥0
˜ψi+nPn(t) =
X
l≥i
˜ψlPl−i(t).
(4.33)
Similarly, relation [Jk, ψj] = ψk+j implies, that
Ψj(¯t) = e
¯
Hψje−¯
H =
X
n≥0
ψj+nPn(¯t) =
X
m≥j
ψmPm−j(¯t)
(4.34)
and ﬁnally32
Hij = P
l≥i
m≥j⟨−∞| ˜ψl G ψm | −∞⟩Pl−i(t)Pm−j(¯t) =
=
P
l≥i
m≥j TlmPl−i(t)Pm−j(¯t),
(4.35)
which implies also that
∂Hij
∂tk
= Hi+k,j;
∂Hij
∂¯tk
= Hi,j+k.
(4.36)
Matrix
Tlm ≡⟨−∞| ˜ψl G ψm | −∞⟩
(4.37)
32 Eqs.(4.34) can be also interpreted as representations of Shur polinomials in terms of
fermionic correlators in the bare vacuum:
Pm(¯t) = ⟨−∞| ˜ψj+me ¯
Hψj | −∞⟩;
Pm(t) = ⟨−∞| ˜ψieHψi+m | −∞⟩
83
is the one which deﬁnes fermion rotations under the action of GL(∞)-group
element G:
GψmG−1 = P
l∈Z ψlTlm;
G−1 ˜ψlG =
P
m∈Z Tlm ˜ψm, or G ˜ψlG−1 =
P
m∈Z(T −1)lm ˜ψm.
(4.38)
If G = 1, Tlm = δlm. If all tk = ¯tk = 0, Hij = Tij.
4.5
Toda-lattice τ-function and linear reductions of Toda
hierarchy
In the previous subsection we derived a formula
τN{t, ¯t | G} = Det i,j<0 Hi+N,j+N
(4.39)
for the basic correlator, which deﬁnes ”Toda-lattice τ-function”. For obvious
reasons ¯t are often refered to as negative-times. τ-function can be normalized
by dividing over the same quantity for all time-variables vanishing, but this
is not always convenient. Eq.(4.39) has generalizations - when similar matrix
elements in a multifermion system is considered - this leads to ”multicompo-
nent Toda” (or AKNS) τ-functions. Generalizations to arbitrary conformal
models should be considered as well. It has also particular ”reductions”, of
which the most important are: KP (Kadomtsev-Petviashvili), forced (semi-
inﬁnite) and Toda-chain τ-functions. This is the subject to be discussed in
this subsection.
Idea of linear reduction is that the form of operator G, or, what is the
same, of the matrix Tlm in eq.(4.35), can be adjusted in such a way, that
τN{t, ¯t | G} becomes independent of some variables, i.e. equation(s)
 X
k
α ∂
∂tk
+
X
k
¯α ∂
∂¯tk
+
X
k
βkDN(k) + γ
!
τN{t, ¯t | G} = 0
(4.40)
can be solved as equations for G for all the values of t, ¯t and N at once.
(In (4.40) DN(k)fN ≡fN+k −fN.) In this case the system of integrable
equations (hierarchy), arising from Hirota equation for τ, gets reduced and
one usually speaks about ”reduced hierarchy”. Usually equation (4.40) is
imposed directly on matrix Hij, of course than (4.40) is just a corollary.
84
We shall refer to the situation when (4.40) is fulﬁlled for any t, ¯t, N as
to ”strong reduction”. It is often reasonable to consider also ”weak reduc-
tions”, when (4.40) is satisﬁed on particular inﬁnite-dimensional hyperplanes
in the space of time-variables. Weak reduction is usually a property of entire
τ-function as well, but not expressible in the from of a local linear equa-
tion, satisﬁed identicall for all values of t, ¯t, N. Now we proceed to concrete
examples:
Toda-chain hierarchy.
This is a strong reduction.
The corresponding
constraint (4.40) is just
∂Hij
∂tk
= ∂Hij
∂¯tk
,
(4.41)
or, because of (4.36), Hi+k,j = Hi,j+k. It has an obvious solution:
Hi,j = ˆHi+j,
(4.42)
i.e. Hij is expressed in terms of a one-index quantity ˆHi. It is, however, not
enough to say, what are restrictions on Hij - they should be fulﬁled for all
t and ¯t at once, i.e. should be resolvable as equations for Tlm. In the case
under consideration this is simple: Tlm should be such that
Tlm = ˆTl+m.
(4.43)
Indeed, then
Hij = P
l,m TlmPl−i(t)Pm−j(¯t) = P
l,m ˆTl+mPl−i(t)Pm−j(¯t) =
= P
n≥0 ˆTn+i+j (Pn
k=0 Pk(t)Pn−k(¯t)) ,
and
ˆHi =
X
n≥0
ˆTn+i
 n
X
k=0
Pk(t)Pn−k(¯t)
!
.
(4.44)
Volterra hierarchy. Toda-chain τ-function can be further weakly reduced
to satisfy the identity
∂τ2N
∂t2k+1

{t2l+1=0}
= 0,
for all k,
(4.45)
85
i.e. τ2N is requested to be even function of all odd-times t2l+1 (this is an
example of ”global characterization” of the weak reduction). Note that (4.45)
is imposed only on Toda-chain τ-function with even values of zero-time. Then
(4.45) will hold whenever ˆHi in (4.44) are even (odd) functions of todd for
even (odd) values of i. Since Shur polinomials Pk(t) are even (odd) functions
of odd-times for even (odd) k, it is enough that the sum in (4.44) goes over
even (odd) n when i is even (odd). In other words, the restriction on Tlm is
that
Tlm = ˆTl+m,
and
ˆT2k+1 = 0 for all k.
(4.46)
Forced hierarchies.
This is another important example of strong re-
duction. It also provides an example of singular τ-functions, arising when
G = exp
P Amnψm ˜ψn

blows up and normal ordered operators should be
used to deﬁne regularized τ-functions. Forced hierarchy appears when G can
be represented in the form [89] G = G0P+, where projection operator P+ is
such that
P+ | N⟩=| N⟩for N ≥N0,
P+ | N⟩= 0 for N < N0.
(4.47)
Explicit expression for this operator is33
P+ = : exp

−
X
l<N0
˜ψlψl

: =
Y
l<N0
(1 −˜ψlψl) =
Y
l<N0
ψl ˜ψl.
Because of (4.47), P+ | −∞⟩=), and the identity G | −∞⟩=| −∞⟩, which
was essentially used in the derivation in (4.27), can be satisﬁed only if G0 is
singular and Tlm = ∞. In order to avoid this problem one usually introduces
in the vicinity of such singular points in the universal module space a sort of
normalized (forced) τ-function τ f
N ≡
τN
τN0 . One can check that now T f
lm = ∞
for all l, m < N0, and τ f can be represented as determinant of a ﬁnal-
dimensional matrix [90],[89]:
τ f
N = DetN0≤i,j<NHf
ij
for N > N0;
33 Normal ordering sign : : means that all operators ˜ψ stand to the left of all operators
ψ. The product at the r.h.s. obviously implies both the property (4.47) and projection
property P 2
+ = P+.
86
τ f
N0 = 1;
τ f
N = 0
for N < N0.
(4.48)
For N > N0 we have now determinant of a ﬁnite-dimensional (N −N0) ×
(N −N0) matrix. The choice of N0 is not really essential, therefore it is better
to put N0 = 0 in order to simplify formulas, phraising and relation with the
discrete matrix models (N0 is easily restored if everywhere N is substituted
by N −N0). For forced hierarchies one can also represent ˆτ as
τ f
N = Det0≤i,j<N∂i
1 ¯∂j
1Hf,
(4.49)
where Hf = Hf
00 and ∂1 =
∂
∂t1, ¯∂1 =
∂
∂¯t1. For forced Toda-chain hierarchy
this turns into even simpler expression:
τ f
N = Det0≤i,j<N∂i+j
1
ˆHf,
(4.50)
while for the forced Volterra case we get a product of two Toda-chain τ-
functions with twice as small value of N [91]:
τ f
2N =

Det0≤i,j<N∂i+j
2
ˆHf
·

Det0≤i,j<N∂i+j
2
(∂2 ˆHf)

=
= τ f
N[ ˆHf] · τ f
N[∂2 ˆHf].
(4.51)
Forced τ f
N can be always represented in the form of a scalar-product ma-
trix model. Indeed,
Hij =
X
TlmPl−i(t)Pm−j(¯t) =
I I
eU(h)+ ¯U(¯h)hi¯hjT(h, ¯h)dhd¯h,
(4.52)
where T(h, ¯h) ≡
P
lm Tlmh−l−1¯h−m−1, and eU(h) = e
P
k>0 tkhk =
P
l≥0 hlPl(t).
Then, since Det0≤i,j<Nhi = ∆N(h) - this is where it is essential that the
hierarchy is forced -
Det0≤i,j<NHij =
Y
i
I I
eU(hi)+ ¯U(¯hi)T(hi, ¯hi)dhid¯hi · ∆N(h)∆N(¯h),
(4.53)
i.e. we obtain a scalar-product model with
dµh,¯h = eU(h)+ ¯U(¯h)T(h, ¯h)dhd¯h.
(4.54)
87
Inverse is also true: partition function of every scalar-product model is forced
Toda-lattice τ-function - see section 4.7 for more details.
KP hierarchy. In this case we just ignore the dependence of τ-function
on times ¯t.
Every Toda-lattice τ-function can be considered also as KP
τ-function: just operator GKP ≡Ge ¯
H (a point of Grassmannian) becomes ¯t-
dependent. Usually N-dependence is also eliminated - this can be considered
as a little more sophisticated change of G. When N is ﬁxed, extra changes of
ﬁeld-variables are allowed, including transformation from Ramond to Neveu-
Schwarz sector etc. Often KP hierarchy is from the very beginning formulated
in terms of Neveu-Schwarz (antiperiodic) fermionic ﬁelds (associated with
principal representations of Kac-Moody algebras), i.e. expansions in the ﬁrst
line of (4.23) are in semi-integer powers of z: ψNS(z) = P
n∈Z ψnzn−1
2dz1/2.
Given a KP τ-function one can usually construct a Toda-lattice one with
the same G, by introducing in appropriate way dependencies on ¯t and N.
For this purpose τ KP should be represented in the form of (4.39):
τ KP{t | G} = Deti,j<0HKP
ij ,
(4.55)
where HKP
ij
= P
l TljPl−i(t). Since Tlm is a function of G only, it does not
change when we built up a Toda-lattice τ-function:
τN{t, ¯t | G} = Deti,j<0Hi+N,j+N;
Hij =
P
l,m TlmPl−i(t)Pm−j(¯t) =
P
m HKP
im Pm−j(¯t).
(4.56)
Then
τ KP{t | G} = τ0{t, 0 | G}.
(4.57)
If we go in the opposite direction, when Toda-lattice τ-function is considered
as KP τ-function,
τ0{t, ¯t | G} = τ KP{t | ˜G(¯t)};
˜HKP
ij
=
X
m
HimPm−j(¯t) and
˜Tlj{ ˜G(¯t)} =
X
m
Tlm{G}Pm−j(¯t).
(4.58)
KP reduction in its turn has many further weak reductions (KdV and
Boussinesq being the simplest examples). We shall mention them again in
section 4.9 below, after Miwa transformation of representation (4.39) will be
considered in the next subsection.
88
4.6
Fermion correlator in Miwa coordinates
Let us now return to original correlator (4.22) and discuss in a little more
details the implications of bosonization identity (4.13). In order not to write
down integrals of J, we introduce scalar ﬁeld:34
φ(z) =
X
k̸=0
k∈Z−0
J−k
k zk + φ0 + J0 log z,
(4.59)
such that ∂φ(z) = J(z). Then (4.13) states that:
: ψ(λ) ˜ψ(˜λ) : = : eφ(˜λ)−φ(λ) :
(4.60)
”Normal ordering” here means nothing more but the requirement to neglect
all mutual contractions (or correlators) of operators in between :
: when
Wick theorem is applied to evaluate corrletion functions. One can also get
rid of the normal ordering sign at the l.h.s. of (4.60), then
ψ(λ) ˜ψ(˜λ) = : eφ(˜λ) : : e−φ(λ) :
(4.61)
In distinguished coordinates on a sphere, when the free ﬁeld propagator is
just log(z −˜z), one also has:
ψ(z) ˜ψ(˜z) =
1
z −˜z : ψ(z) ˜ψ(˜z) :
Our task now is to express operators eH and e ¯
H through the ﬁeld φ. This
is simple:
H =
I

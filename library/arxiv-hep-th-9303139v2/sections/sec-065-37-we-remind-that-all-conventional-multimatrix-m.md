---
doc_id: arxiv-hep-th-9303139v2
doc_title: "ITFA 93-10 March 1993 A.Morozov"
section_id: sec-065-37-we-remind-that-all-conventional-multimatrix-m
section_title: "We remind that all conventional multimatrix models (with inter-matrix"
section_number: 3.7
pages: 101-131
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
doc_brief: "ITFA 93-10 March 1993 A.Morozov — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
interaction of the form exp(TrH(α)H(α+1)) belong to this class. The crucial
formulas are:
ZN = DetNHf
ij = Det0≤i,j≤N−1Hf
ij =
= Det−N≤i,j<0Hf
i+N,j+N;
Hf
ij =
∂2
∂ti∂¯tj Hf =

∂
∂t1
i 
∂
∂¯t1
j Hf.
(4.97)
Here
Hf
ij = ⟨hi | ¯hj⟩=
Z
dˆµh,¯heU(h)+ ¯U(¯h)hi¯hj.
(4.98)
Further,
eU(h) = e
P
k≥0 tkhk =
X
l
hlPl(t);
e
¯U(¯h) = e
P
k≥0 ¯tk¯hk =
X
m
¯hmPm(¯t)
(4.99)
and thus
Hf
ij = P
l,m⟨⟨hi+l | ¯hj+m⟩⟩Pl(t)Pm(¯t) = P
l,m T f
lmPl−i(t)Pm−j(¯t),
T f
lm = ⟨⟨hl | ¯hm⟩⟩,
(4.100)
98
where the scalar product ⟨⟨| ⟩⟩is w.r.to the measure dˆµh,¯h (while ⟨| ⟩is
w.r.to dµh,¯h = eU(h)+ ¯U(¯h)dˆµh,¯h).
One would immediately recognize in these formulas representation (4.39)
of Toda-lattice τ-function, be there no additional restriction that determinant
in (4.97) is over ﬁnite-dimensional N × N matrix (indices are constrained:
i, j ≥−N). This can be automatically taken into account if we require that
T f
lm = ∞for all l, m < 0,
(4.101)
and identify ZN as a τ-function τ f of forced Toda-lattice hierarchy (thus the
supescript f carried by H and T). We conclude that partition functions of
any scalar-product model is a τ f-function of forced Toda-lattice hierarchy.
Let us now consider them as KP τ-functions.
This means that the
¯t-dependence is simply ignored.
However, N will be preserved explicitly
as a parameter, labeling KP τ-function. After Miwa transformation tk =
−1
k
P
γ λ−k
γ
−rk, described in section 3.7, we get:
ZN = ˆZN
detγδ ˆQN+γ−1(λδ)
∆(λ)
,
(4.102)
where ˆQ are orthogonal polinomials w.r.to the measure dˆνh,¯h = e−P
k rkhkdˆµh,¯h.
We conclude that in the framework of KP hierarchy the scalar-product mod-
els are distinguished by the fact, that the corresponding ϕγ(λ) in (4.86) are
polinomials rather than inﬁnite series in powers of λ−1.
1-Matrix model. This is particular example of scalar product model with
a local measure dµh,¯h = eU(h)+ ¯U(¯h)δ(h −¯h)dhd¯h. In this case
Hf
ij = ⟨hi | ¯hj⟩= ⟨hi+j⟩=
∂
∂ti+j
Hf =
 ∂
∂t1
!i+j
Hf.
(4.103)
Thus in this case we deal with the (forced) Toda-chain reduction of Toda-
lattice hierarchy. In the end of this section 4 we use orthogonal polinomials to
present a detailed description of 1-matrix models as a Toda-chain τ-function.
This model can be alternatively deﬁned as Gaussian Kontsevich model:
see section 3.8. The fact that partition function is a τ-function follows then
from the general statement for GKM, see below. The fact that it is forced
τ-function is related to the property c−N = 0, mentioned at the end of s.3.8
99
(and proved in s.3.9). Also reduction to Toda-chain hierarchy can be observed
directly in terms of GKM: see ref.[36] for more details.
Multicomponent (conformal) matrix models. These are related to multi-
component hierarchies, with τ-functions representable as correlators in multi-
fermion systems.
An example of determinant formula which substitutes
(4.39) in the 2-component case, is given at the end of section 3.5, where it is
derived from consideration of the relevant matrix model [39]. For derivation
of the same determinant formula in the theory of τ-functions see ref.[92].
Generic theory of multicomponent hierarchies is now making its ﬁrst steps
and we do not review it in these notes. See [93] for the group-theory approach
to the problem.
Generalized Kontsevich model. Determinant formulas for this case are
derived in Section 3.3. The most important expression is
ZV {N, T} =
1
(detΛ)N
detγδϕγ+N(λδ)
∆(λ)
,
(4.104)
where
ϕγ(λ) =
1
√
2πe−λV ′(λ)+V (λ)q
V ′′(λ)
R xγ−1e−V (x)+V ′(λ)xdx =
= λγ−1(1 + O(λ−1));
(4.105)
and
ϕγ(λ) = Aϕγ−1(λ) = Aγ−1Φ(λ).
(4.106)
For N = 0 this is just the representation, peculiar for KP τ-function in Miwa
parametrization Tk = 1
ktrΛ−k, see eq.(4.86) above. Thus
ZV {T} = τ KP{T | GV },
(4.107)
where it is operator G (the point in Grassmannian) which depends on the
shape of potential V (X). We also remind that the only way in which Z
depends on the size of the matrix n is through the domain of variation of
the time variables T. If (4.104) is extended to full Toda-lattice τ-function,
by introduction of negative times, we get [36]:
ZV {T, N, ¯T} = C−1
V (Λ)
(detΛ)N e−P
k>0 ¯TktrΛ−k×
×
Z
n×n dX(detX)N exp

−trV (X) + trΛX +
X
k>0
¯TktrX−k


(4.108)
100
When this extended partition function is considered as KP τ-function, we
have instead of (4.104):
ZV {T, N, ¯T} =
1
(detΛ)N
detγδϕ{ ˆV }
γ+N(λδ)
∆(λ)
,
(4.109)
and relevant ϕ-functions are
ϕ{ ˆV }
γ+N(λ) =
1
√
2πe−λV ′(λ)+ ˆV (λ)q
V ′′(λ)
R xγ−1e−ˆV (x)+V ′(λ)xdx =
= λN+γ−1(1 + O(λ−1)),
(4.110)
with
ˆV (x) ≡V (x) −N log x −
P
k>0 ¯Tkx−k,
V (x) = ˆV+(x)
(4.111)
(where ˆV+(x) is the positive-power fragment of Laurent series ˆV (x)). Func-
tions ϕγ(λ) in (4.105) are just equal to ϕ{ ˆV }
γ
(λ)

 ¯T=0.
4.8
String equations and general concept of reduction
The role of string equation is to ﬁx the point G in the universal module
space (UMS), associated with the particular matrix model, so that partition
function, considered as a function of time variables, will appear as the cor-
responding τ-function of a ﬁxed shape. In this sense the idea behind the
string equation is exatly the same as reduction of integrable hierarchies. The
diﬀerence is that linear reductions, as deﬁned in the section 4.5 above, are
not enough to ﬁx G unambiguously: they just specify certain subsets in the
Grassmannian, which are still inﬁnite-dimensional. The reason, why these
are usually linear reductions that are considered in the conventional theory of
integrable hierarchies, is that they are associated with the simplest possible -
Kac-Moody - subalgebras in the entire GL(∞). String equations, even their
simplest examples, are usually fragments of more complicated - Virasoro and
W-algebras, and are in fact considerably more restrictive. Moreover, string
equation is usually a distinguished fragment, because it usually belongs to the
Virasoro component of Ward identities, and Virasoro is still a Lie subalgebra
in GL(∞). This is what makes the problem of string equations very similar
to the ”classical” one with linear reduction.
101
More speciﬁcally, in order to include string equations (and in fact the en-
tire set of Virasoro - but not W - constraints) into consideration of reduction
it is enough to allow the coeﬃcients in (4.40) to depend on t and ¯t, without
changing the order of time-derivatives. Of course, there are no obvious rea-
sons to think that any point G in the UMS can be selected by imposing this
kind of linear-derivative constraints on τ-function, - and further investigation
can require essential generalization of such restricted notion of string equa-
tion. However, some of the eigenvalue matrix models are already known to
possess string equations of such simple type, associated with Virasoro sub-
algebras of GL(∞). We do not go into details of the general theory - it is
far not completed yet, - but instead present several examples of how string
equations arise in particular matrix models. These examples can illustrate
also the simpliﬁcations arising when only string equations and not the entire
sets of Ward identities need be derived. In particular, it is clear that in cases
when τ is represented as DetijHij, a linear diﬀerential equation imposed on
Hij will give rise to a similar equation on τ itself. Most of known string equa-
tions can be derived with the help of this technical idea. They are usually
associated with invariance of integrals under constant shifts of integration
variables δh = const in scalar-product and other discrete models, and with
the action of operator tr
∂
∂Ltr in GKM. For somewhat more involved ideas,
associated with string equations see [94].
Scalar-product models. String equation can be easily deduced for very
speciﬁc type of measures dˆµh,¯h. Since integral
Hij =
Z
hi¯hjeU(h)+ ¯U(¯h)dµh,¯h
(4.112)
is invariant under the shift of integration variable δh = const,
Z
hi¯hjeU(h)+ ¯U(¯h)dˆµh,¯h
"
ih−1 + ∂U(h)
∂h
+ ∂
∂h log(dˆµh,¯h)
#
= 0,
(4.113)
or
iHi−1,j +
X
k>0
ktk
∂
∂tk−1
Hij +
"
S
 ∂
∂t, ∂
∂¯t
!#
ij
= 0.
(4.114)
String equation arises straightforwardly, when operator S is linear. This is
true, if log(dˆµh,¯h) ∼hf(ˆh) with any function f(h). If the measure dˆµh,¯h is
102
also required to be symmetric in h and ¯h, we obtain conventional 2-matrix
model as the only example:
dˆµh,¯h = ech¯hdhd¯h.
(4.115)
Equation for Hij is:

X
k>0
ktk
∂
∂tk−1
+ c ∂
∂¯t1

Hij = −iHi−1,j.
(4.116)
Its implication for ˆτN is:

X
k>0
ktk
∂
∂tk−1
+ c ∂
∂¯t1

ˆτN = 0,
(4.117)
since the r.h.s. of (4.116) does not contribute to determinant (the entries in
the i-th row are proportional to those in the i −1-th row).
In particular case of 1-matrix model c = 0, and we recognize the lowest
Virasoro constraint L−1ˆτN = 0. Traditionally the name of string equation is
given not to L−1-constraint itself, but to its t1-derivative:
∂
∂t1(L−1ˆτN) = 0.
For 2-matrix model (4.117) is the lowest (m = 1, n = 0) component of
the Ward identities
 ˜W (m+1)
n−m (t) −(−)m+ncn+1 ˜W (n+1)
m−n (¯t)

ˆτN = 0. Of course,
there is also a similar equation with t ↔¯t.
Multicomponent (conformal) models. The crucial feature of these mod-
els is that intermatrix interaction, when rewritten in terms of eigenvalues,
usually contains only diﬀerences h(α)
i
−h(β)
j
. Thus there is usually covari-
ance under simultaneous shift of all eigenvalues δh(α)
i
= const by a same
constant. This gives rise to a string equation of the form
 X
α
L(α)
−1
!
τN = 0.
(4.118)
See [39] for details.
Generalized Kontsevich Model.
In order to derive string equation one should act on partition function
ZV {Tk = 1
ktrΛ−k} = C−1
V FV {L = V ′(Λ)} with operator tr
∂
∂Ltr = tr
1
V ′′(Λ)
∂
∂Λtr .
We can rewrite the result of this action in terms of time-derivatives,
tr ∂
∂Ltr
log ZV {T} = −
X
k>0
 
tr
1
V ′′(Λ)Λk+1
! ∂
∂Tk
log ZV {T}.
(4.119)
103
Alternatively we can use the fact that tr ∂
∂Ltr
=
X
γ
1
V ′′(λγ)
∂
∂λγ
, l = V ′(λ),
and explicit expression for ZV in terms of eigenvalues (Miwa coordinates),
ZV ∼etrV (Λ)−trΛV ′(Λ)
sY
γ
V ′′(λγ) det ˆϕγ(λδ)
∆(λ)
∼
∼det ϕγ(λδ)
∆(λ)
,
(4.120)
to get:
 
tr ∂
∂Ltr
!
log ZV {T} =
= 1
2tr V ′′′(Λ)
(V ′′(λ))2 + 1
2
X
γ>δ
V ′′(λγ) −V ′′(λδ)
λγ −λδ
·
1
V ′′(λγ)V ′′(λδ)−
−trΛ +
X
β
∂
∂lβ
log detγδ ˆϕγ(lδ).
(4.121)
Comparison of these two expressions gives:
L(V )
−1 ZV
ZV
≡1
ZV

X
k>0
 
tr
1
V ′′(Λ)Λk+1
! ∂
∂Tk
+
+1
2
X
γ>δ
V ′′(λγ) −V ′′(λδ)
λγ −λδ
·
1
V ′′(λγ)V ′′(λδ) −
∂
∂T1

ZV =
= −∂
∂T1
log ZV + trΛ −
X
β
∂
∂lβ
log detγδ ˆϕγ(lδ).
(4.122)
One can show that the r.h.s. is equal to zero, and thus the string equation
arises in the form
L(V )
−1 ZV = 0.
(4.123)
If potential is monomial, Vp = Xp+1
p+1 , then rk = −
p
p+1δk,p+1 and
LVp
−1 →L−p ≡
≡1
p

X
k>0
(k + p)(Tk+p + rk+p) ∂
∂Tk
+ 1
2
p−1
X
k=1
k(p −k)TkTp−k

.
(4.124)
104
The technical idea behind the proof [30] is to represent
∂
∂T1
log ZV = ResZV {Tk +
1
kλk}dλ
ZV {Tk}
,
(4.125)
and make use of the second determinant representation in (4.120) both in
the denominator and the numerator:
∂
∂T1
log ZV = Res
dλ
Qn
γ=1(λ −λγ) ·
det
 
ϕδ(λγ)
ϕn+1(λγ)
ϕδ(λ)
ϕn+1(λ)
!
det ϕδ(λγ)
.
(4.126)
Now we recall that
ϕγ(λ) ∼λγ−1 
1 + O(λ−1)

.
(4.127)
At some moment we shall need even more: in fact
ϕγ(λ) ∼λγ−1 (1 + O(λ−2)) ,
i.e.
ϕγ(λ) = λγ−1 + cγλγ−2 + . . . ,
and cγ = 0 for any γ.
(4.128)
This is a rather delicate property of GKM, it follows from two facts: ﬁrst,
ϕ1 = 1 + O
 V ′′′′
(V ′′)2, (V ′′′)2
(V ′′)3
!
, thus c1 = 0, and second, Kac-Scwarz operator
A, deﬁned in eq.(4.106) below, does not have contributions with zero-th
power of λ, thus cγ+1 = cγ.
(For example, if V (x) =
x2
2 + ax, ϕγ(x) =
1
√
2π
R xγ−1e−1
2(x−λ)2dx = λγ−1 + 0 · λγ−2 + . . .: the dangerous terms with a
simply do not show up in the expression for ϕγ.)
After this comment we can come back to evaluation of (4.126).
The
product in denominator, which arised from the Van-der-Monde determinant,
is already proportional to λn: Qn
γ=1(λ −λγ) = λn (1 + O(λ−1)). Because of
this and the asymptotic formulas (4.127), it is clear that if determinant in the
numerator of (4.126) is rewritten as linear combination of n×n determinants
with the coeﬃcients ϕγ(λ) from the last row, only items with γ ≥n can
contribute.
There are two such items: γ = n and γ = n + 1.
In the
expansion of (n+1)×(n+1) determinant ϕn+1(λ) is multiplied by det ϕγ(λδ),
which exactly cancels with determinant in denominator, and the relevant
105
contribution is
Res
ϕn+1(λ)dλ
Qn
γ=1(λ −λγ) = cn+1 +
X
γ
λγ =
= cn+1 + trΛ.
(4.129)
The item with ϕn(λ) is
det (ϕ1(λγ) . . . ϕn−1(λγ) ϕn+1(λγ))
det (ϕ1(λγ) . . . ϕn−1(λγ) ϕn(λγ)) Res
ϕn(λ)dλ
Qn
γ=1(λ −λγ).
(4.130)
The remaining residue is just unity. Determinant in the numerator diﬀers
from the one in denominator by substitution of the colomn with entries
ϕn(λγ) for that with ϕn+1(λγ).
At last we can return to eq.(4.122) and recall that ∂
∂l ˆϕγ(l) = ϕγ+1(l), thus
X
β
∂
∂lβ
log detγδ ˆϕδ(lγ) =
det ( ˆϕ1(lγ) . . . ˆϕn−1(lγ) ˆϕn+1(lγ))
det ( ˆϕ1(lγ) . . . ˆϕn−1(lγ) ˆϕn(lγ)) ,
(4.131)
what is just the same as (4.130), since ˆϕδ diﬀer from ϕδ by δ-independent
factor of eV (λ)−λV ′(λ)q
V ′′(λ). Thus we conclude that the r.h.s. of (refsteqend)
is equal to −cn+1, which actually vanishes, as was explained several lines
above.
Two things deserve paying attention in this derivation. First, it was ab-
solutely crucial that we had
∂
∂T1 log ZV at the r.h.s. of (4.122) to make it
vanishing, and therefore
∂
∂T1 immedeately appears in the expression for the
L(V )
−1 operator at the l.h.s. (this is the origin of rk-corrections in (4.124). Sec-
ond, the result is both simple and natural, but the proof is full of technical
details and looks somewhat artiﬁcial. It becomes even more involved, when
the general formula (4.136) for Tk-derivatives of ZV with 1 ≤k ≤p [40] is
derived, which plays an important role in the theory of GKM and its appli-
cations to the theory of quantum gravity. The proof of the string equation is
just a particular case of that formula, since using integral representation of
ˆϕ(l) one can represent the r.h.s. of (4.131) as
1
ZV ⟨trX⟩, where ⟨⟩now stand
for the average, deﬁned by Kontsevich integral. Thus
L(V )
−1 ZV
(4.122)
=
−∂
∂T1
ZV + ⟨trΛ −trX⟩
(4.136)
=
0.
(4.132)
106
4.9
On the theory of GKM
We remind that GKM is abbreviation for the Generalized Kontsevich model,
This theory is the naturally broad collection of topics for a separate big
section in these notes.
However, we decided not to include such detailed
presentation. This is because GKM theory seems too incomplete now. First,
we believe that the natural invariant formulation - of which existing matrix
integral is only a speciﬁc realization - is still lacking. Second, GKM is not
yet generalized enough to fulﬁl its main purpose of incorporating infromation
about all the models of 2d gravity (in fact it should include even more: the
entire theory of integrable hierarchies and geometrical quantization). Third,
though the whole approach is very conceptual and deep, many proofs, as avail-
able nowadays, are still very technical and long. All this implies, that the
proper view on the subject of GKM still needs to be found. At the moment
we could describe two complementary approaches: one, starting from inte-
gral representations, another - from the Duistermaat-Heckman (localization)
theory and Fourier analysis on group manifolds. Though intimately related,
these two approaches are still technically diﬀerent in too many respects. The
second one is more fundamental (since ordinary integrals arise from discrete
sums either in special limits or in the cases of iniﬁnite-dimensional algebras,
and, more important, since integral representation is only one of many pos-
sible ways to deﬁne the quantities of interest). However, many of the most
important results, obtained in the ﬁrst approach yet do not have their proper
names and exact counterparts in the second one. We believe that this whole
issue will be very much clariﬁed in the near future and decided to postpone
a detailed review till that time. What we can not avoid in these notes, is
giving at least a list of topics, already included in the theory of GKM, and
this is the purpose of the present subsection.
Kontsevich model with V = X3
3 was derived by Maxim Kontsevich [22]
from the original deﬁnition of topological 2d gravity, given by E.Witten [9]
in terms of generating functional for Chern classes of certain bundles over
Riemann surfaces. Generalization of this reasoning (when more bundles are
taken into consideration) leads to the theory of Landau-Ginzburg Gravity
(LGG), which is believed to be the same as GKM, though not all the proofs
are already avaliable.38
38 Intermidiate results include the study of spherical approximation to LGG, which
exhibits the structures, peculiar for ”quasiclassical integrable hierarchies” (of which Bate-
107
The crucial feature of non-perturbative partition functions, as we dis-
cussed at the neginning of section 2, is their intrinsic integrability.
For
2d gravity this general idea acquires a very concrete formulation: partition
functions are usually just τ-functions of conventional integrable hierarchies,
moreover - for LGG, associated with minimal models, these are just ordinary
multicomponent Toda hierarchies.39
M.Kontsevich found representation for generating functional in the form
of matrix integral, i.e. formulated a matrix model, which later allowed to
prove Witten’s conjecture that the functional is in fact a τ-function. The
concept of GKM as a universal matrix model, including all the information
about generic (eigenvalue?) matrix models and thus all the models of 2d(?)
gravity was introduced in [30], and the analogue of Kontsevich model with
arbitrary potential V (X), i.e. expression
ZV {T}|Tk= 1
k trΛ−k = CV (Λ)−1FV (V ′(Λ)) ∼
∼
q
detV ′′(Λ)
(2π)n2/2etr(ΛV ′(Λ)−V (Λ))
Z
n×n dXe−trV (X)+trV ′(Λ)X
(4.133)
was proposed as an intemediate step in this direction.40 This (still restricted)
version of GKM is already enough to unify all the (p, 1)-models of 2d grav-
ity. In some sense, (p, q)-models with q̸ = 1 are also included, but in a very
non-transparent way (using analytical continuation), which does not even
explicitly respect the p ↔q symmetry. Partition function of such GKM,
ZV {T} depends on two types of variables: time-variables ˆTk and potential
V . Formally these two types of variables are absolutely diﬀerent, V being
responsible for the choice of particular LGG model or, what is essentially the
same, of particular reduction of Toda-lattice or KP hierarchy; while ˆTk are
parameters of the generating functional of all correlation functions in this
man hierarchy to be brieﬂy mentioned in section 5.2 below is an example), and which
also arise in ”quasiclassical approximation” to GKM. For some results in this direction see
[95],[96],[97],[17], [40],[41] and references therein.
39One can say that this is natural: both such models and Toda hierarchies are associated
with the level k = 1 Kac-Moody algebras and corresponding simpliﬁed versions of the
WZNW model.
However, too much still remains to be clariﬁed about this ”obvious”
connection.
40 We remind that detV ′′(Λ) is deﬁned somewhat tricky, see s.2.5 above. The same
matrix integral (4.133) was also considered in refs.[98],[31],[32],[33].
108
particular model. But of course, since we deal with exact (non-perturbative)
approach, there is almost no real diﬀerence between these types of depen-
dencies - on the model (vacuum state) and on the ˆT’s: the model can be
changed by non-inﬁnitesimal shift of ˆT-variables. Technically, in GKM this
is reﬂected in the identity of the form [40]:
ZVp{T} = fp(r | ˆTk + rk) · τ{ ˆTk + rk | Gp}
(4.134)
where rk =
p
k(p−k)Res (V ′(µ))1−k
p dµ provide a speciﬁc parametrization of
potentials V , which is here assumed to be any polinomial of degree p, and fp
is some simple function:
fp(r | ˆTk + rk) = exp −1
2
X
i,j
Aij(r)( ˆTi + ri)( ˆTj + rj);
Aij = Res (V ′(µ))i/p d (V ′(µ))j/p = ∂2 log τ (p)
0
∂ti∂tj
,
(4.135)
and τ (p)
0
is a τ-function of ”quasiclassical hierarchy”. What is important,
Gp (which deﬁne the shape of the τ-function as function of ˆT + r) and fp
depend only on the degree p, but not on the other details of the shape of the
potential. This is a deep formula. It accounts for two phenomena at once:
First, it says that Z depends on the sum of ˆT and r.41 Second, dependence
on V is not quite smooth: when the degree of potential changes, the shapes of
the functions f and τ also changes abruptly. Another side of the same phe-
nomenon is that partition function ZV {T}, which in principle is well deﬁned
as a matrix integral for all choices of V and L (thus ˆT) at once, is in fact
singular at some points: there are phase transitions, manifesting the switch
41 In Miwa parametrization ˆTk =
1
ktr
 V ′
p(Λ)
−k/p. Throughout these notes we used
diﬀerent time-variables Tk = 1
ktrΛ−k, which are independent of the potential V , instead
V -dependence of ZV - which we did not really study - was rather nontrivial. If expressed
in terms of ˆT, partition function ˆZV { ˆT + r} = ZV {T } becomes almost independent of
V : it changes - abruptly - only when the degree p of potential changes. This second type
of description is of course in better accordance with the symmetries of particular model
- which are diﬀerent in diﬀerent ”vacua” (for diﬀerent p). Therefore these are variables
ˆT + r, rather than in T which arise naturally in Ward identites - as we saw in sections
2.5 and 2.6. T ’s and ˆT’s are suited for diﬀerent purposes: T ’s are nice when universality
aspects of GKM are concerned, while ˆT’s arise when speciﬁc features of particular models
(orbits, vacua) are considered.
109
from one LGG model to another. After a phase transition original integral
expression becomes sonewhat symbolical: it deﬁnes partition function only
in the sense of analytical continuation, and it is a separate problem to ﬁnd
an integral representation, adequate in the new phases. In practice, what is
nicely decribed by the integral representation GKM in the form of eq.(4.133),
are (p, 1)-models, with p + 1 being just the power of potential V (x). What
is not yet found, is analogous representation for (p, q)-models with q̸ = 1 (it
can involve multiple matrix integrals, and universal model is supposed to be
”matrix quantum mechanics in external ﬁelds”).
Derivation of the crucial formula (4.134)in any approach - starting from
GKM in the form of either LGG or matrix integrals - is still very tedious. In
matrix-model representation it relies upon identity [40]
∂ZV
∂Tk
= ⟨trΛk −trXk⟩≡
≡C−1
V
Z 
trΛk −trXk
e−trVp(X)+trV ′
p(Λ)XdX
for 1 ≤k ≤p,
(4.136)
which look trivial but are rather hard to derive. (A proof of the string equa-
tion in GKM at the end of the previous subsection is the simplest example of
this kind of exersices.) Certainly some simple derivation ”in two lines” should
exist, but it is not yet found. Formulas of this kind are very important for
all aspects of GKM theory. Besides other things, they are just necessary to
actually evaluate correlation functions in (p, 1)-models of 2d gravity, of which
ZV {T} is a generating functional. If instead of these ”physical” questions,
one asks about integrability theory, identites of this sort also play important
role. For example, looking at (4.136) for a special k = p and special choice of
potential - monomial Vp(X) = Xp+1
p+1 ,- ane can note that the r.h.s. vanishes:
this is just a Ward identity, reﬂecting invariance under the shift of the inte-
gration variable, δX = const. This is a simplest version of a more general
statement:42
if Vp(X) = Xp+1
p + 1,
then
∂ZV
∂Tpk
= 0 for all n ∈Z+.
(4.137)
42 This property was technically implicit in original Kontsevich’s work [22] for p+1 = 3,
where it was related with certain combinatorial identities. A tricky proof, relying upon
properties of τ-functions, was given for any p in [30]. An example of straightforward proof,
again for p+1 = 3, - just in terms of Kontsevich matrix integrals - can be found in ref.[99].
110
Looking from the point of view of integrable hierarchies, one immediately
recognizes (4.137) as an example of reduction condition (4.40). It corresponds
to the so called p-reduction of KP-hierarhy, of which KdV (p = 2) and
Boussinesq (p = 3) are the most celebrated examples. We refer to [30] and
[40] for all details and references, the only thing to mention here is that the
slightly weaker verison of the constraint (4.137),
∂ZV
∂Tpn
= an = const,
(4.138)
where an do not depend on any time variables, can be simply expressed in
Miwa parametrization: it is just the statement that ϕ-functions in
ZV = detγδϕγ(λδ)
∆(λ)
satisfy the p-reduction condition:
λpϕγ(λ) =
γ+p
X
δ=1
ˆVγδϕδ(λ).
(4.139)
This a restrictive relation, because ϕ’s are inﬁnite seria in 1/λ, while at th
r.h.s. in (4.139) there is only a ﬁnite number of items. In GKM it is satisﬁed
for monomial potential just as a corollary of Gross-Newman equation, or
more exact, of the Ward identity for the integral
ϕγ(λ) ∼
Z
xγ−1e−V (x)+V ′(λ)xdx.
Indeed, integral does not change under the shift δx = const, and this implies:
Z
xγ−1

V ′(x) −V ′(λ) −γ −1
x

e−V (x)+V ′(λ)xdx = 0,
i.e.
p+1
X
k=1
kvk

ϕγ+k−1(λ) −λk−1ϕγ(λ)

−(γ −1)ϕγ−1 = 0.
(4.140)
If only vp+1̸ = 0, this leads to an identity of the required form of (4.139).
This description of reduction can be modiﬁed to allow for non-monomial po-
tentials, making use of the concept of ”equivalent hierarchies”, see [100],[40]:
111
in this framework the reduction condition is
V ′(λ)ϕγ(λ) =
X
δ
Vγδϕδ, (λ),
(4.141)
but classes of essentially diﬀerent reductions are labeled by the degree of
potential only.
As we already discussed in the previous subsection, linear constraints like
(4.139) are not restrictive enough to ﬁx the shape of the τ-function (the point
G in the universal module space) unambigously: string equation should be
also imposed. If expressed in terms of ϕ’s, string equation is just the property
(4.106):
ϕγ+1 = Aϕγ,
(4.142)
where the Kac-Schwarz operator
A =
1
V ′′(λ)
∂
∂λ −1
2
V ′′′(λ)
(V ′′(λ))2 + λ.
(4.143)
It has obvious generalization of the form
Ap,q =
∂
∂V ′
p(λ) −1
2
V ′′′
p (λ)
(V ′′
p (λ))2 + Q′
q(λ),
(4.144)
where Qq(λ) is a polinomial of degree q + 1 and (4.142) is substituted be
ϕγ+q = Ap,qϕγ.
(4.145)
This generalization is naturally related to the string equation in (p.q) models,
see [41] and references therein. Generic (p, q) LGG model can be described
by a system of constraints,
(λp −Vp){ϕ} = 0,
Ap,q{ϕ} = 0,
(4.146)
where both operators Vp and Ap,q are not uniquely ﬁxed by choosing p and
q, and there is also a freedom to change variables λ →f(λ) and make
a triangular transformation of basis ϕγ →ϕγ + P
δ<γ Cγδϕδ.
Altogether
the set of equations (4.146) modulo these allowed transformations is ﬁnite -
112
(p −1)(q −1) - dimensional, this is dimension of the module space of LGG
models with given p and q. Kontsevich integral can be now used to establish
duality transformation from (p, q) to (q, p) model [41]:
ZV,Q(Λ) = C−1
V,Q(Λ)
Z
n×n dXe−trSV,Q(X,Λ)+trV ′(Λ)Q′(X)ZQ,V (X).
(4.147)
Here
SV,Q(x, λ) =
Z x
V ′(y)Q′′(y)dy =
Z x
V ′(y)dQ′(y),
(4.148)
As usual, CV,Q(Λ) is the quasiclassical approximation to the integral, and
ZV,Q(Λ) ≡
detγδϕγ(λδ)
∆(λ)
, where ϕ are solutions to (4.146) with Vp and Ap,q
deﬁned by eqs.(4.141) and (4.144) respectively.43
This relation does not
provide any formula for ZVp,Qq(Λ) unless q = 1.
The case of q = 1 is
distinguished because ZQ1,Vp is trivial. Indeed, the 1-reduction constraint
λϕγ = ϕγ+1 +
P
δ≤γ Vγδϕδ, implies that detγδϕγ(λδ) = ∆(λ)
Q
δ ϕ1(λδ), thus
ZQ1,Vp = exp P
k akTk, what is essentially the same as ZQ1,Vp = 1,44 and
(4.147) is just our old formula (4.133) for the (p, 1) version of GKM. (In
fact Q1(X) ∼X2, and ZQ1,Vp is nothing but Gaussian Kontsevich model. It
is trivial when the ”zero-time” N = 0, as we assume here.) Matrix model
realization of ZVp,Qq for q̸ = 1 is yet unknown.
This is not the only important further generalization of GKM (4.133).
Another one is implied by the formula for FV in terms of eigenvalues from
the section 3.3,
FV ∼
n
Y
γ=1
Z
dxγe−V (xγ)∆2(x)I(x, l).
(4.149)
43 Also expression for rk-variables is now modiﬁed:
rk =
p
k(p −k)Res(V ′
p(µ))1−k/pdQ′
p(µ),
For monomial Vp and Qq rk = −
p
p+q δk,p+q.
44 Since ϕ1(λ)
=
1 + P
k>0 bkλ−k,
log ϕ1(λ)
=
P
k>0
ak
k λ−k, and the sum
P
δ log ϕ1(λδ) = P
k>0
ak
k
 P
δ λ−k
δ

= P
k>0 akTk. Addition of any linear combination
of time-variables to log τ does not essentially change τ-function. For example, the ordi-
nary integrable equations (like KdV or KP) are usually written in terms of variables like
u =
∂2
∂T1 log τ, which are second derivatives of log τ.
113
As it was already mentioned in section 3.3, the Itzykson-Zuber integral
I(x, l) ∼
Z
[DU]etrUXU†L ∼detγδexγlδ
∆(x)∆(l)
(4.150)
is in fact a coadjoint orbit integral and has group theoretical interpretation:
under certian conditions it turns into a character χR(g) = TrRg of the group
GL(n). Here g ≡eL is considered as a group element, representation R is
labeled by integer-valued parameters m1, . . . , mn - essentially the lengths of
rows in the Young diagramm. Exact statement is:
I(m, l) · ∆(l)
∆(g) =
detγδgmδ
γ
∆(m)∆(g) = χR(g)
dR
,
(4.151)
i.e. in order to get a character we should integrate over matrices X with
integer-valued eigenvalues.45
Dimension dR of representation can be also
expressed in terms of m-variables: dR = ∆(m). As to the traces trXk =
P
γ xk
γ →
P
γ mk
γ, which appear in the action of GKM, they are very similar
to the k-th Casimir eigenvalue Ck(R) (though is not exactly the same). Thus
we see that the integral in (4.149) is in fact very similar to
F qu
V {g, ¯g} ≡
X
R
χR(¯g)χR(g)e−P∞
k=0 vkCk(R),
(4.152)
evaluated at the point ¯g = I. The only real diﬀerence is that instead of
the integral we have a sum over discrete values of m (sum over all the rep-
resentations, or a model of GL(n)). This ”discretized” (quantum?) GKM
is more general that the continuum one which can be obtained by various
limiting procedures. It is now obvious that the theory of discretized GKM
largely overlaps with that of 2d Yang-Mills theory. The simplest ingredient
45 The ratio
∆(l)
∆(g) =
Y
γ>δ
lγ −lδ
elγ −elδ
is the usual correction factor, which is the price for the possibility to reduce quantum-
mechanical problem of motion on the orbit to a single matrix integral. The full problem
of matrix quantum mechanics can and should be considered as a multi-matrix (in fact,
inﬁnite-matrix) generalization of GKM (4.133), which incorporates all the (p, q) LGG
models.
114
of this theory is the classical result [101], that GL(N) characters are in fact
(singular) Toda-lattice and KP τ-functions. Moreover, the entire sum at the
r.h.s. of (4.152), if considered as a function of Tk =
1
ktrgk, ¯Tk =
1
ktr¯gk is
in fact a Toda-lattice τ-function. There are also features parallel to (4.134).
We refer to [102] for a little more details about discretized GKM (see also a
recent paper [81]). This is one more very important direction of the further
investigation of GKM.
4.10
1-Matrix model versus Toda-chain hierarchy
At the end of this section we use an explicit example of dicrete 1-matrix model
[26] to illustrate, how a more familiar Lax description of integrable hierarchies
arises from determinant formulas. This example will be also usefull in Section
5.3 below, when one of the ways to take double-scaling continuum limit of the
1-matrix model will be discussed. Lax representation appears usually after
some coordinate system is chosen in the Grassmannian. In the example which
we are now considering this system is introduced by the use of orthogonal
polinomials.
We already know from section 3.6, that partition function of 1-matrix
model (which is a one-component model) is given by
ZN = Det0<i,j≤N⟨hi | hj⟩=
N−1
Y
i=0
eφi = Z1
N−1
Y
i=1
RN−i
i
,
(4.153)
where the last two representations are in terms of the norms of orthogonal
polinomials
⟨Qn | Qm⟩= eφnδnm
(4.154)
and parameter of the 3-term relation
hQn(h) = Qn+1(h) + cnQn(h) + RnQn−1(h),
Z1 = eφ0 = ⟨1 | 1⟩,
Rn = eφn−φn−1.
Of course all the information is contained in the determinant formula together
115
with the rule, which deﬁnes time-dependence of Hf
ij = ⟨hi | hj⟩= ˆHf
i+j:
∂Hf
ij
∂tk
= Hf
i+k,j = Hf
i,j+k,
or
∂ˆHf
i
∂tk
= ˆHf
i+k.
(4.155)
(The possibility to express everything in terms of Hf
i with a single matrix
index i is the feature of Toda-chain reduction of generic Toda-lattice hierar-
chy.)
However, in order to reveal the standard Lax representation we need
to go into somewhat more involved considerations.
Namely, we consider
representation of two operators in the basis of orthogonal polinomials. First,
hkQn(h) =
n+k
X
m=0
⟨n | hk | m⟩
⟨m | m⟩
Qm(h) =
n+k
X
m=0
γ(k)
nmQm(h)
(4.156)
(here the simpliﬁed notation is introduced for ⟨n | f(h) | m⟩≡⟨Qn | f(h) |
Qm⟩and γ(k)
nm ≡⟨n | hk | m⟩
⟨m | m⟩
.) Second,
∂Qn(h)
∂tk
= −
n−1
X
m=0
⟨n | hk | m⟩
⟨m | m⟩
Qm(h) = −
n−1
X
m=0
γ(k)
nmQm(h),
∂φn
∂tk
= ⟨n | hk | n⟩
⟨n | n⟩
= γ(k)
nn .
(4.157)
(These last relations arise from diﬀerentiation of orthogonality condition
(4.154):
eφn ∂φn
∂tk
δnm = ∂⟨Qn | Qm⟩
∂tk
=
= ⟨∂Qn
∂tk
| Qm⟩+ ⟨Qn | ∂Qm
∂tk
⟩+ ⟨Qn | hk | Qm⟩
by looking at the cases of m < n and m = n respectively.)
From these relations one immediately derives the Lax-like formula:
∂γ(k)
nm
∂tq
= −
n−1
X
l=m−k
γ(q)
nl γ(k)
lm +
n+k
X
l=m+1
γ(k)
nl γ(q)
lm
(4.158)
116
or, in a matrix form,
∂γ(k)
∂tq
= [Rγ(q), γ(k)],
(4.159)
where
Rγ(k)
mn ≡
(
−γ(k)
mn if m > n,
γ(k)
mn if m < n
(4.160)
(We remind that usually R-matrix acts on a function f(h) =
P+∞
n=−∞fnhn
according to the rule: Rf(h) = P
n≥l fnhn −P
n<l fnhn with some ”level”
l.) These γ(k) are not symmetric matrices, but one can also rewrite all the
formulas above in terms of symmetric ones:
L(k)
mn ≡e
1
2(φn−φm)γ(k)
mn =
⟨m | hk | n⟩
q
⟨m | m⟩⟨n | n⟩
(4.161)
From eqs.(4.158) one can easily deduce Toda-equations for φn:
∂2φn
∂tk∂tl
= ∂
∂tk
⟨n | hl | n⟩
⟨n | n⟩
=
=
 X
m>n
−
X
m<n
! ⟨n | hk | m⟩⟨m | hl | n⟩
⟨m | m⟩⟨n | n⟩
,
(4.162)
where the r.h.s. can be expressed in terms of Rm = eφm−φm−1. In particular,
∂2φn
∂t1∂t1
= Rn+1 −Rn = eφn+1−φn −eφn−φn−1.
(4.163)
Let us also mention that in this formalism the Ward identities (Virasoro
constraints) follow essentially from the relation
 ∂
∂h
!†
= −∂
∂h −
X
k>0
ktkhk−1,
(4.164)
where Hermitean conjugation is w.r.to the scalar product ⟨| ⟩. For example,
this relation implies, that
⟨Qn | ∂Qn
∂h ⟩= −⟨∂Qn
∂h | Qn⟩−
X
k>0
ktk⟨Qn | hk−1 | Qn⟩.
(4.165)
117
Now we note that ∂Qn
∂h is a polinomial of degree n −1, thus ⟨Qn | ∂Qn
∂h ⟩= 0.
(In fact
∂Qn
∂h = −
X
k>0
ktk
 n−1
X
m=0
γ(k−1)
nm
Qm
!
= −
X
k>0
ktk
∂Qn
∂tk−1
.)
Also we recall that ⟨Qn | hk−1 | Qn⟩= ⟨Qn | Qn⟩∂φn
∂tk−1, and obtain:
X
k>0
ktk
∂φn
∂tk−1
= 0
(4.166)
for any n. This should be supplemented by relation ∂φn
∂t0 = φn. In order to get
the lowest Virasoro constraint (string equation), L−1ZN = 0 or L−1 log ZN =
0 it is enough just to sum over n from 0 to N −1.
For more details about 1-matrix model, Toda-chain hierarchy and appli-
cation of the formalism of orthogonal polinomials in this context see [26].
5
Continuum limits of discrete matrix mod-
els
5.1
What is continuum limit
Continuum limit of matrix models is, of course, the crucial issue for their
physical applications whenever these models are interpreted as discrete (lat-
tice) approximations to continuum theory. The very ﬁrst thing to be kept
in mind is that it is not the only possible view on matrix models. Another
approach considers them as describing topological (and thus also in a certain
sense ”discrete”) properties of the theory. Such models, when appearing in
the ﬁeld of, say, quantum gravity (which after all is a sort of a pure topological
theory) do not require any continuum limit to be taken: their discrete nature
(occurence of integer-valued matrix indices) reﬂects not the discrete approx-
imation to the space-time (which does not really exist in quantum gravity),
but rather the essential discreteness of the underlying structures: topology of
the module spaces of geometries. Example of matrix models which allow for
118
this kind of interpretation - in terms of topology of module spaces of bundles
over Riemann surfaces - is provided by Kontsevich models, and this is why
they usually do not require any continuum limit and why we once called them
”continuous matrix models” in the Introduction to these notes. The models
which are usually interpreted in more traditional way - as lattice theories
- are represented by our ”discrete” models, the 1-matrix, conventional and
”conformal” multimatrix models being included into this class. More sophis-
ticated examples are provided by ”c = 1”-theories, Kazakov-Migdal model
and, say, Wilson’s QCD (and inﬁnetely many other lattice theories). It is not
a surprise that continuum limits of some discrete models provide the theories
of Kontsevich type: this happens whenever continuum theory is supposed to
have a kind of topological nature. This is usually the case for quantum grav-
ity (which, as we said, is conceptually a topological theory in the ”module
space of geometries” - the notion which is already made more or less explicit
in the 2d case), but in principle this can be also true for many other theories,
including exhaustive quantum theory of Yang-Mills ﬁelds (again there is al-
ready considerable progress in this direction, as soon as 2d Yang-Mills model
is concerned). There should not be confusion about the presence of gauge
particles in dimensions greater than 2 (for Yang-Mills) and 3 (for gravity):
there is no reason to prevent generic topological theory from possessing con-
tinuum spectrum of excitations, though explicit analogue of Kontsevich-like
description of such situations is not yet found (as we mentioned many times,
it should probably rely upon non-eigenvalue models).
We shall not discuss the non-trivial history of invention and understand-
ing of all these notions (the crucial steps being discovery of the ”multiscaling
continuum limits” [19],[20], which preserve integrable structure of discrete
models in continuum case; hypothesis of equivalence of quantum and topo-
logical 2d gravities [9] and its proof [23],[24], provided by discovery of Kont-
sevich models [22] as a peculiar and powerful tool for description of topology
of the module spaces). Instead, following the mean line of these notes, we
shall concentrate on intrinsic relation between (multiscaling) continuum lim-
its and integrability: the notion of continuum limits is in fact built into the
theory of integrable hierarchies and the underlying representation theory of
Kac-Moody algebras.
In the case of the eigenvalue models the central issue here is the interrela-
tion between Toda-lattice and KP hierarchies, even its more narrow aspect:
elimination of the zero-time N, present in the Toda-lattice case. From rep-
119
resentation theory (or conformal ﬁeld theory, what is essentially the same)
point of view the thing is that the zero-time (which labels the ﬁlling level
of Dirac sea in the fermionic picture) is associated with the zero-modes of
scalar ﬁeld and its elimination is just the change of boundary conditions
which eliminates zero-modes. The simplest example of this ”twisting” pro-
cedure is just transformation from periodic to antiperiodic scalars - it still
preserves possibility to have fermionic description (where it looks like a switch
from Ramond to Neveu-Schwarz sector), and thus does not take us out of
the ﬁeld of conventional integrable hierarchies. In representation theory one
can interpret the same operation just as a switch from the homogeneous to
principal representation, which are associated with the Toda-lattice and KP
hierarchies respectively.
This remarkably simple description is of course far from obvious, if one
investigates continuum limit in naive way, without taking integrable structure
into account explicitly, but just sending the number of degrees of freedom in
discrete theory (i.e. the matrix size N) to inﬁnity (together with the inverse
lattice spacing, if any). We refer to the classical review [18] for discussion
of what are the naive continuum limits in lattice gauge theories, i.e. what
are the conditions for getting the second-order phase transitions, which allow
for a continuum-like scaling behavious in the vicinity of the critical point,
with critical exponents deﬁning all the continuum physics, from quantum
dimesnion of the space-time to spectrum of particles.
The problem with
naive continuum limits is that they can easily destroy integrable structure of
the theory (the underlying hidden symmetries), unless special precaution is
taken: the critical point (which is in fact a low-codimensional hypersurface
in the inﬁnite-dimensional space of parameters) should be approached from
the certain directions, so that Ward identities are not explicitly broken.
As soon as this word - Ward -dentities - is pronounced, we already get into
the ﬁeld of integrable systems and the issue can be discussed inside this ﬁeld.
The above-mentioned switch from periodic to antiperiodic ﬁelds is of course
apparent if the discrete and continuos Virasoro constraints (represented by
formulas (1.2) and (1.3) in the Introduction) are compared, but this is a
posteriori information, because so far we interpreted ”continuous Virasoro
constraints” as the Ward-identities for the V = X3-Kontsevich model, and
it still remains to be explained why Kontsevich model is indeed what arises
after continuum limit is taken. The simplest approach to this problem is
to make use of the identity between discrete 1-matrix model and Gaussian
120
Kontsevich model [56], established in section 3.8 above. Then the X3-model
arises in the large-N limit just when the matrix integral is evaluated by the
steepest descent method [36]. We shall present this simple calculation in
the last subsection below, but before we take a somewhat more direct (and
complicated) approach in order to reveal at least some of ideas, underlying
the entire theory of continuum limits.
5.2
From Toda-chain to KdV
We begin with the simplest existing example: continuum limit, in which the
lowest equation of the ”Volterra hierarchy”,
∂Rn
∂t
= −Rn(Rn+1 −Rn−1),
(5.1)
turns into the lowest KdV equation:
∂r
∂T3
= −1
3r′′′ −2rr′.
(5.2)
Volterra hierarchy is a reduction of Toda-chain hierarchy, with Rn = eφn−φn−1,
arising when all the odd-times t2k+1 = 0 and all φn are supposed to be inde-
pendent of them. Therefore this hierarchy is clearly related to the discrete
1-matrix model.
We”ll turn to the study of 1-matrix model in the next
subsection, but here we just address the transformation from (5.1) to (5.2)
[103],[26].
The basic idea of taking continuum limit is to change discrete ”zero-time”
n for continuum variable x (to be after all substituted by T1 of the continuous
hierarchy). In other words, the idea is to consider a subset of functions Rn,
which satisfy Volterra equation and depend on n very smoothly, so that
they can actually be substituted by a smooth function R(x). This is a very
natural thing to do, of course, when one is interested in the large-n limit of
the equation. Namely, one substitutes (5.1) by
∂R(x)
∂t
= −R(x)(R(x + ǫ) −R(x −ǫ)),
(5.3)
and take the limit ǫ →0, which, after rescaling x →ǫx, gives rise to ”Bate-
man equation”,
∂R(x)
∂t
= −R(x)R′(x).
(5.4)
121
This is a very interesting equation (see [104] for description of the amusements
of the related theory, which is in fact intimately related to the theory of
jets). However, it is much simpler that KdV equation (for example, it is
completely integrable in the most trivial sense of the word: entire set of
solutions, satisfying any boundary conditions can be immediately written
down, see [104]). KdV equation can be considered as a sort of ”quantization”
of (5.4) (unfortunately this very interesting subject did not yet attract enough
attention and is not studied well enough).
Remarkably, Bateman equation is not the only possible limit of Volterra
equation: a ﬁne tuning procedure (”double-scaling limit”) exist, which can
provide less trivial - KdV - equation [103]. Indeed, imagine, that in contin-
uum limit Rn tends to a constant R0, and the function r(x) arises only as
scaling approximation to this constant: R(x) = R0(1 + ǫsr(x)). Then the
leading term at the r.h.s. of (5.4) is ǫRR′(x) = −2ǫsr(x)(1 + O(ǫ2, ǫs)), and
instead of (5.4) we would get:
∂r
∂t = −2ǫR0r′(x)((1 + O(ǫ2, ǫs)).
This equation is even simpler that (5.4) - it is just linear, but in fact it is too
simple to preserve its form: by a simple change of variables46
˜x = x −2ǫR0t,
(5.6)
˜t = ǫ3R0t
(5.7)
it can be transformed into
∂r
∂˜t = ǫ−2O(ǫ2, ǫs),
and terms at the r.h.s. also deserves beeing taken into account. Then we
get:
∂r(x)
∂t
= −2ǫR0

1 + ǫsr(x))(r′(x) + 1
6ǫ2r′′′(x) + O(ǫ4)

=
= −2ǫR0

r′(x) + 1
6ǫ2r′′′(x) + ǫsrr′(x) + ǫ2O(ǫ2, ǫs)

46 This change of variables is implied by the relation:
∂
∂t + 2ǫsR0
∂
∂x =
∂˜t
∂t + 2ǫsR0
∂˜t
∂x
 ∂
∂˜t +
∂˜x
∂t + 2ǫsR0
∂˜x
∂x
 ∂
∂˜x = ∂
∂˜t.
(5.5)
122
and, after the change of variables (5.7),
∂r(˜x)
∂˜t
= −1
3r′′′(˜x) −2ǫs−2rr′(˜x) + O(ǫ2, ǫs).
It is now clear, that the choice s = 2 is distinguished (a critical point) and
at this point we get:
∂r
∂T3
= −1
3
∂3r
∂T 3
1
−2r ∂r
∂T1
,
(5.8)
where new notation T1 and T3 is introduced for ˜x and ˜t respectively. This is
already the KdV equation (5.2), and our conclusion is:
While the naive continuum limit of Volterra equation is just a simple
Bateman equation, the scaling limit can be ﬁne tuned so that KdV equation
arises instead. The crucial ingredient of this adjustement is the change of
time-variables {t} −→{T}, which involves singular parameter ǫ. The proce-
dure can be easily generalized to the entire Volterra hierarchy, and ﬁne tuning
allows to get the entire KdV hierarchy in the limit of ǫ →0. Usually trans-
formation to the ”Kazakov variables” {T} (they are a little diﬀerent from
those originally introduced by V.Kazakov in [19]) from {t} is some linear
triangular transformation.
An important detail is that this procedure requires restriction to only
even time-variables t2m, m ≥0.
(If odd times are also involved, a pair
of KdV hierarchies arises in the continuum limit - this is not a ”minimal”
case.) Thus ”irreducible” realization of continuum limit requires reduction
of original hierarchy. This can be also seen from the fact that the lowest
KdV equation arises from the lowest Volterra equation, which is related to
the second eqaution of Toda-chain hierarchy.
Unfortunately this simple piece of theory (continuum limits in terms of
hierarchies) has never been worked out in full details (for the entire Toda-
lattice hierarchy, its multicomponent generalizations and their reductions).
As we already mentioned, this theory will involve the general relation between
homogeneous and principal representations of the (level k = 1) Kac-Moody
algebras.
5.3
Double-scaling limit of 1-matrix model
Now we proceed to discussion of a slightly diﬀerent approach to continuum
limits, which is directly adjusted to the needs of matrix models. The naive
123
idea [20],[29] is to forget about integrability and just look at the Ward identi-
ties (Virasoro constraints in the 1-matrix case) and take a continuum limit of
these identities. This approach makes close contact with the standard tech-
nique of ”loop equations” (Makeenko-Migdal equations [105]) in the theory
of matrix models, of which Virasoro and W-constraints are just particular
examples.47
However, carefull analysis of continuum limit of discrete Virasoro con-
straints [28] makes it clear that the procedure is far less simple than one can
think in advance (usually derivations are not very carefull and details are
just ”put under the carpet”). The crucial problem is that we want peculiar
(double scaling) rather than naive limit, and, as we mentioned in the pre-
vious subsection, this also requires a certain reduction (elimination of the
odd-times t2m+1). If parity symmetry (w.r.to the change of H →−H in the
original matrix integral) is taken into account, one can easily throw away
ﬁrst derivatives w.r.to the odd-times t2m+1, just because
∂ZN
∂t2m+1

t2k+1=0
= 0,
but this is no longer true as far as the second derivatives
∂2ZN
∂t2m+1∂t2l−1

t2k+1=0
are concerned, which appear in (the ”quantum piece” of) the Virasoro con-
straints (1.2). It is a highly non-trivial feature of loop equations (having its
origin in their integrable structure!), that in continuum limit these terms can
be in fact carefully eliminated. The thing is that the second derivatives of
log ZN appear to be a local objects, in the sense that they depend only on
Z ˜
N with the diﬀerence | ˜N −N |≤m+ l, which does not blow up as N →∞
in continuum limit. Moreover, the diﬀerences
∂2 log ZN
∂t2m+1∂t2l−1
−∂2 log ZN
∂t2m∂t2l
al-
most tend to zero, leaving some simple (though vitaly important) correction
to arising continuous loop equations. This locality property allows one to
get rid of these dangerous odd-time derivatives, substituting them just by
second derivatives w.r.to the even-times. Since such substitution is possi-
47One of the puzzles in the theory of non-eigenvalue models is to identify group-
theoretical meaning of generic loop equations: they are usually introduced as equations of
motion rather than as Ward identities (see discussion at the beginning of Section 2 above),
and thus their implications are more obscure and technical means to deal with them are
much more restricted. When group theory description will be found, it will very soon
reveal the (generalized) integrable structure of non-eigenvalue models and it will be a big
step forward in the whole theory.
124
ble only for logarithms of ZN, continuous constraints appear imposed on the
square root of original partition function (or on the 1
p-th power in the case of
the p −1-component conformal models). Another aspect of this trick to deal
with the odd-time derivatives is that it makes the entire derivation depend-
ing on the fact that the theory is integrable - this is what guarantees the
above-mentioned locality. Since the way to reveal integrability, by looking
at the loop equations themselves is yet not very well understood, the whole
calculation becomes not quite self-contained (but of course, if we know ev-
erything about integrable structure this is not a real drawback, this is just
a limitation of particular approach, starting from the loop equations) . In
particular, this is the only loophole, which is still not ﬁlled in the description
of continuum limit of conformal (multi-component) matrix models, which in
all other respects goes in exactly in parallel with the 1-component (1-matrix)
case.48
We shall now describe brieﬂy the steps of this calculation for the 1-matrix
model, refering for all the details to refs.[28] and [45]. Our previous discussion
already contain motivations for the main steps, so we do not need to go into
detailed explanations.
Manipulations below, involving Kazakov variables
can look a little artiﬁcial, but we repeat that they can be interpreted as a
switch from the Toda-type to KP-type hierarchies, which, as we already saw
in the previous subsection, is naturally associated with the double-scaling
continuum limit.
We start from the discrete Virasoro constraints (1.2), rewritten in terms
of a generating functional (”stress tensor” on the spectral plane):
L−(z)ZN = 0,
(5.9)
where
L−(z) =
∞
X
n≥−1
Lnz−n−2 = 1
2

J2(z)

−,
(5.10)
48 It transforms discrete W-constraints into continuum W-constraints, which in their
turn arise from the GKM with the appropriate potential [30], [55]. Unfortunately, since
the GKM-inteprpretation of discrete multicomponent models (like the one existing in the
1-matrix case, see s.3.8) is yet unknown, the direct way to take their continuum limit
- like the one to be described in the next subsection for the 1-matrix case - is also yet
unavailable. For more details about conformal matrix models, their integrable structure
and continuum limits see refs.[39].
125
and
J(z) = ∂φ(z) =
∞
X
n=−∞
Jnz−n−1;
φ(z) = 1
√
2
X
k≥0
tkzk −
√
2
X
k>0
z−k
k
∂
∂tk
;
J−k =
√
2 ∂
∂tk
;
Jk = 1
√
2ktk,
k ≥0;
∂
∂t0
ZN = NZN.
(5.11)
Next, we need to reduce the original partition function:
ZN{t} −→Zred
N {teven} ≡ZN{todd = 0, teven}.
(5.12)
All odd virasoro generators L2n+1 act trivially on Zred
N , since ∂ZN
∂t2k+1

todd=0
= 0,
and we need to consider only L2n. Introduce also49
φred(z) ≡
1
√
2
P
k≥0 t2kz2k −
√
2 P
k>0
z−2k
k
∂
∂t2k ;
Lred(z) = 1
2

∂φred(z)
2 ;
Lred
2n ≡P
k>0 kt2k
∂
∂t2k+2n + Pn
k=0
∂2
∂t2k∂t2n−2k .
(5.13)
Now we have two issues to be discussed separately. The ﬁrst one is the
change from t2k to Kazakov variables T2m+1. The second is the diﬀerence
between constraints imposed on Zred and Z.
49 Note that φred(z)̸ = φ(z)

todd=0 and similarly Lred
2n (z)̸ = L2n

todd=0: some factors of
2 in (5.13) being responsible for this discreapancy. In fact Lred are related to generators
of the Virasoro constraints in the complex-matrix model [28],
ZC
N =
Z
dM exp

X
k≥0
t2kTr(MM †)k


and in continuum limit ZC
N ∼
q
Zred
2N .
126
The simplest way to describe Kazakov variables is to introduce one more
- antiperiodic - scalar ﬁeld,
Φ(u) = 1
√
2
X
k≥0
T2k+1uk+ 1
2 −
√
2
X
k≥0
u−k−1
2
k + 1
2
∂
∂˜T2k+1
.
(5.14)
Here ˜T and T are related by transfromation
T2k+1 = ˜T2k+1 + ǫ2
k
k + 1
2
˜T2k−1 + 2ǫNδk,0.
(5.15)
Impose now a relation:
∂φred(z) = 1
ǫ2U−1∂Φ(u)U;
z2 = 1 + ǫ2u,
(5.16)
and in continuum limit ǫ is assumed to vanish.
This is a relation which
maps homogeneous representations into principal, but its invariant meaning
(especially - from the point of view of conformal ﬁeld theory) does not seem to
be enough understood. Anyhow, this relations establishes a relation between
teven and T. Namely, comparing the coeﬃcients in front of the positive powers
of u at both sides of this equation, we get:
T2k+1 = 1
2ǫ2k+1 P∞
m≥k
gmΓ(m+ 1
2)
(m−k)!Γ(k+ 3
2),
k ≥0;
gm = mt2m,
m ≥1;
g0 = 2N.
(5.17)
Inverse transformation looks like
gm = 2
X
k≥m
(−)k−m
T2k+1Γ(k + 3
2)
ǫ2k+1(k −m)!Γ(m + 1
2).
(5.18)
Now,
∂
∂t2k
= 1
2
k−1
X
m=0
Γ(k + 1
2)ǫ2k+1
(k −m −1)!Γ(m + 3
2)
∂
∂˜T2m+1
,
(5.19)
and using this formula when comparing the negative powers of u we ﬁnd:
U = exp
P
m,n Amn ˜T2m+1 ˜T2n+1

,
Amn = 2 (−)m+n
ǫ2(m+n+1) ·
Γ(m+ 3
2 )Γ(n+ 3
2 )
m!n!(m+n+1)(m+n+2).
(5.20)
127
The square of relation (5.16) is:

∂φred2 (z) = 1
ǫ4U−1 (∂Φ)2 (u)U,
(5.21)
or
X
p≥0
Lred
2p z−2p−2 = 1
ǫ4U−1

X
n≥−1
˜L2nu−n−2

U.
(5.22)
This equality implies that
U−1 ˜L2nU = ǫ4 X
p≥0
Lred
2p
I
∞
un+1du
z2p+2
=
= ǫ−2n
n+1
X
p=0
(−)n+1−pCp
n+1Lred
2p ,
(5.23)
since
ǫ4
I
∞
un+1du
z2p+2
=
I
∞
un+1du
(1 + ǫ2u)p+1 = 1
ǫ2n
Γ(−p)
(n + 1 −p)!Γ(−n −1) =
= (−)n+p+1
ǫ2n
(n + 1)!
p!(n + 1 −p)! = (−)n+1−p
ǫ2n
Cp
n+1.
Explicit expressions for the generators ˜L2n (which are harmonics of the stress
tensor 1

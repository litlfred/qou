---
doc_id: arxiv-hep-th-9303139v2
doc_title: "ITFA 93-10 March 1993 A.Morozov"
section_id: sec-064-0-uzφz
section_title: "U(z)∂φ(z) = −"
section_number: 0
pages: 92-101
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
doc_brief: "ITFA 93-10 March 1993 A.Morozov — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
I
0 φ(z)∂U(z).
(4.62)
Here as usual U(z) = P
k>0 tkzk and integral is around z = 0. This is very
similar to generic linear functional of φ−(λ) ≡−
P
k>0
1
kJkλ−k,
H =
Z
φ−(λ)f(λ)dλ,
(4.63)
34 One can consider φ as introduced for simplicity of notation, but it should be kept
in mind that the scalar-ﬁeld representation is in fact more fundamental for generic τ-
functions, not related to the level k = 1 Kac-Moody algebras (this phenomenon is well
known in conformal ﬁled theory, see [16] for more details).
89
one should only require that35
∂U(z) =
Z
f(λ)
z −λdλ,
i.e.
U(z) =
Z
log

1 −z
λ

f(λ)dλ.
(4.64)
In terms of time-variables this means that
tk = −1
k
Z
λ−kf(λ)dλ.
(4.65)
Here we required that U(z = 0) = 0, sometimes it can be more natural to
introduce also
t0 =
Z
log λ f(λ)dλ.
(4.66)
This change from the time-variables to ”time density” f(λ) is known as Miwa
transformation. In order to establish relation with fermionic representation
and also with matrix models we shall need it in ”discretized” form:
tk = ξ
k
P
γ λ−k
γ
−P
γ ˜λ−k
γ

,
t0 = −ξ
P
γ log λγ −
P
γ log ˜λγ

.
(4.67)
We changed integral over λ for a discrete sum (i.e.
the density function
f(λ) is a combination of δ-functions, picked at some points λγ, ˜λγ. This is
of course just another basis in the space of the linear functionals, but the
change from one basis to another one is highly non-trivial. The thing is,
that we selected the basis where amplitudes of diﬀerent δ-functions are the
same: parameter ξ in (4.67) is independent of γ. Thus the real parameters
are just positions of the points λγ, ˜λγ, while the amplitude is deﬁned by
the density of these points in the integration (summation) domain.
This
domain does not need to be a priori speciﬁed: it can be real line, any other
contour or - better - some Riemann surface.) Parameter ξ is also unnecessary
35 As it is usual nowadays, a factor of 2πi is assumed to be included into the deﬁnition
of contour integral
H
.
90
to introduce, because basises with diﬀerent ξ are essentially equivalent. We
shall soon put it equal to one, but not before Miwa transformation will be
discussed in a little more detail.
Our next steps will be as follows. Substitution of (4.63) into (4.67), gives:
H = −ξ
X
γ
φ−(λγ) + ξ
X
γ
φ−(˜λγ).
(4.68)
In fact, what we need is not operator H itself, but the state which is created
when eH acts on the vacuum state ⟨N |. Then, since ⟨N | Jm = 0 for m < 0,
⟨N | e−ξφ−(λ) is essentially equivalent to ⟨N | e−ξφ(λ) with φ−(λ) substituted
by entire φ(λ). If ξ = 1, e−φ(λ) can be further changed for ψ(λ) and we obtain
an expression for the correlator (4.22) an expression where eH is substituted
by a product of operators ψ(λγ). The same is of course true for e ¯
H. Then
Wick therem can be applied and a new type of determinant formulas arises
like, for example,
τ ∼
∆(λ, ˜λ)
∆2(λ)∆2(˜λ)detγδ⟨N | ψ(λγ) ˜ψ(˜λδ) G | N⟩
(4.69)
It can be also obtained directly from (4.27), (4.29) and (4.35) by Miwa trans-
formation. The rest of this subsection describes this derivation in somewhat
more details.
The ﬁrst task is to substitute φ−by φ. For this purpose we introduce
operator
∞
X
k=−∞
tkJk = H+ + H−,
(4.70)
where H+ =
P
k>0 tkJk is just our old H, H−=
P
k≥0 t−kJk, and ”negative
times” t−k are deﬁned by ”analytical continuation” of the same formulas
(4.65) and (4.67):
t−k = 1
k
Z
λkf(λ)dλ = −ξ
k
 X
γ
λk
γ −
X
γ
˜λk
γ
!
.
(4.71)
Then
∞
X
k=−∞
tkJk = H+ + H−= −ξ
 X
γ
φ(λγ) −
X
γ
φ(˜λγ)
!
.
(4.72)
91
Further,
eH++H−= e−1
2s(t)eH+eH−= e
1
2 s(t)eH−eH+,
(4.73)
where
s(t) ≡
X
k>0
ktkt−k = −ξ2 X
k>0
1
k
 X
γ

λ−k
γ
−˜λ−k
γ
 X
δ

λk
δ −˜λk
δ
!
=
= ξ2 log



Y
γ,δ
′ (1 −λδ
λγ )(1 −
˜λδ
˜λγ )
(1 −
˜λδ
λγ )(1 −λδ
˜λγ )


+ const,
(4.74)
where prime means that the terms with γ = δ are excluded from the product
in the numerator and accounted for in the inﬁnite ”constant”, added at the
r.h.s. In other words,
e
1
2s(t) = const ·
Q
γ>δ(λγ−λδ)(˜λγ−˜λδ)
Q
γ
Q
δ(λγ−˜λδ)
ξ2
=
= const ·

∆2(λ)∆2(˜λ)
∆(λ,˜λ)
ξ2
.
(4.75)
Since ⟨N | Jm = 0 for all m < 0, we have ⟨N | eH−= ⟨N |, and therefore
⟨N | eH ≡⟨N | eH+ = ⟨N | eH−eH+ = e−1
2 s(t)⟨N | eH++H−.
(4.76)
From eq.(4.72),
eH++H−= const ·
Y
γ
: e−ξφ(λγ) : : eξφ(˜λγ) :
(4.77)
where ”const” is exactly the same as in (4.75). If ξ = 1, eq.(4.61) can be
used to write:36
⟨N | eH =
∆(λ, ˜λ)
∆2(λ)∆2(˜λ)⟨N |
Y
γ
ψ(λγ)
Y
γ
˜ψ(˜λγ)
(4.78)
36 The choice of ξ can be dictated by particular purposes.
Here we impose the re-
quirement on Miwa transform to represent eH = eHCartan as a product of dimension-1/2
operators - this is most natural from the point of view of Hirota equations and simpliﬁes
the relation with integrable hierarchies. However, in section 2.7 and 2.8 we used another
requirement (and there ξ =
1
√
2 rather than ξ = 1). There the 1-matrix model was con-
sidered, which is characterized by especially simple form of the full hamiltonian (product
of dimension-zero operators), and it was more important to adjust operators, which arise
92
Similarly,
e
¯
H | N⟩=
Y
δ
ψ(¯λδ)
Y
δ
˜ψ(˜¯λδ) | N⟩
∆(¯λ, ˜¯λ)
∆2(¯λ)∆2(˜¯λ)
,
(4.79)
where
¯tk = −1
k
X
δ

¯λk
δ −˜¯λ
k
δ

(4.80)
and we used the fact that Jm | N⟩= 0 for all m > 0. Finaly,
τN{t, ¯t | G} = ⟨N | eH G e
¯
H | N⟩=
∆(λ, ˜λ)
∆2(λ)∆2(˜λ)
∆(¯λ, ˜¯λ)
∆2(¯λ)∆2(˜¯λ)
·
·⟨N |
Y
γ
ψ(λγ)
Y
γ
˜ψ(˜λγ) G
Y
δ
ψ(¯λδ)
Y
δ
˜ψ(˜¯λδ) | N⟩.
(4.81)
Singularities at the coinciding points are completely eliminated from this
expression, since poles and zeroes of the correlator are canceled by those
coming from the Van-der-Monde determinants.
Let us now put N = 0 and deﬁne normalized τ-function
ˆτ0{t, ¯t | G} ≡τ0{t, ¯t | G}
τ0{0, 0 | G},
(4.82)
i.e. divide r.h.s. of (4.81) by ⟨0 | G | 0⟩. Wick theorem now allows to rewrite
the correlator at the r.h.s. as a determinant of the block matrix:
det







⟨0 | ψ(λγ) ˜ψ(˜λδ) G | 0⟩
⟨0 | G | 0⟩
⟨0 | ψ(λγ) G ˜ψ(˜¯λδ) | 0⟩
⟨0 | G | 0⟩
−⟨0 | ˜ψ(˜λδ) G ψ(¯λγ) | 0⟩
⟨0 | G | 0⟩
⟨0 | G ψ(¯λγ) ˜ψ(˜¯λδ) | 0⟩
⟨0 | G | 0⟩







(4.83)
from eHCartan after Miwa transform to have simple correlators with eAψ ˜ψ. When ana-
lyzing the 1-matrix model from this point of view one should also keep in mind that it
was actually represented in s.2.3 in terms of two complex fermions. Screening charges
are Q(+) =
H
e
√
2φ =
H ˜ψ1ψ2 =
H
eφ1−φ2,
Q(−) =
H
e−
√
2φ =
H ˜ψ2ψ1 =
H
eφ2−φ1, while
φ =
1
√
2(φ1 −φ2). The Hamiltonian is HCartan =
1
√
2
P
k tkJk = 1
2
P
k tk(J1
k −J2
k), and
Miwa transformation generators insertions of operators χ1 ˜χ2, where χ1 and ˜χ2 have di-
mension 1/8 (rather than 1/2 as in the one (complex)-fermion system, considered in this
section).
93
Special choices of points λγ, . . . , ˜¯λδ can lead to simpler formulas. If ˜¯λγ →
¯λγ, so that ¯tk →0, the matrix elements at the right lower block in (4.83)
blow up, so that the oﬀ-diagonal blocks can be neglected. Then
τ0{t, ¯t | G} →τ KP{t | G} = ⟨0 | eH G | 0⟩
⟨0 | G | 0⟩
=
=
∆(λ, ˜λ)
∆2(λ)∆2(˜λ)detγδ
⟨0 | ψ(λγ) ˜ψ(˜λδ) G | 0⟩
⟨0 | G | 0⟩
.
(4.84)
This function no longer depends on ¯t-times and is just a KP τ-function.
Matrix element
ϕ(λ, ˜λ) = ⟨0 | ψ(λ) ˜ψ(˜λ) G | 0⟩
⟨0 | G | 0⟩
(4.85)
is singular, when λ →˜λ: ϕ(λ, ˜λ) →
1
λ−˜λ. If now in (4.84) all ˜λ →∞,
τ KP{t | G} = detγδϕδ(λγ)
∆(λ)
,
(4.86)
where
ϕδ(λ) ≡⟨0 | ψ(λ)

∂δ−1 ˜ψ

(∞) G | 0⟩∼λδ−1

1 + O
1
λ

.
(4.87)
This is the main determinant representation of KP τ-function in Miwa parametriza-
tion.
Starting from representation (4.86) one can restore the corresponding
matrix HKP
ij
in eq.(4.55) [36]:
HKP
ij {t} =
I
ziϕ−j(z)e
P
k tkzkdz,
(4.88)
i.e.
T KP
lj
=
I
zlϕ−j(z).
(4.89)
Then obviously ∂HKP
ij
∂tk
= HKP
i+k,j. Now we need to prove that the τ-function
is given at once by det ϕγ(λδ)
∆(λ)
and DetHKP
ij {t}. In order to compare these two
94
expressions one should take tk = 1
k
Pn
γ λ−k
γ , so that
exp

X
k>0
tkzk

=
n
Y
γ=1
λγ
λγ −z =
 n
Y
γ
λγ
! X
γ
(−)γ
z −λγ
∆γ(λ)
∆(λ) ,
(4.90)
where
∆γ(λ) =
Y
α>β
α,β̸=γ
(λα −λβ) =
∆(λ)
Q
α̸=γ(λα −λγ),
(4.91)
and
HKP
ij

tk= 1
k
Pn
γ λ−k
γ
=
 n
Y
γ
λγ
! X
γ
(−)γ+1∆γ(λ)
∆(λ)
λi
γϕ−j(λγ).
(4.92)
As far as n is kept ﬁnite, determinant of the inﬁnite-size matrix (4.92),
Deti,j<0HKP
ij

tk= 1
k
Pn
γ λ−k
γ
= 0 since it is obvious from (4.92) that the rank of
the matrix is equal to n. Therefore let us consider the maximal non-vanishing
determinant,
Det−n≤i,j<0HKP
ij

tk= 1
k
Pn
γ λ−k
γ
=
=
 n
Y
γ
λγ
!n
detiγ
 (−)γ+1∆γ(λ)
λiγ∆(λ)
!
· detγjϕj(λγ) =
= detγjϕj(λγ)
∆(λ)
.
(4.93)
We used here the fact that determinant of a matrix is a product of determi-
95
nants and reversed the signs of i and j. Also used were some simple relations:
n
Y
γ=1
∆γ(λ)
∆(λ) =
1
∆2(λ),
detiγ
1
λiγ
=
 n
Y
γ
λγ
!−1
∆(1/λ),
∆(1/λ) =
Y
α>β
 1
λα
−1
λβ
!
= (−)n(n−1)/2∆(λ)
 n
Y
γ
λγ
!−(n−1)
,
thus
 n
Y
γ
λγ
!
(−)n(n−1)/2
n
Y
γ=1
∆γ(λ)
∆(λ) detiγ
1
λi
γ
=
1
∆(λ).
Since (4.93) is true for any n, one can claim that in the limit n →∞
we recover the statement, that τ KP{t} = Deti,j<0HKP
ij
with HKP
ij
given by
eq.(4.92) (that formula does not refer directly to Miwa parametrization and
is deﬁned for any t and any j < 0 and i). This relation between ϕγ’s and
HKP
ij
can now be used to introduce negative times ¯tk according to the rule
(4.58). Especially simple is the prescription for zero-time: Hij →Hi+N,j+N,
when expressed in terms of ϕ just implies that
det ϕγ(λδ)
∆(λ)
→det ϕγ+N(λδ)
(detΛ)N∆(λ).
(4.94)
Generalizations of (4.88), like
Hij{t, ¯t} =
I I
zi¯zj⟨0 | ψ(z) G ˜ψ(¯z) | 0⟩e
P
k(tkzk+¯tk ¯zk)dzd¯z,
(4.95)
also can be considered.
4.7
Matrix models versus τ-functions.
We are now prepared to return to our main subject and discuss integra-
bility properties of eigenvalue matrix models. The claim is that partition
functions of all these models, when considered as functions of time-variables
(parametrizing the shapes of potentials) are in fact τ-functions of (perhaps,
96
multicomponent) Toda-lattice and/or KP type. (Interesting non-eigenvalue
models are believed to be related to integrable systems of more general type,
not restricted to level k = 1 Kac-Moody algebras.)
Partition functions are, however, not generic Toda or KP τ-functions:
ﬁrst, they usually belong to some reduced hierarchies, second, the relevent
operators G (points of Grassmannian) are restricted to stay in peculiar do-
mains of the universal module space, speciﬁed by ”string equations”. String
equation is in fact nothing but the set of Ward-identities (Virasoro or W-
constraints in the examples under investigation), which are now interpreted
as equations on G. The very possibility of such interpretation is highly non-
trivial and reﬂects some deep relation between the constraints and integrable
structure. In the case of Virasoro constraints this is not a puzzle, because
Virasoro algebra is a symmetry (covariance) of the hierarchy, the situation
with other constraints is less clear (see the footnote at section 4.3). In fact,
when applied to a τ-function of appropriately reduced hierarchy, the inﬁnitely
many constraints usually become dependent and it is enough to impose only
the lowest Virasoro constraint L−1τ = 0 (or L−pτ = 0, where p is the degree
of reduction), in order to recover the entire set [29]. It is this lowest con-
straint (or rather its t1-derivative,
∂
∂t1(L−1τ) = 0) that traditionally carries
the name of ”string equation”. It is often much simpler to deduce than the
entire set of identites, what is important in practical applications (especially
because determinant formulas, which imply integrability, can be also simpler
to ﬁnd in some situations than the Ward identities).
In order to give a complete description of some sort of (matrix) models
from the point of view of integrability theory it is enough to specify the hier-
archy, to which it belongs (if partition function is interpreted as τ-function,
Zmodel{t} = τ{t | Gmodel}
(4.96)
and the string equation which serves to ﬁx operator G - the point in the
universal module space.37 After that it becomes an internal (yet unsolved)
problem of integrability theory to explain, what is so special about the set of
37 As we argued in the Introduction and in section 2.1, the word ”matrix” can be
probably omited if generic Lagrangians are considered in other models of quantum ﬁeld
theory.
Also the universal module space (where moduli are - of bundles over spectral
Riemann surfaces) can (and should) be treated as a ”space of theories”. It is one of the
great puzzles (and beauties) of string theory, that Riemann surfaces appear both in the
world-sheet and spectral ”dimensions”. See [6] for more discussion on this issue.
97
points {Gmodel} in this space. (We shall touch this problem in the next sub-
section, devoted to Kac-Schwarz operators.) Alternatively, if there is nothing
special, it is an (unsolved) problem of matrix model theory to ﬁnd models,
associated with any points G in the universal module space (or explain what
is an obstacle, if any).
We proceed now to description of particular matrix models from this
point of view. As everywhere in these notes we consider only the most impor-
tant classes of scalar-product, conformal (multicomponent) and Generalized
Kontsevich models (GKM). All other examples (like models of complex, or-
thogonal, unitary etc matrices) can be included into consideration with more
or less eﬀort (see [28] and [91] for the cases of complex and unitary models
respectively), but they do not add much for the general theory that we are
now considering. String equations will be discussed in the next subsection.
Scalar-product models. These were exhaustively discussed in sections 3.5-

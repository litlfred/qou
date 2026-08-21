---
doc_id: arxiv-math-0111022v1
doc_title: "Some remarks on q-deformed multiple polylogarithms"
section_id: sec-001-1-motivation
section_title: "Motivation"
section_number: 1
pages: 1-10
source_pdf: 0111022v1.pdf
source_sha256: fea7f118014838fe
doc_brief: "Some remarks on q-deformed multiple polylogarithms — We introduce general q-deformed multiple polylogarithms which even in the dilogarithm case diﬀer slightly from the deformat ion usu- ally"
---
In [CL] a family of noncommutative deformations S4,θ of the four dimen-
sional sphere has been introduced from the instanton algebra. Co ncretely,
the algebra of functions on S4,θ is given by the generators t,α,α ∗,β,β ∗ and
relations
αα ∗ = α ∗α, ββ ∗ =β ∗β
1
αβ = λβα, α ∗β =λβα ∗
0 = αα ∗ +ββ ∗ +t2 −t
and the requirement that t commutes with all the other generators. With
ϕ,ψ angles,
0 ≤ϕ ≤ π
2, −π
2 ≤ψ ≤ π
2
and u,v the unitary generators of the algebra of smooth functions on the
noncommutative 2-torus, one has
α = u
2 cosϕ cosψ
β = v
2 sinϕ cosψ
t = 1
2 + 1
2 sinψ
and the Dirac operator corresponding to the round metric on the s phere is
given as (see [CL])
D = (cos ϕ cosψ )− 1δ1γ1 + (sinϕ cosψ )− 1δ2γ2
+ 1
cosψ
√
−1
( ∂
∂ϕ + 1
2 cotϕ − 1
2 tanϕ
)
γ3 +
√
−1
( ∂
∂ψ − 3
2 tanψ
)
γ4
where δ1,δ 2 are the derivations on the noncommutative torus and γi the
Dirac matrices. Using an Ansatz
f =
∑
n,m
anm (ϕ,ψ )unvm
for the Dirac equation
Df = 0
we get a q-deformation of a classical partial diﬀerential equation in ϕ and ψ
for anm. So, solving the Dirac equation on S4,θ translates into a problem of
solving a diﬀerential equation for certain q-special functions.
From a slightly diﬀerent perspective, one can also understand this f rom
the following consideration: It is one of the basic properties of quan tum ﬁeld
theory that one can represent it in terms of inﬁnitely many coupled h armonic
oscillators. This property is not independent of the fact that the s ymmetry
group of ﬂat three dimensional space is related to SU (2) which in turn links
2
to the oscillator algebra. There is a similar situation for the case of th eS4,θ .
The algebrasS4,θ contain the suspension of a noncommutative 3-sphere given
by an analytic continuation of the quantum group SUq (2) to the case where
q is a root of unity. Now, the quantum group SUq (2) relates through the
Jordan-Schwinger isomorphism between the (roughly speaking dua l) quan-
tum algebra ˇUq(sl2) and the extended algebra of two q-oscillators Aext, 2
q to
q-oscillators (see [KS]). By the SUq (2) symmetry of the suspended noncom-
mutative 3-sphere, it follows that a projective module over S4,θ carries always
a coaction of basically SUq (2) on it (taking the coaction of SUq (2) on the
suspended noncommutative 3-sphere and the trivial coaction on t he gener-
ator t of S4,θ ). Remember that a projective module is the noncommutative
analog of a vector bundle. Therefore, the quantum state space o f a non-
commutative gauge theory over S4,θ should always carry a corepresentation
of SUq (2). But then, by the results cited above, such a noncommutative
quantum ﬁeld theory can always be interpreted as a system of coup led q-
oscillators. Now, q-oscillators relate to q-Hermite polynomials as q-special
functions (see [KS]). So, at least if we treat the quantum ﬁeld theor ies on
S4,θ perturbatively, starting from a system of free q-oscillators, we should,
again, be led to expressions in terms of q-special functions.
In conclusion, both arguments suggest that perturbative quant um ﬁeld
theory onS4,θ should have a formulation in terms of q-special functions. Since
in usual quantum gauge theories on commutative space-time, the w eights
of Feynman graphs can be calculated as values of so called multiple poly -
logarithms (see [BK], [Kre]) and this fact plays a considerable role for t he
structural properties of quantum ﬁeld theory (see [CK 1998], [Kon ], [KoSo]),
a ﬁrst step toward perturbative quantum ﬁeld theory on S4,θ should be to
look for q-deformations of multiple polylogarithms. For the logarithm and
dilogarithm cases, q-deformations have been studied (see e.g. [Kir], [Koo]
and the literature cited therein) but even for the dilogarithm case, we use a
slightly diﬀerent form for the q-deformation, here. The main advantage of
the form which we give, here, is that the q-deformed multiple polylogarithms
form an algebra, then, and for the restriction to the case of q-deformed mul-
tiple ζ-values we even get a noncommutative deformation of the classical
Hopf algebra structure of multiple polylogarithms (see [Gon 2001]). S ince
precisely these structural features of multiple polylogarithms give the above
mentioned link to quantum ﬁeld theory, we consider this to be an impor tant
property for the purpose we have in mind.
3
For the reader who is not aquainted with the notations and convent ions
of q-calculus and q-special functions, we refer e.g. to [KS] for a short intro-
duction.
2 q-deformed multiple polylogarithms
Let
Lin1,...,n m (z1,...,z m;q) =
∑
0<k1<...<k m
zk1
1 ...z km
m
(1 −qk1)n1... (1 −qkm)nm
be the q-deformed multiple polylogarithms. We have
(1 −q)n1+... +nm
Lin1,...,n m (z1,...,z m;q)
q→ 1
→ Lin1,...,n m (z1,...,z m)
where
Lin1,...,n m (z1,...,z m) =
∑
0<k1<...<k m
zk1
1 ...z km
m
kn1
1 ...k nm
m
are the classical multiple polylogarithms. With the q-derivative deﬁned as
(see e.g. [KS])
Dz,qf (z0) = f (qzo) −f (zo)
(q − 1)z0
we have the following lemma:
Lemma 1 We have
Dzj ,qLin1,...,n m (z1,...,z m;q) = 1
(1 −q)zj
Lin1,...,n j− 1,...n m (z1,...,z m;q)
Especially
Dz,qLin (z,q ) = 1
(1 −q)z · 1
1 −z
Proof. By calculation.
In contrast to the q-deformations introduced for the logarithm and the
dilogarithm case in [Kir] and [Koo], we have chosen a version for the q-
deformation which has the following important property:
4
Lemma 2 The rational linear span of the Lin1,...,n m (z1,...,z m;q) forms an
associative algebra over Q.
Proof. Follows from the deﬁnition.
A special case of this is the fact that the so called symmetry relation s (see
[Gon 1997]) hold also in the q-deformed case, as is seen from the following
corollary:
Corollary 3 We have
Li1 (x,q )Li1 (y,q ) = Li1, 1 (x,y,q ) +Li (y,x,q ) +Li2 (xy,q )
Also there is a q-deformed version of the so called distribution relations
(see [Gon 1997] for the classical case. again), now:
Lemma 4 We have
Li2 (x,q n) = 1
n
∑
yn=x
Li2 (y,q )
and
Li1, 1 (x1,x 2,q n) = 1
n
∑
yn
i =xi
Li1, 1 (y1,y 2,q )
Proof. Direct calculation.
An important consequence of the property
d
dzj
Lin1,...,n m (z1,...,z m) = 1
zj
Lin1,...,n j− 1,...n m (z1,...,z m)
of the classical multiple polylogarithms is the integral formula
Lin1,...,n m (z1,...,z m) =
∫ zj
0
1
wj
Lin1,...,n j− 1,...,n m (z1,...w j,...,z m)
5
which leads as a special case to the integral formula
ζ (n1,...,n m) =
∑
0<k1<...k m
1
kn1
1 ...k nm
m
=
∫ 1
0
dt
1 −t ◦ dt
t ◦... ◦ dt
t/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
n1times
◦... ◦ dt
1 −t ◦ dt
t ◦... ◦ dt
t/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
nmtimes
noted by Kontsevich (see e.g. [Gon 2001] for the deﬁnition of the rig ht hand
integral) for the multiple ζ-values (i.e. the multiple polylogarithms with all
variables identical to unity and nm> 1). E.g.
ζ (2) =
∫
0≤ t1≤ t2≤ 1
dt1
1 −t1
∧ dt2
t2
As a consequence of Lemma 1, we have a similar integral formula for t he case
of q-deformed multiple ζ-values with the integral replaced by the q-integral
(see e.g. [KS]) and the appropriate powers of (1 −q) inserted. E.g.
ζq (2) = 1
1 −q
∫
0≤ t1≤ t2≤ 1
dqt1
1 −t1
∧ dqt2
t2
Up to now, we have considered the case where the multiple polylogarit hms
become q-deformed but the variables zj remain classical commutative num-
bers from C, only. In the next section, we are going to consider variables
which are q-commutative.
3 q-deformed multiple polylogarithms with q-
commuting variables
Let zj, j ∈ N be q-commuting variables, i.e.
zizj =q zjzi, i<j
We now have to give an ordering for the variables zj in the deﬁnition of the
q-deformed multiple polylogarithms as given above, in order to make th is
well deﬁned in the case of q-commuting variables. We do this by requiring
6
that we order the variables from left to right according to increasin g index,
e.g.
Li1, 1 (z1,z 2;q) =
∑
0<j<k
zj
1zk
2
(1 −qj) (1 −qk)
but
Li1, 1 (z2,z 1;q) =
∑
0<j<k
zk
1zj
2
(1 −qj) (1 −qk)
With this deﬁnition, we have, again, the following property:
Lemma 5 For the ordered deﬁnition of the q-deformed multiple polyloga-
rithms with q-commuting variables as given above, the rational span of th e
q-deformed multiple polylogarithms forms an algebra over Q. Especially, the
symmetry relations hold also for the q-commuting variables, then.
Proof. Direct calculation, again.
Especially, this means that the commutator of two q-deformed multiple
polylogarithms can be expressed as a sum of such.
Since the diﬀerential equation for q-deformed multiple polylogarithms
remains formally valid in the case of q-commuting variables, too, we can
next ask for an integral formula for the q-deformed multiple ζ-values in this
case. In trying to derive such a formula, one makes a strange obse rvation:
On the one hand, we have
ζq (n1,...,n m) =
∑
0<k1<...k m
1
(1 −qk1)n1
... (1 −qkm)nm
i.e. the ζq (n1,...,n m) do not depend on the variables zj at all and therefore
remain commuting with each other. On the other hand, consider e.g. the
case of ζq (2) where the integral formula reads
ζq (2) = 1
1 −q
∫
0≤ t1≤ t2≤ 1
dqt1
1 −t1
∧ dqt2
t2
Now, in a formal sense one would, in the case of q-commuting variables,
consider the integrals not to satisfy the Fubini theorem if one multip lies to
7
expressions of this kind but one would expect the diﬀerentials forma lly to
exchange with a factor q− 1. So, formally this would lead to an exchange rule
ζ (n1,...,n m;q)ζ (j1,...,j l;q) = q(∑ ni)(∑ ji)ζ (j1,...,j l;q)ζ (n1,...,n m;q)
for the q-deformed multiple ζ-values for n1 < ... < nm < j1 < ... < jl in the
ordering for the q-commutativity relations. This means that we should allow
the arguments of the q-deformed multiple ζ-values - i.e. the indices of the
q-deformed multiple polylogarithms - to become noncommuting variabe ls,
too. In the sequel, we will assume this to be the case and the above r elation
for the q-deformed multiple ζ-values to hold true.
We next come to the question of Hopf algebra structure. On the alg ebra of
classical multiple polylogarithms there is a coproduct given (see [Gon 2 001]
for the deﬁnition). Since the coproduct ∆ preserves the subalgeb ra of classical
multipleζ-values, we get a bialgebra Z of classical multiple ζ-values in this
way. For the algebra Zq of q-deformed multiple ζ-values as just deﬁned,
∆ is no longer compatible as a coproduct. The reason for this is that t he
number of arguments - which determines the power of q in the above q-
commutation relation - varies between the diﬀerent terms of the co product
(see the deﬁntion in [Gon 2001]). But this observation immediately sug gests
also the solution: One has to formally insert an appropriate number o f q-
commuting variables into the diﬀerent terms of the coproduct in ord er to
make it an algebra morphism of the deformed product. In conclusion , we
have observed the following result, therefore:
Lemma 6 There is a q-deformation ∆ q of the coproduct ∆ of Z which turns
Zq into a bialgebra. Since there is a full Hopf algebra structur e for Z (see
[Gon 2001]), we can by a general result in Hopf algebra cohomo logy (see e.g
[CP]) assume without loss of generality that Zq carries a full Hopf algebra
structure, too.
Remark 1 The commutators for the full algebra of q-deformed multiple poly-
logarithms - with q-commutation relations for both, the variables and the in-
dices - are much too complicated to allow at present for an ans wer to the
question if there exists a deformation of the full Hopf algeb ra of classical
8
multiple polylogarithms. But since the Hopf structure is in timately tied to
the motivic origin of these periods (see [Gon 2001]), we expe ct that as a con-
sequence of ultrarigidity (see [Sch 2001a], [Sch 2001b]), t here exists no such
deformation (because the multipleζ-values are supposed to give precisely those
periods which are linked to the Grothendieck-Teichm¨ uller group, see [Kon]).
Remark 2 The Hopf algebra of Connes and Kreimer is supposed to be re-
lated to the Hopf algebra of classical multiple ζ-values (see [CK 1998], [CK 1999]).
So, we expect Zq to be related to a q-deformation of the Connes-Kreimer al-
gebra (see also [GS] for the question of deformations of the C onnes-Kreimer
algebra).
Conjecture 7 By the arguments given in the introductory section and by
the connection between the Hopf algebra structure of multip le ζ-values and
the Connes-Kreimer algebra mentioned in the previous remar k, one expects
Zq to act on quantum ﬁeld theories on S4,θ . On the other hand, we know
that the Hopf algebra ~HGT , introduced in [Sch 2001a] as a quantum analog of
the Grothendieck-Teichm¨ uller group, acts on quantum ﬁeld theories on S4,θ
(see [Sch 2001b]). We conjecture that the corresponding rep resentations of
Zq and ~HGT , gained in this way, are isomorphic.
In conclusion, we have seen that it is possible to introduce a special
q-deformation of multiple polylogarithms which allows for quantum coun -
terparts of several of the algebraic features of periods which ha ve become
increasingly important in the study of quantum ﬁeld theories in recen t years.
Acknowledgements:
I thank H. Grosse for discussions on the topics involved and A. Gonc harov
for very helpful explanations on classical motivic structures and f or drawing
my attention to an important reference. Besides this, I thank the Deutsche
Forschungsgemeinschaft (DFG) for support by a research grant and the Erwin
Schr¨ odinger Institute for Mathematical Physics, Vienna, for ho spitality.
9

---
doc_id: arxiv-hep-th-9303139v2
doc_title: "ITFA 93-10 March 1993 A.Morozov"
section_id: sec-037-10-this-is-possible-only-for-very-special-kac-mo
section_title: "This is possible only for very special Kac-Moody algebras, and such formulation is"
section_number: 10
pages: 25-30
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
doc_brief: "ITFA 93-10 March 1993 A.Morozov — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
important in order to deal with conventional formulation of integrability, which usually
involves commuting Hamiltonian ﬂows (not just a closed algebra of ﬂows) and fermionic
realization of the universal module space (universal Grassmannian). In fact these restric-
tions are quite arbitrary and can be removed (though this is not yet done in full details),
see section 4 below for more detailed discussion.
22
the answer. For generic r the similar choice of ”adjacent” (not simple!) roots
(such that their scalar products are +1 or 0) leads to selection of the following
r screening operators Q(1) = i
H ˜ψ1ψ2 Q(2) = −i
H ψ2 ˜ψ3, Q(3) = i
H ˜ψ3ψ4, . . .,
i.e. Q(j) = i
H ˜ψjψj+1 for odd j and Q(j) = −i
H ψj ˜ψj+1 for even j.
2.4
Gross-Newman equation
We turn now to consideration of the WI for another sort of matrix mod-
els. This subject concerns at least two important classes: the conventional
discrete two-matrix models and Kontsevich models.
As it was explained
in the Introduction the theories of the second type arise in consderation of
the (p, 1) continuous matrix models, as well as in the study of topological
Landau-Ginzburg theories, while the two-matrix model is believed to exhibit
a rich pattern of continuous limits and is capable to provide representatives
of all the (p, q) universality classes (this line of reasoning, however, has never
been really developed and we shall not discuss it in these notes).
The starting point and the basic example is provided by the integral
FV,n{L} ≡
Z
n×n dXe−trV (X)+trLX
(2.35)
over n × n Hermitean matrix, which we shall further refer to as ”Kontsevich
integral”, keeping in mind its most important application (though this obvi-
ous quantity has been of course considered by many other people). It may
seem that the action in this integral is not of the most general type and we
can no longer perform arbitrary change of variables X −→f(X) without
changing the functional form of the integral. In fact this is incorrect, because
”external ﬁeld” L is matrix valued and coupled to X linearly, and therefore
any correlator of X-ﬁelds can be represented through L-derivatives. Con-
sider again the shift X →X + ǫnXn+1, n ≥−1. Invariance of the integral
implies:
Z
dXe−trV (X)+trLXtr ǫn
 
−Xn+1V ′(X) + LXn+1 +
n
X
k=0
XktrXn−k
!
= 0,
which can be rewritten as 11
tr ǫn

−
∂
∂Ltr
n+1 V ′ 
∂
∂Ltr

+ L

−
∂
∂Ltr
n+1 +
11The obvious relation is used here: XγδetrLX =
∂
Lδγ etrLX.
Note that the order of
23
Pn
k=0

−
∂
∂Ltr
k tr

−
∂
∂Ltr
n−k
FV {L} =
= tr ǫn

−
∂
∂Ltr
n+1 
V ′ 
∂
∂Ltr

−L

FV {L} = 0
(2.36)
This system is in fact equivalent to a single matrix-valued equation
 
V ′
 ∂
∂Ltr
!
−L
!
FV {L} = 0.
(2.37)
As well as I know this equation was ﬁrst written down in [54], therefore it will
be refered to as the Gross-Newman (GN) equation. It was rediscovered and
implications for the theory of matrix models were investigated in [24],[30],[38].
There are essentially two types of corollaries, which will be discussed in
the next two subsections. First, GN equation can be used to characterize
the function FV {L} itself. This will lead us to consideration of Kontsevich
models. Second, it can be used to derive equations for the 2-matrix model,
which arises after FV {L} is further integrated with some weight over L.
2.5
Ward identities for Generalized Kontsevich Model
Being just the complete set of equation of motion the GN equation (2.37)
provides complete information about the function FV {L}.
However, this
statement needs to be formulated more carefully. A need for this comes, for
example, from the observation that operators
trLm
 
V ′
 ∂
∂Ltr
!
−L
!
(2.38)
do not form a closed algebra: their commutators have some diﬀerent func-
tional form. One of the reasons for these complications is that eq.(2.37) does
not account explicitly for a very important property of FV {L}: this func-
tion in fact depends only on the eigenvalues of L. This information should
be still added somehow to the GN equation. We shall analyze this issue of
eigenvalue-dependence in more details in next sections. For our current pur-
poses this argument implies that one should try to express equation (2.37) in
matrix indices γδ is reversed at the r.h.s. as compared to the l.h.s., i.e. derivatives are in
fact w.r.to transponed matrix L:
f(X)etrLX = f(
∂
∂Ltr )etrLX (at least for any function
f(x), which can be represented as a formal seria in integer powers of X).
24
terms of eigenvalues. Here, however, one should be carefull again. Clearly,
not only FV {L} depends on eigenvalues, it depends on their ”symmetric”
(Weyl-group invariant) combinations, i.e. it rather depends on quantities
like trLa then on particular eigenvalues. Moreover, powers a here should be
negative and fractional.
Indeed, integrals like (2.35) are usually understood as analytical contin-
uation from some values of parameters in the potential V , when integral is
convergent. They can be also related to the formal (perturbation) seria aris-
ing when integrand is expanded around a stationary point. To begin with it
is reasonable to take n = 1 i.e. consider just an ordinary integral. For the
sake of simplicity also take particular V (x) = −xp+1
p+1 . Then the stationary
point is at x = λ
1
p and
Z
dxe−xp+1
p+1 +lx ∼l−p−1
2 e
p
p+1l
p+1
p
X
k≥0
ckl−k
p .
(2.39)
It is now easy to understand what should be done in the general situa-
tion with matrices and arbitrary potentials. First of all, one needs to solve
equation for the stationary point, V ′(X) = L. For this purpose it is most
convenient to introduce a new matrix variable Λ instead of L, which by def-
inition satisﬁes V ′(Λ) = L. Then stationary point is just X = Λ. Second,
one should separate the analogue of the complicated prefactor (quasiclassical
contribution):
CV {Λ} = (2π)n2/2etr(ΛV ′(Λ)−V (Λ))
q
detV ′′(Λ)
,
(2.40)
Then the function that describes pure ”quantum” contribution 12
ZV {T} ≡CV {Λ}−1FV {V ′(Λ)}
(2.41)
12The ”classical action” in (2.40) can be also represented as tr (ΛV ′(Λ) −V (Λ)) =
tr
R
ΛdV ′(Λ). Determinant of quadratic ﬂuctuations is deﬁned as
(2π)n2/2 (detV ′′(Λ))−1/2 ∼
Z
dY e−trV2(Λ,Y ),
where V2(Λ, Y ) ≡limǫ→0 1
ǫ2 (V (Λ + ǫY ) −V (Λ) −ǫV ′(Λ)Y ). For V (Λ) = Λp+1
p+1
we have
V ′′(Λ) = (Pp−1
k=0 Λk ⊗Λp−k−1). One could easily choose an ”opposite” parametrization
in eq.(2.42): Tk = −1
ktrΛ−k. Though not quite obvious, this never inﬂuences any results
(see section 2.10 for an example). Our choice of signs is motivated by simpliﬁcation of
25
to be refered as partition function of the Generalized Kontsevich Model
(GKM) [30], can be represented as a formal (perturbation) series expansion
in variables
Tk = 1
ktrΛ−k.
(2.42)
GN (2.37) equation can be now rewritten as a set of diﬀerential equations
for ZV {T}. Indeed, we already have:
C−1
V
 
V ′
 ∂
∂Ltr
!
−L
!
CV ZV {T} = 0,
(2.43)
but it is still necessary to express the operator at the l.h.s. in terms of T.
This is in fact possible to do, using the relation:
∂
∂Ltr
ZV {T} =
X
k
∂Tk
∂Ltr
∂Z
∂Tk
(2.44)
and substituting the traces of Λ-matrices, which can arise in the process of
calculation, by T’s. It is important only that Λ’s usually appear in negative
powers: this is already achieved by the choice of a proper normalization
factor CV {Λ}. For monomial potential Vp(X) = Xp+1
p+1 this is especialy simple:
L = Λp and
∂Tk
∂Ltr = −1
pΛ−p−k.
This reasoning allows one to rewrite eq.(2.43) identically in the form
X
l
Λ−lOl(T)ZV {T} = 0,
(2.45)
where Ol are some diﬀerential operators, depending on the shape of V , but
independent on the size n of the matrix (as all the above reasoning never
refered to particular values of n, except for a sample example at the very
beginning). It remains to use the fact that matrix L can be arbitrary large
and have arbitrarily many independent entries, in order to conclude that we
derived a set of constraints on ZV in the form
Ol(T)ZV {T} = 0.
(2.46)
formulas for the GKM, including the relation between L and Λ. Instead, some sign factors
appear in formulas, related to Toda-like representations of partition functions and those
involving ˜W-operators.
26
For potential V of degree p + 1 these appear to be exactly the ”continu-
ous Virasoro constraints”. See refs.[24] and [30] for detailed analysis of the
Virasoro case p = 2 (associated with the pure topological gravity and with
the double-scaling limit of the 1-matrix model), and [55] for the exhaustive
presentation of the case of p = 3.
2.6
Discrete Virasoro constraints for the Gaussian Kont-
sevich model
As a simplest illustration of the technique, described in the previous subsec-
tion, we derive now the constraints for the Gaussian Kontsevich model [56]
with potential V (X) = 1
2X2:

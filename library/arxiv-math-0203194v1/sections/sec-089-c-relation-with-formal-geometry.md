---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-089-c-relation-with-formal-geometry
section_title: "Relation with Formal Geometry."
section_number: C
pages: 216-220
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
In this section we need to consider the valuation ring R of K.
Let
us denote by m the maximal ideal of R, and ﬁx a topological generator
0̸ = π ∈m. The residue ﬁeld R/m is denoted by k.
Let A be an aﬃnoid algebra over K. The spectral semi-norm on A is
the function | · |sup : A →R≥0 deﬁned, for any f ∈A, by
|f|sup =
sup
x∈Spm(A)
|f(x)|.
It is known that for any representation α: K{t1, . . . , tn}/I
∼
→A, we have
|f|sup ≤|f|α for every f ∈A (cf. [BGR84, 6.2.1]).
Theorem 3.1 (Maximal modulus principle). For an aﬃnoid algebra A and
an element f ∈A, there exists a point x ∈Spm(A) such that |f(x)| = |f|sup.
We refer [BGR84, 6.2.1] for the proof.
Given an aﬃnoid algebra A over K, we introduce the following notation:
A◦
=
{f ∈A | |f|sup ≤1},
A◦◦
=
{f ∈A | |f|sup < 1},
A
=
A◦/A◦◦;
A◦is a R-subalgebra of A, and A◦◦is an ideal of it. For instance, K◦= R,
K◦◦= m, and K = k.
Example 3.2. We can immediately calculate:
T n
K
◦
=
R{t1, . . . , tn}
: =
 P
ν1,... ,νn≥0 aν1,... ,νntν1
1 · · · tνn
n
|aν1,... ,νn| →0 for
∈R[[t1, . . . , tn]]
ν1 + · · · + νn →∞

T n
K
=
k[t1, . . . , tn].
Note that T n
K
◦is the (π)-adic completion of the polynomial ring R[t1, . . . , tn]
over R. It should be noticed that T n
K is a polynomial ring over k; indeed,
each element in R{t1, . . . , tn} lies, by the convergence condition, in T n
K
◦◦
modulo ﬁnitely many terms.
Proposition 3.3. Let A be an aﬃnoid algebra over K. Then,
(i) A◦is a model of A; i.e. A◦⊗R K ∼= A,
3. RELATION WITH FORMAL GEOMETRY.
213
(ii) A◦is (π)-adically completed,
(iii) A◦is topologically of ﬁnite type over R; i.e. R{t1, . . . , tn}/a ∼= A for
some ideal a in R{t1, . . . , tn},
(iv) A◦is ﬂat over R,
(v) A is a k-algebra of ﬁnite type.
Proof. (i) and (ii) are easy to see. The ﬂatness of R is now equivalent to
the lack of R-torsion. So (iv) can be seen immediately.
Before proving (iii) and (v), we need some terminology: let ∥· ∥α be a
Banach norm of A (α: T n
K →A: surjective). We say an element f of A is
power-bounded if {∥f n∥α | n ∈N} is bounded. This does not depend on
the choice of the presentation α since the equivalence class of the resulting
norms do not change. An element f of A is said to be topologically nilpotent
if lim f n = 0; here the limit is taken with respect to the Banach norm ∥· ∥α,
and is not dependent of the choice.
Let us prove (iii). By [BGR84, 6.2.3], A◦is the set of all power-bounded
elements of A, and A◦◦is the set of all topologically nilpotent elements.
Hence a choice of a presentation α: T n
K →A induces surjections
T n
K
◦
−→
A◦
T n
K
◦◦
−→
A◦◦.
(iii) is due to the surjectivity of the ﬁrst arrow. By the surjectivity of these
arrows and 3.2, we have (v).
Deﬁnition 3.4. An R-algebra A is said to be admissible if A is (π)-adically
completed, ﬂat over R, and topologically of ﬁnite type over R.
Remark 3.5. By [BL93, 1.1 (c)], any admissible R-algebra A is topologi-
cally of ﬁnite presentation, i.e., there exists a ﬁnitely generated ideal a in
R{t1, . . . , tn} such that R{t1, . . . , tn}/a ∼= A.
Deﬁnition 3.6 (Formal model and Analytic reduction). Let X = SpmA
be an aﬃnoid over K.
Then the formal scheme X = Spf A◦over R is
called the formal model of X, and the algebraic scheme X = SpecA over k
is called the analytic reduction of X.
We deﬁne the so-called reduction map
RedX : X = SpmA −→X = Spec A
by a 7→a ∩A◦/a ∩A◦◦.
Proposition 3.7. The map RedX is continuous with respect to the Zariski
topology of X and the G-topology of X; it maps X surjectively onto the set
of all closed points of X.
Proof. Let us consider the aﬃne open set Uf = SpecAf of Spec A relevant
to f ∈A. Take f ∈A◦from the residue class f. The function f takes values
less than equal to 1 on SpmA. So Uf = {x ∈SpmA | |f(x)| = 1} is a rational
subdomain whose associated aﬃnoid is SpmA{f, f −1}. Since the condition
214
A. RAPID COURSE IN p-ADIC ANALYSIS.
|f(x)| = 1 is equivalent to f(RedX(x))̸ = 0, we have Red−1
X (Uf) = Uf. Then
the ﬁrst assertion follows. The last one is almost trivial.
Example 3.8 (Analytic reduction of the unit disk). Let us consider the an-
alytic reduction of the unit disk D1 = D(0, 1+) = SpmK{T} (here we as-
sume that K is algebraically closed for simplicity). The analytic reduction
is given by the aﬃne line A1
k = Spec k[T]. The reduction map RedD1 maps
all “interior” points, i.e. those points lying in D(0, 1−) to the origin in A1
k,
and the other points to the non-zero points. If we identify D1 and R, A1
kand
k, then this is nothing but the mapping obtained by the reduction modulo
m.
It is very important to see how the formal models behave under localiza-
tion of aﬃnoids. Let X = SpmA be an aﬃnoid over K and f0, . . . , fn ∈A a
sequence of elements which does not have common zeros on SpmA. We con-
sider the admissible covering X = S
i Ui consisting of rational subdomains
Ui = {x ∈X | |fj(x)| ≤|fi(x)| for j̸ = i};
by multiplying a suitable power of π, we may assume that each fi belongs
to A◦. For each i,
Ui = SpmA
f0
fi
, . . . , fn
fi

,
and then the corresponding formal model is given by
Ui = Spf A◦
f0
fi
, . . . , fn
fi

/ ((π)−torsions) .
These formal schemes glue and the resulting morphism
[
0≤i≤n
Ui −→X = Spf A◦
is the formal blow-up along the ideal a = (f0, . . . , fn) ⊂A◦. We note here
that the ideal a contains a power of π, or what amounts to the same, a is
an open ideal, for aA = A.
This simple observation indicates:
Slogan (vague): Reﬁnements of admissible coverings corresponds to formal
blow-up’s along open coherent ideals.
Example 3.9. Let us assume in this example that K is algebraically closed.
We consider the admissible covering D1 = U1 ∪U2 of the unit disk D1 =
SpmK{T} given by
U1
=
{z ∈K | |z| ≤|π|}
=
SpmK
 T
π
	
,
U2
=
{z ∈K | |π| ≤|z| ≤1}
=
SpmK

T, π
T
	
.
The corresponding formal models are
U1
=
Spf R
 T
π
	
=
Spf R {T, U} /(πU −T),
U2
=
Spf R

T, π
T
	
=
Spf R {T, V } /(TV −π)
3. RELATION WITH FORMAL GEOMETRY.
215
respectively. We glue them as U = V −1 and get U1 ∪U2 →D1 = Spf R{T},
which is the formal blow-up along the ideal (π, T). Meanwhile, the analytic
reduction is obtained by gluing the following two aﬃne sets:
U1
=
Spec k [T] ,
U2
=
Spec k [T, V ] /(TV ),
this is the normal crossing of the aﬃne line with coordinate T and the
projective line with the inhomogeneous coordinate V .
We are going to state the Raynaud’s theorem, which provides a close
relationship between rigid geometry and formal geometry; we need some
terminology:
Deﬁnition 3.10 (Admissible formal scheme). An R-formal scheme(2) X is
said to be admissible if it is Zariski locally isomorphic to admissible Spf A
with A admissible in the sense of Deﬁnition 3.4.
Deﬁnition 3.11 (Admissible formal blow-up). Let X be an admissible for-
mal scheme. An admissible formal blow-up of X is the formal blow-up along
a coherent open ideal I ⊂OX, i.e.,
X′ = lim
−→
λ
Proj
∞
M
n=0

In ⊗OX OX/πλ
−→X.
We are going to construct the functor from the category of admissible
formal schemes to the category of rigid analytic spaces; let us start by ob-
serving the aﬃne case. From an aﬃne admissible formal scheme X = Spf A,
it is easy to get the corresponding rigid analytic space: we just set
Arig : = A ⊗R K
which is an aﬃnoid algebra over K. If A is presented as A = R{t1, . . . , tn}/a,
then K{t1, . . . , tn}/aK{t1, . . . , tn} gives a presentation of Arig.
To globalize, we need to see the compatibility with localization. Let us
consider the completed localization A{f −1} of A with respect to f ∈A. The
corresponding aﬃnoid algebra is
A{f −1} ⊗R K
=
A{T}/(1 −Tf) ⊗R K
=
Arig{T}/(1 −Tf)
=
Arig{f −1},
and the latter is the aﬃnoid algebra attached to the rational subdomain
{x ∈SpmArig | |f| ≥1};
this means that the completed localization of formal schemes just corre-
sponds to the localization of rigid spaces with respect to the G-topology. So
we globalize the recipe as above to obtain the functor
Rig: X 7→Xrig
from admissible formal R-schemes to K-rigid analytic spaces.
The rigid
analytic space Xrig is called the Raynaud generic ﬁber of X.
(2)We follow [EGA I, §10] for generalities of formal schemes.
216
A. RAPID COURSE IN p-ADIC ANALYSIS.
Proposition 3.12. The functor Rig maps admissible formal blow-up’s of ad-
missible formal schemes to isomorphisms of rigid analytic spaces.
Proof. This has already been essentially shown just before the Slogan.
Indeed, we may limit ourselves to the aﬃne case, for the centers of blow-up’s
are coherent. We have seen in this case that the Raynaud generic ﬁber of
admissible formal blow-up’s is the decomposition into rational subdomains,
which does not change the analytic structure.
Now we state the theorem of Raynaud:
Theorem 3.13 (Raynaud 1972). The functor gives the equivalence of the
following categories,
(i) the category of quasi-compact admissible formal R-schemes, localized
by admissible formal blow-up’s,
(ii) the category of quasi-compact and quasi-separated rigid analytic spaces
over K.
The reader ﬁnds a nice comprehensive account of the proof of this the-
orem in [BL93].

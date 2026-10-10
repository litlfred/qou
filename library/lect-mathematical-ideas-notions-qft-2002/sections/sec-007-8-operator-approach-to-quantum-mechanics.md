---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: sec-007-8-operator-approach-to-quantum-mechanics
section_title: "Operator approach to quantum mechanics"
section_number: "8"
pages: 54-61
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
toc_source: inferred
text_source: text rebuilt from glyph codes of the ps2pdf'd dvips PostScript (bitmap Type-3 fonts carry raw TeX OT1 codes; ps2pdf reports 'c' as U+0020, so a char-level rebuild maps it back and expands ligatures); prose good, display math flattened
---
8. Operator approach to quantum mechanics
In mechanics and field theory (both classical and quantum), there are two main
languages – Lagrangian and Hamiltonian. In the classical setting, the Lagrangian
language is the language of variational calculus (i.e. one studies extremals of the
action functional), while the Hamiltonian language is that of symplectic geometry
and Hamilton equations. Correspondingly, in the quantum setting, the Lagrangian
language is the language of path integrals, while the Hamiltonian language is the
language of operators and Schr¨odinger equation. We have now studied the first one
(at least in perturbation expansion) and are passing to the second.
8.1. Hamilton's equations in classical mechanics. We start with recalling the
Lagrangian formalism of classical mechanics. For more details, we refer the reader
to the excellent book of Arnold “Mathematical methods of classical mechanics”.
Consider the motion of a classical particle (or system of particles). The position
of a particle is described by a point q of the configuration space X, which we will
assume to be a manifold. The Lagrangian of the system is a (smooth) function
L : T X ! R on the total space of the tangent bundle of X. Then the action
R
functional is S(q) = L(q; q_)dt. The trajectories of the particle are the extremals
of S. The condition for q(t) to be an extremal of S is equivalent to the Euler-
Lagrange equation (=the equation of motion), which in local coordinates has the
form
d cL cL
( ) = :
dt cq_ cq
2
For example, if X is a Riemannian manifold, and L(q; v) = v =2 − U(q), where
U : X ! R is a potential function, then the Euler-Lagrange equation is the Newton
equation
q¨ = −gradU(q);
where q¨ = rq_q_ is the covariant derivative with respect to the Levi-Civita connec-
tion.
Consider now a system with Lagrangian L(q; v), whose differential with respect

to v (for fixed q) is a diffeomorphism TqX ! Tq X. This is definitely true in the
above special case of Riemannian X.
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 55
Definition 8.1. The Hamiltonian (or energy function) of the system with La-

grangian L is the function H : T X ! R, which is the Legendre transform of L
along fibers; that is, H(q; p) = pv0 − L(q; v0), where v0 is the (unique) critical point

of pv − L(q; v). The manifold T X is called the phase space (or space of states).
The variable p is called the momentum variable.
2 2
For example, if L = v =2 − U(q), then H(q; p) = p =2 + U(q).
Remark. Since Legendre transform is involutive, we also have that the La-
grangian is the fiberwise Legendre transform of the Hamiltonian.
Let qi be local coordinates on X. This coordinate system defines a coordinate

system (qi; pi) on T X.
Proposition 8.2. The equations of motion are equivalent to the Hamilton equa-
tions
cH cH
q_i = ; p_i = − ;
cpi cqi
in the sense that they are obtained from Hamilton's equations by elimination of pi.
It is useful to write Hamilton's equations in terms of Poisson brackets. Recall that

the manifold T X has a canonical symplectic structure !. In fact, ! = dff, where
 
ff is a canonical 1-form on T M constructed as follows: for any z 2 T(q;p)(T X),

ff(z) = (p; d(q; p)z), where  : T X ! X is the projection. In local coordinates,
P P
we have ff = pidqi, and ! = dpi ^ dqi.

Now let (M; !) be a symplectic manifold (in our case M = T X). Since ! is
−1
nondegenerate, one can define the Poisson bivector ! , which is a section of the
2
bundle ^ T M. Now, given any two smooth functions f; g on M, one can define a
third function – their Poisson bracket
−1
ff; gg = (df 
 dg; ! )
This operation is skew-symmetric and satisfies Jacobi identity, i.e. it is a Lie bracket
1 
on C (M). For M = T X, in local coordinates we have
 
X
cf cg cf cg
ff; gg = − :
cqi cpi cpi cqi
i
This shows that Hamilton's equations can be written in the following manner in
terms of Poisson brackets:
d
(21) f(q(t); p(t)) = ff; Hg(q(t); p(t)):
dt
1 
for any smooth function (“classical observable”) f 2 C (T X). In other words,
Hamilton's equations say that the rate of change of the observed value of f equals
the observed value of ff; Hg.
Note that for a given Lagrangian, the unique function H (up to adding a con-
stant) for which equations (21) are equivalent to the equations of motion is the
Hamiltonian. This provides another definition of the Hamiltonian, which does not
use the notion of the Legendre transform.
8.2. Hamiltonians in quantum mechanics. The yoga of quantization says that
to quantize classical mechanics on a manifold X we need to replace the classical
 2
space of states T X by the quantum space of states – the Hilbert space H = L (X)
on square integrable complex half-densities on X (or, more precisely, the corre-
sponding projective space). Further, we need to replace classical observables, i.e.
56 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
1  ^
real functions f 2 C (T X), by quantum observables f, which are (unbounded)
self-adjoint operators on H (not commuting with each other, in general). Then the
(expected) value of an observable A at a state c 2 H of unit norm is by definition
(c; Ac).
^
The operators f should linearly depend on f. More importantly, they should
depend on a positive real parameter ~ called the Planck constant, and satisfy the
following relation:
^ “ 2
[f; g^] = i~ff; gg + O(~ ); ~ ! 0:
Since the role of Poisson brackets of functions is played in quantum mechanics
by commutators of operators, this relation expresses the condition that classical
mechanics should be the limit of quantum mechanics as ~ ! 0.
We must immediately disappoint the reader by confessing that there is no canon-
^
ical choice of the quantization map f ! f. Nevertheless, there are some standard
^
choices of f for particular f, which we will now discuss.
Let us restrict ourselves to the situation X = R, so on the phase space we have
coordinates q (position) and p (momentum). In this case there are the following
standard conventions.
^
1. f = f(q) (multiplication operator by f(q)) when f is independent of p.
2. pcm ! (−i~ d )m.
dq
(Note that these conventions satisfy our condition, since [q^; p^] = i~, while fq; pg =
1.)
2
Example. For the classical Hamiltonian H = p =2 + U(q) considered above,
2 2
^ ~ d
the quantization will be H = − 2 dq2 + U(q).
Remark. The extension of these conventions to other functions is not unique.
However, such an extension will not be used, so we will not specify it.
Now let us see what the quantum analog of Hamilton's equations should be. In
accordance with the outlined quantization yoga, Poisson brackets should be replaced
−1
in quantum theory by commutators (with coeÆcient (i~) = −i=~). Thus, the
Hamilton's equation should be replaced by the equation
^
d [A; H] i
^
(c(t); Ac(t)) = (c(t); c(t)) = − (c(t); [A; H]c(t));
dt i~ ~
^
where (; ) is the Hermitian form on H (antilinear on the first factor) and H is some
quantization of the classical Hamiltonian H. Since this equation must hold for any
A, it is equivalent to the Schr¨odinger equation
i
_ ^
c = − Hc:
~
Thus, the quantum analog of the Hamilton equation is the Schr¨odinger equation.
Remark. This “derivation” of the Schr¨odinger equation is definitely not a
mathematical argument. It is merely a reasoning aimed to motivate a definition.
The general solution of the Schr¨odinger equation has the form
−itH^ =~
c(t) = e c(0):
Therefore, for any quantum observable A it is reasonable to define a new observable
itH^=~ −itH^=~
A(t) = e A(0)e (such that to observe A(t) is the same as to evolve for
time t and then observe A). The observable A(t) satisfies the equation
0 ^
A (t) = −i[A(t); H]=~;
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 57
and we have
(c(t); Ac(t)) = (c(0); A(t)c(0)):
The two sides of this equation represent two pictures of quantum mechanics: Heisen-
berg's (observables change, states don't), and Schr¨odinger's (states change, observ-
ables don't). The equation expresses the equivalence of the two pictures.
8.3. Feynman-Kac formula. Let us consider a 1-duimensional particle with po-
P
2 2 j
tential U(q) = m q + j3 gjq =j!. Let us assume that U  0 and U(q) ! 1
2 2
^ ~ d
as jqj ! 1. In this case, the operator H = − 2 dq2 + U(q) is positive definite,
and its spectrum is discrete. In particular, we have unique lowest eigenvector 
,
which is given by a positive function with norm 1. The correlation functions in the
Hamiltonian setting are defined by the formula
Ham
Gn (t1; :::; tn) := (
; q(t1):::q(tn)
):
Remark 1. The vecor 
 is called the ground, or vacuum state, since it has
lowest energy, and physicists often shift the Hamiltonian by a constant, so that the
energy of this state is zero (i.e. there is no matter).
Remark 2. Physicists usually write the inner product (v; Aw) as < vjAjw >.
In particular, 
 is written as < 0j or j0 >.
Ham
Theorem 8.3. (Feynman-Kac formula) If t1  :::  tn then the function Gn
admits an asymptotic expansion in ~ (near ~ = 0), which coincides with the path
M
integral correlation function G constructed above. Equivalently, the Wick rotated
n
Ham E
function Gn (−it1; :::; −itn) equals Gn .
This theorem plays a central role in quantum mechanics, and we will prove it
below. Before we do so, let us formulate an analog of this theorem for “quantum
mechanics on the circle”.
Let Gn;L(t1; :::; tn) denote the correlation function on the circle of length L (for
0 ≤ tn ≤ ::: ≤ t1 ≤ L), and let ZL be the partition function on the circle of length
L, defined from path integrals. Also, let
Ham −LH^=~
ZL = Tr(e );
and
−LH^ =~
Tr(q(−itn):::q(−it1)e )
Gn;L(t1; :::; tn) = −LH^=~
Tr(e )
Ham Ham
Theorem 8.4. (Feynman-Kac formula on the circle) The functions Z , G
L n;L
admit asymptotic expansions in ~, which coincide with the functions ZL and Gn;L
computed from path integrals.
Note that Theorem 8.3 is obtained from Theorem 8.4 by sending L to infinity.
Thus, it is suÆcient to prove Theorem 8.4.
E
Remark. As we mentioned before, the function G can be defined by means
n
Ham E
of Wiener integral, and the equality Gn (−it1; :::; −itn) = Gn (t1; :::; tn) actually
holds for numerical values of ~, and not only in the sense of power series expansions.
Ham Ham
The same applies to the equalities ZL = ZL, Gn;L = Gn;L. However, these results
is technically more complicated and are beyond the scope of these notes.
Example. Consider the case of the quadratic potential. By renormalizing vari-
2
ables, we can assume that ~ = m = 1, so U = q =2. In this case we know that
58 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
1 ^
ZL = 2 sinh(L=2) . On the other hand, H is the Hamiltonian of the quantum har-
monic oscillator:
2 2
1 d q
^
H = − + :
2
2 dq 2
2
−x =2
The eigenvectors of this operator are well known: they are Hk(x)e , where Hk
are the Hermite polynomials (k  0), and the eigenvalues are k + 1=2 (see Theorem
4.10). Hence,
1
Ham −L=2 −3L=2
ZL = e + e + ::: = L=2 −L=2 = ZL;
e − e
as expected from the Feynman-Kac formula. (This shows the significance of the
choice C = 1=2 in the normalization of ZL).
8.4. Proof of the Feynman-Kac formula in the free case. Consider again
2 2
^ 1 d q
the quadratic Hamiltonian H = −2 dq2 + 2 . Note that it can be written in the
form
^ y
H = a a + 1=2;
where a = p1 ( d +q), ay = p1 (− d +q). The operators a; ay define a representation
2 dq 2 dq
of the Heisenberg algebra on H:
y
[a; a ] = 1:
2
^ y n −q =2
Thus the eigenvectors of H are (a ) 
 (where 
 = e ) is the lowest eigenvector),
1
and the eigenvalues n + (as we already saw before in Theorem 4.10).
2
y
Remark. The operators a and a are called the annihilation and creation oper-
^
ators, since a
 = 0, while all eigenvectors of H can be “created” from 
 by action
y
of powers of a .
Now, we have
1
y
q(0) = q = p (a + a ):
2
y y y y
Since [a a; a] = −a, [a a; a ] = a , we have
1 y y 1
ita a y −ita a −it it y
q(t) = p e (a + a )e = p (e a + e a )
2 2
This shows that
Tr(Qn (etj ay + e−tj a)e−L(aya+21 ))
Ham −n=2 j=1
Gn;L (−it1; :::; −itn) = 2 y 1 :
Tr(e−L(a a+ 2 ))
t1 y
Now we can easily prove Theorem 8.4. Indeed, let us move the terms e a and
−t1
e a around the trace (using the cyclic property of the trace). This will yield,
after a short calculation,
Xn t1−tj tj−t1
1 e e
Ham
Gn;L (t1; :::; tn) = Gn−2;L(t2; :::; tj−1; tj+1; :::; tn)( − ) =
L −L
2 e − 1 e − 1
j=2
n
X
Gn−2;L(t2; :::; tj−1; tj+1; :::; tn)GL(t1 − tj):
j=2
This implies the theorem by induction.
Note that in the quadratic case there is no formal expansions and the Feynman-
Kac formula holds as an equality between usual functions.
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 59
8.5. Proof of the Feynman-Kac formula (general case). Now we consider
P
2 2 k
an arbitrary potential U = m q =2 + V (q), where V (q) = k3 gkq =k!. For
simplicity we will assume that ~ = 1 and coeÆcients gj as formal parameters (this
does not cause a loss of generality, as this situation can be achieved by rescaling).
Ham −LH^
Let us first consider the case of partition function. We have Z = Tr(e ) =
L
−L(H^0+V ) ^ 1 d2 1 2 2
Tr(e ), where H0 = −2 dq2 + 2 m q is the free (=quadratic) part of the
Hamiltonian. Since gj are formal parameters, we have a series expansion
(22)
Z
X
−L(H^0+V ) −LH^0 N −(L−s1)H^0 −(s1−s2)H^0 −(sn−1−sn)H^0 −snH^0
e = e + (−1) e V e V:::e V e ds
N1 Ls1:::sN0
This follows from the general fact that in the (completed) free algebra with gener-
ators A; B, one has
Z
X
A+B A (1−s1)A (s1−s2)A (sN−1−sN)A sNA
(23) e = e + e Be B:::e Be ds
N1 1s1:::sN0
(check this identity!).
Equation 22 shows that
1
X X
Ham N gj1:::gjN j1 jN −LH^0
ZL = (−1) Tr(q0(−is1) :::q0(−isN) e );
j1!:::jN !
N0 j1;:::;jN=3
where q0(t) is the operator q(t) in the free theory, associated to the potential
2 2
m q =2.
Since the Feynman-Kac formula for the free theory has been proved, the trace
on the right hand side can be evaluated as a sum over pairings. To see what exactly
is obtained, let us collect the terms corresponding to all permutations of j1; ::; jN
together. This means that the summation variables will be the numbers i3; i4; ::
j
of occurences of 3; 4; :: among j1; :::; jN . Further, to every factor q0(−is) will be
assigned a j-valent vertex, with a variable s attached to it, and it is easy to see
Ham
that Z equals the sum over all ways of connecting the vertices (i.e. Feynman
L
diagrams −) of integrals
Z
Y
GL(sv − sw)ds;
0≤s1;:::;sN≤L edgesv−w
Q(−gk)ik Ham
multiplied by the coeÆcients jAut−j . Thus, ZL = ZL, as desired.
Now let us consider correlation functions. Thus we have to compute
−(L−t1)H^ −(t1−t2)H^ −tnH^
Tr(e qe q:::qe ):
Explanding each exponential inside the trace as above, we will clearly get the same
Feynman diagram sum, except that the Feynman diagrams will contain n external
Ham
vertices marked by variables t1; :::; tn. This implies that Gn;L = Gn;L, and we are
done.
8.6. The massless case. Consider now the massless case, m = 0, in the Hamilton-
2 2
2 ^ ~ d
ian setting. For maps q : R ! R, we have H = L (R), and H = − 2 dq2 . This oper-
ator has continuous spectrum, and there is no lowest eigenvector 
 (more precisely,
2
there is a lowest eigenvector 
 = 1, but it is not in L ), which means that we can-
not define the correlation functions in the usual way, i.e. as < 
; q(t1):::q(tn)
 >.
60 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
(This is the reflection, in the Hamiltonian setting, of the diÆculties related to the
growth of the Green's function at infinity, which we encountered in the Lagrangian
setting).
1
Consider now the case q : R ! S = R=2rZ. In this case, we have the same
2 1
Hamiltonian but acting in the space H := L (S ). The eigenvectors of this operator
iNq=r 2 2 2
are e , with eigenvalues ~ N =2r . In particular, the lowest eigenvector is

 = 1. Thus the Hamiltonian correlation functions (in the Euclidean setting, for
t1  :::  tn) are
t1H^=~ ip1q=r (t2−t1)H^=~ ipnq=r −tnH^=~
(
; e e e :::e e 
) =
~ P 2
e 2r2 (tj−tj+1)(p1+:::pj) ;
which is equal to the correlation function in the Lagrangian setting. Thus the
Feynman-Kac formula holds.
Now we pass to the case of quantum mechanics on the circle. First consider
−LH^=~ P −N2L~=2r2
circle valued maps q. In this case, we have Tr(e ) = e , and
N
X P
Tr(et1H^=~eip1q=re(t2−t1)H^ =~:::eipnq=re(L−tn)H^ =~) = e 2r~2 nj=0(tj−tj+1)(N−p1−:::−pj)2;
N
where tn+1 := L, t0 := 0. Simplifying this expression, we obtain
~ P 2 X ~ 2 Pn
e 2r2 j(tj−tj+1)(p1+:::+pj) e−2r2 (LN +2 j=1 pjtjN) =
N
e2r~2 Pj(tj−tj+1)(p1+:::+pj)2( ~ X pjtj; L~):
2 2
2ir r
Comparing with (20), we see that the Feynman-Kac formula holds, and follows
from the modular invariance of the theta-function:
2
2 2 2u 4
−2 u =T
(u; T ) = e ( ; ):
iT T
(which follows from the Poisson summation formula).
Note that the Feynman-Kac formula would be false if in the Lagrangian set-
ting we had ignored the topologically nontrivial maps. Thus we may say that the
Feynman-Kac formula “sees topology”. This ability of the Feynman-Kac formula
to “see topology” (in much more complex situations) lies at the foundation of many
interrelations between geometry and quantum field theory.
Remark. It should be noted that the contributions of topologically nontrivial
maps from the source circle to the target circle are, strictly speaking, beyond our
usual setting of perturbation theory, since they are exponentially small in ~. To be
specific, the contribution from maps of degree N mostly comes from those maps
which are close to the minimal action map qN (t) = 2tNr=L, so it is of the order
2 2 2
−2 N r =L~
e . The maps qN(t) are the simplest examples of “instantons” – noncon-
stant solutions of the classical equations of motion, which have finite action (and
are nontrivial in the topological sense). Exponentially small contributions to the
path integral coming from integration over neighborhoods of instantons are called
“instanton corrections to the perturbation series”.
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 61

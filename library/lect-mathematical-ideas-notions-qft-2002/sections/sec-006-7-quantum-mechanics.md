---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: sec-006-7-quantum-mechanics
section_title: "Quantum mechanics"
section_number: "7"
pages: 41-54
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
toc_source: inferred
text_source: text rebuilt from glyph codes of the ps2pdf'd dvips PostScript (bitmap Type-3 fonts carry raw TeX OT1 codes; ps2pdf reports 'c' as U+0020, so a char-level rebuild maps it back and expands ligatures); prose good, display math flattened
doc_brief: "Mathematical ideas and notions of quantum field theory — 1. Generalities on quantum field theory 1.1. Classical mechanics. In classical mechanics, we study the motion of a par- ticle."
---
7. Quantum mechanics
So far we have considered quantum field theory with 0-dimensional spacetime
(to make a joke, one may say that the dimension of the space is −1). In this section,
we will move closer to actual physics: we will consider 1-dimensional spacetime, i.e.
the dimension of the space is 0. This does not mean that we will study motion in
a 0-dimensional space (which would be really a pity) but just means that we will
consider only point-like quantum objects (particles) and not extended quantum
objects (fields). In other words, we will be in the realm of quantum mechanics.
42 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
7.1. The path integral in quantum mechanics. Let U(q) be a smooth function
0
on the real line (the potential). We will assume that U(0) = 0, U (0) = 0, and
00 2
U (0) = m , where m > 0.
Remark. In quantum field theory the parameter m in the potential is called
the mass parameter. To be more precise, in classical mechanics it has the meaning
of frequency ! of oscillations. However, in quantum theory thanks to Einstein
frequency is identified with energy (E = ~!=2), while in relativisitic theory energy
2
is identified with mass (again thanks to Einstein, E = mc ).
We want to construct the theory of a quantum particle moving in the potential
field U(q). According to what we discussed before, this means that we want to give
sense to and to evaluate the normalized correlation functions
R
iS(q)=~
q(t1) : : : q(tn)e Dq
< q(t1) : : : q(tn) >:= R ;
iS(q)=~
e Dq
R
2
where S(q) = L(q)dt, and L(q) = q_ =2 − U(q).
As we discussed, such integrals cannot be handled rigorously by means of measure
theory if ~ is a positive number; so we will only define these path integrals “in
perturbation theory”, i.e. as formal series in ~.
Before giving this (fully rigorous) definition, we will explain the motivation be-
hind it. We warn the reader that this explanation is heuristic and involves steps
which are mathematically non-rigorous (or “formal” in the language of physicists).
7.2. Wick rotation. In x1 we discussed path integrals with imaginary exponential
(quantum mechanics), as well as real exponential (Brownian motion). If ~ is a
number, then the integrals with imaginary exonential cannot be defined measure
theoretically. Therefore, people study integrals with real exponential (which can
be rigorously defined), and then perform a special analytic continuation procedure
called the Wick rotation.
In our formal setting (~ is a formal parameter), one can actually define the
integrals in both the real and the imaginary case. Still, the real case is a bit
easier, and thus the Wick rotation is still useful. Besides, the Wick rotation is very
important conceptually. Therefore, while it is not technically necessary, we start
with introducing the Wick rotation here.
M
Namely, let us denote < q(t1):::q(tn) > by Gn (t1; :::; tn), and “formally” make a
M
change of variable 
 = it in the formula for Gn (t1; :::; tn). Let q(t) = q(
). Then,
taking into account that d
 = idt, dq=dt = idq=d
 we get
M R q(
1) : : : q(
n)e− R [21 (ddq
 )2+U(q)]=~Dq
Gn (t1; :::; tn) = R e− R [ 12(ddq
 )2+U(q)]=~Dq :
This shows that
M E
Gn (t1; :::; tn) = Gn (it1; :::; itn);
where
R
−SE(q)=~
E q(t1) : : : q(tn)e Dq
Gn (t1; :::; tn) := R e−SE(q)=~Dq :
R
2
where SE(q) = LE(q)dt, and LE(q) = q_ =2 + U(q) (i.e. LE is obtained from L
by replacing U with −U).
This manipulation certainly does not make rigorous sense, but it motivates the
following definition.
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 43
M
Definition 7.1. The function Gn (t1; :::; tn) (ti 2 R) is the analytic continuation of
E
the function Gn (s1; :::; sn) from the point (t1; :::; tn) to the point (it1; :::; itn) along
i
the path e (t1; :::; tn), 0 ≤  ≤ =2.
E
Of course, this definition will only make sense if we define the function Gn (t1; :::; tn)
and show that it admits the required analytic continuation. This will be done below.
M
Terminological remark. The function Gn (t1; :::; tn) is called the Minkowskian
E
(time ordered) correlation function, while Gn (t1; :::; tn) is called the Euclidean cor-
relation function (hence the notation). This terminology will be explained later,
when we consider relativistic field theory.
From now on, we will mostly deal with Euclidean correlation functions, and
therefore will omit the superscript E when there is no danger of confusion.
7.3. Definition of Euclidean correlation functions. Now our job is to define
the Euclidean correlation functions Gn(t1; :::; tn). Our strategy (which will also
be used in field theory) will be as follows. Recall that if our integrals were finite
dimensional then by Feynman's theorem the expansion of the correlation functions
in ~ would be given by a sum of amplitudes of Feynman diagrams. So, in the infinite
dimensional case, we will use the sum over Feynman diagrams as a definition of
correlation functions.
More specifically, because of conditions on U we have an action functional with-
out constant and linear terms in q, so that the correlation function Gn(t1; :::; tn)
should be given by the sum
X b(−)
~
(17) Gn(t1; :::; tn) = F−(`1; : : : ; `n);
jAut(−)j
−2G (n)
3
Thus, we should make sense of (=define) the amplitudes F− in our situation. For
this purpose, we need to define the following objects.
1. The space V .
−1 
2. The form B on V which defines B on V .
3. The tensors corresponding to non-quadratic terms in the action.
4. The covectors `i.
It is clear how to define these objects naturally. Namely, V should be a space of
functions on R with some decay conditions. There are many choices for V , which
do not affect the final result; for instance, a good choice (which we will make) is the
1 
space C (R) of compactly supported smooth functions on R, Thus V is the space
0
of generalized functions on R. Note that V is equipped with the inner product
R
(f; g) = f(x)g(x)dx.
R
The form B, by analogy with the finite dimensional case, should be twice the
R
2 2 2
quadratic part of the action. In other words, B(q; q) = (q_ + m q )dt = (Aq; q),
2 2 2 −1 −1
where A is the operator −d =dt + m . This means that B (f; f) = (A f; f)
−1
The operator A is an integral operator, with kernel K(x; y) = G(x − y),
where G(x) is the Green's function of A, i.e. the fundamental (decaying at infinity)
solution of the differential equation (AG)(x) = Æ(x). It is straightforward to find
that
−mjxj
G(x) = e =2m:
−1  
(thus B is actually defined not on the whole V but on a dense subspace of V ).
Remark. Here we see the usefulness of the Wick rotation. Namely, the spectrum
2 2
of A in L is [m ; +1), so it is invertible and the inverse is bounded. However, if we
44 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
0 2 2 2
did not make a Wick rotation, we would deal with the operator A = −d =dt −m ,
2
whose spectrum is [−m ; +1), i.e. contains 0, so that the operator is not invertible
in the naive sense.
To make sense of the cubic and higher terms in the action as tensors, consider the
2 2
decomposition of U in the (asymptotic) Taylor series at x = 0: U(x) = m x =2 +
P
n
n3 anx =n!. This shows that cubic and higher terms in the action have the form
Z
r
Br(q; q; ; :::; q) = q (t)dt
r 
Thus Br(q1; :::; qr) is an element of (S V ) given by the generalized function Æt1=:::=tr
(the delta function of the diagonal).
Finally, the functionals `i are given by `i(q) = q(ti), so `i = Æ(t − ti).
This leads to the following Feynman rules of defining the amplitude of a diagram
−.
1. To the i-th external vertex of − assign the number ti.
2. To each internal vertex j of −, assign a variable sj.
0
3. For each internal edge connecting vertices j and j , write G(sj − sj0).
4. For each external edge connecting i and j write G(ti − sj).
0
5. For each external edge connecting i and i write G(ti − ti0).
6. Let G−(t; s) be the product of all these functions.
Q R
7. Let F−(`1; :::`n) = j(−av(j)) G−(t; s)ds, where v(j) is the valency of j.
We are finally able to give the following definition.
Definition 7.2. The function Gn(t1; :::; tn) is defined by the formula 17.
Remark. Note that the integrals defining F− are convergent since the integrand
always decays exponentially at infinity. It is, however, crucial that we consider only
graphs without components having no external vertices; for example, if − has a
single 4-valent vertex connected to itself by two loops (Fig.23) then the amplitude
R
2
integral involves G(0) ds, which is obviously divergent.
R
Figure 23
With this definition, the function Gn(t1; :::; tn) is a Laurent series in ~, whose
coeÆcients are symmetric functions of t1; :::; tn, given by linear combinations of
explicit (and convergent) finite dimensional integrals. Furthermore, it is easy to
see that these integrals are in fact computable in elementary functions, i.e. are (in
the region t1  :::  tn) linear combinations of products of functions of the form
r ati
t e . This implies the existence of the analytic continuation required in the Wick
i
rotation procedure.
Remark. An alternative setting for making this definition is to assume that ai
are formal parameters. In this case, ~ can be given a numerical value, e.g. ~ = 1,
and the function Gn will be a well defined power series in a3; a4; :::.
2 2
Example 1. The free theory: U(q) = m q =2. In this case, there is no internal
vertices, and hence we have
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 45
Proposition 7.3. (Wick's theorem) One has Gn(t1; :::; tn) = 0 if n is odd, and
X Y
k
G2k(t1; :::; t2k) = ~ G(ti − t(i)):
2k i2f1;:::;2kg=
In particular, G2(t1; t2) = ~G(t1 − t2). In other words, G2(t1; t2) is (proportional
to) the Green's function. Motivated by this, physicists often refer to correlation
functions of a quantum field theory as Green's functions.
t1 t2
Figure 24
2 2 4
Example 2. Consider the potential U(q) = m q =2 + gq =24, and set ~ = 1.
2
In this case, let us calculate the 2-point correlation function modulo g . In other
words, we have to compute the coeÆcient of g in this function. Thus we have to
consider Feynman diagrams with two external edges and one internal vertex. Such
a diagram − is unique: it consists of one edge with a loop attached in the middle
(Fig. 24). This diagram has automorphism group Z=2. The amplitude of this
diagram is
Z Z
g
−m(js−t1j+js−t2j)
F− = −g G(s; t1)G(s; t2)G(s; s)ds = e ds
3
R 8m R
Because of symmetry in t1 and t2, we may assume that t1  t2. Splitting the
integral in a sum of three integrals, over (−1; t2]; [t2; t1], and [t1; 1), respectively
we get:
e
G2(t1; t2) = G(t1 − t2);
where
1 g 1
e −mjtj 2
G(t) = e (1 − ( + jtj)) + O(g ):
2
2m 8m m
This expression is called the 1-loop approximation to the 2-point function, because
it comes from 0-loop and 1-loop Feynman diagrams.
Remark. Here we are considering quantum mechanics of a single 1-dimensional
particle. However, everything generalizes without diÆculty to the case of an n-
dimensional particle or system of particles (i.e. to path integrals over the space
of vector valued, rather than scalar, functions of one variable). Indeed, if q takes
values in a Euclidean space V then the quadratic part of the Lagrangian is of the
1 2
form (q_ −M(q)), where M is a positive definite quadratic form on V . Reducing M
2
to principal axes, we may assume that the quadratic part of the Lagrangian looks
P
1 2 2 2
like 2 i(q_i − mi qi ), which corresponds to a system of independent harmonic
oscillators. Thus in quantum theory the propagator will be the diagonal matrix
−mijt−sj
with diagonal entries e =2mi, and the correlation functions can be defined
by the usual Feynman diagram procedure.
46 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
c
7.4. Connected Green's functions. Let Gn(t1; :::; tn) be the connected Green's
functions, defined by the sum of the same amplitudes as Gn(t1; :::; tn) but taken
over connected Feynman diagrams only. It is clear that
X Y
c
Gn(t1; :::; tn) = GjSij(tj; j 2 Si):
f1;:::;ng=S1t:::tSk
c c c
For example, G2(t1; t2) = G2(t1; t2) + G1(t1)G1(t2), etc. Thus, to know the correla-
tion functions, it is suÆcient to know the connected correlation functions.
2 2
Example 1. In a free theory (U = m q =2), all connected Green's functions
except G2 vanish.
t2
t1 t3
t4
Figure 25
Example 2. Let us compute the connected 4-point function in the theory
2
associated to quartic potential U as above, modulo g . This means, we should
compute the contribution of connected Feynman diagrams with one internal vertex
and 4 external edges. Such diagram − is unique –it is the cross (with one internal
vertex), Fig.25. This diagram no nontrivial automorphisms. Thus,
Z
c 2
G4(t1; t2; t3; t4) = −g G(t1 − s)G(t2 − s)G(t3 − s)G(t4 − s)ds + O(g ):
R
It is elementary to compute this integral; we leave it as an exercise.
7.5. The clustering property. Note that the Green's function G(t) goes to zero
at infinity. This implies the following clustering property of the correlation functions
of the free theory:
lim Gn(t1; :::; tr; tr+1 + z; :::; tn + z) = Gr(t1; :::; tr)Gn−r(tr+1:::tn):
z!1
Moreover, it is easy to show that the same is true in the interacting theory (i.e.
with potential) in each degree with respect to ~ (check it!). The clustering property
can be more simply expressed by the equation
c
lim Gn(t1; :::; tr; tr+1 + z; :::; tn + z) = 0:
z!1
This property has a physical interpretation: processes distant from each other are
almost statistically independent. Thus it can be viewed as a necessary condition of
a quantum field theory to be “physically meaningful”.
Remark. Nevertheless, there exist theories (e.g. so called topological quantum
field theories) which do not satisfy the clustering property but are interesting both
form a physical and mathematical point of view.
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 47
7.6. The partition function. Let J(t)dt be a compactly supported measure on
the real line. Consider the “partition function with external current J”, which is
the formal expression
Z
−SE(q)+(J;q)
Z(J) = e ~ Dq:
Then we have a formal equality
Z
X −n
Z(J) ~
= Gn(t1; :::; tn)J(t1):::J(tn)dt1:::dtn;
Z(0) n n! Rn
which, as before, we will use as definition of Z(J)=Z(0). So the knowledge of
Z(J)=Z(0) is equivalent to the knowledge of all the Green's functions (in other
words, Z(J)=Z(0) is their generating function). Furthermore, as in the finite di-
mensional case, we have
Proposition 7.4. One has
Z
X −n
Z(J) ~
c
W (J) := ln = Gn(t1; :::; tn)J(t1):::J(tn)dt1:::dtn
Z(0) n!
n
(i.e. W is the generating function of connected Green's functions)
The proof of this proposition is the same as in the finite dimensional case.
Remark. The statement of the proposition is equivalent to the relation between
usual and connected Green's functions, given in the previous subsection.
Remark. The fact that we can only define amplitudes of graphs whose all
components have at least one 1-valent vertex (see above) means that we actually
cannot define either Z(0) or Z(J) but can only define their ratio Z(J)=Z(0).
Like in the finite dimensional case, we have an expansion
−1
W (J) = ~ W0(J) + W1(J) + ~W2(J) + :::;
where Wj are the j-loop contributions (in particular, W0 is given by a sum over
trees). Furthermore, we have explicit formulas for W0 and W1, analogously to the
finite dimensional case.
Proposition 7.5. One has
W0(J) = −SE(qJ) + (qJ ; J);
J
where qJ is the extremal of the functional SE(q) := SE(q) − (q; J) which decays at
infinity. Furthermore,
1
W1(J) = − ln det LJ;
2
2 J 2 0
where LJ is the linear operator on V such that d SE(qJ )(f1; f2) = d SE(0)(LJf1; f2).
The proof of this proposition, in particular, involves showing that qJ is well
defined and that det LJ exists. It is analogous to the proof of the same result in
the finite dimensional case which is given in x3.7 (to be precise, we gave a proof
only in the 0-loop case; but in the 1-loop case, the proof is similar). Therefore we
will not give this proof; rather, we will illustrate the statement by an example.
Example. Let U be the quartic potential and J(t) = aÆ(t). In this case,
R
J 2
S (q) = (q_ =2 + U(q))dt − aq(0). The Euler-Lagrange equation has the form
E
2 3
q¨ = m q + gq =6 − aÆ(t):
48 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
Thus, the function qJ is continuously glued from two solutions q+; q− of the non-
2 3
linear differential equation q¨ = m q + gq =6 on (−1; 0] and [0; 1), with jump of
derivative at 0 equal to −a.
The solutions q+; q− are required to decay at infinity, so they must be solutions of
2
zero energy (E = q_ =2 − U(q) = 0). Thus, by the standard formula for solutions
of Newton's equation, they are defined by the equality
q
Z Z gq2
dq dq 1 1 + 12m2 − 1
t − t = p = q = ln q :
2(E + U(q)) gq2 2m gq2
mq 1 + 12m2 1 + 12m2 + 1
After a calculation one gets
q
12m2
g
qJ(t) = ;
−1 mjtj −mjtj
C e − Ce
where C is the solution of the equation
r
−1
C + C g a
=
−1 2 2
(C − C ) 12m 2m
which is given by a power series in a with zero constant term. >From this it is
J
elementary (but somewhat lengthy) to compute W0 = −SE(qJ).
−1 2
Now, the operator LJ is given by the formula LJ = 1 + gA qJ (t) =2, where
2 2 2 −1 2
A = −d =dt + m . Thus det LJ makes sense. Indeed, the operator A qJ(t) is
−mjx−yj 2
e qJ(y)
given by the kernel , which decays exponentially at infinity; hence this
2m
−1 2
operator is trace class and therefore, 1 + gA qJ(t) =2 is determinant class.
1PI
7.7. 1-particle irreducible Green's functions. Let Gn (t1; :::; tn) denote 1-
particle irreducible Green's functions, i.e. those defined by the sum of the same
amplitudes as the usual Green's functions, but taken only over 1-particle irreducible
Feynman graphs. Define also the amputated 1-particle irreducible Green's function:
1PIa 
n 1PI
G = A G (it is defined by the same sum of amplitudes, except that instead
n n
of G(ti − sj) for external edges, we write Æ(ti − sj)).
1PIa
Let Seff(q) be the generating function of Gn i.e.,
Z
X −n
~
1PIa
Seff(q) = Gn (t1; :::; tn)q(t1):::q(tn)dt1:::dtn;
n!
n
Proposition 7.6. The function W (J) = ln(Z(J)=Z(0)) is the Legendre transform
of Seff(q), i.e. it equals −Seff(q~J ) + (J; q~J), where q~J is the extremal of −Seff(q) +
(J; q) (decaying at infinity).
The proof of this proposition is the same as in the finite dimensional case. The
proposition shows that in order to know the Green's functions, it “suÆces” to
know amputated 1-particle irreducible Green's functions (the generating function
of usual Green's functions can be reconstructed from that for 1PI Green's functions
by taking the Legendre transform and exponentiation). Which is a good news,
since there are a lot fewer 1PI diagrams than general connected diagrams.
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 49
7.8. Momentum space integration. We saw that the amplitude of a Feynman
diagram is given by an integral over the space of dimension equal to the number of
internal vertices. This is sometimes inconvenient, since even for tree diagrams such
integrals can be rather complicated. However, it turns out that if one passes to
Fourier transforms then Feynman integrals simplify and in particular the number
of integrations for a connected diagram becomes equal to the number of loops (so
for tree diagrams we have no integrations at all).
Namely, we will proceed as follows. Instead of the time variable t we will consider
the dual energy variable E. A function q(t) with compact support will be replaced
by its Fourier transform q^(E). Then, by Plancherel formula, for real functions
q1; q2, we have
Z Z
(q1; q2) = q^1(E)q^2(E)dE = q^1(E)q^2(−E)dE:
R R
This implies that the propagator is given by
Z
1
−1 ^ ^
B (f; f) = f(E)f(−E)dE
2 2
R E + m
The vertex tensors standing at k-valent vertices were Æs1=:::=sk, so they will be
replaced by ÆQ1+:::+Qk=0, where Qi are dual variables to si.
Terminological remark. Physicists refer to the time variables ti; sj as po-
sition variables, and to energy variables Ei; Qk as momentum variables, since in
relativistic mechanics (which is the setting we will deal with when we study field
theory) there is no distinction between time and position and between energy and
momentum (due to the action of the Lorenz group).
This shows that the Feynman rules “in momentum space” for a given connected
Feynman diagram − with n external vertices are as follows.
1. Orient the diagram −, so that all external edges are oriented inwards.
2. Assign variables Ei to external edges, and variables Qj to internal ones.
These variables are subject to the linear equations of “the first Kirchhof law”: at
every internal vertex, the sum of the variables corresponding to the incoming edges
equals the sum of those corresponding to the outgoing edges. Let Y (E) be the
space of solutions Q of these equations (it depends on −, but we will not write
the dependence explicitly). It is easy to show that this space is nonempty only if
P
Ei = 0, and in that case dim Y (E) equals the number of loops of − (show this!).
1 1
3. For each external edge, write Ei2+m2 , and for each internal edge, write Q2k+m2 .
Let 
−(E; Q) be the product of all these functions.
^
4. Define the momentum space amplitude of − to be the distribution F−(E) on
P
the hyperplane Ei = 0 defined by the formula
Z
Y
^
F−(E1; :::; En) = (−av(j)) 
−(E; Q)dQ:
Y (E)
j
We will regard it as a distribution on the space of all n-tuples E1; :::; En, extending
it by zero. It is clear that this distribution is independent on the orientation of −.
Remark. Here we must specify the normalization of the Lebesgue measure on
P
the space Ei = 0 and the space Y (E). The first one is just dE1:::dEn−1. To
define the second one, let YZ(0) be the set of integer elements in Y (0). Then the
measure on Y (E) is defined in such a way that the volume of Y (E)=YZ(0) is 1.
Now we have
50 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
^
Proposition 7.7. The Fourier transform of the function F−(Æt1; :::; Ætn) is F−(E1; :::; En).
Hence, the Fourier transform of the connected Green's functions is
X b(−)
~
^c ^
(18) Gn(E1; :::; En) = F−(E1; : : : ; En):
jAut(−)j
−2G (n)
3
The proof of the proposition is straightforward.
To illustrate the proposition, consider an example.
Example 1. The connected 4-point function for the quartic potential, modulo
2
g , in momentum space, looks like:
4
Y X
1
^c 2
Gn(E1; E2; E3; E4) = −g 2 2 Æ( Ei) + O(g ):
E + m
i=1 i
1 3
Q
ER1 - 	E3
5 6
−.
-
 E1 + E2 − Q I
2 E2 E4 4
Figure 26
Example 2. Let us compute the 1PI 4-point function in the same problem,
3 2
modulo g . Thus, in addition to the above, we need to compute the g coeÆcient,
which comes from 1-loop diagrams. There are three such diagrams, differing by
permutation of external edges. One of these diagrams is as follows: it has external
vertices 1; 2; 3; 4 and internal ones 5; 6 such that 1; 2 are connected to 5, 3; 4 to 6,
and 5 and 6 are connected by two edges (Fig.26). This diagram has the symmetry
group Z=2, so its contribution is
2 Z Y4 X
g dQ 1
( ) Æ( Ei):
2 2 2 2 2 2
2 R (Q + m )((E1 + E2 − Q) + m ) i=1 Ei + m
The integral inside is easy to compute for example by residues. This yields
^c
Gn(E1; E2; E3; E4) =
4 4
Y X X
1 g 1
3
−g 2 2 (1 − 2 2 )Æ( Ei) + O(g ):
i=1 Ei + m m i=2 (E1 + Ei) + 4m
7.9. The Wick rotation in momentum space. To obtain the correlation func-
tions of quantum mechanics, we should, after computing them in the Euclidean
setting, Wick rotate them back to the Minkowski setting. Let us do it at the
level of Feynman integrals in momentum space. (We could do it in position space
as well, but it is instructive for the future to do it in momentum space, since in
higher dimensional field theory which we will discuss later, the momentum space
representation is more convenient).
Consider the Euclidean propagator
Z
1
iEt
= G(t)e dt;
2 2
E + m
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 51
where G is the Green's function. When we do analytic continuation back to the
Minkowski setting, we must replace in the correlation functions the time variable t
i
with e t, where  varies from 0 and =2. In particular, the Green's function G(t)
i
must be replaced by G(e t). So we must consider
Z Z
−i
−i e
i iEt −i ie Et
G(e t)e dt = e G(t)e dt = :
−2i 2 2
e E + m
i
As  ! =2, this function tends (as a distribution) to the function lim”!0+ E2−m2+i” .
For brevity the limit sign is usually dropped and this distribution is written as
i
E2−m2+i” .
We see that in order to compute the correlation functions in momentum space in
the Minkowski setting, we should use the same Feynman rules as in the Euclidean
setting except that the propagator put on the edges should be
i
:
2 2
E − m + i”
For instance, the contribution of the diagram in Fig.26 is
2 Z Y4 X
g dQ 1
− ( 2 2 2 2 ) 2 2 Æ( Ej):
2 R (Q − m + i”)((E1 + E2 − Q) − m + i”) j=1 Ej − m + i”
7.10. Quantum mechanics on the circle. It is reasonable (at least mathemat-
ically) to consider Euclidean quantum mechanical path integrals in the case when
the time axis has been replaced with a circle of length L, i.e. t 2 R=LZ. In this
case, the theory is the same, except the Green's function G(t) is replaced by the
2 2 2
periodic solution GL(t) of the equation (−d =dt + m )f = Æ(t) on the circle. This
solution has the form
X −m(t−L=2) −m(L=2−t)
e + e
GL(t) = G(t − kL) = ; 0 ≤ t ≤ L:
mL=2 −mL=2
2m(e − e )
k2Z
We note that in the case of a circle, there is no problem with graphs without ex-
ternal edges (as integral over the circle of a constant function is convergent), and
hence one may define not only correlation functions (i.e. Z(J)=Z(0)), but also Z(0)
P
2 2 n 2 2
itself. Namely, let U(q) = m q =2+ n3 anq =n!, and let m = m0 +a2 (where ai
are formal parameters). Then we can make sense of the ratio Zm0;a;L(0)=Zm0;0;L(0)
(where Zm;a;L(0) denotes the partition function for the specified values of param-
eters; from now on the argument 0 will be dropped). Indeed, this ratio is defined
by the formula
X b(−)
Zm0;a;L ~
= F−;
Zm0;0;L jAut(−)j
−2G2(0)
which is a well defined expression.
It is instructive to compute this expression in the case a2 = a, a3 = a4 = ::: = 0.
In this case, we have only 2-valent vertices, so the only connected Feynman diagrams
are N-gons, which are 1-loop. Hence,
Zm0;a;L 1
ln = W1 = − ln det M;
Zm0;0;L 2
52 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
2 2 2 −1
where M = 1 + a(−d =dt + m ) . This determinant may be computed by look-
0
2 2 2
ing at the eigenvalues. Namely, the eigenfunctions of −d =dt + m0 in the space
2 2
1 2int=L 4 n 2
C (R=LZ) are e , with eigenvalues L2 + m0. So,
Y
a
det M = (1 + 42n2 2 ):
n2Z L2 + m0
Hence, using the Euler product formula for sinh(z), we get
Zm0;a;L sinh(m0L=2)
=
Zm0;0;L sinh(mL=2)
Remark. More informally speaking, we see that the partition function Z for
2 2 C
the theory with U = m q =2 has the form , where C is a constant of our
sinh(mL=2)
choice. Our choice from now on will be C = 1=2; we will see later why such a choice
is convenient.
7.11. The massless case. Consider now the massless case, m = 0. In this case
2
d
the propagator should be obtained by inverting the operator −dt2 , i.e. it should
be a the integral operator with kernel G(t − s), where G(t) is an even function
00
satisfying the differential equation −G (t) = Æ(t). There is a 1-parameter family
1
of such solutions, G(t) = − jtj + C. Using them (for any choice of C), one may
2
define the correlation functions of the theory by the Wick formula.
Note that the function G does not decay at infinity. Therefore, this theory will
not satisfy the clustering property (i.e. is not “physically meaningful”).
We will also have diÆculties in defining the corresponding interacting theory
(i.e. one with a non-quadratic potential), as the integrals defining the amplitudes
of Feynman diagrams will diverge. Such divergences are called infrared divergences,
since they are caused by the failure of the integrand to decay at large times (or, in
momentum space, its failure to be regular at low frequencies).
7.12. Circle valued quantum mechanics. Consider now the theory with the
same Lagrangian in which q(t) takes values in the circle of radius r, R=2rZ (the
2
“sigma-model”). We can do this at least classically, since the Lagrangian q_ =2
makes sense in this case.
Let us define the corresponding quantum theory. The main difference from
the line-valued case is that since q(t) is circle valued, we should consider not the
usual correlators < q(t1):::q(tn) >, but rather correlation functions exponentials
ip1q(t1)=r ipnq(tk)=r
< e :::e >, where pi are integers. They should be defined by the
path integral
Z
ip1q(t1)=r ipnq(tn)=r −S(q)=~
(19) e :::e e Dq;
R R
1 2 −S(q)=~
S(q) = q_ dt where e Dq is agreed to be 1. Note that we should only
2 P
consider the case pi = 0, otherwise the group of translations along the circle
acts nontrivially on the integrand, and hence under any reasonable definition the
integral should be zero.
Now let us define the integral (19). Since the integral is invariant under shifts
along the target circle, we may as well imagine that we are integrating over q : R !
R with q(0) = 0. Now, let us use the finite dimensional analogy. Following this
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 53
analogy, by completing the square we would get
~ −1 P P P 2 P 2
e−2r2 B ( pjq(tj); pjq(tj)) = e−~ plpjG(tl−tj)=2r = e~ l<j plpjjtl−tjj=2r
R
2
where B(q; q) = q_ dt. Thus, it is natural to define the correlators by the formula
P 2
< eip1q(t1)=r:::eipnq(tk)=r >= e~ l<j plpjjtl−tjj=2r :
We note that this theory, unlike the line-valued one, does satisfy the clustering
P
property. Indeed, if pj = 0 (as we assumed), then (assuming t1  t2  :::  tn),
we have
n−1
X X X
2
plpj(tl−tj) = (tj−tj+1)(pj+1+:::+pn)(p1+:::+pj) = − (tj−tj+1)(p1+:::+pj) ;
l<j j=1 j
2
so the clustering property follows from the fact that (p1 + ::: + pj)  0.
7.13. Massless quantum mechanics on the circle. Consider now the theory
2
with Lagrangian q_ =2, where q is a function on the circle of length L. In this
2 2
case, according to the Feynman yoga, we must invert the operator −d =dt on the
00
circle R=LZ, or equivalently solve the differential equation −G (t) = Æ(t). Here we
2 2
run into trouble: the operator −d =dt is not invertible, since it has eigenfunction
1 with eigenvalue 0; correspondingly, the differential equation in question has no
R
00 00
solutions, as G dt must be zero, so −G (t) cannot equal Æ(t) (one may say that
the quadratic form in the exponential is degenerate, and therefore the Gaussian
integral turns out to be meaningless). This problem can be resolved by the following
2 2
technique of “killing the zero mode”. Namely, let us invert the operator −d =dt
R
1
on the space fq 2 C (R=LZ) : qdt = 0g (this may be interpreted as integration
over this codimension one subspace, on which the quadratic form is nondegenerate).
00
This means that we must find the solution of the differential equation −G (t) =
R
1
Æ(t) − , such that Gdt = 0. Such solution is indeed unique, and it equals
L
2
(t−L=2) L 2
G(t) = − , t 2 [0; L]. Thus, for example < q(0) >= L=12.
2L 24
Higher correlation functions are defined in the usual way. Moreover, one can
define the theory with an arbitrary potential using the standard procedure with
Feynman diagrams.
Finally, let us consider the circle valued version of the same theory. Thus, our
integration variable is a map q : R=LZ ! R=2rZ. Let us first consider integration
over degree zero maps. Then we should argue in the same way as in the case t 2 R,
and make the definition
P 2
< eip1q(t1)=r:::eipnq(tn)=r >0= e−~ l;j plpjG(tl−tj)=2r ;
P
where pj = 0. (Here subscript 0 stands for degree zero maps). Assuming that
1  t1; :::; tn  0, we find after a short calculation
P P
~ 2
< eip1q(t1)=r:::eipnq(tn)=r >0= e2r2 ( l<j plpjjtl−tjj+( pjtj) =L):
(the second summand disappears as L ! 1, and we recover the answer on the
line).
It is, however, more natural (as we will see later) to integrate over all (and not
only degree zero) maps q. Namely, let N be an integer. Then all maps of degree N
have the form q(t)+2rNt=L, where q is a map of degree zero. Thus, if we want to
integrate over maps of degree N, we should compute the same integral as in degree
zero, but with shift q ! q + 2rNt=L. But it is easy to see that this shift results
54 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
P 2 2 2
2i pjtjN=L−2 r N =~L
simply in rescaling of the integrand by the factor e . Thus,
the integral over all maps should be defined by the formula
ip1q(t1)=r ipnq(tn)=r
< e :::e >=
P P 2 2 2
e2r~2 (Pl<j plpjjtl−tjj+(P pjtj)2=L): N e2Pi( pj−t2j)N2r=2LN−22=~Lr N =~L :
e
N
Introduce the elliptic theta-function
X 2
2iuN−TN =2
(u; T ) = e
N2Z
Then the last formula (for t1  :::  tn) can be rewritten in the form
(20)
P
P P pjtj 42r2
~ 2 2 ( ; )
< eip1q(t1)=r:::eipnq(tn)=r >= e 2r2 ( j(tj+1−tj)(p1+:::+pj) +( pjtj) =L) L 42r~2L :
(0; )
~L

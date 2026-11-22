---
doc_id: alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari
doc_title: "Theta Functions, Modular Invariance, and Strings"
section_id: sec-004-d-theta-functions
section_title: "Theta Functions"
section_number: d
pages: 14-18
source_pdf: alvarez-gaume-moore-vafa-1986-theta-functions-modular-invariance-and-strings.pdf
source_sha256: c99ca1cd756f7aa6
toc_source: inferred
doc_brief: "Theta Functions, Modular Invariance, and Strings — We use Quillen's theorem and algebraic geometry to investigate the modular transformation properties of some quantities of interest in string"
---
In this section we define the theta functions and explain their relation to spin
structures. We follow the notation and treatment of Mumford [13]. Another
excellent reference is the book of Fay [14]. In analogy with the genus one case,
once we have introduced the Jacobian J{Σ), we can introduce the Riemann theta
function by the series expansion:
3(z|Ω)= Σ
neZε
We also define theta functions with characteristics a, b for a, b e JR^ by the sum
9 Π (z|Ω) = Σ exp(iπ(n + a) • Ω (n + a) + 2πi(n + a) (z + b))
(3 17)
Theta Functions, Modular Invariance, and Strings 
15
if we shift z by the lattice LΩ, θ transforms by
9 L 
(z + Ωn + m\Ω) = e-
inn 
Ω'
n-
2πin^
z 
+ b)e
2πίa 
m9 
* (z|Ω). 
(3.18)
[b]
 (Z|Ω)'
Another useful transformation law is:
9 [b + m]
 (Z|Ω) = e2π
Thus the theta function is not strictly a function on J(Σ); rather, it is a section of a
holomorphic line bundle on J(Σ) called the 9—line bundle, if. From the transition
functions (3.18) one can compute the first Chern class of <£. Alternatively we can
define the hermitian norm on sections of JS? by
|| s||2 = ei«(«-fiK«-fi)-
1-(«-fl)|s|2 
( 3 >20)
and compute the curvature
cά&) = ~ ^δlog||5||
2 = Σ dφ* A dθ
1. 
(3.21)
2π 
i
We can now apply the Kodaira vanishing theorem [11] and the index theorem for
the δ-complex coupled to if to show that if admits only one holomorphic section
which is represented by the theta function.
1
The relation between spinor bundles and theta functions is based on Riemann's
vanishing theorem. To state this fundamental theorem we first introduce the
Jacobian map of Σ into J(Σ). Given a canonical homology basis, and a point P o on
Σ, we can associate to any point F o n Σ a point in J(Σ) by
Φt(P)= ί ωi9 
(3.22)
Po
where the ωt are the holomorphic differentials. As a map from Σ into C
9, Φ is
multivalued, but, considered as a map into J(Σ) it is single-valued since if we move
P around one of the cycles at or bh then (3.22) changes by an element of the
Jacobian lattice. Similarly, the function on Σ defined by
+ f ω|Ω) 
(3.23)
Po 
/
for z in C
9 is multivalued. However, / is a well-defined function on the interior of
the region in Fig. 2. By repeatedly applying Green's theorem to the one-form df/f
on this region one can prove the
Riemann Vanishing Theorem. The function f(P) either vanishes identically for all
PsΣ or f(P) has exactly g zeroes Pu ...,PgonΣ. Furthermore, in the latter case,
there exists a vector Δ depending only on Po and the canonical homology basis so that
the points {PJ satisfy 
g 
P.
z+ £ ί ω = Δ. 
(3.24)
i=l 
Po
1 We thank Dan Freed for explaining this to us
16 
L. Alvarez-Gaume, G. Moore, and C. Vafa
Conversely, forallPu ...,PgeΣJfwedefinezaccording 
to(3.24) then f(Pt) = 0 for
alli = l,...,g.
Δ is known as the vector of Riemann constants. Since we will not need the
explicit form of Δ we refer to [13,14] for details, and the proof of this result.
The set of points z ε J(Σ), where 5(z|Ω) = 0, known as the Θ-divisor, is a variety
of complex codimension one. Θ will be important to us in Sect. 5. The Riemann
vanishing theorem leads to the following description of Θ\
Corollary. θ(e|Ω) = 0 iff there exist g — \ points Pl9 ....P^^εΣ 
so that
e = Δ-V?ω. 
(3.25)
1 Po
One direction of the proof of the corollary is simple. If e is given by (3.25) then
we choose any point PgeΣ and set
g Pj
z = Δ-Σ ί ω.
1 Po
Then the Riemann vanishing theorem implies:
V 
Po
With a little more work one can show the converse [13].
The sums which arise in the above theorems are clearly related to divisors. In
particular, the divisor Σ i "
1 Λ defines a (possibly twisted) spin bundle. Thus the
connection with spinors begins to emerge. The relation can be made more precise
by generalizing the Jacobian map (3.22) to a map / from divisors of degree zero to
J(Σ) as follows. If D is a degree zero divisor, we choose a 1-cycle σ on Σ whose
boundary is D, i.e. dσ = D. Then the Jacobian map is just
J(D)=JωeJ(Σ). 
(3.26)
σ
Note that the choice of cycle does not matter in (3.26). Two important properties of
/ are,
i) Abel's Theorem. I(D) = 0if and only if D is the divisor of a meromorphic function.
Thus I is defined on divisor classes.
ii) Jacobi Inversion Theorem. The set of points I [Σ \ Λ — gPol 
forPl9...9PgeΣis
all of J(Σ).
We are finally in a position to relate spin structures to Θ. We begin with the
remark that, by the index theorem, a degree g — ί bundle E (that is, a twisted spin
bundle) will have a holomorphic section if and only if the bundle K~
1(g)E has a
zero-mode of Vw. We can take the complex conjugate of the zero-mode equation
[considering K~
ι®E as a [7(1) bundle] and translate back into holomorphic
language to see that E has a holomorphic section if and only if K0E"
1 has a
holomorphic section. That is, E has a divisor of the form P1 + ...Pg_1iϊ and only if
K®E~
X has a divisor of the form β x +.. .β g_ v Since a spin structure Lα satisfies
Theta Functions, Modular Invariance, and Strings 
17
L
2. = K, one can show that the set of points
...,Pβ-1eΣ}, 
(3.27)
where Da is a divisor of Lα, is a symmetric subset of J(Σ). However, from the
Riemann vanishing theorem we see that the set Sα is just a translate of Θ by
Δ — J[Dα — (g — 1)Λ)] Thus, to any spin structure we may associate a symmetric
translate of Θ. That is, if e is in Sa9 then so is -e.
On the other hand, since # is an even function of z, Θ is itself symmetric.
Therefore, a translate Θ + e of Θ is symmetric if Θ + 2e = Θ. An application of
Liouville's theorem to the function
on C
9 shows that 2e e LΩ. Thus the symmetric translates of Θ are the translates by
points of order two.
Finally, recall that the difference of two spin structures Dί -D2 is a point of
order two in the Picard variety, hence I[D1—D2] is of order two in J(Σ). Thus
each of the 2
lg spin structures corresponds to one of the 2
2g half-points in J(Σ). In
particular, some spin structure must correspond to the symmetric translate of Θ
given by Θ itself. We call this spin structure Do, i.e.
Δ = /[Do-(0-l)Λ)] 
(
3 2 8)
The vector of Riemann constants depends on P o, but Do does not. Both A and Do
depend on the choice of canonical homology basis.
2
The correspondences we have just outlined allow a division of spin structures
into two classes known as even and odd spin structures. Note that if
Γε Ί
(εuε2) e (%Z/Z)
29 is a half-point then the divisor of θ 
(z|Ω) is a symmetric
L
ε2j
translate of Θ. Also, it is straightforward to show that
Therefore, we call a spin structure with characteristics [_εί ε2] even or odd
depending on whether 4ε1-ε2 is even or odd. As we will see in Sect. 5, the parity of a
spin structure is related to the existence of zero-modes of the Dirac operator. A
simple induction argument shows that there are 2
fif~
1(2
Sί — 1) odd spin structures
and 2
9~
 ί(2
9 +1) even ones. For example, in the one loop case, there is a single odd
spin structure corresponding to θ MM (0|Ω), and three even spin structures with
associated theta functions S 
(0|Ω), 9 r 
(0|Ω), S L 
(0|Ω). In the two-loop
2 Under a change of homology basis A shifts by an even half point, defined below
18

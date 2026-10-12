---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: sec-000-1-generalities-on-quantum-field-theory
section_title: "Generalities on quantum field theory"
section_number: "1"
pages: 1-4
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
toc_source: inferred
text_source: text rebuilt from glyph codes of the ps2pdf'd dvips PostScript (bitmap Type-3 fonts carry raw TeX OT1 codes; ps2pdf reports 'c' as U+0020, so a char-level rebuild maps it back and expands ligatures); prose good, display math flattened
doc_brief: "Mathematical ideas and notions of quantum field theory — 1. Generalities on quantum field theory 1.1. Classical mechanics. In classical mechanics, we study the motion of a par- ticle."
---
1. Generalities on quantum field theory
1.1. Classical mechanics. In classical mechanics, we study the motion of a par-
ticle. This motion is described by a (vector) function of one variable, q = q(t),
representing the position of the particle as a function of time. This function must
satisfy the Newton equation of motion,
0
q¨ = −U (q);
where U the potential energy, and the mass of the particle is 1. Another way
to express this law of motion is to say that q(t) must be a solution of a certain
variational problem. Namely, one introduces the Lagrangian
2
q_
L(q) = − U(q)
2
(the difference of kinetic and potential energy), and the action functional
Z b
S(q) = L(q)dt
a
(for some fixed a < b). Then the law of motion can be expressed as the least action
principle: q(t) must be a critical point of S on the space of all functions with given
q(a) and q(b). In other words, the Newton equation is the Euler-Lagrange equation
for the solution of the variational problem defined by S.
Remark 1. The name “least action principle” comes from the fact that in
00
some cases (for example when U ≤ 0) the action is not only extremized but also
minimized at the solution q(t). In general, however, it is not the case, and the
trajectory of the particle may not be a minimum, but only a saddle point of the
action. Therefore, the law of motion is better formulated as the “extremal (or
stationary) action principle”; this is the way we will think of it in the future.
Remark 2. Physicists often consider solutions of Newton's equation on the
whole line rather than on a fixed interval [a; b]. In this case, the naive definition
R
of an extremal does not make sense, since the action integral S(q) = L(q)dt
R
is improper and in general diverges. Instead, one makes the following “correct”
definition: a function q(t) on R is an extremal of S if the expression
Z Z
d cL cL
js=0 L(q + s”)dt := ( ”_ + ”¨ + :::);
ds R R cq cq_
where ”(t) is any compactly supported perturbation, is identically zero. With this
definition, the extremals are exactly the solutions of Newton's equation.
1
2 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
1.2. Classical field theory. In classical field theory, the situation is similar. In
this case, we should think not of a single particle, but of a “continuum of particles”
(e.g. a string, a membrane, a jet of fluid); so the motion is described by a classical
field – a (vector) function 
(x; t) depending on both space and time coordinates
d
(x 2 R , t 2 R). Consequently, the equation of motion is a partial differential
equation. For example, for a string or a membrane the equation of motion is
2 2
the wave equation 
 = 0, where  is the D'Alambertian ct − v  (here  is
the Laplacian with respect to the space coordinates, and v the velocity of wave
propagation).
As in mechanics, in classical field theory there is a Lagrangian L(
) (a differential
R
polynomial in 
), whose integral S(
) = L(
)dxdt over a region D in space and
D
time is called the action. The law of motion can be expressed as the condition
that the action must be extremized over any closed region D and fixed boundary
conditions; so the equations of motion (also called the field equations) are the Euler-
Lagrange equations for this variational problem. For example, in the case of string
or membrane, the Lagrangian is
1
2 2 2
L(u) = (
 − v (r
) ):
t
2
Remark. Like in mechanics, solutions of the field equations on the whole space
(rather than a closed region D) are extremals of the action in the sense that
Z
d
js=0 L(u + s”)dxdt = 0;
ds Rd+1
where ” is a compactly supported perturbation.
1.3. Brownian motion. One of the main differences between classical and quan-
tum mechanics is, roughly speaking, that quantum particles do not have to obey
the classical equations of motion, but can randomly deviate from their classical
trajectories. Therefore, given the position and velocity of the particle at a given
time, we cannot determine its position at a later time, but can only determine the
density of probability that at this later time the particle will be found at a given
point. In this sense quantum particles are similar to random (Brownian) particles.
Brownian particles are a bit easier to understand conceptually, so let us begin with
them.
d d
The motion of a Brownian particle in R in a potential field U : R ! R is
d
described by a stochastic process q = q(t), q = (q1; : : : ; qd) 2 R . That is, for each
real t we have a random variable q(t) (position of the particle at a time t), such
that the dependence of t is regular in some sense. The random dynamics of the
1 d
particle is “defined” as follows: if y : [a; b] ! R is a continuously differentiable
function, then the density of probability that q(t) = y(t) for t 2 [a; b] is proportional
R
−S(y)=≤ b 1 02
to e , where S(y) := ( y − U(y))dt is the action for the corresponding
a 2
classical mechanical system, and ≤ is the diffusion coeÆcient. Thus, for given
q(a) and q(b), the likeliest q(t) is the one that minimizes S (in particular, solves
0
the classical equations of motion q¨ = −U (q)), while the likelihood of the other
paths decays exponentially with the deviation of the action of these paths from the
minimal possible.
1
We put the word “defined” in quotation marks because this definition is obviously heuristic
and not rigorous; see below for more explanations
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 3
Remark. This discussion assumes that the extremum of S at q is actually a
minimum, which we know is not always the case.
All the information we can hope to get about such a process is contained in the
correlation functions < qi1(t1) : : : qin(tn) >, which by definition are the expectation
values of the products of random variables qi1(t1) : : : qin(tn) (more specifically, by
Kolmogorov's theorem the stochastic process q(t) is completely determined by these
functions). So such functions should be regarded as the output, or answer, of the
theory of the Brownian particle.
So the main question is how to compute the correlation functions. The definition
above obviously gives the following answer: given t1; : : : ; tn 2 [a; b], we have
Z
−S(q)=≤
(1) < qj1(t1) : : : qjn(tn) >= qj1(t1) : : : qjn(tn)e Dq;
n
where integration is carried out over the space of paths [a; b] ! R , and Dq is
R
−S(q)=≤
a Lebesgue measure on the space of paths such that e Dq = 1. Such an
integral is called a path integral, since it is an integral over the space of paths.
It is clear, however, that such definition and answer are a priori not satisfactory
from the mathematical viewpoint, since the infinite dimensional integration that
we used requires justification. In this particular case, such justification is possible
within the framework of Lebesgue measure theory, and the corresponding integra-
tion theory is called the theory of Wiener integrals. (To be more precise, one cannot
−S(q)=≤
define the measure Dq, but one can define the measure e Dq for suÆciently
nice potentials U(q)).
1.4. Quantum mechanics. Now let us turn to a quantum particle. Quantum
mechanics is notoriosly diÆcult to visualize, and the randomness of the behavior of
a quantum particle is less intuitive and more subtle than that of a brownian parti-
cle; nevertheless, it was pointed out by Feynman that the behavior of a quantum
particle in a potential field U(q) is correctly described by the same model, with
the real positive parameter ≤ replaced by the imaginary number i~, where ~ > 0 is
the Planck constant. In other words, the dynamics of a quantum particle can be
expressed (we will discuss later how) via the correlation functions
Z
iS(q)=~
(2) < qj1(t1) : : : qjn(tn) >= qj1(t1) : : : qjn(tn)e Dq;
R
iS(q)=~
where Dq is normalized so that e Dq = 1.
1.5. Quantum field theory. The situation is the same in field theory. Namely,
a useful theory of quantum fields (used in the study of interactions of elementary
particles) is obtained when one considers correlation functions
Z
iS(
)=~
(3) < 
j1(x1; t1) : : : 
jn(xn; tn) >= 
j1(x1; t1) : : : 
jn(xn; tn)e D
;
R
iS(
)=~
where D
 is normalized so that e D
 = 1.
Of course, from the mathematical point of view, this setting is a priori even
less satisfactory than the one for the Brownian particle, since it involves integra-
iS(q)=~
tion with respect to the complex valued measure e Dq, which nobody knows
how to define. Nevertheless, physicists imagine that certain integrals of this type
4 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
exist and come to correct and interesting conclusions (both physical and mathe-
matical). Therefore, making sense of such integrals is an interesting problem for
2
mathematicians, and will be one of our main occupation during the course.

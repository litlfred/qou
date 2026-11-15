---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: page-002
section_title: "Page 2"
pages: 2-2
pdf_page: 2
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
text_source: ocr
granularity: page
doc_brief: "Mathematical ideas and notions of quantum field theory — 78 sections: Page 1; Page 2; Page 3"
---
2 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY

1.2. Classical field theory. In classical field theory, the situation is similar. In
this case, we should think not of a single particle, but of a “continuum of particles”
(e.g. a string, a membrane, a jet of fluid); so the motion is described by a classical
field — a (vector) function ¢(z,t) depending on both space and time coordinates
(a € R?, ¢ € R). Consequently, the equation of motion is a partial differential
equation. For example, for a string or a membrane the equation of motion is
the wave equation O¢ = 0, where O is the D’Alambertian 0? — v?A (here A is
the Laplacian with respect to the space coordinates, and v the velocity of wave
propagation).

As in mechanics, in classical field theory there is a Lagrangian £(¢) (a differential
polynomial in ¢), whose integral S(¢) = f,, £(¢)dxdt over a region D in space and
time is called the action. The law of motion can be expressed as the condition
that the action must be extremized over any closed region D and fixed boundary
conditions; so the equations of motion (also called the field equations) are the Euler-
Lagrange equations for this variational problem. For example, in the case of string
or membrane, the Lagrangian is

1
Llu) = 5(6 — (Voy).
Remark. Like in mechanics, solutions of the field equations on the whole space
(rather than a closed region D) are extremals of the action in the sense that
|
ds\*~°

where € is a compactly supported perturbation.

| L(ut se)dxdt = 0,
Rati

1.3. Brownian motion. One of the main differences between classical and quan-
tum mechanics is, roughly speaking, that quantum particles do not have to obey
the classical equations of motion, but can randomly deviate from their classical
trajectories. Therefore, given the position and velocity of the particle at a given
time, we cannot determine its position at a later time, but can only determine the
density of probability that at this later time the particle will be found at a given
point. In this sense quantum particles are similar to random (Brownian) particles.
Brownian particles are a bit easier to understand conceptually, so let us begin with
them.

The motion of a Brownian particle in R@ in a potential fied U : R¢ > R is
described by a stochastic process q = q(t), = (m,---,¢a) € R*. That is, for each
real ¢ we have a random variable q(t) (position of the particle at a time t), such
that the dependence of t is regular in some sense. The random dynamics of the
particle is “defined” as follows: | if y : [a,b] + R@ is a continuously differentiable
function, then the density of probability that q(t) = y(t) for t € [a, b] is proportional
to e~S()/*, where S(y) := Gy? — U(y))dt is the action for the corresponding
classical mechanical system, and « is the diffusion coefficient. Thus, for given
q(a) and q(b), the likeliest q(t) is the one that minimizes S (in particular, solves
the classical equations of motion g = —U'(q)), while the likelihood of the other
paths decays exponentially with the deviation of the action of these paths from the
minimal possible.

lWe put the word “defined” in quotation marks because this definition is obviously heuristic
and not rigorous; see below for more explanations

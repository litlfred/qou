---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-032-linearly-forced-harmonic-oscillator
section_title: "Linearly forced harmonic oscillator"
section_number: null
pages: 38-39
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
The Hamiltonian function describing a linearly driven harmonic oscillator reads (h = 1)

= : _ 1 2 2 = V2
H= Hy +V(t), with Hy = Seo(p? + 4°), Vid) = V2F(Oq (179)
and f(t) is real. Here q and p stand for the position and momentum operators satisfying [q, p] = iand wo gives the energy

level spacing in absence of the perturbation V(t). We introduce the usual operators a, = 34 = ip), so that [a_, a4] = 1.
With this notation we have

1
Hy = wo (0.0. + :) . V=fO\(@a,+a_). (180)

The eigenstates of Ho are denoted by |n), so that Ho|n) = wo(n + Hn), where n stands for the quantum number. With this
notation n = 0 corresponds to the ground state.
S. Blanes et al. / Physics Reports 470 (2009) 151-238 189

For simplicity in the computations we choose wp) = 1.In accordance with the prescriptions in Section 2.9, the Hamiltonian
in the Interaction Picture is given by (92) and reads

Hy(t) = eo v(tye Hot = Fcty(e“a, +e-"a_). (181)
Accordingly, the evolution operator is factorized as

U(t, 0) = exp(—iHot)U;(t, 0), (182)
where the new evolution operator U, is obtained from U; = Ay(t)U; = —iH,(t)U).

The infinite Magnus series terminates in the present example. It happens because the second order Magnus approximant,
which involves the computation of

(A(t), Hi(t)) = Ff b) (fay, a] + eM fa_, a)
= 2if (tf (t2) sin(t2 — t) (183)

reduces to a scalar function. Thus the Magnus series in the Interaction Picture furnishes the exact evolution operator
irrespective of f(t):

ae ire t 7 7
exp (/ dt,H,(t,) — al arf dt2[H;(t1), fit)
0 0 0

= exp (—i(aa, + a*a_) — ip)

Ui(t, 0)

= exp(—iaa,) exp(—ia*a_) exp(—if — |a|?/2), (184)
where we have defined
t
a= i] dtsf (te, (185)
0
t fay
p= | arf dtof (t1)f (t2) sin(tz — ty). (186)
0 0

Eqs. (184) and (182) yield the exact time-evolution operator for the linearly forced harmonic oscillator Hamiltonian
(179) [120].
To compute transition probabilities between free harmonic oscillator states of quantum numbers n and m,
Pam = [(m|U;|n) |, (187)

the last form in (184) is most convenient. Specifically, assuming that the oscillator was initially in its ground state |0), we
get in particular the familiar Poisson distribution for the transition probabilities

1
Poon = |a|?" exp(—|a|”). (188)

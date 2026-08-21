---
doc_id: di-cairano-2022-j-phys-commun-6-015002
doc_title: "On the derivation of a nonlinear generalized Langevin equation"
section_id: sec-001-11-state-of-art
section_title: "State-of-art"
section_number: 1.1
pages: 2-3
source_pdf: Di_Cairano_2022_J._Phys._Commun._6_015002.pdf
source_sha256: f75313b507f97172
doc_brief: "On the derivation of a nonlinear generalized Langevin equation — 14 sections: Introduction; State-of-art; Introduction to the problem"
---
The generalized Langevin equation(GLE) is an important mathematical tool for investigating a wide class of
both quantum and classical diffusive phenomena[1] and it is an extension of the Langevin equation[2]. The
major advantage of GLE-based approaches is the reduction of the number of degrees of freedom which describe
the system-environment interactions. For example, in case of a particle moving in a given environment, instead
of solving the Newton’s equations of motions for the system and for each particles of the environment, one can
just focus on the velocity vector,U, of the diffusing particle, that is, the GLE reads:
dU
dt tt U d F t ,1
t
0
() ( ) ( ) () ()ò gt t t=- - +
where γ(t − τ) is the friction function and,ﬁnally, F(t) is a zero mean, stochastic, Gaussian colored noise and
they are related through theﬂuctuation-dissipation relation (FDR) [3]:
FtF kT t ,2B() ( ) ( ) ()tg táñ = -
where kB is the Boltzmann constant andT the temperature. Despite the drastic reduction of the degrees of
freedom, the GLE has shown to provide a reliable description of the physical diffusive processes. In fact, it has
been employed in manyﬁelds of research, for instance, in Biophysics, for studying anomalous diffusion of
proteins in lipid membrane[4– 7], in Hydrodynamics, for studying how probe particles diffuse in viscoelastic
materials [8– 12], in Quantum Mechanics, for explaining the dissipation in quantum system on a more
fundamental and general level[13– 17] as well as in case of speciﬁc system such as the Caldeira-Leggett model
[18, 19] and, in Chemistry, as a diffusion model for the chemical reactions[20, 21]. Nevertheless, the accuracy of
the physical description provided by the GLE strictly depends on how one models the parameters and the time-
dependence of the friction function. Its parametrization, in fact, is an openﬁeld of research which involves both
OPEN ACCESS
RECEIVED
11 November 2021
REVISED
13 December 2021
ACCEPTED FOR PUBLICATION
15 December 2021
PUBLISHED
10 January 2022
Original content from this
work may be used under
the terms of theCreative
Commons Attribution 4.0
licence.
Any further distribution of
this work must maintain
attribution to the
author(s) and the title of
the work, journal citation
and DOI.
© 2022 The Author(s). Published by IOP Publishing Ltd
mathematical and physical studies[22– 28] which provide numerically or analytically the correct description of
the kernel function depending on physical system that one considers.
By deﬁnition, the diffusion is a dynamical process at non-equilibrium since the energy is not constant in time
but it varies over time due to the interaction with the environment, thereby, it cannot be described through the
Hamiltonian formalism. In fact, it is not possible to obtain a(generalized) Langevin equation from the
Hamilton’s equations to any Hamiltonian when the time dependence is not explicit. However, if one introduces
a further Hamiltonian containing all the microscopic details of the environment explicating the interactions
with the system, the energy of both the system and the environment can vary but their sum will be unchanged.
The ﬁrst attempts to derive a GLE adopting this approach have been done by Mori[29] and Ford et al [30] in the
context of linear system-environment interactions and, then, by Zwanzig[31] extending the previous works to
the case of non-linear interactions.
The nonlinear GLE obtained by Zwanzig in[31] is derived from a Hamiltonian function where the particles
composing the environment oscillate harmonically around their global equilibrium conﬁguration, denoted with
the map a, which depends on the instantaneous system conﬁguration. The equilibrium map,a, plays a
fundamental role in the derivation since it contains the information about the coupling between the system and
the environment and the(non) linearity feature of the GLE is determined by the(non) linear dependence of this
map by the system variable.
As shown by Zwanzig[31] through a purely theoretical derivation, even in presence of a non-linear coupling,
one can still provide a mathematical deﬁnition for the friction and noise terms and, thereby, theﬂuctuation-
dissipation theorem [32] can be formulated. Unfortunately, as we will show in the upcoming section, by strictly
applying the theoretical deﬁnitions derived in[31], one notices that the friction function is ill-deﬁned since it
does not contain the information about the coupling and this leads to obtain a tautology on the FDR and to an
unbounded friction function in the continuum limit[31].
The ﬁrst aim of this paper is to formalize and adapt the Zwanzig’s derivation in order to provide a preciser
deﬁnition of kernel and noise terms which is consistent with the continuum limit. The second aim is to
underline the importance of the equilibrium map in the context of the GLE and to study its mathematical
properties.

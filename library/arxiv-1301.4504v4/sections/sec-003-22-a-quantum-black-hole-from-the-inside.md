---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-003-22-a-quantum-black-hole-from-the-inside
section_title: "A Quantum Black Hole from the Inside"
section_number: 2.2
pages: 11-13
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
We now consider Alice the infalling observer’s point of view. As mentioned in the
introduction, it may be possible to “embed” Alice’s quantum mechanics into Charlie’s
via some sort of nontrivial operator mapping. We will discuss this eventually but for
the moment will just treat Alice’s theory as an independent construction. Here are the
basic assumptions about it:
• Although Alice eventually hits the singularity, we imagine that well before that
she has an approximately quantum mechanical description of her experiences in
terms of a quantum state on a time slice like the one shown in ﬁgure 1. We will
not insist that the state be pure.
• Alice’s Hilbert space also has a roughly semiclassical factorization of the form
Hinside =HA⊗HB⊗HR⊗HH′. (2.5)
HereHB andHR are factors shared with Charlie, since they are outside the black
hole horizon and are causally accessible to both Charlie and Alice. HA are the
ﬁeld theory modes just inside the horizon, say with support over GM < r <
2GM−ϵ. HH′ are the remaining degrees of freedom having to do with Alice’s
horizon (which is distinct from the black hole horizon). HH is absent; the region
2GM−ϵ < r <2GM +ϵ is passed through by Alice in an extremely short
period of time and does not have any operational meaning to her. Of course, at
times long before she falls in, the black hole horizon is indistinguishable from her
horizon, andHH is roughly part ofHH′. We emphasize however that the details
of this accounting don’t matter.
• BecauseHB andHR are shared with Charlie, we must have ρ{Alice}
BR =ρ{Charlie}
BR .
This is sometimes called the overlap rule, and it is designed to prevent contradic-
tions where Alice and Charlie disagree about the results of experiments they can
communicate about.
With these assumptions, one can now argue following AMPS that Alice must not
see a smooth vacuum at the horizon. Recall that the modes inHB andHA are basically
Rindler modes on two diﬀerent sides of a Rindler horizon. In the Minkowski vacuum
state such modes are close to maximally entangled:
|vac⟩∼
∑
ω
e−βω
2|ω⟩A|ω⟩B, (2.6)
whereβω is the dimensionless Rindler energy; here it is just the ratio of Schwarzschild
energy to the black hole temperature. This however is problematic from our discussion
– 10 –
A B
R
Figure 1 . Alice’s quantum mechanics, compared to Charlie’s. The world inside her horizon
is drawn in blue and the time slice she quantizes on is in red. For reference Charlie’s world
is in yellow, and the overlap is green. We’ve chosen Charlie’s black slice to coincide closely
with Alice’s near B and R.
of Charlie. We argued that for an old black hole Charlie should see B being close
to maximally entangled with RB, and by the third assumption about Alice this must
also be true for her. But entanglement in quantum mechanics is monogamous: such
entanglement prevents B from also being entangled with A as in (2.6). One way to
see this more precisely, again following AMPS, who themselves were motivated by a
similar argument due to Mathur [37], is to note that strong subadditivity [38] requires
SABRB +SB≤SAB +SBRB. (2.7)
By construction we have SBRB = 0, which also implies (for example by the Araki-Lieb
triangle inequality) thatSABRB =SA. For (2.7) to be consistent with the subadditivity
inequalitySA +SB≥SAB we then must have
IAB≡SA +SB−SAB = 0. (2.8)
IAB is called the mutual information between A and B, and it is zero if and only if
the density matrix ρAB is actually a product ρA⊗ρB. This is clearly inconsistent with
A and B being close to the highly entangled state (2.6). This concludes the AMPS
– 11 –
argument; one possible interpretation is that the resolution of the contradiction is that
there is a “ﬁrewall” of high energy quanta at the horizon of an old black hole which
annihilates any infalling observer.

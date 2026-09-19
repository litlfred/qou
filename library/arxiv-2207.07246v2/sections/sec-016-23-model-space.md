---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-016-23-model-space
section_title: "Model Space"
section_number: 2.3
pages: 33-35
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
The interaction used in this work will not change the total number of Z protons
and A−Z neutrons 3 , so the number of possible isospin states is
(A
Z
)
. However the
tensor part Sij can ﬂip spin, so the possible number of spin states is 2 A. Therefore, as
stated before, the total number of spin-isospin basis states is,
Ntot =
(A
Z
)
× 2A = A!
Z!(Z−A)!× 2A. (2.27)
Take 4He as an example, it has Ntot = 6× 16 = 96 spin-isospin basis states. In
other words, our Hilbert space is constructed by the 96 basis states and therefore a
general state is the linear combination of these basis states. We mark these basis states
as|S⟩ and S can be labeled from 1 to 96,
|S⟩≡| s1⟩⊗| s2⟩⊗| s3⟩⊗| s4⟩≡| s1s2s3s4⟩, (2.28)
where si means the spin isospin state of particle i, it can be any state from neutron
spin up|n↑⟩, neutron spin down|n↓⟩, proton spin up|p↑⟩, proton spin down|p↓⟩. In
Eq.(2.28), we implicitly mean particle 1 is at s1 state, particle 2 is at s2 state, particle
3 is at s3 state and particle 4 is at s4 state. To be clear, it is really,
|S⟩≡| s1
1⟩⊗| s2
2⟩⊗| s3
3⟩⊗| s4
4⟩≡| s1
1s2
2s3
3s4
4⟩, (2.29)
3The AV6’ and local chiral N 2LO we use in this work conserve the number of isospin states. For
example, for 4He we begin with
(4
2
)
= 6 diﬀerent isospin states, the interaction we use always generate
isospin states within these 6 states, they do not generate isospin states other than these 6 states.
23
where the subscript (the state label) 1 to 4 represents state 1 to state 4, and the
superscript (particle label) from 1 to 4 represents particle 1 to particle 4.
We denote the spatial conﬁguration of a system with A particles as R,
R≡ (r1,r2,...,rA), (2.30)
whereri = (xi,yi,zi) is the coordinates of particle i. The coordinate space conﬁguration
R of 4He can also be written as a state |R⟩,
|R⟩≡| r1⟩⊗| r2⟩⊗| r3⟩⊗| r4⟩≡| r1r2r3r4⟩. (2.31)
Similar with Eq.(2.29), Eq.(2.31) really means,
|R⟩≡| r1
1⟩⊗| r2
2⟩⊗| r3
3⟩⊗| r4
4⟩≡| r1
1r2
2r3
3r4
4⟩. (2.32)
TakingR and the spin isospin state S in to account, our basis state |RS⟩ can
ﬁnally be written as,
|RS⟩ =|R⟩⊗| S⟩≡| r1r2r3r4⟩⊗| s1s2s3s4⟩, (2.33)
The correspondingly identity operators for our basis are,
∫
dR|R⟩⟨R| = 1, (2.34)
∑
S
|S⟩⟨S| = 1, (2.35)
∑
S
∫
dR|RS⟩⟨RS| =
∫
dR|R⟩⟨R|⊗
∑
S
|S⟩⟨S| = 1. (2.36)
In fact, without the Coulomb interaction, for 4He it is possible to use two |T = 0⟩
states (T is the total isospin quantum number) to couple with 16 spin states to form 32
basis. And due to the fact that the Hamiltonian has time-reversal symmetry, only 16 of
the 32 basis states are independent, therefore we can use 16 states to form the Hilbert
space instead of 96. However the Coulomb interaction does not commute with the
24
total isospin operator, it does not conserve total isospin and can generate T⁄= 0 states,
therefore the 16 spin/isospin states with T = 0 cannot be used when the Coulomb
interaction was present. And this is why we use the 96 states in this work.

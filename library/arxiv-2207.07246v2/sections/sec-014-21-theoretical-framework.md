---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-014-21-theoretical-framework
section_title: "Theoretical Framework"
section_number: 2.1
pages: 24-29
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
PIMC directly calculates the expectation value of an operator ⟨ ˆO⟩ as
⟨ ˆO⟩ =⟨ΨT|e−Hτ1 ˆOe−Hτ2|ΨT⟩
⟨ΨT|e−Hτ|ΨT⟩ , (2.1)
where τi is an imaginary time and the total imaginary time τ =τ1 +τ2. ΨT is a trial
wave function and it can serve as the initial state of the system. H is the Hamiltonian
of the system,
H =T +V, (2.2)
where T and V are kinetic and potential energy operators. Since the operator ˆO is
Hermitian, the numerator and denominator in Eq.(2.1) are real, so in PIMC it is
actually calculated as,
⟨ ˆO⟩ = Re⟨ΨT|e−Hτ1 ˆOe−Hτ2|ΨT⟩
Re⟨ΨT|e−Hτ|ΨT⟩ . (2.3)
On the one hand, if τi = 0, Eq.(2.1) becomes,
⟨ ˆO⟩ =⟨ΨT| ˆO|ΨT⟩
⟨ΨT|ΨT⟩ = Re⟨ΨT| ˆO|ΨT⟩
Re⟨ΨT|ΨT⟩ , (2.4)
so PIMC becomes VMC which gives an upper bound to the true ground state energy.
On the other hand, the trial state |ΨT⟩ can be written as the linear combina-
tion of the eigenstates|Φn⟩ of the Hamiltonian whose eigenvalues are En, and with
corresponding amplitude an such that,
|ΨT⟩ =
∞∑
n=0
an|Φn⟩. (2.5)
14
After operating with the propagator e−Hτ1,|ΨT⟩ becomes,
e−Hτ1|ΨT⟩ =a0e−E0τ1
[
|Φ0⟩ +
∞∑
i=1
ai
a0
e−(Ei−E0)τ1|Φi⟩
]
. (2.6)
Therefore, if τi is big enough, the factor e−(Ei−E0)τ1 will make all the excited states
negligible compared with the ground state |Φ0⟩, and we ﬁnd that,
lim
τi→∞
e−Hτi|ΨT⟩∝| Φ0⟩. (2.7)
So, e−Hτi|ψT⟩ project out the ground state |Φ0⟩. In this case Eq.(2.1) will become
the ground state expectation value of ˆO,
⟨ ˆO⟩ =⟨Φ0| ˆO|Φ0⟩
⟨Φ0|Φ0⟩ = Re⟨Φ0| ˆO|Φ0⟩
Re⟨Φ0|Φ0⟩ . (2.8)
In all kinds of calculations, however, it is usually not easy to directly sample the
whole exact propagator e−Hτi. Instead, we break τi into Ni pieces of time step ∆τ
such that τi = Ni∆τ, and the whole propagator can be written as a product of Ni
short-time propagator e−H∆τ,
e−Hτi = (e−H∆τ)Ni. (2.9)
Typically we approximatee−H∆τ using a Trotter breakup (Schmidt and Lee (1995)),
e−H∆τ≈e−V
2 ∆τe−T ∆τe−V
2 ∆τ, (2.10)
where each of the terms e−V
2 ∆τ and e−T ∆τ can be calculated exactly or well approxi-
mated, as shown later.
If we want to calculate ground state properties, we need to use a suﬃciently large
τi ﬁrst such that e−Hτi can project out the ground state |Φ0⟩, then we choose a proper
Ni to make sure ∆τ is small enough such that time step error are negligible for the
quantity we want to calculate. However, if ∆τ is too small it can cost an unnecessary
15
large amount of computational resources, because then we need a very big Ni which
means many short-time propagators e−H∆τ. Therefore, time step ∆τ should be set at
a reasonable point between accuracy and computational cost.
Once τi, ∆τ and Ni are chosen, then we apply Eq.(2.9) in Eq.(2.3) such that we
accurately multiply the Ni short-time propagators e−H∆τ together to replace e−Hτi,
and therefore the sampling of Eq.(2.3) will be equivalent with Eq.(2.8) the ground
state calculation. So we calculate Eq.(2.3) by choosing a suﬃciently largeτ1 andτ2 ﬁrst
(usually we setτ1 =τ2), then replacing e−Hτ1 ande−Hτ2 with corresponding (e−H∆τ)N1
and (e−H∆τ)N2 such that,
⟨ ˆO⟩ = Re⟨ΨT|e−H∆τ...e−H∆τ ˆOe−H∆τ...e−H∆τ|ΨT⟩
Re⟨ΨT|e−H∆τ...e−H∆τe−H∆τ...e−H∆τ|ΨT⟩ . (2.11)
Eq.(2.11) is basically how PIMC works. As we can see from Eq.(2.11), a PIMC
calculation not only depends on the operator ˆO, but also depends on the Hamiltonian
ˆH, the trial wave function ΨT and the short-time propagator e−H∆τ. All of them will
be introduced one by one in the following sections.
As to the operator ˆO, on the one hand, it may commute with the Hamiltonian. In
this case, ˆO can be moved to the leftmost or the rightmost position, and Eq.(2.3) can
then be written as the average of the two,
⟨ ˆO⟩ =
1
2Re
(
⟨ΨT| ˆOe−Hτ|ΨT⟩+⟨ΨT|e−Hτ ˆO|ΨT⟩
)
Re⟨ΨT|e−Hτ|ΨT⟩ . (2.12)
This is useful when the application of the operator on the trial wave function is simpler
than its application directly on the propagator e−Hτ , or has lower variance.
On the other hand, however, the operator ˆO can also be other operators which do
not commute with H. In fact, a big advantage of PIMC is that it can directly deal
with operators which do not commute with H, while diﬀusion based QMC methods
like GFMC and AFDMC cannot easily do so without tradeoﬀ.
16
Because, fundamentally speaking, unlike Eq.(2.3), all the diﬀusion based QMC
are trying to use a large enough total imaginary time τd in e−Hτd to project out the
ground state and calculate the following quantity,
⟨ ˆO⟩ = Re⟨ΨT| ˆOe−Hτd|ΨT⟩
Re⟨ΨT|e−Hτd|ΨT⟩ = Re⟨ΨT| ˆO|Φ0⟩
Re⟨ΨT|Φ0⟩ , (2.13)
which is called mixed estimator1 . It works ﬁne as long as ˆO commutes withH. However
if ˆO does not commute with H, diﬀusion based QMC cannot directly calculate the
ground state of⟨ ˆO⟩, and often the mixed estimator along with extrapolation of the
errors (Hammond et al. (1994)) are used instead. However, the extrapolated mixed
estimator is not as accurate as the true ground state estimator Eq.(2.3). And in fact,
a lot of operators do not commute with H, and they can only be accurately and
directly calculated by PIMC (or higher variance forward walking additions to diﬀusion
methods). That is one of the main reasons to choose PIMC.
Fig. 2.1 is an example to illustrate the advantage of PIMC. The one-particle
number density operator ˆO = ˆρ(r) whose deﬁnition is Eq.(4.32) does not commute
withH, therefore straightforward DMC can only calculate the mixed estimator of ρ(r)
which is diﬀerent from the exact ρ(r). As one can see from Fig. 2.1, in the 4-particle
system, using three diﬀerent trial wave function ΨT marked as Nr.1, Nr.2 and Nr.3,
the extrapolated estimator ρ(r) from DMC are diﬀerent with each other and none
of them is the true ground state expectation value 2 . However, no matter which of
the 3 trial wave functions ΨT are used, the ρ(r) projected out by PIMC are the same
within error bar, which means they are the true ground state ρ(r). Obviously the
PIMC results are more reliable than the DMC in this case.
It needs to be pointed out that, due to the fact that T and V do not commute
1It can be seen from Eq.(2.13) that the DMC total imaginary time τd can be just half of the
PIMC total imaginary time τ, τd = 0.5τ, because DMC project out the ground state only from one
side while PIMC does so from both sides.
2the DMC results are obtained by using the extrapolated estimator Eq.(B.48).
17
/s48/s46/s48 /s48/s46/s53 /s49/s46/s48 /s49/s46/s53 /s50/s46/s48 /s50/s46/s53 /s51/s46/s48
/s48/s46/s48/s48
/s48/s46/s48/s49
/s48/s46/s48/s50
/s48/s46/s48/s51
/s48/s46/s48/s52
/s48/s46/s48/s53
/s48/s46/s48/s54
/s48/s46/s48/s55
/s48/s46/s48/s56
/s48/s46/s48/s57
/s48/s46/s49/s48
/s48/s46/s49/s49
/s48/s46/s49/s50
/s48/s46/s49/s51
/s48/s46/s49/s52
/s40/s114/s41/s32/s40/s102/s109
/s45/s51
/s41
/s114/s32/s40/s102/s109/s41
/s65/s61/s52/s32/s32/s32/s32/s68/s77/s67/s32/s32/s32/s32/s80/s73/s77/s67
/s78/s114/s46/s49/s32/s32/s32/s32 /s32/s32/s32/s32
/s78/s114/s46/s50/s32/s32/s32/s32 /s32/s32/s32/s32
/s78/s114/s46/s51/s32/s32/s32/s32 /s32/s32/s32/s32
Figure 2.1: Comparison between PIMC and DMC 4-particle calculations for one-
particle number density ρ(r) using 3 diﬀerent trial wave function (Zabolitzky and
Kalos (1981)) and with Malﬂiet-Tjon interaction (Malﬂiet and Tjon (1969)).
with each other as well as V is usually non-trivial, we use approximated short-time
propagator U(∆τ)≈ e−H∆τ in the calculation instead of e−H∆τ. And U(∆τ) and
e−H∆τ are diﬀerent by a time step ∆τ error,
U(∆τ) =e−H∆τ +O(∆τl), (2.14)
where diﬀerent choices of U(∆τ) will give diﬀerent integerl, and the error between the
approximate short-time propagator U(∆τ) and exact short-time propagator e−H∆τ is
of ∆τl order.
Therefore, what we really calculate in PIMC is⟨O(∆τ)⟩, which is an approximation
of the true expectation value ⟨O⟩ in Eq.(2.11),
⟨ ˆO(∆τ)⟩ = Re⟨ΨT|[U(∆τ)]N1 ˆO[U(∆τ)]N2|ΨT⟩
Re⟨ΨT|[U(∆τ)]N1+N2|ΨT⟩ . (2.15)
18
In the limit of the time step ∆ τ becomes zero,⟨O(∆τ)⟩ will be the same as ⟨O⟩,
lim
∆τ→0
⟨ ˆO(∆τ)⟩ =⟨O⟩. (2.16)
So we need to calculate ⟨O(∆τ)⟩ for diﬀerent time step ∆τ, then extrapolate the
⟨O(∆τ)⟩ at ∆τ = 0 in order to ﬁnd the true expectation value ⟨O⟩. If the operator ˆO
in Eq.(2.15) is placed exactly at the middle of the path such that N1 =N2, the PIMC
will essentially be equivalent with VMC whose trial function is [ U(∆τ)]
N
2|ΨT⟩, in this
case⟨O(∆τ)⟩ will be the upper bound of the true expectation ⟨O⟩.

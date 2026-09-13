---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-022-272-path-diagrams
section_title: "Path Diagrams"
section_number: 2.7.2
pages: 50-53
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
Function f(R)lr corresponds to the denominator of Eq.(2.84) and it does not
depend on where the operator ˆO is placed,
f(R)lr =
∑
S0,SN
⟨Ψl
T|R0S0⟩⟨R0S0|[U(∆τ)]N|RNSN⟩⟨RNSN|Ψr
T⟩
=fV
lr (R)gF (R). (2.94)
Functiong(R)lr corresponds to the numerator of Eq.(2.84), and it depends on ˆOM
deﬁned in Eq.(2.85) which means the operator ˆO is placed at bead M (its spatial
conﬁguration is RM),
g(R)lr =
∑
S0,SN
⟨Ψl
T|R0S0⟩⟨R0S0|[U(∆τ)]N1 ˆOM[U(∆τ)]N2|RNSN⟩⟨RNSN|Ψr
T⟩
=gV
lr,M(R)gF (R). (2.95)
FunctiongF (R) in Eqs.(2.94,2.95) is the total free particle propagator,
gF (R) =
N−1∏
I=0
Gf
I,I +1, (2.96)
where the free particle propagator Gf
I,I +1 in Eq.(2.96) is deﬁned as 7 ,
Gf
I,I +1≡⟨RI|e−T ∆τ|RI+1⟩ =
( m
2π∆τ ℏ2
) 3A
2
e
−
(RI−RI+1)2
2∆τ ℏ2
m , (2.98)
and each of these free particle propagator is represented by the black curved line from
below in Fig. 2.5, it carries ∆τ and it connects conﬁguration RI and RI+1 (or we
can say it connects beads I and I + 1). Actually, We can see that the ∏N−1
I=0 Gf
I,I +1
7For any RI and RJ on the time line which is represented by the long horizontal lines in Fig.
2.5 on which there are black points (beads), the general form of the free particle propagator can be
written as,
Gf
I,J≡⟨RI|e−T∆τ|J−I||RJ⟩ =
( m
2π|J−I|∆τ ℏ2
) 3A
2
e
− (RI−RJ)2
2|J−I|∆τ ℏ2
m , (2.97)
40
in functions Alr(R) and Blr(R) actually canceled out because they exist in both the
denominators and the numerators.
Note that in Alr(R) andBlr(R) in Eqs.(2.90,2.91), both f(R)lr andg(R)lr contain
gF (R), therefore Alr(R) and Blr(R) can be simpliﬁed as,
Alr(R) = Re[gV
lr,M(R)]
|Re[fV
lr (R)]|, (2.99)
Blr(R) = Re[fV
lr (R)]
|Re[fV
lr (R)]|. (2.100)
The superscriptV ingV
lr,M(R) andfV
lr (R) means the potential propagators are involved.
0 M+1 MM-11 N-1 N
…
…
…
…
…
…
…
…
Figure 2.5: Path diagrams which illustrate the PIMC beads, f(R)lr, and g(R)lr.
Fig. 2.5 is a visualization of f(R)lr in Eq.(2.94) and g(R)lr in Eq.(2.95). The
calculations of functions gV
lr,M(R) in Eq.(2.99) and fV
lr (R) in Eq.(2.100) can be more
clear with the help of Fig. 2.5 which contains diagrams that visualize the path. By
inserting N + 1 complete basis marked by the black dots and labeling them from 0 to
N, the total time τ is split into N small time step ∆τ soτ =N∆τ. We call each black
dot a bead. For a given whole spatial conﬁguration R deﬁned by Eq.(2.88), each of
41
the beads carries its own spatial conﬁguration. For example, the Ith bead has spatial
conﬁgurationRI. The long black horizontal line represents the total imaginary time
of the path τ and we can call it time line, and it has been split into N pieces and
occupied by N + 1 beads. Each of the black curved lines from the bottom represents
the corresponding free particle propagator, e.g., if the black curved line connects beads
I and I + 1, the black curved line just represents the free particle propagator Gf
I,I +1
in Eq.(2.96). The red curved line from the upper, on the other hand, represents the
accordingly potential part of the propagator, e.g., we use PI to denote the red curved
line as the corresponding e
−VI∆τ
2 whereVI is deﬁned in Eq.(2.62) and it has spatial
conﬁguration RI while P†
I is the Hermitian conjugate of PI which gives the reverse
order of Eq.(2.63). The symbol ↓ means the additional propagator inserted when
needed. For the AV6’ interaction,↓ means 1, for the local chiral N 2LO interaction it
means the eﬀective G which is Eq.(2.71).
For a givenl and r order in the trial wave function ΨT , and a givenR of all the
beads, the calculations of fV
lr (R) and gV
lr,M(R) are straightforward. Here we describe
the computation rule which is basically a two-step process.
Step one First of all, we just need to follow the order of beads in Fig. 2.5 and replace
all the red curves and↓ symbols above the black time line with corresponding
e
−VI∆τ
2 or e
−V†
I ∆τ
2 and the eﬀective G. We next replace all of the black curve
under the black time line with corresponding gF
IJ which are gaussian functions.
Step two Then, for fV
lr (R) in the upper part in Fig. 2.5, we just need to sandwich all
the ordered operators above the black time line between ⟨ψl
T| and|ψr
T⟩ to give
a (complex) number. This number is the corresponding fV
lr (R). We multiply
fV
lr (R) bygF (R) which is the product of all the black curved lines under the
time line to ﬁnd f(R)lr.
42
The calculations of gV
lr,M(R) and g(R)lr are similar. The diﬀerence is that when
calculating gV
lr,M(R), the additional operator ˆO needs to be placed at the appropriate
imaginary time as illustrated in the lower panel in Fig. 2.5.

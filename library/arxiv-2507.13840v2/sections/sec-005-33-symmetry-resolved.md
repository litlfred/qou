---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-005-33-symmetry-resolved
section_title: "Symmetry-resolved"
section_number: 3.3
pages: 7-8
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Symmetry-resolved
entanglement
wit-
nesses
We will now discuss how to exploit symmetry to
enhance the bounds from the witnesses. We will
first focus on the witnesses from the PT moments
before commenting on the realignment moments.
In the presence of a global symmetry, the den-
sity matrix ρ can be split into different charge sec-
tors. For concreteness, we consider a global U(1)
symmetry where the state commutes with the to-
tal number operator Q = P
i(I −Zi)/2.
Such
a state has a block-diagonal form ρ = L
q ρ(q),
where ρ(q) is a block corresponding to the charge
q.
In a bipartite system, we can write Q =
QA + QB, where QA(B) = P
i∈A(B)(I −Zi)/2.
In this case, the partial transpose commutes
with Q′ = QA −QT
B and it can be cast in the
block diagonal form [30, 79]: we denote as ρΓ
(q)
the resulting blocks, where q indicates the charge.
We denote the corresponding moments as p(q)
α ,
with
p(q)
α
= tr((ρΓ
(q))α).
(24)
We can exploit this to define p4-negativity in a
given block
E(q)
4 (ρ) = 1
2 ln
 
(p(q)
2 )3
p(q)
4
!
.
(25)
By similar arguments as the non-symmetry-
resolved case, one can show that
E(q)
4 (ρ) ≤E(q)(ρ) ,
(26)
where
E(q)(ρ) = ln∥ρΓ
(q)∥2
1 = ln
X
i
|λ(q)
i | ,
(27)
where λ(q)
i
are the eigenvalues of ρΓ
(q). It is easy
to see that E(q)(ρ) ≤E(ρ) for any given block,
and combining with Eq. (26), we obtain
E(q)
4 (ρ) ≤E(ρ) .
(28)
Thus,
E(q)
4 (ρ)
plays
a
similar
role
as
the
symmetry-resolved p3-PPT condition [79], which
is able to detect entanglement using symmetry-
resolved moments for a fixed charge.
Notably,
one can enhance the detection capability and ob-
tain a tighter lower bound for the negativity by
combining all quantum number blocks. We de-
fine the symmetry-resolved (SR) p4-negativity as
ESR
4 (ρ) = ln

X
q
v
u
u
t(p(q)
2 )3
p(q)
4

.
(29)
We have
ESR
4 (ρ) ≤E(ρ) .
(30)
Thus, ESR
4 (ρ) is also a quantitative entanglement
witness.
Note that, we can also define
˜E2(ρ) = 1
2 ln (p2) = −1
2S2(ρ) ,
(31)
which satisfies
˜E2(ρ) ≤E(ρ) .
(32)
However, this inequality is not useful for entan-
glement detection since ˜E2(ρ) ≤0 for any state
ρ. Nevertheless, the symmetry-resolved version
˜ESR
2 (ρ) = ln
 X
q
√p2
!
,
(33)
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
7
is not necessarily non-positive, so that it may al-
ready provide a nontrivial witness of entangle-
ment since we have
˜ESR
2 (ρ) ≤E(ρ) .
(34)
By Jensen’s inequality, one can show the upper
bound ˜ESR
2 (ρ) ≤1
2(ln Nq−S2(ρ)), where Nq is the
number of quantum number. For the global U(1)
symmetry, this bound scales as O(ln n) since
Nq = n+1. Thus, while ˜ESR
2 (ρ) is more tractable
since it only involves the second PT moment, it
has a drawback that it can only provide a lim-
ited lower bound to the negativity. In particular,
it cannot be used to certify volume-law entan-
glement. Furthermore, ˜ESR
2 (ρ) fails to detect en-
tanglement when the states are too mixed, with
S2(ρ) ≥ln(n + 1).
Let us also mention that the SR witnesses can
be used to detect the entanglement of arbitrary
states, including those that do not have any sym-
metry [79]. Indeed, there exists a quantum chan-
nel Λ that maps a state ρ to σ = Λ(ρ) that has a
block-diagonal structure with respect to the de-
sired symmetry. This channel is a local opera-
tion, which cannot increase the PT negativity.
This implies
ESR
4 (σ) ≤E(σ) ≤E(ρ),
(35)
which shows that ESR
4 (Λ(ρ)) is also a quantitative
entanglement witness.
Further, the SR witnesses can be defined in
a similar way using the realignment matrix mo-
ments. It is known that the singular values of Rρ
can be split into charge sectors q which are eigen-
values of QA ⊗1 −1 ⊗QT
A [88]. The symmetry-
resolved moments are
r(q)
α
=
X
i
|λ(q)
i |α.
(36)
Then, we define
CSR
4 (ρ) = ln

X
q
v
u
u
t(r(q)
2 )3
r(q)
4

.
(37)
and
˜CSR
2 (ρ) = ln
 X
q
√r2
!
,
(38)
as our SR witnesses from the realignment matrix
moments. Note that the CCNR negativity is not
known to satisfy monotonicity under LOCC, and
therefore the SR witnesses are only applicable for
systems with symmetry, unlike the PT witnesses.

---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-042-134-the-kms-condition
section_title: "The KMS condition."
section_number: 13.4
pages: 102-105
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
The KMS condition.
In the examples of the previous section the operators of the modular group
were easy to calculate explicitly, including the domain of ∆. One can imagine
that this is not always so. If we are particularly interested in the modular
group σφ
t it would be useful to be able to guess it and show that the guess is
right without bothering about the domain of ∆. The KMS (Kubo-Martin-
Schwinger) condition from quantum statistical mechanics allows us to do just
that. The modular group came from the non-trace-like property of a state
and the KMS condition allows us to correct for that. Let us do a formal
calculation assuming that the modular group can be extended to complex
numbers (remember that Ωis ﬁxed by S, J and ∆):
φ(xy)
=
⟨yΩ, x∗Ω⟩
=
⟨yΩ, J∆−1/2∆x∆−1Ω⟩
=
⟨∆x∆−1Ω, SyΩ⟩
=
⟨y∆x∆−1Ω, Ω⟩.
We conclude that
φ(xy) = φ(yσφ
i (x)).
Thus the trace is commutative provide we operate by the modular group.
Exercise 13.4.1. If M is ﬁnite dimensional and φ is a faithful state, show
that φ ◦σφ
t = φ and that for each x and y in M there is an entire function
F(z) with, for t ∈R,
F(t)
=
φ(σφ
t (x)y)
and
F(t + i)
=
φ(yαt(x)).
If M is inﬁnite dimensional we would not expect the function F(z) of the
previous exercise to be entire.
102
Deﬁnition 13.4.2. Let αt be a strongly continuous one parameter automor-
phism group of a von Neumann algebra M, and φ be a faithful normal state
on M. We say that α satisﬁes the KMS condition for φ if φ ◦αt = φ and ,
for each x and y in M, there is a function F, continuous and bounded on
the strip {z : 0 ≤ℑm(z) ≤1}, analytic on the interior of the strip and such
that for t ∈R,
F(t)
=
φ(σφ
t (x)y)
and
F(t + i)
=
φ(yαt(x)).
Theorem 13.4.3. If φ is a faithful normal state on a von Neumann algebra
M then σφ
t is the unique one parameter automorphism group satisfying the
KMS condition for φ.
This chapter has been heavily technical so we defer the proof, which is by
approximation on dense subspaces of the domain of ∆to which the previous
calculations can be applied, to an appendix. We content ourselves here with
an interesting corollary, identifying a part or M on which φ behaves as a
trace.
Corollary 13.4.4. For a ∈M the following are equivalent:
1. φ(ax) = φ(xa) for all x ∈M.
2. σφ
t (a) = a for all t ∈R.
Proof. (1 ⇒2) Observe that for x ∈M, ⟨x∗Ω, aΩ⟩= ⟨Ω, xaΩ⟩= ⟨Ω, axΩ⟩
(by 1). So ⟨SxΩ, aΩ⟩= ⟨a∗Ω, xΩ⟩so that aΩ∈D(S∗) and S∗(aΩ) = Ω∗. So
∆(aΩ) = aΩ, ∆itaΩ= aΩand ﬁnally σφ
t (a) = a for all t ∈R.
(2 ⇒1) φ(σφ
t (x)a) = φ(σφ
t (xa)) = φ(xa) so that F(t) is constant. Use the
Schwarz reﬂection principle to create a holomorphic function, constant on R,
in the union of the strip with its complex conjugate. Thus F is constant on
the strip and φ(xa) = φ(ax).
Deﬁnition 13.4.5. The von Neumann subalgebra of M deﬁned by either of
the conditions of the previous corollary is called the centraliser of the state
φ.
103
104
Chapter 14
Connes’ theory of type III factors.
14.1

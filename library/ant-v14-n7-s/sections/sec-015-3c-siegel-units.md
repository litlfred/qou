---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-015-3c-siegel-units
section_title: "3C. Siegel units"
section_number: null
pages: 18-19
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
Deﬁnition 3.4. For N> 1, and c> 1 an integer coprime to 6 N, let
cgN∈ O(Y1(N))×
be Kato’s Siegel unit (the unit denoted by cg0,1/N in the notation of [Kato 2004, §1]).
Slightly abusively, we shall use the same symbol cgN for the pullback of this unit to Y(M, N), for any
M> 1 (we shall only need this when M| N).
As in [op. cit.] we note that if c, d are two integers that are both > 1 and coprime to 6N, then we have
the identity
(d2−⟨ d⟩)cgN=(c2−⟨ c⟩)dgN. (3-2)
It follows that the dependence on c may be removed after extending scalars to Q: there is an element
gN∈ O(Y1(N))×⊗ Q such that cgN=(c2−⟨ c⟩)· gN for any choice of c.
Proposition 3.5. (i) The Siegel units arenorm-compatible, in the sense that if N′|N and N and N′ have
the same prime divisors, then under the natural map
pr: Y(M, N)→ Y(M, N′)
we have
(pr)∗(cgN)= cgN′.
(ii) The de Rham realisation of gN is the Eisenstein series
d log(gN)(τ)=− 2πi F(2)
1/N(τ) dτ.
Proof. Part (i) is proved in [Kato 2004, Section 2.11]. Part (ii) is [op. cit., Proposition 3.11(2)]. □
One important use of Siegel units comes in the construction of Euler systems; for example, see [Kato
2004; Lei et al. 2014; Kings et al. 2017]. The basic method in each of these cases is similar; one takes
cohomology classes attached to Siegel units under the realisation maps and pushes them forward to
a different symmetric space, then exploits the norm compatibility to prove norm relations for these
cohomology classes. We will do something similar in the Betti cohomology. In particular, we make the
following deﬁnition:
Deﬁnition 3.6. Let cCN:= C(cgN)∈ H1(Y1(N), Z) be the Betti realisation of cgN .
From Proposition 3.5(i), we see that if p| N, the classes cCN pr for r> 0 are compatible under
push-forward, and deﬁne a class
cCN p∞∈ lim←−−r
H1(Y1(N pr), Z).
Lemma 3.7. If ρ denotes the involution of Y1(N) corresponding to x+ iy↦→− x+ iy on H, then
ρ∗(cCN)=− cCN .
p-adic Asai L-functions of Bianchi modular forms 1685
Proof. The variety Y1(N) has a canonical model over Q for whichρ corresponds to complex conjugation
on Y1(N)(C). Since the Siegel units are deﬁned over Q in this model, they intertwine the action of ρ on
Y1(N)(C) with complex conjugation on C×. So it sufﬁces to check that complex conjugation acts as −1
on H1(C×, Z), which is clear. □

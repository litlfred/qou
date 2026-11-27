---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-006-4-general-jet-bundle-jka-over-a-noncommutative-a
section_title: "General jet bundle JkA over a noncommutative algebra"
section_number: 4
pages: 13-14
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
A over a noncommutative algebra
We are now ready to construct bimodules Jk
A over a possibly noncommutative algebra A for
any k. Following the pattern in Section 3, we deﬁne the space of quantum symmetric k-forms
Ωk
S as the joint kernel of Ω 1⊗Ak = Ω1⊗A/uni22EF⊗A Ω1 when applying ∧in any two adjacent places
Ωk
S ∶=/uni22C2.disp
i<k
ker/braceleft.alt3∧i∶Ω1⊗Ak→Ω1⊗A(i−1)⊗
A
Ω2⊗
A
Ω1⊗A(k−i−1)/braceright.alt3
where ∧i is taken to act on the i,i + 1 tensor factors in Ω 1⊗Ak. We set Ω 0
S = A, Ω 1
S = Ω1 and
deﬁne the k-th order jet bimodule as
Jk
A∶=
k
/uni2295.big.disp
i=0
Ωi
S =A⊕Ω1⊕Ω2
S⊕/uni22EF⊕Ωk
S,
together with the bullet A-actions ●k which we will need to deﬁne.
As before, we assume a bimodule connection∇∶Ω1→Ω1⊗A Ω1 on Ω1 with generalised braiding
σ∶Ω1⊗A Ω1→Ω1⊗A Ω1. This automatically extends to tensor product connections ∇n on higher
tensor powers of Ω 1, which can be characterised recursively by
∇n∶Ω1⊗An→Ω1⊗
A
Ω1⊗An, ∇n =∇⊗idn−1+σ1(id⊗∇n−1),
where idk denotes the identity on Ω 1⊗Ak and we set ∇1 = ∇, ∇0 = d. These connections are
bimodule connections with generalised braidings
σ∇n∶Ω1⊗An⊗
A
Ω1→Ω1⊗
A
Ω1⊗An, σ ∇n = (σ⊗idn)(id⊗σ∇n) =σ1...σ n,
where we recall that σi denotes σ acting on the i,i + 1 tensor factors. It is useful to note that
∇n can also be written as
∇n =
n−1
/summation.disp
k=0
σ1...σ k(idk⊗∇⊗idn−1−k) =∇l⊗idn−l+σ1...σ l(idl⊗∇n−l)(5)
for l = 1,/uni22EF,n −1, where in the ﬁrst expression we think of ∇n as acting via ∇on each factor in
Ω1⊗An = Ω1⊗A... ⊗A Ω1 followed by swapping the new Ω1 to the far left by repeatedly applying
σ. In the second expression, we split the domain of ∇n as Ω 1⊗An = Ω1⊗Al⊗A Ω1⊗A(n−l) and
think of ∇n as the tensor product connection on this.
If ∇is extendable then, similarly to the expression for R∇2 in Lemma 3.4, we can ﬁnd a
recursive expression for the curvature R∇n∶Ω1⊗An→Ω2⊗A Ω1⊗An of ∇n as
R∇n =R∇⊗id+(σΩ1,Ω2⊗id)(id⊗R∇n−1) =
n−1
/summation.disp
k=0
σΩ1,Ω2,1...σ Ω1,Ω2,k(idk⊗R∇⊗idn−1−k).(6)
Hence,R∇= 0 directly impliesR∇n = 0 for alln. The proof is deferred until later, see Lemma 5.4.
Armed with these tensor product connections ∇n, we now deﬁne
jk∶A→Jk
A, j k(s) =
k
/summation.disp
i=0
∇is; ∇i∶A→Ω1⊗Ai, ∇is=∇i−1∇i−1s=∇i−1∇i−2... ∇ds
where ∇0 = id and ∇1 = d. We will need to show that the higher order derivatives ∇i land in the
right places so that imjk ⊆Jk
A and that jk is a bimodule map for the ●k actions on Jk
A and left
and right multiplication on A. This will entail extensive use of braided binomials [n
k,σ] cf [16],
in line with the braided integers [n,σ] encountered already in Section 3.
14 SHAHN MAJID AND FRANCISCO SIM ˜AO

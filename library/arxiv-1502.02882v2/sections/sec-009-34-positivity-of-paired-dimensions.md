---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams Bruce Bartlett"
section_id: sec-009-34-positivity-of-paired-dimensions
section_title: "Positivity of paired dimensions"
section_number: 3.4
pages: 14-16
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
doc_brief: "Fusion categories via string diagrams Bruce Bartlett — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
In this subsection, we show that the paired dimensions d{i,i∗} are positive real
numbers.
The ﬁrst step is to show that a root choice gives rise to a ‘twisted’ homo-
morphism from the Grothendieck ring to C, which is to be compared with (13).
Proposition 3.17 (cf. [9, pg. 593]) . In any root choice {di}, we have
djdk =
∑
i
Tr(Ti
jk)di.
Proof.
djdk =
=
=
∑
i,α
=
∑
i,α
ϵi
jk,αdi (by Lemma 3.15)
=
∑
i
Tr(Ti
jk)di.
Lemma 3.18 (cf. [9, pg 594]) . The numbers Tr(Ti
jk) have the following sym-
metry properties:
(i) Tr(Ti
jk) = Tr(Tk∗
i∗j) (Conjugate cyclic)
(ii) Tr(Ti
jk) = Tr(Ti∗
k∗j∗) (Conjugate symmetric)
Proof. To establish (i), suppose that {eα : Xi → Xj⊗Xk} are eigenvectors
of Ti
jk, so that Ti
jkeα = ϵi
jk,αeα. Choose arbitrary right duals ( X∗
i,ηi,ϵi) and
(X∗
k,ηk,ϵk) for Xi and Xk. Then the basis for Hom( X∗
k,X∗
i,Xj) given by
fα :=
14
are also eigenvectors of Tk∗
i∗,j with the same eigenvalues as the eα, since
Tk∗
i∗,j(fα) =
 =ϵi
jk,α
 =ϵi
jk,αfα.
The proof of (ii) is similar, except one uses the dual basis{ˆeα : Xj⊗Xk→Xi}
to deﬁne a basis {gα} for Hom(X∗
i,X∗
k⊗X∗
j ) by setting
gα :=
 .
A similar string diagram argument then establishes that Ti∗
k∗j∗gα =ϵi
jk,αgα.
Theorem 3.19 (cf. [9, Thm 2.3]) . The paired dimensions d{i,i∗} are real and
positive.
Proof. We organize the various roots di≡
 into a column vector:
d =
(
,
 ,...,
)T
.
Deﬁne the matrices Aj via [Aj]ik = Tr(Tk
ji). Then Proposition 3.17 says that d
is a simultaneous eigenvector of each Aj with eigenvaluedj, i.e.
Ajd =djd.
Thus we have AjAj∗d = djdj∗d = d{j,j∗}d and so d{j,j∗} is an eigenvalue of
the matrix AjAj∗. But Aj∗ = AT
j , by the symmetry properties established in
Lemma 3.18:
[Aj∗]ik = Tr(Tk
j∗i)
= Tr(Ti∗
k∗j∗)
= Tr(Ti
jk)
= [Aj]ki.
Thus d{j,j∗} is an eigenvalue of the positive deﬁnite real matrix AjAT
j and is
therefore real and positive.
15
Remark 3.20. From now on, we will always work in the canonical root choice
on a fusion category given by the positive square roots of the paired dimensions,
di =√d{i,i∗}.
Corollary 3.21 (cf. [9, Prop 8.21]) . A fusion category is pseudo-unitary if
and only if its Frobenius-Perron dimensions equal its fusion dimensions, that is
d+
i =di for all i∈I.
Proof. It suﬃces to show that di≤d+
i for all i∈I. Use the Frobenius-Perron
dimensions to deﬁne a norm on C|I| by setting‖x‖ =∑
kd+
k|xk|. Then we can
estimate the operator norm of the operators Aj from the proof of Theorem 3.19
as follows:
‖Ajx‖ =
∑
k
d+
k
⏐⏐⏐⏐⏐
∑
i
Tr(Ti
jk)xi
⏐⏐⏐⏐⏐
≤
∑
k,i
d+
kNi
jk|xi|
=
∑
i,k
d+
kNk
ji∗|xi|
= d+
j
∑
i
d+
i∗|xi|
= d+
j‖x‖.
In the second line we used Tr( Ti
jk) ≤ Ni
jk, in the third line the symmetry
Ni
jk = Nk
ji∗, in the fourth line we used the deﬁnition of the Frobenius-Perron
dimensions, and in the ﬁfth line we used d+
i∗ =d+
i .
Corollary 3.22. In a pseudo-unitary fusion category, the pivotal operators Ti
jk
are the identity maps.
Proof. Combining eq. (13) with Proposition 3.17 and Corollary 3.21, we have
djdk =
∑
i
Tr(Ti
jk)di≤
∑
i
Ni
jkdi =djdk
and hence we must have Ti
jk = id.

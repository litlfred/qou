---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-013-41-monodromy-interpretation-of-the-pivotal-opera
section_title: "Monodromy interpretation of the pivotal operators"
section_number: 4.1
pages: 21-21
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
Monodromy interpretation of the pivotal operators
We can write the pivotal operators T i
jk as the conjugate of a product of cyclic
operators, deﬁned as follows. Write Vijk = Hom(1, Xi ⊗(Xj ⊗Xk)).
Deﬁnition 4.1. In a fusion category, the cyclic operators Cijk : Vijk →Vkij
are deﬁned as follows, using the pairing convention:
7→
The monodromy of the cyclic operators is the operator Tijk on Vijk given as the
composite
Tijk = Vijk
Cijk
−→Vkij
Ckij
−→Vjki
Cjki
−→Vijk .
Write Y and Y −1 for the ‘yanking’ maps
Y : Hom(Xi, Xj ⊗Xk) ⇄Hom(1, X∗
i ⊗Xj ⊗Xk)
deﬁned by making some choice of structure maps equipping X∗
i as the right dual
of Xi. The following lemma is immediate.
Lemma 4.2. The pivotal operator T i
jk computes as the conjugate of the mon-
odromy of the cyclic operators:
T i
jk = Y −1Ti∗jkY
Note that the statement of the lemma is well-deﬁned since the right-hand
side is independent of the right dual structure maps needed to deﬁne Y (the
dependency cancels due to the Y −1).
Remark 4.3. In the special case i = j = k, the trace of the cyclic operator Ciii
is closely related, but not equal, to the 3rd Frobenius-Schur indicator ν3(Xi)
of Xi, as deﬁned in [23]. The indicator ν3(Xi) needs a pivotal structure γ for
its deﬁnition, whence we will write it as νγ
3 (Xi), whereas the cyclic operator
Ciii is well-deﬁned on the underlying fusion category. The 3rd Frobenius-Schur
indicator νγ
3 (Xi) is deﬁned as the trace of an operator whose graphical formula
is identical to the inverse of the formula for Ciii in Deﬁnition 4.1, except it is to
be interpreted using the pivotal structure γ instead of the pairing convention.
Hence on simple objects Xi the relationship is
νγ
3 (Xi) = γi Tr(Ciii)
where γi ∈U(1) are the scalars deﬁning the pivotal structure (see Section 5.1).

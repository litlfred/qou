---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-017-appendix-a-on-lifting-idempotents
section_title: "Appendix A. On lifting idempotents"
section_number: null
pages: 41-42
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Re p(St)."
---
As we were unable to ﬁnd an appropriate reference, in this appendix we give
standard proofs of well-known results on lifting idempotents. Assume F is a ﬁeld,
u is an indeterminate, and A is a free F [[u]]-algebra of ﬁnite rank. Finally, for
a∈ A, let ¯a denote the image of a under the quotient map A→ A/Au. In this
appendix we will show that any idempotent in the F -algebra A/Au can be lifted
to an idempotent in A. First, we need the following lemma.
Lemma A.1. a is a unit in A if and only if ¯a is a unit in A/Au.
Proof. If a is a unit in A, then clearly ¯a is a unit in A/Au with ¯a−1 = a−1. Now
suppose ¯a is a unit in A/Au. Then there exists b∈A with ¯a¯b = ¯1 in A/Au. Hence
ab = 1 +xu for some x∈ A. Thus ab
(
1−∑∞
i=1xiui)
= 1 in A. Thus a is right
invertible. Similarly a is left invertible, hence invertible. □
Now we are ready to prove the following theorem on lifting idempotents.
Theorem A.2. Given an idempotent e∈A/Au, there exists an idempotent ε∈A
such that ¯ε =e (we say ε is a lift of e). Moreover, if two idempotents are conjugate
in A/Au, then their lifts are conjugate in A.
‡The equations in (6.14) are only deﬁned when m is suﬃciently large.
42 JONATHAN COMES AND VICTOR OSTRIK
Proof. To prove the ﬁrst statement let Ai := A/Aui for i > 0 and let ψi denote
the quotient map Ai→ Ai/Aiui−1 = Ai−1 for each i >1. Set e1 = e∈ A1. We
will inductively show that for each i >1 there exists an idempotent ei∈ Ai with
ψi(ei) = ei−1. The ﬁrst statement of the theorem will follow by letting ε be the
unique element ofA such thatε↦→ei under the quotient mapA→Ai for alli> 0.
Now, ﬁx i >1 and assume ei−1 is an idempotent in Ai−1. Choose ai∈ Ai with
ψi(ai) =ei−1 and set ei = 3a2
i− 2a3
i . Then ψi(ei) = 3e2
i−1− 2e3
i−1 =ei−1 in Ai−1.
It remains to show thatei is an idempotent inAi. Set bi =a2
i−ai. Then ψi(bi) = 0,
hence bi∈ Aiui−1. In particular, b2
i = 0 in Ai. Moreover, ei = ai− (2ai− 1)bi.
Since ai and bi clearly commute,
e2
i =a2
i− 2(2ai− 1)bi =a2
i− 4b2
i− 2aibi =a2
i− 2(a3
i−a2
i ) =ei in Ai.
To prove the second statement of the theorem, supposeε andε′ are idempotents
in A. First assume ¯ε = ¯xε′¯x−1 in A/Au for some x∈ A with ¯x invertible. By
Lemma A.1, x is invertible. It follows that xε′x−1 is an idempotent in A with
¯ε = xε′x−1 in A/Au. Therefore, it suﬃces to show ε and ε′ are conjugate in A
whenever ¯ε = ε′. To do so, consider the element a := εε′ + (1−ε)(1−ε′)∈ A.
If ¯ε = ε′, then ¯a = ¯1. Hence a is a unit in A (see Lemma A.1). Moreover,
εa =εε′ =aε′ so that ε =aε′a−1. □

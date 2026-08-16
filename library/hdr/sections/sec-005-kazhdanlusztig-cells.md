---
doc_id: hdr
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-005-kazhdanlusztig-cells
section_title: "Kazhdan–Lusztig cells"
section_number: null
pages: 20-21
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
doc_brief: "HAL Id: tel-01411063 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 27 sections: Algebras of"
---
Let ι be the algebra involution on Hq(W,L ) given by ι(q) = q−1 and ι(Ts) = T−1
s for s∈ S (as a
consequence, ι(Tw) = T−1
w−1 for all w∈W ). By [KaLu1, Theorem 1.1] (see [Lu3, Proposition 2] for the
unequal parameter case), for each w∈W , there exists an element Cw∈H q(W,L ) uniquely determined
by the conditions
ι(Cw) =Cw and ι(Cw) =Tw +
∑
x∈W,x<w
Px,wTx,
17
where < stands for the Chevalley–Bruhat order on W and Px,w∈ q−1Z[q−1]. The elements ( Cw)w∈W
also form a basis of Hq(W,L ), the Kazhdan–Lusztig basis.
Example 2.2 We haveC1 =T1 = 1 and, for all s∈S, Cs =
{ Ts if L(s) = 0
Ts +q−L(s)T1 if L(s)> 0 .
Using the Kazhdan–Lusztig basis, we can deﬁne the following three relations on W . For x,y ∈ W ,
we have:
• x←L y , if Cx appears with non-zero coeﬃcient in hCy for some h∈H q(W,L ).
• x←R y , if Cx appears with non-zero coeﬃcient in Cyh′ for some h′∈H q(W,L ).
• x←LR y , if Cx appears with non-zero coeﬃcient in hCyh′ for some h, h′∈H q(W,L ).
If now we take the transitive closures of the above relations, we can deﬁne the following three preorders
on W :⩽L,⩽R,⩽LR.
The preorder⩽L deﬁnes an equivalence relation∼L on W as follows:
x∼L y ⇔ x⩽L y and y⩽L x.
The equivalence classes for ∼L are called left cells . Similarly, one can deﬁne equivalence relations ∼R
and∼LR on W , whose equivalence classes are called, respectively, right cells and two-sided cells.
Example 2.3 Following the notation of Example 2.1, for W = S3 ={1,s,t,st,ts,sts =tst} andl> 0,
• the left cells are {1},{s,ts},{t,st} and{sts} ;
• the right cells are{1},{s,st},{t,ts} and{sts} ;
• the two-sided cells are{1},{s,t,st,ts } and{sts}.
If l = 0, then all elements of W belong to the same cell (left, right or two-sided).
Let now C be a left cell of W . The following two Z[q,q−1]-modules are left ideals of Hq(W,L ):
H⩽LC =⟨Cy|y⩽L w,w ∈ C⟩Z[q,q−1] and H<LC =⟨Cy|y⩽L w,w ∈ C,y /∈ C⟩Z[q,q−1].
Then
MC :=H⩽LC/H<LC
is a free left Hq(W,L )-module with basis indexed by the elements of C.
Let K⊆ C be a ﬁeld such that the algebra K(q)Hq(W,L ) is split semisimple (for example, we can
takeK = C, or K = Q ifW is a Weyl group). Now, since the left cells form a partition of W , we obtain
a corresponding direct sum decomposition of K(q)Hq(W,L ):
K(q)Hq(W,L )∼=
⨁
C left cell
K(q)MC (isomorphism of left K(q)Hq(W,L )-modules), (2.1)
where K(q)MC := K(q)⊗Z[q,q−1]MC. We obtain analogous decompositions with respect to right and
two-sided cells.

---
doc_id: monodromyhitchiny
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-024-61-desingularization-of-families-of-nodal-curves
section_title: "Desingularization of families of nodal curves. We introduce the notation R = C[[τ ]],"
section_number: 6.1
pages: 9-10
source_pdf: MonodromyHitchinY.pdf
source_sha256: 1c9288ddbb5bc2d8
doc_brief: "HAL Id: hal-00465731 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 30 sections: YVES LASZLO"
---
K = C((τ )) and K the algebraic closure of K. For a variety B deﬁned over C we denote
BR = B × Spec(R) and BK = B × Spec(K).
Proposition 6.1. Let ~F = ( ~π : ~C → B ;s1,...,s n+2) be a family of smooth n + 2 pointed
(not necessarily connected) curves parameterized by a base variety B and let F0 = (π0 : C0 →
9
B;s1,...,s n) be the n-pointed family of nodal curves obtained from ~F by identifying the two
pointssn+1(b) and sn+2(b) of ~Cb = ~π−1(b) for each point b ∈ B . Then there exists a ﬂat family
FR = (πR : CR → B R;s1,R,...,s n,R),
such that
(1) the restriction of FR to the special ﬁber (FR)0 is isomorphic to F0,
(2) the generic ﬁber FK is a family of smooth n-pointed curves over BK.
Proof. Let b ∈ B . We denote by A = ˆOB,b the completion of the local ring OB,b and by
π0 : C0 → Spec(A) the pull-back of the family F0 of nodal curves of genus g to Spec(A). We
introduce the formal deformation space Γ → M of the stable n-pointed nodal curve ( C0)b =C
with one node z ∈C (see [DM] section 1). Then we have the cartesian diagram
C0 − − − →Γ

↓


↓
Spec A
s
− − − → M,
as well as n sections σi : M → Γ. By [DM] page 82, we have
M = Spec C[[t1,...,t 3g−3+n]], and ˆOΓ ,z ∼= C[[t1,...,t 3g−3+n,u,v ]]/(uv −t1),
where t1 = 0 is the equation of the locus of singular curves in M. The classifying map
s : Spec A → Spec C[[t1,...,t 3g−3+n]] = M sends t1 to 0 ∈ A (since Spec A parameterizes
singular curves) and ti to an element fi ∈ A for i ≥ 2. We extend s to ˆs : Spec A[[τ ]] − →
Spec C[[t1,...,t 3g−3+n]] by mapping t1 to τ and ti to fi for i ≥ 2. The base change by ˆs then
deﬁnes an n-pointed family FR over Spec A[[τ ]] such that F|Spec A((τ )) is smooth.
Hence, we have constructed the n-pointed family FR over Spec A[[τ ]] for any complete local
ring A = ˆOB,b, which proves the theorem. □

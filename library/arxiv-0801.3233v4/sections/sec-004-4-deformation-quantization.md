---
doc_id: arxiv-0801.3233v4
doc_title: "Contemporary Mathematics Twisted Deformation Quantization of Algebraic Varieties (Survey) Amnon Yekutieli"
section_id: sec-004-4-deformation-quantization
section_title: "Deformation Quantization"
section_number: 4
pages: 5-6
source_pdf: 0801.3233v4.pdf
source_sha256: d98f9d4a9ecb4c5e
doc_brief: "Contemporary Mathematics Twisted Deformation Quantization of Algebraic Varieties (Survey) Amnon Yekutieli — Let X be a smooth algebraic variety over a ﬁeld of characteristic 0."
---
4. Deformation Quantization
Kontsevich [Ko1] proved that any Poisson deformation of a realC∞manifold
X can be canonically quantized. In this section we present an algebraic version of
this result. But ﬁrst a deﬁnition.
Deﬁnition 4.1.LetA be a Poisson deformation ofOX. Aquantization ofA is an
associative deformationB, such that the ﬁrst order brackets satisfy
{−,−}B ={−,−}A.
Recalling Example 2.2, we see that this deﬁnition captures the essence of de-
formation quantization, namely quantizing a Poisson bracket onOX.
Theorem 4.2([Ye1]). Let K be a ﬁeld containingR, and letX be a smooth aﬃne
algebraic variety overK. There is a canonical bijection
quant :{formal Poisson brackets onOX[[ℏ]]}
gauge equivalence
≃
−→{star products onOX[[ℏ]]}
gauge equivalence .
which is a quantization as deﬁned above.
By “canonical” we mean that this quantization map commutes with étale mor-
phisms X′→X (and in particular with automorphisms ofX).
Actually our result in [Ye1] is stronger – it holds for a wider class of varieties,
not just aﬃne varieties. However all these cases are subsumed in Corollary 6.3
below.
On the other hand, it might be good to remark that when writing [Ye1] we did
not know Theorem A.5, and hence we only considered diﬀerential star products in
that paper. Now we know that there is no diﬀerence (up to gauge equivalence), so
Theorem 4.2 is correct as stated. In the context of complex manifolds this issue is
still open: it is not known if every star product is gauge equivalent to a diﬀerential
one! See [KS2].
It is important to note that even the aﬃne case of Theorem 4.2 is a “global
result”. In this context “local” means a suﬃciently small aﬃne open setU⊂X that
admits an étale coordinate system, namely an étale morphismU→An
K. This is
totally analogous to the case ofC∞manifolds studied by Kontsevich, where “local”
meant an open set in the manifoldAn
R = Rn.
Theorem 4.2 is a consequence of the following more general result.
Theorem 4.3 ([Ye1]). Let K be a ﬁeld containingR, and let X be a smooth
algebraic variety overK. There is a diagram
Tpoly,X

Dpoly,X

MixU(Tpoly,X)
Ψ σ // MixU(Dpoly,X)
where:
•MixU(Tpoly,X) and MixU(Dpoly,X) are sheaves of DG Lie algebras onX,
called mixed resolutions;
•the vertical arrows are DG Lie algebra quasi-isomorphisms;
•and the horizontal arrowΨσis an L∞quasi-isomorphism.
6 AMNON YEKUTIELI
The mixed resolutions combine thecommutative Čech resolutionassociated to
a suﬃciently reﬁned aﬃne open coveringU of X, and theGrothendieck sheaf of
jets. An L∞quasi-isomorphism is a generalization of a DG Lie algebra quasi-
isomorphism. The L∞quasi-isomorphism Ψσdepends on some choices; but the
dependence on these choices and on the coveringU disappears in homotopy. The-
orem 4.3 is proved using theFormality Theoremof Kontsevich [Ko1] and formal
geometry. More on the proof of Theorem 4.3 in Appendices B and C. A somewhat
diﬀerent approach to Theorem 4.3 can be found in Van den Bergh’s paper [VdB].

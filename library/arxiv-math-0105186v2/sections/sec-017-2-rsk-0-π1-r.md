---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-017-2-rsk-0-π1-r
section_title: "(r′−sk) + 0 = π(1 + r′"
section_number: 2
pages: 36-38
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
2 ).
Here we have used (1.20) for the ﬁrst term; and the last term is zero because,
without changing its cohomology class, one can modify δ to make its support ar-
bitrarily close to Z, in which case, since uk avoids the critical point x0, ˆuk would
not meet the support of δ. One can apply Gromov compactness to the sequence
ˆuk : ( ¯D(1),S 1)→ ( ˆEL, ˆQL); the limit of some subsequence will be a pseudo-
holomorphic “cusp disc” or “stable disc” ˆ u∞. Since im(ˆuk)⊂ (ˆπL)−1({sk}×
¯D(1)), we have im(ˆu∞)⊂ (ˆπL)−1({0}× ¯D(1)). Composing with ηL yields a
“cusp disc” u∞ inE whose boundary lies in ηL( ˆQL∩ (ˆπL)−1({0}×S1)) ={x0}.
Because Ω L is exact, u∞ is necessarily constant equal to x0. On the other hand,
the image of uk, for k large and in our subsequence, lies in an arbitrarily small
neighbourhood of the image of u∞. The rest is straightforward.
The second part of the proof of Proposition 2.13 is an explici t computation in
the local model (E,π ) from (2.18). Note that while this is not an exact Lefschetz
ﬁbration, it still makes sense to consider the spaces Ms of holomorphic sections
w : ¯D(s)→ Es with boundary in Qs. In fact Qs is a Lagrangian submanifold
of Cn+1, as one can see from (1.12), and the maximum principle ensure s that
any holomorphic disc in Cn+1 with boundary in Qs is actually contained in Es.
Lemma 2.16. Ms consists of maps w(z) = s−1/2az +s1/2¯a, where a∈ Cn+1
satisﬁes q(a) = 0 and||a||2 = 1/2. All these maps are regular, in the sense that
the associated Fredholm operators are surjective.
Proof. The holomorphic functions v : ¯D(s)→ C which satisfy v(z)∈ z1/2R
for all z∈ ∂ ¯D(s) are v(z) = s−1/2cz +s1/2¯c, for c∈ C. All components of
w∈ Ms must be of this form, and the conditions on a come from q(w(z)) = z.
As for regularity, since we are dealing with the standard com plex structure
J0 on Cn+1, Dw,J0 is an actual ¯∂-operator, see (2.5). Its kernel consists of
holomorphic mapsX : ¯D(s)→ Cn+1 such thatX(z)∈√zRn forz∈∂ ¯D(s), and
Dq(w(z))X(z) = 2 ∑
kwk(z)Xk(z) = 0 for all z. The same argument as before
determines all such X explicitly, the outcome being that ker Dw,J0
∼= R2n−1.
Using the Riemann-Roch formula for surfaces with boundary o ne computes
that indDw,J0 = 2n− 1, which shows that the cokernel is zero.
The condition on a can be written as
||rea||2 =||ima||2 = 1/4, ⟨rea, ima⟩= 0
so that Ms can be identiﬁed with the sphere bundle S(T ∗Sn) by mapping a to
(u,v ) = (−2 ima, 2 rea). With this and the diﬀeomorphism Sn→ Σ s,x↦→√sx,
36
one can identify the evaluation evs : Ms→ Σ s with the projection to the base
S(T ∗Sn)→Sn. This clearly represents the zero cycle in H∗(Sn; Z/2). Hence,
if one deﬁned an invariant Φ 1(Es,πs,Qs) in this local model, it would vanish.
Proof of Proposition 2.13. As in the proof of Lemma 2.15, we consider a holo-
morphic Morse chart ( ξ, Ξ) with Ξ deﬁned on E⊂ Cn+1 for some r′ > 0. We
know that for some suﬃciently small s >0, all u∈ ML,s lie in im(Ξ). Recall
that Ξ is holomorphic with respect to the standard complex st ructure J0 on E
and to J on EL; and that it takes Qs to QL,s. This implies that composition
with Ξ yields a diﬀeomorphism
Ms ∼= /d47/d47
evs
/d15/d15
ML,s
evs
/d15/d15
Σ s
Ξ /d47/d47 Σ L
s.
It is easy to see that, for w ∈ Ms and u = Ξ ◦w ∈ ML,s, the kernels and
cokernels of the associated operators Dw,J0, Du,J coincide. This shows that
J|EL,s is regular, and that the evaluation cycle ML,s→ Σ L
s can be identiﬁed
with projection S(T ∗Sn)→Sn, which as observed before is zero in homology;
together with (2.17) this completes the argument.
Remarks 2.17. (i) As pointed out in Remark 2.6, Φ 1 can be reﬁned to an
invariant taking values in unoriented bordism. Propositio n 2.13 also applies to
this reﬁnement, since (2.17) comes from a cobordism of moduli spaces and the
projectionS(T ∗Sn)→Sn is obviously cobordant to zero.
(ii) Suppose that (E1,π 1,Q 1) is a standard ﬁbration with its standard bound-
ary condition, and that we have another exact Lefschetz ﬁbra tion (E2,π 2,Q 2),
such that the two can be glued together to (E,π,Q ) as in Section 2.1. Proposi-
tion 2.13 together with Proposition 2.7 implies that Φ 1(E,π,Q ) will then be zero.
By pushing this reasoning a little further, one arrives at th e following result: let
(E,π ) be an arbitrary exact Lefschetz ﬁbration over a compact bas eS, with La-
grangian boundary condition Q. Assume that there is a path c : [a;b]→S with
c(a)∈∂S ,c−1(Scrit) ={b}, andc′(b)⁄= 0, whose vanishing cycle Vc(a) is isotopic
to Qc(a) as an exact Lagrangian submanifold in Ec(a); then Φ 1(E,π,Q ) = 0 .
(iii) Despite the vanishing of their Φ 1-invariant, the moduli spaces of pseudo-
holomorphic sections of a standard ﬁbration are never empty . To see this, one
has to use the invariant ˜Φ 2 mentioned in Remark 2.6. The computation of this
can be reduced to the local model in the same way as before, usi ng Lemma 2.15.
The relevant parametrized evaluation map then becomes
[0; 1]× Ms−→ [0; 1]× Σ s× Σ s,
(t,w )↦−→(t,w (s),eπi(1−t)w(se2πit)).
(2.21)
37
Here Σ se2πit → Σ s, x↦→eπi(1−t)x arises as parallel transport along ∂ ¯D(s) in
positive direction. Using Lemma 2.16 one can make (2.21) even more concrete,
identifying it with
[0; 1]×S(T ∗Sn)−→ [0; 1]×Sn×Sn,
(t,u,v )↦−→(t,v,−cos(πt)v− sin(πt)u).
It is now easy to see that ˜Φ 2(EL,πL,QL) is nonzero: it is the image of the
fundamental class [Sn×Sn] under the map
H∗(Sn×Sn; Z/2)→H∗(Sn×Sn, ∆ ∪ ∆; Z/2)∼=
∼=H∗([0; 1]×Sn×Sn,{0}× ∆ ∪{ 1}× ∆; Z/2)
where ∆ , ∆ are the diagonal and antidiagonal, respectively.

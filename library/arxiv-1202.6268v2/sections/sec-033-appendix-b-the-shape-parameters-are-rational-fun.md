---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-033-appendix-b-the-shape-parameters-are-rational-fun
section_title: "Appendix B. The shape parameters are rational functions on the character variety"
section_number: null
pages: 39-40
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
character variety
In this appendix, we prove that the shape parameters of a regular ideal triangulation are
rational functions on Y geom
M , the geometric component of the SL 2(C) A-polynomial curve.
Proposition B.1. Fix a regular ideal triangulation T of a one-cusped hyperbolic manifold
M. Then every shape parameter of T is a rational function on Y geom
M .
Proof. The proof is a little technical, and follows from work of Dunﬁeld [ Dun99, Cor.3.2],
partially presented in the appendix to [ BDR V]. For completeness, we give the details of the
proof here. We thank N. Dunﬁeld for a careful explanation of his pr oof to us.
Consider the aﬃne variety R(M, SL(2, C)) = Hom(π1, SL(2, C)) and its algebrogeometric
quotientXM, PSL(2, C) by the conjugation action of PSL(2, C). Following Dunﬁeld from the Ap-
pendix to [ BDR V], let R(M, SL(2, C)) denote the subvariety of R(M, SL(2, C))×P 1(C) con-
sisting of pairs (ρ,z ) wherez is a ﬁxed point of ρ(π1(∂M )). Let X M, SL(2, C) denote the algebro-
geometric quotient of R(M, SL(2, C)) under the diagonal action of SL(2 , C) by conjugation
and M¨ obius transformations respectively. We will call elements (ρ,z )∈R(M, SL(2, C)) aug-
mented representations. Their images in the augmented character variety X(M, SL(2, C))
will be called augmented characters and will be denoted by square brackets [( ρ,z )]. Like-
wise, replacing SL(2 , C) by PSL(2 , C), we can deﬁne the character variety XM, PSL(2,C ) and
its augmented version X M, PSL(2, C).
The advantage of the augmented character variety X M, SL(2, C) is that given γ∈ π1(∂M )
there is a regular function eγ that sends [( ρ,z )] to the eigenvalue of ρ(γ) corresponding to
z, using Lemma B.3 below. In contrast, in XM, SL(2, C) only the trace eγ +e−1
γ ofρ(γ) is well-
deﬁned. Likewise, in X M, PSL(2,C ) (resp. XM, SL(2, C)) only e2
γ (resp. e2
γ +e−2
γ ) is well-deﬁned.
From now on, we will restrict to the geometric component of the character varietyXM, PSL(2, C)
and we will ﬁx a regular ideal triangulation T . In [
Dun99, Thm.3.1] Dunﬁeld proves that
the natural restriction map
XM, PSL(2, C)−→X∂M, PSL(2, C)
of aﬃne curves is of degree 1. X∂M, PSL(2, C) is an aﬃne curve in ( C∗)2/Z2 and let VM, PSL(2, C)⊂
(C∗)2 denote the preimage of X∂M, PSL(2, C) of the 2:1 map ( C∗)2−→ (C∗)2/Z2. The commu-
tative diagram
(B.1)
X M, PSL(2, C) /d47/d47
/d15/d15
VM, PSL(2, C)
/d15/d15
XM, PSL(2, C) /d47/d47X∂M, PSL(2, C)
has both vertical maps of degree 2, and the bottom horizontal ma p of degree 1. Thus, it
follows that the top horizontal map is of degree 1. In [ BDR V, Sec.10.3] Dunﬁeld constructs
a degree 1 developing map
VT−→X M, PSL(2, C),
which combined with the previous discussion gives a chain of birational curve isomorphisms
(B.2) VT−→X M, PSL(2, C)−→VM, PSL(2, C)
40 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
Since the shape parameters are rational (in fact coordinate) fun ctions on VT , it follows that
they are rational functions on VM, PSL(2, C). Using the regular map VM, SL(2, C)−→VM, PSL(2, C),
we obtain that the shape parameters are rational functions on VM, SL(2, C). □
Proposition
B.1 has the following concrete corollary.
Corollary B.2. Given a regular ideal triangulation T withN tetrahedra, there is a solution
of the shape parameters in Q(m,ℓ )/(A(m,ℓ )).
Lemma B.3. Suppose A =
(
a b
c d
)
∈ SL(2, C) and c⁄= 0. Then, λ is an eigenvalue of A if
and only if z = (λ− 2d)/(2c) is a ﬁxed point of the corresponding M¨ obius transformation in
P 1(C).

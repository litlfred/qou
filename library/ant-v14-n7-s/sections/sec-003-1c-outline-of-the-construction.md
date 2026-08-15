---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-003-1c-outline-of-the-construction
section_title: "1C. Outline of the construction"
section_number: null
pages: 5-6
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
when 9 is a normalised Bianchi modular eigenform of weight 0 (i.e., contributing to cohomology
with trivial coefﬁcients) for some imaginary quadratic ﬁeld F. From 9 we construct a class φ∗
9∈
H1
c(Y∗
F,1(n), R), where Y∗
F,1(n) is a Bianchi manifold with appropriate level structure. This cohomology
group is a free R-module of ﬁnite rank, and its Zp-linear dual is H2(Y∗
F,1(n), R)/(torsion). Ghate [1999]
showed that critical values of the Asai L-function can be obtained by pairing φ∗
9 with certain classes
in this H2 coming from classical weight 2 Eisenstein series. The main new ideas in the present paper
arise in controlling integrality of these Eisenstein classes as the level varies, thus putting them into a
compatible family from which we build a p-adic measure.
The ﬁrst input in our construction is a collection of maps, one for each m> 1 and a∈ OF, deﬁned by
YQ,1(m2N) ι→ Y∗
F,1(m2n) κa/m−−→Y∗
F,1(n),
whereι is the natural embedding, and κa/m is obtained by twisting the natural quotient map by
( 1
0
a/m
1
)
.
Here YQ,1(m2N) is the usual (open) modular curve for GL 2/Q of level m2N, where N= n∩ Z.
The second input is a collection of special cohomology classes (“Betti Eisenstein classes”) cCm2 N∈
H1(YQ,1(m2N), Z). These are constructed using Siegel units. The theory of Siegel units shows that these
classes satisfy norm-compatibility properties as m varies, and that their images in de Rham cohomology
are related to the Eisenstein series used in [Ghate 1999]. (The factor c refers to an auxiliary choice of
integer which serves to kill off denominators from these classes).
1672 David Loeﬄer and Chris Williams
With these deﬁnitions, we set
c4m,n,a:=(κa/m◦ι)∗(cCm2 N)∈ H2(Y∗
F,1(n), Z),
c8r
n,a:=
∑
t∈(Z/pr Z)
c4pr,n,at⊗[ t]∈ H2(Y∗
F,1(n), Z)⊗ Zp[(Z/pr)×].
The key theorem in our construction (Theorem 3.13) is that the classes c8r
n,a satisfy a norm-compatibility
relation in r. Both the statement of this norm-compatibility relation, and its proof, are very closely
analogous to the norm-compatibility relations for Euler system classes in [Lei et al. 2014; 2018].
From this, it follows that after renormalising using the Hecke operator (Up)∗ (the transpose of the
usual Up) the classes c8r
n,a form an inverse system. In particular, they ﬁt together to deﬁne an element
c8∞
n,a∈ eord,∗H2(Y∗
F,1(n), Zp)⊗Zp Zp[[Z×
p]],
where eord,∗ is Hida’s ordinary projector associated to(Up)∗. We view this as a bounded measure on Z×
p
with values in the(Up)∗-ordinary part of H2(Y∗
F,1(n), Zp). We then deﬁne the p-adic Asai L-function to
be the measure
cLAs
p (9):=⟨φ∗
9, c8∞
n,a⟩∈ R[[Z×
p]].
That this measure interpolates the critical values of the (complex) Asai L-function then follows from
[Ghate 1999] together with certain twisting maps (to obtain twisted L-values).
The case of higher-weight Bianchi forms (contributing to cohomology with nonconstant coefﬁcients)
is similar, although unavoidably a little more technical. Suppose 9 is such a form of weight(k, k). Using
[Ghate 1999] and the same twisting methods as in the weight (0, 0) case, one can prove algebraicity for
the critical value LAs(9,χ, j+ 1), where 0⩽ j⩽ k andχ(−1)(−1) j= 1, by pairing with classes in H2
arising from Eisenstein series of weight 2k− 2 j+ 2. For each such j, we deﬁne a compatible system
of cohomology classes with coefﬁcients in a suitable algebraic representation of GL2/F by applying a
p-adic moment map to our Siegel-unit classes, obtaining classes c8∞, j
n,a analogous to c8∞
n,a in the weight
(0, 0) construction. Again, this is a “Betti analogue” of a construction for étale cohomology which is
familiar in the theory of Euler systems [Kings 2015; Kings et al. 2017].
Pairingφ∗
9 with c8∞, j
n,a gives a p-adic measure on Z×
p, as above. Using Kings’ theory of p-adic
interpolation of polylogarithms, it turns out that after a twist by the norm this measure is actually
independent of j, and we deﬁne the p-adic Asai L-function cLAs
p (9) to be the measure for j= 0.
Moreover, the class c8∞, j
n,a can be explicitly related to weight 2k− 2 j+ 2 Eisenstein series, so that
integrating the functionχ( x)x j against cLAs
p (9) computes the value LAs(9,χ, j+ 1) (under the parity
condition above).

---
doc_id: ant-v14-n7-s-p01
doc_title: "p-adic Asai L-functions of Bianchi modular forms"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: ant-v14-n7-s-p01.pdf
source_sha256: 976199bfca4ac086
doc_brief: "p-adic Asai L-functions of Bianchi modular forms — 13 sections: Introduction; Preliminaries and notation; Siegel units and weight 2 Asai–Eis"
---
1A. Background. Several of the most important conjectures in modern number theory, such as the
Bloch–Kato and Beilinson conjectures, relate the special values of L-functions to arithmetic data. In
much of the work on these conjectures to date, an important role has been played by p-adic L-functions:
measures or distributions on Z×
p, for a prime p, interpolating the special values of a given complex
L-function and its twists by Dirichlet characters of p-power conductor. Such functions are expected to
exist in wide generality, but in practice they can be difﬁcult to construct, and there are large classes of
L-functions which at present are not known to have a p-adic analogue. In this paper, we provide such a
construction for a new class of L-functions: the Asai, or twisted tensor, L-functions attached to Bianchi
modular forms (automorphic forms for GL 2/F, where F is imaginary quadratic).
In order to construct our p-adic L-function, we use the Betti cohomology of a locally symmetric space
associated to GL2/F. Ghate [1999] showed that the critical values of the Bianchi Asai L-function and
its twists are computed by certain special elements in Betti cohomology, which can be reinterpreted as
pushforwards of cohomology classes for GL2/Q associated to Eisenstein series. However, interpolating
such classes p-adically is not straightforward. The key novelty in our construction is to simultaneously
vary two parameters: the choice of Eisenstein series, and the choice of embedding of GL2/Q in GL2/F.
This allows us to reduce the interpolation problem to a (much simpler) compatibility property of the
GL2/Q Eisenstein series.
Our construction uses techniques that are closely related to those found in [Lei et al. 2014; 2018] in
which Lei, Zerbes and the ﬁrst author constructed Euler systems (certain compatible families of étale
cohomology classes) for Rankin–Selberg convolutions of modular forms, and for the Asai representation
Loefﬂer was supported by the Royal Society University Research Fellowship “L-functions and Iwasawa theory”.
MSC2010: primary 11F67; secondary 11F41, 11F85, 11M41, 11S40.
Keywords: Asai L-function, p-adic L-function, Bianchi modular form, Betti-Eisenstein classes, Iwasawa theory.
1669
1670 David Loeﬄer and Chris Williams
of a Hilbert modular form over a real quadratic ﬁeld. In the Bianchi setting, there is no étale cohomology
to consider, since Bianchi manifolds (the symmetric spaces associated to GL2/F) are not algebraic
varieties. However, we show in this article that applying the same techniques in this setting instead gives
compatible families of classes in the Betti cohomology of these spaces. Hence the same techniques used
to construct an Euler system for GL2/F when F is real quadratic also give rise to a p-adic L-function
when F is imaginary quadratic.
We hope that these techniques can be extended to build other new p-adic L-functions as “Betti counter-
parts” of known Euler system constructions; in particular, we are presently exploring applications of this
method to the standard L-function of (possibly non-self-dual) cohomological automorphic representations
of GL3/Q.
Note. While working on this project, we learned that Balasubramanyam, Ghate and Vangala [Balasubra-
manyam et al. 2019] have also been working on a construction of p-adic Asai L-functions for Bianchi
cusp forms. Their work is independent of ours, although both constructions rely on [Ghate 1999].
1B. Statement of the main theorem. Let9 be a Bianchi modular form of weight(k, k), for some k> 0,
which is an eigenform for the Hecke operators. We assume that the level n of9 is divisible by all primes
p| p of F; this leads to no loss of generality, since we may replace 9 by a p-stabilisation if necessary.
We let N be the integer generating the ideal n∩ Z.
The Asai L-function of9 is deﬁned by
LAs(9, s):= L(N)(ε9,Q, 2s− 2k− 2)
∑
n>1
c(nOF,9) n−s,
whereε9,Q is the restriction to ˆZ
×
of the nebentypus character of 9, L(N)(−) denotes the Dirichlet
L-function with its Euler factors at primes dividing N omitted, and c(m,9) is the Hecke eigenvalue of9
at the ideal m. We deﬁne similarly the twisted Asai L-function LAs(9,χ, s), for a Dirichlet character χ
(see Deﬁnition 2.10 below).
This function LAs(9, s) has an Euler product, in which the factors at primes 𝓁 ∤ N can be interpreted
in terms of Galois representations: they are the local Euler factors of the tensor induction to Gal(Q/Q)
of the compatible family of 2-dimensional 𝓁-adic representations of Gal(Q/F) attached to9. (We shall
discuss the Euler factors at the “bad” primes in Section 2F below.) The Asai L-function should not be
confused with the standard L-function
Lstd(9, s):=
∑
mPOF
c(m,9) Nm(m)−s
that corresponds to the usual (rather than tensor) induction of the same family ofGal(F/F)-representations.
We choose a ﬁnite extension L/Qp, containing F and the Hecke eigenvalues of 9, with ring of
integers R, and we assume that 9 is ordinary at p, i.e., c(pOF,9) is a unit in R.
p-adic Asai L-functions of Bianchi modular forms 1671
Theorem 1.1. For any integer c> 1 coprime to 6n, there exists a p-adic measure
cLAs
p (9)∈ R[[Z×
p]]
on Z×
p satisfying the following interpolation property: ifχ is a Dirichlet character of conductor pr, and
0⩽ j⩽ k, then we have
∫
Z×p
χ( x)x j dcLAs
p (9)(x)=
{(∗)LAs(9,χ, j+ 1) ifχ(−1)(−1) j= 1,
0 ifχ(−1)(−1) j=− 1,
where(∗) is an explicit factor (which is always nonzero if r> 1).
See Theorem 7.5 of the main text for a precise statement. Note that cLAs
p interpolates all critical values
in the left half of the critical strip. The critical values in the right half are related to these via a functional
equation, but we do not make this explicit.
It is possible to remove the dependence on c entirely if the restriction to Q of the character of 9
is nontrivial and does not have p-power conductor. If this condition is not satisﬁed, then we can only
remove c at the cost of passing to a slightly larger space of “pseudomeasures”, which may be interpreted
as meromorphic (rather than analytic) functions on p-adic weight space; this is a p-adic counterpart of
the fact that, for certain eigenforms 9, the Asai L-function and its twists can have poles. The details of
this are contained in Section 6B.
1C. Outline of the construction. We ﬁrst give a brief outline of the construction in the simplest case,
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

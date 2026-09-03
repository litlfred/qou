---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF F AREY MANIFOLDS"
section_id: sec-017-51-a-normal-form-for-3braids
section_title: "A normal form for 3–braids"
section_number: 5.1
pages: 27-28
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
doc_brief: "CUSP AREAS OF F AREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on t he cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2 –bridge link"
---
generators for B3, the braid group on three strands, as in Figure 1. Thus a posit ive word in
σ1 and σ−1
2 represents an alternating braid diagram. Let C = (σ1σ2)3 denote a full twist of
all three strands; C generates the center of B3. For a braid w ∈ B3, let ˆw denote the link
obtained as the closure of w. Note that ˆw only depends on the conjugacy class of w. We
denote the conjugacy relation by ∼.
In the 1920s, Schreier developed a normal form for this braid group [51]. In particular, he
showed the following.
Theorem 5.1 (Schreier). Let w ∈ B3 be a braid on 3 strands. Then w is conjugate to a
braid in exactly one of the following forms:
(1) C kσp1
1 σ−q1
2 · · ·σps
1 σ−qs
2 , where k ∈ Z and pi, qi, and s are all positive integers,
(2) C kσp
1, for k,p ∈ Z
(3) C kσ1σ2, for k ∈ Z
(4) C kσ1σ2σ1, for k ∈ Z, or
(5) C kσ1σ2σ1σ2, for k ∈ Z.
This form is unique up to cyclic permutation of the word follow ing C k. Braids in form (1)
above are called generic.
Birman and Menasco have shown that nearly every oriented lin k obtained as the closure
of a 3–braid can be represented by a unique conjugacy class in B3, with an explicit list of
exceptions [11]. Thus their theorem, combined with Schreie r’s normal form, gives a classiﬁca-
tion of closed oriented 3–braids. Their paper also contains a modern exposition of Schreier’s
algorithm for placing braids in normal form.
Let K = ˆw be a closed 3–braid deﬁned by the word w, and let A be the braid axis of K.
That is, A is an unknot with the property that the solid torus S3/integerdivideA is swept out by meridian
disks, with each disk intersecting K in 3 points. Then Mw :=S3/integerdivide(K ∪A) is a 4–punctured
sphere bundle over the circle. It is well–known, essentiall y due to work of Thurston [55],
that the Schreier normal form of w predicts the geometry of Mw. We include a proof for
completeness.
Theorem 5.2. Mw is hyperbolic if and only if w is generic. Moreover, Mw has nonzero
Gromov norm if and only if w is generic.
28 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
Proof. The braid generators σ1 and σ−1
2 act on the 4–punctured sphere as the standard
generators L and R of SL2(Z):
σ1 ↦→L :=
[
1 0
1 1
]
, σ −1
2 ↦→R :=
[
1 1
0 1
]
, C ↦→I =
[
1 0
0 1
]
.
Thus generic 3–braids with normal form (1) correspond to pos itive words employing both
lettersL andR, hence to pseudo-Anosov monodromies. Thurston showed that a bundle over
S1 with pseudo-Anosov monodromy is hyperbolic [55]. More conc retely, Gu´ eritaud showed
how to construct the hyperbolic metric from a positive word i n L and R [31]. (See Sections
2.2 and 2.3 above for a review of the connection between the mo nodromy word and the
canonical ideal triangulation of Mw.)
The braids with normal form (2) correspond to reducible mono dromies of the form Lp. In
this case, Mw is a graph manifold obtained by gluing two 3–punctured spher e bundles along
a torus. The braids with normal forms (3–5) correspond to per iodic monodromies, hence Mw
is Seifert ﬁbered. Thus all non-generic normal forms yield n on-hyperbolic manifolds with
Gromov norm 0. □

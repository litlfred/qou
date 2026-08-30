---
doc_id: arxiv-math-0006051v1
doc_title: "Finite and p-adic polylogarithms"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 0006051v1.pdf
source_sha256: 10483e75bd3655ea
doc_brief: "Finite and p-adic polylogarithms — 8 sections: AMNON BESSER; Introduction; The proof"
---
The ﬁnite logarithm was introduced by Kontsevich (under the name “ The 1 1
2
logarithm”) in [Kon]. The ﬁnite logarithm is the case n = 1 of the n-th poly-
logarithm li n ∈ Z/p [z] deﬁned by li n(z) = ∑ p− 1
k=1 zk/k n. In loc. cit. Kontsevich
proved that the ﬁnite logarithm satisﬁes a 4-term functional equa tion, known as
the fundamental equation of information theory. The same funct ional equation is
satisﬁed by the so called inﬁnitesimal dilogarithm −(x log |x| + (1 − x) log |1 − x|).
Cathelineau [Cat96] deﬁned general inﬁnitesimal polylogarithms and found that
they satisfy interesting functional equations. It was the idea of E lbaz-Vincent and
Gangl [EVG00] that these functional equations should be satisﬁed by ﬁnite polylog-
arithms (The name “ﬁnite polylogarithm” is due to them). Inspired by their work,
Kontsevich raised the idea that the ﬁnite polylogarithm could be a red uction of an
inﬁnitesimal version of the p-adic polylogarithm, as deﬁned by Coleman [Col82]. If
such a connection is established, it makes sense to hope that funct ional equations
of the inﬁnitesimal p-adic polylogarithm can be established in a similar way to its
complex counterpart and that these then imply by reduction the fu nctional equa-
tions of the ﬁnite polylogs. A conjectural formula for the precise p-adic polylog
whose “derivative”, in the sense to be explained below, reduces to t he ﬁnite polylog
was formulated by Kontsevich and proved by him for small n. The purpose of this
short note is to prove such a connection between p-adic polylogarithms and ﬁnite
polylogarithms.
To state the main result we recall that Coleman deﬁned p-adic polylogarithms,
Lin : Cp → Cp. These functions are locally analytic in the sense that they are
given by a convergent power series on each residue disc in Cp. We deﬁne the
diﬀerential operator D by D = z(1 − z)d/dz . Let ¯Fp be the algebraic closure of
the ﬁnite ﬁeld with p elements and let W = W (¯Fp) be the ring of Witt vectors of
¯Fp, so W is the ring of integers of the maximal unramiﬁed extension of Qp. Let
σ : ¯Fp → ¯Fp be the automorphism which is the inverse of the p-power map. Let
X = {z ∈ W : |z| = |z − 1| = 1}. Our main result is then:
Theorem 1.1. For every n > 1 let
Fn(z) =
n− 1∑
k=0
ak logk(z) Lin− k(z) ,
with a0 = −n and
ak = (−1)k
(k − 1)! + (−1)k+1n
k! ,
for k > 0. Then the following holds for every p > n +1: One has DFn(X) ⊂ pn− 1W
and for every z ∈ X one has p1− nDFn(z) ≡ lin− 1(σ (z)) (mod p). Furthermore,
1
2 AMNON BESSER
the choice of the coeﬃcients ak is the unique choice of coeﬃcients in Q for which
the theorem holds for all p > n + 1.
We remark that for a given p there will be many other choices of coeﬃcients, for
example those which are suﬃciently congruent to the ak.
The author would like to thank Kontsevich for explaining the conject ure to him
and to Gangl for various comments and corrections. He would also lik e to thank
Nekov´ aˇ r who ﬁrst suggested to him the idea of a connection betw een ﬁnite and
p-adic polylogarithms.

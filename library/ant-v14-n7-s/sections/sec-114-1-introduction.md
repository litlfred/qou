---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-114-1-introduction
section_title: "Introduction"
section_number: 1
pages: 229-232
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
Let p be an odd prime, set q= pk for some positive integer k, and denote by Fq the ﬁnite ﬁeld with q
elements. To (the smooth completion of) any hyperelliptic curve C over Fq one associates a zeta function
ZC(s). Weil has shown that ZC(s)= 0 implies that s= 1
2+ it for some t∈ R.
It is widely believed that for any ﬁxed s= 1
2+ it , the “vast majority” of (hyperelliptic) curves do
not have s as a zero of their zeta function. For example, it follows from the work of Chavdarov [1997]
(and its improvement by Kowalski [2006]) that for any ﬁxed (large enough) g, the proportion of genus g
hyperelliptic zeta functions vanishing at s tends to 0 as q→∞ .
Here we are concerned with the growing g regime. Namely, for ﬁxed q (and s), we give an upper
bound on
hq,s:= sup
g
|{C∈ Hg(Fq): ZC(s)= 0}|
|Hg(Fq)| (1.1)
where Hg(Fq) is the family of genus g hyperelliptic curves over Fq. Our bound is better once q is large,
as given by our main result.
Theorem 1.2 (Theorem 3.2). Fix a prime p, a real number t, and set s= 1
2+ it . Then as k→∞ we
have
h pk,s≪ p−k/276. (1.3)
In particular, h pk,s tends to 0 as k tends to∞.
This complements (but does not quite match) lower bounds on hq,s obtained by Li [2018].
Restricting q to powers of a ﬁxed prime p is not always necessary. In case s⁄= 1
2, one can show
(see [Ray 2018]) using transcendental number theory (six exponentials theorem [Lang 1966, Chapter 2,
MSC2010: 11M38.
Keywords: nonvanishing, L-functions, function ﬁelds, Dirichlet characters.
1895
1896 Jordan S. Ellenberg, Wanlin Li and Mark Shusterman
Section 1]) that there are only ﬁnitely many p for which p−s is algebraic, so hq,s= 0 for any q not divisible
by these p (as ZC(s) is a rational function in q−s). Hence, it sufﬁces to work with one characteristic at a
time, as we do in the theorem above. For s= 1
2, since the upper bound in Corollary 2.6 holds for any 𝓁
when q is a perfect square, we can conclude limq→∞ hq,s= 0 ranging over q which is an even power of
a prime.
Additional motivation for Theorem 1.2 comes from the ability to write ZC(s) as a rational function in
q−s, with the numerator being a quadratic Dirichlet L-function. Interpreted in this language of Dirichlet
characters, Theorem 1.2 improves (for all sufﬁciently large q) upon [Bui and Florea 2018, Corollary 2.1](
they give a lower bound of more than94.27% nonvanishing at s= 1
2
)
. Regarding the analogous vanishing
problem for quadratic Dirichlet L-functions over Z, we refer to the work of Soundararajan [2000]. 1
As we explain in the last section, our theorem can be rephrased as an upper bound for the number of
quadratic twists of a constant abelian variety which have positive rank.
Corollary 1.4 (Corollary 3.3). Let A be a constant abelian variety deﬁned over Fq(x). For each
f ∈ Fqm[x], denote by A f the quadratic twist of A⊗ Fqm(x) by f . Let Rn,m be the set { f ∈
Fqm[x], squarefree, of deg n: A f has positive rank}. Then,
lim
m→∞
lim sup
n→∞
|Rn,m|
qm(n+1)= 0.
Motivated by [Bui and Florea 2018, Corollary 2.2] and the analogous results over Z of Conrey, Ghosh
and Gonek [Conrey et al. 1998], we bound the multiplicity of the zeros of ZC, and obtain further
information on nonvanishing at s= 1
2.
Theorem 1.5. Let C be a hyperelliptic curve of genus at least 2 over Fq and S be the set of Weierstrass
points of C. The Frobenius acts on S by permuting the 2g+ 2 Weierstrass points via some permutationπ.
Suppose that either
• g is even andπ is a(2g+2)-cycle; or
• π is the product of two disjoint cycles of odd length.
Then:
(1) The point s= 1
2 is not a zero of ZC.
(2) All zeros of ZC are of multiplicity at most 2. Moreover, ifπ is the product of two disjoint cycles of
coprime lengths, all zeros of ZC are simple.
In the language of Dirichlet characters, this implies in particular the nonvanishing (at the central point)
in the case of prime conductor of degree not divisible by 4 and therefore gives an explicit set of size on
order X/ log X of Dirichlet characters of conductor at most X which have L-functions nonvanishing at
the critical point. See the statement below.
1Results in [Bui and Florea 2018] and [Soundararajan 2000] were stated at point s= 1
2 but the methods can be extended to
prove the statement for any point on the critical line.
Nonvanishing of hyperelliptic zeta functions over ﬁnite ﬁelds 1897
Corollary 1.6. Letχ be a quadratic character over Fq(x) with conductor f∈ Fq[x]. If f is irreducible
and 4∤ deg f , then L
( 1
2,χ
)
⁄= 0.
In particular, the number of quadratic characters with irreducible conductor of size at most X whose
L-function does not vanish at s= 1
2 is≫ X/ log X as X→∞ . This result improves on the work
of Andrade and Keating [2013, Corollary 2.6] and of Andrade, Bae, and Jung [Andrade et al. 2016,
Corollary 2.8], which give a proportion on order (log X)−2, and goes beyond the methods of Andrade
and Baluyot [2020]. For the analogous problem over Z, we refer to the recent work of Baluyot and Pratt
[2018].
In fact, there is nothing special about hyperelliptic curves in Theorem 1.5. A similar “genus-theory”
argument allows us to handle the case of cyclic 𝓁-covers of P1 for an odd prime𝓁.
Theorem 1.7. Let𝓁 be an odd prime and let C be a(Z/𝓁Z)-cover of P1/Fq branched at a set S⊂ P1(Fq).
Letπ be the permutation induced by Frobenius on S, and suppose thatπ is the composition of disjoint
cycles of orders k1, k2,..., kr, all prime to𝓁.
(1) Suppose the ki are mutually coprime, and either r= 2 or q is not congruent to 1 modulo𝓁. Then
every zero of ZC is simple.
(2) Deﬁneκi to be ki if ki is odd and ki/2 if ki is even. Suppose that either
• q is congruent to 1 modulo𝓁 and r= 2; or
• There is no i such that qκi is congruent to 1 modulo𝓁.
Then the point s= 1
2 is not a zero of ZC.
We remark that this theorem, like Theorem 1.5 above, provides a set of size on order X/ log(X)a of
order-𝓁 Dirichlet characters of conductor at most X whose zeta functions are nonvanishing at s= 1
2, for
some power a∈(0, 1]. See Corollary 1.8 for example. This lower bound improves, for 𝓁= 3, upon
Corollary 1.3 of recent work by David, Florea and Lalin [2019] which gives a lower bound of the form
X 1−ϵ (for anyϵ> 0).
Corollary 1.8. Let𝓁 be an odd prime different from the characteristic of a ﬁxed ﬁnite ﬁeldFq. The number
of𝓁-cyclic Dirichlet characters over Fq(x) with conductor at most X and whose L-function does not
vanish at s= 1
2 is≫ X/(log X)1/2 as X→∞ .
The main idea that connects all the theorems in this paper is the study of L-functions modulo𝓁. The
value of an L-function over Fq(x) at a complex number s can be expressed as a polynomial P(T)∈ Z[T]
evaluated at T= q−s. So if we want to prove that P(T) is nonvanishing, it sufﬁces to prove that P(T) is
nonvanishing modulo𝓁 for some prime𝓁. For Theorem 1.2, we will show that, for suitably chosen 𝓁, the
vanishing mod𝓁 of the L-function is related to the dimension of a certain Frobenius eigenspace in the
𝓁-torsion of a hyperelliptic Jacobian over Fq; the average size of this eigenspace can then be controlled by
a point count on a moduli space over a ﬁnite ﬁeld, which is a modest generalization and explication of the
arguments in [Ellenberg et al. 2016] and [Lipnowski and Tsimerman 2019] respectively. For Theorem 1.5,
on the other hand, we argue that under the given condition on Weierstrass points the L-function ofχ f
1898 Jordan S. Ellenberg, Wanlin Li and Mark Shusterman
is nonvanishing mod 2 at s= 1
2. For the similar Theorem 1.7, the 𝓁 is again the order of the Dirichlet
character in question.

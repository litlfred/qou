---
doc_id: arxiv-0804.0917v1
doc_title: "Composition-Diamond Lemma for Modules ∗"
section_id: sec-004-universal-enveloping-module-for-a-sabinin-algebr
section_title: "Universal enveloping module for a Sabinin algebra"
section_number: null
pages: 11-16
source_pdf: 0804.0917v1.pdf
source_sha256: 887fbd8be47a2781
doc_brief: "Czechoslovak Mathematical Journal — 9 sections: Front matter; Introduction; Composition-Diamond lemma for left"
duplicate_of: "czechmathj-60-2010-1-4"
---
In this section, we deal with the universal enveloping module for a Sa binin algebra.
Deﬁnition 7.1 ([21]) A vector space V is called a Sabinin algebra if it is endowed with
multilinear operation ⟨; ⟩: for any x1, x 2, · · · , x m, y, z ∈ V and any m ≥ 0,
⟨x1, x 2, · · · , x m; y, z ⟩
11
satisfying the identities
⟨x1, x 2, · · · , x m; y, z ⟩ = −⟨x1, x 2, · · · , x m; z, y ⟩,
⟨x1, x 2, · · · , x r, a, b, x r+1, · · · , x m; y, z ⟩ − ⟨x1, x 2, · · · , x r, b, a, x r+1, · · · , x m; y, z ⟩
+
r∑
k=0
∑
α
⟨xα1, · · · , x αk, ⟨xαk+1, · · · , x αr ; a, b ⟩, · · · , x m; y, z ⟩ = 0,
σx,y,z(⟨x1, x 2, · · · , x r, x ; y, z ⟩ +
r∑
k=0
∑
α
⟨xα1, · · · , x αk; ⟨xαk+1, · · · , x αr ; y, z ⟩, x ⟩) = 0 ,
where α runs the set of all bijections of the type α : {1, 2, · · · , r } → { 1, 2, · · · , r }, i ↦→
α i, α 1 < α 2 < · · · < α k, α k+1 < · · · < α r, r ≥ 0, σ x,y,z denotes the cyclic sum by x, y, z .
Let X = {ai|i ∈ Λ } be a totally ordered basis of V . We deﬁne the deg-lex order on X ∗.
Let ∆ : V → V ⊗ V be a linear map which satisﬁes: ∆( ai) = 1 ⊗ ai + ai ⊗ 1, (Id ⊗ ∆)∆ =
(∆ ⊗ Id)∆ (coassociative) and if τ∆ = ∆ then τ(x ⊗ y) = y ⊗ x (cocommutative).
It is customary to write ∆( x) = ∑ x(1) ⊗ x(2).
Let T (V ) be the tensor algebra over V endowed with its natural structure of cocom-
mutative Hopf algebra, that is, V ⊆ P rim(T (V )) (the primitive element of T (V )). Let
⟨; ⟩ : T (V ) ⨂ V ⨂ V → V be a map. Then we may write the deﬁnition of a Sabinin
algebra very shortly as
⟨x; a, b ⟩ = −⟨x; b, a ⟩,
⟨x[a, b ]y; c, e ⟩ +
∑
⟨x(1)⟨x(2); a, b ⟩y; c, e ⟩ = 0,
σa,b,c(⟨xc; a, b ⟩ +
∑
⟨x(1); ⟨x(2); a, b ⟩, c ⟩) = 0 ,
where [ a, b ] = ab − ba.
Deﬁnition 7.2 ([21]) Let ( V, ⟨; ⟩) be a Sabinin algebra. Then
~S(V ) = T (V )/span ⟨xaby − xbay +
∑
x(1)⟨x(2); a, b ⟩y|x, y ∈ T (V ), a, b ∈ V ⟩
is called the universal enveloping module for V .
Since T (V ) ≃ k⟨X⟩ as k-algebras, we can view ~S(V ) as a right k⟨X⟩-module:
~S(V ) = mod⟨X|I⟩k⟨X⟩,
where I = {xab − xba + ∑ x(1)⟨x(2); a, b ⟩|x ∈ X ∗, a > b, a, b ∈ X}.
Then we have the following theorem.
Theorem 7.3 Let I be as above. Then I is the Gr¨ obner-Shirshov basis in mod⟨X⟩k⟨X⟩.
12
Proof: There are two kinds of compositions: w1 = xabc (a > b > c ) and w2 =
ucdvab (c > d, a > b ). Denote by
f1 = xabc − xacb +
∑
(xa)(1)⟨(xa)(2); b, c ⟩,
f2 = xab − xba +
∑
x(1)⟨x(2); a, b ⟩,
f3 = ucdvab − ucdvba +
∑
(ucdv)(1)⟨(ucdv)(2); a, b ⟩,
f4 = ucd − udc +
∑
u(1)⟨u(2); c, d ⟩.
Then
(f1, f 2)w1 = xabc − xacb +
∑
x(1)a⟨x(2); b, c ⟩ +
∑
x(1)⟨x(2)a; b, c ⟩
−xabc + xbac −
∑
x(1)⟨x(2); a, b ⟩c
≡ − xcab +
∑
x(1)⟨x(2); a, c ⟩b +
∑
x(1)a⟨x(2); b, c ⟩ +
∑
x(1)⟨x(2)a; b, c ⟩
+xbca −
∑
x(1)b⟨x(2); a, c ⟩ −
∑
x(1)⟨x(2)b; a, c ⟩ −
∑
x(1)⟨x(2); a, b ⟩c
≡
∑
x(1)c⟨x(2); a, b ⟩ +
∑
x(1)⟨x(2)c; a, b ⟩ +
∑
x(1)⟨x(2); a, c ⟩b
+
∑
x(1)a⟨x(2); b, c ⟩ +
∑
x(1)⟨x(2)a; b, c ⟩ −
∑
x(1)⟨x(2); b, c ⟩a
−
∑
x(1)b⟨x(2); a, c ⟩ −
∑
x(1)⟨x(2)b; a, c ⟩ −
∑
x(1)⟨x(2); a, b ⟩c
≡
∑
x(1)⟨x(2)a; b, c ⟩ +
∑
x(1)⟨x(2); ⟨x(3); b, c ⟩, a ⟩ +
∑
x(1)⟨x(2)b; c, a ⟩
+
∑
x(1)⟨x(2)c; a, b ⟩ +
∑
x(1)⟨x(2); ⟨x(3); c, a ⟩, b ⟩
+
∑
x(1)⟨x(2); ⟨x(3); a, b ⟩, c ⟩
≡ 0
since σa,b,c(⟨xc; a, b ⟩ + ∑ ⟨x(1); ⟨x(2); a, b ⟩, c ⟩) = 0.
13
(f3, f 4)w2 = ucdvab − ucdvba +
∑
u(1)v(1)⟨u(2)cdv(2); a, b ⟩ +
∑
u(1)cv(1)⟨u(2)dv(2); a, b ⟩
+
∑
u(1)dv(1)⟨u(2)cv(2); a, b ⟩ +
∑
u(1)cdv(1)⟨u(2)v(2); a, b ⟩
−ucdvab + udcvab −
∑
u(1)⟨u(2); c, d ⟩vab
≡ − udcvba +
∑
u(1)⟨u(2); c, d ⟩vba +
∑
u(1)v(1)⟨u(2)cdv(2); a, b ⟩
+
∑
u(1)cv(1)⟨u(2)dv(2); a, b ⟩ +
∑
u(1)dv(1)⟨u(2)cv(2); a, b ⟩
+
∑
u(1)cdv(1)⟨u(2)v(2); a, b ⟩ + udcvba −
∑
u(1)v(1)⟨u(2)dcv(2); a, b ⟩
−
∑
u(1)cv(1)⟨u(2)dv(2); a, b ⟩ −
∑
u(1)dv(1)⟨u(2)cv(2); a, b ⟩
−
∑
u(1)dcv(1)⟨u(2)v(2); a, b ⟩ +
∑
u(1)v(1)⟨u(2)⟨u(3); c, d ⟩v(2); a, b ⟩
+
∑
u(1)⟨u(2); c, d ⟩v(1)⟨u(3)v(2); a, b ⟩ −
∑
u(1)⟨u(2); c, d ⟩vba
≡
∑
u(1)v(1)⟨u(2)[c, d ]v(2); a, b ⟩ +
∑
u(1)[c, d ]v(1)⟨u(2)v(2); a, b ⟩
+
∑
u(1)v(1)⟨u(2)⟨u(3); c, d ⟩v(2); a, b ⟩ +
∑
u(1)⟨u(2); c, d ⟩v(1)⟨u(3)v(2); a, b ⟩
≡
∑
(u(1)[c, d ] + u(1)⟨u(2); c, d ⟩)v(1)⟨u(3)v(2); a, b ⟩
+
∑
u(1)v(1)⟨u(2)[c, d ]v(2); a, b ⟩ +
∑
u(1)v(1)⟨u(2)⟨u(3); c, d ⟩v(2); a, b ⟩
≡ 0
since ⟨x[a, b ]y; c, e ⟩ + ∑ ⟨x(1)⟨x(2); a, b ⟩y; c, e ⟩ = 0.
Hence, I is a Gr¨ obner-Shirshov basis in mod⟨X⟩k⟨X⟩. □
Remark: From the above proof, we know that for ~S(V ) = mod⟨X|I⟩k⟨X⟩, the minimal
Gr¨ obner-Shirshov basis is
G = {xab − xba + ∑ x(1)⟨x(2); a, b ⟩|x = ai1 · · ·ain(i1 ≤ · · · ≤ in, n ≥ 0), a > b, a, b ∈ X}.
Now, by Lemma 3.2 and Theorem 7.3, we can easily get the following theo rem.
Theorem 7.4 ([21], Poincare-Birkhoﬀ-Witt) Let {ai|i ∈ Λ } be a totally ordered basis of
V . Then {ai1 · · · ain|i1 ≤ i2 ≤ · · · ≤ in, n ≥ 0} is a basis of ~S(V ).
Acknowledgement: The authors would like to express their deepest gratitude to Prof es-
sor L. A. Bokut for his kind guidance, useful discussions and enthu siastic encouragement.
We also thank Professor J. M. Perez-Izquierdo for some remarks .
References
[1] L. A. Bokut, Unsolvability of the word problem, and subalgebras o f ﬁnitely presented
Lie algebras, Izv. Akad. Nauk. SSSR Ser. Mat. , 36, 1173-1219(1972).
[2] L. A. Bokut, Imbeddings into simple associative algebras, Algebra i Logika , 15, 117-
142(1976).
14
[3] L. A. Bokut and Yuqun Chen, Grobner-Shirshov bases for Lie alg ebras: after A.I.
Shirshov, SEA Bull Math., 31, 811-831(2007).
[4] L. A. Bokut Y. Fong and W.-F. Ke, Gr¨ obner-Shirshov bases and composition lemma
for associative conformal algebras: an example, Contemporary Mathematics , N 264,
AMS, 63-91(2000).
[5] L. A. Bokut and A. A. Klein, Serre relations and Gr¨ obner-Shirsh ov bases for simple
Lie algebras. I, II, Internat. J. Algebra Comput. , 6, 389-400, 401-412(1996).
[6] L. A. Bokut and A. A. Klein, Gr¨ obner-Shirshov bases for excep tional Lie algebras. I,
Ring Theory. Selected Papers from the Conference Held in Miskolc, J uly 15-20, 1996,
Amsterdam(1998), pp. 51-57.
[7] L. A. Bokut and A. A. Klein, Gr¨ obner-Shirshov bases for excep tional Lie alge-
bras E6, E 7, and E8, Algebras and Combinatorivs, Springer-Verlag, Singapore, 37-
46(1999).
[8] L. A. Bokut and P. Malcolson, Gr¨ obner-Shirshov bases for qua ntum enveloping alge-
bras, Israel J. Math. , 96, 97-113(1996).
[9] L. A. Bokut and P. Malcolson, Gr¨ obner-Shirshov bases for rela tions of a Lie algebra
and its enveloping algebra, Algebras and Combinatorics , Springer-Verlag, Singapore,
47-54(1999).
[10] L. A. Bokut, S.-J. Kang, K.-H. Lee and P. Malcolmson: Gr¨ obner -Shirshov bases for
Lie super-algebras and their universal enveloping algebras, J. Algebra , 217, 461-495
(1999).
[11] E.S. Chibrikov, On free Lie conformal algebras, Vestnik Novosibirsk State University ,
4(1), 65-83(2004).
[12] James E. Humphreys, Introduction to Lie Algebras and Repres entation Theory,
Springer-Verlag, 2000, 1970.
[13] V.-G. Kac, Inﬁnite-Dimensional Lie Algebras, Cambridge Univers ity Press, Cam-
bridge, third edition, 1990.
[14] V.-G. Kac, Vertex Algebra for Beginners, University lecture series. , 10, AMS, Prov-
idence, RI, 1997.
[15] S.-J. Kang and K.-H. Lee, Gr¨ obner-Shirshov bases for repre sentation theory, J. Ko-
rean Math. Soc. , 37, 55-72(2000).
[16] S.-J. Kang and K.-H. Lee, Gr¨ obner-Shirshov bases for irredu cible sln+1-modules, J.
Algebra, 232, 1-20(2000).
[17] S.-J. Kang, I.-S. Lee, K.-H. Lee and H. OH, Hecke algebras, Spe che modules and
Gr¨ obner-Shirshov bases,J. Algebra, 252, 258-292(2002).
[18] S.-J. Kang, I.-S. Lee, K.-H. Lee and H. OH, Representations of Ariki-Koike algebras
and Gr¨ obner-Shirshov bases,Proc. London Math. Soc. , 89(3), 54-70(2004).
15
[19] S.-J. Kang and K.-H. Lee, Linear algebraic approach to Gr¨ obne r-Shirshov basis the-
ory, J. Algebra, 313, 988-1004(2007).
[20] P. Lalonde and A. Ram, Standard Lyndon bases of Lie algebras a nd enveloping
algebras, Trans. Amer. Math. Soc. , 347(5), 1821-1830(1995).
[21] J. M. Perez-Izquierdo, Algebras, hyperalgebras, nonassoc iative bialgebras and loops,
Advances in Mathematics , 208, 834-876(2007).
[22] E. N. Poroshenko, Gr¨ obner-Shirshov bases for the Kac-Mo ody algebras of the type
A(1)
n , Commun. Algebra, 30, No.6, 2617-2637(2002).
[23] E. N. Poroshenko, Gr¨ obner-Shirshov bases for the Kac-Mo ody algebras of the type
C (1)
n and D(1)
n , Vestn. Novosib. Gos. Univ. Ser. Mat. Mekh. Inﬀorm. , 2, No.1, 58-
70(2002).
[24] E. N. Poroshenko, Gr¨ obner-Shirshov bases for the Kac-Mo ody algebras of the type
B(1)
n , Int. J. Math. Game Theory Algebra , 13, No.2, 117-128(2003).
[25] M. Roitman, On the free conformal and vertex algebras, J. Algebra , 217(2), 496-
527(1999).
[26] A. I. Shirshov, Some algorithmic problem for Lie algebras, Sibirsk. Mat. Z. , 3(1962),
292-296(in Russian); English translation in SIGSAM Bull., 33(2), 3-6( 1999).
16

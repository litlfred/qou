---
doc_id: candetgl
doc_title: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics"
section_id: sec-015-vii-proof-of-theorem-d
section_title: "PROOF OF THEOREM D"
section_number: VII
pages: 23-25
source_pdf: candetgl.pdf
source_sha256: d788af715428b8b2
doc_brief: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics — 18 sections: INTRODUCTION; PRELIMINARIES; Fuller,9 Bauer, Crick, and"
---
It will be convenient to divide the statement and proof of Theorem D into three pieces, as
follows:
~1! The Biot–Savart operator BS:VF( V)!VF(V) is bounded, and hence extends to a bounded
operator on the L2 completion,
BS:VF~V!!VF~V!;
~2! The operator BS:VF(V)!VF(V) is compact, that is, it takes the unit ball in VF(V) to a set
with compact closure in VF(V);
~3! The operator BS:VF(V)!VF(V) is self-adjoint with respect to the L2 inner product, that is,
^V1 ,BS( V2)&5^BS(V1), V2&, for all vector ﬁelds V1 and V2 in VF(V).
A. A useful lemma
The proof that the Biot–Savart operator is bounded, as asserted in ~1! above, will follow along
the lines of the usual Young’s inequality proof that convolution operators are bounded; see
Folland,
47 p. 9, or Zimmer, 48 Proposition B.3 on p. 10. We extract this proof as a lemma, so that
we can use it again in the proof of part ~2!.
Lemma 3: Let f(x) be a scalar-valued function with the property that
NV~f!5maxy E
V
uf~y2x!u d~volx!
is ﬁnite, where the maximum is over all points y eR3. Then the operator T f :VF( V)!VF(V)
deﬁned by
Tf~V!~y!5 E
V
V~x! 3f~y2x!
y2x
uy2xu d~volx!
is a bounded map with respect to the L 2 norm, and furthermore ,
uTf~V!u < NV~f!uVu.
Proof: Fix yeV. Then, using the Cauchy–Schwarz inequality,
897J. Math. Phys., Vol. 42, No. 2, February 2001 The Biot –Savart operator
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
uTf~V!~y!u< E
V
uV~x!uuf~y2x!u d~volx!
5 E
V
uV~x!$f~y2x!%1/2uu $f~y2x!%1/2u d~volx!
<S E
V
uV~x!u2uf~y2x!u d~volx!D
1/2
S E
V
uf~y2x!u d~volx!D
1/2
<~NV~f!! 1/2
S E
V
uf~y2x!uu V~x!u2 d~volx!D
1/2
. ~7.1!
We square both sides, integrate and use Fubini’s theorem to get
E
V
uTf~V!~y!u2 d~voly!<NV~f! E
V
E
V
uf~y2x!uuV~x!u2 d~volx! d~voly!
5NV~f! E
V
uV~x!u2
S E
V
uf~y2x!u d~voly!Dd~volx!
<NV~f!2 E
V
uV~x!u2 d~volx!. ~7.2!
Taking square roots, we get
uTf~V!u < NV~f!uVu, ~7.3!
and conclude that Tf is a bounded operator whose norm is at most NV(f), as claimed.
B. Proof of 1

Deﬁne the optical size of V, written OS ~V!, to be the number
OS~V!5maxy E
V
1/uy2xu2 d~volx!, ~7.4!
where the maximum is taken over all points ye R3. The integral just above can be taken as a
measure of the effort required to optically scan the domain V from the location y; the optical size
of V is the maximum effort required to scan it from any location.
Then, in the language of Lemma 3,
BS~V!~y!5~1/4p! E
V
V~x!3~y2x!/uy2xu3 d~volx!
5Tf0~V!~y!, ~7.5!
where
f0~y2x!5~1/4p!~1/uy2xu2!. ~7.6!
The lemma yields immediately that, for Ve VF(V),
uBS~V!u < ~1/4p!OS~V!uVu, ~7.7!
and we conclude that BS:VF( V)!VF(V) is a bounded operator.
898 J. Math. Phys., Vol. 42, No. 2, February 2001 Cantarella, DeTurck, and Gluck
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
Now let VF(V) denote the L2 completion of the space VF ~V!; we will refer to the elements
of VF(V)a s L2 vector ﬁelds.
Then we can, and do, extend the Biot–Savart operator to a bounded operator,
BS:VF~V!!VF~V!, ~7.8!
with the same bound as above.
This completes the proof of part ~1!.

---
doc_id: candetgl
doc_title: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics"
section_id: sec-023-a-a-useful-lemma
section_title: "A useful lemma"
section_number: A
pages: 23-26
source_pdf: candetgl.pdf
source_sha256: d788af715428b8b2
toc_source: inferred
doc_brief: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics — 27 sections: Front matter; INTRODUCTION; PRELIMINARIES"
---
The proof that the Biot–Savart operator is bounded, as asserted in ~1! above, will follow along
the lines of the usual Young’s inequality proof that convolution operators are bounded; see
Folland,47 p. 9, or Zimmer,48 Proposition B.3 on p. 10. We extract this proof as a lemma, so that
we can use it again in the proof of part ~2!.
Lemma 3: Let f(x) be a scalar-valued function with the property that
NV~f!5maxyE
Vuf~y2x!u d~volx!
is ﬁnite, where the maximum is over all points yeR3. Then the operator Tf :VF(V)→VF(V)
deﬁned by
Tf~V!~y!5E
VV~x! 3f~y2x!
y2x
uy2xu d~volx!
is a bounded map with respect to the L2 norm, and furthermore,
uTf~V!u < NV~f!uVu.
Proof: Fix yeV. Then, using the Cauchy–Schwarz inequality,
897
J. Math. Phys., Vol. 42, No. 2, February 2001
The Biot–Savart operator
uTf~V!~y!u<E
VuV~x!uuf~y2x!u d~volx!
5E
VuV~x!$f~y2x!%1/2u u$f~y2x!%1/2u d~volx!
<SE
VuV~x!u2uf~y2x!u d~volx!D
1/2SE
Vuf~y2x!u d~volx!D
1/2
<~NV~f!!1/2SE
Vuf~y2x!u uV~x!u2 d~volx!D
1/2
.
~7.1!
We square both sides, integrate and use Fubini’s theorem to get
E
VuTf~V!~y!u2 d~voly!<NV~f!E
VE
Vuf~y2x!uuV~x!u2 d~volx! d~voly!
5NV~f!E
VuV~x!u2SE
Vuf~y2x!u d~voly!D d~volx!
<NV~f!2E
VuV~x!u2 d~volx!.
~7.2!
Taking square roots, we get
uTf~V!u < NV~f!uVu,
~7.3!
and conclude that Tf is a bounded operator whose norm is at most NV(f), as claimed.
B. Proof of „1…
Deﬁne the optical size of V, written OS~V!, to be the number
OS~V!5maxyE
V1/uy2xu2 d~volx!,
~7.4!
where the maximum is taken over all points ye R3. The integral just above can be taken as a
measure of the effort required to optically scan the domain V from the location y; the optical size
of V is the maximum effort required to scan it from any location.
Then, in the language of Lemma 3,
BS~V!~y!5~1/4p!E
VV~x!3~y2x!/uy2xu3 d~volx!
5Tf0~V!~y!,
~7.5!
where
f0~y2x!5~1/4p!~1/uy2xu2!.
~7.6!
The lemma yields immediately that, for Ve VF(V),
uBS~V!u < ~1/4p!OS~V!uVu,
~7.7!
and we conclude that BS:VF(V)→VF(V) is a bounded operator.
898
J. Math. Phys., Vol. 42, No. 2, February 2001
Cantarella, DeTurck, and Gluck
Now let VF(V) denote the L2 completion of the space VF~V!; we will refer to the elements
of VF(V) as L2 vector ﬁelds.
Then we can, and do, extend the Biot–Savart operator to a bounded operator,
BS:VF~V!→VF~V!,
~7.8!
with the same bound as above.
This completes the proof of part ~1!.
C. Proof of „2…
To prove that the Biot–Savart operator is compact, we use two standard facts from functional
analysis. First is the fact that for any compact domain V, if f(x) is continuous on R3, then the
integral operator
~Tff !~y!5E
Vf~y2x!f~x! d~volx!
~7.9!
deﬁnes a compact operator on L2(V); see Zimmer,48 Theorem 3.1.5 on p. 53. It is stated there
only for operators on scalar-valued functions, but the extension to vector-valued ones, using the
deﬁnition given in Lemma 9.3, is trivial.
Second is the fact that the norm-limit of compact operators is compact; see Zimmer,48 Lemma
3.1.3 on p. 52.
Now let
fN~x!5H
N2/4p
if uxu<1/N
1/~4puxu2!
if uxu>1/N.
~7.10!
Note that fN is a continuous function, and that
NV~f02fN!5maxyE
Vuw0~y2x! 2wN~y2x!u d~volx!
<~1/4p!E
uxu<1/N~~1/uxu2!2N2! d~volx!
<~1/4p!E
uxu<1/N~1/uxu2! d~volx!51/N.
~7.11!
By the ﬁrst functional analysis fact, TfN is a compact operator from VF(V) to VF(V). By our
Lemma, we see that as TfN converges in norm to Tf0, the Biot–Savart operator, as N→`. Using
the second functional analysis fact, we conclude that BS:VF(V)→VF(V) is a compact operator.
This completes the proof of part ~2!.
D. Proof of „3…
It is easy to see why the Biot–Savart operator is self-adjoint.
Suppose that V1 and V2 are smooth vector ﬁelds deﬁned on V. Then
899
J. Math. Phys., Vol. 42, No. 2, February 2001
The Biot–Savart operator
^V1 ,BS~V2!&5E
VV1~y!•BS~V2!~y! d~voly!
5E
VV1~y!•F~1/4p!E
VV2~x!3~y2x!/uy2xu3 d~volx!Gd~voly!
5~1/4p!E
V3VV1~y!3V2~x!•~y2x!/uy2xu3 d~volx! d~voly!
5~1/4p!E
V3VV2~x!3V1~y!•~x2y!/ux2yu3 d~voly! d~volx!
5^V2 ,BS~V1!&.
~7.12!
It is a straightforward exercise to check that these improper integrals are all convergent.
Thus BS:VF(V)→VF(V) is a self-adjoint operator, and therefore remains self-adjoint when
extended to the L2 completion VF(V) of VF~V!.
Theorem D is proved.

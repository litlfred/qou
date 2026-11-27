---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-016-62-functions-on-the-group-s3
section_title: "Functions on the group S3"
section_number: 6.2
pages: 33-34
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
generators u = (12), v = (23) and set w = (13) so that uvu =vuv =w. Its algebra of functions
A = C(S3) has a standard 3-dimensional Ω 1 with left-invariant basis eu,ev,ew and relations in
degree 2 of the exterior algebra
e2
a = 0, e u∧ev+ev∧ew+ew∧eu = 0, e v∧eu+ew∧ev+eu∧ew = 0,
deu =−ev∧ew−ew∧ev, dev =−ew∧eu−eu∧ew, dew =−eu∧ev−ev∧eu.
The relations with functions are eaf =Ra(f)ea where a=u,v,w and Ra(f)(g) =f(ga) denotes
the right translation operator. The calculus is inner by θ =eu+ev+ew. Moreover, the products
of u,v,w are never in the set {u,v,w }, hence there can be no bimodule map α∶Ω1→Ω1⊗A Ω1,
as a bimodule map must respect the commutation relations with functions, which in our case
means it must respect the S3-grading where /divides.alt0eu/divides.alt0= u, etc. Hence, all connections ∇on Ω 1 are
inner.
Proposition 6.2. Ω(S3) admits precisely two left-invariant ﬂat torsion free connections obeying
the braid relations, given by q =e±2πi
3 , namely
∇eu = 1
q−1 /parenleft.alt1qeu⊗eu+qeu⊗(ev+ew)+q(ev+ew)⊗eu+ev⊗ew+ew⊗ev+q−1ev⊗ev+q−1ew⊗ew/parenright.alt1
and the same for a permutation of u,v,w . For the braiding, we have
σ(eu⊗eu) = 1
1−q /parenleft.alt1eu⊗eu+q−1ev⊗ev+q−1ew⊗ew/parenright.alt1,
σ(ev⊗ev) = 1
1−q /parenleft.alt1q−1eu⊗eu+ev⊗ev+q−1ew⊗ew/parenright.alt1,
σ(ew⊗ew) = 1
1−q /parenleft.alt1q−1eu⊗eu+q−1ev⊗ev+ew⊗ew/parenright.alt1,
σ(eu⊗ev) = 1
1−q (qeu⊗ev+ev⊗ew+ew⊗eu), σ (ev⊗eu) = 1
1−q (qev⊗eu+ew⊗ev+eu⊗ew),
σ(ev⊗ew) = 1
1−q (qev⊗ew+ew⊗eu+eu⊗ev), σ (ew⊗ev) = 1
1−q (qew⊗ev+eu⊗ew+ev⊗eu),
σ(ew⊗eu) = 1
1−q (qew⊗eu+eu⊗ev+ev⊗ew), σ (eu⊗ew) = 1
1−q (qeu⊗ew+ev⊗eu+ew⊗ev).
These are extendable, ∧-compatible and Leibniz-compatible, so all the conditions of Theorem 4.8
apply.
Proof. We use the analysis of [4, Ex. 3.76] for which left and right translation invariant connec-
tions on S3 are torsion free and ﬂat to narrow down to a 1-parameter family (case (ii) of the
curvature bimodule maps applies) with e=c−1,d =c,b = 1−2c anda= (c−1)(1−2c)/slash.leftc in terms
of the parameterisation there. We then intersect this with those that obey the braid relations
(case (5) applies) which needs 1 + 3c2−3c= 0. This has two solutions,
a=c=d=qb =q−1e= 1
1−q, q =e±2πi
3 .
We then look in [4, Ex. 4.18] for which are extendable and ﬁnd that these both are. By Propo-
sition 6.2, the Leibniz-compatibility property automatically holds.
We also translate the parameterisation in [4, Ex. 4.18] into the explicit formulae stated. Then
we check ∧-compatibility. Thus, we would need from the 2nd part of Fig. 1(c),
σΩ2(euev⊗eu) = 1
1−q ∧2 (σ(eu⊗( ))⊗id)(qev⊗eu+ew⊗ev+eu⊗ew)
34 SHAHN MAJID AND FRANCISCO SIM ˜AO
= 1
(1−q)2(q2eu⊗eveu+qev⊗eweu+qeu⊗ewev+ev⊗euev+eu⊗euew+q−1ev⊗evew).
We similarly ﬁnd
σΩ2(evew⊗eu) = 1
(1−q)2(q2ev⊗eweu+qeu⊗eveu+qev⊗euev+eu⊗ewev+q2eu⊗euew+ev⊗evew),
σΩ2(eweu⊗eu) = 1
(1−q)2(eu⊗eveu+ev⊗eweu+q2eu⊗ewev+q2ev⊗euev+qeu⊗euew+qev⊗evew).
Adding these together, we get zero using 1 +q+q2 = 0. Moreover, cyclic rotation u→v→w→u
of these formulae generate 6 similar expressions suﬃcient to similarly conclude thatσΩ2(( )⊗ev)
and σΩ2(( )⊗ew) are well-deﬁned as regards the ﬁrst relation of Ω 2. The proof for the other
relation of Ω 2 is similar. □
The map σ here is not involutive, i.e. it is strictly braided with eigenvalues −1,−q2 (each 4
times) and −q. The jet bimodule is
J∞
A = spanC(S3)/uni27E81,eu,ev,ew,eu⊗eu,ev⊗ev,ew⊗ew,euv,evu,/uni22EF/uni27E9,
euv ∶=eu⊗ev+ev⊗ew+ew⊗eu, e vu ∶=ev⊗eu+ew⊗ev+eu⊗ew,
where the dots indicate higher order terms. The prolongation map works out as
j∞(a) =a+ /summation.disp
i=u,v,w
(∂ia)ei+ /summation.disp
i=u,v,w
Di(a)ei⊗ei+Duv(a)euv+Dvu(a)evu+/uni22EF
where
∂i =Ri−id, D i = 1
q−1(q2(Ru+Rv+Rw)+Ri+ 4q),
Duv =Ruv+ 1
q−1(Ru+Rv+Rw−3q), D vu =Rvu+ 1
q−1(Ru+Rv+Rw−3q)
for i=u,v,w and Rx(a)(y) =a(yx) for any function a∈C(S3) is the right translation operator.
HereRuv =Rvw =Rwu andRvu =Rwv =Ruw where products are in the groupS3. The ●k actions
can be similarly given in such terms.
In terms of the Sσ(Ω1) algebra, one can compute that in degree 2
ker(id+σ) = spanC(S3)/uni27E8ew⊗ev−eu⊗ew,ev⊗eu−eu⊗ew,ev⊗ew−eu⊗ev,ew⊗eu−eu⊗ev/uni27E9.
Hence, Sσ(Ω1) is generated over A by the algebra Sσ(C3) with at least the quadratic relations
ewev = euew = eveu,evew = euev = eweu. (These can be expected to be all the relations.)
We recognise this is the braided enveloping algebra of the quandle on {u,v,w } regarded as a
braided-Lie algebra [4]. Moreover, this is an example where Sk
σ(Ω1)≅Ωk
S (as it is classically).
This is because for k = 2 the dimension of Sσ(C3) is 5 and hence S2
σ(Ω1) is not only included in
but isomorphic Ω2
S via id+σ. Hence, one could also build the jet bimodule essentially on Sσ(Ω1)
at least for each ﬁnite k and using the ●k bimodule structure transferred to this.

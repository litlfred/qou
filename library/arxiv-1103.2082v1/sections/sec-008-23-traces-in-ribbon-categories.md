---
doc_id: arxiv-1103.2082v1
doc_title: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St)"
section_id: sec-008-23-traces-in-ribbon-categories
section_title: "Traces in Ribbon Categories"
section_number: 2.3
pages: 5-6
source_pdf: 1103.2082v1.pdf
source_sha256: 0ac5371486b38eac
doc_brief: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St) — Deligne has deﬁned a category which interpolates among the representations of the various symmetric groups."
---
trL(f) = (evV⊗ IdW )(IdV∗⊗f)(coev′
V⊗ IdW )∈ EndC(W ), (2.1)
and
trR(f) = (IdV⊗ ev′
W )(f⊗ IdW∗)(IdV⊗ coevW )∈ EndC(V ). (2.2)
Deﬁnition 2.2. IfI is an ideal inC, then a trace onI is a family of linear functions
t ={tV : EndC(V )→K}
where V runs over all objects of I and such that following two conditions hold:
(1) If U∈I and W∈ Ob(C) then for any f∈ EndC(U⊗W ) we have
tU⊗W (f) = tU (trR(f)). (2.3)
(2) If U,V ∈I then for any morphisms f :V→U and g :U→V inC we have
tV (gf ) = tU(fg ). (2.4)
Using the trace onI introduced above, we deﬁne a modiﬁed dimension function on objects
inI. Namely, we deﬁne the modiﬁed dimension function
dt : Ob(I)→K
by the formula
dt(V ) = tV (IdV ).
Example 2.3. IfC is a ribbon category, thenC itself is an ideal and the well knowncategorical
trace function
trC : EndC(V )→K
given by
trC(f) = ev′
V (f⊗ 1) coevV
deﬁnes a trace on C. The modiﬁed dimension function then coincides with the familiar
categorical dimension function.
The following theorem from [GKP10] gives a convenient way of creating ideals with traces.
Assume that J inC admits a linear map
tJ : EndC(J)→K
which satisﬁes
tJ (trL(h)) = tJ (trR(h)),
for all h∈ EndC(J⊗J). Such a linear map is called an ambidextrous trace on J.
For an object J, letIJ denote the ideal whose objects are all objects which are retracts
of J⊗X for some X inC.
Theorem 2.4. If J is an object of C which admits an ambidextrous trace, then there is a
unique trace onIJ determined by that ambidextrous trace.
5

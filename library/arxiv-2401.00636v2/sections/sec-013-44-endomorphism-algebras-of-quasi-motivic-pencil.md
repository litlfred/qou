---
doc_id: arxiv-2401.00636v2
doc_title: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS"
section_id: sec-013-44-endomorphism-algebras-of-quasi-motivic-pencil
section_title: "Endomorphism algebras of quasi-motivic pencils"
section_number: 4.4
pages: 12-12
source_pdf: 2401.00636v2.pdf
source_sha256: 35e372d04cedf234
toc_source: outline
---
module W, let ∇W be the ﬂat connection on X with ﬁber W associated to ∇. It is clear
that if ∇has regular singularities then so does ∇W, and if ∇(s) has periodic monodromy, is
periodic, or is quasi-motivic, then so is ∇W(s)
Let dW = dW(∇) := d(∇W). Let Y ⊂Gr(dW, W) be the Zariski closure of the image of
the rational map γ = γ(∇W) deﬁned in Subsection 3.2, an irreducible closed subvariety.
Theorem 4.7. The action of GL(V ) on Y has a (unique) dense orbit Y ◦.
Proof. By Rosenlicht’s theorem in invariant theory ([PV], 2.3), rational invariants separate
generic orbits. Thus it suﬃces to show that C(Y )GL(V ) = C. Let F be a GL(V )-invariant
rational function on Y . Then F ◦γ is a rational function of s ∈Cn. On the other hand, since
∇has regular singularities, we have γ(s) = W π1(X,x0), where π1(X, x0) acts on W through
the monodromy representation ρs. Thus by Theorem 3.9, F ◦γ is also rational in e2πis.
This implies the statement, since a function simultaneously rational in s and e2πis must be
constant.
□
Let U(∇, W) be the Zariski open set of s ∈Cn such that γ(s) is deﬁned and belongs to
Y ◦. Thus for any two elements s, s′ ∈U(∇, W), the corresponding subspaces γ(s) and γ(s′)
are conjugate under the action of GL(V ).
Corollary 4.8. Every codimension 1 component H of the complement U(∇, W)c is a hy-
perplane contained in Z.
Proof. Since the membership of s in U(∇, W) depends only on ρs, E(H) is contained in Z.
So by Theorem 2.6 it is contained in Zht and the statement follows.
□
Now consider the special case W = V ⊗V ∗.
In this case γ(s), when deﬁned, is the
reduced endomorphism algebra Endred(∇(s)). If s /∈J(∇), it coincides with the usual
endomorphism algebra End(∇(s)), otherwise it is a subalgebra in End(∇(s)) obtained as the
limit of the endomorphism algebra from the generic locus.
Corollary 4.9. For values of s outside ﬁnitely many hyperplanes contained in Z and a
Zariski closed subset of Cn of codimension ≥2, the reduced endomorphism algebra Endred(∇(s))
together with its action on V does not depend on s up to an isomorphism.
Proof. It suﬃces to apply Corollary 4.8 to W = V ⊗V ∗.
□
Let us regard Autred(∇(s)) = Endred(∇(s))× as a group scheme over U(∇, V ⊗V ∗). We
can then project the shift operators Aj(s) to rational sections Aj•(s) of the bundle over
U(∇, V ⊗V ∗) with ﬁber GL(V )/Autred(∇(s)). It is clear that Aj•(s) does not depend on
the choice of Aj. Let Zj• be the pole divisor of Aj•. We obtain the following generalization
of Theorem 4.6(ii).
Corollary 4.10. We have Zj• ⊂Z.
Proof. Using the same argument as in the proof of Theorem 4.6(ii), one establishes that
E(Zj•) ⊂Z. Thus by Theorem 2.6, E(Zj•) ⊂Zht, so the result follows.
□

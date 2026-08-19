---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-042-a1-rules-for-soliton-degeneracies
section_title: "A.1 Rules for soliton degeneracies"
section_number: null
pages: 74-76
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
We consider six two-way streetspn entering a joint as in Figure 46. It is convenient to sum-
marize the soliton spectrum by deﬁning generating functions for the soliton degeneracies
on these six streets:
νn =
∑
¯a
µ(a,pn)Xa, τ n =
∑
¯b
µ(b,pn+3)Xb, (A.1)
– 72 –
ij
ik
jk
ij
ik
jk
kj
kj
ji
ki
ki
ji
Figure 46. The British resolution of a joint with two-way streets. Incoming soliton degeneracies
are described by generating functions νn,n = 1,..., 6. Outgoing soliton degeneracies are described
by generating functions τn, n = 1,..., 6.
where in νn the sum runs over all ingoing charges ¯ a supported on pn (i.e. charges for
which|Z¯a| increases as we go into the joint), in τn the sum runs over all outgoing charges
¯b supported on pn+3, and n is always taken mod 6. Applying the constraint of homotopy
invariance to artfully chosen paths one shows
τ1 =ν1 +ν6τ2, τ 2 =ν2 +τ3ν1, τ 3 =ν3 +ν2τ4, (A.2)
τ4 =ν4 +τ5ν3, τ 5 =ν5 +ν4τ6, τ 6 =ν6 +τ1ν5.
(These equations have a symmetry under a cyclic shift of the index by 1 combined with
reversing order of all products, corresponding to the symmetry of Figure 46 under a rotation
byπ/3 combined with reversing the order of the labels on all lines.) Using (A.2) repeatedly
we obtain the outgoing degeneracy τ1 in terms of the incoming degeneracies νi,
τ1 =ν1 +ν6ν2 +ν6ν3ν1 +ν6ν2ν4ν1 +ν6ν2ν5ν3ν1 +ν6ν2ν4ν6ν3ν1+
+ν6ν2ν4ν1ν5ν3ν1 +ν6ν2ν4ν6ν2ν5ν3ν1 +ν6ν2ν4ν6ν3ν1ν5ν3ν1 +···
= 1
1−−−−−→ν6ν2ν4⊗←−−−−ν5ν3ν1
(ν1 +ν6ν2 +ν6ν3ν1 +ν6ν2ν4ν1 +ν6ν2ν5ν3ν1 +ν6ν2ν4ν6ν3ν1).
(A.3)
The arrows indicate that the the denominator is to be expanded as a geometric series and
then ordered so that factors ( ν6ν2ν4) are to be multiplied successively on the left and the
factors (ν5ν3ν1) are to be multiplied successively on the right.
Note that if we put ν3 = ν4 = ν5 = 0, so that we have only three incoming streets,
then we ﬁnd that τ3 =τ4 =τ5 = 0, and
τ2 =ν2, τ 1 =ν1 +ν6ν2, τ 6 =ν6. (A.4)
This reproduces the rules for one-way streets which we obtained in §5.2, as expected.
For the record, the analog of (A.2) with the American resolution is
τ1 =ν1 +τ6ν2, τ 2 =ν2 +ν3τ1, τ 3 =ν3 +τ2ν4, (A.5)
τ4 =ν4 +ν5τ3, τ 5 =ν5 +τ4ν6, τ 6 =ν6 +ν1τ5,
– 73 –
which leads to
τ1 = 1
1−−−−−→ν1ν5ν3⊗←−−−−ν4ν6ν2
(ν1 +ν6ν2 +ν1ν5ν2 +ν1ν4ν6ν2 +ν1ν5ν3ν6ν2 +ν1ν5ν2ν4ν6ν2).
(A.6)
Figure 47. Three two-way streets around a branch point.
For a branch point with two-way streets we also have new rules. As explained in §5.3
each of the three streets pi emerging from the branch point carries a charge ¯ ai with a
natural lift ai, and µ(ai,pi) = 1. What changes in the two-way case is that there may also
be other charges supported on these streets. Nevertheless, the outgoing degeneracies τn
are fully determined in terms of the incoming ones νn: the general statement is
τn =Xan +νn. (A.7)
(To make sense of this equation we have to say something about how we continue from
one street to another, since τn and νn are deﬁned on diﬀerent streets. Unlike the case of
the joint above, we cannot simply continue from both streets to the branch point, because
there is monodromy there; we have to specify which way we go around the branch point.
We follow the short path around, traversing an angle 2 π/3 rather than 4π/3.) If we take
all νn = 0 then we simply recover
τn =Xan (A.8)
which we found in§5.3.

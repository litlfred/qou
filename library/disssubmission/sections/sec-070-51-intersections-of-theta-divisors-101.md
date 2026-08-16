---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-070-51-intersections-of-theta-divisors-101
section_title: "Intersections of theta divisors 101"
section_number: 5.1
pages: 109-110
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
Proof. The last row follows from the Hodge decomposition for a ppav
of dimensiong = 4 and has only been included for reference. Similarly,
the last column is clear becauseH1(Y,Q) =H1(Y,Q)− = H1(X,Q) by the
weak Lefschetz theorem. It remains to compute the Hodge numbers of the
smooth surfacesY andY+ in cohomology degree two. Corollary 5.6 gives
the topological Euler characteristicχ(Y) = 72, which impliesh2(Y) = 86
becauseh0(Y) = h4(Y) = 1 and h1(Y) = h3(Y) = 8. In the same way, via
lemma 5.5 the Hirzebruch-Riemann-Roch theorem gives the holomorphic
Euler characteristic
χ(OY) = degY(c2
1(Y) +c2(Y))/12 = degY((−2θ)2 +3θ2)/12 = 14.
Plugging in the valuesh0,0(Y) =1 andh0,1(Y) =4 we geth0,2(Y) =17, and
thenh1,1(Y) = 52 because the Hodge numbers in degree two must sum up
to the second Betti numberh2(Y) =86.
To obtain from these numbers also the Hodge numbers of the quotient
surfaceY+ =Y/σ we use that the quotient morphismq :Y→Y+ is an´etale
double covering. In particular we have a commutative diagram
H2(Y+,Q)×H2(Y+,Q) ∪ //
q∗

H4(Y+,Q)
degY+ //
q∗

Q
2·

H2(Y,Q)×H2(Y,Q) ∪ // H4(Y,Q)
degY // Q
where the vertical arrow on the right hand side is multiplication with the
degree deg(q) = 2, and the Chern classes satisfyci(Y) = q∗(ci(Y+)) for
all i. This being said, the Gauss-Bonnet and Hirzebruch-Riemann-Roch
theorem show
χ(Y+) = χ(Y)/2 = 36 and χ(OY+) = χ(OY)/2 = 7.
Hence it follows thath2(Y+) = 36−1−1 = 34 andh0,2(Y+) = 7−1 = 6
by similar computations as above, and we are done. □
As an immediate corollary we obtain that the intersection form has the
following signatures on the various occuring subspaces ofH2(Y,Q), where
we denote bys+ ands− the dimension of maximal subspaces on which the
form is positive resp. negative deﬁnite.
COROLLARY 5.9. For g = 4 the intersection form has the following
signatures on the various subspaces of H2(Y,Q).
H2(Y,Q) H2(Y+,Q) H2(X,Q) V− V+
s+ 35 13 13 22 0
s− 51 21 15 30 6
102 Chapter 5 – A family of surfaces
Proof.The Hodge index theorem [103, th. 6.33] says that for a smooth
compact K¨ahler surfaceS with K¨ahler classω∈ H1,1(X)∩H2(X,R) the
intersection form is
• positive deﬁnite on the subspace(H2,0(S)⊕H0,2(S))∩H2(S,R)
and also on the lineR· ω,
• negative deﬁnite on the orthocomplement of the K¨ahler class ω
insideH1,1(S)∩H2(S,R).
In our case, takingS =Y and using the Hodge numbers in lemma 5.8 one
sees that onH2(Y,Q) = H2(Y,Q)+⊕V− and H2(Y,Q)+ = H2(X,Q)⊕V+
the intersection form has the given signatures. □
In particular, it follows that on the subspaceV+ the intersection form is
negative deﬁnite. In sections 5.3 and 5.4, working on the level of integral
cohomology we will determine the structure of the lattices whose signatures
have been listed above. But let us ﬁrst say a few words about the variations
of Hodge structures deﬁned by the above subspaces.

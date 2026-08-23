---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-069-51-intersections-of-theta-divisors-99
section_title: "Intersections of theta divisors 99"
section_number: 5.1
pages: 107-109
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
at hand, let us brieﬂy recall the deﬁnition and some basic features of Prym
varieties in general, referring to loc. cit. for more details.
For any covering˜C−→C of smooth projective curves we have a norm
homomorphism
N ˜C/C : J ˜C−→JC
between the corresponding Jacobian varieties, induced by the pushforward
morphism on divisors. This norm homomorphism is always surjective. For
an ´etale double covering its kernel has precisely two connected components,
and one deﬁnes the Prym variety
P = Prym( ˜C/C) = ( ker(N ˜C/C))0⊂ J ˜C
to be the connected component which contains the origin. By construction
this is an abelian subvariety ofJ ˜C. The special thing about ´etale double
covers of curves is that this Prym variety also comes along with a principal
polarization, indeed by loc. cit. the principal polarization onJ ˜C restricts
on the Prym varietyP to twice a principal polarization. Prym varieties are
useful in the study of ppav’s since they are more general than Jacobian
varieties but nevertheless still accessible in terms of algebraic curves. Note
that if the curveC has genusg+1 (say), then˜C has genus 2g+1 due to the
Riemann-Hurwitz formula [55, cor. IV .2.4], and then the Prym variety has
dimension
dim(P) = ( 2g+1)−(g+1) = g.
Hence if we denote byMg+1 the coarse moduli space of smooth projective
curves of genusg +1 and deﬁne Rg+1 to be the coarse moduli space of
´etale double covers of such curves, then we have a diagram
Rg+1
ϕ
{{vvvvvvvvv π
""DDDDDDDD
Mg+1 Ag
whereϕ is the forgetful morphism and whereπ is the morphism that assigns
to a double covering its Prym variety. Here the morphismϕ is generically
ﬁnite of degree 2g+1−1 because the´etale double covers of a given curve
correspond bijectively to the non-trivial two-torsion points on its Jacobian
variety. The Prym morphismπ plays an important role for the moduli of
abelian varieties and has been studied a lot in the literature; as the most
important results, we only mention that forg≥ 6 it is generically ﬁnite of
degree one [39] but never injective [34]. In dimensions g < 6 the Prym
morphismπ is no longer generically ﬁnite but its ﬁbres have a surprisingly
rich geometric structure which is discussed in loc. cit.
100 Chapter 5 – A family of surfaces
This brings us back to the´etale double coveringY−→Y+ deﬁned by
the intersection of two general translates of the theta divisor on a complex
ppavX of dimensiong = 3. Here the curveY has genus 7 by corollary 5.6,
hence the Prym varietyP =Prym(Y/Y+) is a complex ppav of dimension 3
as well. The following result has been obtained in [84] and [66].
THEOREM 5.7. For a general complex ppav X of dimension g= 3 the
following properties are satisﬁed.
(a) For general x∈ X(C) the Prym variety P of the cover Yx−→Y+x
is isomorphic to the ppav X.
(b) Every ´etale double covering of smooth curves with Prym variety
isomorphic to X arises as above for some point x∈ X(C), and the
coverings for two points x1,x2 are isomorphic iff x1 =±x2.
In other words, the above construction identiﬁes the ﬁbre of the Prym
morphismπ : R4−→A3 over a general ppavX∈ A4(C) with an open
dense subset of the Kummer variety
KX = X/⟨±idX⟩.
Fixing a general pointx∈ X(C), we now again use the notationY = Yx
etc. The deﬁnition of the Prym varietyP as a component of the kernel of
the norm epimorphismN : JY↠JY+ shows that the Jacobian varietyJY is
isogenous toP×JY+, which together with the identiﬁcation in part(a) of
the above theorem implies
H1(Y,Q) = H1(X,Q)⊕H1(Y+,Q).
Hence in this case we haveV− = 0, andV+ = H1(Y+,Q) is a pure Hodge
structure of weight one and rank eight.
The case g= 4. Here Y−→Y+ is an ´etale double covering of smooth
projective surfaces that will occupy us for the rest of this chapter. We claim
thatV− has Hodge numbersh2,0 = h0,2 = 11 andh1,1 = 30 whereasV+ is
of pure Hodge type(1,1) and rank six. Indeed, bearing in mind the natural
identiﬁcations
H2(Y+,Q) = H2(Y,Q)+ = H2(X,Q)⊕V+
this is a direct consequence of the numerical data in the following table.
LEMMA 5.8. For a complex ppav X of dimension g= 4 we have the
following Hodge numbers.
h2,0 = h0,2 h1,1 h1,0 = h0,1
Y 17 52 4
Y+ 6 22 0
X 6 16 4

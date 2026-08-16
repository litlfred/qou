---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-065-46-singularities-of-type-ak-89
section_title: "Singularities of type Ak 89"
section_number: 4.6
pages: 97-99
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
say that a pointe in Y is a singularity of typeAk if in a neighborhood ofe
the hypersurfaceY is deﬁned by an equation of the form
(⋆) zk+1
0 + z2
1 + z2
2 +··· + z2
n = 0
in suitable local analytic coordinates(z0, . . . ,zn) on Cn+1 centered ate. So
a singularity of typeAk is just an ordinary double point fork = 1 whereas
for k > 1 it is a double point of corank one.
Working as usual with coefﬁcients inΛ = C or Λ = Ql in the algebraic
case, we want to describe the perverse intersection cohomology sheaf near
a singularity of typeAk.
LEMMA 4.16. Let Y⊂ An+1(C) be a complex analytic hypersurface
whose only singular point e is a singularity of type Ak.
(a) If k or n is even, thenδY = ΛY[n].
(b) Otherwise we have an exact sequence of perverse sheaves
0−→δe(−n−1
2 )−→ΛY[n]−→δY−→0.
Proof. We can assumeY is deﬁned by an equation (⋆). To compute
the blowupp : ˜Y−→Y in the singular pointe we choosez = (z0, . . . ,zn)
as coordinates on the afﬁne spaceAn+1 = An+1(C). The corresponding
coordinates onPn = Pn(C) will be denotedu = [u0 :··· : un]. Then the
blowup
˜Y⊂ ˜An+1 ={(z,u)∈ An+1×Pn| z∈ u}
can be computed explicitly in the afﬁne chartsUi ={(z,u)∈ ˜An+1| ui⁄= 0}
with the standard coordinates(u0, . . . ,ui−1,zi,ui+1, . . . ,un) by puttingui =1
andzj = ziuj for j⁄= i. Thus
˜Y∩U0 ={zk−1
0 +u2
1 +··· +u2
n = 0}
whereas fori > 0 one obtains that
˜Y∩Ui ={uk+1
0 zk−1
i +u2
1 +··· +u2
i−1 +1+u2
i+1 +··· +u2
n = 0}.
In particular, fork = 1 it follows that the blowup˜Y is smooth. Fork > 1 it
has an isolated singularity ˜e∈ ˜Y∩U0 of typeAk−2, and we get by induction
on k an exact sequence
0→ κnk→ Λ˜Y[n]→ δ ˜Y→0 where κnk =
{
0 if 2 | nk,
δ˜e(−n−1
2 ) if 2 ∤ nk.
90 Chapter 4 – The Tannaka group of the theta divisor
Furthermore, by purity we can write
Rp∗(δ ˜Y) = δY⊕ε
whereε is a skyscraper complex supported one and self-dual with respect
to Verdier duality up to a Tate twist. We now distinguish two cases.
If k = 1, the above calculations show that the exceptional divisor of the
blowup˜Y is the smooth quadricQn ={u∈ Pn| u2
0 +u2
1 +··· +u2n =0}. The
cohomology of such a quadric has been computed in [32, exp. XII, th. 3.3],
Hi(Qn,Λ) =



Λ(− i
2) if i∈{0,2, . . . ,2n−2}\{ n−1},
Λ2(− i
2) if i = n−1 andn is odd,
0 otherwise .
Since by base changeH i−n(δY⊕ ε)0 = H i−n(Rp∗(δ ˜Y))0 = Hi(Qn,Λ),
one then easily concludes the proof of the lemma by an application of the
hard Lefschetz theorem to the skyscraper summandε.
If k > 1, the above calculations show that the exceptional divisor of the
blowup˜Y is the singular quadricQ⋆n ={u∈ Pn| u2
1 +u2
2 +··· +u2n = 0}. In
this case we will see below that
Hi(Q⋆
n,Λ) =



Λ(− i
2) if i∈{0,2, . . . ,2n−2}\{ n},
Λ2(− i
2) if i = n andn is even,
0 otherwise .
Now by base changeH i−n(Rp∗(Λ˜Y[n]))0 =Hi(Q⋆n,Λ), and combining this
with the distinguished triangle
Rp∗(κnk)−→Rp∗(Λ˜Y[n])−→Rp∗(δ ˜Y)| {z }
= δY⊕ε
−→···
one concludes the proof of the lemma as before by checking that the only
two possibly non-zero cohomology sheaves ofδY areH−1(δY) =Rp∗(κnk)
and H−n(δY) = ΛY in this case.
It remains to check that the cohomology of the singular quadricQ⋆n has
the form given above. Consider the singular pointp = [1 : 0 :··· : 0] of this
quadric, with smooth complementE = Q⋆n\{p}. By the excision sequence
for compactly supported cohomology we haveHic(E,Λ) = Hi(Q⋆n,Λ) for
all i > 1, and in low degrees we have an exact sequence
0→H0
c (E,Λ)→H0(Q⋆
n,Λ)→ Λ→H1
c (E,Λ)→H1(Q⋆
n,Λ)→0.

---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-029-46-singularities-of-type-ak
section_title: "Singularities of type Ak"
section_number: 4.6
pages: 96-101
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
For completeness we include in this section some remarks about double
points that have been used in the proof of part (2) of proposition 4.12. In that
proof we have only dealt with ordinary double points, but since this is hardly
more work, in what follows we place ourselves in a slightly more general
setting. Let Y ⊂Cn+1 be a complex analytic hypersurface. For k ≥1, we
4.6. Singularities of type Ak
89
say that a point e in Y is a singularity of type Ak if in a neighborhood of e
the hypersurface Y is deﬁned by an equation of the form
(⋆)
zk+1
0
+ z2
1 + z2
2 + ··· + z2
n = 0
in suitable local analytic coordinates (z0,...,zn) on Cn+1 centered at e. So
a singularity of type Ak is just an ordinary double point for k = 1 whereas
for k > 1 it is a double point of corank one.
Working as usual with coefﬁcients in Λ = C or Λ = Ql in the algebraic
case, we want to describe the perverse intersection cohomology sheaf near
a singularity of type Ak.
LEMMA 4.16. Let Y ⊂An+1(C) be a complex analytic hypersurface
whose only singular point e is a singularity of type Ak.
(a) If k or n is even, then δY = ΛY[n].
(b) Otherwise we have an exact sequence of perverse sheaves
0 −→δe(−n−1
2 ) −→ΛY[n] −→δY −→0.
Proof. We can assume Y is deﬁned by an equation (⋆). To compute
the blowup p : ˜Y −→Y in the singular point e we choose z = (z0,...,zn)
as coordinates on the afﬁne space An+1 = An+1(C). The corresponding
coordinates on Pn = Pn(C) will be denoted u = [u0 : ··· : un]. Then the
blowup
˜Y ⊂˜An+1 =

(z,u) ∈An+1 ×Pn | z ∈u
	
can be computed explicitly in the afﬁne charts Ui = {(z,u) ∈˜An+1 | ui̸ = 0}
with the standard coordinates (u0,...,ui−1,zi,ui+1,...,un) by putting ui = 1
and zj = zi uj for j̸ = i. Thus
˜Y ∩U0 =

zk−1
0
+u2
1 +···+u2
n = 0
	
whereas for i > 0 one obtains that
˜Y ∩Ui =

uk+1
0
zk−1
i
+u2
1 +···+u2
i−1 +1+u2
i+1 +···+u2
n = 0
	
.
In particular, for k = 1 it follows that the blowup ˜Y is smooth. For k > 1 it
has an isolated singularity ˜e ∈˜Y ∩U0 of type Ak−2, and we get by induction
on k an exact sequence
0 →κnk →Λ˜Y[n] →δ ˜Y →0
where
κnk =
(
0
if 2 | nk,
δ˜e(−n−1
2 )
if 2 ∤nk.
90
Chapter 4 – The Tannaka group of the theta divisor
Furthermore, by purity we can write
Rp∗(δ ˜Y) = δY ⊕ε
where ε is a skyscraper complex supported on e and self-dual with respect
to Verdier duality up to a Tate twist. We now distinguish two cases.
If k = 1, the above calculations show that the exceptional divisor of the
blowup ˜Y is the smooth quadric Qn = {u ∈Pn | u2
0 +u2
1 +···+u2
n = 0}. The
cohomology of such a quadric has been computed in [32, exp. XII, th. 3.3],
Hi(Qn,Λ) =





Λ(−i
2)
if i ∈{0,2,...,2n−2}\{n−1},
Λ2(−i
2)
if i = n−1 and n is odd,
0
otherwise.
Since by base change H i−n(δY ⊕ε)0 = H i−n(Rp∗(δ ˜Y))0 = Hi(Qn,Λ),
one then easily concludes the proof of the lemma by an application of the
hard Lefschetz theorem to the skyscraper summand ε.
If k > 1, the above calculations show that the exceptional divisor of the
blowup ˜Y is the singular quadric Q⋆
n = {u ∈Pn | u2
1 +u2
2 +···+u2
n = 0}. In
this case we will see below that
Hi(Q⋆
n,Λ) =





Λ(−i
2)
if i ∈{0,2,...,2n−2}\{n},
Λ2(−i
2)
if i = n and n is even,
0
otherwise.
Now by base change H i−n(Rp∗(Λ˜Y[n]))0 = Hi(Q⋆
n,Λ), and combining this
with the distinguished triangle
Rp∗(κnk) −→Rp∗(Λ˜Y[n]) −→Rp∗(δ ˜Y)
|
{z
}
= δY ⊕ε
−→···
one concludes the proof of the lemma as before by checking that the only
two possibly non-zero cohomology sheaves of δY are H −1(δY) = Rp∗(κnk)
and H −n(δY) = ΛY in this case.
It remains to check that the cohomology of the singular quadric Q⋆
n has
the form given above. Consider the singular point p = [1 : 0 : ··· : 0] of this
quadric, with smooth complement E = Q⋆
n \{p}. By the excision sequence
for compactly supported cohomology we have Hi
c(E,Λ) = Hi(Q⋆
n,Λ) for
all i > 1, and in low degrees we have an exact sequence
0 →H0
c (E,Λ) →H0(Q⋆
n,Λ) →Λ →H1
c (E,Λ) →H1(Q⋆
n,Λ) →0.
4.6. Singularities of type Ak
91
So it sufﬁces to show
Hi
c(E,Λ) =





Λ(−i
2)
if i ∈{2,4,...,2n−2}\{n},
Λ2(−i
2)
if i = n and n is even,
0
otherwise.
For this we use that the projection [u0 : u1 : ··· : un] 7→[u1 : ··· : un] with
center p deﬁnes a rank one vector bundle
π : E −→Qn−1 ⊂Pn−1
over the smooth quadric Qn−1 = {[u1 : ··· : un] ∈Pn−1 | u2
1 +···+u2
n = 0}
of dimension n−2. Using Poincar´e duality and the homotopy invariance of
cohomology, we thus obtain
Hi
c(E,Λ) ∼= (H2n−2−i(E,Λ)(n−1))∨∼= (H2n−2−i(Qn−1,Λ)(n−1))∨
and the result follows by plugging in on the right hand side the cohomology
of the smooth quadric Qn−1.
□
CHAPTER 5

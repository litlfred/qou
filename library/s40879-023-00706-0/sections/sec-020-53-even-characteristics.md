---
doc_id: s40879-023-00706-0
doc_title: "Bring’s curve: old and new"
section_id: sec-020-53-even-characteristics
section_title: "Even characteristics"
section_number: 5.3
pages: 40-43
source_pdf: s40879-023-00706-0.pdf
source_sha256: 4c5af312d2e5d6a7
toc_source: outline
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
---
In the previous subsection, we were able to fully characterise the odd theta character-
istics on Bring’s curve without too much difﬁculty through the use of existing work
giving the stalls of the canonical embedding. The story for even characteristics is dif-
ferent, as the line bundle corresponding to a generic even theta characteristic has no
sections, which is an obstacle to their study [62]. In [19] the authors were able to use
the Scorza correspondence to calculate the orbit decomposition of even spin structures
on Klein’s curve, but at the time of writing the theory of the Scorza map has not been
developed far enough to cover Bring’s curve. The Scorza quartic necessary to extend
Bring’s curve: old and new
Page 41 of 46
3
Dolgachev and Kanev’s work beyond g = 3, wherein it becomes a codimension-1
hypersurface in Pg−1, has been proven to exist for a generic even spin curve (that is
a pair consisting of a curve and an even theta characteristic on it); it has only been
explicitly found for trigonal curves in g = 4 [62]. In [11], motivated by its realisation
via an elliptic modular surface, Burns identiﬁed a theta characteristic on Bring’s curve
invariant under the A5 subgroup of the automorphism group, though he described this
characteristic only in terms of two line bundles on the curve, not directly in terms of
points on the curve. We shall now fully classify the orbits of the even characteristics
and give an explicit description of Burns’ divisor in the process.
We have two distinct methods of probing the orbit decomposition of the theta
characteristics on Bring’s curve.
• Use the method of [40], wherein theta characteristics are identiﬁed with vectors
in F2g
2 , and the action of automorphisms given by the homology representation of
the automorphism group of the curve as found using the methods of [10].
• Identify theta characteristics with the 22g translates by half-lattice vectors of a
half-canonical vector in the Jacobian of the curve, done using the implementation
of the Abel–Jacobi map developed by Disney-Hogg [17], and the action of auto-
morphisms given by the cohomology representation of the automorphism group
of the curve as found using the methods of [10].
The two methods have different strengths, namely that the ﬁrst uses exact computa-
tions rather than approximations with multi-precision arithmetic, but the second can
concretely relate theta characteristics from their representation to an actual divisor
(class). Both methods not only verify Corollary 5.7 but also gives the following result.
Theorem 5.9 The orbit decomposition of even theta characteristics on Bring’s curve
is
136 = 1 + 5 + 5 + 5 + 10 + 10 + 10 + 30 + 30 + 30.
(21)
Corollary 5.10 Bring’s curve has a unique theta characteristic invariant under the
action of the automorphism group, which is also the theta characteristic invariant
under the A5 subgroup found in [11].
The existence of the unique invariant theta characteristic was known in [8], but it
had not been identiﬁed. This we rectify with the following result.
Theorem 5.11 Thethetacharacteristic(deﬁnedinExample5.3)istheuniqueinvari-
ant theta characteristic in on Bring’s curve.
Proof We ﬁrst consider the action of S on a, b, c, d. We have
a ..= [0 : 0 : 1] ≃[2t3 : t : 1]
S−→[2t3 : ζt : ζ −1] = [2ζt3 : ζ 2t : 1]
= [2(ζ 2t)3 : ζ 2t : 1] = [2ϵ3 : ϵ : 1],
b ..= [0 : 1 : 0] ≃[2t2 : 1/t : 1]
S−→[2t2 : ζ/t : ζ −1] = [2ζt2 : ζ 2/t : 1]
3
Page 42 of 46
H.W. Braden, L. Disney-Hogg
= [2(t/ζ 2)2 : ζ 2/t : 1],
c ..= [1 : 0 : 0]2 ≃[1 : t : t4]
S−→[1 : ζt : ζ −1t4] = [1 : ζt : (ζt)4],
d ..= [1 : 0 : 0]1 ≃[1 : t4 : t]
S−→[1 : ζt4 : ζ −1t] = [1 : (ζ −1t)4 : ζ −1t].
Thus a, b, c and d are invariant under the symmetry S and consequently  = 3a+b−c
is also invariant.
Similarly, as mentioned in Proposition 2.13, the action of U on a, b, c, d can be
calculated as
a 
→c 
→b 
→d 
→a,
and so
 = 3a + b −c 
→3c + d −b = 3a + b −c −(3a + 2b −4c −d)
=  −(x) ∼.
We have thus shown that  is invariant under ⟨S,U⟩. To complete the proof that  is
the invariant theta characteristic, one could attempt to show that  is invariant under
the action of R by direct computation, but this proves to be difﬁcult. It is instead better
to check in Sage that the unique spin structure invariant under the whole automorphism
group is actually also the unique spin structure invariant under the subgroup generated
by S and U. In fact, by [40, Theorem 1.2] and our work in Sect.4, we know there is a
unique theta characteristic invariant under ⟨S⟩,29 and this completes the proof.
This proof strategy is similar to the identiﬁcation of the unique invariant theta
characteristic on Klein’s curve in [40].30
We now want to make the connection to [11]. Recall (3) and (4). This gives us
two degree-3 maps fi : B →P1, namely fi = πi ◦ϕ−1|B, i = 1, 2, where ϕ was
the isomorphism P1× P1 →Q, and πi the projection to the two factors of P1 ×P1.
What are the corresponding divisors? Working in the La coordinates, we can use
Sage to ﬁnd that f −1
1
([1 : 0]) = 2[0 : 0 : 0 : 1] + [1 : 0 : 0 : 0] = 2b + c ..= L′, while
f −1
2
([1 : 0]) = 2[0 : 1 : 0 : 0] + [0 : 0 : 0 : 1] = 2d + b ..= L.
Proposition 5.12 The divisors L, L′ satisfy the properties described in [11], namely
 ∼3(L′ −L) + L,
KB ∼L + L′,
0 ∼5(L′ −L).
Proof This is straightforward veriﬁcation from the deﬁnitions.
29 Under the action of S, the orbit decompositions are 120 = 24×5 and 136 = 1 + 27×5.
30 The ﬁnal part of the proof in that paper, showing invariance under the order-2 generator of PSL2(F7),
is in our opinion incomplete; Kallel (private correspondence) believes our reasoning correct. The theorem
remains correct nevertheless, as one can check using their methodology that invariance under the order-7
generator is enough to specify the unique invariant spin structure, as the decompositions are 28 = 4×7
and 36 = 1 + 5×7. It is a curious coincidence that in both cases it was a generator of order 2 for which the
direct calculation was difﬁcult.
Bring’s curve: old and new
Page 43 of 46
3
Note we can connect this back to the degree-3 map given by Klein. We know from
[66] that we expect this map to be branched at face-centres of the {5, 5 | 3} tessellation,
and these come from face-centres of the {5, 4}6 tessellation, and indeed recall we saw
that a, b, c, d were face-centres.
An additional characterisation of the invariant theta characteristic is given by the
following result.
Proposition 5.13 In the homology basis of [54], the RCV satisﬁes
Ka = 1
10 (3, 2, −2, −3) + Im(τ0)(1, −2, −2, 1)i = Aa().
As such, in the R&R homology basis, the unique invariant theta characteristic is the
divisor (class) of the Szeg˝o kernel, i.e.  = S.
Proof The ﬁrst equality is shown analytically in [8]. The second is shown numerically
in the corresponding notebooks, using the Abel–Jacobi map developed by Disney-
Hogg [17]. To verify the RCV, we implemented the methodology of [16] using the
theta function in Sage developed by Bruin and Ganjian [9]. While these calculations
are numerical in nature, the calculations can be done with arbitrary binary precision.
We were satisﬁed by calculating with 400 binary digits of precision, giving an absolute
error of less than 10−118 for the ﬁrst equality, and of less than 10−23 for the second
equality.

---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-066-4-going
section_title: "(going"
section_number: 4
pages: 59-60
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI) of"
---
froma + 2iπ −iη′ to −iη, see Figure 8) will have order exactly 1√
N as in the classical case of
Section 4.5.1 (see Step 5). There could be cancellations bet ween these two integrals (the ones
over the other subpaths in Figure 8 will have asymptotics of o rdero→∞( 1√
N )), and therefore
we have to compute more precisely the order of the integral on the RHS of (140). We do this
by using Proposition 5.3.
Let us deform the arc C +
a slightly downwards near its endpoint is−
N , so that it reaches the axis
iR in a point is′
N , where s′
N := α′
N < s−
N , and then goes vertically upwards to is−
N . Denote
byC +−
a the subarc from −υ′′ to is′
N , and write
(143)
∫
C+
a
gN (z)
N (l′
0+iπ)/2iπe
N
2π ℑ(f+(z))dz =
∫
C+−
a
gN (z)
N (l′
0+iπ)/2iπe
N
2π ℑ(f+(z))dz
+
∫
[is′
N,is−
N ]
gN (z)
N (l′
0+iπ)/2iπe
N
2π ℑ(f+(z))dz.
Instead of the integral over [ is′
N,is −
N ] on the RHS, let us consider for a while the same
integral but with the contour [ iη1,iη 2], with π
3 >η 2 >η 1 > 0 ﬁxed. We know that for z =it,
we have ℑ(f+(z)) := ℑ(L+(z, −2iπ, 2iπ)) = ℑ(Li2(eit) −t2) = Cl 2(t), and the function
Cl2(t) is strictly increasing and Cl ′
2(t) = −Log|2 sin(t/2)| ⁄= 0 for t ∈]0, π
3 [. In particular
ℑ(f+(z)) < ℑ(f+(iη2)) for every z ∈ [iη1,iη 2]. All the other assumptions of Proposition
5.3(ii) are clearly satisﬁed (the uniform convergence of ( gN ) to ρ on [iη1,iη 2] follows from
Lemma 3.5 and the properties of RN discussed in Lemma 5.1), so this result implies (the sign
in front of the RHS is because [ iη1,iη 2] ends at the maximum iη2 of ℑ(f+(iη2))):
(144)
∫
[iη1,iη2]
gN (z)
N (l′
0+iπ)/2iπe
N
2π ℑ(f+(z))dz
∼N →+∞ −e
N
2iπ (Li2(eiη2 )−η2
2 )
N (l′
0+iπ)/2iπ
ρ(iη2)
−iLog|2 sin(η2/2)| · 1
N.
Now we come back to η2 := s−
N = α− π
N , η1 := s′
N = α′
N < s−
N . By Proposition 5.3 (iii) the
equivalent (144) is uniform in iη2 as long as it stays a maximum of ℑ(f+) along the contour,
it varies in a compact set not containing a critical point of f+, and (gN ) converges uniformly
to ρ on this compact set. As noted above, the ﬁrst two conditions a re satisﬁed here. As for
60 ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2
the convergence of (gN ),iη2 =is−
N leaves any compact subset of ]0 ,i π
3 [ as N → +∞, but the
bounds (65) and (128) (with δ :=απ
N ) on any strip ( α + 1)π
N < I(z)< 2π − (α + 1)π
N ,α> 0,
imply that gN (α− π
N ) = ρ(α− π
N )vN , vN := exp
(1
N Ψu0,N (α− π
N )
)
(1 + 1
NRN (α− π
N )), where
(vN ) is a bounded sequence, bounded from below by a constant > 0. Then, an immediate
adaptation of the proof of Proposition 5.3 (ii) implies that (144) remains valid with η2 :=s−
N
and η1 :=s′
N , by multiplying ρ(iη2) = ρ(is−
N ) with vN .
The result is as follows. We have Cl ′
2(s−

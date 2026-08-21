---
doc_id: on-the-garoufalidis-kashaev-state-integral-invariant
doc_title: "On the Garoufalidis-Kashaev state-integral invariant"
section_id: sec-031-symmetries-of-the-angled-quantum-dilogarithm
section_title: "Symmetries of the Angled Quantum Dilogarithm"
section_number: null
pages: 34-36
source_pdf: On the Garoufalidis-Kashaev State-Integral Invariant.pdf
source_sha256: eda230da2a596783
doc_brief: "On the Garoufalidis-Kashaev state-integral invariant — 61 sections: ACKNOWLEDGMENTS; ABSTRACT; LIST OF TABLES"
---
Throughout this section we adopt the shorthand
(−α)(z) := α−1(z) =α(z)−1,
i.e. the inverse character. Note in particular (−α)(z)̸=−α(z).
Theorem 4 (Symmetry relations). Letb := (1,−1)−a−c. Then
Ψa,c(α−1, 1/x)α(x) = ¯Ψa,b(α,x), (3.4a)
Z
bB×B
Ψa,c(β,y )α(x/y)β(y/x)d(β,y ) = ¯Ψb,c(α,x). (3.4b)
Proof of (3.4a). Insert (α−1, 1/x) into the definition of Ψ a,c:
Ψa,c(α−1, 1/x) =α((1− ¨a/x)¨c) ∥¨a/x∥˙c
∥1− ¨a/x∥1−˙a,
because α−1(z) =α(z)−1. Multiply by α(x) and use multiplicativity:
Ψa,c(α−1, 1/x)α(x) =α((x− ¨a)¨c) ∥¨a/x∥˙c
∥1− ¨a/x∥1−˙a.
Since b = (1,−1)−a−c, one checks that
25
1−x/¨b
¨b
= (x− ¨a)¨c and ∥x/¨b∥˙c
∥1−x/¨b∥1−˙b = ∥¨a/x∥˙c
∥1− ¨a/x∥1−˙a.
Hence
α

1−x/¨b
¨b
 ∥x/¨b∥˙c
∥1−x/¨b∥1−˙b = ¯Ψa,b(α,x)
and (3.4a) follows.
Proof of (3.4b). Write the integral with the explicit kernel and the self–dual Haar
measure d(β,y ) =dβdy:
Z
bB×B
Ψa,c(β,y )α(x
y )β(y
x)dβdy.
Insert the formula for Ψa,c and first integrate in β:
Z
bB
β( y
x(1−¨ay)¨c)dβ =δB( y
x(1−¨ay)¨c− 1),
so the y–integral localises at the unique point
y0 = x¨c
1 + ¨ax¨c.
Substituting y =y0 gives the remaining scalar factor
α( x
y0
) ∥¨ay0∥˙c
∥1− ¨ay0∥1−˙a.
A direct computation, usingb = (1,−1)−a−c so that ˙b = 1− ˙a− ˙c and ¨b =−(¨a¨c)−1,
yields
α( x
y0
) =α(1−x/¨b
¨c ), ∥¨ay0∥˙c
∥1− ¨ay0∥1−˙a = ∥x/¨b∥˙c
∥1−x/¨b∥1−˙b.
26
The product of these two expressions is exactly ¯Ψb,c(α,x). Hence the whole integral
equals ¯Ψb,c(α,x), completing the proof.
Summary
• Symmetry (1) reflects functional and inversion symmetry underx7→ 1/x and
conjugation, with angle reparametrization b = (1,−1)−a−c.
• Symmetry (2) expresses a convolution identity reflecting duality under char-
acter–group Fourier transform, again with a parameter shift.

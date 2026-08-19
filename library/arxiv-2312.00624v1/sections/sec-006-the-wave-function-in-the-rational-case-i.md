---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-006-the-wave-function-in-the-rational-case-i
section_title: "The wave function in the rational case, I"
section_number: null
pages: 14-17
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
We will now apply the results obtained in Section 3.2 to derive explicitly the exact wave function
χ(u; ℏ) in Eq. (3.13) as a power series in X,X−1 for rational values of ℏ. Let us start from the
holomorphic components ϕ(α),WKB(X;q) and fix ℏ as in Eq. (3.15), that is,
q = eiℏ = e2πiP
Q, P,Q ∈ Z>0 coprime. (3.30)
As before, we drop the label α for simplicity and we intend the following discussion to hold for each
choice of the classical branch independently. The singular terms come from the values n = sQ for
s∈ Z>0, while choosing n =sQ +k with 1≤k≤Q− 1 produces only regular terms. Specifically,
the terms involving singularities are obtained by substituting Eq. (3.22a) into Eq. (3.2) and contain
the non-singular contributions
X
s≥1

−1
2 + 1
sQq ∂
∂q
 ˆa±sQ(q)
sQqσ±sQ
X±sQ. (3.31)
The regular terms associated with n̸=sQ are instead
Q−1X
k=1
1
qk− 1
X
s≥0
ˆa±(sQ+k)(q)
(sQ +k)qσ±(sQ+k)
X±(sQ+k), (3.32)
where we have used that qsQ+k = qk. Thus, the sum of the quantities in Eqs. (3.31), (3.32) is the
finite part of ϕWKB(X;q) evaluated at the rational point in Eq. (3.15). It is convenient to introduce
the functions
φ(+)
Q (X) =
X
s≥1
ˆasQ(q)
sQqσsQ
XsQ, (3.33a)
φ(−)
Q (X) =
X
s≥1
ˆa−sQ(q)
(−sQ)qsQ+σ−sQ
X−sQ, (3.33b)
φ(+)
k (X) =
X
s≥0
ˆasQ+k(q)
(sQ +k)qσsQ+k
XsQ+k, k = 1,...,Q − 1, (3.33c)
φ(−)
k (X) =
X
s≥0
ˆa−(sQ+k)(q)
−(sQ +k)qsQ+k+σ−(sQ+k)
X−(sQ+k), k = 1,...,Q − 1, (3.33d)
– 13 –
where we hide the dependence on q to simplify the notation. Moreover, we define
φQ(X) =φ(+)
Q (X) +φ(−)
Q (X), (3.34a)
φk(X) =φ(+)
k (X)−qkφ(−)
k (X), k = 1,...,Q − 1. (3.34b)
Putting Eqs. (3.31), (3.32) together and suitably identifying the functions just introduced in Eq. (3.34),
we can write the holomorphic block as
ϕWKB(X;q) =−1
2φQ(X) +q ∂
∂q
Z X
0
φQ(X′)dX′
X′ +
Q−1X
k=1
φk(X)
qk− 1 . (3.35)
Let us now consider the antiholomorphic component ϕWKB(XD;qD) and fix ℏ as above. The
derivation in this case is very similar to the previous one, but the novelty is the appearance of log X
terms, which originate from the ϵ-expansion of the dual variable
XD =X
2π
ℏ =X
Q
P . (3.36)
Let us add a small positive term ϵ to the rational value of ℏ as in Eq. (3.21). Then, we consider the
limit ϵ→ 0 and find that
Xϵ,D =X
2π
ℏϵ =X
Q
P
1
1+ ϵ
2π
Q
P =X
Q
P

1− Q2
2πP 2ϵ logX +O(ϵ2)

. (3.37)
As described before, the singular terms come from the values n = sP for s∈ Z>0, while choosing
n = sP +k with 1 ≤ k≤ P− 1 produces only regular terms. Specifically, the terms involving
singularities are obtained by substituting Eqs. (3.22b), (3.37) into the Eq. (3.2) and contain the
non-singular contributions
X
s≥1
 i
2πsQ− 1
2 + 1
sPqD
∂
∂qD
∓ i
2π logX
 ˆa±sP (qD)
sPqσ±sP
D
X±sQ. (3.38)
The regular terms associated with n̸=sP are instead
P−1X
k=1
1
qk
D− 1
X
s≥0
ˆa±(sP +k)(qD)
(sP +k)q
σ±(sP +k)
D
X±(sP +k)Q
P , (3.39)
where we have used that qD = e2πQ
P and thus qsP +k
D =qk
D. Therefore, the sum of the quantities in
Eqs. (3.38), (3.39) is the finite part of the function ϕWKB(XD;qD) evaluated at the rational point in
Eq. (3.15). As for the holomorphic block, we introduce the functions
eφ(+)
P (XD) =
X
s≥1
ˆasP (qD)
sPqσsP
D
XsP
D , (3.40a)
eφ(−)
P (XD) =
X
s≥1
ˆa−sP (qD)
−(sP )qsP +σ−sP
D
X−sP
D , (3.40b)
eφ(+)
k (XD) =
X
s≥0
ˆasP +k(qD)
(sP +k)qσsP +k
D
XsP +k
D , k = 1,...,P − 1, (3.40c)
eφ(−)
k (XD) =
X
s≥0
ˆa−(sP +k)(qD)
−(sP +k)q
sP +k+σ−(sP +k)
D
X−(sP +k)
D , k = 1,...,P − 1, (3.40d)
– 14 –
where we hide the dependence on qD to simplify the notation. Moreover, we define
eφP (XD) = eφ(+)
P (XD) +eφ(−)
P (XD), (3.41a)
eφk(XD) = eφ(+)
k (XD)−qk
Deφ(−)
k (XD), k = 1,...,Q − 1. (3.41b)
Putting Eqs. (3.38), (3.39) together and suitably identifying the functions just introduced in Eq. (3.41),
we can now write the antiholomorphic block as
ϕWKB(XD;qD) =−
1
2 + i
2π logX

eφP (XD)
+
 iP
2πQ +qD
∂
∂qD
Z XD
0
eφP (X′
D)dX′
D
X′
D
+
P−1X
k=1
eφk(XD)
qk
D− 1 .
(3.42)
Finally, we observe that
eφ(+)
P (XD) = Q
Pφ(+)
Q (X), eφ(−)
P (XD) = Q
PqsQ(1−Q
P )φ(−)
Q (X), (3.43)
as a direct consequence of the cancellation symmetry in Eq. (3.23). Therefore, after summing
Eqs. (3.35), (3.42) and using the relations in Eq. (3.43), we obtain the expression
ϕWKB(X;q) +ϕWKB(XD;qD) =

−1
2− Q
2P− iQ
2πP logX

φQ(X)
+
 iQ
2πP + 2q ∂
∂q
Z X
0
φQ(X′)dX′
X′
+sQ

1− Q
P
Z X
0
φ(−)
Q (X′)dX′
X′
+
Q−1X
k=1
φk(X)
qk− 1 +
P−1X
k=1
eφk(X
Q
P )
qkQ2
P 2− 1
.
(3.44)
Moreover, the power series defined in Eqs. (3.34), (3.41), which dictate the formula for the exact
wave function at rational points following Eq. (3.44), are determined by the function
Υ(X) = Υ(+)(X) + Υ(−)(X) =
X
n≥1
ˆan(q)
nqσn
Xn +
X
n≥1
ˆa−n(q)
(−n)qn+σ−n
X−n, (3.45)
where, again, we hide the dependence on q to simplify the notation. Indeed, we can write
φQ(X) = 1
Q
Q−1X
m=0
Υ(qmX), (3.46a)
φ(±)
k (X) = 1
Q
Q−1X
m=0
q∓mk Υ(±)(qmX,q ), k = 1,...,Q − 1, (3.46b)
– 15 –
and similarly
eφP (XD) = 1
P
P−1X
m=0
Υ(qm
DXD), (3.47a)
eφ(±)
k (XD) = 1
P
P−1X
m=0
q∓mk
D Υ(±)(qm
DXD), k = 1,...,P − 1. (3.47b)
Let us stress that the derivation we have presented here implies a fixed choice of the classical branch.
Indeed, the functions Υ(X),φQ(X),φk(X),eφP (XD),eφk(XD) are implicitly dependent on the label
α. We note that, applying Eqs. (3.27), (3.28), we can simply read off the integer coefficients c±s,
s∈ Z>0, from the function φQ(X). Namely, we have that
φQ(X) =
X
s≥1
cs
sQXsQ− c−s
sQX−sQ, (3.48)
after substituting qsQ = 1. In Appendix B, we describe an alternative way of computing the integer
sequences{c±s},s∈ Z>0 using Eq. (3.44). We will show in Section 4 that, starting from the known
closed expression for the holomorphic and antiholomorphic blocks, we can successfully compute
the integer coefficients for both series in X,X−1 and all choices of the saddle connection α in the
examples of the figure-eight and the three-twist knots.

---
doc_id: on-the-garoufalidis-kashaev-state-integral-invariant
doc_title: "of the requirements for the degree of Master of Science in Mathematics Boise State University August 2025"
section_id: sec-025-pentagon-identity-in-the-archimedean-case
section_title: "Pentagon identity in the Archimedean case"
section_number: null
pages: 26-28
source_pdf: On the Garoufalidis-Kashaev State-Integral Invariant.pdf
source_sha256: eda230da2a596783
doc_brief: "ON THE GAROUFALIDIS-KASHAEV STATE-INTEGRAL INVARIANT Amelia Palmer Dusenbury A thesis of the requirements for the degree of Master of Science in Mathematics Boise State University August 2025 — 61 sec"
---
Theorem 3. The function φ(α,x) = α(1 +x) satisfies the distributional pentagon
identity:
˜φ(α,x) ˜φ(β,y )α(y)β(x) =
Z
A
˜φ(β−γ,y/z ) ˜φ(γ,z ) ˜φ(α−γ,x/z )γ(z) d(γ,z ) (3.3)
for all (α,x), (β,y )∈A.
Proof of Theorem 3. Recall from Lemma 1 that for (η,t)∈ bB×B =:A with t̸= 1
˜φ(η,t ) = 1
η(t− 1)
1
∥1−t−1∥ = f(t)
η(t− 1),f (t) := 1
∥1−t−1∥.
Compute LHS.
˜φ(α,x) ˜φ(β,y )α(y)β(x) =f(x)f(y)α( y
x−1)β( x
y−1) =: LHS.
17
Expand RHS. Insert the same formula for every ˜φ in the integral:
RHS =
Z
bB
Z
B
f(y/z)
(β−γ)(y/z− 1)
f(z)
γ(z− 1)
f(x/z)
(α−γ)(x/z− 1)γ(z)dγdz.
Isolate the γ-dependence. For fixed z the integrand’s character part equals
γ(z)
γ(z− 1)
1
(β−γ)(y/z− 1)
1
(α−γ)(x/z− 1) =γ((y−z)(x−z)
z(z− 1) ) =:γ(a(z)).
Thus RHS =
R
B
F (z)
R
bBγ(a(z))dγ

dz withF (z) := f(y/z)f(z)f(x/z)
(β−γ)(y/z− 1)γ(z− 1)(α−γ)(x/z− 1)

char. part stripped
.
Because we chose Haar measures so that
R
bBγ(u)dγ =δB(u), we obtain [7] formula
15 Z
bB
γ(a(z))dγ =δB(a(z)).
Hence the γ–integration collapses and forces a(z) = 1, i.e.
a(z) = (y−z)(x−z)
z(z− 1) = 1 = ⇒ z = xy
x +y− 1 =:z0.
Substituting z =z0 into the scalar part gives
RHS =f(x+y−1
x )f( xy
x+y−1)f(x+y−1
y )α( y
x−1)β( x
y−1).
Because f(t) =∥1−t−1∥−1 satisfies f(x)f(y) = f(x+y−1
x )f( xy
x+y−1)f(x+y−1
y ), the
scalar factor above equals f(x)f(y). Multiplying by the same characters α and β we
finally get
RHS =f(x)f(y)α( y
x−1)β( x
y−1) = LHS.
18
Thus LHS = RHS as tempered distributions on A. The proof is complete.

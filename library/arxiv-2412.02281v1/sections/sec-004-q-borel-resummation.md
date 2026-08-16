---
doc_id: arxiv-2412.02281v1
doc_title: "u + A"
section_id: sec-004-q-borel-resummation
section_title: "q-Borel Resummation"
section_number: null
pages: 5-7
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
doc_brief: "Explicit evaluation of the q-Stokes matrices for certain confluent hypergeometric q-difference equations — We prove a connection formula for the basic hypergeomtric fu nction nϕn−1 (a1,...,a n−1"
---
In this subsection, we give a brief review to the theory of q-Borel resummation (see e.g., [1, 7, 18, 30, 42]).
The deﬁnitions and properties can be found in [1, 7, 42]. Deno te that
• C[ [z−1] ] (or C[ [z] ]) is the ring of formal power series of the variable z−1 (or z);
• M(C∗, 0) is the ﬁeld of functions which are meromorphic on some punc tured neighbourhood of 0 in C∗;
• S(a,b ) = {z ∈ ~C∗ | a< arg(z)<b } is an open sector with opening angle b −a on the Riemann surface
~C∗ of the natural logarithm, for two real numbers a<b ;
• [λ ;q] is the discrete q-spiral {λqn | n ∈ Z}.
Deﬁnition 2.6. Given ˆf = ∑ ∞
n=0anz−n ∈ C[ [z−1] ], its q-Borel transformation ˆBq;1 ˆf is deﬁned as:
( ˆBq;1 ˆf )(ξ) :=
∞∑
n=0
anq
n(n−1)
2 ξn ∈ C[ [ξ] ].
Let us introduce the space H[λ ;q]
q;1 of functions with q-exponential growth of order (at most) 1 at inﬁnity
along λ ∈ C∗.
Deﬁnition 2.7. Let λ ∈ C∗ and f (ξ) ∈ M (C∗, 0). We say that f (ξ) ∈ H[λ ;q]
q;1 , if f (ξ) admits an analytic
continuation deﬁned on S(arg(λ ) −ε, arg(λ ) + ε) for some ε > 0, with q-exponential growth of order 1 at
inﬁnity, which means that there exist constants L,M > 0, such that for any ξ ∈S(arg(λ ) −ε, arg(λ ) +ε),
|f (ξ)|<Mθ q(L|ξ|).
5
Deﬁnition 2.8. If a function f (ξ) ∈ H[λ ;q]
q;1 for some λ ∈ C∗, then its q-Laplace transformation is deﬁned by
(L[λ ;q]
q;1 f )(z) :=
∞∑
n=−∞
f (λqn)
θq (λqnz).
It is clear that the q-Laplace transformation is independent of the chosen repre sentativeλ and we have
Proposition 2.9. In a suﬃciently small punctured neighbourhood of inﬁnity, L[λ ;q]
q;1 f has poles of order at
most 1, that are contained in the q-spiral [−λ −1;q].
Now let us introduce [ λ ;q]-summable functions.
Deﬁnition 2.10. For ˆf ∈ C[ [z−1] ], if ˆBq;1 ˆf ∈ H[λ ;q]
q;1 for some λ ∈ C∗, then we say ˆf is [λ ;q]-summable and
call L[λ ;q]
q;1 ◦ ˆBq;1 ˆf its [λ ;q]-sum.
The q-summability of convergent power series is given as follows .
Proposition 2.11. If the disc of convergence of ˆf ∈ C[ [z−1] ]is {z ∈ C∗ | R< |z|}, then ˆf is [λ ;q]-summable
for any λ ∈ C∗ and
L[λ ;q]
q;1 ◦ ˆBq;1 ˆf = ˆf, for z ∈ {z ∈ C∗ | R< |z|} \[−λ −1;q].
The q-summability of the basic hypergeometric series nϕn−2
( a; b;q,z −1) is given as follows.
Proposition 2.12 ([1, 6]) . If a = (a1,...,a n), b = (b1,...,b n−2) satisfy
ai ⁄= 0, ai/a j /∈qZ, for 1 ≤i ⁄=j ≤n, and bl /∈ {0} ∪q−N, for 1 ≤l ≤n − 2, (13)
the formal series nϕn−2
( a; b;q,z −1) is [λ ;q]-summable for any λ ∈ C∗\ [−1;q]. Moreover, for c ∈ C∗, the
formal series nϕn−2
(
a; b;q,cz −1)
is [λ ;q]-summable for any λ ∈ C∗\ [−1/c ;q].
The q-Borel resummation can be applied to a [ λ ;q]-summable formal power series solution of a linear
q-diﬀerence equation (or a linear q-diﬀerence system)
bm(z)y (qmz) +bm−1(z)y
Ä
qm−1z
ä
+... +b0(z)y (z) = 0, (14)
to obtain a meromorphic solution. That is,
Proposition 2.13. Forλ ∈ C∗, it follows that
• If coeﬃcients bi(z) are rational functions, ˆf ∈ C[ [z−1] ]is [λ ;q]-summable and satisﬁes the equation (14),
then L[λ ;q]
q;1 ◦ ˆBq;1 ˆf is a meromorphic solution of (14).
• If coeﬃcients bi(z) are rational matrix-valued functions, ˆF =
( ˆfij
)
is a formal matrix-valued solution of
the system (14), with ˆfij ∈ C[ [z−1] ]being [λ ;q]-summable, then F =
Ä
L[λ ;q]
q;1 ◦ ˆBq;1 ˆfij
ä
is a meromorphic
solution of (14).
Deﬁnition 2.14. Let λ ∈ C∗ and ˆf = ∑ ∞
n=0anz−n ∈ C[ [z−1] ]. Suppose f is a function that is analytic on
some neighbourhood of inﬁnity except along the q-spiral [−λ −1;q]. We say that f is asymptotic to ˆf with
q-Gevrey order 1 along the direction λ , if for any ε,R > 0, there exist constants C,K > 0, such that for any
integerN ≥ 1 and
z ∈ {z ∈ C∗ | R< |z|} \ ∪m∈Z
¶
z ∈ C∗ | 0< |z−1 +λqm|<ε |λqm|
©
,
we have ⏐
⏐
⏐
⏐
⏐f (z) −
N−1∑
n=0
anz−n
⏐
⏐
⏐
⏐
⏐ ≤CKNq− N (N −1)
2 |z|−N.
Proposition 2.15. If ˆf ∈ C[ [z−1] ]is [λ ;q]-summable, then L[λ ;q]
q;1 ◦ ˆBq;1 ˆf is asymptotic to ˆf with q-Gevrey
order 1 along the direction λ .
Similarly, we can deﬁne the q-Borel resummation for ˆg ∈ C[ [z] ].
Deﬁnition 2.16. Given ˆg = ∑ ∞
n=0anzn ∈ C[ [z] ], the q-Borel transformation ˆBq;1ˆg is deﬁned as:
( ˆBq;1ˆg)(ξ) :=
∞∑
n=0
anq
n(n−1)
2 ξn ∈ C[ [ξ] ].
If ˆBq;1ˆg ∈ H[λ ;q]
q;1 for some λ ∈ C∗, then its q-Laplace transformation is given by
L[λ ;q]
q;1 ◦ ˆBq;1ˆg :=
∞∑
n=−∞
ˆBq;1 ˆg (λqn)
θq
Ä
λq n
z
ä .
In this case, we call ˆg is [λ ;q]-summable and L[λ ;q]
q;1 ◦ ˆBq;1ˆg is the [λ ;q]-sum of ˆg.
6
The q-summability of nϕn−2 (a; b;q,z ) is similar to the case of nϕn−2
( a; b;q,z −1) (see Proposition 2.12).
Proposition 2.17 ([1, 6]). If a = (a1,...,a n), b = (b1,...,b n−2) satisfy (13), the formal series nϕn−2 (a; b;q,z )
is [λ ;q]-summable for any λ ∈ C∗\ [−1;q].
We use the following notation to denote the [ λ ;q]-sum of nϕn−2 (a; b;q,z ) for simplicity.
Deﬁnition 2.18. For a = (a1,...,a n), b = (b1,...,b n−2) satisfying (13) and λ ∈ C∗\ [−1;q], the [λ ;q]-sum of
nϕn−2 (a; b;q,z ) is denoted by
nfn−2 (a; b;λ ;q,z ) :=
Ä
L[λ ;q]
q;1 ◦ ˆBq;1nϕn−2 (a; b;q,z )
ä
(z).
We can use the function nfn−2 (a; b;λ ;q,z ) to rewrite the [ λ ;q]-sum of nϕn−2
(
a; b;q,z −1)
. That is,
Proposition 2.19. For a = (a1,...,a n), b = (b1,...,b n−2) satisfying (13), we have
L[λ ;q]
q;1 ◦ ˆBq;1nϕn−2
Ä
a; b;q,z −1ä
= nfn−2
Ä
a; b;λ ;q,z −1ä
, (15)
L[λ ;q]
q;1 ◦ ˆBq;1nϕn−2
Ä
a; b;q,cz −1ä
= nfn−2
Ä
a; b;cλ;q,cz −1ä
. (16)
Here in (15) we require λ ∈ C∗\ [−1;q], and in (16) we require c ∈ C∗, λ ∈ C∗\ [−1/c ;q].

---
doc_id: arxiv-math-0108046v3
doc_title: "arXiv:math/0108046v3 [math.RT] 3 May 2002"
section_id: page-026
section_title: "Page 26"
section_number: null
pages: 26-26
source_pdf: 0108046v3.pdf
source_sha256: f47c1bd39c671cf3
toc_source: undetermined
doc_brief: "Presenting Schur algebras — Motivated by work of R.M. Green, we obtain a pre- sentation of Schur algebras (both the classical and quantized ver- sions) in terms of generators and relations."
---
26
STEPHEN DOTY AND ANTHONY GIAQUINTO
Proof. We will need the following identities (see [Lu2, §2.3 (g3), (g4)]):

Ki; 0
t
 
Ki; −t
t′

=

t + t′
t
 
Ki; 0
t + t′

(t, t′ ∈N)
(7.10)

Ki; c + 1
t

= vt

Ki; c
t

+ vt−c−1K−1
i

Ki; c
t −1

(t ≥1).
(7.11)
From the deﬁning relation (Q3) and the deﬁnition (see §2) of the root
vector Xα one proves that
KlXα = v(εl,α)XαKl
(α ∈Φ).
(7.12)
From this it follows by a simple calculation that

Kl; c
t

Xα = Xα

Kl; c + (εl, α)
t

(α ∈Φ, c ∈Z, t ∈N).
(7.13)
From this last equality it follows that for λ ∈Λ(n, d), α = εi −εj ∈Φ
(i̸ = j) we have
Xα1λ =

Ki; −1
λi
 
Kj; 1
λj
 Y
l̸=i,j

Kl
λl
!
Xα.
Multiply both sides of the preceding equality by

Ki
1

=

Ki; 0
1

and
use (7.10) to simplify the right-hand-side and use (7.13) to simplify the
left-hand-side. The result is the equality
Xα

Ki; 1
1

1λ =

λi + 1
1
 
Ki
λi + 1
 
Kj; 1
λj
 Y
l̸=i,j

Kl
λl
!
Xα.
By Proposition 7.6(a) the left-hand-side of this equality simpliﬁes to
give the equality

λi + 1
1

Xα1λ =

λi + 1
1
 
Ki
λi + 1
 
Kj; 1
λj
 Y
l̸=i,j

Kl
λl
!
Xα
and after cancelling the common scalar factor and expanding by means
of (7.11) (assuming λj > 0) this becomes
Xα1λ =

Ki
λi + 1
 
vλj

Kj
λj

+ vλj−1K−1
j

Kj
λj −1
 Y
l̸=i,j

Kl
λl
!
Xα.
In case λj > 0 after multiplying through in the above expression and
applying Proposition 7.4(c) we see that the ﬁrst summand must be zero,
so the above equality in that case simpliﬁes to Xα1λ = vλj−1K−1
j 1λ+αXα.

---
doc_id: arxiv-2605.19310v1
doc_title: "A FOURIER-FREE DENSITY-INCREMENT PROOF OF ROTH’S THEOREM MARK LEWKO"
section_id: sec-000-2-mark-lewko
section_title: "MARK LEWKO"
section_number: 2
pages: 1-4
source_pdf: 2605.19310v1.pdf
source_sha256: 047d492babc63d2f
doc_brief: "A FOURIER-FREE DENSITY-INCREMENT PROOF OF ROTH’S THEOREM — We give an elementary, Fourier-free proof of Roth’s theorem."
---
Abstract. We give an elementary, Fourier-free proof of Roth’s theorem.
The proof follows Roth’s original density-increment strategy, but replaces
the usual Fourier-analytic step with a direct combinatorial argument
involving averages over sub-progressions.
1.Introduction
In 1953, Roth proved that every subset of the integers of positive upper
density contains a nontrivial three-term arithmetic progression. This can be
stated in the following finite form.
Theorem 1(Roth [ 8]).For every α> 0, if N is sufficiently large, then every
set A⊂{ 0, 1,...,N− 1} with|A|≥αN contains a three-term arithmetic
progressionx, x+r, x+ 2rwithr̸= 0.
Roth’s theorem is a foundational result in density Ramsey theory; its
extension to longer arithmetic progressions is a celebrated theorem of Sze-
mer´ edi [9]. Proofs of Roth’s theorem have been given using quite different
methods: Roth’s original proof is Fourier analytic [ 8]; Furstenberg proved
Szemer´ edi’s theorem in full using ergodic-theoretic methods [2]; and graph-
theoretic proofs of Roth’s theorem follow from the triangle removal lemma
of Ruzsa and Szemer´ edi [7]. More combinatorial proofs have also been given
using Szemer´ edi’s cube lemma [4] as well as using ideas related to the more
general Hales–Jewett theorem [1]. There is also a rich history of quantitative
improvements, which we do not attempt to summarize here; see [ 5, 6] for
recent surveys.
Roth’s original proof uses a density-increment argument. Starting with a
set A⊂ [N] with no nontrivial three-term progressions, one proves that A
has increased density on a long subprogression. Passing to that progression
and rescaling, one repeats the argument. If the original interval is sufficiently
long, the density would eventually have to exceed 1, providing a contradiction.
The purpose of this note is to give a proof with the same density-increment
structure, but without using Fourier analysis. Instead of detecting a large
Fourier coefficient, we estimate certain averages over subprogressions directly.
The combinatorial approaches to Roth’s theorem have typically produced
very weak quantitative bounds. The argument here stays close to Roth’s
1
arXiv:2605.19310v1  [math.CO]  19 May 2026
2 MARK LEWKO
density-increment framework and gives a bound of the form
r3(N)≲ N
(log logN)c
withc = 1/11. This can be improved somewhat at the expense of complicating
the exposition, but the argument in its current form does not seem capable
of recovering the exponentc= 1 obtained by Roth’s original argument.
2.Notation
We write A≲B to mean A≤CB for a positive absolute constant C,
and similarly A≳B . We write A∼B when both A≲B and B≲A hold.
All implicit constants are absolute. For a prime m, write Zm = Z/mZ and
Z×
m =Z m\{0}.
3.Preliminaries
Write [N] ={0,...,N− 1} and choose a prime m with 4N < m <8N,
which we may do by Bertrand’s postulate. We embed [ N] in Zm in the
obvious way. The point of choosing m> 2N is that a three-term progression
inZ m whose terms all lie in [N] is a genuine integer progression.
Let α =|A|/N be the density of A in [N], and define f =1 A−α 1[N] on
Zm. Then f has mean zero on Zm, satisfies−α≤f≤ 1, and is supported
on [N]. For any functiong:Z m→R, set
E(g) =
X
t∈Zm
 X
x∈Zm
g(x)g(x+t)
!2
.
For the balanced function f, write R(t) =P
x∈Zmf(x)f(x +t), soE(f) =P
t∈ZmR(t)2. We will use the following non-negativity property.
Lemma 2.For anyh,k∈Z ×
m, one has
(3.1)
X
d∈Zm
R(hd)R(kd)≥0.
Proof.Letλ=kh −1. Usingt=hd, we have
X
d∈Zm
R(hd)R(kd) =
X
t∈Zm
R(t)R(λt) =
X
a,b,t∈Zm
f(a)f(a+t)f(b)f(b+λt).
To make the non-negativity explicit, use the bijective change of variables
(a,b,t )7→ (a,c,u ) given by c =a +t and u =b−λa . Then b =u +λa and
b+λt=u+λc, so the last sum becomes
X
u,a,c∈Zm
f(a)f(c)f(u+λa)f(u+λc) =
X
u∈Zm
 X
a∈Zm
f(a)f(u+λa)
!2
≥0.
□
A FOURIER-FREE DENSITY-INCREMENT PROOF OF ROTH’S THEOREM 3
4.No progressions imply large energy
For functionsf 1,f 2,f 3 :Z m→R, define
Λ(f1,f 2,f 3) :=
X
x,r∈Zm
f1(x)f2(x+r)f 3(x+ 2r).
If A⊂ [N]⊂Z m, then Λ(1A, 1A, 1A) is the number of three-term arithmetic
progressions in A, including the trivial progressions with r = 0. Hence, if A
contains no nontrivial three-term progressions, then Λ(1A, 1A, 1A) =|A|. On
the other hand, Λ(1 [N], 1[N], 1[N])≳N 2, since [N] contains≳N 2 three-term
progressions.
Lemma 3.Let g1,g 2,g 3 :Z m →R be bounded in absolute value by an
absolute constant. Then
|Λ(g1,g 2,g 3)|4≲m 5 min
1≤i≤3
E(gi).
Proof. It suffices to prove the following estimate. Let F,h 1,h 2 :Z m→R ,
withh 1,h 2 bounded, and leta,b∈Z ×
m witha̸=b. Then

X
y,r∈Zm
F(y)h 1(y+ar)h 2(y+br)

4
≲m 5E(F).
The three possible choices of the distinguished slot in Λ are obtained, after a
change of variables, from this estimate by taking ( a,b ) = (1, 2), (−1, 1), and
(−2,−1).
Let T denote the sum inside the fourth-power. Put λ =ba−1 and change
variables fromrtou=y+ar. Then
T=
X
y,u∈Zm
F(y)h 1(u)h2((1−λ)y+λu).
By Cauchy–Schwarz inu,
|T| 2≲m
X
u∈Zm

X
y∈Zm
F(y)h 2((1−λ)y+λu)

2
.
Expanding the square, then putting t =y′−y and z = (1−λ )y +λu, gives
|T| 2≲m
X
t∈Zm

X
y∈Zm
F(y)F(y+t)


×
 X
z∈Zm
h2(z)h2(z+ (1−λ)t)
!
.

---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY"
section_id: sec-015-323-example-c
section_title: "Example C"
section_number: 3.2.3
pages: 15-17
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
doc_brief: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
As one might have conjectured looking at the ﬁrst two examples, forx∈I2(n)
we have
bx =
∑
y≤x
vl(x)−l(y)hy (10)
If we would want to play the game we played in the ﬁrst two examples, this is,
if we wanted to expressbx as additions and substractions ofBott-Samelsons (i.e.
objects of the type bsbr··· bt, with s,r,...,t ∈S ) then we obtain the combina-
torics appearing in Temperley-Lieb algebras, but this approach is a bit compli-
cated. It is easier to prove directly equation (10).
We will prove equation (10) by induction on the length ofx. Let us call for the
moment
cx :=
∑
y≤x
vl(x)−l(y)hy
So our induction hypothesis is that by =cy for all elements y such that l(y)≤
n. Let us introduce the following
Notation 3.3 In the groupI2(n) =⟨s,r⟩ we will denote, for any 0≤i≤n,
s(i) :=srs···| {z }
i terms
∈W and r(i) :=rsr···| {z }
i terms
∈W
15
We will prove that
cs(n+1) =bscr(n)−cs(n−1) (11)
thus mimicking the construction that we will do in the proof of Theorem 3.2.
Once we have proved this, we are done, because the right-hand side is clearly
self-dual (by induction hypothesis), and the left-hand side clearly belongs to
hs(n+1) +∑
yvZ[v]hy and thuscs(n+1) =bs(n+1).
We callx :=s(n + 1). If
A :=
∑
0≤i≤n
vn−ihr(i)
and
B :=
∑
0<i<n
vn−ihs(i),
thencr(n) =A +B.
We have that
bsA =
∑
0≤i≤n
vn−ihs(i+1) +
∑
0≤i≤n
v(n+1)−ihr(i)
=
∑
1≤j≤n+1
v(n+1)−jhs(j) +
∑
0≤i≤n
v(n+1)−ihr(i)
=cs(n+1).
On the other hand we have, using the quadratic relation,
bsB =
∑
0<i<n
vn−ihr(i−1) +
∑
0<i<n
vn−i−1hs(i)
=
∑
0≤j<n−1
v(n−1)−jhr(j) +
∑
0<i<n
v(n−1)−ihs(i)
=cs(n−1)
thus proving equation (11).
Remark 2 We can see that the proof of equation (11) is independent of the
dihedral group in which one is placed, but one knows that in I2(n) we have
hs(n) =hr(n), and thus, by equation (11) we havebs(n) =br(n). This is the basic
insight of the following example.
16

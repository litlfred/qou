---
doc_id: mod-phi-convergence-approximation-of-discrete-measures-and-2
doc_title: "ANNALES DE L’INSTITUT FOURIER"
section_id: sec-007-21-deconvolution-residues-in-the-wiener-algebra
section_title: "Deconvolution residues in the Wiener algebra"
section_number: 2.1
pages: 16-18
source_pdf: mod-phi-convergence-approximation-of-discrete-measures-and-20yc5c6q3n.pdf
source_sha256: c563cc999000e75d
toc_source: outline
doc_brief: "ANNALES DE L’INSTITUT FOURIER — 27 sections: Front matter; Introduction; Poisson approximation of lattice-v"
---
Recall that the Wiener algebra A (T) is the complex algebra of absolutely
convergent Fourier series, endowed with the norm ∥f∥A = P
n∈Z |cn(f)|.
We shall use the following property of A (T), which is akin to Poincaré’s
inequality for Sobolev spaces (see [39, Section 6.2]):
Proposition 2.1. — There is a constant CH =
π
√
3 = 1.814 . . . such
that
∥f∥A ⩽|c0(f)| + CH∥f ′∥L 2
for all f ∈A .
Proof. — Combining the Cauchy–Schwarz inequality and the Parseval
identity, we obtain
∥f∥A = |c0(f)| +
X
n̸=0
1
n |n cn(f)|
⩽|c0(f)| +
sX
n̸=0
1
n2
sX
n̸=0
|n cn(f)|2
⩽|c0(f)| +
r
π2
3 ∥f ′∥L 2.
Note that the inequality is sharp, and it implies that the Sobolev space
W 1,2(T) of L 2 functions on T with weak derivative in L 2 is topologically
included in the Wiener algebra.
□
TOME 70 (2020), FASCICULE 3
1130
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Another important tool for the computation of total variation distances
is the following Lemma 2.2. Call deconvolution residue of a signed measure
µ on Z by another signed measure ν on Z the function
δ(ξ) := bµ(ξ) (bν(ξ))−1.
By Wiener’s theorem, if bν never vanishes, which is for instance the
case when it is the Fourier transform of an inﬁnitely divisible law ν [53,
Lemma 7.5], then bν−1 ∈A and the previous deconvolution happens in the
Wiener algebra: δ ∈A . Now, in order to measure the distance between
the law µ of X and a reference law ν, one can adopt the following point of
view, which is common in signal processing. For the deconvolution residue
to be considered as a small noise, δ has to be close to the constant function
1 (the Fourier transform of the Dirac distribution at zero). In particular,
suppose that we are given a general scheme of approximation of a sequence
of random variables (Xn)n∈N by a sequence of laws (νn)n∈N. Then, with the
notation of Deﬁnition 1.10, one has a sequence of deconvolution residues
δn(ξ) = c
µn(ξ)
c
νn(ξ) ,
and the quality of our scheme of approximation will be related to the speed
of convergence of (δn)n∈N towards the constant function 1. More precisely:
Lemma 2.2 (Fundamental inequality for deconvolution residues).
Let µ and ν be two signed measures on Z and δ = bµ
bν be the deconvolution
residue (we assume that bν does not vanish on T). For any c ∈A ,
dTV(µ, ν) ⩽∥c(δ −1)bν∥A + ∥δ −1∥A ∥(1 −c)bν∥A .
Proof.
dTV(µ, ν) = ∥bµ −bν∥A = ∥(δ −1)bν∥A
⩽∥c(δ −1)bν∥A + ∥(1 −c)(δ −1)bν∥A
⩽∥c(δ −1)bν∥A + ∥δ −1∥A ∥(1 −c)bν∥A .
□
In practice, c ∈A will be a carefully chosen cut function concentrated
on regions where bν is large. So, informally, ν is a good approximation of µ
if the deconvolution residue δ:
• is close to 1 where bν is large;
• has a reasonable norm in the Wiener algebra.
Note that the fundamental inequality does rely on the algebra norm of
A (T). We now quantify this idea.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1131

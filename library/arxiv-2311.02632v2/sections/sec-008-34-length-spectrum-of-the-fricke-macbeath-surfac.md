---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE CHUL-HEE LEE"
section_id: sec-008-34-length-spectrum-of-the-fricke-macbeath-surfac
section_title: "Length spectrum of the Fricke-Macbeath surface"
section_number: 3.4
pages: 19-21
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE CHUL-HEE LEE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
an in-depth analysis of closed geodesics on Hurwitz surfaces is presented, with a spe-
cial focus on the length spectrum of Hurwitz surfaces of low genera. Of particular
relevance to us, Vogeler offers an exhaustive table [Vog03, Table C.2] enumerating the
short primitive closed geodesics on the Fricke-Macbeath surface, along with their corre-
sponding lengths and multiplicities. This table comprehensively covers geodesics with
lengths below 14.49 [Vog03, p. 57]. For those interested on understanding the method
used, refer to [Vog03, Section 2.3].
In order to compute the multiplicity of λ1 for the Fricke-Macbeath surface using the
Selberg trace formula, we need the conjugacy classes of the two shortest lengths as
input data. The shortest classes have an approximate length of 5.796298891, while the
next shortest classes are about 8.303943294 in length.
To employ interval arithmetic in the trace formula, we need a precise error bound
for these lengths. To convert an entry from [Vog03, Table C.2] into a conjugacy class
of Γ, one can follow these steps:
• A proper label for a geodesic is a sequence consisting of the letters R and L.
The sequence begins with either one or twoR’s, followed by one or twoL’s, and
continues in this alternating pattern. Further details can be found in [Vog03,
p. 19].
20 CHUL-HEE LEE
• This proper label can be converted into a code. A code in the table is a sequence
of 1’s and 2’s. Each number in this sequence denotes the count of consecutive
R’s or L’s. As an illustration, the code (1122) translates to the proper label
RLRRLL. This encoding is described in [Vog03, p. 23].
• Now, one should substitute the letter R with the expression a−1b and the letter
L withb. This transformation yields a word consisting of a andb. The process
is explained in [Vog03, p. 32].
• Lastly, with the aid of (3.5) and (3.6), an exact matrix representation can be
obtained for this word in a and b.
Consider the first entry with code (1222) and n = 2 in [Vog03, Table C.2]. The code
(1222) which translates to the proper label ( RLLRRLL), and since n = 2, this label
repeats twice:
(RLLRRLL)(RLLRRLL).
The geodesic with this label corresponds to the conjugacy class of Γ containing
γ = (a−1b3a−1ba−1b3)(a−1b3a−1ba−1b3)
=γ15, as checked in (3.12).
Let z0 be half the trace of γ, whose minimal polynomial is 1 −x− 9x2 +x3. We can
easily check that
z0∈ (9.09783467903, 9.09783467905).
The length of γ is ℓ(γ) = 2 arccosh(z0) = 5.796298891... . This length is significant
as it represents the shortest geodesic length on the Fricke-Macbeath surface X . This
shortest geodesic length, also termed the systole and denoted by sys(X ), is defined as:
sys(X ) = min{ℓ(γ) :{γ}∈C (Γ)}.
Similarly, the geodesic labeled by the code (11111112) with n = 2 corresponds to
a conjugacy class with length 2 arccosh(z1) = 8.303943294... with z1 having minimal
polynomial−1− 25x− 31x2 +x3. We can easily check that
z1∈ (31.78746324455, 31.78746324457).
Finally, note that the multiplicity of a geodesic listed in Vogeler’s table should be
doubled when we are counting the number of corresponding conjugacy classes. This
adjustment is necessary because the table enumerates unoriented geodesics; see [Vog03,
Definition 9].
The preceding discussion can be summarized in the following proposition:
Proposition 3.9. Let z0 and z1 be the above algebraic numbers. The conjugacy
classes with the minimum length in C(Γ) has length 2 arccosh(z0), and there are 252
classes. There are 504 conjugacy classes that are the second shortest, each with a length
2 arccosh(z1).
SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURF ACE 21
The precise intervals within which z0 and z1 lie, as well as the above multiplicities
play a crucial role in the computations utilizing the Selberg trace formula with interval
arithmetic.

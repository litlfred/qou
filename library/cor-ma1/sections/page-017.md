---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-017
section_title: "Page 17"
section_number: null
pages: 17-17
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
16
SYLVIE CORTEEL AND OLIVIER MALLET
• else if ℓ> 1, remove the overlining of fm+ℓ−1 and overline fm,
• fm+ℓ←fm+ℓ−1, and
• fm ←fm + 1.
For example if m = 1 and the multuple is (1, ¯1, ¯3), we have n = 12, ℓ= 2 and F(1, ¯1, ¯3) = (¯2, 1, ¯2) whose
weight is 10.
Let Bk,i(n, j, N) be the number of overpartitions counted by Bk,i(n, j) of length N.
Let Bk,i(N) =
P
n,j Bk,i(n, j, N)qnaj. Now we divide the multiplicity sequence of an overpartition λ ∈Bk,i(N) into mul-
tuples going from the right to the left and we apply F to each multuple.
We call the result F(λ).
If
F(λ) has a zero part, this part is discarded. Note that if λ has weight n and length N then F(λ) has
weight n −N and length N or N −1. For example, λ = (0, (0, 1), (1, 1, 3)) has weight 24 and length 3 and
F(0, (0, 1), (1, 1, 3)) = (0, 1, 0, 2, 1, 2) whose weight is 21 and length 3.
Let Gk,i(N) be the generating function for the overpartitions µ = F(λ) where λ is an overpartition in
Bk,i+1(N) and has a multuple (f0, . . . , fℓ) with ℓ= 1 and fℓ̸ = ¯1.
Proposition 5.3. Let λ be an overpartition in Bk,i(N) with N > 0. Then
• λ is an overpartition of n and has a multuple (f0, . . . , fℓ) with ℓ> 1 or fℓ= ¯1 if and only if F(λ) is
an overpartition of n −N, has one less overlined part than λ and is in Bk,i(N −1).
• λ is an overpartition of n and has a multuple (f0, . . . , fℓ) with ℓ= 1 and fℓ̸ = ¯1 if and only if F(λ)
is an overpartition of n −N, has the same number of overlined parts as λ and is in Gk,i−1(N).
• λ is an overpartition of n and has no multuple (f0, . . . , fℓ) if and only if F(λ) is an overpartition of
n −N, has the same number of overlined parts as λ and is in Bk,i+1(N).
Let λ be an overpartition in Gk,i(N). Then
• λ is an overpartition of n and has a multuple (f0, . . . , fℓ) with ℓ> 1 or fℓ= ¯1 if and only if F(λ) is
an overpartition of n −N, has one less overlined part than λ and is in Bk,i(N −1).
• λ is an overpartition of n and has a multuple (f0, . . . , fℓ) with ℓ= 1 and fℓ̸ = ¯1 and F(λ) is an
overpartition of n −N, has the same number of overlined parts as λ and is in Gk,i−1(N).
• λ is an overpartition of n and has no multuple (f0, . . . , fℓ) if and only if F(λ) is an overpartition of
n −N + 1, has the same number of overlined parts as λ and is in Bk,i+1(N −1).
Proof. The full proof requires lots of details and is given in [35]. We give here the ﬁrst ingredient of the
proof, that is, if λ is an overpartition such that the condition ∀ℓ, fℓ+ fℓ+1 < k+1 holds, then this condition
still holds for F(λ). Indeed the only successive multiplicities fm and fm+1, where fm + fm+1 can increase
are such that fm or fm+1 is the leftmost entry of a multuple. If it is fm then after the operation fm is now
overlined and fm + fm+1 < k+1 still holds. If it is fm+1 then fm + fm+1 increases by one, only if fm = 0
before the operation. We know that fm+1 < k −1 before the operation (as fm+1 + fm+2 < k and fm+2 > 0)
then fm + fm+1 < k still holds after the operation.
□
Note that Bk,i(0) = 1 as the only overpartition of length 0 is the empty overpartition and that if an
overpartition has a multuple (f0, . . . , fℓ) then i > 1. The previous remark and proposition imply that:
Bk,1(N)
=
qNBk,2(N);
Bk,i(N)
=
qN(Bk,i+1(N) + Gk,i−1(N) + aBk,i(N −1)), if 1 < i ≤k;
Gk,1(N)
=
qN−1Bk,2(N −1);
Gk,i(N)
=
qN−1Bk,i+1(N −1) + qNGk,i−1(N) + aqNBk,i(N −1), if 1 < i < k;
Bk,i(0)
=
1.

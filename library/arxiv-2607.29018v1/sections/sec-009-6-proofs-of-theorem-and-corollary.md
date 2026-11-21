---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-009-6-proofs-of-theorem-and-corollary
section_title: "Proofs of Theorem and Corollary"
section_number: 6
pages: 19-23
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
toc_source: inferred
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
With the preparation in the previous section, we can finally prove Theorem 1.6 and Corollary
1.7.
Proof of Theorem 1.6. Let n ≥5, and let S be a nonempty normal set in Sn. Let AS, BS and
CS be as in (3). Then S = AS ∪BS ∪CS. Since Cay(Sn, S) is normal, by (6) and Table 1,
its eigenvalue corresponding to the partition (n −1, 1) is
λ(n−1,1) =
X
σ∈S
˜χ(n−1,1)(σ)
=
1
n −1
X
σ∈S
(|fix(σ)| −1)
=
1
n −1

X
σ∈AS
(|fix(σ)| −1) −
X
σ∈CS
1


=
1
n −1



X
σ∈AS
|fix(σ)|

−(|AS| + |CS|)

.
(12)
By our assumption (5) and equation (12), we have λ(n−1,1) ≤1.
Necessity. Suppose that Cay(Sn, S) has the Aldous property. Then its strictly second
largest eigenvalue, which is attained by the standard representation ρ(n−1,1), is λ(n−1,1) ≤1.
By Theorem 5.5, we have S ∈{Sn \ {e}, Sn \ An, An \ {e}}.
Sufficiency. If S = Sn \ {e}, then Cay(Sn, S) ∼= Kn! has spectrum {(n! −1)1, (−1)n!−1}.
The eigenvalue n! −1 is attained by ρ(n), while the strictly second largest eigenvalue −1 is
attained by ρ(n−1,1).
If S = Sn \ An, then Cay(Sn, S) ∼= Kn!/2,n!/2 has spectrum

n!
2
1 , 0n!−2,

−n!
2
1
. The
eigenvalue n!
2 is attained by ρ(n), the eigenvalue −n!
2 is attained by ρ(1n), and the strictly
second largest eigenvalue 0 is attained by ρ(n−1,1).
If S = An \ {e}, then Cay(Sn, S) ∼= 2Kn!/2 has spectrum

n!
2 −1
2 , (−1)n!−2

. The
eigenvalue n!
2 −1 is attained by both ρ(n) and ρ(1n), while the strictly second largest eigenvalue
−1 is attained by ρ(n−1,1).
19
Therefore, in all three cases, Cay(Sn, S) has the Aldous property. Moreover, since in each
case the strictly second largest eigenvalue is λ(n−1,1) ≤1, it follows from (12) that all three
sets S satisfy (5).
This proves the sufficiency and completes the proof.
Proof of Corollary 1.7. Let n ≥5, and let S be a nonempty normal set in Sn.
(a) Suppose that S ⊆Suppn({n−1, n}). Then AS = ∅, so S satisfies condition (5). Hence
Theorem 1.6 applies to Cay(Sn, S). Since n ≥5, each of Sn\{e}, Sn\An and An\{e} contains
an element whose support size is neither n −1 nor n. Thus, S /∈{Sn \ {e}, Sn \ An, An \ {e}}
and therefore, by Theorem 1.6, Cay(Sn, S) does not have the Aldous property.
(b) Suppose that |AS| −|CS| + 2(n −1) ≥0 and S /∈{Sn \ {e}, Sn \ An, An \ {e}}. By
(3) and (4), {AS, AS, BS, BS, CS, CS} is a partition of Sn \ {e}. Hence
|AS| + |AS| + |BS| + |BS| + |CS| + |CS| = n! −1.
(13)
Set
X = {(σ, i) ∈Sn × [n] : σ(i) = i}.
We use double counting to enumerate X. First, for each fixed i, there are exactly (n −1)!
permutations σ ∈Sn satisfying σ(i) = i. Therefore,
|X| =
n
X
i=1
|{σ ∈Sn : σ(i) = i}| =
n
X
i=1
(n −1)! = n!.
(14)
Second, each permutation σ contributes exactly |fix(σ)| to the cardinality of X. Thus,
|X| =
X
σ∈Sn
|fix(σ)|
=
n
X
k=0
X
σ∈Suppn(k)
|fix(σ)|
=
X
σ∈Suppn(0)
|fix(σ)| +
X
σ∈Suppn(1)
|fix(σ)| +
n−1
X
k=2
X
σ∈Suppn(k)
|fix(σ)| +
X
σ∈Suppn(n)
|fix(σ)|
= n + 0 +
n−1
X
k=2
X
σ∈Suppn(k)
|fix(σ)| + 0
= n +
X
σ∈Suppn({2,3,...,n−2})
|fix(σ)| +
X
σ∈Suppn(n−1)
|fix(σ)|.
This together with (13) and (14) yields
X
σ∈AS
|fix(σ)| +
X
σ∈AS
|fix(σ)| =
X
σ∈Suppn({2,3,...,n−2})
|fix(σ)|
= n! −n −
X
σ∈Suppn(n−1)
|fix(σ)|
(15)
20
= n! −n −
X
σ∈BS
|fix(σ)| −
X
σ∈BS
|fix(σ)|
= n! −n −|BS| −|BS|
= |AS| + |AS| + |CS| + |CS| + 1 −n.
Since |AS| −|CS| + 2(n −1) ≥0 by our assumption, it follows that
|AS| + |CS| + n −1 −
X
σ∈AS
|fix(σ)| =
X
σ∈AS
|fix(σ)| −|AS| −|CS| + 2(n −1)
=
X
σ∈AS
(|fix(σ)| −1) −|CS| + 2(n −1)
≥|AS| −|CS| + 2(n −1)
≥0.
That is, S satisfies condition (5). Since S /∈{Sn \ {e}, Sn \ An, An \ {e}} by our assumption,
it follows from Theorem 1.6 that Cay(Sn, S) does not have the Aldous property.
(c) Suppose that Suppn(n) ⊆S and S̸ = Sn \ {e}. Since Suppn(n) contains both even
and odd permutations, S is neither Sn \ An nor An \ {e}. Moreover, CS = Suppn(n) and
hence CS = ∅. Thus, |AS| −|CS| + 2(n −1) = |AS| + 2(n −1) ≥0 and therefore by (b),
Cay(Sn, S) does not have the Aldous property.
Acknowledgements
Chenhui Lv was supported by the Outstanding Doctoral Students
Overseas Study Program of the University of Science and Technology of China. Sanming Zhou
was supported by a Discovery Project (DP250104965) of the Australian Research Council.
References
[1] D.
Aldous,
https://www.stat.berkeley.edu/users/aldous/Research/OP/sgap.
html.
[2] G. Alon, G. Kozma, D. Puder, On the Aldous-Caputo spectral gap conjecture for hy-
pergraphs, Math. Proc. Cambridge Philos. Soc. 179 (2025) 259–298.
[3] L.W. Beineke, Characterizations of derived graphs, J. Combin. Theory 9 (1970) 129–135.
[4] P. Caputo, T.M. Liggett, T. Richthammer, Proof of Aldous’ spectral gap conjecture, J.
Am. Math. Soc. 23 (3) (2010) 831–851.
[5] F. Cesi, Cayley graphs on the symmetric group generated by initial reversals have unit
spectral gap, Electron. J. Combin. 16 (1) (2009) N29.
[6] F. Cesi, On the eigenvalues of Cayley graphs on the symmetric group generated by a
complete multipartite set of transpositions, J. Algebraic Combin. 32 (2) (2010) 155–185.
21
[7] F. Cesi, A few remarks on the octopus inequality and Aldous’ spectral gap conjecture,
Comm. Algebra 44 (1) (2016) 279–302.
[8] F. Cesi, On the spectral gap of some Cayley graphs on the Weyl group W(Bn), Linear
Algebra Appl. 586 (2020) 274–295.
[9] F. Chung, J. Tobin, The spectral gap of graphs arising from substring reversals, Electron.
J. Combin. 24 (3) (2017) Paper No. 3.4, 18 pp.
[10] D. Cvetkovi´c, P. Rowlinson, S. Simi´c, Spectral Generalizations of Line Graphs: On
Graphs with Least Eigenvalue −2, London Mathematical Society Lecture Note Series,
Vol. 314, Cambridge Univ. Press, Cambridge, 2004.
[11] P. Diaconis, M. Shahshahani, Generating a random permutation with random transpo-
sitions, Z. Wahrscheinlichkeitstheor. Verwandte Geb. 57 (2) (1981) 159–179.
[12] L. Flatto, A.M. Odlyzko, D.B. Wales, Random shuffles and group representations, Ann.
Probab. 13 (1) (1985) 154–178.
[13] W. Fulton, Young Tableaux: With Applications to Representation Theory and Geom-
etry, London Mathematical Society Student Texts, Vol. 35, Cambridge Univ. Press,
Cambridge, 1997.
[14] C. Godsil, G. Royle, Algebraic Graph Theory, Graduate Texts in Mathematics, Vol. 207,
Springer, New York, 2001.
[15] R.A. Horn, C.R. Johnson, Matrix Analysis, second ed., Cambridge Univ. Press, 2012.
[16] X. Huang, Q. Huang, The second largest eigenvalues of some Cayley graphs on alter-
nating groups, J. Algebraic Combin. 50 (1) (2019) 99–111.
[17] X. Huang, Q. Huang, S.M. Cioab˘a, The second eigenvalue of some normal Cayley graphs
of highly transitive groups, Electron. J. Combin. 26 (2) (2019) P2.44.
[18] I.M. Isaacs, Character Theory of Finite Groups, AMS Chelsea Publishing, Providence,
RI, 2006.
[19] G. James, M. Liebeck, Representations and Characters of Groups, second ed., Cambridge
Univ. Press, New York, 2001.
[20] M. Kassabov, Subspace arrangements and property T, Groups Geom. Dyn. 5 (2) (2011)
445–477.
[21] M. Krebs, A. Shaheen, Expander Families and Cayley Graphs: A Beginner’s Guide,
Oxford Univ. Press, 2011.
22
[22] Y. Li, B. Xia, S. Zhou, Aldous’ spectral gap property for normal Cayley graphs on
symmetric groups, European J. Combin. 110 (2023), Paper No. 103657, 16 pp.
[23] Y. Li, B. Xia, S. Zhou, The second largest eigenvalue of normal Cayley graphs on
symmetric groups generated by cycles, J. Combin. Theory Ser. A 206 (2024), Paper No.
105885, 32 pp.
[24] Y. Li, B. Xia, S. Zhou, The second largest eigenvalue of some nonnormal Cayley graphs
on symmetric groups, J. Combin. Theory Ser. A 218 (2026), Paper No. 106097, 30 pp.
[25] X. Liu, S. Zhou, Eigenvalues of Cayley graphs, Electron. J. Combin. 29 (2) (2022) Paper
No. 2.9, 164 pp.
[26] R. Maleki, A.S. Razafimahatratra, On the second eigenvalue of certain Cayley graphs
on the symmetric group, Bull. Malays. Math. Sci. Soc. 46 (5) (2023) Paper No. 158, 13
pp.
[27] O. Parzanchevski, D. Puder, Aldous’s spectral gap conjecture for normal sets, Trans.
Amer. Math. Soc. 373 (10) (2020) 7067–7086.
[28] B. Sagan, The Symmetric Group: Representations, Combinatorial Algorithms, and Sym-
metric Functions, Vol. 203, Springer Science & Business Media, 2001.
[29] J.P. Serre, Linear Representations of Finite Groups, Springer, 1977.
[30] J. Siemons, A. Zalesski, On the second largest eigenvalue of some Cayley graphs of the
symmetric group, J. Algebraic Combin. 55 (3) (2022) 989–1005.
[31] Z. Stani´c, On regular graphs and coronas whose second largest eigenvalue does not
exceed 1, Linear Multilinear Algebra 58 (5-6) (2010) 545–554.
[32] B. Steinberg, Representation Theory of Finite Groups:
An Introductory Approach,
Springer, 2012.
[33] P.H. Zieschang, Cayley graphs of finite groups, J. Algebra 118 (2) (1988) 447–454.
23

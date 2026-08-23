---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-035-0-log1-ez-2iπ
section_title: "Log(1 −ez− 2iπ"
section_number: 0
pages: 28-28
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI) of"
---
N ) − Log(1 −ez)
)
+ Log(1 −ez).
Using the Taylor expansion Li 2(ez− 2iπ
N ) − Li2(ez) = − 2iπ
N
∫ 1
0 Log(1 −ez− 2iπ
N t)dt and changing
z to z + 2iπ
N this can be written
1
N
(
ΨN (z) − ΨN
(
(z + 2iπ
N
))
=
∫ 1
0
Log(1−ez+ 2iπ
N t)dt+ 1
2
(
Log(1 −ez+ 2iπ
N ) + Log(1 −ez)
)
.
Since we assume R(z)< 0, the real part of the RHS is bounded from above by 2Log(2), an d
hence
⏐
⏐
⏐
⏐exp
( 1
N ΨN (z)
) ⏐
⏐
⏐
⏐ ≤ exp
( 1
N R
(
ΨN
(
z + 2iπ
N
))
+ 2 log(2)
)
≤ exp(CM,α,B ′,B′′ + (k + 2)Log(2)).
Finally, assume that R(z) < −c, c >0. Since Log |1 −ez| ≥ Log|1 − |ez|| ≥ Log(1 −e−c),
similarly as above we obtain | exp( 1
N ΨN (z))| ≤ exp( 1
N R(ΨN (z − 2iπ
N )) − 2Log(1 −e−c)) ≤
exp(CM,α,B ′,B′′ − 2Log(1 −e−c)) for z ∈] − ∞, −c[+i[2π − 3π
2N, 2π]. When 2 π ≤ I(z) ≤ K,
the bound of | exp( 1
N ΨN (z))| is obtained similarly by using (66). This concludes the proo f of
(ii).
(iii) First note that any compact subset of U is contained in UM,α,k,K,c for some M,α,k,K
and c, for N large enough. By (ii) above and Montel’s theorem, it follows that the sequence
of functions exp( 1
N ΨN (z)) is a normal family (that is, it has a subsequence which converges
uniformly on compact subsets) on U . Since by (i) it converges simply to 1 on a subset of U
having a limit point, by Vitali’s Theorem on the convergence of holomorphic functions, the
convergence is uniform on all compact subsets of U . This concludes the proof. □
Recall that y1/N := exp(Log(y)/N) for any y ∈ C∗. Put
(67) gN (z) :=
N −1∏
j=1
(1 −zζ −j)j/N.
In order to prove Theorem 1.1, we will need to study asymptoti cs of gN (ez) for z = l0,N of the
form (39). First note that, by collecting conjugate terms it is immediate that |gN (1)N | =N
N
2 ,
and factorizing by ζ −j/2 each term in the product yields
gN (1)N =e
πi

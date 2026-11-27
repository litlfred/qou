---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-029-722-the-case-of-n-0
section_title: "The case of n= 0"
section_number: 7.2.2
pages: 32-36
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
In the case of n = 0, however, we do not obtain the falloﬀ for the individual terms seen in Figure 3. Indeed, to
stand any chance of recovering the desired central-charge terms in (117b) we must have constant contributions.
In Figure 5 we see that the matrix elements of the individual terms between the ground state and itself indeed
seem to stay constant as N increases, while they decrease as before between the ground state and the ﬁrst
excited state within the same momentum sector (see Figure 10 in Appendix E).
While we must now consider both linear and cubic terms in the expansion of the sinuses, we can still ignore
the quintic and higher terms. We also no longer need to expand any exponentials. This means that most of the
derivation of R above is still valid, as long as we apply it to the linear term inn. There is only one modiﬁcation
we need to make, compared to (123): When n = 0 the normal ordering of (119) becomes important, and we
need to subtract from 2[ ej, [ej+1,ej+2]] +√Q(ejej+1 +ej+1ej) its ground-state expectation value 4 sin 3γ I1,
where the constant I1 follows from the Bethe ansatz [1]
I1 =
∫ ∞
−∞
t2 sinh(π−γ)t
sinh(πt) cosh(γt) dt. (125)
Taking this into account we deﬁne the remainder at n = 0 as
R =−[ej, [ej+1,ej+2]]−
√
Q(ejej+1 +ej+1ej)− 2ej + 8 sin3γI 1. (126)
Including the cubic terms in the expansion of the trigonometric functions in (116) yields
[Lp + ¯L−p, L−p− ¯Lp] = N
2π
( γ
π sinγ
)3
p
{
3
N∑
j=1
[ej, [ej+1,ej+2]] +
N∑
j=1
(√
Q(ejej+1 +ej+1ej)− 2ej
)}
− 1
12
π
N
( γ
π sinγ
)3
p3
{
27
N∑
j=1
[ej, [ej+1,ej+2]] +
N∑
j=1
(√
Q(ejej+1 +ej+1ej)− 2ej
)}
+ O
( 1
N2
)
. (127)
To see whether the term linear in p converges to the desired value we consider matrix elements of (126)
numerically as shown in Figure 6, which indicates a falloﬀ O(1/Nr) for⟨gs|R|gs⟩ with an exponent r around
32
4. We show similar ﬁgures for the ﬁrst few excitations above the ground state in Appendix E. There the value
of the slope r in the limit is more unclear due to larger ﬁnite-size eﬀects, but the results still indicate r> 2 for
these states.
Figure 6: Absolute value of matrix elements of R as deﬁned in (123), plotted using the same conventions as in
Figure 3 but with the choice of |u⟩ =|v⟩.
We now turn our attention to the term ∝p3 in (127), which reads
− 1
12
π
N
( γ
π sinγ
)3
p3
{
27
N∑
j=1
[ej, [ej+1,ej+2]] +
N∑
j=1
(√
Q(ejej+1 +ej+1ej)− 2ej
)}
, (128)
and evaluate its average in the ground state. From our study of the∝p part of (127), we know already that the
contribution from the terms Ep≡⟨ gs|3[ej, [ej+1,ej+2]] +√Q(ejej+1 +ej+1ej)− 2ej|gs⟩ vanishes as N→∞ .
This leaves the contribution from 24[ ej, [ej+1,ej+2]] in (128) and therefore, in order for (116 ↦→ (117) also for
n = 0, we would need the following miraculous identity to hold
Ep3≡ [ej, [ej+1,ej+2]]∞ + π2c
12
(sinγ
γ
)3
?
= 0, (129a)
where we use the notation [ ej, [ej+1,ej+2]]∞ = limN→∞⟨gs|[ej, [ej+1,ej+2]]|gs⟩. Using results from the Bethe
ansatz, it was shown in [1] (section KS 3.3) that (129a) is equivalent to
c
?
=c∗, (129b)
where we have deﬁned
c∗ =− 24γ3I0
π2 sin2γ + 48γ3
π2 I1. (130)
It was furthermore shown in [1] (section KS 3.3) that (129) holds true indeed when x = 1, 2, 3, but not for
general x. We conjecture that Ep3 will make up for the diﬀerence between the left- and right-hand side of
criterion (129), that is precisely
Ep3 = π2
12
(sinγ
γ
)3
(c−c∗). (131)
The numerics indicate that this is true: the extrapolated values of Ep3 are shown for a range of x in Table 2.
That is, the limit of (127) when applied to the ground state is incorrect only for the p3 term, the one that
contains the central charge.
Ep3 satisfying the conjecture (131) is equivalent to the ground-state expectation value of [ ej, [ej+1,ej+2]]
being equal to 2 sinγI0− 4 sin3γI1. Combining this with the result KS (3.41)
[ej, [ej+1,ej+2]]∞ +
√Q
2 (ejej+1 +ej+1ej)∞ = 2 sin3γI 1. (132)
we can improve (132) by conjecturing the values of each of its terms separately:
Exchange of commutators and limits: We have the results
[ej, [ej+1,ej+2]]∞ = 2 sin γI 0− 4 sin3γI 1, (133a)
(ejej+1 +ej+1ej)∞ = 6 sin3γI 1− 2 sinγI 0
cosγ , (133b)
where the integral I0 is deﬁned by (17) and I1 by (125).
33
x = 1:
N Ep3
6 -0.09108037
8 -0.04173017
10 -0.02441356
12 -0.01616525
14 -0.01154442
16 -0.00867872
18 -0.00677235
20 -0.00543712
22 -0.00446415
24 -0.00373254
p8 0.0000006
conj 0
x = 1.5:
N Ep3
6 -0.18750921
8 -0.08790715
10 -0.05204436
12 -0.03471144
14 -0.0249148
16 -0.01880414
18 -0.01472315
20 -0.0118568
22 -0.00976384
24 -0.00818762
p8 -0.00011095
conj -0.00011266
x = 2:
N Ep3
6 -0.26295146
8 -0.12396495
10 -0.07352658
12 -0.04905309
14 -0.03519046
16 -0.02653245
18 -0.02074547
20 -0.0166787
22 -0.01370811
24 -0.01147035
p8 0.0000024
conj 0
x = 2.5:
N Ep3
6 -0.3182588
8 -0.15047958
10 -0.08932876
12 -0.05959601
14 -0.04273623
16 -0.03220009
18 -0.0251554
20 -0.02020382
22 -0.01658653
24 -0.01386144
p8 0.00010867
conj 0.00010568
x = 3 :
N Ep3
6 -0.3587194
8 -0.1700361
10 -0.10107585
12 -0.06750028
14 -0.04844759
16 -0.03653616
18 -0.02857005
20 -0.02297004
22 -0.01887873
24 -0.01579641
p8 0.00000334
conj 0
x = 4 :
N Ep3
6 -0.41165366
8 -0.19603869
10 -0.11698482
12 -0.07843206
14 -0.05653502
16 -0.04283788
18 -0.03367441
20 -0.0272313
22 -0.02252338
24 -0.01897619
p8 -0.00079389
conj -0.00079737
x = 6:
N Ep3
6 -0.46366442
8 -0.22244484
10 -0.13377148
12 -0.09046753
14 -0.06585191
16 -0.05044634
18 -0.04013642
20 -0.0328855
22 -0.02758643
24 -0.02359336
p8 -0.00312128
conj -0.00312477
x = 10π :
N Ep3
6 -0.52432884
8 -0.25560287
10 -0.15658134
12 -0.10816223
14 -0.08061811
16 -0.06337137
18 -0.05182545
20 -0.04370333
22 -0.03776655
24 -0.03329234
p8 -0.01034513
conj -0.01034891
Table 2: Comparison of the numerical measures for Ep3, deﬁned in (129a), and its conjectured value which is
the right-hand side of (131). The agreement between the extrapolated values and the conjecture is seen to be
excellent, with a precision of the order 10 −6 for all values of x. The same conventions as in Table 1 are used
for the extrapolated values p8.
In Appendix D we prove these conjectures (so they are actually theorems), by using known ground state
expectation values of spin operators in the XXZ spin chain [56]. In Appendix D.1 we consider the limit γ→ 0
corresponding to x→∞ , showing that the integrals in (133) take the form of polylogarithms in agreement
with the known results for ground state expectation values of spin operators in the XXX spin chain [57]. We
note that the limit γ→ 0 is where the theory is the most interacting, and where the anomaly is the largest
(c = 1). Solving the integrals within (131) numerically for increasingly large ﬁnite values of x indicates that Ep3
converges towards its limit of Ep3(x)
⏐⏐
x→∞ =−0.011 114 954··· from above, meaning that the magnitude of Ep3
is the largest in this limit. We also see that the eﬀect of parasitic couplings in Figure 2 is the most pronounced
at large x.
We next turn to the ﬁrst few excited states. To have the same deviation for the central term we would need
the matrix elements ⟨v|[ej, [ej+1,ej+2]]|v⟩, for |v⟩ any scaling state, to go towards the same value as for the
ground state—that is, we need ⟨v| :[ej, [ej+1,ej+2]]:|v⟩ to go to zero. This matrix element is shown in Figure
5, where the conjectured ground state expectation value in (133) is used for the normal ordering. We see that
it indeed tends to zero as N→∞ for all scaling states under consideration, which indicates that the central
term is wrong by a constant term, rather than by an operator. This constant deviation corresponds precisely to
replacingc, as given by (32), by the slightly diﬀerent value c∗ given in (130) in the cubic term∝p3. Altogether
we have:
Exchange of commutators and limits: We have the conjecture
[Lp + ¯L−p, L−p− ¯Lp]↦→ 2p
(
L0 + ¯L0− c
12
)
+p3c∗
6 (134)
with c given by (32) and c∗ given by (130).
34
Figure 7: Remake of Figure 2. In this remake the commutator [ L−2, L2] is used, rather than the product
L−2L2, and no cutoﬀ is taken. This commutator is denoted “Original”. We also show the result using a
modiﬁed version of the Koo-Saleur generators given by (137), labelled “Modiﬁed”. “Conj*” refers to the result
found by applying (136), while “Conj” refers to the CFT result as in Figure 2. The same sizes N and method
of extrapolation is used as in Figure 2, and the extrapolated values from Figure 2 are shown for comparison
(“No cutoﬀ” and “Cutoﬀ”).
Having shown by the combination of (124) and (134) that [ Lp+n + ¯L−p−n, L−p− ¯Lp] is conjectured to have
the correct limit up to the central term, it is natural to ask if we can eliminate the chiral-antichiral “cross-terms”
and write the relation for the limit of [Lp+n, L−p] on its own. In other words: is the limit of the chiral-antichiral
commutator [Lp+n, ¯Lp] zero? In Appendix F we explore this question using the same methodology as in this
section, and show that numerical evidence indeed indicates that the chiral-antichiral commutator vanishes in
the limit:
Exchange of commutators and limits: We have the conjecture
[Lp+n, ¯Lp]↦→ 0. (135)
Combining the three conjectures (124), (134) and (135) we thus obtain in the scaling limit a modiﬁcation of
the Virasoro commutation relations (40) on the form
[Lm, Ln] = (m−n)Lm+n +δm+n,0
1
12(m3c∗−mc). (136)
We can remake Figure 2 using this new conjecture. This is done in Figure 7, where it is shown that the
eﬀect of the “parasitic couplings” is in agreement with (136). We stress that this conjecture applies for the
commutator [L2, L−2] and not for the product L2L−2 alone, as is seen in the ﬁgure. We conclude that the
limit of commutators is the same as the commutator of limits up to a modiﬁcation of the central term.
In Figure 7 we also show the modiﬁcation recently suggested by Shokrian-Zini and Wang in [25] (Conjecture
5.5), which amounts to changing the phases within the Koo-Saleur generators (31) to
Ln[N] = N
4π

− γ
π sinγ
N∑
j=1
ein(j+1/2)2π/N (ej−e∞) +ein(j+1)2π/N iγ
π sinγ [ej,ej+1]

 + c
24δn,0, (137a)
¯Ln[N] = N
4π

− γ
π sinγ
N∑
j=1
e−in(j+1/2)2π/N (ej−e∞)−e−in(j+1)2π/N iγ
π sinγ [ej,ej+1]

 + c
24δn,0.(137b)
We ﬁnd that while the numerical values show a faster convergence, the change of the central term is the same
as with the original Koo-Saleur generators. That the central term must behave in the same way indeed follows
directly from the calculations and numerical evidence above, where we in particular ﬁnd that we may shift the
phase by a ﬁnite amount without aﬀecting the limit.
Although the relation in (136) is no longer the expected relation of the Virasoro algebra at central charge c,
35
the Jacobi identity would nevertheless be satisﬁed:
[Lm, [Ln, Lp]] + [Ln, [Lp, Lm]] + [Lp, [Lm, Ln]]
= (n−p)[Lm, Ln+p] + (p−m)[Ln, Lp+m] + (m−n)[Lp, Lm+n]
=δm+n+p,0
1
12
{
(n−p)(m3c∗−mc) + (p−m)(n3c∗−nc) + (m−n)(p3c∗−pc)
}
= 0. (138)
Here, the ﬁrst equality follows from the fact that all Lm+n+p terms cancel; the second equality is the application
of (136); and to establish the third equality, note all terms proportional to c inside the parenthesis cancel out
for any values of m,n,p , while those proportional to c∗ cancel because of the constraint p =−m−n. We could
indeed redeﬁne the generators L0, ¯L0 to obtain from (136) the relation of the Virasoro algebra at central charge
c∗. This would, however, not resolve the underlying diﬀerence between limits of commutators and commutators
of limits.

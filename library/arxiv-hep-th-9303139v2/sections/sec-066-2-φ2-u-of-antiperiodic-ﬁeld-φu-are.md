---
doc_id: arxiv-hep-th-9303139v2
doc_title: "ITFA 93-10 March 1993 A.Morozov"
section_id: sec-066-2-φ2-u-of-antiperiodic-ﬁeld-φu-are
section_title: "(∂Φ)2 (u) of antiperiodic ﬁeld Φ(u)), are:"
section_number: 2
pages: 131-138
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
doc_brief: "ITFA 93-10 March 1993 A.Morozov — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
˜L−2 =
X
k≥1
(k + 1
2)T2k+1
∂
∂˜T2(k−1)+1
+ T 2
1
4 ;
˜L0 =
X
k≥0
(k + 1
2)T2k+1
∂
∂˜T2k+1
;
˜L2n =
X
k≥0
(k + 1
2)T2k+1
∂
∂˜T2(k+n)+1
+
+1
4
n−1
X
k=0
∂2
∂˜T2k+1∂˜T2(n−k−1)+1
−(−)n
16ǫ2n;
n > 0.
(5.24)
So far everything what was done was just change of variables and all relations
were exact for any ǫ, no limits were taken.
128
Operators (5.24) are very similar to L2n, arising in the ”continuous Vi-
rasoro constraints” (1.3), imposed on partition function of X3-Kontsevich
model. There are, however, two discreapancies.
First,
∂
∂˜T appear in (5.24) instead of
∂
∂T in generators in (1.3). One can
argue that this diﬀerence is not really essential, since ˜T2k+1 and T2k+1 diﬀer
by terms, which are proportional to ǫ2 and thus vanish in the continuum
limit ǫ →0. (Note, however, that this reasoning can be applied only for
every particular constraint ˜L2nZ = 0, n ≥−1, not to the entire generating
functional, where diﬀerent terms are summed, multiplied by diﬀerent powers
of ǫ.)
The second discreapancy is a litlle more serious: it is the occurence of
an extra term (−)n+1
16ǫ2n
for all n ≥0 (this diﬀerence is present for n = 0
as well, because L0 contains the item
1
16, which is lacking in (5.24).) This
extra term can not be eliminated by just taking continuum limit: moreover,
it blows up instead of vanishing when ǫ →0. Remarkably enough, this term
disappears when we turn to consideration of actual Virasoro constraints, not
just a formal choice of time variables. It cancels completely with the other
potential source of problem for the derivation of continuous Ward identites.
We proceed now to this most sophisticated matter in this whole subsection.
The thing is that, as we already mentioned before, the reduction of dis-
crete Virasoro constraint L2nZN = 0 contains some non-vanishing terms with
the odd-time derivatives:

X
k>0
2kt2k
∂
∂t2k+2n
+ 2
n
X
k=0
∂2
∂t2k∂t2n−2k

Zred
N
=
=
 n
X
k=0
∂2
∂t2k∂t2n−2k
−
n−1
X
k=0
∂2
∂t2k+1∂t2n−2k−1
!
Zred
N .
(5.25)
We added an extra term with the second even-time derivatives to both sides
of the identity, in order to get at the r.h.s. a combination, which has a chance
to vanish in continuum limit. (This formula still needs to be corrected, see
eq.(5.29) below.)
In order to ﬁnd rigorous reason for elimination of the terms at the r.h.s
we need to address to explicit formulas from the last subsection of section 4
129
(no simpler way is known so far). The crucial formula which we need is:
∂2φn
∂tk∂tl
= ∂
∂tk
⟨n | hl | n⟩
⟨n | n⟩
=
 X
m>n
−
X
m<n
! ⟨n | hk | m⟩⟨m | hl | n⟩
⟨m | m⟩⟨n | n⟩
,
(5.26)
and the most important feature of it is its R-matrix structure (the fact that
a diﬀerence occurs at the r.h.s.).
This structure implies almost complete
cancellation of terms, when we sum over n in order to get log ZN = PN−1
0
φn,
leaving only a ﬁnite sum of the length independent of N:
∂2 log ZN
∂tk∂tl
=
X
0<j<min(k,l)


N−1
X
n=N−j
⟨n | hk | n + j⟩⟨n + j | hl | n⟩
⟨n | n⟩⟨n + j | n + j⟩

.
(5.27)
The ﬁnite sum at the r.h.s. can be expressed in terms of Rn = eφn−φn−1,
which are exactly the quantites to satisfy equations of Volterra hierarchy
and tending to constant (denoted by R0 in the previous section) in continuum
limit. Locality property - the ﬁniteness of the sum at the r.h.s in (5.26) -
implies that this r.h.s. tend to a constant value as N →∞. This constant
does not completely cancels in the diﬀerence
 n
X
k=0
∂2
∂t2k∂t2n−2k
−
n−1
X
k=0
∂2
∂t2k+1∂t2n−2k−1
!
log Zred
N ,
(5.28)
and the remaining contributions appears to be exactly what necessary to
cancel the dangerous term (−)n+1
16ǫ2n
which appeared in the diﬀerence between
˜Ln and Ln. We refer to ref.[28] for more details about these cancellations,
and the only thing to discuss at the rest of this subsection is the diﬀerence
between the r.h.s. of (5.25) and (5.28). In the second expression the second
derivatives are taken of log Z, while they are of z itself in the ﬁrst one. Of
course,
∂2 log Zred
N
∂t2k+1∂t2n−2k−1
=
1
Zred
N
∂2Zred
N
∂t2k+1∂t2n−2k−1
but this is not true for even derivatives. So, identity (5.25) yet needs to be
transformed a little more in order to contain exactly (5.26) at its r.h.s. If
130
this is achieved, the l.h.s. acquires additional contribution and turns into
X
k>0
2kt2k
∂Zred
N
∂t2k+2n
+
n
X
k=0
 
2
∂2Zred
N
∂t2k∂t2n−2k
−
1
Zred
N
∂Zred
N
∂t2k
∂Zred
N
∂t2n−2k
!
=
= 4
q
Zred
N Lred
2n
q
Zred
N .
(5.29)
As a result of all this reasoning we conclude that the double scaling con-
tinuum limit of reduced 1-matrix model can be described by the following
relation:
lim
d.s. ǫ→0, N→∞
q
Zred
N {teven} = U−1ZV = X3
3 {T},
(5.30)
where factor U is deﬁned in (5.20), relation between t and T-variables is
given by (5.17) and ZV = X3
3 {T} is X3-Kontsevich model. The motivation for
this conclusion is that both sides of the equation satisfy the same continuous
Virasoro constraints (1.3).
This whole derivation can be straightforwardly generalized to the case of
multiscaling limit in conformal matrix models and analogous relation con-
tains roots of the p-th degree, see [39] for detailed discussion.
5.4
From Gaussian to X3 Kontsevich model
We shall now abandon these complicated matters and give a simple illustra-
tion of how the things can work, if expressed in the adequate terms. Namely,
as alternative to the sophisticated procedure, involving explicit switch to
Kazakov variables and the study of limits of Ward-identites (loop equations),
we shall just use the equivalence of the discrete 1-matrix model and Gaus-
sian Kontsevich model, proved in the section 3.8 above in order to take the
continuum limit just of this simplest Kontsevich model. This procedure, sug-
gested in ref.[36] appears to be just a kind of a standard eveluation of the
integral in the large N-limit by the steepest descent method. It is important
here that GKM is not sensitive to the size of the matrix n in Kontsevich
integral, therefore this limit, when expressed in terms of GKM, has nothing
to do with the inﬁnitely large matrices.
Relation to be proved below is
lim
d.s. N→∞F{ ˆV } = F 2
{V },
(5.31)
131
where ˆV (X) = 1
2X2 −N log X and V (X) = 1
3X3.
Very naively, what happens as N →∞is that in the Kontsevich integral,
Z
dX exp tr

−1
2X2 + N log X + ΛX

(5.32)
a stationary point arises at X = X0, such that
X0 = N
X0
+ Λ.
(5.33)
Expansion of this action in powers of ˜X = γ−1(X −X0) comes entirely from
the logarithmic piece:
S −S0 = γ2
2 ˜X2 −N

log

1 + γ ˜
X
X0

−
˜
X
X0

=
= γ2
2

1 + N
X2
0
 ˜X2 +
P
k≥3
N
k

−γ
˜
X
X0
k .
(5.34)
In the continuum limit γ should be adjusted in such a way, that quadratic
term is ﬁnite, i.e. γ ∼

1 + N
X2
0
−1/2. Now, if Λ remains ﬁnite as N →∞,
X0 ∼
√
N, γ ∼1 and all the terms with k ≥3 in the sum are damped as
γkNX−k
0
∼N1−k
2 . This is the naive continuum limit. However, it is clear,
that one can usually ask Λ to behave more adequately - blow up together
with growth of N - and ﬁne tune the way in which it tends to inﬁnity so that
at last the ﬁrst term with k = 3 also survives. For this purpose Λ and thus
X0 should scale in such a way, that both quantites γ2
 
1 + N
X2
0
!
and Nγ3
X3
0
remain ﬁnite. This requirement in the case of the latter expression means
that γ ∼X0N−1/3 and then
γ2
 
1 + N
X2
0
!
∼N + X2
0
N2/3
.
This is never ﬁnite, unless N + X2
0 →0 as N →∞. This in turn implies
that X0 ∼i
√
N and Λ →2X0 ∼2i
√
N should be pure imaginary. One can
also check that the terms with k > 3 in the sum (5.34) all tend to zero in
this speciﬁc limit. Thus we are left with a model which has only cubic and
quadratic terms in the action. By simple shift of variables quadratic term
132
can be changed for a linear one and we get a description of the theory in the
vicinity of the stationary point in terms of an X3-Kontsevich model.
In practice things are a little more complicated, because also reduction
to even-times should be taken into account. However, this does not really
add too many new problems. We need that only even times t2k =
1
2ktr 1
Λ2k
remain non-vanishing, while all the odd times t2k+1 =
1
2k+1tr
1
Λ2k+1 = 0. This
obviously implies that the matrix Λ should be of block form:
Λ =
 
M
0
0
−M
!
(5.35)
and, therefore, the matrix integration variable is also naturally decomposed
into block form:
X =
 
X
Z
Z
Y
!
.
(5.36)
Then
F{ ˆV =X2/2−N log X} =
Z
dX dYd2Z
det(XY −¯Z 1
Y ZY)Ne−tr{|Z|2+X 2/2+Y2/2−MX+MY}.
(5.37)
To take the limit N →∞, one should assume certain scaling behaviour of X ,
Y and Z. Moreover, our previous naive consideration gave us some feeling
of the ﬁne tuned scaling behaviour can look like. So we take
X = γ(iβI + x),
Y = γ(−iβI + y),
Z = γζ,
M = γ−1(iαI + m)
(5.38)
with some large real α, β and γ. If expressed through these variables, the
133
action becomes:
tr

|Z|2 + X 2/2 + Y2/2 −MX + MY −N log(XY −¯Z 1
Y ZY)

=
= γ2tr
1
2(iβI + x)2 + 1
2tr(iβI −y)2 + |z|2

−
−tr(iαI + m)(2iβI + x −y)−
−Ntr log β2γ2
 
1 −ix −y
β
+ xy
β2 −|ζ|2
β2 (1 + O(1/β))
!
=
(5.39)
= [2αβ −β2γ2 −2N log βγ]tr I −2iβ tr m+
(A)
+i
 
βγ2 −α + N
β
!
(tr x −tr y) + 1
2
 
γ2 −N
β2
!
(tr x2 + tr y2)+
(B)
+
 
γ2 + N
β2
!
tr|ζ|2−
(C)
−tr mx + tr my + iN
3β3tr(x3 −y3)+
(D)
+O(N/β4) + O
 
|ζ|2 N
β3
!
.
(E)
We want to adjust the scaling behaviour of α, β and γ in such a way that
only the terms in the line (D) survive. This goal is achieved in several steps.
The line (A) describes normalization of functional integral, it does not
contain x and y. Thus, it is not of interest for us at the moment.
Two terms in the line (B) are eliminated by adjustment of α and γ:
γ2 = N
β2 , α = 2N
β
.
(5.40)
As we shall see soon, γ2 = N/β2 is large in the limit of N →∞. Thus, the
term (C) implies that the ﬂuctuations of ζ-ﬁeld are severely suppressed, and
this is what makes the terms of the second type in the line (E) negligible.
More general, this is the reason for the integral Z{ ˆV } to split into a product
of two independent integrals leading to the square of partition function in
the limit N →∞(this splitting is evident as, if Z can be neglected, the only
mixing term log det
 
X
Z
Z
Y
!
turns into log XY = log X + log Y).
134
Thus, we remain with a single free parameter β which can be adjusted so
that
β3
N →const
as
N →∞
(i.e. β ∼N1/3, γ2 ∼N1/3, α ∼N2/3),
(5.41)
making the terms in the last line (E) vanishing and the third term in the
line (D) ﬁnite.
This proves the statement (5.31) in a rather straightforward way. Unfor-
tunately no generalization of this procedure for other discrete models is found
so far, the main problem beeing identiﬁcation of GKM-type realizations of
other (for example, conformal) discrete matrix models.
6

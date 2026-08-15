---
doc_id: arxiv-hep-th-0205308v2
doc_title: "WDVV Equations as Functional Relations"
section_id: sec-001-wdvv-and-dispersionless-hirota-equations
section_title: "WDVV and dispersionless Hirota equations"
section_number: null
pages: 3-5
source_pdf: 0205308v2.pdf
source_sha256: 2de5a4f40d80174c
doc_brief: "WDVV Equations as Functional Relations — 5 sections: Introduction; WDVV and dispersionless Hirota equ; The associativity equations as coc"
---
The WDVV equations usually follow from the crossing relations
∑
k
Ck
ijCn
kl =
∑
k
Ck
ilCn
kj (7)
for the structure constants of some algebra
φ i ◦ φ j =
∑
k
Ck
ijφ k. (8)
It is useful also to write (7) in the matrix form
Ci · Cj = Cj · Ci, ∀i, j (Ci)l
m = Cl
im. (9)
Equations (7) are algebraic relations and they turn into the WDVV sy stem of nonlin-
ear diﬀerential equations after expressing the structure const ants in terms of the third
derivatives of some function F (a1, . . . , a N )
Ck
ij = ηklFijl. (10)
Generically the matrix η can be an arbitrary linear combination with time dependent
coeﬃcients η = ∑
j α j(a)Fj , but for simplicity we will mostly consider η = F1. Then
ηrs = ια dTrs.
3
Various rewritings of the WDVV equations are possible. In the Frobe nius manifold
setting there is a pencil of ﬂat connections, while the general equa tions (1) are equivalent
[12] to the commuting of matrix-valued vector ﬁelds:
[∂i − (Fj )−1Fi ∂j, ∂ k − (Fj )−1Fk ∂j] = 0
(with ﬁxed j). For our purposes one may also rewrite (7) as
∑
k
Ck
ijFkln =
∑
k
Ck
ilFkjn . (11)
With one form C = η−1dT ( i.e. Ck
ijdai = ηkl∂iTjldai = ηklFijldai) we have
[Ci, Cj] = 0 ⇐ ⇒C ∧ C = 0 ⇐ ⇒dT ∧ η−1dT = 0. (12)
Unfortunately the connection C is unrelated to the various connections arising in the
special K¨ ahler geometry because of the (arbitrary) appearance of η which is unrelated to
the special K¨ ahler metric. In general the curvature of C is nonvanishing. (The curvature
will, for example, vanish as a consequence of the WDVV equations if th ere is a symmetry
Lα dT = µdT , for some matrix µ .) The ﬁnal form of (12) is reminiscent of the Hirota
bilinear equations which may be interpreted in terms of Pl¨ ucker for mulae, but again the
appearance of η means the bilinear form in such formulae is not constant. Whatever, the
ﬁnal form shows that the WDVV equations impose relations on the pe riod matrices T ,
and consequently restrict the associated Seiberg-Witten curves that can yield solutions
of (1).
An important observation was made recently in [13] where it was show n that in
the case of dispersionless integrable hierarchies the WDVV equation s maybe derived
directly by diﬀerentiating corresponding Hirota algebraic relations. In particular, the
solutions associated with the Landau-Ginzburg topological models c an be constructed
in this way. Below, we will reverse the arrow of this implication and demo nstrate that
the WDVV equations, if rewritten in terms of second derivatives, ca n be simply viewed
as certain Hirota-like functional relations.
The dispersionless Hirota relations (see [13] and references there in about the details
and their explicit form) for the second derivatives, which can be writ ten as
Fij = Tij(ϕ ) (13)
where Tij are some known functions and {ϕ i} denote some restricted set (of cardinality
N , the size of the matrices under consideration in the ﬁnite-dimension al situation)
second derivatives, for example
ϕ i = F1i(a) (14)
Without specifying form of the functions Tij in (13) this is just a dimensional statement
that the matrix of second derivatives of any function can be expressed in terms of only
a vector of variables.
Consider the “period” matrix (3) which for any integrable system is a function of
only N variables. This means that in the “Siegel upper half-space” {Tij} of dimension
N (N + 1)
2 we have a “submanifold” of dimension N
Tij = Tij(a1, . . . , a N ) (15)
4
or codimension N (N − 1)
2 given by deﬁning equations
fA(Tij) = 0 A = 1, . . . , N (N − 1)
2 (16)
Of course, on this submanifold (under a generic assumption of nons ingularity) one may
choose new variables, say
ϕ i = T1i(a) (17)
Consequently there exist functional relations
Tij = Tij(ϕ 1, . . . , ϕ N ) = Tij(a(ϕ 1, . . . , ϕ N )) (18)
between the matrix elements of the whole period matrix, exactly as o ne has in disper-
sionless Hirota’s relations. In the case of (17) all of the matrix eleme nts of the period
matrix would be expressed in terms of a single row or column. (We give a n example of
this in section 4.)
More generally, let us assume we can ﬁnd coordinates ϕ k so that
dTij = Ck
ij dϕ k. (19)
Using the deﬁnition (10) this means
dϕ k = ηkldal. (20)
Both (19) and (20) have the common integrability condition
dηkl ∧ dal = 0 ⇐ ⇒M i
sFirk = M i
rFisk, M i
r = ∂α i
∂a r , (21)
where the α i’s were the coeﬃcients deﬁning η above. These are certainly satisﬁed for
constant α i. Thus the choice (17) would correspond to η = F1. Supposing the integra-
bility condition (21) holds, our assumption (19) means that the stru cture constants can
be integrated, i.e. deﬁned as derivatives of the functions (13)
Ck
ij = ∂T ij
∂ϕ k
(22)
and that
Tij(ϕ ) =
∫ ∑
k
Ck
ijdϕ k, (23)
i.e. the structure constants determine the form of the Hirota-like relations (13).

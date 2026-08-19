---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-004-42-irreducible-constituents-and-dimension-formul
section_title: "Irreducible constituents and dimension formulas: the Archimedean case"
section_number: 4.2
pages: 11-14
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
The harmonic analysis corresponding to the complex and real Grass mannian is classical
by now. It relates to special cases of harmonic analysis on compact symmetric spaces. To
emphasize the similarities with the non-Archimedean case and the qua ntum case, we now
shortly describe the relevant results for the complex Grassmannia n G(n,d ; C), following
closely the presentation in [5, Section 2]. For the real case, we refe r to [12] and especially
to [30] (the presentation in [30] is very close to the (quantum) com plex case as discussed
in this paper).
12 URI ONN AND JASPER V. STOKMAN
To avoid confusion with standard notations for the complexiﬁcation of a compact Lie
group, we write
(4.3) ( K, M) = (U(d), U(d −n) × U(n))
for the Gelfand pair ( KF, MF) when F = C. The irreducible K-representations are
parametrized by the cone
(4.4) P +
d = {µ ∈ Zd |µ1 ≥µ2 ≥ · · · ≥ µd} ⊂ Zd,
by associating to µ ∈ P +
d the K-representation LC
µ of highest weight µ ∈ P +
d . The Weyl
character formula states that the restriction of the character ofLC
µ (µ ∈P +
d ) to the compact
d-torus of diagonal matrices diag( u1,...,u d) in U(d) is the Schur function
sµ(u1,...,u d) = ∆( u)−1
∑
w∈Sd
(−1)l(w)uw(µ+ρd) (µ ∈P +
d ),
where ∆( u) = ∏
1≤i<j≤d(ui −uj) is the Vandermonde determinant, l(w) is the length of
w ∈ Sn, and ρd = (d − 1,d − 2,..., 0) ∈ P +
d is the staircase partition. The dimension of
LC
µ being the evaluation of its character at the unit element e ∈ K thus yields
(4.5) Dim C(Lq
µ) = sµ(1), µ ∈P +
d .
The resulting, famous, Weyl dimension formula is
(4.6) Dim C(LC
µ) =
∏
1≤i<j≤d
(µi −µj +δi −δj
δi −δj
)
, µ ∈P +
d ,
where
(4.7) δ = 1
2
(
d − 1,d − 3,..., 3 −d, 1 −d
)
is the half sum of positive roots in the standard realization of the Ad−1-type root system in
Rd. We note that other explicit dimension formulas are known, mostly wit h a combinatorial
ﬂavour. For instance, for µ ∈P +
d withµd ≥ 0, Dim C(LC
µ) is the number of standard Young
tableaux of shape µ. Furthermore, Dim C(LC
µ ) can be explicitly expressed in terms of
products of hook-lengths of the Young diagram of shape µ (see [18]).
We state now a diﬀerent type of dimension formula for the subclass o f spherical ir-
reducible representations associated to the complex Grassmannia n G(n,d ; C) ≃ K /M.
This dimension formula is based on the expression (4.2) of the dimensio n in terms of the
corresponding zonal spherical functions. The spherical unitary dual ( KF/MF)ˆ naturally
identiﬁes with the set Λ n of partitions of length at most n via the embedding
(4.8) λ♮ = (λ1,λ 2,...,λ n, 0,..., 0/bracehtipupleft
/bracehtipdownright/bracehtipdownleft/bracehtipupright
d−2n
, −λn,..., −λ2, −λ1)
of Λ n in P +
d . Consequently the irreducibles
V C
λ :=LC
λ♮, (λ ∈ Λ n)
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 13
form a complete set of representatives of the irreducible MF-spherical KF-representations,
and the Grassmann representation C
(
G(n,d ; C)
)
has a multiplicity-free decomposition
C
(
G(n,d ; C)
)
≃
⨁
λ∈Λ n
V C
λ
as KF-module. We write ϕC
λ for the zonal spherical function corresponding to the irreducible
representationV C
λ (λ ∈ Λ n).
Proposition 4.2. Forλ ∈ Λ n we have
DimC
(
V C
λ
)
=
n∏
i=1
(d − 2n + 1 + 2(λi +ρi)
d − 2n + 1 + 2ρi
) d−2n∏
j=1
(j +λi +ρi
j +ρi
) 2
×
∏
1≤j<k≤n
(d − 2n + 1 +λj +λk +ρj +ρk
d − 2n + 1 +ρj +ρk
) 2(λj −λk +ρj −ρk
ρj −ρk
) 2
,
whereρ = (n − 1,n − 2,..., 1, 0) ∈ Λ n is the staircase partition.
The natural proof of the proposition uses the identiﬁcation of the radial parts of the
zonal spherical functions ϕC
λ (λ ∈ Λ n) as BC n-type Heckman-Opdam polynomials with
appropriate multiplicity parameters (see e.g. [12] and [5, Section 2]). The dimension
formula (4.2) then yields an expression in terms of evaluations and qu adratic norms of
Heckman-Opdam polynomials, which both have been explicitly evaluate d.
Proposition 4.2 follows also as a direct consequence of the formula
(4.9) Dim C
(
V C
λ
)
=Dq2
(
λ;q2(d−2n+1),q 2;q2)
|q=1, (λ ∈ Λ n),
expressing the dimensions in terms of the classical ( q = 1) degeneration of the generalized
dimension formula Dq(λ) (see (2.4)). Formula (4.9) is a direct consequence of the identiﬁ-
cation of multivariable little q-Jacobi polynomials with quantum zonal spherical functions
on the quantum complex Grassmannian, see Subsection 5.3 for deta ils. We note also that
the classical (q = 1) degeneration of the multivariable little q-Jacobi polynomials have been
studied in detail in [29], also in the context of harmonic analysis on (qua ntum) complex
Grassmannians (see [5]).
Remark 4.3. Proposition 4.2 can easily be reconﬁrmed by specializing the Weyl dimen sion
formula (4.6) to µ =λ♮ (λ ∈ Λ n).
For the real Grassmannian, ( KR/MR)ˆ also naturally identiﬁes with Λ n, see [12], [23] and
[30]. The harmonic analytic results from [12] lead to similar explicit dimens ion formulas
for the associated irreducible MR-spherical KR-representationsV R
λ (λ ∈ Λ n). In particular
the dimensions can also be expressed as classical ( q = 1) degenerations of generalized
dimensions
(4.10) Dim C
(
V R
λ
)
=Dq2
(
λ;qd−2n+1,q ;q
)
|q=1, (λ ∈ Λ n),
which follow as in the complex case from the results in [12] and [29] (see also [23, §2.1.1]).
14 URI ONN AND JASPER V. STOKMAN

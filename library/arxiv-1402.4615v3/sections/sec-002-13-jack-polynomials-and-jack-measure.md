---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-002-13-jack-polynomials-and-jack-measure
section_title: "Jack polynomials and Jack measure"
section_number: 1.3
pages: 5-7
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
and the main steps of the proof, we ﬁrst need to review the conn ection between
Jack measure and Jack polynomials.
1.3.1. Jack polynomials. In a seminal paper [Jac71], Jack introduced a family of
symmetric functions J (α)
λ depending on an additional parameter α. These func-
tions are now called Jack polynomials. For some special values of α, they coincide
6 M. DOŁ ˛ EGA AND V . FÉRAY
with some established families of symmetric functions. Nam ely, up to multiplica-
tive constants, for α = 1 , Jack polynomials coincide with Schur polynomials, for
α = 2 , they coincide with zonal polynomials, for α = 1 /2, they coincide with
symplectic zonal polynomials, for α = 0 , we recover the elementary symmetric
functions and ﬁnally their highest degree component in α are the monomial sym-
metric functions. Moreover, Jack polynomials for α = −(k + 1)/(r + 1) verify
some interesting annihilation conditions [FJMM02] and the general α case (with
some additional, technical assumptions) is relevant in Kad ell’s work in relation
with generalizations of Selberg’s integral [Kad97].
Over the time it has been shown that several results concerning Schur and zonal
polynomials can be generalized in a rather natural way to Jac k polynomials (Sec-
tion (VI.10) of Macdonald’s book [Mac95] gives a few resultsof this kind), there-
fore Jack polynomials can be viewed as a natural interpolati on between several
interesting families of symmetric functions.
1.3.2. A characterization of Jack measure. Expanding Jack polynomials J (α)
λ in
power-sum symmetric function basis, we deﬁne the coefﬁcients θ(α)
ρ (λ) by:
(6) J (α)
λ =
∑
ρ:
|ρ|=|λ|
θ(α)
ρ (λ) pρ.
In the case α = 1, Jack polynomials specialize to
J (1)
λ = n!
dim(λ) sλ,
where sλ is the Schur function and dim(λ) is the dimension of the symmetric
group representation associated to λ. Hence, using Frobenius formula [Mac95,
page 114], we can express θ(1)
ρ (λ) in terms of irreducible character values of the
symmetric group. Namely
θ(1)
ρ (λ) = n!
zρ
χλ
ρ
dim(λ) ,
where χλ
ρ is the character of the irreducible representation indexed by λ evalu-
ated on a permutation of cycle-type ρ and zρ is the standard numerical factor∏
i imi(ρ)mi(ρ)!, where mi(ρ) is the number of parts of ρ equal to i. By anal-
ogy to this, we use in the general case the terminology Jack characters for θ(α)
ρ (λ)
(while they do not have any representation theoretical inte rpretation, they share a
lot of property with characters of the symmetric groups).
The following property, which corresponds to the case π = (1 n) of [Mat10,
Equation (8.4)], characterizes Jack measure:
(7) EP(α)
n
(θ(α)
ρ (λ)) = δρ,(1n),
where λ is a random Young diagram with n boxes distributed according to P(α)
n .
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 7
1.3.3. A central limit theorem for Jack characters. As in the case α = 1 , an im-
portant intermediate result, which may be of independent in terest, is an algebraic
central limit theorem. Namely we prove that Jack characters for hooks (i.e. ρ is a
hook) have joint Gaussian ﬂuctuations.
Theorem 1.2. Choose a sequence (Ξ k)k=2,3,... of independent standard Gaussian
random variables. Let (λ(n))n≥1 be a sequence of random Young diagrams of size
n distributed according to Jack measure. Deﬁne the random variable
Wk(λ(n)) =
√
k θ(α)
(k,1n−k)(λ(n))
nk/2 .
Then, as n → ∞, we have:
(Wk)k=2,3,...
d− →(Ξ k)k=2,3,... ,
where d− →means convergence in distribution of the ﬁnite-dimensional laws.
In the case α = 1 , this theorem was proved independently by Kerov [Ker93b,
IO02] and Hora [Hor98]. With the method developed here, one c an even give an
upper bound on the speed of convergence of the distribution function:
Theorem 1.3. We use the same notation as in Theorem 1.2. Then, for any integer
d ≥ 2 and real numbers x2, · · · , xd,
⏐
⏐P(W2 ≤ x2, · · · , Wd ≤ xd) − P(Ξ 2 ≤ x2, · · · , Ξ d ≤ xd)
⏐
⏐ = O(n−1/4),
where the constant hidden in the Landau symbol O is uniform on x2, · · · , xd, but
depends on d.
In the case α = 1 and d = 2 , the study of the speed of convergence of W2
towards a Gaussian variable has been initiated by Fulman in [Ful04], who proved a
bound of ordern−1/4. This bound has then been improved ton−1/2 in two different
works [SS06, Ful06]. Fulman then generalized the n−1/4 bound to any Wi, in the
cases α = 1 and α = 2, using the representation-theoretical backgrounds for these
particular values of α, see [Ful08]. Some ideas from these papers are fundamental
here, as explained below.
The main novelty in Theorem 1.3 is of course the fact that our r esult holds for
any value of the parameter α. But, even in the cases α = 1 and α = 2, a bound for
the speed convergence of a vector of random variables and notonly for real-valued
random variables seems to be new.
Remark. We are not able to describe the ﬂuctuations of Jack character θ(α)
ρ when
ρ is not a hook. This is discussed in Subsection 7.7.

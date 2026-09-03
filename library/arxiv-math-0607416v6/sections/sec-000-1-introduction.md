---
doc_id: arxiv-math-0607416v6
doc_title: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0607416v6.pdf
source_sha256: 0705075947ce4a3d
doc_brief: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES — W e characterize all linear operators on ﬁnite or inﬁnite-di mensio- nal polynomial spaces that preserve the property of having"
---
Some of the main challenges in the theory of distribution of zeros of p olynomials
and transcendental entire functions concern the description of linear operators that
preserve certain prescribed (“good”) properties. Notwithstan ding their fundamen-
tal character, most of these problems are in fact still open as the y turn out to be
surprisingly diﬃcult in full generality. Two outstanding questions amo ng these are
the following: let Ω ⊆ C be an appropriate set of interest and denote by π(Ω) the
class of all (complex or real) univariate polynomials whose zeros lie in Ω.
Problem 1. Characterize all linear transformations T : π(Ω) → π(Ω) ∪ {0}.
Let πn be the vector space (over C or R) of all polynomials of degree at most
n and denote by πn(Ω) the subclass of π(Ω) consisting of polynomials of degree at
most n. The ﬁnite degree analog of Problem 1 is as follows.
Problem 2. Describe all linear operators T : πn(Ω) → π(Ω) ∪ {0} for n ∈ N.
These problems were stated in precisely this general form in [12, 16 ] (see also
[5], [38, pp. 182–183]) thereby encompassing essentially all similar que stions or
variations thereof scattered throughout the literature. Proble ms 1–2 originate from
the works of Laguerre [26] and P´ olya-Schur [36] and have been open for all but trivial
choices of Ω, including such important cases when Ω = R or Ω is a half-plane. In
this paper we completely solve Problems 1–2 in arguably the most relev ant cases,
namely all closed circular domains (iii)–(v) and their boundaries (i)–(ii) :
(i) Ω is a line,
(ii) Ω is a circle,
(iii) Ω is a closed half-plane,
(iv) Ω is a closed disk,
(v) Ω is the complement of an open disk.
2000 Mathematics Subject Classiﬁcation. Primary 47B38; Secondary 26C10, 30C15, 32A60.
Key words and phrases. Linear operators on polynomial spaces, zeros of entire func tions, cir-
cular domains, hyperbolicity and stability preservers, mu ltiplier sequences, Sz´ asz principle.
1
2 J. BORCEA AND P. BR ¨AND ´EN
Despite their long history only relatively few results pertaining to Pro blems 1–2
are known. As we note in the following (very brief) survey, these de al almost exclu-
sively with special types of linear transformations satisfying the re quired properties.
To prove the transcendental characterizations of linear preser vers of polynomials
whose zeros are located on a line or in a closed half-plane (Theorems 5 and 6) we
ﬁrst establish a result on uniform limits on compact sets of bivariate p olynomials
which are non-vanishing whenever both variables are in the upper ha lf-plane (The-
orem 12). Entire functions which are uniform limits on compact sets o f sequences
of univariate polynomials with only positive zeros were ﬁrst described by Laguerre
[26]. In the process he showed that if Q(z) is a real polynomial with all negative ze-
ros then T (π(R)) ⊆ π(R) ∪ {0}, where T : R[z] → R[z] is the linear operator deﬁned
by T (zk) = Q(k)zk, k ∈ N. Laguerre also stated without proof the correct result
for uniform limits of polynomials with all real zeros. The class of entire functions
thus obtained – the so-called Laguerre-P´ olya class – was subsequently characterized
by P´ olya [35]. A more complete investigation of sequences of such po lynomials was
carried out in [29]. This also led to the description of entire functions o btained as
uniform limits on compact sets of sequences of univariate polynomials all whose
zeros lie in a given closed half-plane [28, 31, 41] as well as the descript ion of en-
tire functions in two variables obtained as limits, uniformly on compact sets, of
sequences of bivariate polynomials which are non-vanishing when bot h variables
are in a given open half-plane [28].
The Laguerre-P´ olya class has ever since played a signiﬁcant role in t he theory of
entire functions [15, 28]. It was for instance a key ingredient in P´ oly a and Schur’s
(transcendental) characterization of multiplier sequences of the ﬁrst kind [36], see
Theorem 1 below. The latter are linear transformations T on R[z] that are diag-
onal in the standard monomial basis of R[z] and satisfy T (π(R)) ⊆ π(R) ∪ {0}.
P´ olya-Schur’s seminal paper generated a vast literature on this t opic and related
subjects at the interface between analysis, operator theory an d algebra but a solu-
tion to Problem 1 in the case Ω = R has so far remained elusive (cf. [12]). Among
the most noticeable progress in this direction we should mention Theo rem 17 of
[28, Chap. IX], where Levin describes a certain class of “regular” line ar operators
acting on the closure of the set of polynomials in one variable which hav e all zeros
in the closed upper half-plane. However, Levin’s theorem actually us es rather re-
strictive assumptions and seems in fact to rely on additional (albeit n ot explicitly
stated) non-degeneracy conditions for the transformations inv olved. Indeed, one
can easily produce counterexamples to Levin’s result by considering linear opera-
tors such as the ones described in Corollary 2 (a) of this paper. In [1 3] Craven
and Csordas established an analog of the P´ olya-Schur theorem fo r multiplier se-
quences in ﬁnite degree thus solving Problem 2 for Ω = R in the special case of
diagonal operators. Unipotent upper triangular linear operators T on R[z] satisfy-
ing T (π(R)) ⊆ π(R) ∪ {0} were described in [10]. Quite recently, in [3] the authors
solved Problem 1 for Ω = R and obtained multivariate extensions for a large class
of linear transformations, namely all ﬁnite order linear diﬀerential o perators with
polynomial coeﬃcients. Further partial progress towards a solut ion to Problem 1
for Ω = R is preliminarily reported in [17] although the same kind of remarks as in
the case of Levin’s theorem apply here. Namely, the results of op. cit. are valid only
in the presence of extra non-degeneracy or continuity assumptio ns for the operators
under consideration. Various other special cases of Problem 1 for Ω = R have been
P ´OLYA-SCHUR MASTER THEOREMS 3
considered in [1, 7, 8, 22, 23, 24]. Finally, we should mention that to th e best of
our knowledge Problems 1–2 have so far been widely open in cases (ii)– (v).
To begin with, in §2.1 and §3.1–§3.2 we solve Problems 1–2 for Ω = R and
Ω = {z ∈ C : Im(z) ≤ 0} and thus obtain complete algebraic and transcendental
characterizations of linear operators that preserve hyperbolicit y and stability, re-
spectively. In order to deal with Problems 1–2 for all closed circular domains and
their boundaries we are naturally led to considering a third classiﬁcat ion problem,
namely the following more general version of Problem 2.
Problem 3. Let n ∈ N and Ω ⊂ C. Describe all linear operators
T : πn(Ω) \ πn−1(Ω) → π(Ω) ∪ {0}.
As we explain in §2.2, Problems 2 and 3 are equivalent for closed unbounded sets
but for closed bounded sets the latter problem is more natural and actually turns
out to be a crucial step in solving Problems 1–2 for closed discs. In §2.2 and §3.3
we fully answer Problem 3 for any closed circular domain or the bounda ry of such
a domain and as a consequence we get complete solutions to Problems 1–2 in all
cases ((i)–(v)) listed above.
On the one hand, these results accomplish the classiﬁcation progra m originat-
ing from the works of Laguerre and P´ olya-Schur that we brieﬂy ou tlined in this
introduction. On the other hand, they seem to have numerous app lications ranging
from entire function theory and operator theory to real algebra ic geometry, matrix
theory and combinatorics. Some of these will make the object of fo rthcoming pub-
lications. The paper concludes with several remarks on related ope n problems and
potential further developments ( §4).

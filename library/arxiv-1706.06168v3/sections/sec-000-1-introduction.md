---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
---
In 1914, P´ olya and Schur [ PS14] characterized the set of diagonal linear operators on polynomials which
preserve real-rootedness. Since this seminal paper, much work h as been done in extending this character-
ization to other classes of linear operators. This program in essenc e came to a close in 2009 with a paper
of Borcea and Br¨ and´ en [BB09a], which gave a complete characterization of linear operators on poly nomials
which preserve real-rootedness.
Their real-rootedness preservation characterization is derived f rom a more general result pertaining to
stable polynomials. Given Ω ⊂ Cm, we say that a polynomial f ∈ C[x1,...,x m] is Ω -stable if f does not
vanish in Ω. Further, f is real stable if it has real coeﬃcients and is Hm
+ -stable, where H+ ⊂ C is the
open upper half-plane. (We also denote the open lower half-plane by H− ⊂ C.) We additionally use the
terms weakly Ω-stable and weakly real stable if we allow f ≡ 0. Finally, we write f ∈ Cλ[x1,...,x m] for
λ ≡ (λ1,...,λ m) if f is of degree at most λk inxk. We are then led to the following problems for K ∈ {C, R},
generalized from the P´ olya-Schur characterization:
Problem 1. Characterize linear operators T : Kλ[x1,...,x m] → K[x1,...,x m] preserving weak Ω-stability.
Problem 2. Characterize linear operators T : K[x1,...,x m] → K[x1,...,x m] preserving weak Ω-stability.
In [ BB09a], Borcea and Br¨ and´ en were able to solve these problems in many ca ses. In particular, they
solved both problems for K = R and Ω = Hm
+ , where m = 1 corresponds to the case of preservation of
real-rooted polynomials. For K = C, they were able to solve Problem 1 for Ω that is any product of open
circular regions in C.
In this paper we will only be concerned with Problem 1, for which we now state the solution from [ BB09a].
Given a linear operator T : Kλ[x1,...,x m] → K[x1,...,x m], a polynomial Symb BB (T ) called the (Borcea-
Br¨ and´ en) symbolis associated to T . Speciﬁcally, the symbol is a polynomial in Kλ⊔λ[x1,...,x m,z 1,...,z m]
(i.e., of 2 m variables), where λ ⊔λ := (λ1,...,λ m,λ 1,...,λ m). The crucial feature of the symbol is that
it shares certain stability properties with its associated linear opera tor, which yields the characterizations
stated in the following results. (We will express these results in more detail in §6 and §7.)
1
Theorem 1.1 (Borcea-Br¨ and´ en). Fix a linear operator T : Cλ[x1,...,x m] → C[x1,...,x m] which has image
of dimension greater than one. Then, T maps Hm
+ -stable polynomials to weakly Hm
+ -stable polynomials if
and only if SymbBB (T ) is H2m
+ -stable.
Theorem 1.2 (Borcea-Br¨ and´ en). Fix a linear operator T : Rλ[x1,...,x m] → R[x1,...,x m] which has image
of dimension greater than two. Then, T maps real stable polynomials to weakly real stable polynomi als if and
only if either SymbBB (T ) or SymbBB (T −) is real stable, where T −(p) := T (p(−x1,..., −xm)).
To deal with other products of circular regions, one then conjuga tesT by certain M¨ obius transformations
and applies Theorem 1.1 to the conjugated operator. Unfortunately though, this is a ted ious process which
has to be done each time a new stability region is to be considered. Add itionally, the image dimension
restrictions give rise to degeneracy cases which have to be dealt wit h separately. Both of these issues obscure
the connection between an operator and its symbol.
In this paper, we present a new conceptual approach to the Borc ea-Br¨ and´ en characterization via the
representation theory of SL 2(C). In particular, we derive a new symbol (denoted Symb) in a natura l way,
and our deﬁnition eliminates the issues discussed above. This is seen in the following results, which are
our simpliﬁed and generalized versions of the Borcea-Br¨ and´ en characterizations. Note that for the sake of
simplicity, we have omitted a few details here regarding non-convex c ircular regions. Speciﬁcally, circular
regions of C should be thought of as lying in the Riemann sphere, so that compleme nts of discs contain the
point at ∞.
Theorem 6.2. Fix a linear operator T : Cλ[x1,...,x m] → Cα[x1,...,x l], a product of all open or all
closed circular regions Ω 0 = C1 × · · · × Cm, and a product of sets Ω 1 := S1 × · · · × Sm. Further, denote
~Ω 0 := ( C \C1) × · · · × (C \Cm). Up to certain degree and convexity (of Ck) restrictions, we have that T
maps Ω 0-stable polynomials to nonzero Ω 1-stable polynomials if and only if Symb(T ) is (~Ω 0 × Ω 1)-stable.
Theorem 7.2. Fix a linear operator T : Rλ[x1,...,x m] → Rα[x1,...,x l]. Up to certain degree restrictions,
T maps real stable polynomials to nonzero real stable polynom ials if and only if Symb(T ) is either (H−
m
×
Hl
+)-stable or (H−
m
× Hl
−)-stable.
We summarize the speciﬁc improvements that this and our other rela ted results give over the Borcea-
Br¨ and´ en characterization as follows.
1. Diﬀerent stability regions can be considered using the same symbol. The symbol we deﬁne in this
paper is universal: for example, it gives stability-preservation infor mation for any product of open
circular regions. The Borcea-Br¨ and´ en symbol, on the other hand, required the application of M¨ obius
transformations. In addition, our symbol also allows for the outpu t stability region to be chosen
independently of the input stability region. While this does not literally im prove the result, it does
allow for quicker computations. In particular, see Examples 6.3 and 6.4 where classical polynomial
convolution results are easily derived from our framework.
2. Our characterization does not require any degeneracy condi tion. Our results characterize operators
which preserve (strong) stability rather than weak stability. As se en above, this slightly stronger
notion of stability enables us to eliminate any image dimension degenera cy condition, as required
in the Borcea-Br¨ and´ en characterizations (Theorems1.1 and 1.2). This demonstrates a cleaner link
between an operator and its symbol.
3. Closed circular regions and projectively convex regions ca n be considered. The symbol we deﬁne in this
paper handles products of open circular regions, as well as produc ts of closed circular regions. (In
[Mel15], Melamud proves a result similar to the Borcea-Br¨ and´ en charact erization for closed circular
regions.) Further, we are also able to consider more general projectively convex regions (circular regions
with portions of their boundary; also called generalized circular regions , see [ Zer60] and [ Zah76]) in
Proposition 6.5. This allows us to determine stability-preservation information abou t real intervals
and half-lines. It also turns out, somewhat surprisingly, that our s ymbol can handle products of any
sets as possible output space stability regions (as seen in Theorem 6.2 above).
2
In the process of generalizing the Borcea-Br¨ and´ en characterization we develop a general algebraic frame-
work which also encompasses many of the classical polynomial tools. This framework aims to motivate
classical results and provide intuition for the connection between a stability preserving operator and its
symbol.
The Main Idea
A major purpose of this paper is to explain a certain conceptual thr ead in the history of polynomial stability
theory: that it is often possible to determine general stability infor mation from restricted sets of polynomials.
For example, the P´ olya-Schur and Borcea-Br¨ and´ en characterizations derive from a single polynomial (i.e.,
the symbol) stability properties of a whole collection of polynomials in th e output of a given linear operator.
Additionally, the Grace-Walsh-Szeg˝ o coincidence theorem says that stability information of any polynomial
can be determined from its polarization, which is of degree at most on e in each variable.
As it turns out, these sorts of phenomena can be explained using re latively basic algebraic and represen-
tation theoretic concepts. We view Cn[x] as a representation of SL 2(C) via the standard action, given as
follows. For φ ∈ SL2(C) and f ∈ Cn[x], we deﬁne:
(φ ·f )(x) := f (φ−1x)
Here φ−1 acts on x ∈ C as a M¨ obius transformation, or equivalently φ acts on the roots of f . (Similarly,
Cλ[x1,...,x m] can be viewed as a representation of (SL 2(C))m via this action in each variable.) Under this
interpretation, important maps like polarization, projection, the a polarity form, and even the symbol turn
out to be invariant under these SL 2(C) actions. This leads us to a conceptual thesis: SL 2(C)-invariant maps
transfer stability information .
The goal of this paper is then to explicate and answer the most impor tant question related to this thesis:
what does it mean for the symbol map to be SL 2(C)-invariant and how does it transfer stability information?
To answer this, we consider the following standard ideas relating spa ces of linear operators to tensor products.
Let W1,W 2 be two ﬁnite dimensional representations of a group G, and let Hom( W1,W 2) denote the
space of linear maps from W1 to W2. Then, Hom( W1,W 2) ∼= W ∗
1 ⊠W2 (the outer tensor product) can
viewed as a representation of G ×G. If we further have a G-invariant bilinear form on W1, then we also
haveW1 ∼=W ∗
1 . This leads to the following identiﬁcation:
Hom(W1,W 2) ∼=W ∗
1 ⊠W2 ∼=W1 ⊠W2
IfW1 andW2 are spaces of polynomials, each in m variables, then their tensor product W1 ⊠W2 is isomorphic
to a larger space of polynomials in 2 m variables. That is, a linear operator between polynomial spaces
W1 and W2 can be associated to some polynomial in double the variables, via the a bove identiﬁcation of
representations. This is precisely the idea of the symbol of an oper ator.
Let’s see how this works in the univariate case. Consider Cn[x] as a representation of the group SL 2(C),
as described above. It is then a standard result that the classical bilinear apolarity form is invariant under
the action of M¨ obius transformations. That is, the apolarity form is an SL 2(C)-invariant bilinear form on
Cn[x]. This form, applied to f,g ∈ Cn[x] with coeﬃcients fk,g k, is deﬁned as follows:
⟨f,g ⟩n :=
n∑
k=0
( n
k
) −1
(−1)kfkgn−k
With this, we obtain the identiﬁcation described above: Hom( Cn[x], Cm[x]) ∼= Cn[x] ⊠ Cm[x] ∼= C(n,m)[x,z ].
The ﬁnal piece of the puzzle is then to ﬁnd a way to transfer stability information through this identiﬁcation
of representations. The key result to this end is the classical Grac e’s theorem:
Theorem ([Gra02]). Let f,g ∈ Cn[x] be polynomials of degree exactly n. Further, let C be some open or
closed circular region such that f is C-stable and g is (C \C)-stable. Then, ⟨f,g ⟩n ⁄= 0.
3
That is, the apolarity form not only provides the link between a linear o perator and its symbol, but also
captures stability information. So, whatever stability claims we can m ake about polynomials in C(n,m)[x,z ]
can then be seamlessly transferred to corresponding linear opera tors in Hom( Cn[x], Cm[x]). From this we are
able to recover the Borcea-Br¨ and´ en characterization. Additionally, all of the theory here relating stability
and the representation theory of SL 2(C) can be generalized to multivariate polynomials in a straightforward
manner. The details will be discussed in §3.
In a similar fashion, other important maps also have SL 2(C)-invariance properties (e.g., polarization and
projection, as used in the Grace-Walsh-Szeg˝ o coincidence theor em, explicitly give the isomorphisms of a
classical representation theoretic result; see Appendix B). A main feature of our conceptual thesis is that it
allows for a uniﬁcation of many seemingly related results in polynomial s tability theory. A crucial point to
make then is that Grace’s theorem is at the heart of this uniﬁcation. That said, a signiﬁcant portion of this
paper is devoted to discussing it.
A Generalized Grace’s Theorem and Interval- and Ray-Rooted ness
In [ BB09b], Borcea and Br¨ and´ en are able to prove a multivariate Grace’s the orem using their operator
characterization. In this paper we will prove the multivariate versio n from scratch, and then use it to derive
a new characterization of stability-preserving linear operators. I n addition, we generalize it to projectively
convex regions, which consist of an open circular region with a portion of its b oundary (see §4.2). We state
our new result as follows. Note that this result can be seen as an ext ension of the generalized Grace’s theorem
given in Corollary 4.4 of [ Zah76].
Theorem 5.1. Fix λ ∈ Nm
0 and f,g ∈ Cλ[x1,...,x m] such that f and g both have a nonzero term of degree
λ. Also, denote C := H+ ∪ R+ and ~C := H− ∪ R−. If f is Cm-stable and g is ~Cm-stable, then ⟨f,g ⟩λ ⁄= 0.
This result can, for instance, give stability information about positiv e- and negative-rooted polynomials.
Since the apolarity form is invariant under the action of M¨ obius tran sformations, we immediately obtain
similar statements regarding the union of any open circular region an d a portion of its boundary. Notice
also that, unlike the classical Grace’s theorem, the stability regions C and ~C have non-empty intersection.
In the vein of this extension, we provide a new characterization of a certain class of linear operators
which preserve ray- and interval-rootedness. The problem of clas sifying all such operators is still open in
general (see e.g., the end of [ BB09c]). Here, we solve this problem for a restricted class of operators: namely,
operators which both preserve weak real-rootedness and also pr eserve ray- or interval-rootedness. Our main
result in this direction is stated as follows, where a polynomial is called J-rooted when all of its roots are in
J:
Theorem 7.8. Fix a linear operator T : Rn[x] → Rm[x] which has image of dimension greater than two.
Further, let I,J ⊆ R be intervals or rays. Up to certain degree restrictions, T preserves weak real-rootedness
and maps I-rooted polynomials to nonzero J-rooted polynomials if and only if Symb(T ) is either (H− ∪I) ×
(H+ \J)-stable or (H− ∪I) × (H− \J)-stable.
In §7.4, this result is stated in a more restricted manner as the degenerac y condition (image dimension)
and degree restrictions end up being more tedious than in the other results. Corollary 7.9 and further
explication then give the result as stated here.
As a ﬁnal note, all of the results given here in the introduction are s tated slightly diﬀerently in §5, §6,

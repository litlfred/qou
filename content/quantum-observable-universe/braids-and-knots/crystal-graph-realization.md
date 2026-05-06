**Conjecture (crystal-graph realisation of Hecke normal forms).**
*Let $K$ be a closed braid with
[Hecke normal form](#def:hecke-normal-form) $T_w \in H_n(R, q)$.
Under the Brundan–Kleshchev isomorphism
\cite{brundankleshchev2009} between $H_n(R, q)$ and the cyclotomic
quotient of the corresponding KLR algebra, the Gröbner–Shirshov
canonical basis element $T_w$ corresponds to an indecomposable
graded projective KLR module, and the latter is a highest-weight
vector of the Kashiwara crystal $\mathrm{Cryst}(\mathfrak{sl}_n)$
\cite{kashiwara1991}: it satisfies $\tilde e_i \cdot T_w = 0$ for
every Kashiwara raising operator $\tilde e_i$.*

**Computational shortcut.**
*Consequently the GS reduction engine that computes $T_w$ from a
braid word may be replaced by a directed traversal on the crystal
graph: starting from the input word and applying $\tilde e_i$
operators recursively, the procedure terminates at $T_w$.  Because
the relevant component of $\mathrm{Cryst}(\mathfrak{sl}_n)$ is
finite, termination is immediate; no Diamond-Lemma S-polynomial
overlap analysis is required.  The plactic-monoid bridge of
Lecouvey \cite{lecouvey2007} certifies that the GS irreducible
forms and crystal highest-weight vertices are in bijection.*

**Why a conjecture and not a theorem.**
*The literature establishes the Brundan–Kleshchev isomorphism and
the GS↔crystal bijection at the level of generic Hecke and KLR
algebras.  What remains conjectural in this manuscript is that the
**specific** GS reduction order used here
([Hecke normal form](#def:hecke-normal-form), shortlex on the
Yang–Baxter generators) is precisely the order whose irreducible
forms match the canonical basis labels under Brundan–Kleshchev for
the QOU knot/particle ansatz.  The match is verified empirically
on the witnessed normal forms; a rigorous proof requires
formalising the GS reduction order inside the KLR diagrammatic
calculus.*

**Status.**
*Used by [confinement–grading correspondence](#conj:confinement-grading-correspondence)
to upgrade the heuristic confinement filtration to a $\mathbb{Z}$-graded
KLR shift, and by
[cemetery-group emergence](#conj:cemetery-group-emergence) to
explain the GS engine's homological pruning.  No new $\mathrm{sorry}$
is introduced in Lean: the conjecture replaces a class of brute-force
S-polynomial bounds rather than an existing proof.*

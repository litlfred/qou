## Statement

**Theorem (conditional on [`conj:klr-categorification`](#conj:klr-categorification)).**
*Let $H_n(q)$ be the Iwahori–Hecke algebra of type $A_{n-1}$ with
substrate parameter $q$, and let $R_n^\Lambda$ be the cyclotomic
quotient of the Khovanov–Lauda–Rouquier (KLR) algebra of type
$A_\infty$ at level $\Lambda$. Assume the **Brundan–Kleshchev
isomorphism**:*

$$
  R_n^\Lambda \;\cong\; H_n^\Lambda(q)
$$

*as $\mathbb{Z}$-graded algebras (Brundan–Kleshchev 2009).*

*Let $\mathcal{C}_n$ denote the category of finitely generated graded
projective $R_n^\Lambda$-modules, with split Grothendieck group
$K_0(\mathcal{C}_n)$ that decategorifies via*

$$
  K_0\!\left(\bigoplus_{n \geq 0} \mathcal{C}_n\right) \;\cong\;
  \mathbf{f}^- \;\subset\; U_q^-(\widehat{\mathfrak{sl}}_e)
$$

*(the negative half of the quantum affine algebra; Khovanov–Lauda 2009,
Lusztig 1990).*

*Then for every multi-particle knot configuration $K$ encoded as a
braid word $\beta \in B_n$ with closure carrying canonical mass-formula
data, the unique **stable algebraic normal form** for $K$ — the
ansatz output before Markov-trace reduction — corresponds to a
**highest-weight vector** in $\mathcal{C}_n$ under the Kashiwara
crystal operators $\tilde e_i$:*

$$
  \widehat{\beta}_{\mathrm{stable}} \in \mathcal{C}_n
    \quad \text{satisfies} \quad
    \tilde e_i \, \widehat{\beta}_{\mathrm{stable}} = 0 \quad \text{for all $i$.}
$$

*Equivalently, $\widehat{\beta}_{\mathrm{stable}}$ is an
**indecomposable graded projective KLR module**, and its image in
$K_0(\mathcal{C}_n)$ is the corresponding **Lusztig canonical basis
element** (equivalently, **Kashiwara global crystal basis element**).*

## Consequence — Gröbner–Shirshov ↔ crystal-graph traversal

The Gröbner–Shirshov reduction engine for the substrate-derived
mass formula does **not** need to resolve $S$-polynomial overlaps
(the Diamond Lemma path). It instead executes a **crystal-graph
traversal**:

1. **Input** an ansatz word $w$ for the multi-particle knot $K$.
2. **Filter** by KLR $\mathbb{Z}$-grading bound (the confinement
   level; see [`prop:confinement-as-z-grading`](#prop:confinement-as-z-grading)).
3. **Apply** $\tilde e_i$ recursively. Termination at a highest-weight
   vector is guaranteed because the crystal graph is finite.
4. **Prune** any branch that enters the $\omega$-annihilated
   subcategory (cemetery group; see
   [`prop:cemetery-as-annihilated-subcategory`](#prop:cemetery-as-annihilated-subcategory)).
5. **Output** the canonical-basis element associated to the terminal
   vertex.

This replaces the term-rewriting search-space (factorial in the
braid length) with a **directed graph traversal** whose terminal
states are precisely the canonical bases. Convergence is automatic
by the finiteness of $\mathcal{C}_n$.

## Proof (conditional on the KLR-categorification class)

**Step 1 — Brundan–Kleshchev gives $H_n^\Lambda \cong R_n^\Lambda$.**
The class instance $\textsf{KLRCategorification}_n$ supplies a graded
algebra isomorphism $\Phi_n : R_n^\Lambda \xrightarrow{\sim} H_n^\Lambda(q)$
(field `klr_to_hecke_iso`). This is the Brundan–Kleshchev theorem
held as a class hypothesis.

**Step 2 — categorified module category.** The class fixes an
abelian category $\mathcal{C}_n$ of f.g.\ graded projective
$R_n^\Lambda$-modules and a split Grothendieck-group isomorphism

$$
  K_0(\mathcal{C}_n) \otimes_\mathbb{Z} \mathbb{Z}[v, v^{-1}]
   \;\xrightarrow{\sim}\;
   \mathbf{f}^-_n
$$

(field `decategorification`).

**Step 3 — crystal operators.** The class supplies $\tilde e_i,
\tilde f_i : \mathcal{C}_n \to \mathcal{C}_{n \pm 1}$ with the
Kashiwara axioms (field `crystal_operators`):

* $\tilde f_i \circ \tilde e_i = \mathrm{id}$ on the locus where
  $\tilde e_i$ is non-zero,
* the underlying graph is the crystal graph of $\mathbf{f}^-$.

**Step 4 — the stable normal form is a highest-weight vector.**
Given $\widehat{\beta}_{\mathrm{stable}}$ as the output of the
ansatz, recursive application of $\tilde e_i$ terminates because
each step strictly decreases either the rank of the underlying
KLR module or the $\mathbb{Z}$-grading degree. By the finiteness
of the crystal graph (Kashiwara 1991), termination is at a vertex
$v$ with $\tilde e_i v = 0$ for all $i$. By Step 2, $v$ is an
indecomposable graded projective module — i.e., a canonical-basis
element.

**Step 5 — uniqueness.** The canonical basis is unique up to scalar
(Lusztig 1990, Kashiwara 1991), so the terminal vertex is unique
modulo equivalence. The ansatz's stable normal form is therefore
canonically determined.

$\square$

## Cross-references

* [`prop:markov-trace-axiomatic-closed-form`](#prop:markov-trace-axiomatic-closed-form)
  — the categorified object is what the closed-form anchors against
* [`prop:cemetery-as-annihilated-subcategory`](#prop:cemetery-as-annihilated-subcategory)
  — the kill-switch via $\omega$-kernel
* [`prop:confinement-as-z-grading`](#prop:confinement-as-z-grading)
  — the grading-bound filter
* [`conj:categorical-neutrality-saturated-shells`](#conj:categorical-neutrality-saturated-shells)
  — magic-shell highest-weights

## Computational verification

The crystal-traversal interpretation is consistent with the
existing canonical-form witness (`canonical-knot-id-sdp`) which
identifies indecomposable knot operators per atom — these are the
canonical-basis elements per this proposition's Step 4.

## References

* M. Khovanov, A. D. Lauda. *A diagrammatic approach to
  categorification of quantum groups I.* Representation Theory **13**
  (2009), 309–347.
* J. Brundan, A. Kleshchev. *Blocks of cyclotomic Hecke algebras and
  Khovanov–Lauda algebras.* Inventiones mathematicae **178**
  (2009), 451–484.
* M. Kashiwara. *On crystal bases of the q-analogue of universal
  enveloping algebras.* Duke Math. J. **63** (1991), 465–516.
* G. Lusztig. *Canonical bases arising from quantized enveloping
  algebras.* J. Amer. Math. Soc. **3** (1990), 447–498.

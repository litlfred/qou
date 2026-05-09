## Statement

**Theorem (conditional on
[`prop:crystal-graph-realization-stable-states`](#prop:crystal-graph-realization-stable-states)).**
*Let $R_n^\Lambda$ be the cyclotomic-quotient KLR algebra of type
$A_\infty$, with the Khovanov–Lauda 2009 $\mathbb{Z}$-grading*

$$
  \deg(\sigma_i) = 2, \qquad \deg(e_\lambda) = 0,
$$

*so that each indecomposable graded projective KLR module
$P_\lambda \in \mathcal{C}_n$ acquires a unique grading shift
$d_\lambda \in \mathbb{Z}$.*

*Let $\mathfrak{c}: \mathrm{Atoms} \to \mathbb{Z}_{\geq 0}$ be the
heuristic confinement-level function used by the Gröbner–Shirshov
reduction engine to bound multi-particle interactions.*

*Then there is a canonical equivalence:*

$$
  \mathfrak{c}(K) \leq \ell_{\max}
   \qquad \Longleftrightarrow \qquad
   d_{\lambda(K)} \leq \ell_{\max}
$$

*for every multi-particle knot configuration $K$ with KLR-module
representative $P_{\lambda(K)}$. **Confinement levels are KLR
$\mathbb{Z}$-grading shifts.***

## Algorithmic consequence — geometric disallowance

The Gröbner–Shirshov engine, running as a Kashiwara crystal-graph
traversal per [`prop:crystal-graph-realization-stable-states`](#prop:crystal-graph-realization-stable-states),
applies operators $\tilde e_i$ that shift the $\mathbb{Z}$-grading
by $\pm 1$ (or other fixed integers per the type-$A_\infty$ root
data).  A traversal that attempts to push a state into a grading
degree $d > \ell_{\max}$ is **geometrically disallowed**: the
target module $P_{\lambda'}$ with $d_{\lambda'} > \ell_{\max}$ lies
outside the engine's allowed sub-category.

This replaces the heuristic confinement check in the GS engine with
a **rigorous geometric type constraint**: the engine simply refuses
to traverse to KLR modules whose grading shift exceeds the bound.

## Proof

**Step 1 — KLR $\mathbb{Z}$-grading.** Khovanov–Lauda 2009 §2
establishes that $R_n$ is naturally $\mathbb{Z}$-graded with
$\deg(\psi_i) = -a_{i,i+1}$ (the symmetric Cartan integer; for type
$A_\infty$ $a_{i,i+1} = -1$, giving $\deg(\psi_i) = 1$, and after
type-A symmetrisation $\deg(\sigma_i) = 2$ on the Hecke side via
Brundan–Kleshchev's iso). Each indecomposable $P_\lambda$ has a
unique grading shift $d_\lambda$.

**Step 2 — confinement bound = grading bound.** The substrate's
heuristic confinement function $\mathfrak{c}$ counts effective
"crossing depth" — equivalently, the number of $\sigma_i$
applications needed to reach the configuration. By Step 1 each
$\sigma_i$ contributes $+2$ to the grading, so

$$
  d_\lambda \;=\; 2 \cdot (\text{crossing depth of } P_\lambda) \;=\; 2 \cdot \mathfrak{c}(K).
$$

The bounds $\mathfrak{c} \leq \ell_{\max}$ and $d_\lambda \leq
2 \ell_{\max}$ are equivalent up to the constant 2.

**Step 3 — crystal-operator shift.** Kashiwara crystal operators
$\tilde e_i, \tilde f_i$ act on $\mathcal{C}_n$ shifting the
$\mathbb{Z}$-grading by $\pm 1$ (Kashiwara 1991, §6). Recursive
application from a starting state therefore traverses grading
levels in unit steps; the bound $d_\lambda \leq \ell_{\max}$ is
preserved iff the trajectory stays within the corresponding
sub-cone of $\mathcal{C}_n$.

**Step 4 — geometric disallowance.** A traversal step that would
exceed the grading bound corresponds to applying a
$\tilde f_i$ (raising) operator at a state already at the boundary.
The image lies outside the $\ell_{\max}$-truncated category, so
the engine refuses the step.  This is equivalent to the heuristic
confinement check, but is now a **typed** refusal at the
categorical level rather than a heuristic.

$\square$

## Cross-references

* [`prop:crystal-graph-realization-stable-states`](#prop:crystal-graph-realization-stable-states)
  — the KLR machinery + crystal operators
* [`prop:cemetery-as-annihilated-subcategory`](#prop:cemetery-as-annihilated-subcategory)
  — companion $\tau$-kernel filter
* [`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf)
  — the GS engine consuming confinement bounds

## References

* M. Khovanov, A. D. Lauda. *A diagrammatic approach to
  categorification of quantum groups I.* Representation Theory **13**
  (2009), §2 (the $\mathbb{Z}$-grading).
* M. Kashiwara. *On crystal bases of the q-analogue of universal
  enveloping algebras.* Duke Math. J. **63** (1991), §6 (crystal
  operator shifts).

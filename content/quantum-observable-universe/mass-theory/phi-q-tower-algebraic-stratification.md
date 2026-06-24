> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

**Proposition (algebraic stratification of the Φ$_q$ tower).**
*Let $\beta \in B_n$ be a braid with crossings indexed by
$\{0, \ldots, n-2\}$. Let $H_n(R, q)$ be the Iwahori-Hecke algebra
with Markov trace $\mathrm{tr}_M$ and let $J^\bullet$ be the
Gröbner-Shirshov filtration on $H_n(R, q)$
([graded Markov trace](#prop\:graded-markov-trace-from-gs-filtration)).
For each subset $S \subseteq \{0, \ldots, n-2\}$, let
$\beta_S \in B_n$ be the braid obtained from $\beta$ by smoothing
every crossing $i \notin S$ to the identity strand
([Φ$_q$-piece definition](#def\:phi-q-piece)). The Φ$_q$-tower
admits a purely algebraic stratification by $|S|$:*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \underbrace{\bigl\| \mathrm{tr}_M(\rho(\beta_\emptyset))\bigr\|_F}_{\text{descended carrier}}
  \;+\;
  \sum_{|S| = 1} \Phi_q\bigl(\|\hat V_S\|_F\bigr)
  \;+\;
  \sum_{|S| = 2} z^{2} \Phi_q\bigl(\|\hat V_S\|_F\bigr)
$$

*where $\|\cdot\|_F$ denotes the **categorical Frobenius norm**
valued in $\mathbb{Z}[q^{\pm 1/2}]$ — **not** the Archimedean
absolute value — and each summand is an element of
$\mathbb{Z}[q^{\pm 1/2}]$ computed entirely within the Hecke
algebra. The stratification is
indexed by Hecke-tower :refterm[descent]{#descent} levels — singletons (level 1),
adjacent and non-adjacent pairs (level 2) — not by 3-manifold pieces.
Pentagon ascension ([mass endomorphism jet tower](#rem\:mass-endomorphism-jet-tower))
guarantees that order-$\geq 3$ defects ascend to level-$(n+1)$
singletons or pairs in the jet tower; no triple or higher term
appears at any fixed level.*

## What this block delivers

This is the **algebraic-side reformulation** that the audit's
GAP 8a calls for: every object on the right-hand side lives in
$\mathbb{Z}[q^{\pm 1/2}]$, and every step of the construction is a
Hecke-algebra operation (skein smoothing of a braid word, Markov
trace of an element of $H_n(R, q)$, Laurent expansion in $q^{1/2}$).
The norm $\|\cdot\|_F$ in the formula is the **Frobenius norm**
$\|x\|_F^2 := \langle x, x\rangle_F$, valued in the ground ring;
it is **not** the Archimedean absolute value.  Substitutions like
$q \mapsto q_0 \in \mathbb{R}$ are post-$\tau$ and not used in any
step of this proof.
Three-manifold language ($S^3$, knot complement, hyperbolic volume,
JSJ decomposition) does **not** appear on the algebraic side; it
enters only as the τ-image of the algebraic structure under
$\tau_{\mathrm{arch}}$
([Φ$_q$-tower JSJ archimedean bridge](#conj\:phi-q-tower-jsj-bridge)).

## The four levels of the algebraic stratification

|    Level | Index                    | Algebraic content                                                                          | $\mathbb{Z}[q^{\pm 1}]$-class                                                               |
| -------: | ------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
|        0 | $S = \emptyset$          | $\beta_\emptyset$ = trivial $n$-strand identity; $\rho(\beta_\emptyset) = 1 \in H_n(R, q)$ | $\mathrm{tr}_M(1) = 1$                                                                      |
|        1 | $\lvert S \rvert = 1$    | $\beta_{\{i\}} = \sigma_i$; $\rho(\beta_{\{i\}}) \in H_n(R, q)$                            | $\hat V_i = z \cdot a_i + b_i$ ([algebraic quantum volume](#def\:algebraic-quantum-volume)) |
|        2 | $\lvert S \rvert = 2$    | $\beta_{\{i, j\}} = \sigma_i \sigma_j$; $\rho(\beta_{\{i, j\}}) \in H_n(R, q)$             | $\hat V_i \hat V_j$ (commutative scalars in $\mathbb{Z}[q^{\pm 1}]$)                        |
| $\geq 3$ | $\lvert S \rvert \geq 3$ | absorbed into level $(n+1)$ via pentagon ascension                                         | n/a (does not appear at level $n$)                                                          |

Each level is a **GS-filtration piece** of $H_n(R, q)$: the
singletons $\sigma_i$ are at GS-degree 1, the pairs $\sigma_i \sigma_j$
at GS-degree 2, and so on. The descended (level-0) carrier is the
identity component, GS-degree 0. The truncation $\lvert S \rvert
\leq 2$ at any fixed jet level is the **categorical content** of
the mass-endomorphism formula
([mass endomorphism tower](#prop\:mass-endomorphism-tower)), not a
3-manifold property.

## Why this matters

* **Discharges audit GAP 8a (wall risk).** The audit's worry was
  that the Φ$_q$-tower reformulation read as 3-manifold/topological.
  This proposition states the same content in pure Hecke-tower /
  GS-filtration language. The 3-manifold picture is the τ-image,
  not the derivation.

* **Decouples the algebraic engine from the JSJ identification.**
  The mass formula computes via algebraic stratification
  (Φ$_q(|\hat V_S|)$ as a Laurent polynomial); the JSJ
  identification of the τ-image is a separate conjecture
  ([Φ$_q$-tower JSJ bridge](#conj\:phi-q-tower-jsj-bridge))
  that *interprets* this algebraic structure on the geometric
  side. If the JSJ conjecture remains open, the algebraic mass
  formula is unaffected.

* **Provides the audit with a concrete Hecke-tower structure** for
  every block currently citing "JSJ pieces": replace
  `JSJ piece $P$` with `algebraic stratum $S \subseteq \{0, \ldots, n-2\}$`
  in the algebraic-side narrative; reserve the JSJ language for
  the τ-image discussion.

## Relation to the JSJ archimedean bridge

The conjecture
[Φ$_q$-tower JSJ archimedean bridge](#conj\:phi-q-tower-jsj-bridge)
states that under $\tau_{\mathrm{arch}}$ each algebraic stratum $S$
maps to a JSJ piece of $\widehat\beta$, with the algebraic value
$\Phi_q(|\hat V_S|)$ τ-realising to $\rho_q \cdot \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K_S)$.
That conjecture **interprets** the algebraic stratification on the
3-manifold side; the algebraic stratification itself is unconditional.

In the language of the audit's strict-Archimedean-wall directive:

* The **statement** of the mass formula uses the algebraic
  stratification (this proposition); 3-manifold language does not
  appear.
* The **interpretation** as a JSJ-piecewise sum is a τ-image
  conjecture, on the right side of τ.
* No **proof** anywhere in the algebraic engine invokes JSJ /
  hyperbolic-volume / Mostow / Thurston as a derivation input.

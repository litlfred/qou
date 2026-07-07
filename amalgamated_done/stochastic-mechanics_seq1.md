<!-- FILE_START: intro-markov-axioms-braid-link.md -->
Markov's theorem states that two braid words have isotopic closures iff they differ by a finite sequence of conjugation and stabilisation moves. This section promotes Markov's theorem to a categorical setting. We fix the precision ladder that controls the substrate-level Markov trace and enumerate the braid-link bijection that drives the counting arguments.

The first blocks establish the $q$-deformed categorical precision ladder and prove its compatibility with the Markov axioms. The middle blocks enumerate the closure types (knot, link, mutually disjoint) and record the substrate-level character of each. The closing blocks specialise to the small-$n$ cases that drive the explicit binding-energy formulas, including cases where the Markov-trace ambiguity propagates and must be resolved by parity classification downstream.

The output is the categorical braid-link enumeration with explicit substrate-trace evaluations. This is the combinatorial engine. Every closed-form prediction below relies on knowing both the count and the trace value for each braid-link equivalence class.
<!-- FILE_END: intro-markov-axioms-braid-link.md -->

<!-- FILE_START: polynomial-bar-involution.md -->
**Proposition (polynomial bar-involution).**

*Let $R$ be a commutative ring and $R[X]$ its polynomial ring in one indeterminate. The map*

$$
\overline{(\cdot)} \colon R[X] \to R[X], \qquad p(X) \mapsto p(-X)
$$

*is a ring involution. Under this bar:*

- *the indeterminate $X$ is **bar-anti-symmetric** ($\overline X = -X$);*
- *every constant $c \in R \hookrightarrow R[X]$ is **bar-symmetric**;*
- *every even-degree monomial $X^{2n}$ is **bar-symmetric**;*
- *every odd-degree monomial $X^{2n+1}$ is **bar-anti-symmetric**;*
- *the bar-symmetric subring is exactly $R[X^2]$.*

## Categorical role

This is the canonical non-trivial bar-involution in QOU. It provides a concrete categorical setting where the polynomial indeterminate $X$ plays the role of the bar-anti-symmetric Hecke skein

$$h \;=\; q - q^{-1},$$

with the correct bar-action $h \mapsto -h$ matching the general definition ([`def:bar-involution`](#def:bar-involution)).

We work in $R[X]$ rather than directly with the Hecke skein for three reasons. First, algebraic decidability: `Polynomial.comp` lemmas give the four ring-involution axioms for free. Second, no analysis is needed: unlike $\mathbb{C}$ with conjugation, the bar map is defined by formal substitution. Third, concrete bar-symmetric subring identification: the bar-symmetric subring is exactly $R[X^2]$, providing a concrete model of "$P_{\mathrm{avg}}$ kills odd powers".

## Proved theorems (Lean)

The Lean sibling [`polynomial-bar-involution.lean`](polynomial-bar-involution.lean) proves the following (see [Table](#tbl:polynomial-bar-involution-table-data)). All proofs use only `Polynomial.comp` lemmas from Mathlib.

## Connection to the three-layer synthesis

In `prop:bar-symmetric-three-layer-synthesis`, the universal kernel is bar-anti-symmetric. The polynomial indeterminate $X$ is the canonical such kernel. The series, phase, and gain layers are all even-power polynomials in $X$, hence in $R[X^2]$. Each layer functor is concretely realised as a `BarHeckeFunctor R[X]` sending bar-anti-symmetric inputs to bar-symmetric outputs. The synthesis-class fields become explicit elements of $R[X^2]$.

## Proofs (Lean $\leftrightarrow$ paper bridge)

Every Lean theorem below has both a narrative proof here and a fully formalised Lean proof in [`polynomial-bar-involution.lean`](polynomial-bar-involution.lean). The core bar-involution proofs use only the four ring-involution axioms plus Mathlib's `Polynomial.comp` lemmas.

### Core bar-involution axioms

**Proposition (Lean: `barPoly_X`).** $\overline X = -X$.
<!-- FILE_END: polynomial-bar-involution.md -->

<!-- FILE_START: markov-axioms-braid-link-li2q-phiq-bar-intro.md -->
Continuation of the preceding sub-section.
<!-- FILE_END: markov-axioms-braid-link-li2q-phiq-bar-intro.md -->

<!-- FILE_START: c5-involution-leibniz-decomposition.md -->
**Proposition ($c_5$ involution + Leibniz decomposition).**

*Let $c_5(q)$ be the precision-ladder coefficient at rung $N=5$ in the $\mathfrak{Q}_\beta$ categorical formula ([`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)). Then $c_5$ admits the categorical decomposition:*

$$
\boxed{\;
c_5(q) \;=\; \underbrace{-b(q)^2}_{\text{pure-}\sigma\text{ Kashiwara}}
\;-\; \underbrace{\tfrac{1}{2}}_{\substack{\text{averaged-crossing}\\\text{involution fingerprint}}}
\;}
$$

*where $b(q)^2 = (q^4+q^2+1)/(q^2+1)^2$ is the Hoefsmit off-diagonal coupling squared on $V_{(2,1)}$. The $-1/2$ summand is the fingerprint of the bar-invariant averaged-crossing operator $\sigma_{\text{avg}} = (\sigma + \sigma^{-1})/2$ used at specific positions in the typed-$\mathbf{B}_3$ braid recipe ([`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic)).*

*The decomposition resolves the Pell-Lucas outlier status of $c_5$ at the silver ratio ([`prop:silver-ratio-beta-decay-null`](#prop:silver-ratio-beta-decay-null)). The pure-$\sigma$ part $-b^2$ evaluates to $-7/8$, and the involution fingerprint $-1/2$ is the non-Hecke correction.*
<!-- FILE_END: c5-involution-leibniz-decomposition.md -->

<!-- FILE_START: c5-involution-leibniz-decomposition-interpretation.md -->
**Remark (bar-symmetry class, categorical sectors, and the $c_5$ falsifiable prediction).**

> **Bar-symmetry class** (per [`def:bar-involution`](#def:bar-involution)):
> $c_5(q) = -b^2(q) - 1/2 = -3/2 + 1/[2]_q^2$ is **bar-symmetric** as a function of $q$. The Hoefsmit-Quantum-2 identity $b^2 = 1 - 1/[2]_q^2$ is a proved algebraic theorem in the Lean sibling. The "$-1/2$" piece is a q-independent commutative-QOU constant; $c_5(q=1) = -5/4$ proved as `c5_classical_limit_eq_neg_five_quarters`. The $c_5$ outlier at silver is the arithmetic sum of two clean bar-symmetric pieces landing on inert prime $11 \in \mathbb{Z}[1+\sqrt 2]$, not a quantum-deformation artifact.

> **Pentagon-reduction cross-link.** The Leibniz expansion uses the q-dilogarithm pentagon identity implicitly. The algebraic identity making this rigorous lives in [`pentagon_reduction_li2q.py`](../../../computations/pentagon_reduction_li2q.py). The Pentagon coherence layer of $c_5$'s decomposition is what `pentagon_reduction_li2q.py` makes algebraic.

## Categorical interpretation

The $\mathfrak{Q}_\beta$ predictions live in two distinct categorical sectors. First, the pure-$\sigma$ sector ($c_3, c_4, c_6, c_7$): contributions from positions acting as pure Hecke generators or their inverses. This algebraically lives in the $\mathbb{Z}$-span of Hecke-quadratic eigenvalues. Second, the bar-invariant fixed-point sector ($c_5$): contributions from averaged-crossing positions. This algebraically lives in the bar-invariant subring (fixed by $\sigma \leftrightarrow \sigma^{-1}$).

The two sectors are independent categorical inputs. Pure-$\sigma$ is the Hecke-generator action; bar-invariant fixed-point is the involution-projector action. Both reproduce $\mathfrak{Q}_\beta$ exactly via the precision ladder.

## Falsifiable prediction

Any future rung $c_k$ at $k \geq 8$ whose order $\hbar_q^{2k}$ coincides with an averaging-resonance position will pick up similar $1/2$ fingerprints.

The proton braid has 11 typed crossings: 7 pure $\sigma_0$, 4 pure $\sigma_1$, 1 averaged $\sigma_0$, 1 averaged $\sigma_1$, 3 inverted $\sigma_1^{-1}$. The averaging-resonance rungs are determined by the positions where two averaged crossings interact. 

By combinatorial counting, the predicted averaging-resonance rungs are those $k$ for which $\binom{2}{2} \cdot (\text{combinatorial weight})$ peaks. The first is $k = 5$; subsequent peaks are predicted at $k = 8, 11, \ldots$ (every 3 rungs).

This is testable by extending SDP-$T_\beta$ extraction to $k \geq 8$ and checking whether $c_8$ has a $1/2$ fingerprint. The probe is queued in [`computations/qbeta/qbeta_decay_sdp_extended_ck.py`](../../computations/qbeta/qbeta_decay_sdp_extended_ck.py).

## Discussion

This decomposition is a structural identification, not a first-principles derivation. The $-b^2$ and $-1/2$ summands are identified categorically. The proof that the precision-ladder $c_5$ takes exactly this form requires computing the typed-$\mathbf{B}_3$ Markov-trace expansion at order $b^5 \hbar_q^{10}$, and separating pure-$\sigma$ contributions from averaged-position contributions. Both are concrete computations not yet executed. This proposition sets up the categorical grammar; its full proof is gated on the order-by-order Hecke expansion machinery.
<!-- FILE_END: c5-involution-leibniz-decomposition-interpretation.md -->

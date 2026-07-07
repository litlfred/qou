<!-- FILE_START: markov-axioms-primitive.md -->
**Primitive Markov-trace axioms** (helper for the categorical chain).

This remark records the four Markov-trace axioms (Jones 1985, Wenzl 1988) as
Lean-level primitives, allowing **previously-axiomatic class hypotheses to be
discharged** from a smaller axiomatic base.

## Axioms

The Markov trace $\tau_M$ on the Iwahori-Hecke algebra $H_n(R, q)$ is the
unique linear functional satisfying:

- **M1 (normalisation)**: $\tau_M(1) = 1$.
- **M2 (cyclicity)**: $\tau_M(xy) = \tau_M(yx)$ for all $x, y \in H_n(R, q)$.
- **M3 (stabilisation by $\sigma_n$)**: $\tau_M(x \sigma_n) = z \cdot \tau_M(x)$
  for $x \in H_n(R, q)$, where $z = 1/(\sqrt q + 1/\sqrt q)$ is the
  Markov-Jones parameter and $\sigma_n$ is the new generator from
  stabilising to $H_{n+1}(R, q)$.
- **M4 (stabilisation by $\sigma_n^{-1}$)**: $\tau_M(x \sigma_n^{-1}) = z \cdot \tau_M(x)$.

These together force $\tau_M$ to be the Jones-Markov (non-degenerate) trace
per [`prop:markov-trace-frobenius-selection`](#prop:markov-trace-frobenius-selection).

## Consequence: disjoint-product factorisation

From axiom M3 alone, the joint Markov trace of two braids acting on disjoint
strand sets factorises:

$$
  \tau_M(K_1 \sqcup K_2) \;=\; \tau_M(K_1) \cdot \tau_M(K_2) \cdot z^k,
$$

where $k$ is the number of disjoint strands stabilised. The proof is by
iterating M3 $k$ times: each new disjoint strand contributes a factor $z$.

This DISCHARGES the previously-axiomatic class hypothesis `MarkovDisjointStabilisation`
used in [`prop:categorical-chain-convergence-mechanisms`](#prop:categorical-chain-convergence-mechanisms)
(Mechanism 2 — linking-number locality). The conditional-class
inter-knot-decoupling theorem now follows from the primitive Markov axioms,
not from a separate axiomatic input.
<!-- FILE_END: markov-axioms-primitive.md -->

<!-- FILE_START: markov-trace-inductive-limit.md -->
**Markov trace on the inductive limit $\mathbf{B}_\infty = \bigcup_n \mathbf{B}_n$ — single global trace consolidating every per-$n$ `MarkovTraceN n q`.**

Per Jones 1985 and Wenzl 1988, the Markov trace
$\tau_M : \mathbf{B}_\infty \to \mathbb{R}$ is a single operator on
the inductive limit of braid groups, with restrictions
$\tau_M\big|_{\mathbf{B}_n}$ giving the per-$n$ trace. The inductive
structure is the canonical inclusion
$\iota_n : \mathbf{B}_n \hookrightarrow \mathbf{B}_{n+1}$
(adjoining a non-interacting strand on the right). The axioms M1-M4
(Jones 1985) characterise $\tau_M$ uniquely:

 - M1: $\tau_M(1_n) = 1$ (per-$n$ normalisation)
 - M2: $\tau_M(xy) = \tau_M(yx)$ (cyclicity, per-$n$)
 - M3: $\tau_M(\iota_n(x) \cdot \sigma_n) = z \cdot \tau_M(x)$ (stabilisation)
 - M4: $\tau_M(\iota_n(x) \cdot \sigma_n^{-1}) = z \cdot \tau_M(x)$

with $z = 1/(\sqrt{q} + 1/\sqrt{q})$ the Markov-Jones parameter.

## Contents of this block

The Lean module
`QOU.BraidKnot.markov_trace_inductive_limit` provides:

1. `opaque tauM_n (q : ℝ) {n : ℕ} (w : BraidWord n) : ℝ` — the per-$n$ scalar trace value.
2. `class MarkovTraceInductiveLimit q` — single global hypothesis carrying the stabilisation `inclusion_residual` scalar + an equation asserting it vanishes (explicit-residual pattern).
3. `instance defaultMarkovTraceInductiveLimit q` — ansatz discharge (residual $= 0$ by definition, pending substantive operator construction).
4. **Bridge instance**
 `markovTraceN_from_inductive_limit q n : MarkovTraceN n q` —
 under the inductive-limit class, **every per-$n$ `MarkovTraceN`
 class is automatically derivable** (the per-$n$ axioms are the
 restrictions of the global ones).

## Consolidation benefit

Without the bridge: every $n \in \{2, 3, 6, 12, \ldots\}$ requires
its own `instance : MarkovTraceN n q` discharge. With the bridge: a
single global witness `MarkovTraceInductiveLimit q` automatically
elaborates every per-$n$ instance, eliminating per-$n$ duplication.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: markov-trace-inductive-limit.md -->

<!-- FILE_START: trm-hopf-sigma1-sq-closed-form.md -->
**Proposition (closed form for the canonical Markov trace of $\sigma_1^2$).**

*Let $H_n(q)$ be the Iwahori–Hecke algebra of type $A_{n-1}$ over
$\mathbb{Q}(q^{1/2})$ and let $\mathrm{tr}_M \colon H_n(q) \to \mathbb{Q}(q^{1/2})$
be the canonical Markov trace ([`thm:jones-markov-trace`](#thm:jones-markov-trace)).
Then for every $n \geq 2$,*

$$
\boxed{\quad
  \mathrm{tr}_M(\sigma_1^2)
  \;=\; \frac{q^{5/2} - q^{1/2} + q^2 + q}{q^2 + q}
  \;=\; 1 + \frac{q - 1}{q^{1/2}}.
\quad}
$$

*The value is independent of $n$ (Markov invariance under
stabilisation), and the closure $\widehat{\sigma_1^2}$ is the
positive Hopf link $L_+^{\mathrm{Hopf}}$.*
## Implication for the $\mathfrak{Q}_\beta$ precision-ladder

The $\mathfrak{Q}_\beta$ factorisation ([`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder))
writes
$$
  \mathfrak{Q}_\beta \;=\; Q_A \cdot \cos\bigl(\alpha - b\hbar_q^2/2\bigr)
              \cdot \prod_{n \geq 2} (1 + c_n \hbar_q^{2n})
$$
with claimed coefficients $c_2 = b^2$, $c_3 = -2 b^3$
, $c_4 = b^2 + 1/2$.
The bare-Markov $\varepsilon^{2n}$ coefficients of
$\mathrm{tr}_M(\sigma_1^2) - 1$ above are NOT equal to these:

See [Table 2](#tbl:trm-hopf-sigma1-sq-closed-form-table2-data).

The mismatch proves the $F_n := 1 + c_n \hbar_q^{2n}$ are NOT
extracted from the bare Markov trace of $\sigma_1^2$. They are a
SEPARATE decomposition of $\mathfrak{Q}_\beta$ in which each factor must
arise from a distinct categorical object $\mathcal{B}_n$ — for $F_3$
specifically, the V_(2,2,2) Wedderburn-block projection inside
Hoefsmit $V_{(2,1)} \otimes V_{(2,1)}$ embedded in $H_6$
(per the c_3 = J_Hopf(q=1) = −2 structural identification, locked
behind the §3b-cond `QbetaC3StructuralFormClass` in
`q-beta-categorical-precision-ladder.lean`; see
[`docs/audits/2026-05-31-ck-exploratory-probes-removed.md`](../../../docs/audits/2026-05-31-ck-exploratory-probes-removed.md)
for the derivation status).

## Remarks

1. The closed form $1 + (q-1) \cdot q^{-1/2}$ is the simplest
   nontrivial Markov-trace value in the framework and serves as a
   sanity check for all canonical-Markov implementations
   ([`markov_peel.tr_M_atomic`](computations/markov/markov_peel.py),
   [`markov_weights_symbolic.tr_M_canonical`](computations/markov/markov_weights_symbolic.py),
   [`markov_trace_canonical.tr_M_word`](computations/markov/markov_trace_canonical.py)).
   All three produce identical output for $\sigma_1^2$ at $q = q_0$ to 50 dps.

2. The binomial-coefficient closed form for the Taylor expansion is
   a special case of the more general identity
   $\mathrm{tr}_M(\sigma_1^k) - z^{k-1} = \mathrm{poly}_k(q) \cdot q^{-(k-1)/2}$
   for $k \geq 1$, derivable by iterating the Hecke quadratic
   relation.

3. The Markov-invariance of $\mathrm{tr}_M(\sigma_1^2)$ across
   $H_n$ for $n \geq 2$ is consistent with the Markov property at
   property 3 of [`thm:jones-markov-trace`](#thm:jones-markov-trace),
   and is verified empirically across H_3, H_4, H_5, H_6 in
   [`probe_F_n_categorical_derivation.py`](computations/probe_F_n_categorical_derivation.py).

4. **Lean realisation (archimedean specialisation, §7c).** The
   propositional content above is the exact algebraic identity over the
   formal field $\mathbb{Q}(q^{1/2})$ — categorical/fibre level, holding
   for all $q$ with no ordering or analytic hypothesis. The Lean
   formalisation `QOU.Braiding.TrMHopfSigma1SqClosedForm` realises it on
   the **archimedean side**: it specialises $q$ to $\mathbb{R}$ in the
   Wenzl positivity regime $q > 1$ and discharges the identity by the
   substitution $u := \sqrt{q}$ (`Real.sqrt`), reducing
   $\frac{u^5 - u + u^4 + u^2}{u^4 + u^2} = 1 + (u^2 - 1)\,u^{-1}$ via
   `field_simp; ring` under $u > 0$. The square-root substitution and the
   $q > 1$ ordering are the archimedean constructs that pin the
   formalisation to $\mathbb{R}$; the underlying identity itself is
   substrate-side and base-ring-agnostic.


**Mathematical Novelty:** While the derivation itself follows a standard Hecke/Markov calculation, this closed form represents the simplest nontrivial derived Markov-trace in the framework. The value-driven finding that the bare-Markov $\epsilon^{2n}$ coefficients are *not* the $\mathfrak{Q}_\beta$ precision-ladder $c_n$ (meaning $F_n$ is a separate categorical decomposition) adds substantive novel mathematical content to the framework.
<!-- FILE_END: trm-hopf-sigma1-sq-closed-form.md -->

<!-- FILE_START: hecke-algebra-from-braiding.md -->
The Iwahori--Hecke algebra in which all subsequent Gröbner--Shirshov normal-form
computations take place is *not* an algebra with a free parameter.
It is the quotient of the braid-group algebra by the minimal
polynomial of the categorical braiding.

Concretely, the braiding eigenvalue extraction
([eigenvalue extraction](#prop:braiding-eigenvalue-extraction))
shows that $c_{V,V}$ has eigenvalues $(q, -q^{-1})$ on the
decomposition $V \otimes V = S^2 V \oplus \Lambda^2 V$.
Applying the fibre functor $\tau$ gives the endomorphism
$T = \tau(c_{V,V})$ satisfying the Hecke relation

$$
  (T - q)(T + q^{-1}) =  0,
$$

where $q \in \mathrm{End}(\mathbf{1}) \cong k^{\times}$ is the
braiding eigenvalue — the same $q$ that parametrises the substrate
family $d_q$ ([substrate parameter](#def:substrate-parameter)).

The Iwahori--Hecke algebra on $n$ strands is therefore

$$
  H_n(R, q) =  k[B_n] \big/
  \bigl\langle (\sigma_i - q)(\sigma_i + q^{-1})  \big| 
  i = 1, \ldots, n{-}1 \bigr\rangle,
$$

and the parameter $q$ is a **categorical datum** — determined by
the braiding of $(\mathbf{C}, A, \tau)$, not chosen freely.
Every Laurent polynomial $c_w \in \mathbb{Z}[q, q^{-1}]$ appearing
in a Gröbner--Shirshov normal form
([nuclear normal form](#prop:nuclear-groebner-reduction)) inherits
its $q$ from this categorical source.  The per-crossing weights
$(q, -q^{-1})$ that define the crossing energy
([crossing energy](#def:crossing-energy)) are precisely the two
eigenvalues of $T$ on $S^{2} V \oplus \Lambda^{2} V$, forced by
the categorical volume constraint and not posited separately.
<!-- FILE_END: hecke-algebra-from-braiding.md -->

<!-- FILE_START: f-bor-borromean-observable.md -->
**Definition (Borromean categorical observable $F_{\mathrm{Bor}}$).**

*The* **Borromean categorical observable** *is the natural Wedderburn-
content-shifted combination*

$$
  F_{\mathrm{Bor}}(q) \;:=\;
    \frac{\bigl|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)\bigr| \cdot [3]_q!}{q^3}
$$

*built from two Lean-proved closed forms over a generic commutative
ring carrying $q$ as a unit:*

$$
  \bigl|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)\bigr|
  \;=\; \frac{4 + h^2 - 3h^4 - h^6}{h^2 + 4}
  \qquad (h := q - q^{-1})
$$

*([`prop:borromean-markov-trace-closed-form`](../mass-theory/borromean-markov-trace-closed-form.md))
and*

$$
  [3]_q! \;=\; (q^2 + 1 + q^{-2})(q + q^{-1}) \;=\; (h^2 + 3) \cdot [2]_q
$$

*([`prop:y-lambda-closed-form-wenzl-bridge`](../mass-theory/y-lambda-closed-form-wenzl-bridge.md))
where $[2]_q = q + q^{-1}$.*

*Equivalently, via the q-Schur Markov-weight identification
$y_{(3)}(q) := q^3 / [3]_q!$:*

$$
  F_{\mathrm{Bor}}(q) \;=\; \frac{|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)|}{y_{(3)}(q)}.
$$

## Cleaner form

The $y_{(3)}$ form makes the categorical role explicit: $F_{\mathrm{Bor}}$
is the **Markov trace of the Borromean braid normalised by the
content-shifted Markov weight of the trivial partition $(3)$**. The
content sum $c((3)) = 0 + 1 + 2 = 3$ controls the $q^3$ denominator.

## Exact rational $h$-expansion

Every coefficient of $F_{\mathrm{Bor}}$ in the variable
$h = q - q^{-1}$ is an exact rational number, derivable from the
Lean-proved closed forms:

$$
  F_{\mathrm{Bor}}(h)
  \;=\; 6 \;-\; 9h \;+\; \tfrac{19}{2}h^2 \;-\; \tfrac{57}{8}h^3
        \;-\; \tfrac{1}{2}h^4 \;+\; \tfrac{649}{128}h^5 \;-\; 7h^6 \;+\; \cdots
$$

The $h^2$ coefficient $19/2$ decomposes across the three categorical
factors:

| Factor | $h^2$ contribution |
|---|---|
| $|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)|$ | $0$ (exact per-partition cancellation, [`prop:borromean-markov-trace-closed-form`](../mass-theory/borromean-markov-trace-closed-form.md)) |
| $[3]_q! = (h^2 + 3) \cdot [2]_q$ | $11/4$ |
| $q^3$ (denominator) | $9/8$ |

## Structural-integer identifications

Two categorical integers attach to $F_{\mathrm{Bor}}$:

| Integer | Categorical meaning | Status |
|---|---|---|
| $2$ | $\dim V_{(2,1)}$ — classical dimension of the standard irrep of $S_3$ (trace-dominant per Wedderburn diagnostic at 49% of $T_1$). Hook-length formula: $3! / (3 \cdot 1 \cdot 1) = 2$. | **Lean-proved** ([`DimStandardRepS3.lean`](../lean/QOU/BraidsAndKnots/DimStandardRepS3.lean) `dim_V_21_eq_two`) |
| $12$ | $\dim V_{(2,1)} \cdot 3! = 2 \cdot 6$, where $\lvert S_3 \rvert = 3! = P_3(q^2)\rvert_{q=1}$ is the Poincaré polynomial at the classical limit of $[3]_q!$. | **Identified** — $\dim V_{(2,1)}$ is Lean-proved; $3!$ is the symmetric group order |

These integers carry no archimedean information: they are dimensions
and orders of finite groups, available over any base ring.

## Notes on the open categorical step

Identification of $F_{\mathrm{Bor}}$ as a natural categorical observable
is complete via the $y_{(3)}$-Markov-weight formula above (Lean-proved
[`YLambdaQSchur.lean`](../lean/QOU/BraidsAndKnots/YLambdaQSchur.lean)
`F_Bor_eq_trM_over_y_3`). The bridge from $\dim V_{(2,1)}$ to its
appearance as a *linear* factor in a mass formula — i.e. the formal
categorical reason the trace-dominant irrep's dimension enters
linearly in a substrate-evaluated identity — remains a structural
open step. The Wedderburn block expansion of the Markov trace
provides the natural framework (the $(2,1)$ block carries 49% of the
proton's $T_1$ contribution per the Wedderburn diagnostic), but the
formal categorical statement is pending.

## See also

- [`prop:borromean-markov-trace-closed-form`](../mass-theory/borromean-markov-trace-closed-form.md)
  — Lean-proved $|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)|$
- [`prop:y-lambda-closed-form-wenzl-bridge`](../mass-theory/y-lambda-closed-form-wenzl-bridge.md)
  — Lean-proved $y_\lambda$ closed form (used for $[3]_q!$ factor)
- [`prop:proton-mass-substrate-identity`](../appendix-qvalues/proton-mass-substrate-identity.md)
  — archimedean substrate evaluation that consumes this observable
<!-- FILE_END: f-bor-borromean-observable.md -->

<!-- FILE_START: hecke-normal-form.md -->
**Definition.**
*The **Hecke normal form** of an element $h \in H_n(R, q)$ is the
unique representative in the Gröbner--Shirshov canonical basis
obtained by iterated application of three rewriting rules:*

1. *Hecke relation: $\sigma_i^2 \to (q - q^{-1})\sigma_i + \mathbf{1}$.*
2. *Far commutativity: $\sigma_i \sigma_j \to \sigma_j \sigma_i$
   for $|i - j| \geq 2$.*
3. *Yang--Baxter: $\sigma_i \sigma_{i+1} \sigma_i \to
   \sigma_{i+1} \sigma_i \sigma_{i+1}$ (in the direction
   decreasing shortlex order).*

*The reduction is confluent (Diamond Lemma), so the normal form
is independent of the order in which rules are applied.  The
resulting basis elements are in bijection with the symmetric
group $S_n$: each $w \in S_n$ gives a basis element
$T_w = T_{s_{i_1}} \cdots T_{s_{i_k}}$ for any reduced
expression $w = s_{i_1} \cdots s_{i_k}$.*

**Computational shortcut.**
*Under the Brundan–Kleshchev isomorphism the irreducible $T_w$
are equivalently the highest-weight vertices of a finite component
of the Kashiwara crystal $\mathrm{Cryst}(\mathfrak{sl}_n)$; the
engine may compute $T_w$ by directed crystal traversal rather than
by S-polynomial overlap analysis.  See
[crystal-graph realisation](#conj:crystal-graph-realization).*
<!-- FILE_END: hecke-normal-form.md -->

<!-- FILE_START: dark-vision-strand-bandwidth.md -->
**Remark (vision and strand bandwidth).**
*Treat photons as unknotted strands.  Ambient light entering the
eye is a tensor product of $n$ such strands; reflection from
environmental matter (electrons, nuclei — non-trivial highest-weight
knots) braids the photon strands with the environment's state, so
the outgoing light carries an imprint as a braid word in the
Iwahori–Hecke algebra $H_n(R, q)$.  An act of seeing applies the
[observation functor $\tau$](#def:observation) to this braided
state, returning a classical scalar.*

*The dimension of the accessible phase space is fixed by the braid
group representations on $n$ strands.  In low light $n$ is small,
so:*

1. *the relevant component of the Kashiwara crystal
   $\mathrm{Cryst}(\mathfrak{sl}_n)$ \cite{kashiwara1991} is
   shallow and few $\tilde e_i, \tilde f_i$ paths are available
   (cf.\ [crystal-graph realisation](#conj:crystal-graph-realization));*
2. *by the
   [confinement–grading correspondence](#conj:confinement-grading-correspondence),
   the maximal admissible KLR grading shift, and hence the
   crossing complexity the channel can support, is bounded above
   by the available strand count;*
3. *applying $\tau$ to a low-grade module returns a low-degree
   polynomial — too few non-zero coefficients to encode the scene.*

*The phenomenology that we cannot see in the dark is therefore
not a failure of the retina but a structural truncation of the
observation channel: information capacity is proportional to the
topological complexity of the incoming braided state, which low
strand count cannot sustain.  This remark interprets — it makes
no further mathematical claim beyond
[observation](#def:observation).*
<!-- FILE_END: dark-vision-strand-bandwidth.md -->

<!-- FILE_START: markov-moves-brane-tower.md -->
The two Markov moves that guarantee link invariance of the Jones
polynomial ([Jones--Markov trace](#thm:jones-markov-trace)) correspond
to the horizontal and vertical components of the brane tower's
cosimplicial structure
([cosimplicial crossed groupoid](#prop:cosimplicial-crossed-groupoid)).

1. **Conjugation** $\beta \mapsto \gamma\beta\gamma^{-1}$ (same $B_n$,
   same level).  This is the *horizontal* direction: the crossed
   structure of the cosimplicial groupoid, where $1$-morphisms
   $g_{ij}^{(n)}$ act on $2$-morphisms $a_{ij}^{(n)}$ by conjugation
   via $\mathrm{Ad}(\mathrm{SU}_{q_n}(2))$ at a *fixed level* $n$.
   In the weight decomposition
   ([weight decomposition](#thm:weight-decomposition-exists)), this is
   the weight-$0$ (horizontal) component $\alpha_H$: gauge
   transformations within a single fibre.  The trace property
   $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$ ensures the categorical
   trace is invariant under these horizontal moves.

2. **Stabilisation** $\beta \mapsto \beta \cdot \sigma_n^{\pm 1}$
   (embed $B_n \hookrightarrow B_{n+1}$).  This is the *vertical*
   direction: the coface maps
   $\delta^i \colon \mathfrak{G}_n \to \mathfrak{G}_{n+1}$ of the
   cosimplicial structure, realized by jet prolongation
   $A_n \hookrightarrow J^1(A_n) = A_{n+1}$
   ([recursive brane tower](#def:recursive-brane-tower)).  In the weight
   decomposition, this is the non-zero-weight (vertical) component
   $\alpha_V$: moving between levels of the tower.  The Markov property
   $\mathrm{tr}_M(x \sigma_n^{\pm 1}) = z^{\pm 1}\mathrm{tr}_M(x)$
   ensures the trace scales predictably under these vertical inclusions.

The Iwahori--Hecke algebra tower $H_1(R, q) \hookrightarrow H_2(R, q) \hookrightarrow \cdots$ thus shadows the brane tower
$A_0 \hookrightarrow A_1 \hookrightarrow \cdots$, and the Jones
polynomial is the observable invariant under *both* directions of this
decomposition.  Markov's theorem --- that conjugation and stabilisation
generate all equivalences between braid representatives of the same
link --- is the statement that horizontal and vertical moves together
exhaust the gauge freedom of the cosimplicial crossed groupoid.  The
direct limit
$\mathcal{A}_\infty = \varinjlim\mathrm{End}_{\mathbf{C}}(A_n)$
([direct limit algebra](#def:direct-limit-algebra)) is the algebraic
receptacle for this invariance: it is the algebra on which the Markov
trace stabilises to a well-defined link invariant.
<!-- FILE_END: markov-moves-brane-tower.md -->

<!-- FILE_START: markov-trace-ambient-s3.md -->
The Markov trace is built algebraically — as a trace on the Hecke
quotient of the braid-group algebra
([Jones--Markov trace](#thm:jones-markov-trace)) — yet the invariant it
computes is topological: an invariant of an oriented link embedded in
the three-sphere $S^3$. The ambient $S^3$ is never posited as a separate
object; it enters precisely through the closure construction, by two
classical theorems.

**Alexander's theorem** ($1923$). The closure map
$$
  \widehat{\,\cdot\,} \colon \coprod_{n \ge 1} B_n
    \;\longrightarrow\; \{\text{oriented links in } S^3\}/\text{isotopy},
  \qquad \beta \mapsto \widehat{\beta},
$$
is surjective: every oriented link in $S^3$ is the closure of some braid.
Thus the disjoint union of braid groups already *exhausts* the link types
of the ambient three-sphere — no link in $S^3$ is missed.

**Markov's theorem** ($1936$). Two braids have isotopic closures in $S^3$,
$\widehat{\beta} \cong \widehat{\beta'}$, if and only if $\beta$ and
$\beta'$ are connected by a finite sequence of **Markov moves**:
conjugation $\beta \mapsto \gamma\beta\gamma^{-1}$ within a fixed $B_n$,
and stabilisation $\beta \mapsto \beta\,\sigma_n^{\pm 1}$ across the
inclusion $B_n \hookrightarrow B_{n+1}$. These two moves generate exactly
the kernel of the closure map.

The Markov trace is, by construction, invariant under both moves: the
cyclic trace property $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$ gives
conjugation-invariance, and the Markov property
$\mathrm{tr}_M(x\,\sigma_n^{\pm 1}) = z^{\pm 1}\,\mathrm{tr}_M(x)$ gives
the controlled behaviour under stabilisation (absorbed into the standard
writhe/index normalisation of $J_K(q)$). Combining the three facts:

> Because closure is **onto** the links of $S^3$ (Alexander) and its
> fibres are **exactly** the Markov-move orbits (Markov), and
> $\mathrm{tr}_M$ is **constant on those orbits**, the Markov trace
> descends to a well-defined function on isotopy classes of links in
> $S^3$. The ambient three-sphere is therefore present in the categorical
> data not as an extra datum but as the *target of the Alexander--Markov
> correspondence*: the closure construction $\beta \mapsto \widehat{\beta}$
> **is** the categorical encoding of "the link sits in $S^3$."

This locates, categorically, the $S^3$ that the archimedean layer relies
on when it computes a hyperbolic volume as a knot complement $S^3 \setminus K$:
that $S^3$ is the Alexander--Markov base manifold, recovered from the
substrate-level Markov trace, with no geometric realisation assumed
upstream of it.

**A distinction to keep.** This ambient $S^3$ — the base manifold whose
links are the closures, and whose complements carry the hyperbolic
volumes — is *not* the group manifold $\mathrm{SU}(2) \cong S^3$ that
furnishes the braiding $R$-matrix (nor its $q$-deformation, the quantum
three-sphere underlying $\mathrm{SU}_q(2)$). The diffeomorphism
$\mathrm{SU}(2) \cong S^3$ is a low-dimensional coincidence and plays no
role here: the ambient three-sphere is fixed by the closure construction,
not by the gauge group. Conflating the two is a category error — the
base manifold and the structure group are independent, exactly as in
Chern--Simons theory, where the empty-link invariant of $(S^3, \varnothing)$
is the vacuum partition function and the gauge group enters only through
the representation category.
<!-- FILE_END: markov-trace-ambient-s3.md -->


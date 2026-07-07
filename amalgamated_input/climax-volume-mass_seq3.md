<!-- FILE_START: atom-isotope-confinement-intro.md -->
The previous section calibrated the mass formula on three Wedderburn inputs. We now climb to the full confinement structure: knot operator, confinement level, atom, isotope, electron shell, and the stability test that decides which configurations survive. The shadow-price LP that ranks Wedderburn channels turns out to be the structural mechanism, so the entire ladder is read off LP-dual data.

The section opens with Definition: Knot operator energy (LP-dual shadow price), which writes each knot operator's energy as a shadow price of the operator-selection LP, and Definition: Local shadow-price ordering, which orders the operators by that price. Definition: Confinement level via shadow-price filtration packages the ordering into a filtration on the Hecke subalgebra, with Definition: Cemetery group (subcategory annihilated by $\tau$) recording the kernel — the configurations the observation frame drops — and the existence and uniqueness propositions for each fixing the structural data. The conjectural blocks Conjecture: Crystal-graph realisation of the confinement filtration, Conjecture: Confinement-grading correspondence (and its conditional counterpart), and Remark: Cemetery group emergence layer the categorical reading on top of the LP data.

The substrate-side machinery follows. Remark: Ontological agnosticism flags the substrate-independence of the picture, Conjecture: Type-B folding forces matter/antimatter to be created in conjugate-operator pairs and Remark: Two-photon pair production use the symmetric-crystal technique to enforce CPT, and the conjectures Conjecture: Iwahori--Hecke algebra is the anyon algebra, Conjecture: Root-of-unity MTC truncation, Conjecture: Kazhdan--Lusztig classical limit of $H_n(q)$, and Conjecture: Anyon observation collapse form the substrate-level anyonic backbone. Definition: Confined particle, Definition: Confinement category, and Definition: Electron shell as cabled strands with SDP-selected binding lift the substrate data to the particle-level objects.

The confinement-and-stability layer follows. Definition: Dressed particle (atom) packages the configuration with its electron shell, Proposition: Shell closure stability: noble-gas configurations are local terminal objects, with its interpretation remark, supplies the noble-gas stability law, and Proposition: Level sufficiency with its interpretation guarantees that the confinement level alone suffices to classify the result. The atom-side defines Definition: Atom as a knot via Gröbner normal form, with its existence and uniqueness, Definition: Isotope knot with its equivalence relation, and the pair Definition: Stable atom (ILP feasibility), its decidability, Definition: Unstable atom, and the Definition: Unstable atom decay channel. The blocks Remark: Confinement phase stratification, Remark: Phase-scoped applicability, Remark: ILP solution-count unwrap, Proposition: Shell Schur--Weyl self-duality, Proposition: Compound-beta shell calibration, Proposition: Magic-shell coupling slope $\kappa$, and the closing Definition: Quantum dilogarithm disambiguation: $\Phi_q$ (product form) vs $-\mathrm{Li}_2^q(-z)$ (Kashaev integration limit) complete the toolkit. The next section, **Nuclear Binding and Beta Stability**, takes the confinement filtration and the magic-shell coupling as fixed and extends them across the nuclear binding stratum and the beta-stability valley.
<!-- FILE_END: atom-isotope-confinement-intro.md -->

<!-- FILE_START: knot-operator-energy.md -->
**Definition.**
*Let $H_n(R, q)$ be the Hecke algebra at substrate parameter $q$.
For each Wedderburn block indexed by a partition $\lambda \vdash k$
($k = 2, \ldots, k_{\max}(K, q)$, where $k_{\max}(K, q)$ is the
per-atom truncation determined by the interaction-strand
requirement of $K$ — see [confinement level](#def:confinement-level)),
the **knot operator energy** of $\lambda$ at $q$ is the absolute
value of its LP-dual shadow price
([prop:mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)):*

$$
  E(\lambda, q)
  \;:=\;
  \bigl| u_\lambda(q) \bigr|
  \;=\;
  \left|
    \frac{w_\lambda(q)}{d_\lambda(q)}
    \;-\;
    \frac{1}{[k]_q!}
  \right|,
$$

*where $w_\lambda(q) = d_q(\lambda)^2 / [k]_q!$ is the Wedderburn
weight, $d_\lambda(q) = \dim_q V_\lambda$ is the quantum dimension,
and $1/[k]_q!$ is the LP-dual variable of the normalisation
constraint (the smallest $w_\lambda/d_\lambda$ across partitions of
$k$, attained by the trivial $1$-dimensional $(k)$ and $(1^k)$
representations).*

**Values.**
*The energy takes values in:*
- *Archimedean realisation $R = \mathbb{R}$: $E(\lambda, q)
  \in \mathbb{R}_{\geq 0}$ (totally ordered).*
- *Non-archimedean $\mathbb{Q}_p$: $E(\lambda, q) \in
  \{p^{-n} : n \in \mathbb{Z}\} \cup \{0\}$ (also totally ordered).*
- *Finite field $\mathbb{F}_p$: no archimedean absolute value —
  the energy filtration is undefined, and confinement falls back
  to ILP feasibility (see [stable atom](#def:stable-atom)) which
  IS base-ring-independent.*
<!-- FILE_END: knot-operator-energy.md -->

<!-- FILE_START: knot-operator-energy-vanishing.md -->
**Remark (vanishing locus and cheap/expensive operators).**

**Vanishing locus.**
The set $\{q \in Q : E(\lambda, q) = 0\}$ is the **LP boundary**
for partition $\lambda$: at these $q$-values the operator
$\lambda$ becomes constraint-binding, and its inclusion or
exclusion in the LP-dual basis switches.  Crossing such a
$q$-value is a categorical phase transition for any atom whose
NF includes operator $\lambda$.

**Cheap and expensive operators.**
$1$-dimensional partitions $(k), (1^k)$ have
$w_\lambda/d_\lambda = 1/[k]_q!$, so $E(\lambda, q) = 0$
identically — these operators carry no shadow-price weight and
are always available.  Only mixing partitions ($d_\lambda \geq 2$)
have nonzero $E$ and contribute to the confinement filtration.
<!-- FILE_END: knot-operator-energy-vanishing.md -->

<!-- FILE_START: knot-operator-energy-consumers.md -->
**Remark (consumers: gluon-channel selection by energy minimisation).**
The [proton](#def:categorical-proton) and
[neutron](#def:categorical-neutron) select gluon-stabilisation
channels by minimising the [knot operator
energy](#def:knot-operator-energy) $E(\lambda, q)$ across partitions
of $H_3(q)$.
<!-- FILE_END: knot-operator-energy-consumers.md -->

<!-- FILE_START: knot-operator-energy-exists.md -->
**Proposition.**
*For any partition $\lambda \vdash k$ with $k \leq k_{\max}$ and any
$q$ in the generic locus
$\{q \in R : [k]_q! \neq 0 \;\forall k \leq k_{\max}\}$, the
[knot operator energy](#def:knot-operator-energy)
$E(\lambda, q) = |u_\lambda(q)|$ exists as an element of the
absolute-value image $|R|$ of the base ring.*

*The shadow price $u_\lambda(q) = w_\lambda(q)/d_\lambda(q) -
1/[k]_q! \in R$ is a rational function of $q$ with denominator
$[k]_q! \cdot d_\lambda(q)$, both of which are nonzero on the
generic locus by [mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price).
The absolute value $|\cdot|: R \to |R|$ is well-defined for:*

- *$R = \mathbb{R}$: archimedean $|\cdot|_\infty$, image $\mathbb{R}_{\geq 0}$;*
- *$R = \mathbb{Q}_p$: $p$-adic $|\cdot|_p$, image $\{p^{-n}\} \cup \{0\}$;*
- *$R = \mathbb{F}_p$: no archimedean absolute value, $|R| = \emptyset$;
  the energy filtration is undefined and confinement falls back to
  ILP feasibility ([stable atom](#def:stable-atom)).*

*In each archimedean or non-archimedean case, $E(\lambda, q)$ exists
and is uniquely determined by $\lambda$ and $q$.*
<!-- FILE_END: knot-operator-energy-exists.md -->

<!-- FILE_START: knot-operator-energy-unique.md -->
**Proposition.**
*The knot operator energy
$E(\lambda, q) = |u_\lambda(q)|$
([knot operator energy](#def:knot-operator-energy)) is **uniquely
determined** by:*

1. *the partition $\lambda \vdash k$ (a classical Young diagram —
   $q$-independent indexing),*
2. *the substrate parameter $q$ in the generic locus,*
3. *the choice of absolute value $|\cdot|_v$ on $R$ (archimedean
   or non-archimedean).*

*The shadow price $u_\lambda(q)$ itself is unique in $R$ by LP
duality (complementary slackness gives a unique dual variable per
binding constraint).  The absolute value $|\cdot|_v$ is unique up
to equivalence within each place by Ostrowski's theorem (over
$\mathbb{Q}$) — for $R \in \{\mathbb{R}, \mathbb{Q}_p, \mathbb{F}_p\}$
the canonical choice is fixed by the base ring itself.*

*Uniqueness is "up to base ring equivalence" — the same shadow
price evaluated under equivalent absolute values gives equal
energies.*
<!-- FILE_END: knot-operator-energy-unique.md -->

<!-- FILE_START: local-shadow-ordering.md -->
**Definition.**
*For two partitions $\lambda_1, \lambda_2$ with shadow prices
$y_{\lambda_1}(q), y_{\lambda_2}(q) \in R$, the **local shadow-price
ordering** at $q$ is:*

$$
  \lambda_1 \;\preceq_q\; \lambda_2
  \;\iff\;
  \exists\, U \ni q\;\text{open such that}\;
  |y_{\lambda_1}(q')| \;\leq\; |y_{\lambda_2}(q')|
  \;\;\forall q' \in U.
$$

*Read: "$\lambda_1$ has at most the energy of $\lambda_2$ on a
neighborhood of $q$".*
<!-- FILE_END: local-shadow-ordering.md -->

<!-- FILE_START: shadow-price-continuity.md -->
**Proposition.**
*Each shadow price $u_\lambda(q) = w_\lambda(q)/d_\lambda(q) -
1/[k]_q!$ is a **rational function** of $q$ over the base ring,
with denominator $[k]_q! \cdot d_\lambda(q)$.  On the generic
locus $\{q : [k]_q! \cdot d_\lambda(q) \neq 0\}$, $u_\lambda$ is
continuous in $q$ (smooth in the $\mathbb{R}$ realisation,
$p$-adic continuous in $\mathbb{Q}_p$, well-defined Zariski
on $\mathbb{F}_p$).*

*By continuity, if $|y_{\lambda_1}(q)| < |y_{\lambda_2}(q)|$
strictly, then the [local shadow-price ordering](#def:local-shadow-ordering)
$\lambda_1 \preceq_q \lambda_2$ holds on a neighborhood.*
<!-- FILE_END: shadow-price-continuity.md -->

<!-- FILE_START: phase-boundary-variety.md -->
**Proposition.**
*The locus*

$$
  \mathcal{B}_{\lambda_1, \lambda_2}
  \;:=\;
  \{q \in Q : |y_{\lambda_1}(q)| = |y_{\lambda_2}(q)|\}
$$

*is a **Zariski-closed** subvariety of $Q$, generically of
codimension $\geq 1$ (defined by the polynomial equation
$y_{\lambda_1}^2(q) = y_{\lambda_2}^2(q)$).  The full **phase-boundary
variety** is*

$$
  \mathcal{B}
  \;:=\;
  \bigcup_{\lambda_1 \neq \lambda_2}
    \mathcal{B}_{\lambda_1, \lambda_2}
  \;\cup\;
  \bigcup_\lambda
    \{q : u_\lambda(q) = 0\},
$$

*the union of pairwise-equality varieties and shadow-price-vanishing
varieties.  $\mathcal{B}$ is measure-zero in $Q$.*
<!-- FILE_END: phase-boundary-variety.md -->

<!-- FILE_START: confinement-local-constancy.md -->
**Proposition.**
*The [confinement level](#def:confinement-level) $\ell(K, q)$ is
**locally constant** on $Q \setminus \mathcal{B}$: for any $q
\notin \mathcal{B}$, there is an open $U \ni q$ such that
$\ell(K, q') = \ell(K, q)$ for all $q' \in U$.  The level changes
only at points of the [phase-boundary variety](#prop:phase-boundary-variety)
$\mathcal{B}$ — these are exactly the **categorical phase
boundaries**.*
<!-- FILE_END: confinement-local-constancy.md -->

<!-- FILE_START: shadow-ordering-compute-shortcut.md -->
**Remark (computational shortcut from local constancy).**
Per [unstable-atom](#def:unstable-atom) "Computational shortcut",
expensive computations (per-generator $\hat V_i^{\mathrm{full}}$
extraction in the tower formula
[mass-endomorphism-tower](#prop:mass-endomorphism-tower)) need
exact evaluation only at points of the [phase-boundary
variety](#prop:phase-boundary-variety) $\mathcal{B}$.  In the
complement $Q \setminus \mathcal{B}$, all shadow prices, the
filtration, and the per-generator data are locally constant (by
[local constancy of confinement](#prop:confinement-local-constancy))
— linear interpolation between nearest magic-number anchors is
mathematically justified.
<!-- FILE_END: shadow-ordering-compute-shortcut.md -->

<!-- FILE_START: selection-rule-anchors-c1-c3.md -->
**Proposition (selection-rule anchors at c=1 and c=3).**

*Let $q \in \mathbb{R}_{>0}$ and let $h := q - q^{-1}$.  The per-component
selection rule*

$$
  \mathrm{lw}(c)(q) \;:=\; \frac{1}{c+1} \sum_{\lambda \vdash (c+1)} \dim_q V_\lambda
$$

*satisfies the two exact identities*

$$
  \mathrm{lw}(1)(q) \;=\; 1 \qquad (\text{exactly, } \forall q > 0),
$$

$$
  \mathrm{lw}(3)(q) \;=\; \frac{3q^2 + 4 + 3q^{-2}}{4} \;=\; \frac{5}{2} + \frac{3}{4} h^2.
$$

*These are the muon (c=1, knot) and the proton (c=3, Borromean 3-link)
anchors of the per-component selection rule.*

## Significance

The zero-parameter selection rule is
$\mathrm{lw}(L) = \frac{1}{c+1}\sum_{\lambda\vdash(c+1)} \dim_q V_\lambda$
where $c$ is the number of link components.  The c=1 case must equal 1
for all $q$ (muon, a knot, framework `linking_weight = 1`); the c=3 case
must equal the Family-A formula
$\frac{5}{2} + \frac{3}{4}h^2$ (proton).  This proposition Lean-formalises
both identities, giving the selection rule's two anchors a derivation-tight
status (not a fit — both follow from the q-deformed hook-length formula).

## Lean proof structure

Two purely algebraic identities at the symbolic level, each closed by
`field_simp; ring`:

1. **c=1 anchor** (`selection_rule_c1_eq_one`):
   $\frac{1}{2}\bigl( \dim_q V_{(2)} + \dim_q V_{(1,1)} \bigr) = 1$.
   Both q-dimensions equal $1$ (each partition of 2 has hook product equal
   to the q-factorial), so the average is exactly 1.

2. **c=3 anchor** (`selection_rule_c3_eq_family_a`):
   $\frac{1}{4} \bigl( \dim_q V_{(4)} + \dim_q V_{(3,1)} + \dim_q V_{(2,2)} +
   \dim_q V_{(2,1,1)} + \dim_q V_{(1,1,1,1)} \bigr)
   = (3q^2 + 4 + 3q^{-2})/4$.

   Using the explicit q-hook formula:
   - $\dim_q V_{(4)} = \dim_q V_{(1,1,1,1)} = 1$
   - $\dim_q V_{(3,1)} = \dim_q V_{(2,1,1)} = [3]_q = q^2 + 1 + q^{-2}$
   - $\dim_q V_{(2,2)} = [4]_q / [2]_q = q^2 + q^{-2}$

   Their sum is $1 + (q^2{+}1{+}q^{-2}) + (q^2{+}q^{-2}) + (q^2{+}1{+}q^{-2})
   + 1 = 4 + 3q^2 + 3q^{-2}$, and dividing by 4 gives the stated form.
   The $h^2$ form follows from $q^2 + q^{-2} = h^2 + 2$.

   Both steps are pure polynomial identities in $\mathbb{Z}[q, q^{-1}]$,
   closed by `ring` after `field_simp` to clear the $q^{-1}$ denominators.

## q-usage discipline

Stated over real $q > 0$ (the substrate-anchor regime).  Both
identities are q-rational, fibre-level, with the c=1 case true
for ALL $q > 0$ — an infinite set of constraints, not one point.
AGENTS.md §7c-compliant.

## Cross-references

- $\operatorname{def:coulomb-charge}$ — where the $h = q - q^{-1}$ structure
  enters at the per-crossing level.
- $\operatorname{prop:coulomb-strong-ratio-q-rational}$ — companion identity
  proving $\tanh(\ln q) = (q^2-1)/(q^2+1)$ over real $q > 0$.
- Derivation audit doc:
  [`docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md`](../../../docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md).
<!-- FILE_END: selection-rule-anchors-c1-c3.md -->

<!-- FILE_START: selection-rule-c2-prediction.md -->
**Proposition (selection-rule at c=2 — prediction).**

*Let $q \in \mathbb{R}_{>0}$.  The per-component selection rule
([`prop:selection-rule-anchors-c1-c3`](#prop:selection-rule-anchors-c1-c3))
applied at $c=2$ gives the closed form*

$$
  \mathrm{lw}(2)(q) \;:=\; \frac{1}{3} \sum_{\lambda \vdash 3} \dim_q V_\lambda
  \;=\; \frac{2 + [2]_q}{3} \;=\; \frac{(q+1)^2}{3q}.
$$

*This is the rule's prediction for a 2-component link (= 2 link components,
e.g. the Hopf link).  The closed form is a finite Laurent rational over
$\mathbb{Z}[q, q^{-1}]$ — like the c=1 and c=3 anchors, derivation-tight
(no fit, zero free parameters).*

## Significance

The per-component rule is
$\mathrm{lw}(c) = (1/(c+1)) \sum_{\lambda \vdash (c+1)} \dim_q V_\lambda$,
anchored at c=1 (muon, $\mathrm{lw}=1$ exactly $\forall q$) and c=3
(proton, $\mathrm{lw} = 5/2 + (3/4)h^2$ via Family-A).  The c=2 case is the
**first testable prediction** of the rule beyond the two known anchors.

This proposition Lean-formalises the closed form for c=2 so the prediction
sits alongside its anchors with the same provenance (pure algebraic identity
in the q-deformed hook-length formula).  Any independent determination of a
2-component link's linking_weight in the framework — e.g. a Hopf-link or
gluon EM-linking application — can be tested against this exact formula
without ambiguity.

## Lean proof structure

Single algebraic identity at the symbolic level:

$$
  \frac{1}{3} \bigl( \dim_q V_{(3)} + \dim_q V_{(2,1)} + \dim_q V_{(1,1,1)} \bigr)
  \;=\; \frac{(q+1)^2}{3q}.
$$

Using the explicit q-hook values for partitions of 3:

- $\dim_q V_{(3)} = 1$ (single-row Young diagram, all hooks contribute trivially)
- $\dim_q V_{(2,1)} = [2]_q = q + q^{-1}$ (standard rep at H_3; q-hook computation)
- $\dim_q V_{(1,1,1)} = 1$ (single-column, conjugate of $V_{(3)}$)

Their sum is $2 + q + q^{-1}$, and dividing by 3 gives
$(2 + q + q^{-1})/3 = (q^2 + 2q + 1)/(3q) = (q+1)^2/(3q)$.

This is a pure polynomial-ring identity once $q^{-1}$ denominators are
cleared.  Closed by `field_simp; ring` over $\mathbb{R}_{>0}$.
## q-usage discipline

Stated over real $q > 0$ (substrate-anchor regime).  The closed form
$(q+1)^2/(3q)$ is a Laurent rational in $\mathbb{Z}[q, q^{-1}]$ — fibre-level
construction.  At $q = q_0$ it evaluates to $\approx 1.337$.  No $|q|=1$
step; both $q$ and $q^{-1}$ are real positive at any real $q > 0$.
AGENTS.md §7c-compliant.

## Cross-references

- [`prop:selection-rule-anchors-c1-c3`](#prop:selection-rule-anchors-c1-c3) — the two
  known anchors that the rule's existence is established on.
- Derivation audit:
  [`docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md`](../../../docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md).
<!-- FILE_END: selection-rule-c2-prediction.md -->


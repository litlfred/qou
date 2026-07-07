<!-- FILE_START: atom-isotope-confinement-intro.md -->
The previous section calibrated the mass formula on three Wedderburn inputs. We now build the full confinement structure: knot operator, confinement level, atom, isotope, electron shell, and the stability test that determines survival. The shadow-price LP that ranks Wedderburn channels supplies the structural mechanism; the entire ladder is read from LP-dual data.

The section opens with Definition: Knot operator energy (LP-dual shadow price), writing each knot operator's energy as a shadow price of the operator-selection LP. Definition: Local shadow-price ordering ranks the operators by this price. Definition: Confinement level via shadow-price filtration packages the ordering into a filtration on the Hecke subalgebra. Definition: Cemetery group (subcategory annihilated by $\tau$) isolates the kernel—the configurations the observation frame discards. The corresponding existence and uniqueness propositions secure the structural data. Conjecture: Crystal-graph realisation of the confinement filtration, Conjecture: Confinement-grading correspondence, and Remark: Cemetery group emergence layer the categorical interpretation over the LP data.

The substrate-side machinery follows. Remark: Ontological agnosticism confirms the substrate-independence of the framework. Conjecture: Type-B folding forces matter/antimatter creation in conjugate-operator pairs, while Remark: Two-photon pair production employs the symmetric-crystal technique to enforce CPT. The conjectures on the anyon algebra, root-of-unity MTC truncation, Kazhdan--Lusztig classical limit, and anyon observation collapse establish the substrate-level anyonic backbone. Definition: Confined particle, Definition: Confinement category, and Definition: Electron shell as cabled strands with SDP-selected binding lift this substrate data to particle-level objects.

The confinement-and-stability layer concludes the sequence. Definition: Dressed particle (atom) packages the configuration with its electron shell. Proposition: Shell closure stability: noble-gas configurations are local terminal objects provides the noble-gas stability law. Proposition: Level sufficiency guarantees that the confinement level alone completely classifies the result. For the atom-side, we define Definition: Atom as a knot via Gröbner normal form, Definition: Isotope knot, Definition: Stable atom (ILP feasibility), its decidability, Definition: Unstable atom, and Definition: Unstable atom decay channel. The closing remarks and propositions complete the toolkit, preparing for the next section, **Nuclear Binding and Beta Stability**, which extends the confinement filtration and magic-shell coupling across the nuclear binding stratum and the beta-stability valley.
<!-- FILE_END: atom-isotope-confinement-intro.md -->

<!-- FILE_START: knot-operator-energy.md -->
**Definition.**
*Let $H_n(R, q)$ be the Hecke algebra at substrate parameter $q$. For each Wedderburn block indexed by a partition $\lambda \vdash k$ ($k = 2, \ldots, k_{\max}(K, q)$, where $k_{\max}(K, q)$ is the per-atom truncation determined by the interaction-strand requirement of $K$ — see [confinement level](#def:confinement-level)), the **knot operator energy** of $\lambda$ at $q$ is the absolute value of its LP-dual shadow price ([prop:mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)):*

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

*where $w_\lambda(q) = d_q(\lambda)^2 / [k]_q!$ is the Wedderburn weight, $d_\lambda(q) = \dim_q V_\lambda$ is the quantum dimension, and $1/[k]_q!$ is the LP-dual variable of the normalisation constraint. The trivial $1$-dimensional $(k)$ and $(1^k)$ representations attain this minimum value of $w_\lambda/d_\lambda$ across partitions of $k$.*

**Values.**
*The energy takes values in:*
- *Archimedean realisation $R = \mathbb{R}$: $E(\lambda, q) \in \mathbb{R}_{\geq 0}$ (totally ordered).*
- *Non-archimedean $\mathbb{Q}_p$: $E(\lambda, q) \in \{p^{-n} : n \in \mathbb{Z}\} \cup \{0\}$ (totally ordered).*
- *Finite field $\mathbb{F}_p$: no archimedean absolute value exists. The energy filtration is undefined. Confinement falls back to ILP feasibility (see [stable atom](#def:stable-atom)), which IS base-ring-independent.*
<!-- FILE_END: knot-operator-energy.md -->

<!-- FILE_START: knot-operator-energy-vanishing.md -->
**Remark (vanishing locus and cheap/expensive operators).**

**Vanishing locus.**
The set $\{q \in Q : E(\lambda, q) = 0\}$ is the **LP boundary** for partition $\lambda$. At these $q$-values, the operator $\lambda$ becomes constraint-binding. Its inclusion or exclusion in the LP-dual basis switches. Crossing such a $q$-value marks a categorical phase transition for any atom whose NF includes operator $\lambda$.

**Cheap and expensive operators.**
The $1$-dimensional partitions $(k), (1^k)$ satisfy $w_\lambda/d_\lambda = 1/[k]_q!$, so $E(\lambda, q) = 0$ identically. These operators carry no shadow-price weight and are always available. Only mixing partitions ($d_\lambda \geq 2$) possess nonzero $E$ and contribute to the confinement filtration.
<!-- FILE_END: knot-operator-energy-vanishing.md -->

<!-- FILE_START: knot-operator-energy-consumers.md -->
**Remark (consumers: gluon-channel selection by energy minimisation).**
The [proton](#def:categorical-proton) and [neutron](#def:categorical-neutron) select gluon-stabilisation channels by minimising the [knot operator energy](#def:knot-operator-energy) $E(\lambda, q)$ across partitions of $H_3(q)$.
<!-- FILE_END: knot-operator-energy-consumers.md -->

<!-- FILE_START: knot-operator-energy-exists.md -->
**Proposition.**
*For any partition $\lambda \vdash k$ with $k \leq k_{\max}$ and any $q$ in the generic locus $\{q \in R : [k]_q! \neq 0 \;\forall k \leq k_{\max}\}$, the [knot operator energy](#def:knot-operator-energy) $E(\lambda, q) = |u_\lambda(q)|$ exists as an element of the absolute-value image $|R|$ of the base ring.*

*The shadow price $u_\lambda(q) = w_\lambda(q)/d_\lambda(q) - 1/[k]_q! \in R$ is a rational function of $q$ with denominator $[k]_q! \cdot d_\lambda(q)$. Both are nonzero on the generic locus by [mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price). The absolute value $|\cdot|: R \to |R|$ is well-defined for:*

- *$R = \mathbb{R}$: archimedean $|\cdot|_\infty$, image $\mathbb{R}_{\geq 0}$;*
- *$R = \mathbb{Q}_p$: $p$-adic $|\cdot|_p$, image $\{p^{-n}\} \cup \{0\}$;*
- *$R = \mathbb{F}_p$: no archimedean absolute value, $|R| = \emptyset$. The energy filtration is undefined and confinement falls back to ILP feasibility ([stable atom](#def:stable-atom)).*

*In each archimedean or non-archimedean case, $E(\lambda, q)$ exists and is uniquely determined by $\lambda$ and $q$.*
<!-- FILE_END: knot-operator-energy-exists.md -->

<!-- FILE_START: knot-operator-energy-unique.md -->
**Proposition.**
*The knot operator energy $E(\lambda, q) = |u_\lambda(q)|$ ([knot operator energy](#def:knot-operator-energy)) is **uniquely determined** by:*

1. *the partition $\lambda \vdash k$ (a classical Young diagram — $q$-independent indexing),*
2. *the substrate parameter $q$ in the generic locus,*
3. *the choice of absolute value $|\cdot|_v$ on $R$ (archimedean or non-archimedean).*

*The shadow price $u_\lambda(q)$ is unique in $R$ by LP duality (complementary slackness dictates a unique dual variable per binding constraint). The absolute value $|\cdot|_v$ is unique up to equivalence within each place by Ostrowski's theorem (over $\mathbb{Q}$). For $R \in \{\mathbb{R}, \mathbb{Q}_p, \mathbb{F}_p\}$, the base ring itself fixes the canonical choice.*

*Uniqueness holds "up to base ring equivalence": the same shadow price evaluated under equivalent absolute values yields equal energies.*
<!-- FILE_END: knot-operator-energy-unique.md -->

<!-- FILE_START: local-shadow-ordering.md -->
**Definition.**
*For two partitions $\lambda_1, \lambda_2$ with shadow prices $y_{\lambda_1}(q), y_{\lambda_2}(q) \in R$, the **local shadow-price ordering** at $q$ is:*

$$
  \lambda_1 \;\preceq_q\; \lambda_2
  \;\iff\;
  \exists\, U \ni q\;\text{open such that}\;
  |y_{\lambda_1}(q')| \;\leq\; |y_{\lambda_2}(q')|
  \;\;\forall q' \in U.
$$

*We read this as: "$\lambda_1$ has at most the energy of $\lambda_2$ on a neighborhood of $q$".*
<!-- FILE_END: local-shadow-ordering.md -->

<!-- FILE_START: shadow-price-continuity.md -->
**Proposition.**
*Each shadow price $u_\lambda(q) = w_\lambda(q)/d_\lambda(q) - 1/[k]_q!$ is a **rational function** of $q$ over the base ring, with denominator $[k]_q! \cdot d_\lambda(q)$. On the generic locus $\{q : [k]_q! \cdot d_\lambda(q) \neq 0\}$, $u_\lambda$ is continuous in $q$ (smooth in the $\mathbb{R}$ realisation, $p$-adic continuous in $\mathbb{Q}_p$, well-defined Zariski on $\mathbb{F}_p$).*

*By continuity, if $|y_{\lambda_1}(q)| < |y_{\lambda_2}(q)|$ strictly, then the [local shadow-price ordering](#def:local-shadow-ordering) $\lambda_1 \preceq_q \lambda_2$ holds on a neighborhood.*
<!-- FILE_END: shadow-price-continuity.md -->

<!-- FILE_START: phase-boundary-variety.md -->
**Proposition.**
*The locus*

$$
  \mathcal{B}_{\lambda_1, \lambda_2}
  \;:=\;
  \{q \in Q : |y_{\lambda_1}(q)| = |y_{\lambda_2}(q)|\}
$$

*is a **Zariski-closed** subvariety of $Q$, generically of codimension $\geq 1$ (defined by the polynomial equation $y_{\lambda_1}^2(q) = y_{\lambda_2}^2(q)$). The full **phase-boundary variety** is*

$$
  \mathcal{B}
  \;:=\;
  \bigcup_{\lambda_1 \neq \lambda_2}
    \mathcal{B}_{\lambda_1, \lambda_2}
  \;\cup\;
  \bigcup_\lambda
    \{q : u_\lambda(q) = 0\}.
$$

*This is the union of pairwise-equality varieties and shadow-price-vanishing varieties. $\mathcal{B}$ has measure zero in $Q$.*
<!-- FILE_END: phase-boundary-variety.md -->

<!-- FILE_START: confinement-local-constancy.md -->
**Proposition.**
*The [confinement level](#def:confinement-level) $\ell(K, q)$ is **locally constant** on $Q \setminus \mathcal{B}$. For any $q \notin \mathcal{B}$, there exists an open $U \ni q$ such that $\ell(K, q') = \ell(K, q)$ for all $q' \in U$. The level changes only at points of the [phase-boundary variety](#prop:phase-boundary-variety) $\mathcal{B}$ — these correspond exactly to the **categorical phase boundaries**.*
<!-- FILE_END: confinement-local-constancy.md -->

<!-- FILE_START: shadow-ordering-compute-shortcut.md -->
**Remark (computational shortcut from local constancy).**
Following the [unstable-atom](#def:unstable-atom) "Computational shortcut", we restrict expensive computations (per-generator $\hat V_i^{\mathrm{full}}$ extraction in the tower formula [mass-endomorphism-tower](#prop:mass-endomorphism-tower)) to exact evaluation only at points of the [phase-boundary variety](#prop:phase-boundary-variety) $\mathcal{B}$. In the complement $Q \setminus \mathcal{B}$, all shadow prices, the filtration, and the per-generator data are locally constant (by [local constancy of confinement](#prop:confinement-local-constancy)). Linear interpolation between nearest magic-number anchors is mathematically justified.
<!-- FILE_END: shadow-ordering-compute-shortcut.md -->

<!-- FILE_START: selection-rule-anchors-c1-c3.md -->
**Proposition (selection-rule anchors at c=1 and c=3).**

*Let $q \in \mathbb{R}_{>0}$ and let $h := q - q^{-1}$. The per-component selection rule*

$$
  \mathrm{lw}(c)(q) \;:=\; \frac{1}{c+1} \sum_{\lambda \vdash (c+1)} \dim_q V_\lambda
$$

*satisfies the two exact identities:*

$$
  \mathrm{lw}(1)(q) \;=\; 1 \qquad (\text{exactly, } \forall q > 0),
$$

$$
  \mathrm{lw}(3)(q) \;=\; \frac{3q^2 + 4 + 3q^{-2}}{4} \;=\; \frac{5}{2} + \frac{3}{4} h^2.
$$

*These form the muon (c=1, knot) and the proton (c=3, Borromean 3-link) anchors of the per-component selection rule.*

## Significance

The zero-parameter selection rule reads $\mathrm{lw}(L) = \frac{1}{c+1}\sum_{\lambda\vdash(c+1)} \dim_q V_\lambda$, where $c$ is the number of link components. The c=1 case must equal 1 for all $q$ (muon, a knot, framework `linking_weight = 1`). The c=3 case must equal the Family-A formula $\frac{5}{2} + \frac{3}{4}h^2$ (proton). This proposition Lean-formalises both identities. It grants the selection rule's two anchors derivation-tight status (they are not a fit; both follow from the q-deformed hook-length formula).

## Lean proof structure

We provide two purely algebraic identities at the symbolic level, each closed by `field_simp; ring`:

1. **c=1 anchor** (`selection_rule_c1_eq_one`):
   $\frac{1}{2}\bigl( \dim_q V_{(2)} + \dim_q V_{(1,1)} \bigr) = 1$.
   Both q-dimensions equal $1$ (each partition of 2 has a hook product equal to the q-factorial), so the average is exactly 1.
2. **c=3 anchor** (`selection_rule_c3_eq_family_a`):
   $\frac{1}{4} \bigl( \dim_q V_{(4)} + \dim_q V_{(3,1)} + \dim_q V_{(2,2)} + \dim_q V_{(2,1,1)} + \dim_q V_{(1,1,1,1)} \bigr) = (3q^2 + 4 + 3q^{-2})/4$.

   Using the explicit q-hook formula:
   - $\dim_q V_{(4)} = \dim_q V_{(1,1,1,1)} = 1$
   - $\dim_q V_{(3,1)} = \dim_q V_{(2,1,1)} = [3]_q = q^2 + 1 + q^{-2}$
   - $\dim_q V_{(2,2)} = [4]_q / [2]_q = q^2 + q^{-2}$

   Their sum is $1 + (q^2{+}1{+}q^{-2}) + (q^2{+}q^{-2}) + (q^2{+}1{+}q^{-2}) + 1 = 4 + 3q^2 + 3q^{-2}$. Dividing by 4 yields the stated form. The $h^2$ form follows from $q^2 + q^{-2} = h^2 + 2$.

   Both steps operate as pure polynomial identities in $\mathbb{Z}[q, q^{-1}]$. They close by `ring` after `field_simp` clears the $q^{-1}$ denominators.

## q-usage discipline

This holds over real $q > 0$ (the substrate-anchor regime). Both identities are q-rational, fibre-level constructs. The c=1 case holds for ALL $q > 0$ (an infinite set of constraints, not a single point). It is AGENTS.md §7c-compliant.

## Cross-references

- $\operatorname{def:coulomb-charge}$ — introduces the $h = q - q^{-1}$ structure at the per-crossing level.
- $\operatorname{prop:coulomb-strong-ratio-q-rational}$ — companion identity proving $\tanh(\ln q) = (q^2-1)/(q^2+1)$ over real $q > 0$.
- Derivation audit doc: [`docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md`](../../../docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md).
<!-- FILE_END: selection-rule-anchors-c1-c3.md -->

<!-- FILE_START: selection-rule-c2-prediction.md -->
**Proposition (selection-rule at c=2 — prediction).**

*Let $q \in \mathbb{R}_{>0}$. The per-component selection rule ([`prop:selection-rule-anchors-c1-c3`](#prop:selection-rule-anchors-c1-c3)) applied at $c=2$ yields the closed form:*

$$
  \mathrm{lw}(2)(q) \;:=\; \frac{1}{3} \sum_{\lambda \vdash 3} \dim_q V_\lambda
  \;=\; \frac{2 + [2]_q}{3} \;=\; \frac{(q+1)^2}{3q}.
$$

*This supplies the rule's prediction for a 2-component link (e.g. the Hopf link). The closed form is a finite Laurent rational over $\mathbb{Z}[q, q^{-1}]$. Like the c=1 and c=3 anchors, it is derivation-tight (no fit, zero free parameters).*

## Significance

The per-component rule states $\mathrm{lw}(c) = (1/(c+1)) \sum_{\lambda \vdash (c+1)} \dim_q V_\lambda$. It is anchored at c=1 (muon, $\mathrm{lw}=1$ exactly $\forall q$) and c=3 (proton, $\mathrm{lw} = 5/2 + (3/4)h^2$ via Family-A). The c=2 case provides the **first testable prediction** of the rule beyond the two known anchors.

This proposition Lean-formalises the closed form for c=2. The prediction shares the same provenance as its anchors (a pure algebraic identity in the q-deformed hook-length formula). Any independent determination of a 2-component link's linking_weight—such as a Hopf-link or gluon EM-linking application—can be tested against this exact formula unequivocally.

## Lean proof structure

We rely on a single algebraic identity at the symbolic level:

$$
  \frac{1}{3} \bigl( \dim_q V_{(3)} + \dim_q V_{(2,1)} + \dim_q V_{(1,1,1)} \bigr)
  \;=\; \frac{(q+1)^2}{3q}.
$$

Using the explicit q-hook values for partitions of 3:

- $\dim_q V_{(3)} = 1$ (single-row Young diagram, all hooks contribute trivially)
- $\dim_q V_{(2,1)} = [2]_q = q + q^{-1}$ (standard rep at H_3; q-hook computation)
- $\dim_q V_{(1,1,1)} = 1$ (single-column, conjugate of $V_{(3)}$)

Their sum is $2 + q + q^{-1}$. Dividing by 3 yields $(2 + q + q^{-1})/3 = (q^2 + 2q + 1)/(3q) = (q+1)^2/(3q)$.

This constitutes a pure polynomial-ring identity once we clear $q^{-1}$ denominators. We close it by `field_simp; ring` over $\mathbb{R}_{>0}$.

## q-usage discipline

This holds over real $q > 0$ (substrate-anchor regime). The closed form $(q+1)^2/(3q)$ is a Laurent rational in $\mathbb{Z}[q, q^{-1}]$ — a fibre-level construction. At $q = q_0$, it evaluates to $\approx 1.337$. There is no $|q|=1$ step; both $q$ and $q^{-1}$ are real positive at any real $q > 0$. It is AGENTS.md §7c-compliant.

## Cross-references

- [`prop:selection-rule-anchors-c1-c3`](#prop:selection-rule-anchors-c1-c3) — the two known anchors that establish the rule's existence.
- Derivation audit: [`docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md`](../../../docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md).
<!-- FILE_END: selection-rule-c2-prediction.md -->

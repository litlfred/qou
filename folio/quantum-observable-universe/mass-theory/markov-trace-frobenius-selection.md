*Let $R \supseteq \mathbb{Q}(q)$ with $q$ generic; write $[m]_q = (q^m - q^{-m})/(q - q^{-1})$, so that $[2]_q = q + q^{-1}$. A **Markov trace** on the tower $H_1 \subset H_2 \subset \cdots$ is a compatible family of linear functionals $\tau_n \colon H_n(R,q) \to R$ satisfying M1 ($\tau(1) = 1$), M2 (cyclicity, $\tau(xy) = \tau(yx)$) and M3 ($\tau(x \sigma_{n-1}) = z \, \tau(x)$ for $x \in H_{n-1}$), for a parameter $z \in R$.*

**(i) Uniqueness at a fixed parameter.** *For each $z$ there is exactly one Markov trace on the tower with that parameter, the Ocneanu–Jones trace $\mathrm{tr}^{z}_M$. This follows from M1–M3 alone. Non-degeneracy of the induced pairing is neither a hypothesis nor a conclusion of it, and cannot serve as the selection criterion: on the split semisimple $H_n(R,q)$ **every** weight vector $(w_\lambda)_{\lambda \vdash n}$ with all $w_\lambda \neq 0$ induces a non-degenerate associative form, so "non-degenerate" singles out nothing — and in particular does not fix $z$.*

**(ii) Selection of the parameter in the QOU mass channel.** *What fixes $z$ is not non-degeneracy but a prescribed degeneracy. The mass fibre is the fundamental $V$ of $\mathrm{SU}_q(2)$, of quantum dimension $[2]_q$, so $V^{\otimes n}$ carries no channel $\lambda$ with $\ell(\lambda) \geq 3$ ([eigenbasis decomposition](#lem:feynman-eigenbasis-decomposition)). A trace that is the categorical trace of the fibre action therefore puts weight $y_\lambda = 0$ on every such $\lambda$ (the **row cap**) and nonzero weight on the channels the fibre does supply (**faithfulness on the two-row blocks**). Imposed at level $3$ — the first level at which the row cap says anything — those two conditions, together with M1–M3 at an unknown $z$, determine everything:*

$$
  y_{(n-k,\,k)} \;=\; \frac{[\,n-2k+1\,]_q}{[2]_q^{\,n}},
  \qquad
  y_\lambda \;=\; 0 \ \ (\ell(\lambda) \geq 3),
  \qquad
  z \, [2]_q \;=\; q^{2},
$$

*that is, $z = q^{3}/(q^{2}+1)$ — **convention D** of the [trace-convention registry](../../../docs/coordination/trace-convention-registry.md). Neither condition may be dropped: without the row cap $z$ is free (the whole Ocneanu family, convention C among it), and without faithfulness the trivial character $y = (1, 0, \ldots, 0)$ at $z = q$ satisfies M1–M3 and the row cap alike.*

**(iii) What the pairing then is.** *Consequently $\langle x, y \rangle_\tau := \mathrm{tr}_M(xy)$ is **degenerate** on $H_n(R,q)$ for $n \geq 3$, and the radical of the form (not the Jacobson radical — $H_n$ is split semisimple at generic $q$) is exactly the Temperley–Lieb ideal $I_n = \ker\bigl(H_n(q) \twoheadrightarrow \mathrm{TL}_n(q)\bigr)$, neither larger nor smaller. $\mathrm{tr}_M$ vanishes identically on $I_n$, so it is still determined on all of $H_n(R,q)$ — uniqueness is on the nose, not merely modulo the radical — and it descends to a non-degenerate pairing on the quotient. It is $(\mathrm{TL}_n(q), \mathrm{tr}_M)$, not $(H_n(R,q), \mathrm{tr}_M)$, that is a symmetric Frobenius algebra.*

**Status.** *(i) and (iii) are unconditional. (ii) is an implication whose antecedent — that the mass-channel trace is the categorical trace of the fibre action on $V^{\otimes n}$ — is **open**; the implication itself is proved at $n = 3$. Its extension to $n > 3$ rests on the restriction property together with the closed form above, which is verified against every partition of $n \leq 7$ to a worst residual of $1.34 \times 10^{-51}$ and proved only as fixed-$n$ instances of the recursion $[m+2]_q + [m]_q = [2]_q [m+1]_q$, not by a general-$n$ induction.*

| form | $\tau(1)$ | $z = \tau(\sigma_i)$ | $y_\lambda$ | radical of $\langle \cdot, \cdot \rangle_\tau$ | non-degenerate? |
|---|---:|---:|---|---|---|
| Jones–Markov $\mathrm{tr}_M$, **convention D** | $1$ | $q^{3}/(q^{2}+1)$ | $y_{(n-k,k)} = [\,n-2k+1\,]_q / [2]_q^{\,n}$; $y_\lambda = 0$ for $\ell(\lambda) \geq 3$ | the Temperley–Lieb ideal $I_n$ (zero for $n \leq 2$) | **no** on $H_n(q)$; **yes** on $\mathrm{TL}_n(q) = H_n(q)/I_n$ |

## Proof

The chain from the QOU substrate to the Markov trace runs through four
steps:

### Step 1: Cat-action of $\mathbf{C}$ on the state bundle

A quantum observable universe specifies a rigid monoidal category $\mathbf{C}$ with a fibre functor $\tau \colon \mathbf{C} \to \mathbf{Vect}$. The category fixes the acting Frobenius–Hopf algebra $A$. The typical case is $A = H_n(R, q)$.

### Step 2: Non-abelian Stokes at finite slice

Yekutieli's non-abelian Stokes theorem at finite slice depth yields the multiplicative trace on the closed surface obtained by Markov closure of the braid word $T_w$:

$$
  \int_{S^1} T_w
  \;=\;
  \mathrm{tr}\bigl(\rho(\sigma_{i_1}) \cdots \rho(\sigma_{i_\ell})\bigr).
$$
This trace is the categorical trace in $\mathbf{C}$. It depends on the fibre functor $\tau$.

### Step 3: Frobenius pairing

The categorical trace descends to an integral $\int_A \colon A \to R$, defining the symmetric associative bilinear form

$$
  \langle x, y \rangle_\tau \;:=\; \tau(xy).
$$

Under the row cap this form is **not** non-degenerate on $A = H_n(R,q)$: its radical is the Temperley–Lieb ideal $I_n$, and it is the quotient $\mathrm{TL}_n(q) = A/I_n$ that is Frobenius relative to the induced integral.

The QOU mass identity uses the Frobenius co-Casimir trace identity: for a self-dual Frobenius algebra $A = H_n(R, q)$ with Markov trace $\tau$ and $\tau(p_\lambda) \neq 0$ for every central idempotent $p_\lambda$, the quantum-co-dimension element $C_{\dim_q} := \sum_{\lambda \in \widehat{A}} \frac{1}{\dim_q(\lambda) \cdot \tau(p_\lambda)} \cdot p_\lambda \in Z(A)$ satisfies

$$
  \tau(C_{\dim_q}) \;=\; \sum_\lambda \frac{1}{\dim_q(\lambda)}.
$$

> **Open.** As written, $C_{\dim_q}$ divides by $\tau(p_\lambda)$ and the sum runs over *every* Wedderburn block, so under convention D the element is **undefined**: $\tau(p_\lambda) = 0$ for every $\lambda$ with $\ell(\lambda) \geq 3$. Two ways out, with different costs.
>
> **(a) Restrict to the radical quotient.** Read $C_{\dim_q}$ and the identity on $\mathrm{TL}_n(q) = H_n(q)/I_n$, i.e. sum only over $\ell(\lambda) \leq 2$. The identity then holds verbatim with a smaller right-hand side. **Cost:** every published value computed through the co-Casimir — in particular Term 4 of the six-term mass identity, $\mathrm{tr}(G^{-1} \cdot D)$ — is computed on a different index set and must be **republished**, regenerated by its producer.
>
> **(b) Retire the co-Casimir route.** Drop it alongside the refuted Frobenius / co-Casimir deuteron result. **Cost:** Term 4 loses its derivation and the six-term identity is reduced to five derived terms plus a gap.
>
> Until this is decided, no Term-4 number in the corpus is to be edited, and no block may assert that the co-Casimir identity holds on $H_n(R,q)$ under convention D.

The **Jones–Markov form** $\mathrm{tr}_M$ satisfies:
- $\mathrm{tr}_M(1) = 1$.
- $\mathrm{tr}_M(x \sigma_{n-1}) = z \cdot \mathrm{tr}_M(x)$ for $x \in H_{n-1}$, with $z = q^{3}/(q^{2}+1)$ (**convention D**; the value is derived in Step 3b of the proof, not stipulated).

Its block weights are $\mathrm{tr}_M(p_\lambda) = y_\lambda$, given by the Ocneanu hook–content product at framing ratio $a^2 = z / z_{-}$, where $z_{-} = z - (q - q^{-1})$. Under convention D that ratio is exactly $q^{4}$, since $z_{-} = 1/(q(q^{2}+1))$ and hence $z / z_{-} = q^{4}$ identically in $q$. The numerator factor $z \, q^{c(x)} - z_{-} \, q^{-c(x)}$ therefore vanishes precisely on cells of content $c(x) = -2$ — the cells in position $(r+2, r)$, the first of which is $(3,1)$ — and a Young diagram contains such a cell if and only if $\ell(\lambda) \geq 3$. Hence $y_\lambda = 0 \iff \ell(\lambda) \geq 3$: the row cap is not an extra input to the weight formula but a reading of it, and the vanishing set is *exactly* the Temperley–Lieb ideal. The Markov-trace uniqueness theorem then fixes $\mathrm{tr}_M$ among traces with this $z$; it says nothing about non-degeneracy.

### Step 4: Wedderburn + Markov-trace formula

The trace $\mathrm{tr}_M$ admits the explicit form:

$$
  \mathrm{tr}_M(x) \;=\; \sum_\lambda y_\lambda(q) \cdot \chi_\lambda(x),
$$
where the sum runs over $\lambda \vdash n$ with $\ell(\lambda) \leq 2$ — every other character is annihilated — and $y_{(n-k,k)} = [\,n-2k+1\,]_q / [2]_q^{\,n}$. Equivalently $\mathrm{tr}_M$ factors through $\mathrm{TL}_n(q)$, whose dimension is $\mathrm{Catalan}(n)$ \cite{kimlee2018}, and the surviving blocks carry $\sum d_\lambda^2 = \mathrm{Catalan}(n)$ of the $n!$ dimensions of $H_n(q)$.

## Selection theorem

**Theorem (Markov-trace selection).** *Let $\tau$ be a cyclic functional on the tower satisfying M1 and M3 for **some** parameter $z$, and let $(w_\lambda)_{\lambda \vdash 3}$ be its level-$3$ weight vector. Suppose*

1. *(**row cap**) $w_\lambda = 0$ whenever $\ell(\lambda) \geq 3$, and*
2. *(**faithfulness on the quotient**) $w_\lambda \neq 0$ whenever $\ell(\lambda) \leq 2$.*

*Then $z$ is forced to satisfy $z \, [2]_q = q^{2}$, and $\tau = \mathrm{tr}_M$, the convention-D Jones–Markov trace, at every level of the tower — **on all of** $H_n(R,q)$, not merely modulo the radical, because $\tau$ is identically zero on the radical. The radical of $\langle \cdot, \cdot \rangle_\tau$ is exactly $I_n$, and the descended pairing on $\mathrm{TL}_n(q)$ is non-degenerate.*

*Level $3$ is where the hypotheses bite, and the statement is false if they are imposed lower: at $n \leq 2$ the row cap is vacuous and M1 + M3 leave one free parameter, so $z$ is genuinely undetermined there. Given level $3$, no higher level adds freedom — the restriction of a level-$n$ Markov trace to $H_3(R,q)$ is again a Markov trace with the same $z$.*

*Both hypotheses are load-bearing and neither is redundant. Dropping 1 leaves $z$ free (the full Ocneanu family, convention C among it). Dropping 2 admits the trivial character $y = (1, 0, 0)$ at $z = q$, which satisfies M1–M3 and the row cap and makes the conclusion **false**, not merely unprovable. Dropping M1 / M3 admits, at $n = 3$, the entire two-parameter family $\{(y_{(3)}, y_{(2,1)}, 0) : y_{(2,1)} \neq 0\}$ — so hypotheses 1 and 2 alone do **not** single out $\mathrm{tr}_M$; the Markov axioms are still required.*

*Proved at $n = 3$, division-free, over a generic commutative domain, together with the corresponding statement from the fibre-side antecedent.*

## Discussion

This proposition is a structural theorem about the representation theory of the Hecke algebra. No fitting or empirical input enters, and no numerical $q_0$: parts (i) and (iii) are unconditional, and part (ii) is division-free over a generic commutative domain. What it is **conditional** on is one named categorical premise — that the mass-channel trace is the categorical trace of the fibre action on $V^{\otimes n}$ — which is open. Conditional-proved is not premise-established.

## Computational consequence

The QOU production stack computes $\mathrm{tr}_M$ on the canonical atomic word — 11 letters on 3 strands for the two $A = 1$ atoms, 23 on 6 strands for the deuteron — through two independent colour-weighted paths: the Gröbner-Shirshov reduction and the Frobenius combiner $\sum_\lambda y_\lambda \chi^\lambda$. At the proton-pinned $q_0$, in **production convention D** — SU(2)/Temperley–Lieb (Jones), $z = q^3/(q^2+1)$, [registry](../../../docs/coordination/trace-convention-registry.md) id **D**, `forcing_status: forced-given-premise`:

| atom | $\mathrm{tr}_M(\beta_{\rm atom}, q_0)$ | peel vs combiner |
|---|---:|---:|
| proton | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.0.tr_M_at_q0_50dps | precision: 17 }}$ | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.0.peel_cross_check.abs_diff_vs_bridge | precision: 3 | scientific }}$ |
| neutron | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.1.tr_M_at_q0_50dps | precision: 17 }}$ | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.1.peel_cross_check.abs_diff_vs_bridge | precision: 3 | scientific }}$ |
| deuteron | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.2.tr_M_at_q0_50dps | precision: 17 }}$ | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.2.peel_cross_check.abs_diff_vs_bridge | precision: 3 | scientific }}$ |

The agreement column is the residual between those two paths at 50 dps, and it sits at the serialization floor rather than at any tolerance the computation imposes; the L1 target is $1$ ppQ ($10^{-15}$), which it clears by 35 orders.

> **Two scope notes on the cross-check, both material.** *(i)* Two **further** paths exist — Hoefsmit (Rust canonical-$\chi$) and Habiro — and the four-way cross-check compares all four, but those two legs are **colour-blind**: they carry no $\delta$ colour split, so they diverge from the colour-weighted pair by up to $3.24\times 10^{-9}$ (measured on a fresh gate run, worst case the deuteron), which the gate reports as its `(cb≠)` status rather than as a failure. The $1$ ppQ certification therefore rests on the **two** colour-weighted paths tabulated above, not on a four-way agreement. *(ii)* That gate is **muon-canonical** — it refuses to run off the ideal CAL-2 pin — so it certifies at $q_0^{(\mu)}$, while the table above is evaluated at the canonical proton pin. The two pins differ by $11.6$ ppb (measured against the CODATA-2022 muon pin), which is the $\mu$–p substrate tension and is far above the agreement column; do not read the two as one measurement.

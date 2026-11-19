*Let $R \supseteq \mathbb{Q}(q)$ with $q$ generic; write $[m]_q = (q^m - q^{-m})/(q - q^{-1})$, so that $[2]_q = q + q^{-1}$. A **Markov trace** on the tower $H_1 \subset H_2 \subset \cdots$ is a compatible family of linear functionals $\tau_n \colon H_n(R,q) \to R$ satisfying M1 ($\tau(1) = 1$), M2 (cyclicity, $\tau(xy) = \tau(yx)$) and M3 ($\tau(x \sigma_{n-1}) = z \, \tau(x)$ for $x \in H_{n-1}$), for a parameter $z \in R$.*

**(i) Uniqueness at a fixed parameter.** *For each $z$ there is exactly one Markov trace on the tower with that parameter, the Ocneanu–Jones trace $\mathrm{tr}^{z}_M$. This follows from M1–M3 alone. Non-degeneracy of the induced pairing is neither a hypothesis nor a conclusion of it, and cannot serve as the selection criterion: on the split semisimple $H_n(R,q)$ **every** weight vector $(w_\lambda)_{\lambda \vdash n}$ with all $w_\lambda \neq 0$ induces a non-degenerate associative form, so "non-degenerate" singles out nothing, and in particular does not fix $z$.*

**(ii) Selection of the parameter in the QOU mass channel.** *What fixes $z$ is not non-degeneracy but a prescribed degeneracy. The mass fibre is the fundamental $V$ of $\mathrm{SU}_q(2)$, of quantum dimension $[2]_q$, so $V^{\otimes n}$ carries no channel $\lambda$ with $\ell(\lambda) \geq 3$ ([eigenbasis decomposition](#lem:feynman-eigenbasis-decomposition)). A trace that is the categorical trace of the fibre action therefore puts weight $y_\lambda = 0$ on every such $\lambda$ (the **row cap**) and nonzero weight on the channels the fibre does supply (**faithfulness on the two-row blocks**). Imposed at level $3$ (the first level at which the row cap says anything), those two conditions, together with M1–M3 at an unknown $z$, determine everything:*

$$
  y_{(n-k,\,k)} \;=\; \frac{[\,n-2k+1\,]_q}{[2]_q^{\,n}},
  \qquad
  y_\lambda \;=\; 0 \ \ (\ell(\lambda) \geq 3),
  \qquad
  z \, [2]_q \;=\; q^{2},
$$

*that is, $z = q^{3}/(q^{2}+1)$ (**convention D**). Neither condition may be dropped: without the row cap $z$ is free (the whole Ocneanu family, convention C among it), and without faithfulness the trivial character $y = (1, 0, \ldots, 0)$ at $z = q$ satisfies M1–M3 and the row cap alike.*

**(iii) What the pairing then is.** *Consequently $\langle x, y \rangle_\tau := \mathrm{tr}_M(xy)$ is **degenerate** on $H_n(R,q)$ for $n \geq 3$, and the radical of the form (distinct from the Jacobson radical, as $H_n$ is split semisimple at generic $q$) is exactly the Temperley–Lieb ideal $I_n = \ker\bigl(H_n(q) \twoheadrightarrow \mathrm{TL}_n(q)\bigr)$, neither larger nor smaller. $\mathrm{tr}_M$ vanishes identically on $I_n$, so it is still determined on all of $H_n(R,q)$ (uniqueness holds on the nose rather than merely modulo the radical), and it descends to a non-degenerate pairing on the quotient. It is $(\mathrm{TL}_n(q), \mathrm{tr}_M)$, rather than $(H_n(R,q), \mathrm{tr}_M)$, that is a symmetric Frobenius algebra.*

**Scope.** *(i) and (iii) are unconditional. (ii) is an implication whose antecedent (that the mass-channel trace is the categorical trace of the fibre action on $V^{\otimes n}$) is **open**; the implication itself is established algebraically at $n = 3$. Its extension to $n > 3$ rests on the restriction property together with the closed form above, which is verified against every partition of $n \leq 7$ to a worst residual of $1.34 \times 10^{-51}$ and established as fixed-$n$ instances of the recursion $[m+2]_q + [m]_q = [2]_q [m+1]_q$.*

| form | $\tau(1)$ | $z = \tau(\sigma_i)$ | $y_\lambda$ | radical of $\langle \cdot, \cdot \rangle_\tau$ | non-degenerate? |
|---|---:|---:|---|---|---|
| Jones–Markov $\mathrm{tr}_M$, **convention D** | $1$ | $q^{3}/(q^{2}+1)$ | $y_{(n-k,k)} = [\,n-2k+1\,]_q / [2]_q^{\,n}$; $y_\lambda = 0$ for $\ell(\lambda) \geq 3$ | the Temperley–Lieb ideal $I_n$ (zero for $n \leq 2$) | **no** on $H_n(q)$; **yes** on $\mathrm{TL}_n(q) = H_n(q)/I_n$ |

## Proof

The chain from the QOU aether to the Markov trace runs through four
steps:

### Step 1: Cat-action of $\mathbf{C}$ on the state bundle

A quantum observable universe specifies a rigid monoidal category $\mathbf{C}$ with a fibre functor $\tau \colon \mathbf{C} \to \mathbf{Vect}$. The category fixes the acting Frobenius–Hopf algebra $A$, typically taken to be $A = H_n(R, q)$.

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

The QOU mass identity uses the Frobenius co-Casimir trace identity ([Frobenius co-Casimir universal](#thm:frobenius-codim-universal)):

$$
  \tau(C_{\dim_q}) \;=\; \sum_\lambda \frac{1}{\dim_q(\lambda)}.
$$

> **Co-Casimir domain under convention D.** Written as a sum over *every* Wedderburn block of $H_n(R,q)$, the element $C_{\dim_q}$ divides by $\tau(p_\lambda)$ and is **undefined** under convention D whenever $n \geq 3$, because $\tau(p_\lambda) = 0$ for every partition with $\ell(\lambda) \geq 3$. Restricting $C_{\dim_q}$ and its trace identity to the radical quotient $\mathrm{TL}_n(q) = H_n(q)/I_n$ (summing only over $\ell(\lambda) \leq 2$) restores a well-defined identity on the two-row blocks (compare [Gram-matrix spectral connection](#rem:gram-matrix-spectral-connection)), whereas omitting the co-Casimir term altogether leaves Term 4 of the six-term mass decomposition open.

The **Jones–Markov form** $\mathrm{tr}_M$ satisfies:
- $\mathrm{tr}_M(1) = 1$.
- $\mathrm{tr}_M(x \sigma_{n-1}) = z \cdot \mathrm{tr}_M(x)$ for $x \in H_{n-1}$, with $z = q^{3}/(q^{2}+1)$ (**convention D**; the value is derived in Step 3b of the proof, not stipulated).

Its block weights are $\mathrm{tr}_M(p_\lambda) = y_\lambda$, given by the Ocneanu hook–content product at framing ratio $a^2 = z / z_{-}$, where $z_{-} = z - (q - q^{-1})$. Under convention D that ratio is exactly $q^{4}$, since $z_{-} = 1/(q(q^{2}+1))$ and hence $z / z_{-} = q^{4}$ identically in $q$. The numerator factor $z \, q^{c(x)} - z_{-} \, q^{-c(x)}$ therefore vanishes precisely on cells of content $c(x) = -2$ (the cells in position $(r+2, r)$, the first of which is $(3,1)$), and a Young diagram contains such a cell if and only if $\ell(\lambda) \geq 3$. Hence $y_\lambda = 0 \iff \ell(\lambda) \geq 3$: the row cap is not an extra input to the weight formula but a reading of it, and the vanishing set is *exactly* the Temperley–Lieb ideal. The Markov-trace uniqueness theorem then fixes $\mathrm{tr}_M$ among traces with this $z$; it says nothing about non-degeneracy.

### Step 4: Wedderburn + Markov-trace formula

The trace $\mathrm{tr}_M$ admits the explicit form:

$$
  \mathrm{tr}_M(x) \;=\; \sum_\lambda y_\lambda(q) \cdot \chi_\lambda(x),
$$
where the sum runs over $\lambda \vdash n$ with $\ell(\lambda) \leq 2$ (every other character is annihilated) and $y_{(n-k,k)} = [\,n-2k+1\,]_q / [2]_q^{\,n}$. Equivalently $\mathrm{tr}_M$ factors through $\mathrm{TL}_n(q)$, and the surviving blocks carry $\sum d_\lambda^2 = \mathrm{Catalan}(n)$ of the $n!$ dimensions of $H_n(q)$ (verified explicitly at $n = 3, 4, 5$).

## Selection theorem

**Theorem (Markov-trace selection).** *Let $\tau$ be a cyclic functional on the tower satisfying M1 and M3 for **some** parameter $z$, and let $(w_\lambda)_{\lambda \vdash 3}$ be its level-$3$ weight vector. Suppose*

1. *(**row cap**) $w_\lambda = 0$ whenever $\ell(\lambda) \geq 3$, and*
2. *(**faithfulness on the quotient**) $w_\lambda \neq 0$ whenever $\ell(\lambda) \leq 2$.*

*Then $z$ is forced to satisfy $z \, [2]_q = q^{2}$, and $\tau = \mathrm{tr}_M$, the convention-D Jones–Markov trace, at every level of the tower, **on all of** $H_n(R,q)$ rather than merely modulo the radical, because $\tau$ is identically zero on the radical. The radical of $\langle \cdot, \cdot \rangle_\tau$ is exactly $I_n$, and the descended pairing on $\mathrm{TL}_n(q)$ is non-degenerate.*

*Level $3$ is where the hypotheses bite, and the statement is false if they are imposed lower: at $n \leq 2$ the row cap is vacuous and M1 + M3 leave one free parameter, so $z$ is genuinely undetermined there. Given level $3$, no higher level adds freedom: the restriction of a level-$n$ Markov trace to $H_3(R,q)$ is again a Markov trace with the same $z$.*

*Both hypotheses are load-bearing and neither is redundant. Dropping 1 leaves $z$ free (the full Ocneanu family, convention C among it). Dropping 2 admits the trivial character $y = (1, 0, 0)$ at $z = q$, which satisfies M1–M3 and the row cap and makes the conclusion **false** rather than merely unprovable. Dropping M1 / M3 admits, at $n = 3$, the entire two-parameter family $\{(y_{(3)}, y_{(2,1)}, 0) : y_{(2,1)} \neq 0\}$, so hypotheses 1 and 2 alone do **not** single out $\mathrm{tr}_M$; the Markov axioms are still required.*

*This $n = 3$ uniqueness theorem holds division-free over any generic commutative domain.*

## Discussion

This proposition is a structural theorem about the representation theory of the Hecke algebra. No fitting, empirical input, or numerical $q_0$ enters: parts (i) and (iii) are unconditional, and part (ii) is division-free over a generic commutative domain. What it is **conditional** on is one named categorical premise (that the mass-channel trace is the categorical trace of the fibre action on $V^{\otimes n}$), which is open. Conditional-proved is not premise-established.

## Numerical verification on light atomic braids

Evaluating $\mathrm{tr}_M$ on the canonical atomic braid words (11 letters on 3 strands for the two $A = 1$ nucleons, 23 on 6 strands for the deuteron) through two independent colour-weighted algorithms, Gröbner–Shirshov reduction (recursive Markov peeling) and the Frobenius character expansion $\sum_\lambda y_\lambda \chi^\lambda$, at the proton-calibrated $q_0$ in **convention D** ($\mathrm{SU}_q(2)$/Temperley–Lieb, $z = q^3/(q^2+1)$) yields:

| atom | $\mathrm{tr}_M(\beta_{\rm atom}, q_0)$ | peel vs combiner |
|---|---:|---:|
| proton | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.0.tr_M_at_q0_50dps | precision: 17 }}$ | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.0.peel_cross_check.abs_diff_vs_bridge | precision: 3 | scientific }}$ |
| neutron | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.1.tr_M_at_q0_50dps | precision: 17 }}$ | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.1.peel_cross_check.abs_diff_vs_bridge | precision: 3 | scientific }}$ |
| deuteron | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.2.tr_M_at_q0_50dps | precision: 17 }}$ | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.2.peel_cross_check.abs_diff_vs_bridge | precision: 3 | scientific }}$ |

The agreement column records the 50-decimal-place residual between the two colour-weighted evaluations, clearing $10^{-15}$ by 35 orders of magnitude.

> **Colour-blind comparison and calibration sensitivity.** *(i)* Evaluating the same braids via unsplit Hoefsmit characters or the Habiro expansion omits the $\delta$ colour splitting and shifts $\mathrm{tr}_M$ by up to $3.24\times 10^{-9}$ (attained on the deuteron), so sub-$10^{-15}$ agreement holds specifically between the two colour-weighted evaluations tabulated above. *(ii)* Evaluating at the muon-calibrated parameter $q_0^{(\mu)}$ rather than the proton-calibrated $q_0$ shifts $q_0$ by $11.6$ ppb (against CODATA 2022), many orders above the $50$-digit algebraic agreement between the two trace evaluations.

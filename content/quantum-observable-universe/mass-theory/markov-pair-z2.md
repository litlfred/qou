Let $H_n(R, q)$ be the Iwahori--Hecke algebra with Markov trace
$\mathrm{tr}_M$ normalised by $\mathrm{tr}_M(1_k) = 1$ for all $k$
and Markov axiom $\mathrm{tr}_M(x\sigma_{k-1}) = z\,\mathrm{tr}_M(x)$
for $x \in H_{k-1}(q)$, where
$z = q^{3}/(q^{2}+1)$ (**convention D**, [Jones--Markov trace](#thm:jones-markov-trace)).

**Proposition.** For every pair of braid generators
$\sigma_i, \sigma_j$ with $0 \le i < j$, embedded in any
$H_n(R, q)$ with $n > j$,

$$
  \mathrm{tr}_M(\sigma_i\sigma_j) \;=\; z^2.
$$

The identity holds whether $(i,j)$ are adjacent ($j = i+1$)
or non-adjacent ($j \ge i+2$).
## Operator interpretation

> **Retracted and replaced, 2026-08-09.** This section read:
>
> > The value $z^2$ is the **Jones polynomial of the Hopf link** (unknotted
> > two-component linking) evaluated at the substrate parameter:
> > $J_{\mathrm{Hopf}}(q) = -(q^{1/2} + q^{-1/2})\cdot z^2
> > = -(q + q^{-1})/(q^{1/2} + q^{-1/2})$.
>
> That is wrong three times over, and only the third is about the convention.
>
> 1. **Wrong link.** $z^2 = \mathrm{tr}_M(\sigma_i\sigma_j)$. The closure of
>    $\sigma_1\sigma_2$ in $B_3$ is the **unknot**; the closure of
>    $\sigma_1\sigma_3$ in $B_4$ is the **two-component unlink**. Neither is the
>    Hopf link, which is the closure of $\sigma_1^2$ in $B_2$ and has trace
>    $\mathrm{tr}_M(\sigma_1^2) = hz + 1$, not $z^2$.
> 2. **Wrong kind of object.** A raw Markov-trace value is not a Jones
>    polynomial. Without the loop factor $\delta^{\,n-1}$ and the framing
>    correction it is not even an invariant of the closure — it changes under
>    Markov stabilisation, which is exactly what $z$ measures.
> 3. **Wrong loop parameter.** $q^{1/2}+q^{-1/2}$ is $[2]_{\sqrt q} = 2.0027\ldots$
>    at $q_0$; the Temperley–Lieb loop value of the production trace is
>    $\delta = [2]_q = q+q^{-1} = 2.010896866707122\ldots$ — the same conflation
>    as $1/\delta = 0.4972905456\ldots$ against the excised
>    $z_{\mathrm{C}} = 0.4993203342\ldots$.

**The correct normalisation.** For $\beta \in B_n$ with exponent sum $e$,

$$
  V_{\hat\beta}(t) \;=\; q^{-2e}\,[2]_q^{\,n-1}\,\mathrm{tr}_M(\beta),
  \qquad t = q^{-2},
$$

with **no square roots anywhere**. The reason is that under convention D the
element $e_i := q - \sigma_i$ is a Temperley–Lieb generator,

$$
  e_i^2 \;=\; q^2 - 2q\sigma_i + \sigma_i^2 \;=\; (q^2+1) - (q+q^{-1})\sigma_i
       \;=\; [2]_q\,e_i ,
$$

and convention D is *precisely* the statement that $\mathrm{tr}_M(e_i) = 1/\delta$:

$$
  \mathrm{tr}_M(e_i) = q - z, \qquad (q-z)\,[2]_q = 1 .
$$

So $\mathrm{tr}_M$ is not merely compatible with the Jones–Temperley–Lieb trace —
written in $e_i$ it **is** that trace, which is what the registry name
"SU(2)/Temperley–Lieb (Jones) decomposition" means as an identity. The Kauffman
variable is $A^2 = -q$, giving $\delta = -A^2-A^{-2}$ and $t = A^{-4} = q^{-2}$;
the odd powers of $A$ in $\rho(\sigma_i) = (A/q)\sigma_i$ cancel against the
writhe factor $(-A^3)^{-e}$, leaving $q^{-2e}$.

Four closures, computed from the formula and checked against their known Jones
polynomials:

| closure | braid | $e$ | $n$ | $\mathrm{tr}_M$ | $V$ from the formula | known |
|---|---|:-:|:-:|---|---|---|
| unknot | $\widehat{\sigma_1}$, $B_2$ | 1 | 2 | $z$ | $1$ | $1$ |
| unknot | $\widehat{\sigma_1\sigma_2}$, $B_3$ | 2 | 3 | $z^2$ | $1$ | $1$ |
| Hopf link | $\widehat{\sigma_1^2}$, $B_2$ | 2 | 2 | $hz+1 = \tfrac{q^4+1}{q^2+1}$ | $q^{-1}+q^{-5}$ | $-t^{1/2}-t^{5/2}$ |
| 2-unlink | $\widehat{\sigma_1\sigma_3}$, $B_4$ | 2 | 4 | $z^2$ | $[2]_q$ | $-t^{1/2}-t^{-1/2}$ |

The last two rows are the point. Rows 2 and 4 have the **same** trace value
$z^2$ and different links; only $n$ distinguishes them. Any account that reads a
Jones polynomial off a raw trace value cannot tell them apart at all — which is
how the retracted sentence came to call the unknot a Hopf link.

For the Hopf row the sign sits entirely in the branch of $t^{1/2}$: with
$t^{1/2} := A^{-2} = -q^{-1}$, $-t^{1/2}-t^{5/2} = q^{-1}+q^{-5}$. In $q$ there is
no ambiguity, which is one practical reason to state the normalisation in $q$.

**Why this is a link invariant, and why D is the only choice.** The table above
would be worth little if it rested on knowing which link each braid closes to. It
does not. By **Markov's theorem**, two braids have the same closure exactly when
they are related by conjugation and by stabilisation
$\beta \in B_n \mapsto \beta\sigma_n^{\pm 1} \in B_{n+1}$, so invariance under
those moves *is* the statement that $V$ is a link invariant — and all three
checks are algebra, with no knot theory in them:

| move | effect | invariance condition |
|---|---|---|
| conjugation | $e$, $n$ fixed; $\mathrm{tr}_M$ cyclic | automatic, any $z$ |
| positive stabilisation | $e \mapsto e+1$, $n \mapsto n+1$, $\mathrm{tr}_M \mapsto z\,\mathrm{tr}_M$ | $q^{-2}[2]_q\,z = 1$ |
| negative stabilisation | $e \mapsto e-1$, $n \mapsto n+1$, $\mathrm{tr}_M \mapsto (z-h)\,\mathrm{tr}_M$ | $q^{2}[2]_q\,(z-h) = 1$ |

(The negative row uses $\sigma^{-1} = \sigma - h$, which follows from the
quadratic relation alone: $\sigma(\sigma - h) = \sigma^2 - h\sigma = 1$.)

Each stabilisation condition is not merely *satisfied by* convention D — each
one, on its own, **forces** it, needing only $q \neq 0$. Hence:

> **Convention D is the unique Markov parameter for which
> $q^{-2e}[2]_q^{\,n-1}\mathrm{tr}_M$ is a link invariant.**

That the two stabilisations independently pin the *same* $z$ is a genuine
consistency check on the normalisation, not a restatement — and it passes.

Under this statement the retracted prefactor $q^{1/2}+q^{-1/2}$ is not a
near-miss. With it the quantity fails to survive a stabilisation move, so it is
not an invariant of anything at all.

Proved in
[`JonesNormalisation.lean`](../lean/QOU/QBeta/JonesNormalisation.lean) —
`tl_generator_sq`, `sigma_inv`, `stab_pos_iff_conventionD`,
`stab_neg_iff_conventionD`, `jonesV_stabilise_pos`, `jonesV_stabilise_neg`,
`conventionD_iff_markov_invariant`, plus the four closure values
(`unknot_two_strand`, `unknot_three_strand`, `hopf_link`,
`two_component_unlink`) and `kauffman_loop`. Sorry-free; every hypothesis is
`IsConventionD` plus $q \neq 0$, and $q^2+1 \neq 0$ is *derived* rather than
assumed (`q_sq_add_one_ne_zero`) — in a general field it can vanish, so assuming
it would have been a hidden hypothesis.

The four closure rows are retained as sanity checks — they confirm the invariant
is normalised so the unknot is $1$ — but they are no longer load-bearing.

**The proposition above is unaffected.** $\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$
follows from the Markov axiom alone and holds for any Markov parameter. So the
pair blow-up centre at coordinate $\hat V_i\hat V_j$ still carries weight $z^2$
regardless of its position in the braid, matching the empirically-verified
all-pairs set on atoms $A \ge 6$ (cf. `adjacent-vs-full-canonical evaluation.witness.json`,
[jet-tower remark](#rem:mass-endomorphism-jet-tower)). Only the knot-theoretic
gloss was wrong.

> **The proposition is convention-independent; the Hopf-link normalisation above
> is not, and has NOT been re-derived.** Flagged 2026-08-09, not fixed.
>
> $\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$ follows from the Markov axiom alone and
> holds for any Markov parameter, so switching $z$ to **convention D**
> ($z = q^3/(q^2+1)$, as the cited theorem now states) leaves the proposition
> untouched.
>
> The normalisation $J_{\mathrm{Hopf}}(q) = -(q^{1/2}+q^{-1/2})\cdot z^2$ is a
> different matter. Its prefactor is the loop parameter at **half argument**,
> $[2]_{\sqrt q} = q^{1/2}+q^{-1/2} = 2.0027\ldots$ at $q_0$, whereas the
> Temperley–Lieb loop value of the production trace is
> $\delta = [2]_q = q + q^{-1} = 2.010896866707122\ldots$ — a $0.4\%$ difference,
> and the two are conflated across the corpus (the reciprocal $1/\delta =
> 0.497290545604915556$ against $z_C = 0.499320334183694452$ is the same
> confusion). The identity was derived when $z$ was $z_C$, and under convention D
> — which *is* the Jones/Temperley–Lieb trace — both the prefactor and $z^2$
> change, so the displayed second equality
> $-(q+q^{-1})/(q^{1/2}+q^{-1/2})$ cannot be assumed to survive.
>
> Deliberately left as-is rather than patched: getting the Jones normalisation
> right under D is a derivation, not a substitution, and quietly editing the
> prefactor would produce a formula nobody has checked. Bean `qou-98g5`
> (δ vs $z_C$ conflation) and `qou-emyt`.

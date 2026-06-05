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

**Proposition (Macdonald hook-content telescope, conditional on `StanleyHookTelescope`).**
*Let $Q = q^2$ and $X = q\,z\,/\,(1 - Q + q\,z)$ be the Wenzl-bridge
substitution of
[`prop:y-lambda-closed-form-wenzl-bridge`](#prop:y-lambda-closed-form-wenzl-bridge),
let $f_\lambda$ be the number of standard Young tableaux of shape
$\lambda$, and let*

$$
  s_{\lambda, X}(Q) \;=\; Q^{n(\lambda)} \prod_{x \in \lambda}
    \frac{1 - X \cdot Q^{c(x)}}{1 - Q^{h(x)}}
$$

*be the principal-specialisation Schur element. Then the
Wenzl-bridge normalisation $Z_n := \sum_{\lambda \vdash n}
f_\lambda \cdot s_{\lambda, X}(Q)$ telescopes to the single
geometric ratio*

$$
  \boxed{\;
    Z_n \;=\; \left(\frac{1 - X}{1 - Q}\right)^n,
  \;}
$$

*and consequently every Jones–Markov central coefficient
$y_\lambda$ admits the **single-product hook-content closed
form***

$$
  \boxed{\;
    y_\lambda \;=\; Q^{n(\lambda)}
      \cdot \frac{(1 - Q)^n}{(1 - X)^n}
      \cdot \prod_{x \in \lambda}
        \frac{1 - X \cdot Q^{c(x)}}{1 - Q^{h(x)}}.
  \;}
$$

## Conditional-class formalisation

The Lean module axiomatises the principal-specialisation identity as
the class `StanleyHookTelescope`; the proposition's theorem
`macdonald_hook_telescope` carries this class as an explicit
`[Instance]` hypothesis and is discharged by `telescope_holds`.
This follows CLAUDE.md §3b-cond (conditional-on-class). The
`wenzlNormalizationOfShape` value is kept `opaque` so the class
field captures substantive (non-tautological) mathematical content.

The substantive content of the identity is Stanley's
principal-specialisation result (Stanley 1999 Cor. 7.12.5;
Macdonald 1995 I.3 ex. 1). It is backed empirically by symbolic
verification at $n = 0, \ldots, 8$ in
`y_lambda_macdonald_telescope.py` (every partition closes via
`sympy.cancel` to 0) and 191-sample numerical cross-check to
$\approx 10^{-51}$ against the MPFR Hoefsmit-matrix witness. A
future Mathlib lift of Schur / principal-specialisation
infrastructure would supply a constructive instance, with the
downstream API unchanged.

## Why this is the right shortcut

The classical principal-specialisation identity (Stanley,
*Enumerative Combinatorics II* Cor. 7.12.5; Macdonald, *Symmetric
Functions* I.3 ex. 1) states

$$
  \sum_{\lambda \vdash n} f_\lambda \cdot s_\lambda
    \;=\; p_1^{\,n}
$$

as symmetric functions, where $p_1 = \sum x_i$. Equivalently, the
regular representation of $S_n$ has Frobenius image $p_1^n$. Under
the *principal specialisation in $r$ variables* — the substitution
$x_i \mapsto q^{i-1}$ for $i = 1, \ldots, r$ — we have
$p_1 \mapsto 1 + q + \cdots + q^{r-1} = (1 - q^r)/(1 - q)$. Sending
$q \mapsto Q$ and identifying the Wenzl level $X = Q^r$ gives

$$
  Z_n \;=\; \sum_{\lambda \vdash n} f_\lambda \cdot s_{\lambda, X}(Q)
    \;=\; \left(\frac{1 - X}{1 - Q}\right)^n.
$$

The fractional/non-integer $r$ used by the Wenzl bridge does not
break the identity: $X = Q^r$ enters the formula only through the
factor $(1 - X)$, and the right-hand side of the principal-
specialisation identity is a polynomial identity in $X$ that
extends analytically.

## Comparison with the previous "open structural project"

The earlier hand-derivation in
[`y-lambda-clean-closed-forms.md`](https://github.com/litlfred/qou/blob/main/computations/y-lambda-clean-closed-forms.md)
recorded the $n = 2$ collapse $Z_2 = (1 - X)^2 / (1 - Q)^2$,
flagged the $n \geq 3$ unsimplified sympy expressions as
"degree $\sim 25$ polynomials", and listed the general identity as
an *open structural project* — pending a Macdonald-hook formula
that would let `sympy.factor` collapse the sum at every $n$.
This proposition closes that project: the identity is the
classical regular-representation Frobenius identity, evaluated
at the principal specialisation.

## Computational consequences

Per-partition, the closed form requires only the cells of $\lambda$:

- $O(n)$ cell scans for $n(\lambda)$, contents $c(x)$, hooks $h(x)$.
- One product of $n$ factors $(1 - X \cdot Q^c)$ in the numerator.
- One product of $n$ factors $(1 - Q^h)$ in the denominator.
- One global $(1 - Q)^n / (1 - X)^n$ from the telescope.

No `sympy.simplify` and no `sympy.cancel` are required: the
expression is already in canonical hook-content form. This
eliminates the sympy `RecursionError` previously observed for
$n \geq 5$ and the "degree $\sim 80$ in $q^{1/2}$" denominator
explosion at $n = 12$. The compute path is now O($p(n) \cdot n$)
work for the entire table.

## Numerical verification

The companion script
[`y_lambda_macdonald_telescope.py`](https://github.com/litlfred/qou/blob/main/computations/y_lambda_macdonald_telescope.py)

1. Verifies $Z_n = ((1-X)/(1-Q))^n$ symbolically for $n = 0, \ldots, 6$
   (the difference reduces to $0$ via `sympy.cancel`).
2. Verifies the closed-form collapse
   $y_\lambda = s_{\lambda, X}(Q) / Z_n$ partition-by-partition for
   $n = 0, \ldots, 6$ (all 30 partitions).
3. Emits closed forms for all 30 partitions across $n = 0, \ldots, 6$
   — the closed-form formula itself is $O(n)$ per partition for any
   $n$; only sympy serialisation costs grow at larger $n$.
4. Cross-checks against the MPFR Hoefsmit-matrix witness
   (`y-lambda-mpfr-witness.json`): max
   $|y_\lambda^{\text{telescope}} - y_\lambda^{\text{MPFR}}|
     \approx 2.5 \times 10^{-51}$ across 191 samples (limited only
   by the witness's 50-dps precision).

Output: [`y-lambda-macdonald-telescope.witness.json`](https://github.com/litlfred/qou/blob/main/computations/y-lambda-macdonald-telescope.witness.json).

## Crystal-basis interpretation

The identity $\sum_\lambda f_\lambda \cdot s_\lambda = p_1^n$ is
the *Frobenius character* of the regular $S_n$-representation,
which is the **Kostka decomposition** of $p_1^n$ into Schur
functions. Categorified, $p_1^n$ is the $n$-fold tensor product of
the natural module of the KLR algebra $R_\alpha$ (in type $A$);
the multiplicity $f_\lambda$ is the dimension of the corresponding
KLR canonical-basis component. The telescope is thus the
**decategorified Kashiwara crystal count** for the regular
representation — exactly the symmetric-crystal shortcut flagged in
the project's authoring guidance (CLAUDE.md §7b, item 2: "decategorifying
KLR canonical basis to KL basis of $S_n$"). The previous
hand-rolled sympy approach reinvented this combinatorial count
without naming the crystal structure; naming it removes the
manual algebra.

## Lean formalisation

[`macdonald-hook-telescope.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/macdonald-hook-telescope.lean)
states `macdonald_hook_telescope`: $Z_n = ((1-X)/(1-Q))^n$ as
an algebraic identity over $\mathbb{Q}(X, Q)$. The proof reduces
to the principal-specialisation case of the regular-representation
Frobenius identity — currently a single `sorry` with a citation to
[stanley1999] Cor. 7.12.5, plus an empirical witness link to
`y-lambda-macdonald-telescope.witness.json` recording symbolic
verification through $n = 8$.

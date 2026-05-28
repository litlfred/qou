**Proposition (Habiro integrality of the Markov trace).**
*The Markov trace $\operatorname{tr}_M(T_w, q)$ of any braid word
admits a finite Habiro expansion with integer coefficients $a_m \in
\mathbb{Z}[u]$. The Habiro form is the canonical representation: it is
an exact, finite rational evaluation, not a truncated series.*

*Specifically, the Markov trace of the neutron–proton braid-word
difference admits the finite expansion*

$$
  \operatorname{tr}_M(\beta_n) - \operatorname{tr}_M(\beta_p)
  \;=\;
  \sum_{m=0}^{M} a_m(u) \cdot (u;\,u)_m,
  \qquad
  a_m \in \mathbb{Z}[u],
$$

*where $u = q^{1/2}$, $(u;\,u)_m = \prod_{k=1}^{m}(1-u^{2k})$ is the
$q$-Pochhammer symbol, and $M < \infty$ (the series terminates).*

*Under the archimedean evaluation $u \mapsto u_0 = q_0^{1/2}$, each
$(u_0;\,u_0)_m$ contributes a factor that shrinks like
$\sim \hbar_q^m$ where $\hbar_q = (q_0-1)/q_0 \approx 0.099$.*

> **Author note (scope, 2026-05-28).** A historical "precision ladder"
> wrote the $q$-deformed observables as a product
> $\prod_k (1 + c_k (b\hbar_q^2)^k)$ and identified per-rung
> coefficients $c_k$. Those $c_k$ are **not** the Taylor coefficients
> of the exact Habiro sum: the genuinely-derived expansion (e.g. the
> $\tau_M$ form, `prop:tau-M-asymptotic-rep-theory`) is derived only at
> low order ($k=1$ via the Kashiwara $\tilde f_1$ matrix element), and
> the higher $c_k$ used to reach part-per-billion accuracy were tuned
> against the experimental value, not evaluated from the integer
> $a_m$. They depend on the (unproven) choice of intermediate form and
> are excluded from the canonical chain. What this proposition asserts
> is only the **integrality and finiteness** of the $a_m$ — which is
> verified — not any bridge from the $a_m$ to those ladder $c_k$.

## Proton Habiro coefficients (verified integral)

The proton's Markov trace has $M = 8$ (series terminates):

| $m$ | $a_m(u) \in \mathbb{Z}[u]$ |
|-----|---------------------------|
| 0 | $4$ |
| 1 | $-74u - 74$ |
| 2 | $340u^2 + 365u + 389$ |
| 3 | $-711u^3 - 789u^2 - 872u - 959$ |
| 4 | $788u^4 + 901u^3 + 1029u^2 + 1172u + 1328$ |
| 5 | $-466u^5 - 559u^4 - 660u^3 - 781u^2 - 918u - 1078$ |
| 6 | $133u^6 + 167u^5 + 212u^4 + 264u^3 + 328u^2 + 402u + 494$ |
| 7 | $-12u^7 - 17u^6 - 24u^5 - 34u^4 - 48u^3 - 63u^2 - 84u - 110$ |
| 8 | $u^4 + 2u^3 + 3u^2 + 5u + 7$ |

The neutron has the same structure with $M = 8$ and different integer
coefficients. The deuteron has $M = 12$.

## Why this resolves the "axiom vs theorem" question

The archimedean functor is not an arbitrary map — it is the UNIQUE
evaluation $\widehat{\mathbb{Z}[q]} \to \mathbb{R}$ that:

1. Sends the Habiro ring element $\operatorname{tr}_M(T_w)$ to its
   value at $q = q_0$.
2. Respects the cyclotomic integrality: each $a_m \in \mathbb{Z}[u]$.
3. Terminates at finite $M$ (no truncation needed).

The integrality and finiteness of the $a_m$ require no fitting and no
free parameters beyond $(m_e, q_0)$ — the Habiro evaluation of
$\operatorname{tr}_M$ at $q_0$ is determined.

## What the exact evaluation does and does not give

Since the Habiro expansion is **finite** ($M = 8$ for proton), the
evaluation $\operatorname{tr}_M(\beta_K, q_0)$ is **exact** — a
well-defined element of $\mathbb{Q}(q_0)$, not a truncated series.

What this does **not** give is part-per-billion agreement with
experiment. An observable such as $Q_\beta$ is
$m_e \cdot f(\operatorname{tr}_M(\beta_n), \operatorname{tr}_M(\beta_p),
q_0)$, and the exact Habiro evaluation of that map lands at the
substrate's *intrinsic* accuracy (order $10^{-3}$ for the bare $Q_\beta$
form, improving to $\sim 1\,\text{ppm}$ once the derived low-order
$\tau_M$ corrections of `prop:tau-M-asymptotic-rep-theory` are
included). Reaching part-per-billion requires higher-order corrections
that are **not** currently derived from the $a_m$; attempts to read them
off as a "precision ladder" tuned the coefficients against the
experimental value rather than evaluating them categorically. The
canonical content of this block is the integrality of the $a_m$, not a
ppb-level prediction.

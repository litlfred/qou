**Proof.** The Jones polynomial of the Borromean rings is
\cite{murasugi1996}:

$$
  V(\mathcal{B}_3, t)
  = -t^{-3} + 3t^{-2} - 2t^{-1} + 4 - 2t + 3t^2 - t^3.
$$

Setting $t = q^2$ and introducing $u := q^2 + q^{-2}$, this becomes
a polynomial in $u$:

$$
  V = -u^3 + 3u^2 + u - 2.
$$

For a 3-component link, the Markov trace is $\mathrm{tr}_M =
V / [2]_q^2$ where $[2]_q^2 = (q + q^{-1})^2 = u + 2$. Polynomial
long division yields:

$$
  \frac{V}{u + 2}
  = -u^2 + 5u - 9 + \frac{16}{u + 2}.
$$

Substituting $u = h^2 + 2$ (where $h = q - q^{-1}$, so
$q^2 + q^{-2} = h^2 + 2$):

$$
  \mathrm{tr}_M
  = -(h^2 + 2)^2 + 5(h^2 + 2) - 9 + \frac{16}{h^2 + 4}
  = \frac{4 + h^2 - 3h^4 - h^6}{h^2 + 4}.
$$

$\square$

## The $h$-expansion (purely even)

Taylor-expanding around $h = 0$:

$$
  \mathrm{tr}_M
  = 1
    + \underbrace{0}_{\text{no } h^2}
    \cdot h^2
    - \underbrace{\frac{3}{4}}_{h^4} \cdot h^4
    - \underbrace{\frac{1}{16}}_{h^6} \cdot h^6
    + \underbrace{\frac{1}{64}}_{h^8} \cdot h^8
    + \cdots
$$

The series is **purely even** in $h$ (the numerator and denominator
are both even polynomials in $h$). The higher-order coefficients
follow a geometric tail from the remainder term $16/(h^2 + 4)$.

## The $h^2$ coefficient is exactly zero

The vanishing of the $h^2$ term is a **non-trivial cancellation**:
the numerator HAS an $h^2$ coefficient ($+1$), but the denominator's
$h^2$ coefficient ($+1$) cancels it exactly:

$$
  \frac{4 + h^2 - 3h^4 - h^6}{4 + h^2}
  = \frac{(4 + h^2) + (-3h^4 - h^6)}{4 + h^2}
  = 1 + \frac{-3h^4 - h^6}{h^2 + 4}.
$$

The first non-trivial correction appears at $h^4$ with coefficient
$-3/4$: the **first topological invariant** of the Borromean linking
structure — the part of the Jones polynomial that distinguishes
$\mathcal{B}_3$ from the trivial 3-component unlink.

## Per-representation decomposition and exact $h^2$ budget

The three irreps of $S_3$ / $H_3(q)$ contribute distinctly to the
Frobenius expansion $\mathrm{tr}_M = \sum_\lambda y_\lambda \chi^\lambda$.

> **Convention note.** Two distinct
> Markov-trace normalisations are in use for $H_3(q)$, and
> they have **different** Wenzl weights and different per-partition
> budgets:
>
> 1. the **Jones-closure** normalisation
>    $\mathrm{tr}_M = V_{\mathrm{Jones}} / [2]_q^{\,c-1}$ — the
>    convention of *the closed form above* — with weights
>    $y_{(3)} = [4]_q/[2]_q^3$, $y_{(2,1)} = 1/[2]_q^2$,
>    $y_{(1^3)} = 0$ identically
>    ([Closed-form Jones/Temperley–Lieb weights on $H_3(q)$ (Borromean Jones polynomial): $y_{(3)} = [4]_q/[2]_q^3$, $y_{(2,1)} = 1/[2]_q^2$, $y_{(1^3)} = 0$](h3-markov-wenzl-weights.md));
> 2. the **Wenzl-bridge / Ocneanu** normalisation (producer
>    `y-lambda-wenzl-bridge-symbolic-witness.json`, used by
>    the formal derivation), whose
>    weights are all non-zero and whose trace value on
>    $\beta_{\mathrm{Bor}}$ **differs** from the closed form above
>    (e.g. $0.91926$ vs $0.93917$ at $q = 1.3$; that witness
>    records `lean_form_matches: false`).
>
> An earlier revision of this section tabulated the bridge-convention
> budget $(5/128, -20/128, 15/128)$ without labelling the convention —
> those numbers decompose the *bridge* trace, **not** the closed form
> above. Both budgets sum to zero (each trace separately has
> $h^2 = 0$), which masked the mismatch.

In the **Jones-closure convention used here**, the per-partition
decomposition is:

- **$\lambda = (3)$ [trivial, dim 1]:** $\chi^{(3)}(\beta_{\mathrm{Bor}}) = 1$
  exactly for all $q$ (writhe-zero braid, trivial eigenvalue $q^0 = 1$);
  weight $y_{(3)} = [4]_q/[2]_q^3$.
  Per-partition $h^2$ coefficient of $y_{(3)} \cdot \chi^{(3)}$: $\;+1/8$.

- **$\lambda = (1^3)$ [sign, dim 1]:** $\chi^{(1^3)}(\beta_{\mathrm{Bor}}) = 1$
  exactly (writhe-zero, sign eigenvalue $(-q^{-1})^0 = 1$); weight
  $y_{(1^3)} = 0$ **identically** — the Jones polynomial factors
  through Temperley–Lieb, which annihilates the 3-row partition.
  Per-partition $h^2$ coefficient: $\;0$.

- **$\lambda = (2,1)$ [standard, dim 2]:** The **only non-abelian
  irrep**, with exact rational character

  $$
    \chi^{(2,1)}(\beta_{\mathrm{Bor}})
    = \frac{-q^{12} + 3q^{10} - 3q^8 + 4q^6 - 3q^4 + 3q^2 - 1}{q^6}
    \;=\; 2 - 3h^4 - h^6;
  $$

  weight $y_{(2,1)} = 1/[2]_q^2$. ALL correction terms
  ($h^4, h^6, \ldots$) of $\mathrm{tr}_M$ originate from this
  partition alone.
  Per-partition $h^2$ coefficient of $y_{(2,1)} \cdot \chi^{(2,1)}$: $\;-1/8$.

The $h^2$ budget is exact:

$$
  \underbrace{\frac{1}{8}}_{(3)}
  \;+\; \underbrace{\left(-\frac{1}{8}\right)}_{(2,1)}
  \;+\; \underbrace{0}_{(1^3)}
  \;=\; 0.
$$

(For the record, the bridge-convention budget is
$(5/128, -20/128, 15/128)$, also summing to zero — but it decomposes
the bridge-normalised trace, a different functional.)

## Vanishing of $h^2$: universal identity + Borromean symmetry

The cancellation follows from two independent facts:

**Fact 1 (universal).** The Markov trace normalization
$\sum_\lambda y_\lambda(q) \cdot d_\lambda = 1$ holds identically
in $q$. Differentiating twice in $h$ at $h = 0$:

$$
  \sum_\lambda \bigl[h^2\text{-coeff of } y_\lambda\bigr] \cdot d_\lambda = 0.
$$

This is a **knot-independent** identity — it constrains the Wenzl
weights regardless of which braid is traced.

**Fact 2 (Borromean-specific).** The braid $\beta_{\mathrm{Bor}} =
(\sigma_1^{-1}\sigma_2)^3$ maps under $\pi\colon B_3 \to S_3$ to
$(s_1 s_2)^3 = (1\,2\,3)^3 = \mathrm{id}$. Since it also has
writhe $= 3 \cdot 1 + 3 \cdot (-1) = 0$, the one-dimensional
characters satisfy $\chi^{(3)}(\beta_{\mathrm{Bor}}) =
\chi^{(1^3)}(\beta_{\mathrm{Bor}}) = 1$ *exactly*. At $q = 1$
(i.e. $h = 0$), the standard character evaluates to
$\chi^{(2,1)}(\mathrm{id}) = d_{(2,1)} = 2$.

**Fact 3 (Borromean-specific).** The standard character has no
$h^2$ term: $\chi^{(2,1)}(\beta_{\mathrm{Bor}}) = 2 - 3h^4 - h^6$.

Combining: write $\mathrm{tr}_M = \sum_\lambda y_\lambda \chi^\lambda$
and take the $h^2$ coefficient. It is

$$
  \sum_\lambda \bigl[h^2\bigr] y_\lambda \cdot \chi^\lambda\big|_{h=0}
  \;+\; \sum_\lambda y_\lambda\big|_{h=0} \cdot \bigl[h^2\bigr] \chi^\lambda .
$$

The first sum is $\sum_\lambda [h^2]y_\lambda \cdot d_\lambda = 0$ by
Facts 1 and 2. In the second sum the one-dimensional characters are
constant, so only $y_{(2,1)}|_{h=0} \cdot [h^2]\chi^{(2,1)}$ survives,
and it vanishes by Fact 3.

## Generalization: conditions for $h^2 = 0$

The argument needs three conditions on $\beta \in B_n$:

1. **Pure braid**: $\pi(\beta) = \mathrm{id} \in S_n$
   (so $\chi^\lambda(\beta)|_{q=1} = d_\lambda$ for all $\lambda$).
2. **Writhe zero**: equal positive and negative crossings
   (so 1-dimensional characters are identically $1$).
3. **No $h^2$ term in the multi-dimensional characters**:
   $[h^2]\chi^\lambda(\beta) = 0$ for every $\lambda$ with
   $y_\lambda|_{h=0} \neq 0$ and $d_\lambda > 1$.

Conditions 1 and 2 alone do not suffice, even at $H_3$. The pure,
writhe-zero braid $\sigma_1^2 \sigma_2^{-2}$ has
$\chi^{(2,1)} = 2 + 3h^2 + h^4$ and
$\mathrm{tr}_M = 1 + \tfrac34 h^2 + O(h^4)$ under convention D.

Cross-isotope verification: the deuteron ($H_6$), tritium ($H_9$),
and ${}^3\mathrm{He}$ ($H_9$) atom braids have $h^2 \ne 0$
($12.7$, $18.7$, $36.6$ respectively). The three conditions are
sufficient for every $n$, so each of these braids violates at least one
of them.

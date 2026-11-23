*Define, for a substrate parameter $q$ and a mass scale $m_e$,*

$$
  \kappa_{\mathrm{closed}}(q, m_e)
  \;=\; -\,\frac{E_0 \cdot \log(1/h)}{[2]_q \cdot [3]_q},
  \qquad
  E_0 = \frac{m_e}{q(q-1)}, \quad h = q - q^{-1},
$$

*where $[n]_q = (q^n - q^{-n}) / (q - q^{-1})$ is the balanced q-bracket. At the substrate parameter this evaluates to $\kappa_{\mathrm{closed}} \approx -1.0704$.*

**No physical quantity is claimed for this expression.** It was formerly proposed as the per-excess slope of a magic-shell coupling; that identification is withdrawn, for the reason recorded below. The name is retained because the corpus refers to it, not because the identification stands.

## Why the identification was withdrawn

The expression was matched, to $3.4 \times 10^{-4}$, against a measured value of $\approx -1.0708\;\text{MeV}$. That value is the electrostatic energy of ${}^{3}$He's $pp$ pair, attributed to the proton–neutron interface asymmetry.

The fit that produced it ran at two anchors and disagreed with itself:

| anchor | excess $(n_{pp} - n_{nn})$ | slope |
|---|---|---|
| ${}^{3}$He $(2,1)$ | $+1$ | $-1.0707908\;\text{MeV}$ |
| ${}^{3}$H $(1,2)$ | $-1$ | $+0.2023095\;\text{MeV}$ |

Opposite signs, a factor of $5.3$ apart. The hypothesis under test was that a single coefficient holds across the anchors, and the producing computation recorded that it does not. The ${}^{3}$He arm became the published value; the ${}^{3}$H arm was not carried forward.

Those two nuclides differ in exactly one respect besides the sign of the excess: ${}^{3}$He contains a $pp$ pair and ${}^{3}$H does not. Restoring that electrostatic energy removes the discord. Both residuals become negative — under every radius model tried, including the one derived from $\bar\lambda_\pi$ and two independent alternatives — and under the derived radius they agree to $0.021\;\text{MeV}$, essentially the ${}^{4}$He residual of $0.022\;\text{MeV}$ measured where the excess vanishes identically.

A term proportional to $(n_{pp} - n_{nn})$ must change sign between anchors of excess $+1$ and $-1$. What survives the correction does not: it is an excess-*independent* offset of order $0.2\;\text{MeV}$, three to fifteen times smaller than the matched value. **The excess coefficient is zero.**

That single diagnosis accounts for the two independent negatives found before it. No term of this form and size appears in mirror-split binding data at $A = 3$, $15$, $39$, because the coefficient vanishes. And the original fit contradicted itself because it was describing an electrostatic energy with a categorical form, and only one of its two anchors has one.

## What is proved about the expression

The following hold independently of any physical reading, and are unaffected by the withdrawal.

The bracket is the canonical balanced q-integer: $[n]_q$ as written here coincides with it unconditionally and including on the degenerate locus, so this definition introduces no competing q-integer convention.

The denominator is a q-factorial. $[2]_q \cdot [3]_q = [3]_q!$, hence

$$
  [2]_q \cdot [3]_q \;=\; [3]_q! \;=\; \frac{q^3}{y_{(3)}(q)},
$$

the inverse Markov weight of the trivial partition $(3) \vdash 3$. This is the reusable content of the block. The index $3$ is the strand count of a single nucleon — the nucleon is the Borromean link, carried by the braid word $(\sigma_1 \sigma_2^{-1})^3 \in B_3$ — and the same normalization appears in the Borromean observable $F_{\mathrm{Bor}} = |\mathrm{tr}_M(\beta_{\mathrm{Bor}})| / y_{(3)}(q)$.

The sign is forced. For $q > 1$, $m_e > 0$, and $0 < h < 1$: $E_0 > 0$, $\log(1/h) > 0$, and $[2]_q, [3]_q > 0$, so $\kappa_{\mathrm{closed}} < 0$. This is a property of the expression and is asserted of nothing else.

## A separate question, deliberately not attached here

After the electrostatic correction, an excess-independent offset of order $0.2\;\text{MeV}$ remains at $A = 3$ that the same form does not exhibit at $A = 4$, where its residual is $0.022\;\text{MeV}$. That is a real and unexplained baseline. It is not the quantity this block was about, and giving it this block's name would repeat the error the withdrawal corrects.

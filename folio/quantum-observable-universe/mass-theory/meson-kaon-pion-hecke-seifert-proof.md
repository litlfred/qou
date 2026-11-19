**Proof.**
The algebraic factor arises from the Hecke representation theory
of $H_3(q_0)$.  On the standard $(2,1)$ irreducible representation,
$\sigma_1$ acts diagonally in the Hoefsmit seminormal basis with
eigenvalues $q$ and $-q^{-1}$
(cf. [Hoefsmit binding amplitude](../braids-and-knots/hoefsmit-binding-amplitude.md)).
The character of $\sigma_1^n$ for odd $n$ is therefore

$$
  \chi^{(2,1)}(\sigma_1^n)
  = q^n + (-q^{-1})^n
  = q^n - q^{-n}
  = h \cdot [n]_q.
$$

The topological factor uses the Seifert fibration of the torus knot
complements.  The Seifert Euler number of $T(2,n)$ is
$e = 1 - \tfrac{1}{2} - \tfrac{1}{n}$, giving volumes

$$
  V_S(T(2,3)) = \frac{\pi}{3}, \qquad
  V_S(T(2,5)) = \frac{3\pi}{5}, \qquad
  \frac{V_S(T(2,5))}{V_S(T(2,3))} = \frac{9}{5}.
$$

The squaring exponent $n_q = 2$ reflects the meson's two-body composite
structure: each quark constituent contributes one factor of the Seifert
volume ratio to the geometric part of the mass formula.  A power scan
over exponents $1$, $2$, $3$ is consistent with that reading, giving
$290\;\mathrm{ppm}$ at $n_q = 2$ against
$444{,}605\;\mathrm{ppm}$ at $n_q = 1$ and
$799{,}479\;\mathrm{ppm}$ at $n_q = 3$.  The scan is a weak check and
is not offered as evidence for the exponent: the two-body rationale
names $n_q = 2$ in advance, and the two alternatives miss by $44\%$ and
$80\%$ rather than marginally, so a scan that selected the exponent
against the data would look no different.  What the scan establishes is
only that the a-priori exponent is not contradicted.

Combining: $(q_0^5 - q_0^{-5}) \times (9/5)^2 \approx 1.0914 \times
3.24 = 3.5361$. $\square$

## Numerical verification

Direct $50$-digit evaluation verifies the formula, confirms the algebraic
identity $q^5 - q^{-5} = h \cdot [5]_q$, and validates the Seifert
ratio $V_S(T(2,5))/V_S(T(2,3)) = 9/5$ exactly.

## Algebraic identities vs. empirical gap

The argument separates the **two algebraic identities** (proved unconditionally over any field of characteristic $\neq 2, 3, 5$) from the **physical / empirical content** of the mass-ratio comparison:

| Component | Mathematical statement | Status |
|---|---|---|
| Odd-power character | $\chi^{(2,1)}(\sigma_1^n)=q^n+(-q^{-1})^n=q^n-q^{-n}$ for odd $n$ | **proved** |
| Seifert ratio | $V_S(T(2,5))/V_S(T(2,3))=9/5$ | **proved** (char $\neq 2,3,5$) |
| Squaring exponent | the exponent record $n_q=2$ | **definition** |
| Assembled ratio | $\chi^{(2,1)}(\sigma_1^5)\cdot(9/5)^2$ | **definition** |

**What is not derived by the two identities above:**

1. **The exponent $n_q=2$** has a *physical rationale* (two-quark
   composite) and is *not contradicted* by the power scan ($290$ ppm at
   $n_q=2$ vs $4.4\times 10^5$ ppm at $n_q=1$). It is **not derived** from
   the aether, and the scan does not supply the missing derivation —
   see the caveat in the proof body. The squaring-exponent definition
   only records the value; it does not select it.
2. **The match to the PDG ratio** ($\approx 290$ ppm) is an empirical
   *witnessed near-match* rather than an exact algebraic identity.

**Base-ring note.** The two algebraic identities hold over any generic
field $R$ (with no archimedean $\mathbb{R}$ dependence): the odd-power character identity is
unconditional, and the Seifert ratio identity requires only $2,3,5\neq 0$ in $R$.

## Scope — this is not the canonical route to $m_K/m_\pi$

This proof establishes the two algebraic identities above and assembles
them into a *witnessed near-match*. It is **not** the framework's
canonical closure of the meson ratio, and the two must not be conflated.
The canonical route is the $q$-Clebsch--Gordan fusion together with the
electromagnetic term,
$m_K^2/m_\pi^2 = [3]_q\,[4]_q + (\alpha_{\mathrm{em}}/\pi)\bigl(1 + \log(1+\hbar_q)\bigr)$
([meson sinh-channel closed form](../braids-and-knots/meson-em-sinh-closed-form.md)),
which is what the per-observable accuracy dashboard scores. The
$(q_0^5 - q_0^{-5})(9/5)^2$ form here was formerly used there and was
excluded from that role.

The two agree with each other only to about a part in $3\,400$: the form
proved here sits at $290$ parts per million, which misses this
observable's accuracy target of $263.6$ parts per billion by a factor of
$1{,}099$, while the canonical route sits at $51.5$ parts per billion.
A reader who takes the $290$ ppm figure as the framework's accuracy on
$m_K/m_\pi$ will be wrong by more than three orders of magnitude in the
conservative direction.

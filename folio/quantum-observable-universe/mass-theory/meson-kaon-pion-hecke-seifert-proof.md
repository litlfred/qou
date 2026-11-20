**Proof.**
The algebraic factor arises from the Hecke representation theory
of $H_3(q_0)$.  On the standard $(2,1)$ irreducible representation,
$\sigma_1$ acts diagonally in the Hoefsmit seminormal basis with
eigenvalues $q$ and $-q^{-1}$
(cf. [`prop:hoefsmit-binding-amplitude`](../braids-and-knots/hoefsmit-binding-amplitude.md)).
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

## Computational witness

[`meson-kaon-pion-derivation.witness.json`](../../../computations/meson-kaon-pion-derivation.witness.json)
verifies the formula at $50$-digit precision, confirms the algebraic
identity $q^5 - q^{-5} = h \cdot [5]_q$, and validates the Seifert
ratio $V_S(T(2,5))/V_S(T(2,3)) = 9/5$ exactly.

## Lean structure — what is proved vs. the remaining gap

The Lean sibling separates the **two algebraic identities** (proved)
from the **physical / empirical content** of the mass-ratio
claim (not a Lean theorem). This makes precise what remains "to be
proved" downstream.

| Lean declaration | content | status |
|---|---|---|
| `chi_21_odd` | $\chi^{(2,1)}(\sigma_1^n)=q^n+(-q^{-1})^n=q^n-q^{-n}$ for odd $n$ | **proved** |
| `seifert_ratio_T25_T23` | $V_S(T(2,5))/V_S(T(2,3))=9/5$ | **proved** (needs char $\neq 2,3,5$) |
| `meson_squaring_exponent` | the exponent record $n_q=2$ | **proved** (`rfl`) |
| `mesonMassRatio` | the assembled formula $\chi^{(2,1)}(\sigma_1^5)\cdot(9/5)^2$ | **definition** |

**The gap (NOT Lean-proved, and intentionally so):**

1. **The exponent $n_q=2$** has a *physical rationale* (two-quark
   composite) and is *not contradicted* by the power scan ($290$ ppm at
   $n_q=2$ vs $4.4\times 10^5$ ppm at $n_q=1$). It is **not derived** from
   the substrate, and the scan does not supply the missing derivation —
   see the caveat in the proof body. The `meson_squaring_exponent` lemma
   only records the value; it does not select it.
2. **The canonical exact match to the PDG ratio** ($\approx 290$ ppm) is a
   *witnessed near-match*, not a Lean equality — the witness JSON is the
   evidence, the Lean file proves only the two underlying identities.

**Base-ring note.** The Lean sibling is stated over a generic
`[Field R]` (no archimedean `$\mathbb{R}$` dependence). `chi_21_odd` is
unconditional; `seifert_ratio_T25_T23` carries explicit `$2,3,5\neq 0$`
hypotheses — the invertibility the rational identity genuinely needs,
vacuous in any characteristic-0 specialisation. This avoids `CharZero`
entirely and is verified (`lake env lean`).

## Scope — this is not the canonical route to $m_K/m_\pi$

This proof establishes the two algebraic identities above and assembles
them into a *witnessed near-match*. It is **not** the framework's
canonical closure of the meson ratio, and the two must not be conflated.
The canonical route is the $q$-Clebsch--Gordan fusion together with the
electromagnetic term,
$m_K^2/m_\pi^2 = [3]_q\,[4]_q + (\alpha_{\mathrm{em}}/\pi)\bigl(1 + \log(1+\hbar_q)\bigr)$
([Meson EM sinh-channel closed-form $1 + \hbar_q - \hbar_q^2/2 = (3q^2 - 1)/(2q^2)$](../braids-and-knots/meson-em-sinh-closed-form.md)),
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

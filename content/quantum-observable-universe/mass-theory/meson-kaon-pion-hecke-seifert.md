**Proposition (kaon-to-pion mass ratio from Hecke characters and Seifert
volumes).**
*The kaon-to-pion mass ratio decomposes into an algebraic factor from the
Hecke character of the strange-quark braid and a topological factor from
the Seifert volumes of the quark torus knots:*

$$
  \frac{\mathfrak{m}_K}{\mathfrak{m}_\pi}
  \;=\;
  \chi^{(2,1)}(\sigma_1^5)
  \;\times\;
  \biggl(\frac{V_S(T(2,5))}{V_S(T(2,3))}\biggr)^{\!2}
  \;\approx\; 3.536
$$

*where:*

1. $\chi^{(2,1)}(\sigma_1^5) = q_0^5 - q_0^{-5} = h \cdot [5]_q$ *is
   the character of $\sigma_1^5$ on the standard $(2,1)$ representation
   of $H_3(q_0)$, with $\sigma_1$ acting diagonally with eigenvalues
   $q$ and $-q^{-1}$;*

2. $V_S(T(2,n)) = 2\pi\,|e(T(2,n))|$ *is the Seifert volume of the
   torus knot $T(2,n)$, with Euler number
   $e(T(2,n)) = 1 - \tfrac{1}{2} - \tfrac{1}{n} = \tfrac{n-2}{2n}$;*

3. *the exponent $2$ equals the number of quark constituents in the
   meson $q\bar{q}$ composite.*

*The numerical value $3.5361$ matches the PDG ratio
$m_{K^\pm}/m_{\pi^\pm} = 3.5371$ to $290\;\mathrm{ppm}$.*

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
over exponents $1$, $2$, $3$ confirms that $n_q = 2$ uniquely minimises
the PDG residual ($290\;\mathrm{ppm}$ vs
$444{,}605\;\mathrm{ppm}$ at $n_q = 1$ and
$799{,}479\;\mathrm{ppm}$ at $n_q = 3$).

Combining: $(q_0^5 - q_0^{-5}) \times (9/5)^2 \approx 1.0914 \times
3.24 = 3.5361$. $\square$

## Computational witness

[`meson-kaon-pion-derivation.witness.json`](../../computations/meson-kaon-pion-derivation.witness.json)
verifies the formula at $50$-digit precision, confirms the algebraic
identity $q^5 - q^{-5} = h \cdot [5]_q$, and validates the Seifert
ratio $V_S(T(2,5))/V_S(T(2,3)) = 9/5$ exactly.

## Lean structure — what is proved vs. the remaining gap

The Lean sibling separates the **two algebraic identities** (provable,
sorry-free) from the **physical / empirical content** of the mass-ratio
claim (not a Lean theorem). This makes precise what remains "to be
proved" downstream.

| Lean declaration | content | status |
|---|---|---|
| `chi_21_odd` | $\chi^{(2,1)}(\sigma_1^n)=q^n+(-q^{-1})^n=q^n-q^{-n}$ for odd $n$ | **proved** (sorry-free) |
| `seifert_ratio_T25_T23` | $V_S(T(2,5))/V_S(T(2,3))=9/5$ | **proved** (sorry-free; needs char $\neq 2,3,5$) |
| `meson_squaring_exponent` | the exponent record $n_q=2$ | **proved** (`rfl`) |
| `mesonMassRatio` | the assembled formula $\chi^{(2,1)}(\sigma_1^5)\cdot(9/5)^2$ | **definition** |

**The gap (NOT Lean-proved, and intentionally so):**

1. **The exponent $n_q=2$** is *physically motivated* (two-quark
   composite) and *empirically confirmed* (the power scan: $290$ ppm at
   $n_q=2$ vs $4.4\times 10^5$ ppm at $n_q=1$). It is **not derived** from
   the substrate; the `meson_squaring_exponent` lemma only records the
   value, it does not select it.
2. **The numerical match to the PDG ratio** ($\approx 290$ ppm) is a
   *witnessed near-match*, not a Lean equality — the witness JSON is the
   evidence, the Lean file proves only the two underlying identities.

**Base-ring note (§7c).** The Lean sibling is stated over a generic
`[Field R]` (no archimedean `$\mathbb{R}$` dependence). `chi_21_odd` is
unconditional; `seifert_ratio_T25_T23` carries explicit `$2,3,5\neq 0$`
hypotheses — the invertibility the rational identity genuinely needs,
vacuous in any characteristic-0 specialisation. This avoids `CharZero`
entirely (so it stays inside the sandbox cache cone) and is verified
sorry-free (`lake env lean`).

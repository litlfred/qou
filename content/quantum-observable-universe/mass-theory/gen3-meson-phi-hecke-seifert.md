**Proposition (third-generation meson mass ratio).**
*The third-generation meson built on the torus knot $T(2,7)$ has mass ratio*

$$
  \frac{\mathfrak{m}_X}{\mathfrak{m}_\pi}
  \;=\; \chi^{(2,1)}(\sigma_1^7)\cdot\Bigl(\frac{V_S(T(2,7))}{V_S(T(2,3))}\Bigr)^2
  \;=\; (q_0^7 - q_0^{-7})\cdot\Bigl(\frac{15}{7}\Bigr)^2
  \;\approx\; 7.320,
$$

*which identifies $X$ with the $\phi(1020)$ meson:
$\mathfrak{m}_\phi/\mathfrak{m}_\pi^{\mathrm{PDG}} = 7.304$, a
$2167\;\mathrm{ppm}$ match.*

This extends the proved kaon ratio
([`prop:meson-kaon-pion-hecke-seifert`](#prop:meson-kaon-pion-hecke-seifert))
to the next odd torus knot $T(2,7)$. The two algebraic ingredients are
identical in form to the kaon:

- **Hecke character.** On the standard $(2,1)$ representation of $H_3(q)$,
  $\chi^{(2,1)}(\sigma_1^7) = q^7 + (-q^{-1})^7 = q^7 - q^{-7} = h\,[7]_q$
  (odd $n$; Lean `chi_21_odd`).
- **Seifert ratio.** With $V_S(T(2,n)) = 2\pi\,e(T(2,n)) = \pi(n-2)/n$,
  $$\frac{V_S(T(2,7))}{V_S(T(2,3))} = \frac{5/14}{1/6} = \frac{15}{7}$$
  (Lean `seifert_ratio_T27_T23`, requiring $2,3,7 \neq 0$).
- **Squaring exponent** $n_q = 2$ (the two-body $\bar q q$ composite), the
  same value as the kaon.

## It is the φ, not the η

The substrate-table dictionary listed the third generation as
"$\eta,\phi$". The computation selects **$\phi$ unambiguously**: the
predicted ratio $7.320$ matches the $\phi$ to $2167\;\mathrm{ppm}$, while
the next-closest light meson is the $\eta'$ ($66{,}700\;\mathrm{ppm}$) and
the $\eta$ misses by $\sim 8.6\times 10^{5}\;\mathrm{ppm}$. This tracks the
strangeness progression — $\pi$ (generation 1, $\bar u u/\bar d d$), $K$
(generation 2, one strange quark), $\phi$ (generation 3, pure $\bar s s$
vector) — so the odd-torus tower follows the strange-vector line. The
$\eta$, a flavour-singlet pseudoscalar carrying an axial-anomaly
contribution, lies outside the single-torus-knot model and is not
predicted by this formula. The witness records the full comparison across
$K,\eta,\rho,\omega,K^\ast,\eta',\phi$.

## Status

As with the kaon, the two algebraic identities (`chi_21_odd`,
`seifert_ratio_T27_T23`) are Lean-proved sorry-free over a generic
`[Field R]` — no archimedean $\mathbb{R}$/$\mathbb{C}$ dependence; the
substrate evaluation at $q_0$ lives downstream. The exponent $n_q=2$ is
empirically selected (a two-body rationale, not substrate-derived), and
the $\approx 2167\;\mathrm{ppm}$ PDG match is a witnessed near-match, not a
Lean equality.

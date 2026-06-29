Tate's thesis \cite{tate1967} realises the global
Riemann / Dedekind $\zeta$-function as an **adelic Fourier
transform**: the global zeta integral factors as a restricted product
over local zeta integrals, one per place of $\mathbb{Q}$.  The QOU
framework lifts this factorisation to the surreal register: each
local place carries its own Reeb infinitesimal $\varepsilon_v$, the
global $\varepsilon$ is a restricted product of $\varepsilon_v$'s,
and the [surreal squeeze](#lem:surreal-squeeze) at each prime
descends to the global squeeze of [RH surreal bound](#rem:rh-surreal-bound).

**$\tau$ and $\mathrm{St}$ are dual archimedean reductions.**
Two morphisms in this paper extract real-valued data from
substrate-internal data, and they meet at the archimedean place
$v = \infty$ of $\mathbb{A}$:

- $\tau$ — the
  [QOU fibre functor](#rem:fibre-functor-rigidity), restricted
  to its archimedean component
  $\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$, is the
  algebraic-geometry / Weil realization. It evaluates the
  algebraic quantum volume on the $\mathbb{R}$-component of
  the adelic ring (see
  [Vol(K) factors through $\tau$](#prop:vol-through-tau)).
- $\mathrm{St}$ — the
  [standard-part functor](#def:standard-part-functor) is the
  surreal-field extraction $\mathbf{No} \to \mathbb{R}$ that
  collapses positive infinitesimals to $0$.

They are *dual* reductions: $\tau_{\mathrm{arch}}$ projects across
the adelic places (selecting $v = \infty$), while $\mathrm{St}$
projects along the surreal birthday filtration (collapsing
$\varepsilon \to 0$). This remark uses both — $\mathrm{St}$ inside
each local factor (to read off the real-valued bound) and
$\tau_{\mathrm{arch}} = \pi_\infty$ across factors (to assemble the
global zeta).

**Setup.** Let $\mathbb{A} = \mathbb{R} \times \prod_p' \mathbb{Q}_p$
be the rational adele ring.  For each place $v$ of $\mathbb{Q}$
(archimedean $v = \infty$ or non-archimedean $v = p$), the local
Reeb flow on the substrate's local completion carries its own
local Reeb infinitesimal

$$
  \varepsilon_v
   \;\in\; \mathrm{Der}(A_v)
  \qquad (\text{positive infinitesimal in }\mathbf{No}).
$$

The global Reeb infinitesimal $\varepsilon$
([Reeb infinitesimal](#def:reeb-epsilon)) is the restricted product
of the $\varepsilon_v$'s, in the following sense: for almost every
place $v$, $\varepsilon_v$ equals the "tame" infinitesimal
$\varepsilon_\infty$ (archimedean reference), and the global
$\varepsilon$-adic valuation $\ordw_{\mathbb{A}}(f)$ of an adelic
observable is the **sum** over $v$ of local $\ordw$-orders:

$$
  \ordw_{\mathbb{A}}(f)
   \;=\; \sum_{v} \ordw_v(f_v)
  \qquad \text{(finite sum by restricted-product condition).}
$$

**The local--global surreal bound.** For each place $v$, the
local surreal-squeeze
$\delta^2 \cdot \varepsilon_v^{-1} > \varepsilon_v^3$ in
$\mathbb{R}(\varepsilon_v)$ gives a strict inequality in
$\omega$-orders (cost has higher $\ordw$-grade than budget,
$+1 > -3$):

$$
  \ordw_v(\delta^2 \cdot \varepsilon_v^{-1}) \;>\; \ordw_v(\varepsilon_v^3).
$$

Summing over all places (equivalently, taking the adelic
$\omega$-order) yields the global inequality

$$
  \ordw_{\mathbb{A}}(\delta^2 \cdot \varepsilon^{-1})
   \;=\; \sum_v \ordw_v(\delta^2 \cdot \varepsilon_v^{-1})
   \;>\; \sum_v \ordw_v(\varepsilon_v^3)
   \;=\; \ordw_{\mathbb{A}}(\varepsilon^3),
$$

which is the global surreal squeeze of
[RH surreal bound](#rem:rh-surreal-bound).

**Tate's local functional equation in surreal form.** Tate's
thesis proves each local zeta integral
$\zeta_v(f_v, s) = \int_{\mathbb{Q}_v^\times} f_v(x) \, |x|_v^s \, d^\times x$
satisfies a local functional equation
$\zeta_v(f_v, s) = \gamma_v(s) \cdot \zeta_v(\hat{f}_v, 1 - s)$
for each place $v$.  In the surreal register, this lifts to:

| Classical | Surreal |
|---|---|
| Local $\zeta_v(f_v, s)$ | $\ordw_v$-graded expansion in $\varepsilon_v$ |
| Gamma factor $\gamma_v(s)$ | $\ordw_v$-preserving reflection $s \leftrightarrow 1 - s$ |
| Local $L$-factor $(1 - p^{-s})^{-1}$ | Euler factor $(1 - \varepsilon_p)^{-1}$ at $s = 1$ |
| Global Euler product | Adelic $\varepsilon$-product $\prod_v (1 + \varepsilon_v)$ |

**Conclusion.** The Tate thesis Fourier factorisation of the global
$L$-function is compatible with the surreal-order decomposition:
each prime contributes its own local Reeb infinitesimal
$\varepsilon_p$, the squeeze holds at every prime, and the global
squeeze is the adelic sum.  This provides the **local--global**
structure missing from [RH surreal bound](#rem:rh-surreal-bound):
it is not only the global $\varepsilon$-squeeze that forbids rogue
zeros, but a separate squeeze at each prime.

**Outlook.** The adelic lift of the surreal squeeze is the key to
generalising the Reeb-$\varepsilon$ framework from the rational
zeta function to automorphic $L$-functions (Langlands programme) —
each automorphic representation contributes its own collection of
local $\varepsilon_v$-data, and the adelic squeeze becomes the
automorphic analogue of
[macroscopic stability equivalence](#thm:macroscopic-stability-equivalence).
This is out of scope for the present paper but is the natural next
target.

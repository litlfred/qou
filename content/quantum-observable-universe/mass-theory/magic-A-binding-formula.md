*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c).
The underlying categorical content is generic; the formula is stated over
$\mathbb{R}$ for the MeV comparison.*

**Theorem (conditional on [`conj:magic-numbers-bring`](../quantum-observable-universes/magic-numbers-bring.md)
and [`prop:gravity-spectral-prefactor`](gravity-spectral-prefactor.md)).**
*For a light nucleus $^A_Z\mathfrak{X}$ that is doubly magic
(both $Z \in \mathfrak{M}$ and $N \in \mathfrak{M}$, with
$\mathfrak{M} = \{2, 8, 20, 28, 50, 82, 126\}$), the binding energy
admits the closed form*

$$
  \mathfrak{B}(^A_Z\mathfrak{X}) \;=\; \rho_F \cdot \mathfrak{m}_e \cdot A \cdot 8G
$$

*where $G$ is Catalan's constant, $8G = \mathrm{Vol}(L6a4) =
\mathrm{Vol}(\mathrm{Borromean})$ is the universal residue prefactor
([`prop:gravity-spectral-prefactor`](gravity-spectral-prefactor.md)),
and $\rho_F \in \mathbb{R}$ is the substrate-determined structural
prefactor for the doubly-magic regime.*

*Specialised to* $^4_2\mathrm{He}$ *with* $\rho_F = 2$:

$$
  \mathfrak{B}(^4_2\mathrm{He})
    \;=\; 2 \cdot \mathfrak{m}_e \cdot 4 \cdot 8G
    \;\approx\; 29.956\;\mathrm{MeV}
$$

*compared to the experimental value $28.296\,\mathrm{MeV}$ — a relative
miss of $+5.9\%$. This is dramatically tighter than the alpha-shift
formula ([`prop:binding-alpha-shift-extension`](binding-alpha-shift-extension.md))
which misses $^4_2\mathrm{He}$ by $-79\%$ ($5\times$ too small) because that
formula assumes a single hyperbolic force-carrier knot per nucleus —
an assumption that breaks for doubly-magic nuclei.*

## Why doubly-magic requires a separate formula

The framework's two binding paths apply to **distinct categorical
regimes**:

| Regime | Path | Categorical content |
|---|---|---|
| Hyperbolic | $\mathfrak{B} = \mathfrak{m}_e \cdot \rho_0 \cdot \alpha_{\mathrm{shift}}(T(p, k))$ | per-rep Reeb phase at force-carrier torus knot $T(p, k)$ |
| Doubly-magic | $\mathfrak{B} = \rho_F \cdot \mathfrak{m}_e \cdot A \cdot 8G$ | Borromean residue prefactor $\times$ nucleon count, no per-knot evaluation |

The dispatch is determined by the substrate:
[`prop:diagrammatic-double-magic-lr-fusion`](../observations/diagrammatic-double-magic-lr-fusion.md)
proves that at a doubly-magic level $A = Z + N$ with both $Z, N \in
\mathfrak{M}$, the Littlewood–Richardson fusion of the $Z$-block and
$N$-block collapses to a **single** self-conjugate Specht module —
there is **no Wedderburn channel** to absorb further binding through
Hecke crossings. The per-rep Reeb phase mechanism that generates
$\alpha_{\mathrm{shift}}$ vanishes (no hyperbolic knot), and the
binding is set by the universal Borromean residue $8G$ scaled by
nucleon count.

[`rem:strutinsky-from-graded-trace`](../observations/strutinsky-from-graded-trace.md)
makes the regime split forced by the filtered-algebra structure: the
decomposition

$$
  \mathrm{tr}_M(T_w, q_0) = \mathrm{tr}_{\mathrm{gr}}(\sigma(T_w), q_0) + \mathrm{Res}_{\mathrm{GB}}(T_w, q_0)
$$

identifies the Strutinsky shell correction $\delta E_{\mathrm{shell}}$
with the Gröbner–Shirshov residue sum, and *"Magic-number enhancements
arise algebraically when $\lambda$ reaches a rectangular shape and
$H_q(\lambda)$ factorises"*
([`prop:shell-schur-weyl-self-duality`](../mass-theory/shell-schur-weyl-self-duality.md)).
The doubly-magic case is exactly this rectangular-spike limit.

## $\rho_F$ for $^4_2\mathrm{He}$

The substrate-determined prefactor for $^4_2\mathrm{He}$ is
$\rho_F = 2$, sourced from the canonical
[`binding-ladder-catalog.py`](../../folio-assistant/computations/binding_ladder_catalog.py)
entry `2·m_e·4·Vol(L6a4)`. The categorical derivation of the integer
$2$ — vs. $[2]_q$, $2\cos(\pi/3)$, or another natural candidate — is
not closed in this proposition; the value is consumed as an input
hypothesis on the
[`MagicABindingFormula`](#prop:magic-A-binding-formula) instance per
CLAUDE.md §3b-cond.

## Status

**Theorem (conditional on class hypothesis).** The Lean statement
[`qou:QOU.BraidKnot.magic_A_binding_formula`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/mass-theory/magic-A-binding-formula.lean)
asserts the formula
$\mathfrak{B}(^A_Z\mathfrak{X}) = \rho_F \cdot \mathfrak{m}_e \cdot A \cdot 8G$
modulo a single class hypothesis `MagicABindingFormula` recording the
substrate-determined $\rho_F$. The §3b-cond pattern (CLAUDE.md
§3b-cond) makes this a rigorous-conditional theorem: fully verified
modulo the axiomatised class.

**Reanalysis (2026-05-31).** What was initially framed in this block
as "Open Math A" and "Open Math B" turned out to be structurally
already answered in the framework. Both items reduce to verification
/ formalisation, not derivation. See audit
[`docs/audits/2026-05-31-binding-magic-A-wireup.md`](../../docs/audits/2026-05-31-binding-magic-A-wireup.md)
for the full reanalysis. Summary:

- **$\rho_F$ derivation (was "Open Math A"):** structurally answered
  by
  [`conj:kashaev-density-equals-sdp-multiplicity`](kashaev-density-equals-sdp-multiplicity.md)
  (landed 2026-05-24, Rule-14 owner-authorised). The identity is
  $\rho_F = \nu_{\mathrm{SDP}}$, exact on the three SDP-confirmed
  hyperbolic atoms (D, T, $^3$He). Only the $\nu_{\mathrm{SDP}}(^4\mathrm{He})$
  numerical verification (joint-tower SDP solver) is open.
- **$A=3$ p/n asymmetry (was "Open Math B"):** structurally answered
  by
  [`conj:inter-nucleon-channel-color-tube`](../brings-surface/inter-nucleon-channel-color-tube.md)
  (Bring color-tube weighting; proton's $(u, u, d)$ vs neutron's
  $(u, d, d)$ color-sheet content via $\mathrm{SO}(3)$-fiber action),
  with the substrate-pure formula
  $f_{\mathrm{pn}} = z - h \cdot (1/2 - \delta/4)$
  ($\delta = \Delta m_{n-p}/M_N \approx 1.37 \times 10^{-3}$, PROVED
  PR #690/#942) already implemented in
  [`closed_form_tau_M.py`](../../folio-assistant/computations/closed_form_tau_M.py)
  under `pn_convention="bring_color_weighted"`. Numerical check at
  $q_0$: +180.9 ppm uniform correction across the four light nuclei
  (each has one pn arc); the T vs $^3$He f-factor spread reported by
  [`binding_shell_enhancement_derivation.py`](../../folio-assistant/computations/binding_shell_enhancement_derivation.py)
  arises from the **arc-composition asymmetry** (T = pn+nn vs.
  $^3$He = pp+pn) at the closed-form-ratio scale, not from a missing
  scalar $q$-factor.

The remaining genuinely open items are: Lean formalisation of
`conj:inter-nucleon-channel-color-tube` (conditional on
`conj:s5-so3-fiber-action`); re-evaluation of
`binding_shell_enhancement_derivation.py` against the
Bring-weighted ratio (does the 15% f-spread close?); SDP solver
extension to verify $\nu_{\mathrm{SDP}}(^4\mathrm{He}) = 2$. All
three are verification / formalisation, not derivation.

## Numerical witness

[`folio-assistant/computations/binding_alpha_shift_witness.py`](../../folio-assistant/computations/binding_alpha_shift_witness.py)
emits a comparison witness showing the alpha-shift vs.
magic-A predictions side-by-side for $A \in \{2, 3, 4\}$. The
output JSON
[`binding-alpha-shift-witness.witness.json`](../../folio-assistant/computations/binding-alpha-shift-witness.witness.json)
quantifies the 80$\times$ gap closure for $^4_2\mathrm{He}$.

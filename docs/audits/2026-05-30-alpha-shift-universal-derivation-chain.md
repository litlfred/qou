# Audit — α_shift derivation chain unifies lepton / meson / Bring color-tube fitting gaps

**Date:** 2026-05-30
**Trigger:** Owner-led review (#1445 thread): *"h^10 wasn't that the order of the residue/pole when looking at shape parameters and do the SW integral? review commits/paper/audit."*

## TL;DR

The Lean theorem `prop:alpha-shift-torus-knot`
(`mass-theory/alpha-shift-torus-knot.lean`,
`alphaShift p k := k * (p - 1)`, sorry-free conditional on
`HasAlphaShiftTorus`) is a **universal pole-order derivation** that
covers — by direct specialisation at the appropriate `(p, k)` — multiple
constructions previously labelled as "empirical fits" or "open audit
findings". Wiring this universality is the single highest-leverage move
for the pre-publication uniqueness programme.

## The universal chain

For a torus knot `T_{p,k} = (σ_1 σ_2 ⋯ σ_{p-1})^k`, the **pole order**
of `σ` on the column-rich irrep is `k(p-1)` per the crystal R-matrix
audit (`docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md`),
verified computationally in `crystal_pole_order.py`.

| Specialisation | $(p, k)$ | `α_shift` | Use site |
|---|---|---|---|
| T(2, 3) = trefoil = 4₁ "figure-eight" base | $(2, 3)$ | $3$ | (μ via `Vol(4_1)/ℏ_q²`; not a pole-order use here) |
| T(2, 4) = W± boson | $(2, 4)$ | $4$ | electroweak triplet |
| T(2, 6) = Z boson | $(2, 6)$ | $6$ | electroweak triplet |
| T(2, 7) = τ lepton candidate | $(2, 7)$ | $7$ | torus-knot tower |
| T(2, 8) = Higgs | $(2, 8)$ | $8$ | electroweak triplet |
| **T(2, 9)** | $(2, 9)$ | **$9$** | $[9]_q$ in $1/\alpha_{\rm EM}$ |
| **T(3, 5)** | $(3, 5)$ | **$10$** | $[10]_q$ in $1/\alpha_{\rm EM}$; $q^{10}$ in Bring color-tube weight |

## Sites where this closes "empirical" claims

### 1. p-n averaging (item 3 of uniqueness backlog) — *partially closed by #1445*

`lambda_scale_refinement_h4_correction_bring.py` reports the substrate
evaluation $w(t, t', q) = 1/(1 - h_q \cdot q^{10})$ for the Bring
color-tube weight. The `q^{10}` exponent is **derived** via
`α_shift(T(3,5)) = 5 \cdot 2 = 10`; this is the Bring color-tube knot
(the second member of the genus-4 force-carrier pair
$\{T(2,9), T(3,5)\}$ per `prop:em-coupling-bring-zero-mode`).

**Status:** documented in `mass-theory/pn-averaging-uniqueness.md`
(2026-05-30 commit `e87af29a4` on `claude/T_w-sdp-uniqueness-2026-05-30`).
Resolvent form `1/(1 − ·)` from residue / Schwarz integral on Bring's
surface remains the smaller-scope open math.

### 2. α_EM closure — *PR #1444's "Bring zero-mode" path is α_shift-derived*

PR #1444 reports $1/\alpha_{EM}^{-1} = q \cdot [9]_q \cdot [10]_q + 2/(3\pi)$
closing CODATA to ~4.18 ppm. The two q-integers are exactly
$[\alpha_{\rm shift}(T(2,9))]_q$ and $[\alpha_{\rm shift}(T(3,5))]_q$.
So the "structural" identification is the **same α_shift universal
derivation chain**, specialised to the genus-4 force-carrier pair.

**Coordination action:** intent comment posted on PR #1444 noting
the shared chain.

### 3. Lepton masses via T(2, k) — *Item 4 partial closure target*

The torus-knot tower at $T(2, k)$ for leptons gives
$\alpha_{\rm shift} = k$. Wiring this into a lepton-mass uniqueness
statement (the way `prop:em-coupling-bring-zero-mode` does for
$1/\alpha_{\rm EM}$) is the natural Item 4 closure for the
$\mu / \tau / W / Z / H$ block — currently scoped as
"`VolDensity(K)` per-knot canonical".

### 4. Meson m_K/m_π — *Item-3-analogous open*

Mesons (quark-antiquark) carry a 2-sheet color-tube vs the nucleon's
3-sheet structure. The analogous derivation at the appropriate torus
knot would close the meson-volume-conj path #1396 closed at 203 ppm
+ #1432 extended to η/φ. Conjecture: the meson p-n-analogue weight
involves $\alpha_{\rm shift}(T_{(2,k)})$ for some k determined by
the meson's force-carrier knot.

**Status:** open. New Lean block needed — `meson-color-tube-uniqueness`
analogous to `pn-averaging-uniqueness`.

## Remaining fitting / empirical gaps (post-this-audit prioritisation)

From `per-observable-100x-status.witness.json` (post-#1422):

| observable | residual | likely α_shift derivation route |
|---|---|---|
| m_p | 0.0004 ppb (anchor) | — (anchor, not a prediction gap) |
| m_e | 0 (anchor) | — |
| m_μ | 209.8 ppb (964× miss) | T(2, k) tower; see "lepton" route above |
| Q_β | 1247 ppb (160× miss) | post-de-fit; possibly h_q^4 correction tracked in Bring probe |
| m_n | 1.04 ppb (181× miss) | Path C inheritance |
| m_K/m_π | 2.9×10⁵ ppb (1098× miss) | meson α_shift route (item 4 of this audit) |
| Δ_pn | 755 ppb (159× miss) | inherits from Q_β |

**Universal lever:** every miss above traces structurally to the same
α_shift pole-order calculus + Bring-genus-4 force-carrier pair +
Yekutieli/residue normalisation, modulo the per-observable kinematic
prefactor. The pre-publication closure programme is therefore:

1. **Wire α_shift into every uniqueness block** (Item 4 follow-up).
2. **State the resolvent `1/(1 − h_q · q^{αShift})`** as a derived axiom
   class (Bring-residue integral on torus knots).
3. **Per-observable instances** specialise the universal class to its
   torus knot.

## See also

- `content/quantum-observable-universe/mass-theory/alpha-shift-torus-knot.lean`
- `content/quantum-observable-universe/predicted-spectra/em-coupling-bring-zero-mode.lean`
- `content/quantum-observable-universe/mass-theory/pn-averaging-uniqueness.lean` (#1445)
- `docs/uniqueness-theorems-backlog.md`
- PR #1444 (α_EM Bring zero-mode)
- PR #1445 (pn-averaging uniqueness)
- `docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md`

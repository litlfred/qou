# q-Bessel 2nd-kind as the color-tube radial propagator — avenue for the mass endomorphism

**Date:** 2026-06-23
**Branch:** `claude/nice-dirac-ywun65` (PR #2661)
**Status:** scope / avenue doc — framing + corpus-grep state + the one open gate. No fit; nothing wired; exploratory.
**Bean:** [`qbk2`](../../.beans/qbk2--qbessel-2nd-kind-quadratic-action-binding-correction.md)

## The picture (owner intuition, made precise)

Bessel **2nd-kind** functions are the *tube* solutions:

| solution | behaviour at the axis `r=0` | geometry it belongs to |
|----------|------------------------------|------------------------|
| `J_ν` (1st kind) | regular | solid disk (no hole) |
| `Y_ν` (2nd kind / log-Neumann) | singular (log/power) | **annulus / tube** (axis excluded) |
| `K_ν` (modified) | exponential decay | **confined** mode in the tube wall |

So a **color flux tube** — a cylinder with a core — has its transverse modes built from `Y_ν` / `K_ν`, not `J_ν` alone. The product `J_ν(x)·Y_ν(x)` is the diagonal of the **radial Green's function** — the *coincidence propagator*. "Information propagation across the color tube" = the off-diagonal Green's-function elements = the inter-nucleon coupling = **binding**.

### Why this is structurally exact in QOU, not an analogy

- The Hahn–Exton q-Bessel is the **matrix coefficient of `E_q(2)`** (the quantum group of motions of the plane, the `SU_q(2) → E_q(2)` contraction; Vaksman–Korogodsky 1989 / Koelink 1994 — cited in [`QBesselContiguityRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QBesselContiguityRecurrence.lean)). `E_q(2)` is the symmetry of a **q-cylinder**.
- The **first/second-kind partners** (`qbessel_first_kind_coeff_closed_form` / `qbessel_second_kind_coeff_closed_form`, wired in this PR) are the **`SU_q(1,1)` (quantum *hyperbolic* plane)** solutions — the negative-curvature "throat" geometry of a flux tube.
- The **Reeb flow** (writhe/framing rotational flow on knot operations) is the radial datum: the "growth sector" `|r_λ|>1`, `θ_λ = arccosh|r_λ|`, the extensive `q^{writhe}` channel ([`2026-06-20-qbessel-reeb-flow-radial-argument.md`](../audits/2026-06-20-qbessel-reeb-flow-radial-argument.md)).

So binding is, on this picture, a **q-Bessel Green's-function difference along the Reeb flow**:
$$\delta \;=\; \sum_\lambda y_\lambda\,\chi_\lambda \,\big[\,G_q^\lambda(x_{\text{atom}}) - G_q^\lambda(x_{\text{free}})\,\big],\qquad x_\lambda=\theta_\lambda,\ \nu=\dim_\lambda-1,$$
with `G_q = g1·g2 / Casoratian` the q-Casoratian-normalised coincidence propagator (q-Abel law proved sorry-free in `QCasoratianAbel.lean`).

## Is qbk2 wired into compute? — precise answer

**Production: NO.** qbk2 is the **subdominant-but-real / not-yet-forced** binding correction — not in any production mass/binding path; `c_k` / `Δ_λ` stay cal-anchored. Wiring it into production would require it to be **forced AND on-scale**, which it is not yet (matching `B(D)` by a chosen prefactor would be a CAL-4 fit).

**Lean machinery: YES, sorry-free** — `QBesselContiguityRecurrence`, `QCasoratianAbel`, `QLommelOrderRecurrence`. The **contiguity skeleton** is now compute-wired (this PR, `qbessel_jackson_contiguity.py`).

**Exploratory compute: YES, a rich trail** (all "no fit; nothing wired"):

| script | what it computes | result |
|--------|------------------|--------|
| `qbessel_reeb_flow_radial_forced.py` | classical `(πx/2)J_n Y_n` propagator δ | δ = −0.172, ratio **0.04×** (~25× small) |
| `qbessel_qdeformed_reeb_scale.py` | fully q-deformed `G_q` (±0.5 order proxy) | ratio **6.16**, cross-anchor stable (0.033) — a **~150× q-enhancement** into the few-× ballpark, BUT proxy-swing 0.43 + 64% single-block-dominated ⇒ **not forced** |
| `qbessel_reeb_yweighted_gap.py` | proper integer-order `g2` + real `y_λ` weights | (run-and-captured in this PR) |

## The one open gate (the script's own verdict)

The q-deformation is a **real ~150× effect** — "not wrong, just first computed in the classical convention." What it is **not yet** is *forced*. To go from "promising lead" to "wireable", three forced (non-fit) steps remain:

1. **Proper integer-order log-Neumann** `Y_n(x;q)` — remove the ±0.5 half-integer proxy that produces the proxy-swing (0.43) and the unphysical `ν=−0.5` single-block domination (64%). The **reduction-of-order `g2`** (q-integral form, `qbessel_reeb_yweighted_gap.py`) is the proper integer-order second solution and has **no `(q^k−q^ν)` resonance**, so it evaluates at integer `ν=dim−1` directly.
2. **Real `y_λ χ_λ` Markov weights** — substrate-fixed (depend on `q₀` only), no knob.
3. **Definite bar-parity** — the correction must carry a fixed `q ↦ q⁻¹` parity (`QBesselBarCovariance.lean`).

**Decisive test (this PR):** does the proper integer-order + `y_λ`-weighted δ stay on-scale AND lose the single-block-domination artifact? If yes → promote to a Lean lemma + wiring candidacy. If it drifts off-scale → the q-enhancement was a proxy artifact and the lead is demoted honestly.

## Why this could sharpen the mass endomorphism

The mass endomorphism's binding part is its **inter-block (inter-nucleon) coupling**. Casting it as a Green's-function *difference* reframes binding as a **spectral / propagator** quantity — **extensive, additive over inter-nucleon bonds** — which is exactly the 2026-06-02 reframe (binding is the additive many-body bond sum / Path A, not an intensive per-λ `Δ_λ` density). The q-Bessel modes diagonalise the q-tube radial operator, so this is the natural basis in which the endomorphism's binding sector is block-diagonal. It does **not** touch the per-knot mass (`m = m_e·Vol·ρ/ℏ_q²`); it is a binding-sector organising principle.

## Convergence with live siblings (coordination)

- **#2325** — wires "q-Bessel **2nd-kind** m_qCLT factorized binding" + the b-ladder `b = 2cosh(10η₀)` *from the 2nd kind*. Same tube-mode object.
- **#2612** — found the charge `S_λ` = the "**free-vs-atom q-Reeb phase `|Δθ_λ|`**" (117% of the Coulomb scale, right order). The same Reeb-bundle propagator-difference, applied to the charge split.

Three independent lines circling the same object is a genuine signal, not a coincidence.

## Discipline

No fit. The binding scale must be reached by the **forced** q-deformation + `y_λχ_λ` weights, never a tuned prefactor or chosen order-offset. Exploratory; audit-only; gated until forced AND on-scale. Per the "too small ≠ wrong" triage ([`2026-06-23-too-small-not-wrong-conflation-triage.md`](../audits/2026-06-23-too-small-not-wrong-conflation-triage.md)), qbk2 is **SUBDOMINANT-but-REAL**, not refuted.

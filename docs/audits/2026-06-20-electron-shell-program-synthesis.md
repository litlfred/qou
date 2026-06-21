# The electron-shell program in QOU — consolidated synthesis

**Date:** 2026-06-20
**Branch:** `claude/zealous-hypatia-05xyp9` (PR #2348, bean `e2nf`)
**Status:** consolidation of the electron-shell arc (6 audits + compute below).
Paper-ready prose; **to promote** to a `predicted-spectra` content block once the
content-validation pipeline is available (absent on this sparse checkout).

---

The Level-6 (atom→electron) layer of QOU asks how much of the **periodic table** —
shell capacities, the Aufbau order, the noble gases, the electron-binding scale —
follows from the substrate Hecke structure rather than being imposed. The arc
below answers it sharply: **QOU derives the capacities and the binding scale, and
names the ordering's structure, but leaves one reading of the ordering
un-derived.** Throughout, the discipline was *formalize-first* (state the
structural claim, then test), and three would-be derivations of the ordering were
ruled out by sign or by overshoot at the physical `q₀ ≈ 1.11`.

## 1. Shell capacity `2n²` — the self-square of one bar-even element (essentially derived)

The capacity is the **self-fusion of a single angular q-dimension**, with **no
second compact `SU(2)`**:

$$
  2n^2 \;=\; 2\,[n]_q^2\big|_{q=1},
  \qquad
  [n]_q^2 \;=\; \sum_{\ell=0}^{n-1} [2\ell+1]_q \quad(\text{q-Clebsch–Gordan}),
$$

with `[n]_q = U_{n-1}((q+q^{-1})/2)` the **bar-even (cosh)** Chebyshev evaluation
of the shell element `U_{n-1}` (verified exactly, `shell_capacity_chebyshev_bridge.py`).
The standard `SO(4)=SU(2)×SU(2)` `(j,j)` "doubling" is here the *self-square*
`V⊗V` of **one** object — the second factor a copy of the first, tied by the
coproduct — so the owner's "we don't need a second SU(2)" is vindicated: the
compact (`cos/sin`, root of unity) and non-compact (`cosh/sinh`, real `q`) forms
are the two real forms of one `sl(2,ℂ)` = the complex volume `𝔙`
(`bar-parity-split`, duality-tracker D1/D3). Residual: that the shell space *is*
the self-square (one clean coproduct step), not a fit.
*(Audit: `2026-06-20-shell-2n2-from-self-square-no-second-su2.md`.)*

## 2. Shell stability `σ_F` — the monotone confinement-SDP dual

The selection principle is the **dual objective** of the confinement SDP,
`σ_F(P^Z,q) = n_target·y₀*`, which is **monotone non-decreasing** in the electron
count (SDP-relaxation, strong-duality gap ≈ 1e-9; `electron_sigma_f_chain.py`).
Consequences:

- "Add electrons until the SDP won't solve" is structurally invalid — `σ_F` never
  goes infeasible; the raw-Gram `Gx≥0` "capacities" (H≈5, He≈8) are the excluded
  **eigenvalue-interlacing** branch (`electron_shell_sdp_capacity.py`).
- The noble-gas signal is the **marginal** `Δσ_F = I₁` (ionisation energy) plus
  binding multiplicity `μ ≥ 2`, **not** a local maximum of `σ_F` itself. This
  resolved a real `monotone`-vs-`local-max` inconsistency in
  `prop:shell-closure-stability` (claims 1 vs 2), corrected across the prop, its
  interprets remark, and the Lean docstrings.
*(Audits: `…-electron-shell-sdp-capacity-formalize-first`,
`…-shell-closure-sigma-f-inconsistency-resolved`.)*

## 3. Electron-binding scale — the e-Hartree conditional theorem

The binding scale is the Hartree energy `E_h = α_EM²·m_e c²` (`= 27.21 eV`,
`hecke_core.E_HARTREE_EV`; reproduces hydrogen's 13.6 eV exactly). The `α²`
**scaling is exact in `R`** (the 25-round `conj:e-hartree-categorical-derivation`,
round 20); the absolute energy unit `m_e c²` is **CAL-1**, not derivable by design
(owner-declined Subgoal-2). Wiring it (Level-6 `m_atom = m_sym + Z·m_e − E_e`)
reproduces ¹H atomic mass exactly and shows the atomic-mass residual is ~100% the
nuclear `B_sym` model error (electrons are sub-keV).
*(Audits: `…-level6-atom-electron-wiring`; bonus correction of a prior
25-MeV/electron scale blunder.)*

## 4. Ordering (Aufbau / noble gases) — NOT derived (H_scalar refuted)

The filling order reduces to a single **ℓ-coefficient `a`** in the key
`K(n,ℓ)=n+a·ℓ` (Madelung is `a=+1`).

**What IS derived (eigenvalue identity).** The `T_γe = [[q−q⁻¹,1],[1,0]]`
eigenvalues are **exactly** `{q, −q⁻¹}` (sympy: discriminant `(q−q⁻¹)²+4 =
(q+q⁻¹)²`, `det=−1`), **identical to the Hecke generator eigenvalues**
`(σ−q)(σ+q⁻¹)=0`. Since `σ_i` obeys this quadratic in *every* representation, its
eigenvalues are `{q, −q⁻¹}` on **every** block, with Perron `λ₊ = q`. `T_γe` *is*
a Hecke generator. And on the **scalar** (trivial, 1-dim) block `σ_i ↦ q`, so a
length-`L` word weighs `q^L` ([`prop:symmetric-block-domain-weight`](../../content/quantum-observable-universe/molecular-construction/symmetric-block-domain-weight.md),
`symmetric_block_domain_weight`, **Lean sorry-free**).

**What is NOT derived — `a=+1` (owner: "don't assume only scalar channels").** The
`q^ℓ = λ₊^ℓ` reading (a=+1) lives on the **scalar** block. But angular momentum
`ℓ` is intrinsically the **non-scalar** `(2ℓ+1)`-dim irrep `V_ℓ`, where `σ_i` is a
*matrix* and **every** natural object overshoots to `q^{2ℓ}` (a=+2): the weights
`q^{2m}` (`m=−ℓ..ℓ`), the highest weight `q^{2ℓ}`, and the trace (q-dimension)
`[2ℓ+1]_q` (`aufbau_symmetric_block_channel.py`). **No** weight equals `q^ℓ`
(needs half-integer `m=ℓ/2`). So `q^ℓ` is obtainable **only** by projecting the
angular content onto the scalar block *and* equating word-length with `ℓ` — and
**those assumptions are exactly the content of Madelung.** The scalar shortcut is
**load-bearing**; without it everything overshoots.

| channel | object | `a` | status |
|---|---|--:|---|
| scalar block | `q^ℓ = λ₊^ℓ` | +1 | **matches Aufbau, but ASSUMES the scalar projection** |
| non-scalar `V_ℓ` (weight/h.w./trace) | `q^{2ℓ}` | +2 | the genuine angular rep — overshoots |
| antisymmetric (#2531) | `(λ₋/λ₊)^ℓ` | −2 | wrong sign |

**The ordering is OPEN — to be DERIVED, not accepted as input and not fitted.**
Correctly framed:

> **Why would an atomic orbital's angular content be the SCALAR-block projection
> (`q^ℓ`, a=+1) and not the genuine non-scalar `V_ℓ` action (`q^{2ℓ}`, a=+2)?**

The candidate bridge [`conj:palindromicity-orbital-type`](../../content/quantum-observable-universe/molecular-construction/palindromicity-orbital-type.md)
(`ℓ = ½·palindromic-defect`) was **examined and does not bridge** (audit
`2026-06-21-palindromicity-does-not-justify-scalar-projection`): its defect `= 2ℓ`
is the *same* `2ℓ` as the non-scalar overshoot, and the `½` recovers the *label*
`ℓ`, not the *energy* — so proving it supports `q^{2ℓ}`, not `q^ℓ`. The gap
therefore reduces to **one** isolated hypothesis:

> **H_scalar** — an orbital's energy is the **symmetric-block (scalar) component**
> of its angular braid word (`q^ℓ`), not the non-scalar `V_ℓ` action (`q^{2ℓ}`).

**`H_scalar` was attacked and REFUTED** (audit
`2026-06-21-h-scalar-refuted-post-hoc-functional-choice`): QOU has **three**
natural orbital-energy functionals — `σ_F` (SDP dual, `a=0`), symmetric-block
`q^ℓ` (`a=+1`), `tr_M`/q-dim `q^{2ℓ}` (`a=+2`) — and `a=+1` sits **between** the
two natural outputs, never produced by either. Decisive rep-theory: the atomic
orbital `V_ℓ` (ℓ≥1) has **zero** trivial-block multiplicity, so `q^ℓ` is the
**molecular `C_nv`-projector** construct with **no atomic analog** (isolated atom:
full `SO(3)_q`, trivial rep only `ℓ=0`); the rotation-invariant atomic scalar is
the q-dim trace `~q^{2ℓ}` (`a=+2`). So `H_scalar` selects the `a=+1` functional
**because it matches Madelung** — a fit-by-functional-choice, forbidden by the
three-calibration discipline.

**Honest framework conclusion: QOU derives the shell *capacities* (`2n²`,
sorry-free Lean) but does NOT derive the shell *ordering*.** Its canonical
observable (`tr_M`) predicts `a=+2` — the ℓ-dominated overshoot — disagreeing with
the empirical periodic table. Madelung stays **OPEN**, not accepted as a
semi-empirical input and not reached by selecting a functional to fit it (owner
STRICT). A real derivation would need a *derived* screening operator contributing
exactly `+ℓ` per unit angular momentum (from the inner-shell penetration braid),
which is not in the corpus.

*(Audits: `…-h-scalar-refuted-post-hoc-functional-choice` (refutation),
`…-palindromicity-does-not-justify-scalar-projection`,
`…-aufbau-lambda-plus-channel-from-symmetric-block`,
`…-aufbau-from-dominant-eigenvalue-duality`.)*

## Net

| layer | QOU result |
|---|---|
| **capacity** `2n²` | **derived** — self-square `[n]_q²` of the bar-even element; no second SU(2) |
| **stability** `σ_F` | **derived** — monotone confinement-SDP dual; closure = marginal `Δσ_F` + `μ≥2` |
| **binding scale** `E_h` | **conditional theorem** — `α²` exact in `R`; unit = CAL-1 (by design) |
| **ordering** (Aufbau) | **NOT derived** — `H_scalar` refuted (fit-by-functional-choice). Canonical `tr_M` predicts `a=+2` (ℓ-dominated overshoot), disagreeing with the periodic table; `a=+1` Madelung sits between the framework's `σ_F` (a=0) and `tr_M` (a=+2) outputs, produced by neither. **OPEN**, not accepted (STRICT) |

QOU **derives the periodic-table capacities and the electron-binding scale**, but
**does NOT derive the shell ordering** — its canonical observable predicts an
ℓ-dominated overshoot, and the empirical Madelung order is reachable only by
selecting a functional to fit it (refuted). The CAL-1 unit remains by design. No
fits were introduced; the open items — and the framework's failure to derive the
ordering — are stated, not papered over.

## Provenance

Compute: `shell_capacity_chebyshev_bridge.py`, `electron_sigma_f_chain.py`,
`electron_shell_sdp_capacity.py`, `electron_sigma_f_marginal.py`,
`atom_electron_mass.py`, `madelung_sdp_filling_order.py`,
`aufbau_eigenvalue_channel.py`. Sibling: #2531 (merged, eigensplit null).
Audits (all `docs/audits/2026-06-{16,20}-…`): level6-atom-electron-wiring,
electron-shell-sdp-capacity-formalize-first, sigma-f-electron-dressing-chain,
shell-closure-sigma-f-inconsistency-resolved, 2n2-shell-capacity-derivation-gap,
2026-06-20-shell-2n2-from-self-square-no-second-su2,
2026-06-20-madelung-from-sdp-falsifiable-test,
2026-06-20-gap2-ordering-ell-coefficient-synthesis,
2026-06-20-aufbau-from-dominant-eigenvalue-duality.

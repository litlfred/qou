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

## 4. Ordering (Aufbau / noble gases) — structure named, one reading un-derived

The filling order reduces to a single **ℓ-coefficient `a`** in the key
`K(n,ℓ)=n+a·ℓ` (3d/4s crossover needs `a>½`; Madelung is `a=+1`). The angular `ℓ`
couples through one of the `T_γe` eigenvalues (`λ₊=q₀` dominant, `λ₋=−1/q₀`
sub-dominant, `λ₊λ₋=det=−1`), and the **Markov/Frobenius pairing is
Perron-dominated by `λ₊`** — so reading `ℓ` on the dominant channel,
`λ₊^ℓ = q₀^ℓ`, gives `a=+1` = the **empirical Aufbau order** (4s<3d, 5s<4d, …;
`aufbau_eigenvalue_channel.py`). That is the right eigenvalue and the right order.

But the *derivation* of "angular `ℓ` enters as `λ₊^ℓ`" is **not** supplied: three
structural candidates for `a` were each ruled out —

| candidate | object | `a` | ruled out by |
|---|---|--:|---|
| eigensplit (#2531, merged) | `(λ₋/λ₊)^ℓ` | −2 | **sign** (anti-penetration) |
| q-dim loop-trace | `[2ℓ+1]_q` | +2 | **overshoot** (ns-dominated) |
| `√`-q-dim ("half") | `√[2ℓ+1]_q` | — | **overshoot at `q₀`** (near-classical) |

The exact `λ₊^ℓ` works but rests on the un-derived *open-transfer* reading; the
natural categorical objects (the loop-trace and its root) overshoot because
`q₀≈1.11` is near 1, where `[2ℓ+1]_q≈2ℓ+1` (classical) rather than `q^{2ℓ}`.

**The ordering is OPEN — to be DERIVED, not accepted as input and not fitted.**
The derivation target is now precise: *prove that an electron orbital's angular
momentum `ℓ` enters the Markov/Frobenius amplitude as `ℓ` **dominant-channel
(`λ₊`) open-transfer steps** — `λ₊^ℓ` — from the braid topology of the open
electron strand, exactly as the radial `n` enters as `n` dominant curls.* The
three ruled-out candidates (sub-dominant `λ₋`, loop-trace q-dim, its root) narrow
the search; `λ₊^ℓ` is the **unique** survivor that yields Aufbau, so the open
problem is its **topological derivation** — why the angular nodes are dominant
(`λ₊`) curls, not sub-dominant or loop closures. (Madelung's known fragility in
standard QM — Cr, Cu, Pd — is why this is *hard*, not a licence to accept it.)
*(Audits: `…-gap2-ordering-ell-coefficient-synthesis`,
`…-aufbau-from-dominant-eigenvalue-duality`.)*

## Net

| layer | QOU result |
|---|---|
| **capacity** `2n²` | **derived** — self-square `[n]_q²` of the bar-even element; no second SU(2) |
| **stability** `σ_F` | **derived** — monotone confinement-SDP dual; closure = marginal `Δσ_F` + `μ≥2` |
| **binding scale** `E_h` | **conditional theorem** — `α²` exact in `R`; unit = CAL-1 (by design) |
| **ordering** (Aufbau) | **structure named** (`λ₊`/Aufbau); 3 derivations ruled out — **OPEN, derivation target:** angular `ℓ = ℓ` `λ₊` open-transfer steps (`λ₊^ℓ`), topological (not input, not fit) |

QOU **derives the periodic-table capacities and the electron-binding scale, and
identifies the ordering's eigenvalue structure**, while the ordering's one free
reading and the CAL-1 unit remain — the latter by design. No fits were
introduced; the open items are stated, not papered over.

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

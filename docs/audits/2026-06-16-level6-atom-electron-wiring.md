# Level 6 — atom→electron mass wiring (diagnostic)

**Date:** 2026-06-16
**Branch:** `claude/zealous-hypatia-05xyp9`
**Compute:** [`computations/atom_electron_mass.py`](../../computations/atom_electron_mass.py)
**Class:** exploratory diagnostic — no production rewire, no fit, no witness
(mirrors `/dashboard-low` and PR #2343).

## Scope

Extends the nuclear mass dashboard (`m_sym`, `/dashboard-low`, which compares
*nuclear* masses) up one level to the **neutral atom**, so the prediction can be
compared against AME2020 **atomic** masses apples-to-apples:

$$
  m_{\text{atom}}(Z,N) = \underbrace{m_{\text{sym}}(Z,N)}_{\text{nucleus}}
    + Z\,m_e - E_{e\text{-binding}}(Z).
$$

This is the "Level 6 (atom-electron)" item that the infrastructure audit lists
as not-yet-in-pipeline. It exercises the electron-shell terms the owner asked
about ("isotope + an electron, add electrons until the SDP won't solve").

## Coordinate context (why this scope)

The `m_sym` / binding / Δ_λ area is heavily in flight (all owner PRs, all
< 24 h at session start):

| PR | what | relation |
|---|---|---|
| #2343 | m_sym **error budget** (pred vs AME/CODATA, decomposed to source) | the error-breakdown itself — **done** |
| #2078 | atom→V_hyp→**Δ_λ closure** of `B(K)=m_e Σ y_λ χ^λ Δ_λ` | the B_sym frontier |
| #2325 | m_qCLT binding wired; **Δ_λ b-ladder slope derived** (A=2..12) | the B_sym frontier (deepest) |

None touch the **electron-shell level** — so this session takes that
unclaimed piece. It buys *completeness* (atomic comparison + the electron
terms), **not** accuracy: the atomic-mass residual is dominated entirely by the
nuclear `B_sym` model error (MeV), which #2078 / #2325 already own.

## The electron-binding scale is already derived-to-its-floor

The binding scale is **not** an open green-field problem. It is the Hartree
energy and is the subject of the 25-round
[`conj:e-hartree-categorical-derivation`](../../content/quantum-observable-universe/predicted-spectra/e-hartree-categorical-derivation.md)
([investigation log](2026-06-13-e-hartree-investigation-log.md)) — a **clean
conditional theorem**:

| piece | status |
|---|---|
| `E_h = α_EM²·m_e c²` — the **α² scaling** | **exact in R** (round 20) |
| 1/n² relative shell spacing | derived (round 8b) |
| electron **capacity** (count / noble-gas closure) | categorical — `ElectronShell.bindingMultiplicity` (SDP active dual support) |
| absolute energy **unit** `m_e c²` | **CAL-1**, owner-declined Subgoal-2 — not a gap, a calibration input by design |
| inter-electron **screening** (`Z_eff`) | open magnitude piece (eV-scale) |

The canonical value is **wired already**: `hecke_core.E_HARTREE_EV = 27.2115 eV`,
`α_EM = 1/137.036` (derived), `Ry = E_h/2 = 13.6057 eV`.

**Correction of the prior detour.** A prior session (different agent) recomputed
the electron scale from scratch as `E₀·α² ≈ 223 eV` using the *nucleon* scale
`E₀ ≈ 4.186 MeV`, then `−α_EM·ln|V|` updates worth ~25 MeV **per electron** — a
scale error of ~6 orders of magnitude — and concluded the electron binding was
"research-grade, not derived" (reading only the stale `bohr_radius_categorical`
caveat, missing the entire e-Hartree thread). The correct scale is the electron
Hartree `α²·m_e ≈ 27 eV`, and it is already canonical.

## Results (low isotopes ¹H–⁷Li)

`q₀ = 1.109979`, `α = E₀ = 4.1860 MeV`, `E_Hartree = 27.2115 eV`,
`Ry = 13.6057 eV`.

### Electron binding (QOU shell structure @ e-Hartree scale, bare-Z)

| atom | Z | shell fill | E_e (eV) | note |
|---|--:|:--|--:|:--|
| ¹H–³H | 1 | n1:1 | 13.61 | **= H ionization, exact** |
| ³He,⁴He | 2 | n1:2 | 108.85 | over-binds (no screening; real He 79 eV) |
| ⁶Li,⁷Li | 3 | n1:2·n2:1 | 275.52 | over-binds (no screening; real Li 204 eV) |

### Atomic mass vs AME2020, residual decomposed

`Δ_total = Δ_nuclear (B_AME − B_sym) + Δ_electron` (sub-keV).

| atom | A | m_atom | M_AME(atom) | Δ total (MeV) | Δ nuclear | Δ electron (keV) |
|---|--:|--:|--:|--:|--:|--:|
| ¹H | 1 | 938.783 | 938.783 | **+0.000** | +0.000 | +0.000 |
| ²H | 2 | 1874.459 | 1876.124 | −1.665 | −1.665 | +0.000 |
| ³H | 3 | 2808.846 | 2809.432 | −0.586 | −0.586 | +0.000 |
| ³He | 3 | 2810.335 | 2809.414 | +0.921 | +0.921 | −0.082 |
| ⁴He | 4 | 3744.722 | 3728.401 | +16.321 | +16.321 | −0.082 |
| ⁶Li | 6 | 5614.985 | 5603.051 | +11.934 | +11.934 | −0.235 |
| ⁷Li | 7 | 6549.373 | 6535.366 | +14.007 | +14.007 | −0.234 |

## Findings

1. **¹H atomic mass is reproduced exactly** (Δ = 0.000 MeV) to the 13.6 eV
   electron-binding level, from canonical constants + the e-Hartree scale alone.
2. **The electron terms are correctly book-kept.** `Z·m_e` (MeV, exact CAL-1)
   and `E_e_binding` (sub-keV) are both right; the no-screening over-binding for
   Z ≥ 2 stays sub-keV (`Δ electron` column: −0.08 keV He, −0.23 keV Li).
3. **The atomic-mass residual is ~100 % the nuclear `B_sym` error** — every
   `Δ_total` equals `Δ_nuclear = B_AME − B_sym` to within the sub-keV electron
   remainder. This confirms the #2343 error-budget verdict at the atomic level:
   accuracy is gated by the nuclear binding model, ~12 orders above 1 ppQ, and
   electrons do not move it.

## Follow-ups (not this PR)

- **Screening (`Z_eff`)** is the open inter-electron magnitude piece of the
  e-Hartree conjecture; a categorical screening would come from the shell-SDP
  inter-electron crossings. eV-scale; does not reach the mass residual.
- **Live SDP capacity demo.** The "add electrons until the confinement SDP goes
  infeasible" experiment wants the `electron-shell-ilp` solver, currently in
  `computations/_deprecated/`. Reviving it canonically (the deprecated scratch
  gave wrong capacities, e.g. H=5) is a separate tranche; here the capacity for
  Z ≤ 3 is the trivial Aufbau filling, with noble-gas closure cited from
  `ElectronShell.lean`.
- Accuracy only moves on `B_sym` → defer to #2078 / #2325.

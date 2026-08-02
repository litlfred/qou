# Deuteron binding as a closed-form symbolic q-invariant of the σ₁³ trefoil — proof-tier attempt

**Date:** 2026-08-02 · **Branch:** `claude/deuteron-symbolic-closed-form-2026-08-02` ·
**Bean:** (deuteron Δ_λ magnitude, `qou-3q7t` family) · **Axis:** Δ_λ / `C_knot` magnitude ·
**Tier:** PROOF-tier attempt (symbolic/exact → Lean-provable if closed) — complement to the
EMPIRICAL tessellation state-sum on the sibling branch
`claude/sigma1cubed-seifert-tessellation-nastokes-2026-08-02` (PR #4619).

## 0. BLUF (to be filled after compute)

The deuteron 5.853× binding deficit collapsed (pincer #4615 `qou-prjo` + #4617 `qou-i4pz`) to
ONE object — the transverse NA-Stokes surface-curvature term on the σ₁³ trefoil Seifert surface =
first-order per-bond amplitude Δ¹g = the fitted `C_knot = 5.853`. A triangulation-invariant
q-deformed surface state-sum (WRT / Turaev–Viro) has a CLOSED FORM equal to a known q-invariant of
the trefoil. This audit asks the **derive-then-check** question: does a closed-form symbolic
q-invariant of the σ₁³ trefoil (T(2,3)), evaluated at the canonical q₀, reproduce
`C_knot = 5.853` with **zero free parameters**?

## 1. Target (locked BEFORE compute — anti-fit)

| quantity | value | source |
|---|---|---|
| B_D (deuteron binding) | 2.22452 MeV | AME2020 (diagnostic only, never inverted) |
| m_e | 0.51099895 MeV | CODATA |
| `\|S(D)\|` | 0.7438 | committed Wenzl-weighted signed Markov sum (#4543) |
| first-order `m_e·\|S\|` | 0.38008 MeV | DT-count derived (#4601) |
| **target `C_knot`** | **5.8528** | `B_D/(m_e·\|S\|)` — the number the closed form must hit, 0-fit |

q₀ (muon-anchored, `computations/` canonical) = `1.10997859555733471989976...`

The trefoil is the **torus knot T(2,3)** = closure of σ₁³ in B₂; **non-hyperbolic**, so
volume/dilogarithm (Bloch–Wigner) routes give 0 and are excluded a priori (§7b caveat).

## 2. Method

Enumerate the canonical closed-form q-invariants of the σ₁³ trefoil at q₀ and check each against
5.8528 with 0 tuning. A hit is proof-tier ONLY if the object is the one the corpus **independently**
identifies as the NA-Stokes surface term (not a scan-selected coincidence — invariant/normalization
choice is a hidden freedom, cf. F3 of `2026-07-13-na-stokes-ck-recursion-binding-adversarial-review.md`).

Probe: [`computations/deltalambda/deuteron_trefoil_qinvariant_closed_form_probe.py`](../../computations/deltalambda/deuteron_trefoil_qinvariant_closed_form_probe.py)
(sympy exact + mpmath 50 dps).

## 3. Results

_(pending compute)_

## 4. Verdict

_(pending)_

## Anti-fit ledger

| statement | status |
|---|---|
| target `C_knot=5.8528` locked before compute | ✓ |
| B_AME used only as diagnostic ratio, never inverted | ✓ |
| free parameters | 0 |

# Q_β 1ppQ keystone — execute the #1622 open bridge (mode → ladder cₖ)

**Date:** 2026-06-18
**Branch:** `claude/dreamy-feynman-nns0ol`
**Goal:** 1ppQ — Q_β (the fibre-level Habiro element `F(q)`, decay-side axis)
**Owner directive:** "gate open this session" + "continue stalled agent"
(the gate = the Q_β 1ppQ keystone; the stalled agent = #2106, last commit
2026-06-10, 8 days idle — it executed Hoefsmit **Stage B** (per-block
operator levels) but did **not** take the orthogonal #1622 **mode→ladder
bridge**, which has never been executed).

---

## 0. What this scope executes

PR #1622 (`habiro_q_difference_mode_solve.py`) decomposed `Δtr_M(u)`,
`u = q^{1/2} = \check q` (the spinor information rate), **exactly** into
three spectral sectors (partial fraction = Fourier-mode q-difference
solve):

| sector | content | bar-symmetry |
|---|---|---|
| (A) entire | `−u⁴/4 − u³/2 + u/2 − 1/2` | — |
| (B) ζ₄ cyclotomic | `1/(u²+1)` pole pair, residues `∓i/2` (WRT level-4) | **bar-even part = exactly 1/2** |
| (C) u=0 Laurent | tower `u⁻¹, u⁻³, u⁻⁴` | — |

`A + B + C = Δtr_M` exactly. PR #1622 left **one defined step open**: the
change of variable `u = √q ↦ u_L = b·ℏ_q²` to read off the ladder `cₖ`
from `Q_β = Q_base · ∏_{k≥2}(1 + cₖ u_L^k)`. This scope executes it.

The ladder/anchor constants (canonical, from
`q-beta-operator-valued-N3.witness.json`):

- `q₀ = 1.10997858275138…`
- `b = 0.86758406696525…` (Hoefsmit)
- `ℏ_q = (q−1)/q`, so in `u`: `ℏ_q = 1 − u⁻²`, `u_L = b·(u²−1)²/u⁴`
- `u_L(q₀) ≈ 0.00852`, `1/u_L ≈ 117`, each rung ≈ 2.07 decimal digits.

---

## 1. Formalize-first gate (the invariant, stated BEFORE the run)

Per the refuted-class map
[`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](../audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
§1, the surviving `F(q)` is **fibre-level complex-analytic / cyclotomic**,
**never a real-q formula in q₀** (class **C1 REFUTED**: `dc₃/dq ≈ 4.6×10⁶`
rigidity ⇒ any real-q construction matches the proton anchor only).
**Anchor-stability (proton + muon cross-anchor swing < 1%) is THE
canonicity gate** (registry §8).

**Prediction (formalize-first, stated before running):**

- A **naive real-q analytic Taylor expansion** of (bar-even) `Δtr_M` in
  `u_L` at `q₀` is a real-q construction ⇒ **predicted C1-refuted**
  (proton-only match, cross-anchor swing ≫ 1%). Running it is the
  **control**, not the closure attempt.
- The **non-refuted path** is the **formal/cyclotomic** change of
  variable applied sector-by-sector to the **anchor-independent exact
  rationals** (the ζ₄ residue `1/2`, the Laurent-tower coefficients).
  A `cₖ` read off from anchor-independent rationals is anchor-stable
  **by construction** — the only honest route to passing the gate.

**Invariants any surviving `cₖ` must satisfy** (gate; a candidate that
fails symbolically is killed on paper, no anchor sweep):

1. **c₂ = −1 exactly** (the one PROVED rung — fixes the overall scale).
2. **Anchor-stability** — proton+muon swing < 1% (else `empirical`, dead).
3. **bar-evenness** (`q ↦ q⁻¹`) — the c₂ rung is bar-even (Kashiwara `f̃₁²`).
4. **q=1 shadow** — `c₃ → J_Hopf(1) = −2` without fitting.
5. **ζ₄ modular residue 1/2** carried through the change of variable.

---

## 2. Discipline (STRICT)

- **Exact symbolic** throughout; `u_L` change of variable done formally,
  not by float evaluation at a single anchor.
- **Tiered reporting** (proved / near-match / fitted) — never binary
  wired/dropped (canonical framing
  `2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`).
- **No fitted form, no production wiring, no registry tier change** from
  this probe unless a result passes ALL §1 invariants at compute
  precision at BOTH anchors (which would be a genuine closure — escalate
  to owner, do not self-wire).
- **Outcome → durable record:**
  - genuine closure ⇒ registry rung tier upgrade + owner escalation;
  - near-match / refutation ⇒ **new row C13** in the refuted-class map
    + formalize-the-refutation (§3.4) so the dead construction cannot be
    silently re-proposed;
  - underdetermined ⇒ characterize precisely what `Δtr_M` alone does /
    does not fix, sharpen the open `f`.
- **Coordinate:** #2106 (stalled) holds the Stage-B operator machinery;
  this probe is the orthogonal mode→ladder bridge and touches the
  `habiro_q_difference_mode_solve` lineage, not Stage-B files. Intent
  posted on #2106.

---

## 3. Deliverable

`computations/habiro/habiro_mode_to_ladder_bridge.py` + witness:
executes the sector-by-sector formal `u → u_L` bridge, extracts
`c₂, c₃, c₄` both ways (analytic-at-q₀ **control** vs formal-sector
**attempt**), checks the §1 invariants, reports tiered. Verdict appended
to the ledger + (if not a closure) a C13 row in the refuted-class map.

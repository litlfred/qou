# The keystone wall, mapped from four directions — session consolidation

**Session:** 2026-08-11. **Beans:** `qou-exam`, `rtep`, `qou-sib1`, `qou-dt14`.
**Purpose:** one map so the next session does not re-walk the closed region.

This session produced two new structural negatives, salvaged four formalization
deliverables, and executed one framework-level excision. None of it opened the
keystone. That is the finding, and this document records *why* each escape is
closed, so the effort is spent elsewhere.

## 1. What the framework no longer claims — absolute mass (owner ruling)

**Absolute nucleon/atomic mass in MeV is EXCISED as a prediction**
([`2026-08-11-excise-absolute-mass-notion.md`](2026-08-11-excise-absolute-mass-notion.md),
bean `qou-exam`; PRs #4977 / #4981 / #4987). Absolute mass is
`m_e · (dimensionless ratio)` and `m_e` (CAL-1) sets the MeV scale *by fiat*, so
the MeV figure double-counts the calibration. Retained and untouched: the
dimensionless ratios (`m_μ/m_e`, `m_K/m_π`), binding `B(K)`, decay Q-values
(`Q_β`), splittings (`Δ_pn`). Nothing proved was deleted; the MeV numbers remain
derivable as renderings.

**Consequence for where effort belongs:** post-excision the framework's live
predictive content is the **relations**, not absolute masses. The L2 scorecard
was reframed accordingly.

## 2. The wall itself — four independent closures

| direction | result | verdict |
|---|---|---|
| substrate `q₀` derivation | owner ruling 2026-08-02 (`qou-eic1`) | **FOREVER GATED** |
| `Stokes = DT` from the 13 QOU drivers | #4599: the Euler characteristic gives `−2` (a norm), never the count `3` | **not derivable** |
| the missing input itself | #4601: `Δ_λ` magnitude ≡ `A_ω` is one categorical Behrend-weighted DT moduli count, **irreducibly external** to the drivers | **external** |
| would closing it help? | #4601 derive-then-check: the derived `Δ_λ` fragment leaves the deuteron at `B(D) = 0.380 MeV` (−82.9 %) | **would not close binding** |

## 3. This session's two negatives — both *price* an escape rather than open one

### 3a. The roots-of-unity gate cannot reach `q₀` (bean `qou-sib1`, PR #4993)

Sibling #4973 excluded the **rational** BW row (gate at all roots of unity ⇒
`f·c(λ) = 0` ⇒ `f = 0`, tautological framing). The natural escape was the
**non-rational** class, via the transcendental Faddeev / Andersen–Kashaev state
integral — which converges at `q₀` (`τ = b² = −0.0166i`, in-domain) precisely
where the Habiro route provably diverges.

**It does not work, and the reason is a dichotomy** (both horns proved,
`KeystoneRootsToQ0Bridge.lean`):

* **analytic bridge** (`q0_determined_of_analytic_bridge`) — if the candidate and
  the Hecke row are analytic on one preconnected open set containing an
  accumulation point of the gate *and* `q₀`, the identity theorem pins them.
  Roots of unity are dense in `|q| = 1`, so *any* candidate analytic near an arc
  of the circle together with real `q₀ ≈ 1.10998` lands here — back to #4973's
  `f = 0`.
* **no bridge** (`gate_does_not_determine_q0`) — if `q₀` is not in the gate set,
  gate-agreement is consistent with *any* value at `q₀`.

**By-product worth carrying forward:** #4973's *rationality* hypothesis is not
the real restriction — **analyticity across the circle** is, and it is much
weaker, so that exclusion reaches further than stated.

**Price of the state-integral route:** convergence at `q₀` is **not** an
identification. Such a construction must supply an **independent** identification
at `q₀`; it cannot inherit one from the gate. This is the formal version of the
route-selection caveat *"convergence ≠ identification of `W_λ`"*.

### 3b. The DT count's Behrend weighting must be non-constant (bean `qou-dt14`, PR #4998)

Not *what* the missing count is, but **what any supplier must satisfy**
(`DTBehrendParityObstruction.lean`, Mathlib-free). A DT count is a
**Behrend-weighted** Euler characteristic `Σ_i n_i · χ_eu,i`; the unweighted
total is the ordinary `χ_eu`. The QOU machinery produces `χ_eu = −2`; the target
count is `3`. Proved:

* `chiEu_even_blocks_three` — for **every even** total `E` and any constant
  Behrend value `c`, `c · E ≠ 3`;
* `at_least_two_strata` — any supplier has ≥ 2 Behrend strata;
* `odd_count_needs_odd_stratum` — some stratum carries **both** an odd Behrend
  value and an odd Euler characteristic.

**The prune (scope-(b), invariant named = parity):** a **smooth** moduli space
has the constant Behrend function `(−1)^dim`, so no smooth moduli with even
`χ_eu` can ever supply `3`. This excludes the whole *"smooth moduli + (signed)
Euler characteristic"* family — the shape **every** QOU-internal route has taken —
and explains *structurally* why they all land on `−2`: such a count has **no
mechanism to be odd**.

**Robustness.** The corpus was ambiguous about which integer is "the Euler
characteristic" (the G3 directive hinted `−6`; `−6 = (−2)·3` is the GGM sandwich
`(0,1)` entry, i.e. prefactor × count, *not* an Euler characteristic). The
general theorem blocks **every even** total, so the obstruction is independent of
that resolution. Both readings are excluded. Disambiguation table now in the file
and in the notation register.

## 4. Formalization banked (not closures)

`bwse` remains open; these are reusable infrastructure, salvaged and re-verified
against current `main` (PR #4969): `KeystoneHeckeMTC` (the Hecke side as a
concrete MTC — the *target* of the BW=Hecke identification), `KeystoneRibbonCategory`
+ `KeystoneBalancedRibbon` (the ribbon/twist layer Mathlib lacks),
`KeystoneFramedTangleScaffold` (honest RT skeleton; Turaev relations and Kirby
moves remain open), and the `bwhk` S/T modular-data corroboration (scope-(a)
**evidence** for BW=Hecke, not a proof). The `qDimObj(Xᘁ) = qDimObj X` goal hit
the double-dual/pivotal wall Mathlib lacks and was **beaned (`rtqd`), not
sorry'd or axiomatised**.

## 5. Notation fixed (so the collision cannot recur)

The register carried **no** Euler-characteristic symbol while `χ` was already
claimed by the characters (`χ_λ`, `χ_ζ`) and the Lyapunov exponent `χ_q`. Now
registered: **`χ_eu`**, never a bare `χ`; total `χ_eu(M)` vs stratum `χ_eu,i`.
Note `\Chi` (uppercase) is **not** a valid KaTeX/LaTeX macro — it fails the
render gate; use `\chi_{\mathrm{eu}}`.

## 6. What remains open

* `bwse` — the two irreducible inputs stand: RT/Kirby-invariance (cited pure
  math, not Mathlib-formalizable without a 3-manifold library) and BW=Hecke
  (physics identification). Roadmap: `rtep` + children (`rtrb`/`rttg`/`rtkb`/`hkmt`/`bwhk`).
* `qou-cvst` (deferred) — does the `4₁` character variety actually carry the
  odd·odd Behrend stratum the parity obstruction demands? Would upgrade a
  necessary condition to an identification.
* `rtqd` — `qDimObj` conjugation symmetry, blocked on a pivotal structure Mathlib
  does not provide.

**Where effort is better spent (§1):** the relations — the μ–p tension
(`m_μ/m_e`, ~210 ppb), `Q_β`, `Δ_pn` — which is where the framework's live
predictive precision now sits.

## Honest scope

Nothing here closes `bwse`, `A_ω`, or `Δ_λ`. Both new results are **prunes**: they
exclude classes of attack and name the invariant that does the excluding (identity
theorem; parity). No fit; nothing wired; L2 unchanged. Every Lean file cited is
`lean`-direct exit 0 and sorry-free.

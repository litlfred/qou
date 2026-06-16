# Coordination ledger — q ↔ CAL anchor drift + local-q evolution

**Goal slug:** `q-local-evolution`
**Lead PR:** [#2346](https://github.com/litlfred/qou/pull/2346) — branch `claude/gracious-lovelace-uzuovl`
**Opened:** 2026-06-16
**Owner driver:** "figure out CAL 1/2/3 and relation to q; how does q evolve locally at p" + 4 proposed routes.

## Scope map

| PR / branch | Relationship | Classification | Action |
|---|---|---|---|
| **#2346** (this) | lead | — | audit + routes 3/4 done; 1/2 sketched |
| [#1556](https://github.com/litlfred/qou/pull/1556) `m-mu-chain-audit` | **overlap (high)** — m_μ anchor-vs-prediction status | no file overlap; finding-dependency | intent posted; cited their ratio-anchored convention split for the m_μ L2 reconciliation |
| [#2345](https://github.com/litlfred/qou/pull/2345) `jolly-newton` (Q_β kernel / Koide) | overlap (moderate) — Q_β role, lepton masses | no file overlap; orthogonal (c_k ladder vs base-Q_β CAL) | intent posted; flagged Q_β-becomes-derived + "q is the ratio" reparam vs their Koide-CAL-4 refutation |
| [#2081](https://github.com/litlfred/qou/pull/2081) (metallic q↔ρ) | tangential — q↔ρ ≠ q↔CAL | not in scope | skipped (no comment — avoid noise) |

## Key findings

- **Anchor drift (3-way):** live compute is **proton-anchored** (`m_p/m_e`,
  re-pin 2026-05-28 `01c18125`); paper blocks still say muon; CLAUDE.md
  table says neutron. `m_μ/m_e` is now a 9.5σ prediction.
- **3rd-CAL fork:** paper blocks say `Q_β`; cheat-sheet diagram says
  `m_π` (`Q_β` derived). **Owner resolution:** 3rd CAL = `m_π`, `Q_β`
  derived, `q₀` proton-anchored.
- **"q is the ratio"** = reparameterization (any one ratio coordinatizes
  `q₀`), not an identity. Ratio-anchored convention is exactly this.

## Route status (see audit Part B)

| Route | Verdict | State |
|---|---|---|
| 4 fix-drift | ✅ | **done** — author-notes on both calibration blocks |
| 3 un-stub Lean | ✅ | **done + build-verified** (lean-direct exit 0, v4.24.0) |
| 2 germ-dynamics | ✅ ½-exists | **sketched** (scope doc); 2a/2b = paper-content follow-ups |
| 1 fixed-point | ⚠ naive refuted | **sketched** (scope doc); q₀-selection re-opened research |

## Follow-ups (tracked, not done here)

1. **Prose migration** of the calibration basis (muon→proton, Q_β→m_π)
   in `prop:three-calibration-discipline` + ripples
   (`prop:three-calibration-inputs`, Wedderburn-count prop, SDP
   `m_π`-independence). Owner-confirm before rewriting scholarly prose.
2. **Route 2a/2b** paper blocks (germ-commutator = q-curvature prop;
   q-harmonic flow conjecture) — gated on the content-validation tooling
   (`folio-assistant/schemas` absent on this checkout) + Lean.
3. **Route 1a** probe (`‖(q-1)𝓕_q^intr‖(q)` critical point) — owner-gated
   (re-opened substrate-q₀ derivation), needs `pyhecke_native`.
4. **Stale-doc cleanup:** cheat-sheet §1 internal CAL-3 inconsistency
   (diagram says `m_π`, CLAUDE.md table neutron); `qou-substrate/README.md:29`
   prints the muon `q₀`.

## Log

- 2026-06-16 02:3x — PR #2346 opened; audit + route 4 author-notes +
  route 3 verified Lean repair landed; routes 1/2 scope doc; intent on
  #1556, #2345. Gemini at daily quota on #2346 (no review until reset).

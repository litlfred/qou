---
# bws0
title: 'Keystone: full formal closure of bwS0_eq_hecke (the loc_matches gate)'
status: in-progress
type: milestone
priority: high
created_at: 2026-07-27T00:30:00Z
updated_at: 2026-07-27T00:30:00Z
---

Full formal closure of `bwS0_eq_hecke` (`KeystoneVerlindeSMatrixBridge.BWVacuumRowIsHecke`) —
the single open conjecture that `loc_matches` (the W_λ keystone / Subgoal-2, m_p·m_μ) reduces to:
the Chern–Simons/WRT gauge vacuum row `bwS0(λ)` equals the Hecke modular datum `d_q(λ)/√(Σ d_q²)`
at real q>1.

**Strategy (PR #4365):** reduce the conjecture to named/cited inputs via interpolation rigidity,
then discharge each input as far as honest. `bwS0_eq_hecke` is NOT provable outright (it rests on
the TQFT identification WRT = BW-localization, a physics input — §Axiomatization-is-NOT-a-Proof);
the goal is to isolate the irreducible content and Lean-prove everything else.

Decomposition (see child task beans bwsa–bwse):
- rigidity engine + distinct root points — DONE (bwsa)
- root realization + value-map continuation — DONE (bwsb, #4365)
- WRT=modular-data agreement across enough roots — OPEN (bwsc)
- bwS0 bounded-degree (Habiro rigidity) — OPEN (bwsd)
- WRT=BW-localization identification — irreducible cited input (bwse)

Closure = bwsc + bwsd landed; then bwse is the one remaining *cited* (not derived) hinge.

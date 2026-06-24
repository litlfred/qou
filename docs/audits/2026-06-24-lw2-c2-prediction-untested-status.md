# lw(2) c=2 prediction — derivation-tight but UNTESTED (no independent c=2 observable) (2026-06-24)

**Branch:** `claude/lw2-c2-prediction-keystone-coord-2026-06-24` · **PR #2674**
**Follows:** merged #2612 (lever-1 selection-rule unification).
**Discipline:** corpus-grep + no-fit. The disposition is an honest negative — **no
fabricated test.**

## The question

Can the selection rule's c=2 value
`lw(2) = (1/3)·Σ_{λ⊢3} dim_q V_λ = (q+1)²/(3q) ≈ 1.337` (at q₀) be **tested**? The
rule `lw(c)=(1/(c+1))·Σ_{λ⊢c+1} dim_q` is confirmed at c=1 (muon, `lw=1`) and c=3
(proton, Family-A = `(3q²+4+3q⁻²)/4`, bit-for-bit = production
`linking_weight_family_a`). `lw(2)` is the rule's **first falsifiable prediction
beyond the two mass anchors**.

## Verdict — derivation-tight, but no independent c=2 observable exists

| property | status |
|---|---|
| derivation-tight (Lean-proved, canonical q-hook `dim_q`) | ✅ (`selection-rule-c2-prediction.lean`, `field_simp; ring`) |
| consistent with c=1 / c=3 anchors | ✅ |
| independent c=2 (2-component-link) linking-weight to test against | ❌ **none in the corpus** |

**Corpus-grep result (no independent c=2 determination):**

- **c=2 = 2-component link** (Hopf, T₂,₂) — per `selection-rule-anchors-c1-c3.md`
  (c=1 muon/knot, c=3 proton/Borromean) and `selection-rule-c2-prediction.md`.
- The **Hopf diquark** (`hopf-diquark.md`) is the natural c=2 object — two quarks
  Hopf-linked — but carries **no mass / VolDensity / linking-weight prediction**.
  The Hopf link also appears in `hopf-link-non-magic.md` and
  `hopf-link-symmetric-decomposition.md` (van-der-Waals correlation), again with
  **no linking-weight assignment**.
- The **deuteron** is NOT a c=2 link — it is the **6₂ knot (6-strand)**
  (`vol_density_deuteron_perknot_probe.py`); its mass uses `canonical_tr_m("D",1,1)`
  (H₆ trace), no linking weight. So lw(2) ≠ a deuteron observable.
- Production `linking_weight` (`_li_2_q_util.py`) defines only the c=3
  `linking_weight_family_a`; **no c=2 function**.

## The concrete falsifiable prediction (for future work)

`lw(2) = (q+1)²/(3q) ≈ 1.337` is the framework's **predicted linking weight for a
c=2 / 2-component-link object**. The decisive test: independently compute a Hopf
diquark's (or gluon EM-linking) VolDensity / linking weight — it must equal
`(q+1)²/(3q)`. Candidate paths:

1. **Hopf-diquark VolDensity** — assign `hopf-diquark.md` a Vol + per-block trace,
   extract its linking weight, compare to 1.337.
2. **Gluon EM-linking** — if a 2-component EM-linking weight is defined, test it.

Until such a c=2 observable is independently computed, `lw(2)` stands as a
**derivation-tight, untested prediction** — the rule's cleanest open falsification
target. No comparison is fabricated here (per the workplan directive + CAL-4).

## Cross-references

- [`content/quantum-observable-universe/climax-volume-mass/selection-rule-c2-prediction.md`](../../content/quantum-observable-universe/climax-volume-mass/selection-rule-c2-prediction.md) — the c=2 closed form (Lean-proved).
- [`computations/binding_selection_rule_tau_closure.py`](../../computations/binding_selection_rule_tau_closure.py) — the lw(c) unification (#2612).
- [`docs/audits/2026-06-23-delta-lambda-three-lever-status.md`](2026-06-23-delta-lambda-three-lever-status.md) — lever-1 status.

# Coordination ledger — level-selection rule (averaging-resonance, $c_k$ sectors)

**Goal**: close the level-selection rule for precision-ladder $c_k$ sectors.
Specifically: classify each rung $k$ as pure-$\sigma$ or averaging-resonant
under the silver-ratio Pell-Lucas test, and surface a candidate categorical
criterion that singles out the resonant rung(s).

**Lead PR**: #816 (`claude/close-level-selection-rule-bvMvw`).

## Scope map (2026-05-19)

| PR | Branch | Relation | Status |
|----|--------|----------|--------|
| **#816** (this) | `claude/close-level-selection-rule-bvMvw` | lead | open, awaiting CI |
| #814 | `claude/qbeta-fsc-categorical-ratio-2026-05-19` | **upstream / inconsistent finding** (see §1) | open |
| #808 | `claude/co-casimir-extension-2026-05-19` | unrelated (5-atom co-casimir; no $c_k$ touch) | open |
| #801 | `claude/log-delta-categorical-derivation` | unrelated (Δ_I^K interface-knot binding) | open |
| #806 | `claude/lean-substantive-pass-2026-05-19` | possible Lean-build interaction only | open |
| #807 | `claude/compute-audit-P33-P34-2026-05-19` | possible compute-audit policy interaction | open |
| #802 | `claude/canonical-discipline-l1-l3-l4-2026-05-19` | unrelated | open |

## §1 — Inconsistent finding flagged on #814

**Disagreement**: PR #814 classifies $c_8 = 49/16$ and $c_{10} = 343/128$
as averaging-resonant (commit `7179a7e3` titled "averaging-resonance
confirmed at k=8, 10"). PR #816 reclassifies both as pure-$\sigma$ under
the same Pell-Lucas test, on the basis that $49 = a_3^2$ and $343 = a_3^3$
are Pell-Lucas powers (clean numerators).

**Posted** as a coordination comment on #814
(https://github.com/litlfred/qou/pull/814#issuecomment-4485520795) —
two-option ask (revise #814 framing, or treat #816 as supersession).
No silent rewrite, no cherry-pick.

## §2 — Reviewer triage on #816

| Reviewer | Comment | Verdict | Commit |
|----------|---------|---------|--------|
| gemini-code-assist | `is_pell_lucas_clean` misses $pl^j \cdot 2^m$ | **accept** | `1b3e2c940` |
| gemini-code-assist | `>` should be `>=` in `classify_sector_predictive` | **accept** | `1b3e2c940` |
| gemini-code-assist | centralise utility (e.g. into `murnaghan_nakayama.py`) | **deferred** | follow-up — out of scope for #816 |

## §3 — Open follow-ups

1. **Categorical derivation of half-fill hypothesis**:
   $k_{\text{outlier}} = \lfloor n_{\text{total}}/2 \rfloor$ is empirically
   consistent on the proton typed-$\mathbf{B}_3$ ladder but not yet
   derived from the Markov-trace cyclicity structure. Open R&D.

2. **Probe extension** beyond $k = 10$ and at other $n_{\text{total}}$ —
   needed to test/falsify the half-fill rule.

3. **Per-Wedderburn-block weighting** for refining the predictive rule.

4. **Pell-Lucas utility centralisation** (Gemini's follow-up): move
   `is_pell_lucas_clean` and related primitives into a shared module
   (candidate: `folio-assistant/computations/silver_ratio_utils.py`).

## §4 — Watch state

- `origin/main` checked at session start; no new commits touching
  `braids-and-knots/averaging-*`, `silver-ratio-*`, or `ck_sector_*`.
- Subscribed to PR #816 activity.

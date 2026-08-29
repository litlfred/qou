---
# qou-jqla
title: 'Witness prose contradicts witness data: su4-connected-1111-magnitude and b4-framework-connected-cumulant-deficit carry hardcoded convention-C-era verdict strings'
status: completed
type: task
priority: normal
created_at: 2026-08-29T07:05:04Z
updated_at: 2026-08-29T11:12:20Z
---

Measured 2026-08-29 on branch claude/he4-magnitude-fork-2026-08-29 (PR #5966).

Two committed witnesses on main carry hardcoded verdict prose from the
convention-C era while their data blocks hold current convention-D values:

1. computations/probes/su4-connected-1111-magnitude.witness.json
   data: delivered x1.398, |b4c|=1.17395, ungated A=6 cluster 10.17
   verdict_note: 'x1.54 delivered vs x2.09 needed, 74%' and 'overshoots to 22.2'
   The producer also PRINTS a stale caveat line: 'the direct |b4c|=1.96 vs
   2.093 (6%)' — the live D-frame figure is 1.174 vs 2.097, i.e. 44% off,
   not 6%. That printed 6% is the near-match trap the same line warns about.

2. computations/probes/b4-framework-connected-cumulant-deficit.witness.json
   data: b4 = -0.3035 MeV = -3.28% of the 9.243 target; b3 = -1.3878
   verdict: 'b4 = 0.583 MeV = 6.3% of the 9.243 target ... -2.52 vs +1.43 ...
   must supply ~94% of the 4-body'
   Its assertion framework_b4_far_below_target (expected 0.063 +/- 0.02,
   computed -0.03284) is LIVE FAILING on main, and allPassed is false.

Both verdict strings are hardcoded in the producer, so re-running regenerates
the numbers and preserves the stale prose. Fix at the producer: derive the
verdict text from the computed values.

Not fixed on PR #5966 to avoid touching producers a sibling may hold.

## RESOLVED — PR #6014, branch `claude/jqla-witness-prose-2026-08-29`

Both producers now derive **every** figure in their verdict/description prose from
the computed values via f-strings. Neither can go stale again without the numbers
going stale too.

### b4-framework-connected-cumulant-deficit (was LIVE FAILING on main)

The assertion pinned `expected: "0.063"` — a **past measurement**, not a
prediction — against a computed `-0.03284`. It could only ever be "fixed" by
editing the number, which is the laundering the precision discipline forbids.
Replaced with the **proposition** the probe exists to establish (`frac_b4 < 0.5`,
threshold stated explicitly), value carried in the data block.

The bean recorded the prose as stale. Measured, it is stale in a way that
**changes the physics**: b4 has changed **SIGN**.

| | b₂ | b₃ | b₄ | fraction |
|---|---:|---:|---:|---:|
| prose | 3.056 | −2.525 | **+0.583** | 6.3% |
| live | 1.927 | −1.388 | **−0.304** | **−3.3%** |

So the printed "[1^4] Slater term must supply ~94%" is wrong twice: it is
**~103%**, and the term must **reverse** b4 as well as b3. Added
`framework_b4_wrong_sign` — a strengthening, now asserted rather than observed.

### su4-connected-1111-magnitude (allPassed was TRUE; prose wrong anyway)

| | said | live |
|---|---:|---:|
| delivered | ×1.54 | **×1.398** |
| delivered/needed | 74% | **67%** |
| ungated A=6 overshoot | 22.2 | **10.17** |

And the producer **printed** "the direct |b4c|=1.96 vs 2.093 (6%)" on the very
line warning the figure is units-mismatched and not a derivation. Live D-frame:
**1.174 vs 2.097 = 44% off**. A stale 6% inside a near-match caveat is exactly
the trap that caveat names. The 44% direct reading is now recorded in the witness
beside the flattering normalised one.

### Rode along: the same defect class one layer up

The read-first `docs/canonical-derivation-cheat-sheet.md` item 4 stated in bold
that the q-Reeb phase "closes the A=3 mirror pair to **2%, no fit**". That 2%
came from `C_knot = 5.852 = B_AME/(m_e·|Σ|)` — a straight AME anchor inversion,
i.e. a **fit**, retracted in PR #1417. The retraction existed three lines below in
a trailing "Net:" a reader need not connect. The same figure was listed as a
**live lead** in `docs/audits/2026-06-23-...:359`, written *after* the retraction
— which is how a fitted number stayed on an open-work list for two months. Both
corrected; the **structural** claim (binding carried per-rep, not by the collapsed
scalar) is kept.

### Two defects of my own, caught before commit

- The **witness shape guard** flagged that my added sentence raised the file's
  `\\uXXXX` escape count 17 → 19. Rewrote it ASCII-only; `collapsed: 0`.
- I had the overshoot figure as `b_conn_abs + 1` = 11.17 instead of
  `b_conn_abs` = 10.17 — caught by checking against this bean's own recorded
  value before committing.

### Verification

`precision-gates.sh --changed`: NEW dirty **0**, REGRESSED **0** on both float64
ratchets; neither witness named in any red gate (grep count 0). The 4 remaining
reds are pre-existing on main. Audit witnesses the gate regenerates in passing
were reverted, not swept in.

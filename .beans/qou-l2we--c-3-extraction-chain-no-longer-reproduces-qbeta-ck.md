---
# qou-l2we
title: 'c_3 extraction chain no longer reproduces qbeta-ck-cache: off by 972 against a 1e-8 tolerance'
status: completed
type: bug
priority: high
created_at: 2026-08-30T16:12:03Z
updated_at: 2026-08-30T18:10:02Z
---

Surfaced 2026-08-30 by fixing `qou-ya1e`. This producer had been unrunnable, so
the regression was invisible rather than absent.

## The failure

`computations/probes/qbeta_ck_basis_constrained_pslq.py`, once it could run
again:

```
name       extraction_chain_reproduces_cache_c3
computed   972.3622884795565
expected   0.0
tolerance  1e-08
passed     False
source     same chain + same Q_codata + same q0 as qbeta-ck-cache.witness.json
```

`allPassed` True → **False**. Its previous witness was computed **2026-07-11**;
the producer has been dying at the save ever since (the `qou-ya1e` stamp import),
so nothing re-ran it and nothing noticed.

## Not caused by the repair

The only change to that file is a 4-line `sys.path` / `_path_bridge` preamble —
verified in `a5851c9e5`. It cannot move a number. The chain drifted from its
cache at some point in the last ~7 weeks and this is the first run since.

972 against a 1e-8 tolerance is not precision drift. Something structural moved:
a convention change, a pin change, or the cache itself.

## Todo

- [ ] Diff `qbeta-ck-cache.witness.json`'s history against the extraction
      chain's inputs over 2026-07-11 → now and find what moved.
- [ ] Check the convention-D propagation (2026-08-09/10) first — it is the
      largest structural change in that window and it is known to have moved
      other qbeta results by tens of percent.
- [ ] Decide which side is right: the cache or the chain. Do NOT retune the
      tolerance to make it pass.

## Related

`qou-s2no` (same cluster: `qbeta-decay-sdp-extended-ck` publishes all-null c_k
because no rung resolves). Whether these share a root cause is unestablished —
do not assume it.

## 2026-08-30 — RESOLVED: convention D in the chain; fixed by removing the frame

### Root cause

`ladder_chain` carried `z = q**3/(q**2 + 1)` — **convention D** — while every
value it was compared against was convention C. Everything else in the chain was
algebraically identical to `qbeta_ck_cache.py`, including `b`: the probe's
`sqrt(d1*d2 + 1)` and the cache's `sqrt((h^2+3)/(h^2+4))` both reduce to
`sqrt(q^4+q^2+1)/(q^2+1)` and agree to **0.0 exactly**. `z` was the sole
difference.

Measured at the pin the probe used (muon vintage A):

    conv C   c_3 = -2.02018812814143945582     <- reproduces the committed witness
    conv D   c_3 = -974.382476607697851631     <- what the file actually ran
    |delta|  = 972.3622884795564...            <- the reported 972.3622884795565

Same defect `qbeta_ck_cache.py` carried until `a340f7c87` ("the producer was
silently convention D with a C witness"), one file over, unfixed here.

### `qou-u6cz`'s premise was wrong — recorded there

u6cz concluded "**Not a simple z-convention swap** … `alpha`/`Q_N1`/`Q_A`
structure moved, not just `z`" after testing five candidate `z`. All five were
*rational* functions of q; it never tested convention C itself,
`z = sqrt(q)/(1+q)` — the one form with a square root — which reproduces the
committed value to ~1e-30 (the committed assertion's own `1.583530407934892e-30`).
It **was** a simple z-swap.

### Resolution: EXCISE, not swap (owner ruling, this bean)

The obvious fix — put the probe on convention C — is refused. **C is excised.**
D has no derived ladder (`qou-cds1`: `decayLadder_zC_threeRow_ne_zero`,
`eigenphase_bar_defect_of_fullBar`, both sorry-free). With no admissible frame
there is no chain to reproduce, so the assertion
`extraction_chain_reproduces_cache_c3` cannot survive and was **retired**, not
retuned.

What it was really protecting is that the STAGE-1 VERDICT does not depend on the
frame. That is now asserted directly and frame-free:

- `ladder_chain` → `substrate_scalars`, which computes `h`, `hbar_q`, `b`, `u`
  and contains **no `z` at all**.
- `c_3` is CONSUMED from the on-record readout, never recomputed.
- `c_4 = 0` exactly, by an algebraic argument needing no frame.
- amplifier `(Q/Q_Nk)/u^k` reported at `Q/Q_Nk -> 1`; the frame-dependent factor
  is `1 + O(6e-4)` worst-case across BOTH frames, worth `<3e-4` of a digit.
- new assertion `entropy_bound_is_convention_immune`: **0.000262 digits** shift
  against a **6.99-digit** deficit. Mechanises row P3 of
  `docs/audits/2026-08-15-c3-refutation-chain-convention-validity-audit.md`
  ("Q_N2 moves 6e-4 relative under D — bound unchanged; VALID-immune").

Stage-1 verdict **unchanged: ENTROPY-BLOCKED**, `D_eff(c_3) = 2.21`, matching the
corpus's long-documented "≤ ~2.2 reliable digits per anchor". The witness is
green because a false assertion was removed and a true one proved — not because
a tolerance moved.

### Also fixed here

- `C3_EMP_CACHE` → `C3_MUON_PIN_A`, `Q0_CANONICAL` → `Q0_MUON_PIN_A`. The old
  names asserted "this is the cache" / "this is canonical"; the cache moved to
  the proton pin on 2026-08-08 (`633ac8a7d`) and pin A was retired 2026-08-22.
  Mislabelled constants are what let this sit unnoticed for seven weeks.
- `C3_EMP_PROTON` agrees with the CURRENT cache c_3 to every digit the cache
  records — an independent cross-check, now noted at the definition.
- **float64 17 → 18 regressed and is fixed at the producer.** `bc8131bd5`
  drained 1232 declared tolerances out of 499 witnesses but left the PRODUCERS
  emitting floats, so re-running one silently undid the drain. `tolerance` is
  now emitted as a string. Back to 17; baseline NOT widened.

### Gates — NOT green, for pre-existing reasons

Both ratchets are red on this branch independently of this change:

    q0_anchor_ratchet --strict   FAIL: 3 newly unstamped
        c-knot-tau-transfer-artifact      (73567a64e, sibling takeover)
        toffoli-published-vs-construction (2f3e5b2f8)
        toffoli-trio-rederivation         (04f14b7c2)
    witness_raw_float64_audit --strict   FAIL: 1 regressed (after this fix)
        iterative-lp-dual-h6-deuteron 96 -> 99  (ac6310b31, my qou-mjcd fix)

None is caused by this change; this file's own stamp is unchanged (`ambiguous`
before and after) and its float64 count improved. Beaned separately — do not
read this bean's closure as those being clean.

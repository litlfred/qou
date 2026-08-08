# The Q_β L2 row straddles the q₀ layers — guarded (2026-08-08)

**Tier:** compute defect + fix · **Wired:** guard only; no prediction changed.
**No fit.** Producer: [`per_observable_100x_status.py`](../../computations/per_observable_100x_status.py) ·
witness: `computations/per-observable-100x-status.witness.json`.

Follows [`2026-08-08-qbeta-l2-assessment-post-week-landings.md`](2026-08-08-qbeta-l2-assessment-post-week-landings.md)
§3, which identified this straddle but did not guard it, and §2, whose
`load_witness` fix is what made it live.

---

## 1. The defect

`computations/qbeta/qbeta-ck-cache.witness.json` is stamped:

```
q0Anchor : "muon"
q0Value  : 1.10997859555733471989976322048322502665620840878015368660798114614493
```

`per_observable_100x_status.py` evaluates at the **proton** pin
(`q_parameter.Q_50_DIGIT_STR = 1.1099785827513808075916…`) — the default that
AGENTS.md §q₀-anchor made mandatory for production compute on 2026-08-07.

The field the producer consumes from that cache is
`Q_pred_after_this_rung_MeV` — a **prediction**, which depends on q₀. So one
dashboard row combines a muon-built number with a proton-pinned evaluation.
That is precisely the hazard the directive names: *"Never straddle the two
layers inside one quantity."*

**The trap that hides it.** Each cache rung carries a `q0_dependent` flag, and
the only DERIVED rung (k = 2, `c_2 = −1`) is flagged `q0_dependent: False`. That
flag describes the **coefficient** `c_k`, not the cached prediction. Reading it
as covering the prediction is the error, and it is an easy one — the flag sits
in the same row as the value it does not cover.

**And it is newly live.** Before §2's fix, `load_witness` resolved names
flat-only, the cache lookup returned `{}`, and the row went down the legacy
fallback. Fixing the dead code connected the cache — and with it the straddle.
The fix was correct and necessary; this is its follow-on.

## 2. Size

Recomputed independently here (symbolic log-derivative of the base form
`Q_β = m_e·|q²−2q−1|·(q+1)/(2q³)`, no hard-coded constant), reproducing the
§3 figures exactly:

```
dlnQ_beta/dlnq  at proton pin =  -2.5967550825999519729
pin difference (proton-muon)  = -11.537118 ppb
=> induced Q_beta error       =  29.959069 ppb
   L2 target for Q_beta       =   7.797    ppb
   ratio                      =   3.84 x
```

Read this the way §3 did, because it cuts both ways:

- **2.4 % of today's 1248 ppb residual** — so it is not why Q_β misses, and
  re-pinning is not a lever that closes L2.
- **3.84× the entire L2 target** — so it alone disqualifies a pass.

## 3. Why it needed a guard rather than a fix-in-place

The correct end state is the whole quantity on the proton pin. Getting there
means regenerating `qbeta-ck-cache` at the experimental anchor — which is the
tracked migration under bean `tnjb`, and which AGENTS.md §q₀-anchor rule 4
explicitly says is **not** an idle-drain: *"Untouched muon witnesses: leave
them. Do not mass-regenerate."* So the witness is left alone.

What is not acceptable is leaving the mismatch **silent**, because the failure
is armed to fire on exactly the event the ladder exists to detect. Today the
residual is 1248 ppb and the anchor term is noise inside it. The day a higher
`c_k` is proved Taylor-exact and promoted to `tier='derived'`, the residual
collapses toward the target — and a ~30 ppb layer artefact becomes the dominant
error in the row that decides whether Q_β meets L2. That is the same shape as
the dead-code bug: silent, harmless now, decisive precisely when it matters.

## 4. The guard

`_anchor_layer_check()` compares the cache's `q0Value` stamp against the pin the
dashboard evaluates at, computes the induced Q_β error from the closed-form
log-derivative, and:

1. **reports** it in the row's source string, in a console banner, in a witness
   caveat, and as a structured `anchor_layer_qbeta` block;
2. **suppresses a 100× PASS** on the Q_β row while the anchor-induced error
   alone exceeds the L2 target.

Clause 2 can only ever turn a would-be PASS into a FAIL, and only when that pass
would have been an artefact of the layer mismatch rather than a result. It is a
one-directional guard by construction.

## 5. Verification — numerically a no-op today

Re-ran against the committed witness:

```
summary old : {'total': 7, 'beats_1x_count': 2, 'beats_100x_count': 2}
summary new : {'total': 7, 'beats_1x_count': 2, 'beats_100x_count': 2}
rows with changed err_ppb or 100x verdict : NONE
anchor_layer_qbeta.status                 : STRADDLE
anchor_error_over_target                  : 3.8423
```

The L2 count stays **2/7**. No prediction, no error, and no verdict changed —
the diff is the diagnostic itself. Q_β already misses by ~160×, so the
suppression clause is inert; it arms correctly for the promotion event.

## 6. Resolved same day — the cache is now proton-pinned

The scoped half of bean `tnjb` was run for this one chain: `qbeta_ck_cache.py`
regenerated at the proton pin. Two things came out of it.

**The numbers moved by exactly the predicted amount.**

```
Q_beta   1248.2 -> 1278.6 ppb   (+30.4 ppb; predicted anchor swing 29.96 ppb)
c_3      -2.0202 -> -2.0693     (2.4% cross-anchor swing, cal-anchored tier)
m_n      2.389 -> 2.414 ppb     (rides on Q_beta)
Delta_pn 755.6 -> 773.9 ppb
```

The L2 count is unchanged at **2/7**. And the corrected Q_β figure —
**1279 ppb, 164.0× miss** — is exactly what `docs/precision-goals.md`
§"Key distinctions" already quoted. The committed witness had been carrying the
straddled value while the prose carried the layer-consistent one; they now
agree. The per-observable table there is corrected to match.

**A second defect surfaced: the anchor stamp lied.** After regenerating at the
proton pin the witness *still* read `q0Anchor: "muon"`. Cause: `q0Anchor` is
written only by `stamp_staleness_metadata`, which a producer must call
explicitly (184 of ~780 do); `qbeta_ck_cache` does not. So `save()` fell to its
preserve-forward branch and copied the pre-re-pin stamp onto a freshly
proton-computed value. The Q_β prediction had moved 30.4 ppb under a label
saying it had not — the stamp AGENTS.md rule 4 relies on ("say which pin you
used") was not derived from the pin actually used.

Fixed in `qou_substrate/witness.py`:

1. `build()` now stamps the pin whenever it is **positively declared** for the
   producer, so the manifest is load-bearing at write time rather than only at
   audit time.
2. preserve-forward no longer carries a pin that a positive declaration
   contradicts; on contradiction it **drops** rather than corrects, since
   writing in a resolved pin would assert a stamp the producer never
   established and `Q0_ANCHOR_MISSING` is a tolerated state.
3. `q0_anchor_is_declared()` is the new gate. This distinction is load-bearing:
   `resolve_q0_anchor` returns `"proton"` for every stem **absent** from the
   manifest — ~470 producers — so gating on it directly would have stripped
   legitimate `muon` labels wholesale. The repo's own
   `tests/test_q0_anchor.py::test_save_carries_forward_a_recorded_pin` caught
   that on the first attempt.

`qbeta_ck_cache` and `per_observable_100x_status` are added to the manifest's
`physical_proton` list, so both now carry a stamp that reflects reality. Full
substrate suite: 33 passed.

## 7. Scope

**Not a precision claim.** No prediction improved or degraded. The residual is
now correctly stated as 1279 ppb rather than 1248 ppb; that 30 ppb is a
mislabelling being corrected, not physics moving. It remains, entirely, the c₃
truncation.

**Not a closure of bean `tnjb`.** Only the Q_β chain was migrated — one cache,
not the ~840-witness sweep, which still needs its scoped sign-off. The guard now
reports `status: "matched"` for this row and its suppression clause has stood
down on its own, exactly as designed.

**Consequence for any future "Q_β meets L2" claim.** Per the pin-discipline rule
(`docs/precision-goals.md` §"Pin discipline", bean `qou-qb8c`), such a claim must
state its anchor. This makes the dashboard enforce that rather than rely on the
reader: deriving c₃ is necessary but **not sufficient** — the anchor layer must
be settled too, or the row cannot pass on its own numbers.

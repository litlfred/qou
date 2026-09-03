# The q₀ drain backlog, item by item — what reproduced and what was already closed

**Date:** 2026-08-29 · **PR:** #5962 · **Branch:** `claude/q0-defect-drain-2026-08-29`

Companion to
[`2026-08-29-q0-muon-anchor-repin-drain.md`](2026-08-29-q0-muon-anchor-repin-drain.md),
which recorded two drain passes and left a backlog. This document verifies each
backlog item **against current `main`** before acting on it.

That verification step is the point. Four of the seven items were **already
closed** by the drains that landed in parallel, and an agent acting on the
backlog list without re-measuring would have re-done work, or worse, "fixed"
something that was no longer broken.

## Verdicts

| # | item | verdict |
|---|---|---|
| 1 | `low_isotope_sign_flip_diagnostic` `TypeError` | **already closed**; one float64 residual fixed here |
| 2 | `cross_check_trM_cw_seminormal_leg` TIMEOUT | **not a timeout, and its root cause landed on `main`** |
| 3 | 3 remaining `Q0_FLIP` | reproduced at 3; each dispositioned, none cleared by re-stamping |
| 4 | `lever1_...` manifest-vs-witness | **already consistent**; verified by re-run |
| 5 | `qou-wgaw` L1 disagreement | **settled — the dashboard is wrong, twice** |
| 6 | `hadron_knot_table` | not run to completion, deliberately; hot call named |
| 7 | `qou-mass` vendor mirror | **already in sync**, 6 module drifts gone |

---

## 1 — `low_isotope_sign_flip_diagnostic`: closed, with one residual

The `TypeError: unsupported operand type(s) for +: 'int' and 'str'` is gone. The
producer exits 0 and reports R² 0.2653 / 0.0018, matching the drain doc's
recorded 0.265294.

**The fix that landed is the right one, not the banned one.** The drain doc
warned that the naive `float()` repair would install exactly what AGENTS.md
bans. It did not happen: `_pearson_r` and `_linear_fit` coerce through `_mpf`
and carry `mpmath` end to end.

**One residual, fixed here.** Line 232 still read
`if float(r.get("err_pct", 0)) < 0`. That is not a display — it classifies a row
into the KLR-positivity violation list whose count is recorded in the witness.
Now `_mpf`. Verdict unchanged (3 under / 2 over, R² identical to every digit
printed), so this is a fixed producer, not a changed result.

**Side effect worth recording:** the ratchet reports
`low-isotope-sign-flip-diagnostic 24 → 0` raw float64 fields. The mpf work
drained the whole file.

## 2 — `cross_check_trM_cw_seminormal_leg`: the timeout was never the problem

The backlog asks whether this is genuinely long-compute or has a pathology. It
is **both, and neither is news** — bean `qou-2wtx` had already bisected it:

- **It does not time out.** It completes; helium-4 alone is ~99 % of the wall.
- **It was failing at O(1)** — `|Δ|/ref` 1.20, 0.955, **1.91** — because the
  peel reference it compares against was **convention-C-era stale** while the
  leg itself computes in convention D.

**`main` has since regenerated that reference** (`cfe73b8eb5`), and its values
match `qou-2wtx`'s predicted regeneration to every digit. Re-running the leg on
current `main` confirms the O(1) term is gone:

| atom | before (C-era peel) | now | wall |
|---|---|---|---|
| proton | — | 7.89e-08 | 0 s |
| neutron | — | 6.99e-08 | 0 s |
| deuteron | — | 1.52e-07 | 0 s |
| triton | **1.20e+00** | 1.98e-07 | 1 s |
| helium-3 | **9.55e-01** | 2.53e-07 | 1 s |
| helium-4 | **1.91e+00** | **2.99e-07** | **1499 s** |

Worst `|Δ|/ref` **1.91e+00 → 2.99e-07**, a **6.4e6× improvement**, from a fix
that landed elsewhere. What remains is `qou-2wtx`'s *defect 2*, the pin
straddle: the peel reference is stamped `proton` while this leg resolves
`ideal_muon`. ~1e-7 is the μ–p tension accumulated across the word — and it is
the same scale as the 2.9066e-07 the L1 cross-check reports for helium-4 in
item 5, from the other direction.

**It still FAILS its 1 ppQ assertion, and that is correct.** 1e-7 is eight
orders above 1e-15. `allPassed` moves True → False, which is the pass→fail
regression `qou-2wtx` recorded, now landed with its cause removed rather than
concealed. The honest state is a much smaller red, not a green.

### The budget, measured — and it is NOT the 996 s on record

**Total 1501 s (25.0 min); helium-4 alone is 1499 s, 99.9 % of it.** Bean
`qou-2wtx` measured 996 s for the same producer on 2026-08-24. Both runs are
real; the 1.5× difference is not explained here and should not be read as a
regression. Two candidates, neither tested: this container is slower, or the
convention-D peel regeneration changed the work. **Budget 1500 s, not 996 s**,
and expect the whole cost to sit in the last atom.

The practical note from `qou-2wtx` still holds and is worth repeating: the five
cheap atoms take ~2 s combined **and every one of them fails too**, so any
hypothesis about this producer is testable in seconds rather than 25 minutes.

### It clears its `Q0_FLIP` honestly

`q0Value` moves `1.109978595557334…` (**A**) → `1.109978595642739…` (**C**) with
`q0Anchor` staying `muon` — the A→C re-pin, not a stamp change. This producer is
on the **resolve** side of the partition (it reads `derived_50_digit.q` and
asserts the C prefix), so the re-run migrates arithmetic and stamp together.
`Q0_FLIP 3 → 2`, `Q0_OK 1032 → 1033`.

## 3 — the three `Q0_FLIP`: reproduced, and they are not re-stamping work

Measured on this tree: `Q0_FLIP 3`, `Q0_OK 1032`, `Q0_COMPARISON 4`. The three
are exactly the ones the drain doc named.

**Every one of the three RESOLVES its pin — none hardcodes.** That matters
because the backlog warns against clearing a flip by re-running a producer whose
q₀ is a frozen literal, which would stamp `proton` onto muon-computed
arithmetic. Verified by reading each import:

| witness | pin source | manifest | a re-run yields | disposition |
|---|---|---|---|---|
| `cross-check-trM-cw-seminormal` | `derived_50_digit.q`, asserted | `ideal_muon` | muon@C — **correct** | **closeable**, and closed by item 2 |
| `hadron-knot-table` | `q_parameter.Q_50_DIGIT_STR` | `ideal_muon` | muon@C — correct | **blocked on compute**, not mechanism |
| `qbeta-c4even-exact-sseries` | `substrate.q_parameter.Q_50_DIGIT_STR` | **UNLISTED** | **proton** | **blocked on scope** (`qou-cds1`) |

The last one is blocked twice over: an unlisted stem resolves proton rather than
the muon@C this migration is about, *and* its payload is the convention C→D
ladder re-derivation that `qou-cds1` owns. Landing either inside a q₀ PR is the
error the drain doc's Group-P reasoning avoided.

## 4 — `lever1_binding_habiro_single_element_test`: already consistent

The backlog reports the manifest listing `ideal_muon` while `main`'s witness was
stamped `proton`. **Neither side is wrong on current `main`** — they agree:

- manifest: `ideal_muon`
- witness: `q0Anchor: muon`, `q0Value: 1.1099785956427390466817` (**C**, current)
- producer: routes through `q_parameter.q_at`, so the `ideal_muon` listing is
  effective rather than inert

Verified rather than inferred: the producer was re-run and its witness came back
**unchanged**. The branch's own producer fix (`97c6f695e0`, replacing a direct
`qou_substrate.constants` read) is what made the listing bite; the merge
resolution described in the drain doc landed it.

## 5 — `qou-wgaw`: they measure the same thing, and the dashboard is wrong twice

Bean `qou-wgaw` was explicit that it had **not** established whether the two
fields measure the same quantity. They do.

`onepb_status_dashboard.py` reads `cross-check-trM-1ppb.witness.json` and
reduces over its own `data.deltas`. It is not a method-vs-method check standing
beside the per-atom one — it is a **projection of the very witness it
contradicts**.

### Defect 1 — a key that does not exist

```python
"max_rel_delta": max((float(d.get("rel_delta", 0)) for d in ...), default=0.0)
```

**No delta entry has ever carried `rel_delta`.** The keys present are
`rel_delta_max`, `peel_rel_delta`, `exact_method_rel_delta`,
`pairwise_rel_deltas`. So the generator yielded `0` six times and
`max_rel_delta` was `0.0` **by key-miss, not by measurement**.

That field feeds the **gating** assertion `markov_trace_max_rel_delta`
(expected 0.0, tolerance 1e-9). **The L1 Markov-trace gate was structurally
incapable of failing** — and AGENTS.md sends agents to this witness for L1
status.

Measured from the key that exists: **2.90663e-7**, 290× the gate's own
tolerance, on 6 of 6 atoms.

### Defect 2 — forty days stale

`all_within_1ppb` and `any_diverge` pass straight through and were stale:
dashboard computed 2026-07-20, cross-check 2026-08-29.

### Why the distinction is the finding

**Staleness drains on a re-run; a key-miss does not.** Defect 2 would have
cleared itself the next time anyone regenerated the dashboard. Defect 1 would
have survived every regeneration, indefinitely, still reporting `0.0`.

### Result

```
max_rel_delta    0.0   -> 2.90663064970691e-7
any_diverge      False -> True
all_within_1ppb  True  -> False
allPassed        True  -> False
```

**The 1e-9 tolerance is unchanged.** No baseline widened, no `--rebaseline`, no
hand-edited digit. The gate fails because it can finally see its input.

### The naming, which the bean flagged and which turned out to be mechanical

Both fields are named `1ppb` while L1's target has been **1 ppQ (1e-15)** since
2026-05-26. The source witness **already carries `within_1ppQ`** (False on all
6), so surfacing it was a two-line change. Added `all_within_1ppQ` and an
`l1_target_note` naming which to quote; `*_1ppb` kept for consumer
compatibility. Also recorded `max_rel_delta_source_key` and
`n_atoms_with_rel_delta`, so a future key rename surfaces as a changed field
rather than silently reading `0.0` again.

### The float64 ratchet regression here is NOT from this change

The ratchet reports `onepb-status-dashboard` 5 → 6. **Control: `main`'s
unmodified producer, regenerated on this tree, gives the identical 5 → 6.** The
added fields are all `structural_lp_dual.dual_values[*]`, copied verbatim from
the upstream LP witness, whose `y_star[0]` entries moved from exactly `0.0`
(integral, carved out of the ratchet) to tiny non-zero and so left the carve-out
— the same mechanism the drain doc records for `c-k-beta-decay-bound`. This
branch's own field is an mpf string and is not in the added set.

Left as-is. The fix is an mpf refactor of the LP producer; suppressing it with a
baseline edit is the thing the ratchet exists to prevent.

## 6 — `hadron_knot_table`: not run to completion, but the hot call is named

Deliberately **not** run to completion. AGENTS.md records > 50 min for one bound
atom of nineteen, and the backlog says a cheap "why" is worth more than an
expensive "done". So: a stack sampler
(`faulthandler.dump_traceback_later(25, repeat=True)`) over a 200 s bounded run,
which needs no completion and no profiler.

**Two hot sites, both under one caller.** Every sample sits inside
`hecke_core_legacy.unified_iterative_correction`, reached from
`binding_energy:2334` ← `hadron_knot_table.compute_atom:180`:

| sample | innermost frame | via |
|---|---|---|
| 1 | `_count_syts_by_12_relation.fill` at **recursion depth 16** | `partition_character_sigma1:389` ← `_partition_table:436` ← `_ensure_ysn_attached:1167` ← `__iter__:488` ← `unified_iterative_correction:1364` |
| 2 | `_matmul_dim:1102` | `unified_iterative_correction:1506` |

`fill` is a single-cell recursive **brute-force enumeration of every standard
Young tableau** of a shape, used only to bucket SYTs by whether 1 and 2 share a
row, a column, or neither. A depth of 16 means shapes of ≥ 16 cells, and the
enumeration is `Σ_λ f^λ` — the involution number, ~4.6e7 at n = 16. That is the
cost, and it is arithmetic-free: pure Python lists and integers.

**This corroborates AGENTS.md's "does not crash; it is very slow" and sharpens
it.** AGENTS.md names `unified_iterative_correction` as the site; these samples
name the two calls inside it. Note also what is *absent* from every stack:
no `scipy.sparse`, no dtype-object boundary. The sparse defect that bean
`qou-q7lf` reported is not what this producer is doing.

**Not claimed:** that `fill` is the dominant cost overall. Three samples over
200 s of one atom is evidence about where this atom spends its first minutes,
not a profile. `χ_λ(σ_1)` has a closed form — the docstring states it — so a
memoised or closed-form `_count_syts_by_12_relation` is the obvious lead, but
nothing here measures what that would buy.

## 7 — the `qou-mass` vendor mirror: in sync

`scripts/sync-qou-mass-vendor.py --check` reports **in sync** — 47 modules, 23
witness JSON, 122 package-data witness JSON. The **six pre-existing module
drifts** the drain reported are gone; the drain's own regeneration landed and
closed them. Nothing hand-edited.

---

## What is still open

Filed rather than closed, each with the reason:

| item | bean | blocked on |
|---|---|---|
| `hadron-knot-table` flip | `qou-r4w5` | compute. It **resolves** its pin correctly, so a re-run would be a valid migration — it just cannot finish. The hot call is now named. |
| `qbeta-c4even-exact-sseries` flip | `qou-cds1` | scope. Its stem is UNLISTED so a re-run yields **proton**, not the muon@C this migration is about; and its payload is the convention C→D ladder re-derivation that `qou-cds1` owns. |
| the remaining ~1e-7 on the seminormal leg | `qou-2wtx` step 2 | a pin-policy decision on an L1 reference — dropping the leg's `QOU_Q0_ANCHOR=ideal` default so both legs sit at proton. |
| `onepb` / LP-dual raw float64 | `qou-ftuv` | an mpf refactor of the LP producer. Pre-existing; reproduced identically from `main`'s own producer. |
| **L1 is not met, and the corpus says otherwise in two places** | `qou-3zby`, `qou-mj1o` | see below. |

### The L1 status claim needs an owner

This is the finding with the widest blast radius, so it is stated plainly.

AGENTS.md's Precision-goals table records **"L1 compute met"** and directs
readers to `onepb-status-dashboard.witness.json`. That witness now reports
`allPassed: False`, driven by `markov_trace_max_rel_delta` = **2.90663e-7**
against a 1e-9 tolerance, with `all_within_1ppQ` False on 6 of 6 atoms.

Two corpus records point the other way and both are now wrong:

- **`qou-mj1o`** is `completed` and its title asserts *"L1 actually MET"*. Its
  own fix was correct — excluding dead structural inventory from `allPassed` —
  and is untouched here. But the green it left behind rested on an assertion
  that could not fail.
- **AGENTS.md** itself. Not edited here: a Precision-goals change is an owner
  call, not a drain's.

**`qou-3zby` reached the same conclusion from the other side on 2026-08-16** —
*"while it is red, 'L1 compute met' is not supportable by this cross-check"* —
and it is `in-progress`. The dashboard side now agrees with it. Two independent
routes, one conclusion.

**This is a reporting defect, not a new physics failure.** The 2.9e-7 was
already in the committed cross-check witness on `main`; nothing computed here
made L1 worse. What changed is that the dashboard can no longer report `0.0`
for it.

## One defect this branch introduced, and the gate that caught it

Worth recording because it is a trap in the *fix* rather than the bug.

Adding `import mpmath as mp` to the dashboard — to replace the banned
`float()` — introduced a quieter version of the same defect one layer down:
**mpmath defaults to `dps=15`**, so the max over 50-digit decimal strings was
still being taken at float64 precision. The witness recorded
`2.90663064970691e-7`, fifteen significant figures.

The `never-raises-dps` ratchet flagged it as `NEW: onepb_status_dashboard.py`,
and the fix is the module-scope idempotent `set_compute_dps()` the ratchet's own
message prescribes. The witness now records the full
`0.00000029066306497069143204195642669120799801012802521353`. Not baselined —
the gate says *"Do NOT add the file to the baseline to silence this"*, and the
value really was low.

**An mpf fix can itself be a precision defect if the module never raises dps.
The two are one import apart.**

## Discipline

No baseline was widened at any point: no `--rebaseline`, no file added to a
baseline JSON, no hand-edited digit. `scripts/precision-gates.sh --changed`
before each commit.

**Audit-witness byproducts were reverted, not landed.** Running the gates
regenerates `q0-value-drift-audit`, `mpf-float-source-audit`,
`witness-provenance-audit` and others. Their moves are `main`'s drain tail
(`q0-value-drift` STALE 307 → 236) and the audit producers' own re-stamps, not
this branch's work. The gate's own instruction — *"check whether the movement is
yours or main's before claiming it"* — is why they are not in this PR.

**Every producer run was tracked and reaped.** Nothing was started with
`start_new_session=True`; each background run carries a recorded PID and a
`timeout`, and the two long ones were polled to completion rather than
abandoned.

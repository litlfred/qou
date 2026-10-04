---
# qou-wpp2
title: 'Vendor mirror ratchet is RED on main: 9 modules drifted, 1 witness missing from the cone'
status: todo
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-19T21:03:40Z
updated_at: 2026-10-04T15:11:41Z
parent: qou-5vkl
---

Measured on origin/main 5b158ef06c, 2026-08-19.
`python3 scripts/sync-qou-mass-vendor.py --check` exits non-zero.

    MISSING from qou-mass/src/qou_mass/_internal (1):
      data/hecke-character-symbolic.witness.json
    DRIFTED from source (9):
      data/atomic-tr-m-mpfr-50dps.witness.json
      _li_2_q_util
      _precision
      canonical_braid_crossings
      codata_constants
      hecke_character_symbolic
      markov_peel
      markov_trace_canonical
      wedderburn_jones_markov

The ratchet was built (PR #5073) precisely because all 14 vendored copies had
rotted by hand-copy, and because one of those rots was MASKING the defect a
test existed to find. It is red again after four days, so nobody is running
`--apply` when a cone module changes. The generator is not the problem — it
takes one command.

The drift is not cosmetic. `wedderburn_jones_markov` alone is 37 diff lines and
includes a live behavioural change the mirror does not have:

    if sp.sympify(y).is_zero:
        continue   # zero Ocneanu weight => y*chi = 0 (TL_n radical)

That is the convention-D TL_n radical skip (`conventionD_weight_eq_zero_iff`,
audit 2026-08-16). Skipping those blocks changes no value, so the mirror is not
computing wrong numbers today — but the mirror is now a generation behind on the
module that decides which Wedderburn blocks are even built, which is exactly the
distance at which the last mask formed.

`data/hecke-character-symbolic.witness.json` is MISSING, not drifted: a new
witness entered the 42-module cone and the mirror never got it.

## Next step

`--apply`, verify `qou-mass` still passes 20, commit. Then the real question:
the ratchet is advisory — nothing runs it on a push. Either it joins
`scripts/check-sidecars.sh` as a hand-run preflight with a named trigger
(any edit under the cone), or it stays red on a four-day cycle. Recommend the
former; the cone list is machine-derivable, so the trigger can be exact.



---

## Note from qou-cdj8 (2026-08-21) — this is RESOLVED; status left for its owner

The drift recorded here was fixed **28 minutes after this bean was filed**:

    qou-wpp2 filed        2026-08-19 21:03:40
    e4906af5a4c           2026-08-19 21:31:30  chore(vendor): regenerate the mirror

On current main `--check` exits **0** (42 modules, 18 witness JSON). I hit the
identical measurement independently on my own branch and filed `qou-hp3g` for
it, then had to retract that too — same cause, a checkout predating the fix.

Verified the detector still fires rather than trusting exit 0: planted one line
in the vendored `_precision.py` → `exit 1, DRIFTED (1): _precision` → restored
→ clean.

**Your root-cause line is the durable part and it is confirmed.** "Nobody is
running `--apply` when a cone module changes" — I grepped every `.sh` and
`.yml`: **nothing invokes this script.** It is in no gate array and no
workflow, only in docs and beans, while AGENTS.md calls `--check` "the gate".
That is why it went red again in four days and will again. Fourth instance of
the qou-j6gb pattern.

Also found, and split to `qou-cdj8`: the check covers 42 modules + 18
witnesses, while **122 further witness files** under `qou-mass/src` are never
compared, and **17 witnesses exist in both the package root and `data/`** —
2 of those pairs divergent, including `q-pinning-50-digit` (root 2026-08-21,
data/ 2026-07-18), the substrate modulus record.

Not touching this bean's status — it is yours.

## Now 10, and the 10th is a DIFFERENT KIND of drift (2026-09-06, PR #6960)

`closed_form_tau_M` joined the drift list today. It is not another
accumulated hand-copy divergence like the other nine — it appeared the moment
the `qou-y2o7` option-B fix landed on the source without a vendor sync.

**What that means concretely.** `compute_tau_M_nucleon_H3` on the source now
takes its word from `atom_braid_word_3A` and produces the canonical ordering
(tau_p 0.6293). The vendored mirror still carries the pre-fix body, which
builds a grouped word inline and produces tau_p 1.1458 — a factor 1.82. So the
shipped `qou-mass` package computes the SUPERSEDED physics while its own
source computes the ruling's. That is the 'two copies fork' hazard `qou-y2o7`
flagged for the habiro witnesses, realised in code instead.

Found independently by `computations/audits/self_built_braid_word_audit.py`
(PR #6960), which flags the mirror as MONOTONE_LITERAL while correctly reading
the fixed source as MIXED — so the audit separates 'has a canonical path' from
'does not', and the mirror does not.

**Not fixed here, deliberately.** `sync-qou-mass-vendor.py` has no per-module
flag: `--apply` is all-or-nothing across all 10 entries including 3 witness
JSONs, so running it from a feature branch would sweep in nine unrelated
pre-existing drifts and regenerate numbers. That belongs with whoever drains
this bean, not with an audit PR.

Live count: `--check` exits 1, DRIFTED 10 (7 modules + 3 witnesses).

## DRAINED — PR pending (2026-09-07)

`sync-qou-mass-vendor.py --apply`. `--check` now exits 0: 51 modules, 25
witness JSON, 122 package-data witness JSON, all in sync.

**Correcting my own note above:** I wrote that syncing 'would regenerate
numbers'. It does not. The script is a pure copy — `dest.write_bytes(
src.read_bytes())` for witnesses, `render()`-then-write for modules — and runs
no producer. Verified: all 7 changed JSON files are byte-identical to their
`computations/` source, 0 mismatches. Nothing here was recomputed; the numbers
already existed on main.

What moved in the shipped package (grouped -> canonical):

    proton tau   1.14575969245730 -> 0.62932840220292
    neutron tau  0.98774368811581 -> 0.47513351715568
    deuteron     0.57517224391777 -> 0.15196833920423
    helium-4     0.16097414544241 -> 0.01123741766155

One orphan reported not deleted: `canonical_braid_marshalling` is vendored but
outside the cone; removing a shipped module is an API decision.

## The drain does NOT make the package canonical — bean `qou-36i2`

Measured after syncing: `canonical_braid(1,0).generators` is still
`(0,0,0,0,0,0,0,1,1,1,1)` (grouped) and `compute_tr_M(1,0)` still returns
1.1457 (superseded). Both APIs read
`canonical-mass-table-extended.witness.json` FIRST, deliberately, and that
shard — `computedAt` 2026-08-28, a week before the ruling — stores the grouped
word in a field named `braid_word_canonical`, for all 9 rows.

So the mirror was one of THREE carriers, and the one this bean covers is now
the only one closed by copying. Filed as `qou-36i2`; it needs producer work
that should land with `qou-xwet` and `qou-3wqg`, which already say that file
needs regenerating.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

---
# qou-wpp2
title: 'Vendor mirror ratchet is RED on main: 9 modules drifted, 1 witness missing from the cone'
status: todo
type: bug
priority: normal
created_at: 2026-08-19T21:03:40Z
updated_at: 2026-08-21T21:54:08Z
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

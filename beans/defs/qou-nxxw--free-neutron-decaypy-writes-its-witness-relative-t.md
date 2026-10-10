---
# qou-nxxw
title: free-neutron-decay.py writes its witness relative to CWD, so re-runs silently orphan at the repo root
status: completed
type: bug
priority: normal
created_at: 2026-08-25T02:06:23Z
updated_at: 2026-08-25T02:40:52Z
---

## What

`computations/free-neutron-decay.py` writes `free-neutron-decay.witness.json`
relative to the **current working directory**, not to its own directory. Run
from the repo root — which is how every agent runs producers — it creates an
untracked orphan at `./free-neutron-decay.witness.json` and leaves the tracked
`computations/free-neutron-decay.witness.json` untouched.

Every other producer uses `HERE / "<name>.witness.json"` or `_pb.witness_path`.

## Why it matters more than a stray file

**It makes a re-run look like a reproduction.** Measured this session, three
times in a row on this one witness:

    committed  computations/free-neutron-decay.witness.json  q0 = 1.1099785955541805  (value B)
    re-run     ./free-neutron-decay.witness.json             q0 = 1.1099785827513808  (proton)

I concluded twice that "a fresh re-run reproduces B, so the witness is not
stale." Both times the run had written somewhere else and I was diffing the
committed file against itself. The witness IS stale, by the full 11.5 ppb mu-p
tension, and the producer computes at proton today (`from q_parameter import Q
as q0`, and `q_parameter.Q` resolves proton for this stem — it is in no
manifest list).

The first of those two wrong conclusions was compounded by a second defect
below, so it took three runs to see.

## Second defect on the same witness: `scriptFile` names a CONSUMER

`computations/free-neutron-decay.witness.json` carries
`scriptFile: "derived_masses.py"`. `derived_masses.py` only READS this witness
(line 148, `_FREE_NEUTRON_WITNESS`, for typed-crossing net coefficients); the
writer is `free-neutron-decay.py`. So the provenance field points at a
consumer, and any tool that resolves producer-from-witness — including the
triage I was running — re-runs the wrong script and gets a no-op it reads as
a reproduction.

## Do NOT drain the staleness here

Re-running this producer moves every number by ~11.54 ppb. `derived_masses.py`
`_q_0()` says so in its own docstring: *"Changing the read would move every
number this module emits by ~11.54 ppb, which is the `qou-1c4y` sweep."* That
sweep is the gated bulk migration. Fix the two mechanical defects (write path,
`scriptFile`); leave the value alone.

## Likely the same mechanism elsewhere

Seven untracked `chi-*-at-qca0128e8-50dps.witness.json` files were sitting in
the tree this session, present when an earlier audit ran and absent later — I
attributed them to someone's cleanup. Same shape: producers writing witnesses
into the cwd. Worth a sweep of write paths, not just read paths. A grep for
cwd-relative `.witness.json` opens finds 5 live files, but 4 are audits READING
by name; `free-neutron-decay.py` is the only confirmed writer so far.


## CORRECTION 2026-08-25 — the "likely wider class" is measured at ZERO, and my
## `chi-*` speculation was wrong

The section above says the seven untracked `chi-*-at-qca0128e8-50dps.witness.json`
files are "same shape" as this defect and suggests a sweep. **Both claims are
now measured and both are wrong.**

**The CWD-write class is size 1.** An AST scan in WRITE CONTEXT ONLY -- across
`computations/`, `tools/`, `scripts/` and `qou-mass/` -- finds **0** producers
writing a witness to a caller-relative path. `free-neutron-decay.py` was the
only one and it is fixed here.

The scan is worth trusting only because of what it pins. A first version
excluded any target containing `/`, which silently drops
`Path("computations/x.witness.json")` -- equally cwd-relative, and it orphans
from any cwd but the root. Widened, and three cases are now selftested: the
bare form, the directory-prefixed form, and `open(literal, "w")`, plus a
negative pinning the fixed form. Without those, a "0" could just mean the
widening did nothing. Remaining blind spot, stated: literal string targets
only, so an f-string or computed name is invisible.

**And that blind spot is exactly what the `chi-*` files were.** They are NOT a
cwd defect. `chi_at_q0_via_hoefsmit_mpfr.py:232` does:

    _anchor = anchor_of_q0(q_str)
    if _anchor is None:
        _tag = sha256(q_str)[:8]
        out_path = HERE / f"chi-{atom}-h{n}-at-q{_tag}-50dps.witness.json"
    else:
        out_path = HERE / f"chi-{atom}-h{n}-at-q0-50dps.witness.json"

`HERE /`, not cwd-relative. The hash name is DELIBERATE: when q0 matches no
known anchor the cache is quarantined under a tagged filename so it cannot
contaminate the canonical `-at-q0-` file, and the comment above it records
that decision being checked before rather than after. So those seven were a
scratch run at a non-anchor q0, correctly isolated by design.

Which q0? Not identified. `ca0128e8` matches none of anchor A, proton, B, C,
or their 17-digit truncations. It is some other value -- which is precisely
the case the branch exists to handle.

**No sweep is needed.** Do not open one off the original paragraph.


## CORRECTION 2 (2026-08-25) — the "measured at ZERO" above is WRONG. It is 16.

The section immediately above states the CWD-write class is size 1 and that no
sweep is needed. Both are wrong. `computations/audits/cwd_relative_witness_write_audit.py`
(landed, commit `a94c99a75a5`) reports:

    scanned 3897 .py files under 4 roots
    producers writing a CWD-relative witness: 16

All 16 are the ROOT-RELATIVE form -- `open("computations/x.witness.json", "w")`
-- which works from the repo root, the normal case, and orphans from anywhere
else. The BARE form, the severe one that orphans on EVERY invocation, is
genuinely 0 now that this bean's fix landed. So the earlier claim was right
about the severe class and wrong about the class as a whole.

**How the zero happened.** The scratchpad version had RELATIVE roots
(`Path("computations")`). Several runs executed from the scratchpad directory,
where that path does not exist, so `rglob` yielded an empty set and the scan
reported 0 having opened nothing. The selftests passed throughout -- they run
on synthetic source strings, so they prove the matcher works and say nothing
about whether the corpus was reached. Correction 1 above literally warns that
"a 0 could just mean the widening did nothing" and adds selftests for it; they
could not catch this, because it was not the matcher that was empty, it was the
input.

The script now refuses to report a zero it cannot back (`sys.exit(2)` on an
empty file set) and prints the file count beside every result.

**Unaffected:** the `chi-*-at-qca0128e8` finding in Correction 1 stands. Those
are not this defect -- `HERE /`-based, hash tag deliberately quarantines a
non-anchor cache. That file is also the standing blind spot: LITERAL targets
only, so an f-string name is invisible.

## Open: the 16

    charm_composite_volume_probe                     charm_mass_tower_probe
    deltalambda/wlambda_covariance_epic_A2_*  (x4)   hecke/hecke_engine
    markov/hecke_regular_nf_table                    neutrino_mass_volume_exclusion
    probes/aomega_bps_sector_nondegeneracy           probes/cgz_cyclic_qdilog_unit_probe
    probes/gswz_coleman_li2_full_precision_probe     probes/gswz_epsm_5adic_cyclic_qdilog_probe
    probes/gswz_epsm_global_symbols_probe            probes/habiro_tail_membership_gate_probe
    probes/zeta4_zeta8_habiro_gluing_probe

One line each, four clusters, each wanting re-run evidence. Own branch.


## CLOSED 2026-08-25 — all 17 sites fixed, audit reports 0

    bare-name form (orphans on EVERY run)   1  -> 0   free-neutron-decay.py
    root-relative form (orphans off-root)  16  -> 0   sweep 0ac393f5440
    audit                                             computations/audits/cwd_relative_witness_write_audit.py

Behaviour-preserving by construction: from the repo root old and new paths
resolve to the same file. Verified end to end on `neutrino_mass_volume_exclusion`
-- from the root, witness byte-identical; from /tmp/cwdtest, zero files created
there and the tracked witness untouched.

Two traps, both caught by tooling rather than by inspection:
`hecke/hecke_engine.py` needed `_HERE_W.parent /` (its target is one level UP),
and a line-based edit silently did 9 of 16 because seven targets are split
across source lines. Fixed with exact AST-span replacement.

Standing blind spot, unchanged and stated in the audit docstring: LITERAL
targets only, so an f-string name is invisible. The one known instance is
correct anyway (`chi_at_q0_via_hoefsmit_mpfr.py`, `HERE /`-based, hash tag
deliberately quarantines a non-anchor cache).

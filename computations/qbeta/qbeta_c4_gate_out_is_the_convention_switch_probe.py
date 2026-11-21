#!/usr/bin/env python3
"""The 4.50e+04 `c_4` gate-out is the CONVENTION C -> D SWITCH, amplified by 1/u^4.

Bean `qou-oiz3` (the witness refresh) found `qbeta-habiro-tower-1ppq` moving by a worst
relative 4.50e+04 -- by far the largest move in the whole 78-producer pass. This probe
identifies the cause exactly and reproduces both recorded values. Scope (a); emits no
witness, wires nothing, moves no number, fits nothing: every quantity below is either read
from a committed artifact or computed from it in closed form.

THE ANSWER. It is not drift, not environment, and not precision. `Q_N1` in the upstream
witness `q-beta-operator-valued-N3.witness.json` is

    Q_N1 = Q_A * cos(alpha_eff),   alpha = (z - 1)*h/2,   alpha_eff = alpha - b*hbar^2/2

so it depends on `z`, the MARKOV PARAMETER -- i.e. on the convention. The owner ruled
convention D canonical on 2026-08-15 (`z_D = q^3/(q^2+1)`, replacing `z_C = sqrt(q)/(q+1)`),
AFTER the committed witness was written on 2026-06-28. Measured:

    z_C = 0.499320334184        z_D = 0.612688037146
    alpha_C = -0.05233612027    alpha_D = -0.04048577734      (a 22.6 % change)
    Q_N1^C  =  0.78239116750    Q_N1^D  =  0.78286150493      (6.01e-4 relative)

and the Habiro peel PINS `c_2 = -1` and `c_3 = -2`, so the entire discrepancy lands on the
next free rung, `c_4 = (R_remaining - 1)/u^4`, at a gain of `1/u^4 ~ 1.9e8`:

    c_4^C = -2.5438      (witness records -2.5378659117940257)
    c_4^D = -114136.15   (witness records -114136.0)

So a 6.01e-4 move upstream becomes a 4.50e+04 move in a recorded "tower coefficient". The
gate was right to refuse it, and for a stronger reason than staleness: the quantity is fit
output, not a measurement.

WHAT IS NEW HERE AND WHAT IS THE CORPUS'S. The corpus already holds the characterisation.
`docs/coordination/1ppq-qbeta.md` calls this producer "form-fitting iterative peel"
(2026-05-31), and `qbeta_habiro_integrality_kill_test.py` states that *"c_4, c_5 have NO
scheme-independent empirical value: once c_3 absorbs the single CODATA residual, sequential
extraction returns c_4 = c_5 = 0 identically; every recorded c_4/c_5 number presupposes a
structural choice at a lower rung (extended-ck imposes c_3 = -2 ...)"*. This producer IS
that variant. What this probe adds is the quantitative demonstration -- the exact cause,
reproduced to 5.8e-39 on the D side -- and the integrality defect below.

AND IT IS A MEASURED CASE FOR AGENTS.md's STANDING WARNING. That document states the ladder
"must be RE-DERIVED under D, and that is NOT a z-swap" (bean `qou-cds1`). Here is what a
z-swap actually produces: `c_4 = -114136` where the C frame had `-2.54`, with the
integrality claim below gone vacuous. The ladder's C-frame conclusions stay C-conditional.

THE INTEGRALITY TEST IS RELATIVE, SO IT GOES VACUOUS AS c_k GROWS -- not found in the
corpus, and it is a defect in the producer rather than in the mathematics. The criterion is

    frac = |c_float - round(c_float)| / |c_float| * 100 < 5

which admits a window of +/- 5 % OF c_k. At `c_4 = -114136` that is +/- 5707, so "c_k is an
integer" carries no information; and the producer then CONTINUES PEELING with the rounded
value, so the next rung absorbs the rounding error. The `1 ppQ ACHIEVED` banner is likewise
unfalsifiable: `c_k := (R-1)/u^k` followed by `R /= (1 + c_k u^k)` gives `R/R = 1` exactly,
so the final residual is zero BY CONSTRUCTION at any anchor. Compare AGENTS.md on
`qbeta_ck_cache.py`, which "extracts ONE rung by inverting the target" for the same reason.

ATTRIBUTION IS NOT AVAILABLE, and saying so is part of the result. The only commit this
clone's log attributes to the upstream witness in the window is `806d5146227`, which IS a
shallow boundary (checked against `.git/shallow`), so the log is truncated there. The
VALUES are reliable -- both are read out of git -- but which commit moved `Q_N1` cannot be
determined here. Do not quote `806d5146227` as the cause.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = next(p for p in HERE.parents if p.name == "computations")
ROOT = COMP.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

UPSTREAM = "computations/q-beta-operator-valued-N3.witness.json"
TOWER = "computations/qbeta/qbeta-habiro-tower-1ppq.witness.json"
#: the committed witness's own `commitSha` -- the correct window, not the merge base.
WITNESS_SHA = "69f7ec22fef"
#: proton pin, 70 digits (q_parameter.Q_MP); written out so the probe needs no anchor import.
Q0 = ("1.1099785827513808075916690956107688798744991218735787360728142401817989")


def _git_show(rev: str, path: str) -> dict:
    out = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True,
                         text=True, cwd=str(ROOT))
    if out.returncode != 0 or not out.stdout.strip():
        raise RuntimeError(f"cannot read {path} at {rev}")
    return json.loads(out.stdout)


def _peel_c4(d: dict, u, q):
    """Reproduce the producer's peel exactly: N=1 from the witness, then pinned c2, c3."""
    Q_AME = mp.mpf(str(d["Q_AME"]))
    Q_A = mp.mpf(str(d["Q_A"]))
    Q_N1 = mp.mpf(str(d["Q_N1"]))
    R = Q_AME / Q_A
    R = R / (Q_N1 / Q_A)                 # N=1, read from upstream
    R = R / (1 + mp.mpf(-1) * u ** 2)    # c_2 = -1, PINNED
    R = R / (1 + mp.mpf(-2) * u ** 3)    # c_3 = -2, PINNED
    return (R - 1) / u ** 4, Q_N1, Q_A


def main() -> int:
    q = mp.mpf(Q0)
    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2

    z_C = mp.sqrt(q) / (q + 1)
    z_D = q ** 3 / (q ** 2 + 1)

    old_up = _git_show(WITNESS_SHA, UPSTREAM)["data"]
    new_up = _git_show("HEAD", UPSTREAM)["data"]
    # The gate baselines against HEAD, so HEAD's tower witness is the comparison.
    head_tw = _git_show("HEAD", TOWER)
    sha_tw = _git_show(WITNESS_SHA, TOWER)
    new_c4_recorded = mp.mpf("-114136.0")          # the fresh run, recorded in the pass
    old_c4_recorded = mp.mpf(str(head_tw["data"]["tower_coefficients"]["c_4"]))
    sha_c4_recorded = mp.mpf(str(sha_tw["data"]["tower_coefficients"]["c_4"]))

    c4_old, qn1_old, QA_old = _peel_c4(old_up, u, q)
    c4_new, qn1_new, QA_new = _peel_c4(new_up, u, q)

    def qn1_from(z, QA):
        alpha = (z - 1) * h / 2
        return QA * mp.cos(alpha - b * hbar ** 2 / 2), alpha

    qn1_C, a_C = qn1_from(z_C, QA_new)
    qn1_D, a_D = qn1_from(z_D, QA_new)

    checks: list[tuple[str, bool, str]] = []

    checks.append((
        "convention_D_reproduces_live_Q_N1",
        abs(qn1_D - qn1_new) / qn1_new < mp.mpf("1e-30"),
        f"|Q_N1^D - Q_N1(HEAD)|/Q_N1 = {mp.nstr(abs(qn1_D-qn1_new)/qn1_new, 4)} < 1e-30",
    ))
    checks.append((
        "convention_C_reproduces_committed_Q_N1",
        abs(qn1_C - qn1_old) / qn1_old < mp.mpf("1e-6"),
        f"|Q_N1^C - Q_N1(witness)|/Q_N1 = {mp.nstr(abs(qn1_C-qn1_old)/qn1_old, 4)} < 1e-6 "
        f"(residual is the Q_A precision difference between the two upstreams)",
    ))
    checks.append((
        "Q_N1_moved_by_about_6e-4",
        mp.mpf("5e-4") < abs(qn1_new - qn1_old) / qn1_old < mp.mpf("7e-4"),
        f"relative Q_N1 move = {mp.nstr(abs(qn1_new-qn1_old)/qn1_old, 6)}",
    ))
    checks.append((
        "peel_reproduces_committed_c4",
        abs(c4_old - old_c4_recorded) / abs(old_c4_recorded) < mp.mpf("3e-3"),
        f"reconstructed {mp.nstr(c4_old,10)} vs HEAD-recorded {mp.nstr(old_c4_recorded,10)}",
    ))
    # The witness's OWN commitSha holds a DIFFERENT c_4 than HEAD does: it has been
    # re-committed since that sha was stamped, so `commitSha` does not identify the
    # content at HEAD. AGENTS.md records this class for `scriptCommitSha`; it applies to
    # `commitSha` too, and it is why the gate must baseline against HEAD, not the sha.
    checks.append((
        "witness_commitSha_does_not_match_HEAD_content",
        abs(sha_c4_recorded - old_c4_recorded) / abs(old_c4_recorded) > mp.mpf("0.1"),
        f"c_4 at {WITNESS_SHA} = {mp.nstr(sha_c4_recorded,10)} but at HEAD = "
        f"{mp.nstr(old_c4_recorded,10)} -- the witness moved after its sha was stamped",
    ))
    checks.append((
        "peel_reproduces_fresh_c4",
        abs(c4_new - new_c4_recorded) / abs(new_c4_recorded) < mp.mpf("1e-4"),
        f"reconstructed {mp.nstr(c4_new,10)} vs recorded {mp.nstr(new_c4_recorded,10)}",
    ))
    gain = 1 / u ** 4
    checks.append((
        "amplification_is_one_over_u_fourth",
        mp.mpf("1.8e8") < gain < mp.mpf("2.0e8"),
        f"1/u^4 = {mp.nstr(gain,6)}; 6.01e-4 * that ~ {mp.nstr(mp.mpf('6.01e-4')*gain,6)}",
    ))
    checks.append((
        "c4_move_is_about_4_5e4",
        mp.mpf("4e4") < abs((c4_new - c4_old) / c4_old) < mp.mpf("5e4"),
        f"|c4_D - c4_C|/|c4_C| = {mp.nstr(abs((c4_new-c4_old)/c4_old),6)} "
        f"(the pass recorded worst = 4.50e+04)",
    ))
    # the integrality defect: a RELATIVE tolerance is vacuous at scale
    window_small = abs(old_c4_recorded) * mp.mpf("0.05")
    window_large = abs(new_c4_recorded) * mp.mpf("0.05")
    checks.append((
        "integrality_tolerance_is_relative_hence_vacuous_at_scale",
        window_large > mp.mpf("5000") and window_small < mp.mpf("1"),
        f"the producer's `frac < 5` admits +/-{mp.nstr(window_small,3)} at c_4 = "
        f"{mp.nstr(old_c4_recorded,6)} but +/-{mp.nstr(window_large,6)} at "
        f"{mp.nstr(new_c4_recorded,6)} -- the integer claim carries no information there",
    ))

    print("=" * 78)
    print(" the 4.50e+04 c_4 gate-out IS the convention C -> D switch (bean qou-oiz3)")
    print("=" * 78)
    print(f"\n  u = b*hbar^2 = {mp.nstr(u,12)}     1/u^4 = {mp.nstr(1/u**4,6)}")
    print(f"\n  {'':<22}{'convention C':>26}{'convention D':>26}")
    print(f"  {'z':<22}{mp.nstr(z_C,12):>26}{mp.nstr(z_D,12):>26}")
    print(f"  {'alpha = (z-1)h/2':<22}{mp.nstr(a_C,10):>26}{mp.nstr(a_D,10):>26}")
    print(f"  {'Q_N1 = Q_A cos(a_eff)':<22}{mp.nstr(qn1_C,14):>26}{mp.nstr(qn1_D,14):>26}")
    print(f"\n  upstream Q_N1 at the witness's own sha : {mp.nstr(qn1_old,20)}")
    print(f"  upstream Q_N1 at HEAD                  : {mp.nstr(qn1_new,20)}")
    print(f"  relative move                          : "
          f"{mp.nstr(abs(qn1_new-qn1_old)/qn1_old,6)}")
    print(f"\n  c_4 reconstructed from the committed upstream : {mp.nstr(c4_old,12)}")
    print(f"  c_4 recorded at HEAD (the gate's baseline)    : {mp.nstr(old_c4_recorded,12)}")
    print(f"  c_4 recorded at the witness's OWN commitSha   : {mp.nstr(sha_c4_recorded,12)}"
          f"   <- differs; the witness was re-committed since")
    print(f"  c_4 reconstructed from the HEAD upstream      : {mp.nstr(c4_new,12)}")
    print(f"  c_4 recorded by the fresh run                 : {mp.nstr(new_c4_recorded,12)}")

    print("\n  CHECKS")
    ok = True
    for name, passed, why in checks:
        print(f"    [{'PASS' if passed else 'FAIL'}] {name}")
        print(f"           {why}")
        ok = ok and passed
    print(f"\n  {sum(1 for _, p, _ in checks if p)}/{len(checks)} checks passed")
    print("\n  SCOPE (a). The gate-out is explained, not repaired: the recorded quantity is")
    print("  fit output whose free rung carries a 1.9e8 gain on an upstream value. The")
    print("  C-frame ladder conclusions stay C-conditional (bean qou-cds1), and a z-swap")
    print("  is NOT the re-derivation AGENTS.md asks for -- this is what one produces.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

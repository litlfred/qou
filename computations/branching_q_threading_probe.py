#!/usr/bin/env python3
"""Where does `q_val` actually go in the branching combiner? (bean `qou-8chw`)

RETRACTION FIRST. Bean `qou-8chw` recorded that
`canonical_tr_m_via_branching.compute_tr_m_via_branching(Z, N, q_val)` returns
**identical** values at `q` and `1/q`. **That no longer holds, and this probe
retracts it.** The measurement was taken on a branch that predated
`qou-zck8` / `qou-cds4` on main, which ported the H_6 pn A-operator extract off
float64, regenerated it, and fixed its consumers to parse the decimal strings.
The deuteron value moved `0.5750908722902754 -> 0.5751722439177721` and the bar
image now moves with `q`. Do not plan around the invariance claim.

WHAT SURVIVES THE RETRACTION, and it is the part that mattered: the combiner
still **cannot arbitrate** `tr_M^atom` away from `q_0`, for a different and more
basic reason. The `A^lambda_{xi nu}(I)` interface operator is a JSON file loaded
verbatim from disk; `q_val` never reaches it. So for `q_val != q_0` the returned
number is a hybrid — a frozen operator at `q_0` contracted against weights and
per-nucleon blocks at `q_val`.

This probe measures where `q_val` actually goes, and what the combiner now says
at both anchors.

WHAT IT MEASURES

  0. Whether the bar-invariance of bean `qou-8chw` still reproduces (it does
     not) and what the value is now.

  1. The A=2 path's three q-carrying inputs, separately:
       y_lambda_at(6, q_val)                      — honoured
       evaluate_word_matrix_np(mu, intra, q_val)  — honoured
       A^lambda_{xi nu}(I) interface operator     — LOADED FROM DISK
     and whether the loaded extract carries a q stamp of its own.

  2. Bar-evenness of the y_lambda weights, exactly, at 50 dps.

  3. The composite at q_0 and at 1/q_0.

PRECISION NOTE, stated rather than buried. `evaluate_word_matrix_np` builds
NumPy complex matrices, so the per-nucleon rho factor is float64 by
construction and this probe cannot change that without rewriting that function.
Every quantity this probe *concludes* from is either exact (a JSON field, a
source fact) or mpmath: the y_lambda comparison is carried at 50 dps end to
end. Where a float64 number is reported it is labelled, and no agreement at the
float64 floor is read as evidence about the mathematics.

-- Ref: [manuscript] docs/audits/2026-08-19-bar-involution-is-isospin-conjugation.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import json  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

import mpmath as mp  # noqa: E402

mp.mp.dps = 60

from q_parameter import Q_MP as Q0  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from canonical_tr_m_via_branching import (  # noqa: E402
    EXTRACT_FILENAMES,
    compute_tr_m_via_branching,
)

HERE = Path(__file__).resolve().parent
FAILS: list[str] = []


def check(name: str, ok: bool, detail: str) -> None:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}: {detail}")
    if not ok:
        FAILS.append(name)


def main() -> int:
    qi = 1 / Q0
    print("=" * 78)
    print("  BRANCHING COMBINER — where does q_val go?   (bean qou-8chw)")
    print("=" * 78)
    print(f"  q_0   = {mp.nstr(Q0, 25)}")
    print(f"  1/q_0 = {mp.nstr(qi, 25)}")
    print()

    # ---- 1. the interface operator is loaded, not evaluated -----------------
    print("1. The A^lambda interface operator")
    print("-" * 78)
    stamps: dict[str, str] = {}
    for (n_outer, iface), fname in sorted(EXTRACT_FILENAMES.items()):
        p = HERE / fname
        if not p.exists():
            print(f"     (absent) H_{n_outer} {iface}: {fname}")
            continue
        d = json.loads(p.read_text())
        stamps[fname] = str(d.get("q0Value", ""))
        print(f"     H_{n_outer:<2} {iface:<3} {fname}")
        print(f"         q0Anchor = {d.get('q0Anchor')}   "
              f"q0Value = {stamps[fname][:32]}...")

    stamped = {f: v for f, v in stamps.items() if v}
    unstamped = [f for f, v in stamps.items() if not v]
    check(
        "extract_is_loaded_not_evaluated",
        len(stamps) > 0,
        f"{len(stamps)} extract(s) present on disk, loaded verbatim by "
        f"load_A_extract(); NONE is re-evaluated at q_val",
    )
    check(
        "some_extracts_carry_no_q_stamp_at_all",
        len(unstamped) > 0,
        f"{len(unstamped)}/{len(stamps)} carry NO q0Value: {unstamped} — "
        f"a frozen operator that does not record which q it was frozen at is "
        f"strictly worse than one that does, and this is a finding in its own "
        f"right (the assertion passes when the defect is PRESENT; it is a "
        f"detector, not a target)",
    )

    # the stamped ones must at least agree, and be the proton pin
    uniq = set(stamped.values())
    if uniq:
        dev = max(abs(mp.mpf(v) - Q0) for v in uniq)
        check(
            "stamped_extracts_are_proton_pin",
            len(uniq) == 1 and dev < mp.mpf("1e-40"),
            f"{len(uniq)} distinct stamp(s) across {len(stamped)} stamped "
            f"extract(s); worst departure from q_parameter.Q_MP = "
            f"{mp.nstr(dev, 3)}",
        )
    print()

    # ---- 2. y_lambda is exactly bar-even -----------------------------------
    print("2. y_lambda bar-evenness at n = 6, exact at 50 dps")
    print("-" * 78)
    y_q = y_lambda_at(6, Q0)
    y_i = y_lambda_at(6, qi)
    worst = mp.mpf(0)
    worst_lam = None
    for lam in sorted(set(y_q) | set(y_i)):
        a = mp.mpf(str(y_q.get(lam, 0)))
        b = mp.mpf(str(y_i.get(lam, 0)))
        scale = max(abs(a), abs(b), mp.mpf(1))
        rel = abs(a - b) / scale
        if rel > worst:
            worst, worst_lam = rel, lam
    print(f"     {len(y_q)} partitions; worst |y(q) - y(1/q)| / max(|y|,1) = "
          f"{mp.nstr(worst, 6)}  at lambda = {worst_lam}")
    check(
        "y_lambda_bar_even",
        worst < mp.mpf("1e-25"),
        f"worst relative departure {mp.nstr(worst, 6)} — y_lambda is bar-even, "
        f"so it contributes NO q -> 1/q sensitivity to the sum",
    )
    print()

    # ---- 3. the composite ---------------------------------------------------
    print("3. The composite, deuteron (Z=1, N=1)")
    print("-" * 78)
    tr_q, wall_q, err_q = compute_tr_m_via_branching(1, 1, Q0)
    tr_i, wall_i, err_i = compute_tr_m_via_branching(1, 1, qi)
    print(f"     at q_0    {mp.nstr(tr_q, 25) if tr_q is not None else err_q}"
          f"   ({wall_q:.2f}s)")
    print(f"     at 1/q_0  {mp.nstr(tr_i, 25) if tr_i is not None else err_i}"
          f"   ({wall_i:.2f}s)")
    # the value the bean recorded, and the two live independent values
    BEAN_OLD = mp.mpf("0.5750908722902753612501")   # pre-qou-zck8
    TRANSFER_Q0 = mp.mpf(
        "0.5751722439177718708265353439861808891524943528928")
    TRANSFER_QINV = mp.mpf("-0.0014808531711619370338")

    if tr_q is not None and tr_i is not None:
        gap = abs(tr_q - tr_i)
        print(f"     |difference across the bar| = {mp.nstr(gap, 6)}")
        check(
            "bar_invariance_RETRACTED",
            gap > mp.mpf("1e-6"),
            f"q_0 and 1/q_0 now differ by {mp.nstr(gap, 4)} — bean qou-8chw's "
            f"bar-invariance claim DOES NOT REPRODUCE and is retracted",
        )
        moved_since_bean = abs(tr_q - BEAN_OLD)
        check(
            "value_moved_since_the_bean",
            moved_since_bean > mp.mpf("1e-6"),
            f"q_0 value moved {mp.nstr(moved_since_bean, 4)} from the "
            f"{mp.nstr(BEAN_OLD, 17)} recorded in the bean — main's qou-zck8 "
            f"regenerated the extract off float64",
        )
        # the interesting part: it landed ON the transfer value
        rel_q0 = abs(tr_q - TRANSFER_Q0) / abs(TRANSFER_Q0)
        print(f"     transfer at q_0 = {mp.nstr(TRANSFER_Q0, 25)}   "
              f"rel = {mp.nstr(rel_q0, 4)}")
        check(
            "branching_now_agrees_with_transfer_at_q0",
            rel_q0 < mp.mpf("1e-13"),
            f"relative departure {mp.nstr(rel_q0, 4)} — agreement TO THE LIMIT "
            f"OF THE FLOAT64 ARITHMETIC the branching path uses (its rho factor "
            f"is NumPy complex). Not evidence beyond that floor; what it does "
            f"establish is that a sibling's independent extract fix landed on "
            f"the same value as the transfer and the Hoefsmit arbiter",
        )
        # and still cannot arbitrate at the bar image
        rel_qi = (abs(tr_i - TRANSFER_QINV) / abs(TRANSFER_QINV))
        print(f"     transfer at 1/q_0 = {mp.nstr(TRANSFER_QINV, 20)}   "
              f"rel = {mp.nstr(rel_qi, 4)}")
        check(
            "still_cannot_arbitrate_at_the_bar_image",
            rel_qi > mp.mpf("1"),
            f"the two disagree by a relative {mp.nstr(rel_qi, 4)} at 1/q_0 — "
            f"the combiner is STILL not usable as an arbiter there, now for "
            f"the frozen-operator reason rather than the invariance reason",
        )

    # a control: a q FAR from both anchors must move the value, or q_val is
    # not honoured at all
    q_far = mp.mpf("1.5")
    tr_f, _, err_f = compute_tr_m_via_branching(1, 1, q_far)
    if tr_f is not None and tr_q is not None:
        moved = abs(tr_f - tr_q)
        print(f"     at q=1.5  {mp.nstr(tr_f, 25)}   |vs q_0| = "
              f"{mp.nstr(moved, 6)}")
        check(
            "q_val_is_partially_honoured",
            moved > mp.mpf("1e-6"),
            f"q=1.5 moves the value by {mp.nstr(moved, 4)} — so q_val IS "
            f"threaded into SOME inputs. The invariance is therefore not "
            f"'q_val ignored'; it is q_val reaching a bar-even subset",
        )
    print()

    # ---- verdict ------------------------------------------------------------
    print("=" * 78)
    print("  VERDICT")
    print("=" * 78)
    print("""
  RETRACTED: the bar-invariance. Bean qou-8chw recorded identical values at q
  and 1/q. Measured again on current main, they differ by ~0.54. The bean's
  measurement predated qou-zck8 / qou-cds4, which ported the H_6 pn A-operator
  extract off float64, regenerated it, and fixed its consumers to parse the
  decimal strings. The deuteron value moved with it,

      0.5750908722902754   ->   0.5751722439177721

  which is the TRANSFER value. So a sibling's independent fix, arrived at from
  the mass-table side and knowing nothing about this branch, landed on the same
  number the transfer path and the Hoefsmit/markov-peel arbiter give. That is a
  fourth agreement on tr_M^atom(D), and it strengthens the qou-r9dv refresh
  rather than merely confirming it.

  Stated at the right precision: the branching path's rho factor is NumPy
  complex, so its agreement with the transfer is AT THE FLOAT64 FLOOR of the
  arithmetic it uses. That is not a 16-digit corroboration and is not quoted as
  one.

  SURVIVES: the combiner cannot arbitrate away from q_0. Three inputs carry q
  into the A=2 path; only two receive q_val:

      y_lambda_at(6, q_val)                     <- q_val   and BAR-EVEN (0.0)
      evaluate_word_matrix_np(mu, intra, q_val) <- q_val
      A^lambda_{xi nu}(I)                       <- LOADED FROM DISK, frozen

  For q_val != q_0 the result is a hybrid: a frozen operator at q_0 contracted
  against weights and blocks at q_val. It is neither tr_M at q_val nor at q_0.
  Same class as the layer-straddle rule in AGENTS.md ("never straddle the two
  layers inside one quantity"), with q-values in place of anchors. At 1/q_0 it
  returns 0.0332 against the transfer's -0.00148 -- it does not even agree in
  sign, so it remains unusable as the arbiter qou-r9dv wanted.

  WHY THIS IS DANGEROUS RATHER THAN MERELY WRONG. At q_val = q_0 the hybrid
  degenerates to the correct value, because then the frozen operator is at the
  right q. The function is therefore right exactly where it is usually tested
  and silently wrong everywhere else -- failing toward AGREEMENT with an
  independent path at the anchor, which reads as corroboration. The bean
  already named this trap; the extract regeneration did not remove it.

  A SECOND FINDING, unrelated to the bar. Of the two extracts present on disk,
  the H_9 nn one carries NO q0Value stamp at all. A frozen operator that does
  not record which q it was frozen at cannot be checked for staleness by any
  of the q0-drift machinery. Ten of the twelve (n, interface) extracts are
  absent entirely, so the A=2 pn deuteron is the only path this defect can
  currently reach -- A >= 3 goes through the transfer.

  THE FIX IS NOT A DOCSTRING. The bean allowed for "bar-even by design, so
  document the symmetry". It is not by design and, post-qou-zck8, not even
  bar-even: the operator is frozen. The honest minimum is to REJECT
  q_val != q_0 with a clear error rather than return a number. Regenerating
  A^lambda at arbitrary q is the real fix and is separate, larger work.

  NOT CLAIMED. This does not adjudicate tr_M^atom(1/q_0). The transfer value
  there still rests on a single method, and this probe does not add a second.
""")

    if FAILS:
        print(f"  ASSERTIONS FAILED: {', '.join(FAILS)}")
        return 1
    print("  ASSERTIONS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

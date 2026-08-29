#!/usr/bin/env python3
"""qbeta_d_frame_admissible_base_correction_search_probe.py — is there a
PARAMETER-FREE correction closing either convention-D admissible base? (bean
qou-cds1, the ladder/correction side; takeover of #5337's unstarted goal.)

## What is asked

Under convention D the Q_β base functional is one of exactly two admissible
choices (`ConventionDAdmissibleRoots.admissible_markov_param_iff`, Lean, roots
`{q, z_D}`; `net` at `z=1` is excluded). Measured on the NF vector (qou-99qc,
`qbeta_admissible_functionals_bracket_probe`, 15/15), both miss CODATA badly:

    augmentation (z=q) : |Q| = 0.8798905613 MeV   (+12.470 %)
    Markov trace (z_D) : |Q| = 0.4447004085 MeV   (-43.157 %)

so each needs a multiplicative correction `F_required = Q_codata / base`. #5337's
stated goal ("fold the Wenzl two-row cap into the D decay correction") reduces to:
is there a PARAMETER-FREE categorical object that supplies `F_required`, or is the
correction only reachable by a fit? The single specific candidate "F = the
two-row restriction fraction" is already pruned (`qbeta_d_frame_two_row_cap_prune_probe`,
13.6x). This probe does the systematic enumeration on BOTH bases, with the
anti-fit discipline, and diagnoses the one near-match.

## Method (anti-fit — no winner adopted)

`F_required(aug) = 0.88913`, `F_required(tr_M) = 1.75924`. Enumerate the natural
parameter-free objects in `{q, h, z_D}` and report distances. The discipline: a
match counts only if UNIQUELY singled out by a categorical principle *before*
seeing the target; a basket coincidence is a fit.

## Result

- **tr_M base: WALLED.** `F_required = 1.75924`; the closest parameter-free
  object is `q^6` at 6.3 %, `1/z_D` at 7.2 %. No parameter-free correction.

- **augmentation base: the near-match is the FORBIDDEN `z=1` return.** The tempting
  `sqrt(1−h) = 0.889348` lands 0.025 % from `F_required`. But it is a basket
  coincidence pointing in the forbidden direction: the base is `∝ tr_M(Δ_S)`
  (affine, `= h²/2 − h·z`), so the required correction is, to 0.17 % (exactly the
  net-vs-CODATA gap), the trace's OWN `z=q → z=1` ratio

      net/aug  =  tr_M(Δ_S)|_{z=1} / tr_M(Δ_S)|_{z=q}  =  (h/2 − 1)/(h/2 − q)
               =  0.8906174   (measured base ratio agrees to 1.3e-11),

  i.e. "correcting" the augmentation base back to CODATA IS the return to the
  `z=1` (net) value that convention D **excludes** (`ConventionDAdmissibleRoots.one_not_root`).
  `sqrt(1−h)` merely sits 0.025 % from `F_required` and 0.14 % from that forbidden
  ratio — a clean form near a forbidden object, not an admissible derivation.

## Verdict (scope-(a))

No parameter-free ADMISSIBLE correction closes either convention-D base; the one
sub-0.1 % near-match is the forbidden `z=1` return in disguise. The D re-derivation
does not close at the current framing (base + one multiplicative correction). This
closes #5337's stated question with a measured negative and extends the
two-row-cap prune to both bases. Nothing wired; `free_parameters = 0`;
`sqrt(1−h)` is NOT adopted.

-- Ref: QOU.QBeta.AdmissibleRoots (admissible roots {q, z_D}; z=1 excluded)
-- Ref: computations/qbeta/qbeta_d_frame_two_row_cap_prune_probe.py (single-candidate prune)
-- Ref: .beans/qou-99qc (admissible bases bracket CODATA; base values)
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP / "qbeta"), str(_COMP), str(_COMP / "substrate"),
                str(_COMP.parent / "tools" / "qou-substrate" / "python")]
import _path_bridge  # noqa: F401,E402

mp.mp.dps = 50


def main() -> int:
    from q_parameter import Q_MP  # exact mpf, proton pin
    q = mp.mpf(Q_MP)
    h = q - 1 / q
    zD = q ** 3 / (q ** 2 + 1)
    zC = mp.sqrt(q) / (q + 1)

    # Admissible base |Q| on the NF vector (qou-99qc; E0 normalization) and the
    # inadmissible coordinate-sum (net, z=1) base with its published +0.167757%.
    aug = mp.mpf("0.8798905613")
    trMzD = mp.mpf("0.4447004085")
    net = mp.mpf("0.7836458274")
    Qcod = net / (1 + mp.mpf("0.00167757"))

    Fa = Qcod / aug
    Ft = Qcod / trMzD

    # affine decay trace tr_M(Δ_S)(z) = h²/2 − h·z  (#5897); base ∝ this value
    trM = lambda z: h ** 2 / 2 - h * z
    trace_ratio = trM(1) / trM(q)          # (h/2−1)/(h/2−q), the z=q→z=1 ratio

    cands = {
        "sqrt(1-h)": mp.sqrt(1 - h), "1-h/2": 1 - h / 2, "1-h": 1 - h,
        "1/q": 1 / q, "1/q^2": 1 / q ** 2, "z_D": zD, "1/z_D": 1 / zD,
        "z_C": zC, "1/z_C": 1 / zC, "1/[2]_q": 1 / (q + 1 / q),
        "[2]_q": q + 1 / q, "q": q, "q^3": q ** 3, "q^6": q ** 6,
        "1+h": 1 + h, "1+3h/2": 1 + 3 * h / 2, "(1+h)/(1-h/2)": (1 + h) / (1 - h / 2),
        "(1-h/2)^2": (1 - h / 2) ** 2,
    }

    def closest(F):
        return sorted(((k, v, abs(v - F) / F) for k, v in cands.items()),
                      key=lambda r: r[2])

    ra, rt = closest(Fa), closest(Ft)
    print(f"q0={mp.nstr(q,12)}  h={mp.nstr(h,10)}  zD={mp.nstr(zD,10)}")
    print(f"F_required(aug)  = {mp.nstr(Fa,12)}   F_required(tr_M) = {mp.nstr(Ft,12)}")
    print("\n[augmentation base] closest parameter-free candidates:")
    for k, v, rel in ra[:4]:
        print(f"   {k:16s} = {mp.nstr(v,10):>12s}  rel={mp.nstr(rel*100,4)}%")
    print("\n[tr_M base] closest parameter-free candidates:")
    for k, v, rel in rt[:4]:
        print(f"   {k:16s} = {mp.nstr(v,10):>12s}  rel={mp.nstr(rel*100,4)}%")

    # the diagnosis of the augmentation near-match
    base_ratio = net / aug
    ratio_agree = abs(base_ratio / trace_ratio - 1)
    Fa_vs_ratio = Fa / trace_ratio - 1
    print("\n[diagnosis] augmentation correction = forbidden z=1 return:")
    print(f"   net/aug (measured base ratio) = {mp.nstr(base_ratio,12)}")
    print(f"   trace ratio (h/2-1)/(h/2-q)   = {mp.nstr(trace_ratio,12)}  agree to {mp.nstr(ratio_agree,3)}")
    print(f"   F_required(aug)/trace_ratio-1 = {mp.nstr(Fa_vs_ratio*100,4)}%  (= net-vs-CODATA gap)")

    trM_walled = rt[0][2] > mp.mpf("0.05")                 # nothing < 5%
    aug_nearmatch_is_forbidden = ratio_agree < mp.mpf("1e-9")  # base ∝ trace confirmed
    verdict = (
        "SCOPE-(a): no parameter-free ADMISSIBLE correction closes either "
        "convention-D base. tr_M base WALLED (closest %s at %s%%); augmentation "
        "near-match sqrt(1-h) (0.025%%) is the FORBIDDEN z=1 return in disguise "
        "(F_required = the trace's z=q->z=1 ratio to 0.17%%, base proportional to "
        "tr_M(Delta_S) confirmed to 1e-11). Nothing wired; sqrt(1-h) NOT adopted."
        % (rt[0][0], mp.nstr(rt[0][2] * 100, 3))
    )
    print(f"\nVERDICT: {verdict}")

    try:
        from witness_base import WitnessBuilder
    except Exception:
        print("(witness_base unavailable — printing only)")
        return 0
    w = WitnessBuilder("qbeta-d-frame-admissible-base-correction-search", engine="mpmath")
    w.set_description(
        "bean qou-cds1 ladder/correction side (takeover of #5337 unstarted goal): "
        "is there a parameter-free correction closing either convention-D admissible "
        "base? tr_M base WALLED (closest > 6%); augmentation near-match sqrt(1-h) "
        "(0.025%) DIAGNOSED as the forbidden z=1 (net) return — base is proportional "
        "to tr_M(Delta_S), so F_required = the affine trace's z=q->z=1 ratio to 0.17% "
        "(the net-vs-CODATA gap). No parameter-free ADMISSIBLE correction; nothing "
        "wired; free_parameters=0; sqrt(1-h) NOT adopted. VERDICT: " + verdict
    )
    w.set_audit_only("docs/audits/2026-08-29-cds1-admissible-base-correction-search.md")
    w.add_data("q0", mp.nstr(q, 30))
    w.add_data("F_required_augmentation", mp.nstr(Fa, 18))
    w.add_data("F_required_trM", mp.nstr(Ft, 18))
    w.add_data("trM_base_closest_name", rt[0][0])
    w.add_data("trM_base_closest_relerr", mp.nstr(rt[0][2], 10))
    w.add_data("aug_base_closest_name", ra[0][0])
    w.add_data("aug_base_closest_relerr", mp.nstr(ra[0][2], 10))
    w.add_data("trace_ratio_z_q_to_1", mp.nstr(trace_ratio, 18))
    w.add_data("base_ratio_net_over_aug", mp.nstr(base_ratio, 18))
    w.add_data("trM_base_walled", bool(trM_walled))
    w.add_data("aug_near_match_is_forbidden_z1_return", bool(aug_nearmatch_is_forbidden))
    w.add_data("free_parameters", 0)
    w.add_data("sqrt_1_minus_h_adopted", False)
    w.add_data("verdict", verdict)
    w.add_assertion("base_proportional_to_affine_trace",
                    mp.nstr(ratio_agree, 6), "0.0", tolerance="1e-9",
                    source="net/aug == (h/2-1)/(h/2-q) (base proportional to tr_M(Delta_S))")
    w.add_assertion("trM_base_no_parameter_free_correction_under_5pct",
                    1 if trM_walled else 0, 1,
                    source="closest parameter-free object to F_required(tr_M) exceeds 5%")
    out = w.save()
    print(f"witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

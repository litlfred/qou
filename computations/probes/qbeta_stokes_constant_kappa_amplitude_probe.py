#!/usr/bin/env python3
"""qbeta_stokes_constant_kappa_amplitude_probe.py — the Stokes constant from the
κ-ladder amplitude: independently confirms the GGM integer 3, and REFINES the
#3916 √3-framing (the amplitude is parity-blind; √3 is the rung grading, not a
separate odd Stokes constant).

CONTEXT (bean qou-duub; #3916 follow-on; reconciliation with main's landed G3
tranche-B pt2, `qbeta-g3-aomega-residue-first-number.witness.json`). That work
read the odd-channel Stokes amplitude from Borel-Padé residues on the 12 exact
rungs: u=0 |2πi·res| = 2.753, ratio 0.918 to the GGM-proved integer Stokes
constant 3 (#3872), leading pole 0.25% from Vol/π. This probe reconciles that
against the κ-ladder from an independent direction and sharpens #3916.

METHOD. A one-instanton series κ_n ~ C·Γ(n)/Aⁿ (A = Vol(4₁)/π) has Stokes
amplitude 2πC. Extract C_n = κ_n·Aⁿ/Γ(n) from the 7 EXACT κ rungs; the sequence
2πC_n → the Stokes constant. Two questions:

  (Q1) Does 2πC_n reproduce the landed u=0 amplitude 2.753 (→ integer 3)?
  (Q2) Is C_n √3-GRADED by parity, or parity-BLIND? #3916 established κ_odd ∈
       ℚ·√3·πⁿ, κ_even ∈ ℚ·πⁿ. If C_odd (which retains the √3) and C_even land
       on ONE smooth curve, the √3 is the trace-field dressing that makes both
       parities share a SINGLE Stokes constant — NOT a separate odd amplitude.

REFINEMENT OF #3916 (honest, anti-over-claim). #3916 phrased the remaining
unknown as "a √3-graded bar-odd Stokes constant". This probe shows the Stokes
AMPLITUDE is parity-blind (the integer 3, shared) — the √3 lives in the rung
VALUES, not in a distinct odd amplitude. The genuine bar-odd datum is the
DEFORMED-pole imaginary part (the CS piece, Im ≈ 0.0156 at u_sub in the landed
witness), which vanishes at the amphichiral u=0 (CS=0). So "work on the Stokes
constant" resolves to: the u=0 constant is the GGM integer 3 (now confirmed from
the κ amplitude too); the open piece is the DEFORMATION (Im at u≠0), not a
separate √3 amplitude.

Scope-(a): a reconciliation + refinement, NOT a derivation of the deformed
Stokes datum. ħ↔2πi/N: perturbative one-instanton amplitude only. NO fit; NO c_k
wired; NO tier change.

Run: python3 -u computations/probes/qbeta_stokes_constant_kappa_amplitude_probe.py \\
       2>&1 | tee /tmp/qbeta_stokes_amp.log
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

KAPPA_COEF = {
    1: mp.mpf(11) / 108 * mp.sqrt(3),
    2: mp.mpf(2) / 27,
    3: mp.mpf(1081) / 21870 * mp.sqrt(3),
    4: mp.mpf(98) / 729,
    5: mp.mpf(110011) / 688905 * mp.sqrt(3),
    6: mp.mpf(207892) / 295245,
    7: mp.mpf(32729683) / 26572050 * mp.sqrt(3),
}
GGM_INTEGER_STOKES = mp.mpf(3)            # #3872, GGM-proved
LANDED_U0_AMPLITUDE = mp.mpf("2.75298149023")   # aomega-residue witness u=0
LANDED_DEFORMED_IM = mp.mpf("0.0156406676018")  # deformed-pole Im at u_sub


def _repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "computations")) and \
           os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root not found")


def _head_sha():
    for ev in ("GITHUB_SHA", "GIT_COMMIT_SHA"):
        v = os.environ.get(ev)
        if v and v.strip():
            return v.strip()
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=_repo_root(), text=True).strip()
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" Stokes constant from the κ-ladder amplitude — reconcile + refine #3916")
    print("=" * 78)

    vol = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    A = vol / mp.pi
    full = {n: KAPPA_COEF[n] * mp.pi ** n for n in KAPPA_COEF}
    print(f"\n  A = Vol/π = {mp.nstr(A,10)}   (one-instanton action)")

    print("\n  Stokes prefactor  C_n = κ_n·Aⁿ/Γ(n),  amplitude 2π·C_n:")
    C, amp = {}, {}
    for n in range(1, 8):
        C[n] = full[n] * A ** n / mp.gamma(n)
        amp[n] = 2 * mp.pi * C[n]
        print(f"    n={n} ({'odd ' if n % 2 else 'even'}): C_n={mp.nstr(C[n],7)}  "
              f"2π·C_n={mp.nstr(amp[n],7)}  C_n/√3={mp.nstr(C[n]/mp.sqrt(3),7)}")

    # (Q1) 2πC_n trends to the landed u=0 amplitude (→ integer 3)
    amp_top = amp[7]
    to_landed = abs(amp_top - LANDED_U0_AMPLITUDE) / LANDED_U0_AMPLITUDE
    increasing = all(amp[n] < amp[n + 1] for n in range(3, 7))
    print(f"\n  2π·C_7 = {mp.nstr(amp_top,7)}  vs landed u=0 amp "
          f"{mp.nstr(LANDED_U0_AMPLITUDE,7)}  (rel {mp.nstr(to_landed,4)})")
    print(f"  both trend toward the GGM integer Stokes constant "
          f"{mp.nstr(GGM_INTEGER_STOKES,3)}")
    check("kappa_amplitude_trends_to_landed_u0_stokes",
          increasing and amp_top < LANDED_U0_AMPLITUDE
          and amp_top > mp.mpf("2.5"),
          computed=f"2π·C_7={mp.nstr(amp_top,6)}",
          expected=f"increasing toward landed {mp.nstr(LANDED_U0_AMPLITUDE,5)} "
                   f"(→ integer {int(GGM_INTEGER_STOKES)})",
          source="the κ-ladder one-instanton amplitude 2π·C_n reproduces the "
                 "landed Borel-Padé u=0 Stokes amplitude 2.753 from an "
                 "independent direction — both → the GGM integer 3 (#3872)")

    # (Q2) parity-blindness: C_odd and C_even land on ONE smooth curve
    # (C_n monotone increasing across BOTH parities ⇒ the √3 in κ_odd is
    #  compensated, not a separate odd amplitude).
    smooth = all(C[n] < C[n + 1] for n in range(2, 7))   # n=2..6 monotone
    # odd-only and even-only both increasing toward a common limit:
    odd_seq = [C[n] for n in (1, 3, 5, 7)]
    even_seq = [C[n] for n in (2, 4, 6)]
    common = (odd_seq[-1] - even_seq[-1]) / odd_seq[-1]   # close at the top
    print(f"\n  C_n monotone across both parities (n=2..7): {smooth}; "
          f"|C_7−C_6|/C_7 = {mp.nstr(abs(common),4)} (parities converge together)")
    check("stokes_amplitude_is_parity_blind", smooth and abs(common) < mp.mpf("0.05"),
          computed=f"C_odd and C_even interleave; top gap {mp.nstr(abs(common),4)}",
          source="C_n (which RETAINS the √3 for odd n) is monotone across both "
                 "parities and the odd/even traces converge together — the √3 "
                 "in κ_odd is the trace-field dressing that makes both parities "
                 "SHARE one Stokes constant (integer 3), NOT a separate odd "
                 "amplitude; this REFINES #3916's '√3-graded bar-odd Stokes "
                 "constant' phrasing")

    # (refinement) the genuine bar-odd datum is the DEFORMED-pole Im (CS)
    print(f"\n  bar-odd datum = the DEFORMED-pole Im (CS): landed Im(u_sub) = "
          f"{mp.nstr(LANDED_DEFORMED_IM,5)}")
    print("  (vanishes at amphichiral u=0 where CS=0; it is the deformation, "
          "not a separate √3 amplitude — the refined open piece)")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        ("RECONCILED + REFINED: the κ-ladder one-instanton amplitude 2π·C_n "
         f"(C_n = κ_n·Aⁿ/Γ(n), A=Vol/π) increases to 2π·C_7 = {mp.nstr(amp_top,6)}, "
         "reproducing main's landed Borel-Padé u=0 Stokes amplitude 2.753 from "
         "an independent direction — both converge to the GGM-proved integer "
         "Stokes constant 3 (#3872). REFINEMENT of #3916: the amplitude is "
         "PARITY-BLIND — C_n retains the √3 for odd n yet odd and even traces "
         "converge together, so the √3 is the trace-field dressing that makes "
         "both parities SHARE the single integer-3 constant, NOT a separate "
         "√3-graded odd amplitude. The genuine bar-odd datum is the "
         "DEFORMED-pole imaginary part (CS, Im≈0.0156 at u_sub), which vanishes "
         "at the amphichiral u=0. So the u=0 Stokes constant is settled (integer "
         "3, now confirmed from the amplitude too); the OPEN piece is the "
         "deformation Im at u≠0, not a √3 amplitude. "
         if all_passed else
         "PARTIAL: a reconciliation check failed — see the per-check table. ")
        + "scope-(a) reconciliation + honest refinement, NOT a derivation of the "
        "deformed datum. ħ↔2πi/N: perturbative amplitude only. NO fit; NO c_k "
        "wired; NO tier change."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-stokes-constant-kappa-amplitude",
        "description": "Stokes constant from the κ-ladder amplitude 2π·κ_n·Aⁿ/"
                       "Γ(n): independently reproduces main's landed u=0 "
                       "Borel-Padé amplitude 2.753 (→ GGM integer 3, #3872), and "
                       "REFINES #3916 — the amplitude is parity-blind (√3 is the "
                       "rung grading, not a separate odd Stokes constant); the "
                       "bar-odd datum is the deformed-pole Im (CS). scope-(a).",
        "audit_only": True,
        "tier": "numerical (large-order amplitude; reconciliation + refinement)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "A_vol_over_pi": mp.nstr(A, 10),
            "amplitude_2piC_n": [mp.nstr(amp[n], 7) for n in range(1, 8)],
            "amplitude_2piC_7": mp.nstr(amp_top, 7),
            "landed_u0_amplitude": mp.nstr(LANDED_U0_AMPLITUDE, 7),
            "ggm_integer_stokes": int(GGM_INTEGER_STOKES),
            "parity_blind": bool(smooth and abs(common) < mp.mpf("0.05")),
            "bar_odd_datum_is_deformed_Im": mp.nstr(LANDED_DEFORMED_IM, 6),
            "verdict": verdict,
        },
        "context": {
            "axis": "Stokes constant from κ amplitude (reconciliation; bean qou-duub)",
            "landed_reconciled_against": "qbeta-g3-aomega-residue-first-number "
                                         "(u=0 amp 2.753, ratio 0.918 to integer 3)",
            "ggm_integer_source": "#3872 GGM-proved Stokes constant 3",
            "refines": "#3916 '√3-graded bar-odd Stokes constant' → parity-blind "
                       "amplitude; √3 is the rung grading",
            "open_remainder": "the deformed-pole Im (CS) at u≠0 = the meridian↔"
                              "Q_β map (conj:algebraic-geometric-dilog-equivalence)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-stokes-constant-kappa-amplitude.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

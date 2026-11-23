#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical evaluation at q = q_0, not symbolic.
"""binding_sum_C_vs_D_per_isotope_probe.py — the binding sum under the
binding channel's current convention C vs the mass channel's convention D,
per isotope.

MEASUREMENT ONLY.  Nothing is tuned; no production value is changed.  The
AME2020 numbers appear as comparison targets in the OUTPUT only -- they are
never an input to any weight, coefficient or convention here.

WHAT IS MEASURED
----------------
Two sums, on the SAME canonical atomic braid word and the SAME characters,
differing ONLY in the Ocneanu parameter of the Markov trace:

  (a) trace         tr_M      = sum_lambda y_lambda * chi^lambda
  (b) binding sum   B/m_e     = |sum_lambda y_lambda * chi^lambda * Delta_lambda|

with Delta_lambda = (-1)^{n(lambda)} * f^lambda -- the PROVED per-partition
value (sorry-free, general-n,
QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional, PR #4580).

  convention C (what the binding chain runs on today):
      z_C = 1/(q^{1/2} + q^{-1/2})   -- hard-coded at
      y_lambda_wenzl_bridge.py:122,140; N_eff = 2.5995..., no integer fibre
  convention D (what the mass channel is settled on):
      z_D = q^3/(q^2+1) = q^2/[2]_q  -- N = 2, dim V = 2, the SU(2)/TL fibre

chi^lambda is convention-INDEPENDENT (it is a character of the braid word in
the Hoefsmit seminormal basis), so the C-vs-D difference is entirely in the
weight vector.  Under D, y_lambda = 0 for every lambda with ell(lambda) > 2
(proved in the sibling probe binding_channel_convention_exposure_probe.py,
C2: the bridge's (1 - X*Q^{c(x)}) factor vanishes at X = Q^N exactly on the
cell of content -N, which exists iff ell(lambda) > N).  Hence the D sums are
the TWO-ROW PARTIAL SUMS of the C sums, and the D/C ratio is exactly the
two-row share.

WHY THIS IS NOT A 195 ppm QUESTION
----------------------------------
The 1.955e-4 (195.8 ppm) D-vs-C gap on beta_Bor is the n = 3 case, where
only one partition (1^3) is affected.  Binding runs at n = 3A: the deuteron
is at n = 6 (7 of 11 blocks zeroed under D) and 4He at n = 12 (70 of 77).
def:two-row-stratum already records the consequence in prose -- "the
ell(lambda) > 2 share of the binding sum grows from ~26% at 2H to ~100% at
4He, where the two-row contribution is ~0.02% of the total" -- this probe
measures it at the proton pin with a live D weight vector.

PIN
---
EXPERIMENTAL / proton, q_parameter.Q_50_DIGIT_STR (owner directive
2026-08-07).  No muon-built cache is read: y_lambda is computed live from the
Wenzl-bridge closed form at both z values (never y_lambda_at() /
y-lambda-at-q0.witness.json), and chi^lambda is computed
live from the Hoefsmit seminormal matrices at the proton q_0 (never the
committed chi-<atom>-h<n>-at-q0-50dps.witness.json files, which carry the
MUON q_0 = 1.10997859555733471... and are marked q0Anchor: "ambiguous").

Ref: docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md
Ref: docs/audits/2026-08-08-borromean-trace-convention-forcing.md
Ref: folio/quantum-observable-universe/mass-theory/two-row-stratum.md
Ref: computations/two_row_vs_higher_row_binding_split.py (same split, muon inputs)
Ref: QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional (Delta_lambda value)
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge (substrate/ subdir)
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from y_lambda_wenzl_bridge import (  # noqa: E402
    classical_dim, partitions_of, schur_principal, n_lambda,
)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from tr_m_wenzl_bridge_mpfr import (  # noqa: E402
    _build_seminormal_matrices_mpf, _chi_lambda_of_word_mpf,
)
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)

T0 = time.time()

# CODATA / AME2020 -- OUTPUT COMPARISON TARGETS ONLY, never an input.
M_E_MEV = "0.51099895069"
AME_B_MEV = {
    "deuteron": _ame_nstr(AME_B_DEUTERON_MEV_VALIDATION, 30),
    "tritium": _ame_nstr(AME_B_TRITIUM_MEV_VALIDATION, 30),
    "helium-3": _ame_nstr(AME_B_HE3_MEV_VALIDATION, 30),
    "helium-4": _ame_nstr(AME_B_HE4_MEV_VALIDATION, 30),
}
# (Z, N) for atom_braid_word_3A; n_strands = 3*(Z+N)
ATOMS = {
    "deuteron": (1, 1),
    "tritium": (1, 2),
    "helium-3": (2, 1),
    "helium-4": (2, 2),
}


def log(msg: str) -> None:
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def q_int(q, k):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def z_C(q):
    """Convention C: the binding chain's hard-coded Ocneanu parameter."""
    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))


def z_D(q):
    """Convention D: q^2/[2]_q, the N = 2 / SU(2)-TL Ocneanu parameter."""
    return q ** 3 / (q ** 2 + 1)


def y_vector_at_z(n, q, z):
    """{lambda: y_lambda} from the Wenzl-bridge closed form at Ocneanu z.

    Identical to y_lambda_wenzl_bridge_numeric except z is a parameter
    rather than hard-coded, so both conventions come from ONE code path.
    """
    Q = q ** 2
    X = q * z / (1 - Q + q * z)
    parts = [tuple(p) for p in partitions_of(n)]
    s = {p: schur_principal(list(p), X, Q) for p in parts}
    norm = sum(classical_dim(list(p)) * s[p] for p in parts)
    return {p: s[p] / norm for p in parts}


def delta_lambda(lam):
    """Delta_lambda = (-1)^{n(lambda)} * f^lambda (PROVED value)."""
    return (-1) ** n_lambda(list(lam)) * classical_dim(list(lam))


def measure_atom(atom, q, dps, two_row_only=False):
    """chi^lambda once, then both conventions' sums off the same characters.

    `two_row_only` restricts the chi computation to ell(lambda) <= 2.  This is
    EXACT for the convention-D sums (D annihilates every >2-row weight, proved
    in the sibling probe's C2) and gives the two-row PARTIAL sum on the C side;
    the C total is then unavailable and reported as None.  It exists because
    the full n = 12 character set includes blocks of dimension up to 2673,
    while the seven two-row blocks of 12 top out at 297.
    """
    Z, N = ATOMS[atom]
    n = 3 * (Z + N)
    word = atom_braid_word_3A(Z, N)
    parts = [tuple(p) for p in partitions_of(n)]
    if two_row_only:
        parts = [p for p in parts if len(p) <= 2]
    log(f"{atom}: H_{n}, {len(parts)} partitions"
        f"{' (two-row only)' if two_row_only else ''}, {len(word)} crossings")

    # NOTE: y_vector_at_z always normalises over ALL partitions of n
    # (sum_lambda y_lambda d_lambda = 1); restricting `parts` above only
    # restricts which chi are computed, never the normalisation.
    yC = y_vector_at_z(n, q, z_C(q))
    yD = y_vector_at_z(n, q, z_D(q))

    chi = {}
    for i, lam in enumerate(parts, 1):
        sig, dim = _build_seminormal_matrices_mpf(lam, q)
        if dim == 0:
            chi[lam] = mp.mpf(0)
            continue
        chi[lam] = _chi_lambda_of_word_mpf(sig, dim, word, q=q)
        if i % 5 == 0 or i == len(parts):
            log(f"  {atom}: chi {i}/{len(parts)}  (last lam={list(lam)}, "
                f"dim={dim})")

    zero_tol = mp.mpf(10) ** (-(dps - 5))
    trC = trD = sumC = sumD = mp.mpf(0)
    two_row_sum = mp.mpf(0)
    rows = []
    for lam in parts:
        d_lam = delta_lambda(lam)
        cC, cD = yC[lam] * chi[lam], yD[lam] * chi[lam]
        trC += cC
        trD += cD
        sumC += cC * d_lam
        sumD += cD * d_lam
        if len(lam) <= 2:
            two_row_sum += cC * d_lam
        rows.append({
            "partition": list(lam), "ell": len(lam),
            "f_lambda": classical_dim(list(lam)),
            "Delta_lambda": d_lam,
            "y_C": mp.nstr(yC[lam], 20),
            "y_D": mp.nstr(yD[lam], 20),
            "y_D_is_zero": bool(abs(yD[lam]) < zero_tol),
            "chi_lambda": mp.nstr(chi[lam], 20),
            "binding_term_C": mp.nstr(cC * d_lam, 20),
        })

    # Under D the >2-row terms vanish identically, so sum_D must equal the
    # two-row partial sum of the C-weighted terms re-weighted by y_D.  The
    # check that matters is the weaker, exact one: no >2-row term survives.
    surviving_gt2 = [r["partition"] for r in rows
                     if r["ell"] > 2 and not r["y_D_is_zero"]]

    me = mp.mpf(M_E_MEV)
    ame = mp.mpf(AME_B_MEV[atom])
    B_C, B_D = me * abs(sumC), me * abs(sumD)
    out = {
        "atom": atom, "Z": Z, "N": N, "n_strands": n,
        "n_partitions": len(parts),
        "n_two_row": sum(1 for p in parts if len(p) <= 2),
        "n_zeroed_under_D": sum(1 for p in parts if len(p) > 2),
        "surviving_gt2_row_under_D": surviving_gt2,
        "tr_M_C": mp.nstr(trC, 25), "tr_M_D": mp.nstr(trD, 25),
        "tr_M_D_over_C": mp.nstr(trD / trC, 12) if trC != 0 else None,
        "binding_sum_C": mp.nstr(sumC, 25),
        "binding_sum_D": mp.nstr(sumD, 25),
        "binding_D_over_C": mp.nstr(sumD / sumC, 12) if sumC != 0 else None,
        "two_row_share_of_C_binding_sum": (
            mp.nstr(two_row_sum / sumC, 12) if sumC != 0 else None),
        "B_MeV_C": mp.nstr(B_C, 15), "B_MeV_D": mp.nstr(B_D, 15),
        "B_AME2020_MeV": AME_B_MEV[atom],
        "rel_err_C": mp.nstr((B_C - ame) / ame, 10),
        "rel_err_D": mp.nstr((B_D - ame) / ame, 10),
        "two_row_only": bool(two_row_only),
        "totals_are_two_row_partial": bool(two_row_only),
        "by_partition": rows,
    }
    log(f"  {atom}: tr_M  C={mp.nstr(trC,12)}  D={mp.nstr(trD,12)}")
    log(f"  {atom}: B/MeV C={mp.nstr(B_C,12)}  D={mp.nstr(B_D,12)}  "
        f"AME={AME_B_MEV[atom]}")
    log(f"  {atom}: rel err  C={mp.nstr((B_C-ame)/ame,6)}  "
        f"D={mp.nstr((B_D-ame)/ame,6)}   D/C(binding)="
        f"{out['binding_D_over_C']}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--atoms", default="deuteron",
                    help="comma-separated subset of "
                         "deuteron,tritium,helium-3,helium-4")
    ap.add_argument("--dps", type=int, default=50)
    ap.add_argument("--two-row-only", action="store_true",
                    help="compute chi only for ell(lambda) <= 2: EXACT for the D sums, two-row partial on the C side")
    args = ap.parse_args()

    set_compute_dps()
    mp.mp.dps = max(mp.mp.dps, args.dps + 20)
    q = mp.mpf(Q_50_DIGIT_STR)
    log(f"proton pin q_0 = {Q_50_DIGIT_STR}  (dps={mp.mp.dps})")
    log(f"z_C = {mp.nstr(z_C(q), 20)}   z_D = {mp.nstr(z_D(q), 20)}")

    wanted = [a.strip() for a in args.atoms.split(",") if a.strip()]
    results = {}
    for atom in wanted:
        if atom not in ATOMS:
            raise SystemExit(f"unknown atom {atom!r}")
        results[atom] = measure_atom(atom, q, args.dps,
                                     two_row_only=args.two_row_only)

    slug = "-".join(a[:4] for a in wanted) + \
        ("-tworow" if args.two_row_only else "")
    wb = WitnessBuilder(f"binding-sum-c-vs-d-{slug}", engine="mpmath")
    wb.add_parameter("q_0", Q_50_DIGIT_STR)
    wb.add_parameter("q_0_pin", "experimental/proton "
                                "(q_parameter.Q_50_DIGIT_STR)")
    wb.add_parameter("uses_muon_built_cache", False)
    wb.add_parameter("uses_experimental_target_values_as_input", False)
    wb.add_parameter("z_C", mp.nstr(z_C(q), 30))
    wb.add_parameter("z_D", mp.nstr(z_D(q), 30))
    wb.add_parameter("atoms", wanted)
    wb.add_parameter("two_row_only", bool(args.two_row_only))
    for atom, r in results.items():
        wb.add_data(atom, r)
        wb.add_assertion(
            f"{atom}_no_gt2_row_block_survives_under_D",
            len(r["surviving_gt2_row_under_D"]), 0,
            source="convention D annihilates every ell(lambda) > 2 "
                   "Wedderburn block, so the D binding sum is the two-row "
                   "partial sum of the C one",
        )
    wb.set_description(
        "Binding sum sum_lambda y_lambda chi^lambda Delta_lambda under the "
        "binding channel's current convention C (z = 1/(q^1/2+q^-1/2), "
        "N_eff = 2.5995) vs the mass channel's settled convention D "
        "(z = q^3/(q^2+1), N = 2), on the same canonical atomic braid and "
        "the same characters, at the EXPERIMENTAL (proton) q_0. Measurement "
        "only: no production value changed, nothing tuned, AME2020 used as "
        "an output comparison target only."
    )
    wb.set_content_block("def:two-row-stratum")
    path = wb.save()
    log(f"witness -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

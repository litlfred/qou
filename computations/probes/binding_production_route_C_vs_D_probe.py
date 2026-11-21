#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical evaluation at q = q_0, not symbolic.
"""binding_production_route_C_vs_D_probe.py — the PRODUCTION binding route
under convention C vs convention D.

MEASUREMENT ONLY.  Nothing tuned; no production value changed.  AME2020
appears as an output comparison target, never as an input.

The sibling probe `binding_sum_C_vs_D_per_isotope_probe.py` measures the
Delta_lambda route B/m_e = |sum_lambda y_lambda chi^lambda Delta_lambda|.
That is the object `def:two-row-stratum` discusses, but it is NOT what
production computes.  `binding_canonical.py:346-352` computes

    delta_tr = tr_M(W_free) - tr_M(W_atom)          (signed)
    B        = E_0 * delta_tr,   E_0 = Q_NEUTRON_MEV

with both traces in the SAME convention, i.e. both currently C (the
Wenzl-bridge y_lambda with z = 1/(q^1/2+q^-1/2), hard-coded at
y_lambda_wenzl_bridge.py:122,140).

This probe recomputes delta_tr and B under BOTH conventions, on the same two
braid words and the same characters.  chi^lambda is convention-independent,
so the entire C-vs-D difference is in the weight vector -- and under D every
weight with ell(lambda) > 2 is zero, so B_D is built from the two-row stratum
alone.

The escape hatch "binding is a ratio, so the scale cancels" does NOT apply:
delta_tr is a DIFFERENCE of two traces taken with the SAME weights, so a
common rescaling of y would cancel, but C -> D is not a rescaling -- it moves
the weights per-block (it zeroes 7 of 11 blocks at n = 6 and 70 of 77 at
n = 12).  A per-block reweighting does not cancel in a difference.

PIN: EXPERIMENTAL / proton, q_parameter.Q_50_DIGIT_STR (owner directive
2026-08-07).  y_lambda computed live from the closed form at both z; chi
computed live from the Hoefsmit seminormal matrices at the proton q_0.  No
muon-built cache is read (not y_lambda_at(), not the committed
chi-<atom>-h<n>-at-q0-50dps witnesses, which carry the MUON q_0).

Ref: computations/binding_canonical.py (the production route being measured)
Ref: docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md
Ref: folio/quantum-observable-universe/mass-theory/two-row-stratum.md
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

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import Q_NEUTRON_MEV as E_0  # noqa: E402
from y_lambda_wenzl_bridge import (  # noqa: E402
    classical_dim, partitions_of, schur_principal,
)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from tr_m_wenzl_bridge_mpfr import (  # noqa: E402
    _build_seminormal_matrices_mpf, _chi_lambda_of_word_mpf,
)
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)

T0 = time.time()

AME_B_MEV = {
    "deuteron": _ame_nstr(AME_B_DEUTERON_MEV_VALIDATION, 30), "tritium": _ame_nstr(AME_B_TRITIUM_MEV_VALIDATION, 30),
    "helium-3": _ame_nstr(AME_B_HE3_MEV_VALIDATION, 30), "helium-4": _ame_nstr(AME_B_HE4_MEV_VALIDATION, 30),
}
ATOMS = {"deuteron": (1, 1), "tritium": (1, 2),
         "helium-3": (2, 1), "helium-4": (2, 2)}


def log(msg: str) -> None:
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def z_C(q):
    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))


def z_D(q):
    return q ** 3 / (q ** 2 + 1)


def y_vector_at_z(n, q, z):
    Q = q ** 2
    X = q * z / (1 - Q + q * z)
    parts = [tuple(p) for p in partitions_of(n)]
    s = {p: schur_principal(list(p), X, Q) for p in parts}
    norm = sum(classical_dim(list(p)) * s[p] for p in parts)
    return {p: s[p] / norm for p in parts}


def chi_of_word(word, parts, q, label):
    out = {}
    for i, lam in enumerate(parts, 1):
        sig, dim = _build_seminormal_matrices_mpf(lam, q)
        out[lam] = (mp.mpf(0) if dim == 0
                    else _chi_lambda_of_word_mpf(sig, dim, word, q=q))
        if i % 10 == 0 or i == len(parts):
            log(f"    {label}: chi {i}/{len(parts)}")
    return out


def measure(atom, q, two_row_only=False):
    Z, N = ATOMS[atom]
    n = 3 * (Z + N)
    w_atom = atom_braid_word_3A(Z, N, include_inter=True)
    w_free = atom_braid_word_3A(Z, N, include_inter=False)
    parts = [tuple(p) for p in partitions_of(n)]
    if two_row_only:
        # EXACT for the D traces (D annihilates every >2-row weight); the C
        # traces then become two-row partials.  Needed at n = 12, where the
        # full character set reaches dim 2673 but the seven two-row blocks
        # of 12 stop at 297.
        parts = [p for p in parts if len(p) <= 2]
    log(f"{atom}: H_{n}, {len(parts)} partitions"
        f"{' (two-row only)' if two_row_only else ''}, "
        f"atom {len(w_atom)} / free {len(w_free)} crossings")

    yC, yD = y_vector_at_z(n, q, z_C(q)), y_vector_at_z(n, q, z_D(q))
    chi_a = chi_of_word(w_atom, parts, q, f"{atom} atom")
    chi_f = chi_of_word(w_free, parts, q, f"{atom} free")

    def tr(y, chi):
        return sum(y[l] * chi[l] for l in parts)

    def tr_two_row(y, chi):
        return sum(y[l] * chi[l] for l in parts if len(l) <= 2)

    trA_C, trF_C = tr(yC, chi_a), tr(yC, chi_f)
    trA_D, trF_D = tr(yD, chi_a), tr(yD, chi_f)
    dt_C, dt_D = trF_C - trA_C, trF_D - trA_D
    e0 = mp.mpf(str(E_0))
    B_C, B_D = e0 * dt_C, e0 * dt_D
    ame = mp.mpf(AME_B_MEV[atom])

    out = {
        "atom": atom, "Z": Z, "N": N, "n_strands": n,
        "n_partitions": len(parts),
        "n_zeroed_under_D": sum(1 for p in parts if len(p) > 2),
        "two_row_only": bool(two_row_only),
        "C_values_are_two_row_partial": bool(two_row_only),
        "E_0_MeV": str(E_0),
        "tr_M_atom_C": mp.nstr(trA_C, 25),
        "tr_M_free_C": mp.nstr(trF_C, 25),
        "tr_M_atom_D": mp.nstr(trA_D, 25),
        "tr_M_free_D": mp.nstr(trF_D, 25),
        "delta_tr_C": mp.nstr(dt_C, 25),
        "delta_tr_D": mp.nstr(dt_D, 25),
        "delta_tr_D_over_C": mp.nstr(dt_D / dt_C, 12) if dt_C != 0 else None,
        "B_MeV_C": mp.nstr(B_C, 15),
        "B_MeV_D": mp.nstr(B_D, 15),
        "B_AME2020_MeV": AME_B_MEV[atom],
        "rel_err_C": mp.nstr((B_C - ame) / ame, 10),
        "rel_err_D": mp.nstr((B_D - ame) / ame, 10),
        # how much of the C-convention delta_tr the two-row stratum carries
        "two_row_share_of_delta_tr_C": mp.nstr(
            (tr_two_row(yC, chi_f) - tr_two_row(yC, chi_a)) / dt_C, 12)
        if dt_C != 0 else None,
    }
    log(f"  {atom}: delta_tr C={mp.nstr(dt_C,12)}  D={mp.nstr(dt_D,12)}  "
        f"D/C={out['delta_tr_D_over_C']}")
    log(f"  {atom}: B/MeV   C={mp.nstr(B_C,12)}  D={mp.nstr(B_D,12)}  "
        f"AME={AME_B_MEV[atom]}")
    log(f"  {atom}: rel err C={mp.nstr((B_C-ame)/ame,6)}  "
        f"D={mp.nstr((B_D-ame)/ame,6)}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--atoms", default="deuteron")
    ap.add_argument("--two-row-only", action="store_true")
    args = ap.parse_args()
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    log(f"proton pin q_0 = {Q_50_DIGIT_STR}  (dps={mp.mp.dps})")
    log(f"E_0 = {E_0} MeV (experimental_constants.Q_NEUTRON_MEV)")

    wanted = [a.strip() for a in args.atoms.split(",") if a.strip()]
    results = {a: measure(a, q, two_row_only=args.two_row_only)
               for a in wanted}

    slug = "-".join(a[:4] for a in wanted) + \
        ("-tworow" if args.two_row_only else "")
    wb = WitnessBuilder(f"binding-production-route-c-vs-d-{slug}",
                        engine="mpmath")
    wb.add_parameter("q_0", Q_50_DIGIT_STR)
    wb.add_parameter("q_0_pin", "experimental/proton "
                                "(q_parameter.Q_50_DIGIT_STR)")
    wb.add_parameter("uses_muon_built_cache", False)
    wb.add_parameter("uses_experimental_target_values_as_input", False)
    wb.add_parameter("z_C", mp.nstr(z_C(q), 30))
    wb.add_parameter("z_D", mp.nstr(z_D(q), 30))
    for atom, r in results.items():
        wb.add_data(atom, r)
        # A convention change is not a common rescaling: assert the
        # production delta_tr actually MOVES (this is the measurement).
        wb.add_assertion(
            f"{atom}_delta_tr_changes_under_D",
            1 if abs(mp.mpf(r["delta_tr_D_over_C"]) - 1) > mp.mpf("1e-6")
            else 0, 1,
            source="the C->D change is a per-block reweighting, not a "
                   "common scale, so it does not cancel in the trace "
                   "difference that production uses",
        )
    wb.set_description(
        "PRODUCTION binding route (delta_tr = tr_M(free) - tr_M(atom), "
        "B = E_0 * delta_tr, per binding_canonical.py) evaluated under the "
        "binding channel's current convention C and under the mass "
        "channel's settled convention D, at the EXPERIMENTAL (proton) q_0. "
        "Measurement only."
    )
    wb.set_content_block("prop:h3-markov-wenzl-weights")
    log(f"witness -> {wb.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

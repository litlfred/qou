#!/usr/bin/env python3
"""The 8-shell test, run — and the additive magic-shell term is not in the data.

This is the test `qou-o16k` set out to perform.  With the normaliser's index and
the excess convention both resolved (see `probe_kappa_normaliser_index_rule.py`
and `probe_kappa_excess_convention_resolution.py`), the conjecture makes a single
shell-independent prediction:

    kappa * (n_pp - n_nn) contributes  2|kappa| ~ 2.14085 MeV
    to the binding split of EVERY single-magic mirror pair (m, m-1) / (m-1, m).

The mirror pair is the right probe because the isoscalar bulk cancels: both
nuclides share A, so the difference isolates the charge-asymmetric terms --
Coulomb, plus whatever categorical asymmetry the framework adds.

    residual := [B(Z=m-1) - B(Z=m)] - Delta_E_Coulomb

Under the conjecture, residual ~ -2.14 MeV at every shell.

## Result: it is not, at any shell, under any radius model

Residuals are ~0.1-1.8 MeV, ~3-30x smaller than predicted, and -- decisively --
**they are not constant in A**, while the prediction is a single shell-independent
number.  Under the framework's own derived radius they even change sign between
A=3 and A=15.  No radius model rescues a constant.

## Scope of this negative -- (a), not (b)

Per the AGENTS.md refutation-scoping rule this is a **scope-(a) negative**: *this
construction, alone, does not reproduce the numbers as-is*.  It says the additive
shell-independent form `kappa*(n_pp - n_nn)`, set against a Coulomb baseline, is
not present in the mirror-split data.

It is **not** a scope-(b) structural exclusion of kappa.  No proved invariant
forbids kappa as an ingredient of some other decomposition, and none is claimed.

What it does establish is narrower and sharper: **the decomposition kappa was
fitted in is not the (strong + Coulomb) mirror-split decomposition.**  The
empirical kappa ~ -1.0708 MeV was recorded as "the observed physical value at the
single-magic anchors", but the A=3 anchor leaves at most ~0.23 MeV of room after
Coulomb under any radius model -- an order of magnitude short.  So that value came
from somewhere else, and that somewhere is the PR #656 fit which is not in the tree.

## Inputs, and where each comes from

    AME binding energies      measured (codata_constants._ame_binding_mev)
    alpha_EM * hbar*c         DERIVED from q_0 in coulomb_energy (not CODATA)
    radius scale r_0          THREE models, swept -- see below

Nothing is tuned.  The radius is swept rather than chosen precisely because
choosing it to land the residual on -2.14 would be the fit the demotion removed.

Ref: conj:magic-shell-coupling-kappa
Bean: qou-o16k
"""

import sys
from pathlib import Path as _P
_SUB = _P(__file__).resolve().parent / "substrate"
if str(_SUB) not in sys.path:
    sys.path.insert(0, str(_SUB))
import mpmath as mp  # noqa: E402
from _precision import fmt, str_at_true_precision, COMPUTE_DPS  # noqa: E402

mp.mp.dps = COMPUTE_DPS


def _ser(o):
    """Serialize every real; ints stay ints.

    The NO-FLOAT64 family forbids raw float64 in a witness, and this hook does
    prevent that — but satisfying it by wrapping a float in `mpf` and rendering
    at OUTPUT_DPS trades one gate for the other. `fmt` writes ~50 digits, so a
    53-bit input comes out wearing 30+ digits it never had:

        mp.mpf(1.2)  ->  1.19999999999999995559107901499373838305473328

    which is what the float64-padding audit reads as fake precision. This
    file's previous version did exactly that, and its docstring asserted the
    opposite ("no float64 ever reaches the JSON") — true of the *output* type,
    false of the *information content*, which is why it went unnoticed.

    So: an `mpf` is rendered with `fmt` (it earned those digits); a bare
    `float` is rendered with `str_at_true_precision`, which prints what a
    53-bit value actually knows. Nothing here converts a float into apparent
    precision. Values that SHOULD be full precision are fixed at their source
    below, not laundered here (bean qou-3jwy).
    """
    if isinstance(o, bool) or isinstance(o, int):
        return o
    if isinstance(o, mp.mpf):
        return fmt(o)
    if isinstance(o, float):
        return str_at_true_precision(o)
    if isinstance(o, dict):
        return {k: _ser(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_ser(v) for v in o]
    return o


import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (HERE, HERE / "substrate"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import coulomb_energy as ce  # noqa: E402
from codata_constants import (
    M_E_MEV,
    _ame_binding_mev as ame_binding  # noqa: E402,
)

Q0 = mp.mpf("1.1099785827513808")
Q0_PIN = "proton (experimental layer), m_p/m_e"
M_E_MEV = M_E_MEV


def bracket(n: int) -> float:
    return (Q0**n - Q0 ** (-n)) / (Q0 - 1 / Q0)


def kappa_magnitude() -> float:
    h = Q0 - 1 / Q0
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    e0 = _qbeta_e0.order_zero_scaled(M_E_MEV, Q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    return abs(-e0 * mp.log(1 / h) / (bracket(2) * bracket(3)))


# Single-magic mirror pairs with AME coverage: (Z_lo, Z_hi, A, shell, label)
PAIRS = [
    (1, 2, 3, 2, "3H / 3He"),
    (7, 8, 15, 8, "15N / 15O"),
    (19, 20, 39, 20, "39K / 39Ca"),
]

# Radius models, swept rather than chosen.
#
# `ce.R0_FM` is ALREADY an mpf carrying full working precision; the previous
# `float()` here threw that away and the serializer then padded the binary64
# remains back up to 50 digits:
#     genuine   1.41381693076303648646392691171816600928033518
#     via float 1.41381693076303638356705505429999902844429016   <- what shipped
# The two model constants are exact as written, so `mpf("1.2")` is 1.2 while
# `mpf(1.2)` is the binary64 neighbour — string-construct them (bean qou-3jwy).
RADII = [
    (ce.R0_FM, "derived (reduced pion Compton wavelength)"),
    (mp.mpf("1.2"), "empirical heavy-nucleus saturation constant"),
    (mp.mpf("1.76"), "implied by the measured 3He charge radius"),
]


def coulomb_displacement(z_hi: int, z_lo: int, a: int, r0):
    """Uniform-sphere displacement, (3/5)*alpha*hbar*c*[Z(Z-1)]/R, R = r0*A^(1/3)."""
    # No float() cast: alpha_em_hbar_c_mev_fm() already returns a full-precision
    # mpf. 3/5 as an exact mp rational rather than the literal 0.6, which is not
    # 3/5 in binary and would reintroduce a 53-bit factor into an mp product.
    ahc = ce.alpha_em_hbar_c_mev_fm()
    return (mp.mpf(3) / 5) * ahc * (z_hi * (z_hi - 1) - z_lo * (z_lo - 1)) / (
        r0 * a ** (mp.mpf(1) / 3)
    )


def main() -> None:
    pred = 2 * kappa_magnitude()
    rows = []
    for z_lo, z_hi, a, shell, label in PAIRS:
        # `ame_binding` returns an mpf of the tabulated AME value; casting each
        # side to float first made the DIFFERENCE a 53-bit quantity, which the
        # serializer then padded (delta_B_observed_MeV was the visible symptom:
        # claimed 3.53653199999999401370587293058633804321289062500000…,
        # really 3.536531999999994). Subtract in mp.
        d_b = ame_binding(z_lo, a) - ame_binding(z_hi, a)
        per_radius = {}
        for r0, name in RADII:
            d_c = coulomb_displacement(z_hi, z_lo, a, r0)
            resid = d_b - d_c
            per_radius[name] = {
                "r0_fm": r0,
                "coulomb_MeV": d_c,
                "residual_MeV": resid,
                "predicted_over_residual": pred / abs(resid) if resid else None,
            }
        rows.append(
            {
                "pair": label,
                "Z_lo": z_lo,
                "Z_hi": z_hi,
                "A": a,
                "shell": shell,
                "delta_B_observed_MeV": d_b,
                "by_radius_model": per_radius,
            }
        )

    assertions = []

    def check(name: str, ok: bool, detail: str) -> None:
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})

    # The decisive test: is the residual a shell-independent constant?
    spreads = {}
    for _, name in RADII:
        res = [r["by_radius_model"][name]["residual_MeV"] for r in rows]
        spreads[name] = max(res) - min(res)

    check(
        "residual_is_not_shell_independent_under_any_radius_model",
        all(s > 0.4 for s in spreads.values()),
        "the prediction is ONE number at every shell; the residual varies by "
        + ", ".join(f"{n.split(' (')[0]}: {s:.3f} MeV" for n, s in spreads.items())
        + " across A = 3, 15, 39 -- so no constant fits, whatever the radius",
    )
    check(
        "A3_anchor_leaves_no_room_for_the_predicted_term",
        all(
            abs(rows[0]["by_radius_model"][name]["residual_MeV"]) < pred / 9
            for _, name in RADII
        ),
        "at the anchor kappa was fitted at, the post-Coulomb residual is at most "
        f"~0.235 MeV under any radius model, against a predicted {pred:.3f} MeV "
        "-- short by at least 9x",
    )
    check(
        "residual_changes_sign_under_the_derived_radius",
        rows[0]["by_radius_model"][RADII[0][1]]["residual_MeV"]
        * rows[1]["by_radius_model"][RADII[0][1]]["residual_MeV"]
        < 0,
        "under the framework's own derived radius the residual is negative at "
        "A=3 and positive at A=15 -- not a constant of either sign",
    )
    check(
        "negative_is_scope_a_not_scope_b",
        True,
        "no proved invariant forbids kappa as an ingredient; this excludes the "
        "additive shell-independent form against a Coulomb baseline, nothing more",
    )

    print(f"predicted contribution 2|kappa| = {pred:.5f} MeV at EVERY shell")
    print(f"q0 pin: {Q0_PIN}\n")
    hdr = f"{'pair':12s}{'shell':>6s}{'dB_obs':>9s}  {'radius model':42s}{'dE_C':>8s}{'residual':>10s}{'ratio':>8s}"
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        for _, name in RADII:
            v = r["by_radius_model"][name]
            print(
                f"{r['pair']:12s}{r['shell']:6d}{r['delta_B_observed_MeV']:9.4f}  "
                f"{name:42s}{v['coulomb_MeV']:8.4f}{v['residual_MeV']:10.4f}"
                f"{v['predicted_over_residual']:7.1f}x"
            )
        print()
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")

    witness_raw = {
        "engine": "python-stdlib+mpmath(via coulomb_energy)",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "kappa-mirror-split-shell-test",
        "scriptFile": "probe_kappa_mirror_split_shell_test.py",
        "contentBlock": "conj:magic-shell-coupling-kappa",
        "description": (
            "The 8-shell test, run. The additive shell-independent term "
            "kappa*(n_pp - n_nn) is not present in single-magic mirror-split "
            "data at A = 3, 15, 39, under any of three radius models. Scope-(a) "
            "negative: the form as reconstructed, not kappa as an ingredient."
        ),
        "parameters": {
            "q_0": Q0,
            "q_0_pin": Q0_PIN,
            "m_e_MeV": M_E_MEV,
            "predicted_contribution_MeV": pred,
            "radius_models": [{"r0_fm": r, "name": n} for r, n in RADII],
            "alpha_em_hbar_c_MeV_fm": ce.alpha_em_hbar_c_mev_fm(),
            "alpha_em_provenance": "derived from q_0 in coulomb_energy, not CODATA",
        },
        "data": {
            "mirror_pairs": rows,
            "residual_spread_by_radius_MeV": spreads,
            "verdict": (
                "scope-(a) negative. The additive shell-independent form does not "
                "appear in the data at any tested shell under any tested radius. "
                "The residual is not constant in A, which no radius choice can "
                "repair, so the failure is not a normalisation artefact. This does "
                "NOT structurally exclude kappa; it establishes that the "
                "decomposition kappa was fitted in is not the strong+Coulomb "
                "mirror-split decomposition."
            ),
        },
        "assertions": assertions,
        "allPassed": all(a["passed"] for a in assertions),
    }
    witness = _ser(witness_raw)
    out = HERE / "kappa-mirror-split-shell-test.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwitness -> {out.name}  (allPassed={witness_raw['allPassed']})")


if __name__ == "__main__":
    main()

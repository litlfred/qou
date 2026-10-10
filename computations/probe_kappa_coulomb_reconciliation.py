#!/usr/bin/env python3
"""The two discordant anchors reconcile — and what reconciles them is Coulomb,
not a categorical excess coupling.

`probe_kappa_provenance.py` established that the published kappa is the 3He arm
of a two-anchor fit whose own witness recorded `hypothesis_supported: false`: the
anchors gave slopes of opposite sign, -1.0708 MeV (3He) and +0.2023 MeV (T).

This probe asks the obvious next question. The two anchors differ by exactly one
thing besides the excess sign: 3He has a pp pair and T does not, so 3He carries a
Coulomb energy that T does not. What happens to the discord if that is removed?

## It disappears — and takes kappa with it

The model under test is

    residual := Delta_coupling - H7a_prediction  =  (n_pp - n_nn) * kappa * h * E_0

so a term proportional to the excess MUST FLIP SIGN between the two anchors,
whose excesses are +1 and -1.

Restoring the Coulomb energy to the 3He arm (T needs no correction -- no pp
pair), using the framework's own module with alpha_EM derived from q_0:

    r_0 model                        3He residual   T residual
    derived (lambda-bar_pi)             -0.2234       -0.2023
    empirical 1.2 fm                    -0.0724       -0.2023
    implied by measured 3He radius      -0.3901       -0.2023

**Same sign, comparable magnitude, under every radius model** -- despite opposite
excess. An excess-proportional term cannot do that. What survives Coulomb removal
is an excess-INDEPENDENT offset of order -0.2 MeV, which is a baseline the H7a
form misses, not a coupling to the p/n asymmetry.

Under the derived radius the two agree to 0.021 MeV -- essentially the 4He
residual of 0.0223 MeV, measured at the anchor where the excess vanishes
identically and so where no kappa term exists by construction. That is the noise
floor of the H7a form itself.

## What this resolves

The published kappa ~ -1.0708 MeV was **un-subtracted Coulomb**. Reading it as a
categorical excess coupling attributed an electrostatic effect to the p/n
interface asymmetry, which is why the 3He arm was large and negative while the T
arm -- Coulomb-free -- was small and positive.

This closes the loop on the two earlier negatives, and explains both:

  * `probe_kappa_mirror_split_shell_test.py` found no room for the additive term
    in binding data. There is none, because the coefficient is zero.
  * `probe_kappa_provenance.py` found the fit self-refuted. It was self-refuted
    because it was fitting Coulomb with a categorical form.

## Scope: still (a), and now with a diagnosis

Scope-(a): this construction does not carry the effect attributed to it. The
effect is Coulomb. No claim is made that a p/n interface coupling is structurally
forbidden -- only that the A=3 anchors do not evidence one, and that what was
measured there is electrostatic.

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

    The claim this docstring used to make — "no float64 ever reaches the JSON" —
    was true of the output TYPE and false of its information content, which is
    why the padding went unnoticed. An `mpf` is rendered with `fmt` because it
    earned those digits; a bare `float` is rendered with `str_at_true_precision`
    because it did not. Values that should be full precision are fixed at their
    source below rather than laundered here (bean qou-3jwy).
    """
    if isinstance(o, bool) or isinstance(o, int):
        return o
    if isinstance(o, mp.mpf):
        return fmt(o)
    if isinstance(o, float):
        # NOT fmt(mp.mpf(o)): that renders a 53-bit value at OUTPUT_DPS and
        # emits 30+ digits it never had, which trades the raw-float64 gate for
        # the padding gate (bean qou-3jwy).
        return str_at_true_precision(o)
    if isinstance(o, dict):
        return {k: _ser(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_ser(v) for v in o]
    return o


import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (HERE, HERE / "substrate"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import coulomb_energy as ce  # noqa: E402

SOURCE = HERE.parent / "fsh-guts" / "deprecated" / "computations" / "interface-type-resolved-coupling-probe.witness.json"
KAPPA_PUBLISHED = -mp.mpf("1.0707907503265857")

# `ce.R0_FM` and `alpha_em_hbar_c_mev_fm()` are already full-precision mpf; the
# float() casts threw that away and the serializer padded the binary64 remains
# back to 50 digits. The two model constants are exact as written, so
# string-construct them — mpf(1.2) is the binary64 neighbour, mpf("1.2") is 1.2
# (bean qou-3jwy).
RADII = [
    (ce.R0_FM, "derived (reduced pion Compton wavelength)"),
    (mp.mpf("1.2"), "empirical heavy-nucleus saturation constant"),
    (mp.mpf("1.76"), "implied by the measured 3He charge radius"),
]


def coulomb_A3(r0):
    """Coulomb energy of the single pp pair in 3He; T has none."""
    # 3/5 as an exact mp rational, not the literal 0.6 (not 3/5 in binary).
    ahc = ce.alpha_em_hbar_c_mev_fm()
    return (mp.mpf(3) / 5) * ahc * (2 * 1) / (r0 * 3 ** (mp.mpf(1) / 3))


def main() -> None:
    src = json.loads(SOURCE.read_text())
    anchors = {a["label"]: a for a in src["data"]["anchors"]}
    he3, t, he4 = anchors["³He"], anchors["T"], anchors["⁴He"]

    rows = []
    for r0, name in RADII:
        r3 = he3["H7a_residual_MeV"] + coulomb_A3(r0)
        rt = t["H7a_residual_MeV"]
        rows.append(
            {
                "r0_fm": r0,
                "radius_model": name,
                "coulomb_MeV": coulomb_A3(r0),
                "he3_residual_corrected_MeV": r3,
                "t_residual_MeV": rt,
                "same_sign": r3 * rt > 0,
                "gap_MeV": abs(r3 - rt),
            }
        )

    assertions = []

    def check(name: str, ok: bool, detail: str) -> None:
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})

    check(
        "corrected_residuals_share_a_sign_under_every_radius_model",
        all(r["same_sign"] for r in rows),
        "the anchors carry excess +1 and -1; an excess-proportional term must "
        "flip sign between them. After Coulomb removal both residuals are "
        "negative under all three radius models, so the surviving quantity is "
        "not proportional to the excess",
    )
    check(
        "derived_radius_reconciles_the_anchors_to_the_4He_noise_floor",
        abs(rows[0]["gap_MeV"]) < 1.5 * abs(he4["H7a_residual_MeV"]),
        f"gap {rows[0]['gap_MeV']:.4f} MeV vs the 4He residual "
        f"{abs(he4['H7a_residual_MeV']):.4f} MeV, measured where the excess "
        "vanishes identically and no kappa term exists by construction",
    )
    check(
        "surviving_offset_is_far_smaller_than_the_published_kappa",
        all(abs(r["he3_residual_corrected_MeV"]) < abs(KAPPA_PUBLISHED) / 2.5 for r in rows),
        f"published |kappa| = {abs(KAPPA_PUBLISHED):.4f} MeV; the corrected 3He "
        "residual is 0.07-0.39 MeV, 3-15x smaller, under every radius model",
    )
    check(
        "the_3He_arm_was_dominated_by_coulomb",
        abs(coulomb_A3(ce.R0_FM)) > 0.6 * abs(KAPPA_PUBLISHED),
        f"the derived Coulomb energy {coulomb_A3(ce.R0_FM):.4f} MeV is "
        f"{100 * coulomb_A3(ce.R0_FM) / abs(KAPPA_PUBLISHED):.0f}% of the "
        "published kappa -- the fitted 'coupling' is mostly electrostatics",
    )

    print("residual := Delta_coupling - H7a_prediction;  model: residual = excess * kappa\n")
    print(f"  3He excess = {he3['iface_excess_pp_minus_nn']:+d}   T excess = {t['iface_excess_pp_minus_nn']:+d}")
    print(f"  published kappa = {KAPPA_PUBLISHED:.6f} MeV (the 3He arm)\n")
    hdr = f"{'radius model':44s}{'E_Coul':>9s}{'3He resid':>11s}{'T resid':>10s}{'same sign':>11s}"
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        print(
            f"{r['radius_model']:44s}{r['coulomb_MeV']:9.4f}"
            f"{r['he3_residual_corrected_MeV']:11.4f}{r['t_residual_MeV']:10.4f}"
            f"{str(r['same_sign']):>11s}"
        )
    print(f"\n  4He residual (excess = 0, no kappa term by construction): "
          f"{he4['H7a_residual_MeV']:+.4f} MeV")
    print()
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")

    witness_raw = {
        "engine": "python-stdlib+mpmath(via coulomb_energy)",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "kappa-coulomb-reconciliation",
        "scriptFile": "probe_kappa_coulomb_reconciliation.py",
        "contentBlock": "conj:magic-shell-coupling-kappa",
        "description": (
            "The two discordant anchors of the original kappa fit reconcile once "
            "the Coulomb energy of 3He's pp pair is restored. What survives is an "
            "excess-INDEPENDENT offset of order 0.2 MeV, same sign at both "
            "anchors despite opposite excess, so it cannot be an "
            "excess-proportional coupling. The published kappa was un-subtracted "
            "Coulomb."
        ),
        "parameters": {
            "published_kappa_MeV": KAPPA_PUBLISHED,
            "alpha_em_hbar_c_MeV_fm": ce.alpha_em_hbar_c_mev_fm(),
            "alpha_em_provenance": "derived from q_0 in coulomb_energy, not CODATA",
            "radius_models": [{"r0_fm": r, "name": n} for r, n in RADII],
            "source_witness": str(SOURCE.relative_to(HERE.parent)),
        },
        "data": {
            "by_radius_model": rows,
            "he4_residual_MeV": he4["H7a_residual_MeV"],
            "finding": (
                "The published kappa ~ -1.0708 MeV was un-subtracted Coulomb. "
                "Removing it leaves an excess-independent offset that cannot be a "
                "coupling to the p/n asymmetry, and that is 3-15x smaller than the "
                "published value. This diagnoses both earlier negatives: the "
                "mirror-split test found no room because the coefficient is zero, "
                "and the original fit refuted itself because it was fitting "
                "electrostatics with a categorical form."
            ),
        },
        "assertions": assertions,
        "allPassed": all(a["passed"] for a in assertions),
    }
    witness = _ser(witness_raw)
    out = HERE / "kappa-coulomb-reconciliation.witness.json"
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

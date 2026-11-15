#!/usr/bin/env python3
"""Where kappa ~ -1.0708 MeV actually came from — and what the probe that
produced it concluded.

`qou-o16k` recorded the empirical kappa as tracing to a "PR #656 v6 single-magic
anchor fit" that was "not in the tree in any form".  That was wrong: the fit
survives, under `fsh-guts/deprecated/computations/`, in
`interface-type-resolved-coupling-probe.witness.json`.  Reading it settles the
provenance question and turns up something sharper than a missing record.

## The decomposition kappa was fitted in

    Delta_coupling(Z,N) ~ [A-2]_q * E_0 * log(1/h)
                          + (n_pp - n_nn) * kappa * h * E_0

Two things follow immediately, both bearing on how the content block states it:

1.  The fit was to **Delta_coupling**, not to binding energy.  The block's `.md`
    describes kappa as controlling "the (n_pp - n_nn) excess contribution to
    ATOMIC BINDING".  Those are not the same observable.
2.  kappa there is **dimensionless**, in units of `h * E_0`; the MeV figure is
    the derived per-excess slope.

## What the probe concluded: hypothesis_supported = FALSE

The hypothesis needs ONE kappa across the anchors.  The probe's own stated
criterion: "If 3He and T give the same kappa to <= 5% AND 4He has residual
<= 5% of base, the hypothesis is supported."

    3He  slope = -1.0707907503265857 MeV   (-1.2235895570703044 in h*E_0)
    T    slope = +0.2023094733886944 MeV   (+0.2311784621405252 in h*E_0)

The two single-magic anchors disagree **in sign**, and by a factor of ~5.3.  The
witness records `slope_consistent_to_5pct: false` and
`hypothesis_supported: false`.

**kappa ~ -1.0708 is the 3He arm alone.**  The T arm, which is positive, was not
carried forward.

## Why this matters

The content block reports kappa as "the observed physical value at the
single-magic anchors" -- plural.  The anchors do not agree; one of them was kept.
So the conjecture's 0.034 % agreement is between a categorical closed form and
one arm of a two-arm measurement that the producing probe itself declared
inconsistent.

That is a stronger statement than "unrecorded provenance", and it is independent
of `probe_kappa_mirror_split_shell_test.py`: that probe found no room for the
additive term in binding data; this one finds that the fit was self-refuted
before binding data entered the picture.

## Bonus: C1 is confirmed independently

`canonical-braid-interface-composition.witness.json` sweeps the interface
composition using `n_pp = max(0, Z-1)`, `n_nn = max(0, N-1)` -- convention **C1**.
That is the same convention `probe_kappa_excess_convention_resolution.py` selected
on corpus-structure grounds, reached here by a different route.

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

    This probe reads values out of a deprecated witness where they were stored
    as raw float64 — so they ARE 53-bit, and the old docstring said as much
    before concluding that lifting them to `mpf` made them safe. It removed the
    float64 TYPE and kept the float64 information, then `fmt` printed the
    result at OUTPUT_DPS:

        published_kappa_MeV
          claims -1.0707907503265856608010153649956919252872467041015…
          really -1.0707907503265857

    An `mpf` computed here is rendered with `fmt`; a value that arrived as a
    float is rendered with `str_at_true_precision`, which prints what 53 bits
    actually determine. These particular values cannot be fixed at the source —
    the source is a committed deprecated witness — so honest rendering is the
    whole fix (bean qou-3jwy).
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
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEP = HERE.parent / "fsh-guts" / "deprecated" / "computations"

COUPLING = DEP / "interface-type-resolved-coupling-probe.witness.json"
COMPOSITION = DEP / "canonical-braid-interface-composition.witness.json"

# Deliberately a float64: the assertion below is that the published value equals
# the 3He arm BIT-FOR-BIT as recorded in the source witness, which is a claim
# about float64 identity. Lifting it to mpf via a decimal string would change
# the value and break a true assertion. Serialization still goes through
# _precision.fmt, so no float64 reaches the emitted witness.
KAPPA_AS_PUBLISHED = -1.0707907503265857


def main() -> None:
    cw = json.loads(COUPLING.read_text())
    anchors = {a["label"]: a for a in cw["data"]["anchors"]}
    verdict = cw["data"]["verdict"]

    he3 = anchors["³He"]
    t = anchors["T"]
    he4 = anchors["⁴He"]

    assertions = []

    def check(name: str, ok: bool, detail: str) -> None:
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})

    check(
        "published_kappa_is_the_3He_arm_alone",
        he3["slope_per_excess_unit_MeV"] == KAPPA_AS_PUBLISHED,
        "the value the content block carries is exactly the 3He anchor's slope, "
        "to the last bit -- not a combination of the two single-magic anchors",
    )
    check(
        "the_two_single_magic_anchors_disagree_in_sign",
        he3["slope_per_excess_unit_MeV"] * t["slope_per_excess_unit_MeV"] < 0,
        f"3He gives {he3['slope_per_excess_unit_MeV']:.6f} MeV, "
        f"T gives {t['slope_per_excess_unit_MeV']:+.6f} MeV -- opposite signs, "
        f"ratio {abs(he3['slope_per_excess_unit_MeV'] / t['slope_per_excess_unit_MeV']):.1f}x",
    )
    check(
        "the_producing_probe_recorded_its_hypothesis_as_unsupported",
        verdict.get("hypothesis_supported") is False
        and verdict.get("slope_consistent_to_5pct") is False,
        "the witness carries hypothesis_supported=false and "
        "slope_consistent_to_5pct=false -- the fit refuted itself at the time",
    )
    check(
        "the_fit_was_to_delta_coupling_not_to_binding",
        "Delta_coupling" in cw["description"] or "Δ_coupling" in cw["description"],
        "the probe's hypothesis is about Delta_coupling; the content block "
        "describes kappa as an atomic-BINDING coefficient -- different observables",
    )

    # C1 corroboration from the composition sweep.
    comp = json.loads(COMPOSITION.read_text())
    rows = comp["data"]["sweep_table"]
    c1_ok = all(
        r["interface_composition"]["n_pp"] == max(0, r["Z"] - 1)
        and r["interface_composition"]["n_nn"] == max(0, r["N"] - 1)
        for r in rows
    )
    check(
        "composition_sweep_uses_convention_C1",
        c1_ok,
        "n_pp = max(0, Z-1) and n_nn = max(0, N-1) hold on every swept row -- "
        "the same convention selected on corpus-structure grounds elsewhere",
    )

    print("Provenance of the published kappa\n")
    print(f"  published value           {KAPPA_AS_PUBLISHED:.16f} MeV")
    print(f"  3He anchor slope          {he3['slope_per_excess_unit_MeV']:.16f} MeV")
    print(f"  T   anchor slope          {t['slope_per_excess_unit_MeV']:+.16f} MeV")
    print(f"  4He residual              {he4['H7a_residual_MeV']:+.6f} MeV (excess = 0)")
    print()
    print(f"  slope_consistent_to_5pct  {verdict.get('slope_consistent_to_5pct')}")
    print(f"  hypothesis_supported      {verdict.get('hypothesis_supported')}")
    print()
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")

    witness_raw = {
        "engine": "python-stdlib",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "kappa-provenance",
        "scriptFile": "probe_kappa_provenance.py",
        "contentBlock": "conj:magic-shell-coupling-kappa",
        "description": (
            "Locates the fit that produced the published kappa. It survives under "
            "fsh-guts/deprecated/computations/. The published value is the 3He arm alone; "
            "the T arm has the opposite sign; and the producing witness records "
            "hypothesis_supported=false. The fit was to Delta_coupling, not to "
            "binding energy as the content block states."
        ),
        "parameters": {
            "published_kappa_MeV": KAPPA_AS_PUBLISHED,
            "source_witness": str(COUPLING.relative_to(HERE.parent)),
            "corroborating_witness": str(COMPOSITION.relative_to(HERE.parent)),
        },
        "data": {
            "anchors": {
                "3He": {
                    "slope_MeV": he3["slope_per_excess_unit_MeV"],
                    "slope_in_h_E0_units": he3["slope_in_h_E0_units"],
                    "excess": he3["iface_excess_pp_minus_nn"],
                },
                "T": {
                    "slope_MeV": t["slope_per_excess_unit_MeV"],
                    "slope_in_h_E0_units": t["slope_in_h_E0_units"],
                    "excess": t["iface_excess_pp_minus_nn"],
                },
                "4He": {
                    "residual_MeV": he4["H7a_residual_MeV"],
                    "excess": he4["iface_excess_pp_minus_nn"],
                },
            },
            "original_verdict": verdict,
            "finding": (
                "The conjecture's 0.034% agreement is with one arm of a two-arm "
                "measurement whose own probe recorded the single-kappa hypothesis "
                "as unsupported. The block reports the value as observed 'at the "
                "single-magic anchors' (plural); the anchors disagree in sign."
            ),
        },
        "assertions": assertions,
        "allPassed": all(a["passed"] for a in assertions),
    }
    witness = _ser(witness_raw)
    out = HERE / "kappa-provenance.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwitness -> {out.name}  (allPassed={witness_raw['allPassed']})")


if __name__ == "__main__":
    main()

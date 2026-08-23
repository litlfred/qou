#!/usr/bin/env python3
"""
Bridge: Term 6 (Habiro residue) → MPFR 50 dps witness schema.

The existing producer ``term6_residues_at_roots.py`` computes T6
in f64 + sympy via principal-part-at-roots-of-unity, emitting
``term6-residues-at-roots.witness.json`` keyed by particle name.

The consumer
``mass_formula_6term_mpfr_50dps.term_6_habiro_residue_mp(A)``
expects a sibling witness
``term6-habiro-residue-mpfr-50dps.witness.json`` keyed by
``atom == f"A={A}"`` with a ``term6_b_pred_mev_50dps`` field.

This script bridges the two — reads the existing f64 values and
re-emits them in the expected schema.  T6 is **not** lifted to
50 dps here (the upstream producer is still f64); the f64 value
is wrapped in ``mp.mpf(str(value))`` for downstream consumption.

The T6 magnitudes for A=1 atoms are small (~2 MeV for proton/
neutron, divided by m_e gives ~4 cat units vs m_p_hecke ~1.18M),
so the f64 → 50 dps precision loss is ~10⁻¹⁵ of m_p_hecke,
well below the 1.50 % residual gate.

A=0 (electron) is **not in the upstream witness** — T6 for the
electron via the residue-at-roots path needs its own derivation
(the electron's tr_M(σ_1^3, q) has a different pole structure
than the nucleon braids).  Surfaced as a documented gap.

UPSTREAM SHAPE CHANGE — A ≥ 2 IS NOW A GAP, NOT A NUMBER
--------------------------------------------------------
``term6-residues-at-roots.witness.json`` no longer carries
``term6_at_q0_real`` on every row.  Only the two A=1 rows (proton,
neutron) resolve; deuteron / tritium / helium-3 / helium-4 each carry
an ``error`` string instead::

    ValueError: LaurentQ.from_sympy: non-Laurent factor
    -(1 - 1/q**4)*(q - 1)**2/12 + 1/2 in ...

i.e. the upstream partial-fraction split fails on every multi-nucleon
braid.  Reading ``r["term6_at_q0_real"]`` unconditionally is what made
this bridge die with ``KeyError: 'term6_at_q0_real'``.

The field was **not renamed and did not move under a nested key** — it
is absent because the upstream compute did not produce a value.  The
number is therefore not derivable here, and this bridge does not invent
one: A ≥ 2 is emitted as a null row carrying the verbatim upstream
error, exactly like the A=0 electron gap.  The A=2/3/4 values in the
previously committed witness (55.82 / -21375.48 / 692957.92 MeV) came
from a pre-failure upstream (recorded sha256 299c86d8…, computed
2026-05-05) and are not reproducible from the witness on disk.

Un-gapping A ≥ 2 means fixing ``LaurentQ.from_sympy`` /
``term6_residues_at_roots.py`` — a different producer, and a real
derivation gap, not a reader bug.

Output: ``term6-habiro-residue-mpfr-50dps.witness.json``
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

# P31 compliance: m_e from codata_constants module-level (single source).
from codata_constants import M_E_MEV as _M_E_MEV_CONST  # noqa: E402
M_E_MEV_MP = mp.mpf(str(_M_E_MEV_CONST))
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder, load_and_hash_upstream  # noqa: E402

SRC_PATH = _pb.witness_path("term6-residues-at-roots.witness.json", HERE)
OUT_PATH = _pb.witness_path("term6-habiro-residue-mpfr-50dps.witness.json", HERE)

# The upstream field this bridge is built around.  Named once so the
# presence test and the error message cannot drift apart.
VALUE_KEY = "term6_at_q0_real"


def _mpf(v):
    """Coerce an upstream witness value to ``mp.mpf`` at the READ boundary.

    ``mpf`` and not ``float``: the corpus is migrating its witness numerics
    to precision-preserving decimal STRINGS, and a ``float()`` here would
    truncate a 60-digit string to 17 digits at the exact point the value
    enters the pipeline.  The script-QA sidecar flags the old
    ``float(r["term6_at_q0_real"])`` as `does_not_default_to_float`, severity
    major, for that reason.

    ``mp.mpf(v)`` parses a decimal string exactly; a legacy JSON float goes
    through ``repr`` (its shortest round-tripping decimal) so the literal the
    file states is recovered rather than the binary64 tail.  Same helper shape
    as ``binding_per_block_magnitude_a3_probe._mpf``.
    """
    if v is None:
        return None
    if isinstance(v, mp.mpf):
        return v
    # float64-intentional: `repr` is the shortest round-tripping decimal of a
    # legacy JSON float, so this recovers the literal the file states.
    return mp.mpf(v) if isinstance(v, str) else mp.mpf(repr(v))


def main() -> int:
    src, src_hash = load_and_hash_upstream(SRC_PATH)
    rows = src.get("data", {}).get("results", [])

    # Group by A and select the canonical representative per A.
    # For A=1 we use the proton (Z=1, N=0); for A=2 the deuteron;
    # for A=3 the triton (or ³He, identical structure); for A=4 ⁴He.
    # T6 at A=1 must apply uniformly to {p, n, e} consumers, so the
    # f64 proton row is used as the A=1 representative.  T6 for the
    # electron at H_2 is a separate derivation and is surfaced as a
    # null row with documented gap.
    # Prefer proton for A=1, deuteron for A=2, triton for A=3, He-4 for A=4.
    prefer = {
        1: "proton", 2: "deuteron", 3: "tritium", 4: "helium-4",
    }
    # `canonical`: rows that actually carry a value.  `failed`: rows where the
    # upstream compute raised, keyed by A.  Splitting the two is the fix for
    # `KeyError: 'term6_at_q0_real'` — the old loop let an error row become the
    # representative for its A and then indexed the missing key.  A row is only
    # eligible to represent its A if it HAS the value.
    canonical: dict = {}
    failed: dict = {}
    for r in rows:
        A = r.get("A")
        if A is None:
            continue
        if VALUE_KEY not in r:
            # Keep the first error seen for this A; it is quoted verbatim in
            # the gap row so the reason travels with the witness.
            failed.setdefault(A, r)
            continue
        if r.get("atom") == prefer.get(A) or A not in canonical:
            canonical[A] = r

    out_rows = []
    for A in sorted(set(canonical) | set(failed)):
        if A not in canonical:
            # Upstream produced no value for this A.  Emit the gap, quoting the
            # upstream error, rather than substituting a number.  Consumers
            # already skip null `term6_b_pred_mev_50dps` (see
            # `mass_formula_6term_mpfr_50dps.term_6_habiro_residue_mp`).
            fr = failed[A]
            out_rows.append({
                "atom":                  f"A={A}",
                "A":                     A,
                "source_particle":       fr.get("atom"),
                "term6_b_pred_mev_50dps": None,
                "term6_cat_units_f64":   None,
                "upstream_error":        fr.get("error"),
                "precision_note":        (
                    f"GAP: upstream 'term6-residues-at-roots' emitted no "
                    f"'{VALUE_KEY}' for A={A} — its partial-fraction split "
                    f"raised on the multi-nucleon braid.  No value is "
                    f"substituted here; the bridge cannot manufacture one. "
                    f"Fix belongs in term6_residues_at_roots.py / "
                    f"LaurentQ.from_sympy."
                ),
            })
            continue
        r = canonical[A]
        # The upstream value 'term6_at_q0_real' is in mass-formula
        # cat-units (dimensionless multiplier of m_e).  Convert to
        # MeV by multiplying by the module-level M_E_MEV_MP (P31 compliant).
        cat_units = _mpf(r[VALUE_KEY])
        t6_b_pred_MeV = M_E_MEV_MP * cat_units
        out_rows.append({
            "atom":                  f"A={A}",
            "A":                     A,
            "source_particle":       r.get("atom"),
            # `fmt`, not `str(mpf)`: `str` renders at the live COMPUTE dps
            # (70), 10 guard digits wider than the serialization contract.
            "term6_b_pred_mev_50dps": fmt(t6_b_pred_MeV),
            # The upstream literal, verbatim and unpadded.  Deliberately NOT
            # `fmt`: this value IS a float64 and re-rendering it at 60 dps
            # would emit its binary expansion as if measured — the exact
            # laundering `witness_float64_padding_audit.py` exists to catch.
            "term6_cat_units_f64":   str(r[VALUE_KEY]),
            "precision_note":        (
                "Bridged from f64 source 'term6-residues-at-roots'; "
                "downstream consumer wraps in mp.mpf for 50-dps arithmetic. "
                "Upstream precision is f64 (~10^-15 relative)."
            ),
        })

    # Document electron gap (A=0 is not in the upstream witness).
    out_rows.append({
        "atom":             "A=0",
        "A":                0,
        "source_particle":  "electron (NOT YET DERIVED)",
        "term6_b_pred_mev_50dps": None,
        "term6_cat_units_f64":   None,
        "precision_note":   (
            "Electron T6 at H_2 (σ_1^3 trefoil) is a separate "
            "derivation — the upstream f64 producer does not "
            "cover non-nucleon braids.  Surfaced as a documented "
            "gap pending an electron-specific residue compute."
        ),
    })

    w = WitnessBuilder("term6-habiro-residue-mpfr-50dps", engine="mpmath")
    w.set_description(
        "Term 6 (Habiro residue) bridged from the f64 producer "
        "'term6_residues_at_roots.py' into the schema expected by "
        "mass_formula_6term_mpfr_50dps.term_6_habiro_residue_mp(A). "
        "T6 magnitudes for A=1 are small (~2 MeV / m_e ≈ 4 cat units) "
        "relative to m_p_hecke (~1.18e6), so the f64 → 50 dps wrap "
        "is precision-safe at the current 1.50 % m_p closure gate. "
        "Electron T6 (A=0 / H_2) is surfaced as a null row pending "
        "an electron-specific residue derivation."
    )
    n_gap = len(failed)
    if n_gap:
        w.add_caveat(
            "UPSTREAM GAP — "
            + ", ".join(f"A={A} ({failed[A].get('atom')})" for A in sorted(failed))
            + f": 'term6-residues-at-roots.witness.json' carries no "
            f"'{VALUE_KEY}' for these rows; its partial-fraction split raises "
            "`ValueError: LaurentQ.from_sympy: non-Laurent factor` on every "
            "multi-nucleon braid.  Those A are emitted as NULL rows with the "
            "upstream error attached — no value is substituted.  Note that a "
            "previously committed revision of this witness carried numbers "
            "for A=2/3/4 (55.82 / -21375.48 / 692957.92 MeV); they were "
            "bridged from a pre-failure upstream (recorded sha256 299c86d8…, "
            "computed 2026-05-05) and are NOT reproducible from the witness "
            "on disk.  MEASURED downstream effect: "
            "`mass_formula_6term_mpfr_50dps.term_6_habiro_residue_mp(A)` now "
            "RAISES KeyError for A=2/3/4 (it already did for A=0) rather than "
            "returning a stale number — that is its documented design, which "
            "refuses to assemble a 6-term sum with a term missing.  "
            "`paper_six_term_isotope_sweep._t6_by_A` is unaffected: it reads "
            "`results_by_atom` at the TOP level while WitnessBuilder nests it "
            "under `data`, so its cache is already empty and every T6 is "
            "already 0 — a pre-existing path bug in that reader, not a "
            "consequence of this gap.  Whoever fixes that path must also skip "
            "null rows: `mp.mpf(None)` raises TypeError, which its "
            "`except (KeyError, IndexError, ValueError)` does not catch."
        )
    w.set_audit_only("docs/audits/2026-05-16-t1-t4-tower-closure-plan.md")
    w.add_upstream(SRC_PATH)
    w.add_parameter("m_e_MeV", str(M_E_MEV_MP))
    w.add_parameter("dps", mp.mp.dps)
    w.add_data("results_by_atom", out_rows)
    w.add_data("upstream_resolution", {
        "value_key": VALUE_KEY,
        "A_resolved": sorted(canonical),
        "A_upstream_gap": sorted(failed),
        "upstream_errors": {
            str(A): failed[A].get("error") for A in sorted(failed)
        },
    })
    w.set_content_block("prop:term6-binding-density")
    w.save()
    print(f"  Wrote {OUT_PATH.name} with {len(out_rows)} A-keyed rows")
    print(f"  resolved from upstream : A={sorted(canonical)}")
    print(f"  upstream gap (no value): A={sorted(failed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

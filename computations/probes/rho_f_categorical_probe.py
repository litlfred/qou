#!/usr/bin/env python3
"""W-1 — Categorical probe for ρ_F substrate correction.

> SUPERSEDED-ρ_q purge marker (2026-05-24, PR #1127):
> This script is EXPLORATORY (testing alternative `ρ_F`-type candidates).
> Function names `rho_q_integer` and `rho_q_trm_combined` refer to
> CANDIDATE Frobenius packing factors being probed, NOT to the
> SUPERSEDED scalar `ρ_q = 1/ℏ_q²` (which was purged from
> [`q_pinning_50_digit.py`](q_pinning_50_digit.py) per
> [`docs/audits/2026-05-24-superseded-rho-q-purge.md`](../../docs/audits/2026-05-24-superseded-rho-q-purge.md)).
> The categorical replacement target is
> [`prop:rho-k-graded-expansion`](../../folio/quantum-observable-universe/braids-and-knots/rho-k-graded-expansion.md);
> this probe's candidates are direct competitors.

Goal: find a PURELY categorical formula for ρ_F(Z,N) that improves on
the integer rule ρ_F = ⌈A/2⌉ without using any AME binding-energy input.

The paper's current derivation (`rem:frobenius-packing-density`) gives the
INTEGER rule ρ_F ∈ {m_e, 2m_e} from the Wedderburn alt-block occupation:

    ρ_F = m_e  if alt ∉ Λ(K)   (single-chirality, e.g. D)
    ρ_F = 2m_e if alt ∈ Λ(K)   (CPT-saturated, e.g. ³He, T)

This gives ρ_F = ⌈A/2⌉ · m_e for the census atoms (A ≤ 4).  However the
*empirical* true_ρ from `rho-census-wedderburn-experiment.witness.json` is:

    ²H:   true_ρ = 0.9892  (error +1.09% from integer 1)
    ³H:   true_ρ = 2.0031  (error +0.15% from integer 2)
    ³He:  true_ρ = 2.0612  (error -2.97% from integer 2)  ← worst

W-1 tests four categorical candidates C0–C3 that are **zero-AME-input**:
every formula depends only on q₀ and the atomic-braid tr_M values (which
are computed from the Hecke algebra, not from AME data).

Candidates
──────────
C0  Integer rule  ρ = ⌈A/2⌉                   (current paper baseline)
C1  q-integer     ρ = [⌈A/2⌉]_q               (q-deform of ceiling)
C2  tr_M-ratio    ρ = ⌈A/2⌉ · (Σ_i tr_M_i) / (A·tr_M_avg)
                    where tr_M_i = tr_M(nucleon_i braid)
C3  Combined      ρ = [⌈A/2⌉]_q · (Σ_i tr_M_i) / (A·tr_M_avg)
                    = C1 × correction from C2

All tr_M values are loaded from `markov-peel-atomic-tr-m.witness.json`
(zero AME input; computed from the Hoefsmit / Wenzl bridge at 50 dps).
The empirical true_ρ from `rho-census-wedderburn-experiment.witness.json`
is used only to SCORE the candidates, not as input.

Outputs: `rho-f-categorical-probe.witness.json`.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from _precision import set_compute_dps, fmt  # noqa: E402
# q0 read BY NAME from `q_parameter` (bean qou-9ugp, 2026-09-04). Idempotent.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

set_compute_dps()

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
from canonical_trm_reference import tr_m_nucleon  # noqa: E402  (serves the deuteron row too)
import json
import sys

import mpmath as _mp  # noqa: E402
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent

# ── Load tr_M values (zero AME) ────────────────────────────────────────────
# ANCHOR-MATCHED (2026-08-25). This probe is manifest-declared `ideal_muon`, its
# Q0 below is the MUON value, and the hardcoded TR_M table beneath matches the
# MUON peel witness to every digit it carries. Reading the base-name peel
# witness -- which is PROTON -- meant `TR_M.update(_peel_data)` silently
# OVERWROTE that coherent muon basis with proton values. The hardcoded table is
# effectively the control showing what the probe intends, so the fix is verified
# by the override becoming a no-op.
_peel = _pb.witness_path("markov-peel-atomic-tr-m-muon.witness.json", HERE)
_peel_data: dict = {}
if _peel.exists():
    _pd = json.loads(_peel.read_text())
    # results live in assertions list (newer WitnessBuilder format)
    _candidates: list = []
    _candidates += _pd.get("assertions", []) or []
    for key in ("rows", "data", "atoms", "results"):
        v = _pd.get(key)
        if isinstance(v, list):
            _candidates += v
        elif isinstance(v, dict):
            _candidates += v.get("results", []) or []
    for r in _candidates:
        if not isinstance(r, dict):
            continue
        z = r.get("Z")
        n = r.get("N")
        trm = r.get("tr_M_at_q0") or r.get("tr_M") or r.get("trM")
        if z is not None and n is not None and trm:
            _peel_data[(int(z), int(n))] = _mp.mpf(str(trm))

# Hardcode from markov-peel witness (verified; see below)
# These are the gold-standard values at q_0 = 1.1099785955573347, 50 dps.
# mpf, not float64 literals: these are 50-dps witness values and a bare Python
# float truncates them at the 17th digit before any arithmetic runs.
TR_M: dict = {
    # CONVENTION FIX (2026-08-30, bean qou-46ab): were convention-C literals,
    # 7.55% from the canonical D values.
    (1, 0): tr_m_nucleon("proton"),
    (0, 1): tr_m_nucleon("neutron"),
    # deuteron: was the superseded grouped/convention-C literal 0.38828647…
    # (tracker #7735 item K). Never read below (only p/n are); kept consistent.
    (1, 1): tr_m_nucleon("deuteron"),   # deuteron  (D)
    (1, 2): _mp.mpf("0.1040521186755260"),   # tritium   (³H)
    (2, 1): _mp.mpf("0.2065408585622625"),   # helium-3  (³He)
    (2, 2): _mp.mpf("0.0553483458766980"),   # helium-4  (⁴He)
}
# Merge any live witness values (override hardcoded if present)
TR_M.update(_peel_data)

TR_M_P = TR_M[(1, 0)]   # proton
TR_M_N = TR_M[(0, 1)]   # neutron
TR_M_AVG = (TR_M_P + TR_M_N) / _mp.mpf(2)

# ── Load empirical true_ρ (used only for scoring, not as formula input) ─────
_census_path = _pb.witness_path("rho-census-wedderburn-experiment.witness.json", HERE)
_TRUE_RHO: dict[tuple[int, int], dict] = {}
if _census_path.exists():
    _cd = json.loads(_census_path.read_text())
    for r in (_cd.get("rows") or []):
        z, n_ = r.get("Z"), r.get("N")
        if z is not None and n_ is not None:
            _TRUE_RHO[(int(z), int(n_))] = {
                "true_rho":        r.get("true_rho"),
                "delta_rho":       r.get("delta_rho"),
                "rho_handpick":    r.get("rho_handpick"),
            }

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). It was the literal
# 1.1099785955573347 labelled '(MUON layer)' -- the RETIRED self-certified
# pin A, superseded 2026-08-22, so the label named a layer the value no longer
# belonged to.
#
# MIGRATED TO PROTON on owner instruction, 2026-09-04. Until this commit the
# stem was listed `ideal_muon`, so `q_parameter` bound the MUON anchor to
# `Q_50_DIGIT_STR` here and this line read the live CODATA-2022 muon
# derivation. The stem is now `physical_proton`, so the same by-name read
# resolves the proton pin -- an 11.54 ppb move, not the 0.077 ppb of a
# within-layer refresh.
#
# Nothing in this file establishes exception E2 (the ideal CAL-1/2/3 layer),
# and under the 2026-08-30 ruling the burden is on the exception, so proton is
# the default this producer falls to. The manifest change and the regenerated
# witness land in ONE commit, per the AGENTS.md constraint that the
# `ideal_muon` migration must never be split.
Q0 = _mp.mpf(Q_50_DIGIT_STR)

# MERGE NOTE 2026-09-04. `origin/main` changed this same block in the opposite
# direction: it moved the read from the retired literal to `q_muon_at()`, i.e.
# it REFRESHED WITHIN the muon layer and wrote "Whether it should instead be
# proton is the `q0Anchor: independent` disposition question owned by bean
# `qou-324i`, and is deliberately not decided here."
#
# That deferral is superseded, not overruled on a judgement call: the owner
# ruling of 2026-08-30 makes proton the DEFAULT and puts the burden on the
# exception -- "it should be proton unless it is an explicit comparison /
# discussion on CAL 123 math ideal or so". This producer is neither (E1: it
# makes no proton-vs-muon comparison; E2: it is not about the calibration
# triple as mathematics), and "it has always been muon" is explicitly not a
# reason. So `qou-324i`'s question is answered for this stem.
#
# The sibling's finding is kept and is the reason this reads by NAME rather
# than by literal: the q0-value drift audit prescribes "fix by RE-RUNNING THE
# PRODUCER, never by hand-editing the number", and that remedy CANNOT work
# against a hardcoded literal -- a re-run reproduces it faithfully. Measured
# there: re-running left the audit still flagging it.


def q_integer(n: int, q=Q0):
    """[n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    if abs(q - 1) < _mp.mpf("1e-12"):
        return _mp.mpf(n)
    return (q**n - q**(-n)) / (q - q**(-1))


def rho_integer(A: int):
    """C0: ρ = ⌈A/2⌉  (current paper integer rule)."""
    return _mp.mpf(-(-A // 2))          # exact integer ceiling, no float divide


def rho_q_integer(A: int, q=Q0):
    """C1: ρ = [⌈A/2⌉]_q  (q-deformation of the ceiling function)."""
    return q_integer(-(-A // 2), q)


def rho_trm_ratio(Z: int, N: int):
    """C2: ρ = ⌈A/2⌉ · (Σ nucleon tr_M) / (A · tr_M_avg).

    Uses per-nucleon Markov traces from markov-peel-atomic-tr-m.witness.json.
    Zero AME input.
    """
    A = Z + N
    n_half = _mp.mpf(-(-A // 2))
    trm_sum = Z * TR_M_P + N * TR_M_N
    return n_half * trm_sum / (A * TR_M_AVG)


def rho_q_trm_combined(Z: int, N: int, q=Q0):
    """C3: ρ = [⌈A/2⌉]_q · (Σ nucleon tr_M) / (A · tr_M_avg).

    Combines the q-deformed integer C1 with the tr_M composition correction C2.
    Zero AME input.
    """
    A = Z + N
    q_ceil = q_integer(-(-A // 2), q)
    trm_sum = Z * TR_M_P + N * TR_M_N
    return q_ceil * trm_sum / (A * TR_M_AVG)


# ── Census atoms (Kashaev-rule only; ⁴He uses magic-A, not census) ──────────
ATOMS = [
    {"sym": "2H",  "Z": 1, "N": 1, "A": 2, "label": "deuteron"},
    {"sym": "3H",  "Z": 1, "N": 2, "A": 3, "label": "tritium"},
    {"sym": "3He", "Z": 2, "N": 1, "A": 3, "label": "helium-3"},
]


def score(rho_pred, true_rho) -> dict:
    """Scored in mpf and SERIALISED AS STRINGS.

    `delta` and `err_pct` were bare float64 in the witness -- and with `true_rho`
    read from a witness as a float, the subtraction was float64 on both sides.
    """
    if true_rho is None:
        return {"delta": None, "err_pct": None}
    tr = _mp.mpf(str(true_rho))
    delta = _mp.mpf(str(rho_pred)) - tr
    err_pct = delta / tr * 100
    return {"delta": fmt(delta), "err_pct": fmt(err_pct)}


def main() -> int:
    print("=" * 90)
    print("W-1 — Categorical ρ_F probe  (zero AME input)")
    print(f"  q₀ = {Q0}")
    print(f"  tr_M(proton) = {_mp.nstr(TR_M_P, 12)}")
    print(f"  tr_M(neutron) = {_mp.nstr(TR_M_N, 12)}")
    print(f"  tr_M_avg = {_mp.nstr(TR_M_AVG, 12)}")
    print(f"  [2]_q = {_mp.nstr(q_integer(2), 10)}")
    print("=" * 90)

    rows = []
    header = (f"  {'atom':>4}  {'Z':>2} {'N':>2}  "
              f"{'true_ρ':>8}  "
              f"{'C0(int)':>8}  {'C0 err%':>8}  "
              f"{'C1([n]q)':>10} {'C1 err%':>8}  "
              f"{'C2(trM)':>9} {'C2 err%':>8}  "
              f"{'C3(q+trM)':>10} {'C3 err%':>9}")
    print(header)
    print("  " + "-" * 88)

    for atom in ATOMS:
        Z, N, A = atom["Z"], atom["N"], atom["A"]
        key = (Z, N)
        true_data = _TRUE_RHO.get(key, {})
        true_rho = true_data.get("true_rho")

        c0 = rho_integer(A)
        c1 = rho_q_integer(A)
        c2 = rho_trm_ratio(Z, N)
        c3 = rho_q_trm_combined(Z, N)

        def fmt_rho(r) -> str:
            return f"{_mp.nstr(_mp.mpf(str(r)), 6):>8}" if r is not None else "      n/a"

        def fmt_err(r: float | None, t: float | None) -> str:
            if r is None or t is None:
                return "     n/a"
            _d = (_mp.mpf(str(r)) - _mp.mpf(str(t))) / _mp.mpf(str(t)) * 100
            _sgn = "+" if _d >= 0 else "-"
            return f"{_sgn}{_mp.nstr(abs(_d), 5):>7}%"

        print(
            f"  {atom['sym']:>4}  {Z:>2} {N:>2}  "
            f"{fmt_rho(true_rho)}  "
            f"{fmt_rho(c0)}  {fmt_err(c0, true_rho)}  "
            f"{fmt_rho(c1)}  {fmt_err(c1, true_rho)}  "
            f"{fmt_rho(c2)}  {fmt_err(c2, true_rho)}  "
            f"{fmt_rho(c3)}  {fmt_err(c3, true_rho)}"
        )

        rows.append({
            "sym":      atom["sym"],
            "Z": Z, "N": N, "A": A,
            "label":    atom["label"],
            "true_rho": (None if true_rho is None else fmt(_mp.mpf(str(true_rho)))),
            "C0_integer": {
                "rho":    fmt(c0),
                **score(c0, true_rho),
            },
            "C1_q_integer": {
                "rho":    fmt(c1),
                **score(c1, true_rho),
            },
            "C2_trm_ratio": {
                "rho":    fmt(c2),
                **score(c2, true_rho),
            },
            "C3_q_trm_combined": {
                "rho":    fmt(c3),
                **score(c3, true_rho),
            },
        })

    # ── Summary: mean absolute error per candidate ──────────────────────────
    print()
    print("  Mean |err %| per candidate (Kashaev-rule atoms with true_ρ known):")
    scored = [r for r in rows if r["true_rho"] is not None]
    for cand in ("C0_integer", "C1_q_integer", "C2_trm_ratio", "C3_q_trm_combined"):
        # `err_pct` is a serialised STRING now -- read it back as mpf rather
        # than letting float() quietly re-enter through the summary.
        errs = [abs(_mp.mpf(r[cand]["err_pct"])) for r in scored
                if r[cand]["err_pct"] is not None]
        mean_err = _mp.fsum(errs) / len(errs) if errs else _mp.nan
        max_err = max(errs) if errs else _mp.nan
        print(f"    {cand:25s}  mean={_mp.nstr(mean_err, 5):>8}%  "
              f"max={_mp.nstr(max_err, 5):>8}%")

    # ── Witness ─────────────────────────────────────────────────────────────
    witness = {
        "computation":  "rho-f-categorical-probe",
        "description": (
            "W-1 categorical ρ_F probe.  Tests four zero-AME-input candidates "
            "(C0: integer ceiling, C1: q-integer, C2: tr_M-ratio correction, "
            "C3: C1×C2 combined) against the empirical true_ρ from the "
            "rho-census-wedderburn-experiment witness.  "
            "Best single-atom result: C3 gives ³He at −0.14% "
            "(vs C0 integer at −2.97%)."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        # These were bare floats; the mpf values now carry 50 dps and are
        # serialised through `_precision.fmt` rather than truncated by json.
        "parameters": {
            "q_0":          fmt(Q0),
            "q_0_anchor":   "muon (ideal 3-CAL) — matches the -muon peel read above",
            "tr_M_proton":  fmt(TR_M_P),
            "tr_M_neutron": fmt(TR_M_N),
            "tr_M_avg":     fmt(TR_M_AVG),
            "q_2_q":        fmt(q_integer(2)),
        },
        "candidates": {
            "C0": "integer ρ = ⌈A/2⌉  (paper baseline)",
            "C1": "q-integer ρ = [⌈A/2⌉]_q",
            "C2": "tr_M-ratio ρ = ⌈A/2⌉ · (Z·tr_M_p + N·tr_M_n)/(A·tr_M_avg)",
            "C3": "combined ρ = [⌈A/2⌉]_q · (Z·tr_M_p + N·tr_M_n)/(A·tr_M_avg)",
        },
        "rows": rows,
        "note": (
            "C3 reduces ³He error from −2.97% to −0.14% with zero AME input.  "
            "However C3 worsens ³H (−2.0% vs C0 +0.15%).  "
            "The residual ³H deficit implies an additional categorical "
            "correction beyond the proton/neutron tr_M ratio is needed.  "
            "GAP-A remains partially open.  See analysis doc "
            "docs/audits/2026-05-04-w1-rho-substrate-analysis.md."
        ),
    }
    out = HERE / "rho-f-categorical-probe.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        # q0_anchor was False -- 'this witness carries no q0-dependent field'.
        # Measured false at the migration (2026-09-04): moving muon -> proton
        # moves the published `parameters.q_2_q` = [2]_q by 1.21e-9 and the C1
        # err_pct by 3.1e-7. The error PERCENTAGES are near-invariant because
        # they are ratios and the scale cancels -- but 'the headline is a ratio'
        # is not the same claim as 'no field depends on q0', and it is the
        # second that this flag asserted.
        witness, script_path=__file__, engine=None)
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False))
    print(f"\n  Witness written: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

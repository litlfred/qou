#!/usr/bin/env python3
"""Barrier-1 attack: the binding link is B₃ (8G) scaled by a factor f(Z,N).

The deuteron binding is B(D) = m_e · Vol(B₃) · Δtr with Vol(B₃)=8G
(Borromean, +0.19%). Testing whether the SAME 8G volume works for T/³He
shows it does NOT (−64%, −59%): each nuclide needs its own Vol(K_bind).

But the required volumes are NOT exotic per-atom census knots — they
factor as Vol(K_bind) = 8G · f(Z,N):

    f(Z,N) = B_AME / (m_e · 8G · Δtr)        [extracted from AME]

This script computes f for D/T/³He from the canonical Δtr (binding-
canonical, H_{3A} Wedderburn sum). The result f = {D:1.00, T:2.82,
³He:2.45} matches the per-magic-closure factors found independently in
#1417, and the T↔³He difference is the Coulomb energy of ³He's two
protons (mirror-nucleus split) — i.e. the #1417 sinh(ln q) ≈ α_EM
channel.

A consistent 4th point (⁴He, Z=2 N=2, same binding-canonical producer)
then tests the pairwise-bond hypothesis f = A(A−1)/2 − κ·Z(Z−1)/2 with
κ fixed from the A=3 mirror. ⁴He is OUT-OF-SAMPLE and FALSIFIES it:
f(⁴He)=8.29 vs predicted 5.63 (+47%). Doubly-magic ⁴He binds
collectively, not pairwise — so f is a magic-SHELL-closure quantity
(exactly #1417's "per-magic-closure f"), to be derived from the
Demazure crystal closure level (AGENTS.md §7b), NOT inter-nucleon bonds.

STATUS: f is EXTRACTED from AME (not derived). The findings here are
(i) the *factorisation* Vol(K_bind)=8G·f·Δtr — the census-free derived
part is 8G·Δtr; (ii) the Coulomb structure of f (A=3 mirror split); and
(iii) the *falsification* of the pairwise-bond model. f is NOT fittable
from 4 points (forbidden ansatz); deriving it from crystal-closure is
the open Barrier-1 research. Discipline: structural probe, f labelled
AME-extracted; no fitted coefficient is wired to production.

CANONICAL-TRACE MIGRATION (2026-11-15, owner-approved, tracker #7735).
Every number quoted ABOVE this paragraph (f = {D:1.00, T:2.82, ³He:2.45,
⁴He:8.29}, "+0.19%", "+47%") was computed from hardcoded GROUPED-word /
CONVENTION-C traces (e.g. deuteron 0.38829, free p+n 0.98353). Those are
retired: the canonical trace is the borromean word (owner ruling
qou-hu1f), convention D (ruling 2026-08-15), proton pin. The traces are
now READ at run time — atoms p/n/D/T/³He through
`canonical_trm_reference.tr_m_nucleon` (which refuses a pin or ordering
mismatch), ⁴He from `canonical-tr-m-via-chi-cache.witness.json` (the only
witness that owns it; its pin is checked here), and the free trace is the
disjoint product |tr_M(p)|^Z·|tr_M(n)|^N on the same functional. Both are
cross-checked against `binding-canonical.witness.json`'s `tr_M_atom` /
`tr_M_free` to 1e-40. The quoted figures above are kept as a record of
what the C/grouped frame gave; the witness carries the canonical ones.
"""
from __future__ import annotations

import json
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

from mpmath import mp, mpf, catalan

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)

# Canonical tr_M (free constituents, bound atom): borromean word, convention
# D, proton pin. Read at run time; never hardcoded (the previous hardcoded
# table was the grouped/convention-C frame — see the module docstring).
# AME binding energies are validation inputs (compared against, not fed in).
AME_B_MEV = {
    # name: (Z, N, canonical-atom-key, B_AME_MeV)
    "D":   (1, 1, "deuteron", _ame_nstr(AME_B_DEUTERON_MEV_VALIDATION, 30)),
    "T":   (1, 2, "tritium", _ame_nstr(AME_B_TRITIUM_MEV_VALIDATION, 30)),
    "3He": (2, 1, "helium-3", _ame_nstr(AME_B_HE3_MEV_VALIDATION, 30)),
    "4He": (2, 2, "helium-4", _ame_nstr(AME_B_HE4_MEV_VALIDATION, 30)),
}
_HERE = Path(__file__).resolve().parent


def _load_json(name: str) -> dict:
    # parse_float=str: never let a recorded digit pass through float64.
    return json.loads((_HERE / name).read_text(), parse_float=str)


def _helium4_from_chi_cache() -> "mpf":
    """⁴He is owned only by canonical-tr-m-via-chi-cache; check its pin."""
    from q_parameter import Q_50_DIGIT_STR  # noqa: PLC0415
    w = _load_json("canonical-tr-m-via-chi-cache.witness.json")
    if w.get("q0Anchor") != "proton":
        raise ValueError(f"chi-cache q0Anchor={w.get('q0Anchor')!r}, need proton")
    rows = {r["atom"]: r for r in w["results"]}
    row = rows["helium-4"]
    if abs(mpf(row["q_0_50dps"]) - mpf(Q_50_DIGIT_STR)) > mpf("1e-40"):
        raise ValueError("chi-cache ⁴He row is not at this run's q0 pin")
    return abs(mpf(row["tr_M_q0"]))


def canonical_traces() -> dict:
    """{atom: (Z, N, tr_M_free, tr_M_atom, B_AME)} on the canonical functional."""
    from canonical_trm_reference import tr_m_nucleon  # noqa: PLC0415
    p, n = tr_m_nucleon("proton"), tr_m_nucleon("neutron")
    bc = {r["atom"]: r for r in
          _load_json("binding-canonical.witness.json")["data"]["results"]}
    out = {}
    for name, (Z, N, key, bame) in AME_B_MEV.items():
        atom = _helium4_from_chi_cache() if key == "helium-4" else tr_m_nucleon(key)
        free = p ** Z * n ** N
        # Independent cross-check against binding-canonical (same functional).
        for label, mine, theirs in (("tr_M_atom", atom, bc[name]["tr_M_atom"]),
                                    ("tr_M_free", free, bc[name]["tr_M_free"])):
            if abs(mine - mpf(theirs)) > mpf("1e-40") * abs(mine):
                raise ValueError(f"{name} {label}: {mine} vs binding-canonical {theirs}")
        out[name] = (Z, N, free, atom, bame)
    return out


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("binding-factor-f-decomposition", engine="mpmath")
    me = mpf(str(M_E_MEV))
    vol_b3 = 8 * catalan
    scale = me * vol_b3

    print("=" * 72)
    print("Binding factor f(Z,N): Vol(K_bind) = 8G · f  (Barrier-1 reframe)")
    print("=" * 72)
    print(f"  m_e·8G = {mp.nstr(scale, 8)} MeV   (8G = Vol(Borromean) = {mp.nstr(vol_b3, 8)})")
    print(f"  {'atom':5}{'Z,N':>6}{'Δtr':>10}{'B_AME':>9}{'f=B/(m_e·8G·Δtr)':>20}")
    rows = []
    fvals = {}
    ATOMS = canonical_traces()
    for name, (Z, N, free, atomtr, bame) in ATOMS.items():
        dtr = free - atomtr
        B = mpf(bame)
        f = B / (scale * dtr)
        print(f"  {name:5}{f'{Z},{N}':>6}{mp.nstr(dtr, 6):>10}{mp.nstr(B, 6):>9}{mp.nstr(f, 8):>20}")
        fvals[name] = f
        rows.append({
            "atom": name, "Z": Z, "N": N, "A": Z + N,
            "tr_M_free": mp.nstr(free, 50),
            "tr_M_atom": mp.nstr(atomtr, 50),
            "delta_tr": mp.nstr(dtr, 30),
            "B_AME_MeV": str(bame),
            "f_AME_extracted": mp.nstr(f, 30),
        })
    # Coulomb structure: T and ³He are A=3 mirror nuclei; f(T) > f(³He)
    df = fvals["T"] - fvals["3He"]  # κ: Coulomb per proton-pair, from A=3 mirror
    print()
    print(f"  f(T) − f(³He) = {mp.nstr(df, 6)}  (mirror split; ³He's 2 protons → Coulomb, #1417)")

    # ── Pairwise-bond hypothesis test: f = pairs(A) − κ·proton-pairs(Z) ──
    # κ fixed from the A=3 mirror; deuteron fixes the bond unit. ⁴He (Z=2,N=2)
    # is then a TRUE out-of-sample test of the pairwise-bond model.
    print()
    print("  Pairwise-bond test  f_pred = A(A−1)/2 − κ·Z(Z−1)/2 :")
    print(f"  {'atom':5}{'A':>3}{'Z':>3}{'pairs':>6}{'f_pred':>9}{'f_ext':>9}{'err%':>9}")
    bond_rows = []
    for name, (Z, N, free, atomtr, bame) in ATOMS.items():
        A = Z + N
        pairs = A * (A - 1) // 2
        ppair = Z * (Z - 1) // 2
        f_pred = pairs - df * ppair
        f_ext = fvals[name]
        err = (f_ext / f_pred - 1) * 100
        print(f"  {name:5}{A:>3}{Z:>3}{pairs:>6}{mp.nstr(f_pred, 5):>9}"
              f"{mp.nstr(f_ext, 5):>9}{mp.nstr(err, 4):>9}")
        bond_rows.append({"atom": name, "A": A, "pairs": pairs,
                          "f_pred_bondcount": mp.nstr(f_pred, 20),
                          "f_extracted": mp.nstr(f_ext, 20),
                          "err_pct": mp.nstr(err, 20)})
    d_err = mpf(bond_rows[0]["err_pct"])
    he4_err = mpf(bond_rows[-1]["err_pct"])
    print()
    print(f"  Bond-count model: D err {mp.nstr(d_err, 4)}%, ⁴He err {mp.nstr(he4_err, 4)}%.")
    print("  (Numbers computed from the canonical borromean/D/proton traces; the")
    print("   docstring's D:+0.19% / ⁴He:+47% were the retired grouped/C frame.)")

    f_summary = ", ".join(f"{k}:{mp.nstr(v, 4)}" for k, v in fvals.items())
    wb.add_data("scale_m_e_8G_MeV", mp.nstr(scale, 30))
    wb.add_data("trace_frame", {
        "intra_ordering": "borromean (owner ruling qou-hu1f)",
        "markov_convention": "D, z = q^3/(q^2+1) (ruling 2026-08-15)",
        "q0Anchor": "proton",
        "sources": ["atomic-tr-m-mpfr-50dps-proton.witness.json "
                    "(via canonical_trm_reference.tr_m_nucleon): p, n, D, T, 3He",
                    "canonical-tr-m-via-chi-cache.witness.json: 4He",
                    "free trace = |tr_M(p)|^Z |tr_M(n)|^N; cross-checked "
                    "against binding-canonical.witness.json to 1e-40"],
        "superseded": "hardcoded grouped-word / convention-C table "
                      "(deuteron 0.38829, free 0.98353) removed 2026-11-15",
    })
    wb.add_data("rows", rows)
    wb.add_data("mirror_split_T_minus_He3", mp.nstr(df, 30))
    wb.add_data("bondcount_test", {
        "model": "f = A(A-1)/2 - kappa*Z(Z-1)/2, kappa from A=3 mirror",
        "rows": bond_rows,
        "verdict": (f"canonical traces: D err {mp.nstr(d_err, 4)}%, "
                    f"4He err {mp.nstr(he4_err, 4)}%. The model asserts "
                    f"f(D) = 1 by construction (pairs = 1, no pp pair)."),
    })
    wb.add_data("finding", (
        f"Vol(K_bind) = 8G·f(Z,N); f={{{f_summary}}} (AME-extracted, "
        "canonical borromean/D/proton traces). f is NOT derived and NOT "
        "fittable from 4 points — open Barrier-1. The earlier "
        "f={D:1.00,T:2.82,3He:2.45,4He:8.29} was the retired grouped/C frame."))
    wb.add_assertion(
        "deuteron_f_is_unity",
        computed=rows[0]["f_AME_extracted"], expected=mpf("1"),
        tolerance=mpf("0.01"),
        source="B(D) = m_e·8G·Δtr → f(D)=1 (Borromean volume, +0.19%)")
    wb.save()
    print("\n  Witness: binding-factor-f-decomposition.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

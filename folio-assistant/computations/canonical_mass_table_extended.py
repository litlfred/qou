"""Canonical mass table extended through the new fast pipeline.

Uses:
  - Rust hecke-canonical-chi for χ^λ(β_atom; q_0)
    (f64 path: ~10s for ⁴He H_12; MPFR-50dps path: ~15min)
  - mpmath-direct y_λ(q_0) via wedderburn_jones_markov.y_lambda_at
    (sub-second for n=18; cached for n ≤ 21)
  - IsotopeRecord schema for per-atom knot-operator catalogue

For each atom in the user-provided list:
  1. Build IsotopeRecord with knot-operator catalogue + braid word.
  2. Compute |tr_M(β_atom, q_0)| via Σ y_λ · χ^λ.
  3. Cross-reference the existing `mass-table-ppb.witness.json`
     prediction (Vol-based / α-cluster) — this script does NOT
     compute B_pred from |tr_M|; the mass-formula step is a
     separate downstream concern handled by the existing 6-term
     or atlas-Vol scripts.
  4. Compare to AME 2020 reference (via the cross-referenced B_pred).
  5. Aggregate into a witness JSON.

This is the **Layer 1 canonical pipeline** of
`docs/audits/2026-05-18-all-atoms-isotopes-plan.md`. Atoms beyond
A ≈ 4 hit Rust Hoefsmit walltime limits in the current
implementation; Layer 2..4 paths (α-cluster recursion, brane-tower)
take over there.

## CLI

    python3 canonical_mass_table_extended.py \\
        --atoms p,n,D,T,3He,4He,5Li,6Li,7Li \\
        --precision f64

The witness output filename is fixed by WitnessBuilder
(`canonical-mass-table-extended.witness.json`).
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

mp.mp.dps = 50

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from canonical_tr_m_via_rust import canonical_word_for, find_binary  # noqa: E402
from isotope_record_schema import (  # noqa: E402
    IsotopeRecord, CalibrationSource, PredictionMethod,
    build_knot_operator_catalogue,
)
from q_parameter import Q as Q_FLOAT, Q_50_DIGIT_STR  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# AME 2020 binding energies (MeV) for the canonical atoms.
B_AME_MEV: dict[tuple[int, int], float] = {
    (1, 0):  0.0,        # proton (no binding)
    (0, 1):  0.0,        # neutron (no binding; mass excess separate)
    (1, 1):  2.22456589, # D
    (1, 2):  8.4817983,  # T
    (2, 1):  7.7180428,  # ³He
    (2, 2): 28.295673,   # ⁴He
    (3, 2): 26.328,      # ⁵Li (unstable, half-life ~10⁻²² s)
    (3, 3): 31.99405,    # ⁶Li
    (3, 4): 39.24522,    # ⁷Li
    (4, 3): 37.6,        # ⁷Be
    (4, 4): 56.49951,    # ⁸Be
}

# Default atom list: full coverage through A=7 via canonical
DEFAULT_ATOMS = [
    (1, 0, "p"),
    (0, 1, "n"),
    (1, 1, "D"),
    (1, 2, "T"),
    (2, 1, "3He"),
    (2, 2, "4He"),
    (3, 2, "5Li"),
    (3, 3, "6Li"),
    (3, 4, "7Li"),
]


def compute_tr_m_canonical(
    Z: int, N: int, label: str, dps: int = 0, timeout_sec: int = 1500
) -> tuple[mp.mpf | None, float, str | None]:
    """Compute |tr_M(β_atom, q_0)| via Rust χ + mpmath y_λ.

    Returns (|tr_M|, wall_seconds, error_str).
    """
    bin_path = find_binary()
    if bin_path is None:
        return None, 0.0, "Rust binary missing — build via cargo"
    n = 3 * (Z + N)

    n_strands, word = canonical_word_for(Z, N)
    spec: dict = {
        "n_strands": n_strands, "q": Q_FLOAT, "label": label, "word": word,
    }
    if dps > 0:
        spec["q_str"] = Q_50_DIGIT_STR
    t0 = time.time()
    result = subprocess.run(
        [str(bin_path), "--dps", str(dps)],
        input=json.dumps(spec), capture_output=True, text=True,
        timeout=timeout_sec,
    )
    wall = time.time() - t0
    if result.returncode != 0:
        return None, wall, (
            f"Rust exit {result.returncode}: "
            f"stderr={result.stderr[:300]}"
        )
    r = json.loads(result.stdout)

    y_table = y_lambda_at(n, Q_FLOAT)
    tr_m = mp.mpf(0)
    for term in r["chi_lambda_terms"]:
        lam = tuple(term["lambda"])
        chi_str = (
            term.get("chi_q_normalised")
            or term.get("chi_q_f64_normalised")
        )
        chi = mp.mpf(str(chi_str))
        y = y_table.get(lam)
        if y is None:
            return None, wall, f"y_λ table missing λ={lam}"
        y_mp = mp.mpf(str(y))
        tr_m += y_mp * chi
    return abs(tr_m), wall, None


def lookup_b_pred_existing(Z: int, N: int) -> tuple[float | None, str | None]:
    """Cross-reference the existing mass-table-ppb prediction (if any).

    The canonical pipeline of this script computes |tr_M(q_0)|; mapping
    to binding-energy MeV is the job of downstream formulas (atlas
    Vol-based, α-cluster recursion, or 6-term mass formula). This
    helper looks up the existing prediction so we can tabulate it
    alongside |tr_M|.

    Returns (B_pred_MeV, origin_label) or (None, None) if absent.
    """
    try:
        path = HERE / "mass-table-ppb.witness.json"
        if not path.exists():
            return None, None
        w = json.loads(path.read_text())
        rows = w.get("data", w).get("rows", [])
        for r in rows:
            if r.get("Z") == Z and r.get("N") == N:
                return r.get("B_pred_MeV"), r.get("origin")
        return None, None
    except (KeyError, json.JSONDecodeError):
        return None, None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--atoms", default=",".join(label for _, _, label in DEFAULT_ATOMS),
        help="Comma-separated atom labels (e.g. 'p,n,D,T,3He,4He,5Li')."
    )
    parser.add_argument(
        "--precision", choices=["f64", "mpfr"], default="f64",
        help="Rust precision: 'f64' (fast, ~15 sig figs) or "
             "'mpfr' (slow, 50 dps).",
    )
    parser.add_argument("--timeout", type=int, default=1500)
    args = parser.parse_args()

    dps = 50 if args.precision == "mpfr" else 0

    label_to_ZN = {label: (Z, N) for Z, N, label in DEFAULT_ATOMS}
    label_to_ZN.update({"proton": (1, 0), "neutron": (0, 1)})
    requested = [s.strip() for s in args.atoms.split(",") if s.strip()]

    print("=" * 90)
    print(f"  Canonical mass table — Rust χ ({args.precision}) + mpmath y_λ")
    print("=" * 90)
    print()
    print(f"  q_0 = {Q_FLOAT}")
    print(f"  Precision: {dps} dps")
    print()
    print(f"  {'atom':<6} {'A':>2} {'n':>3} {'|tr_M(q_0)|':<22} "
          f"{'B_pred(existing)':>16} {'B_AME':>10} {'origin':<22} "
          f"{'wall(s)':>8}")
    print("  " + "-" * 110)

    records: list[dict] = []
    for atom_str in requested:
        if atom_str not in label_to_ZN:
            print(f"  {atom_str:<6} (skip — unknown)")
            continue
        Z, N = label_to_ZN[atom_str]
        A = Z + N
        n = 3 * A

        # Build IsotopeRecord
        ops = build_knot_operator_catalogue(Z, N)

        # Compute |tr_M| via the canonical pipeline
        tr_m, wall, err = compute_tr_m_canonical(
            Z, N, atom_str, dps=dps, timeout_sec=args.timeout,
        )
        if err:
            print(f"  {atom_str:<6} {A:>2} {n:>3} ERROR: {err[:60]}")
            continue
        # Cross-reference existing mass-table-ppb prediction (Vol-based,
        # α-cluster, or volume-match) — this script computes |tr_M|; the
        # mass-formula step is a separate downstream concern.
        b_pred_existing, origin = lookup_b_pred_existing(Z, N)
        b_ame = B_AME_MEV.get((Z, N))

        # Populate braid word + closure for provenance per the schema.
        from isotope_record_schema import CANONICAL_CLOSURES
        braid_word = [
            (int(gen), ctype) for (gen, ctype) in atom_canonical_crossings(Z, N)
        ]
        record = IsotopeRecord(
            Z=Z, N=N, A=A, n_strands=n,
            braid_word_canonical=braid_word,
            markov_closure=CANONICAL_CLOSURES.get((Z, N)),
            knot_operators=ops,
            tr_M_q0_canonical_50dps=mp.nstr(tr_m, 50, strip_zeros=False),
            prediction_method=PredictionMethod.CANONICAL_TRACE,
            calibration_source=CalibrationSource.CAL_1,
            prediction_MeV_50dps=(
                str(b_pred_existing) if b_pred_existing else None
            ),
            B_AME_MeV=b_ame,
            err_MeV=(
                b_pred_existing - b_ame
                if (b_pred_existing is not None and b_ame is not None) else None
            ),
            chi_cache_witness="(computed live via Rust hecke-canonical-chi)",
        )
        records.append(record.to_dict())

        tr_m_str = mp.nstr(tr_m, 15)
        pred_str = f"{b_pred_existing:.4f}" if b_pred_existing is not None else "—"
        ame_str = f"{b_ame:.4f}" if b_ame is not None else "—"
        origin_str = (origin or "—")[:20]
        print(f"  {atom_str:<6} {A:>2} {n:>3} {tr_m_str:<22} "
              f"{pred_str:>16} {ame_str:>10} {origin_str:<22} "
              f"{wall:>8.1f}")

    atoms_actually_computed = [r["Z"] for r in records], [r["N"] for r in records]
    builder = (
        WitnessBuilder("canonical-mass-table-extended", engine="rust+mpmath")
        .set_description(
            "Extended canonical mass table via Rust hecke-canonical-chi "
            f"({args.precision}) + mpmath y_λ. Layer 1 canonical pipeline "
            "per docs/audits/2026-05-18-all-atoms-isotopes-plan.md. "
            "Coverage is determined by --atoms (see parameters.atoms_requested); "
            "the actual rows reflect what completed within the per-atom "
            "timeout. Each row carries the per-atom IsotopeRecord with "
            "explicit knot-operator catalogue (intra-nucleon, inter-nucleon "
            "interfaces, closure topology)."
        )
        .add_parameter("q_0", Q_50_DIGIT_STR)
        .add_parameter("precision", args.precision)
        .add_parameter("dps", dps)
        .add_parameter("atoms_requested", ",".join(requested))
        .add_parameter("timeout_per_atom_sec", args.timeout)
        .add_data("rows", records)
        .add_data("n_atoms_computed", len(records))
    )
    out = builder.save()
    print()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

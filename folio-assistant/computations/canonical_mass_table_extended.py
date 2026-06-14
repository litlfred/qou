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

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
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

from _precision import set_compute_dps, fmt, COMPUTE_DPS, OUTPUT_DPS  # noqa: E402
from active_set_pruning import (  # noqa: E402
    select_active_set, verify_pruning_safe, CHI_MAX_EMPIRICAL_BOUND,
)
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from canonical_tr_m_via_rust import canonical_word_for, find_binary  # noqa: E402
from isotope_record_schema import (  # noqa: E402
    IsotopeRecord, CalibrationSource, PredictionMethod,
    build_knot_operator_catalogue,
)
from q_parameter import Q as Q_FLOAT, Q_50_DIGIT_STR  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

# qou-substrate (Layer 2a): import WitnessBuilder directly from the
# package rather than via the witness_base back-compat shim (which
# re-exports the identical class). Bootstrap the in-repo package path —
# mirrors low_isotopes_binding_sweep.py.
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder  # noqa: E402

set_compute_dps()  # ensure mp.mp.dps = COMPUTE_DPS (consistent with infra)

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

# Default atom list: full coverage through A=7 via canonical.
#
# ORDERING INVARIANT (per Gemini #781 review): the row order in the
# emitted witness `data.rows` is *deterministic* when --atoms is
# omitted; downstream consumers (notably content/values/registry.ts's
# `B_2H_AME_MeV` lookup at path `data.rows.2.B_AME_MeV`) depend on:
#
#     index 0: proton          (Z=1, N=0, A=1)
#     index 1: neutron         (Z=0, N=1, A=1)
#     index 2: deuteron        (Z=1, N=1, A=2)
#     index 3: triton          (Z=1, N=2, A=3)
#     index 4: 3He             (Z=2, N=1, A=3)
#     index 5: 4He             (Z=2, N=2, A=4)
#     index 6: 5Li             (Z=3, N=2, A=5)
#     index 7: 6Li             (Z=3, N=3, A=6)
#
# Do NOT reorder this list without also updating
# content/values/registry.ts and any other consumer that indexes
# into `data.rows`. A (Z, N)-keyed lookup would be more robust;
# tracked as a follow-up.
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
    Z: int, N: int, label: str, dps: int = 0, timeout_sec: int = 1500,
    method: str = "markov_peel",
) -> tuple[mp.mpf | None, float, str | None, str | None]:
    """Compute |tr_M(β_atom, q_0)| via the requested fast path.

    Methods (ranked by speed at H_n):
      - "laurent_q_rust" — **Tier 1.A** full Rust + MPFR pipeline
                          (pyhecke_native.tr_m_atomic_mpfr, v0.6.0+).
                          R1+R2+R3 reduce in Rust BigRational; trace
                          recursion in Rust; MPFR substitution at q₀
                          in Rust; one PyO3 call, one decimal string
                          back.  Cross-checked bit-identical to
                          laurent_q at 1e-50 relative.
      - "laurent_q"    — LaurentQ-direct Markov-axiom recursive ascent
                          (laurent_q_trace.tr_M_atomic_lq).
                          ⁴He: 4s; ⁵Li: 22s; ⁶Li: ~4 min; ⁷Li: ~1.1 hr.
                          (PR #859 / Strategy #1 from
                          docs/audits/2026-05-20-markov-peel-bottleneck-profile.md)
      - "markov_peel"  — Symbolic-q Markov-axiom recursive ascent (markov_peel.tr_M_atomic).
                          Original fast path; sympy-heavy in trace assembly.
                          ⁴He: 11s; ⁵Li: 67s; ⁶Li: 17 min.
      - "rust_f64"     — Rust hecke-canonical-chi (direct Hoefsmit, f64).
                          ⁴He: 12s; ⁵Li: > 1500s (infeasible at H_15+).
      - "rust_mpfr"    — Rust hecke-canonical-chi (MPFR-50dps).
                          ⁴He: ~15 min; H_15+ impractical.

    Returns (|tr_M|, wall_seconds, error_str, method_used).
    """
    if method == "laurent_q_rust":
        try:
            from markov_peel_rust_bridge import tr_M_atomic_rust_full
            # Honor caller-provided dps when it exceeds the 50-dps
            # production floor; never go below 50 (CLAUDE.md §L1
            # mandates ≥ 50 dps for the production trace).  The
            # `dps=0` default from the function signature collapses
            # to 50, matching the implicit policy used in the
            # sibling `laurent_q` / `markov_peel` branches below.
            effective_dps = max(int(dps), 50)
            t0 = time.time()
            tr_mp = tr_M_atomic_rust_full(Z, N, dps=effective_dps)
            wall = time.time() - t0
            return abs(tr_mp), wall, None, "laurent_q_rust"
        except NotImplementedError as e:
            # Case C — return an error tuple; the outer caller
            # (`main()`) currently SKIPS atoms with a non-empty `err`
            # rather than chaining into `laurent_q` / `markov_peel`.
            # Re-running the script with `--method laurent_q` (or
            # `markov_peel`) handles the same atom via the sympy
            # ocneanu path.  Manual chain — no automatic fallback
            # here, see PR #886 review thread r3289356832.
            return None, 0.0, (
                f"laurent_q_rust: Case C — re-run with --method "
                f"laurent_q or markov_peel: {e}"
            ), "laurent_q_rust"
        except ImportError as e:
            return None, 0.0, (
                f"laurent_q_rust: pyhecke_native missing; "
                f"build via `cd tools/pyhecke-native && maturin build "
                f"--release` and pip install the wheel. {e}"
            ), "laurent_q_rust"
        except Exception as e:  # noqa: BLE001
            return None, 0.0, (
                f"laurent_q_rust: {type(e).__name__}: {e}"
            ), "laurent_q_rust"

    if method == "laurent_q":
        try:
            from laurent_q_trace import tr_M_atomic_lq
            from q_parameter import Q_50_DIGIT_STR
            t0 = time.time()
            zh = tr_M_atomic_lq(Z, N)
            # MPFR-50dps evaluation — NEVER f64. Per CLAUDE.md §Precision
            # goals L1, the production trace must be at 50-dps precision
            # to preserve the structural-zero distinction needed for
            # categorical identities.
            tr_mp = zh.evaluate_mpf(Q_50_DIGIT_STR, dps=50)
            wall = time.time() - t0
            return abs(tr_mp), wall, None, "laurent_q"
        except NotImplementedError as e:
            # Case C — fall through to markov_peel sympy path which has ocneanu fallback.
            return None, 0.0, f"laurent_q: case-C → fallback needed: {e}", "laurent_q"
        except Exception as e:  # noqa: BLE001
            return None, 0.0, f"laurent_q: {type(e).__name__}: {e}", "laurent_q"

    if method == "markov_peel":
        try:
            import sympy as sp
            from markov_peel import tr_M_atomic
            t0 = time.time()
            tr_sym = tr_M_atomic(Z, N)
            wall = time.time() - t0
            # Substitute q = q_0 at mpmath precision
            q_sym = sp.Symbol("q", positive=True)
            free = list(tr_sym.free_symbols) if hasattr(tr_sym, "free_symbols") else []
            for f in free:
                if f.name == "q":
                    q_sym = f
                    break
            tr_at_q0 = tr_sym.subs(q_sym, sp.Float(str(Q_FLOAT), 50))
            tr_mp = mp.mpf(str(sp.N(tr_at_q0, 50)))
            return abs(tr_mp), wall, None, "markov_peel"
        except Exception as e:  # noqa: BLE001
            return None, 0.0, f"markov_peel: {type(e).__name__}: {e}", "markov_peel"

    if method == "branching":
        try:
            from canonical_tr_m_via_branching import compute_tr_m_via_branching
            tr_mp, wall, err = compute_tr_m_via_branching(Z, N, q_val=float(Q_FLOAT))
            if err:
                return None, wall, err, "branching"
            return abs(tr_mp) if tr_mp is not None else None, wall, None, "branching"
        except Exception as e:
            return None, 0.0, f"branching: {type(e).__name__}: {e}", "branching"

    # Rust paths (f64 or MPFR)
    bin_path = find_binary()
    if bin_path is None:
        return None, 0.0, "Rust binary missing — build via cargo", method
    rust_dps = 50 if method == "rust_mpfr" else 0
    n_strands, word = canonical_word_for(Z, N)
    spec: dict = {
        "n_strands": n_strands, "q": Q_FLOAT, "label": label, "word": word,
    }
    if rust_dps > 0:
        spec["q_str"] = Q_50_DIGIT_STR
    t0 = time.time()
    result = subprocess.run(
        [str(bin_path), "--dps", str(rust_dps)],
        input=json.dumps(spec), capture_output=True, text=True,
        timeout=timeout_sec,
    )
    wall = time.time() - t0
    if result.returncode != 0:
        return None, wall, (
            f"Rust exit {result.returncode}: "
            f"stderr={result.stderr[:300]}"
        ), method
    r = json.loads(result.stdout)
    n = 3 * (Z + N)
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
            return None, wall, f"y_λ table missing λ={lam}", method
        y_mp = mp.mpf(str(y))
        tr_m += y_mp * chi
    return abs(tr_m), wall, None, method


def lookup_b_pred_existing(
    Z: int, N: int, mass_table_ppb: dict | None = None,
) -> tuple[float | None, str | None]:
    """Cross-reference the existing mass-table-ppb prediction (if any).

    The canonical pipeline of this script computes |tr_M(q_0)|; mapping
    to binding-energy MeV is the job of downstream formulas (atlas
    Vol-based, α-cluster recursion, or 6-term mass formula). This
    helper looks up the existing prediction so we can tabulate it
    alongside |tr_M|.

    Pass the pre-loaded mass_table_ppb dict (from
    ``WitnessBuilder.add_upstream``) so the upstream sha256 is
    recorded in the emitted witness. Falls back to a fresh disk
    read for legacy callers.

    Returns (B_pred_MeV, origin_label) or (None, None) if absent.
    """
    try:
        if mass_table_ppb is None:
            path = _pb.witness_path("mass-table-ppb.witness.json", HERE)
            if not path.exists():
                return None, None
            mass_table_ppb = json.loads(path.read_text())
        rows = mass_table_ppb.get("data", mass_table_ppb).get("rows", [])
        for r in rows:
            if r.get("Z") == Z and r.get("N") == N:
                return r.get("B_pred_MeV"), r.get("origin")
        return None, None
    except (KeyError, json.JSONDecodeError):
        return None, None


def lookup_nucleon_mass_borromean(
    Z: int, N: int, borromean: dict | None = None,
) -> tuple[float | None, str | None]:
    """Cross-reference the Borromean tower m_p / m_n prediction.

    `canonical-mass-table-extended` computes |tr_M| but does not
    self-derive nucleon mass. The Borromean tower verification
    (`m-p-borromean-verification-50dps.witness.json`) provides
    m_p and m_n at 0.25 ppm, conditional on
    `conj:borromean-baryon-mass-formula`. For p (Z=1, N=0) and n
    (Z=0, N=1) rows we surface this prediction so the table is
    not misleadingly empty for free nucleons.

    Returns (m_pred_MeV, origin_label) or (None, None).
    """
    try:
        if borromean is None:
            path = _pb.witness_path("m-p-borromean-verification-50dps.witness.json", HERE)
            if not path.exists():
                return None, None
            borromean = json.loads(path.read_text())
        data = borromean.get("data", borromean)

        def _to_float(x: Any) -> float | None:
            # The Borromean witness stores values as mpmath-formatted
            # strings (e.g. "938.27185263683084707"). Coerce to f64
            # for downstream arithmetic; the 50-dps source value is
            # preserved as a string in the witness file itself.
            if x is None:
                return None
            try:
                return float(x)
            except (TypeError, ValueError):
                return None

        if Z == 1 and N == 0:
            return (
                _to_float(data.get("proton", {}).get("m_p_pred_MeV")),
                "borromean-tower (conj:borromean-baryon-mass-formula)",
            )
        if Z == 0 and N == 1:
            return (
                _to_float(data.get("neutron", {}).get("m_n_pred_MeV")),
                "borromean-tower (conj:borromean-baryon-mass-formula)",
            )
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
        help="Rust precision when using --method rust_f64/rust_mpfr: 'f64' "
             "(fast, ~15 sig figs) or 'mpfr' (slow, 50 dps).",
    )
    parser.add_argument(
        "--method",
        choices=["laurent_q_rust", "markov_peel", "laurent_q", "rust_f64", "rust_mpfr", "branching"],
        default="branching",
        help=(
            "Computation method. `branching` (operator-valued Wenzl combiner) "
            "is the canonical pipeline per user directive, replacing empirical fits."
        ),
    )
    parser.add_argument(
        "--target-dps", type=int, default=OUTPUT_DPS,
        help=(
            "Target precision (decimal places) for the |tr_M| sum. "
            "When < COMPUTE_DPS, active-set pruning drops y_λ terms "
            "whose tail-bound contribution falls below 10^(-target-dps). "
            "Paper hard floor ~780 ppb means target_dps > 10 is "
            "over-spent precision."
        ),
    )
    parser.add_argument("--timeout", type=int, default=1500)
    args = parser.parse_args()

    # dps policy:
    #   - markov_peel: f64-substrate via sp.Float(str(Q_FLOAT), 50)
    #   - laurent_q / laurent_q_rust: enforced MPFR-50dps via dispatcher
    #     (see compute_tr_m_canonical:147 — effective_dps=max(dps, 50))
    #   - rust_f64: f64 dps=0; rust_mpfr: MPFR dps=50
    if args.method in ("laurent_q", "laurent_q_rust"):
        dps = 50
    else:
        dps = 50 if args.precision == "mpfr" else 0

    label_to_ZN = {label: (Z, N) for Z, N, label in DEFAULT_ATOMS}
    label_to_ZN.update({"proton": (1, 0), "neutron": (0, 1)})
    requested = [s.strip() for s in args.atoms.split(",") if s.strip()]

    paper_floor_ppb = 780.0
    paper_floor_dps = float(-mp.log10(mp.mpf(paper_floor_ppb) * mp.mpf("1e-9")))
    pruning_safe = verify_pruning_safe(args.target_dps, paper_floor_ppb)

    print("=" * 90)
    print(f"  Canonical mass table — method={args.method} "
          f"(precision={args.precision} if Rust)")
    print("=" * 90)
    print()
    print(f"  q_0 = {Q_FLOAT}")
    print(f"  Method: {args.method} (Rust dps={dps}; markov_peel uses symbolic-q)")
    print(f"  COMPUTE_DPS / OUTPUT_DPS / target_dps = "
          f"{COMPUTE_DPS} / {OUTPUT_DPS} / {args.target_dps}")
    print(f"  Paper hard floor: {paper_floor_ppb} ppb "
          f"(~{paper_floor_dps:.1f} dps; CAL-2 propagation)")
    print(f"  Active-set pruning at target_dps={args.target_dps}: "
          f"{'SAFE (within paper bound)' if pruning_safe else 'WARNING — below paper floor'}")
    print()
    print(f"  {'atom':<6} {'A':>2} {'n':>3} {'|tr_M(q_0)|':<22} "
          f"{'B_pred(existing)':>16} {'B_AME':>10} {'origin':<22} "
          f"{'method':<12} {'wall(s)':>8}")
    print("  " + "-" * 122)

    # Engine + descriptor strings (used both in print headers and below).
    engine_str = "python+mpmath"
    method_desc = {
        "markov_peel": "markov_peel.tr_M_atomic (symbolic-q recursive ascent) + mpmath y_λ",
        "laurent_q":   "laurent_q_trace.tr_M_atomic_lq (Python LaurentQ + evaluate_mpf) + mpmath y_λ (MPFR-50dps)",
        "laurent_q_rust": "pyhecke-native v0.9.0 tr_m_atomic_mpfr (Tier 1.A Rust + MPFR) + mpmath y_λ (MPFR-50dps)",
        "rust_f64":  f"Rust hecke-canonical-chi (f64) + mpmath y_λ",
        "rust_mpfr": f"Rust hecke-canonical-chi (MPFR-50dps) + mpmath y_λ",
    }.get(args.method, f"unknown method '{args.method}'")

    # Pre-load upstream witnesses through the builder so their
    # sha256 hashes land in data.upstream_witness_hashes. The two
    # upstreams are:
    #   - mass-table-ppb.witness.json (B_pred via Kashaev law +
    #     α-cluster, light-isotope cross-reference)
    #   - m-p-borromean-verification-50dps.witness.json (m_p, m_n,
    #     m_μ at 0.25 ppm via Borromean tower; conditional on
    #     conj:borromean-baryon-mass-formula)
    builder = WitnessBuilder("canonical-mass-table-extended", engine=engine_str)
    mass_table_ppb_data: dict | None = None
    borromean_data: dict | None = None
    try:
        mass_table_ppb_data = builder.add_upstream(
            _pb.witness_path("mass-table-ppb.witness.json", HERE)
        )
    except FileNotFoundError:
        pass
    try:
        borromean_data = builder.add_upstream(
            _pb.witness_path("m-p-borromean-verification-50dps.witness.json", HERE)
        )
    except FileNotFoundError:
        pass

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

        # Compute |tr_M| via the canonical pipeline (default: markov_peel)
        tr_m, wall, err, method_used = compute_tr_m_canonical(
            Z, N, atom_str, dps=dps, timeout_sec=args.timeout,
            method=args.method,
        )
        if err:
            print(f"  {atom_str:<6} {A:>2} {n:>3} ERROR ({method_used}): {err[:60]}")
            continue
        # Unified prediction semantics per user directive 2026-05-19:
        # prediction_MeV_50dps + B_AME_MeV + err_MeV / err_ppm hold the
        # right observable for the row, signalled by prediction_type.
        #   p, n  -> prediction_type="mass"; values from Borromean tower
        #            (m_pred_MeV vs CODATA m_p / m_n).
        #   D and up -> prediction_type="binding_energy"; values from
        #            mass-table-ppb (B_pred vs AME B).
        is_nucleon = (Z, N) in [(1, 0), (0, 1)]
        pred: float | None = None
        ref: float | None = None
        origin: str | None = None
        prediction_type = "mass" if is_nucleon else "binding_energy"
        if is_nucleon:
            pred, origin = lookup_nucleon_mass_borromean(Z, N, borromean_data)
            # CODATA references taken from the Borromean witness so the
            # comparison stays consistent with the prediction source.
            try:
                bdata = (borromean_data or {}).get("data", borromean_data or {})
                key = "proton" if (Z, N) == (1, 0) else "neutron"
                codata_key = (
                    "m_p_codata_MeV" if (Z, N) == (1, 0)
                    else "m_n_codata_MeV"
                )
                v = bdata.get(key, {}).get(codata_key)
                ref = float(v) if v is not None else None
            except (TypeError, ValueError):
                ref = None
        else:
            pred, origin = lookup_b_pred_existing(Z, N, mass_table_ppb_data)
            ref = B_AME_MEV.get((Z, N))

        err_val: float | None = None
        err_pct_val: float | None = None
        err_ppb_val: float | None = None
        err_ppm_val: float | None = None
        if pred is not None and ref is not None:
            err_val = pred - ref
            if ref != 0.0:
                rel = err_val / ref
                err_pct_val = rel * 100.0
                err_ppm_val = rel * 1e6
                err_ppb_val = rel * 1e9

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
            tr_M_q0_canonical_50dps=fmt(tr_m),  # OUTPUT_DPS via _precision
            prediction_method=PredictionMethod.CANONICAL_TRACE,
            calibration_source=CalibrationSource.CAL_1,
            prediction_type=prediction_type,
            prediction_MeV_50dps=(
                str(pred) if pred is not None else None
            ),
            B_AME_MeV=ref,
            err_MeV=err_val,
            err_pct=err_pct_val,
            err_ppb=err_ppb_val,
            err_ppm=err_ppm_val,
            # Provenance reflects actual method used (Copilot review).
            chi_cache_witness=(
                f"(computed live via {method_used})"
            ),
        )
        records.append(record.to_dict())

        tr_m_str = fmt(tr_m, dps=15)  # display-only, full precision via fmt
        pred_str = f"{pred:.4f}" if pred is not None else "—"
        ame_str = f"{ref:.4f}" if ref is not None else "—"
        origin_str = (origin or "—")[:20]
        print(f"  {atom_str:<6} {A:>2} {n:>3} {tr_m_str:<22} "
              f"{pred_str:>16} {ame_str:>10} {origin_str:<22} "
              f"{method_used:<12} {wall:>8.1f}")

    # Builder was created early to record upstream sha256 via
    # add_upstream(); now we finish populating it.
    builder = (
        builder
        .set_description(
            f"Extended canonical mass table via {method_desc}. "
            "Layer 1 canonical pipeline per "
            "docs/audits/2026-05-18-all-atoms-isotopes-plan.md. "
            "Coverage is determined by --atoms (see parameters.atoms_requested); "
            "the actual rows reflect what completed within the per-atom "
            "timeout. Each row carries the per-atom IsotopeRecord with "
            "explicit knot-operator catalogue (intra-nucleon, inter-nucleon "
            "interfaces, closure topology). For p and n, the prediction "
            "column is the Borromean-tower nucleon mass (conditional on "
            "conj:borromean-baryon-mass-formula, sub-ppm vs CODATA); for "
            "D and up the prediction column is the mass-table-ppb binding "
            "energy (Kashaev law / α-cluster / volume-match)."
        )
        .add_parameter("q_0", Q_50_DIGIT_STR)
        .add_parameter("method", args.method)
        # `precision` reflects what the dispatcher actually does, not
        # the raw CLI flag (which only governs the rust_f64/rust_mpfr
        # branches). For laurent_q / laurent_q_rust / markov_peel the
        # effective precision is MPFR-50dps regardless of args.precision.
        .add_parameter("precision", (
            "mpfr" if args.method in ("laurent_q", "laurent_q_rust", "markov_peel")
            else args.precision
        ))
        .add_parameter("dps", dps)
        .add_parameter("compute_dps", COMPUTE_DPS)
        .add_parameter("output_dps", OUTPUT_DPS)
        .add_parameter("target_dps", args.target_dps)
        .add_parameter("paper_hard_floor_ppb", paper_floor_ppb)
        .add_parameter("active_set_pruning_safe", pruning_safe)
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

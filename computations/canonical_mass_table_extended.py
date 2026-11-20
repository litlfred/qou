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
from q_parameter import Q as Q_FLOAT, Q_50_DIGIT_STR, Q_MP  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

# qou-substrate (Layer 2a): import WitnessBuilder directly from the
# package rather than via the witness_base back-compat shim (which
# re-exports the identical class). Bootstrap the in-repo package path —
# mirrors low_isotopes_binding_sweep.py.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_LI6_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402
from codata_constants import AME_B_LI7_MEV_VALIDATION  # noqa: E402  (AME registry)

set_compute_dps()  # ensure mp.mp.dps = COMPUTE_DPS (consistent with infra)


#: Columns exposed in the nuclide-keyed view — the scalars a witnessed-value
#: pin can address. Excludes `knot_operators` / `braid_word_canonical` and the
#: provenance strings: those are bulk, and duplicating them doubles the file.
#:
#: Every numeric column here is a `fmt` STRING, not a float+`_str` pair. The
#: pair was this branch's earlier design and it is superseded by bean qou-3wqg,
#: which lifted the prediction chain to mpmath at the root: once `pred` is a
#: genuine mpf, `fmt` writes digits that exist and the shadow rule has nothing
#: left to excuse. The pair only ever made sense while `pred` was still a float
#: — i.e. while the extra digits were binary64 noise wearing a string.
_PINNABLE_COLUMNS = (
    "Z", "N", "A", "n_strands",
    "prediction_type", "prediction_method",
    "tr_M_q0_canonical_50dps", "prediction_MeV_50dps",
    "B_AME_MeV", "err_MeV", "err_pct", "err_ppb", "err_ppm",
)
# AME 2020 binding energies (MeV) for the canonical atoms.
# mpf throughout (bean qou-3wqg). The five `AME_B_*_MEV_VALIDATION` constants
# ARE mpf in `codata_constants`; wrapping them in `float()` here truncated them
# on the way in, and the four literals below were plain floats. `err = pred -
# ref` is now mpf on both sides, so it carries the precision the port to
# `mass_table_ppb.py` made available rather than losing it at the subtraction.
# The literals become strings for the same reason a `mpf(<float literal>)` is
# flagged elsewhere: `mp.mpf(26.328)` binds the binary64 value, `mp.mpf("26.328")`
# binds the decimal one.
B_AME_MEV: dict[tuple[int, int], mp.mpf] = {
    (1, 0):  mp.mpf(0),  # proton (no binding)
    (0, 1):  mp.mpf(0),  # neutron (no binding; mass excess separate)
    (1, 1):  AME_B_DEUTERON_MEV_VALIDATION,  # D
    (1, 2):  AME_B_TRITIUM_MEV_VALIDATION,   # T
    (2, 1):  AME_B_HE3_MEV_VALIDATION,   # ³He
    (2, 2): AME_B_HE4_MEV_VALIDATION,    # ⁴He
    (3, 2): mp.mpf("26.328"),      # ⁵Li (unstable, half-life ~10⁻²² s)
    (3, 3): AME_B_LI6_MEV_VALIDATION,     # ⁶Li
    (3, 4): AME_B_LI7_MEV_VALIDATION,    # ⁷Li
    (4, 3): mp.mpf("37.6"),        # ⁷Be
    (4, 4): mp.mpf("56.49951"),    # ⁸Be
}

# Default atom list: full coverage through A=7 via canonical.
#
# ORDERING INVARIANT (per Gemini #781 review): the row order in the
# emitted witness `data.rows` is *deterministic* when --atoms is
# omitted; downstream consumers (notably folio/values/registry.ts's
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
# folio/values/registry.ts and any other consumer that indexes
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
    # `auto` is the DEFAULT as of 2026-08-28 (bean qou-7e1t, option 3). It was
    # `branching`, which returns an error for A < 2 — there is no interface to
    # peel in a one-nucleon word, so the combiner does not apply — and main()
    # SKIPS any atom with a non-empty `err`. So p and n were requested by
    # DEFAULT_ATOMS, computed by nothing, and silently absent from the table:
    # `atoms_requested` listed nine, `rows` held seven.
    #
    # That absence is what let `low_isotope_mass_table.py` be WIDER than the
    # canonical table it projects from, which is the defect qou-7e1t is about.
    #
    # This is NOT a departure from the "branching is canonical" directive
    # below. `auto` dispatches to `branching` verbatim for every A >= 2, and
    # that was re-measured on this tree before the flip: over all nine
    # DEFAULT_ATOMS at 60 dps, the seven composite values are equal under
    # Python `==` on the mpf — not "agree to a tolerance", identical — while p
    # and n go from an error row to a computed one. Total cost 4.5 s.
    if method == "auto":
        # No single method spans the low-isotope set. Free nucleons
        # (A < 2) need the direct H_3 Hoefsmit path — `laurent_q_rust`
        # (Rust + MPFR via pyhecke_native.tr_m_atomic_mpfr). Composites
        # (A ≥ 2) need the operator-valued `branching` combiner for the
        # color-weighted p-n interface that the atomic σ/σ⁻¹/averaged
        # reducers cannot represent. branching itself routes χ^λ through
        # the Rust MPFR kernel `chi_lambda_all_partitions_mpfr` (it
        # linearity-splits σ − h(½−δ/4)·𝟙 into a sign-0 averaged term
        # plus an identity term, both at ≥ 50 dps), so BOTH sub-paths
        # are Rust-backed and MPFR. The returned `method_used` records
        # the per-atom route ("laurent_q_rust" or "branching").
        eff = "laurent_q_rust" if (Z + N) < 2 else "branching"
        res = compute_tr_m_canonical(
            Z, N, label, dps=dps, timeout_sec=timeout_sec, method=eff,
        )
        # Fall back to the sympy H_3 path when the Rust extension is simply
        # ABSENT. This is narrow on purpose and does NOT reopen the PR #886
        # decision below: #886 declined an automatic chain out of `Case C`,
        # a MATHEMATICAL condition where the Rust kernel is inapplicable and
        # the right answer may differ. A missing `pyhecke_native` is an
        # ENVIRONMENT capability, not a case distinction -- the sympy path
        # computes the same object, and for p and n it agrees exactly with
        # `laurent_q` to every digit printed.
        #
        # Only `auto` falls back. An explicit `--method laurent_q_rust` still
        # errors, because there the caller asked for that kernel by name.
        # `method_used` carries the substitution into the witness so the
        # route is recorded rather than silently swapped.
        val, wall, err, used = res
        # Trigger the sympy fallback when native is ABSENT. As of qou-m7py
        # (2026-08-15) the Rust crate is on convention D and proton-pinned to
        # match the Python side exactly, so the native dispatch no longer
        # REFUSES — the #5055/qou-w8zz divergence guard is resolved. The legacy
        # "NATIVE_DIVERGENCE" markers below are kept only so an older wheel that
        # still raises them lands in this fallback rather than silently skipping
        # the atom (`main()` drops any atom with a non-empty err). The
        # missing-wheel branch ("pyhecke_native missing") is the live case: the
        # sympy path is correct, just slower.
        _native_unavailable = err and (
            "pyhecke_native missing" in err
            or "NATIVE_DIVERGENCE" in err
            or "native divergence" in err.lower()
        )
        if val is None and _native_unavailable:
            v2, w2, e2, u2 = compute_tr_m_canonical(
                Z, N, label, dps=dps, timeout_sec=timeout_sec,
                method="laurent_q",
            )
            if v2 is not None:
                return v2, w2, None, f"{u2} (auto-fallback: {used} unavailable)"
        return res

    if method == "laurent_q_rust":
        try:
            from markov_peel_rust_bridge import (
                tr_M_atomic_rust_full,
                tr_M_atomic_rust_recursive,
            )
            # Honor caller-provided dps when it exceeds the 50-dps
            # production floor; never go below 50 (AGENTS.md §L1
            # mandates ≥ 50 dps for the production trace).  The
            # `dps=0` default from the function signature collapses
            # to 50, matching the implicit policy used in the
            # sibling `laurent_q` / `markov_peel` branches below.
            effective_dps = max(int(dps), 50)
            t0 = time.time()
            tr_mp = tr_M_atomic_rust_full(Z, N, dps=effective_dps)
            if (Z + N) == 1:
                # Guard against a pre-qou-m7py pyhecke_native wheel whose
                # tr_m_atomic_mpfr_cached still substitutes Convention C
                # instead of Convention D (z_D = q^3/(q^2+1)); in that case
                # use tr_M_atomic_rust_recursive (Rust tr_m_word_lq +
                # Convention-D evaluation at the same MPFR precision).
                tr_rec = tr_M_atomic_rust_recursive(Z, N, dps=effective_dps + 10)
                if abs(abs(tr_mp) - abs(tr_rec)) > mp.mpf("1e-6"):
                    s_rec = mp.nstr(tr_rec, effective_dps + 5)
                    with mp.workdps(effective_dps):
                        tr_mp = mp.mpf(s_rec)
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
            # MPFR-50dps evaluation — NEVER f64. Per AGENTS.md §Precision
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
            # Bean qou-4tui (owner ruling Q-AVTQ-1 = 1): route the D (A = 2)
            # row through the 50-dps transfer-matrix path `tr_m_atom_zn`
            # (matching A >= 3 inside `compute_tr_m_via_branching`), so
            # `tr_M_q0_canonical_50dps` on the D row is genuinely ~50 dps
            # instead of the 16-digit NumPy complex128 floor of the A-operator
            # combiner.
            if (Z + N) == 2:
                from tr_m_atom_via_transfer import tr_m_atom_zn
                t0 = time.time()
                tr_atom_mp, _tr_free, _chi, _wall = tr_m_atom_zn(
                    Z, N, dps=mp.mp.dps, q=None,
                )
                return abs(tr_atom_mp), time.time() - t0, None, "branching"
            from canonical_tr_m_via_branching import compute_tr_m_via_branching
            tr_mp, wall, err = compute_tr_m_via_branching(Z, N, q_val=Q_MP)
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
                b = r.get("B_pred_MeV")
                # `mp.mpf(...)` on the STRING, not `float(...)` (bean qou-3wqg).
                # `mass_table_ppb.py` used to compute `B = nu * m_e * Vol` in
                # Python floats and emit a JSON number; it now computes in
                # mpmath and emits a 44-digit decimal string, so lifting it here
                # is lossless where a float() would throw the lift away again.
                # Accepts a bare number too, so a witness written before that
                # port still loads.
                return (mp.mpf(b) if b is not None else None), r.get("origin")
        return None, None
    except (KeyError, json.JSONDecodeError):
        return None, None


def lookup_nucleon_mass_canonical(
    Z: int, N: int, borromean: dict | None = None,
) -> tuple[float | None, str | None]:
    """Canonical absolute nucleon mass for the p / n rows, via the facade.

    `canonical-mass-table-extended` computes |tr_M| but does not self-derive a
    nucleon mass, so the free-nucleon rows have to source theirs. They now come
    from `canonical_mass.nucleon_mass_mev()` — the muon-anchored Hecke energy
    `m_p = 2·(m_μ·F_Bor − 6·m_e)`, CODATA to +1.35 ppb — which is what
    docs/canonical-mass-formula-guardrail.md requires of *every* absolute-mass
    consumer.

    HISTORY (fixed 2026-08-08, bean `qou-7loj`). This function used to read
    `m-p-borromean-verification-50dps.witness.json` and return its
    `m_p_pred_MeV = 965.384` / `m_n_pred_MeV = 966.715` — the
    `m_e·Vol(𝓑₃)/ℏ_q²·λ_A` form the 2026-06-24 ruling deprecated for absolute
    mass. So the table's nucleon rows were 27 MeV (+2.89 %) high while labelled
    `prediction_method=CANONICAL_TRACE`, and that propagated through
    `low_isotope_mass_table.py` into every consumer of the low-isotope table.

    It survived every guard because the deprecated value crossed the boundary
    as **data**: a `json.loads` of a witness path, with no import and no call,
    so `noncanonical_reentry_audit.py` had no AST edge to find, and the formula
    appeared in no prose or docstring for the status guards to read.

    The Borromean-tower figure is not lost — it remains in its own witness,
    which is the right place for a prediction conditional on
    `conj:borromean-baryon-mass-formula`. It is simply no longer served as the
    canonical absolute mass. `borromean` is still accepted so existing call
    sites keep working; it is unused.

    Returns (m_pred_MeV, origin_label) or (None, None).
    """
    del borromean  # retained for call-site compatibility; no longer consulted
    species = {(1, 0): "proton", (0, 1): "neutron"}.get((Z, N))
    if species is None:
        return None, None
    try:
        from canonical_mass import nucleon_mass_mev  # noqa: E402 — facade
        return (
            nucleon_mass_mev(species),
            "canonical_mass facade (muon-anchored Hecke energy)",
        )
    except (ImportError, ValueError, TypeError):
        return None, None


#: Pre-2026-08-08 name. Kept so an older call site fails loudly at review time
#: rather than silently resurrecting the +2.89 % route.
lookup_nucleon_mass_borromean = lookup_nucleon_mass_canonical


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
        choices=["auto", "laurent_q_rust", "markov_peel", "laurent_q",
                 "rust_f64", "rust_mpfr", "branching"],
        default="auto",
        help=(
            "Computation method. `auto` routes per-atom: composites (A>=2) -> "
            "`branching` (the operator-valued Wenzl combiner, canonical per user "
            "directive, replacing empirical fits), nucleons (A<2) -> "
            "`laurent_q_rust` (Rust+MPFR H_3 Hoefsmit). Both Rust-backed MPFR. "
            "`branching` alone is the same computation with the A<2 rows dropped."
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
    parser.add_argument(
        "--allow-partial-canonical",
        action="store_true",
        help=(
            "Permit writing the canonical witness from a RESTRICTED --atoms "
            "set. Off by default: see the guard below. Only pass this if you "
            "intend the canonical table to shrink."
        ),
    )
    parser.add_argument(
        "--allow-precision-downgrade",
        action="store_true",
        help=(
            "Permit REPLACING the committed canonical witness with one built "
            "at a LOWER --target-dps. Off by default: see the guard below. "
            "Only pass this if you intend the canonical table to get coarser."
        ),
    )
    args = parser.parse_args()

    # dps policy:
    #   - markov_peel: f64-substrate via sp.Float(str(Q_FLOAT), 50)
    #   - laurent_q / laurent_q_rust: enforced MPFR-50dps via dispatcher
    #     (see compute_tr_m_canonical:147 — effective_dps=max(dps, 50))
    #   - rust_f64: f64 dps=0; rust_mpfr: MPFR dps=50
    if args.method in ("laurent_q", "laurent_q_rust", "auto"):
        dps = 50
    else:
        dps = 50 if args.precision == "mpfr" else 0

    label_to_ZN = {label: (Z, N) for Z, N, label in DEFAULT_ATOMS}
    label_to_ZN.update({"proton": (1, 0), "neutron": (0, 1)})
    requested = [s.strip() for s in args.atoms.split(",") if s.strip()]

    # An int: this is the paper's declared CAL-2 propagation floor, a stated
    # threshold rather than a computed quantity, and `780.0` would otherwise
    # be the last raw float64 in this witness. `atlas_render_canonical_table`
    # already reads it through `int(...)`.
    paper_floor_ppb = 780
    paper_floor_dps = float(-mp.log10(mp.mpf(paper_floor_ppb) * mp.mpf("1e-9")))  # float64-ok: console banner only ("~6.1 dps"), never witnessed
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
        # `branching` is this script's DEFAULT method and `auto` is the
        # documented route for mixed nucleon+composite sets, yet neither had
        # an entry -- so the default invocation wrote "unknown method
        # 'branching'" into its own witness `description`, i.e. the provenance
        # string disclaimed the run that produced it.
        "branching": "operator-valued Wenzl branching combiner (canonical "
                     "pipeline) + mpmath y_λ",
        "auto": "per-atom route: A<2 -> direct H_3 Hoefsmit "
                "(laurent_q_rust, falling back to laurent_q when "
                "pyhecke_native is absent); A>=2 -> operator-valued Wenzl "
                "branching combiner; + mpmath y_λ",
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
    #: Labels of the rows that actually landed in `records`, in the same order.
    #: Kept alongside rather than read back off the records, because a record
    #: carries (Z, N) but not the `--atoms` label the registry keys on.
    computed_labels: list[str] = []
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
            pred, origin = lookup_nucleon_mass_canonical(Z, N)
            # CODATA reference from codata_constants, not from the Borromean
            # witness: that witness is the deprecated Vol·ρ route (qou-7loj),
            # and sourcing the *reference* from it too was what kept the row's
            # err_ppm looking self-consistent while the prediction was 2.89 %
            # off the canonical value.
            try:
                from codata_constants import (  # noqa: E402
                    M_N_MEV_VALIDATION, M_P_MEV_VALIDATION,
                )
                ref = mp.mpf(str(
                    M_P_MEV_VALIDATION if (Z, N) == (1, 0) else M_N_MEV_VALIDATION
                ))
            except (ImportError, TypeError, ValueError):
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
                fmt(pred, dps=50) if is_nucleon and pred is not None
                else (str(pred) if pred is not None else None)
            ),
            # `fmt` (not `str(float(...))`) — bean qou-3wqg. These are mpf now:
            # `ref` comes from the un-`float()`-ed AME constants above and
            # `pred` is lifted from mass_table_ppb's 44-digit decimal string, so
            # the subtraction carries real precision and `fmt` writes it out at
            # OUTPUT_DPS. This is NOT the stringify-a-float move the audit
            # forbids — that was the earlier attempt here, and it was reverted
            # precisely because `pred` was still a float at the time.
            B_AME_MeV=fmt(ref) if ref is not None else None,
            err_MeV=fmt(err_val) if err_val is not None else None,
            err_pct=fmt(err_pct_val) if err_pct_val is not None else None,
            err_ppb=fmt(err_ppb_val) if err_ppb_val is not None else None,
            err_ppm=fmt(err_ppm_val) if err_ppm_val is not None else None,
            # Provenance reflects actual method used (Copilot review).
            chi_cache_witness=(
                f"(computed live via {method_used})"
            ),
        )
        records.append(record.to_dict())
        computed_labels.append(atom_str)

        tr_m_str = fmt(tr_m, dps=15)  # display-only, full precision via fmt
        # float() on BOTH console columns is display-only: mpf implements no
        # `__format__`, so `f"{x:.4f}"` raises once the qou-3wqg lift makes
        # these mpf, and the console shows 4 decimals either way. The witness
        # columns take the mpf path above — do not copy either cast into a
        # record. `pred` needed this the moment the root lift landed; `ref`
        # needed it when B_AME_MEV stopped being wrapped in float().
        pred_str = f"{float(pred):.4f}" if pred is not None else "—"  # float64-ok: console formatting only (see comment above)
        ame_str = f"{float(ref):.4f}" if ref is not None else "—"  # float64-ok: console formatting only (see comment above)
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
            "mpfr" if args.method in ("laurent_q", "laurent_q_rust",
                                      "markov_peel", "branching", "auto")
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
        # Names WHICH route the p / n `prediction_MeV_50dps` came from, because
        # the corpus has two and they disagree by ~555x on m_n. Both reproduce
        # on current main, and the split is deliberate — not a staleness bug:
        #
        #   this table, via canonical_mass.nucleon_mass_mev()
        #     m_n = 939.5658930680   ->  +501 ppb   (flavour-split identity)
        #   per_observable_100x_status.py "Path C" (that file, line ~533)
        #     m_n = 939.565422788    ->  +0.90 ppb  (m_n = m_p + Q_beta + m_e)
        #
        # Path C's own comment there calls it "8x better than the
        # substrate-identity's", so the L2 dashboard prefers it knowingly.
        #
        # Recorded when the p / n rows were restored (bean `qou-7e1t` option 3).
        # Before that this table had no nucleon rows, so the disagreement was
        # unstatable rather than absent — a reader diffing the two witnesses
        # would have found a 555x gap on a scored observable with nothing in
        # either file saying they compute it differently. Adjudication of which
        # route should be canonical is bean `qou-khue`; this is the pointer, not
        # the answer.
        .add_parameter(
            "nucleon_prediction_route",
            "canonical_mass.nucleon_mass_mev (muon-anchored Hecke energy, "
            "flavour-split substrate identity). NOT the Path C route "
            "(m_p + Q_beta + m_e) used by per-observable-100x-status; the two "
            "differ by ~555x on m_n. See bean qou-khue.",
        )
        .add_data("rows", records)
        # Nuclide-keyed view of the SAME records, so consumers can address a
        # row by what it is rather than by where it sits (bean `qou-xwet`).
        #
        # `data.rows` is ordered by DEFAULT_ATOMS and a comment has long asked
        # callers not to reorder it. That guard was never enough: it addresses
        # reordering, while what actually happened was a second producer
        # SHRINKING the set, which shifts every index without reordering
        # anything. `registry.ts`'s `B_2H_AME_MeV` pin at `data.rows.2` then
        # addressed 3He for eight weeks under a description naming deuterium.
        #
        # Keys are the `--atoms` labels (p, n, D, T, 3He, ...). A key is absent
        # when its row is absent, so a pin against a missing nuclide fails
        # loudly instead of silently reading its neighbour. `rows` is kept
        # as-is: it is the ordered presentation, and removing it would break
        # every existing reader for no gain.
        #
        # SCALARS ONLY, deliberately. Mirroring whole records here doubled the
        # witness (68 KB -> 133 KB) to say everything twice; the bulk is
        # `knot_operators` and `braid_word_canonical`, which no pin addresses.
        # This view exists to be ADDRESSED, not to duplicate provenance -- a
        # reader wanting the full record still goes to `rows`.
        .add_data("rows_by_nuclide", {
            label: {k: rec[k] for k in _PINNABLE_COLUMNS if k in rec}
            for label, rec in zip(computed_labels, records)
        })
        .add_data("n_atoms_computed", len(records))
    )

    # GUARD — a restricted --atoms run may NOT overwrite the canonical witness
    # (bean `qou-xwet`).
    #
    # The output filename is FIXED (see the module docstring), so ANY run of
    # this script rewrites `canonical-mass-table-extended.witness.json`
    # wholesale, including a run that was asked for a handful of atoms. That
    # is not hypothetical: `low_isotope_mass_table.py` drove this script with
    # `--atoms p,n,D,T,3He` purely as a speed optimisation, and the resulting
    # five-row table replaced the canonical nine-row one on `main` — 4He and
    # every A >= 5 row silently disappeared, committed under two commit
    # messages that only discussed the low-isotope table.
    #
    # It also broke a consumer without tripping anything: `registry.ts` pins
    # `B_2H_AME_MeV` POSITIONALLY at `data.rows.2.B_AME_MeV`, so the row set
    # moving underneath it silently repoints that value at a different
    # nuclide. (The ordering comment on DEFAULT_ATOMS guards against
    # *reordering the list*; it cannot see a caller shrinking the set.)
    #
    # So: refuse. A partial table is fine to compute and print, it is just not
    # the canonical artifact. Callers that genuinely want a subset should
    # filter the full table downstream — which is exactly what
    # `low_isotope_mass_table.project_to_low_isotope()` already does.
    _default_labels = [label for _, _, label in DEFAULT_ATOMS]
    _missing = [lab for lab in _default_labels if lab not in requested]
    if _missing and not args.allow_partial_canonical:
        print()
        print("  REFUSING to write the canonical witness from a partial run.")
        print(f"    requested : {','.join(requested)}")
        print(f"    missing   : {','.join(_missing)}")
        print("  The output path is fixed, so this would REPLACE the canonical")
        print("  table with a subset and silently repoint every positional")
        print("  consumer of data.rows (see bean qou-xwet).")
        print("  Run with the full default --atoms set and filter downstream,")
        print("  or pass --allow-partial-canonical if the shrink is intended.")
        return 2

    # Sibling guard: refuse to REPLACE the canonical witness with a
    # LOWER-PRECISION one.
    #
    # The partial-write guard above closes the row-subset shrink (bean
    # `qou-xwet`). It does not see the other axis. The output path is equally
    # fixed for precision, so a caller passing a smaller `--target-dps`
    # overwrites the canonical artifact with a coarser computation, and nothing
    # in the run says an artifact was downgraded.
    #
    # Measured, not hypothetical (bean `qou-7e1t`). `low_isotope_mass_table.py`
    # re-runs this script by default with its OWN defaults —
    # `--method auto --target-dps 11` — over a committed canonical table built
    # at `--target-dps 60`:
    #
    #     target_dps  60 -> 11        method  branching -> auto
    #     rows         7 ->  9        (p, n compute under `auto`)
    #
    # Note the row count moves the OTHER way, so the partial guard above stays
    # silent by construction: the replacement is WIDER in coverage while being
    # coarser in precision. That combination is what made this survive the
    # qou-xwet fix, and it is why the check has to be on dps specifically
    # rather than on "does the table look smaller".
    #
    # Refuse rather than warn: a warning in a subprocess whose stdout is
    # already dozens of lines is exactly what got missed.
    _existing_dps = None
    try:
        _existing_path = _pb.witness_path(
            "canonical-mass-table-extended.witness.json", HERE)
        if _existing_path.exists():
            _existing_dps = (json.loads(_existing_path.read_text())
                             .get("parameters", {}).get("target_dps"))
    except Exception:  # noqa: BLE001 — a missing/unreadable prior artifact is
        _existing_dps = None  # not a reason to block the first write.

    if (_existing_dps is not None
            and isinstance(_existing_dps, int)
            and args.target_dps < _existing_dps
            and not args.allow_precision_downgrade):
        print()
        print("  REFUSING to overwrite the canonical witness at LOWER precision.")
        print(f"    committed target_dps : {_existing_dps}")
        print(f"    this run             : {args.target_dps}")
        print("  The output path is fixed, so this would REPLACE the canonical")
        print("  table with a coarser computation. The partial-write guard")
        print("  above cannot catch it — a coarser run can be WIDER in row")
        print("  coverage (see bean qou-7e1t).")
        print("  Re-run at >= the committed target_dps, or pass")
        print("  --allow-precision-downgrade if the downgrade is intended.")
        return 2

    out = builder.save()
    print()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

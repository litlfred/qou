#!/usr/bin/env python3
"""
Shared SDP (Lasserre moment-matrix) lift for LP(PSD) files.

This module implements the engine side of
``prop:confinement-sdp`` (content/quantum-observable-universe/
particle-interactions/confinement-sdp.md): the scalar LP with
componentwise G·x ≥ 0 is the rank-1 projection of the full matrix
SDP with Φ ⪰ 0 and per-block Frobenius positivity.  Here we run
the Lasserre moment-matrix relaxation (M = [[1, xᵀ], [x, X]] ⪰ 0,
with tr(G·X) ≥ 0) as the SDP-feasibility certificate.

The LPs in ``confinement-lp.py``, ``nuclear-binding-lp.py``,
``lp-constrained-6he.py``, ``molecular-frobenius-lp.py``,
``ch-bond-lp.py``, and ``integer-lp-gluon.py`` all enforce Frobenius
positivity of an H_3(q) NF vector x via the componentwise constraint
G · x ≥ 0, where G is the 6×6 Markov-trace Gram matrix.

At q₀ ≈ 1.11, G has a negative eigenvalue (min eig ≈ -0.74), so the
componentwise constraint is strictly weaker than the quadratic
Frobenius positivity  xᵀ G x ≥ 0.  The batch audit
(``sdp_lift_audit.py``) confirmed that every one of the 10 flagged
LP cases produces a solution violating xᵀ G x ≥ 0.

This module provides a drop-in SDP lift: given the LP data
``(c, A_eq, b_eq, G, bounds)``, it runs the Lasserre moment-matrix
relaxation with the extra constraint ``tr(G · X) ≥ 0``, returning
both LP and SDP solutions plus a validity report.

Usage from an LP script:

    from sdp_moment_lift import lp_vs_sdp_report, save_sdp_witness
    rep = lp_vs_sdp_report(c=TR_M_BASIS, G=G,
                              A_eq=np.ones((1, 6)),
                              b_eq=np.array([target_net]))
    print(rep.summary_lines())
    save_sdp_witness(out_path, rep, context={"atom": "proton"})
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from datetime import datetime, timezone
from typing import Any

import numpy as np

try:
    import cvxpy as cp
    HAVE_CVXPY = True
except ImportError:
    HAVE_CVXPY = False


# ── Rust Clarabel moment-SDP backend (no cvxpy dependency) ───────

def _find_moment_sdp_bin(explicit: str | None = None) -> str:
    """Locate the ``clarabel-confinement-moment-sdp`` binary."""
    import os

    if explicit:
        return explicit
    env = os.environ.get("QOU_CLARABEL_MOMENT_SDP_BIN")
    if env:
        return env
    rel = (Path("tools") / "hecke-engine" / "target" / "release"
           / "clarabel-confinement-moment-sdp")
    for parent in Path(__file__).resolve().parents:
        cand = parent / rel
        if cand.exists():
            return str(cand)
    raise FileNotFoundError(
        "clarabel-confinement-moment-sdp not found. Build via\n"
        "  cargo build --release --manifest-path tools/hecke-engine/Cargo.toml "
        "--features clarabel-sdp --bin clarabel-confinement-moment-sdp\n"
        "or set $QOU_CLARABEL_MOMENT_SDP_BIN."
    )


def solve_moment_sdp_clarabel(c, G, n_target, *, lo=-10.0, hi=10.0,
                              bin_path: str | None = None) -> dict:
    """Solve the Lasserre moment SDP via the Rust Clarabel CLI (f64).

    Same moment lift as ``lp_vs_sdp_report`` (M = [[1, xᵀ], [x, X]] ⪰ 0,
    X ⪰ 0, tr(G·X) ≥ 0) but a **direct Clarabel call with no cvxpy
    dependency** — `prop:confinement-sdp` solved by `#4`'s Rust engine
    (`operator_selection_sdp::solve_confinement_moment_sdp`).

    Cross-checked to ~1e-14 against the cvxpy+CLARABEL path
    (`operator_selection_sdp::tests::moment_sdp_known_case`).

    Returns ``{x_star, xtgx, tr_gx, objective, feasible, status}``.
    """
    import subprocess

    c = np.asarray(c, dtype=float).flatten()
    G = np.asarray(G, dtype=float)
    payload = {
        "c": c.tolist(), "G": G.tolist(),
        "n_target": float(n_target), "lo": float(lo), "hi": float(hi),
    }
    proc = subprocess.run(
        [_find_moment_sdp_bin(bin_path)],
        input=json.dumps(payload), capture_output=True, text=True,
    )
    out = json.loads(proc.stdout) if proc.stdout.strip() else {}
    if proc.returncode != 0 or "error" in out:
        raise RuntimeError(
            out.get("error", proc.stderr.strip() or "moment SDP solve failed")
        )
    return out


@dataclass
class SdpLiftReport:
    """LP vs SDP comparison for a single problem instance."""
    label: str = ""
    lp_status: str = ""
    sdp_status: str = ""
    lp_objective: float = float("nan")
    sdp_objective: float = float("nan")
    lp_x: list[float] = field(default_factory=list)
    sdp_x: list[float] = field(default_factory=list)
    lp_xTGx: float = float("nan")       # quadratic Frobenius check on LP
    sdp_xTGx: float = float("nan")      # quadratic Frobenius check on SDP
    sdp_tr_GX: float = float("nan")     # moment-matrix Frobenius trace
    sdp_moment_rank: int = 0
    gram_min_eigenvalue: float = float("nan")

    @property
    def lp_frobenius_valid(self) -> bool:
        return self.lp_xTGx >= -1e-9

    @property
    def sdp_frobenius_valid(self) -> bool:
        return self.sdp_tr_GX >= -1e-9

    def summary_lines(self) -> list[str]:
        tag = "✓" if self.lp_frobenius_valid else "✗ INVALID"
        return [
            f"  ── SDP lift validation ({self.label}) ──",
            (f"  LP:  obj={self.lp_objective:+.6f}  "
             f"xᵀGx={self.lp_xTGx:+.6f} [{tag}]"),
            (f"  SDP: obj={self.sdp_objective:+.6f}  "
             f"tr(G·X)={self.sdp_tr_GX:+.6f}  "
             f"rank={self.sdp_moment_rank}"),
            (f"  Gram min eig = {self.gram_min_eigenvalue:+.4f}"
             f" ({'G is not PSD' if self.gram_min_eigenvalue < -1e-9 else 'G is PSD'})"),
        ]


def lp_vs_sdp_report(*, c: np.ndarray, G: np.ndarray,
                       A_eq: np.ndarray, b_eq: np.ndarray,
                       bounds: tuple[float, float] = (-10.0, 10.0),
                       label: str = "") -> SdpLiftReport:
    """Run LP + Lasserre-moment SDP on the same problem; return diff.

    The SDP adds the quadratic Frobenius constraint tr(G · X) ≥ 0
    via a moment-matrix PSD variable  M = [[1, xᵀ], [x, X]] ⪰ 0.
    """
    if not HAVE_CVXPY:
        raise ImportError("cvxpy required for sdp_moment_lift")
    c = np.asarray(c, dtype=float).flatten()
    G = np.asarray(G, dtype=float)
    n = c.size
    assert G.shape == (n, n), f"G shape {G.shape} != ({n},{n})"
    A_eq = np.asarray(A_eq, dtype=float).reshape(-1, n)
    b_eq = np.asarray(b_eq, dtype=float).flatten()

    rep = SdpLiftReport(label=label)
    rep.gram_min_eigenvalue = float(np.min(np.linalg.eigvals(G).real))

    # ── LP ────────────────────────────────────────────────────
    x = cp.Variable(n)
    lp_constraints = [
        A_eq @ x == b_eq,
        G @ x >= 0,
        x >= bounds[0],
        x <= bounds[1],
    ]
    lp_prob = cp.Problem(cp.Minimize(c @ x), lp_constraints)
    try:
        lp_prob.solve(solver="HIGHS")
        rep.lp_status = lp_prob.status
        if lp_prob.status in {"optimal", "optimal_inaccurate"}:
            lp_x = np.asarray(x.value).flatten()
            rep.lp_x = lp_x.tolist()
            rep.lp_objective = float(lp_prob.value)
            rep.lp_xTGx = float(lp_x @ G @ lp_x)
    except cp.error.SolverError as e:
        rep.lp_status = f"solver_error: {e}"

    # ── SDP (Lasserre moment relaxation) ──────────────────────
    x = cp.Variable(n)
    X = cp.Variable((n, n), symmetric=True)
    M = cp.bmat([[np.ones((1, 1)),
                    cp.reshape(x, (1, n), order="C")],
                   [cp.reshape(x, (n, 1), order="C"), X]])
    sdp_constraints = [
        M >> 0,
        X >> 0,
        A_eq @ x == b_eq,
        G @ x >= 0,
        cp.trace(G @ X) >= 0,
        x >= bounds[0],
        x <= bounds[1],
    ]
    sdp_prob = cp.Problem(cp.Minimize(c @ x), sdp_constraints)
    try:
        sdp_prob.solve(solver="CLARABEL")
        rep.sdp_status = sdp_prob.status
        if sdp_prob.status in {"optimal", "optimal_inaccurate"}:
            sdp_x = np.asarray(x.value).flatten()
            sdp_X = np.asarray(X.value)
            rep.sdp_x = sdp_x.tolist()
            rep.sdp_objective = float(sdp_prob.value)
            rep.sdp_xTGx = float(sdp_x @ G @ sdp_x)
            rep.sdp_tr_GX = float(np.trace(G @ sdp_X))
            rep.sdp_moment_rank = int(np.sum(
                np.linalg.svd(sdp_X, compute_uv=False) > 1e-6))
    except cp.error.SolverError as e:
        rep.sdp_status = f"solver_error: {e}"

    return rep


def save_sdp_witness(out_path: Path,
                       reports: list[SdpLiftReport] | SdpLiftReport,
                       context: dict[str, Any] | None = None):
    """Persist one or more SdpLiftReports as a witness JSON."""
    if isinstance(reports, SdpLiftReport):
        reports = [reports]
    witness = {
        "computation": out_path.stem,
        "description": (
            "SDP (Lasserre moment-matrix) lift of the LP.  Adds the "
            "quadratic Frobenius positivity constraint tr(G·X) ≥ 0 "
            "that the componentwise LP cannot express (G has a "
            "negative eigenvalue at q₀, so G·x ≥ 0 is strictly "
            "weaker than xᵀG x ≥ 0).  See sdp_moment_lift.py."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "context": context or {},
        "reports": [asdict(r) for r in reports],
    }
    out_path.write_text(json.dumps(witness, indent=2, default=str))


if __name__ == "__main__":
    # Smoke test: replicate confinement_sdp on the proton case.
    import sys
    from pathlib import Path as _P
    sys.path.insert(0, str(_P(__file__).parent))
    import importlib.util
    import os as _os
    spec = importlib.util.spec_from_file_location(
        "_conf", _P(__file__).parent / "confinement-lp.py")
    _old = _os.dup(1)
    _null = _os.open(_os.devnull, _os.O_WRONLY)
    _os.dup2(_null, 1)
    try:
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    finally:
        _os.dup2(_old, 1)
        _os.close(_null)
        _os.close(_old)
    G = mod.G
    TR_M = np.asarray(mod.TR_M_BASIS)
    proton_confined = mod.apply_typed_crossings(mod.b3_vec,
                                                    ['u', 'u', 'd'])
    proton_net = float(np.sum(proton_confined))
    rep = lp_vs_sdp_report(c=TR_M, G=G, A_eq=np.ones((1, 6)),
                              b_eq=np.array([proton_net]),
                              label="confinement/proton (smoke test)")
    for line in rep.summary_lines():
        print(line)

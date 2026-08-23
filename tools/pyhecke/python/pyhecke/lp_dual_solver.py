"""
LP-dual solver — first-class infrastructure for operator-selection LPs.

Per `prop:operator-selection-lp`, every knot-operator-selection block
must compute BOTH primal and dual:

    primal: min Σ t_i x_i  s.t.  Σ x_i = n_target,  Gx ≥ 0,  x_i ≥ -M
    dual:   max n_target · y_0  s.t.  y_0 + Σ G_{ji} y_i ≤ t_j,  y_i ≥ 0

The dual variables are the SHADOW PRICES:
    y_0^*  = marginal cost of unit target mass (binding-energy density)
    y_i^*  = saturation price of channel i (zero if slack, positive if tight)

The active demand channels are A = {i : y_i^* > 0} — the
"most receptive sub-braids on the shell".

Strong duality (no LP duality gap):
    Σ t_i x_i^*  =  n_target · y_0^*

This module is the canonical entry point. Any operator-selection
compute SHOULD use `solve_operator_selection_lp` to get a witness
that includes BOTH primal (coefficients) and dual (shadow prices).

The `verify_dual_present` validator checks that any operator-selection
witness JSON includes the required dual fields, so the LP dual
computation cannot be silently omitted again.
"""
from __future__ import annotations

import json
import os
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import numpy as np


@dataclass
class LpDualResult:
    """Both sides of the operator-selection LP, with strong-duality check.

    Required fields per `prop:operator-selection-lp`:
      x_star          — primal optimum (knot operator coefficients)
      y0_star         — dual: shadow price of net constraint
      y_star          — dual: shadow prices of Frobenius constraints (≥ 0)
      active_set      — indices i with y_star[i] > tol
      primal_obj      — Σ t_i x_i^*
      dual_obj        — n_target · y0^*
      duality_gap     — |primal_obj - dual_obj|  (should be ~0)
    """
    x_star: list[float]
    y0_star: float
    y_star: list[float]
    active_set: list[int]
    primal_obj: float
    dual_obj: float
    duality_gap: float
    feasible: bool
    # Full-precision decimal strings, populated ONLY by the clarabel-MPFR
    # backend. The solver already works at `prec_bits` (~50 dps) and already
    # returns its answer as decimal strings; until now `_lp_result_from_dict`
    # ran them through `float()` and threw ~35 digits away at the very last
    # step, so no caller could get a float64-free result no matter how the
    # inputs were supplied (bean qou-t0rf). `None` on the scipy path, which
    # genuinely has nothing beyond f64 to report.
    x_star_str: Optional[list] = None
    y0_star_str: Optional[str] = None
    y_star_str: Optional[list] = None
    primal_obj_str: Optional[str] = None
    dual_obj_str: Optional[str] = None
    duality_gap_str: Optional[str] = None
    #: Set only when the false-infeasible rescue fired: the power of two the
    #: cost vector was scaled by before re-solving. `None` on a normal solve.
    #: Present so a witness records that the raw solve was rejected rather
    #: than the rescue happening silently.
    rescaled_by_pow2: Optional[int] = None
    #: Set when the Rust tolerance ladder had to loosen to converge; carries
    #: the full ladder so a witness records the tolerance its numbers actually
    #: meet rather than the one that was requested.
    loosened_status: Optional[str] = None
    # WHICH SOLVER PRODUCED THIS, and at what width.
    #
    # `backend="auto"` picks clarabel-MPFR when the Rust binary is on disk and
    # falls through to scipy f64 when it is not — silently, by default. So the
    # same producer run in CI, in a fresh container, and on a developer box
    # could write witnesses differing by ~28 orders of magnitude in residual
    # with nothing in the file saying which had happened. A witness that does
    # not record how it was solved cannot be told apart from one solved the
    # other way.
    #
    # `"clarabel-mpfr"` with `precision_bits` set, or `"scipy-highs"` with
    # `precision_bits = 53`. Always emitted by `to_dict()`.
    backend: Optional[str] = None
    precision_bits: Optional[int] = None

    def to_dict(self) -> dict:
        """Serialize both sides of the LP.

        The numeric fields are kept verbatim: every existing consumer does
        arithmetic on them (`sum(r["y_star"] ...)`, `r["duality_gap"] < 1e-6`),
        so turning them into strings here would break readers silently rather
        than loudly.

        When the clarabel-MPFR backend supplied full-precision decimals, they
        are emitted ALONGSIDE as `*_str`. Before this, `_lp_result_from_dict`
        kept them on the dataclass (bean `qou-t0rf`) but `to_dict` dropped them
        again, so a ~50-dps solve still reached its witness as f64 — the same
        truncation qou-t0rf fixed one layer up, re-applied at the last step.
        `None` on the scipy path, which has nothing beyond f64 to report; the
        key is omitted rather than emitted as null, so a reader can use
        `"y_star_str" in d` to ask "was this solved at precision?".
        """
        d = {
            "x_star": list(self.x_star),
            "y0_star": float(self.y0_star),
            "y_star": list(self.y_star),
            "active_set": list(self.active_set),
            "primal_obj": float(self.primal_obj),
            "dual_obj": float(self.dual_obj),
            "duality_gap": float(self.duality_gap),
            "feasible": bool(self.feasible),
        }
        if self.backend is not None:
            d["backend"] = self.backend
        if self.precision_bits is not None:
            d["precision_bits"] = int(self.precision_bits)
        if self.rescaled_by_pow2 is not None:
            d["rescaled_by_pow2"] = int(self.rescaled_by_pow2)
        if self.loosened_status is not None:
            d["loosened_status"] = str(self.loosened_status)
        for key, val in (
            ("x_star_str", self.x_star_str),
            ("y0_star_str", self.y0_star_str),
            ("y_star_str", self.y_star_str),
            ("primal_obj_str", self.primal_obj_str),
            ("dual_obj_str", self.dual_obj_str),
            ("duality_gap_str", self.duality_gap_str),
        ):
            if val is not None:
                d[key] = list(val) if isinstance(val, (list, tuple)) else str(val)
        return d


#: Every full-precision companion either result class can carry. Kept as one
#: tuple so a new `*_str` field is picked up by `provenance()` automatically
#: rather than needing a matching edit in ten producers.
PROVENANCE_STR_FIELDS = (
    "x_star_str", "y0_star_str", "y_star_str",
    "X_star_str", "Z_star_str", "eigenvalues_str",
    "primal_obj_str", "dual_obj_str", "duality_gap_str",
)


def provenance(res) -> dict:
    """Solver provenance + full-precision companions, to spread into a witness row.

    Producers do not all serialize via `to_dict()`. Most cherry-pick the
    numeric fields off the result and `float()`-cast each one, which drops
    `backend`, `precision_bits` and every `*_str` companion at the last
    step. That is the *same* truncation `qou-t0rf` fixed on the dataclass
    and this module's `to_dict` docstring describes fixing again one layer
    up — recurring a third time, in the producers. Spreading `provenance(res)`
    into the row keeps "which solver, at what precision, with what digits"
    attached to the numbers it describes.

    Keys are omitted rather than emitted as null, so a reader can ask
    `"backend" in row` / `"y_star_str" in row` and get a truthful answer;
    an all-f64 scipy solve contributes `backend`/`precision_bits` only.
    """
    # Accepts either a result dataclass or its `to_dict()`: producers hold
    # both forms, and a helper that silently returned `{}` for the dict form
    # would be an absent check indistinguishable from a passing one.
    if isinstance(res, dict):
        def _get(key):
            return res.get(key)
    else:
        def _get(key):
            return getattr(res, key, None)

    out: dict = {}
    backend = _get("backend")
    if backend is not None:
        out["backend"] = str(backend)
    bits = _get("precision_bits")
    if bits is not None:
        out["precision_bits"] = int(bits)
    resc = _get("rescaled_by_pow2")
    if resc is not None:
        out["rescaled_by_pow2"] = int(resc)
    loose = _get("loosened_status")
    if loose is not None:
        out["loosened_status"] = str(loose)
    for key in PROVENANCE_STR_FIELDS:
        val = _get(key)
        if val is not None:
            out[key] = list(val) if isinstance(val, (list, tuple)) else str(val)
    return out


def solve_frobenius_dual_lp(
    t: np.ndarray,
    G: np.ndarray,
    n_target: float,
    u_demand: np.ndarray,
    *,
    M_bound: float = 1e6,
    dual_tol: float = 1e-9,
) -> LpDualResult:
    """Frobenius-dual minimum-action LP — TIGHTER than the basic
    Gx ≥ 0 inequality formulation.

    Problem:
        min t · x
        s.t. 1ᵀ x = n_target
             G x = u_demand          (equality, not inequality)

    The equality on G x = u_demand selects the unique x whose
    Frobenius pairing with the basis matches a target "demand
    vector" u_demand (typically the demand profile at the magic
    shell). This is the closed-form Frobenius-dual minimum-action
    formulation per `confinement-operator-selection.py`.

    Dual:
        max n_target · y_0 + u_demand · y
        s.t. y_0 · 1 + Gᵀ y = t      (no positivity on y here)

    Both y_0 and the y vector are returned; strong duality verified.
    """
    from scipy.optimize import linprog

    t = np.asarray(t, dtype=float)
    G = np.asarray(G, dtype=float)
    u = np.asarray(u_demand, dtype=float)
    d = len(t)

    c = t.copy()
    # Combined equalities: net + Frobenius-dual demand
    A_eq = np.vstack([np.ones((1, d)), G])
    b_eq = np.concatenate([[n_target], u])
    res = linprog(
        c=c, A_eq=A_eq, b_eq=b_eq,
        bounds=[(-M_bound, None)] * d,
        method="highs",
    )
    if not res.success:
        return LpDualResult(
            x_star=[float("nan")] * d,
            y0_star=float("nan"),
            y_star=[float("nan")] * d,
            active_set=[],
            primal_obj=float("nan"),
            dual_obj=float("nan"),
            duality_gap=float("nan"),
            feasible=False,
            backend="scipy-highs",
            precision_bits=53,
        )

    x_star = np.asarray(res.x)
    primal_obj = float(c @ x_star)
    # eq.marginals: first is y_0, remaining d are y_i
    eq_marginals = np.asarray(res.eqlin.marginals)
    y0_star = float(eq_marginals[0])
    y_star = eq_marginals[1:].tolist()
    active_set = [i for i, y in enumerate(y_star) if abs(y) > dual_tol]
    dual_obj = float(n_target * y0_star + u @ np.asarray(y_star))
    duality_gap = abs(primal_obj - dual_obj)

    return LpDualResult(
        x_star=list(x_star),
        y0_star=y0_star,
        y_star=y_star,
        active_set=active_set,
        primal_obj=primal_obj,
        dual_obj=dual_obj,
        duality_gap=duality_gap,
        feasible=True,
        # This is the SUCCESS path and it recorded nothing until 2026-08-23,
        # while the infeasible branch above already set `backend`. So a
        # successful f64 solve through this entry point was invisible to the
        # float64 gate and only a FAILED one was caught — an absent check
        # indistinguishable from a passing one, in the gate itself.
        # `solve_frobenius_dual_lp` is public and has live callers
        # (`frobenius_repose_probe.py`, `all_nuclides_sdp_admissibility.py`).
        backend="scipy-highs",
    )


def _find_clarabel_lp_bin(explicit: Optional[str] = None) -> str:
    """Locate the ``clarabel-operator-selection-lp`` binary.

    Search order: explicit arg, ``$QOU_CLARABEL_LP_BIN``, then the known
    ``tools/hecke-engine/target/release/`` path walking up from this file.
    """
    import os

    if explicit:
        return explicit
    env = os.environ.get("QOU_CLARABEL_LP_BIN")
    if env:
        return env
    rel = Path("tools") / "hecke-engine" / "target" / "release" / "clarabel-operator-selection-lp"
    for parent in Path(__file__).resolve().parents:
        cand = parent / rel
        if cand.exists():
            return str(cand)
    raise FileNotFoundError(
        "clarabel-operator-selection-lp not found. Build it via\n"
        "  cargo build --release --manifest-path tools/hecke-engine/Cargo.toml "
        "--features clarabel-mpfr --bin clarabel-operator-selection-lp\n"
        "or set $QOU_CLARABEL_LP_BIN."
    )


def _lp_result_from_dict(out: dict, d: int) -> LpDualResult:
    """Build an ``LpDualResult`` from the clarabel binding/CLI output dict."""
    if not out or "error" in out or not out.get("feasible", False):
        return LpDualResult(
            x_star=[float("nan")] * d, y0_star=float("nan"),
            y_star=[float("nan")] * d, active_set=[],
            primal_obj=float("nan"), dual_obj=float("nan"),
            duality_gap=float("nan"), feasible=False,
            # An infeasible verdict is a claim about the LP, and which solver
            # made it matters — clarabel returns false infeasibles on
            # badly-conditioned costs where HiGHS succeeds. Recording the
            # backend is what let that be diagnosed rather than believed.
            backend="clarabel-mpfr", precision_bits=None,
        )
    return LpDualResult(
        x_star=[float(v) for v in out["x_star"]],
        y0_star=float(out["y0_star"]),
        y_star=[float(v) for v in out["y_star"]],
        active_set=[int(i) for i in out["active_set"]],
        primal_obj=float(out["primal_obj"]),
        dual_obj=float(out["dual_obj"]),
        duality_gap=float(out["duality_gap"]),
        feasible=True,
        # Keep what the solver actually computed, alongside the f64 view.
        #
        # This used to read `str(out["y0_star"])` -- the *f64* key -- while
        # the genuine MPFR decimals sat right beside it under `y0_star_str`.
        # Both transports emit them (the CLI formats them from the MPFR
        # values; the PyO3 binding returns them as `str`/`list[str]`
        # alongside its f64 convenience view), so the digits were always
        # there and always discarded:
        #
        #   y0_star      0.9999999999997836                    (f64, 17 sig)
        #   y0_star_str  9.999999999997835691118368666860018…e-1  (52 sig)
        #
        # So `qou-t0rf` -- which added these fields to stop `float()`
        # throwing ~35 digits away -- fixed the storage and kept the wrong
        # source, and every `*_str` since has been f64 wearing a string.
        # That is worse than an absent field: a reader takes `*_str` as the
        # authoritative value precisely because it is a string.
        **_str_fields_if_decimal(out),
        backend="clarabel-mpfr",
        precision_bits=int(out["precision_bits"]) if out.get("precision_bits") else None,
    )


_STR_KEYS = ("x_star", "y0_star", "y_star", "primal_obj", "dual_obj",
             "duality_gap")


def _str_fields_if_decimal(out: dict) -> dict:
    """`*_str` kwargs, taken only from a source that really sent decimals.

    Reads the solver's own `*_str` key first -- that is the MPFR value, and
    reading the f64 key instead was the defect this replaces. Falls back to
    the plain key only when it is itself a string. A float is DROPPED rather
    than stringified: `str(0.9999999999997836)` fabricates an authoritative
    -looking field carrying no digits beyond f64. Absent is honest.
    """
    def _pick(key):
        val = out.get(f"{key}_str", out.get(key))
        if isinstance(val, str):
            return val
        if isinstance(val, (list, tuple)):
            return list(val) if all(isinstance(v, str) for v in val) else None
        return None

    return {f"{k}_str": v for k in _STR_KEYS if (v := _pick(k)) is not None}




def _input_dps(rows) -> int:
    """Significant decimal digits actually present in a decimal-string matrix.

    Rank determination cannot be sharper than the data. Returns at least 15 so
    an all-integer matrix (``"1"``, ``"0"``) is not treated as one-digit data.
    """
    best = 0
    for row in rows:
        cells = row if isinstance(row, (list, tuple)) else [row]
        for cell in cells:
            digits = str(cell).lstrip("-").replace(".", "")
            # strip a leading exponent-free zero run, then drop any exponent
            digits = digits.split("e")[0].split("E")[0].lstrip("0")
            best = max(best, len(digits))
    return max(best, 15)


def gram_pseudo_inverse_solve(G_str, rhs_str, *, dps: int = 50,
                              cutoff_rel_dps: float = 0.8):
    """Minimum-norm solve of ``G y = rhs`` for a SYMMETRIC, possibly SINGULAR G.

    Use this instead of an inverse whenever `G` is a Gram matrix that may be
    rank-deficient. Measured 2026-08-23 on the H_3 six-channel Gram (bean
    `qou/ftuv`), `G` is **exactly singular**: its determinant tracks the
    working precision rather than converging to a value ---

        dps= 60   det(G) = -2.008684335e-57   |eig|min = 1.478983446e-57
        dps=120   det(G) = +5.724314033e-117  |eig|min = 4.215451518e-117

    --- sign flip included, which is what a determinant of exactly zero looks
    like when it is computed in floating point. `G` has a one-dimensional
    kernel, so `G^-1` does not exist and no amount of precision creates it:
    at 120 dps the condition number is 1e117 and an inverse-based solve still
    has zero correct digits.

    What that cost: `frobenius_repose_probe.py` computed `y = G^-T t` through
    `numpy.linalg.inv` and recorded the result. The committed values

        f64 (via the nonexistent inverse)   0.75, 0.5,    0.25,  0.5,    0.154, -0.311
        minimum-norm (this function)        0.777, 0.201, 0.201, -0.181, -0.181, 0.163

    differ by factors of 1e7--1e8, and the f64 row BREAKS a symmetry the true
    solution has exactly (`y[1] == y[2]`, `y[3] == y[4]`) --- independent
    evidence that it is round-off, not an approximation.

    The minimum-norm solution IS well defined whenever `rhs` lies in
    `range(G)`, which for symmetric `G` means orthogonal to the kernel; `t` is
    (`v . t = -3.4e-76` at 80 dps). It is unique only up to a kernel vector,
    and this returns the representative with no kernel component.

    Raises `ValueError` when `rhs` is NOT in `range(G)`, because then no
    solution exists and returning a vector would present "no solution" as an
    answer --- the failure this whole arc keeps finding.
    """
    from mpmath import mp as _mp

    with _mp.workdps(dps):
        G = _mp.matrix([[_mp.mpf(str(v)) for v in row] for row in G_str])
        b = _mp.matrix([_mp.mpf(str(v)) for v in rhs_str])
        d = G.rows
        E, V = _mp.eigsy(G)
        # RELATIVE rank cutoff, scaled by the working precision. An absolute
        # threshold is wrong twice: it is not scale-invariant (a Gram scaled
        # by 1e-6 would read as all-kernel), and a fixed 1e-40 is TIGHTER than
        # the arithmetic below ~50 dps, so a genuinely zero eigenvalue
        # computed as 1e-31 at dps=30 would be classified as nonzero and the
        # kernel missed entirely. Caught by
        # `test_pseudo_inverse_refuses_an_out_of_range_rhs`.
        emax = max((abs(E[j]) for j in range(G.rows)), default=_mp.mpf(1))
        if emax == 0:
            emax = _mp.mpf(1)
        # Bound the cutoff by the precision of the INPUT, not just the working
        # precision. Rank is a property of the data: asking for 80 dps from
        # 50-dps decimal strings invents 30 digits, and the exactly-zero
        # eigenvalue then reads as ~1e-50 input noise rather than zero — so
        # the kernel is missed, and the H_3 solve silently returned
        # `y[0] = 1.0` with its exact `y[1] == y[2]` symmetry broken. A helper
        # that answers a question its inputs cannot support is the same absent
        # check this whole arc keeps turning up, so cap it and mean it.
        eff_dps = min(dps, _input_dps(G_str))
        cut = emax * _mp.mpf(10) ** (-cutoff_rel_dps * eff_dps)

        kernel = [j for j in range(d) if abs(E[j]) < cut]
        # Range test: for symmetric G, range(G) = kernel-perp.
        nb = _mp.sqrt(sum(x ** 2 for x in b))
        for j in kernel:
            ip = sum(V[r, j] * b[r] for r in range(d))
            if nb > 0 and abs(ip) / nb > _mp.mpf(10) ** (-cutoff_rel_dps * eff_dps):
                raise ValueError(
                    f"right-hand side is not in range(G): kernel component "
                    f"{_mp.nstr(abs(ip) / nb, 6)} of ||rhs||. No solution "
                    f"exists; do not record one."
                )

        y = _mp.matrix(d, 1)
        for j in range(d):
            if abs(E[j]) < cut:
                continue
            coeff = sum(V[r, j] * b[r] for r in range(d)) / E[j]
            for r in range(d):
                y[r] += coeff * V[r, j]
        return ([_mp.nstr(y[i], dps) for i in range(d)],
                [float(y[i]) for i in range(d)],
                len(kernel))


def _certifies_optimality(t_str, G_str, n_str, m_str, res) -> tuple[bool, str]:
    """Check `(x*, y*)` against the ORIGINAL data, for a loosened solve.

    A rescaled or tolerance-loosened solve answers a problem that is NOT
    quite the one asked about, and it answers it *well* — so its own reported
    `duality_gap` is small and cannot detect the substitution. Measured
    2026-08-23 (bean `qou/ftuv`) on two solves the rescue accepted:

        uniform 1e6 costs   primal 104901.11715303971  rel gap 3.3e-41  CORRECT
        rho_k 1e15 range    primal      1.4571747644   rel gap 1.2e-30  WRONG
                                        (scipy: 1.2745481388661641)

    Both gaps are tiny; only one answer is right. What separates them is DUAL
    FEASIBILITY in the original `t`: the LP dual requires `y0·1 + Gᵀy ≤ t`
    with `y ≥ 0`, and a `y` optimal for a rescaled `t` violates it. Measured
    on the same pair, normalised by the objective the duality theorem ties it
    to:

        max(y0·1 + Gᵀy − t) / max(|primal_obj|, 1)   =  1.4e-16   vs   1.1e-01

    Eight orders apart, so this is a discriminating test rather than a
    threshold fitted to two points. Returns `(ok, reason)`.
    """
    import numpy as _np

    try:
        t = _np.array([float(x) for x in t_str], dtype=float)
        G = _np.array([[float(v) for v in row] for row in G_str], dtype=float)
        n_target = float(n_str)
        m_bound = float(m_str)
        x = _np.asarray(res.x_star, dtype=float)
        y = _np.asarray(res.y_star, dtype=float)
        y0 = float(res.y0_star)
    except (TypeError, ValueError):
        return False, "certificate unreadable"
    if not (_np.all(_np.isfinite(x)) and _np.all(_np.isfinite(y))
            and _np.isfinite(y0)):
        return False, "certificate non-finite"

    d = len(t)
    scale = max(abs(float(res.primal_obj)), 1.0)
    tol = 1e-9 * scale

    dual_viol = float(_np.max(y0 * _np.ones(d) + G.T @ y - t))
    if dual_viol > tol:
        return False, (f"dual infeasible in the original t: "
                       f"max(y0·1 + Gᵀy − t) = {dual_viol:.3e} > {tol:.3e}")
    if float(_np.min(y)) < -tol:
        return False, f"dual sign violated: min(y) = {float(_np.min(y)):.3e}"
    if abs(float(x.sum()) - n_target) > tol:
        return False, "primal net constraint violated"
    if float(_np.min(G @ x)) < -tol:
        return False, "primal Frobenius positivity violated"
    if float(_np.min(x)) < -m_bound - tol:
        return False, "primal bound violated"
    return True, "ok"


def _solve_operator_selection_lp_clarabel(
    t: np.ndarray,
    G: np.ndarray,
    n_target: float,
    *,
    M_bound: float = 1e6,
    dual_tol: float = 1e-9,
    prec_bits: int = 167,
    clarabel_bin: Optional[str] = None,
) -> LpDualResult:
    """EXPERIMENTAL: solve at ``prec_bits`` MPFR precision (≈50 dps) via
    Clarabel — the in-process ``pyhecke_native.operator_selection_lp`` PyO3
    binding when the installed wheel carries it (built with
    ``--features clarabel-lp``), else the ``clarabel-operator-selection-lp``
    CLI (subprocess).

    Values cross the boundary as decimal strings, so the marshalling adds no
    f64 truncation (the *inputs* are still f64 here because callers pass
    ``np.ndarray``; pass 50-dps strings upstream for full precision).

    CROSS-CHECKED 2026-08-23 (bean ``qou/ftuv``), and it passes by 20 orders
    of margin.  On the H_3 operator-selection LP with 50-dps string inputs,
    against ``backend="scipy"`` at ``n_target`` in {1.0, 0.6614, 3.0}::

        |Δ y0_star|   ≤ 7.5e-46          active_set   identical, [0]
        max |Δ y_star| ≤ 2.8e-47
        primal_obj     scipy 1.07e-10    clarabel 3.6e-44

    The stated precondition — "that needs a scipy+numpy environment" — was
    stale; both install from PyPI.

    Reaching that needed a fix in ``operator_selection_lp.rs``: the solver
    tolerance was hardcoded ``1e-12``/``1e-8``, so ``prec_bits`` widened the
    arithmetic and never tightened termination.  The residual sat at
    3.81482e-16 identically at 167 and 333 bits.  It now derives from ``F``'s
    probed working precision and tracks it: 3.6e-44 at 167 bits, 3.8e-84 at
    333, 3.8e-124 at 500.

    The scipy backend nonetheless REMAINS the default, and changing it is an
    owner call rather than a consequence of this fix: ``to_dict()``'s f64
    fields feed arithmetic in 56 producers, and switching the default moves
    every LP/SDP witness in the corpus at once.  This path stays opt-in via
    ``backend="clarabel"``.
    """
    # STRINGS IN, not just strings out. Callers may pass decimal strings (or
    # mpmath mpf) for `t`, `G` and `n_target` — e.g. from
    # `gram.gram_matrix_mp_strings()` / `gram.tr_m_mp_strings()`, which exist
    # for precisely this boundary — and they now reach the MPFR solver intact.
    # Passing np.ndarray still works and still enters as f64, as before.
    def _s(x) -> str:
        return x if isinstance(x, str) else repr(float(x))

    if isinstance(t, np.ndarray) or not isinstance(t[0], str):
        t = np.asarray(t, dtype=float)
        G = np.asarray(G, dtype=float)
        d = len(t)
        assert G.shape == (d, d), f"Gram matrix shape {G.shape} ≠ ({d},{d})"
        t_str = [repr(float(x)) for x in t]
        G_str = [[repr(float(G[i, j])) for j in range(d)] for i in range(d)]
    else:
        d = len(t)
        assert len(G) == d and all(len(r) == d for r in G), \
            f"Gram matrix shape ≠ ({d},{d})"
        t_str = [_s(x) for x in t]
        G_str = [[_s(G[i][j]) for j in range(d)] for i in range(d)]

    n_str = _s(n_target)
    m_str = repr(float(M_bound))
    dt_str = repr(float(dual_tol))

    def _solve(t_vals: list) -> dict:
        """One trip through the binding, else the CLI."""
        try:
            import pyhecke_native
            _binding = getattr(pyhecke_native, "operator_selection_lp", None)
        except ImportError:
            _binding = None
        if _binding is not None:
            return dict(_binding(t_vals, G_str, n_str, m_str, dt_str,
                                 int(prec_bits)))

        import json as _json
        import subprocess

        payload = {
            "t": t_vals, "G": G_str, "n_target": n_str,
            "m_bound": m_str, "dual_tol": dt_str, "prec_bits": int(prec_bits),
        }
        binp = _find_clarabel_lp_bin(clarabel_bin)
        proc = subprocess.run(
            [binp], input=_json.dumps(payload), capture_output=True, text=True,
        )
        return _json.loads(proc.stdout) if proc.stdout.strip() else {}

    out = _solve(t_str)
    if out.get("feasible", False):
        res = _lp_result_from_dict(out, d)
        # A solve the Rust tolerance ladder had to loosen answers a slightly
        # different question than the one asked. Verify it like a rescued one.
        if "after [" in str(out.get("status", "")):
            ok, why = _certifies_optimality(t_str, G_str, n_str, m_str, res)
            if not ok:
                return _lp_result_from_dict(
                    {"feasible": False,
                     "error": f"loosened solve failed certification: {why}"}, d)
            res.loosened_status = str(out.get("status"))
        return res

    # ── False-infeasible rescue ───────────────────────────────────────
    # `t` appears ONLY in the objective: the feasible set is
    # {x : Σx = n_target, G-positivity, x ≥ -M_bound} and does not mention
    # `t` at all. So rescaling the cost vector CANNOT change whether the
    # problem is feasible. If the unscaled solve says infeasible and a
    # scaled one says feasible, the unscaled verdict was a numerical
    # artifact, not a fact about the LP — this rescue corrects that and can
    # never manufacture a feasible answer for a genuinely infeasible LP.
    #
    # Measured 2026-08-23 (bean `qou/ftuv`): with the default M_bound=1e6,
    # cost magnitudes at or above ~1e6 drive the interior-point method to a
    # spurious infeasible. `rho_k_h3a_gg_trajectory.py` builds
    # t = 1/(dim_q · |y·χ|) with a 1e-15 floor, so its costs reach 1e15 and
    # every nucleon came back NaN under clarabel while scipy solved it.
    # Raising prec_bits does not help (167/333/500 all fail): it is
    # conditioning, not precision.
    #
    # The scale is a POWER OF TWO so both the f64 and the MPFR scaling are
    # exact — no rounding is introduced in either direction.
    _mags = [abs(float(v)) for v in t_str if float(v) != 0.0]
    if not _mags:
        return _lp_result_from_dict(out, d)
    import math as _math
    _k = -_math.frexp(max(_mags))[1]          # 2**_k · max|t| ∈ [0.5, 1)
    if _k == 0:
        return _lp_result_from_dict(out, d)

    from mpmath import mp as _mp_mod, mpf as _mpf
    _dps = max(60, int(prec_bits * 0.30103) + 10)
    with _mp_mod.workdps(_dps):
        _scale = _mpf(2) ** _k
        t_scaled = [_mp_mod.nstr(_mpf(v) * _scale, _dps) for v in t_str]
        out2 = _solve(t_scaled)
        if not out2.get("feasible", False):
            # Genuinely infeasible (or a failure the rescale cannot reach) —
            # return the ORIGINAL verdict rather than the rescaled one, so
            # the reported numbers match the inputs the caller passed.
            return _lp_result_from_dict(out, d)

        # Undo the scaling on every t-linear quantity. `x_star` and
        # `active_set` are scale-INVARIANT (the argmin does not move), so
        # they pass through untouched.
        _inv = _mpf(2) ** (-_k)
        for _key in ("y0_star", "primal_obj", "dual_obj", "duality_gap"):
            if _key in out2:
                out2[_key] = float(_mpf(str(out2[_key])) * _inv)
            _sk = _key + "_str"
            if _sk in out2 and out2[_sk] is not None:
                out2[_sk] = _mp_mod.nstr(_mpf(str(out2[_sk])) * _inv, _dps)
        if "y_star" in out2:
            out2["y_star"] = [float(_mpf(str(v)) * _inv) for v in out2["y_star"]]
        if out2.get("y_star_str") is not None:
            out2["y_star_str"] = [_mp_mod.nstr(_mpf(str(v)) * _inv, _dps)
                                  for v in out2["y_star_str"]]

    res = _lp_result_from_dict(out2, d)

    # CERTIFY BEFORE ACCEPTING. Scaling `t` cannot change the feasible set,
    # but it can change which vertex a finite-precision solver lands on: on a
    # cost vector spanning 1.1 … 1e15, scaling the max to 1 pushes the small
    # entries to ~1e-15, where the solver treats them as zero and optimises a
    # DIFFERENT objective — returning 1.4572 where the true optimum is
    # 1.2745, with a reported duality gap of 1.2e-30 because it solved that
    # other problem well. The gap cannot catch this; dual feasibility in the
    # original `t` can, and does, by eight orders.
    ok, why = _certifies_optimality(t_str, G_str, n_str, m_str, res)
    if not ok:
        return _lp_result_from_dict(
            {"feasible": False,
             "error": f"rescaled solve failed certification: {why}"}, d)

    # Say so. A silent rescue is an absent check indistinguishable from a
    # passing one; the witness should record that the raw solve was rejected.
    res.rescaled_by_pow2 = _k
    return res


def solve_operator_selection_lp(
    t: np.ndarray,
    G: np.ndarray,
    n_target: float,
    *,
    M_bound: float = 1e6,
    dual_tol: float = 1e-9,
    backend: str = "auto",
    prec_bits: int = 167,
    clarabel_bin: Optional[str] = None,
) -> LpDualResult:
    """Solve operator-selection LP per prop:operator-selection-lp.

    Args:
      t: Markov traces t_i = tr_M(b_i), shape (d,)
      G: Frobenius Gram G_{ij} = tr_M(b_i b_j), shape (d, d)
      n_target: target categorical mass
      M_bound: large bound on x_i for boundedness
      dual_tol: threshold for "active" dual variable
      backend: "auto" (default — clarabel MPFR at ~50 dps when its binary
        or wheel is available, else scipy HiGHS f64), "scipy", or "clarabel"
        (force MPFR; raises if unavailable). The clarabel path is
        cross-checked equivalent to scipy to ~1e-12 (clarabel_lp_crosscheck.py).
      prec_bits: MPFR precision for the clarabel backend (167 ≈ 50 dps).
      clarabel_bin: explicit path to the clarabel LP binary (else autodetect).

    Returns LpDualResult with BOTH primal coefficients AND dual shadow
    prices.  Strong duality is verified; mismatch raises ValueError.
    """
    if backend not in ("auto", "scipy", "clarabel"):
        raise ValueError(f"unknown backend {backend!r}; use 'auto', 'scipy', or 'clarabel'")
    if backend in ("auto", "clarabel"):
        try:
            _res = _solve_operator_selection_lp_clarabel(
                t, G, n_target, M_bound=M_bound, dual_tol=dual_tol,
                prec_bits=prec_bits, clarabel_bin=clarabel_bin,
            )
        except (ImportError, FileNotFoundError) as _e:
            if backend == "clarabel":
                raise
            # clarabel unavailable. In strict mode (QOU_REQUIRE_CLARABEL=1)
            # do NOT silently downgrade to scipy float64 — raise so the
            # missing MPFR binary surfaces instead of producing low-precision
            # duals. Otherwise fall through to scipy.
            if os.environ.get("QOU_REQUIRE_CLARABEL") == "1":
                raise RuntimeError(
                    "QOU_REQUIRE_CLARABEL=1 but the clarabel-MPFR binary is "
                    "unavailable; refusing to fall back to scipy float64. "
                    f"Build it (see _find_clarabel_lp_bin). Cause: {_e!r}"
                ) from _e
            # Not strict — but say so. The downgrade is ~28 orders of
            # magnitude in residual (3.6e-44 -> 1.07e-10 on H_3), and it used
            # to happen with nothing printed, so a CI run and a local run
            # could write materially different witnesses and look identical
            # in the log. The result records `backend` either way; this makes
            # it visible at the moment it happens too.
            warnings.warn(
                "clarabel-MPFR unavailable — falling back to scipy float64. "
                "Duals will carry ~16 digits instead of ~46, and the witness "
                'will record backend="scipy-highs". Build the binary, or set '
                "QOU_REQUIRE_CLARABEL=1 to make this an error. "
                f"Cause: {_e!r}",
                RuntimeWarning,
                stacklevel=2,
            )
        else:
            # Return clarabel when forced, or in auto mode when it actually
            # solved; otherwise (auto + infeasible/error) fall back to scipy.
            if backend == "clarabel" or _res.feasible:
                return _res

    from scipy.optimize import linprog  # SciPy is required for LP duals.

    t = np.asarray(t, dtype=float)
    G = np.asarray(G, dtype=float)
    d = len(t)
    assert G.shape == (d, d), f"Gram matrix shape {G.shape} ≠ ({d},{d})"

    # Use bounds=[(-M, None)] directly to keep x in the original variable
    # — avoids the substitution sign ambiguity for dual extraction.
    c = t.copy()  # objective: min c·x

    # Equality (net): Σ x_i = n_target
    A_eq = np.ones((1, d))
    b_eq = np.array([n_target])

    # Inequality (Frobenius positivity, in linprog ≤ form):  -Gx ≤ 0
    A_ub = -G
    b_ub = np.zeros(d)

    res = linprog(
        c=c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
        bounds=[(-M_bound, None)] * d,
        method="highs",
    )

    if not res.success:
        return LpDualResult(
            x_star=[float("nan")] * d,
            y0_star=float("nan"),
            y_star=[float("nan")] * d,
            active_set=[],
            primal_obj=float("nan"),
            dual_obj=float("nan"),
            duality_gap=float("nan"),
            feasible=False,
            # Which solver returned the infeasible verdict is part of the
            # verdict: the two backends disagree on badly-conditioned costs.
            backend="scipy-highs",
        )

    x_star = np.asarray(res.x)
    primal_obj = float(c @ x_star)

    # Extract dual variables. linprog ('highs') returns marginals with
    # convention: ∂(opt obj)/∂(rhs). For our MIN primal:
    #   ∂primal/∂b_eq[0] = y0  (the y_0 of operator-selection LP)
    #   ∂primal/∂b_ub[i] = -y_i  (since A_ub = -G, increasing b_ub[i]
    #     loosens the Frobenius constraint, decreasing optimum →
    #     marginal is negative)
    # In linprog 'highs' terms (gradient of LP value w.r.t. RHS):
    y0_star = float(res.eqlin.marginals[0])
    y_star = (-np.asarray(res.ineqlin.marginals)).tolist()
    active_set = [i for i, y in enumerate(y_star) if y > dual_tol]

    dual_obj = float(n_target * y0_star)
    duality_gap = abs(primal_obj - dual_obj)

    return LpDualResult(
        x_star=list(x_star),
        y0_star=y0_star,
        y_star=y_star,
        active_set=active_set,
        primal_obj=primal_obj,
        dual_obj=dual_obj,
        duality_gap=duality_gap,
        feasible=True,
        backend="scipy-highs",
        precision_bits=53,
    )


def verify_dual_present(witness_path: str | Path) -> dict:
    """Validate that an operator-selection witness JSON includes dual.

    Required keys (anywhere in the JSON, recursive search):
      y0_star  — shadow price of net constraint
      y_star   — shadow prices of Frobenius constraints
      active_set OR active_constraints  — indices of tight Frobenius constraints
      primal_obj
      dual_obj
      duality_gap

    Returns:
      {"ok": bool, "missing": [list of required keys not found],
       "found": [keys found]}

    Use this as a content-validation hook on any block whose
    `tags` include "operator-selection" or "shadow-price".
    """
    REQUIRED = {"y0_star", "y_star", "primal_obj", "dual_obj", "duality_gap"}
    OPTIONAL_ALIASES = {"active_set", "active_constraints", "active_channels"}

    p = Path(witness_path)
    if not p.exists():
        return {"ok": False, "missing": list(REQUIRED), "found": [],
                "reason": f"witness file not found: {p}"}
    data = json.loads(p.read_text())

    found = set()

    def _meaningful(v) -> bool:
        # A dual field is "present" only if it carries a real value.
        # A null, or an empty list/dict, is a hollow placeholder that
        # passed the old presence-only check while computing no dual
        # (the devils-advocate class-3 / witness-hollowness pattern).
        if v is None:
            return False
        if isinstance(v, (list, dict, str)) and len(v) == 0:
            return False
        return True

    # Records where an empty active set CONTRADICTS a nonzero y_star.
    inconsistent: list[str] = []

    def _nonzero_shadow_prices(y) -> list[int]:
        """Indices with a shadow price above tolerance."""
        if isinstance(y, list):
            items = enumerate(y)
        elif isinstance(y, dict):
            items = y.items()
        else:
            return []
        out = []
        for i, x in items:
            if isinstance(x, bool) or not isinstance(x, (int, float)):
                continue
            if abs(float(x)) > 1e-12:
                out.append(i)
        return out

    def _scan(obj, path="<root>"):
        if isinstance(obj, dict):
            # ── active-set / y_star CONSISTENCY, checked pairwise ──────────
            #
            # An EMPTY active set is a legitimate dual result *on its own*: it
            # means no Frobenius constraint is tight (every shadow price is
            # sub-tolerance), i.e. an interior LP/SDP optimum. Corpus evidence
            # backs this — of 3096 witnesses, 14 carry an empty active set and
            # ALL of them pair it with an absent or all-zero `y_star`. So
            # rejecting emptiness outright would reject 11 well-formed duals.
            #
            # What is NEVER legitimate is an empty active set sitting next to a
            # NONZERO `y_star`, because the active set is *defined* as
            # {i : y_star[i] > 0}. Those two fields then contradict each other,
            # and one of them is wrong. No corpus witness has that shape; the
            # null-hardening test does, which is what it was really pinning.
            #
            # Hence a pairwise consistency check rather than a presence check:
            # it accepts every real interior optimum and still fails the
            # contradictory shape. Presence-only checks (in either direction)
            # cannot separate the two, which is why the previous
            # implementation and its test disagreed.
            akey = next(
                (k for k in OPTIONAL_ALIASES
                 if k in obj and isinstance(obj[k], list)),
                None,
            )
            if akey is not None and len(obj[akey]) == 0:
                hot = _nonzero_shadow_prices(obj.get("y_star"))
                if hot:
                    inconsistent.append(
                        f"{path}: {akey} is empty but y_star has "
                        f"{len(hot)} nonzero entr"
                        f"{'y' if len(hot) == 1 else 'ies'} at "
                        f"{hot[:5]} — the active set is by definition "
                        "{i : y_star[i] > 0}, so these contradict"
                    )

            for k, v in obj.items():
                if k in REQUIRED and _meaningful(v):
                    found.add(k)
                elif k in OPTIONAL_ALIASES and isinstance(v, list):
                    found.add(k)
                _scan(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                _scan(item, f"{path}[{i}]")

    _scan(data)
    missing = REQUIRED - found
    has_active = bool(found & OPTIONAL_ALIASES)
    if not has_active:
        missing.add("active_set OR active_constraints OR active_channels")
    return {
        "ok": not missing and not inconsistent,
        "missing": sorted(missing),
        "found": sorted(found),
        "inconsistent": inconsistent,
    }


@dataclass
class SdpDualResult:
    """SDP version: primal + dual + strong-duality check.

    The SDP relaxes Frobenius positivity G x ≥ 0 (componentwise) to
    a Positive-Semidefinite Programming constraint M(x) ≽ 0 where
    M(x) is some PSD matrix linearly depending on x. Use when the
    LP relaxation is too loose (e.g., higher-strand cases where
    the Gram matrix has indefinite cross-block structure).

    Required fields:
      X_star          — primal optimum (matrix or vector, depending on problem)
      Z_star          — dual PSD certificate
      primal_obj
      dual_obj
      duality_gap
      eigenvalues     — of the optimum's PSD matrix (all should be ≥ -tol)
    """
    X_star: list  # may be vector or matrix
    Z_star: list
    primal_obj: float
    dual_obj: float
    duality_gap: float
    eigenvalues: list[float]
    feasible: bool
    # Full-precision decimal companions, mirroring `LpDualResult`. Populated
    # by `_solve_psd_via_clarabel_lp` from the MPFR solve; `None` on the
    # cvxpy/SCS f64 path, so `X_star_str is not None` answers "was this
    # solved at precision?".
    X_star_str: Optional[list] = None
    Z_star_str: Optional[list] = None
    primal_obj_str: Optional[str] = None
    dual_obj_str: Optional[str] = None
    duality_gap_str: Optional[str] = None
    eigenvalues_str: Optional[list] = None
    # Which solver produced this, and at what width — same reason as
    # `LpDualResult`: `backend="auto"` silently picks clarabel-MPFR or
    # cvxpy/SCS f64 depending on whether a Rust binary happens to be built,
    # and a witness that does not say which cannot be told apart from one
    # solved the other way.
    backend: Optional[str] = None
    precision_bits: Optional[int] = None

    def to_dict(self) -> dict:
        """Serialize the SDP, f64 fields verbatim plus `*_str` companions.

        The f64 fields stay f64 for the same reason `LpDualResult.to_dict`
        gives: consumers do arithmetic on them, so replacing them with
        strings breaks readers silently.

        **The `*_str` half was missing entirely until 2026-08-23.** The
        diagonal-lift path solves through `_solve_operator_selection_lp_clarabel`
        at 167 bits, and every digit past f64 was discarded here — a ~50-dps
        solve reaching its witness as f64. That is exactly the defect
        `qou-t0rf` fixed for `LpDualResult` and never for this one, and it is
        why the LP-dual float64 carve-out looked structurally necessary on
        the SDP side (bean `qou/ftuv`).
        """
        out = {
            "X_star": self.X_star,
            "Z_star": self.Z_star,
            "primal_obj": float(self.primal_obj),
            "dual_obj": float(self.dual_obj),
            "duality_gap": float(self.duality_gap),
            "eigenvalues": list(self.eigenvalues),
            "feasible": bool(self.feasible),
        }
        if self.backend is not None:
            out["backend"] = self.backend
        if self.precision_bits is not None:
            out["precision_bits"] = int(self.precision_bits)
        for key, val in (
            ("X_star_str", self.X_star_str),
            ("Z_star_str", self.Z_star_str),
            ("primal_obj_str", self.primal_obj_str),
            ("dual_obj_str", self.dual_obj_str),
            ("duality_gap_str", self.duality_gap_str),
            ("eigenvalues_str", self.eigenvalues_str),
        ):
            if val is not None:
                out[key] = val
        return out


def _solve_psd_via_clarabel_lp(
    t: np.ndarray,
    G: np.ndarray,
    n_target: float,
    *,
    M_bound: float = 1e6,
    prec_bits: int = 167,
    clarabel_bin: Optional[str] = None,
) -> SdpDualResult:
    """Faithful Clarabel port of the *diagonal* PSD lift.

    ``solve_psd_operator_selection_sdp`` enforces ``M(x) = diag(Gx) ⪰ 0``,
    which is exactly the componentwise constraint ``Gx ≥ 0`` of the
    operator-selection LP.  So the faithful MPFR port delegates to the
    verified LP solver (`_solve_operator_selection_lp_clarabel`) and
    repackages the result as an ``SdpDualResult`` — the PSD matrix's
    eigenvalues are its diagonal entries ``(Gx)_i``.

    A genuine *dense* PSD lift (off-diagonal correlations / moment matrix)
    is NOT this function: it needs Clarabel's PSD cone (``clarabel-sdp``
    f64 + LAPACK, or an MPFR eigensolver) and is tracked as a follow-up.
    """
    lp = _solve_operator_selection_lp_clarabel(
        t, G, n_target, M_bound=M_bound, prec_bits=prec_bits,
        clarabel_bin=clarabel_bin,
    )
    if not lp.feasible:
        d = len(np.asarray(t, dtype=float))
        return SdpDualResult(
            X_star=[float("nan")] * d, Z_star=[],
            primal_obj=float("nan"), dual_obj=float("nan"),
            duality_gap=float("nan"), eigenvalues=[], feasible=False,
            backend=lp.backend, precision_bits=lp.precision_bits,
        )
    G_f = np.asarray(G, dtype=float)
    x_star = np.asarray(lp.x_star, dtype=float)
    gx = (G_f @ x_star).tolist()

    # The eigenvalues of `diag(Gx)` ARE `(Gx)_i`, and recomputing them through
    # numpy would re-truncate an MPFR solve to f64 — the second leak on this
    # path. When both `G` and `x*` are available as decimals, redo the product
    # with `mpmath` at the same working precision so `eigenvalues_str` is as
    # good as the solve that produced it.
    gx_str = None
    if lp.x_star_str is not None:
        try:
            import mpmath as _mp
            with _mp.workdps(max(60, int(prec_bits * 0.30103) + 10)):
                if isinstance(G[0][0], str):
                    G_m = [[_mp.mpf(G[i][j]) for j in range(len(G))]
                           for i in range(len(G))]
                else:
                    G_m = [[_mp.mpf(repr(float(G_f[i, j]))) for j in range(G_f.shape[1])]
                           for i in range(G_f.shape[0])]
                x_m = [_mp.mpf(v) for v in lp.x_star_str]
                gx_m = [sum((G_m[i][j] * x_m[j] for j in range(len(x_m))), _mp.mpf(0))
                        for i in range(len(G_m))]
                gx_str = [_mp.nstr(v, _mp.mp.dps) for v in sorted(gx_m)]
        except Exception:  # noqa: BLE001 — companions are best-effort
            gx_str = None

    z_str = None
    if lp.y0_star_str is not None and lp.y_star_str is not None:
        z_str = [lp.y0_star_str, *lp.y_star_str]

    return SdpDualResult(
        X_star=lp.x_star,
        Z_star=[lp.y0_star, *lp.y_star],
        primal_obj=lp.primal_obj,
        dual_obj=lp.dual_obj,
        duality_gap=lp.duality_gap,
        eigenvalues=sorted(gx),
        feasible=True,
        X_star_str=lp.x_star_str,
        Z_star_str=z_str,
        primal_obj_str=lp.primal_obj_str,
        dual_obj_str=lp.dual_obj_str,
        duality_gap_str=lp.duality_gap_str,
        eigenvalues_str=gx_str,
        backend=lp.backend,
        precision_bits=lp.precision_bits,
    )


def solve_psd_operator_selection_sdp(
    t: np.ndarray,
    G: np.ndarray,
    n_target: float,
    *,
    backend: str = "auto",
    prec_bits: int = 167,
    clarabel_bin: Optional[str] = None,
) -> SdpDualResult:
    """SDP version of operator-selection: enforce M(x) ≽ 0 instead of Gx ≥ 0.

    The PSD lift: build M(x) = diag(Gx) (positive-semidefinite ⇔
    componentwise non-negative for diagonal); equivalent to LP for
    diagonal but generalizable when off-diagonal correlations matter.

    For higher-strand cases where the LP relaxation is too loose
    (Frobenius constraints don't capture cross-channel correlation),
    replace M(x) with a denser SDP lift (e.g., the moment-matrix
    SDP from sdp_moment_lift.py).

    Args:
      backend: "auto" (default — clarabel MPFR via the diagonal-lift LP when
        available, else cvxpy/SCS f64; falls back to cvxpy if clarabel is
        unavailable or infeasible), "cvxpy", or "clarabel" (force; raises if
        unavailable). For the current diagonal lift clarabel is EXACT. The
        genuine dense-PSD cone is `operator_selection_sdp.rs`
        (Rust, clarabel-sdp) — not yet wired into this Python entry point.
      prec_bits: MPFR precision for the clarabel backend (167 ≈ 50 dps).
      clarabel_bin: explicit path to the clarabel LP binary (else autodetect).

    Returns SdpDualResult with both X*, Z* and strong-duality gap.
    """
    if backend not in ("auto", "cvxpy", "clarabel"):
        raise ValueError(f"unknown SDP backend {backend!r}; use 'auto', 'cvxpy', or 'clarabel'")
    if backend in ("auto", "clarabel"):
        try:
            _res = _solve_psd_via_clarabel_lp(
                t, G, n_target, prec_bits=prec_bits, clarabel_bin=clarabel_bin,
            )
        except (ImportError, FileNotFoundError) as _e:
            if backend == "clarabel":
                raise
            # clarabel unavailable. Strict mode refuses the cvxpy float64
            # downgrade so the missing MPFR binary surfaces.
            if os.environ.get("QOU_REQUIRE_CLARABEL") == "1":
                raise RuntimeError(
                    "QOU_REQUIRE_CLARABEL=1 but the clarabel-MPFR binary is "
                    "unavailable; refusing to fall back to cvxpy float64. "
                    f"Build it (see _find_clarabel_lp_bin). Cause: {_e!r}"
                ) from _e
        else:
            # Return clarabel when forced, or in auto mode when it solved;
            # otherwise (auto + infeasible/error) fall back to cvxpy.
            if backend == "clarabel" or _res.feasible:
                return _res

    try:
        import cvxpy as cp
    except ImportError as e:
        raise ImportError(
            "SDP requires cvxpy. Install via `pip install cvxpy`."
        ) from e

    t = np.asarray(t, dtype=float)
    G = np.asarray(G, dtype=float)
    d = len(t)

    x = cp.Variable(d)
    constraints = [
        cp.sum(x) == n_target,
        G @ x >= 0,  # Frobenius positivity (componentwise; LP-equivalent)
    ]
    objective = cp.Minimize(t @ x)
    prob = cp.Problem(objective, constraints)
    prob.solve(solver="SCS")

    feasible = prob.status in ("optimal", "optimal_inaccurate")
    if not feasible:
        return SdpDualResult(
            X_star=[float("nan")] * d, Z_star=[],
            primal_obj=float("nan"), dual_obj=float("nan"),
            duality_gap=float("nan"), eigenvalues=[], feasible=False,
        )

    x_star = np.asarray(x.value)
    primal_obj = float(prob.value)

    # Dual variables (CVXPY exposes via .dual_value on each constraint).
    # CVXPY sign convention for `Minimize` + `==`: dual_value is the
    # negative of scipy's marginal — flip to match the operator-
    # selection LP's stated dual program (max n_target · y_0).
    y_eq = -float(constraints[0].dual_value)
    y_ineq = np.asarray(constraints[1].dual_value)
    dual_obj = float(n_target * y_eq)
    duality_gap = abs(primal_obj - dual_obj)

    # PSD eigenvalues (here Gx is a vector; treat as diag PSD matrix)
    Gx = G @ x_star
    eigenvalues = sorted(Gx.tolist())

    return SdpDualResult(
        X_star=x_star.tolist(),
        Z_star=[float(y_eq), *y_ineq.tolist()],
        primal_obj=primal_obj,
        dual_obj=dual_obj,
        duality_gap=duality_gap,
        eigenvalues=eigenvalues,
        feasible=True,
    )


if __name__ == "__main__":
    # Quick smoke test on a 3-channel dummy LP.
    print("=" * 70)
    print("Smoke test: 3-channel dummy LP")
    print("=" * 70)
    t = np.array([1.0, 0.5, 0.3])
    G = np.array([[1.0, 0.2, 0.1],
                  [0.2, 1.0, 0.3],
                  [0.1, 0.3, 1.0]])
    n_target = 1.0
    res = solve_operator_selection_lp(t, G, n_target)
    print(f"  Primal x*  = {[f'{x:.4f}' for x in res.x_star]}")
    print(f"  Dual y0*   = {res.y0_star:.6f}  (shadow price of net constraint)")
    print(f"  Dual y*    = {[f'{y:.4f}' for y in res.y_star]}")
    print(f"  Active set = {res.active_set}")
    print(f"  Primal obj = {res.primal_obj:.6f}")
    print(f"  Dual obj   = {res.dual_obj:.6f}")
    print(f"  Gap        = {res.duality_gap:.2e}  (should be ~0)")
    print(f"  Feasible   = {res.feasible}")
    assert res.feasible
    assert res.duality_gap < 1e-6, f"Strong duality fails: gap = {res.duality_gap}"
    print()
    print("  ✓ LP strong duality verified")
    print()
    print("=" * 70)
    print("Smoke test: SDP version (same problem)")
    print("=" * 70)
    try:
        sdp = solve_psd_operator_selection_sdp(t, G, n_target)
        print(f"  Primal obj   = {sdp.primal_obj:.6f}")
        print(f"  Dual obj     = {sdp.dual_obj:.6f}")
        print(f"  Gap          = {sdp.duality_gap:.2e}")
        print(f"  Min eigenval = {min(sdp.eigenvalues):.4e}")
        print(f"  Feasible     = {sdp.feasible}")
        if sdp.feasible and sdp.duality_gap < 1e-4:
            print()
            print("  ✓ SDP strong duality verified")
    except ImportError as e:
        print(f"  (skipped — {e})")

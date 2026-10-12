#!/usr/bin/env python3
"""VERIFY the L-natural-concavity lead on the `Xbot` objective `G`, rather than rely on it.

Bean `qou-as81` (A1), epic `qou-3e6w`.  This probe exists to check a claim a sibling session
recorded as a lead and explicitly flagged *"to verify before relying on"*: that

    G(u)  =  sum_j phi_j(u_j)  +  sum_{j < jp} psi_{j,jp}(u_jp - u_j)

with every univariate piece concave, which on `Z^J` is the L-natural-concave form.  If it holds,
the INTEGER maximum per `(pe, T)` is characterised by local optimality over `+-chi_X` and is
reachable by steepest ascent — so A1 would not need the continuous relaxation, the integrality
penalty (excluded, `PenaltyFamilyCeiling.lean`) or support branching (no 27-branch reduction,
`SupportBranchingValidity.lean`) at all.

**The corpus does not hold the literature.**  Corpus-grep for Murota / L-natural / discrete
convex analysis across `library/` (INDEX, `sections/`, and the `ocr/` tier the documented path
misses), `beans/`, `content/`, `folio/`, `computations/` and `docs/` returns one unrelated hit
(a 2026 Algorithmica paper on concentration of submodular functions).  So the claim cannot be
discharged by citation and has to be measured here.

## What is checked, and what each check can and cannot settle

- **C1 structural form.**  Read off `G`'s own source: the one-body/tail/cost terms depend on a
  single `u_j`, and the only coupling is `epsx(g) - epsx(g + u_jp - u_j)`, a function of the
  DIFFERENCE alone.  Asserted here against the live source text so the check fails if `G`
  changes shape, rather than silently passing on a stale reading.
- **C2 univariate concavity.**  The form is only the L-natural shape if each piece is concave:
  `-R(b+u)` needs `R` convex, `-W(c-u)` needs `W` convex, `-epsx(g+d)` needs `epsx` convex.
  Measured by second difference at `mp.dps = 60`.  A single violation refutes the lead.
- **C3 Hessian off-diagonal sign — the continuous shadow.**  For this form the Hessian is
  `diag(phi_j'') + sum psi''*(e_j - e_jp)(e_j - e_jp)^T`; with `psi'' <= 0` the off-diagonal
  entries are `-psi'' >= 0`.  So **every off-diagonal of `H_G` must be non-negative**.  This is
  free: it reuses the Hessian machinery of `rev_e_infinity_hessian_budget_probe.py`.  It is a
  NECESSARY condition on the continuous function, not the discrete property.
- **C4 discrete midpoint concavity — the definition.**  `f` is L-natural-concave iff
  `f(x) + f(y) <= f(floor((x+y)/2)) + f(ceil((x+y)/2))` for all `x, y` in `Z^J`.  Checked on
  random integer pairs inside the domain.  **This is the one that decides it**, and it is a
  refutation instrument: a violation refutes, while no violation over a sample does not prove.

## Scope, stated up front

C4 is a sample, and a sample of a refutation instrument: a violation refutes, a pass does not
prove.  **The IMPLICATION `C1 + C2 => discrete midpoint concavity` is proved separately**, in
`QOU/BraidKnot/LNaturalConcaveForm.lean` (6 theorems, sorry-free) — derived here rather than
cited, because the corpus does not hold the literature.  So what this probe contributes is the
evidence for its HYPOTHESIS (C1, C2) and an independent direct check of the conclusion (C4).

What remains after a 4/4 pass is therefore sharp and small: C2 samples 52 points, and the
implication needs `R`, `W`, `epsx` convex on their whole domains.  That is a statement about
three explicit series.  The ALGORITHMIC half — local optimality over `+-chi_X` implying global,
and termination of steepest ascent — is NOT established by anything here.

No witness, deliberately: `G` lives in `rev_e_infinity_xbot_relaxation_probe.py`, on the
unmerged #7419 branch, so a `scriptHash` written from here would be mis-provenanced.  On a
branch without that file this exits 0 with an explicit SKIP banner.
"""

from __future__ import annotations

import io
import os
import random

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))

# Package import, not the bare `_precision` shim — see the sibling probe's note on the
# `_path_bridge` ordering trap.  Raised BEFORE the module constants below are built.
from qou_substrate.precision import set_compute_dps  # noqa: E402

set_compute_dps()

RELAX = os.path.join(HERE, "rev_e_infinity_xbot_relaxation_probe.py")
_CUT_BANNER = 'print("R1  does the real extension reproduce the committed integer evaluator?")'

# C1 is an assertion about the live source text, not about a remembered reading.  Each fragment
# must still be present in `G`'s body; if `G` is restructured the probe fails loudly instead of
# certifying a shape that no longer exists.
_FORM_FRAGMENTS = (
    "tot += R(b) - R(b + u[j]) + W(mp.mpf(bT - b), pe, Tlen) - W(y, pe, Tlen)",  # one-body + tail
    "arg = g + u[jp] - u[j]",                                                     # pair: DIFFERENCE
    "tot += epsx(g) - epsx(arg)",                                                 # pair value
    "- LNQ * lin",                                                                # linear wall cost
    "(LNQ_HALF - lam) * mp.fsum(x * x for x in u)",                               # quadratic cost
)

FD = mp.mpf(10) ** (-20)
TOL = mp.mpf(10) ** (-30)


def _load_defs(path: str) -> dict:
    lines = io.open(path, encoding="utf-8").readlines()
    cut = next((n for n, L in enumerate(lines) if L.rstrip("\n") == _CUT_BANNER), None)
    if cut is None:
        raise SystemExit(
            "rev_e_infinity_lnatural_concavity_probe: the R1 banner moved in\n"
            f"  {path}\n"
            "Re-locate the definition/execution boundary before trusting any number here."
        )
    src = "".join(lines[:cut])
    ns = {"__name__": "_relax_probe_defs", "__file__": path}
    exec(compile(src, path, "exec"), ns)  # noqa: S102 — our own source, bounded by `cut`
    ns["_full_text"] = "".join(lines)
    return ns


def _second_diff(f, x, h):
    """f''(x) by central second difference.  One order worse than differencing a gradient, but
    these are univariate series with no gradient available, and `dps = 60` with `h = 1e-12`
    leaves ~36 digits."""
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)


def main() -> int:
    if not os.path.exists(RELAX):
        print("rev_e_infinity_lnatural_concavity_probe: SKIP — no measurement attempted.")
        print(f"  {RELAX} is absent.  `G` lives in that file, which is on the unmerged")
        print("  #7419 branch; check it out and re-run.  This is a SKIP, not a pass.")
        return 0

    ns = _load_defs(RELAX)
    mp.mp.dps = 60
    for k in ("_DC", "_GAMMA"):
        if isinstance(ns.get(k), dict):
            ns[k].clear()

    G = ns["G"]
    dG = ns["dG_coord"]
    R = ns["R"]
    W = ns["W"]
    epsx = ns["epsx"]
    PEMAX = ns["PEMAX"]
    JPAD = ns["JPAD"]
    b0_of = ns["b0_of"]
    text = ns["_full_text"]

    print("Xbot objective G: is it L-natural-concave?  (verifying a sibling's lead)")
    print(f"  mp.dps = {mp.mp.dps}; PEMAX = {PEMAX}, JPAD = {JPAD}")
    print()

    results: list[tuple[str, bool, str]] = []

    # ---- C1 structural form -----------------------------------------------------------------
    missing = [f for f in _FORM_FRAGMENTS if f not in text]
    c1 = not missing
    print("C1  separable + difference-coupled form, asserted against the live source")
    for f in _FORM_FRAGMENTS:
        print(f"      {'ok  ' if f in text else 'MISS'}  {f}")
    if missing:
        print(f"      {len(missing)} fragment(s) absent — G's shape has changed")
    results.append((
        "C1 G = sum_j phi_j(u_j) + sum_{j<jp} psi(u_jp - u_j): the only coupling is the "
        "DIFFERENCE u_jp - u_j, via epsx",
        c1,
        f"{len(_FORM_FRAGMENTS) - len(missing)}/{len(_FORM_FRAGMENTS)} fragments present",
    ))
    print()

    # ---- C2 univariate convexity of R, W, epsx ----------------------------------------------
    print("C2  univariate pieces: -R(b+u), -W(c-u), -epsx(g+d) concave  <=>  R, W, epsx convex")
    h = mp.mpf(10) ** (-12)
    c2_bad: list[str] = []
    probes = []
    for x in ("0.5", "1", "2", "3.5", "5", "8", "13", "21"):
        probes.append(("R", R, mp.mpf(x)))
        probes.append(("epsx", epsx, mp.mpf(x)))
    for pe in (0, 4, PEMAX):
        for T in (4, 12, JPAD):
            for y in ("0.5", "1.5", "4", "9"):
                probes.append((f"W(pe={pe},T={T})", (lambda yy, p=pe, t=T: W(yy, p, t)), mp.mpf(y)))
    worst = {}
    for name, f, x in probes:
        try:
            d2 = _second_diff(f, x, h)
        except Exception as exc:                      # domain edge
            print(f"      {name} at {mp.nstr(x, 6)}: skipped ({type(exc).__name__})")
            continue
        key = name.split("(")[0]
        if key not in worst or d2 < worst[key][0]:
            worst[key] = (d2, name, x)
        if d2 < -TOL:
            c2_bad.append(f"{name} at {mp.nstr(x, 8)}: f'' = {mp.nstr(d2, 8)}")
    for key, (d2, name, x) in sorted(worst.items()):
        print(f"      {key:6s} most-negative f'' over the sample: {mp.nstr(d2, 10):>16s} "
              f"(at {name}, x = {mp.nstr(x, 6)})")
    if c2_bad:
        print(f"      {len(c2_bad)} CONCAVE-VIOLATING point(s) — the lead is refuted:")
        for b in c2_bad[:6]:
            print(f"        {b}")
    results.append((
        "C2 R, W and epsx are convex on the sampled range, so every univariate piece of G is "
        "concave",
        not c2_bad,
        f"{len(probes)} points sampled, {len(c2_bad)} violation(s)",
    ))
    print()

    # ---- C2b series coefficients strictly positive — EXHAUSTIVE, not sampled ----------------
    # This is the premise the Lean proof consumes.  `QOU.BraidKnot.LNaturalConcaveForm
    # .neg_exp_series_concave` proves that MINUS a non-negative combination of `exp(-r L x)` is
    # concave; what it needs from the producer is that every coefficient really is non-negative:
    #
    #   R:  c_r = t^-r / (r (1 - t^-r))   > 0  whenever 0 < t^-r < 1, i.e. for t > 1
    #   W:  c_r = (D_r - 1)/r             > 0  iff D_r > 1
    #
    # and `D_r = head + t^(-r m)/(1 - t^(-2r))` with `head = sum_{d < m} t^(-r d)`.  For `m = 0`
    # that is `1/(1 - w)` with `0 < w < 1`, hence `> 1`; for `m >= 1` the head already contains
    # the `d = 0` term `= 1` plus a strictly positive tail.  So `D_r > 1` always.  Checked over
    # the producer's WHOLE grid rather than a sample, because it is cheap and because the
    # smallest margin is at the truncation edge (`r = RSER`), exactly where a sample would miss.
    print("C2b series coefficients strictly positive (the premise the Lean proof consumes)")
    D_coeffs = ns["_D_coeffs"]
    E = ns["_E"]
    RSER = ns["RSER"]
    c2b_min = None
    c2b_n = 0
    for pe in range(0, PEMAX + 1):
        for T in range(1, JPAD + 1):
            for r, d in enumerate(D_coeffs(pe, T), 1):
                c2b_n += 1
                if c2b_min is None or (d - 1) < c2b_min[0]:
                    c2b_min = (d - 1, pe, T, r)
    e_min = min(E)
    print(f"      {c2b_n} W-coefficients over pe=0..{PEMAX}, T=1..{JPAD}, r=1..{RSER}")
    print(f"      min (D_r - 1) = {mp.nstr(c2b_min[0], 12)} at pe={c2b_min[1]}, T={c2b_min[2]}, "
          f"r={c2b_min[3]}")
    print(f"      min R-coefficient t^-r/(1 - t^-r) = {mp.nstr(e_min, 12)}")
    results.append((
        "C2b every series coefficient of R and W is strictly positive, over the producer's "
        "whole (pe, T, r) grid — exhaustive, not sampled",
        c2b_min[0] > 0 and e_min > 0,
        f"{c2b_n} W-coefficients + {len(E)} R-coefficients; min (D_r - 1) = "
        f"{mp.nstr(c2b_min[0], 8)}, min R-coefficient = {mp.nstr(e_min, 8)}",
    ))
    print()

    # ---- C3 Hessian off-diagonal sign -------------------------------------------------------
    print("C3  Hessian off-diagonals must be >= 0 (psi concave => off-diag = -psi'' >= 0)")
    c3_bad = []
    c3_min = None
    for pe in (0, 4, PEMAX):
        for T in (4, 8, 12):
            u = [mp.mpf("0.25")] * T
            if G(u, pe) == mp.mpf("-inf"):
                continue
            mn = None
            for i in range(T):
                for j in range(T):
                    if i == j:
                        continue
                    up, um = list(u), list(u)
                    up[j] += FD
                    um[j] -= FD
                    hij = (dG(up, pe, i, u[i]) - dG(um, pe, i, u[i])) / (2 * FD)
                    if mn is None or hij < mn:
                        mn = hij
                    if hij < -TOL:
                        c3_bad.append(f"pe={pe} T={T} H[{i},{j}] = {mp.nstr(hij, 8)}")
            print(f"      pe={pe} T={T:2d}: min off-diagonal = {mp.nstr(mn, 12)}")
            if c3_min is None or mn < c3_min:
                c3_min = mn
    results.append((
        "C3 every sampled off-diagonal Hessian entry is non-negative, the continuous shadow of "
        "the difference-coupled form",
        not c3_bad,
        f"min off-diagonal over the sample = {mp.nstr(c3_min, 10) if c3_min is not None else 'n/a'}, "
        f"{len(c3_bad)} violation(s)",
    ))
    if c3_bad:
        for b in c3_bad[:6]:
            print(f"      VIOLATION {b}")
    print()

    # ---- C4 discrete midpoint concavity — the definition ------------------------------------
    print("C4  discrete midpoint concavity: G(x)+G(y) <= G(floor mid)+G(ceil mid) on Z^J")
    # 🛑 TWO SAMPLING TRAPS, both hit on the first version of this check, both of which make it
    # report PASS while testing nothing:
    #
    #  1. **Admissibility.**  `G` is `-inf` unless `u_j - u_jp < g_{j,jp} = b0(jp) - b0(j)` for
    #     every pair AND `u_j < bT - b0(j)`.  Uniform-random integer vectors violate the pair
    #     constraint almost always: the first version got **13 admissible pairs out of ~900**.
    #     The second version sampled NON-DECREASING vectors, reasoning that `u_j - u_jp <= 0 < g`
    #     makes the pair constraint automatic.  It does — and it is still wrong, because the
    #     per-row ceiling `bT - b0(j) - 1` DECREASES in `j`, so a non-decreasing vector hits its
    #     own ceiling almost immediately: **44 vectors generated out of 6000, every one trivial.**
    #     The admissible set has to be derived, not guessed.  It is a system of CONSECUTIVE
    #     difference constraints: with `lo_j = max(0, u_{j-1} - (b0(j) - b0(j-1)) + 1)` and
    #     `hi_j = bT - b0(j) - 1`, drawing `u_j` from `[lo_j, hi_j]` enforces every consecutive
    #     pair, and the non-consecutive ones follow by telescoping
    #     (`u_j - u_jp <= b0(jp) - b0(j) - (jp - j) < b0(jp) - b0(j)`).  Note what this says about
    #     the geometry: for `j < pe` the gap is 1, so `u` must be NON-DECREASING there; for
    #     `j >= pe` it is 2, so `u` may fall by at most 1 per row.  Midpoints stay admissible
    #     because floor and ceil of a feasible point of an integer difference system are feasible.
    #  2. **Triviality.**  If `{floor mid, ceil mid} = {x, y}` the inequality is an IDENTITY and
    #     its slack is exactly 0.  That is what the first version reported as its tightest
    #     case: `x = [1,1,1]`, `y = [0,0,0]`, slack `0.0`.  Such pairs are excluded here, and
    #     the count of genuinely non-trivial pairs is reported — a check that tests only
    #     identities passes for free.
    random.seed(20261011)
    c4_bad = []
    c4_tested = 0
    c4_trivial = 0
    c4_inadmissible = 0
    c4_worst = None

    def _mid(x, y):
        lo = [mp.floor((x[j] + y[j]) / 2) for j in range(len(x))]
        up = [mp.ceil((x[j] + y[j]) / 2) for j in range(len(x))]
        return lo, up

    for pe in (0, 2, 4, 6, PEMAX):
        for T in (3, 5, 8):
            bT = b0_of(pe, T)
            hi = [max(0, bT - b0_of(pe, j) - 1) for j in range(T)]
            if min(hi) <= 0:
                continue
            def _draw():
                """One admissible integer vector from the consecutive-difference system, drawn
                from the LAST row BACKWARDS.

                Direction matters and the forward version nearly killed this check.  The ceiling
                `hi_j = bT - b0(j) - 1` decreases in `j` while the difference constraint
                `u_j - u_{j+1} <= b0(j+1) - b0(j) - 1` bounds `u_j` ABOVE in terms of the next
                row.  Drawing forwards, a uniform `u_j` is typically near its (large) ceiling and
                then `lo_{j+1} = u_j - g + 1` overshoots the (smaller) next ceiling: measured,
                **97 % of forward draws died**, leaving 38 usable pairs.  Backwards, the ceiling
                and the difference constraint bound the same end, so the interval is non-empty by
                construction and every draw succeeds.
                """
                v = [None] * T
                nxt = random.randint(0, hi[T - 1])
                v[T - 1] = nxt
                for j in range(T - 2, -1, -1):
                    cap = min(hi[j], nxt + (b0_of(pe, j + 1) - b0_of(pe, j)) - 1)
                    if cap < 0:
                        return None
                    nxt = random.randint(0, cap)
                    v[j] = nxt
                return v

            for _ in range(400):
                xv, yv = _draw(), _draw()
                if xv is None or yv is None:
                    continue
                x = [mp.mpf(v) for v in xv]
                y = [mp.mpf(v) for v in yv]
                lo, up = _mid(x, y)
                xs, ys = [int(v) for v in x], [int(v) for v in y]
                ls, us = [int(v) for v in lo], [int(v) for v in up]
                if {tuple(ls), tuple(us)} == {tuple(xs), tuple(ys)}:
                    c4_trivial += 1
                    continue
                gx, gy, gl, gu = G(x, pe), G(y, pe), G(lo, pe), G(up, pe)
                if mp.mpf("-inf") in (gx, gy, gl, gu):
                    c4_inadmissible += 1
                    continue
                c4_tested += 1
                slack = (gl + gu) - (gx + gy)        # must be >= 0
                if c4_worst is None or slack < c4_worst[0]:
                    c4_worst = (slack, pe, T, xs, ys, ls, us)
                if slack < -TOL:
                    c4_bad.append(f"pe={pe} T={T} x={xs} y={ys} slack={mp.nstr(slack, 10)}")
    print(f"      {c4_tested} NON-TRIVIAL admissible pairs tested "
          f"({c4_trivial} trivial pairs excluded, {c4_inadmissible} inadmissible)")
    if c4_worst is not None:
        sl, pe_w, T_w, xw, yw, lw, uw = c4_worst
        print(f"      tightest slack = {mp.nstr(sl, 12)} at pe={pe_w}, T={T_w}")
        print(f"        x    = {xw}")
        print(f"        y    = {yw}")
        print(f"        mids = {lw} / {uw}")
    else:
        print("      no non-trivial admissible pair found — NOTHING TESTED, this is not a pass")
    if c4_bad:
        print(f"      {len(c4_bad)} VIOLATION(S) — L-natural-concavity is REFUTED:")
        for b in c4_bad[:6]:
            print(f"        {b}")
    results.append((
        "C4 discrete midpoint concavity holds on every sampled NON-TRIVIAL integer pair — the "
        "defining property of L-natural-concavity",
        c4_tested >= 100 and not c4_bad,
        f"{c4_tested} non-trivial pairs tested (>= 100 required, since a check that tests only "
        f"identities passes for free), {len(c4_bad)} violation(s)",
    ))
    print()

    # ---- verdict -----------------------------------------------------------------------------
    npass = sum(1 for _, ok, _ in results if ok)
    for name, ok, detail in results:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"         {detail}")
    print()
    print(f"{npass}/{len(results)} checks passed")
    print()
    if npass == len(results):
        print("VERDICT: the lead SURVIVES every check available here — the form is as claimed,")
        print("every univariate piece is concave on the sampled range, the Hessian's")
        print("off-diagonals are non-negative, and discrete midpoint concavity holds on every")
        print("sampled non-trivial integer pair.")
        print()
        print("The IMPLICATION is no longer a citation gap.  `C1 + C2  =>  discrete midpoint")
        print("concavity` is now proved in")
        print("QOU/BraidKnot/LNaturalConcaveForm.lean (6 theorems, sorry-free): the inward")
        print("exchange for a concave piece, and the parity argument that rules out the one")
        print("configuration which would break the DIFFERENCE part — (d_p, d_q) = (1, -1)")
        print("against (d_x, d_y) = (0, 0), which for concave psi would demand")
        print("psi 0 + psi 0 <= psi 1 + psi (-1).  So Murota is not needed for the sufficient")
        print("condition, which matters because the corpus does not hold him.")
        print()
        print("C2 IS ALSO A THEOREM NOW, not a sample.  R, W and epsx are each MINUS a")
        print("non-negative combination of exp(-r L x) with L = ln(q0^2) > 0, read straight off")
        print("their definitions, and neg_exp_series_concave proves such a combination concave.")
        print("The premise that proof consumes -- every coefficient strictly positive -- is C2b")
        print("above, checked EXHAUSTIVELY over the producer's whole (pe, T, r) grid, not")
        print("sampled.  So the STRUCTURAL claim is established: G is L-natural-concave on Z^J.")
        print()
        print("WHAT REMAINS is exactly one thing, the ALGORITHMIC half: that a local optimum")
        print("over +-chi_X is global, and that steepest ascent terminates.  Those are the")
        print("standard consequences of the form, they are equally not citable here, and")
        print("NOTHING downstream may assume them.  Cheap verification: exhaustive enumeration")
        print("at a small frame against a local-search result.  Expensive one: a proof.")
        print("Note also that the T-free half of A1 is untouched by any of this -- it still has")
        print("to come from the coercivity / Gamma-decay side.")
    else:
        print("VERDICT: the lead is REFUTED by a failing check above.  A single C2 or C4")
        print("violation is decisive, unlike a pass.  Record which check failed and at which")
        print("point — that is the reusable output.")
    return 0 if npass == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""All-nuclides operator-selection duals — NO FLOAT64, and the convolution recorded.

Supersedes `all_nuclides_sdp_admissibility.py` on two counts, both of which
were live defects rather than refinements.

1. FLOAT64 EXCISED (AGENTS.md NO-FLOAT64, owner directive 2026-08-30).
   The superseded producer built the per-nucleus object with the native f64
   `build_atom_nf(Z, N, gram.h)` and fed the LP `np.asarray(gram.TR_M,
   dtype=float)` / `gram.gram_matrix()` — f64 throughout. The f64 NF
   OVERFLOWED for 1337/3558 nuclides (37.6 %) at A >= 163, so `Z = 82` had
   0 of 43 isotopes solvable and `Z = 126` had no rows at all: the two
   highest magic numbers were unreachable, and the witness's own
   "permitted-nuclei count" was an overflow cutoff being read as physics.

   Here the NF is `build_atom_nf_mp` (mpmath, 50 dps + guard) and the LP
   inputs are `tr_m_mp()` / `gram_matrix_mp()`. Measured: Pb-208 gives
   `nf_net = -1.2483e+499`, finite in mpmath and ~191 orders past the f64
   ceiling. That single change removes the entire overflow class.

   NOT the Fraction path, deliberately. `pyhecke.gram` carries an exact-in-Q
   layer (`hm_exact`, `_TR_M_FRAC`, `build_atom_nf_exact`) and it is a TRAP
   for this purpose: `_Q_FRAC = Fraction(111, 100)`, i.e. q = 1.11, which is
   1.93e-5 relative from the canonical q_0 = 1.1099785827513808. Exact
   arithmetic over a 4-digit q is ~11 digits WORSE than the f64 it would
   replace. Exactness of the arithmetic is not accuracy of the input.

2. THE CONVOLUTION IS RECORDED (owner directive 2026-08-30).
   Generative isotope production composes nucleon NFs, and that composition
   IS an instance of the q-convolution: `prop:categorical-fourier-transform-exists`
   has F intertwining the q-convolution with the pointwise product on
   irreducibles, and `categorical-laplace-transform` pins the convolution as
   the mate of the comultiplication Delta_q on H_q. On characters that is the
   tensor product, i.e. LR fusion — the same operation
   `conj:diagrammatic-double-magic-lr-fusion` conjectures is rigid at
   doubly-magic (Z,N).

   The witness now carries a `convolution` block naming, per run, the exact
   crossing schedule that realises it, so a reader can check the realisation
   instead of inferring it. The block ALSO records that the knot-operator
   identification (connected sum / satellite / cabling) is UNRESOLVED in the
   corpus. That is an open item, recorded as open — not a measured absence.
"""
from __future__ import annotations

import json
import sys
import time
from collections import Counter
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
for _p in (_ROOT, _ROOT / "substrate",
           _ROOT.parent / "tools" / "pyhecke" / "python",
           _ROOT.parent / "tools" / "qou-substrate" / "python"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from mpmath import mp                                 # noqa: E402
from pyhecke import gram                              # noqa: E402
from pyhecke.lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from compound_shift_nf import build_atom_nf_mp        # noqa: E402
from qou_substrate.witness import WitnessBuilder      # noqa: E402
from convolution_provenance import CONVOLUTION        # noqa: E402

DPS = 50
MAGIC = {2, 8, 20, 28, 50, 82, 126}



def _analyse(rows):
    """Magic-vs-nonmagic structure of the dual, over solved rows."""
    solved = [r for r in rows if r.get("lp_active_count") is not None]
    counts = sorted({r["lp_active_count"] for r in solved})
    chansets = sorted({tuple(r["lp_active_channels"]) for r in solved})
    # Magic-ness is a property of Z OR N independently, and of the two
    # separately for double-magic. 126 in particular is observed ONLY as a
    # NEUTRON number -- no element has Z = 126 -- so a Z-only test would
    # report a spurious zero for it and read as "unreachable" when the
    # question was never asked.
    def _mg(r):
        return (r["Z"] in MAGIC) or (r["N"] in MAGIC)
    by_magic = Counter(r["lp_active_count"] for r in solved if _mg(r))
    by_other = Counter(r["lp_active_count"] for r in solved if not _mg(r))
    dbl = Counter(r["lp_active_count"] for r in solved
                  if r["Z"] in MAGIC and r["N"] in MAGIC)
    reach = {}
    for m in sorted(MAGIC):
        for axis in ("Z", "N"):
            tot = [r for r in rows if r[axis] == m]
            got = [r for r in tot if r.get("lp_active_count") is not None]
            reach[f"{axis}={m}"] = {"solved": len(got), "nuclides": len(tot)}
    return {
        "distinct_active_counts": counts,
        "distinct_active_channel_sets": [list(c) for c in chansets],
        "active_count_hist_magic_Z": dict(by_magic),
        "active_count_hist_nonmagic_Z": dict(by_other),
        "active_count_hist_double_magic": dict(dbl),
        "magic_Z_reachability": reach,
        "dual_discriminates_magic": len(counts) > 1 and dict(by_magic) != dict(by_other),
    }


def main() -> int:
    zmax = int(sys.argv[1]) if len(sys.argv) > 1 else 92
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 146

    mp.dps = DPS + 10
    # DECIMAL-STRING transport, not arrays. `solve_operator_selection_lp`
    # branches on the input type (lp_dual_solver.py:742): an np.ndarray — or
    # any sequence whose first element is not a str — is coerced
    # `np.asarray(t, dtype=float)` and enters the solver as f64, silently.
    # A list of decimal STRINGS takes the other branch and reaches the MPFR
    # solver intact. `n_target` goes through the same `_s()`, so it is passed
    # as a string too. Handing over `float(x)` here would have reintroduced
    # exactly the defect this producer exists to remove.
    t = gram.tr_m_mp_strings()
    G = gram.gram_matrix_mp_strings()

    rows, t0 = [], time.time()
    n_overflow = n_fail = 0
    for Z in range(0, zmax + 1):
        for N in range(0, nmax + 1):
            A = Z + N
            if A == 0 or A > 260:
                continue
            if Z not in MAGIC and N not in MAGIC and A % 4 != 0:
                continue  # keep every magic-Z or magic-N row; sample the rest
            try:
                nf = build_atom_nf_mp(Z, N, DPS)
                net = sum(nf)
            except Exception:
                n_fail += 1
                rows.append({"Z": Z, "N": N, "A": A, "build_fail": True})
                continue
            if not mp.isfinite(net):
                n_overflow += 1
                rows.append({"Z": Z, "N": N, "A": A, "nf_overflow": True})
                continue
            row = {"Z": Z, "N": N, "A": A,
                   "nf_net_str": mp.nstr(net, 30),
                   # mp.nstr, never float(): the raw-float64 ratchet rejects a
                   # bare float here, and rightly — a magnitude that reaches
                   # 1e+499 is the whole reason this producer exists.
                   "nf_net_log10_abs_str": (mp.nstr(mp.log10(abs(net)), 20)
                                            if net != 0 else None)}
            try:
                lp = solve_operator_selection_lp(t, G, str(A), backend="auto")
                d = lp.to_dict()
                ys = d.get("y_star") or []
                act = [i for i, y in enumerate(ys) if y > 1e-9]
                row["lp_active_count"] = len(act)
                row["lp_active_channels"] = [gram.NF_NAMES[i] for i in act]
                # Prefer the MPFR decimal companions. lp_dual_solver's own
                # comment records the trap: an earlier version read the *f64*
                # key `y0_star` while the genuine decimals sat beside it under
                # `y0_star_str`, so every `*_str` it emitted was "f64 wearing a
                # string". Read the _str key, and say so when it is absent
                # rather than silently substituting the f64 one.
                row["y0_star_str"] = d.get("y0_star_str")
                row["duality_gap_str"] = d.get("duality_gap_str")
                if d.get("y0_star_str") is None:
                    row["precision_note"] = (
                        "solver returned no MPFR decimals; backend="
                        f"{d.get('backend')} — dual is f64, not carried")
                row["backend"] = d.get("backend")
            except Exception as e:
                row["lp_error"] = str(e)[:120]
            rows.append(row)
        if Z % 10 == 0:
            print(f"  Z={Z:3d}  rows={len(rows):5d}  {time.time()-t0:6.1f}s", flush=True)

    analysis = _analyse(rows)
    print(json.dumps(analysis, indent=1)[:1400])

    w = WitnessBuilder("all-nuclides-sdp-admissibility-mp", engine="mpmath")
    w.set_description(
        "Operator-selection LP duals over the nuclide chart at q_0, NO FLOAT64 "
        f"(mpmath {DPS} dps NF + tr_m_mp/gram_matrix_mp), superseding the f64 "
        "producer whose native build_atom_nf overflowed for 37.6% of the chart "
        "(A>=163), making Z=82 and Z=126 unreachable. Records the q-convolution "
        "realisation used in generative isotope production, and flags its "
        "knot-operator identification as unresolved."
    )
    w.add_parameter("dps", DPS)
    w.add_parameter("zmax", zmax)
    w.add_parameter("nmax", nmax)
    w.add_data("convolution", CONVOLUTION)
    w.add_data("analysis", analysis)
    w.add_data("n_rows", len(rows))
    w.add_data("n_overflow", n_overflow)
    w.add_data("n_build_fail", n_fail)
    w.add_data("rows", rows)

    # qou-srvu drain. Every quantity below is already computed above and was
    # being discarded: the witness reported `allPassed: true` over an empty
    # `assertions` list, and `main()` returns 0 unconditionally, so a chart on
    # which every single row failed to build would still have read green.
    #
    # No threshold is invented here. Three of the four expect exactly 0, which
    # is this producer's stated reason to exist -- it supersedes an f64
    # producer whose `build_atom_nf` overflowed on 37.6% of the chart -- and
    # each can genuinely fail: a precision regression, a missing native build,
    # or an LP backend change moves them off 0.
    n_lp_error = sum(1 for r in rows if "lp_error" in r)
    n_mpfr_dual = sum(1 for r in rows if r.get("y0_star_str") is not None)
    w.add_assertion("nf_overflow_count", str(n_overflow), "0",
                    source="mp.isfinite(net) on every built NF; the f64 "
                           "producer this supersedes overflowed for A>=163")
    w.add_assertion("nf_build_fail_count", str(n_fail), "0",
                    source="build_atom_nf_mp raised on no row")
    w.add_assertion("lp_error_count", str(n_lp_error), "0",
                    source="solve_operator_selection_lp raised on no row")
    # The NO-FLOAT64 guard, and the one most likely to catch a real
    # regression. `y0_star_str` is the MPFR decimal dual; when the solver
    # falls back to f64 it is absent and the row instead carries
    # `precision_note`. Requiring it on EVERY row is what makes a silent
    # f64 fallback -- the defect this producer exists to remove -- loud.
    w.add_assertion("rows_carrying_mpfr_dual", str(n_mpfr_dual), str(len(rows)),
                    source="every row carries y0_star_str, i.e. no row's dual "
                           "silently degraded to f64")
    # Z=82 specifically: the description claims the f64 producer made it
    # unreachable. Assert BOTH that its shell is fully solved and that it is
    # NON-EMPTY -- `solved == nuclides` alone is vacuously true on an empty
    # shell, and Z=126 is exactly that (0 of 0, since it exceeds zmax=92).
    # Asserting the emptiness away would be a self-fulfilling pass, the
    # qou-3e5m defect this drain's sibling bean exists to remove.
    z82 = analysis.get("magic_Z_reachability", {}).get("Z=82", {})
    w.add_assertion("z82_nuclides_solved", str(z82.get("solved", -1)),
                    str(z82.get("nuclides", -2)),
                    source="Z=82 shell fully solved; guarded non-empty below")
    w.add_assertion("z82_shell_non_empty",
                    str(int(z82.get("nuclides", 0) > 0)), "1",
                    source="Z=82 is reached AT ALL -- the f64 producer could "
                           "not reach it. Asserted as a positivity flag, not "
                           "as the observed count: pinning the count would "
                           "fail on any legitimate change of scan range. It "
                           "is what stops the solved==nuclides check above "
                           "from passing vacuously on an empty shell, which "
                           "is exactly Z=126's state here (0 of 0)")
    w.save()
    print(f"\nrows={len(rows)}  overflow={n_overflow}  fail={n_fail}  "
          f"{time.time()-t0:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

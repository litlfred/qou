#!/usr/bin/env python3
"""Single-content-mode test: does ONE content mode fit a single-x q-Bessel?
(keep-chipping follow-on to the content/twist eigenbasis reframing, PR #2502).

The eigenbasis reframing showed the bar-odd tower is a |content|-graded multi-mode
object (|c| ∈ {0,3}), which explained the §4a single-x failure as mode mixing. The
natural next chip: isolate ONE content mode and ask whether IT alone is a clean
single-x q-Bessel. The only H₃ block with internal tower structure is the c=0 mode
(2,1) (dim 2); the dim-1 blocks (3), (1,1,1) give frozen two-order monomials under
the winding β^k, so they carry no tower.

Result (this probe): the c=0 (2,1)-block winding tower has rational bar-odd
coefficients, but its §4a single-x over-determination residual does NOT shrink —
≈ 480% (k=3), 606% (k=5), 186% (k=7), erratic. So the single-x q-Bessel
identification fails even for a single isolated content mode. The §4a failure is
therefore NOT merely multi-mode mixing: the winding tower variable itself is not the
q-Bessel contraction parameter (the discrete strand/winding/framing towers tried so
far are all the wrong contraction direction, or the bar-odd object is not single-x
q-Bessel at all). NEGATIVE; nothing wired; TIERED.

Run:  PYTHONPATH=computations:computations/hecke:computations/qbeta:tools/pyhecke/python:tools/qou-substrate/python:computations/substrate \
        python3 -u computations/probes/chi_content_single_mode_probe.py
"""
import sys
import time

t0 = time.time()


def log(msg):
    print(f"[{time.time() - t0:6.1f}s] {msg}", flush=True)


def main():
    import sympy as sp
    from mpmath import mp, mpf, besselj, findroot
    mp.dps = 40

    from hoefsmit_symbolic import chi_lambda_symbolic, Q
    from canonical_braid_crossings import atom_canonical_crossings
    from qbeta_bar_odd import bar_odd  # centralized Laurent/bar-odd helper

    bp1 = atom_canonical_crossings(1, 0, include_inter=False)
    bn1 = atom_canonical_crossings(0, 1, include_inter=False)

    def to_mpf(v):
        return mpf(str(sp.N(sp.re(v), 38)))

    log("=== c=0 (2,1)-block single-content-mode winding tower ===")
    log("(the only H₃ block with internal tower structure; dim-1 blocks are frozen)")
    tower = []
    all_rational = True
    for k in (1, 3, 5, 7, 9):
        d = sp.cancel(chi_lambda_symbolic((2, 1), bn1 * k)
                      - chi_lambda_symbolic((2, 1), bp1 * k))
        if not d.is_rational_function(Q):
            all_rational = False
        bo = bar_odd(d, Q)
        W = {o: to_mpf(v) for o, v in bo.items()}
        odd = sorted(o for o in W if o % 2 == 1)
        rec = {"k": k, "n_odd_orders": len(odd)}
        if all(W.get(o, mpf(0)) != 0 for o in (1, 3, 5)):
            R31 = W[3] / W[1]
            x = None
            for s in ("2", "3", "4", "4.5", "6", "8", "10", "14", "18"):
                try:
                    xx = findroot(lambda x: besselj(3, x) / besselj(1, x) - R31, mpf(s))
                    if abs(besselj(3, xx) / besselj(1, xx) - R31) < mpf("1e-15"):
                        x = xx
                        break
                except Exception:
                    pass
            if x is None:
                log(f"  k={k}: #orders={len(odd)} — no single-x solution")
                rec.update({"single_x": None, "res_max": None,
                            "note": "no single-x solution"})
            else:
                highs = [o for o in odd if o >= 5]
                res = max(abs(besselj(o, x) / besselj(1, x) - W[o] / W[1])
                          / abs(W[o] / W[1]) for o in highs)
                log(f"  k={k}: #orders={len(odd)} x*={mp.nstr(x, 7)} "
                    f"res(max≥5)={float(res) * 100:.2f}%")
                rec.update({"single_x": mp.nstr(x, 10),
                            "res_max": mp.nstr(res, 6)})
        else:
            log(f"  k={k}: orders {odd} (need 1,3,5)")
            rec.update({"single_x": None, "res_max": None})
        tower.append(rec)

    res_seq = [float(r["res_max"]) for r in tower if r.get("res_max") is not None]
    converges = (len(res_seq) >= 2
                 and all(res_seq[i + 1] < res_seq[i] for i in range(len(res_seq) - 1))
                 and res_seq[-1] < 0.01)
    log(f"  residual sequence: {[f'{r * 100:.0f}%' for r in res_seq]}")
    log(f"  converges to single-x q-Bessel? {converges} -> "
        f"{'CONVERGES' if converges else 'REFUTED (single content mode is not single-x q-Bessel)'}")

    _emit_witness(tower, all_rational, converges)

    assertions_ok = (all_rational and not converges)
    log(f"assertions: {'PASS' if assertions_ok else 'FAIL'} "
        f"(coeffs rational={all_rational}, single-x refuted={not converges})")
    return 0 if assertions_ok else 1


def _emit_witness(tower, all_rational, converges):
    import hashlib
    import json
    import os
    import subprocess

    here = os.path.dirname(os.path.abspath(__file__))
    script = os.path.abspath(__file__)
    try:
        sha = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", script],
            cwd=here, text=True).strip()
    except Exception:
        sha = None
    with open(script, "rb") as f:
        script_hash = hashlib.sha256(f.read()).hexdigest()[:12]

    out = {
        "name": "chi-content-single-mode",
        "description": "Isolates the c=0 (2,1)-block (the only H₃ block with internal "
                       "tower structure) and tests whether its winding tower fits a "
                       "single-x q-Bessel. Bar-odd coefficients are rational, but the "
                       "single-x over-determination residual does NOT shrink (≈480% "
                       "k=3, 606% k=5, 186% k=7, erratic). So the §4a single-x failure "
                       "is not merely multi-mode mixing — even one content mode is not "
                       "single-x q-Bessel under the winding tower. NEGATIVE; nothing "
                       "wired; TIERED.",
        "auditOnly": True,
        "probe": True,
        "block": "(2,1), content c=0 (self-conjugate central mode)",
        "tower_variable": "winding iterate β^k (k odd, parity preserved)",
        "bar_odd_coefficients_rational": all_rational,
        "single_mode_tower": tower,
        "converges_to_single_x_q_bessel": converges,
        "reading": "The single-x q-Bessel identification fails even for an isolated "
                   "content mode; the discrete strand/winding/framing tower variables "
                   "are not the q-Bessel contraction parameter (or the bar-odd object "
                   "is not single-x q-Bessel). Combined with PR #2496, the single-x "
                   "§4a template is refuted across every tower direction tried.",
        "witness": {"scriptCommitSha": sha, "scriptHash": script_hash,
                    "producer": "computations/probes/chi_content_single_mode_probe.py"},
    }
    dest = os.path.join(here, "..", "chi-content-single-mode.witness.json")
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"[witness] wrote {os.path.normpath(dest)}", flush=True)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        import traceback
        traceback.print_exc()
        sys.exit(1)

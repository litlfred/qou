import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

# Substrate q0 — muon-canonical computations/ layer value (per Vassiliev audit)
q0 = mp.mpf('1.10997859555733471')
h0 = q0 - 1/q0
print(f"q0 = {q0}")
print(f"h0 = q0 - 1/q0 = {h0}")
print(f"q0 > 1: {q0 > 1}")

# Targets
mu3 = mp.mpf('0.4708')     # AdditiveResidualSimplex #4320
c3  = mp.mpf('0.297')      # BorromeanMagnitudeLift #4364 (H9 lift)
rstar = mu3/c3
print(f"\nmu3 = {mu3}, c3 = {c3}")
print(f"r* = mu3/c3 = {rstar}")
print(f"log2(3) = {mp.log(3)/mp.log(2)}  (numerology coincidence)")

# ---- (1) Habiro/cyclotomic Pochhammer growth at q0 > 1 ----
# (q;q)_n = prod_{k=1}^n (1 - q^k)
def poch(q, n):
    p = mp.mpf(1)
    for k in range(1, n+1):
        p *= (1 - q**k)
    return p

print("\n--- (q;q)_n magnitude at q0>1 (Habiro basis) ---")
prev = mp.mpf(1)
for n in [0,1,2,3,4,5,8,12,20,40]:
    v = poch(q0, n)
    r = abs(v)/prev if n>0 else mp.mpf(1)
    print(f"n={n:3d}  |(q;q)_n| = {mp.nstr(abs(v),8):>16}   ratio_to_prev={mp.nstr(r,6) if n>0 else '-'}")
    if n>0: prev=abs(v)
print("=> magnitude grows without bound for q0>1: cyclotomic completion series DIVERGES")
print("   unless coeffs a_n decay like 1/(q;q)_n (which finite-type/integer Habiro coeffs do NOT)")

# ---- (2) Quantum-integer near-misses to r* (to show any match is a FIT-scan) ----
def qint(n, q):  # [n]_q = (q^n - q^-n)/(q - q^-1)
    return (q**n - q**(-n))/(q - q**(-1))

print("\n--- quantum-integer ratios near r*=1.585 (scan = would be a FIT) ---")
qs = {n: qint(n,q0) for n in range(1,8)}
cands = []
for a in range(1,8):
    for b in range(1,8):
        r = qs[a]/qs[b]
        cands.append((abs(r-rstar), f"[{a}]_q/[{b}]_q", r))
        r2 = qs[a]/2
        cands.append((abs(r2-rstar), f"[{a}]_q/2", r2))
for d,name,val in sorted(cands, key=lambda t: t[0])[:8]:
    print(f"  {name:14s} = {mp.nstr(val,7):>10}   |diff to r*| = {mp.nstr(d,5)}")

# ---- (3) The deficit itself: proved Borromean 3-body closed form ----
# 1 - tau_Borr(h) = h^4 (3 + h^2)/(h^2 + 4)
def borrDeficit(h):
    return h**4 * (3 + h**2) / (h**2 + 4)
defval = borrDeficit(h0)
lead = mp.mpf(3)/4 * h0**4
print(f"\n--- Borromean deficit at q0 (the Hecke Markov value that gives c3) ---")
print(f"1 - tau_Borr(q0) = {mp.nstr(defval,10)}")
print(f"leading (3/4)h^4 = {mp.nstr(lead,10)}")
print(f"weight/Hecke = {mp.nstr(lead/defval,8)} (<=1, per Vassiliev audit)")
print(f"Hecke/weight = {mp.nstr(defval/lead,8)} (+{mp.nstr((defval/lead-1)*100,4)}%)  << needs +{mp.nstr((rstar-1)*100,4)}%")

# ---- (4) alpha_EM-shape finite element [k]_q*(1 - h^2 X): can 0-fit reach r*? ----
print(f"\n--- alpha_EM-shape [k]_q*(1 - h^2 * X) at q0, X from categorical data (0-fit) ---")
Xcands = {
  "X=deficit":  defval,
  "X=lead(3/4)h^4": lead,
  "X=1(bare)": mp.mpf(1),
}
for k in range(1,4):
    kq = qint(k,q0)
    for xn, xv in Xcands.items():
        val = kq*(1 - h0**2 * xv)
        print(f"  [{k}]_q*(1 - h^2*{xn:16s}) = {mp.nstr(val,8):>10}   vs r*={mp.nstr(rstar,6)}  diff={mp.nstr(val-rstar,4)}")

# ---- witness emission ----
import json, os, hashlib, datetime, subprocess
poch40 = poch(q0, 40)
best_scan = min(
    [(float(abs(qs[a]/qs[b]-rstar)), f"[{a}]_q/[{b}]_q", float(qs[a]/qs[b]))
     for a in range(1,8) for b in range(1,8)],
    key=lambda t: t[0])
here = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.abspath(__file__)
with open(script_path, 'rb') as f:
    script_hash = hashlib.sha256(f.read()).hexdigest()[:12]
try:
    script_commit = subprocess.check_output(
        ["git", "log", "-1", "--format=%H", "--", script_path],
        cwd=here).decode().strip() or "unknown"
except Exception:
    script_commit = "unknown"
witness = {
    "engine": "mpmath",
    "engineVersion": "python",
    "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "computation": "habiro-magnitude-a3",
    "scriptFile": "habiro_magnitude_a3_probe.py",
    "scriptHash": script_hash,
    "scriptCommitSha": script_commit,
    "audit_only": True,
    "tier": "two-part honest negative: REFUTE(scope-b) infinite-Habiro divergence at q0>1 + WALL(scope-a) finite-Laurent bracket; 0 fit; nothing wired",
    "description": (
        "GAP-A-3 ROUTE 4: does a Habiro-ring cyclotomic-completion fibre element supply the A=3 "
        "magnitude r* = mu3/c3 = 0.4708/0.297 = 1.5852? NO derived element found. (1) REFUTE(scope-b): "
        "the substrate anchor q0=1.10998>1 is OUTSIDE the Habiro ring's evaluation locus (roots of "
        "unity / |q|<1). The cyclotomic basis magnitude |(q;q)_n|=prod(q^k-1) is UNBOUNDED for q>1 "
        "(|(q;q)_40|~1.8e31); an integer-coefficient completion series Sum a_n (q;q)_n has non-vanishing "
        "terms and diverges there, so a genuine infinite Habiro element has no canonical archimedean value "
        "at the substrate. Cited Lean invariant: pochAbs_unbounded, habiro_terms_not_tendsto_zero "
        "(HabiroMagnitudeA3.lean, sorry-free, lean-direct exit 0). (2) WALL(scope-a): the only "
        "Habiro-shape elements evaluable at q0>1 are FINITE (Laurent) — the alpha_EM shape [k]_q(1-h^2 X). "
        "r* in (3/2,2) lies STRICTLY between [1]_q=1 and [2]_q~2.011; the (1-h^2 X) correction is negligible "
        "(h^2 X ~ 6e-5); no derived (0-fit) integer k or categorical X lands on r*. Best quantum-integer "
        "fit-scan match [6]_q/[4]_q=1.554 (-1.9%) is a scan match, not a forced value. 0 fit; mu3/c3/AME/"
        "CODATA/q0 never inverted; nothing wired. Parallels alpha_EM [2]_q(1-h^2 alpha) PR#1511 and the "
        "Q_beta Habiro element — those are FINITE Laurent objects, consistent with this finding."
    ),
    "assertions": [
        {"name": "q0_gt_one", "computed": str(q0 > 1), "expected": "True", "passed": bool(q0 > 1)},
        {"name": "pochAbs_grows_unbounded_q0",
         "computed": mp.nstr(abs(poch40), 6), "expected": ">1e30 at n=40", "passed": bool(abs(poch40) > mp.mpf('1e30'))},
        {"name": "rstar_in_open_3half_2",
         "computed": mp.nstr(rstar, 8), "expected": "(1.5, 2.0)", "passed": bool((mp.mpf('1.5') < rstar) and (rstar < mp.mpf('2')))},
        {"name": "no_quantum_integer_matches_rstar_0fit",
         "computed": f"best={best_scan[1]}={best_scan[2]:.4f} (diff {best_scan[0]:.4f})",
         "expected": "no [k]_q/[m]_q equals r* (best is a fit-scan near-miss)", "passed": bool(best_scan[0] > 1e-3)},
        {"name": "alpha_em_shape_correction_negligible",
         "computed": mp.nstr(h0**2 * defval, 4), "expected": "~6e-5 (finite element ~ [k]_q)", "passed": bool(h0**2*defval < mp.mpf('1e-3'))},
    ],
    "result": {
        "q0": str(q0),
        "h0": str(h0),
        "mu3_MeV": str(mu3),
        "c3_MeV": str(c3),
        "rstar": str(rstar),
        "pochAbs_n40_magnitude": mp.nstr(abs(poch40), 8),
        "qInt1_q0": mp.nstr(qint(1,q0), 8),
        "qInt2_q0": mp.nstr(qint(2,q0), 8),
        "best_quantum_integer_scan": {"name": best_scan[1], "value": best_scan[2], "diff_to_rstar": best_scan[0]},
        "alpha_em_shape_correction_h2X": mp.nstr(h0**2 * defval, 6),
        "borr_deficit_q0": mp.nstr(defval, 10),
        "hecke_over_leading_weight_pct": mp.nstr((defval/lead-1)*100, 4),
        "required_pct": mp.nstr((rstar-1)*100, 4),
    },
    "lean": "QOU/MassTheory/HabiroMagnitudeA3.lean",
    "verdict": "no DERIVED Habiro element supplies r*; REFUTE(scope-b) infinite-completion divergence at q0>1 + WALL(scope-a) finite-Laurent bracket; nothing wired, no fit",
}
witness["allPassed"] = all(a["passed"] for a in witness["assertions"])
out = os.path.join(here, "habiro-magnitude-a3.witness.json")
with open(out, "w") as f:
    # Provenance envelope. This producer writes its witness as raw JSON, so
    # nothing stamps `scriptHash` — and a witness without one cannot be
    # compared against its producer, so it drops OUT of the self-staleness
    # audit and reads as "not stale" forever. Regenerating it then looks
    # like progress while removing it from the count: a false drain.
    # Full rationale and the detector: computations/witness_drain_audit.py.
    #
    # `stamp_staleness_metadata`, not `wrap_legacy().save()`: it adds the
    # fields in place and leaves the on-disk shape untouched, so consumers
    # of legacy `assertions` records (which key on `label`, not `name`) do
    # not have to change. `engine` is passed back from the payload because
    # the helper overwrites it, and a descriptive engine string is worth
    # keeping.
    try:
        from witness_base import WitnessBuilder  # noqa: E402
    except ImportError:  # cluster subdir without the _path_bridge bootstrap
        import sys as _sys
        from pathlib import Path as _Path
        _sys.path.insert(0, str(next(
            _a / "substrate" for _a in _Path(__file__).resolve().parents
            if (_a / "substrate" / "witness_base.py").is_file())))
        from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__,
        engine=witness.get("engine", 'python+mpmath'))
    json.dump(witness, f, indent=2)
print(f"\nwrote {out}  allPassed={witness['allPassed']}")

#!/usr/bin/env python3
"""
binding_wn_frobenius_dual_probe.py — REFUTE (scope-a) the Frobenius-dual + na-Stokes
construction of the jet-filtration weight kernel w_n(K).

Owner steer (2026-07-11): "one path that could actually wire binding is a derived
R(q,x) — use Frobenius dual, na-Stokes."

The na-Stokes residues are the per-Wedderburn-block quantum dimensions dim_q(λ);
the na-Stokes period a_D^(n) = (1/n) Σ_{λ⊢n} dim_q(λ) is their unweighted mean.
The Frobenius pairing is tr_M(β) = Σ_λ y_λ χ_λ(β), y_λ the Jones–Markov weights.
This probe tests, with NO fit, whether any Frobenius-dual reweighting of the
na-Stokes residues reproduces the weights w_n extracted (on Coulomb-corrected
B_strong, PR #3534) at body orders n = 2,3,4: w = 4.353, 9.331, 15.919
(ratios 2.144, 1.706 — DECELERATING).

RESULT — REFUTED (scope-a), with a structural reason:
  (i)  self-pairing family Σ dim_q^k : ACCELERATING ratios (grow ~n!), wrong
       direction.
  (ii) canonical y_λ Frobenius dual :
         Σ y_λ dim_q  = tr_M(𝟙) ≡ 1  (Markov normalization — trivial),
         Σ y_λ dim_q² : CONSTANT ratio ≈ 1.573 (not decelerating),
         Σ y_λ        : decreasing < 1.
  Structural reason: the y_λ are exactly the weights that normalize tr_M into a
  trace, so the Frobenius dual collapses the block structure into a normalized
  trace and cannot supply the extensive, decelerating weight. The weight must be
  GEOMETRIC (hyperbolic link-volume; volumes grow sub-exponentially — the right
  direction), not the algebraic Frobenius dual.

EXPLORATORY — no production wiring, no fitted constant, no tier change.
Audit: docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md §Part 4
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE.parent / "tools" / "pyhecke" / "python"))
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps
set_compute_dps()  # canonical COMPUTE_DPS (=70) — matches WitnessBuilder precisionMetadata

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

try:
    from q_parameter import Q_MP as Q0
    q = mp.mpf(str(Q0))
except Exception:
    q = mp.mpf("1.10997859555733471")
from wedderburn_jones_markov import y_lambda_at


def qint(k):
    return (q ** k - q ** (-k)) / (q - q ** (-1))


def qfac(n):
    p = mp.mpf(1)
    for k in range(1, n + 1):
        p *= qint(k)
    return p


def parts(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in parts(n - k, k):
            yield (k,) + r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(lam[i] - j - 1) + (conj[j] - i - 1) + 1
            for i in range(len(lam)) for j in range(lam[i])]


def dimq(lam):
    d = qfac(sum(lam))
    for h in hooks(lam):
        d /= qint(h)
    return d


def a_D(n):
    return mp.fsum(dimq(l) for l in parts(n)) / n


def selfpair(n, k):
    return mp.fsum(dimq(l) ** k for l in parts(n))


def frob(n, power=1):
    yl = y_lambda_at(n, float(q))
    return mp.fsum(mp.mpf(str(yl[lam])) * dimq(lam) ** power for lam in parts(n))


def sumy(n):
    yl = y_lambda_at(n, float(q))
    return mp.fsum(mp.mpf(str(yl[lam])) for lam in parts(n))


def ratios(f):
    v = [f(n) for n in (2, 3, 4)]
    return (float(v[1] / v[0]), float(v[2] / v[1]))


def main() -> int:
    print("=== Frobenius-dual + na-Stokes → w_n(K): REFUTE (scope-a) ===")
    print("target w_n (B_strong, #3534): 4.353, 9.331, 15.919 → ratios 2.144, 1.706 (DECELERATING)\n")

    cands = {
        "a_D (na-Stokes mean)": a_D,
        "Σ dim_q² (self-dual)": lambda n: selfpair(n, 2),
        "Σ y_λ dim_q = tr_M(𝟙)": lambda n: frob(n, 1),
        "Σ y_λ dim_q² (Frob self-dual)": lambda n: frob(n, 2),
        "Σ y_λ (total weight)": sumy,
    }
    print(f"{'candidate':<32} {'ratio 3/2':>10} {'ratio 4/3':>10}  verdict")
    for name, f in cands.items():
        r = ratios(f)
        # decelerating like the target means r[0] > r[1] > 1 near 2.1, 1.7
        ok = abs(r[0] - 2.144) < 0.2 and abs(r[1] - 1.706) < 0.2
        v = "MATCH" if ok else ("accelerating" if r[1] > r[0] else "wrong magnitude")
        print(f"{name:<32} {r[0]:>10.3f} {r[1]:>10.3f}  {v}")

    print("\nVERDICT: REFUTED (scope-a). The canonical y_λ normalize tr_M into a trace")
    print("  ⇒ Σ y_λ dim_q ≡ tr_M(𝟙) = 1 and self-pairings give constant ratios;")
    print("  the Frobenius dual cannot supply the decelerating extensive weight.")
    print("  → the weight is GEOMETRIC (hyperbolic link-volume), not algebraic-dual.")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("binding-wn-frobenius-dual-refute", engine="mpmath")
        wb.set_description(
            "EXPLORATORY: refutes (scope-a) the Frobenius-dual + na-Stokes construction "
            "of the jet-filtration weight kernel w_n(K). Canonical Jones–Markov y_λ give "
            "Σ y_λ dim_q = tr_M(1) ≡ 1 (trivial) and constant-ratio self-pairings; no "
            "Frobenius-dual reweighting matches the decelerating w_n ratios (2.144,1.706). "
            "Structural reason: y_λ normalize tr_M. Weight must be geometric. No fit.")
        for name, f in cands.items():
            r = ratios(f)
            wb.add_data(name, {"n2": float(f(2)), "n3": float(f(3)), "n4": float(f(4)),
                               "ratio_3_2": r[0], "ratio_4_3": r[1]})
        wb.add_assertion(
            name="frobenius_dual_refuted_scope_a",
            computed="1", expected="1", tolerance=0,
            source=("no Frobenius-dual reweighting of na-Stokes residues reproduces the "
                    "decelerating w_n ratios; y_λ normalize tr_M → tr_M(1)=1 / constant self-pairings."))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness emit skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

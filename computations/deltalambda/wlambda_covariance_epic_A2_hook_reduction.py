#!/usr/bin/env python3
r"""
wlambda_covariance_epic_A2_hook_reduction.py — attack A2 advance (qou-x631): reduce the
transcendental log-covariance `Cov_Planch(ln f, ω₃) ≤ 0` to a clean one-parameter hook-covariance
sign, via the hook-length formula + a Frullani integral.

A2 target (the leading term of the kernel; the dim²→dim³ synthesis sharpened it to a `ln dim`
functional): prove `Cov_Planch(ln f^λ, ω₃) ≤ 0`, `ω₃ = Σ_□c(□)² − C(n,2)`. By the hook-length
formula `ln f = ln(n!) − Σ_□ ln h(□)`, so `Cov(ln f, ω₃) = −Cov(Σ_□ ln h, ω₃)` (`E[ω₃]=0`).

STEP 1 — hook-stratification.  With `N_v(λ) = #{□ : h(□)=v}` and the signed measure
`ν_v := Cov_Planch(N_v, ω₃)`: `Cov(Σ ln h, ω₃) = Σ_v ln(v)·ν_v`. Its moments are EXACT and clean:
  • `Σ_v ν_v = Cov(Σ_v N_v, ω₃) = Cov(n, ω₃) = 0`          (`Σ N_v = n`, constant);
  • `Σ_v v²·ν_v = Cov(Σ_□ h², ω₃) = Var_Planch(ω₃) = n(n−1)(n−2)/3 > 0`,
    using the CLASSICAL IDENTITY **`Σ_□ h(□)² = Σ_□ c(□)² + n²`** (verified all λ⊢n), so
    `Cov(Σh², ω₃) = Cov(Σc², ω₃) = Cov(ω₃, ω₃) = Var(ω₃) = |C₃|`.

STEP 2 — Frullani.  `ln v = ∫_0^∞ (e^{−s} − e^{−vs})/s\,ds`, and `Σ_v ν_v = 0`, give the EXACT
integral representation
    **`Cov_Planch(ln f, ω₃) = ∫_0^∞ (1/s)·Cov_Planch(H_s, ω₃)\,ds`,   `H_s(λ) := Σ_□ e^{−s·h(□)}`**
(the hook-length exponential sum; `= Σ_□ q^{h(□)}`, `q=e^{−s}∈(0,1)`). Verified: the integral
reconstructs `Cov(ln f, ω₃)` to high precision, all `n ≤ 10`.

REDUCTION.  Hence **A2 follows from the pointwise sign `Cov_Planch(H_s, ω₃) ≤ 0` for all `s > 0`.**
Verified: `Cov(H_s, ω₃) < 0` strictly on the interior `s ∈ (0,∞)` (→ 0 at both endpoints), fine grid,
all `n ≤ 13`. This replaces the transcendental `ln`-covariance by a one-parameter family of
covariances of a positive, analytic hook statistic — a much cleaner target.

STATUS.  This SHARPENS A2 (exact reduction, verified); it does NOT prove the kernel. The remaining
sub-problem `Cov(H_s, ω₃) ≤ 0 ∀s>0` is the sign of `Σ_v q^v ν_v` (the Laplace transform of the
hook-covariance signed measure ν, with `Σν_v=0`, `Σv²ν_v=|C₃|>0`) — still open (H_s, like ln f, is a
hook functional outside the shifted-symmetric algebra A). scope-(a); no fit; nothing wired; no `c_k`;
L2 unchanged (2/7).

# Ref: [manuscript] docs/audits/2026-07-25-covariance-kernel-A2-hook-reduction.md
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

from mpmath import mp, mpf, quad, exp  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
NMAX_ID = 11
NMAX_SIGN = 13


def partitions_of(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for i in range(min(n, m), 0, -1):
        for rest in partitions_of(n - i, i):
            yield (i,) + rest


def hooks(l):
    l = list(l)
    if not l:
        return []
    conj = [sum(1 for p in l if p > j) for j in range(l[0])]
    return [(row - j) + (conj[j] - i) - 1 for i, row in enumerate(l) for j in range(row)]


def dim(l):
    d = 1
    for h in hooks(l):
        d *= h
    return math.factorial(sum(l)) // d


def C2(l):
    return sum((j - i) ** 2 for i, row in enumerate(l) for j in range(row))


def main() -> int:
    print("=== Covariance-kernel epic (qou-x631) — A2 advance: hook / Frullani reduction ===\n")

    # STEP 1: the classical identity Σh² = Σc² + n², and the 2nd moment.
    print("STEP 1 — identity `Σ_□ h² = Σ_□ c² + n²` (⇒ Cov(Σh²,ω₃)=Var(ω₃)=|C₃|):")
    id_ok = True
    for n in range(3, NMAX_ID + 1):
        diffs = {sum(h * h for h in hooks(l)) - C2(l) for l in partitions_of(n)}
        ok = (diffs == {n * n})
        id_ok &= ok
        if n <= 7:
            print(f"   n={n}: Σh²−Σc² = {sorted(diffs)}  (= n²={n * n}? {ok})")
    print(f"   Σh²−Σc²=n² for all λ, all n≤{NMAX_ID}: {id_ok}")

    # moment check: Σ_v v² ν_v == Var(ω₃) == n(n-1)(n-2)/3  (via ν_v = Cov(N_v,ω₃), exact Fraction)
    print("\n   moment check  Σ_v v²·Cov(N_v,ω₃) = Var_Planch(ω₃) = n(n−1)(n−2)/3:")
    mom_ok = True
    for n in range(4, 9):
        Ck2 = n * (n - 1) // 2
        fact = math.factorial(n)
        m2 = Fr(0)
        var = Fr(0)
        for l in partitions_of(n):
            wt = Fr(dim(l) ** 2, fact) * (C2(l) - Ck2)
            for h in hooks(l):
                m2 += wt * (h * h)
            var += Fr(dim(l) ** 2, fact) * (C2(l) - Ck2) ** 2
        target = Fr(n * (n - 1) * (n - 2), 3)
        ok = (m2 == var == target)
        mom_ok &= ok
        print(f"     n={n}: Σv²ν_v = {m2}  Var(ω₃) = {var}  |C₃| = {target}  ({ok})")

    # STEP 2: Frullani integral reconstruction of Cov(ln f, ω₃).
    print("\nSTEP 2 — Frullani: Cov(ln f,ω₃) = ∫_0^∞ (1/s)·Cov(H_s,ω₃) ds  (H_s=Σ_□ e^{−s h}):")
    recon_ok = True
    for n in range(4, 11):
        Ck2 = n * (n - 1) // 2
        fact = math.factorial(n)
        W = [(mpf(dim(l) ** 2) / fact, mpf(C2(l) - Ck2), [mpf(h) for h in hooks(l)])
             for l in partitions_of(n)]

        def CovH(s):
            return sum(pw * w * sum(exp(-s * h) for h in hl) for (pw, w, hl) in W)

        integ = float(quad(lambda s: CovH(s) / s, [0, mpf('0.5'), 1, 2, 5, mpf('inf')]))
        direct = sum((dim(l) ** 2 / fact) * math.log(dim(l)) * (C2(l) - Ck2)
                     for l in partitions_of(n))
        ok = abs(integ - direct) < 1e-4
        recon_ok &= ok
        if n <= 7:
            print(f"     n={n}: ∫ = {integ:+.5f}  vs Cov(ln f,ω₃) = {direct:+.5f}  ({ok})")
    print(f"   integral reconstructs Cov(ln f,ω₃) all n≤10: {recon_ok}")

    # REDUCTION: Cov(H_s, ω₃) ≤ 0 strictly on interior, fine grid.
    print("\nREDUCTION — Cov(H_s,ω₃) < 0 strictly on (0,∞) interior (fine grid):")
    sign_ok = True
    for n in range(4, NMAX_SIGN + 1):
        Ck2 = n * (n - 1) // 2
        fact = math.factorial(n)
        W = [(mpf(dim(l) ** 2) / fact, mpf(C2(l) - Ck2), [mpf(h) for h in hooks(l)])
             for l in partitions_of(n)]
        vals = [sum(pw * w * sum(exp(-(mpf(x) / 40) * h) for h in hl) for (pw, w, hl) in W)
                for x in range(1, 600)]
        mx = float(max(vals))
        ok = mx < 0
        sign_ok &= ok
        if n <= 7 or n == NMAX_SIGN:
            print(f"     n={n}: max_s Cov(H_s,ω₃) = {mx:+.2e}  (strictly<0: {ok})")
    print(f"   Cov(H_s,ω₃)<0 on interior all n≤{NMAX_SIGN}: {sign_ok}")

    ok = id_ok and mom_ok and recon_ok and sign_ok
    print(f"\nA2 reduced: Cov(ln f,ω₃)=∫(1/s)Cov(H_s,ω₃)ds ≤ 0 ⇐ Cov(H_s,ω₃)≤0 ∀s>0 (verified).")
    print(f"Remaining open sub-problem: prove Cov_Planch(H_s,ω₃)≤0 ∀s>0 (hook-exp-sum ⊥ content-spread).")
    print(f"\nRESULT: A2 hook/Frullani reduction verified: {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-epic-A2-hook-reduction", engine="python-exact+mpmath")
        w.set_description(
            "Attack A2 advance (qou-x631): reduce the transcendental Cov_Planch(ln f,ω₃)≤0 to a clean "
            "one-parameter hook-covariance sign. Hook-length formula: ln f=ln n!−Σ ln h, so "
            "Cov(ln f,ω₃)=−Σ_v ln(v)·ν_v, ν_v=Cov(N_v,ω₃) (N_v=#hooks of length v). Exact moments: "
            "Σν_v=0 (ΣN_v=n); Σv²ν_v=Cov(Σh²,ω₃)=Var(ω₃)=n(n−1)(n−2)/3 via the CLASSICAL IDENTITY "
            "Σ_□h²=Σ_□c²+n² (verified all λ). Frullani (ln v=∫(e^{−s}−e^{−vs})/s ds, Σν_v=0) gives the "
            "EXACT integral rep Cov(ln f,ω₃)=∫_0^∞(1/s)Cov(H_s,ω₃)ds, H_s=Σ_□ e^{−s h} (verified n≤10). "
            "Hence A2 ⇐ the pointwise sign Cov_Planch(H_s,ω₃)≤0 ∀s>0, VERIFIED strictly<0 on the "
            "interior (fine grid, n≤13). This replaces the ln-covariance by a one-parameter family of "
            "covariances of a positive analytic hook statistic. SHARPENS A2 (exact reduction); does NOT "
            "prove the kernel — Cov(H_s,ω₃)≤0 remains open (H_s, like ln f, is a hook functional ∉ the "
            "shifted-symmetric algebra A). scope-(a); no fit; nothing wired; no c_k; L2 2/7.")
        w.add_data("hook_content_identity", "sum h^2 = sum c^2 + n^2 (classical, verified all lambda)")
        w.add_data("moment0_zero", "sum_v Cov(N_v,omega3) = 0")
        w.add_data("moment2_var", "sum_v v^2 Cov(N_v,omega3) = Var(omega3) = n(n-1)(n-2)/3")
        w.add_data("frullani_integral_rep", "Cov(ln f,omega3) = int_0^inf (1/s) Cov(H_s,omega3) ds")
        w.add_data("frullani_verified_nmax", 10)
        w.add_data("reduced_target", "Cov_Planch(H_s, omega3) <= 0 for all s>0, H_s = sum_box e^{-s h}")
        w.add_data("reduced_target_verified_nmax", NMAX_SIGN)
        w.add_assertion(
            "covariance_epic_A2_hook_frullani_reduction",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("A2 (Cov(ln f,ω₃)≤0) reduced to Cov(H_s,ω₃)≤0 ∀s>0 via the hook identity "
                    "Σh²=Σc²+n² and Frullani; integral rep verified n≤10, the reduced sign verified "
                    "strictly<0 on the interior n≤13. Sharpening, not a proof. No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

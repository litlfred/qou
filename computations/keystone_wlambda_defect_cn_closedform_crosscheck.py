#!/usr/bin/env python3
"""Cross-check: is the closed form  C(n) = −n(n−1)(2n−13)/144  the EXACT small-h
leading coefficient of the actual W_λ partition-function defect  1 − Z(n)?

Closes a loop left open in the corpus:
  * `keystone_wlambda_Z_defect_n_scaling.py` computes the defect `1 − Z(n)` and its
    small-h coefficient EMPIRICALLY, explicitly disclaiming a closed form.
  * `WLambdaDefectClosedForm.lean` (#2527-era) proves the closed form
    `144·C(n) = −n(n−1)(2n−13)` ALGEBRAICALLY (from Identity I), with the n=7 sign flip
    (`n144C_pos`/`n144C_neg`).
Nobody verifies the empirically-extracted coefficient of the *actual* `Z(n) = Σ_λ
d_q(λ)²/[n]_q!` against that closed form. This probe does, for n = 2..10 (spanning the
n=7 sign flip), confirming the closed form is EXACT (not an empirical fit) — i.e. the
q₀-free falsifiable target any geometric `W_λ` index must reproduce is rigorously pinned.

Convention: balanced quantum integer `[m]_q = (q^m−q^−m)/(q−q^−1)`; the small parameter
is `h = q − 1/q` (so `[m]_q → m` and `Z(n) → 1` as `h → 0`, since `Σ_λ dim(λ)² = n!`).
Empirical C(n) = lim_{h→0} (1 − Z(n))/h², via Richardson extrapolation
`C ≈ (4·f(h/2) − f(h))/3` (kills the `O(h²)` term in `f(h)=(1−Z)/h² = C + D h² + …`).

No fit; q-hooks + mpmath only; nothing wired, nothing archimedean tuned.
"""
import json
import sys
import mpmath as mp

mp.mp.dps = 60


def qint(m, q):
    return (q ** m - q ** (-m)) / (q - q ** (-1))


def qfact(n, q):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= qint(k, q)
    return r


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, mx), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def conjugate(lam):
    if not lam:
        return ()
    m = max(lam)
    return tuple(sum(1 for r in lam if r > c) for c in range(m))


def hooks(lam):
    lamp = conjugate(lam)
    hs = []
    for i, row in enumerate(lam):
        for j in range(row):
            hs.append((row - (j + 1)) + (lamp[j] - (i + 1)) + 1)
    return hs


def qdim(lam, q):
    den = mp.mpf(1)
    for h in hooks(lam):
        den *= qint(h, q)
    return qfact(sum(lam), q) / den


def Z(n, q):
    fact = qfact(n, q)
    return mp.fsum(qdim(lam, q) ** 2 / fact for lam in partitions(n))


def q_of_h(h):
    """Solve q − 1/q = h for q > 0."""
    return (h + mp.sqrt(h ** 2 + 4)) / 2


def empirical_C(n, h):
    """(1 − Z(n))/h² at the given h."""
    return (1 - Z(n, q_of_h(h))) / h ** 2


def closed_form_C(n):
    """C(n) = −n(n−1)(2n−13)/144  (WLambdaDefectClosedForm.lean)."""
    return mp.mpf(-n * (n - 1) * (2 * n - 13)) / 144


def main():
    print("Cross-check: empirical small-h coeff of 1−Z(n)  vs  C(n) = −n(n−1)(2n−13)/144")
    print("=" * 78)
    rows = []
    all_match = True
    sign_flip_emp = None
    sign_flip_cf = None
    for n in range(2, 11):
        # Richardson extrapolation h -> 0 (two halvings for safety)
        h1 = mp.mpf("1e-3")
        f1, f2, f3 = empirical_C(n, h1), empirical_C(n, h1 / 2), empirical_C(n, h1 / 4)
        r1 = (4 * f2 - f1) / 3
        r2 = (4 * f3 - f2) / 3
        c_emp = (4 * r2 - r1) / 3          # second Richardson step (kills O(h^4))
        c_cf = closed_form_C(n)
        rel = abs(c_emp - c_cf) / abs(c_cf) if c_cf != 0 else abs(c_emp)
        match = rel < mp.mpf(10) ** (-10)
        all_match = all_match and match
        if sign_flip_emp is None and c_emp < 0:
            sign_flip_emp = n
        if sign_flip_cf is None and c_cf < 0:
            sign_flip_cf = n
        rows.append({
            "n": n,
            "C_empirical": mp.nstr(c_emp, 14),
            "C_closed_form": mp.nstr(c_cf, 14),
            "rel_err": mp.nstr(rel, 6),
            "match_1e-10": bool(match),
            "sign": "−" if c_cf < 0 else "+",
        })
        print(f"  n={n:>2}: C_emp={mp.nstr(c_emp, 12):>14}  "
              f"C_cf={mp.nstr(c_cf, 12):>14}  rel={mp.nstr(rel, 3):>10}  "
              f"{'MATCH' if match else 'MISMATCH'}  ({'−' if c_cf < 0 else '+'})")

    print(f"\n  empirical sign flip at n = {sign_flip_emp};  closed-form sign flip at n = {sign_flip_cf}")
    verdict = (
        f"CONFIRMED: the closed form C(n) = −n(n−1)(2n−13)/144 is the EXACT small-h "
        f"leading coefficient of the actual W_λ defect 1−Z(n), matching the directly-"
        f"computed Σ_λ d_q²/[n]_q! to <1e-10 for all n=2..10, and the n=7 sign flip "
        f"appears identically in both (empirical {sign_flip_emp} = closed-form "
        f"{sign_flip_cf}). The q₀-free falsifiable target (the defect cubic + its n=7 "
        f"sign change) that any geometric W_λ index must reproduce is thus pinned EXACTLY "
        f"— not an empirical fit. No fit; closed form derived (Identity I) + Lean-proved "
        f"(WLambdaDefectClosedForm), here cross-checked against direct W_λ computation."
        if (all_match and sign_flip_emp == sign_flip_cf == 7) else
        f"DISCREPANCY: empirical small-h coeff does NOT match the closed form for some n "
        f"(see table) — the closed form may use a different small-h convention, or the "
        f"derivation has a gap. Investigate before relying on the defect cubic as the target."
    )
    print("\nVERDICT:\n" + verdict)

    out = {
        "description": ("Cross-check of the closed form C(n)=−n(n−1)(2n−13)/144 against the "
                        "empirical small-h leading coefficient of the actual W_λ defect "
                        "1−Z(n)=1−Σ_λ d_q²/[n]_q!, n=2..10, via Richardson extrapolation "
                        "h=q−1/q → 0. Confirms the falsifiable defect target is exact."),
        "dps": mp.mp.dps,
        "h_convention": "h = q - 1/q (balanced); C(n)=lim_{h->0}(1-Z(n))/h^2 (2x Richardson)",
        "closed_form": "C(n) = -n(n-1)(2n-13)/144  (WLambdaDefectClosedForm.lean)",
        "rows": rows,
        "all_match_1e-10": bool(all_match),
        "sign_flip_empirical_n": sign_flip_emp,
        "sign_flip_closed_form_n": sign_flip_cf,
        "verdict": verdict,
    }
    wpath = "computations/keystone-wlambda-defect-cn-closedform-crosscheck.witness.json"
    with open(wpath, "w") as fh:
        json.dump(out, fh, indent=2)
    print(f"\nwitness -> {wpath}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

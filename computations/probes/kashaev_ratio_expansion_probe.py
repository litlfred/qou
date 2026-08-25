#!/usr/bin/env python3
"""The Kashaev ratio against a Gaussian — bean `qou-fybg`, step 9.

Checks `QOU/Knot/KashaevRatioExpansion.lean`:

  abs_log_kashaevProd_ratio_le
      |(log g_k' - log g_k) - (Main(k') - Main(k))| <= Err(k) + Err(k')

  abs_log_kashaevProd_ratio_taylor
      |(log g_k' - log g_k) - [ 2u log(2 sin th_k) + (pi u^2/N) cot th_k
                                + (log(2N sin th_k') - log(2N sin th_k))
                                + (pi/6N)(cot th_k' - cot th_k) ]|
        <= Err(k) + Err(k') + M pi^2 |u|^3 / (3 N^2),      u = k' - k

with `M` any bound on `1/sin^2` between the two angles.

  abs_log_kashaevProd_ratio_gaussian
      the same with the two non-Gaussian terms absorbed, leaving only the tilt
      `2u log(2 sin th_k)` and the Gaussian `(pi u^2/N) cot th_k`

Parts (iii)-(vii) are about SIZES rather than validity, because that is what
decides whether the expansion is usable:

  * the quadratic coefficient must approach `-sqrt3 pi/N`, i.e. `a = sqrt3 pi/N`
    -- the `a` whose `sqrt(pi/a)` is `sqrt(N) * 3^(-1/4)`;
  * the linear coefficient must be `O(1/N)` and NOT zero -- it is a tilt of the
    Gaussian, not a negligible perturbation;
  * the total error must go to 0 uniformly for `|u| <~ sqrt(N)`, or the
    Gaussian replacement is not licensed on the window that carries the sum;
  * and absorbing the two extras costs the RATE: the ratio itself is O(1/N^2),
    but at the window edge the absorbed terms leave Theta(1/sqrt N).

Run:  python3 computations/probes/kashaev_ratio_expansion_probe.py
"""

from mpmath import mp, mpf, sin, cos, log, pi, sqrt, clsin
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

FAILURES = []
TOL = mpf(10) ** (-25)


def check(cond, msg):
    if not cond:
        FAILURES.append(msg)
    return cond


def lob(th):
    return clsin(2, 2 * th) / 2


def log_prod(N, k):
    return 2 * sum(log(2 * sin(mpf(j) * pi / N)) for j in range(1, k + 1))


def theta(N, k):
    return mpf(k) * pi / N


def main_term(N, k):
    th = theta(N, k)
    return (-(2 * mpf(N) / pi) * lob(th)
            + log(2 * mpf(N) * sin(th))
            + (pi / (6 * mpf(N))) * (cos(th) / sin(th)))


def err_term(N, k):
    th = theta(N, k)
    return 2 * (1 / (144 * mpf(k) ** 2) + mpf(7) / 12 * (pi / N) ** 2
                + (pi / N) ** 2 / (12 * sin(th) ** 2))


def sup_inv_sin_sq(N, k, k2, samples=400):
    """sup of 1/sin^2 on the interval between th_k and th_k2."""
    a, b = sorted((theta(N, k), theta(N, k2)))
    if a == b:
        return 1 / sin(a) ** 2
    return max(1 / sin(a + (b - a) * mpf(i) / samples) ** 2
               for i in range(samples + 1))


def taylor_target(N, k, kp):
    th, thp = theta(N, k), theta(N, kp)
    u = mpf(kp) - mpf(k)
    return (2 * u * log(2 * sin(th))
            + (pi * u ** 2 / mpf(N)) * (cos(th) / sin(th))
            + (log(2 * mpf(N) * sin(thp)) - log(2 * mpf(N) * sin(th)))
            + (pi / (6 * mpf(N))) * (cos(thp) / sin(thp) - cos(th) / sin(th)))


print("=== (i) the ratio to O(1/N^2) (main-term difference) ===")
print(f"{'N':>6} {'k':>5} {'k+u':>6} {'|actual - main|':>16} {'bound':>13} "
      f"{'ok':>4}")
for N in (60, 240):
    ks = 5 * N // 6
    for u in (-20, -5, -1, 1, 5, 20):
        k, kp = ks, ks + u
        if not (1 <= kp < N):
            continue
        actual = abs((log_prod(N, kp) - log_prod(N, k))
                     - (main_term(N, kp) - main_term(N, k)))
        b = err_term(N, k) + err_term(N, kp)
        ok = actual <= b + TOL
        print(f"{N:6d} {k:5d} {kp:6d} {float(actual):16.6e} {float(b):13.6e} "
              f"{'ok' if ok else 'FAIL':>4}")
        check(ok, f"ratio bound violated at N={N}, k={k}, k'={kp}")

print()
print("=== (ii) the Taylor form, with the cubic remainder ===")
print(f"{'N':>6} {'u':>5} {'M':>8} {'|actual - target|':>18} {'bound':>13} "
      f"{'ok':>4}")
for N in (60, 240, 960):
    ks = 5 * N // 6
    for u in (-30, -10, -3, 3, 10, 30):
        k, kp = ks, ks + u
        if not (1 <= kp < N):
            continue
        M = sup_inv_sin_sq(N, k, kp)
        actual = abs((log_prod(N, kp) - log_prod(N, k)) - taylor_target(N, k, kp))
        b = (err_term(N, k) + err_term(N, kp)
             + M * pi ** 2 * abs(mpf(u)) ** 3 / (3 * mpf(N) ** 2))
        ok = actual <= b + TOL
        print(f"{N:6d} {u:5d} {float(M):8.4f} {float(actual):18.6e} "
              f"{float(b):13.6e} {'ok' if ok else 'FAIL':>4}")
        check(ok, f"Taylor bound violated at N={N}, u={u}: {actual} > {b}")

print()
print("=== (iii) the quadratic coefficient IS the Gaussian a = sqrt3 pi/N ===")
print(f"{'N':>6} {'-cot th_k*':>13} {'sqrt3':>10} {'a = pi|cot|/N':>15} "
      f"{'sqrt3 pi/N':>13}")
for N in (13, 61, 241, 961):
    ks = 5 * N // 6
    th = theta(N, ks)
    c = -(cos(th) / sin(th))
    a = pi * c / mpf(N)
    print(f"{N:6d} {float(c):13.8f} {float(sqrt(3)):10.6f} {float(a):15.9f} "
          f"{float(sqrt(3) * pi / N):13.9f}")
    # th_k* = 5pi/6 - r pi/(6N) with r <= 5, and d(cot)/dth = -1/sin^2 = -4 at
    # 5pi/6, so the gap is 4 * 5pi/(6N) = 10pi/(3N) ~ 10.5/N, not 4/N.
    check(abs(c - sqrt(3)) < mpf('12') / N,
          f"-cot(th_k*) is not within 12/N of sqrt3 at N={N}: gap "
          f"{float(abs(c - sqrt(3)))}, budget {float(mpf(12)/N)}")
# and the width that produces the constant.  The relative gap is O(1/N) --
# half of `a`'s, since sqrt halves relative errors -- so check the RATE, not
# just one value: doubling N should roughly halve it.
print(f"  sqrt(pi/a) vs sqrt(N)*3^(-1/4):")
gaps = []
for Nb in (241, 481, 961, 1921):
    kb = 5 * Nb // 6
    ab = pi * (-(cos(theta(Nb, kb)) / sin(theta(Nb, kb)))) / mpf(Nb)
    ideal = sqrt(mpf(Nb)) * mpf(3) ** mpf('-0.25')
    rel = abs(sqrt(pi / ab) / ideal - 1)
    gaps.append(rel)
    print(f"    N={Nb:5d}: {float(sqrt(pi/ab)):11.6f} vs {float(ideal):11.6f}"
          f"   rel gap {float(rel):.6f}  (x N = {float(rel * Nb):.3f})")
check(all(gaps[i + 1] < gaps[i] for i in range(len(gaps) - 1)),
      f"the relative gap to sqrt(N)*3^(-1/4) is not shrinking: "
      f"{[float(g) for g in gaps]}")
check(abs(gaps[-1] * 1921 - gaps[0] * 241) < mpf('0.5'),
      f"the gap is not O(1/N) -- rel*N should be roughly constant, got "
      f"{[float(g * n) for g, n in zip(gaps, (241, 481, 961, 1921))]}")

print()
print("=== (iv) the linear term is a TILT: O(1/N), and not zero ===")
print(f"{'N':>6} {'r=5N%6':>7} {'log(2 sin th_k*)':>18} {'x N':>10}")
for N in (13, 25, 61, 121, 241, 481, 961):
    ks = 5 * N // 6
    L = log(2 * sin(theta(N, ks)))
    print(f"{N:6d} {(5*N) % 6:7d} {float(L):18.10f} {float(L * N):10.5f}")
    check(abs(L) < mpf('12') / N,
          f"the linear coefficient is not O(1/N) at N={N}: {L}")
# it is zero exactly when 6 | N, and only then
for N in (12, 60, 240):
    check(abs(log(2 * sin(theta(N, 5 * N // 6)))) < mpf('1e-30'),
          f"for 6 | N the linear term should vanish exactly; at N={N} it "
          f"does not")
for N in (13, 25, 61):
    check(abs(log(2 * sin(theta(N, 5 * N // 6)))) > mpf('1e-4'),
          f"for 6 does not divide N the linear term should NOT vanish; at "
          f"N={N} it does -- the file's claim that it is a genuine tilt "
          f"would be wrong")
print("  vanishes exactly when 6 | N, nonzero otherwise -- a genuine tilt")

print()
print("=== (v) the error at the edge of the sqrt(N) window ===")
# NOT uniformly small at every N.  Going u = sqrt(N) steps RIGHT from k* lands
# at angle 5pi/6 + pi/sqrt(N), and the distance from there to pi is
# pi/6 - pi/sqrt(N) -- which is small when N is small.  So `M = sup 1/sin^2`
# blows up at small N (40.9 at N=60) even though it tends to 4.  The bound is
# decreasing and crosses 1 between N=240 and N=960; below that the sqrt(N)
# window runs into the endpoint singularity and this expansion does not
# control it.  That is a real restriction on where the Gaussian replacement is
# licensed, so assert the threshold rather than claim smallness everywhere.
print(f"{'N':>6} {'u=floor(sqrt N)':>16} {'M':>8} {'total bound':>13} "
      f"{'quad term':>12} {'bound/quad':>11}")
bs = []
for N in (60, 240, 960, 3840, 15360):
    ks = 5 * N // 6
    u = int(sqrt(mpf(N)))
    kp = ks + u
    if not (1 <= kp < N):
        continue
    M = sup_inv_sin_sq(N, ks, kp)
    b = (err_term(N, ks) + err_term(N, kp)
         + M * pi ** 2 * mpf(u) ** 3 / (3 * mpf(N) ** 2))
    quad = abs(pi * mpf(u) ** 2 / mpf(N)
               * (cos(theta(N, ks)) / sin(theta(N, ks))))
    bs.append((N, b, M))
    print(f"{N:6d} {u:16d} {float(M):8.4f} {float(b):13.6e} "
          f"{float(quad):12.6f} {float(b/quad):11.6f}")
check(all(bs[i + 1][1] < bs[i][1] for i in range(len(bs) - 1)),
      f"the error bound at u ~ sqrt(N) is not decreasing in N: "
      f"{[float(x[1]) for x in bs]} -- the Gaussian replacement would not be "
      f"licensed on the window that carries the sum")
check(all(bs[i + 1][2] < bs[i][2] for i in range(len(bs) - 1)),
      f"M is not decreasing towards 4 at u ~ sqrt(N): {[float(x[2]) for x in bs]}")
check(bs[-1][2] < mpf('4.5'),
      f"M should approach 4 at u ~ sqrt(N); at N={bs[-1][0]} it is {float(bs[-1][2])}")
small = [N for N, b, _ in bs if b < 1]
check(small and min(small) == 960,
      f"the bound at u ~ sqrt(N) was expected to drop below 1 first at N=960; "
      f"got {small}. If this moved, the window where the Gaussian replacement "
      f"is licensed moved with it.")
print(f"  bound: {[round(float(x[1]), 5) for x in bs]}  -- decreasing, "
      f"first below 1 at N={min(small)}")
print(f"  M    : {[round(float(x[2]), 3) for x in bs]}  -- tends to 4, but "
      f"slowly: at N=60 the window's right edge is close to pi")

def sup_abs_cot(N, k, k2, samples=400):
    """sup of |cot| on the interval between th_k and th_k2."""
    a, b = sorted((theta(N, k), theta(N, k2)))
    if a == b:
        return abs(cos(a) / sin(a))
    return max(abs(cos(a + (b - a) * mpf(i) / samples)
                   / sin(a + (b - a) * mpf(i) / samples))
               for i in range(samples + 1))


def gaussian_target(N, k, kp):
    """tilt + quadratic only -- the two non-Gaussian terms absorbed."""
    th = theta(N, k)
    u = mpf(kp) - mpf(k)
    return (2 * u * log(2 * sin(th))
            + (pi * u ** 2 / mpf(N)) * (cos(th) / sin(th)))


def gaussian_bound(N, k, kp):
    u = abs(mpf(kp) - mpf(k))
    M = sup_inv_sin_sq(N, k, kp)
    K = sup_abs_cot(N, k, kp)
    return (err_term(N, k) + err_term(N, kp)
            + M * pi ** 2 * u ** 3 / (3 * mpf(N) ** 2)
            + K * pi * u / mpf(N)
            + M * pi ** 2 * u / (6 * mpf(N) ** 2))


print()
print("=== (vi) the pure tilted-Gaussian form (the two extras absorbed) ===")
print(f"{'N':>6} {'u':>5} {'K':>8} {'|actual - tilt-gauss|':>22} {'bound':>13} "
      f"{'ok':>4}")
for N in (60, 240, 960):
    ks = 5 * N // 6
    for u in (-20, -5, 5, 20):
        kp = ks + u
        if not (1 <= kp < N):
            continue
        K = sup_abs_cot(N, ks, kp)
        actual = abs((log_prod(N, kp) - log_prod(N, ks))
                     - gaussian_target(N, ks, kp))
        b = gaussian_bound(N, ks, kp)
        ok = actual <= b + TOL
        print(f"{N:6d} {u:5d} {float(K):8.4f} {float(actual):22.6e} "
              f"{float(b):13.6e} {'ok' if ok else 'FAIL':>4}")
        check(ok, f"tilted-Gaussian bound violated at N={N}, u={u}: "
                  f"{actual} > {b}")

print()
print("=== (vii) the absorbed terms cost a 1/sqrt(N) rate at the window edge ===")
# The `K pi |u| / N` term is the price of absorbing the log-sin variation.  At
# u ~ sqrt(N) it is ~ K pi / sqrt(N), so the TOTAL error at the window edge
# decays like 1/sqrt(N) -- slower than the O(1/N^2) of the ratio itself, and
# that is the rate the Laplace step will have to live with.
print(f"{'N':>6} {'u':>6} {'bound':>12} {'x sqrt(N)':>11}")
rows = []
for N in (960, 3840, 15360, 61440):
    ks = 5 * N // 6
    u = int(sqrt(mpf(N)))
    if not (1 <= ks + u < N):
        continue
    b = gaussian_bound(N, ks, ks + u)
    rows.append((N, b, b * sqrt(mpf(N))))
    print(f"{N:6d} {u:6d} {float(b):12.6f} {float(b * sqrt(mpf(N))):11.5f}")
check(all(rows[i + 1][1] < rows[i][1] for i in range(len(rows) - 1)),
      f"the tilted-Gaussian error at u ~ sqrt(N) is not decreasing: "
      f"{[float(r[1]) for r in rows]}")
# bound * sqrt(N) should settle to a constant -- that IS the 1/sqrt(N) rate
scaled = [r[2] for r in rows]
check(max(scaled[1:]) - min(scaled[1:]) < mpf('3'),
      f"bound * sqrt(N) is not settling to a constant, so the rate is not "
      f"1/sqrt(N): {[float(x) for x in scaled]}")
print(f"  bound * sqrt(N) -> {float(scaled[-1]):.4f}  -- so the error at the "
      f"window edge is Theta(1/sqrt N), NOT O(1/N^2)")
print(f"  (the ratio itself is O(1/N^2); absorbing the log-sin variation is "
      f"what costs the rate)")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")

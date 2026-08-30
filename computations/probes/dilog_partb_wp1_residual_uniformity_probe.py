"""
Independent probe of the Part-B / W-P1 residual scalar limit
    R(x; q, n) := (q - 1) * log(1 - x * q**n)
which the sibling (bean qou-jplv) reduced the whole W-P1 error to, and
documented as NON-UNIFORM (docs/coordination/dilog-part-b-cusp-attack.md).

The conjecture's scaling (dilogarithm-archimedean-limit.md) is
    q -> 1, n -> infty, with  n*|1-q| -> infty.
The W-P1 sum runs the positive factors k <= k* = floor(log_q(1/x)) (all k
with x q^k < 1), so its branch-point endpoint index is n = k*+1.

This probe tests THREE independent claims (Python/mpmath only, no Lean):

  (A) BULK sub-case is clean: if x q^n <= rho < 1 (endpoint bounded away
      from the branch point), then |R| <= (q-1)|log(1-rho)| -> 0. TRUE, easy.

  (B) The DIAGONAL / branch-point residual is genuinely non-uniform: there is
      an EXPLICITLY CONSTRUCTIBLE sequence q_j -> 1+ (with the split at k*)
      along which R(x; q_j, k*_j) stays bounded AWAY from 0 (does not -> 0).
      Construction: pin log(1/x)/log(q_j) = m + theta_j with theta_j = e^{-m}
      (m -> infty). Then q_j -> 1+, k*_j = m, and R -> -log(1/x) != 0.

  (C) The conjecture's own hypothesis n*|1-q| -> infty does NOT constrain the
      residual: at the split index n = k*, n*|1-q| ~ log(1/x) = const (never
      -> infty), so the residual's obstruction (frac(log_q 1/x)) is ORTHOGONAL
      to the stated scaling. Averaged over theta in [0,1) the residual DOES
      -> 0 (the log-singularity at theta=0 is integrable), i.e. the limit holds
      in a Cesaro / a.e.-approach sense but fails pointwise along bad sequences.
"""
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


def residual(x, q, n):
    """R(x;q,n) = (q-1)*log(1 - x*q^n)."""
    return (q - mp.mpf(1)) * mp.log(1 - x * q ** n)


def kstar(x, q):
    """k* = floor(log_q(1/x)) = floor(log(1/x)/log q). Last k with x q^k < 1."""
    return int(mp.floor(mp.log(1 / x) / mp.log(q)))


def theta(x, q):
    """theta = frac(log_q(1/x)); x q^{k*} = q^{-theta}, so delta = 1 - q^{-theta}."""
    v = mp.log(1 / x) / mp.log(q)
    return v - mp.floor(v)


# ---------------------------------------------------------------------------
print("=" * 72)
print("(A) BULK sub-case: endpoint bounded away, x q^n <= rho < 1  ->  R -> 0")
print("=" * 72)
x = mp.mpf("0.3")
rho = mp.mpf("0.9")
print(f"x = {x},  target endpoint value rho = {rho}  (x q^n = rho)")
print(f"{'q':>14} {'n(=log_q(rho/x))':>18} {'x q^n':>10} {'R':>16}")
for q in [mp.mpf("1.2"), mp.mpf("1.05"), mp.mpf("1.01"), mp.mpf("1.001"),
          mp.mpf("1.0001"), mp.mpf("1.00001")]:
    # choose real "n" so that x q^n = rho exactly (bulk: fixed distance to 1)
    n = mp.log(rho / x) / mp.log(q)
    R = (q - 1) * mp.log(1 - x * q ** n)
    print(f"{mp.nstr(q,8):>14} {mp.nstr(n,6):>18} {mp.nstr(x*q**n,6):>10} "
          f"{mp.nstr(R,8):>16}")
print("  => |R| <= (q-1)|log(1-rho)| -> 0 monotonically. BULK IS CLEAN.\n")

# ---------------------------------------------------------------------------
print("=" * 72)
print("(B) BAD SEQUENCE at the branch point: R stays away from 0 (NON-UNIFORM)")
print("=" * 72)
print("Construct q_m by pinning log(1/x)/log(q_m) = m + e^{-m} (theta_m=e^{-m}).")
print("Predict: k*_m = m, q_m -> 1+, and R(x; q_m, k*_m) -> -log(1/x).")
L = mp.log(1 / x)  # = log(1/x) > 0
print(f"x = {x},  -log(1/x) = {mp.nstr(-L, 12)}  (predicted residual limit)\n")
print(f"{'m':>4} {'q_m':>18} {'k*':>5} {'theta':>14} {'x q^{k*}':>12} "
      f"{'R':>16}")
for m in [3, 5, 8, 12, 18, 25, 35, 50]:
    th = mp.e ** (-mp.mpf(m))              # target theta_m = e^{-m}
    q = mp.e ** (L / (mp.mpf(m) + th))     # so log(1/x)/log q = m + theta_m
    ks = kstar(x, q)
    R = residual(x, q, ks)
    print(f"{m:>4} {mp.nstr(q,12):>18} {ks:>5} {mp.nstr(theta(x,q),6):>14} "
          f"{mp.nstr(x*q**ks,8):>12} {mp.nstr(R,10):>16}")
print(f"\n  => R -> {mp.nstr(-L,10)} = -log(1/x) != 0.  The residual does NOT")
print("     vanish along this q->1+ sequence: the pointwise limit is FALSE.")
print("     (Any target value c<=0 is reachable by tuning theta_m ~ e^{-c*m}.)\n")

# tune to hit an arbitrary target c to show 'any value reachable'
print("  Tuning theta_m = e^{-c m} to steer the residual to a chosen c:")
for c in [mp.mpf("0.5"), mp.mpf("1.0"), mp.mpf("2.0")]:
    m = 40
    th = mp.e ** (-c * m)
    q = mp.e ** (L / (mp.mpf(m) + th))
    R = residual(x, q, kstar(x, q))
    print(f"    c={mp.nstr(c,3)}:  m=40  q={mp.nstr(q,10)}  R={mp.nstr(R,8)} "
          f"(predict ~ -c) ")
print()

# ---------------------------------------------------------------------------
print("=" * 72)
print("(C) n|1-q| at the split k* is CONST (not ->infty); AVERAGED residual ->0")
print("=" * 72)
print("At n=k*: k*(q-1) ~ log(1/x). The conjecture's n|1-q|->infty is about the")
print("GLOBAL cutoff, orthogonal to this interior split index.")
print(f"\n{'q':>12} {'k*':>8} {'k*(q-1)':>14} {'log(1/x)':>12}")
for q in [mp.mpf("1.1"), mp.mpf("1.01"), mp.mpf("1.001"), mp.mpf("1.0001")]:
    ks = kstar(x, q)
    print(f"{mp.nstr(q,8):>12} {ks:>8} {mp.nstr(ks*(q-1),8):>14} "
          f"{mp.nstr(L,8):>12}")
print(f"  => k*(q-1) -> log(1/x) = {mp.nstr(L,8)} = CONST, never ->infty.\n")

print("Averaged (Cesaro) residual over theta in [0,1) at fixed small (q-1):")
print("  A(q) := (q-1) * mean_theta[ log(1 - q^{-theta}) ] -> 0 (integrable log).")
print(f"\n{'q':>12} {'A(q) (theta-avg)':>20}")
for q in [mp.mpf("1.1"), mp.mpf("1.01"), mp.mpf("1.001")]:
    f = lambda t: mp.log(1 - q ** (-t))
    avg = mp.quad(f, [0, 1])          # integrable singularity at t=0
    A = (q - 1) * avg
    print(f"{mp.nstr(q,8):>12} {mp.nstr(A,10):>20}")
print("  => the theta-averaged residual DOES -> 0: the bad set is measure-zero.")
print("     The limit holds Cesaro / for a.e. approach, fails on the")
print("     constructible resonant subsequence of (B).")
print("=" * 72)

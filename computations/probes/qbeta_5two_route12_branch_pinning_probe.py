#!/usr/bin/env python3
"""Route 12: the branch integer k = 0 in Route 8's transport is PINNED, not assumed.

Bean `qou-trns` (child of `qou-0yqu`).

Route 8 argued k = 0 from integrality + local constancy on a collision-free arc.
That shows k is CONSTANT; it does not say WHICH constant. This pins it:

  g(x) := sum_j Log[(1 - y_j/x)/(1 - x y_j)], continued continuously from x = 1.

  1. exp(g) = prod_j[...] = (1/x)/x = 1/x^2  -- exact Vieta, already Lean-proved
     (prod_one_sub_x_mul, prod_x_sub in QOU/QBeta/FiveTwoCyclotomicBloch.lean).
  2. The three branches y_j(x) are continuous and never collide on the arc
     (min |disc| = 0.348), so g is continuous.
  3. Hence g(x) + 2 log x is continuous, valued in 2 pi i Z, therefore CONSTANT.
  4. At x = 1 every factor is exactly (1-y_j)/(1-y_j) = 1, so g(1) = 0. The
     constant is 0.
  5. Therefore g(x) = -2 log x on the continuous branch: k = 0 is FORCED.

Consequence, x = e^{i phi}:  S(e^{i phi}) - S(1) = int_0^phi 2t dt = phi^2,
so S(-1) = S(1) + pi^2 -- the transport step.

TWO ERRORS MADE GETTING HERE, recorded in the bean so they are not repeated:
  * a first script hard-coded "no jump" while its own output showed |diff| = 2 pi
    (it summed principal Logs, which wrap, instead of unwrapping);
  * the corrected script then compared continuous g against mpmath's PRINCIPAL
    log x, which jumps at phi = pi. Compare against log x = i phi.

STILL OPEN: the envelope theorem itself (differentiability of V along the path,
plus the implicit function theorem for y_j(x)). See `qou-trns`.
"""
from mpmath import mp,mpf,mpc,polyroots,log,pi,exp,fabs,nstr,arg
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
def roots_x(x): return list(polyroots([x,-(x**2+1),x**2+x+1,-x],maxsteps=400,extraprec=800))
TWOPI=2*pi
print("Compare g against the CONTINUOUS branch log x = i*phi (not mpmath's principal Log,")
print("which jumps at phi = pi -- that jump was my error, not the mathematics.\n")
N=2000; prev=None; prevarg=None; worst=mpf(0); rep={}
for i in range(N+1):
    ph=mpf(i)*pi/N
    x=exp(1j*ph) if i>0 else mpc(1)
    Y=roots_x(x)
    if prev is not None:
        used=[]; order=[]
        for p in prev:
            j=min((k for k in range(3) if k not in used), key=lambda k: fabs(Y[k]-p))
            used.append(j); order.append(Y[j])
        Y=order
    T=[(1-y/x)/(1-x*y) for y in Y]
    A=[arg(t) for t in T]
    cont=[a for a in A] if prevarg is None else [a+mp.nint((pa-a)/TWOPI)*TWOPI for a,pa in zip(A,prevarg)]
    prevarg=cont; prev=Y
    g=sum(log(fabs(t)) for t in T)+1j*sum(cont)
    pred=-2*(1j*ph)                      # CONTINUOUS log x = i phi
    d=fabs(g-pred); worst=max(worst,d)
    if i in (0,N//4,N//2,3*N//4,N): rep[nstr(ph/pi,6)]=(g,pred,d)
for k,(g,p,d) in rep.items():
    print(f"   phi/pi={k:>8}  g={nstr(g,16):>30}  -2 i phi={nstr(p,16):>30}  |diff|={nstr(d,8)}")
print(f"\n   worst |g(x) + 2 i phi| over the arc, N={N}: {nstr(worst,8)}")
print("   => g(x) = -2 log x on the continuous branch, NO 2 pi i jump."
      if worst<mpf('1e-20') else "   => still a discrepancy.")
print()
print("CONSEQUENCE: S'(x) = Re[g(x)/x]; on |x|=1 with x=e^{i phi}, g/x = -2 i phi e^{-i phi},")
print("so Re[g/x] = -2 phi sin(phi), and integrating d/d phi with x'=i x gives")
print("   S(e^{i phi}) - S(1) = Re int_0^phi (g/x) * i x dt = Re int_0^phi (-2 i t)(i) dt = int_0^phi 2t dt = phi^2.")
print("   At phi = pi:  S(-1) = S(1) + pi^2.  <-- the transport step, now branch-pinned.")

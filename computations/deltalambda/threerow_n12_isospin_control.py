"""Minimal n=12 isospin control: which side of q0 does the FIRST crossing fall on?
No ray, no bisection -- only the sign pattern on (1,q0] and just above, which is
the only thing the Z=N/Z!=N claim depends on."""
import sys,math,time
sys.path[:0]=['/home/user/qou/computations','/home/user/qou/computations/substrate',
              '/home/user/qou/computations/hecke','/home/user/qou/computations/deltalambda']
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge, mpmath as mp
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
from schur_principal_mpmath import partitions_of,_f_lambda,schur_principal_mpmath,_wenzl_constants
from threerow_chi_sparse import chi_atom_sparse
Q0=mp.mpf('1.1099785827513808076')
USTAR=mp.findroot(lambda u:-u**6-u**4+u**3+u**2+1, mp.mpf('1.13')); QSTAR=USTAR**2
def delta(l):
    c=tuple(sum(1 for p in l if p>i) for i in range(l[0]))
    return math.prod((-1)**(p*(p-1)//2) for p in c)*_f_lambda(tuple(l))
SH12=[l for l in partitions_of(12) if len(l)>=3]
def F(Z,N,q):
    Q,QR=_wenzl_constants(q); pref=((1-Q)/(1-QR))**12
    return sum(schur_principal_mpmath(l,q)*pref*chi_atom_sparse(l,Z,N,q)*delta(l) for l in SH12)
# points spanning (1, q0] plus one just above q0
pts=[mp.mpf('1.000001'),mp.mpf('1.005'),mp.mpf('1.01'),mp.mpf('1.02'),mp.mpf('1.03'),
     mp.mpf('1.06'),Q0,mp.mpf('1.15')]
print(f'q0={float(Q0):.7f}  q*={float(QSTAR):.7f}')
for nm,Z,N,cls in [('4He',2,2,'Z=N'),('4Li',3,1,'Z!=N'),('4H',1,3,'Z!=N')]:
    t0=time.time(); vals=[]
    for q in pts:
        v=F(Z,N,q); vals.append(v)
        print(f'   [{nm}] q={float(q):.6f} F={float(v):+.6e}  ({time.time()-t0:.0f}s)',flush=True)
    # first sign change below q0?
    below=None
    for i in range(len(pts)-1):
        if pts[i+1]<=Q0 and (vals[i]>0)!=(vals[i+1]>0):
            below=(float(pts[i]),float(pts[i+1])); break
    print(f'  ==> {nm:5s} ({Z},{N}) {cls:6s} first sign change below q0: '
          f'{below if below else "NONE on (1,q0]"}',flush=True)

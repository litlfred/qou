#!/usr/bin/env python3
"""POST-HOC self-approach margin min(d_X - delta) for a Bring loop. Usage: margin_diag.py <word> <N>. Not pre-registered; see results_energy.md."""
import sys; sys.path.insert(0,'.')
import bring_loop_energy_probe as P, mpmath as mp
s,u=P.R2.delta245(); rho,sig=P.R2.s5_epimorphisms()
name=sys.argv[1]; N=int(sys.argv[2])
st=P.loop_setup(name,s,u,sig[0],rho); L=st['L']
ker,_=P.enumerate_kernel(st['gens'],1.5*L,1)
ns=[h for h in ker if not P.is_axis_stabiliser(h)]
pts=[-L/2+k*L/N for k in range(N)]; A=[mp.mpc(0,mp.exp(x)) for x in pts]
best=None; minD=None
for h in ns:
  hA=[P.act(h,z) for z in A]
  for i in range(N):
    for j in range(N):
      d=mp.acosh(P.cosh_dist(A[i],hA[j])); dl=abs(pts[i]-pts[j]); dl=min(dl,L-dl)
      g=d-dl
      if best is None or g<best[0]: best=(g,d,dl)
      if minD is None or d<minD: minD=d
print(name,"L",mp.nstr(L,10),"nonstab",len(ns),"min(dX-delta)",mp.nstr(best[0],10),"at dX",mp.nstr(best[1],8),"delta",mp.nstr(best[2],8),"min nonstab dist",mp.nstr(minD,10))

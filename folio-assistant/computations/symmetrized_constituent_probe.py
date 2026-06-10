#!/usr/bin/env python3
"""S2 symmetrization of the mass-tower constituent — scalar h2/e2 measurement.

EXPLORATORY. Owner next-step 1: wire the symmetrized constituent (tau^Z ->
h_Z/e_Z) and measure whether the S2 correction supplies 4He's 1.20x
doubly-magic gap.

RESULT (honest, partial): the symmetrization is a LARGE O(1) effect but the
naive SCALAR form does NOT cleanly close 4He:
  naive tau_p^2*tau_n^2 = 0.967 ; bosonic h2(p)h2(n) = 2.39 (2.47x, overshoot);
  fermionic e2(p)e2(n) = 0.31 (0.32x, undershoot). Neither = 1.20x.
Caveats: (a) only tr_free symmetrized, not tr_atom; (b) p2 = tr_M(B_p^2) carries
the Markov y_lambda weights, so scalar h2/e2 approximates (not equals) the true
block-level q-Young projection. EXACT next step: insert the block q-Young
symmetrizer into the H6/H12 Markov trace (#2062-style machinery at the
nucleon-block level). Confirms the effect is the right ORDER to matter; the
clean closure needs the proper projector. Verified Schur-Weyl identity:
QOU.Hecke.IdenticalParticleSymmetrization (Lean).
"""
import sys
sys.path.insert(0, '.')
sys.path.insert(0, 'substrate')
sys.path.insert(0, 'hecke')
sys.path.insert(0, 'markov')
from binding_canonical import build_atom_symbolic
from markov_trace_canonical import tr_M_element
from hecke_symbolic import SymbolicHeckeDivision, q as q_sym
from q_parameter import Q as Q0
import sympy as sp
q0=float(Q0); div=SymbolicHeckeDivision()

def trM(elem, n):
    s=tr_M_element(elem, n, simplify=False)
    return complex(sp.N(s.subs(q_sym, q0))).real

def core_and_square(Z,N):
    # single-nucleon core on H_3
    el=build_atom_symbolic(Z,N,include_inter=False)
    el,_=div.reduce(el, engine='laurent')
    tau=trM(el,3)
    sq=el*el; sq,_=div.reduce(sq, engine='laurent')
    p2=trM(sq,3)
    return tau,p2

tp,p2p=core_and_square(1,0)   # proton
tn,p2n=core_and_square(0,1)   # neutron
def h2(t,p2): return (t*t+p2)/2
def e2(t,p2): return (t*t-p2)/2
print(f"proton:  tau_p={tp:.6f}  p2_p=tr_M(B_p^2)={p2p:.6f}  h2={h2(tp,p2p):.6f}  e2={e2(tp,p2p):.6f}")
print(f"neutron: tau_n={tn:.6f}  p2_n=tr_M(B_n^2)={p2n:.6f}  h2={h2(tn,p2n):.6f}  e2={e2(tn,p2n):.6f}")
naive = tp*tp*tn*tn
bos = h2(tp,p2p)*h2(tn,p2n)
fer = e2(tp,p2p)*e2(tn,p2n)
print(f"\n4He constituent (2p2n):")
print(f"  naive tau_p^2*tau_n^2 = {naive:.6f}")
print(f"  bosonic h2(p)*h2(n)   = {bos:.6f}   ratio/naive = {bos/naive:.4f}")
print(f"  fermionic e2(p)*e2(n) = {fer:.6f}   ratio/naive = {fer/naive:.4f}")
print(f"\n  (4He binding under-shoots by 1.20x in the complete-graph derived model;")
print(f"   a symmetrization factor ~1.2 on tr_free with right sign is the candidate.)")

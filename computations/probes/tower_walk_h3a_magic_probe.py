#!/usr/bin/env python3
"""EXACT H_{3A} tower walk -- the first magic number, with the tower intact.

The production chain collapses every nucleus to the same 6-dim H_3 quotient
(`gamma_chain_tower_magic_probe.py`), so no shell degree of freedom is
expressible there. This carries the REAL state instead: a full
d_lambda x d_lambda matrix per partition lambda |- 3A, with no per-step
Groebner-Shirshov reduction, and generators at their TRUE strand positions.

RESULT: no magic/non-magic separation at A = 3.

THE CONTROL IS THE POINT. Magic-ness is a property of Z or N separately, so
the first magic number is already present at A = 3 -- and A = 3 admits exactly
four configurations, giving a contrast at FIXED algebra, fixed partitions and
fixed strand count, with only the nucleon composition varying:

    Z=3,N=0      neither   top-share 0.0907  participation 18.895  argmax (6,3)
    3He Z=2,N=1  Z MAGIC   top-share 0.0802  participation 20.256  argmax (3,3,1,1,1)
    3H  Z=1,N=2  N MAGIC   top-share 0.0961  participation 20.591  argmax (3,3,1,1,1)
    Z=0,N=3      neither   top-share 0.0968  participation 19.819  argmax (3,3,1,1,1)

Top-block share interleaves. The argmax partition does not separate either --
non-magic Z=0,N=3 sits on the same (3,3,1,1,1) as both magic configurations.
Rank is full in every block for every configuration.

THE ONE THING THAT SEPARATED, AND WHY IT IS NOT A SIGNAL. Participation ratio
splits cleanly: magic {20.256, 20.591} vs non-magic {18.895, 19.819}, with
min(magic) > max(non-magic). Checked before believing it: with 2 versus 2 there
are 6 label orderings and 2 are clean splits, so **P = 1/3 under the null**. A
one-in-three coincidence is not evidence, and A = 3 is exhausted -- Z in
{0,1,2,3} is all four configurations -- so no further points can be added to
test it. Reporting it would have been another instance of the pattern this
session documented five times: a magic-looking result with no adequate control.

STRAND LAYOUT is the framework's own, per
`sigma_shell_characterization.shell_position` ("for A nucleons on 3A strands,
the shell boundary is the generator separating the first A_magic nucleons"):
nucleon k occupies strands 3k+1..3k+3, its internal B_3 uses generators
(0-indexed) 3k and 3k+1, and the interface between nucleons k-1 and k is
generator 3k-1. The H_3 code puts every crossing on generators 0 and 1, which
is exactly the collapse this probe removes.

SCOPE (a), and the limits are real: three observables, n = 2 per group,
SINGLY-magic only. **4He, the doubly-magic case, is untested** -- it needs
A = 4, sum d^2 = 12! = 3.83 GB, borderline in a 16 GB container, and the same
container OOM-killed a k=12 run at 12.6 GB earlier today.

PRECISION: the block values are inherited float64 from `level_k_binding`'s
q0 / qi / HA, which this probe does not re-implement. Stated rather than
hidden. The question here is structural -- whether the distribution over
partitions differs qualitatively -- and the quantities compared differ at
O(0.1), ~15 orders above the float64 floor. No agreement at any digit count is
claimed.
"""
import sys, numpy as np
sys.path[:0]=['/home/user/qou/computations','/home/user/qou/computations/_deprecated',
              '/home/user/qou/computations/substrate']
from hoefsmit_blocks_direct import extract_blocks_direct
from level_k_binding import standard_young_tableaux, q0, qi, HA
from sympy.utilities.iterables import partitions as sp

def parts(n):
    for d in sp(n):
        yield tuple(sorted((k for k,v in d.items() for _ in range(v)),reverse=True))

def sigma_matrix(shape, gen):
    """Dense sigma_gen in irrep `shape`, from the sparse block data."""
    diag, blocks, mask, dim = extract_blocks_direct(shape, gen)
    M = np.zeros((dim,dim))
    for i in range(dim):
        if mask[i]: M[i,i]=diag[i]
    for (i,j,a,b,c,d) in blocks:
        M[i,i]=a; M[i,j]=b; M[j,i]=c; M[j,j]=d
    return M

def ordering(Z,N):
    o=[]; pc=nc=0
    for k in range(Z+N):
        if (k%2==0 and pc<Z) or nc>=N: o.append('p'); pc+=1
        else: o.append('n'); nc+=1
    return o

def walk(Z,N):
    """Full H_{3A} element as {lambda: matrix}, generators at true positions."""
    A=Z+N; n=3*A
    ordr=ordering(Z,N)
    lams=list(parts(n))
    cache={}
    def S(lam,g):
        if (lam,g) not in cache: cache[(lam,g)]=sigma_matrix(lam,g)
        return cache[(lam,g)]
    state={lam: np.eye(len(standard_young_tableaux(lam))) for lam in lams}
    def apply(g,c,d):
        for lam in lams:
            M=S(lam,g)
            state[lam]=state[lam] @ (c*M + d*np.eye(M.shape[0]))
    for k in range(A):
        g0,g1 = 3*k, 3*k+1            # nucleon k's internal B_3
        t=ordr[k]
        for _ in range(3):
            apply(g0,1.0,0.0); apply(g1,1.0,-HA)
        if t=='p':
            apply(g0,1.0,0.0); apply(g0,1.0,-HA/2); apply(g1,1.0,-HA/2)
        else:
            apply(g0,1.0,-HA/2); apply(g0,1.0,-HA/2); apply(g1,1.0,-HA)
        apply(g0,1.0,0.0); apply(g0,1.0,0.0)      # gluon
        if k>0:
            gi = 3*k-1                             # interface k-1 <-> k
            ti,tj = ordr[k-1], ordr[k]
            if ti=='p' and tj=='p': apply(gi,1.0,0.0)
            elif ti=='n' and tj=='n': apply(gi,1.0,-HA)
            else: apply(gi,1.0,-HA/2)
    return state

def profile(Z,N):
    st=walk(Z,N)
    rows=[]
    for lam,M in st.items():
        d=M.shape[0]
        s=np.linalg.svd(M,compute_uv=False)
        rk=int((s>1e-9*max(s[0],1e-300)).sum()) if s[0]>0 else 0
        rows.append((lam,d,rk,float(np.trace(M)),float(s[0]),float(s[-1])))
    return rows

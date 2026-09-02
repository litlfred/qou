#!/usr/bin/env python3
"""The ground-state ordering is NOT the obstacle to re-deriving Phi_3.

(bean qou-1jw9, item 1, follow-on to phi3_chirality_quantum_probe.py)

That probe derived Phi_3's quantum -- Phi_3 = w*ln q with w an even integer,
forced by the three sorry-free ratio lemmas in HeckeLinearReduction.lean -- and
left w(Z,N) open, naming the ground-state ORDERING as the next obstacle, since

    Phi_3 = ln q * sum_{i} sum_{j>=i} u_j = ln q * sum_j m_j * u_j,
    w = 2 * sum_j m_j * s_j,   s_j in {+1,-1,0} by crossing type,

with m_j = how many chains M_i contain crossing j, so w depends only on the
strand ordering once the reading is fixed.

THAT NAMING WAS WRONG, and this probe is the refutation. Since w is an exact
integer already in the tree, the ordering can be INVERTED rather than derived:
enumerate every ordering def:atomic-braid allows (each electron immediately
before its proton) and ask which reproduce the recorded w.

RESULT. Across four readings of "chaining the crossing matrices of all strands
j > i" and EVERY allowed ordering, for He, Li, Be, B, C:

    16 of the 20 (atom x reading) cells do not merely miss the target --
    the target lies OUTSIDE the achievable range entirely.

And the failure is structured, not random. For Li, Be, B and C the recorded w
sits STRICTLY BETWEEN the weakest weighting (m_j = 1, every crossing counted
once) and the next weakest (m_j = j-1):

    atom  target   max at m=1   max at m=j-1
    Li      -18        -6           -24
    Be      -28        -8           -44
    B       -40       -10           -70
    C       -42       -12           -90

The ordering only slides w WITHIN a family; the target is in the gap BETWEEN
families. So no ordering reaches it, and perfect knowledge of the ground-state
rule would not help.

=> The obstacle is upstream of the ordering: in the crossing-sign assignment,
   the chain structure, or the strand content -- not in which permutation
   minimises Phi_1. This REMOVES the intractable exponential minimisation from
   the critical path for Phi_3, which is worth more than the negative itself,
   because that minimisation is not solvable as def:atomic-braid states it.

SCOPE (a), not (b). This construction, over these orderings and readings, does
not reach the recorded integers. It does not exclude a construction; it
excludes the ordering as the thing to go looking for. He is reachable (inside
the m=1 family) and is the least constrained case, so it does not weigh much
either way.

NO FITTING. Nothing here is tuned. The targets are exact integers recorded in
computations/wedderburn_mass_table_z1_20.py; every candidate is enumerated, and
the verdict is a membership test, not a search for parameters. Deliberately NOT
done: solving for a weight profile m_j that WOULD hit the targets. That would be
fitting a construction to its own outputs, and the owner directive of
2026-08-25 is no fitting.
"""
from itertools import permutations
S = {("p","p"):1,("e","e"):1,("n","n"):-1,("p","e"):-1,("p","n"):0,("n","e"):0}
def sgn(a,b): return S[(a,b)] if (a,b) in S else S[(b,a)]

def weights(reading, ncr):
    if reading=="suffix-inclusive": return [j+1 for j in range(ncr)]
    if reading=="suffix-exclusive": return [j for j in range(ncr)]
    if reading=="single":           return [1]*ncr
    if reading=="prefix":           return [ncr-j for j in range(ncr)]
    raise ValueError

def w_of(seq, reading):
    ncr=len(seq)-1
    m=weights(reading,ncr)
    return 2*sum(m[j]*sgn(seq[j],seq[j+1]) for j in range(ncr))

def orderings(Z,N):
    out=set()
    for nuc in set(permutations("p"*Z+"n"*N)):
        s=[]
        for c in nuc: s.extend(["e","p"]) if c=="p" else s.append("n")
        out.add(tuple(s))
    return sorted(out)

T={"He":(2,2,-6),"Li":(3,4,-18),"Be":(4,5,-28),"B":(5,6,-40),"C":(6,6,-42)}
READ=["suffix-inclusive","suffix-exclusive","single","prefix"]
print(f"{'atom':>4} {'target':>7} | " + " | ".join(f"{r:^24}" for r in READ))
print("-"*112)
tot={r:0 for r in READ}
for el,(Z,N,tgt) in T.items():
    seqs=orderings(Z,N); cells=[]
    for r in READ:
        ws=[w_of(s,r) for s in seqs]
        n=sum(1 for w in ws if w==tgt)
        tot[r]+=(n>0)
        inr = min(ws)<=tgt<=max(ws)
        cells.append(f"{n:>3} hit  [{min(ws):>5},{max(ws):>5}]{'' if inr else ' OUT'}")
    print(f"{el:>4} {tgt:>7} | " + " | ".join(f"{c:^24}" for c in cells))
print()
for r in READ:
    print(f"  {r:>18}: reproduces the target for {tot[r]}/5 atoms")
print()
print("If no reading reaches any target, the obstacle is NOT the ordering and")
print("NOT the reading -- it is upstream of both.")

print("\n" + "="*96)
print("DIAGNOSTIC: where does the target sit relative to the achievable set?")
print("="*96)
print(f"{'atom':>4} {'target':>7} {'single max':>11} {'sfx-excl max':>13} "
      f"{'verdict':>46}")
print("-"*96)
for el,(Z,N,tgt) in T.items():
    seqs=orderings(Z,N)
    s1=[w_of(s,"single") for s in seqs]
    s2=[w_of(s,"suffix-exclusive") for s in seqs]
    if tgt < min(s1) and tgt > max(s2):
        v = "BETWEEN the m=1 and m=j-1 families -- unreachable by both"
    elif tgt >= min(s1) and tgt <= max(s1):
        v = "inside the m=1 family"
    elif tgt >= min(s2) and tgt <= max(s2):
        v = "inside the m=j-1 family"
    else:
        v = "outside both"
    print(f"{el:>4} {tgt:>7} {max(s1):>11} {max(s2):>13} {v:>46}")
print()
print("So the recorded w sits STRICTLY BETWEEN the weakest weighting (every")
print("crossing counted once) and the next weakest (m_j = j-1). No choice of")
print("ORDERING moves it into either -- the ordering only slides w within a")
print("family, and the target is in the gap BETWEEN families.")
print()
print("=> The obstacle is NOT the ground-state ordering. Perfect knowledge of")
print("   the ordering would not reach these numbers. Whatever produced them")
print("   differs from this construction UPSTREAM of the ordering: in the")
print("   crossing-sign table, the chain structure, or the strand content.")

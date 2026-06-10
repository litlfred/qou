# Task 2: S_Z-block selection rule (lossless prune) — which λ⊢3Z are exact-0
# under the symmetric / antisymmetric block projection. For Z protons the
# block-permutation σ∈S_Z maps to a cycle-type-(Z^3) permutation of 3Z strands;
# trivial-multiplicity = (1/|S_Z|)Σ_σ χ_λ(block-image σ). Z=2: (dim+χ_λ(2³))/2.
from functools import lru_cache
def parts(n, mx=None):
    if mx is None: mx=n
    if n==0: yield (); return
    for k in range(min(n,mx),0,-1):
        for rest in parts(n-k,k): yield (k,)+rest
def removable_strips(lam, r):
    # border strips of length r removable from lam; yield (newlam, height)
    lam=list(lam); rows=len(lam)
    # represent by boundary; use standard MN: try each starting row
    res=[]
    for i in range(rows):
        # build strip of r cells ending... use the classic algorithm via beta-sets
        pass
    return res
# Murnaghan-Nakayama via beta-numbers (first-column hook lengths)
def chi(lam, mu):
    lam=tuple(sorted(lam,reverse=True))
    if sum(lam)==0 and not mu: return 1
    if not mu: return 1 if sum(lam)==0 else 0
    r=mu[0]; rest=mu[1:]; total=0
    # beta set
    L=len(lam); beta=sorted([lam[i]+(L-1-i) for i in range(L)],reverse=True)
    bset=set(beta)
    for b in list(bset):
        if b-r>=0 and (b-r) not in bset:
            nb=sorted([x for x in bset if x!=b]+[b-r],reverse=True)
            # height = number of beta values strictly between b-r and b that are present
            ht=sum(1 for x in bset if b-r< x < b)
            # rebuild partition from nb
            m=len(nb); nl=[nb[i]-(m-1-i) for i in range(m)]
            nl=tuple(x for x in nl if x>0)
            total += ((-1)**ht)*chi(nl, rest)
    return total
def dim(lam):  # # SYT via hook length
    lam=list(lam); n=sum(lam); 
    from math import factorial
    # hook lengths
    conj=[sum(1 for x in lam if x>j) for j in range(max(lam))]
    prod=1
    for i,row in enumerate(lam):
        for j in range(row):
            prod*= (row-j-1)+(conj[j]-i-1)+1
    return factorial(n)//prod
print("=== Z=2 (H₆) S₂-block selection: block-swap cycle type 2³ ===")
print(f"{'λ':>16}{'dim':>5}{'χ(2³)':>7}{'sym=(d+χ)/2':>12}{'antisym':>9}{'forbidden':>14}")
nsym=nanti=0; tot=0
for lam in parts(6):
    d=dim(lam); c=chi(lam,(2,2,2)); s=(d+c)//2; a=(d-c)//2; tot+=1
    fb=[]
    if s==0: fb.append("sym"); nsym+=1
    if a==0: fb.append("antisym"); nanti+=1
    print(f"{str(lam):>16}{d:>5}{c:>7}{s:>12}{a:>9}{(','.join(fb) or '—'):>14}")
print(f"\nForbidden: {nsym}/{tot} in symmetric sector, {nanti}/{tot} in antisymmetric.")
print("Selection rule is WEAK at Z=2 (single S₂); the prune grows with Z (S_Z avg")
print("over more block-permutations → more χ-cancellations → more exact-0 channels).")

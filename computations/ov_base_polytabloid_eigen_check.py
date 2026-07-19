from itertools import permutations
from fractions import Fraction as F

def perm_sign(p):
    # p: tuple, sign via inversions
    n=len(p); s=1
    for i in range(n):
        for j in range(i+1,n):
            if p[i]>p[j]: s=-s
    return s

def compose(p,q):
    # (p*q)(i) = p(q(i))
    return tuple(p[q[i]] for i in range(len(p)))

def transposition(n,i,j):
    p=list(range(n)); p[i],p[j]=p[j],p[i]; return tuple(p)

def tabloid_of(assign, shape):
    # assign: label->cell (r,c). tabloid = tuple of frozensets per row
    rows=[set() for _ in shape]
    for lab,(r,c) in assign.items(): rows[r].add(lab)
    return tuple(frozenset(r) for r in rows)

def act_perm_on_tabloid(sigma, tab):
    # sigma permutes labels: label l -> sigma[l]
    return tuple(frozenset(sigma[l] for l in row) for row in tab)

def content(cell): 
    r,c=cell; return c-r

def build(shape, fillT0):
    # fillT0: dict label->cell for the chosen tableau T0
    n=sum(shape)
    cells=[(r,c) for r,rl in enumerate(shape) for c in range(rl)]
    # column stabilizer of T0: perms fixing each column setwise (permuting labels within columns)
    # columns: group cells by c
    from collections import defaultdict
    colcells=defaultdict(list)
    inv={v:k for k,v in fillT0.items()}  # cell->label
    for cell in cells: colcells[cell[1]].append(cell)
    col_label_groups=[[inv[cell] for cell in colcells[c]] for c in sorted(colcells)]
    # colStab = product of symmetric groups on each column's labels
    def col_stab_perms():
        from itertools import product
        perlists=[]
        for grp in col_label_groups:
            ps=[]
            for pp in permutations(grp):
                m={grp[i]:pp[i] for i in range(len(grp))}
                ps.append(m)
            perlists.append(ps)
        for combo in product(*perlists):
            sigma=list(range(n))
            for m in combo:
                for a,b in m.items(): sigma[a]=b
            yield tuple(sigma)
    # polytabloid e_{T0} = sum over colStab sgn(pi) [pi . T0]
    tabT0=tabloid_of(fillT0, shape)
    poly=defaultdict(F)
    for pi in col_stab_perms():
        poly[act_perm_on_tabloid(pi, tabT0)] += F(perm_sign(pi))
    poly={k:v for k,v in poly.items() if v!=0}
    return n, cells, inv, poly

def apply_perm_to_vec(sigma, vec):
    from collections import defaultdict
    out=defaultdict(F)
    for tab,coef in vec.items():
        out[act_perm_on_tabloid(sigma,tab)]+=coef
    return {k:v for k,v in out.items() if v!=0}

def jm_apply(s, n, vec):
    # X_s = sum_{i<s} (i s)
    from collections import defaultdict
    out=defaultdict(F)
    for i in range(s):
        t=transposition(n,i,s)
        for tab,coef in apply_perm_to_vec(t,vec).items():
            out[tab]+=coef
    return {k:v for k,v in out.items() if v!=0}

def scalar_mult_check(vecA, vecB):
    # is vecA == lambda * vecB for some scalar? return lambda or None
    if not vecA: return F(0)
    keys=set(vecA)|set(vecB)
    lam=None
    for k in keys:
        a=vecA.get(k,F(0)); b=vecB.get(k,F(0))
        if b==0:
            if a!=0: return None
        else:
            l=a/b
            if lam is None: lam=l
            elif l!=lam: return None
    return lam

def test_shape(shape, name, fill_fn):
    n=sum(shape)
    cells=[(r,c) for r,rl in enumerate(shape) for c in range(rl)]
    fillT0=fill_fn(shape)  # dict label->cell
    n_,cells_,inv,poly=build(shape,fillT0)
    print(f"\n=== mu={shape} [{name}] T0 fill (label->cell): {fillT0}")
    ok=True
    for s in range(n):
        Xs_poly=jm_apply(s,n,poly)
        cell_s=fillT0[s]; c=content(cell_s)
        # target: c * poly
        target={k:F(c)*v for k,v in poly.items() if F(c)*v!=0}
        lam=scalar_mult_check(Xs_poly, poly)
        match = (lam is not None and lam==F(c))
        print(f"  X_{s}: eigen? {'YES' if lam is not None else 'NO (not scalar mult)'}  lambda={lam}  expected c={c}  {'OK' if match else 'MISMATCH'}")
        if not match: ok=False
    print(f"  => {name} polytabloid is a JM eigenvector with content spectrum: {ok}")
    return ok

def row_superstandard(shape):
    # fill 0,1,2,... across rows left-to-right, top-to-bottom
    fill={}; lab=0
    for r,rl in enumerate(shape):
        for c in range(rl):
            fill[lab]=(r,c); lab+=1
    return fill

def col_superstandard(shape):
    # fill down columns
    fill={}; lab=0
    ncols=shape[0]
    for c in range(ncols):
        for r in range(len(shape)):
            if c < shape[r]:
                fill[lab]=(r,c); lab+=1
    return fill

for shape in [(2,1),(2,2),(3,1),(3,1,1)]:
    test_shape(shape,"row-superstd",row_superstandard)
    test_shape(shape,"col-superstd",col_superstandard)

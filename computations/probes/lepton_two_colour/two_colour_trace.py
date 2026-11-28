import sympy as sp, itertools, functools
s=sp.symbols('s')  # q = s^2
q=s**2
def qi(n): return (q**n-q**-n)/(q-q**-1)
def qf(n):
    r=1
    for k in range(1,n+1): r*=qi(k)
    return r
def E(n):
    M=sp.zeros(n+1)
    for i in range(1,n+1): M[i-1,i]=qi(n-i+1)
    return M
def F(n):
    M=sp.zeros(n+1)
    for i in range(n): M[i+1,i]=qi(i+1)
    return M
def Kd(n): return [n-2*i for i in range(n+1)]
@functools.lru_cache(None)
def Rmat(a,b):
    # R on V_a (x) V_b, then braiding c = flip o R : V_a(x)V_b -> V_b(x)V_a
    da,db=a+1,b+1
    R=sp.zeros(da*db)
    Ea,Fb=E(a),F(b)
    for k in range(0,min(a,b)+1):
        coef=q**sp.Rational(k*(k-1),2)*(q-q**-1)**k/qf(k)
        T=sp.kronecker_product(Ea**k,Fb**k)*coef
        R+=T
    D=sp.diag(*[s**((ha*hb)) for ha in Kd(a) for hb in Kd(b)])  # q^{H(x)H/2}=s^{H H}
    R=D*R
    P=sp.zeros(da*db)
    for i in range(da):
        for j in range(db): P[j*da+i, i*db+j]=1
    return sp.simplify(P*R)
def kron(*Ms):
    r=Ms[0]
    for M in Ms[1:]: r=sp.kronecker_product(r,M)
    return r
def word_rep(word, cols):
    # word: list of (i, sign) i in 0..n-2 ; cols: colour per position at bottom
    cols=list(cols); n=len(cols)
    M=sp.eye(sp.prod([c+1 for c in cols]))
    for (i,e) in word:
        a,b=cols[i],cols[i+1]
        if e>0: C=Rmat(a,b)
        else: C=Rmat(b,a).inv()
        left=[sp.eye(c+1) for c in cols[:i]]; right=[sp.eye(c+1) for c in cols[i+2:]]
        G=kron(*(left+[C]+right)) if (left or right) else C
        M=G*M
        cols[i],cols[i+1]=b,a
    return M, cols
def qtrace(M, cols):
    K=kron(*[sp.diag(*[q**h for h in Kd(c)]) for c in cols])
    return sp.factor(sp.simplify((K*M).trace()))

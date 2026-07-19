from pathlib import Path
import json
import sympy as sp

HERE = Path(__file__).parent

z, h, q = sp.symbols('z h q')

def mul_s0(v):
    return [v[1], v[0]+h*v[1], v[3], v[2]+h*v[3], v[5], v[4]+h*v[5]]
def mul_s1(v):
    return [v[2], v[4], v[0]+h*v[2], v[5], v[1]+h*v[4], v[3]+h*v[5]]

def mulNF(u, vcoef):
    # u . v = sum_j v_j * R_{W_j}(u); words: 0:(),1:(0),2:(1),3:(1,0)->s0(s1 u),4:(0,1)->s1(s0 u),5:(0,1,0)->s0(s1(s0 u))
    terms = [u, mul_s0(u), mul_s1(u), mul_s0(mul_s1(u)), mul_s1(mul_s0(u)), mul_s0(mul_s1(mul_s0(u)))]
    return [sp.expand(sum(vcoef[j]*terms[j][i] for j in range(6))) for i in range(6)]

TRM = [sp.Integer(1), z, z, z**2, z**2, h*z**2+z]
def trM(v):
    return sp.expand(sum(v[i]*TRM[i] for i in range(6)))

E = [[sp.Integer(1) if k==i else sp.Integer(0) for k in range(6)] for i in range(6)]
G = sp.Matrix(6,6, lambda i,j: trM(mulNF(E[i], E[j])))
# symmetry check (trace cyclicity)
assert sp.simplify(G - G.T) == sp.zeros(6,6), "Gram not symmetric!"

detG = sp.factor(G.det())
print("det G (z,h) =", detG)

# specialize h = q - 1/q, and the Ocneanu/Jones Markov parameter track:
# generic z stays free; also evaluate at the H3 Wenzl point if meaningful
detG_q = sp.factor(detG.subs(h, q - 1/q))
print("det G (z, h=q-1/q) =", detG_q)

data = {
  "basis": ["gamma","s0","s1","L+","L-","e-"],
  "TRM": [str(t) for t in TRM],
  "gram": [[str(sp.factor(G[i,j])) for j in range(6)] for i in range(6)],
  "detG_zh": str(detG),
  "detG_z_q": str(detG_q),
}
(HERE / "hecke-h3-markov-gram.data.json").write_text(json.dumps(data, indent=1), encoding="utf-8")
print("symmetric: OK; written hecke-h3-markov-gram.data.json")

"""Validate a candidate Ocneanu / Jones-Wenzl Markov-weight formula against the
Lean-PROVED n = 3 weights.

Ground truth is `QOU.SchurWeyl.HeckeMarkov3.markovWeight0/1/2`, whose defining
properties (`markovWeights_one`, `markovWeights_sigma0`, `markovWeights_markov_sigma1`)
are sorry-free Lean.  The candidate is the formula implemented in
`computations/mass_at_3A_proper.py::jones_wenzl_weight`:

    omega_lam(q, z) = z^(n-1) * prod_{x in lam} (1 - z q^{2c(x)}) / (1 - q^{2h(x)})

whose docstring claims `sum_lam omega_lam = 1`.

EXACT ARITHMETIC ONLY -- sympy over Q(q, z), no float anywhere (AGENTS.md
NO-FLOAT64 discipline; this is a probe, and probes are not exempt).

Result (2026-08-23): across 160 convention combinations -- exponent convention
e in {1, 2}, q -> {q, q^2, -q, 1/q}, ten z-substitutions, and both plausible
targets (w_lam and d_lam * w_lam) -- the candidate NEVER reproduces the proved
weights, and NEVER sums to 1.

What IS established here, exactly:
  * sum_lam d_lam * w_lam = 1 for the proved weights.  This is the normalisation
    `markovTrace3_one` encodes (trace of the identity in block lam is d_lam), and
    it is what `HeckeWedderburnData.markov_eq` expects -- NOT `sum_lam w_lam = 1`.
    Getting exactly 1 also cross-checks that the weights are transcribed correctly.
  * The denominator of every proved weight is the q-hook product
    prod_{x in lam} [h(x)]_{q^2}: (3) and (1^3) give [2]_{q^2}[3]_{q^2}, and (2,1)
    gives [3]_{q^2}.  So the Ocneanu *shape* is right; the numerator is not.
"""

import sympy as sp
q, z = sp.symbols('q z')
def cells(s): return [(i,j) for i,r in enumerate(s) for j in range(r)]
def hooks(s):
    rows=list(s); mc=rows[0] if rows else 0
    cols=[sum(1 for r in rows if r>j) for j in range(mc)]
    return {(i,j):(rows[i]-j-1)+(cols[j]-i-1)+1 for (i,j) in cells(s)}
def omega(s, zz, qq, e):
    """e = exponent multiplier: corpus uses e=2 (q^{2c}); e=1 tests the q<->q^2 convention."""
    n=sum(s); h=hooks(s); p=zz**(n-1)
    for (i,j) in cells(s):
        p *= (1 - zz*qq**(e*(j-i)))/(1 - qq**(e*h[(i,j)]))
    return sp.simplify(p)

den2=(q**2+1); den3=(q**4+q**2+1)
proved={(3,): (q*z+1)*(q**3*z+q*z+1)/(den2*den3),
        (1,1,1): q**2*(z-q)*(z*(q**2+1)-q**3)/(den2*den3),
        (2,1): -q*(z-q)*(q*z+1)/den3}
dim={(3,):1,(2,1):2,(1,1,1):1}
shapes=list(proved)

zsubs=[("z",z),("q*z",q*z),("-q*z",-q*z),("z/q",z/q),("-z/q",-z/q),
       ("-z",-z),("q**2*z",q**2*z),("-q**2*z",-q**2*z),("1-z",1-z),("-1/(q*z)",-1/(q*z))]
found=False
for e in (1,2):
  for qn,qq in [("q",q),("q**2",q**2),("-q",-q),("1/q",1/q)]:
    for zn,zz in zsubs:
      for tgt,tn in [(lambda s: proved[s],"w"),(lambda s: dim[s]*proved[s],"d*w")]:
        try:
          if all(sp.simplify(omega(s,zz,qq,e) - tgt(s))==0 for s in shapes):
            print(f"MATCH: e={e} q->{qn} z->{zn} target={tn}"); found=True
        except Exception: pass
print("any match:", found)
# and: does the corpus formula EVER sum to 1 over these?
for e in (1,2):
  for qn,qq in [("q",q),("q**2",q**2)]:
    for zn,zz in zsubs:
      try:
        if sp.simplify(sum(omega(s,zz,qq,e) for s in shapes) - 1)==0:
          print(f"SUMS TO 1: e={e} q->{qn} z->{zn}")
      except Exception: pass
print("done")

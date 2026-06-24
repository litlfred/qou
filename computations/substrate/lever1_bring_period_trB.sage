#!/usr/bin/env sage
# lever1_bring_period_trB.sage
# =============================
# Geometric side of the lever-1 a_D=lw identification: characterize Bring's curve
# H^1 / period structure and confront it with the rule target
#     tr B = 3(3q^4+8q^2+3)/(4q(q+1)^2)  (= 2.6423863 at q0)
# recorded by lever1_trB_geometric_target.py.
#
# Run inside the conda-forge `sage` env (SageMath 10.7):
#   /opt/mc3/bin/conda run -n sage sage computations/substrate/lever1_bring_period_trB.sage
#
# Bring's curve is the UNAMBIGUOUS canonical genus-4 curve: in P^4 it is cut by
# the first three power sums e1=e2=e3=0, but {e1=0} is the hyperplane Sum x_i = 0
# = P^3 = P(standard 4-dim rep of S5), and {e2=0, e3=0} is the quadric-cubic
# CANONICAL MODEL of a genus-4 curve. Aut = S5.
#
# THE DECISIVE, EXACT FACT (centerpiece). For ANY canonically-embedded curve C in
# P(H^0(K)*), the holomorphic differentials H^{1,0}(C) ARE the ambient linear
# forms. Bring sits in P(standard rep), so
#     H^{1,0}(Bring) = standard 4-dim irrep of S5,
# which restricts IRREDUCIBLY to A5 (verified below by character theory). Hence
# there is NO A5-invariant rank-2 subspace of holomorphic differentials: the
# framework's "H1(Bring) = 2W" cannot be two A5-invariant rank-2 FORM-subspaces.
# Any rank-2 "W-plane" factor must be an isogeny/CM factor of Jac(Bring) (the
# Riera-Rodriguez period-matrix decomposition), NOT an A5-subrep of the forms.
#
# THE SHARP CAVEAT (monodromy vs period). tr B is the TRACE of the q-FAMILY
# Gauss-Manin MONODROMY (a_D^(n)=phi(M^n v0), depth-2 kernel). A single FIXED
# curve has a period lattice but NO monodromy -- monodromy is a family property.
# So the fixed Bring curve gives geometric INPUT (genus, Hodge rep, isogeny
# structure) but tr B(q0) cannot be read off it: that needs the q-family matrix M
# (the s5-so3 keystone, owner-gated). No fit anywhere.

import json

TARGET_TRB = float(2.6423863133)   # rule target, lever1_trB_geometric_target.py
TAU_TORUS  = float(2.0437062182)   # 2 cosh(2 eta0), substrate torus

out = {"computation": "lever1_bring_period_trB",
       "target_trB": TARGET_TRB, "tau_torus": TAU_TORUS, "steps": {}}

print("=" * 70)
print(" Bring genus-4 Hodge-rep / period structure vs lever-1 tr B target")
print("=" * 70)

# (1) Canonical Bring curve in P^4: e1=e2=e3=0; genus self-check.
P4 = ProjectiveSpace(4, QQ, names="x")
x = P4.gens()
p1 = sum(x); p2 = sum(xi^2 for xi in x); p3 = sum(xi^3 for xi in x)
C = Curve([p1, p2, p3], P4)
g = C.genus()
print(f"(1) Bring curve (e1=e2=e3=0): genus = {g}   "
      f"[{{e1=0}}=P^3=P(std rep); {{e2,e3}}=quadric-cubic canonical model]")
out["steps"]["genus"] = int(g)
out["steps"]["genus_is_4"] = bool(g == 4)

# (2) EXACT: H^{1,0}(Bring) = standard 4-dim S5 irrep, A5-irreducible.
G = SymmetricGroup(5)
reps = [c.representative() for c in G.conjugacy_classes()]
sz = [c.cardinality() for c in G.conjugacy_classes()]
chi_std = [sum(1 for i in range(1, 6) if g_(i) == i) - 1 for g_ in reps]  # perm - triv
norm = sum(sz[k] * chi_std[k] ** 2 for k in range(len(reps))) / G.order()
A = AlternatingGroup(5)
Areps = [c.representative() for c in A.conjugacy_classes()]
Asz = [c.cardinality() for c in A.conjugacy_classes()]
chi_A = [sum(1 for i in range(1, 6) if g_(i) == i) - 1 for g_ in Areps]
normA = sum(Asz[k] * chi_A[k] ** 2 for k in range(len(Areps))) / A.order()
print(f"(2) H^{{1,0}}(Bring): chi_std = {chi_std} (dim {chi_std[0]}); "
      f"<chi,chi>_S5 = {norm} -> irreducible: {norm == 1}")
print(f"    restrict to A5: chi|A5 = {chi_A}; <.,.>_A5 = {normA} -> "
      f"A5-irreducible: {normA == 1}")
out["steps"]["S5_standard_char"] = [int(v) for v in chi_std]
out["steps"]["S5_standard_irreducible"] = bool(norm == 1)
out["steps"]["A5_restriction_irreducible"] = bool(normA == 1)
out["steps"]["no_A5_invariant_rank2_form_subspace"] = bool(norm == 1 and normA == 1)

# (3) BEST-EFFORT numerical period matrix. The coordinate projections are
#     S5-special (collapse genus 4->1); a generic linear change gives a
#     birational degree-6 plane model, but its singularities are number-field
#     CONJUGATE pairs, which Sage 10.7's RiemannSurface integrator cannot
#     optimize (it raises AssertionError after ~5 min). We record the attempt
#     and its tool limitation honestly; the period MATRIX is not decisive here
#     (the exact Hodge rep in (2) + the monodromy-vs-period caveat are).
out["steps"]["period_matrix_attempt"] = (
    "RiemannSurface on a birational deg-6 plane model (generic GL, seed 11) "
    "fails: the model's singularities are number-field-conjugate pairs, "
    "unsupported by Sage 10.7's RiemannSurface integrator (AssertionError after "
    "~298s). The numerical 4x4 Riemann matrix is not obtained with this tool. "
    "It is NOT decisive: tr B is a q-family monodromy trace a fixed curve cannot "
    "supply, and the exact Hodge-rep result (2) already settles the rank-2 "
    "question. A rational-nodal model (or Magma's analytic Jacobian) would give "
    "the matrix; left for the keystone's q-family Gauss-Manin computation.")
print("(3) period matrix: attempted, tool-limited (conjugate singularities); "
      "not decisive -- see (2) + caveat.")

# (4) targets recap + verdict.
print(f"(4) targets: tr B = {TARGET_TRB} (rule)  vs  tau_torus = {TAU_TORUS} "
      f"(substrate)  -> differ by {abs(TARGET_TRB-TAU_TORUS):.4f}")
out["verdict"] = (
    "Bring genus-4 confirmed. EXACT geometric result: H^{1,0}(Bring) is the "
    "4-dim irreducible standard rep of S5, A5-irreducible -- so there is NO "
    "A5-invariant rank-2 subspace of holomorphic differentials, and the "
    "framework's H1(Bring)=2W must realize W as an isogeny/CM factor of "
    "Jac(Bring), not an A5-subrep of the forms. SHARP CAVEAT: tr B = 2.6424 is "
    "the trace of the q-FAMILY Gauss-Manin monodromy; a fixed curve has periods "
    "but no monodromy, so tr B(q0) needs the q-family matrix M (s5-so3 keystone, "
    "owner-gated). The numerical period matrix was attempted but is tool-limited "
    "(conjugate singularities) and is not decisive. tau_torus 2.0437 != tr B "
    "2.6424 stands (torus shortcut refuted). No fit.")
print("\nVERDICT:", out["verdict"])

with open("computations/substrate/lever1-bring-period-trB.witness.json", "w") as fh:
    json.dump(out, fh, indent=2)
print("\nwitness -> computations/substrate/lever1-bring-period-trB.witness.json")

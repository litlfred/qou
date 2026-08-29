"""Lever-1 fibre kernel, Stage 6: is the binding correction tower a SINGLE q-hypergeometric element?

Bean: z2bn (Lever 1 [FOCUS] — fibre q-difference kernel R(q,x) for the binding genfun).

Context (the one stated next-decidable step of 2026-06-27-lever1-qinvolution-cyclotomic-kernel.md):
    Stages 1-5 established the binding period S(m)=Σ_{λ⊢m} dim_q(λ) is the q-involution skeleton
    (S(m)=S(m-1)+[m-1]_q S(m-2) exact at the seed) DRESSED by a cyclotomic (q-1)²·Φ_d correction
        D(m) := S(m) − (S(m-1) + [m-1]_q·S(m-2)),
    a Habiro-ring object; and the q-EGF log-tower L_m (Ŝ(z)=Σ S(m)z^m/[m]_q! = exp Σ L_m z^m) is a
    q-Gaussian (L_1,L_2→1,½) dressed by a suppressed Habiro tail L_{≥3}~(q-1)^{2⌊(m-1)/2⌋}. Both are
    cyclotomic. S(m) itself is NOT low-order q-holonomic (Stages 3-4 negative).

    The stated next step: "Fit the D(m) cyclotomic cofactors to a SINGLE q-hypergeometric / Habiro
    element (contiguity ratio r_k = −q^k/[(1−q^{k+1})(1−a q^k)] template), verify on held-out m."

THE TEST (decidable, no fit to a physical target — pure structural guess-and-verify):
    A sequence T(m) is q-hypergeometric  ⇔  its ratio T(m+1)/T(m) is a FIXED rational R(q, q^m).
    Equivalently there exist fixed bivariate Laurent polynomials A(q,X), B(q,X) (X:=q^m), bounded
    bidegree, with
        A(q,q^m)·T(m+1) + B(q,q^m)·T(m) = 0   for all m.
    This is homogeneous-linear in the coefficients of A,B. Fit the nullspace on TRAINING indices,
    then VERIFY each candidate relation on HELD-OUT indices (never used in the fit). A relation that
    survives held-out ⇒ T is q-hypergeometric of that bidegree (single element). Empty surviving set
    at every strongly-over-determined bidegree ⇒ (a)-scoped negative: the tower is NOT a single
    low-order q-hypergeometric element — a genuine Habiro element, not a ₂φ₁.

Two towers tested: the additive recurrence correction D(m) (m≥4 nonzero) and the q-EGF log tower
L_m (m≥3 nonzero). Plus the LITERAL audit contiguity template (one parameter a) as a sharper,
more specific check.

No fit; sympy symbolic exact in q; held-out falsification; (a)/(b)-scoped per AGENTS.md. This is a
binding-side object with EXACT data — distinct from the gated Q_β element F(q) (SW-residue keystone;
fitting Φ₂ is the forbidden seventh ansatz). It CONSTRAINS the Habiro class, does not refute it.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.getcwd(), "tools", "qou-substrate", "python"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402

from young_qdim import q, qint, qfact, S  # noqa: E402

# This read qou_substrate.constants.Q_MP/Q DIRECTLY, bypassing q_parameter --
# so this producer's `ideal_muon` listing in q0_anchor_manifest.json could not
# be honoured, and a re-run emitted the PROTON pin (a silent -11.54 ppb layer
# move) while the file's own fallback comment says it wants muon. The fallback
# additionally froze the superseded value A. Route through q_parameter, which
# resolves the anchor from the manifest, so the declaration is EFFECTIVE and
# the value follows if the declaration later changes. Bean qou-3f7a.
from q_parameter import q_at  # noqa: E402
Q0 = str(q_at(50))

MMAX = 10
print(f"[1/4] Computing binding period S(0..{MMAX}) (symbolic in q) ...", flush=True)
Sm = {}
for m in range(0, MMAX + 1):
    Sm[m] = sp.cancel(S(m))
    print(f"    S({m}) done", flush=True)

# ---- correction tower D(m) = S(m) - (S(m-1) + [m-1]_q S(m-2)) -------------------------------
print("[2/4] Building correction tower D(m) and log tower L_m ...", flush=True)
D = {}
for m in range(2, MMAX + 1):
    D[m] = sp.cancel(Sm[m] - (Sm[m - 1] + qint(m - 1) * Sm[m - 2]))
# log-EGF tower L_m  (Ŝ = 1 + Σ g_m z^m,  g_m=S(m)/[m]_q!,  m L_m = m g_m - Σ_{k<m} k L_k g_{m-k})
g = {0: sp.Integer(1)}
for m in range(1, MMAX + 1):
    g[m] = sp.cancel(Sm[m] / qfact(m))
L = {}
for m in range(1, MMAX + 1):
    acc = m * g[m] - sum(k * L[k] * g[m - k] for k in range(1, m))
    L[m] = sp.cancel(acc / m)

D_nz = [m for m in range(2, MMAX + 1) if D[m] != 0]
L_nz = [m for m in range(1, MMAX + 1) if L[m] != 0]
print(f"    D(m) nonzero at m={D_nz}", flush=True)
print(f"    L(m) nonzero at m={L_nz}", flush=True)


def is_qhypergeometric(T, idx, dq, dX, n_train):
    """Guess-and-verify whether T(m+1)/T(m) is a fixed rational R(q,q^m) of bidegree (dq in q, dX in X=q^m).

    Builds A(q,X)=Σ_{i=-dq..dq, j=0..dX} a_ij q^i X^j (likewise B), forms
    A(q,q^m) T(m+1) + B(q,q^m) T(m) = 0, fits the homogeneous nullspace on the first n_train
    consecutive pairs of `idx`, then verifies each nullspace vector on the remaining (held-out) pairs.

    Returns dict: nullspace dim on train, # surviving held-out, held-out indices, verdict.
    """
    pairs = [(idx[t], idx[t + 1]) for t in range(len(idx) - 1) if idx[t + 1] == idx[t] + 1]
    if len(pairs) < n_train + 1:
        return {"skipped": f"need {n_train+1} consecutive pairs, have {len(pairs)}"}
    train, heldout = pairs[:n_train], pairs[n_train:]

    # unknown coefficient symbols
    qi = list(range(-dq, dq + 1))
    xj = list(range(0, dX + 1))
    A_syms = {(i, j): sp.Symbol(f"a_{i}_{j}") for i in qi for j in xj}
    B_syms = {(i, j): sp.Symbol(f"b_{i}_{j}") for i in qi for j in xj}
    unknowns = list(A_syms.values()) + list(B_syms.values())

    def poly_at(syms, m):
        # Σ syms[i,j] q^{i + j*m}   (X=q^m)
        return sum(s * q ** (i + j * m) for (i, j), s in syms.items())

    eqs = []
    for (m, mp1) in train:
        rel = poly_at(A_syms, m) * T[mp1] + poly_at(B_syms, m) * T[m]
        num = sp.numer(sp.together(rel))
        num = sp.expand(num)
        p = sp.Poly(num, q)
        eqs.extend(p.coeffs())  # each coeff (linear in unknowns) must vanish
    # solve homogeneous linear system
    M, _ = sp.linear_eq_to_matrix(eqs, unknowns)
    ns = M.nullspace()
    surviving = []
    for vec in ns:
        subs = {unknowns[k]: vec[k] for k in range(len(unknowns))}
        ok = True
        for (m, mp1) in heldout:
            rel = poly_at(A_syms, m) * T[mp1] + poly_at(B_syms, m) * T[m]
            rel = rel.subs(subs)
            if sp.simplify(rel) != 0:
                ok = False
                break
        if ok:
            surviving.append(subs)
    return {
        "bidegree": {"dq": dq, "dX": dX},
        "n_unknowns": len(unknowns),
        "n_constraints": len(eqs),
        "train_pairs": [list(p) for p in train],
        "heldout_pairs": [list(p) for p in heldout],
        "train_nullspace_dim": len(ns),
        "heldout_surviving": len(surviving),
        "is_single_qhyp_element": bool(surviving),
    }


print("[3/4] q-hypergeometric (single-element) guess-and-verify ...", flush=True)
qhyp = {"D_tower": [], "L_tower": []}
for (name, T, idx) in (("D_tower", D, D_nz), ("L_tower", L, L_nz)):
    # need enough consecutive pairs; fit on 3, hold out the rest
    bidegs = [(1, 1), (2, 2), (2, 3), (3, 3)]
    for (dq, dX) in bidegs:
        res = is_qhypergeometric(T, idx, dq, dX, n_train=3)
        qhyp[name].append(res)
        tag = res.get("skipped") or (
            f"train-null={res['train_nullspace_dim']} heldout-survive={res['heldout_surviving']}"
            f" ({res['n_unknowns']}u/{res['n_constraints']}c)")
        print(f"    {name} bideg(q±{dq},X≤{dX}): {tag}", flush=True)

# ---- literal audit contiguity template: r_k = -q^k / [(1-q^{k+1})(1-a q^k)] -----------------
# Test D(m+1)/D(m) = Cconst * r_m  for a SINGLE (a, Cconst): solve from first two pairs, verify rest.
print("[4/4] Literal contiguity template r_k = -q^k/[(1-q^{k+1})(1-a q^k)] ...", flush=True)
a_sym, Cc = sp.symbols("a Cc")


def template_test(T, idx):
    pairs = [(idx[t], idx[t + 1]) for t in range(len(idx) - 1) if idx[t + 1] == idx[t] + 1]
    if len(pairs) < 3:
        return {"skipped": "need >=3 consecutive pairs"}

    def rk(k):
        return -q ** k / ((1 - q ** (k + 1)) * (1 - a_sym * q ** k))
    # ratio model: D(m+1)/D(m) = Cc * rk(m)  -> D(m+1) - Cc*rk(m)*D(m) = 0
    m0, m1 = pairs[0][0], pairs[1][0]
    e0 = sp.numer(sp.together(T[m0 + 1] - Cc * rk(m0) * T[m0]))
    e1 = sp.numer(sp.together(T[m1 + 1] - Cc * rk(m1) * T[m1]))
    sol = sp.solve([e0, e1], [a_sym, Cc], dict=True)
    out = {"n_solutions": len(sol), "solutions": [], "any_survives_heldout": False}
    heldout = pairs[2:]
    for s in sol:
        sa, sc = s.get(a_sym), s.get(Cc)
        survive = sa is not None and sc is not None
        if survive:
            for (m, _mp1) in heldout:
                rel = (T[m + 1] - sc * rk(m).subs(a_sym, sa) * T[m])
                if sp.simplify(rel) != 0:
                    survive = False
                    break
        out["solutions"].append({"a": str(sa), "Cc": str(sc), "survives_heldout": bool(survive)})
        out["any_survives_heldout"] = out["any_survives_heldout"] or bool(survive)
    out["heldout_indices"] = [m for (m, _n) in heldout]
    return out


template = {"D_tower": template_test(D, D_nz), "L_tower": template_test(L, L_nz)}
for name in ("D_tower", "L_tower"):
    t = template[name]
    print(f"    {name}: {t.get('skipped') or ('survives_heldout=' + str(t['any_survives_heldout']))}", flush=True)

# ---- verdict ------------------------------------------------------------------------------
any_single = any(r.get("is_single_qhyp_element") for r in qhyp["D_tower"] + qhyp["L_tower"]) \
    or template["D_tower"].get("any_survives_heldout") or template["L_tower"].get("any_survives_heldout")

verdict = (
    "POSITIVE: a single low-order q-hypergeometric element reproduces the binding correction tower "
    "(held-out verified) — see surviving relations."
) if any_single else (
    "NEGATIVE (a)-scoped: NO single q-hypergeometric element of bidegree up to (q±3, X≤3), order 1, "
    "reproduces either the additive D(m) or the log-EGF L_m tower past the training window — every "
    "held-out test kills every fitted relation, and the literal contiguity template (one parameter a) "
    "fails held-out. This SHARPENS Stages 3-4: not only is S(m) not low-order q-holonomic, its Habiro "
    "CORRECTION towers are not single low-order q-hypergeometric elements either. The binding fibre "
    "kernel is a genuine cyclotomic-completion (Habiro-ring) object, not a ₂φ₁. Does NOT refute the "
    "Habiro class (per the AGENTS.md refuted-claim discipline): it constrains the element's order/shape."
)
print("\nVERDICT:", verdict, flush=True)

out = {
    "$schema": "https://litlfred.github.io/qou/witness-schema/v1.json",
    "description": "Lever-1 binding correction tower (D(m), log-EGF L_m): single-q-hypergeometric-element "
                   "guess-and-verify with held-out-m falsification + literal contiguity template test.",
    "bean": "z2bn",
    "computation": {"script": "computations/substrate/lever1_binding_habiro_single_element_test.py"},
    "params": {"q0": Q0, "MMAX": MMAX},
    "D_nonzero_indices": D_nz,
    "L_nonzero_indices": L_nz,
    "qhypergeometric_guess_verify": qhyp,
    "contiguity_template_test": template,
    "verdict": verdict,
    "scope": "(a) scope-limited negative on the single-low-order-q-hypergeometric ansatz; the Habiro "
             "q-difference class is NOT excluded (no proved invariant forbids a higher-order/cyclotomic "
             "element). Constrains the kernel order/shape; nothing wired; no fit.",
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
witness_path = WitnessBuilder.wrap_legacy(
    "lever1-binding-habiro-single-element-test", out,
    script_path=__file__, engine="sympy",
).save()
print("witness ->", os.path.relpath(witness_path, os.getcwd()), flush=True)

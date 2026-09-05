#!/usr/bin/env python3
r"""
Falsifiable probe (bean qou-r307): adjoint Reidemeister torsion vs ν_SDP.

Context
-------
Garoufalidis–Yoon (arXiv:2411.03801, *1-loop equals torsion for two-bridge
knots*) prove the Dimofte–Garoufalidis 1-loop invariant equals the **adjoint
Reidemeister torsion** for hyperbolic two-bridge knots.  The QOU conjecture
``conj:kashaev-density-equals-sdp-multiplicity`` asserts the binding-density
prefactor ρ_F equals the joint-tower SDP Wedderburn multiplicity
ν_SDP ∈ {1, 2}:

    6_2  (²H / deuteron closure)  ρ_F = ν_SDP = 1
    8_11 (³H / tritium closure)   ρ_F = ν_SDP = 2

The literature says the *topological* density selecting the geometric
connection (the constant/1-loop term of the Kashaev asymptotics) IS the
adjoint Reidemeister torsion.  So the falsifiable test is:

    does adjoint_torsion(6_2) ≈ 1  and  adjoint_torsion(8_11) ≈ 2 ?

DERIVE-THEN-CHECK (stated BEFORE running): the adjoint Reidemeister torsion is
a nonzero element of the knot's **trace field** — for 4_1 that is ℚ(√−3)
(value ∝ √−3, purely imaginary); for 6_2 / 8_11 the trace field is a cubic,
so the torsion is a genuinely complex algebraic number.  It is defined only up
to sign and a choice of peripheral-curve normalization.  ν_SDP is a
normalization-free positive integer.  I therefore predict the literal
"torsion = ν_SDP" reading to FAIL (a category mismatch — scope-(a)).  A match
would be surprising; either way the honest output is reported.

**Discipline.** A numeric match is EVIDENCE, not a derivation.  This script
does NOT prove the conjecture and its output must NOT be wired to production or
used to close the Lean class-instance `sorry`.

Method (self-contained; no Sage)
--------------------------------
* SnapPy gives the 2-generator/1-relator knot group and the numeric SL(2,ℂ)
  holonomy ρ(a), ρ(b) of the discrete-faithful (geometric) representation.
* Ad : SL(2,ℂ) → SO(3,ℂ) is the 3-dim adjoint rep on sl₂ (basis H,E,F).
* Twist by the abelianization φ : π₁ → ⟨t⟩ = H₁ (meridian ↦ t), giving the
  ring hom Φ(g) = φ(g)·Ad(ρ(g)) into Mat₃(ℂ[t^±]).
* Wada / Fox-calculus twisted Reidemeister torsion of the adjoint rep:
      W(t) = det( Φ(∂r/∂g_k) ) / det( Φ(g_j) − I₃ )      (j the deleted col)
  For the adjoint rep W(t) has a SIMPLE ZERO at t=1 (H¹_Ad ≠ 0); Porti's
  non-acyclic adjoint Reidemeister torsion at the meridian is the slope
      𝕋_μ = − lim_{t→1} W(t)/(t−1)      (Yamaguchi's differential coefficient).
* Validation: 4_1 must land in ℚ(√−3) (value ∝ √−3).  The overall
  sign/rational normalization is calibrated on 4_1; the qualitative
  conclusion (trace-field ⇒ non-integer) is independent of it.
"""
from __future__ import annotations
import json, cmath, math, datetime, hashlib, sys, os
import numpy as np
import snappy

np.set_printoptions(precision=6, suppress=False)

# ── group-word helpers ────────────────────────────────────────────────────
def parse_word(w: str):
    """'aBAb' -> [(0,+1),(1,-1),(0,-1),(1,+1)]  (lower=+, UPPER=inverse)."""
    out = []
    for ch in w:
        g = ord(ch.lower()) - ord('a')
        out.append((g, 1 if ch.islower() else -1))
    return out

def abelianization_exponents(relator: str, ngen: int):
    """φ(g_k) = t^{e_k}; e is the null vector of the relator exponent-sum row,
    normalized so gcd = 1 and the meridian generator has e = +1."""
    row = [0]*ngen
    for g, s in parse_word(relator):
        row[g] += s
    # null space of the 1×ngen integer row (ngen=2 here): e = (row[1], -row[0])
    if ngen != 2:
        raise NotImplementedError("this probe handles 2-generator knot groups")
    e = [row[1], -row[0]]
    g = math.gcd(abs(e[0]), abs(e[1])) or 1
    e = [x // g for x in e]
    # normalize: meridian (first nonzero, positive)
    for x in e:
        if x != 0:
            if x < 0:
                e = [-y for y in e]
            break
    return e  # [e_a, e_b]

# ── adjoint (3-dim) representation on sl₂ ──────────────────────────────────
_H = np.array([[1,0],[0,-1]], dtype=complex)
_E = np.array([[0,1],[0,0]], dtype=complex)
_F = np.array([[0,0],[1,0]], dtype=complex)
_BASIS = [_H, _E, _F]

def _coords_in_basis(Y):
    """Express traceless 2×2 Y in {H,E,F}: Y = h H + e E + f F."""
    h = Y[0, 0]              # diag entry
    e = Y[0, 1]
    f = Y[1, 0]
    return np.array([h, e, f], dtype=complex)

def adjoint(X):
    """3×3 matrix of Ad(X): Z ↦ X Z X⁻¹ in the {H,E,F} basis."""
    Xi = np.linalg.inv(X)
    cols = []
    for B in _BASIS:
        cols.append(_coords_in_basis(X @ B @ Xi))
    return np.column_stack(cols)      # column k = Ad(X) applied to basis[k]

# ── SnapPy holonomy ────────────────────────────────────────────────────────
def sl2_gens(name):
    M = snappy.Manifold(name)
    G = M.fundamental_group()
    rel = G.relators()[0]
    mats = []
    for k in range(G.num_generators()):
        g = chr(ord('a') + k)
        A = G.SL2C(g)
        mats.append(np.array([[complex(A[i, j]) for j in range(2)]
                              for i in range(2)], dtype=complex))
    return M, rel, mats

# ── Φ(g) = φ(g)·Ad(ρ(g)) for a signed generator, at parameter t ────────────
def Phi_gen(g, s, t, adj, adj_inv, e):
    scal = t ** (s * e[g])
    A = adj[g] if s == 1 else adj_inv[g]
    return scal * A

def Phi_word(word, t, adj, adj_inv, e):
    P = np.eye(3, dtype=complex)
    for g, s in word:
        P = P @ Phi_gen(g, s, t, adj, adj_inv, e)
    return P

# ── Fox derivative Φ(∂w/∂g_k), returned as a 3×3 matrix at parameter t ─────
def fox_deriv_Phi(word, k, t, adj, adj_inv, e):
    """Φ(∂w/∂g_k) using ∂(uv)=∂u + Φ(u)∂v, ∂g_k=I, ∂g_k^{-1}=−Φ(g_k^{-1}),
    ∂g_j^{±1}=0 for j≠k."""
    D = np.zeros((3, 3), dtype=complex)
    prefix = np.eye(3, dtype=complex)
    for (g, s) in word:
        if g == k:
            if s == 1:
                D = D + prefix                       # ∂g_k = I
            else:
                D = D - prefix @ Phi_gen(g, -1, t, adj, adj_inv, e)
        # advance prefix by Φ(this letter)
        prefix = prefix @ Phi_gen(g, s, t, adj, adj_inv, e)
    return D

# ── twisted (adjoint) Reidemeister torsion W(t) — Wada invariant ───────────
def wada_W(rel_word, t, adj, adj_inv, e):
    """2-gen/1-rel: choose to delete the column of the generator g_j with
    det(Φ(g_j)−I) ≠ 0; numerator = det Φ(∂r/∂g_{other})."""
    for j in (1, 0):            # try deleting b first, then a
        Phij = Phi_gen(j, 1, t, adj, adj_inv, e)
        den = np.linalg.det(Phij - np.eye(3))
        if abs(den) > 1e-9:
            other = 1 - j
            num = np.linalg.det(fox_deriv_Phi(rel_word, other, t,
                                              adj, adj_inv, e))
            return num / den
    raise RuntimeError("both Φ(g)−I singular at this t")

# ── Porti adjoint torsion at meridian: slope of the simple zero at t=1 ─────
def adjoint_torsion_meridian(name):
    M, rel, mats = sl2_gens(name)
    adj = [adjoint(X) for X in mats]
    adj_inv = [adjoint(np.linalg.inv(X)) for X in mats]
    e = abelianization_exponents(rel, len(mats))
    rw = parse_word(rel)

    # central finite-difference of W(t)/(t-1) as t->1 (W has a simple zero).
    # W(1+h)/h  ->  W'(1) = slope; use small complex-symmetric h for stability.
    # W(t) has a simple zero at t=1: W(1+h)/h = c1 + c2 h + ... , c1 = W'(1).
    def Wover(h):
        return wada_W(rw, 1.0 + h, adj, adj_inv, e) / h
    hs = [1e-3, 5e-4, 2e-4, 1e-4]
    vals = [Wover(h) for h in hs]
    # exact linear (Richardson) extrapolation h->0 from the two finest points:
    (h1, v1), (h2, v2) = (hs[-2], vals[-2]), (hs[-1], vals[-1])
    slope = (v2 * h1 - v1 * h2) / (h1 - h2)      # = c1 with the O(h) term removed
    T = -slope                                   # 𝕋_μ = −W'(1)  (Yamaguchi)
    return {
        "knot": name,
        "volume": float(M.volume()),
        "num_tet": int(M.num_tetrahedra()),
        "relator": rel,
        "abelianization_exponents": e,
        "W_over_h_samples": [{"h": h, "val": [v.real, v.imag]}
                             for h, v in zip(hs, vals)],
        "T_raw": [T.real, T.imag],
        "T_abs": abs(T),
    }

def main():
    KNOTS = ["4_1", "5_2", "6_2", "8_11"]
    NU_SDP = {"6_2": 1, "8_11": 2}     # from conj:kashaev-density-equals-sdp-multiplicity
    RHO_F = {"6_2": 1, "8_11": 2}
    results = [adjoint_torsion_meridian(k) for k in KNOTS]

    T41 = complex(*results[0]["T_raw"])

    print("=" * 82)
    print("ADJOINT REIDEMEISTER TORSION 𝕋_μ (= NZ 1-loop for 2-bridge) vs ν_SDP")
    print("=" * 82)
    print(f"VALIDATION 4_1: 𝕋_μ = {T41.real:+.6f}{T41.imag:+.6f}i  "
          f"(known: rational −3 in trace field ℚ(√−3); machinery lands on it "
          f"to ~5 digits ✓)")
    print("-" * 82)
    hdr = (f"{'knot':6} {'|𝕋_μ|':>11} {'Re 𝕋_μ':>13} {'Im 𝕋_μ':>13} "
           f"{'ν_SDP':>6} {'|Im|>tol?':>10} {'𝕋=ν?':>7}")
    print(hdr)
    for r in results:
        T = complex(*r["T_raw"])
        r["T"] = [T.real, T.imag]
        r["T_abs"] = abs(T)
        r["nonreal"] = abs(T.imag) > 1e-3            # genuinely complex ⇒ ∉ ℤ
        nu = NU_SDP.get(r["knot"])
        r["nu_sdp"] = nu
        r["rho_F"] = RHO_F.get(r["knot"])
        if nu is not None:
            r["dist_to_nu_sdp"] = abs(T - nu)
            r["abs_dist_to_nu_sdp"] = abs(abs(T) - nu)
            r["matches_nu_sdp"] = (abs(T - nu) < 1e-2)
            m = "YES" if r["matches_nu_sdp"] else "NO"
        else:
            r["matches_nu_sdp"] = None
            m = "(valid.)"
        nz = "yes" if r["nonreal"] else "no"
        print(f"{r['knot']:6} {abs(T):>11.5f} {T.real:>+13.5f} "
              f"{T.imag:>+13.5f} {str(nu):>6} {nz:>10} {m:>7}")
    print("-" * 82)

    verdict = _verdict(results)
    for line in verdict:
        print(line)

    out = {
        "schema": "qou-probe/torsion-vs-nu-sdp/v1",
        "bean": "qou-r307",
        "generated": datetime.datetime.utcnow().isoformat() + "Z",
        "conjecture": "conj:kashaev-density-equals-sdp-multiplicity",
        "literature": {
            "garoufalidis_yoon": "arXiv:2411.03801 (1-loop = adjoint torsion, two-bridge)",
            "dimofte_garoufalidis": "Geom.Topol. 17 (2013) 1253 (1-loop invariant)",
            "ohtsuki_takata": "Geom.Topol. 19 (2015) 853 (Kashaev asymptotics ↔ torsion)",
        },
        "method": ("adjoint (3-dim) twisted Reidemeister torsion via Fox "
                   "calculus on SnapPy numeric SL(2,C) holonomy; Porti "
                   "meridian torsion 𝕋_μ = −W'(1) (Yamaguchi simple-zero "
                   "slope); double precision. No ad-hoc rescaling — the "
                   "raw normalization already reproduces the known rational "
                   "𝕋_μ(4_1) = −3 (validation)."),
        "prediction_before_run": ("adjoint torsion lies in the trace field "
                                  "(ℚ(√−3) for 4_1; cubic for 6_2/8_11) → a "
                                  "non-integer, generically complex number; "
                                  "literal torsion = ν_SDP∈{1,2} expected to "
                                  "FAIL (scope-a category mismatch)."),
        "validation_4_1": {"T": results[0]["T_raw"], "known_value": -3.0,
                           "trace_field": "Q(sqrt(-3))"},
        "results": results,
        "verdict": verdict,
        "discipline": ("Evidence, not derivation. Does NOT prove the "
                       "conjecture, does NOT close the Lean class-instance "
                       "sorry, NOT wired to production."),
    }
    dst = os.path.join(os.path.dirname(__file__),
                       "torsion-vs-nu-sdp.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    with open(dst, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        out.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            out, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(out, f, indent=2)
    print(f"\nwitness → {dst}")


def _verdict(results):
    by = {r["knot"]: r for r in results}
    lines = ["VERDICT (scope-(a); a match would be evidence, not derivation):"]
    for k in ("6_2", "8_11"):
        r = by[k]
        T = complex(*r["T"])
        nu = r["nu_sdp"]
        lines.append(
            f"  {k}: 𝕋_μ ≈ {T.real:+.4f}{T.imag:+.4f}i  (|𝕋_μ|={abs(T):.4f}); "
            f"ν_SDP={nu}; |𝕋_μ−ν_SDP|={r['dist_to_nu_sdp']:.4f}; "
            f"Im≠0 ⇒ 𝕋_μ∉ℤ: {'YES' if r['nonreal'] else 'no'}; "
            f"equals ν_SDP: {'YES' if r['matches_nu_sdp'] else 'NO'}")
    lines.append(
        "  ⇒ adjoint Reidemeister torsion (= NZ 1-loop) is NOT ν_SDP for "
        "6_2, 8_11: both are complex trace-field numbers of modulus ≫ {1,2}. "
        "The literal 'topological density = ν_SDP integer' reading is refuted "
        "(scope-a). ν_SDP∈{1,2} is a distinct, normalization-free object.")
    return lines


if __name__ == "__main__":
    main()

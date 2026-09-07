"""aomega_m3_floor_remainder_from_derived_shape_fields_probe.py

Route C, milestone M3 (beans qou-rtec / qou-m3ad Part 4), on the corpus's OWN
data.  H_floor says: the knot-independent core of the DT index set is the
triple {trivial, geometric, conjugate-geometric} and the knot-DEPENDENT
remainder is the number of REAL embeddings of the trace field (Garoufalidis-
Zagier §2.1, transcribed into QOU/QBeta/AdjointIndexSetM3.lean as
`realEmbeddings`).  Until now both inputs of that rule -- the field and its
signature -- were read from a table.

This probe takes them from the two-bridge derivation instead
(two_bridge_layered_nz_probe.py, #6985): the shape fields the Farey-word
triangulations produce, 4_1 <- R giving z = e^{i pi/3} (minimal polynomial
x^2 - x + 1, disc -3) and 5_2 <- RL giving theta^3 - theta + 1 = 0 (disc -23),
and computes

  (1) the signature (r_1, r_2) of each field by an EXACT real-root count (Sturm
      sequence via sympy.real_roots on the integer polynomial; no floats decide
      anything);
  (2) |P_K| = 1 + r_1 + 2 r_2 and H_floor's remainder |P_K| - 3, compared with
      the transcribed Lean values (4_1 -> 0, 5_2 -> 1);
  (3) the Galois-conjugate complete structures: the shapes of every tetrahedron
      pushed through every embedding of the field, and the Bloch-Wigner volume
      Sum_i D(sigma(z_i)) at each -- the real embedding of 5_2 gives real shapes
      and volume exactly 0, the complex pair gives +/-Vol.  These are the
      Chern-Simons values {0, +V, -V} H_floor grades by, now derived rather than
      recalled (mpmath at 50 dps; the zero is exact because D vanishes on R).

What this does NOT do: it does not decide H_Ad vs H_floor (Part 2's T7 stands:
the core is 3 under both), and it does not touch the (-2,3,7) prediction, whose
field is not derived in this corpus.  Audit-only; scope-(a); no q, no anchor.
"""
from __future__ import annotations

import json
import os
import sys
import time

import mpmath as mp
import sympy as sp

mp.mp.dps = 50

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while ROOT != os.path.dirname(ROOT):
    if os.path.exists(os.path.join(ROOT, "AGENTS.md")):
        break
    ROOT = os.path.dirname(ROOT)
sys.path.insert(0, os.path.join(ROOT, "computations"))

NZ_WITNESS = os.path.join(HERE, "two-bridge-layered-nz.witness.json")


def bloch_wigner(z):
    """D(z) = Im Li_2(z) + arg(1-z) log|z|, mpmath, exact 0 on the real line."""
    z = mp.mpc(z)
    if z.imag == 0:
        return mp.mpf(0)
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def signature(poly):
    """(r1, r2) of Q[x]/(poly) by an exact Sturm real-root count."""
    x = sp.symbols("x")
    P = sp.Poly(poly, x)
    assert P.is_irreducible, poly
    r1 = len(sp.real_roots(P))         # Sturm, exact
    deg = P.degree()
    assert (deg - r1) % 2 == 0
    return r1, (deg - r1) // 2


def embeddings(poly, dps=50):
    """All complex roots, mpmath at dps, sorted real-first then by imaginary part."""
    x = sp.symbols("x")
    coeffs = [int(c) for c in sp.Poly(poly, x).all_coeffs()]
    roots = mp.polyroots(coeffs, maxsteps=200, extraprec=200)
    roots = [mp.mpc(r) for r in roots]
    # clean exact reals
    out = []
    for r in roots:
        if abs(r.imag) < mp.mpf(10) ** (-(dps - 10)):
            out.append(mp.mpc(r.real, 0))
        else:
            out.append(r)
    return sorted(out, key=lambda r: (r.imag != 0, mp.im(r)))


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    with open(NZ_WITNESS) as fh:
        nz = json.load(fh)
    nzd = nz["data"]
    x = sp.symbols("x")

    # ---- the derived shape fields ------------------------------------------
    # 4_1 <- R: both shapes e^{i pi/3}; minimal polynomial x^2 - x + 1.
    # 5_2 <- RL: shapes (theta, theta, theta^2-1, theta^2-1), theta^3 - theta + 1 = 0
    #   (the NZ witness records the relation and the Q(theta)-expressions).
    knots = {
        "fourone": dict(poly=x**2 - x + 1,
                        shape_exprs=[x, x],
                        n_tet=2,
                        lean_real_embeddings=0,   # AdjointIndexSetM3.realEmbeddings fourOne
                        lean_complex_pairs=1),
        "fivetwo": dict(poly=x**3 - x + 1,
                        shape_exprs=[sp.sympify(s) for s in nzd["fivetwo_shapes_in_Q_theta"]],
                        n_tet=4,
                        lean_real_embeddings=1,   # AdjointIndexSetM3.realEmbeddings fiveTwo
                        lean_complex_pairs=1),
    }
    # the derived 5_2 relation, from the witness, must be this cubic
    disc52 = int(nzd["fivetwo_cubic_discriminant"])
    check("fivetwo-derived-cubic-discriminant-is-minus-23", disc52 == -23 and
          int(sp.discriminant(knots["fivetwo"]["poly"], x)) == -23, witness=disc52)
    check("fourone-derived-shape-minimal-polynomial-disc-minus-3",
          int(sp.discriminant(knots["fourone"]["poly"], x)) == -3)

    results = {}
    for name, K in knots.items():
        P = K["poly"]
        r1, r2 = signature(P)
        pk = 1 + r1 + 2 * r2
        remainder = pk - 3
        print(f"\n[{name}] shape field Q[x]/({P}), disc {int(sp.discriminant(P, x))}: "
              f"signature (r1, r2) = ({r1}, {r2}); |P_K| = 1 + r1 + 2 r2 = {pk}; "
              f"H_floor remainder = {remainder}")
        check(f"{name}-signature-matches-transcribed-lean-values",
              r1 == K["lean_real_embeddings"] and r2 == K["lean_complex_pairs"],
              derived=(r1, r2), lean=(K["lean_real_embeddings"], K["lean_complex_pairs"]))
        check(f"{name}-pk-size-and-floor-remainder",
              pk == 1 + K["lean_real_embeddings"] + 2 * K["lean_complex_pairs"]
              and remainder == K["lean_real_embeddings"] + 2 * (K["lean_complex_pairs"] - 1),
              pk=pk, remainder=remainder)

        # ---- Galois-conjugate structures and their Bloch-Wigner volumes -------
        embs = embeddings(P)
        vols = []
        for sigma in embs:
            # evaluate each shape expression at the embedded root, exactly as a polynomial in x
            shapes = []
            for e in K["shape_exprs"]:
                cs = [int(c) for c in sp.Poly(e, x).all_coeffs()]
                v = mp.mpc(0)
                for c in cs:
                    v = v * sigma + c
                shapes.append(v)
            vol = mp.fsum(bloch_wigner(z) for z in shapes)
            vols.append((sigma, shapes, vol))
        vols_sorted = sorted(vols, key=lambda t: mp.re(t[2]))
        vol_values = [v for (_, _, v) in vols_sorted]
        print(f"    embeddings and volumes Sum_i D(sigma(z_i)):")
        for sigma, shapes, vol in vols_sorted:
            print(f"      sigma(theta) = {mp.nstr(sigma, 25):>60}   vol = {mp.nstr(vol, 30)}")
        results[name] = dict(
            poly=str(P), signature=[r1, r2], pk_size=pk, floor_remainder=remainder,
            embeddings=[mp.nstr(s, 45) for (s, _, _) in vols_sorted],
            conjugate_volumes=[mp.nstr(v, 45) for v in vol_values],
        )
        # the real embedding(s) carry volume exactly 0; the complex pair +/-V
        real_vols = [v for (s, _, v) in vols if s.imag == 0]
        cplx_vols = [v for (s, _, v) in vols if s.imag != 0]
        check(f"{name}-real-embeddings-have-volume-exactly-zero",
              len(real_vols) == r1 and all(v == 0 for v in real_vols),
              n_real=len(real_vols))
        check(f"{name}-complex-pair-carries-plus-minus-V",
              len(cplx_vols) == 2 and abs(cplx_vols[0] + cplx_vols[1]) < mp.mpf(10) ** -40
              and abs(cplx_vols[0]) > 1,
              pm=[mp.nstr(v, 30) for v in cplx_vols])
        results[name]["chern_simons_value_set"] = sorted(
            {"0"} | {mp.nstr(v, 40) for v in cplx_vols}) if r1 else sorted({mp.nstr(v, 40) for v in cplx_vols})

    # cross-knot: the derived Vol(5_2) reproduces the NZ witness's volume
    v52 = max(abs(mp.mpmathify(v)) for v in results["fivetwo"]["conjugate_volumes"])
    v41 = max(abs(mp.mpmathify(v)) for v in results["fourone"]["conjugate_volumes"])
    vol41_ref = 2 * mp.clsin(2, mp.pi / 3)       # 2*Cl_2(pi/3) = Vol(4_1)
    check("fourone-conjugate-volume-is-2Cl2(pi/3)", abs(v41 - vol41_ref) < mp.mpf(10) ** -40,
          v41=mp.nstr(v41, 30), ref=mp.nstr(vol41_ref, 30))
    vol52_ref = mp.mpmathify("2.8281220883307831627")
    check("fivetwo-conjugate-volume-matches-corpus-Vol(5_2)", abs(v52 - vol52_ref) < mp.mpf(10) ** -18,
          v52=mp.nstr(v52, 30), ref=str(vol52_ref))

    # the H_floor core is 3 for both, and the remainder differs by exactly 1 --
    # Part 1's forced unit remainder, now from the derived fields
    check("core-three-both-knots-remainder-differs-by-one",
          results["fourone"]["pk_size"] - results["fourone"]["floor_remainder"] == 3
          and results["fivetwo"]["pk_size"] - results["fivetwo"]["floor_remainder"] == 3
          and results["fivetwo"]["floor_remainder"] - results["fourone"]["floor_remainder"] == 1)

    verdict = (
        "H_floor's two inputs for 4_1 and 5_2 -- the trace field and its signature -- are "
        "now DERIVED from the corpus's own Farey-word triangulations (#6985) rather than "
        "transcribed from Garoufalidis-Zagier: x^2-x+1 (disc -3, signature (0,1)) and "
        "theta^3-theta+1 (disc -23, signature (1,1)), so |P_K| = 3, 4 and the remainders "
        "0, 1 follow by exact real-root counts, and the Galois-conjugate structures carry "
        "the Chern-Simons value sets {+V,-V} and {0,+V,-V} with the real embedding of 5_2 "
        "at volume exactly 0. This upgrades Part 4's rule from imported to derived on the "
        "two knots the corpus derives; it does NOT separate H_Ad from H_floor (core 3 under "
        "both) and does not reach (-2,3,7)."
    )
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    witness = {
        "name": "aomega-m3-floor-remainder-from-derived-shape-fields",
        "description": "H_floor's remainder (real-embedding count of the trace field) for "
                       "4_1 and 5_2 derived from the two-bridge shape fields, with the "
                       "Galois-conjugate Bloch-Wigner volumes {0, +/-V}.",
        "computation": "aomega-m3-floor-remainder-from-derived-shape-fields",
        "engine": "python",
        "scriptFile": os.path.basename(__file__),
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "durationMs": int((time.time() - t0) * 1000),
        "auditOnly": True,
        "auditDoc": "docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md",
        "parameters": {
            "source_witness": os.path.basename(NZ_WITNESS),
            "source_scriptHash": nz.get("scriptHash"),
            "source_computedAt": nz.get("computedAt"),
            "mp_dps": mp.mp.dps,
        },
        "data": results,
        "verdict": verdict,
        "assertions": assertions,
    }
    _WB.stamp_staleness_metadata(witness, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-floor-remainder-from-derived-shape-fields.witness.json")
    with open(out, "w") as fh:
        json.dump(witness, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())

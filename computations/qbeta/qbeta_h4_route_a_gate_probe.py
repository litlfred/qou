#!/usr/bin/env python3
"""qbeta_h4_route_a_gate_probe.py — bean 8we6 Route A: three owner-authorized
4th-strand framings, built and gate-tested for the canonical c4^even rung.

Owner authorization (2026-07-13 session, PR #3769): build ALL THREE candidate
framings from the 2026-07-03 route-B prune audit and let the decoupling gate
decide. The gate (recorded in that audit): the H4 object's ladder must
reproduce the trusted H3 rungs c2^even = -8.00641…, c3^even = +86.66116…
EXACTLY; if lower rungs move, the object is wrong (honest gate-fail).

Framings (all extend the SAME validated H3 net-route element
Delta(net) = net(NF(B3·crossings(u,d,d))) − net(NF(B3·crossings(u,u,d))),
free-neutron-decay.py conventions reproduced exactly and validated against
its witness):

  A1 "brane/Hopf strand" — 4th strand of else-branch type: the pairwise
      crossing loop extended to A=4 with pairs (i,3) falling to the bare
      sigma_gen branch (crossings at gens 0,1,2).
  A2 "lepton strand"     — the emitted electron's own word, shifted to the
      upper strands: multiply by sigma_1·sigma_2·sigma_1 (e- = s0s1s0 in H3).
  A3 "4-Brunnian core"   — replace B3 = (s0·s1^-1)^3 by the alternating
      4-strand candidate B4 = (s0·s1^-1·s2·s1^-1)^3 (Brunnian-style word;
      Brunnian property NOT verified here — the gate is the test), same three
      quark crossings.

For each framing: exact symbolic Delta(net)_4 in H4 (n-agnostic GB reducer:
Hecke + far-comm + Yang-Baxter, identical rules to free-neutron-decay.py),
(q-1)-regularizability check, exact s-series ladder through s^8
(qbeta_c3even_exact_sseries_probe.py machinery, KC=4), gate on exact c2/c3
match vs the in-run H3 baseline, and c4^even for gate-passers. W3 Casoratian
reported CONDITIONALLY (c4^odd is CAL-anchored tier; c3^odd -> -2 is the q=1
shadow) for any surviving rung.

auditOnly; NO production wiring; NO fit (every number is a Taylor coefficient
of an exact object; the framings are owner-authorized design candidates and
the gate can only falsify, not tune).

Witness: qbeta-h4-route-a-gate.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp
from mpmath import mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

HERE = Path(__file__).resolve().parent          # computations/qbeta
ROOT = HERE.parent                               # computations/
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "substrate"))

q, s = sp.symbols("q s", positive=True)
HA = q - 1 / q

KC = 4           # extract through c_4 (s^8)
NS = 2 * KC      # series order in s

# Trusted H3 rungs: loaded from the committed 1jrh exact-measurement witness
# (qbeta-c3even-exact-sseries.witness.json numeric_50dps), NOT hardcoded — an
# earlier draft hand-extended the bean's 6-digit quotes and tripped the repro
# assertion at 1e-9 spuriously.
_1JRH = json.loads((Path(__file__).resolve().parent / "qbeta-c3even-exact-sseries.witness.json").read_text())
C2_GATE = _1JRH["numeric_50dps"]["c2_even"]
C3_GATE = _1JRH["numeric_50dps"]["c3_even"]


# ── quiet n-agnostic GB reducer (rules identical to free-neutron-decay.py) ──
def reduce_quiet(terms_dict, max_iterations=20000):
    terms = {w: c for w, c in terms_dict.items() if c != 0}
    changed, iteration = True, 0
    while changed and iteration < max_iterations:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if coeff == 0:
                continue
            reduced_this = False
            # R1 Hecke: s_i^2 -> (q - q^-1) s_i + 1
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1] and word[pos] >= 0:
                    i = word[pos]
                    w1 = word[:pos] + (i,) + word[pos + 2:]
                    w2 = word[:pos] + word[pos + 2:]
                    new_terms[w1] = sp.expand(new_terms.get(w1, sp.Integer(0)) + coeff * HA)
                    new_terms[w2] = sp.expand(new_terms.get(w2, sp.Integer(0)) + coeff)
                    reduced_this = changed = True
                    break
            if reduced_this:
                continue
            # R2 far-comm: descending adjacent pair with |i-j| >= 2
            for pos in range(len(word) - 1):
                i_gen, j_gen = word[pos], word[pos + 1]
                if abs(i_gen - j_gen) >= 2 and i_gen > j_gen and i_gen >= 0 and j_gen >= 0:
                    new_word = word[:pos] + (j_gen, i_gen) + word[pos + 2:]
                    new_terms[new_word] = sp.expand(new_terms.get(new_word, sp.Integer(0)) + coeff)
                    reduced_this = changed = True
                    break
            if reduced_this:
                continue
            # R3 Yang-Baxter (orientation: only if it lowers the word)
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and a >= 0 and b >= 0 and abs(a - b) == 1 and (b, a, b) < (a, b, a):
                    new_word = word[:pos] + (b, a, b) + word[pos + 3:]
                    new_terms[new_word] = sp.expand(new_terms.get(new_word, sp.Integer(0)) + coeff)
                    reduced_this = changed = True
                    break
            if not reduced_this:
                new_terms[word] = sp.expand(new_terms.get(word, sp.Integer(0)) + coeff)
        terms = {w: c for w, c in new_terms.items() if c != 0}
        iteration += 1
    assert iteration < max_iterations, "reducer did not terminate"
    return terms


def mul_terms(a_terms, b_terms):
    result = {}
    for wa, ca in a_terms.items():
        for wb, cb in b_terms.items():
            w = wa + wb
            result[w] = sp.expand(result.get(w, sp.Integer(0)) + ca * cb)
    return {w: c for w, c in result.items() if c != 0}


def crossing(type_i, type_j, gen):
    """free-neutron-decay.py crossing rules (code-authoritative forms)."""
    if type_i == type_j == "u":
        return {(gen,): sp.Integer(1)}
    if type_i == type_j == "d":
        return {(gen,): sp.Integer(1), (): -HA}
    if {type_i, type_j} == {"u", "d"}:
        return {(gen,): sp.Integer(1), (): -HA / 2}
    return {(gen,): sp.Integer(1)}    # else-branch: bare sigma_gen ("Hopf")


def baryon(core, types):
    elem = dict(core)
    for i in range(len(types)):
        for j in range(i + 1, len(types)):
            elem = reduce_quiet(mul_terms(elem, crossing(types[i], types[j], i)))
    return elem


def net(terms):
    return sp.simplify(sum(terms.values(), start=sp.Integer(0)))


def ladder_cks(dnet, kc=KC, ns=NS, label=""):
    """Exact s-series triangular solve of the net-route ladder (1jrh machinery)."""
    dnet_reg = sp.cancel(sp.together(dnet) / (q - 1))
    hbar = (q - 1) / q
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    u = b * hbar**2
    z = q**3 / (q**2 + 1)
    h = q - 1 / q
    alpha_eff = (z - 1) * h / 2 - u / 2
    QA_over_me = (2 * q + 1 - q**2) * (q + 1) / (2 * q**3)
    # sign at the substrate anchor
    q0n = mp.mpf("1.1099785955573347198997632204832250266562084087802")
    sgn = int(mp.sign(mp.mpf(str(sp.N(dnet.subs(q, sp.Rational(11099785955573347, 10000000000000000)), 30)))))
    Qb_over_me = sgn * dnet_reg / q
    Rq = Qb_over_me / (QA_over_me * sp.cos(alpha_eff))
    R1 = sp.simplify(Rq.subs(q, 1))
    t1 = time.monotonic()
    logR_ser = sp.series(sp.log(Rq.subs(q, 1 + s) / R1), s, 0, ns + 1).removeO()
    u_ser = sp.series(u.subs(q, 1 + s), s, 0, ns + 1).removeO()
    logR_c = [sp.simplify(logR_ser.coeff(s, i)) for i in range(ns + 1)]
    u_c = [sp.simplify(u_ser.coeff(s, i)) for i in range(ns + 1)]
    print(f"    [{label}] series to O(s^{ns+1}) in {time.monotonic()-t1:.1f}s; R(1)={R1}")

    def ser_mul(a, bb):
        return [sp.expand(sum(a[i] * bb[n - i] for i in range(n + 1))) for n in range(ns + 1)]

    upow = {1: u_c}
    for k in range(2, kc + 1):
        upow[k] = ser_mul(upow[k - 1], u_c)
    c, model = {}, [sp.Integer(0)] * (ns + 1)
    for k in range(2, kc + 1):
        order = 2 * k
        resid = sp.simplify(logR_c[order] - model[order])
        ck = sp.simplify(resid / upow[k][order])
        c[k] = ck
        cku = [sp.expand(ck * t) for t in upow[k]]
        cur = [sp.Integer(1)] + [sp.Integer(0)] * ns
        n = 1
        while n * order <= ns:
            cur = ser_mul(cur, cku)
            sign = sp.Integer((-1) ** (n + 1))
            for i in range(ns + 1):
                model[i] = sp.expand(model[i] + sign * cur[i] / n)
            n += 1
    return c, R1


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    print("=" * 78)
    print(" 8we6 Route A: three 4th-strand framings, decoupling-gated (owner-authorized)")
    print("=" * 78)

    # ── H3 baseline, validated against the committed witness ──
    sig1_inv = {(1,): sp.Integer(1), (): -HA}
    unit = reduce_quiet(mul_terms({(0,): sp.Integer(1)}, sig1_inv))
    b3 = reduce_quiet(mul_terms(reduce_quiet(mul_terms(unit, unit)), unit))
    elem_n3 = baryon(b3, ["u", "d", "d"])
    elem_p3 = baryon(b3, ["u", "u", "d"])
    dnet3 = sp.simplify(net(elem_n3) - net(elem_p3))

    d_wit = json.loads((ROOT / "free-neutron-decay.witness.json").read_text())
    q0 = mp.mpf(str(d_wit.get("q0", "1.1099785955573347198997632204832250266562084087802")))
    dn_wit = mp.mpf(str(d_wit["transition"]["delta_net"]))
    dn_mine = mp.mpf(str(sp.N(dnet3.subs(q, sp.nsimplify(str(q0))), 30)))
    ok_wit = abs(dn_mine - dn_wit) < mp.mpf("1e-6")
    print(f"\n[0] H3 Delta(net) reproduction vs witness: {ok_wit}  ({mp.nstr(dn_mine,10)} vs {mp.nstr(dn_wit,10)})")

    print("\n[1] H3 baseline ladder (in-run, same conventions):")
    c3base, _ = ladder_cks(dnet3, label="H3")
    c2b = mp.mpf(str(sp.N(c3base[2], 40)))
    c3b = mp.mpf(str(sp.N(c3base[3], 40)))
    gate_repro = (abs(c2b - mp.mpf(C2_GATE)) < mp.mpf("1e-9")) and (abs(c3b - mp.mpf(C3_GATE)) < mp.mpf("1e-9"))
    print(f"    c2^even={mp.nstr(c2b,14)} c3^even={mp.nstr(c3b,14)}  (trusted-rung repro: {gate_repro})")
    print(f"    H3 c4-order coefficient (baseline, s^8): {mp.nstr(mp.mpf(str(sp.N(c3base[4], 30))), 10)}")

    # ── the three framings ──
    framings = {}

    # A1: brane/Hopf 4th strand — pairwise loop extended to A=4, else-branch pairs
    framings["A1_brane_hopf_strand"] = (
        baryon(b3, ["u", "d", "d", "b"]),
        baryon(b3, ["u", "u", "d", "b"]),
        "pairwise loop extended to A=4; (i,3) pairs take the bare sigma_gen else-branch",
    )

    # A2: lepton strand — multiply by the shifted electron word s1 s2 s1
    e_word = {(1, 2, 1): sp.Integer(1)}
    framings["A2_lepton_strand"] = (
        reduce_quiet(mul_terms(elem_n3, e_word)),
        reduce_quiet(mul_terms(elem_p3, e_word)),
        "emitted-lepton word e- = s0s1s0 shifted to upper strands (s1s2s1), appended",
    )

    # A3: 4-Brunnian core — B4 = (s0 s1^-1 s2 s1^-1)^3, same quark crossings
    sig2 = {(2,): sp.Integer(1)}
    unit4 = reduce_quiet(mul_terms(mul_terms(unit, sig2), sig1_inv))
    b4 = reduce_quiet(mul_terms(reduce_quiet(mul_terms(unit4, unit4)), unit4))
    framings["A3_brunnian4_core"] = (
        baryon(b4, ["u", "d", "d"]),
        baryon(b4, ["u", "u", "d"]),
        "core replaced by candidate B4 = (s0 s1^-1 s2 s1^-1)^3 (Brunnian property unverified)",
    )

    results = {}
    for name, (en, ep, desc) in framings.items():
        print(f"\n[2] framing {name}: {desc}")
        dnet4 = sp.simplify(net(en) - net(ep))
        at1 = sp.simplify(dnet4.subs(q, 1))
        regularizable = (at1 == 0)
        print(f"    Delta(net)_4(q=1) = {at1}  (regularizable: {regularizable})")
        entry = {"description": desc, "delta_net4": str(dnet4), "regularizable": bool(regularizable)}
        if not regularizable:
            entry["gate"] = "FAIL (structural: (q-1) does not divide Delta(net)_4)"
            print("    GATE: FAIL structurally — no (q-1) zero, the ladder is not defined.")
            results[name] = entry
            continue
        if sp.simplify(dnet4 - dnet3) == 0:
            entry["gate"] = "TRIVIAL (Delta(net)_4 == Delta(net)_3 identically; no new rung)"
            print("    GATE: TRIVIAL — identical to H3; the framing adds no sigma_2 content to net().")
            results[name] = entry
            continue
        cks, _ = ladder_cks(dnet4, label=name)
        c2n = mp.mpf(str(sp.N(cks[2], 40)))
        c3n = mp.mpf(str(sp.N(cks[3], 40)))
        d2 = sp.simplify(cks[2] - c3base[2])
        d3 = sp.simplify(cks[3] - c3base[3])
        gate_pass = (d2 == 0) and (d3 == 0)
        if not gate_pass:  # exact simplify can miss; confirm numerically
            gate_pass = (abs(c2n - c2b) < mp.mpf("1e-30")) and (abs(c3n - c3b) < mp.mpf("1e-30"))
        entry.update({"c2_even": mp.nstr(c2n, 25), "c3_even": mp.nstr(c3n, 25),
                      "c2_shift": mp.nstr(c2n - c2b, 10), "c3_shift": mp.nstr(c3n - c3b, 10),
                      "gate": "PASS" if gate_pass else "FAIL (lower rungs moved)"})
        print(f"    c2^even={mp.nstr(c2n,14)} (shift {mp.nstr(c2n-c2b,6)})  c3^even={mp.nstr(c3n,14)} (shift {mp.nstr(c3n-c3b,6)})")
        print(f"    GATE: {entry['gate']}")
        if gate_pass:
            c4n = mp.mpf(str(sp.N(cks[4], 40)))
            entry["c4_even_exact"] = str(cks[4])
            entry["c4_even"] = mp.nstr(c4n, 25)
            # conditional W3 (c4^odd CAL-anchored tier; c3^odd -> -2 shadow)
            W3 = c3n * mp.mpf("-0.97157") - c4n * mp.mpf("-2")
            entry["W3_conditional"] = mp.nstr(W3, 15)
            print(f"    c4^even = {mp.nstr(c4n,14)}   W3(cond, CAL-anchored c4^odd) = {mp.nstr(W3,10)}")
        results[name] = entry

    # ── witness ──
    witness = {
        "computation": "qbeta-h4-route-a-gate",
        "description": (
            "Bean 8we6 Route A: the three owner-authorized 4th-strand framings "
            "(brane/Hopf pairwise extension, lepton strand s1s2s1, 4-Brunnian core "
            "candidate) built in H4 with the n-agnostic GB reducer and gate-tested: "
            "the ladder must reproduce the trusted H3 rungs c2^even/c3^even exactly "
            "(decoupling gate, 2026-07-03 audit); c4^even extracted only for "
            "gate-passers; W3 Casoratian reported conditionally on the CAL-anchored "
            "c4^odd tier. auditOnly; no production wiring; no fit."
        ),
        "audit_only": True,
        "parameters": {"q0": str(q0), "series_order": NS, "KC": KC,
                       "gate_values": {"c2_even": C2_GATE, "c3_even": C3_GATE}},
        "h3_baseline": {"delta_net": str(dnet3),
                        "c2_even": mp.nstr(c2b, 25), "c3_even": mp.nstr(c3b, 25),
                        "c4_order_coeff_baseline": mp.nstr(mp.mpf(str(sp.N(c3base[4], 30))), 20)},
        "framings": results,
        "assertions": [
            {"label": "H3 Delta(net) matches committed witness at q0 (<1e-6)", "passed": bool(ok_wit)},
            {"label": "in-run H3 ladder reproduces trusted rungs c2/c3 (<1e-9)", "passed": bool(gate_repro)},
        ],
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    import os
    witness["scriptFile"] = os.path.basename(__file__)
    witness["durationMs"] = int((time.monotonic() - t0) * 1000)
    out = HERE / "qbeta-h4-route-a-gate.witness.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"\n  Witness: {out.name}   ({time.monotonic() - t0:.1f}s wall)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

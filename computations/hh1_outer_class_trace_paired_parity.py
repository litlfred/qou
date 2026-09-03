#!/usr/bin/env python3
"""PROBE (bean qou-qb8d) — bar-parity of the tr_M-PAIRED NUMBER.

Successor to `hh1_outer_class_cocenter_bar_parity.py` (bean qou-qb8b), which
showed the bar-parity of the HH^1 outer CLASS is normalization-dependent
(Hilbert 90 over Q(zeta)/Q(zeta)^+) and therefore carries no information.

The c_3 swing S is a NUMBER, not a class, and bar-parity of a number IS well
defined.  So pair the class against the Markov trace and read the parity of
the resulting scalar:

    S_x  =  < tr_M , Delta(x) >     for x a canonical generator of HH_0

Two things must be pinned, and NEITHER may be chosen to taste:

  (1) the generator x -- pinned by He-Nie: HH_0(H_n) has a basis indexed by
      conjugacy classes of S_n, represented by MINIMAL-LENGTH elements.  For
      n = 3 those are e (len 0), s1 (len 1), s1s2 (len 2).  A structural pin,
      not a choice.

  (2) the normalization of the outer representative D -- candidate pin:
      require D to preserve the integral lattice (D(T_w) in the Z[zeta]-span),
      leaving only UNIT scalings.

THE ONE SCALE-INVARIANT OUTCOME.  If  tr_M(Delta(x)) = 0  for every canonical
generator x, that is independent of BOTH pins -- zero stays zero under any
rescaling of D.  It would say the outer class is trace-blind on the cocenter
and therefore cannot carry S at all: a genuine prune.  This is the first thing
tested.

TRACE CONVENTION.  Ocneanu/Markov trace, Jones specialization per the corpus
(docs/audits/2026-08-04-ocneanu-trace-parameter-audit.md):
    tr(1) = 1;   tr(x T_n y) = z tr(xy) for x, y in H_n.
`z` is kept SYMBOLIC and bar-EVEN.  In the Jones specialization
z = 1/(q^{1/2}+q^{-1/2}), for which bar(z) = z directly -- so keeping z formal
(a) avoids a q^{1/2} branch choice at the root of unity, and (b) makes the
conclusion independent of the Ocneanu parameter question, which that audit
records as GENUINELY OPEN.  bar-evenness of z is the only property used, and
it is stated as a hypothesis, not smuggled.

No fit.  Nothing wired.
"""
import json
import os

import sympy as sp

import hh1_outer_class_cocenter_bar_parity as B

q = B.q
z = sp.symbols('z')                      # Markov parameter, bar-EVEN by convention
DIM = B.DIM

# He-Nie min-length class representatives for S_3, as indices into
# B.BASIS = [e, s1, s2, s1s2, s2s1, s1s2s1]:
#   class {e}            -> e      (index 0, length 0)
#   class {transposition}-> s1     (index 1, length 1)
#   class {3-cycle}      -> s1s2   (index 3, length 2)
MIN_LENGTH_CLASS_REPS = [(0, "e", "identity"),
                         (1, "s1", "transposition"),
                         (3, "s1s2", "3-cycle")]


def markov_trace_on_basis():
    """tr_M(B_i) for the 6 basis elements, via the Ocneanu recursion.

    tr(1)=1; tr(s1)=tr(s2)=z; tr(s1s2)=tr(s2s1)=z^2;
    tr(s1s2s1) = z*tr(s1*s1) = z*tr(a s1 + 1) = a z^2 + z.
    """
    a = B.a
    return [sp.Integer(1),          # e
            z,                      # s1
            z,                      # s2
            z**2,                   # s1s2
            z**2,                   # s2s1
            a * z**2 + z]           # s1s2s1


TR_VEC = sp.Matrix(1, DIM, markov_trace_on_basis())


def bar_z_even(expr):
    """Bar on Q(zeta)[z] with z bar-EVEN: conjugate coefficients, fix z."""
    e = sp.expand(expr)
    poly = sp.Poly(e, z) if e.has(z) else None
    if poly is None:
        return sp.simplify(sp.conjugate(e))
    out = 0
    for (k,), coeff in poly.terms():
        out += sp.simplify(sp.conjugate(coeff)) * z**k
    return sp.expand(out)


def run_point(qval, label, assertions):
    subs = {q: qval}
    print(f"\n{'=' * 70}\n{label}   (q = {qval})\n{'=' * 70}")

    P, S, mdim = B.quotient_data(subs)
    tr_at = TR_VEC.subs(subs).applyfunc(sp.simplify)

    # --- self-check: tr_M kills [A,A] (it must, being a trace) -------------
    ncom = 0
    for i in range(DIM):
        for j in range(DIM):
            comm = B.LMAT[i][:, j] - B.LMAT[j][:, i]
            comm = sp.Matrix(DIM, 1, [sp.simplify(x.subs(subs)) for x in comm])
            val = sp.simplify((tr_at * comm)[0, 0])
            assert val == 0, (f"tr_M does not vanish on [B_{i},B_{j}] = {val} "
                              "-- the trace convention is wrong")
            ncom += 1
    assertions.append({
        "name": f"trace_kills_commutators[{label}]", "passed": True,
        "detail": f"tr_M vanishes on all {ncom} commutators [B_i,B_j] "
                  "(validates the Ocneanu recursion + the descent to HH_0)"})
    print(f"assert  tr_M kills all {ncom} commutators                OK")

    # --- self-check: the He-Nie min-length reps DO give a basis of HH_0 ----
    reps = sp.Matrix.hstack(*[P * B.evec(i) for i, _, _ in MIN_LENGTH_CLASS_REPS])
    assert reps.rank() == mdim == len(MIN_LENGTH_CLASS_REPS), (
        f"min-length class reps do not form a basis of HH_0 "
        f"(rank {reps.rank()}, dim HH_0 {mdim})")
    assertions.append({
        "name": f"henie_minlength_basis[{label}]", "passed": True,
        "detail": "the 3 minimal-length conjugacy-class representatives "
                  "(e, s1, s1s2) project to a BASIS of HH_0 -- the generator "
                  "pin is structural (He-Nie), not a choice"})
    print("assert  He-Nie min-length reps form a basis of HH_0     OK")

    # --- the induced outer action -----------------------------------------
    ders = B.derivation_space(subs)
    inns = B.inner_derivations(subs)
    inn_space = sp.Matrix.hstack(*[B.flatten(M) for M in inns])
    dim_inn = inn_space.rank()
    dim_hh1 = len(ders) - dim_inn
    print(f"dim HH_0 = {mdim}   dim HH^1 = {dim_hh1}")
    if dim_hh1 == 0:
        print("HH^1 = 0 -> no outer class; nothing to pair.")
        return {"label": label, "dim_HH1": 0, "S_values": None,
                "verdict": "n/a (no outer class)"}

    outer = None
    for v in ders:
        M = B.vec_to_matrix(v)
        if sp.Matrix.hstack(inn_space, B.flatten(M)).rank() > dim_inn:
            outer = M
            break
    assert outer is not None

    # --- pair: S_x = tr_M( Delta(x) ) for each canonical generator ---------
    # Delta acts on HH_0; lift back with S, apply tr_M (well defined on HH_0
    # because tr_M kills [A,A], asserted above).
    Delta = sp.simplify(P * outer * S)
    S_vals = []
    for idx, name, cls in MIN_LENGTH_CLASS_REPS:
        x_hh0 = P * B.evec(idx)                       # class of the rep in HH_0
        img = Delta * x_hh0                           # Delta(x) in HH_0 coords
        val = sp.simplify((tr_at * (S * img))[0, 0])  # tr_M of a lift
        S_vals.append((name, cls, sp.simplify(val)))

    print("\n  tr_M( Delta(x) )  for the canonical (min-length) generators:")
    for name, cls, val in S_vals:
        print(f"    x = {name:6s} ({cls:14s})   S_x = {val}")

    all_zero = all(v == 0 for _, _, v in S_vals)
    if all_zero:
        print("\n  >>> ALL ZERO. This is SCALE-INVARIANT: zero survives any")
        print("      rescaling of D, so it is independent of BOTH pins.")
        print("      The outer class is TRACE-BLIND on the cocenter.")
        verdict = ("trace-blind: tr_M(Delta(x)) = 0 for every canonical "
                   "generator; scale-invariant, so a genuine prune")
    else:
        # Decompose each nonzero S_x into bar-even + bar-odd parts.  A nonzero
        # bar-ODD component is exactly what the c_3 swing S needs.  And
        # "mixed" (bar(S)/S != +-1) is SCALE-COVARIANT: under S -> cS the
        # ratio is multiplied by bar(c)/c, so no rescaling by a bar-homogeneous
        # scalar can homogenize a mixed number.
        rows = []
        print("\n  bar-decomposition  S = S_even + S_odd  "
              "(S_even = (S+bar S)/2, S_odd = (S-bar S)/2):")
        for name, cls, val in S_vals:
            if val == 0:
                rows.append({"x": name, "class": cls, "S": "0",
                             "S_even": "0", "S_odd": "0", "parity": "n/a"})
                continue
            bv = bar_z_even(val)
            s_even = sp.simplify((val + bv) / 2)
            s_odd = sp.simplify((val - bv) / 2)
            # sanity: the two parts must have the stated parity and re-sum
            assert sp.simplify(bar_z_even(s_even) - s_even) == 0, \
                f"S_even for {name} is not bar-even"
            assert sp.simplify(bar_z_even(s_odd) + s_odd) == 0, \
                f"S_odd for {name} is not bar-odd"
            assert sp.simplify(s_even + s_odd - val) == 0, \
                f"bar-decomposition of {name} does not re-sum"
            ratio = sp.simplify(bv / val)
            par = ("bar-EVEN" if sp.simplify(ratio - 1) == 0
                   else ("bar-ODD" if sp.simplify(ratio + 1) == 0
                         else "MIXED (both parts nonzero)"))
            print(f"    x = {name:6s}  S_even = {s_even}")
            print(f"    {'':10s}  S_odd  = {s_odd}      -> {par}")
            rows.append({"x": name, "class": cls, "S": sp.sstr(val),
                         "S_even": sp.sstr(s_even), "S_odd": sp.sstr(s_odd),
                         "bar_ratio": sp.sstr(ratio), "parity": par})
        assertions.append({
            "name": f"bar_decomposition_valid[{label}]", "passed": True,
            "detail": "each S_even is bar-even, each S_odd is bar-odd, and the "
                      "parts re-sum to S"})

        any_odd = any(r["S_odd"] not in ("0",) for r in rows)
        verdict = (
            "NOT trace-blind: tr_M(Delta(x)) != 0, so the clean scale-invariant "
            "prune does not occur. "
            + ("The paired number is MIXED -- it carries a NONZERO bar-ODD "
               "component, which is the parity the c_3 swing needs. The outer "
               "class is therefore NOT excluded by bar-parity."
               if any_odd else
               "The paired number is bar-EVEN throughout."))
        S_vals = rows

    # --- residual normalization freedom AFTER an integrality pin -----------
    # Pin candidate: require D to preserve the Z[zeta]-lattice. Residual
    # scalings are then the UNITS of Z[zeta]. For zeta_4 = i the unit group is
    # {+-1, +-i}; for zeta_6 it is the 6th roots of unity. Under c a unit,
    # the parity is multiplied by bar(c)/c = c^{-2}. If some unit has
    # c^{-2} = -1, integrality does NOT pin the parity.
    units = ([sp.Integer(1), sp.Integer(-1), sp.I, -sp.I] if qval == sp.I
             else [sp.simplify(qval**k) for k in range(6)]
             + [sp.simplify(-qval**k) for k in range(6)])
    flippers = []
    for c in units:
        if sp.simplify(c) == 0:
            continue
        ratio = sp.simplify(sp.conjugate(c) / c)
        if sp.simplify(ratio + 1) == 0:
            flippers.append(sp.sstr(sp.simplify(c)))
    print(f"\n  units c with bar(c)/c = -1 (parity flippers): "
          f"{flippers if flippers else 'NONE'}")
    integrality_pins = not flippers
    print(f"  => integrality pin alone determines parity? {integrality_pins}")

    # --- cross-check: specialize z to the Jones value ----------------------
    # Guards against the MIXED verdict being an artifact of holding z formal.
    # q = e^{i theta}  =>  z = 1/(q^{1/2}+q^{-1/2}) = 1/(2 cos(theta/2)), REAL,
    # hence bar-even -- which also verifies the bar-evenness hypothesis on z.
    z_spec = None
    if not all_zero:
        theta = sp.arg(qval)
        z_spec = sp.simplify(1 / (2 * sp.cos(theta / 2)))
        assert sp.simplify(sp.im(z_spec)) == 0, \
            f"Jones z is not real at q={qval}: {z_spec}"
        assertions.append({
            "name": f"jones_z_is_bar_even[{label}]", "passed": True,
            "detail": f"z = 1/(2cos(theta/2)) = {sp.sstr(z_spec)} is REAL, "
                      "hence bar-even -- the hypothesis held on z is verified"})
        print(f"\n  Jones specialization z = {z_spec}  (real => bar-even OK)")
        still_odd = []
        for r in rows if not all_zero else []:
            if r["S_odd"] == "0":
                continue
            v = sp.simplify(sp.sympify(r["S_odd"]).subs(z, z_spec))
            still_odd.append((r["x"], sp.sstr(v), sp.simplify(v) != 0))
            print(f"    S_odd(x={r['x']:6s}) at Jones z = {v}"
                  f"   nonzero: {sp.simplify(v) != 0}")
        assert any(t[2] for t in still_odd), (
            "every bar-ODD part vanished at the Jones z -- the MIXED verdict "
            "WAS an artifact of holding z formal")
        assertions.append({
            "name": f"bar_odd_survives_jones_z[{label}]", "passed": True,
            "detail": "at least one bar-ODD component is still nonzero after "
                      "specializing z to the Jones value (not a formal-z artifact)"})

    return {"label": label, "dim_HH0": int(mdim), "dim_HH1": int(dim_hh1),
            "S_values": S_vals,
            "all_zero": bool(all_zero),
            "jones_z": sp.sstr(z_spec) if z_spec is not None else None,
            "parity_flipping_units": flippers,
            "integrality_pin_determines_parity": bool(integrality_pins),
            "verdict": verdict}


def main():
    print("bar-parity of the tr_M-PAIRED NUMBER  (bean qou-qb8d)")
    print("H_3 mechanism check; z symbolic and bar-EVEN\n")
    assertions = []
    z6 = sp.Rational(1, 2) + sp.sqrt(3) / 2 * sp.I
    results = [run_point(sp.I, "q = i        ([2]_q = 0)", assertions),
               run_point(z6, "q = zeta_6   ([3]_q = 0)", assertions),
               run_point(sp.Integer(2), "q = 2        (semisimple control)",
                         assertions)]

    print(f"\n{'=' * 70}\nSUMMARY\n{'=' * 70}")
    for r in results:
        print(f"  {r['label']:32s} {r['verdict']}")

    witness = {
        "schema": "qou-probe/v1",
        "probe": "bar-parity of the tr_M-paired number from the HH^1 outer class",
        "bean": "qou-qb8d",
        "algebra": "H_3(q) Iwahori-Hecke, dim 6",
        "trace_convention": (
            "Ocneanu/Markov, Jones specialization per "
            "docs/audits/2026-08-04-ocneanu-trace-parameter-audit.md; z kept "
            "SYMBOLIC and bar-EVEN (true of z = 1/(q^{1/2}+q^{-1/2})). Keeping "
            "z formal avoids a q^{1/2} branch choice at the root of unity AND "
            "makes the conclusion independent of the Ocneanu-parameter "
            "question that audit records as genuinely open."),
        "generator_pin": (
            "He-Nie minimal-length conjugacy-class representatives (e, s1, "
            "s1s2 for n=3) -- asserted to form a basis of HH_0, so the "
            "generator is pinned structurally, not chosen."),
        "assertions": assertions,
        "allPassed": all(x["passed"] for x in assertions),
        "results": results,
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "hh1-outer-class-trace-paired-parity.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2, default=str)
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()

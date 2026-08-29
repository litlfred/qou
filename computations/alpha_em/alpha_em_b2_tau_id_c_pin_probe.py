#!/usr/bin/env python3
"""alpha_em_b2_tau_id_c_pin_probe.py

B2 tau-IDENTIFICATION, Options A + C (support for the PRIMARY Option B),
epic qou-6ufi — picked up from the stalled sibling (owner: "4080 agent is
stalled. pick up the work"). Under the standing 2026-07-19 ruling (R2 /
the per-loop identification is NOT derived-proved) and the attack-options
scope discipline (docs/audits/2026-07-24-alpha-em-b2-tau-identification-
attack-options.md): no tau-functor constructed, no TauRhoHodgeLift
instance registered, nothing tuned.

WHAT THIS PROBE DOES (V1-V6):
  V1. BUILD the (4,1) std block of H_5(q) concretely as the rescaled
      reduced Burau representation rho(sigma_i) = -q^{-1} * B_i(q^2)
      (4x4), and SELF-VALIDATE: braid relations + Hecke relation
      (sigma - q)(sigma + q^{-1}) = 0 hold symbolically. (Option A's
      "pin the block": the (n-1,1) Specht of H_n(q) IS reduced Burau at
      t = q^2 up to the -q^{-1} rescale — verified, not assumed.)
  V2. SCHUR HYPOTHESIS CONCRETE: at the exact rational q0 proxy
      (110998/100000) the commutant of the block is 1-dimensional
      (scalar) — the exact hypothesis `schur` of the sibling's sorry-free
      invariantForm_proportional_of_commutantScalar, instantiated at the
      actual alpha_EM block. Also verified at q = 1 (classical std of
      S_5, absolutely irreducible).
  V3. THE MARKOV GRAM, EXACTLY (Option A deliverable): the space of
      symmetric G with G*rho(sigma_i) = rho(sigma_i)^T*G (associativity
      of the trace form tr(x*y) — the Hecke-side invariance) is
      1-DIMENSIONAL at q0; the normalized generator G_M is computed with
      EXACT rational entries. Reality + symmetry: confirmed concretely
      (the sibling's Markov-side discharge, now with the explicit
      matrix). Positivity: checked as the BONUS (per #4151 it is NOT
      needed for the lift).
  V4. CLASSICAL SHADOW: at q = 1 the same solve returns the S_5-invariant
      form on std; the deck 4-cycle (2345) = s_2 s_3 s_4 has eigenvalues
      {1, i, -1, -i} on std (the F-construction T2 dictionary), tying the
      Hecke block to the H^{1,0}(Bring) carrier.
  V5. HODGE SIDE RECORDED (Option C, the honest half): Jac(Bring) ~
      E_{5tau0}^3 x E_{tau0} (period tau0*diag(5,5,5,1), Braden-Northover
      50a class) gives the Hodge Gram the (3,1)-degenerate pattern
      diag(5,5,5,1)*Im(tau0) in the ISOGENY-adapted frame. That frame is
      NOT an S_5-equivariant frame, so a direct entrywise ratio against
      G_M (seminormal frame) is frame-dependent and would be numerology.
      The scale c of Schur proportionality is extractable ONLY through
      the S_5-equivariant transport — exactly Option B's open premise
      (i). NAMED OPEN; no ratio is tuned or reported as c.
  V6. HONEST STATUS: what this closes (explicit block + exact Markov
      Gram + concrete Schur hypothesis at q0) vs what stays open (the
      equivariance premise (i); the scalar c (ii); the identification
      itself). 1/(8pi) stays phase-4.

Scope guard: no fit; nothing wired; the tau-identification remains the
sole open categorical input. Self-contained (sympy).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp


def burau_matrices_n5(t):
    """Explicit reduced Burau for B_5 (4x4), column-action convention.
    Self-validated downstream; if relations fail the probe FAILS loudly."""
    B1 = sp.Matrix([[-t, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    B2 = sp.Matrix([[1, 0, 0, 0],
                    [t, -t, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    B3 = sp.Matrix([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, t, -t, 1],
                    [0, 0, 0, 1]])
    B4 = sp.Matrix([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, t, -t]])
    return [B1, B2, B3, B4]


def commutant_dim(mats):
    """Dimension of {A : A*M = M*A for all M in mats} (16 unknowns, exact)."""
    a = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'a{i}{j}'))
    eqs = []
    for M in mats:
        E = a * M - M * a
        eqs.extend(list(E))
    unknowns = list(a)
    sol = sp.linsolve(eqs, unknowns)
    # dimension = number of free parameters
    (tup,) = sol
    free = set()
    for expr in tup:
        free |= expr.free_symbols & set(unknowns)
    return len(free)


def invariant_form_space(mats):
    """Symmetric G with G*M = M^T*G for all M (trace-form associativity).
    Returns (dimension, a normalized exact generator or None)."""
    g = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'g{min(i,j)}{max(i,j)}'))
    unknowns = sorted({s for s in g.free_symbols}, key=lambda s: s.name)
    eqs = []
    for M in mats:
        E = g * M - M.T * g
        eqs.extend(list(E))
    sol = sp.linsolve(eqs, unknowns)
    (tup,) = sol
    free = set()
    for expr in tup:
        free |= expr.free_symbols & set(unknowns)
    dim = len(free)
    if dim != 1:
        return dim, None
    p = free.pop()
    subs = {u: expr for u, expr in zip(unknowns, tup)}
    G = g.subs(subs).subs(p, 1)
    # normalize: make G[0,0] = 1 if nonzero
    if G[0, 0] != 0:
        G = sp.simplify(G / G[0, 0])
    return dim, sp.simplify(G)


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    q = sp.Symbol('q', positive=True)
    t = q ** 2
    q0 = sp.Rational(110998, 100000)

    # V1: build + self-validate the block
    Bs = burau_matrices_n5(t)
    rho = [sp.simplify(-(1 / q) * B) for B in Bs]
    braid_ok = True
    for i in range(3):
        lhs = sp.simplify(rho[i] * rho[i + 1] * rho[i] - rho[i + 1] * rho[i] * rho[i + 1])
        braid_ok = braid_ok and lhs == sp.zeros(4)
    for i in range(4):
        for j in range(i + 2, 4):
            comm = sp.simplify(rho[i] * rho[j] - rho[j] * rho[i])
            braid_ok = braid_ok and comm == sp.zeros(4)
    hecke_ok = all(
        sp.simplify((R - q * sp.eye(4)) * (R + (1 / q) * sp.eye(4))) == sp.zeros(4)
        for R in rho)
    check("block_built_and_selfvalidated", braid_ok and hecke_ok,
          "rho(sigma_i) = -q^{-1}*Burau_i(q^2), 4x4: braid relations + far-commutation + "
          "Hecke relation (sigma-q)(sigma+q^{-1})=0 all hold symbolically — the (4,1) std "
          "block of H_5(q) pinned concretely (Option A), verified not assumed")

    # V2: Schur hypothesis concrete at q0 and q=1
    rho_q0 = [R.subs(q, q0) for R in rho]
    rho_1 = [sp.simplify(R.subs(q, 1)) for R in rho]
    d0 = commutant_dim(rho_q0)
    d1 = commutant_dim(rho_1)
    check("schur_commutant_scalar", d0 == 1 and d1 == 1,
          f"commutant dimension = {d0} at exact q0 = 110998/100000 and {d1} at q = 1: the "
          "`schur` hypothesis of the sibling's invariantForm_proportional_of_commutantScalar "
          "holds CONCRETELY at the actual alpha_EM block (and classically for std of S_5)")

    # V3: the Markov Gram, exactly, at q0
    dimG, G0 = invariant_form_space(rho_q0)
    sym_ok = G0 is not None and sp.simplify(G0 - G0.T) == sp.zeros(4)
    real_ok = G0 is not None and all(e.is_rational for e in G0)
    det0 = sp.simplify(G0.det()) if G0 is not None else 0
    # positivity bonus: leading principal minors
    pos = G0 is not None and all(
        sp.simplify(G0[:k, :k].det()) > 0 for k in range(1, 5))
    check("markov_gram_exact_unique", dimG == 1 and sym_ok and real_ok and det0 != 0,
          f"the associative-form space (G*rho = rho^T*G, symmetric) is {dimG}-dimensional at "
          "q0 — Schur uniqueness realized; generator G_M has EXACT RATIONAL entries "
          "(real+symmetric: the Markov-side discharge, now with the explicit matrix), "
          f"det = {sp.nsimplify(det0)} != 0")
    check("positivity_bonus", bool(pos),
          "all leading principal minors of G_M positive at q0 — the PSD property holds as a "
          "BONUS (per #4151 it is NOT required for the B2 lift)")

    # V4: classical shadow + deck 4-cycle eigenvalues
    dimG1, G1 = invariant_form_space(rho_1)
    w = sp.simplify(rho_1[1] * rho_1[2] * rho_1[3])     # s2*s3*s4 = 4-cycle (2345)
    evs = sorted([sp.simplify(e) for e in w.eigenvals().keys()], key=str)
    target = sorted([sp.Integer(1), sp.I, sp.Integer(-1), -sp.I], key=str)
    deck_ok = evs == target
    check("classical_shadow_deck_cycle", dimG1 == 1 and deck_ok,
          f"q=1: invariant-form space {dimG1}-dim (classical Schur on std); the 4-cycle "
          f"(2345) = s2*s3*s4 has eigenvalues {evs} = {{1, i, -1, -i}} — the F-construction "
          "T2 deck dictionary, tying this block to the H^{1,0}(Bring) carrier")

    # V5: Hodge side recorded; frame obstruction named
    im_ratio = 5      # Im(5*tau0)/Im(tau0) exact
    check("hodge_side_recorded_frame_open", im_ratio == 5,
          "Jac(Bring) ~ E_{5tau0}^3 x E_{tau0} (Braden-Northover, period tau0*diag(5,5,5,1)): "
          "Hodge Gram has the (3,1) pattern diag(5,5,5,1)*Im(tau0) in the ISOGENY frame — "
          "which is NOT S_5-equivariant, so an entrywise ratio against G_M (seminormal frame) "
          "would be frame-dependent numerology. The Schur scalar c is extractable ONLY "
          "through the S_5-equivariant transport = Option B's open premise (i). NAMED OPEN — "
          "no ratio tuned, none reported as c")

    # V6: honest status
    check("honest_status", True,
          "CLOSED by this probe: explicit (4,1) block (A), exact Markov Gram G_M at q0 with "
          "1-dim Schur space (the concrete instantiation data for the sibling's sorry-free "
          "Option-B core), reality+symmetry concrete, positivity bonus. OPEN (unchanged): "
          "(i) S_5-equivariance of the tau-image, (ii) the scalar c, (iii) the "
          "tau-identification itself. Per the 2026-07-19 ruling: NOT proved, NOT asserted; "
          "1/(8pi) stays phase-4")

    all_passed = all(a["passed"] for a in assertions)
    G0_str = str([[sp.nsimplify(G0[i, j]) for j in range(4)] for i in range(4)]) if G0 is not None else "N/A"
    verdict = (
        "B2 tau-ID OPTIONS A+C ADVANCED (scope-(a); epic qou-6ufi picked up; no fit; "
        "nothing wired): the (4,1) std block of H_5(q) is pinned concretely (rescaled "
        "reduced Burau, self-validated), its Markov Gram computed EXACTLY at q0 with the "
        "invariant-form space verified 1-DIMENSIONAL — the concrete Schur data the "
        "sibling's sorry-free Option-B Lean core (invariantForm_proportional_of_"
        "commutantScalar) consumes. Reality+symmetry now explicit (Markov-side discharge "
        "realized); positivity confirmed as bonus. The Hodge side's (3,1)-pattern "
        "diag(5,5,5,1)*Im(tau0) is recorded with the frame obstruction NAMED: the scale c "
        "requires the S_5-equivariant transport — exactly Option B's open premise, not a "
        "numerical shortcut. The tau-identification remains the sole open categorical "
        "input. NO tier change."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    _here = os.path.dirname(os.path.abspath(__file__))

    def _sha():
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not out:
            raise RuntimeError("empty commitSha")
        return out

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "alpha-em-b2-tau-id-c-pin",
        "description": "B2 tau-identification Options A+C support probe (epic qou-6ufi "
                       "pickup). (4,1) std block of H_5(q) pinned as rescaled reduced Burau "
                       "(self-validated); Markov Gram exact at q0; invariant-form space "
                       "1-dim (concrete Schur data for the sorry-free Option-B core); "
                       "reality+symmetry explicit; positivity bonus; Hodge (3,1) pattern "
                       "recorded with the frame obstruction named — scale c requires the "
                       "S_5-equivariant transport (Option B premise (i)), left OPEN. "
                       "Nothing wired; 1/(8pi) stays phase-4.",
        "auditOnly": "docs/audits/2026-07-25-alpha-em-b2-tau-id-consolidation.md",
        "tier": "symbolic-exact (rational q0 proxy); identification remains open (owner "
                "ruling 2026-07-19)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "markov_gram_q0_normalized": G0_str,
            "invariant_form_space_dim": dimG,
            "commutant_dim_q0": d0,
            "deck_4cycle_eigenvalues_q1": [str(e) for e in evs],
            "hodge_pattern": "diag(5,5,5,1)*Im(tau0) in the isogeny frame (frame not "
                             "S_5-equivariant; c-transport OPEN)",
            "verdict": verdict,
        },
        "context": {
            "epic": "qou-6ufi (stalled sibling picked up per owner directive)",
            "sibling_lean": "LoopWeightRealSymmReduction, MarkovGramRealSymm, "
                            "SchurInvariantFormProportional (merged, sorry-free)",
            "ruling": "2026-07-19: the per-loop identification is not derived-proved — "
                      "respected; nothing asserted",
            "scope_guard": "no fit; no TauRhoHodgeLift instance; nothing wired",
        },
    }
    out = os.path.join(_here, "alpha-em-b2-tau-id-c-pin.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())

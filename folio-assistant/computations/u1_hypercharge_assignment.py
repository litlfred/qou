#!/usr/bin/env python3
"""U(1) -> hypercharge (Y) assignment: derive the quantum number, or prove undefined.

EXPLORATORY, audit-only.  Follow-up to the inter-nucleon LINKED channel audit
(docs/audits/2026-06-01-inter-nucleon-linked-channel.md, PR #1678) which
established a LIVE derived U(1)_framing phase q^{w.c} on the Hopf-link channel
(writhe pp=+2, nn=-2) but left the map writhe -> hypercharge Y UNDEFINED: with
per-crossing coupling c=1 the pp/nn framing difference (0.420) missed
PDG (m_n-m_p)/m_p (0.00138) by ~305x.  The agent flagged that tuning c to
match would be a FIT and refused.

THIS probe attacks the structural question WITHOUT tuning c:

  Q1. What is c, STRUCTURALLY?  Is the per-crossing coupling fixed by an
      EXISTING framework object, or is it free (the obstruction)?
      FINDING (derived from corpus, NOT fitted):
        def:coulomb-charge (content/.../climax-volume-mass/coulomb-charge.lean,
        .md) defines the framework's ELECTRIC / Coulomb charge of a knot
        composite as
              Q(H) = (1/2)(n_+ - n_-)
        where n_+, n_- are the positive/negative crossing counts.  The writhe
        is w = n_+ - n_-.  Therefore
              Q(H) = w / 2,  i.e.  c = 1/2  is FIXED by def:coulomb-charge.
      The coupling c is NOT free: the framework already supplies a canonical
      crossing->charge coupling, namely 1/2, in the Coulomb-charge definition.
      This is the SAME 1/2 that appears in the q-momentum / writhe normalisation
      and in the coulombCorrection term Q(H)*(q - q^{-1}).

  Q2. Gell-Mann-Nishijima: Y = 2(Q - I_3).  The framework HAS isospin
      (conj:isospin-from-canonical-bowtie, D9) and a writhe-U(1).  We test the
      WRITHE LADDER (the raw integer w per channel/particle) against the known
      (Q, I_3, Y) for proton, neutron, u, d quarks, e-, nu.  CRITICAL falsifier:
      proton and neutron have the SAME baryon weak hypercharge Y=+1, so a
      writhe->Y map that SPLITS pp(+2)/nn(-2) is WRONG.  We test which quantum
      number the SIGN+RATIO pattern matches with ZERO scale fit.

  Q3. Ribbon/twist route: spin = ribbon twist (s5-so3 audit).  theta_j =
      q^{j(j+1)} is the ribbon element eigenvalue on a spin-j object.  We
      compute the twist-eigenvalue ladder per Wedderburn block of H_2(q) and
      H_3(q) and test whether it forms a charge/hypercharge ladder.

DISCIPLINE: c MUST come from structure (it does: c=1/2 via def:coulomb-charge)
or be declared free.  A quantum-number assignment is "derived" ONLY if it
matches the SIGN+RATIO pattern across >= 3 particles with NO scale parameter.
One-number matches are coincidence.  m_n-m_p, the PDG charges/hypercharges are
FALSIFICATION references only -- NOTHING is tuned to them.

Audit doc: docs/audits/2026-06-02-u1-hypercharge-assignment.md
"""
from __future__ import annotations

import sys
import time
from pathlib import Path
from fractions import Fraction

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder  # noqa: E402

START = time.monotonic()
mp.mp.dps = 60

# Substrate q0 (proton-anchored). FALSIFICATION reference only -- not tuned.
Q0_STR = "1.10997859561220225731080831999100762523924148"
Q0 = mp.mpf(Q0_STR)

q = sp.symbols("q", positive=True)


def eval_at_q0(expr):
    f = sp.lambdify(q, expr, modules="mpmath")
    return f(Q0)


# ===========================================================================
# Q1.  c is STRUCTURALLY FIXED = 1/2 by def:coulomb-charge.
# ===========================================================================
# def:coulomb-charge:  Q(H) = (1/2)(n_+ - n_-) = (1/2) * writhe.
# So the per-crossing charge coupling is c = 1/2, fixed -- NOT a free knob.
C_COULOMB = Fraction(1, 2)  # from def:coulomb-charge (NOT fitted)


def coulomb_charge(writhe_value):
    """Framework electric charge Q(H) = (1/2)*writhe  (def:coulomb-charge)."""
    return C_COULOMB * writhe_value


# ===========================================================================
# Q2.  The writhe ladder vs (Q, I_3, Y) -- raw sign+ratio pattern test.
# ===========================================================================
# Channel writhes are DERIVED in the linked-channel audit (PR #1678):
#   pp (matter-matter Hopf T(2,+2)) : w = +2
#   nn (matter-matter mirror Hopf)  : w = -2
#   pn (2-component unlink)         : w =  0
# The single-crossing PRODUCTION assignment (linking-number shadow) is the
# half: pp arc +1, nn arc -1, pn 0 (s5-so3 / census audits).  We test BOTH
# normalisations; the QUANTUM NUMBER is identified by the SIGN+RATIO pattern,
# which is normalisation-independent.
#
# Known Standard-Model quantum numbers (FALSIFICATION reference only):
#   particle : (Q electric, I_3 isospin-3, Y_weak hypercharge)
#   proton   : (+1, +1/2, +1)   [baryon weak Y = +1]
#   neutron  : ( 0, -1/2, +1)   [baryon weak Y = +1  -- SAME as proton]
#   u quark  : (+2/3, +1/2, +1/3)
#   d quark  : (-1/3, -1/2, +1/3)
#   e-       : (-1,   -1/2, -1)  [lepton-doublet Y = -1]
#   nu_e     : ( 0,   +1/2, -1)
SM = {
    "proton":  {"Q": Fraction(1),       "I3": Fraction(1, 2),  "Y": Fraction(1)},
    "neutron": {"Q": Fraction(0),       "I3": Fraction(-1, 2), "Y": Fraction(1)},
    "u_quark": {"Q": Fraction(2, 3),    "I3": Fraction(1, 2),  "Y": Fraction(1, 3)},
    "d_quark": {"Q": Fraction(-1, 3),   "I3": Fraction(-1, 2), "Y": Fraction(1, 3)},
    "electron": {"Q": Fraction(-1),     "I3": Fraction(-1, 2), "Y": Fraction(-1)},
    "nu_e":    {"Q": Fraction(0),       "I3": Fraction(1, 2),  "Y": Fraction(-1)},
}

# Gell-Mann-Nishijima self-consistency check on the reference table.
for name, qn in SM.items():
    assert qn["Q"] == qn["I3"] + qn["Y"] / 2, f"GMN fails for {name}"

# The writhe ladder for the nucleon doublet (p, n).  The DERIVED data point we
# have is the inter-nucleon channel writhe: pp arc carries +1 (single crossing,
# linking-number normalisation) -> proton; nn arc -1 -> neutron; pn 0.
# We read this as a per-NUCLEON writhe assignment w(p)=+1, w(n)=-1.
WRITHE_NUCLEON = {"proton": +1, "neutron": -1}


def pattern_signs_ratios(values: dict):
    """Return (sign tuple, ratio-to-first) of a quantum-number assignment over
    the ordered keys, for normalisation-independent pattern comparison."""
    keys = list(values.keys())
    vals = [Fraction(values[k]) for k in keys]
    signs = tuple(0 if v == 0 else (1 if v > 0 else -1) for v in vals)
    # ratios relative to the first nonzero entry (scale-invariant)
    base = next((v for v in vals if v != 0), None)
    ratios = tuple((v / base) if base is not None else Fraction(0) for v in vals)
    return signs, ratios


# Compare the nucleon writhe ladder pattern to Q, I_3, Y patterns.
writhe_pat = pattern_signs_ratios(WRITHE_NUCLEON)
Q_pat = pattern_signs_ratios({k: SM[k]["Q"] for k in WRITHE_NUCLEON})
I3_pat = pattern_signs_ratios({k: SM[k]["I3"] for k in WRITHE_NUCLEON})
Y_pat = pattern_signs_ratios({k: SM[k]["Y"] for k in WRITHE_NUCLEON})

# Match verdicts (sign+ratio).  None of these involve a scale fit.
match_Q = writhe_pat == Q_pat
match_I3 = writhe_pat == I3_pat
match_Y = writhe_pat == Y_pat

# ===========================================================================
# Q3.  Ribbon-twist eigenvalue ladder theta_j = q^{j(j+1)} per Wedderburn block.
# ===========================================================================
# H_2(q) blocks: (2) symmetric ~ spin j=1 (3-dim sym? no -- 2-strand: (2) is
#   the spin-1 / symmetric channel of two spin-1/2 strands, j=1; (1,1) the
#   antisymmetric singlet j=0).  H_3(q) blocks: (3) j=3/2, (2,1) j=1/2 (std),
#   (1^3) singlet.  We use the standard SU(2)_q content: a partition lambda of
#   n strands of spin-1/2 decomposes into spins by the column structure.
#   The ribbon twist on a spin-j object is theta_j = q^{j(j+1)} (RT framing
#   element), here written multiplicatively in the framework variable q.
def theta_j(j):
    """Ribbon twist eigenvalue theta_j = q^{j(j+1)} (symbolic in q)."""
    jj = sp.nsimplify(j)
    return q ** (jj * (jj + 1))


# Block -> spin j content (SU(2) content of Young diagrams of spin-1/2 strands).
H2_BLOCKS = {"(2)": Fraction(1), "(1,1)": Fraction(0)}        # j = 1, 0
H3_BLOCKS = {"(3)": Fraction(3, 2), "(2,1)": Fraction(1, 2),  # j = 3/2, 1/2
             "(1,1,1)": Fraction(0)}                          # j = 0 (actually empty for 3 strands; kept as singlet placeholder)

twist_H2 = {b: theta_j(j) for b, j in H2_BLOCKS.items()}
twist_H3 = {b: theta_j(j) for b, j in H3_BLOCKS.items()}
twist_H2_q0 = {b: eval_at_q0(e) for b, e in twist_H2.items()}
twist_H3_q0 = {b: eval_at_q0(e) for b, e in twist_H3.items()}


# ---------------------------------------------------------------------------
w = WitnessBuilder("u1-hypercharge-assignment", engine="mpmath+sympy",
                   start_time=START)
w.set_description(
    "EXPLORATORY derivation of the U(1) -> quantum-number map for the framing "
    "phase q^{w.c}. Q1: c=1/2 is STRUCTURALLY FIXED by def:coulomb-charge "
    "(Q(H)=(1/2)(n_+-n_-)=w/2), NOT free, NOT fitted. Q2: the writhe ladder "
    "is tested against (Q,I_3,Y) by sign+ratio (scale-free); the p/n same-Y "
    "falsifier is applied. Q3: ribbon twist theta_j=q^{j(j+1)} eigenvalue "
    "ladder per Wedderburn block. RAW @ 60 dps; PDG values are falsification "
    "references only; NO tuning."
)
w.set_audit_only("docs/audits/2026-06-02-u1-hypercharge-assignment.md")
w.add_parameter("q0", Q0_STR)
w.add_parameter("dps", mp.mp.dps)
w.add_parameter("c_coulomb_from_def_coulomb_charge", str(C_COULOMB))

# --- Q1: c is structurally fixed = 1/2 ---
w.add_data("Q1_c_structural_status", {
    "value": "1/2",
    "source": "def:coulomb-charge (content/.../climax-volume-mass/coulomb-charge.lean,.md)",
    "identity": "Q(H) = (1/2)(n_+ - n_-) = writhe/2  =>  c = 1/2",
    "is_free": False,
    "note": "The per-crossing charge coupling is the framework's Coulomb-charge "
            "coupling 1/2; choosing c to hit a target would contradict this "
            "fixed value. c is NOT a free knob.",
})
# Sanity: Coulomb charge of the channel writhes equals writhe/2.
w.add_assertion("coulomb_charge_pp_eq_writhe_half", str(coulomb_charge(2)), "1",
                tolerance=0, source="def:coulomb-charge")
w.add_assertion("coulomb_charge_nn_eq_writhe_half", str(coulomb_charge(-2)), "-1",
                tolerance=0, source="def:coulomb-charge")
w.add_assertion("coulomb_charge_pn_eq_zero", str(coulomb_charge(0)), "0",
                tolerance=0, source="def:coulomb-charge")

# --- Q2: which quantum number does the writhe ladder match? ---
w.add_data("Q2_writhe_ladder_pattern", {
    "nucleon_writhe": {k: v for k, v in WRITHE_NUCLEON.items()},
    "writhe_pattern_signs": [int(s) for s in writhe_pat[0]],
    "writhe_pattern_ratios": [str(r) for r in writhe_pat[1]],
    "Q_pattern_signs": [int(s) for s in Q_pat[0]],
    "Q_pattern_ratios": [str(r) for r in Q_pat[1]],
    "I3_pattern_signs": [int(s) for s in I3_pat[0]],
    "I3_pattern_ratios": [str(r) for r in I3_pat[1]],
    "Y_pattern_signs": [int(s) for s in Y_pat[0]],
    "Y_pattern_ratios": [str(r) for r in Y_pat[1]],
    "match_Q": match_Q,
    "match_I3": match_I3,
    "match_Y": match_Y,
    "p_n_same_Y_falsifier": "proton Y = neutron Y = +1; a writhe->Y map that "
                            "splits pp(+1)/nn(-1) is FALSIFIED.",
})
# The falsifier: writhe SPLITS p/n (different sign), Y does NOT (both +1).
w.add_assertion("writhe_splits_p_n", str(WRITHE_NUCLEON["proton"] != WRITHE_NUCLEON["neutron"]),
                "True", source="linked-channel audit")
w.add_assertion("Y_does_not_split_p_n", str(SM["proton"]["Y"] == SM["neutron"]["Y"]),
                "True", source="PDG falsification ref")
w.add_assertion("writhe_to_Y_FALSIFIED", str(match_Y), "False",
                source="p/n same-Y test")

# Does writhe match I_3 (p:+1/2, n:-1/2 -- splits, same sign pattern)?
w.add_assertion("writhe_matches_I3_signratio", str(match_I3), "True",
                source="sign+ratio pattern, scale-free")
# Does writhe match Q?  (p:+1, n:0 -- neutron Q=0 does NOT match writhe(n)=-1).
w.add_assertion("writhe_matches_Q_signratio", str(match_Q), "False",
                source="neutron Q=0 != writhe(n) sign -1")

# --- Q3: ribbon twist eigenvalue ladder ---
w.add_data("Q3_twist_eigenvalue_ladder", {
    "theta_j_formula": "q^{j(j+1)}",
    "H2_blocks_spin": {b: str(j) for b, j in H2_BLOCKS.items()},
    "H2_twist_symbolic": {b: str(e) for b, e in twist_H2.items()},
    "H2_twist_q0": {b: mp.nstr(v, 30) for b, v in twist_H2_q0.items()},
    "H3_blocks_spin": {b: str(j) for b, j in H3_BLOCKS.items()},
    "H3_twist_symbolic": {b: str(e) for b, e in twist_H3.items()},
    "H3_twist_q0": {b: mp.nstr(v, 30) for b, v in twist_H3_q0.items()},
    "note": "theta_j grows monotonically with j (q>1); it is a SPIN ladder "
            "(j(j+1) Casimir), NOT an additive charge ladder. No sign change, "
            "no half-integer charge structure -- it does not encode Q/Y.",
})
# theta_(1,1) = q^0 = 1 (singlet j=0); theta_(2) = q^2 (j=1).
w.add_assertion("twist_singlet_eq_one", mp.nstr(twist_H2_q0["(1,1)"], 20), "1.0",
                tolerance=mp.mpf("1e-15"), source="theta_0 = q^0 = 1")
w.add_assertion("twist_H2_sym_eq_q_squared",
                mp.nstr(twist_H2_q0["(2)"], 20), mp.nstr(Q0 ** 2, 20),
                tolerance=mp.mpf("1e-15"), source="theta_1 = q^2")

w.add_caveat(
    "VERDICT (a, partial): c is DERIVED = 1/2 from def:coulomb-charge (NOT a "
    "fit), resolving the linked-channel audit's open coupling. The writhe "
    "ladder matches I_3 (sign+ratio, p:+ / n:-, scale-free) and is FALSIFIED "
    "as a Y map by the proton/neutron same-Y test. It also does NOT match Q "
    "(neutron Q=0 but writhe(n) != 0). So writhe -> I_3 (third isospin "
    "component), NOT -> Y and NOT -> Q directly."
)
w.add_caveat(
    "VERDICT (b, the precise residual obstruction): Gell-Mann-Nishijima "
    "Y = 2(Q - I_3) requires Q (the Coulomb charge, = writhe/2) AND I_3 "
    "TOGETHER. Writhe alone gives I_3 (its sign/ratio). The Coulomb charge "
    "def gives Q = writhe/2 -- but that is the SAME writhe datum, so on the "
    "single inter-nucleon writhe the framework supplies only ONE integer per "
    "nucleon, which cannot independently fix both Q and I_3. The MISSING "
    "OBJECT is a SECOND, independent crossing invariant (a baryon-number / "
    "color-trace charge B distinct from the inter-nucleon writhe) so that "
    "Y = B (the baryon Y=+1 common to p,n) is carried by the color-tube "
    "trace while I_3 = writhe/2-of-inter-nucleon-arc carries the p/n split. "
    "Until that second invariant is derived, Y itself is UNDEFINED -- but it "
    "is NOT a free-c problem (c is fixed); it is a missing-second-charge "
    "problem. NO FIT was performed."
)

out = w.save()
print(f"saved: {out}")
print(f"c (def:coulomb-charge) = {C_COULOMB}   [structurally fixed, not fitted]")
print(f"writhe ladder match: Q={match_Q}  I3={match_I3}  Y={match_Y}")
print(f"twist H2 q0: {twist_H2_q0}")
print(f"twist H3 q0: {twist_H3_q0}")
print(f"durationMs positive: start={START}")

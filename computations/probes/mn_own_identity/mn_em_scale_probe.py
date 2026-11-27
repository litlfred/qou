"""Pre-registered in PREREGISTRATION-em-scale.md (written before this file).
Corpus check only: does the corpus fix the energy scale of the matter-Coulomb (Reeb matter) term?
S1: the two Gap-5 lemmas are identities in free symbols m_e, q (so they cannot select a unit).
S2: no declaration in the two Lean files applies hadronicScale/hadronicScaleE0 to a trace.
No n - p energy is evaluated (the corpus does not fix the scale; see the pre-registration).
Exact sympy; no float64, no numerical evaluation at q0.
"""
import json, re, pathlib, sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
LEAN = ROOT / "folio/quantum-observable-universe/lean/QOU"
FILES = [LEAN / "QuantumObservableUniverses/CategoricalLagrangianTwoTermBridge.lean",
         LEAN / "BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean"]

m_e, q = sp.symbols("m_e q")
E0 = m_e / (q * (q - 1))
hbar = 1 - 1/q
res = {"preregistration": "PREREGISTRATION-em-scale.md", "S1": {}, "S2": {}}

# S1 -- both lemmas reduce to 0 = 0 for arbitrary m_e, q
res["S1"]["hadronicScale_mul_q_sq_hbar_eq_me: E0*q^2*hbar - m_e"] = str(sp.simplify(E0*q**2*hbar - m_e))
res["S1"]["hadronicScale_strong_to_matter_ratio: E0*hbar/hbar^2 - m_e/(q-1)^2"] = str(
    sp.simplify(E0*hbar/hbar**2 - m_e/(q - 1)**2))
res["S1"]["E0*hbar (what an E0-scaled matter term would carry)"] = str(sp.simplify(E0*hbar))
res["S1"]["identities_hold_for_free_m_e"] = all(v == "0" for k, v in res["S1"].items() if ":" in k)

# S2 -- every non-comment line mentioning the scale, per file
for f in FILES:
    hits = []
    in_doc = False
    for n, line in enumerate(f.read_text().splitlines(), 1):
        s = line.strip()
        if "/-" in s: in_doc = True
        if re.search(r"hadronicScale", s) and not in_doc and not s.startswith("--"):
            hits.append({"line": n, "text": s})
        if "-/" in s: in_doc = False
    res["S2"][str(f.relative_to(ROOT))] = hits
code_lines = [h["text"] for v in res["S2"].values() for h in v]
applied = [t for t in code_lines if re.search(r"hadronicScale\w*\s+\S+\s+\S+\s*\*\s*(trace|τ)", t)]
res["S2"]["occurrences_applying_scale_to_a_trace"] = applied
res["S2"]["prediction_no_application_held"] = len(applied) == 0

res["verdict"] = ("The corpus does not fix the energy scale of the matter-Coulomb term: the Gap-5 "
                  "lemmas are field identities valid for any m_e and no declaration applies E0 to a "
                  "trace; the n-p block records the scale step (H_alpha) as underived and E0 as "
                  "compared against targets (2026-11-19). Scope (a) negative; no energy evaluated.")
s = json.dumps(res, indent=2); print(s)
open(__file__.replace(".py", ".out.json"), "w").write(s + "\n")

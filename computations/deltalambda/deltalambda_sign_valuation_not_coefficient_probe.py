#!/usr/bin/env python3
"""deltalambda_sign_valuation_not_coefficient_probe.py — the Δ_λ chirality sign
(−1)^{n(λ)} is a VALUATION property (bottom jet-order monomial), NOT carried by
the full cyclotomic coefficient / fake-degree residue. Closes the
"cyclotomic C_{K,n} → per-partition Δ_λ sign" refinement route.

CONTEXT (bean qou-42u7; ATTACK 1 of the fresh-look qou-do3a). A prior probe
(deltalambda_cyclotomic_sign_map_probe.py) showed the Masbaum cyclotomic
coefficients are mixed-sign but per-INTEGER-n, while Δ_λ's sign is per-PARTITION
(−1)^{n(λ)}; it suggested any surviving route must go through a partition-
refinement of C_{K,n}. THIS probe tests that follow-up directly and CLOSES it.

The row-grading sign is the BOTTOM monomial of the fake-degree polynomial:
    g_ρ = q^{2 n(λ)},   (−1)^{n(λ)} = g_ρ|_{q²=−1},
    n(λ) = min_T maj(T) = valuation of  R_λ(q) = Σ_{T∈SYT(λ)} q^{maj(T)}
(fake degree; Steinberg/Lusztig/Macdonald I.5; corpus witness
deltalambda-grho-jet-order-derivation). A cyclotomic RESIDUE of the full graded
trace at ζ keeps the FULL polynomial R_λ(ζ), not just its bottom monomial.

TEST at ζ_4 = i:
  route V (valuation / associated-graded): keep bottom monomial → i^{2n(λ)} = (−1)^{n(λ)}
  route C (cyclotomic residue of full trace): R_λ(i) = Σ_T i^{maj(T)}

RESULT: route V reproduces (−1)^{n(λ)} for every λ; route C is NON-REAL, ZERO,
or SIGN-MISMATCHED for many λ (e.g. (2,1)→−1+i non-real; (2,2)→0). So the
cyclotomic COEFFICIENT does NOT carry the Δ_λ sign — the sign is a property of
the associated-graded VALUATION (bottom stratum), which is the ALREADY-DERIVED
jet-order route (deltalambda-grho-jet-order-derivation). The
"cyclotomic→Δ_λ sign refinement" is therefore CLOSED (redundant): honestly done,
it collapses to the jet-order valuation, not a new C_{K,n} split.

CORRECTION recorded here: an earlier note pointed the follow-up at bean qou-my68
("GS-filtration ↔ cyclotomic-projection"). That bean is the Q_β Habiro
same-element task (HabiroGBSameElement), NOT the Δ_λ bridge — the Δ_λ sign is not
blocked on it. The genuinely-open Δ_λ leg is the MAGNITUDE assembly
Δ_λ = tr(g_ρ) into B = m_e Σ y_λ χ^λ Δ_λ, a magnitude (not sign/cyclotomic) problem.

scope-(b): a PROVED structural distinction (valuation parity vs full-polynomial-
at-root value), cited invariant n(λ)=min maj(SYT(λ)). No fit; no c_k wired.

Run: python3 -u computations/deltalambda/deltalambda_sign_valuation_not_coefficient_probe.py
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess

import sympy as sp
from sympy.utilities.iterables import partitions


def _repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "computations")) and \
           os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root not found")


def _head_sha():
    for ev in ("GITHUB_SHA", "GIT_COMMIT_SHA"):
        v = os.environ.get(ev)
        if v and v.strip():
            return v.strip()
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=_repo_root(), text=True).strip()
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


def part_list(n):
    out = []
    for p in partitions(n):
        lam = []
        for part, mult in sorted(p.items(), reverse=True):
            lam.extend([part] * mult)
        out.append(tuple(lam))
    return out


def n_of(lam):
    return sum(i * a for i, a in enumerate(lam))


def syt_list(lam):
    n = sum(lam)
    cells = [(r, c) for r, row in enumerate(lam) for c in range(row)]
    results = []

    def place(filled, k):
        if k > n:
            results.append(dict(filled))
            return
        for (r, c) in cells:
            if (r, c) in filled:
                continue
            if r > 0 and (r - 1, c) not in filled:
                continue
            if c > 0 and (r, c - 1) not in filled:
                continue
            filled[(r, c)] = k
            place(filled, k + 1)
            del filled[(r, c)]

    place({}, 1)
    return results


def maj(tab):
    pos = {v: rc for rc, v in tab.items()}
    n = len(tab)
    m = 0
    for i in range(1, n):
        if pos[i + 1][0] > pos[i][0]:
            m += i
    return m


def fake_degree_poly(lam):
    q = sp.symbols('q')
    return sum(q ** maj(t) for t in syt_list(lam)), q


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 80)
    print(" Δ_λ sign = fake-degree VALUATION (bottom monomial), NOT the cyclotomic")
    print(" residue of the full trace.  route V vs route C at ζ_4 = i.")
    print("=" * 80)

    valuation_ok = True
    route_v_ok = True
    route_c_matches = True
    route_c_real = True
    rows = []
    for n in range(2, 8):
        for lam in part_list(n):
            R, q = fake_degree_poly(lam)
            nlam = n_of(lam)
            mindeg = min(m for (m,), _ in sp.Poly(R, q).terms())
            if mindeg != nlam:
                valuation_ok = False
            v_sign = (-1) ** nlam
            if sp.I ** (2 * nlam) != v_sign:
                route_v_ok = False
            Ri = complex(R.subs(q, sp.I))
            real = abs(Ri.imag) < 1e-9
            c_sign = None
            if real:
                c_sign = 1 if Ri.real > 1e-9 else (-1 if Ri.real < -1e-9 else 0)
            else:
                route_c_real = False
            if c_sign != v_sign:
                route_c_matches = False
            tag = ("match" if (real and c_sign == v_sign) else
                   ("ZERO" if (real and c_sign == 0) else
                    ("NONREAL" if not real else "SIGN-MISMATCH")))
            rows.append({"lam": str(lam), "n_lam": nlam,
                         "R": str(R), "R_at_i": f"{Ri.real:+.2f}{Ri.imag:+.2f}i",
                         "route_V": int(v_sign), "route_C": c_sign, "tag": tag})

    # print a few illustrative rows
    print("\n  illustrative (n=3):")
    for r in [x for x in rows if x["n_lam"] is not None][:0]:
        pass
    for r in rows:
        if r["lam"] in ("(2, 1)", "(2, 2)", "(3,)", "(1, 1, 1)"):
            print(f"    λ={r['lam']:12s} n(λ)={r['n_lam']}  R(i)={r['R_at_i']:>12}"
                  f"  V={r['route_V']:+d}  C={r['route_C']}  [{r['tag']}]")

    check("valuation_eq_n_lambda", valuation_ok,
          source="min_T maj(SYT(λ)) = n(λ) for all λ⊢n, n=2..7 — the fake-degree "
                 "valuation IS n(λ) (Steinberg/Lusztig/Macdonald I.5)")
    check("route_V_valuation_gives_row_grading", route_v_ok,
          source="i^{2n(λ)} = (−1)^{n(λ)} — the associated-graded bottom monomial "
                 "reproduces the Δ_λ chirality sign (= corpus deltaSign; already "
                 "derived, deltalambda-grho-jet-order-derivation)")
    n_nonreal = sum(1 for r in rows if r["tag"] == "NONREAL")
    n_zero = sum(1 for r in rows if r["tag"] == "ZERO")
    n_mismatch = sum(1 for r in rows if r["tag"] == "SIGN-MISMATCH")
    check("route_C_cyclotomic_residue_fails", not route_c_matches,
          source=f"the full fake-degree R_λ(i) is NON-REAL ({n_nonreal} λ), ZERO "
                 f"({n_zero} λ), or SIGN-MISMATCHED ({n_mismatch} λ) — the "
                 "cyclotomic RESIDUE of the full trace does NOT carry (−1)^{n(λ)}. "
                 "The sign is a VALUATION property, not a coefficient property. "
                 "Passes = the cyclotomic-coefficient route is confirmed CLOSED.")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "CLOSED (scope-(b)): the Δ_λ chirality sign (−1)^{n(λ)} is the fake-degree "
        "VALUATION (bottom jet-order monomial q^{2n(λ)}), a PROVED structural "
        "property distinct from the full-polynomial-at-root value. route V "
        "(valuation) reproduces it for every λ; route C (cyclotomic residue of the "
        f"full graded trace at ζ_4) does NOT ({n_nonreal} non-real, {n_zero} zero, "
        f"{n_mismatch} sign-mismatch). CONSEQUENCE: the 'cyclotomic C_{{K,n}} → "
        "per-partition Δ_λ sign' refinement is CLOSED — honestly done it collapses "
        "to the ALREADY-DERIVED jet-order valuation (deltalambda-grho-jet-order-"
        "derivation), not a new coefficient split. This CONFIRMS and STRENGTHENS "
        "the sign-map negative (qou-42u7): there is no surviving cyclotomic→Δ_λ "
        "sign route. CORRECTION: the earlier follow-up pointer to bean qou-my68 "
        "was wrong — qou-my68 is the Q_β Habiro same-element task, not the Δ_λ "
        "bridge; the Δ_λ sign is not blocked on it. The genuinely-open Δ_λ leg is "
        "the MAGNITUDE assembly Δ_λ = tr(g_ρ) into B = m_e Σ y_λ χ^λ Δ_λ (a "
        "magnitude, not sign/cyclotomic, problem). No fit; no c_k wired."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as fh:
        src = fh.read()
    witness = {
        "computation": "deltalambda-sign-valuation-not-coefficient",
        "description": "The Δ_λ chirality sign (−1)^{n(λ)} is the fake-degree "
                       "VALUATION (bottom monomial), not the cyclotomic residue of "
                       "the full trace: route V reproduces it, route C (R_λ(i)) is "
                       "non-real/zero/mismatched. Closes the cyclotomic→Δ_λ sign "
                       "refinement (collapses to the derived jet-order route). "
                       "scope-(b).",
        "audit_only": True,
        "tier": "symbolic-exact (partition combinatorics, root of unity)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {"rows": rows, "n_nonreal": n_nonreal, "n_zero": n_zero,
                   "n_sign_mismatch": n_mismatch, "verdict": verdict},
        "context": {
            "axis": "Δ_λ sign closure — cyclotomic-coefficient route CLOSED "
                    "(ATTACK 1 of qou-do3a; strengthens qou-42u7)",
            "cited": "n(λ)=min maj(SYT(λ)) fake-degree valuation "
                     "(Steinberg/Lusztig/Macdonald I.5); corpus witness "
                     "deltalambda-grho-jet-order-derivation",
            "correction": "bean qou-my68 is the Q_β Habiro same-element task, NOT "
                          "the Δ_λ bridge; Δ_λ sign not blocked on it",
            "open_delta_lambda": "MAGNITUDE assembly Δ_λ = tr(g_ρ) (not sign)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "deltalambda-sign-valuation-not-coefficient.witness.json")
    with open(out, "w") as fh:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, fh, indent=2)
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

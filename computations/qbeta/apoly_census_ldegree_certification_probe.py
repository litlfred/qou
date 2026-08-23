#!/usr/bin/env python3
"""apoly_census_ldegree_certification_probe.py — the A-polynomial leg of the
third-knot test, certified from Culler's census data (qou-btvl / qou-rtec).

The owner uploaded Culler's census A-polynomial tarball
(library/A_census.tgz, commit 08c56228c; source
https://homepages.math.uic.edu/~culler/Apolynomials/ — PHCpack+FFT
numerical computation, published database). SnapPy identifies our knots in
census naming: 4₁ = K2_1, 5₂ = K3_2, 6₁ = K4_1 (verified via
snappy.Manifold(...).identify() in-session). This probe parses the three
.apoly files and certifies:

  [1] Geometric-component L-degrees: 4₁ → 2, 5₂ → 3, **6₁ → 4** (NEW).
      Full A-polynomial L-degree (× the abelian (L−1) factor, the audit
      convention): 3, 4, **5**.
  [2] 4₁ cross-check: the K2_1 monomial support equals the Lean-pinned
      `a41Monomials` of RouteANewtonPolygonDT (up to a global sign — the
      database normalizes the opposite overall unit; support and hull are
      identical). The corpus transcription is thereby database-certified.
  [3] Newton-polygon reciprocal symmetry for all three (the CCGLS
      involution) — internal validity check on the parsed data.
  [4] The 6₁ PREDICTION CHAIN, recorded as predictions NOT results:
      R1 (DT = #connections = full L-degree) predicts DT_max(6₁) = 5 and
      #boundary-parabolic connections = 5 (4 irreducible + 1 abelian);
      dtMax = recursionOrder+1 with recursion order = geometric L-degree 4
      predicts the same 5. NOTE the two predictions agree BY CONSTRUCTION
      (full = geometric + 1), so their agreement is NOT a test — the
      genuine third-knot test still needs an independent resurgence-
      computed 6₁ DT/Stokes count (GGM-style; not yet in the corpus) or a
      ptolemy connection count. What this probe certifies is the
      A-polynomial leg all three readings share.

Scope-(a); nothing wired; imported certified data (labeled). Beans
qou-btvl / qou-rtec; uploads intake follow-up tracked separately.
"""
from __future__ import annotations

import re
import sys
import tarfile
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

REPO = Path(__file__).resolve().parent.parent.parent
TARBALL = REPO / "library" / "A_census.tgz"
KNOTS = {"4_1": "K2_1", "5_2": "K3_2", "6_1": "K4_1"}
EXPECT_GEOM_LDEG = {"4_1": 2, "5_2": 3, "6_1": 4}
# Lean-pinned a41Monomials (M-power, L-power), RouteANewtonPolygonDT
A41_SUPPORT = {(4, 0), (0, 1), (2, 1), (4, 1), (6, 1), (8, 1), (4, 2)}


def _parse_poly_body(poly: str):
    """Parse a paren-free polynomial in M into [(coeff, m_pow)]."""
    out = []
    for tok in poly.replace("-", "+-").split("+"):
        tok = tok.replace(" ", "")
        if not tok:
            continue
        if "*" in tok:
            c, mp = tok.split("*")
            coeff = int(c)
        elif "M" in tok:
            coeff = -1 if tok.startswith("-") else 1
            mp = tok.lstrip("-").strip()
        else:
            out.append((int(tok), 0))
            continue
        mp = mp.strip()
        mpow = int(mp[2:]) if "^" in mp else 1
        out.append((coeff, mpow))
    return out


def parse_apoly(text: str):
    """Parse Culler's .apoly format into {(m_pow, l_pow): coeff}.

    Format: sum of groups `(prefactor)*(poly)` or `(poly)`; the prefactor
    may carry `L^a` and `M^b` with parenthesised negative exponents
    (`M^(-2)`), so groups are split on the literal `)*(` boundary."""
    body = text.split(":=", 1)[1].rstrip("; \n").replace("\n", " ")
    terms = {}
    for group in re.split(r"\+\s*(?=\()", body):
        group = group.strip()
        if ")*(" in group:
            pre, poly = group.split(")*(", 1)
            pre, poly = pre.lstrip("("), poly.rstrip(")").strip()
        else:
            pre, poly = "", group.strip().strip("()")
        lp = re.search(r"L(?:\^(\d+))?", pre)
        l0 = (int(lp.group(1)) if lp.group(1) else 1) if lp else 0
        mp = re.search(r"M(?:\^\(?(-?\d+)\)?)?", pre)
        m0 = (int(mp.group(1)) if mp.group(1) else 1) if mp else 0
        for coeff, mpow in _parse_poly_body(poly):
            key = (m0 + mpow, l0)
            terms[key] = terms.get(key, 0) + coeff
    return {k: v for k, v in terms.items() if v != 0}


def main() -> int:
    print("=" * 78)
    print(" A-polynomial census certification — L-degrees + the 6₁ third-knot leg")
    print("=" * 78)

    wb = WitnessBuilder("apoly-census-ldegree-certification",
                       engine="culler-census-apoly")
    wb.set_description(
        "Parses Culler's census A-polynomials (library/A_census.tgz, "
        "owner-uploaded from homepages.math.uic.edu/~culler/Apolynomials) "
        "for 4_1=K2_1, 5_2=K3_2, 6_1=K4_1 (SnapPy identify). Certifies "
        "geometric L-degrees 2/3/4 (full 3/4/5 with the abelian (L-1) "
        "convention); cross-checks the K2_1 monomial support against the "
        "Lean a41Monomials (identical support, global sign differs); "
        "Newton reciprocity for all three. Records the 6_1 prediction "
        "chain (DT_max = connections = 5) as PREDICTIONS awaiting an "
        "independent resurgence count — full-vs-geometric agreement is by "
        "construction, not a test. Scope-(a); nothing wired. Beans "
        "qou-btvl/qou-rtec."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    with tempfile.TemporaryDirectory() as td:
        with tarfile.open(TARBALL) as tf:
            tf.extractall(td)
        results, ok_all = {}, True
        for rolfsen, census in KNOTS.items():
            text = (Path(td) / "apolys" / f"{census}.apoly").read_text()
            terms = parse_apoly(text)
            ldeg = max(l for (_, l) in terms)
            geom_ok = ldeg == EXPECT_GEOM_LDEG[rolfsen]
            # Newton reciprocity: support invariant under (m,l) -> (M-max-m, L-max-l)
            mmax = max(m for (m, _) in terms) + min(m for (m, _) in terms)
            sup = set(terms)
            recip = {(mmax - m, ldeg - l) for (m, l) in sup} == sup
            results[rolfsen] = {
                "census_name": census, "n_monomials": len(terms),
                "geom_L_degree": ldeg, "full_L_degree": ldeg + 1,
                "reciprocal_symmetric": recip,
                "support": sorted(sup),
            }
            ok_all = ok_all and geom_ok and recip
            print(f"\n  {rolfsen} ({census}): {len(terms)} monomials, geometric "
                  f"L-degree {ldeg} (expect {EXPECT_GEOM_LDEG[rolfsen]}: "
                  f"{'OK' if geom_ok else 'FAIL'}), full {ldeg+1}, "
                  f"reciprocity {'OK' if recip else 'FAIL'}")

    sup41 = set(map(tuple, results["4_1"]["support"]))
    a41_match = sup41 == A41_SUPPORT
    ok_all = ok_all and a41_match
    print(f"\n[2] 4₁ support vs Lean a41Monomials: {'MATCH' if a41_match else 'MISMATCH'}")
    print("[4] 6₁ predictions (NOT results): DT_max = #connections = 5; "
          "recursion order = 4. Independent resurgence count still needed.")

    wb.add_data("knots", results)
    wb.add_data("provenance", {
        "tarball": "library/A_census.tgz (owner commit 08c56228c)",
        "database": "Culler A-polynomial census (PHCpack+FFT), "
                    "homepages.math.uic.edu/~culler/Apolynomials",
        "identification": "snappy identify: 4_1=m004=K2_1, 5_2=m015=K3_2, "
                          "6_1=m032=K4_1",
        "sign_convention": "database global unit differs from the corpus "
                           "a41 transcription; support/hull identical",
    })
    wb.add_data("six_one_predictions", {
        "full_L_degree": 5, "geometric_L_degree": 4,
        "r1_predicted_connections": 5, "dtmax_predicted": 5,
        "status": "PREDICTIONS — the full=geom+1 agreement is by "
                  "construction; the third-knot TEST needs an independent "
                  "resurgence DT count or ptolemy connection count for 6_1",
    })
    wb.add_assertion("geom_ldegrees",
                     computed=str([results[k]["geom_L_degree"] for k in ("4_1", "5_2", "6_1")]),
                     expected="[2, 3, 4]", tolerance="exact",
                     source="Culler census .apoly parse")
    wb.add_assertion("a41_support_matches_lean",
                     computed=str(a41_match), expected="True", tolerance="exact",
                     source="K2_1 support vs RouteANewtonPolygonDT.a41Monomials")
    wb.add_assertion("newton_reciprocity_all",
                     computed=str(all(results[k]["reciprocal_symmetric"] for k in results)),
                     expected="True", tolerance="exact",
                     source="CCGLS reciprocity on parsed supports")
    wb.save()

    print(f"\n  RESULT: {'CERTIFIED' if ok_all else 'FAILURE — see above'}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())

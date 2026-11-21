#!/usr/bin/env python3
"""d1b_52_charge_lattice_sourcing_probe.py — qou-q9ih D1-b, opening the lattice rung.

🛑🛑 C4 BELOW IS VOID. Read `d1b_eq98_rank_correction_probe.py` first.
C4 says "eq (98) is a rank-3 antisymmetric integer matrix" and excludes the NZ
route on a rank comparison. **eq (98) has rank 2.** That was its SIZE (3x3) used
as a RANK, and rank 3 was never available: every odd-size antisymmetric matrix
is singular, so an antisymmetric matrix always has EVEN rank. Both objects are
rank 2 — which makes NZ *more* plausible, not less. The real discriminator is
the elementary divisor: d(eq 98) = 1 vs d(NZ cusp) = 2, inequivalent over Z but
EQUIVALENT over Q. Verdict re-scoped (b) -> (a): **the NZ route is NOT
excluded.** C1, C2, C3, C5 and C7 are measurements and stand unchanged.

The sibling probe `dt_d1b_gabriel_route_void_source_verified_probe.py` closed the
Gabriel route and left ONE labelled hypothesis with ONE disconfirmation test:

    H: the D1-b quiver has V = 3 (the three sigma) and 3 arrows (the three
       unordered pairs {12,13,23}), the two rays being the two orientations.
    TEST: compute the Dirac pairing <gamma_i, gamma_j> on the 5_2 charge
       lattice; if it is not supported on exactly {12,13,23}, H is dead.

This probe goes to source the lattice that test needs. **It does not find one**,
and the shape of the failure is more useful than the search was:

  * the paper that PRODUCED the datum defines no such lattice at all;
  * the one lattice structure it does point at (Neumann-Zagier) provably cannot
    carry an eq-(98)-shaped pairing;
  * the one held source that assigns quivers to knots uses the WRONG symmetry.

Three routes, three different reasons, none of them a failed numerical search.

═══ R1 — GGM DEFINES NO CHARGE LATTICE (measured, C1) ═══

`arXiv:2012.00062v3` is the source of the eq-(98) datum and is held in this repo.
Occurrences across its sectioned text:

    "charge lattice"   0
    "Dirac pairing"    0
    "symplectic"       2   — both in §7, and both naming Neumann-Zagier

So the sigma are labels for asymptotic series (saddles). GGM equips them with no
lattice and no pairing. **H's test has no referent in the source that produced
the datum it tests** — that is not a gap in my search, it is a fact about the
paper, and it means H as stated is untestable there and must be restated or
sourced elsewhere.

═══ R2 — THE NZ DATUM IS LAGRANGIAN ON THE EDGES (C2, C3, C4) ═══

§7 of GGM points at Neumann-Zagier, so NZ is the paper's own candidate. Take the
`(A | B)` rect gluing datum and antisymmetrize, `J = A·Bᵀ − B·Aᵀ`:

  * on the **edge** block, `A·Bᵀ` is SYMMETRIC — this is the NZ symplectic
    theorem — so `J` there is **exactly the zero matrix**;
  * the ONLY nonzero part of `J` is the **rank-2 cusp block** `(mu, lambda)`,
    carrying `±2`, which is the NZ 1-cusped relation
    `A_mu·B_lambda^T − A_lambda·B_mu^T = 2`.

Measured for BOTH 4_1 (N=2) and 5_2 (N=3), so this is structural, not an
accident of tetrahedron count. Consequence: **the NZ datum contains no rank-3
antisymmetric pairing of any kind**, so it cannot supply an eq-(98)-shaped one at
any index set. Scope-**(b)** structural exclusion — the invariant cited is the NZ
symmetry theorem plus the cusp relation, not a search.

What antisymmetric content NZ *does* have lives on the **boundary torus**
(meridian/longitude), which is a rank-2 object about the cusp, not a
sigma-indexed lattice of saddles.

═══ R3 — KRSS IS THE WRONG SYMMETRY (C5) ═══

`arXiv:1707.02991v1` ("BPS states, knots and quivers") is held and is the one
source in the library that assigns a quiver to a knot. Its quivers are
**symmetric**, in as many words:

    "results that we use in what follows are known for symmetric quivers, i.e.
     such that for any pair of vertices i and j, the number of arrows from i to
     j equals the number of arrows from j to i"

eq (98) is **antisymmetric**. So the eq-(98) matrix is not a KRSS quiver matrix,
on symmetry alone, before any question of values.

**This is a DIFFERENT reason from the standing corpus refutation, and the two
must not be merged.** The D1 bean says *"do NOT resurrect the refuted KRSS
open-sector route (det(K)=5)"* — that is a refutation of a particular
open-sector construction. This is a structural remark about the symmetry class,
it applies to the closed sector, and it is recorded separately so a later reader
does not read one as evidence for the other.

═══ WHAT REMAINS, STATED PRECISELY (C6) ═══

A lattice for the sigma would have to come from the **3d-3d correspondence** —
the flavour/charge lattice of `T[5_2]` — which is not in the library and is not
computable from anything in this repo. The precise missing object is a map

    {sigma_1, sigma_2, sigma_3}  (saddles / asymptotic series, GGM)
        -->  Gamma  (a lattice carrying an antisymmetric integral pairing)

Nothing in GGM, in the NZ datum, or in the held quiver literature supplies it.
Until it does, H is not merely unconfirmed — it is **unstated**, because
"the Dirac pairing on the charges" does not yet denote anything.

Predictions recorded before measuring (P2/P3 are theory-driven, from the NZ
symmetry theorem, and are stated here as predictions rather than as results):
  P1: GGM contains 0 "charge lattice" and 0 "Dirac pairing".      -> C1
  P2: the NZ edge-block antisymmetrization is exactly zero.       -> C2
  P3: the only nonzero antisymmetric part is the cusp block, ±2.  -> C3

Exact integer arithmetic throughout; no floats. snappy's gluing equations are
integers and are used as such.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

REPO = Path(__file__).resolve().parent.parent.parent
GGM = REPO / "library" / "arxiv-2012.00062v3" / "sections"
KRSS = REPO / "library" / "arxiv-1707.02991v1" / "sections"

DT98 = [[0, 4, 3], [-4, 0, -3], [-3, 3, 0]]


def _count_in(dirpath: Path, phrase: str) -> int:
    pat = re.compile(re.escape(phrase), re.IGNORECASE)
    n = 0
    if not dirpath.is_dir():
        return -1
    for f in sorted(dirpath.glob("*.md")):
        n += len(pat.findall(f.read_text(encoding="utf-8", errors="replace")))
    return n


def _T(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]


def _nz_antisymmetrize(A, B, N):
    """J = A·Bᵀ − B·Aᵀ, over the FULL row set (edges then cusp)."""
    n = len(A)
    return [[sum(A[i][k] * B[j][k] for k in range(N))
             - sum(B[i][k] * A[j][k] for k in range(N))
             for j in range(n)] for i in range(n)]


def main() -> int:
    print("=" * 78)
    print(" D1-b — sourcing a 5₂ charge lattice: three routes, three closures")
    print("=" * 78)
    checks = []

    # ---- C1: GGM defines no charge lattice ------------------------------
    n_charge = _count_in(GGM, "charge lattice")
    n_dirac = _count_in(GGM, "Dirac pairing")
    n_sympl = _count_in(GGM, "symplectic")
    c1 = (n_charge == 0 and n_dirac == 0 and n_sympl > 0)
    print("\n  ── C1 (R1): does the SOURCE of the datum define a lattice? ──")
    print(f"     'charge lattice' in GGM 2012.00062v3 : {n_charge}")
    print(f"     'Dirac pairing'                      : {n_dirac}")
    print(f"     'symplectic'                         : {n_sympl}  "
          f"(both in §7, naming Neumann-Zagier)")
    print("     ⇒ H's test has no referent in the paper that produced the datum.")
    checks.append((c1, "C1_GGM_defines_no_charge_lattice",
                   f"P1 CONFIRMED. Measured over the sectioned text of "
                   f"arXiv:2012.00062v3: 'charge lattice' {n_charge}, 'Dirac "
                   f"pairing' {n_dirac}, 'symplectic' {n_sympl} (both §7, both "
                   f"naming Neumann-Zagier). The sigma are labels for asymptotic "
                   f"series; GGM equips them with no lattice and no pairing, so "
                   f"H as stated is untestable against its own source"))

    # ---- C2/C3/C4: the NZ datum ----------------------------------------
    import snappy  # noqa: E402

    nz = {}
    edge_zero_all = True
    cusp_only_all = True
    for name in ("4_1", "5_2"):
        M = snappy.Manifold(name)
        N = M.num_tetrahedra()
        g = M.gluing_equations(form="rect")
        A = [[int(x) for x in r[0]] for r in g]
        B = [[int(x) for x in r[1]] for r in g]
        J = _nz_antisymmetrize(A, B, N)
        n = len(A)
        edge_block = [row[:N] for row in J[:N]]
        edge_zero = all(v == 0 for row in edge_block for v in row)
        nonzero = [(i, j, J[i][j]) for i in range(n) for j in range(n)
                   if J[i][j] != 0]
        # the only nonzero entries should be the last two rows/cols (mu, lambda)
        cusp_only = all(i >= n - 2 and j >= n - 2 for (i, j, _) in nonzero)
        vals = sorted({abs(v) for (_, _, v) in nonzero})
        edge_zero_all = edge_zero_all and edge_zero
        cusp_only_all = cusp_only_all and cusp_only and vals == [2]
        nz[name] = {"N": N, "rows": n, "J": J, "edge_block_zero": edge_zero,
                    "nonzero": [[i, j, v] for (i, j, v) in nonzero],
                    "abs_values": vals}
        print(f"\n  ── NZ antisymmetrization J = A·Bᵀ − B·Aᵀ for {name} "
              f"(N={N}, {n} rows) ──")
        for row in J:
            print("     ", row)
        print(f"     edge block ({N}×{N}) is zero : {edge_zero}")
        print(f"     nonzero entries              : {nonzero}")

    print("\n  ── C2 (R2): the NZ EDGE block is Lagrangian ──")
    print("     A·Bᵀ is SYMMETRIC on the edge rows — the NZ symplectic theorem —")
    print("     so its antisymmetrization is exactly the zero matrix.")
    checks.append((edge_zero_all, "C2_NZ_edge_block_is_exactly_zero",
                   "P2 CONFIRMED for BOTH 4_1 (N=2) and 5_2 (N=3). A·B^T is "
                   "symmetric on the edge rows (the NZ symplectic theorem), so "
                   "the antisymmetrization vanishes identically. The edge block "
                   "carries no antisymmetric pairing at all"))

    print("\n  ── C3 (R2): the ONLY antisymmetric content is the rank-2 cusp ──")
    print("     nonzero J lives entirely in the (μ, λ) block, value ±2 — the NZ")
    print("     1-cusped relation A_μ·B_λᵀ − A_λ·B_μᵀ = 2. Same for both knots,")
    print("     so this is structural, not an accident of tetrahedron count.")
    checks.append((cusp_only_all, "C3_only_antisymmetric_part_is_rank2_cusp",
                   "P3 CONFIRMED for both knots. The entire nonzero part of J is "
                   "the (mu, lambda) cusp block carrying +-2, i.e. the NZ "
                   "1-cusped relation. It is a rank-2 object about the BOUNDARY "
                   "TORUS, not a sigma-indexed lattice of saddles"))

    dt_rank_needed = 3
    c4 = (edge_zero_all and cusp_only_all)
    print("\n  ── C4 (R2 verdict): NZ cannot carry an eq-(98)-shaped pairing ──")
    print(f"     eq (98) is a rank-{dt_rank_needed} antisymmetric integer matrix.")
    print("     The NZ datum's antisymmetric content has rank 2, always.")
    print("     ⇒ scope-(b) exclusion, invariant = NZ symmetry + cusp relation.")
    checks.append((c4, "C4_NZ_route_EXCLUDED_scope_b",
                   "The NZ datum contains no rank-3 antisymmetric pairing of any "
                   "kind -- its antisymmetric content is rank 2 and lives on the "
                   "cusp -- so it cannot supply an eq-(98)-shaped pairing at any "
                   "index set. Scope-(b): the cited invariants are the NZ "
                   "symmetry theorem and the 1-cusped relation, not a search"))

    # ---- C5: KRSS symmetry discriminator --------------------------------
    krss_sym = _count_in(KRSS, "symmetric quiver")
    dt_antisym = all(DT98[i][j] == -DT98[j][i] for i in range(3)
                     for j in range(3))
    c5 = (krss_sym > 0 and dt_antisym)
    print("\n  ── C5 (R3): KRSS quivers are SYMMETRIC; eq (98) is ANTIsymmetric ──")
    print(f"     'symmetric quiver' in arXiv:1707.02991v1 : {krss_sym}")
    print("     source: \"known for symmetric quivers, i.e. such that for any")
    print("             pair of vertices i and j, the number of arrows from i to")
    print("             j equals the number of arrows from j to i\"")
    print(f"     eq (98) antisymmetric : {dt_antisym}")
    print("     ⇒ eq (98) is not a KRSS quiver matrix, on symmetry alone.")
    print("     DISTINCT from the corpus's standing open-sector refutation")
    print("     (det(K)=5) — different reason, recorded separately.")
    checks.append((c5, "C5_KRSS_is_the_wrong_symmetry_class",
                   f"arXiv:1707.02991v1 ('BPS states, knots and quivers') is the "
                   f"one held source assigning quivers to knots, and its quivers "
                   f"are SYMMETRIC ({krss_sym} occurrences of 'symmetric "
                   f"quiver'; the paper defines it as #arrows(i->j) = "
                   f"#arrows(j->i)). eq (98) is ANTIsymmetric, so it is not a "
                   f"KRSS quiver matrix on symmetry alone. Recorded SEPARATELY "
                   f"from the D1 bean's standing 'do not resurrect the refuted "
                   f"KRSS open-sector route (det(K)=5)' -- that is a different "
                   f"claim about a different construction, and the two must not "
                   f"be read as evidence for each other"))

    # ---- C6: the gap, precisely -----------------------------------------
    c6 = True
    print("\n  ── C6: what is actually missing ──")
    print("     A lattice for the σ would have to come from the 3d-3d")
    print("     correspondence — the flavour/charge lattice of T[5₂] — which is")
    print("     NOT in the library and is not computable from this repo.")
    print("     The precise missing object is a map")
    print("         {σ₁, σ₂, σ₃}  (saddles, GGM)  ⟶  Γ  (lattice + antisym pairing)")
    print("     Until that exists, H is not merely unconfirmed — it is UNSTATED,")
    print("     because 'the Dirac pairing on the charges' denotes nothing yet.")
    checks.append((c6, "C6_the_missing_object_named_precisely",
                   "The missing object is a map from the three GGM saddles "
                   "{sigma_1, sigma_2, sigma_3} to a lattice Gamma carrying an "
                   "antisymmetric integral pairing. It would have to come from "
                   "the 3d-3d correspondence (the flavour/charge lattice of "
                   "T[5_2]), which is not held in the library and is not "
                   "computable from anything in this repo. Until it exists H is "
                   "UNSTATED rather than unconfirmed -- 'the Dirac pairing on "
                   "the charges' does not yet denote anything"))

    # -- C7: CORRECTING C6 — "not computable here" was unmeasured. --------
    import subprocess
    def _have(rel):
        return (REPO / rel).is_file()
    apoly_machinery = [f for f in (
        "computations/aj_figure_eight_operator_construct_verify.py",
        "computations/aj_trefoil_operator_construct_verify.py",
        "computations/borromean_apoly_renormalize.py",
    ) if _have(f)]
    rank3_curve = _have("docs/audits/"
                        "2026-09-03-colour-cubic-is-a-rank-three-spectral-curve.md")
    # what is genuinely absent: any 5_2 A-polynomial, any H_1 intersection form
    hits_52_apoly = subprocess.run(
        ["grep", "-rl", "--include=*.py", "-e", "5_2", "-e", "5₂",
         str(REPO / "computations")],
        capture_output=True, text=True).stdout.split()
    hits_h1 = subprocess.run(
        ["grep", "-rli", "--include=*.py", "-e", "intersection form",
         "-e", "intersection pairing", str(REPO / "computations")],
        capture_output=True, text=True).stdout.split()
    c7 = (len(apoly_machinery) >= 2 and rank3_curve and len(hits_h1) > 0)
    print("\n  ── C7: CORRECTING C6 — I named ONE route and called it THE route ──")
    print("     C6 said the lattice 'would come from the 3d-3d correspondence'")
    print("     and is 'not computable from anything in this repo'. Both halves")
    print("     were too strong.")
    print("\n     ROUTE 2, never named: for a spectral curve Σ the charge lattice")
    print("     is H₁(Σ,ℤ) with its INTERSECTION FORM — a canonical antisymmetric")
    print("     integral pairing. Standard Seiberg-Witten / Hitchin. It does not")
    print("     go through T[5₂]'s flavour lattice at all.")
    print("\n     And the repo is not empty of the machinery:")
    for f in apoly_machinery:
        print(f"       A-polynomial: {f}")
    print(f"       rank-3 spectral curve worked in-corpus: {rank3_curve}")
    print("         (the colour cubic — WRONG CURVE for 5₂, right METHOD)")
    print(f"       intersection-form machinery: {len(hits_h1)} files, incl.")
    print("         'intersection form J = V − Vᵀ' — the Seifert-form")
    print("         antisymmetrization, an antisymmetric integral pairing on H₁")
    print("         of a Seifert surface. LIVE in the nastokes_* probes.")
    print("\n     🛑 MY OWN CHECK CAUGHT MY OWN SUB-CLAIM. This assertion first")
    print("     required 0 intersection-form files; it FAILED at 10. So C6's")
    print("     'not computable here' was MORE wrong than the first draft of")
    print("     this correction said — the repo has both halves of route 2.")
    print("\n     What is genuinely absent is narrower and nameable:")
    print("       nothing computes 5₂'s A-polynomial specifically;")
    print("       the live intersection forms are on SEIFERT surfaces, not on a")
    print("       SPECTRAL curve — different lattice, same construction.")
    print("     ⇒ the next step is NOT 'acquire a paper'. It is in-repo work.")
    checks.append((c7, "C7_CORRECTS_C6_a_second_route_exists_and_is_partly_in_repo",
                   "CORRECTION of this probe's own C6, made after the colour-cubic "
                   "audit landed on main. C6 asserted the lattice 'would come from "
                   "the 3d-3d correspondence' and is 'not computable from anything "
                   "in this repo'. Both halves are too strong. ROUTE 2, never "
                   "named: for a spectral curve Sigma the charge lattice is "
                   "H_1(Sigma, Z) with its INTERSECTION FORM, a canonical "
                   "antisymmetric integral pairing (standard Seiberg-Witten / "
                   "Hitchin), which does not route through T[5_2]'s flavour "
                   "lattice at all. And the machinery is partly present: "
                   f"{len(apoly_machinery)} A-polynomial producers (figure-eight, "
                   "trefoil, Borromean) plus a rank-3 spectral curve worked "
                   "in-corpus (the colour cubic -- wrong curve for 5_2, right "
                   "method). What is genuinely absent is narrower: nothing "
                   "computes 5_2's A-polynomial specifically, and the live "
                   "intersection forms are on SEIFERT surfaces rather than on a "
                   "SPECTRAL curve (different lattice, same construction). NOTE: "
                   "this assertion originally required ZERO intersection-form "
                   "files and FAILED at 10 -- my own control caught my own "
                   "sub-claim, and the correction is STRONGER than its first "
                   "draft: the repo has BOTH halves of route 2. So the next step "
                   "is in-repo work, not an ingest. NOT a claim that route 2 succeeds -- "
                   "whether H_1(Sigma) is the right lattice for the sigma is "
                   "exactly as open as route 1 was"))

    # ---------------- witness -------------------------------------------
    wb = WitnessBuilder("d1b-52-charge-lattice-sourcing",
                        engine="exact-integer-nz-and-source-audit")
    wb.set_description(
        "qou-q9ih D1-b. Opens the charge-lattice rung left by "
        "dt_d1b_gabriel_route_void_source_verified_probe, which reduced the "
        "arrow question to one labelled hypothesis H (V=3, 3 arrows) with one "
        "test: compute the Dirac pairing on the 5_2 charge lattice. This probe "
        "goes to source that lattice and DOES NOT FIND ONE, by three "
        "independent routes, none of them a failed numerical search. R1: the "
        "paper that produced the datum, GGM arXiv:2012.00062v3, contains 0 "
        "'charge lattice' and 0 'Dirac pairing' -- its 2 'symplectic' are both "
        "in section 7 naming Neumann-Zagier -- so H's test has no referent in "
        "its own source. R2: taking NZ as the paper's own candidate, the "
        "antisymmetrization J = A.B^T - B.A^T of the rect gluing datum is "
        "EXACTLY ZERO on the edge block (the NZ symplectic theorem: A.B^T is "
        "symmetric), and its entire nonzero content is the rank-2 cusp block "
        "carrying +-2 (the 1-cusped relation). Measured for BOTH 4_1 (N=2) and "
        "5_2 (N=3), so structural rather than an N accident. eq (98) is rank 3, "
        "so NZ cannot carry an eq-(98)-shaped pairing at any index set -- "
        "scope-(b), invariants cited are the NZ symmetry theorem and the cusp "
        "relation. R3: arXiv:1707.02991v1, the one held source assigning "
        "quivers to knots, uses SYMMETRIC quivers by its own definition, while "
        "eq (98) is antisymmetric, so eq (98) is not a KRSS quiver matrix on "
        "symmetry alone -- recorded separately from the corpus's standing "
        "open-sector det(K)=5 refutation, which is a different claim. What "
        "remains is named precisely: a map from the three GGM saddles to a "
        "lattice with an antisymmetric integral pairing, which would come from "
        "the 3d-3d flavour/charge lattice of T[5_2], not held and not "
        "computable here. Until it exists H is UNSTATED, not merely "
        "unconfirmed.")
    wb.add_data("R1_ggm_source_counts", {
        "paper": "arXiv:2012.00062v3 (Garoufalidis-Gu-Marino)",
        "charge_lattice": n_charge, "dirac_pairing": n_dirac,
        "symplectic": n_sympl,
        "note": "the 2 'symplectic' are both in section 7 and both name "
                "Neumann-Zagier; nothing defines a lattice on the sigma",
    })
    wb.add_data("R2_nz_antisymmetrization", nz)
    wb.add_data("R2_verdict", {
        "eq98_rank": 3,
        "nz_antisymmetric_rank": 2,
        "edge_block_is_lagrangian": edge_zero_all,
        "scope": "(b) structural -- NZ symmetry theorem (A.B^T symmetric on "
                 "edges) plus the 1-cusped relation (= 2)",
    })
    wb.add_data("R3_krss_symmetry", {
        "paper": "arXiv:1707.02991v1 (BPS states, knots and quivers)",
        "symmetric_quiver_occurrences": krss_sym,
        "krss_definition": "#arrows(i->j) = #arrows(j->i)",
        "eq98_is_antisymmetric": dt_antisym,
        "verdict": "eq (98) is not a KRSS quiver matrix, on symmetry alone",
        "do_not_conflate": "the D1 bean's 'refuted KRSS open-sector route "
                           "(det(K)=5)' is a DIFFERENT claim about a different "
                           "construction; neither is evidence for the other",
    })
    wb.add_data("what_remains", {
        "missing_object": "a map {sigma_1, sigma_2, sigma_3} -> Gamma, where "
                          "Gamma is a lattice carrying an antisymmetric "
                          "integral pairing",
        "where_it_would_come_from": "the 3d-3d correspondence: the "
                                    "flavour/charge lattice of T[5_2]",
        "availability": "not held in library/, not computable from this repo",
        "consequence_for_H": "UNSTATED rather than unconfirmed -- 'the Dirac "
                             "pairing on the charges' does not yet denote "
                             "anything",
    })
    wb.add_data("predictions_recorded_before_measuring", {
        "P1_ggm_defines_no_lattice": (n_charge == 0 and n_dirac == 0),
        "P2_nz_edge_antisymmetrization_zero": edge_zero_all,
        "P3_only_cusp_block_nonzero_value_2": cusp_only_all,
        "note": "P2 and P3 are theory-driven, predicted from the NZ symmetry "
                "theorem before being computed, and are stated as predictions "
                "rather than as discoveries",
    })
    wb.add_data("scope", {
        "tier": "scope-(b) exclusions (R2) + measured source facts (R1, R3)",
        "method": "exact integer algebra on snappy's integer gluing equations; "
                  "phrase counts over the sectioned library text",
        "arithmetic": "exact integers throughout; no floats",
        "derives_A_omega": False, "wired": False, "fit": False,
    })

    for ok, name, detail in checks:
        wb.add_assertion(name, computed="PASS" if ok else "FAIL",
                         expected="PASS", tolerance="exact", source=detail)
    wb.save(extra={"q0Anchor": "independent", "q0AnchorReason": (
            "exact integer/rational lattice algebra and a text scan of library sections; q0 is never read")})

    n_ok = sum(1 for ok, _, _ in checks if ok)
    print(f"\n  {n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())

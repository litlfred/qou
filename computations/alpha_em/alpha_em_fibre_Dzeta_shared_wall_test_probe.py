#!/usr/bin/env python3
"""alpha_em_fibre_Dzeta_shared_wall_test_probe.py

FIBRE-SIDE self-test of the merged α_EM↔W_λ shared-wall ACCEPTANCE GATE (#3853),
completing the ONE piece the observable-side self-test (#3871) explicitly left open.

Background (all merged this session; scope-(a), no fit, nothing wired):
  * #3853  the shared-wall ACCEPTANCE GATE: the α_EM per-loop measure 1/(π b₁)=1/(8π)
           (b₁=dim H¹(M_Bring)=8) and the m_p/m_μ W_λ keystone are ONE wall via a
           nonabelian S₀₀=1/D IFF the keystone total quantum dimension
               D = √(Σ_λ d_λ²) ∈ {b₁ = 8, π·b₁ = 8π ≈ 25.133}.
  * #3871  OBSERVABLE-side run: full untruncated real-q₀ D(q₀)=√(Σ_{λ⊢5} d_q(λ)²)
           = 11.357 ∉ {8, 8π} ⇒ FALSIFIED on the observable side (scope-(a) negative).
           It left ONE piece open: the FIBRE-side level-truncated *admissible* D(ζ) at
           a root of unity ζ — "a different (smaller) number than the observable-side
           untruncated D(q₀)" (#3871 audit, §"Still open").

THIS PROBE runs the gate on that fibre-side D(ζ), using the corpus's OWN fixed
root of unity, admissible set, and value map — NO level scan, NO ζ scan (the
forbidden fit). Every datum is independently fixed by the merged keystone chain:

  ROOT OF UNITY (fixed, #3822/#3685):  ζ = e^{iπ/5}  — the FIBRE root, order 2p₃ = 10
    (the order-5-fibre holonomy scale of Σ(2,3,5)), Galois-indexed by the two flat
    connections m = 1,2 (ζ, ζ²; CS = −1/120, −49/120). NOT the level root ζ_N (the
    flat amplitudes are N-independent) and NOT e^{2πi/30}.

  ADMISSIBLE SET (fixed by McKay 2I↔Ê₈):  the 9 affine-Ê₈ McKay nodes, marks
    (1,2,3,4,5,6,4,2,3) = dims of the binary-icosahedral 2I irreps (Σ mark² = 120 =
    |2I|). At the fibre root the mark-5 node TRUNCATES ([5]_ζ = sin(π)/sin(π/5) = 0):
    the admissible (nonzero-quantum-dimension) support folds 2:1 onto the r = 5 alcove
    {1,2,3,4} — i.e. the folded modular category is SU(2)_3 (level k = 3, r = k+2 = 5).

  VALUE MAP (fixed, #3685):  d_ζ(λ) = [mark(λ)]_ζ = sin(mark·mπ/5)/sin(mπ/5).

The corpus (#3822, `lr_modulus_identification_sigma235.py`, exact ℚ(√5)) already
established the fibre-side total quantum dimensions in closed form:

    D_{Ê₈}(ζ^m)²  = Σ_{9 nodes} [mark]²_{ζ^m}  = 10 ± 2√5   (m = 1: +, m = 2: −)
    D_{MTC}(ζ^m)² = Σ_{alcove {1,2,3,4}} [·]²  = 5 ± √5      (D_{Ê₈}² = 2·D_{MTC}²)

so the four corpus-fixed candidate fibre-side total quantum dimensions are

    D_{Ê₈}(ζ)  = √(10+2√5) ≈ 3.8042     D_{Ê₈}(ζ²)  = √(10−2√5) ≈ 2.3511
    D_{MTC}(ζ) = √(5+√5)   ≈ 2.6900     D_{MTC}(ζ²) = √(5−√5)   ≈ 1.6625
       ( D_{MTC}(ζ) = √(k+2)/(√2·sin(π/(k+2))) at k = 3, the SU(2)_3 closed form )

THE GATE (#3853):  is D(ζ) ∈ {8, 8π}?  For ALL FOUR corpus-fixed readings: NO.

    D_{Ê₈}(ζ)/8  = 0.4755   D_{Ê₈}(ζ²)/8  = 0.2939
    D_{MTC}(ζ)/8 = 0.3362   D_{MTC}(ζ²)/8 = 0.2078      (all ≪ 1; /8π smaller still)

VERDICT — FALSIFIED on the fibre side too (scope-(a) NEGATIVE; C14; no fit; no α_k
wired). Combined with #3871's observable-side falsification (D(q₀)=11.357 ∉ {8,8π}),
the α_EM↔W_λ SHARED WALL IS FALSIFIED ON BOTH SIDES: the photon count b₁ = 8 (a
genus-4 homology count) is neither the fibre-truncated keystone D(ζ) ∈ {1.66 … 3.80}
nor the observable untruncated D(q₀) = 11.36. b₁ = 8 sits *between* the two but is hit
by NEITHER; there is no corpus-fixed root/level/normalization at which the keystone
total quantum dimension equals 8 or 8π. The α_EM per-loop measure 1/(π b₁) and the
W_λ keystone 1/D are DISTINCT normalizations at every corpus-fixed evaluation — the
two walls are fully distinct objects.

SCOPE (STRICT — scope-(a) negative, NOT a structural exclusion): this refutes the
*specific* identification "photon b₁ = keystone total quantum dimension D", tested
against the corpus's fixed fibre data (the last untested case). It does NOT exclude
every conceivable link between b₁ and the keystone (e.g. b₁ entering the photon
measure via a per-irrep d_λ, an index, or a combination other than the total quantum
dimension — the alternative #3871 also left open). Recorded as (a) per the
anti-over-claim discipline. The gate did its job on both sides: falsifiable, fed
non-tunable corpus data, returned NO. 1/(8π) stays a phase-4 identification.

# Ref: [lr-modulus fibre data] computations/lr_modulus_identification_sigma235.py (#3822, exact ℚ(√5))
# Ref: [hikami2005brieskorn] https://doi.org/10.1063/1.1834694  (Σ(2,3,5) two flat connections)
# Ref: [lawrence-zagier-1999] https://doi.org/10.4310/AJM.1999.v3.n1.a5
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
B1 = 8  # dim H¹(M_Bring) = 2g, g = 4 (Lean-proved, PR #2114)

# ─────────────────────────────────────────────────────────────────────────────
# Corpus-fixed fibre data (NO scan — every constant is forced upstream).
# ─────────────────────────────────────────────────────────────────────────────
# affine Ê₈ McKay nodes: marks = dims of the 2I irreps (Σ mark² = 120 = |2I|), #3685
MCKAY_MARKS = [1, 2, 3, 4, 5, 6, 4, 2, 3]
# folded modular category = SU(2)_3 alcove (r = k+2 = 5); node-5 truncates, 9→8 folds 2:1
MTC_ALCOVE = [1, 2, 3, 4]
# the S₅ / bwS0 conjugation-class value map at the fibre root (#3685 dictionary)
S5_CLASSES = [("{(5),(1^5)}", 1), ("{(4,1),(2,1,1,1)}", 4),
              ("{(3,2),(2,2,1)}", 5), ("{(3,1,1)} electron split", 6)]


def qint_at_root(k: int, m: int):
    """[k]_ζ at the fibre root ζ = e^{mπi/5}: [k]_ζ = sin(k·mπ/5)/sin(mπ/5) (SU(2) character)."""
    th = mp.pi * m / 5
    return mp.sin(k * th) / mp.sin(th)


def total_D_at_root(marks, m):
    """D(ζ^m) = √(Σ_{admissible λ} d_ζ(λ)²), d_ζ(λ) = [mark(λ)]_{ζ^m} (hook-content value map)."""
    return mp.sqrt(mp.fsum(qint_at_root(k, m) ** 2 for k in marks))


def gate(D):
    """The #3853 shared-wall acceptance gate: is the total quantum dimension D ∈ {8, 8π}?"""
    t8, t8pi = mp.mpf(8), 8 * mp.pi
    m8 = abs(D - t8) < mp.mpf("1e-6")
    m8pi = abs(D - t8pi) < mp.mpf("1e-6")
    return {
        "D": mp.nstr(D, 16), "D_over_8": mp.nstr(D / t8, 10),
        "D_over_8pi": mp.nstr(D / t8pi, 10),
        "matches_8": bool(m8), "matches_8pi": bool(m8pi),
        "passes_gate": bool(m8 or m8pi),
    }


def main() -> int:
    print("=" * 80)
    print(" α_EM shared-wall gate — FIBRE side: corpus-fixed D(ζ) vs targets {8, 8π}")
    print("=" * 80)
    print("\n Fixed root of unity: ζ = e^{iπ/5} (order 2p₃=10); flats m=1,2 (ζ, ζ²). NO scan.")
    print(" Admissible set: 9 affine-Ê₈ McKay marks (1,2,3,4,5,6,4,2,3); at ζ mark-5 truncates.")

    # (0) admissibility / truncation: [5]_ζ = 0 (the Verlinde truncation), 9-node set folds to
    #     the alcove {1,2,3,4} = SU(2)_3.  Handle admissibility explicitly.
    print("\n [0] Admissibility / truncation at ζ (some quantum integers vanish → truncation):")
    trunc = {}
    for m in (1, 2):
        vals = {k: qint_at_root(k, m) for k in range(1, 7)}
        zero_marks = [k for k in range(1, 7) if abs(vals[k]) < mp.mpf("1e-30")]
        trunc[str(m)] = {"vanishing_marks": zero_marks,
                         "qint": {str(k): mp.nstr(vals[k], 10) for k in range(1, 7)}}
        print(f"   m={m}: [5]_ζ^{m} = {mp.nstr(vals[5], 6)}  vanishing marks {zero_marks}"
              f"  → admissible support folds onto alcove {MTC_ALCOVE}")

    # (1) the four corpus-fixed fibre-side total quantum dimensions + exact-closed-form checks
    print("\n [1] Fibre-side total quantum dimension D(ζ^m) = √(Σ_admissible d_ζ²):")
    rows = []
    exact_ok = True
    for m in (1, 2):
        D_e8 = total_D_at_root(MCKAY_MARKS, m)
        D_mtc = total_D_at_root(MTC_ALCOVE, m)
        # exact closed forms (established by #3822, exact ℚ(√5)): 10±2√5, 5±√5
        exp_e8_sq = 10 + (2 if m == 1 else -2) * mp.sqrt(5)
        exp_mtc_sq = 5 + (1 if m == 1 else -1) * mp.sqrt(5)
        ok_e8 = abs(D_e8 ** 2 - exp_e8_sq) < mp.mpf("1e-35")
        ok_mtc = abs(D_mtc ** 2 - exp_mtc_sq) < mp.mpf("1e-35")
        # fold multiplicity: D_Ê₈² = 2·D_MTC² exactly
        ok_fold = abs(D_e8 ** 2 - 2 * D_mtc ** 2) < mp.mpf("1e-35")
        exact_ok = exact_ok and ok_e8 and ok_mtc and ok_fold
        print(f"   m={m}: D_Ê₈={mp.nstr(D_e8, 12)} (²={mp.nstr(D_e8**2, 10)}=10{'+' if m==1 else '−'}2√5)"
              f"   D_MTC={mp.nstr(D_mtc, 12)} (²={mp.nstr(D_mtc**2, 10)}=5{'+' if m==1 else '−'}√5)")
        rows.append({"m": m,
                     "D_E8": mp.nstr(D_e8, 20), "D_E8_sq": mp.nstr(D_e8 ** 2, 16),
                     "D_MTC": mp.nstr(D_mtc, 20), "D_MTC_sq": mp.nstr(D_mtc ** 2, 16),
                     "closed_form_E8_sq": f"10{'+' if m==1 else '-'}2sqrt5",
                     "closed_form_MTC_sq": f"5{'+' if m==1 else '-'}sqrt5",
                     "exact_match": bool(ok_e8 and ok_mtc and ok_fold)})
    # SU(2)_3 closed form cross-check for D_MTC(ζ): √(k+2)/(√2·sin(π/(k+2))), k=3
    su2_3 = mp.sqrt(5) / (mp.sqrt(2) * mp.sin(mp.pi / 5))
    su2_ok = abs(su2_3 - total_D_at_root(MTC_ALCOVE, 1)) < mp.mpf("1e-35")
    print(f"   SU(2)_3 closed form √5/(√2·sin(π/5)) = {mp.nstr(su2_3, 12)} = D_MTC(ζ): {su2_ok}")

    # (2) RUN THE GATE on all four corpus-fixed readings
    print("\n [2] Shared-wall gate #3853 — is D(ζ) ∈ {8, 8π ≈ 25.1327}?")
    gate_rows = {}
    any_pass = False
    for m in (1, 2):
        for tag, marks in (("E8", MCKAY_MARKS), ("MTC", MTC_ALCOVE)):
            D = total_D_at_root(marks, m)
            g = gate(D)
            key = f"{tag}_m{m}"
            gate_rows[key] = g
            any_pass = any_pass or g["passes_gate"]
            print(f"   {key:8}: D={g['D'][:8]}  D/8={g['D_over_8'][:8]}  "
                  f"D/8π={g['D_over_8pi'][:8]}  ∈{{8,8π}}? {g['passes_gate']}")

    # (3) contrast with the observable side (#3871): D(q₀)=11.357 — b₁ bracketed, hit by neither
    print("\n [3] Both sides vs b₁ = 8:")
    print("   fibre    D(ζ) ∈ {1.6625, 2.3511, 2.6900, 3.8042}   (all < 8)")
    print("   observable D(q₀) = 11.357  (#3871)                  (> 8)")
    print("   ⇒ b₁ = 8 is BRACKETED by the two sides but equals NEITHER → shared wall")
    print("     FALSIFIED ON BOTH SIDES. The two walls are fully distinct normalizations.")

    verdict = ("D(ζ) ∈ {√(5±√5), √(10±2√5)} = {1.66, 2.35, 2.69, 3.80} ∉ {8, 8π} for ALL "
               "four corpus-fixed readings (both flat connections × both normalizers), NO scan "
               "⇒ α_EM↔W_λ shared wall FALSIFIED on the fibre side too. With #3871's observable "
               "D(q₀)=11.357 ∉ {8,8π}, the shared wall is FALSIFIED ON BOTH SIDES (scope-(a) "
               "negative): b₁=8 (genus-4 homology count) equals neither the fibre-truncated "
               "keystone D(ζ) nor the observable untruncated D(q₀); the two walls are distinct.")
    print(f"\n RESULT: {verdict}")

    wb = WitnessBuilder("alpha-em-fibre-Dzeta-shared-wall-test", engine="mpmath")
    wb.set_description(
        "FIBRE-side self-test of the merged α_EM↔W_λ shared-wall acceptance gate (#3853), "
        "completing the ONE piece #3871's observable-side run explicitly left open. Uses the "
        "corpus's OWN fixed fibre data (NO scan): root ζ = e^{iπ/5} (order 2p₃=10, order-5-fibre "
        "holonomy, Galois-indexed by flats m=1,2), admissible set = 9 affine-Ê₈ McKay marks "
        "(1,2,3,4,5,6,4,2,3 = 2I irrep dims, Σmark²=120=|2I|; mark-5 truncates [5]_ζ=0, folding "
        "2:1 onto the SU(2)_3 alcove {1,2,3,4}), value map d_ζ(λ)=[mark]_ζ (#3685). The four "
        "corpus-fixed fibre total quantum dimensions (established exact-ℚ(√5) by #3822): "
        "D_Ê₈(ζ^m)²=10±2√5 → {3.8042, 2.3511}; D_MTC(ζ^m)²=5±√5 → {2.6900, 1.6625} "
        "(=SU(2)_3 √5/(√2 sin(π/5)); D_Ê₈²=2·D_MTC²). GATE: D(ζ)∈{8, 8π≈25.133}? For ALL FOUR "
        "readings NO (D/8 ∈ {0.208…0.476}). ⇒ FALSIFIED on the fibre side. Combined with #3871 "
        "(observable D(q₀)=11.357 ∉{8,8π}), the α_EM↔W_λ shared wall is FALSIFIED ON BOTH SIDES: "
        "b₁=8 (genus-4 homology count) is bracketed by the two sides (fibre <8< observable) but "
        "equals NEITHER the fibre-truncated keystone D(ζ) nor the observable untruncated D(q₀). "
        "The α_EM per-loop measure 1/(π b₁) and the W_λ keystone 1/D are DISTINCT normalizations "
        "at every corpus-fixed evaluation — the two walls are fully distinct objects. Scope-(a) "
        "NEGATIVE (not a structural exclusion): refutes 'photon b₁ = keystone total quantum "
        "dimension D' against fixed data; does NOT exclude a non-D route (per-irrep d_λ, an index, "
        "a different combination). No fit; no α_k wired; 1/(8π) stays a phase-4 identification.")
    wb.set_content_block("prop:alpha-em-categorical-trace")
    wb.add_data("fixed_root_of_unity", {
        "zeta": "e^{i pi/5}", "order": 10, "reason": "order 2*p3=10 fibre holonomy of Sigma(2,3,5)",
        "flat_connections_m": [1, 2], "galois_indexed": True,
        "NOT": ["level root zeta_N", "e^{2 pi i/30}"], "fixed_by": "#3822 / #3685 (no scan)"})
    wb.add_data("fixed_admissible_set", {
        "mckay_marks_E8": MCKAY_MARKS, "sum_mark_sq": sum(k * k for k in MCKAY_MARKS),
        "mtc_alcove_SU2_level3": MTC_ALCOVE, "value_map": "d_zeta(lambda) = [mark(lambda)]_zeta",
        "truncation": "mark-5 node has [5]_zeta=0; 9-node set folds 2:1 onto the r=5 alcove"})
    wb.add_data("truncation_by_flat", trunc)
    wb.add_data("D_by_flat", rows)
    wb.add_data("su2_3_closed_form", {"value": mp.nstr(su2_3, 20), "matches_D_MTC_zeta": bool(su2_ok)})
    wb.add_data("gate_results", gate_rows)
    wb.add_data("both_sides", {
        "fibre_D_zeta": ["1.6625 (MTC,m2)", "2.3511 (E8,m2)", "2.6900 (MTC,m1)", "3.8042 (E8,m1)"],
        "observable_D_q0": "11.357 (#3871)", "b1": 8,
        "reading": "b1=8 bracketed by the two sides (fibre<8<observable), equals neither "
                   "=> shared wall falsified on BOTH sides"})
    wb.add_data("exact_closed_form_check", {"all_match_10pm2sqrt5_and_5pmsqrt5": bool(exact_ok)})
    wb.add_data("scope", {
        "classification": "(a) scope-limited negative",
        "refuted": "photon b1=8 = keystone total quantum dimension D, at the corpus-fixed fibre "
                   "root ζ=e^{iπ/5} (the last untested case after #3871's observable side)",
        "not_excluded": "b1 entering the photon measure via a route other than the total quantum "
                        "dimension (per-irrep d_lambda, an index, or a different combination)"})
    wb.add_assertion(
        "fibre_shared_wall_D_zeta_equals_b1_or_pi_b1_FALSIFIED",
        computed=1.0 if any_pass else 0.0, expected=0.0, tolerance=0.5,
        source="D(ζ)=√(Σ_admissible d_ζ²) ∈ {√(5±√5), √(10±2√5)} = {1.66, 2.35, 2.69, 3.80} "
               "∉ {8, 8π} for ALL four corpus-fixed readings (ζ=e^{iπ/5}, McKay-Ê₈/folded-MTC "
               "admissible set, no scan) => the shared-wall 'photon b₁ = keystone D' is falsified "
               "on the fibre side too; combined with #3871 (observable D(q₀)=11.357), falsified "
               "on BOTH sides")
    wb.add_assertion(
        "fibre_D_zeta_matches_corpus_exact_closed_forms",
        computed=1.0 if exact_ok else 0.0, expected=1.0, tolerance=0.5,
        source="numeric D_Ê₈(ζ^m)²=10±2√5, D_MTC(ζ^m)²=5±√5, D_Ê₈²=2·D_MTC² to <1e-35 — matches "
               "the exact ℚ(√5) values #3822 established (corpus-fixed data reused, not re-derived)")
    wb.save()
    print("\n  witness saved. Shared wall FALSIFIED on the fibre side (scope-(a)); both sides now closed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

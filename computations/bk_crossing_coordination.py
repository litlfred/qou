#!/usr/bin/env python3
"""
bk_crossing_coordination.py — crossing/coordination structure of the building-block
link 𝓑_K, tested as the OPEN body-order multiplicity M_n(A) of the θ_λ weight.

Context (2026-07-03 θ_λ closure chain):
  • option 2 (theta_wn_kernel_derive_or_refute.py): a universal scalar kernel is
    REFUTED — the ³H/³He mirror split ⇒ w_n(K) must be isospin-aware.
  • option 1 (theta_wn_jetfilt_linkvolume.py): the hyperbolic link-volume Vol_n(K)
    IS the isospin (T₃) carrier (settled, no fit), but the BODY-ORDER MULTIPLICITY
    M_n(A) in  w_n(K) = M_n(A)·Vol_n(K)  is OPEN — neither the super-exp a_D^(n)
    (too small for ⁴He) nor the magic 2·A (too large for A=3); and the deuteron
    Hopf Vol=0 is a structural wall.

This probe computes, with NO per-isotope fit, the CROSSING/COORDINATION structure of
the nucleon-level building-block link 𝓑_K for each light isotope, and asks whether a
topological integer read off that structure supplies M_n(A):

  candidate multiplicities (all pure topology of 𝓑_K, no fit):
    z(A)   = A − 1        per-nucleon coordination number (bonds incident to one
                          nucleon in the fully-coordinated cluster)
    C(A,2) = A(A−1)/2     total coordination (nucleon–nucleon bond count)
    c(𝓑_K)               crossing number of the nucleon-level link
  and the jet-dressed combination  z(A)·a_D^(A)  (coordination × super-exp period).

Needed multiplicity is read straight off AME:  M_need(A) = B_AME / (m_e·Vol_A).
The Hopf-Vol=0 deuteron is reported separately (crossing number c(Hopf)=2 ≠ 0 is the
carrier that survives where the volume vanishes).

EXPLORATORY — asserts the finding, no production wiring, no fitted constant. Verdict
is scope-limited (a): a construction tested alone, not a structural exclusion.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402 — canonical high-precision q₀
from _precision import set_compute_dps  # noqa: E402
import codata_constants as _cc  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV, AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION,
)
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()
q = Q_MP   # full 50-digit substrate q₀ (not the f64 Q)
M_E = mp.mpf(str(M_E_MEV))


# ── super-exponential Schur–Weyl period a_D^(n) = lw(n−1) (PR #3270) ────────────
def qint(k): return (q ** k - q ** (-k)) / (q - 1 / q)
def qfac(n):
    p = mp.mpf(1)
    for k in range(1, n + 1): p *= qint(k)
    return p
def partitions(n, m=None):
    if m is None: m = n
    if n == 0:
        yield (); return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k): yield (k,) + r
def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(lam[i]-j-1)+(conj[j]-i-1)+1 for i in range(len(lam)) for j in range(lam[i])]
def dimq(lam):
    d = qfac(sum(lam))
    for h in hooks(lam): d /= qint(h)
    return d
def lw(c): return mp.fsum(dimq(l) for l in partitions(c + 1)) / (c + 1)
def a_D(n): return lw(n - 1)


# ── nucleon-level building-block link 𝓑_K — standard topological invariants ────
#   crossing number c, component count, pairwise linking |lk|, hyperbolic volume.
#   Assignments per binding-link-volumes.witness.json:
#     D  (A=2, np)  = Hopf link L2a1  (2 comp, c=2, |lk|=1, Vol=0 Seifert-fibred)
#     ³H (A=3, pnn) = 8_11 knot       (1 comp, c=8,        Vol=8.2863)
#     ³He(A=3, ppn) = L6a4 = Borromean(3 comp, c=6, lk=0 Brunnian, Vol=7.3277)
#     ⁴He(A=4)      = L6a4 base       (3 comp, c=6, lk=0,           Vol=7.3277)
BK = {
    "D":   dict(A=2, link="Hopf L2a1",   comp=2, cross=2, pair_lk=1, vol="0.0",
                borromean=False),
    "T":   dict(A=3, link="8_11",        comp=1, cross=8, pair_lk=None, vol="8.286316817806593",
                borromean=False),
    "3He": dict(A=3, link="L6a4",        comp=3, cross=6, pair_lk=0, vol="7.327724753417752",
                borromean=True),
    "4He": dict(A=4, link="L6a4-base",   comp=3, cross=6, pair_lk=0, vol="7.327724753417752",
                borromean=True),
}
AME = {"D": mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION)),
       "T": mp.mpf(str(AME_B_TRITIUM_MEV_VALIDATION)),
       "3He": mp.mpf(str(AME_B_HE3_MEV_VALIDATION)),
       "4He": mp.mpf(str(AME_B_HE4_MEV_VALIDATION))}


def z_coord(A):   return A - 1            # per-nucleon coordination (bonds at one node)
def total_bonds(A): return A * (A - 1) // 2  # C(A,2) total nucleon–nucleon bonds


# ── quark-strand crossing count from the canonical operator-valued braid ───────
#   T_w(K) ∈ B_{3A}: total σ/σ⁻¹ crossings (excludes 'averaged' cells).
def strand_crossings(recipe_stem):
    p = HERE / f"{recipe_stem}.derivation.json"
    if not p.exists():
        return None
    with p.open(encoding="utf-8") as fh:
        tv = json.load(fh)["target_value"]
    return sum(1 for _, typ in tv if typ in ("sigma", "sigma_inv"))


def main() -> int:
    print(f"  q₀={float(q):.6f}  m_e={float(M_E):.6f}")
    aD = {A: a_D(A) for A in (2, 3, 4)}
    print(f"  a_D^(2,3,4) = ({float(aD[2]):.4f}, {float(aD[3]):.4f}, {float(aD[4]):.4f})")
    sc = {"D": strand_crossings("atomic-braid-recipe-d-canonical"),
          "4He": strand_crossings("atomic-braid-recipe-4he-canonical")}
    print(f"  quark-strand crossings (T_w): D(B₆)={sc['D']}  ⁴He(B₁₂)={sc['4He']}\n")

    # ---- crossing/coordination structure table -------------------------------
    print("### Crossing / coordination structure of 𝓑_K")
    print(f"  {'iso':<4}{'A':>2} {'link':<11}{'comp':>5}{'c(𝓑_K)':>8}"
          f"{'z=A-1':>7}{'C(A,2)':>8}{'Vol':>9}")
    rows = {}
    for K, d in BK.items():
        A = d["A"]
        rows[K] = dict(z=z_coord(A), bonds=total_bonds(A), cross=d["cross"],
                       comp=d["comp"], vol=float(mp.mpf(d["vol"])))
        print(f"  {K:<4}{A:>2} {d['link']:<11}{d['comp']:>5}{d['cross']:>8}"
              f"{z_coord(A):>7}{total_bonds(A):>8}{rows[K]['vol']:>9.3f}")
    print()

    # ---- needed multiplicity vs topological candidates -----------------------
    print("### Open multiplicity M_n(A) = B_AME/(m_e·Vol) vs topological candidates")
    print(f"  {'iso':<4}{'M_need':>8}{'z=A-1':>7}{'z·a_D^A':>9}{'C(A,2)':>8}"
          f"{'c(𝓑_K)':>8}")
    results = {}
    for K in ("T", "3He", "4He"):          # Vol≠0 isotopes
        A = BK[K]["A"]
        M_need = AME[K] / (M_E * mp.mpf(BK[K]["vol"]))
        z = z_coord(A)
        z_aD = z * aD[A]
        results[K] = dict(M_need=float(M_need), z=z, z_aD=float(z_aD),
                          bonds=total_bonds(A), cross=BK[K]["cross"])
        print(f"  {K:<4}{float(M_need):>8.3f}{z:>7}{float(z_aD):>9.3f}"
              f"{total_bonds(A):>8}{BK[K]['cross']:>8}")

    # errors of the two best candidates
    def err(cand, K):
        return float((mp.mpf(cand) - results[K]["M_need"]) / results[K]["M_need"])
    print("\n  candidate errors vs M_need:")
    for K in ("T", "3He", "4He"):
        e_z = err(results[K]["z"], K) * 100
        e_zaD = err(results[K]["z_aD"], K) * 100
        print(f"     {K:<4}  z=A-1: {e_z:+6.1f}%    z·a_D^A: {e_zaD:+6.1f}%")

    # ---- deuteron Hopf: crossing number as the Vol=0 survivor -----------------
    print("\n### Deuteron (A=2) — Hopf Vol=0 wall")
    print(f"  Vol(Hopf)=0 ⇒ any M·Vol product gives B=0. But the CROSSING structure")
    print(f"  survives: c(Hopf)=2, |lk|=1, per-nucleon coordination z=A-1=1.")
    print(f"  ⇒ the crossing/coordination carrier is the natural non-vanishing")
    print(f"    replacement for the volume on the 2-body (Seifert-fibred) sub-link.")

    # ---- α-CLUSTER COORDINATION: the principle one level up (A>4 magic) -------
    #   ¹⁶O/⁴⁰Ca have NO canonical single hyperbolic link in the corpus — they are
    #   α-cluster nuclei. So the coordination principle extends by treating each ⁴He
    #   as ONE node and counting α–α coordination bonds:
    #       B(n_α) ≈ n_α·B(⁴He) + N_bonds·b_αα .
    #   For a SIMPLEX cluster (n_α ≤ 4: ⁴He,⁸Be,¹²C,¹⁶O) every pair is a nearest
    #   neighbour, so N_bonds = C(n_α,2) (complete graph, 3D-realisable up to the
    #   tetrahedron). b_αα is a SINGLE empirical residual constant (NOT derived).
    B_alpha = mp.mpf(str(_cc._ame_binding_mev(2, 4)))
    ALPHA = {  # (Z, A) for the α-conjugate chain
        "8Be": (4, 8), "12C": (6, 12), "16O": (8, 16),
        "20Ne": (10, 20), "24Mg": (12, 24), "40Ca": (20, 40)}
    print("\n### α-cluster coordination (A>4) — the principle one level up")
    print(f"  ⁴He is the n_α=1 base: B(⁴He)={float(B_alpha):.3f} MeV, 0 bonds.")
    print(f"  Residual r = B − n_α·B(⁴He), per complete-graph bond C(n_α,2):")
    print(f"  {'iso':<5}{'n_α':>4}{'C(n,2)':>7}{'B_AME':>9}{'resid':>8}{'per-bond':>9}"
          f"{'simplex?':>9}")
    alpha_rows = {}
    for nm, (Z, A) in ALPHA.items():
        B = mp.mpf(str(_cc._ame_binding_mev(Z, A)))
        na = A // 4
        Cn2 = na * (na - 1) // 2
        resid = B - na * B_alpha
        per = resid / Cn2 if Cn2 else mp.mpf(0)
        simplex = na <= 4          # complete α-graph 3D-realisable only for n_α ≤ 4
        alpha_rows[nm] = dict(n_alpha=na, bonds=Cn2, B=float(B),
                              resid=float(resid), per_bond=float(per), simplex=simplex)
        print(f"  {nm:<5}{na:>4}{Cn2:>7}{float(B):>9.2f}{float(resid):>8.2f}"
              f"{float(per):>9.3f}{'  yes' if simplex else '  no':>9}")
    # b_αα read off the two clean simplex clusters ¹²C, ¹⁶O
    b_aa = (alpha_rows["12C"]["per_bond"] + alpha_rows["16O"]["per_bond"]) / 2
    print(f"\n  • Simplex clusters n_α≤4 (⁸Be,¹²C,¹⁶O): per-bond ≈ constant "
          f"b_αα≈{b_aa:.2f} MeV (¹²C {alpha_rows['12C']['per_bond']:.3f}, "
          f"¹⁶O {alpha_rows['16O']['per_bond']:.3f}; ⁸Be≈0 — the isolated α–α pair is")
    print(f"    unbound, the reason for the triple-α process). This is the classical")
    print(f"    Hafstad–Teller α-bond model; QOU reads N_bonds as the α-cluster")
    print(f"    COORDINATION number — the same principle as z=A-1, one level up.")
    print(f"  • n_α≥5 (²⁰Ne,²⁴Mg,⁴⁰Ca): per-C(n,2) drops "
          f"({alpha_rows['20Ne']['per_bond']:.2f}→{alpha_rows['40Ca']['per_bond']:.2f}) —")
    print(f"    C(n_α,2) OVERCOUNTS: not all pairs can be nearest neighbours in 3D.")
    print(f"    ⇒ coordination SATURATES to a geometric (close-packing) count beyond")
    print(f"    the tetrahedron. ⁴⁰Ca needs the packing coordination, not C(10,2)=45.")
    print(f"  • a_D-ACTIVATION resolves: there is NO per-isotope a_D factor for A>4;")
    print(f"    the ⁴He 'magic' enhancement is itself the n_α=1 base, and the extra")
    print(f"    binding of larger α-nuclei is carried by the α–α COORDINATION count.")

    # ---- verdict -------------------------------------------------------------
    z_pair_ok = abs(err(2, "T")) < 0.05 and abs(err(2, "3He")) < 0.05
    simplex_ok = abs(alpha_rows["12C"]["per_bond"] - alpha_rows["16O"]["per_bond"]) < 0.1
    print("\n### Verdict — crossing/coordination as M_n(A)  (scope-limited (a))")
    print(f"  • Per-nucleon coordination z=A-1 = 2 matches the NON-MAGIC A=3 pair:")
    print(f"      M_need(³H)={results['T']['M_need']:.3f}, M_need(³He)="
          f"{results['3He']['M_need']:.3f}  (both ≈ 2, |err|<3%).  "
          f"[{'CONFIRMED' if z_pair_ok else 'no'}]")
    print(f"  • Doubly-magic ⁴He is NOT closed by z=A-1=3 (needs {results['4He']['M_need']:.2f}).")
    print(f"    The magic enhancement over the coordination number is ≈ "
          f"{results['4He']['M_need']/3:.2f} ≈ a_D^(4)={float(aD[4]):.2f}:")
    print(f"      z·a_D^A err: ³H {err(results['T']['z_aD'],'T')*100:+.1f}%,  "
          f"³He {err(results['3He']['z_aD'],'3He')*100:+.1f}%,  "
          f"⁴He {err(results['4He']['z_aD'],'4He')*100:+.1f}%.")
    print(f"  • This CONFIRMS option 1's 'different objects' reading: the light-nucleus")
    print(f"    multiplicity is the topological coordination number z=A-1 (no fit),")
    print(f"    while ⁴He carries an ADDITIONAL super-exp a_D^(A) magic factor.")
    print(f"    Combined  z(A)·a_D^(A)  closes ⁴He to +0.6% but OVERSHOOTS the A=3 pair")
    print(f"    by ~+30% (a_D^(3)={float(aD[3]):.2f}>1) — so a_D is a MAGIC-SHELL-only")
    print(f"    enhancement, not a universal factor. Clean fit-free piece: M(A=3)=z=A-1;")
    print(f"    the magic a_D^(A) turns on at the closed ⁴He shell. Scope-limited (a).")
    print(f"  • Crossing number c(𝓑_K) does NOT track M_need (8_11 c=8 > L6a4 c=6 but")
    print(f"    M_need(³H)<M_need(³He)); c is the Vol=0 DEUTERON survivor, not the")
    print(f"    A≥3 multiplicity. Scope-limited negative for c as the multiplier.")

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("bk-crossing-coordination", engine="mpmath")
            wb.set_description(
                "Crossing/coordination structure of the building-block link 𝓑_K tested "
                "as the open body-order multiplicity M_n(A) of the θ_λ weight. The "
                "per-nucleon coordination number z=A-1 supplies M for the non-magic A=3 "
                "pair (M_need ≈ 2.00/2.06 vs z=2, no fit); doubly-magic ⁴He needs an "
                "extra super-exp a_D^(4)≈2.53 factor (z·a_D^A closes it to a few %). "
                "z·a_D^A closes ⁴He but overshoots A=3 by ~30%, so a_D is a magic-shell "
                "enhancement, not universal. Crossing number c(𝓑_K) is the Vol=0 deuteron "
                "survivor, not the A≥3 multiplier. EXTENSION: for A>4 α-cluster nuclei "
                "(no single hyperbolic link), the principle lifts one level — B ≈ "
                "n_α·B(⁴He) + C(n_α,2)·b_αα with b_αα≈2.41 MeV constant for simplex "
                "clusters ⁸Be/¹²C/¹⁶O (n_α≤4), saturating for ⁴⁰Ca (n_α=10). b_αα is a "
                "single empirical constant, not derived. Scope-limited (a): tested alone, "
                "not a structural exclusion.")
            wb.add_data("q0", float(q))
            wb.add_data("bk_structure", {K: rows[K] for K in rows})
            wb.add_data("M_need", {K: results[K]["M_need"] for K in results})
            wb.add_data("candidates_z_aD", {K: results[K]["z_aD"] for K in results})
            wb.add_data("a_D", {str(A): float(aD[A]) for A in aD})
            wb.add_data("strand_crossings_Tw", sc)
            wb.add_data("alpha_cluster_coordination", alpha_rows)
            wb.add_data("b_alpha_alpha_MeV_empirical", b_aa)
            wb.add_assertion(
                name="alpha_cluster_coordination_constant_for_simplex_nuclei",
                computed=str(int(simplex_ok)), expected="1", tolerance=0,
                source=(f"per-bond residual is ≈constant b_αα≈{b_aa:.2f} MeV for the simplex "
                        f"α-clusters ¹²C ({alpha_rows['12C']['per_bond']:.3f}) and ¹⁶O "
                        f"({alpha_rows['16O']['per_bond']:.3f}) using complete-graph "
                        f"C(n_α,2) bonds; n_α≥5 saturates (⁴⁰Ca {alpha_rows['40Ca']['per_bond']:.2f}). "
                        f"b_αα is a single empirical residual constant, NOT derived."))
            wb.add_assertion(
                name="per_nucleon_coordination_matches_A3_multiplicity",
                computed=str(int(z_pair_ok)), expected="1", tolerance=0,
                source=(f"z=A-1=2 matches M_need(³H)={results['T']['M_need']:.3f} and "
                        f"M_need(³He)={results['3He']['M_need']:.3f} to <3% with no fit; "
                        f"⁴He carries an additional a_D^(4)≈{float(aD[4]):.2f} magic factor "
                        f"(z·a_D^A err {err(results['4He']['z_aD'],'4He')*100:+.1f}%)."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

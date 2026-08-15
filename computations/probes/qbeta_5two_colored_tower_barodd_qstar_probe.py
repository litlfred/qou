#!/usr/bin/env python3
"""A5.1 (bean qou-3yxn): the categorical colored tower of 5₂ via Masbaum's
twist-knot formula — build, gate, and run the q*-zero test on the bar-odd
tower datum at the substrate.

WHY. A3 falsified the analytic NZ-saddle datum as the capstone carrier
(no zero at q*; a smooth prefactor cannot manufacture one), narrowing the
Im 𝔙_q → N_odd carrier search to the CATEGORICAL colored-trace face. This
probe builds that face exactly, from the owner-supplied Masbaum paper
(library/0306345v1/0306345v1.pdf, arXiv:math/0306345), and asks the same
falsification question: does the bar-odd tower datum
    B_N(q) := [J'_N(q) − J'_N(1/q)] / 2      (bar involution = mirror)
have a zero crossing at (or near) q* — capstone constraint (2)?

CONSTRUCTION (Masbaum Thm 5.1 + Rmk 5.2 + §5 Example, transcribed exactly;
5₂ = K₂ in the twist-knot family K_p, K₁ = left trefoil, K₋₁ = 4₁; q = a²):

    J'_{K_p}(N) = Σ_{n<N} f̃_{K_p,n} · (q^{1−N};q)_n (q^{1+N};q)_n     (Rmk 5.2)
    f̃_{K_p,n} = (−1)^n q^{−n(n+1)/2} f_{K_p,n},  f_{K_p,n} = a^{n(n+3)/2} c'_{n,p}
    c'_{n,2}  = (−1)^n a^{(5n²+7n)/2} Σ_{k=0}^n a^{k²−2k−3nk} [n;k]      (§5 Ex, p=2)
    [n;k] = [n][n−1]···[n−k+1]/[k]!,  [m] = (a^{2m}−a^{−2m})/(a²−a^{−2})

Symbolic plumbing check (done during authoring, asserted numerically here):
c'_{n,1} = (−1)^n a^{n(n+3)/2} ⇒ f̃_{K₁,n} = q^n ✓ and c'_{n,−1} = a^{−n(n+3)/2}
⇒ f̃_{K₋₁,n} = (−1)^n q^{−n(n+1)/2} ✓ — both exactly the printed Rmk 5.2 values.

Each J'_N costs O(N²) — the tower reaches N ≈ 150 (an earlier R-matrix
attempt at O(N⁸) failed its own braid-relation gate and was discarded
pre-commit; gates exist to catch exactly that).

STATUS AFTER VALIDATION (2026-07-18) — **the p=2 tower FAILS external
validation at N ≥ 3, and this probe certifies the DISCREPANCY, not the
tower.** The gate battery caught it:

  • G1 (N=2 = corpus TL₃ Jones, 1e-41), G2 (p=±1 plumbing = Rmk 5.2), G3
    (amphichiral 4₁ bar-odd null, 1e-30) all PASS; the p=−1 (4₁) tower also
    reproduces the PROVEN volume-conjecture growth (measured − 3π·logN/N →
    2.0299 = Vol(4₁) at N=20..80) — the assembly machinery is validated.
  • But the p=2 (K₂ = 5₂) tower at the Kashaev points contradicts the
    independent GZ 2111.06645 eq (7.9) double-sum for ⟨5₂⟩ (which itself
    converges cleanly to Vol(5₂): 2.71, 2.76, 2.80 after the 3π·logN/N
    subtraction): moduli differ already at N=3 (16.093 vs 20.952) and the
    ratio diverges exponentially (13× at N=20, 3.6e4× at N=80); my tower's
    growth constant extrapolates to ≈ 2.03, not 2.828 — impossible for the
    true J'_N(5₂) since the VC for 5₂ is a theorem.
  • Eliminated: c'_{n,2} transcription (the §5 Example ≡ the independent
    §4 skein composition eq36+eq40+eq43+μ²_m=a^{m²+2m} to 1e-31 at n ≤ 5;
    eq-44 and the whole p=1 chain verified symbolically); mirror variants
    (a→1/a in c' and/or f) do not match GZ either; K₂'s identity as 5₂
    (its N=2 Jones IS V(5₂), and the twist-knot table pins K₂ = 5₂).
  ⇒ Either a subtle transcription error upstream of both my routes (the §4
    composition display), or a genuine literature discrepancy in the
    Masbaum Thm-5.1 p ≥ 2 assembly. OPEN — needs independent arbitration
    (e.g. an N=3 colored Jones of 5₂ via TL 2-cabling).

THE q*-TEST (fine scan of B_N across q* ± 2e-8, N = 3..8, 16, 32) is
therefore reported as an UNCERTIFIED DIAGNOSTIC ONLY — its "no zero"
outcome cannot be attributed to 5₂ until the tower discrepancy is resolved.
No falsification claim is made. auditOnly; no c_k wired; no fit.

Run: python3 -u computations/probes/qbeta_5two_colored_tower_barodd_qstar_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_colored_tower.log
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40
Q_MUON = mp.mpf("1.10997859555733471")
Q_PROTON = mp.mpf("1.1099785827513808075916690956107688798744991218736")
Q_STAR = mp.mpf("1.10997859303152")
VOL_5_2 = mp.mpf("2.8281220883307832")


def qbracket(m, a):
    """[m] = (a^{2m} − a^{−2m})/(a² − a^{−2})."""
    return (a ** (2 * m) - a ** (-2 * m)) / (a ** 2 - a ** -2)


def qbinom(n, k, a):
    """[n;k] = [n][n−1]···[n−k+1]/[k]!."""
    num = mp.mpf(1) if not isinstance(a, mp.mpc) else mp.mpc(1)
    for t in range(k):
        num *= qbracket(n - t, a)
    den = num * 0 + 1
    for t in range(1, k + 1):
        den *= qbracket(t, a)
    return num / den


def c_prime(n, p, a):
    """c'_{n,p}: p=1, −1 closed forms (Masbaum eq before (35)); p=2 from the
    §5 Example. Other p not needed here."""
    if p == 1:
        return (-1) ** n * a ** (n * (n + 3) / 2)
    if p == -1:
        return a ** (-n * (n + 3) / 2)
    if p == 2:
        s = a * 0
        for k in range(n + 1):
            s += a ** (k * k - 2 * k - 3 * n * k) * qbinom(n, k, a)
        return (-1) ** n * a ** ((5 * n * n + 7 * n) / 2) * s
    raise ValueError(p)


def f_tilde(n, p, a):
    """f̃_{K_p,n} = (−1)^n q^{−n(n+1)/2}·a^{n(n+3)/2}·c'_{n,p},  q = a²."""
    return (-1) ** n * a ** (-n * (n + 1)) * a ** (n * (n + 3) / 2) * c_prime(n, p, a)


def J_twist(N, p, q):
    """J'_{K_p}(N) at q (Rmk 5.2): Σ_{n<N} f̃_n (q^{1−N})_n (q^{1+N})_n."""
    a = mp.sqrt(q)
    total = q * 0
    poch_m = q * 0 + 1     # (q^{1−N};q)_n running
    poch_p = q * 0 + 1     # (q^{1+N};q)_n running
    for n in range(N):
        if n > 0:
            poch_m *= (1 - q ** (1 - N) * q ** (n - 1))
            poch_p *= (1 - q ** (1 + N) * q ** (n - 1))
        total += f_tilde(n, p, a) * poch_m * poch_p
    return total


def gz79(N):
    """GZ 2111.06645 eq (7.9): ⟨5₂⟩ = Σ_{m,k≤m} q^{−(m+1)k}(q;q)_m²/(q⁻¹;q⁻¹)_k
    at q = e^{2πi/N} — the independent arbiter (converges to the proven VC)."""
    q = mp.e ** (2j * mp.pi / N)
    tot = mp.mpc(0)
    for m in range(N):
        qm = mp.mpc(1)
        for j in range(1, m + 1):
            qm *= (1 - q ** j)
        for k in range(m + 1):
            qk = mp.mpc(1)
            for j in range(1, k + 1):
                qk *= (1 - q ** -j)
            tot += q ** (-(m + 1) * k) * qm ** 2 / qk
    return tot


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" A5.1 — 5₂ colored tower (Masbaum K₂): gates + the GZ-(7.9) discrepancy")
    print("=" * 78)

    # ---- G1: N=2 vs the corpus-validated Jones (both knots) ----
    def V41_known(q):
        return q**4 - q**2 + 1 - q**-2 + q**-4

    def V52_known(q):
        return -q**12 + q**10 - q**8 + 2 * q**6 - q**4 + q**2

    g1_ok = True
    print("\n[G1] N=2 vs corpus TL₃ Jones (mirror-tolerant, t-variable-tolerant):")
    for qt in (mp.mpf("1.13"), mp.mpf("0.91"), mp.mpf("1.037")):
        j41 = J_twist(2, -1, qt)
        j52 = J_twist(2, 2, qt)
        # corpus polys are in the QOU q-convention (t = q²); Masbaum's q is the
        # classical t. Compare against known at BOTH variable readings + mirror.
        cand41 = [V41_known(qt), V41_known(mp.sqrt(qt))]
        cand52 = [V52_known(qt), V52_known(1 / qt),
                  V52_known(mp.sqrt(qt)), V52_known(1 / mp.sqrt(qt))]
        e41 = min(abs(j41 - c) / abs(c) for c in cand41)
        e52 = min(abs(j52 - c) / abs(c) for c in cand52)
        g1_ok &= (e41 < mp.mpf("1e-25") and e52 < mp.mpf("1e-25"))
        print(f"    q={qt}: 4₁ best rel err {mp.nstr(e41,3)}; 5₂ best rel err {mp.nstr(e52,3)}")
    print(f"    {'PASS' if g1_ok else 'FAIL'}")

    # ---- G2: p=±1 plumbing identities ----
    g2_ok = True
    a_t = mp.mpf("1.0731")
    for n in range(0, 8):
        lhs1 = f_tilde(n, 1, a_t)
        rhs1 = (a_t ** 2) ** n                                   # q^n
        lhsm = f_tilde(n, -1, a_t)
        rhsm = (-1) ** n * (a_t ** 2) ** (-n * (n + 1) / 2)      # (−1)^n q^{−n(n+1)/2}
        g2_ok &= abs(lhs1 - rhs1) / abs(rhs1) < mp.mpf("1e-30")
        g2_ok &= abs(lhsm - rhsm) / abs(rhsm) < mp.mpf("1e-30")
    print(f"\n[G2] p=±1 plumbing: f̃_{{K₁,n}}=q^n, f̃_{{K₋₁,n}}=(−1)^n q^{{−n(n+1)/2}} "
          f"(n=0..7): {'PASS' if g2_ok else 'FAIL'}")

    # ---- G3: amphichiral NULL — B_N(4₁) = 0 ----
    print("\n[G3] amphichiral null B_N(4₁) at q₀:")
    g3_ok = True
    for N in (2, 3, 4, 6, 8, 10):
        va = J_twist(N, -1, Q_MUON)
        vb = J_twist(N, -1, 1 / Q_MUON)
        rel = abs(va - vb) / abs(va)
        g3_ok &= rel < mp.mpf("1e-30")
        print(f"    N={N:>2}: |J(q₀)−J(1/q₀)|/|J| = {mp.nstr(rel, 3)}")
    print(f"    {'PASS' if g3_ok else 'FAIL'}  (structural mirror/bar control)")

    # ---- G4a: 4₁ VC control — validates the assembly machinery ----
    print("\n[G4a] 4₁ VC control: (2π/N)log|J'_N(4₁)| − 3π·logN/N → Vol(4₁)=2.0299:")
    ctrl = []
    for N in (20, 40, 80):
        qk = mp.e ** (2j * mp.pi / N)
        v = 2 * mp.pi * mp.log(abs(J_twist(N, -1, qk))) / N - \
            3 * mp.pi * mp.log(N) / N
        ctrl.append(float(v))
        print(f"    N={N:>3}: {float(v):.4f}")
    g4a_ok = all(ctrl[i + 1] > ctrl[i] for i in range(len(ctrl) - 1)) and \
        abs(ctrl[-1] - 2.0299) < 0.05
    print(f"    increasing toward 2.0299: {'PASS' if g4a_ok else 'FAIL'}")

    # ---- G4b: THE DISCREPANCY — K₂ tower vs GZ (7.9) at Kashaev points ----
    print("\n[G4b] p=2 tower vs the independent GZ eq-(7.9) ⟨5₂⟩ (the arbiter):")
    growth = []
    disc = {}
    Ns = (20, 40, 80, 150)
    for N in Ns:
        qk = mp.e ** (2j * mp.pi / N)
        jk = J_twist(N, 2, qk)
        v = 2 * mp.pi * mp.log(abs(jk)) / N
        growth.append(float(v))
        if N <= 80:
            g = gz79(N)
            vg = float(2 * mp.pi * mp.log(abs(g)) / N - 3 * mp.pi * mp.log(N) / N)
            ratio = float(abs(g) / abs(jk))
            disc[N] = {"gz_growth_sub": vg, "ratio_gz_over_tower": ratio}
            print(f"    N={N:>3}: tower−3πlogN/N = "
                  f"{float(v)-float(3*mp.pi*mp.log(N)/N):.4f}   GZ−3πlogN/N = {vg:.4f}"
                  f"   |GZ|/|tower| = {ratio:.4g}")
    tower_sub_150 = growth[-1] - float(3 * mp.pi * mp.log(150) / 150)
    # the discrepancy is CONFIRMED when GZ tracks Vol(5₂) while the tower does
    # not, and the ratio diverges
    g4b_disc = (abs(disc[80]["gz_growth_sub"] - 2.828) < 0.1
                and tower_sub_150 < 2.2
                and disc[80]["ratio_gz_over_tower"] > 100)
    print(f"    tower(N=150)−3πlogN/N = {tower_sub_150:.4f} (≈2.03, NOT 2.828); "
          f"discrepancy {'CONFIRMED' if g4b_disc else 'not confirmed — inspect'}")

    # ---- UNCERTIFIED DIAGNOSTIC: B_N zero-scan at q* (see docstring) ----
    print("\n[T — UNCERTIFIED DIAGNOSTIC] bar-odd tower datum B_N(q), q* ± 2e-8:")
    half = mp.mpf("2e-8")
    npts = 9
    grid = [Q_STAR - half + 2 * half * i / (npts - 1) for i in range(npts)]
    t_res = {}
    no_zero_all = True
    for N in (3, 4, 5, 6, 7, 8, 16, 32):
        vals = []
        for qq in grid:
            B = (J_twist(N, 2, qq) - J_twist(N, 2, 1 / qq)) / 2
            vals.append(B)
        sc = sum(1 for x, y in zip(vals, vals[1:])
                 if mp.sign(x) != mp.sign(y))
        B_mu = (J_twist(N, 2, Q_MUON) - J_twist(N, 2, 1 / Q_MUON)) / 2
        B_pr = (J_twist(N, 2, Q_PROTON) - J_twist(N, 2, 1 / Q_PROTON)) / 2
        rel_slope = float(abs(B_mu - B_pr) / abs(B_mu) / (Q_MUON - Q_PROTON))
        t_res[N] = {"B_qstar": vals[npts // 2], "sign_changes": sc,
                    "rel_slope": rel_slope}
        no_zero_all &= (sc == 0 and abs(vals[npts // 2]) > 0)
        print(f"    N={N:>2}: B(q*) = {mp.nstr(vals[npts//2], 6):>14}  "
              f"sign changes = {sc}  |d ln B/dq| ≈ {rel_slope:.3e}")
    max_rel_slope = max(r["rel_slope"] for r in t_res.values())
    smooth = max_rel_slope < 1e5
    print(f"\n    diagnostic only: {'no zero found' if no_zero_all else 'zero found'}"
          f"; max rel slope {max_rel_slope:.3e} — NOT attributable to 5₂ until the "
          "tower discrepancy is resolved")

    print("\n  VERDICT: the gate battery + the GZ-(7.9) arbiter CONFIRM a discrepancy")
    print("  in the Masbaum Thm-5.1 p=2 assembly as transcribed: N=2 Jones exact,")
    print("  p=±1 exact (incl. the proven 4₁ VC growth), §4 chain self-consistent —")
    print("  yet the p=2 tower diverges from the independent ⟨5₂⟩ (GZ eq 7.9, which")
    print("  tracks the PROVEN Vol(5₂)) already at N=3. OPEN: literature/transcription")
    print("  arbitration needed (N=3 via TL 2-cabling). The q*-scan stays uncertified;")
    print("  no falsification claim is made. Bean qou-3yxn stays open, blocked here.")

    wb = WitnessBuilder("qbeta-5two-colored-tower-barodd-qstar",
                        engine="mpmath", _script_path=__file__)
    wb.set_description(
        "A5.1 (bean qou-3yxn): the Masbaum math/0306345 Thm-5.1 twist-knot "
        "tower at p=2 (K₂ = 5₂) FAILS external validation at N ≥ 3, and this "
        "witness certifies the DISCREPANCY: gates pass (N=2 = corpus TL₃ "
        "Jones at 1e-41; p=±1 plumbing = Rmk 5.2; amphichiral 4₁ bar-odd "
        "null at 1e-30; 4₁ VC control reproduces the proven Vol(4₁)=2.0299 "
        "growth), the §5-Example c'_{n,2} ≡ the independent §4 skein "
        "composition to 1e-31, yet the p=2 tower contradicts the independent "
        "GZ 2111.06645 eq-(7.9) ⟨5₂⟩ already at N=3 (16.09 vs 20.95) with "
        "exponentially diverging ratio, and its growth constant ≈ 2.03 ≠ "
        "Vol(5₂) = 2.828 (the VC for 5₂ is a theorem; GZ-(7.9) tracks it). "
        "Mirror variants eliminated. OPEN: transcription-vs-literature "
        "arbitration needed. The B_N q*-scan is recorded as an UNCERTIFIED "
        "diagnostic; no capstone falsification is claimed on this face. "
        "auditOnly; no c_k wired; no fit.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("gate_N2_equals_corpus_jones",
                     computed=1.0 if g1_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="J'_2(K₋₁), J'_2(K₂) reproduce the validated TL₃ V(4₁), "
                            "V(5₂) (variable/mirror-tolerant) at 3 q-points")
    wb.add_assertion("gate_p_pm1_plumbing",
                     computed=1.0 if g2_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="f̃_{K₁,n}=q^n and f̃_{K₋₁,n}=(−1)^n q^{−n(n+1)/2} "
                            "(Masbaum Rmk 5.2) from the same c'-machinery as p=2")
    wb.add_assertion("gate_amphichiral_41_null",
                     computed=1.0 if g3_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="B_N(4₁) = 0 to 1e-30 for N ≤ 10 — mirror/bar control")
    wb.add_assertion("gate_41_vc_control",
                     computed=1.0 if g4a_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="4₁ tower growth − 3π·logN/N increasing toward the proven "
                            "Vol(4₁) = 2.0299 (N=20..80) — assembly machinery validated")
    wb.add_assertion("p2_tower_vs_gz79_discrepancy_confirmed",
                     computed=1.0 if g4b_disc else 0.0, expected=1.0, tolerance=0.5,
                     source="GZ eq-(7.9) tracks Vol(5₂)=2.828 while the p=2 tower's "
                            "growth constant ≈ 2.03 and |GZ|/|tower| > 100 at N=80 — "
                            "the Thm-5.1 p=2 assembly (as transcribed) is NOT J'_N(5₂)")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("source", "Masbaum math/0306345 (library/0306345v1/0306345v1.pdf) Thm 5.1, "
                          "Rmk 5.2, §5 Example (p=2); arbiter: GZ 2111.06645 eq (7.9)")
    wb.add_data("kashaev_growth_tower", {str(N): f"{v:.6f}"
                                         for N, v in zip(Ns, growth)})
    wb.add_data("gz79_discrepancy", {str(N): {"gz_growth_sub3pilogN": f"{d['gz_growth_sub']:.4f}",
                                              "ratio_gz_over_tower": f"{d['ratio_gz_over_tower']:.4g}"}
                                     for N, d in disc.items()})
    wb.add_data("eliminated", ["c'_{n,2} transcription (Example = skein composition, 1e-31)",
                               "mirror variants a->1/a in c' and/or f",
                               "K₂ identity (N=2 Jones = V(5₂) exactly)",
                               "assembly machinery (p=-1 gives proven 4₁ VC growth)"])
    wb.add_data("qstar_scan_UNCERTIFIED_diagnostic",
                {str(N): {"B_qstar": mp.nstr(r["B_qstar"], 10),
                          "sign_changes": r["sign_changes"],
                          "rel_slope": f"{r['rel_slope']:.4e}"}
                 for N, r in t_res.items()})
    wb.add_data("verdict",
                ("DISCREPANCY CERTIFIED, TOWER NOT: the Masbaum Thm-5.1 p=2 "
                 "assembly (as transcribed, with every cheaper explanation "
                 "eliminated) contradicts the independent GZ eq-(7.9) ⟨5₂⟩ and "
                 "the proven VC. The categorical-face q*-test stays OPEN pending "
                 "arbitration (N=3 TL 2-cable). No falsification claim; bean "
                 "qou-3yxn blocked here. This is the session's third caught "
                 "literature/transcription fault (GGM τ², A2 towers-vs-entries, "
                 "now Thm-5.1 p=2)."
                 if ok else "GATES FAILED — inspect before trusting even the "
                            "discrepancy claim."))
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-t0:.0f}s)")
    print("  witness -> computations/probes/qbeta-5two-colored-tower-barodd-qstar.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

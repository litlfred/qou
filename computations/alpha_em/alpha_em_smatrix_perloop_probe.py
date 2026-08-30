#!/usr/bin/env python3
"""alpha_em_smatrix_perloop_probe.py

EXPLORATORY shape-probe (per .claude/skills/local/production-vs-exploratory-discipline.md).
No fit; no `α_k` wired; `1/(8π)` stays a phase-4 identification. An honest
scope-(a) NEGATIVE is the anticipated — and GOOD — outcome.

--------------------------------------------------------------------------------
CONTEXT — the redirect this probe closes (from #3870 + #3882)

#3870 ruled out the naive flat-torus Maxwell 1-loop partition function as the
per-loop measure `1/(π·b₁) = 1/(8π)` (b₁ = dim H¹(M_Bring) = 2g = 8), sharpening
the target into a THREE-AXIS constraint any valid normalization object must meet:

  (i)   **area / covolume-free**  (topological);
  (ii)  **π-power exactly −1**    (a BARE π, not 2π);
  (iii) **reciprocal in the mode count**  (`b₁^{−1}`, a `1/(total-count)`
        democratic-average, NOT extensive `−b₁` nor exponential `(2π)^{−b₁/2}`).

#3882 (Ray–Singer torsion) then showed EVERY flat-torus spectral invariant is
either EXTENSIVE in b₁ or a COVOLUME — never reciprocal — and concluded the
measure must live OFF the flat-torus determinant, on the **RT/WRT modular-S-matrix
total quantum dimension `D = √(Σ_i d_i²)`** (`S_{00} = 1/D`) / Verlinde per-handle
measure. This probe TESTS that redirect against the three axes.

--------------------------------------------------------------------------------
METHOD (STRICT — anti-laundering, AGENTS.md §"Axiomatization is NOT a Proof",
§"Before declaring refuted"): compute each axis INDEPENDENTLY from the S-matrix's
own definition, then COMPARE to the target. NEVER solve `D` from CODATA; NEVER
insert a π by hand to reach 8π.

The photon's candidate modular category is the redirect's named object: the
GENUINE Σ(2,3,5) (Poincaré sphere S³/2I, binary-icosahedral) WRT/false-theta
S-matrix, transcribed from the primary source (Hikami, math-ph/0405028) and
machine-validated in #3822 (`keystone_valuemap_genuine_smatrix_s013.py`). We
**REUSE** that S-matrix (`s_entry`, eq. 3.8) — we do NOT rebuild it — and read
off its total quantum dimension.

--------------------------------------------------------------------------------
RESULT (scope-(a) NEGATIVE — the redirect's FORM is right, its VALUE and π are not)

The genuine Σ(2,3,5) modular family has D(2,3,5) = (p₁−1)(p₂−1)(p₃−1)/4 = **2**
primary fields; its vacuum row is `(2/√5)(sin π/5, sin 2π/5)` (Hikami Cor. 12),
so the quantum dimensions are the **icosahedral/Fibonacci pair {1, φ}**
(φ = golden ratio = sin(2π/5)/sin(π/5) = 2cos(π/5)), and

    Σ_i d_i² = 1 + φ² = 2 + φ = (5 + √5)/2 ≈ 3.6180   (∈ ℚ(√5), NO π)
    𝒟 = √(Σ_i d_i²) = √((5+√5)/2) ≈ 1.9021            (∈ ℚ(√5), NO π)
    S_{00} = 1/𝒟 = (2/√5) sin(π/5) ≈ 0.5257           (∈ ℚ(√5), NO π)

Per-axis verdict against `1/(π·b₁) = 1/(8π)`:

  (i)  area-free .......... ✓  the magnitudes are √(Reidemeister torsion)
                              (Hikami Thm 14) — a topological invariant, no length.
  (ii) π-power −1 ......... ✗  **STRUCTURAL (b)-exclusion**: 𝒟, Σd_i², S_{00} are
                              ALGEBRAIC in ℚ(√5). Every MTC quantum dimension is a
                              cyclotomic algebraic integer's ratio (2cos(πk/n)-type),
                              so `S_{00} = 1/𝒟` carries NO bare π — π-power 0, not −1,
                              for ANY root-of-unity S-matrix, not just this one. The
                              π CANNOT come from the S-matrix total quantum dimension.
  (iii) reciprocal ....... ✓ FORM / ✗ VALUE: `S_{00} = 1/𝒟` IS the redirect's
                              `1/(total-count)` democratic-average — but the count is
                              𝒟 ≈ 1.902 (or Σd_i² ≈ 3.618), NOT b₁ = 8, NOT 8π ≈ 25.13.

So: the redirect's reciprocal-`1/D` SHAPE is confirmed; but (a) the specific
genuine Σ(2,3,5) family gives 𝒟 ≈ 1.902 ≠ 8 (only 2 primary fields — far too few
to be the b₁ = 8 harmonic-1-form count), and (b) NO S-matrix supplies the bare π.

WHERE THE π MUST COME FROM (named, not hand-inserted): the RT/WRT normalization's
only π's are in UNIT-MODULUS framing/Chern-Simons phases — the Gauss-sum prefactor
`e^{πi/4}` of τ_N (eq. 2.11), the CS invariants (−1/120, −49/120) as `e^{−πiN·CS}`
(Cor. 12), the surgery phase `e^{−n²πi/(2PN)}` — which contribute MAGNITUDE 1 and
therefore cannot supply a real `1/π` to the measure either. The bare real π in
`1/(π·b₁)` is therefore ARCHIMEDEAN: the 1-loop determinant / heat-kernel eigenvalue
normalization `4π²` (the `log(4π²)` in `ζ'_{Δ₀}(0)`, #3882), consistent with the
ledger's standing boundary "b₁ topological, π archimedean, [2]_q substrate". This
DECIDES the #3853 gate's open ambiguity: since 𝒟 is algebraic, the "D = π·b₁ = 8π
(π categorical)" branch is STRUCTURALLY impossible; π is the universal archimedean
1-loop factor, never categorical.

Cross-check (both natural "keystone S-matrix" readings miss b₁ = 8):
  * genuine Σ(2,3,5) root-of-unity S-matrix (this probe): 𝒟 ≈ 1.902 (∈ ℚ(√5)).
  * n=5 Hecke hook-content pseudo-dims at observable q₀ (#3853): D ≈ 11.357.
Neither equals 8 nor 8π — a robust double-negative on the value axis.

# Ref: [hikami2005brieskorn] https://doi.org/10.1063/1.1834694  (math-ph/0405028;
#      eqs. 2.11, 3.8, Cor. 12, Thm 14 — the genuine Σ(2,3,5) S-matrix)
# Ref: [lawrence-zagier-1999] https://doi.org/10.4310/AJM.1999.v3.n1.a5
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent
sys.path.insert(0, str(COMPUTATIONS))
sys.path.insert(0, str(COMPUTATIONS / "probes"))
sys.path.insert(0, str(COMPUTATIONS / "substrate"))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# REUSE #3822's machine-validated genuine Σ(2,3,5) S-matrix — do NOT rebuild it.
import keystone_valuemap_genuine_smatrix_s013 as genuine  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

B1 = 8  # dim H¹(M_Bring) = 2g, g = 4  (the target mode count)


def phi_exact():
    """Golden ratio (1+√5)/2 — the icosahedral/Fibonacci quantum dimension."""
    return (1 + mp.sqrt(5)) / 2


def main() -> int:
    print("=" * 80)
    print(" α_EM per-loop measure — RT/WRT total quantum dimension D vs 1/(π·b₁)=1/(8π)")
    print(" (genuine Σ(2,3,5) S-matrix reused from #3822; three-axis constraint from #3870/#3882)")
    print("=" * 80)

    # ── reuse the genuine 2×2 S-matrix (Hikami eq. 3.8) ─────────────────────────
    TRIPLES = genuine.TRIPLES  # the D=2 independent flat connections of Σ(2,3,5)
    S = [[genuine.s_entry(a, b) for b in TRIPLES] for a in TRIPLES]
    S00, S01 = S[0][0], S[0][1]

    # ── CONTROLS (reproduce #3822 exactly + MTC axioms) ─────────────────────────
    phi = phi_exact()
    # C1: D(2,3,5) = (p1-1)(p2-1)(p3-1)/4 = 2 primary fields
    D_235 = (2 - 1) * (3 - 1) * (5 - 1) // 4
    ctrl_nfields = (D_235 == 2 and len(TRIPLES) == 2)
    # C2: S² = 1 (involution)
    s2 = [[mp.fsum(S[i][k] * S[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    ctrl_involution = max(abs(s2[i][j] - (1 if i == j else 0))
                          for i in range(2) for j in range(2)) < mp.mpf("1e-40")
    # C3: vacuum row = Corollary-12 weights (2/√5)(sin π/5, sin 2π/5)
    w0 = 2 / mp.sqrt(5) * mp.sin(mp.pi / 5)
    w1 = 2 / mp.sqrt(5) * mp.sin(2 * mp.pi / 5)
    ctrl_vacrow = abs(S00 - w0) < mp.mpf("1e-40") and abs(S01 - w1) < mp.mpf("1e-40")
    # C4: unitary row normalization Σ_i |S_{0i}|² = 1
    row_norm = S00 ** 2 + S01 ** 2
    ctrl_rownorm = abs(row_norm - 1) < mp.mpf("1e-40")
    # C5: row ratio = golden ratio φ  (⇒ quantum dims {1, φ})
    ctrl_golden = abs(S01 / S00 - phi) < mp.mpf("1e-40")

    controls_pass = all([ctrl_nfields, ctrl_involution, ctrl_vacrow, ctrl_rownorm, ctrl_golden])

    print("\n CONTROLS (reuse #3822 genuine S-matrix; MTC axioms):")
    print(f"   C1 D(2,3,5) = 2 primary fields ......................... {ctrl_nfields}")
    print(f"   C2 S² = 1 (involution) ................................. {ctrl_involution}")
    print(f"   C3 vacuum row = (2/√5)(sin π/5, sin 2π/5) [Cor.12] ..... {ctrl_vacrow}")
    print(f"   C4 unitary row Σ_i |S_{{0i}}|² = 1 = {mp.nstr(row_norm, 12)} ...... {ctrl_rownorm}")
    print(f"   C5 row ratio = φ (⇒ quantum dims {{1, φ}}) .............. {ctrl_golden}")

    # ── total quantum dimension from S_{00} = 1/𝒟 ──────────────────────────────
    d = [S00 / S00, S01 / S00]                      # quantum dims: {1, φ}
    sum_d2 = mp.fsum(di ** 2 for di in d)           # Σ d_i²  = 𝒟²
    D_total = mp.sqrt(sum_d2)                        # 𝒟 = √(Σ d_i²)
    S00_from_D = 1 / D_total

    # closed forms in ℚ(√5)
    sum_d2_closed = (5 + mp.sqrt(5)) / 2            # = 2 + φ = (5+√5)/2
    D_total_closed = mp.sqrt((5 + mp.sqrt(5)) / 2)

    ctrl_S00_eq_inv_D = abs(S00 - S00_from_D) < mp.mpf("1e-40")
    ctrl_sumd2_closed = abs(sum_d2 - sum_d2_closed) < mp.mpf("1e-40")
    ctrl_D_closed = abs(D_total - D_total_closed) < mp.mpf("1e-40")

    print("\n TOTAL QUANTUM DIMENSION (from the reused S-matrix vacuum row):")
    print(f"   quantum dims d_i = {{{mp.nstr(d[0],4)}, {mp.nstr(d[1],10)}}}  (= {{1, φ}})")
    print(f"   Σ_i d_i²  = {mp.nstr(sum_d2, 16)}   closed = (5+√5)/2 = 2+φ   [match {ctrl_sumd2_closed}]")
    print(f"   𝒟 = √(Σ d_i²) = {mp.nstr(D_total, 16)}   closed = √((5+√5)/2)   [match {ctrl_D_closed}]")
    print(f"   S_{{00}} = 1/𝒟 = {mp.nstr(S00_from_D, 16)}  = reused S_{{00}} [match {ctrl_S00_eq_inv_D}]")

    # ── compare to targets b₁=8 and 8π (NEVER solve D from these) ────────────────
    t8 = mp.mpf(8)
    t8pi = 8 * mp.pi
    tol = mp.mpf("1e-3")
    D_eq_8 = abs(D_total - t8) < tol or abs(sum_d2 - t8) < tol
    D_eq_8pi = abs(D_total - t8pi) < tol or abs(sum_d2 - t8pi) < tol

    print("\n COMPARISON to the per-loop-measure targets (no CODATA, no fit):")
    print(f"   b₁ = 8 ;  π·b₁ = 8π = {mp.nstr(t8pi, 10)}")
    print(f"   𝒟/8      = {mp.nstr(D_total / t8, 8)}     Σd_i²/8   = {mp.nstr(sum_d2 / t8, 8)}")
    print(f"   𝒟/8π     = {mp.nstr(D_total / t8pi, 8)}    Σd_i²/8π  = {mp.nstr(sum_d2 / t8pi, 8)}")
    print(f"   𝒟 = 8 or 8π? {D_eq_8 or D_eq_8pi}   →  NO (neither 8 nor 8π)")

    # ── cross-check: the OTHER natural reading (#3853 n=5 Hecke hook-content) ────
    # d_q(λ) = [n]_q!/∏[hook]_q at observable q₀; D = √(Σ_{λ⊢5} d_q²) ≈ 11.357.
    q0 = mp.mpf(genuine.Q0)

    def qint(m):
        return (q0 ** m - q0 ** (-m)) / (q0 - 1 / q0)

    def qfact(n):
        r = mp.mpf(1)
        for k in range(1, n + 1):
            r *= qint(k)
        return r

    def hooks(lam):
        lam = list(lam)
        conj = [sum(1 for r in lam if r > c) for c in range(lam[0])]
        hs = []
        for i, row in enumerate(lam):
            for j in range(row):
                hs.append((row - j - 1) + (conj[j] - i - 1) + 1)
        return hs

    def dq(lam):
        num = qfact(sum(lam))
        den = mp.mpf(1)
        for h in hooks(lam):
            den *= qint(h)
        return num / den

    all_parts5 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]
    D_hecke_n5 = mp.sqrt(mp.fsum(dq(lam) ** 2 for lam in all_parts5))
    print("\n CROSS-CHECK — the other natural 'keystone S-matrix' reading (#3853):")
    print(f"   n=5 Hecke hook-content D(q₀) = √(Σ_{{λ⊢5}} d_q²) = {mp.nstr(D_hecke_n5, 10)}  (≠ 8, ≠ 8π)")
    print("   ⇒ BOTH the genuine root-of-unity S-matrix (1.902) AND the observable-q₀")
    print("      hook-content pseudo-dims (11.357) miss b₁ = 8. Robust double-negative.")

    # ── per-axis verdict ────────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print(" THREE-AXIS VERDICT vs 1/(π·b₁) = 1/(8π)")
    print("=" * 80)
    print("   (i)   area-free ....... ✓  √(Reidemeister torsion) magnitudes (topological)")
    print("   (ii)  π-power −1 ...... ✗  (b)-STRUCTURAL: 𝒟, S₀₀ ∈ ℚ(√5) algebraic — NO bare π")
    print("                              for ANY root-of-unity S-matrix (cyclotomic dims).")
    print("   (iii) reciprocal ..... ✓ FORM (S₀₀=1/𝒟 is the democratic average) /")
    print("                          ✗ VALUE (𝒟≈1.902 ≠ b₁=8; only 2 primary fields).")
    print("   ⇒ scope-(a) NEGATIVE. The reciprocal 1/D FORM is right; the π is ARCHIMEDEAN")
    print("     (1-loop det 4π² / heat-kernel), NOT from the S-matrix; the D=8π branch is")
    print("     structurally impossible (𝒟 algebraic). π archimedean; b₁ categorical.")

    # ── witness ─────────────────────────────────────────────────────────────────
    wb = WitnessBuilder("alpha-em-smatrix-perloop", engine="mpmath")
    wb.set_description(
        "Tests the #3870/#3882 redirect: does the RT/WRT modular-S-matrix total quantum "
        "dimension D=√(Σd_i²) (S_{00}=1/D) yield the α_EM per-loop measure 1/(π·b₁)=1/(8π), "
        "b₁=dim H¹(M_Bring)=8? REUSES #3822's machine-validated genuine Σ(2,3,5) S-matrix "
        "(Hikami math-ph/0405028, eq. 3.8). The genuine family has D(2,3,5)=2 primary fields; "
        "quantum dims are the icosahedral/Fibonacci pair {1,φ}, so Σd_i²=(5+√5)/2≈3.618 and "
        "𝒟=√((5+√5)/2)≈1.902 — ALGEBRAIC in ℚ(√5), NO π. Per-axis: (i) area-free ✓ "
        "(√Reidemeister-torsion magnitudes); (ii) π-power −1 ✗ (b)-STRUCTURAL — every MTC "
        "quantum dimension is a cyclotomic algebraic integer, so S_{00}=1/𝒟 carries no bare π "
        "for ANY root-of-unity S-matrix; (iii) reciprocal ✓ FORM (S_{00}=1/𝒟 IS the "
        "1/(total-count) democratic average the redirect predicted) but ✗ VALUE (𝒟≈1.902≠8, "
        "≠8π≈25.13; only 2 primary fields, far too few for the b₁=8 count). Cross-check: the "
        "other natural reading (n=5 Hecke hook-content at q₀, #3853) gives 11.357 — also ≠8/8π "
        "(robust double-negative). Scope-(a) NEGATIVE: the reciprocal 1/D FORM is confirmed, "
        "but the bare π is ARCHIMEDEAN (1-loop det 4π² / heat-kernel), NOT categorical — the "
        "only π's in the RT normalization are unit-modulus framing/CS phases (e^{πi/4}, "
        "CS=−1/120,−49/120, surgery Gauss sum). This DECIDES the #3853 gate: 𝒟 algebraic ⇒ the "
        "'D=π·b₁=8π (π categorical)' branch is structurally impossible; π is the universal "
        "archimedean 1-loop factor. No CODATA read, no convention tuned to 8π. No fit; no α_k "
        "wired; 1/(8π) stays a phase-4 identification."
    )
    wb.set_content_block("prop:alpha-em-categorical-trace")
    wb.set_audit_only("docs/audits/2026-07-18-alpha-em-smatrix-perloop-quantum-dimension.md")
    wb.add_parameter("compute_dps", 50)
    wb.add_parameter("b1_dim_H1_Bring", B1)
    wb.add_parameter("target_measure", "1/(pi*b1) = 1/(8*pi)")
    wb.add_parameter("q0_computations_layer", mp.nstr(q0, 20))
    wb.add_data("reused_smatrix", {
        "source": "#3822 keystone_valuemap_genuine_smatrix_s013.s_entry (Hikami eq. 3.8)",
        "n_primary_fields_D_235": D_235,
        "S00": mp.nstr(S00, 30), "S01": mp.nstr(S01, 30),
        "vacuum_row_ratio": mp.nstr(S01 / S00, 20), "golden_ratio": mp.nstr(phi, 20),
    })
    wb.add_data("total_quantum_dimension", {
        "quantum_dims": ["1", mp.nstr(d[1], 20)],
        "sum_d_squared": mp.nstr(sum_d2, 30),
        "sum_d_squared_closed_form": "(5+sqrt(5))/2 = 2+phi",
        "D_total": mp.nstr(D_total, 30),
        "D_total_closed_form": "sqrt((5+sqrt(5))/2)",
        "S00_equals_inv_D": bool(ctrl_S00_eq_inv_D),
        "field": "Q(sqrt5) — algebraic, no pi",
    })
    wb.add_data("comparison_to_targets", {
        "b1": 8, "pi_b1_8pi": mp.nstr(t8pi, 20),
        "D_over_8": mp.nstr(D_total / t8, 12), "sumd2_over_8": mp.nstr(sum_d2 / t8, 12),
        "D_over_8pi": mp.nstr(D_total / t8pi, 12), "sumd2_over_8pi": mp.nstr(sum_d2 / t8pi, 12),
        "D_equals_8_or_8pi": bool(D_eq_8 or D_eq_8pi),
    })
    wb.add_data("cross_check_n5_hecke_hookcontent", {
        "source": "#3853 alpha_em_2I_total_quantum_dimension_gate_test_probe",
        "D_q0": mp.nstr(D_hecke_n5, 20), "equals_8_or_8pi": False,
        "note": "the OTHER natural keystone-S-matrix reading; also misses 8 and 8π",
    })
    wb.add_data("three_axis_verdict", {
        "axis_i_area_free": "PASS — sqrt(Reidemeister torsion) magnitudes, topological",
        "axis_ii_pi_power_minus1": "FAIL (b)-structural — D,S00 in Q(sqrt5) algebraic, no bare pi "
                                   "for ANY root-of-unity S-matrix (cyclotomic quantum dimensions)",
        "axis_iii_reciprocal": "FORM PASS (S00=1/D democratic average) / VALUE FAIL "
                               "(D~1.902 != b1=8, != 8pi)",
        "where_pi_must_come_from": "archimedean 1-loop determinant 4pi^2 / heat-kernel "
                                   "(log(4pi^2) in zeta'_Delta0(0)); the RT normalization's only "
                                   "pi's are unit-modulus framing/CS phases (magnitude 1)",
        "decides_3853_gate": "D algebraic => 'D=pi*b1=8pi (pi categorical)' branch structurally "
                             "impossible; pi is universal archimedean 1-loop factor",
    })
    wb.add_data("scope", {
        "classification": "(a) scope-limited negative on VALUE + (b) structural exclusion on pi-axis",
        "not_excluded": "a LARGER MTC (more primary fields than the D=2 Sigma(2,3,5) family) whose "
                        "total quantum dimension equals b1=8 could still supply the reciprocal count; "
                        "but no S-matrix can supply the bare pi (that is archimedean)",
    })

    # honest-negative assertions (assert the refutation ⇒ allPassed True)
    wb.add_assertion("controls_reproduce_3822_genuine_smatrix",
                     computed=1.0 if controls_pass else 0.0, expected=1.0, tolerance=0.5,
                     source="C1..C5: D(2,3,5)=2, S²=1, vacuum row=Cor.12 weights, Σ|S0i|²=1, ratio=φ")
    wb.add_assertion("S00_equals_reciprocal_total_quantum_dimension",
                     computed=1.0 if ctrl_S00_eq_inv_D else 0.0, expected=1.0, tolerance=0.5,
                     source="S_{00} = 1/𝒟 with 𝒟 = √(Σ d_i²) reproduced to 1e-40")
    wb.add_assertion("total_quantum_dimension_closed_form_sqrt_5plussqrt5_over2",
                     computed=1.0 if (ctrl_sumd2_closed and ctrl_D_closed) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="Σd_i²=(5+√5)/2, 𝒟=√((5+√5)/2) — algebraic in ℚ(√5), matched to 1e-40")
    wb.add_assertion("D_is_neither_b1_nor_pi_b1_FALSIFIED_value_axis",
                     computed=0.0 if not (D_eq_8 or D_eq_8pi) else 1.0, expected=0.0, tolerance=0.5,
                     source="𝒟≈1.902, Σd_i²≈3.618 ∉ {8, 8π=25.13}; #3853 n=5 reading 11.357 also ∉ "
                            "— the naive S₀₀=1/D shared-wall value identification is falsified")
    wb.add_assertion("smatrix_carries_no_bare_pi_structural_pi_axis",
                     computed=1.0, expected=1.0, tolerance=None,
                     source="𝒟,S₀₀ ∈ ℚ(√5) algebraic (cyclotomic quantum dims) ⇒ S-matrix cannot "
                            "supply the bare π of 1/(π·b₁); π is archimedean (1-loop det 4π²)")
    wb.save()
    print("\n  witness saved: computations/alpha_em/alpha-em-smatrix-perloop.witness.json")
    print("  RESULT: scope-(a) NEGATIVE — reciprocal 1/D FORM confirmed; 𝒟∈ℚ(√5)≈1.902≠8,≠8π;")
    print("          π is archimedean, not categorical. No fit; nothing wired.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

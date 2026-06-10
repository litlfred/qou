#!/usr/bin/env python3
"""qbeta_hoefsmit_stage_b_per_block_ck_probe.py — Hoefsmit Stage B
(probe 6.d′): per-block operator-level c_k structure from the exact
symbolic decay normal forms, with the heat-trace R_λ gate-check.

Owner-approved live-menu option 1 (2026-06-10 synthesis §6): "build
Hoefsmit-rep ρ_λ(𝓑₃) per Wedderburn block, form net(T_w), take Tr
symbolically for exact unbiased c_4..c_8" — executed against the two
standing structural refutations:

  * the scalar u-Taylor route is REFUTED (u = b·ℏ_q² is quadratic in
    t = q−1 ⇒ q→u reversion needs √u; PR #1840 + the operator-markov
    probe), and
  * a sequential scalar peel against a single reference SATURATES at
    the first free rung (after ĉ_3 absorbs the residual, ĉ_4..ĉ_8 ≡ 0
    identically) — demonstrated numerically below, not assumed.

So the unbiased c_k≥4 must be read off the OPERATOR level structure.
This probe builds exactly that:

  1. Parse the canonical neutron/proton normal forms (exact symbolic
     coefficients per basis word) from `free-neutron-decay.witness.json`
     — the canonical GB engine's own output, avoiding any convention
     drift from a re-derivation (per the Stage-B scope doc warning).
  2. Per Wedderburn block λ ⊢ 3: symbolic Hoefsmit characters χ^λ(w)
     for the 6 H_3 basis words; GATE 1 (per-block recombination
     identity): Σ_λ y_λ(q)·χ^λ(w) = tr_M(w) symbolically AND at q_0
     to the 65-dps budget, for every basis word.
  3. Per-block, per-LEVEL decomposition of the decay operator
     ΔT = T_n − T_p (level ℓ = basis-word length 0..3): the
     operator-valued analog of Δ(net). Per the keystone recipe, level
     N=k carries u^k via substrate scaling — the level table IS the
     operator ladder data.
  4. Bar-parity (q ↦ 1/q) of each Markov level component: the rung-3
     object is predicted bar-ODD (triple-confirmed a_1 = √2·Φ₂,
     PRs #1900/#1907/#1911) — tested here on exact symbolic objects.
  5. STRUCTURAL FINDING (asserted): the H_3 normal form has no words
     of length > 3, so the per-block operator route on H_3 populates
     rungs k ≤ 3 ONLY. The unbiased c_4..c_8 require the H_{n≥4}
     towers or the kernel recursion — this *derives* the registry's
     "c_4 = normalisation artifact" tier and localises Stage C.
  6. Heat-trace R_λ gate-check (synthesis §3-bis candidate family):
     per-mode depth-1 kernels R_λ(q,t) = 1 − (q−1)·μ_λ(q)·t with the
     content-Casimir spectrum μ_λ = ℏ_q²·Σ_cells [c]_q[c+1]_q. Gates:
     bar-parity of the implied leading coefficient (must be bar-ODD to
     generate a_1 = √2·Φ₂) + magnitude at q_0 vs √2·Φ₂ ≈ 2.0694.
     Honest: candidate family stays UNGATED unless both pass; nothing
     is wired.

No SDP, no fit, no CODATA inside the operator chain (CODATA Q_β
appears only in the ĉ_3 reproduction + saturation demo, clearly
labelled). Tier discipline respected: no registry change, no
production wiring.
"""
from __future__ import annotations


import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
for _sub in ("", "hecke", "markov"):
    _p = str(HERE.parent / _sub) if _sub else str(HERE.parent)
    if _p not in sys.path:
        sys.path.insert(0, _p)

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from hoefsmit_symbolic import (  # noqa: E402
    Q as q_sym, chi_lambda_symbolic, q_int,
)
from markov_weights_symbolic import tr_M_canonical, solve_y_lambda  # noqa: E402
from qbeta_utils import substrate_ladder_quantities, c3_target_at  # noqa: E402
from experimental_constants import M_E_MEV, Q_NEUTRON_MEV  # noqa: E402

_DPS = 65

# Substrate anchors (proton re-pin canonical; muon per 569bedda1 —
# same provenance as qbeta_symbolic_tbeta_ck4_8_probe.py).
Q_PROTON = mp.mpf("1.1099785827513808075916690956107688798744991218736")
Q_MUON = mp.mpf("1.10997859555")

SHAPES = [(3,), (2, 1), (1, 1, 1)]


def evalq(expr, qval):
    """Evaluate a sympy expression in q at an mpmath anchor, full dps."""
    return mp.mpf(str(sp.N(expr.subs(q_sym, sp.Float(mp.nstr(qval, _DPS), _DPS)),
                           _DPS)))


def safe_cancel(expr):
    """sp.cancel with a together() fallback — sympy's heuristic GCD
    can raise HeuristicGCDFailed on the large y_λ-weighted rational
    functions; the uncancelled form is numerically equivalent."""
    try:
        return sp.cancel(expr)
    except Exception:
        return sp.together(expr)


def bar(expr):
    """Bar involution q ↦ q⁻¹ on a symbolic expression."""
    return safe_cancel(expr.subs(q_sym, 1 / q_sym))


def _numerically_zero(expr) -> bool:
    """Multi-point numeric zero test (robust where sympy's heuristic
    GCD fails on the large y_λ-weighted rational functions). Three
    independent positive q samples at the 65-dps budget; an expression
    vanishing at all three to < 1e-40 is treated as identically zero
    (these are rational functions in √q of modest degree — three
    generic samples vastly over-determine zero)."""
    for qv in ("1.1099785827513808", "1.2345678901234567", "0.81234567890123456"):
        if abs(evalq(expr, mp.mpf(qv))) > mp.mpf("1e-40"):
            return False
    return True


def bar_parity_split(expr):
    """Return (even_part, odd_part, verdict) under the bar involution."""
    e = safe_cancel((expr + bar(expr)) / 2)
    o = safe_cancel((expr - bar(expr)) / 2)
    if _numerically_zero(o):
        verdict = "bar-EVEN"
    elif _numerically_zero(e):
        verdict = "bar-ODD"
    else:
        verdict = "MIXED"
    return e, o, verdict


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-hoefsmit-stage-b-per-block-ck-probe",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Hoefsmit Stage B (probe 6.d'): per-Wedderburn-block, per-level "
        "decomposition of the exact symbolic decay operator ΔT = T_n − T_p "
        "from the canonical free-neutron-decay normal forms; gate 1 = "
        "per-block recombination identity Σ_λ y_λ·χ^λ(w) = tr_M(w) for all "
        "6 H_3 basis words (symbolic + q_0); bar-parity of each Markov "
        "level component (rung-3 bar-ODD prediction); scalar-peel "
        "saturation demo (ĉ_4..ĉ_8 ≡ 0 after ĉ_3 absorbs the residual — "
        "why c_k≥4 is operator-only); structural finding that H_3 levels "
        "stop at ℓ=3 (c_4..c_8 need H_{n≥4} towers / kernel recursion); "
        "heat-trace R_λ depth-1 kernel gate-check (bar-parity + √2·Φ₂ "
        "magnitude). No SDP, no fit; nothing wired."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Hoefsmit Stage B — per-block operator levels from exact decay NFs")
    print("=" * 78)
    print()

    # ── §0  Parse the canonical normal forms from the witness ────────
    wp = HERE.parent / "free-neutron-decay.witness.json"
    with open(wp, encoding="utf-8") as f:
        fnd = json.load(f)
    q0_float = fnd["q0"]

    def parse_nf(side):
        terms = {}
        for t in fnd[side]["nf_terms"]:
            w = tuple(t["word"])
            terms[w] = sp.cancel(sp.sympify(t["coefficient_symbolic"],
                                            locals={"q": q_sym}))
        return terms

    terms_n = parse_nf("neutron")
    terms_p = parse_nf("proton")
    basis_words = sorted(set(terms_n) | set(terms_p), key=lambda w: (len(w), w))

    # Validate the parse against the witness's own numeric snapshots
    # (float-level tolerance: the witness stores 16-digit floats).
    n_match = 0
    n_total = 0
    for side, terms in (("neutron", terms_n), ("proton", terms_p)):
        for t in fnd[side]["nf_terms"]:
            n_total += 1
            mine = float(evalq(terms[tuple(t["word"])], mp.mpf(repr(q0_float))))
            if abs(mine - t["coefficient_numeric"]) < 1e-9:
                n_match += 1
    print(f"  §0 canonical NF parse: {len(terms_n)}+{len(terms_p)} terms, "
          f"{n_match}/{n_total} numeric snapshots reproduced (≤1e-9)")
    delta_net_witness = fnd["transition"]["delta_net"]
    print(f"     witness Δ(net) at q_0 = {delta_net_witness:+.13f} "
          f"(coefficient-sum functional)")
    print()
    builder.add_data("nf_parse", {
        "basis_words": [list(w) for w in basis_words],
        "numeric_snapshots_reproduced": f"{n_match}/{n_total}",
        "delta_net_witness_q0": delta_net_witness,
    })
    builder.add_assertion(
        "nf_parse_matches_witness_numerics",
        computed=n_match, expected=n_total, tolerance=0,
        source=("Exact symbolic NF coefficients sympify'd from "
                "free-neutron-decay.witness.json must reproduce the "
                "witness's own numeric snapshots at q_0 (float-level "
                "1e-9, witness stores 16-digit floats). Guards against "
                "parse/convention drift before any per-block work."),
    )

    # ── §1  Per-block characters + GATE 1 (recombination identity) ───
    print("  §1 per-block Hoefsmit characters χ^λ(w) + recombination gate")
    y_lam = solve_y_lambda(3)
    chi = {}   # chi[shape][word] symbolic
    for shape in SHAPES:
        chi[shape] = {}
        for w in basis_words:
            crossings = [(g, "sigma") for g in w]
            chi[shape][w] = sp.cancel(chi_lambda_symbolic(shape, crossings))

    q0_mp = mp.mpf(repr(q0_float))
    gate1_pass = 0
    gate1_rows = []
    for w in basis_words:
        crossings = [(g, "sigma") for g in w]
        trM_w, _ = tr_M_canonical(crossings, 3)
        recomb = safe_cancel(sum(y_lam[s] * chi[s][w] for s in SHAPES))
        diff = sp.simplify(recomb - trM_w)
        sym_zero = diff == 0
        num_diff = abs(evalq(recomb - trM_w, q0_mp))
        ok = sym_zero or num_diff < mp.mpf("1e-45")
        gate1_pass += int(ok)
        gate1_rows.append({
            "word": list(w),
            "symbolic_zero": bool(sym_zero),
            "abs_diff_at_q0": mp.nstr(num_diff, 8),
            "pass": bool(ok),
        })
        print(f"     w={str(list(w)):<12} Σ_λ y_λ·χ^λ − tr_M : "
              f"{'≡ 0 symbolic' if sym_zero else f'|Δ|={mp.nstr(num_diff, 3)} at q_0'}"
              f"  {'✓' if ok else '✗'}")
    print()
    builder.add_data("gate1_recombination_identity", gate1_rows)
    builder.add_assertion(
        "per_block_recombination_identity_all_words",
        computed=gate1_pass, expected=len(basis_words), tolerance=0,
        source=("GATE 1 (the Stage-B entry gate): the Wenzl y_λ weights "
                "and the symbolic Hoefsmit characters must recombine to "
                "the canonical Markov trace, Σ_λ y_λ(q)·χ^λ(w) = tr_M(w), "
                "for every H_3 basis word — symbolically or < 1e-45 at "
                "q_0 (65-dps budget). Failure ⇒ convention drift; no "
                "downstream level reading would be trustworthy."),
    )

    # ── §2  Per-block, per-level decomposition of ΔT = T_n − T_p ─────
    print("  §2 per-block per-level operator decomposition of ΔT = T_n − T_p")
    delta_c = {w: sp.cancel(terms_n.get(w, sp.Integer(0))
                            - terms_p.get(w, sp.Integer(0)))
               for w in basis_words}
    max_len = max(len(w) for w in basis_words)
    levels = list(range(max_len + 1))

    # per-block per-level: Δχ_λ^{(ℓ)} = Σ_{|w|=ℓ} Δc_w · χ^λ(w)
    per_block_level = {}
    for shape in SHAPES:
        per_block_level[shape] = {}
        for ell in levels:
            expr = safe_cancel(sum(delta_c[w] * chi[shape][w]
                                 for w in basis_words if len(w) == ell))
            per_block_level[shape][ell] = expr

    # Markov level components L_ℓ(q) = Σ_λ y_λ · Δχ_λ^{(ℓ)}
    L = {ell: safe_cancel(sum(y_lam[s] * per_block_level[s][ell]
                            for s in SHAPES))
         for ell in levels}
    delta_trM = safe_cancel(sum(L.values()))
    delta_net_sym = sp.cancel(sum(delta_c.values()))  # coefficient-sum functional

    print(f"     {'block λ':<12}" + "".join(f"  ℓ={ell:<14}" for ell in levels))
    pb_table = []
    for shape in SHAPES:
        row = {"lambda": list(shape)}
        cells = []
        for ell in levels:
            v = evalq(per_block_level[shape][ell], q0_mp)
            row[f"level_{ell}_at_q0"] = mp.nstr(v, 20)
            row[f"level_{ell}_symbolic"] = str(per_block_level[shape][ell])
            cells.append(f"  {float(v):+14.8f}")
        pb_table.append(row)
        print(f"     {str(shape):<12}" + "".join(cells))
    print()
    dtr_q0 = evalq(delta_trM, q0_mp)
    dnet_q0 = evalq(delta_net_sym, q0_mp)
    print(f"     Δtr_M(q_0)  [Markov functional]      = {mp.nstr(dtr_q0, 20)}")
    print(f"     Δ(net)(q_0) [coefficient-sum funct.] = {mp.nstr(dnet_q0, 20)}")
    print(f"     witness Δ(net) cross-check            = {delta_net_witness:+.13f}")
    print()
    builder.add_data("per_block_per_level_at_q0", pb_table)
    builder.add_data("markov_level_components", {
        f"L_{ell}": {
            "symbolic": str(L[ell]),
            "at_q0": mp.nstr(evalq(L[ell], q0_mp), 25),
        } for ell in levels
    })
    builder.add_data("delta_functionals_at_q0", {
        "delta_trM_markov": mp.nstr(dtr_q0, 25),
        "delta_net_coefficient_sum": mp.nstr(dnet_q0, 25),
        "delta_net_witness": delta_net_witness,
    })
    dnet_match = abs(float(dnet_q0) - delta_net_witness) < 1e-9
    builder.add_assertion(
        "coefficient_sum_delta_matches_canonical_witness",
        computed=1 if dnet_match else 0, expected=1, tolerance=0,
        source=("The symbolic coefficient-sum Δ(net)(q) evaluated at q_0 "
                "must reproduce the canonical free-neutron-decay witness "
                "delta_net (float-level 1e-9) — the operator decomposition "
                "is built over the SAME normal forms."),
    )

    # ── §3  Bar-parity of each Markov level component ────────────────
    print("  §3 bar-parity (q ↦ 1/q) of the Markov level components")
    parity_rows = []
    for ell in levels:
        e, o, verdict = bar_parity_split(L[ell])
        if L[ell] == 0:
            verdict = "ZERO"
            frac = mp.mpf(0)
        else:
            o_q0 = evalq(o, q0_mp)
            tot_q0 = evalq(L[ell], q0_mp)
            frac = abs(o_q0 / tot_q0) if tot_q0 != 0 else mp.mpf("inf")
        parity_rows.append({
            "level": ell, "verdict": verdict,
            "odd_fraction_at_q0": mp.nstr(frac, 10) if L[ell] != 0 else "0",
        })
        print(f"     L_{ell}: {verdict:<10} "
              f"(|odd part|/|total| at q_0 = {mp.nstr(frac, 6) if L[ell] != 0 else '—'})")
    print(f"     [prediction: the rung-3 object is bar-ODD — a_1 = √2·Φ₂, "
          f"PRs #1900/#1907/#1911]")
    print()
    builder.add_data("level_bar_parity", parity_rows)

    # ── §4  Level→rung diagnostics at both anchors (NOT wired) ───────
    print("  §4 level→rung diagnostics c_ℓ^cand = m_e·E₀·L_ℓ/(Q_A·cos α_eff·u^ℓ)")
    E0 = 1 / (q_sym * (q_sym - 1))   # form-A E₀ (qbeta_delta_tr_vs_formA)
    diag = {}
    for label, anchor in (("proton", Q_PROTON), ("muon", Q_MUON)):
        sub = substrate_ladder_quantities(anchor)
        Q_A = mp.mpf(M_E_MEV) * sub["Q_A_over_me"]
        QN1 = Q_A * mp.cos(sub["alpha"] - sub["b"] * sub["hbar_q"] ** 2 / 2)
        rows = {}
        for ell in levels:
            if L[ell] == 0:
                continue
            val = mp.mpf(M_E_MEV) * evalq(E0, anchor) * evalq(L[ell], anchor)
            rows[f"level_{ell}"] = mp.nstr(val / (QN1 * sub["u"] ** ell), 20)
        diag[label] = rows
    for ell in levels:
        key = f"level_{ell}"
        if key in diag["proton"]:
            cp, cm = mp.mpf(diag["proton"][key]), mp.mpf(diag["muon"][key])
            swing = abs((cm - cp) / cp) if cp != 0 else mp.mpf("inf")
            print(f"     ℓ={ell}:  proton {mp.nstr(cp, 10):>16}   "
                  f"muon {mp.nstr(cm, 10):>16}   swing {mp.nstr(swing, 4)}")
    print(f"     [diagnostic only — the level→rung normalisation IS the open "
          f"f-map; nothing here is a c_k value]")
    print()
    builder.add_data("level_rung_diagnostics", diag)

    # ── §5  CODATA ĉ_3 reproduction + scalar-peel saturation demo ────
    print("  §5 CODATA-referenced ĉ_3 + scalar-peel saturation (k ≥ 4)")
    sat = {}
    for label, anchor in (("proton", Q_PROTON), ("muon", Q_MUON)):
        sub = substrate_ladder_quantities(anchor)
        u = sub["u"]
        Q_A = mp.mpf(M_E_MEV) * sub["Q_A_over_me"]
        QN1 = Q_A * mp.cos(sub["alpha"] - sub["b"] * sub["hbar_q"] ** 2 / 2)
        QN2 = QN1 * (1 - u ** 2)                      # c_2 = −1 proved
        c3_hat = (mp.mpf(Q_NEUTRON_MEV) / QN2 - 1) / u ** 3
        c3_ref = c3_target_at(anchor, mp.mpf(Q_NEUTRON_MEV), mp.mpf(M_E_MEV))
        Q_running = QN2 * (1 + c3_hat * u ** 3)
        residual_after_c3 = abs(mp.mpf(Q_NEUTRON_MEV) / Q_running - 1)
        ck_after = {}
        for k in range(4, 9):
            ck_k = (mp.mpf(Q_NEUTRON_MEV) / Q_running - 1) / u ** k
            ck_after[f"c_{k}_hat"] = mp.nstr(ck_k, 8)
            Q_running = Q_running * (1 + ck_k * u ** k)
        sat[label] = {
            "c3_hat": mp.nstr(c3_hat, 25),
            "c3_target_at_ref": mp.nstr(c3_ref, 25),
            "rel_diff_vs_ref": mp.nstr(abs(c3_hat / c3_ref - 1), 8),
            "residual_after_c3": mp.nstr(residual_after_c3, 8),
            "sequential_peel_c4_to_c8": ck_after,
        }
        print(f"     {label:<7} ĉ_3 = {mp.nstr(c3_hat, 15)}  "
              f"(c3_target_at: {mp.nstr(c3_ref, 15)})  "
              f"residual after ĉ_3: {mp.nstr(residual_after_c3, 3)}")
    c3_repro_ok = (mp.mpf(sat["proton"]["rel_diff_vs_ref"]) < mp.mpf("1e-30"))
    saturated = (mp.mpf(sat["proton"]["residual_after_c3"]) < mp.mpf("1e-50"))
    print(f"     ⇒ sequential ĉ_4..ĉ_8 ≡ 0 to 65 dps: {saturated} — a single "
          f"scalar reference")
    print(f"       populates exactly ONE free rung; c_4..c_8 are operator-only.")
    print()
    builder.add_data("codata_c3_and_saturation", sat)
    builder.add_assertion(
        "c3_codata_target_reproduced",
        computed=1 if c3_repro_ok else 0, expected=1, tolerance=0,
        source=("The probe's in-line N=2 ladder inversion must agree with "
                "the canonical qbeta_utils.c3_target_at at the proton "
                "anchor to < 1e-30 relative — same construction, shared "
                "substrate chain; guards the §5 saturation demo."),
    )
    builder.add_assertion(
        "scalar_peel_saturates_after_first_free_rung",
        computed=1 if saturated else 0, expected=1, tolerance=0,
        source=("After ĉ_3 absorbs the N=2 residual, the remaining "
                "relative residual is 0 to 65 dps, so the sequential "
                "scalar peel yields ĉ_4..ĉ_8 ≡ 0 identically. This is the "
                "constructive demonstration that c_k≥4 CANNOT come from "
                "any scalar single-reference extraction (complements the "
                "§4 precision floor and the u-quadratic √u obstruction) — "
                "they are operator-level objects."),
    )

    # ── §6  Structural finding: H_3 levels stop at ℓ = 3 ─────────────
    print("  §6 structural finding: H_3 level support")
    print(f"     max basis-word length in the decay NFs = {max_len} "
          f"(words: {[list(w) for w in basis_words]})")
    print(f"     ⇒ the per-block operator route on H_3 populates rungs "
          f"k ≤ {max_len} only;")
    print(f"       unbiased c_4..c_8 require H_(n≥4) towers (A ≥ 4 canonical "
          f"words) or the kernel")
    print(f"       recursion — this derives the registry's 'c_4 = artifact' "
          f"tier structurally.")
    print()
    builder.add_assertion(
        "h3_level_structure_max_word_length",
        computed=max_len, expected=3, tolerance=0,
        source=("The H_3 decay normal forms contain no basis word longer "
                "than 3 (the trefoil σ₀σ₁σ₀ is the deepest level). With "
                "level N=k carrying u^k (keystone recipe), the H_3 "
                "per-block operator route supports rungs k ≤ 3 only — "
                "the unbiased c_4..c_8 live in H_{n≥4} towers or the "
                "kernel recursion. Localises Stage C."),
    )

    # ── §7  Heat-trace R_λ depth-1 kernel gate-check (§3-bis) ────────
    print("  §7 heat-trace R_λ gate-check — μ_λ = ℏ_q²·Σ_cells [c]_q[c+1]_q")
    hbar_sym = (q_sym - 1) / q_sym
    PHI2_TARGET = mp.mpf("1.46324616887618")        # proton anchor (synthesis §2.4)
    A1_TARGET = mp.sqrt(2) * PHI2_TARGET            # √2·Φ₂ = −c_3 ≈ 2.0694
    heat_rows = []
    for shape in SHAPES:
        cells = [(i, j) for i, r in enumerate(shape) for j in range(r)]
        mu = sp.cancel(hbar_sym ** 2
                       * sum(q_int(j - i) * q_int(j - i + 1) for i, j in cells))
        a1_cand = sp.cancel(-(q_sym - 1) * mu)
        _, _, parity = bar_parity_split(a1_cand)
        a1_q0 = evalq(a1_cand, q0_mp)
        mag_ratio = (abs(a1_q0) / A1_TARGET) if A1_TARGET != 0 else mp.mpf("inf")
        passes = (parity == "bar-ODD") and abs(mag_ratio - 1) < mp.mpf("0.01")
        heat_rows.append({
            "lambda": list(shape),
            "mu_lambda_symbolic": str(mu),
            "a1_candidate_symbolic": str(a1_cand),
            "a1_bar_parity": parity,
            "a1_at_q0": mp.nstr(a1_q0, 15),
            "abs_a1_over_sqrt2_phi2": mp.nstr(mag_ratio, 10),
            "passes_both_gates": bool(passes),
        })
        print(f"     λ={str(shape):<10} a₁-cand = −(q−1)μ_λ : {parity:<9} "
              f"|a₁(q_0)| = {mp.nstr(abs(a1_q0), 8)}  "
              f"(target √2·Φ₂ ≈ {mp.nstr(A1_TARGET, 8)})  "
              f"{'✓ GATES PASS' if passes else '✗ stays ungated'}")
    any_pass = any(r["passes_both_gates"] for r in heat_rows)
    print(f"     depth-2 note: the two-mode composition has t-dependent "
          f"coefficients ⇒ NOT in the")
    print(f"     constant-depth-2 class refuted by #1900 (that refutation "
          f"does not close this family).")
    print(f"     VERDICT: candidate family "
          f"{'produces a passing a₁' if any_pass else 'stays UNGATED — no per-mode a₁ is bar-ODD with the √2·Φ₂ magnitude'};"
          f" nothing wired.")
    print()
    builder.add_data("heat_trace_r_lambda_gate_check", {
        "per_block": heat_rows,
        "a1_target_sqrt2_phi2": mp.nstr(A1_TARGET, 25),
        "phi2_proton": mp.nstr(PHI2_TARGET, 25),
        "depth2_note": ("two-mode composition coefficients are t-dependent "
                        "⇒ outside the #1900 constant-depth-2 refuted class"),
        "any_candidate_passes": bool(any_pass),
    })
    builder.add_assertion(
        "heat_trace_gate_check_executed",
        computed=len(heat_rows), expected=len(SHAPES), tolerance=0,
        source=("The §3-bis heat-trace candidate family was gate-checked "
                "per Wedderburn block (bar-parity of the implied a₁ + "
                "magnitude vs √2·Φ₂). The verdict field records pass/fail "
                "per block; the family is wired NOWHERE regardless — this "
                "assertion only guarantees the check ran on all blocks."),
    )

    builder.save()
    print(f"  Witness: qbeta-hoefsmit-stage-b-per-block-ck-probe.witness.json")
    print(f"  Wall: {time.monotonic() - t0:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

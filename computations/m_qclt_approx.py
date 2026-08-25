"""m_qCLT_approx — leading-order JSJ-additive heavy-isotope mass channel.

Wires *channel 2* of
`content/quantum-observable-universe/mass-theory/q-clt-jsj-mass-scaling.md`,
which was previously announced but backed by no compute and no witness.

## The channel

The Jaco–Shalen–Johannson decomposition glues the atomic knot complement
along essential (inter-nucleon) tori, and hyperbolic volume is **additive**
under torus gluing.  Hence the *leading* mass term is volume-additive:

    m_qCLT_leading(Z, N) = Z · m_p + N · m_n

The exact atomic mass differs from this leading term by the **binding
energy** B(Z, N) (the mass defect = the Δ_λ correction):

    m_qCLT_approx(Z, N) = Z · m_p + N · m_n − B(Z, N)

## Two regimes for the nucleon mass (the source of the residual)

The nucleon masses this script reads from `low-isotope-mass-table.witness.json`
are the canonical ones — m_p ≈ 938.2721, m_n ≈ 939.5654, +1.35 / +2.39 ppb via
the `canonical_mass` facade — so the production leading term now tracks CODATA
to ppb and the residual below is the q-CLT approximation itself.

Until 2026-08-08 they were **+2.89 % high** (m_p 965.38, m_n 966.71): that
table's nucleon rows were read from the deprecated `m_e · per_knot_density_borromean`
form via `canonical_mass_table_extended`, which the 2026-06-24 ruling had
removed for absolute mass. Fixed under bean `qou-7loj`.

⚠ **The spectral-phase correction was correcting that artifact.** The
"derived, no-fit" factor θ/(8ℏ²) ≈ 0.9711 was reported to close the +2.89 %
gap ~35× to −819 ppm. It did so by removing an excess that came from the
deprecated baseline, not from physics: applied to the canonical leading term it
overshoots the other way, to ≈ −2.89 %. The witness now asserts that direction.
This is a scope-(a) result — the factor does not improve *this channel* as a
multiplier on the canonical value; it is not an exclusion of the quantity, and
its derivation is untouched. `docs/audits/2026-05-28-spectral-phase-correction-derived.md`
should be re-read against a canonical baseline.

This script reports the JSJ-additive channel in **both** regimes so the
residual is transparently the nucleon-mass-gap status, not a floor of the
channel itself:

  * production    — err_full ≈ +2.89 % (the proved leading-order gap);
  * spectral (exp) — err_full ≈ −0.08 % (the derived correction applied).

The additive **structure** is exact in both: the binding-corrected channel
reproduces CODATA atomic mass to within whatever the nucleon-mass gap is,
*uniformly* across isotopes.  Validated on D, T, ³He (the light compound
nuclei where the framework supplies B); all inputs internal (the
framework's own predicted m_p, m_n, B; CODATA refs from the source
witness's `B_AME_MeV` fields; spectral factor from `_li_2_q_util`).

## Derived binding for the channel — the factorized q-CLT (item 1, 2026-06-15)

The binding `B(Z, N)` above is taken from the framework's per-isotope Δ_λ
prediction (`B_pred`), which is itself gated (the `q₀^{10A−5}` exponent
keystone is open, PR #2316).  This channel ALSO carries a **self-contained,
derived** binding — the **factorized q-CLT** form

    B_qCLT_fac(Z, N) = E₀ · Σ_type n_type · L_type           (all-pairs)
    B_qCLT_fac(Z, N) = E₀ · (A−1) · (Σ_type n_type · L_type)/C(A,2)   (chain)

with the **derived** energy scale `E₀ = m_e/(q₀(q₀−1))` (q₀, m_e only — NOT
Q_β, NOT a fit) and the per-bond-type 2-nucleon sub-braid log-suppressions
`L_type = ln(tr_free/tr_atom)` for the three bond types
(p-p = (2,0), p-n = (1,1), n-n = (0,2)).  The `L_type` are the SAME canonical
Jones–Markov transfer-path traces recorded in
`binding-single-pipeline-comparison.witness.json` (consumed here so the Rust
Hecke engine that produces them is not required in every sandbox); the source
witness's `scriptCommitSha` is pinned for staleness audit.

This binding contains **no fitted coefficients** and resolves the **T/³He
isospin split** that the isospin-blind leading term `Z·m_p + N·m_n` cannot:
tritium carries an n-n bond (`L_nn`) where ³He carries a p-p bond (`L_pp`),
and `L_nn > L_pp`, so the factorized form predicts T more bound than ³He —
matching B_AME.  Caveats (honest, per the discipline): the chain-(A−1) vs
all-pairs-C(A,2) bond count is a **modeling choice, not derived**; A≥4
undershoots ~1.6× (per-knot-trace ceiling); and the *absolute* channel mass
still carries the +2.89 % nucleon gap (the binding is derived/gate-respecting,
the absolute mass is not yet a ppb observable).
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — substrate path bridge
import _path_bridge as _pb  # noqa: E402
import json  # noqa: E402
import time
from math import comb
from pathlib import Path

import mpmath as mp  # noqa: E402

from qou_substrate.witness import WitnessBuilder  # noqa: E402
from _li_2_q_util import spectral_correction_borromean  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

HERE = Path(__file__).resolve().parent
SOURCE_WITNESS = _pb.witness_path("low-isotope-mass-table.witness.json", HERE)
# Factorized-q-CLT bond-type traces: consumed from the recorded canonical
# single-pipeline witness (transfer-path 2-nucleon sub-braid trace ratios; the
# Rust Hecke engine that produces them is not present in every sandbox).
BOND_WITNESS = _pb.witness_path(
    "binding-single-pipeline-comparison.witness.json", HERE)

set_compute_dps()


def _q0():
    from q_parameter import Q  # noqa: E402
    return mp.mpf(str(Q() if callable(Q) else Q))


def _rows():
    src = json.loads(SOURCE_WITNESS.read_text())
    data = src.get("witness", src).get("data", src.get("data", {}))
    rows = data.get("rows") or src.get("rows") or []  # tolerate legacy schemas
    if not rows:
        raise KeyError(f"no per-atom rows in {SOURCE_WITNESS.name}")
    return rows, src


def _bond_type_L():
    """Per-bond-type 2-nucleon sub-braid log-suppression `L = ln(tr_free/tr_atom)`.

    Consumed from the recorded canonical single-pipeline witness (transfer-path
    traces).  Returns `(L_dict, source_meta)`; the source `scriptCommitSha` and
    `computedAt` are pinned so the witness pipeline can flag staleness if the
    upstream trace producer changes.
    """
    d = json.loads(BOND_WITNESS.read_text())
    w = d.get("witness", d)
    p = w.get("parameters", {})
    try:
        L = {k: mp.mpf(str(p[f"L_bond_{k}"])) for k in ("pp", "pn", "nn")}
    except KeyError as e:  # pragma: no cover - explicit staleness signal
        raise KeyError(
            f"{BOND_WITNESS.name} missing bond-type L parameters {e}; "
            "regenerate binding_single_pipeline_comparison.py") from e
    meta = {
        "source_witness": BOND_WITNESS.name,
        "source_scriptCommitSha": w.get("scriptCommitSha") or d.get("scriptCommitSha"),
        "source_computedAt": w.get("computedAt") or d.get("computedAt"),
    }
    return L, meta


def _b_qclt_fac(Z, N, E0, L):
    """Factorized q-CLT derived binding `B = α · Σ_i ln|V_i|` over BOND TYPES.

    No fitted coefficients: `α = E₀` is derived; each `L_type` is a 2-nucleon
    sub-braid trace ratio.  Complete bond graph: `C(Z,2)` p-p, `Z·N` p-n,
    `C(N,2)` n-n bonds.  `chain` scales `(A−1)` bonds by the composition-weighted
    mean; `allpairs` is the literal complete-graph sum (overbinds ~A² at large A).
    """
    A = Z + N
    n_pp, n_pn, n_nn = comb(Z, 2), Z * N, comb(N, 2)
    sigma_L = n_pp * L["pp"] + n_pn * L["pn"] + n_nn * L["nn"]
    bonds_chain = A - 1
    bonds_allpairs = comb(A, 2)
    Lbar = sigma_L / bonds_allpairs if bonds_allpairs else mp.mpf(0)
    return {
        "n_pp": n_pp, "n_pn": n_pn, "n_nn": n_nn,
        "B_qCLT_fac_chain_MeV": E0 * bonds_chain * Lbar,
        "B_qCLT_fac_allpairs_MeV": E0 * sigma_L,
    }


def main() -> int:
    t0 = time.monotonic()
    rows, src = _rows()
    q0 = _q0()
    # Derived (no-fit) spectral-phase factor; EXPLORATORY per the 2026-05-28
    # audit — applied here only to the labelled exploratory variant.
    spectral = mp.mpf(str(spectral_correction_borromean(q0)))
    # Derived canonical energy scale E₀ = m_e/(q₀(q₀−1)) (q₀, m_e only — NOT Q_β,
    # NOT a fit) + the recorded canonical bond-type sub-braid L's (item 1).
    from codata_constants import M_E_MEV  # noqa: E402 — CAL-1 electron mass
    E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))
    Lbond, bond_meta = _bond_type_L()

    by_zn = {(r["Z"], r["N"]): r for r in rows}

    def pred(Z, N):
        return mp.mpf(str(by_zn[(Z, N)]["prediction_MeV_50dps"]))

    def ame(Z, N):
        return mp.mpf(str(by_zn[(Z, N)]["B_AME_MeV"]))

    # framework-predicted nucleon masses (prediction_type="mass", production)
    m_p, m_n = pred(1, 0), pred(0, 1)
    m_p_ame, m_n_ame = ame(1, 0), ame(0, 1)  # CODATA nucleon masses

    compound = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1)]
    out_rows = []
    for label, Z, N in compound:
        B_pred = pred(Z, N)
        B_ame = ame(Z, N)
        leading = Z * m_p + N * m_n              # production leading term
        leading_sp = leading * spectral          # spectral-corrected leading
        full = leading - B_pred                  # production channel
        full_sp = leading_sp - B_pred            # spectral channel (exp)
        m_ref = Z * m_p_ame + N * m_n_ame - B_ame  # CODATA atomic mass
        err_full = (full - m_ref) / m_ref
        err_full_sp = (full_sp - m_ref) / m_ref
        binding_frac = B_ame / m_ref
        # ---- factorized q-CLT derived binding (item 1; no fitted coefficients) --
        fac = _b_qclt_fac(Z, N, E0, Lbond)
        B_fac = fac["B_qCLT_fac_chain_MeV"]
        full_fac = leading - B_fac               # channel mass w/ derived binding
        err_full_fac = (full_fac - m_ref) / m_ref
        B_fac_miss = B_ame / B_fac               # binding miss factor (B_AME/B_fac)
        out_rows.append({
            "label": label, "Z": Z, "N": N, "A": Z + N,
            "m_qCLT_leading_MeV": mp.nstr(leading, 16),
            "m_qCLT_approx_production_MeV": mp.nstr(full, 16),
            "m_qCLT_approx_spectral_MeV": mp.nstr(full_sp, 16),
            "m_qclt_approx_fac_MeV": mp.nstr(full_fac, 16),
            "m_ref_codata_MeV": mp.nstr(m_ref, 16),
            "B_pred_MeV": mp.nstr(B_pred, 12),
            "B_qCLT_fac_chain_MeV": mp.nstr(B_fac, 12),
            "B_qCLT_fac_allpairs_MeV": mp.nstr(fac["B_qCLT_fac_allpairs_MeV"], 12),
            "B_qCLT_fac_miss_x": mp.nstr(B_fac_miss, 6),
            "n_pp": fac["n_pp"], "n_pn": fac["n_pn"], "n_nn": fac["n_nn"],
            "binding_fraction_pct": mp.nstr(binding_frac * 100, 6),
            "err_full_production_pct": mp.nstr(err_full * 100, 6),
            "err_full_spectral_pct": mp.nstr(err_full_sp * 100, 6),
            "err_full_spectral_ppm": mp.nstr(err_full_sp * 1e6, 6),
            "err_full_fac_pct": mp.nstr(err_full_fac * 100, 6),
        })
        print(f"  {label:>4}  prod={mp.nstr(full,10)} ({mp.nstr(err_full*100,4)}%)  "
              f"spectral={mp.nstr(full_sp,10)} ({mp.nstr(err_full_sp*1e6,4)} ppm)  "
              f"ref={mp.nstr(m_ref,10)}", flush=True)
        print(f"        qclt_fac: B_fac={mp.nstr(B_fac,8)} "
              f"({mp.nstr(B_fac_miss,4)}× AME)  m={mp.nstr(full_fac,10)} "
              f"({mp.nstr(err_full_fac*100,4)}%)", flush=True)

    errs_prod = [mp.mpf(r["err_full_production_pct"]) for r in out_rows]
    errs_sp = [mp.mpf(r["err_full_spectral_pct"]) for r in out_rows]
    spread_prod = max(errs_prod) - min(errs_prod)
    gap_prod = (m_p - m_p_ame) / m_p_ame * 100
    gap_sp = (m_p * spectral - m_p_ame) / m_p_ame * 100
    reduction = abs(max(errs_prod, key=abs)) / abs(max(errs_sp, key=abs))

    # ---- factorized q-CLT derived-binding diagnostics (item 1) ----------------
    by_label = {r["label"]: r for r in out_rows}
    T_r, He3_r = by_label["T"], by_label["3He"]
    B_fac_T = mp.mpf(T_r["B_qCLT_fac_chain_MeV"])
    B_fac_He3 = mp.mpf(He3_r["B_qCLT_fac_chain_MeV"])
    B_ame_T, B_ame_He3 = ame(1, 2), ame(2, 1)
    # The derived factorized binding RESOLVES the T/³He split (T more bound),
    # which the isospin-blind leading term Z·m_p+N·m_n cannot.
    split_resolved = (B_fac_T - B_fac_He3) * (B_ame_T - B_ame_He3) > 0
    fac_miss_T = mp.mpf(T_r["B_qCLT_fac_miss_x"])
    fac_miss_He3 = mp.mpf(He3_r["B_qCLT_fac_miss_x"])
    fac_worst_T_He3 = max(max(m, 1 / m) for m in (fac_miss_T, fac_miss_He3))

    builder = WitnessBuilder(
        "m-qclt-approx", engine="python+mpmath", start_time=t0,
    )
    (
        builder
        .set_description(
            "Leading-order JSJ-additive heavy-isotope mass channel "
            "(channel 2 of q-clt-jsj-mass-scaling). "
            "m_qCLT_approx(Z,N) = Z·m_p + N·m_n − B(Z,N). The additive "
            "structure is exact (volume additive under torus gluing); the "
            "absolute residual is the nucleon-mass gap, reported in BOTH "
            "regimes — production (+2.89%, proved-only linking weight) and "
            "spectral-corrected (~-819 ppm; EXPLORATORY, derived θ/(8ℏ²), "
            "not wired per production-vs-exploratory discipline). The channel "
            "ALSO carries a self-contained DERIVED binding — the factorized "
            "q-CLT B = E₀·(A−1)·(Σ n_type·L_type)/C(A,2), E₀=m_e/(q₀(q₀−1)) "
            "derived, L_type the 2-nucleon sub-braid log-traces (recorded "
            "canonical) — which resolves the T/³He isospin split (L_nn>L_pp) "
            "with NO fit. Caveats: chain-vs-allpairs bond count is a modeling "
            "choice (not derived); A≥4 undershoots; absolute mass still carries "
            "the nucleon gap. NOT an 'exact asymptotic limit': the leading-term "
            "error is the binding fraction (plateaus, does not vanish for heavy A)."
        )
        .add_parameter("source_witness", SOURCE_WITNESS.name)
        .add_parameter("q0", mp.nstr(q0, 12))
        .add_parameter("spectral_correction_factor", mp.nstr(spectral, 12))
        .add_parameter("m_p_pred_production_MeV", mp.nstr(m_p, 12))
        .add_parameter("m_n_pred_production_MeV", mp.nstr(m_n, 12))
        .add_parameter("E0_derived_MeV", mp.nstr(E0, 12))
        .add_parameter("L_bond_pp", mp.nstr(Lbond["pp"], 9))
        .add_parameter("L_bond_pn", mp.nstr(Lbond["pn"], 9))
        .add_parameter("L_bond_nn", mp.nstr(Lbond["nn"], 9))
        .add_parameter("bond_L_source_witness", bond_meta["source_witness"])
        .add_parameter("bond_L_source_scriptCommitSha",
                       bond_meta["source_scriptCommitSha"])
        .add_data("rows", out_rows)
        .add_data("nucleon_gap_production_pct", mp.nstr(gap_prod, 6))
        .add_data("nucleon_gap_spectral_pct", mp.nstr(gap_sp, 6))
        .add_data("spectral_reduction_factor", mp.nstr(reduction, 6))
        .add_data("err_full_production_cross_isotope_spread_pct",
                  mp.nstr(spread_prod, 6))
        .add_data("factorized_qclt", {
            "form": ("B = E₀·(A−1)·(Σ_type n_type·L_type)/C(A,2); "
                     "E₀ = m_e/(q₀(q₀−1)) derived (q₀,m_e only, no fit); "
                     "L_type = 2-nucleon sub-braid log-trace per bond type."),
            "E0_derived_MeV": mp.nstr(E0, 8),
            "T_vs_3He_split_resolved": bool(split_resolved),
            "B_fac_T_MeV": mp.nstr(B_fac_T, 8), "B_ame_T_MeV": mp.nstr(B_ame_T, 8),
            "B_fac_3He_MeV": mp.nstr(B_fac_He3, 8),
            "B_ame_3He_MeV": mp.nstr(B_ame_He3, 8),
            "worst_miss_factor_T_3He": mp.nstr(fac_worst_T_He3, 6),
            "modeling_choice": ("chain (A−1) bond count is a modeling choice, "
                                "NOT derived (blocker 3); all-pairs C(A,2) "
                                "overbinds; A≥4 undershoots ~1.6×."),
            "absolute_caveat": ("channel mass still carries the +2.89% nucleon "
                                "gap (blocker 1); the binding is derived/"
                                "gate-respecting, the absolute mass is not ppb."),
            "source": bond_meta,
        })
        .add_data("interpretation", {
            "leading_term": "Z·m_p + N·m_n (JSJ volume-additivity asymptotic)",
            "correction_pred": "B(Z,N) framework Δ_λ binding (item 2; gated A>8)",
            "correction_fac": "B_qCLT_fac derived factorized binding (item 1; no fit)",
            "production_residual": "the proved +2.89% nucleon-mass gap, uniform",
            "spectral_residual": "~-819 ppm — derived θ/(8ℏ²), EXPLORATORY/unwired",
            "spectral_audit": "docs/audits/2026-05-28-spectral-phase-correction-derived.md",
            "overclaim_corrected": "'exact asymptotic limit' → asymptotically "
                                   "linear structure; residual = nucleon gap",
        })
    )
    # Production err_full uniform (additive structure sound) — spread < 0.1%.
    builder.add_assertion(
        "err_full_production_uniform_across_isotopes",
        computed=bool(spread_prod < mp.mpf("0.1")),
        expected=True,
        source="binding removed ⇒ only per-nucleon calibration error remains",
    )
    # Production err_full tracks the known proved +2.89% nucleon gap.
    builder.add_assertion(
        "err_full_production_equals_nucleon_gap",
        computed=mp.nstr(max(errs_prod), 6),
        expected=mp.nstr(gap_prod, 6),
        tolerance=1e-1,
        source="m_qCLT_approx − CODATA mass = the m_p gap (binding cancels)",
    )
    # The spectral correction WORSENS the canonical leading term (qou-7loj).
    #
    # This assertion used to read "reduces the residual by ≳ 20×", after the
    # ~35× closure of the 2026-05-28 audit. That closure was measured against a
    # leading term of m_e·Vol(𝓑₃)/ℏ_q²·λ_A, which was +2.89 % high because the
    # nucleon rows were read from the deprecated Vol·ρ witness. Multiplying by
    # θ/(8ℏ_q²) ≈ 0.9711 removed most of that excess — so the correction was
    # cancelling an artifact of the wrong baseline, not closing a physical gap.
    #
    # With the leading term now canonical (+1.35 ppb via the facade) the same
    # factor moves the result to ≈ −2.89 %: it subtracts an excess that is no
    # longer there. Asserted in the direction that is now true, so the finding
    # is recorded rather than silently dropped.
    #
    # SCOPE (a), per AGENTS.md §"Before declaring refuted": this says the
    # spectral factor does not improve *this* channel *as a multiplier on the
    # canonical leading term*. It is NOT a structural exclusion of θ/(8ℏ_q²) —
    # no invariant forbids the quantity, and its derivation is untouched. What
    # is refuted is the +2.89 % → −819 ppm closure claim that rested on the
    # deprecated baseline. The 2026-05-28 audit needs re-reading in that light.
    builder.add_assertion(
        "spectral_correction_no_longer_improves_canonical_leading_term",
        computed=bool(reduction < mp.mpf("1")),
        expected=True,
        source=(
            "qou-7loj: the ~35× closure was measured against the deprecated "
            "Vol·ρ leading term (+2.89%); against the canonical facade value "
            "(+1.35 ppb) the θ/(8ℏ_q²) factor overshoots to ≈ −2.89%"
        ),
    )
    # Leading term is NOT exact: err_leading = err_full + binding_fraction, and
    # the binding fraction B/m is strictly positive for every bound nucleus
    # (the bound state is lighter than the free nucleon sum). Non-vacuous.
    binding_fracs = [mp.mpf(r["binding_fraction_pct"]) for r in out_rows]
    leading_not_exact = all(bf > mp.mpf("1e-3") for bf in binding_fracs)
    builder.add_assertion(
        "leading_term_not_exact",
        computed=bool(leading_not_exact),
        expected=True,
        source="err_leading − err_full = binding_fraction B/m > 0 (mass defect positive)",
    )
    # Item 1: the factorized DERIVED binding RESOLVES the T/³He isospin split
    # (T more bound than ³He: n-n bond L > p-p bond L) — the isospin-blind
    # leading term Z·m_p+N·m_n cannot.
    builder.add_assertion(
        "factorized_binding_resolves_T_3He_split",
        computed=bool(split_resolved),
        expected=True,
        source="sign(B_fac(T)−B_fac(³He)) == sign(B_AME(T)−B_AME(³He)); "
               "L_nn=%s > L_pp=%s" % (mp.nstr(Lbond["nn"], 4), mp.nstr(Lbond["pp"], 4)),
    )
    # Item 1: the derived factorized binding lands within ~1.25× of B_AME on the
    # non-anomalous A=3 nuclei at the DERIVED scale E₀ (no fit).
    builder.add_assertion(
        "factorized_binding_within_1p25x_T_3He",
        computed=mp.nstr(fac_worst_T_He3, 6),
        expected="1.0",
        tolerance=0.25,
        source="max over {T,³He} of max(miss,1/miss) for B=E₀·(A−1)·L̄_comp; "
               "derived inputs (E₀, bond-type sub-braid traces), no fitted coeff.",
    )

    out = builder.save()
    print(f"\n  production gap: {mp.nstr(gap_prod,5)}%   "
          f"spectral gap: {mp.nstr(gap_sp,5)}%   "
          f"reduction: {mp.nstr(reduction,4)}×")
    print(f"  factorized q-CLT (derived): T/³He split resolved={bool(split_resolved)}  "
          f"worst miss {mp.nstr(fac_worst_T_He3,4)}× on T/³He")
    print(f"  Wrote {out.name} ({len(out_rows)} compound nuclei)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

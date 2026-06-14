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
energy** B(Z, N) (the mass defect):

    m_qCLT_approx(Z, N) = Z · m_p + N · m_n − B(Z, N)

B(Z, N) is exactly the Δ_λ binding correction (the Track-A / q-Lommel
item, gated for A > 8).  For A ≤ 8 the framework already predicts B
(see `low-isotope-mass-table.witness.json`, `prediction_type =
"binding_energy"`).

## Why this corrects an overclaim

The remark called `m_qCLT_approx` "the **exact** topological asymptotic
limit".  That is too strong.  The leading term's relative error is the
**binding fraction** B/m, which runs from ~0.1 % (D) up to ~0.9 %
mid-mass and *plateaus* (nuclear saturation) — it does **not** vanish for
heavy A.  Including B cancels the binding fraction and leaves only the
framework's known **2.89 % nucleon-mass gap** (the m_p gap), uniform
across isotopes.  So the honest statement is: the JSJ channel is
*asymptotically linear* in (Z, N) — the additive **structure** is exact —
but the absolute prediction is a ~1 %-level estimator gated by (i) the
nucleon-mass gap and (ii) the binding model.

This script validates the additive structure on the three light compound
nuclei where the framework supplies B (D, T, ³He), emits a witness, and
reports the error decomposition.  All inputs are internal (the framework's
own predicted m_p, m_n, B); the CODATA references come from the
`B_AME_MeV` fields already carried in the source witness.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — substrate path bridge
import _path_bridge as _pb  # noqa: E402
import time
from pathlib import Path

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

HERE = Path(__file__).resolve().parent
SOURCE_WITNESS = _pb.witness_path("low-isotope-mass-table.witness.json", HERE)

# CODATA nucleon masses (MeV) — used only to turn the source witness's
# B_AME (binding) references into reference atomic masses for the error
# column.  These mirror the B_AME_MeV fields the source witness already
# carries for p and n (prediction_type="mass").
mp.mp.dps = 50


def _rows():
    src = _pb.load_json(SOURCE_WITNESS) if hasattr(_pb, "load_json") else None
    if src is None:
        import json
        src = json.loads(SOURCE_WITNESS.read_text())
    data = src.get("witness", src).get("data", src.get("data", {}))
    return data["rows"], src


def main() -> int:
    t0 = time.monotonic()
    rows, src = _rows()

    by_zn = {(r["Z"], r["N"]): r for r in rows}

    def pred(Z, N):
        return mp.mpf(str(by_zn[(Z, N)]["prediction_MeV_50dps"]))

    def ame(Z, N):
        return mp.mpf(str(by_zn[(Z, N)]["B_AME_MeV"]))

    # framework-predicted nucleon masses (prediction_type="mass")
    m_p, m_n = pred(1, 0), pred(0, 1)
    # CODATA nucleon masses (the B_AME reference on the p/n rows)
    m_p_ame, m_n_ame = ame(1, 0), ame(0, 1)

    compound = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1)]
    out_rows = []
    for label, Z, N in compound:
        B_pred = pred(Z, N)          # framework binding-energy prediction
        B_ame = ame(Z, N)            # CODATA binding
        leading = Z * m_p + N * m_n
        full = leading - B_pred
        m_ref = Z * m_p_ame + N * m_n_ame - B_ame  # CODATA atomic mass
        err_leading = (leading - m_ref) / m_ref
        err_full = (full - m_ref) / m_ref
        binding_frac = B_ame / m_ref
        out_rows.append({
            "label": label, "Z": Z, "N": N, "A": Z + N,
            "m_qCLT_leading_MeV": mp.nstr(leading, 16),
            "m_qCLT_approx_MeV": mp.nstr(full, 16),
            "m_ref_codata_MeV": mp.nstr(m_ref, 16),
            "B_pred_MeV": mp.nstr(B_pred, 12),
            "binding_fraction_pct": mp.nstr(binding_frac * 100, 6),
            "err_leading_pct": mp.nstr(err_leading * 100, 6),
            "err_full_pct": mp.nstr(err_full * 100, 6),
        })
        print(f"  {label:>4}  leading={mp.nstr(leading,10)}  "
              f"approx={mp.nstr(full,10)}  ref={mp.nstr(m_ref,10)}  "
              f"err_leading={mp.nstr(err_leading*100,4)}%  "
              f"err_full={mp.nstr(err_full*100,4)}%", flush=True)

    # Structural validation: err_full is the nucleon-mass gap, which must
    # be (a) ≈ the known 2.89 % m_p gap and (b) UNIFORM across isotopes
    # (binding has been removed, so only the per-nucleon calibration
    # error remains).  A small cross-isotope spread is the evidence that
    # the JSJ-additive structure is sound.
    errs_full = [mp.mpf(r["err_full_pct"]) for r in out_rows]
    spread = max(errs_full) - min(errs_full)
    nucleon_gap = (m_p - m_p_ame) / m_p_ame * 100

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
            "absolute prediction is a ~1%-level estimator gated by the "
            "2.89% nucleon-mass gap and the binding model (Δ_λ). NOT an "
            "'exact asymptotic limit' — the leading-term error is the "
            "binding fraction, which plateaus (does not vanish) for heavy A."
        )
        .add_parameter("source_witness", SOURCE_WITNESS.name)
        .add_parameter("m_p_pred_MeV", mp.nstr(m_p, 12))
        .add_parameter("m_n_pred_MeV", mp.nstr(m_n, 12))
        .add_data("rows", out_rows)
        .add_data("nucleon_mass_gap_pct", mp.nstr(nucleon_gap, 6))
        .add_data("err_full_cross_isotope_spread_pct", mp.nstr(spread, 6))
        .add_data("interpretation", {
            "leading_term": "Z·m_p + N·m_n (JSJ volume-additivity asymptotic)",
            "correction": "B(Z,N) binding = Δ_λ term (item 2; gated A>8)",
            "err_full_is": "the 2.89% nucleon-mass gap, uniform in isotope",
            "err_leading_is": "nucleon gap + binding fraction (grows with A)",
            "overclaim_corrected": "'exact asymptotic limit' → asymptotically "
                                   "linear structure; ~1% absolute estimator",
        })
    )
    # err_full must be uniform (additive structure sound) — spread < 0.1%.
    builder.add_assertion(
        "err_full_uniform_across_isotopes",
        computed=bool(spread < mp.mpf("0.1")),
        expected=True,
        source="binding removed ⇒ only per-nucleon calibration error remains",
    )
    # err_full must track the known nucleon-mass gap (~2.89%).
    builder.add_assertion(
        "err_full_equals_nucleon_gap",
        computed=mp.nstr(max(errs_full), 6),
        expected=mp.nstr(nucleon_gap, 6),
        tolerance=1e-1,
        source="m_qCLT_approx − CODATA mass = the m_p gap (binding cancels)",
    )
    # The leading term is NOT exact: its error strictly exceeds err_full
    # by the binding fraction for every compound nucleus.
    leading_exceeds = all(
        mp.mpf(r["err_leading_pct"]) > mp.mpf(r["err_full_pct"])
        for r in out_rows
    )
    builder.add_assertion(
        "leading_term_not_exact",
        computed=bool(leading_exceeds),
        expected=True,
        source="err_leading = err_full + binding_fraction > err_full",
    )

    out = builder.save()
    print(f"\n  nucleon-mass gap: {mp.nstr(nucleon_gap,5)}%   "
          f"err_full spread: {mp.nstr(spread,4)}%")
    print(f"  Wrote {out.name} ({len(out_rows)} compound nuclei)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

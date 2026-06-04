#!/usr/bin/env python3
"""Option A diagnostic — per-knot Vol(β_K) vs uniform Family-A linking
weight, light isotope series {p, n, D, T, ³He, ⁴He}.

Executes the diagnostic plan in
[`docs/audits/2026-06-04-option-a-vol-per-knot-scoping.md`](../../docs/audits/2026-06-04-option-a-vol-per-knot-scoping.md)
§4 — measures the per-knot-vs-uniform `Geom_full` gap at q₀ for the
light series WITHOUT touching production. The flip from uniform to
per-block in production is owner-gated (§5 of the scope doc): per-block
tr_M alone undershoots m_p by ≈ 2.38× (m_p is the CAL-2 anchor).

For each light isotope K the probe records:
  geom_uniform(q₀)  = geom_full_borromean(q₀)
                    = Vol(𝓑₃) / ℏ_q² · linking_weight_family_a(q₀)
  geom_perknot(q₀)  = geom_full_per_block(Vol_K, tr_M_K, q₀)
                    = Vol(K) / ℏ_q² · tr_M(β_K, q₀)
  ratio             = geom_perknot / geom_uniform
  m_K_uniform(MeV)  = m_e · geom_uniform        (for the proton this IS m_avg,
                                                 the value m_p is calibrated against)
  m_K_perknot(MeV)  = m_e · geom_perknot        (the would-be prediction under
                                                 a per-block flip)

For p/n the tr_M(β_K, q₀) is loaded from the canonical 50-dps chi-cache
(`chi-{atom}-h3-at-q0-50dps.witness.json`). For D/T/³He/⁴He the chi-
cache is not yet built — those rows record `tr_M_at_q0: null` with a
`note` pointing to the canonical braid word from `atom_braid_word_3A`
(producer for the chi-cache row).

Precision: 65-dps mpmath working precision (the `_precision.py`
default), inputs and outputs serialised at 50 dps to match the input
witness floor (the canonical knot-volume and chi-cache witnesses are
50-dps). No input is "upgraded" beyond its witnessed precision.

EXPLORATORY / DIAGNOSTIC. No production code, content blocks, or
production witnesses are changed. Emits:
  `option-a-vol-per-knot-light-series.witness.json` with
  `discipline: "EXPLORATORY"` and `production_wired: false`.

Counter-pin for the eventual production-switch PR: the proton row
should reproduce the docstring's quoted gap ratio
geom_uniform/geom_perknot ≈ 2.53/1.065 ≈ 2.38 (`_li_2_q_util.py:298-313`).
"""
from __future__ import annotations

# Path bridge — same pattern as the other probes/ scripts.
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402

from _li_2_q_util import (  # noqa: E402
    geom_full_borromean,
    geom_full_per_block,
)
from substrate.knot_volumes import (  # noqa: E402
    VOL_BORROMEAN_MPF,
    VOL_6_2_MPF,
    VOL_8_11_MPF,
)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402


HERE = Path(__file__).resolve().parent

# m_e (CODATA 2022) — canonical 50-dps value used across the compute,
# matches `codata_2022_source.py` ("0.51099895069").
M_E_MEV_50DPS = "0.51099895069"

# Chi-cache witnesses live in folio-assistant/computations/ (one
# directory up from probes/).
COMPUTE_DIR = HERE.parent
CHI_CACHE_DIR = COMPUTE_DIR


def _load_chi_cache(atom: str) -> dict:
    """Return the parsed chi-cache for `atom` ∈ {proton, neutron}."""
    path = CHI_CACHE_DIR / f"chi-{atom}-h3-at-q0-50dps.witness.json"
    if not path.exists():
        raise FileNotFoundError(f"chi-cache missing: {path}")
    return json.loads(path.read_text())


# Light isotope registry.  Knot/strand-count assignment matches
# `build_six_term_substrate_model_b.py:MODEL_B_BRAID_REGISTRY`:
#   p / n  : 𝓑₃ (Borromean / L6a4)  — n_canon = 3
#   D      : 6_2                    — n_canon = 3
#   T      : 8_11                   — n_canon = 5
#   ³He    : L6a4 (Borromean)       — n_canon = 3
#   ⁴He    : open (Model B);
#            production uses magic-A: Vol = 4·VOL_BORROMEAN
#
# For ⁴He the production magic-A formula uses `Vol = 4 · Vol(L6a4)`
# (`per_atom_rho_deviation.py:70`, "L6a4_x4"); recording it that way
# here is for diagnostic parity with production, NOT a derivation
# claim — the magic-A wiring is itself part of the open binding-link
# assignment gate (audit
# `docs/audits/2026-06-03-binding-link-assignment-heuristic.md`).
ISOTOPES = [
    {
        "label": "p",
        "Z": 1, "N": 0,
        "knot": "L6a4 (Borromean)",
        "n_strands": 3,
        "chi_cache_atom": "proton",
    },
    {
        "label": "n",
        "Z": 0, "N": 1,
        "knot": "L6a4 (Borromean)",
        "n_strands": 3,
        "chi_cache_atom": "neutron",
    },
    {
        "label": "D",
        "Z": 1, "N": 1,
        "knot": "6_2",
        "n_strands": 3,
        "chi_cache_atom": None,  # not yet built
    },
    {
        "label": "T",
        "Z": 1, "N": 2,
        "knot": "8_11",
        "n_strands": 5,
        "chi_cache_atom": None,  # not yet built
    },
    {
        "label": "3He",
        "Z": 2, "N": 1,
        "knot": "L6a4 (Borromean)",
        "n_strands": 3,
        "chi_cache_atom": None,  # not yet built
    },
    {
        "label": "4He",
        "Z": 2, "N": 2,
        "knot": "L6a4_x4 (magic-A: 4·Vol(L6a4))",
        "n_strands": None,  # magic-A formula; no single-knot strand count
        "chi_cache_atom": None,  # not built (magic-A is a Vol shortcut,
                                  # the per-block tr_M at A=4 needs the
                                  # H₄ chi-cache via markov_peel.tr_M_atomic)
    },
]


def _vol_for(iso: dict) -> mp.mpf:
    """Hyperbolic-volume lookup for the production assignment."""
    if iso["label"] == "4He":
        return mp.mpf(4) * VOL_BORROMEAN_MPF
    knot = iso["knot"]
    if "L6a4" in knot or "Borromean" in knot:
        return VOL_BORROMEAN_MPF
    if knot == "6_2":
        return VOL_6_2_MPF
    if knot == "8_11":
        return VOL_8_11_MPF
    raise KeyError(f"no Vol assignment for {iso['label']!r} ({knot!r})")


def _fmt(x: mp.mpf, dps: int = 50) -> str:
    """Serialise an mpf at `dps` decimal places."""
    return mp.nstr(x, dps, strip_zeros=False)


def main() -> int:
    w = WitnessBuilder("option-a-vol-per-knot-light-series", engine="mpmath")
    w.set_audit_only("docs/audits/2026-06-04-option-a-vol-per-knot-scoping.md")
    w.set_description(
        "Option A diagnostic (PR #1762 §5 / scoping #1816): measure the "
        "per-knot-vs-uniform Geom_full(K, q₀) gap for the light "
        "isotope series {p, n, D, T, ³He, ⁴He} alongside production. "
        "DOES NOT change production — flipping uniform → per-block "
        "would break m_p (the CAL-2 anchor) by ≈ 2.38× per the "
        "`_li_2_q_util.py:298-313` discipline note. Per-knot Vol(K) "
        "from `substrate/knot_volumes.py`; tr_M from "
        "`chi-{atom}-h3-at-q0-50dps.witness.json` for p/n; D/T/³He/⁴He "
        "record `tr_M_at_q0: null` with the canonical braid word from "
        "`atom_braid_word_3A` as the next-step producer pointer."
    )

    # Load q_0 from the proton chi-cache (the canonical 50-dps anchor
    # — both proton and neutron caches use the SAME q_0 string).
    proton_cache = _load_chi_cache("proton")
    neutron_cache = _load_chi_cache("neutron")
    q_0_str = proton_cache["q_0_50dps"]
    assert neutron_cache["q_0_50dps"] == q_0_str, (
        "proton and neutron chi-caches disagree on q_0 — refresh them "
        "via canonical_tr_m_via_chi_cache.py before re-running."
    )
    q_0 = mp.mpf(q_0_str)
    q_inv = mp.mpf(1) / q_0
    m_e = mp.mpf(M_E_MEV_50DPS)

    geom_uniform = geom_full_borromean(q_0, q_inv)
    m_avg_uniform_MeV = m_e * geom_uniform

    w.add_parameter("q_0_50dps", q_0_str)
    w.add_parameter("m_e_MeV", M_E_MEV_50DPS)
    w.add_parameter("compute_dps", mp.mp.dps)
    w.add_parameter("serialization_dps", 50)
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data("scoping_doc",
               "docs/audits/2026-06-04-option-a-vol-per-knot-scoping.md")
    w.add_data("geom_uniform_borromean", _fmt(geom_uniform))
    w.add_data(
        "geom_uniform_description",
        "geom_full_borromean(q_0) = Vol(𝓑₃)/ℏ_q² · "
        "linking_weight_family_a(q_0) = Vol(𝓑₃)/ℏ_q² · (5/2 + (3/4)·h²); "
        "applied uniformly to every atom in production "
        "(mass_table_comprehensive.py:208).",
    )
    w.add_data("m_avg_uniform_MeV", _fmt(m_avg_uniform_MeV))

    print("=" * 78)
    print("Option A diagnostic — per-knot vs uniform Geom_full(K, q₀)")
    print("=" * 78)
    print(f"  q_0 (50-dps)            = {q_0_str}")
    print(f"  m_e  (MeV, 50-dps)      = {M_E_MEV_50DPS}")
    print(f"  geom_uniform(q_0)       = {mp.nstr(geom_uniform, 30)}")
    print(f"  m_avg_uniform (MeV)     = {mp.nstr(m_avg_uniform_MeV, 30)}")
    print("-" * 78)

    rows = []
    for iso in ISOTOPES:
        label = iso["label"]
        vol_K = _vol_for(iso)
        chi_atom = iso["chi_cache_atom"]

        # tr_M(β_K, q_0) from the 50-dps chi-cache when available.
        if chi_atom is not None:
            cache = _load_chi_cache(chi_atom)
            assert cache["q_0_50dps"] == q_0_str, (
                f"chi-cache for {chi_atom} disagrees on q_0"
            )
            tr_M = mp.mpf(cache["tr_M_at_q0"])
            tr_M_source = (
                f"chi-{chi_atom}-h3-at-q0-50dps.witness.json"
            )
        else:
            tr_M = None
            tr_M_source = None

        # Per-knot Geom_full(K, q_0) — full three-arg signature.
        if tr_M is not None:
            geom_perknot = geom_full_per_block(vol_K, tr_M, q_0, q_inv)
            ratio = geom_perknot / geom_uniform
            m_K_perknot_MeV = m_e * geom_perknot
            geom_perknot_str = _fmt(geom_perknot)
            ratio_str = _fmt(ratio)
            m_K_perknot_str = _fmt(m_K_perknot_MeV)
        else:
            geom_perknot = None
            ratio = None
            m_K_perknot_MeV = None
            geom_perknot_str = None
            ratio_str = None
            m_K_perknot_str = None

        # The uniform mass per atom is the same `m_avg_uniform_MeV`
        # for every atom — by construction, since `geom_full_borromean`
        # is the global scalar. Record it per-row so the JSON has a
        # consistent comparison structure.
        m_K_uniform_str = _fmt(m_avg_uniform_MeV)

        # Canonical braid word from the H_{3A} producer — used as a
        # pointer for the next-step chi-cache build when tr_M is null.
        try:
            braid_word = atom_braid_word_3A(iso["Z"], iso["N"])
            braid_word_len = len(braid_word)
            braid_word_snippet = (
                [list(map(float, t)) for t in braid_word[:6]]
                + (["…"] if braid_word_len > 6 else [])
            )
        except Exception as e:
            braid_word_len = None
            braid_word_snippet = f"unavailable ({type(e).__name__}: {e})"

        row = {
            "label": label,
            "Z": iso["Z"], "N": iso["N"],
            "knot": iso["knot"],
            "n_strands": iso["n_strands"],
            "vol_K_50dps": _fmt(vol_K),
            "tr_M_at_q0": _fmt(tr_M) if tr_M is not None else None,
            "tr_M_source": tr_M_source,
            "geom_uniform_50dps": _fmt(geom_uniform),
            "geom_perknot_50dps": geom_perknot_str,
            "ratio_perknot_over_uniform_50dps": ratio_str,
            "m_K_uniform_MeV_50dps": m_K_uniform_str,
            "m_K_perknot_MeV_50dps": m_K_perknot_str,
            "canonical_braid_word_len": braid_word_len,
            "canonical_braid_word_first_6": braid_word_snippet,
            "next_step_producer": (
                None
                if tr_M is not None
                else "markov_peel.tr_M_atomic(Z, N) or "
                     "canonical_tr_m_via_chi_cache.py to build "
                     "chi-{atom}-h{n_canon}-at-q0-50dps.witness.json"
            ),
        }
        rows.append(row)

        if tr_M is not None:
            print(
                f"  {label:>4s}  knot={iso['knot']:<28s}  "
                f"Vol={float(vol_K):.6f}  tr_M={float(tr_M):.6f}  "
                f"ratio(per/uni)={float(ratio):.6f}"
            )
        else:
            print(
                f"  {label:>4s}  knot={iso['knot']:<28s}  "
                f"Vol={float(vol_K):.6f}  tr_M=<null: needs chi-cache>"
            )

    w.add_data("rows", rows)
    w.add_data(
        "interpretation",
        "Each row's `ratio_perknot_over_uniform_50dps` quantifies how "
        "far the per-knot Stage-4 sum `tr_M(β_K, q₀)` is from the "
        "global Family-A scalar `linking_weight_family_a(q₀) ≈ 2.53`. "
        "For p the docstring (`_li_2_q_util.py:298-313`) quotes a ≈ "
        "2.38× gap (i.e. ratio ≈ 1/2.38 ≈ 0.42) and m_K_perknot ≈ "
        "−57% vs CODATA m_p; this row counter-pins that quote. The "
        "null tr_M rows are diagnostic gaps to fill via the chi-cache "
        "producer pointed at by `next_step_producer`; building them "
        "is the next concrete commit on this PR.",
    )

    # Counter-pin the docstring's 2.38× quote at the proton row.
    proton_row = next(r for r in rows if r["label"] == "p")
    assert proton_row["ratio_perknot_over_uniform_50dps"] is not None
    proton_ratio = mp.mpf(proton_row["ratio_perknot_over_uniform_50dps"])
    docstring_ratio = mp.mpf("1.065") / mp.mpf("2.53")
    w.add_assertion(
        "proton_per_block_under_uniform_within_1pct",
        computed=float(proton_ratio),
        expected=float(docstring_ratio),
        tolerance=1e-2,
    )

    out_path = w.save()
    print("-" * 78)
    repo_root = COMPUTE_DIR.parent.parent
    try:
        rel = out_path.relative_to(repo_root)
    except ValueError:
        rel = out_path
    print(f"Wrote witness: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

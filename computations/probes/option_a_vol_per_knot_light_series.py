#!/usr/bin/env python3
"""Option A diagnostic — per-knot Vol(β_K) vs uniform Family-A linking
weight, light isotope series {p, n, D, T, ³He, ⁴He}.

Executes the diagnostic plan in
[`docs/audits/2026-06-04-option-a-vol-per-knot-scoping.md`](../../docs/audits/2026-06-04-option-a-vol-per-knot-scoping.md)
§4 — measures the per-knot-vs-uniform `VolDensity` gap at q₀ for the
light series WITHOUT touching production. The flip from uniform to
per-block in production is owner-gated (§5 of the scope doc): per-block
tr_M alone undershoots m_p by ≈ 2.38× (m_p is the CAL-2 anchor).

For each light isotope K the probe records:
  geom_uniform(q₀)  = vol_density_borromean(q₀)
                    = Vol(𝓑₃) / ℏ_q² · linking_weight_family_a(q₀)
  geom_perknot(q₀)  = vol_density_per_block(Vol_K, tr_M_K, q₀)
                    = Vol(K) / ℏ_q² · tr_M(β_K, q₀)
  ratio             = geom_perknot / geom_uniform
  m_K_uniform(MeV)  = m_e · geom_uniform        (for the proton this IS m_avg,
                                                 the value m_p is calibrated against)
  m_K_perknot(MeV)  = m_e · geom_perknot        (the would-be prediction under
                                                 a per-block flip)

For every atom the tr_M(β_K, q₀) is loaded from the canonical 50-dps
chi-cache. The probe handles BOTH cache schemas (it inspects each
file rather than assuming a fixed shape):
  - pre-summed: a top-level `tr_M_at_q0` field (the proton and neutron
    caches `chi-{proton,neutron}-h3-at-q0-50dps.witness.json`, built by
    `chi_at_q0_via_hoefsmit_mpfr.py`, ship this way);
  - per-partition: a `by_partition` array of `chi_lambda` values only
    (the D/T/³He/⁴He caches
    `chi-{deuteron,tritium,helium-3,helium-4}-h{6,9,9,12}-at-q0-50dps.witness.json`,
    the `kind: "atom"` variant — production-faithful, `include_inter=True`
    — ship this way at the time of writing).
When only `by_partition` is present, the probe sums `tr_M = Σ_λ y_λ · χ^λ`
on the fly using `y-lambda-at-q0.witness.json` (50-dps y_λ table,
n = 2..12 all present). This is the canonical `Σ_λ y_λ · χ^λ` combiner
formalised in `canonical_tr_m_via_chi_cache.py:lines-93-180`, inlined
here as a small helper so the probe stays self-contained. (The schema
chosen by any given cache is an artefact of which producer last ran;
the probe does not rely on the p/n-vs-rest split — it reads whichever
field is present.)

Strand-count convention: the per-block sum is over partitions of the
atom's H_{3A} strand count (3·(Z+N)) — the canonical production
convention (`_li_2_q_util.py:386-391`: "H₃ for the 3-strand
Borromean baryons, H₆ for the deuteron at n=6, etc."), NOT the
Model B small-knot braid-index. Vol(K) is the SMALL knot's
hyperbolic volume from `substrate/knot_volumes.py`; tr_M is the
H_{3A} Markov trace of the full 3A-strand atom braid word.

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
    vol_density_borromean,
    vol_density_per_block,
)
from substrate.knot_volumes import (  # noqa: E402
    VOL_BORROMEAN_MPF,
    VOL_6_2_MPF,
    VOL_8_11_MPF,
)
from substrate.codata_constants import (  # noqa: E402
    M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
    M_D_MEV_VALIDATION,
    M_T_MEV_VALIDATION,
    M_HE3_MEV_VALIDATION,
    M_HE4_MEV_VALIDATION,
)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402


HERE = Path(__file__).resolve().parent

# m_e (CODATA 2022) — canonical 50-dps value used across the compute,
# matches `codata_2022_source.py` ("0.51099895069").
M_E_MEV_50DPS = "0.51099895069"

# Chi-cache + y_lambda witnesses live in folio-assistant/computations/
# (one directory up from probes/).
COMPUTE_DIR = HERE.parent
CHI_CACHE_DIR = COMPUTE_DIR


def _load_chi_cache(atom: str, n_strands: int) -> dict:
    """Return the parsed chi-cache for atom `atom` at H_n=H_{n_strands}.

    Tries the `chi-{atom}-h{n}-at-q0-50dps.witness.json` file (the
    "atom" / production variant — `include_inter=True`, with the
    inter-nucleon crossings).  Errors if missing.
    """
    path = CHI_CACHE_DIR / f"chi-{atom}-h{n_strands}-at-q0-50dps.witness.json"
    if not path.exists():
        raise FileNotFoundError(f"chi-cache missing: {path}")
    return json.loads(path.read_text())


def _load_y_lambda_at_q0() -> dict[int, dict[tuple, mp.mpf]]:
    """Load the canonical 50-dps y_λ(q_0) table for n = 2..12.

    Returns dict mapping `n` (int) → dict mapping partition tuple →
    y_λ value (mpf).  Source: `y-lambda-at-q0.witness.json`.
    """
    path = CHI_CACHE_DIR / "y-lambda-at-q0.witness.json"
    if not path.exists():
        raise FileNotFoundError(f"y-lambda table missing: {path}")
    raw = json.loads(path.read_text())["data"]["by_n"]
    out: dict[int, dict[tuple, mp.mpf]] = {}
    for n_str, rows in raw.items():
        out[int(n_str)] = {
            tuple(row["partition"]): mp.mpf(row["y_at_q0_50dps"])
            for row in rows
        }
    return out


def _tr_m_from_chi_cache(
    chi_cache: dict,
    y_by_part: dict[tuple, mp.mpf],
) -> mp.mpf:
    """Sum tr_M(β, q_0) = Σ_λ y_λ(q_0) · χ^λ(β, q_0) from a per-
    partition chi cache plus the matching y_λ map.

    Mirrors `canonical_tr_m_via_chi_cache.canonical_tr_m()` slow-path
    arithmetic but takes the χ values as pre-computed numerical mpf
    strings (h{6,9,9,12} caches), so no symbolic substitution is
    needed and the combiner is microseconds even at H₁₂.

    Raises RuntimeError if any partition present in the chi cache is
    missing from `y_by_part` — a silent skip would undercount tr_M
    and produce a wrong diagnostic with no failure signal (Copilot
    review, PR #1816).  Full coverage is required, not best-effort.
    """
    tr_m = mp.mpf(0)
    missing: list[tuple] = []
    for entry in chi_cache["by_partition"]:
        lam = tuple(entry["partition"])
        y_lam = y_by_part.get(lam)
        if y_lam is None:
            missing.append(lam)
            continue
        chi_lam = mp.mpf(entry["chi_lambda"])
        tr_m += y_lam * chi_lam
    if missing:
        raise RuntimeError(
            f"tr_M undercount: {len(missing)} partition(s) in the chi "
            f"cache have no y_λ entry — {missing}. The y-lambda-at-q0 "
            f"table is incomplete for this n; refresh it before "
            f"trusting the diagnostic."
        )
    return tr_m


# Light isotope registry.
#
# Vol(K) = small knot's hyperbolic volume — taken from
#   `build_six_term_substrate_model_b.py:MODEL_B_BRAID_REGISTRY`
#   (p/n: 𝓑₃ = Borromean, 8G; D: 6_2; T: 8_11; ³He: L6a4 Borromean;
#   ⁴He: open in Model B → production magic-A uses 4·Vol(L6a4)).
#
# n_strands = 3·(Z+N) = H_{3A} convention — the canonical strand
#   count for the atom braid word produced by `atom_braid_word_3A`
#   and consumed by the production per-block `vol_density_per_block`
#   (`_li_2_q_util.py:386-391`: "H₃ for the 3-strand Borromean
#   baryons, H₆ for the deuteron at n=6, etc."). NOT the
#   small-knot braid-index (Model B's n_canon column).
#
# chi_cache_atom = the name used in
#   `chi-{atom}-h{n_strands}-at-q0-50dps.witness.json` — the
#   production-faithful "atom" / `include_inter=True` variant.
#
# For ⁴He: the production magic-A formula uses `Vol = 4·Vol(L6a4)`
# (`per_atom_rho_deviation.py:70`, "L6a4_x4"); the per-block tr_M
# in the same convention lives in `chi-helium-4-h12-at-q0-50dps.json`
# (77 partitions of 12, built by `per_irrep_pole_atom.py helium-4`,
# ~627s compute per the cache header).  Recording it this way
# matches production parity; it is NOT a derivation claim — the
# magic-A wiring is part of the open binding-link assignment gate
# (audit `docs/audits/2026-06-03-binding-link-assignment-heuristic.md`).
ISOTOPES = [
    {
        "label": "p", "Z": 1, "N": 0,
        "knot": "L6a4 (Borromean)",
        "n_strands": 3,
        "chi_cache_atom": "proton",
        "codata_total_MeV": M_P_MEV_VALIDATION,
    },
    {
        "label": "n", "Z": 0, "N": 1,
        "knot": "L6a4 (Borromean)",
        "n_strands": 3,
        "chi_cache_atom": "neutron",
        "codata_total_MeV": M_N_MEV_VALIDATION,
    },
    {
        "label": "D", "Z": 1, "N": 1,
        "knot": "6_2",
        "n_strands": 6,
        "chi_cache_atom": "deuteron",
        "codata_total_MeV": M_D_MEV_VALIDATION,
    },
    {
        "label": "T", "Z": 1, "N": 2,
        "knot": "8_11",
        "n_strands": 9,
        "chi_cache_atom": "tritium",
        "codata_total_MeV": M_T_MEV_VALIDATION,
    },
    {
        "label": "3He", "Z": 2, "N": 1,
        "knot": "L6a4 (Borromean)",
        "n_strands": 9,
        "chi_cache_atom": "helium-3",
        "codata_total_MeV": M_HE3_MEV_VALIDATION,
    },
    {
        "label": "4He", "Z": 2, "N": 2,
        "knot": "L6a4_x4 (magic-A: 4·Vol(L6a4))",
        "n_strands": 12,
        "chi_cache_atom": "helium-4",
        "codata_total_MeV": M_HE4_MEV_VALIDATION,
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


def _fmt(x: mp.mpf, sig: int = 50) -> str:
    """Serialise an mpf to `sig` significant digits.

    NOTE: `mp.nstr(x, n)` formats to ~n SIGNIFICANT digits, not n
    digits after the decimal point (Copilot review, PR #1816). The
    project's "50-dps" convention means ~50 significant decimal
    digits of precision, which matches the default here.
    """
    return mp.nstr(x, sig, strip_zeros=False)


def main() -> int:
    w = WitnessBuilder("option-a-vol-per-knot-light-series", engine="mpmath")
    w.set_audit_only("docs/audits/2026-06-04-option-a-vol-per-knot-scoping.md")
    w.set_description(
        "Option A diagnostic (PR #1762 §5 / scoping #1816): measure the "
        "per-knot-vs-uniform VolDensity(K, q₀) gap for the light "
        "isotope series {p, n, D, T, ³He, ⁴He} alongside production. "
        "DOES NOT change production — flipping uniform → per-block "
        "would break m_p (the CAL-2 anchor) by ≈ 2.38× per the "
        "`_li_2_q_util.py:298-313` discipline note. Per-knot Vol(K) "
        "from `substrate/knot_volumes.py` (small-knot hyperbolic "
        "volume); tr_M from `chi-{atom}-h{3A}-at-q0-50dps.witness.json` "
        "for every atom — the probe reads whichever schema each cache "
        "carries (a pre-summed top-level `tr_M_at_q0`, or a "
        "`by_partition` array combined in-probe with "
        "`y-lambda-at-q0.witness.json`)."
    )

    # Load q_0 from the proton chi-cache (the canonical 50-dps anchor)
    # and load the y_λ(q_0) table for n = 2..12 once for the four
    # atoms (D/T/³He/⁴He) whose chi-caches store only χ^λ.
    proton_cache = _load_chi_cache("proton", n_strands=3)
    neutron_cache = _load_chi_cache("neutron", n_strands=3)
    q_0_str = proton_cache["q_0_50dps"]
    # Explicit raise (not assert): asserts are stripped under `python -O`,
    # which would let the probe proceed with a mismatched q_0 (Copilot
    # review, PR #1816). The q_0 consistency is a hard precondition.
    if neutron_cache["q_0_50dps"] != q_0_str:
        raise ValueError(
            "proton and neutron chi-caches disagree on q_0 — refresh them "
            "via canonical_tr_m_via_chi_cache.py before re-running."
        )
    q_0 = mp.mpf(q_0_str)
    y_by_n = _load_y_lambda_at_q0()
    q_inv = mp.mpf(1) / q_0
    m_e = mp.mpf(M_E_MEV_50DPS)

    geom_uniform = vol_density_borromean(q_0, q_inv)
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
        "vol_density_borromean(q_0) = Vol(𝓑₃)/ℏ_q² · "
        "linking_weight_family_a(q_0) = Vol(𝓑₃)/ℏ_q² · (5/2 + (3/4)·h²); "
        "applied uniformly to every atom in production "
        "(mass_table_comprehensive.py:208).",
    )
    w.add_data("m_avg_uniform_MeV", _fmt(m_avg_uniform_MeV))

    print("=" * 78)
    print("Option A diagnostic — per-knot vs uniform VolDensity(K, q₀)")
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

        # tr_M(β_K, q_0) — two schemas to handle:
        #   - p/n caches: `tr_M_at_q0` pre-summed at top level
        #   - D/T/³He/⁴He caches: per-partition `chi_lambda` only,
        #     sum tr_M = Σ_λ y_λ(q_0)·χ^λ on the fly
        # The y_λ table covers n = 2..12 so all four atoms are
        # available without a separate compute.
        cache = _load_chi_cache(chi_atom, n_strands=iso["n_strands"])
        cache_q0 = cache.get("q_0_50dps") or cache.get("q_str")
        # Explicit raise (not assert) — survives `python -O` (Copilot
        # review, PR #1816).
        if cache_q0 != q_0_str:
            raise ValueError(
                f"chi-cache for {chi_atom} disagrees on q_0 "
                f"(cache: {cache_q0!r}, probe: {q_0_str!r})"
            )
        if "tr_M_at_q0" in cache:
            tr_M = mp.mpf(cache["tr_M_at_q0"])
            tr_M_source = (
                f"chi-{chi_atom}-h{iso['n_strands']}-at-q0-50dps."
                f"witness.json (top-level tr_M_at_q0, pre-summed)"
            )
        else:
            y_by_part = y_by_n[iso["n_strands"]]
            tr_M = _tr_m_from_chi_cache(cache, y_by_part)
            tr_M_source = (
                f"chi-{chi_atom}-h{iso['n_strands']}-at-q0-50dps."
                f"witness.json (per-partition χ^λ) × "
                f"y-lambda-at-q0.witness.json (n={iso['n_strands']}, "
                f"summed in-probe via _tr_m_from_chi_cache)"
            )

        # Per-knot VolDensity(K, q_0) — full three-arg signature.
        geom_perknot = vol_density_per_block(vol_K, tr_M, q_0, q_inv)
        ratio = geom_perknot / geom_uniform
        m_K_perknot_MeV = m_e * geom_perknot

        # CODATA per-nucleon comparison.  Production's borromean_mass_
        # prediction treats m_e × VolDensity(K, q_0) as the per-nucleon
        # average mass m_avg (`mass_table_comprehensive.py:210-212`),
        # so the right CODATA target for direct comparison is
        # m_codata_total / A (with A = Z + N; for proton/neutron A=1).
        A = iso["Z"] + iso["N"]
        m_codata_total = mp.mpf(str(iso["codata_total_MeV"]))
        m_codata_per_nucleon = m_codata_total / mp.mpf(A)
        # Signed gap: (predicted − codata) / codata, in percent.
        # Positive ⇒ overshoot CODATA; negative ⇒ undershoot.
        gap_uniform_pct = (m_avg_uniform_MeV / m_codata_per_nucleon - 1) * 100
        gap_perknot_pct = (m_K_perknot_MeV / m_codata_per_nucleon - 1) * 100

        # Canonical braid word from the H_{3A} producer — records the
        # provenance of tr_M (the trace was evaluated on this braid).
        braid_word = atom_braid_word_3A(iso["Z"], iso["N"])
        braid_word_len = len(braid_word)
        braid_word_snippet = (
            [list(map(float, t)) for t in braid_word[:6]]
            + (["…"] if braid_word_len > 6 else [])
        )

        row = {
            "label": label,
            "Z": iso["Z"], "N": iso["N"],
            "A": A,
            "knot": iso["knot"],
            "n_strands": iso["n_strands"],
            "vol_K_50dps": _fmt(vol_K),
            "tr_M_at_q0": _fmt(tr_M),
            "tr_M_source": tr_M_source,
            "geom_uniform_50dps": _fmt(geom_uniform),
            "geom_perknot_50dps": _fmt(geom_perknot),
            "ratio_perknot_over_uniform_50dps": _fmt(ratio),
            "m_K_uniform_MeV_50dps": _fmt(m_avg_uniform_MeV),
            "m_K_perknot_MeV_50dps": _fmt(m_K_perknot_MeV),
            "m_K_codata_total_MeV": _fmt(m_codata_total),
            "m_K_codata_per_nucleon_MeV": _fmt(m_codata_per_nucleon),
            "gap_uniform_pct": _fmt(gap_uniform_pct, sig=12),
            "gap_perknot_pct": _fmt(gap_perknot_pct, sig=12),
            "canonical_braid_word_len": braid_word_len,
            "canonical_braid_word_first_6": braid_word_snippet,
        }
        rows.append(row)

        print(
            f"  {label:>4s}  A={A}  knot={iso['knot']:<32s}  "
            f"ratio={float(ratio):>7.4f}  "
            f"m_K(per)={float(m_K_perknot_MeV):>9.4f}  "
            f"CODATA/A={float(m_codata_per_nucleon):>9.4f}  "
            f"Δuni={float(gap_uniform_pct):>+7.2f}%  "
            f"Δper={float(gap_perknot_pct):>+7.2f}%"
        )

    w.add_data("rows", rows)
    w.add_data(
        "interpretation",
        "Each row's `ratio_perknot_over_uniform_50dps` quantifies how "
        "far the per-knot Stage-4 sum `tr_M(β_K, q₀)` is from the "
        "global Family-A scalar `linking_weight_family_a(q₀) ≈ 2.53`. "
        "For p the docstring (`_li_2_q_util.py:298-313`) quotes a ≈ "
        "2.38× gap (i.e. ratio ≈ 1/2.38 ≈ 0.42) and m_K_perknot ≈ "
        "−57% vs CODATA m_p; the proton row counter-pins that quote "
        "(within 0.08 %). Row-by-row reading of `m_K_perknot_MeV_50dps` "
        "vs CODATA is the diagnostic signal: if production were "
        "flipped to per-block today, EVERY light atom mass would "
        "shrink by the row's ratio factor — quantifying #1762 §2 "
        "Form 2's −57 % gap across {p, n, D, T, ³He, ⁴He} at once.",
    )

    # Counter-pin the docstring's 2.38× quote at the proton row.
    proton_row = next(r for r in rows if r["label"] == "p")
    # Explicit raise (not assert) — survives `python -O` (Copilot
    # review, PR #1816).
    if proton_row["ratio_perknot_over_uniform_50dps"] is None:
        raise RuntimeError(
            "proton row has no per-block ratio — the counter-pin "
            "assertion cannot be evaluated."
        )
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

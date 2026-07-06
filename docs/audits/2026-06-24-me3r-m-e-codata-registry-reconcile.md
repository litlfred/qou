# me3r: the three m_e CODATA registries (two truncated) — finding + recommendation

**Date:** 2026-06-24
**Bean:** `me3r` (data-integrity).
**Disposition:** finding documented; a candidate fix was prepared and **reverted per owner request** —
the owner will apply the package-constant change. The analysis below is retained as the rationale for
when that happens. **No package source is changed by this branch.**

## The finding (confirmed)

CODATA-2022 `m_e = 0.51099895069(15)` MeV is defined in **three** registries with **two truncated** copies:

| Registry | Value | Layer |
|---|---|---|
| `computations/substrate/codata_constants.py` | `0.51099895069` (imports `codata_2022_source`) ✅ | in-repo compute (Layer 3) |
| `tools/qou-substrate/python/qou_substrate/constants.py:283` | `0.51099895000` ⚠ (−3 digits) | `qou-substrate` PyPI (Layer 2a) |
| `qou-mass/src/qou_mass/_internal/codata_constants.py:99` | `0.51099895` ⚠ (−3 digits) | `qou-mass` PyPI facade |

The two truncated copies look like **oversights, not contracts**: each carries a comment citing the
*full* value (`0.5109989500(15)`) or claiming *"values match"* the authoritative source, while the
literal is short by 3 digits (≈ `1.35×10⁻⁹` relative — above the L1 1 ppQ floor and the m_e CAL-1 error
band).

## Why it is low-risk (the rationale for the recommended fix)

- **`M_P_MEV` is hardcoded separately** in both packages (not `ratio × m_e`), so an m_e fix would **not**
  cascade to m_p.
- **Proven no in-repo effect (isolation test):** running `per_observable_100x_status.py` with the *old*
  (truncated) vs the *full* package `m_e` gives a **bit-identical** result (m_μ pred `105.658375644`
  either way) — the in-repo dashboards read the `computations/substrate` source, **not** the package
  copies. So the only consumers a fix would touch are **external package importers** (qou-substrate /
  qou-mass PyPI), which would gain the correct precision; **no in-repo number moves.**
- (Aside: that dashboard's committed witness shows m_μ `105.658397811` / 209.8 ppb while the script now
  emits `105.658375644` / 0.05 ppb — that 210 ppb gap is the **q₀-anchor staleness** (proton-anchor
  witness vs current script), a *separate* issue owned by `me-codata-reconcile`; **unrelated to m_e**.)

## Recommendation (owner to apply)

Route both package copies to the full value — `qou-substrate constants.py:283` → `0.51099895069`,
`qou-mass codata_constants.py:99` → `mp.mpf("0.51099895069")` — satisfying `me3r` acceptance (a) (all
three registries agree, single canonical value). The full `pyhecke_native`-dependent dashboards should
be re-run on an environment with the native wheel (not available in this sandbox) to confirm the (very
likely nil) L1/L2 delta. Not closing the bean (owner closes). No fit.

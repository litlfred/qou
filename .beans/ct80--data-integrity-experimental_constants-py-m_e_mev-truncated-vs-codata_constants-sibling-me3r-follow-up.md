
## Progress 2026-06-28 (branch claude/ct80-me-codata-dedup-2026-06-28)

**Source fix SHIPPED** (commit bf6580fc8b): `experimental_constants.py`
M_E_MEV …000 → …069.

- **Chose literal-correct, NOT import-dedup** (the bean's step-2
  suggestion): `experimental_constants.py` is a deliberately mpmath-free
  float registry; 40 of its 166 importers run mpmath-free, so importing
  M_E_MEV from `codata_2022_source` (mpf) would couple them all to
  mpmath — a regression. The literal is corrected in place + a comment
  cites codata_2022_source as canonical.
- **Impact assessment (bean step 1):** 73 witnesses carry an m_e value;
  325 occurrences already …069, only **29 (3 witnesses)** carry the
  truncated …000. Change is 1.35e-9 rel (negligible).
- **Witness regen deferred to canonical CI** — the 3 witnesses
  (delta-lambda-empirical-tabulation, nv-pslq-extended-basis,
  audits/hardcoded-literal-audit) have mpmath/pyhecke-requiring
  producers; regenerating in an ad-hoc pip env CORRUPTS them via
  env-skew (tr_M shifts at the 8th sig fig, q_50dp at the ~10th, from
  missing pyhecke_native/clarabel + different mpmath/sympy vs canonical
  python 3.11.2 / pyhecke_native 0.9.0 / clarabel 0.11.1). Must be
  refreshed by the pinned witness-pipeline env. The hardcoded-literal-
  audit is ALSO independently stale vs current main (8000+ line corpus
  drift) — a separate sidecar-refresh concern.
- **Leftover (broader, me3r scope):** the audit found ~20 OTHER
  truncated …000 m_e literals elsewhere in the corpus (not
  experimental_constants.py) — out of ct80 scope.

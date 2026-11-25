---
name: accuracy-scorecard
description: Redisplay, regenerate, HTML-stage, or QA-gate QOU's 80-dps observational accuracy scorecard (`ACCURACY.md`) across all 5 empirical categories and the `1 ppQ` precision floor.
roles: [reader, collaborator, owner]
---

# accuracy-scorecard

`ACCURACY.md` is QOU's single witness-backed observational comparison scorecard across:
1. **Particle & Nuclear Masses** (elementary leptons/hadrons + `2,542` non-estimated $A \ge 2$ AME2020 nuclides),
2. **Nuclear Binding Energy** (3D $K_A$ tetrahedral plaquette for $A = 2\text{--}4$ + symbolic 1D Q-CLT baseline across $A \ge 2$),
3. **Charge, Hypercharge, $\alpha_{\mathrm{EM}}^{-1}$, Mirror-Nuclei Coulomb & Molecular Geometry**,
4. **Weak $\beta$-Decay** (free neutron conditional $T^3$ split, `6` monotone transfer-matrix benchmarks, `1,010` measured $\beta^-$ transitions, and $G_F$ crossing invariant $N_v$),
5. **$\alpha$-Decay & Composite Fission** (`7` Gamow WKB emitters spanning $24$ orders of magnitude, $N=126$ Mayer–Jensen $^{210}\mathrm{Po}$ preformation, `1,051` exothermic $\alpha$ emitters, and $T(2,9) \to 3\,T(2,3)$ threshold fission),

together with the CODATA/PDG/AME2020 **`1 ppQ` ($10^{-15}$) experimental precision floor** and the Lean 4 scope theorems (`QOU.CategoricalMassMarkov`, `QOU.Observations.QCltNonCommutative`, `QOU.MassTheory.AmeBindingNotPairwise`, `QOU.MassTheory.ChainBindingNoSaturationPeak`).

## Architecture & Commit Stability

- **Generator:** [`scripts/generate-accuracy-scorecard.py`](../../../scripts/generate-accuracy-scorecard.py) (`mp.dps = 80`, zero `float64`, `< 2s` runtime).
- **Template:** [`scripts/templates/accuracy-scorecard.md.tmpl`](../../../scripts/templates/accuracy-scorecard.md.tmpl).
- **Rendered Root Artifact:** [`ACCURACY.md`](../../../ACCURACY.md) (linked in [`README.md`](../../../README.md) under `## Read the work`).
- **Published Web Route:** `_site/accuracy/index.html` $\to$ `https://litlfred.github.io/qou/accuracy/` (built by `scripts/build-site.sh` and railed by `rail-standalone-pages.ts`).
- **Deterministic Provenance:** `ACCURACY.md` never embeds `git rev-parse HEAD` or wall-clock timestamps. Instead, Section 5.3 records a 12-row **Upstream Witness Provenance Table** (`sha256[:12]` per witness/dataset), so `ACCURACY.md` changes **if and only if** one of its 12 upstream witnesses or the template changes.

## Commands

```bash
# 1. Redisplay the live 80-dps scorecard in terminal / chat without writing files:
nice -n 15 python3 scripts/generate-accuracy-scorecard.py --print

# 2. Regenerate ACCURACY.md after updating any of the 12 upstream witnesses:
nice -n 15 python3 scripts/generate-accuracy-scorecard.py --write

# 3. Run the strict QA gate (checks witness allPassed, byte-identity, one-voice hygiene, README link):
nice -n 15 python3 scripts/generate-accuracy-scorecard.py --check --qa-report

# 4. Stage standalone HTML for site publishing (invoked automatically by scripts/build-site.sh):
nice -n 15 python3 scripts/generate-accuracy-scorecard.py --check --qa-report --html-out _site/accuracy/index.html

# 5. Run detector negative-control self-tests (drift, forbidden jargon, missing link, failed witness):
nice -n 15 python3 scripts/generate-accuracy-scorecard.py --self-test

# 6. Run via the unified compute-QA runner:
nice -n 15 python3 scripts/compute-qa.py --gate accuracy-scorecard
```

## Pipeline & QA Integration

`accuracy-scorecard` is enforced as a strict QA gate across three surfaces:
1. **`scripts/compute-qa.py` (`--gate accuracy-scorecard`):** Runs `--self-test` followed by `--check`, emitting `test/results/compute-qa/accuracy-scorecard.json` (`qou-compute-qa/v1`) for `compute-qa.yml` and the `cat/cat-harness/qa-reports` branch.
2. **`scripts/build-site.sh`:** Verifies `ACCURACY.md` is current and stages `_site/accuracy/index.html` during every site build (both via `.github/workflows/build.yml` / `folio-staging.yml` and locally).
3. **`scripts/publish-main-local.sh` (`post-merge-rebuild`):** Runs `--check --qa-report` fail-fast before building the site and rails `_site/accuracy/index.html` into `gh-pages`.

## Strict Public-Reader Hygiene Rules

`ACCURACY.md` and `scripts/templates/accuracy-scorecard.md.tmpl` face external mathematics and physics readers directly. `--check` enforces **zero** occurrences of:
- Internal iteration labels (`Convention` + `A`/`B`/`C`/`D`, `z_C`, `z_D`) — always state the canonical Markov weight directly as $z = q^3/(q^2+1)$;
- Internal calibration shorthand (`CAL-` + `1`/`2`/`3`/`4`) — always name the three physical calibration inputs ($m_e$, $m_p/m_e \leftrightarrow q_0$, $m_{\pi^\pm}$) in mathematical prose;
- Internal issue-tracker bean identifiers (`qou-xxxx`).

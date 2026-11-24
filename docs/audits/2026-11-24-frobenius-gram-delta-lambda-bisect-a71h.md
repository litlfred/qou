# Audit Ledger: `frobenius-gram-delta-lambda` Import-Cone Bisect & 80-dps Borromean Refresh (`qou-a71h`)

**Date:** 2026-11-24  
**Beans:** `qou-a71h` (under Stability Swarm Epic `qou-s028`)  
**Producer:** [`frobenius_gram_delta_lambda_probe.py`](../../computations/probes/frobenius_gram_delta_lambda_probe.py)  
**Witness:** [`frobenius-gram-delta-lambda.witness.json`](../../computations/frobenius-gram-delta-lambda.witness.json)

---

## 1. Claim & Exact Numerical Resolution

Bean `qou-a71h` reported that on `³He` (`Z = 2, N = 1, n = 9`), the Frobenius-Gram weighted sum
`result.per_isotope.3He.variants["frob  Σ y·‖ρa‖²·dχ"].S` moved from `-842.1174706` (committed in
`796eaf09475f`, `2026-07-05T12:51:01Z`) to `-436.2405707` (`831980f1ce68`, `2026-09-04T03:53:33Z`,
`-48.20%`), and hypothesized that the move originated inside `gram_transfer_quadratic`'s
`‖ρ_λ(W)‖²_F` compute path because reverting `wenzl-y-lambda-h9.witness.json` to `852e64fb4e^` left
`-436.2405707` unchanged.

Direct 80-dps counterfactual measurement refutes that hypothesis and isolates **two** exact,
independent root causes:

1. **Historical `-842.1174706 -> -436.2405707` move (`2026-07-05 .. 2026-09-04`) — 100% caused by commit `1ab204f8edb7` (`2026-08-11T00:15:54Z`) on `wenzl-y-lambda-h9.witness.json`:**
   - Comparing all six variants between `796eaf09475f` (`2026-07-05`) and `831980f1ce68` (`2026-09-04`) shows that **all four `y_λ`-independent Frobenius variants remained constant to 7–9 significant digits across every isotope**:
     - `³He` `frob Σ ‖ρa‖²·dχ`: `-1588438.893 -> -1588438.905` (`rel 7.6e-9`)
     - `³He` `frobRatio Σ (‖ρa‖²/‖ρf‖²)·dχ`: `-892.8819446 -> -892.8819577` (`rel 1.5e-8`)
     - `³He` `frobDefect Σ (‖ρa‖²−‖ρf‖²)·dχ`: `-105670.092 -> -105670.0934` (`rel 1.3e-8`)
     - `³He` `sqrtFrob Σ ‖ρa‖·dχ`: `-34993.31273 -> -34993.31307` (`rel 9.7e-9`)
     Thus `gram_transfer_quadratic` (`‖ρ_λ(W)‖²_F`) did **not** move at all.
   - Only the two `y_λ`-weighted sums (`ref_trM Σ y·dχ` and `frob Σ y·‖ρa‖²·dχ`) moved on all four isotopes (`D`: `-29.19406689 -> -22.53556008` via `7e4d1aa6d07c` on `rho-k-h3a-lp-dual.witness.json`; `T`: `-608.979702 -> -297.776234`, `³He`: `-842.1174706 -> -436.2405707`, `⁴He`: `-19044.35481 -> -5933.78778` via `1ab204f8edb7` on `wenzl-y-lambda-h9/h12.witness.json`).
   - **Why `qou-a71h`'s test missed `y_λ`:** `852e64fb4e^` was committed on `2026-08-29`, **18 days after** `1ab204f8edb7` (`2026-08-11`) had already migrated `wenzl-y-lambda-h9.witness.json` from $z_{\mathrm{pre}} = \sqrt{q}/(q+1)$ to $z = q^3/(q^2+1)$.
   - **Exact representation-theoretic mechanism:** In Wenzl's Ocneanu weight formula (`mass_at_3A_proper.jones_wenzl_weight`),
     $$y_\lambda(q, z) = \prod_{(i,j)\in\lambda} \frac{q^{2i}(q^2 - 1 - q z) + q^{2j+1} z}{q^{2 h(i,j)} - 1},$$
     at cell $(i, j) = (2, 0)$ (row 3, column 1), the numerator factor is $q^4(q^2 - 1 - q z) + q z$, which **vanishes identically when $z = q^3/(q^2+1)$**. Under $z_{\mathrm{pre}} = \sqrt{q}/(q+1)$, all **30** partitions of $9$ carried nonzero weight $y_\lambda > 0$, feeding the large $d_\lambda^2$-scale Frobenius norms of $\ell(\lambda) \ge 3$ Temperley–Lieb kernel blocks into `S = -842.1174640` (`-842.1174706` at the 2026-07-05 muon pin). Under $z = q^3/(q^2+1)$, all **25** partitions with $\ell(\lambda) \ge 3$ are identically zero (`max |y_λ| < 1e-75`), leaving only the **5** two-row partitions `(9), (8,1), (7,2), (6,3), (5,4)` and yielding `S = -436.2405723` (`-436.2405707` on `2026-09-04` disk inputs).

2. **Live `origin/main` crash since `2026-09-05` (`7db032fb482b`, `qou-hu1f`) & 80-dps Borromean resolution:**
   - One day after `831980f1ce68`, commit `7db032fb482b` (`2026-09-05`) switched `atom_braid_word_3A` to the canonical alternating Borromean intra-nucleon word (`intra_order="borromean"`), and `62adab672504` (`2026-11-21`) refreshed `atom-chi-rust-{d,t,3he,4he}.witness.json` onto that canonical Borromean word. Because `gram_transfer_quadratic.gram_all_lambda` required strict generator monotonicity (`gen 0 after 1`), `frobenius_gram_delta_lambda_probe.py` crashed with `ValueError` on `origin/main` and also carried a drifted `scriptHash` after `7d0af73553aa` (`2026-11-20`).
   - Because each nucleon subword acts purely on $\{3k, 3k+1\}$ (an $H_3$ block across $s_{3k} \subset m_1 \subset m_2 \subset s_{3k+3}$ of dimension $\le 6$) interspersed with single-letter interfaces on $3k+2$, `gram_all_lambda_block_h3` in `frobenius_gram_delta_lambda_probe.py` computes exact 80-dps $\lVert \rho_\lambda(W) \rVert_F^2$ without $d_\lambda$ materialisation — matching `gram_all_lambda` on grouped words to `< 1.2e-78` across all $\lambda \vdash 6, 9, 12$ and dense float64 einsums on Borromean words to `< 1.5e-14`.

---

## 2. Canonical Borromean 80-dps Results vs Grouped Provenance Control

| Isotope ($n = 3A$) | Target $-B_{\mathrm{AME}}/m_e$ | Borromean `frob Σ ‖ρa‖²·dχ` | Borromean `frob Σ y·‖ρa‖²·dχ` | Grouped `frob Σ y·‖ρa‖²·dχ` (`2026-09-04`) | Grouped `frob Σ y·‖ρa‖²·dχ` (`2026-07-05`, $z_{\mathrm{pre}}$) |
|---|---:|---:|---:|---:|---:|
| `D` ($n=6$) | `-4.35327704` | **`+3.83386479`** *(sign flip)* | `-1.53483780` | `-22.53556008` | `-29.19406689` |
| `T` ($n=9$) | `-16.59846853` | `-128.58625968` | `-5.35413247` | `-297.776234` | `-608.979702` |
| `³He` ($n=9$) | `-15.10383008` | **`+108.13517037`** *(sign flip)* | `-10.02547357` | `-436.2405707` | `-842.1174706` |
| `⁴He` ($n=12$) | `-55.37322995` | `-5811.08169044` | `-36.84988302` | `-5933.78778` | `-19044.35481` |

**Durable GAP-A implication:** On the canonical Borromean word, the refutation of $\lVert \rho_\lambda(W) \rVert_F^2$ as the GAP-A closing weight is strictly stronger than on the superseded grouped word: all four $y_\lambda$-free Frobenius variants (`frob`, `frobRatio`, `frobDefect`, `sqrtFrob`) violate binding sign across $\{\mathrm{D}, \mathrm{T}, {}^3\mathrm{He}, {}^4\mathrm{He}\}$, while the sole sign-preserving variant (`frob Σ y·‖ρa‖²·dχ`) under-binds every isotope (`miss = 2.82, 11.24, 5.08, 18.52`).

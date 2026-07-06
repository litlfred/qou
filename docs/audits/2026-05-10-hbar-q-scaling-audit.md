# $\hbar_q$ scaling audit — operator-dependent convention map

**Status:** read-only audit. No code change. Per owner directive
2026-05-10 ("I think they are already derived. no fitting / guessing"):
this note reports what is **already in the codebase**, maps each
binding/mass script to its $\hbar_q$ power signature, and flags any
mismatches against the canonical content-block conventions.

## TL;DR

Three distinct $E_0$ conventions co-exist in `computations/`,
each with its own $\hbar_q$ scaling. **None are wrong** — each is the
correct convention for a specific operator class — but **conflating
them at consumer sites silently double-counts or omits $\hbar_q$
factors**. Phase 3+ binding-energy work must pick one convention up
front and stay in it.

## The three $E_0$ conventions

| Convention | Value at $q_0$ | Where defined | Scaling | Operator class |
|---|---:|---|---|---|
| **A — single-Hecke-tick** | $4.186$ MeV | `derived_masses.e_0_full_mev` (this PR), `neutron-qvalue-symbolic.md`, `energy-scale-planck.md` | $E_0 = m_e \cdot c_q^2 \cdot \hbar_q^1$ | β-decay single-wrap $\Delta_\text{NF}$ |
| **B — Q-value absorbed** | $0.7823$ MeV | `hecke_core.E_0_CALIBRATION_MEV` | $E_0 = Q_\beta^{\text{CODATA}}$ (implicit $\lvert\Delta\rvert = 1$, $\hbar_q^2$ absorbed) | hecke_core consumer chain (canonical_tower, hecke_characters, mass_at_3A_proper, ...) |
| **C — proton back-fit** | $\sim 200$ MeV | `atomic_braid_mass_table.py:441` | $E_0 = (M_p^{\text{CODATA}} - t_6) / \mathrm{total\_hecke}(p)$ | Strategy-3 multi-term atomic-mass assembly |

**A is the canonical** per `prop:beta-decay-energy-scale`. B and C
are calibrated simplifications for specific consumer chains.

## Operator $\hbar_q$ signatures

| Operator | Net $\hbar_q$ power | Source content block |
|---|:-:|---|
| β-decay $\Delta(\text{net}) = h(h-2)/2$ | $\hbar_q^1$ (linear in $h \approx 2\hbar_q$) | `neutron-qvalue-symbolic.md` |
| Hyperbolic-knot mass $\mathrm{Vol}(K)/\hbar_q^2$ | $1/\hbar_q^2$ (mass scales **inversely**) | `skein-mass-from-linking.md` |
| Mass-tower remainder at level $N$ | $\hbar_q^{2(N+1)}$ | `per-braid-mass-tower.md:30` |
| Noether $q$-anomaly $\delta_q$ | $\hbar_q^2$ | `noether-theorem-callout.md:32` |
| α-EM correction $\delta_{CS}$ | $\hbar_q^4 \cdot [5]_q$ | `alpha-em-categorical-trace.md:21` |
| Categorical $\rho_q = 1/\hbar_q^2$ prefactor | $1/\hbar_q^2$ (cat-units → MeV) | `probe_brane_tower_finite_laurent.py:100` |

## Combined $\hbar_q$ power at the Q-value level

| Process | $E_0$ convention | Operator $\hbar_q$ power | Combined |
|---|:-:|:-:|:-:|
| β-decay single-wrap (mine) | A: $\hbar_q^1$ | $\hbar_q^1$ ($\Delta$ at leading order) | $\hbar_q^2$ |
| `per-braid-mass-tower` bound at $N=0$ | (any) | $\hbar_q^2$ | $\hbar_q^2$ ✓ matches |
| Hyperbolic-knot binding (Phase 3+) | A: $\hbar_q^1$ would be WRONG | $1/\hbar_q^2$ | $\hbar_q^{-1}$ — mismatch |
| Hyperbolic-knot binding via Vol | implicit in Vol/$\hbar_q^2$ | $1/\hbar_q^2$ | $\hbar_q^{-2}$ — direct form |

**β-decay row: confirmed scaling-consistent** — $E_0 \cdot |\Delta|$ gives net $\hbar_q^2$, matching the structural bound at level $N=0$. The 0.17% residual sits inside the bound's $\hbar_q^2/(1-\hbar_q^2) \approx 1\%$ ceiling.

**Hyperbolic-knot binding row: WOULD BE WRONG if computed via A's $E_0 \cdot |\Delta|$**. For Phase 3 Triton (and ³He, ⁴He), the mass operator is hyperbolic-knot, scaling as $\mathrm{Vol}/\hbar_q^2$, NOT $E_0 \cdot \mathrm{something}$. Naively using my $E_0 = 4.186$ MeV with a $\Delta(\text{Triton net})$ analog would be a 4-orders-of-magnitude error from missing the $1/\hbar_q^2$ factor.

## Script-by-script audit

### Scripts in convention A (single-Hecke-tick, $\hbar_q^1$ in $E_0$)

| Script | $E_0$ source | Operator | OK? |
|---|---|---|:-:|
| `derived_masses.py` (Phase 0b.4 / this PR) | $m_e/(q(q-1))$ derived | β-decay single-wrap | ✓ |
| `q_beta_predicted.py` | calls `derived_masses` | β-decay | ✓ |

### Scripts in convention B ($E_0 = Q_\beta$, $\hbar_q^2$ absorbed)

| Script | Source | Operator | OK? |
|---|---|---|:-:|
| `hecke_core.py:2922` | `_Q_NEUTRON_MEV` = 0.7823 MeV | binding $B_\text{bulk}(Z,N) = E_0 \cdot (\lvert\mathrm{tr}_M(W_\text{free})\rvert - \lvert\mathrm{tr}_M(W_\text{atom})\rvert)$ | ✓ if consumer uses raw $\lvert\mathrm{tr}_M\rvert$ (the dimensionless form that already has $\hbar_q^2$ baked in via the operator) |
| `canonical_tower.py:446-528` | imports `E_0_CALIBRATION_MEV` | atom-level binding | ✓ |
| `hecke_characters.py:39` | imports `E_0_CALIBRATION_MEV` | character-chain | ✓ |
| `mass_at_3A_proper.py:676` | references `E_0_CALIBRATION_MEV` | mass formula at H_{3A} | ✓ |
| `adjacent_vs_full_probe.py:46` | imports `E_0_CALIBRATION_MEV` | tower probe | ✓ |

### Scripts in convention C (proton-back-fit, $\sim 200$ MeV)

| Script | $E_0$ source | Operator | Flag |
|---|---|---|:-:|
| `atomic_braid_mass_table.py:441` | back-fit from `M_p_CODATA / total_hecke(p)` | Strategy-3 multi-term | ⚠️ 4th-calibration violation per `2026-05-10-workplan-0b §5` |

### Scripts using direct $1/\hbar_q^2$ prefactor (no $E_0$)

| Script | Formula | Operator | OK? |
|---|---|---|:-:|
| `probe_brane_tower_finite_laurent.py:100` | $\rho_q = 1/\hbar_q^2$ explicit | atom-mass prefactor | ✓ matches `skein-mass-from-linking.md` |
| `mass-from-q-symbolic.py:102` | $R_{\mu e} = V_{41}/\hbar_q^2$ | $m_\mu/m_e$ ratio | ✓ |
| `q_pinning_50_digit.py:236` | $\xi(q) = D(\lambda_\text{Descartes})/\hbar_q^2$ | substrate pinning | ✓ |
| `beta-decay-from-q.py:71` | $\delta_q = (A-1)/A^2 \cdot \hbar_q^2$ | $q$-anomaly correction | ✓ matches Noether |

### Scripts NOT using $\hbar_q$ explicitly

`binding_canonical.py`, `binding_k_solver.py`, `atomic_braid_mass_table.py` (other than the back-fit on line 441), `atomic_mass_via_rho_k.py` — these use scalar $E_0$ or $Q_\beta$ in MeV directly without manipulating $\hbar_q$. **Scaling-correct provided their $E_0$ choice matches their operator class.**

## Phase 3 implication (Triton at H_9)

For the Triton binding $B(T) = E(T_w^T) - E(T_w^p) - 2 E(T_w^n)$:

- **DO NOT** use convention A ($E_0 = 4.186$ MeV) with a $\Delta(\text{net})$-style operator difference. Would miss $1/\hbar_q^2$ × $\hbar_q^2$ ≈ 1/0.0098 ≈ 102× factor.
- **DO** use convention B (`hecke_core.E_0_CALIBRATION_MEV = Q_\beta`) with $\lvert\mathrm{tr}_M(W_\text{free})\rvert - \lvert\mathrm{tr}_M(W_\text{atom})\rvert$ as per `hecke_core._canon`. The dimensionless trace differences carry the right $\hbar_q$ powers.
- **OR** use the direct hyperbolic-knot form $\mathrm{Vol}(K)/\hbar_q^2$ per `skein-mass-from-linking.md` — but this needs Vol(T_w) at H_9, which is not yet wired.

The `canonical_tower.py:446-528` and `hecke_core._canon` path is the **already-derived** binding chain — Phase 3 should consume from there, NOT reinvent the scaling.

## Action items (read-only audit; no code change)

1. **Phase 3 Triton work** must consume `hecke_core.E_0_CALIBRATION_MEV` + canonical binding chain, NOT my β-decay-sector $E_0$. Cross-reference `prop:atom-knot-mass-derivation` for the right operator form.

2. **`atomic_braid_mass_table.py:441` 4th-calibration violation** remains tracked under Workplan 0b §5. Per owner directive, the back-fit $E_0 \approx 200$ MeV is to be replaced by a derived chain via `prop:operator-selection-lp` LP-dual shadow prices — separate work from the $\hbar_q$ audit.

3. **Cross-script $E_0$ disagreement** (4.186 vs 0.7823 vs 200 MeV) is convention, not error — but a **single-source-of-truth registry** mapping each script's $E_0$ to its convention would prevent silent miscompositions. Candidate location: `computations/derivation_chain.py` already aggregates similar constants; an `E_0_CONVENTIONS` dict there would surface the choice at every consumer.

4. **β-decay 0.168% / 1.31 keV residual** (post-`4649650f`) is consistent with the $\hbar_q^2$ structural bound at $N=0$ — **closing it requires the $N=1$ tower extension**, which is the open R&D in `brane-tower-z-habiro.md` (the level-selection rule $n_\star$). Not a scaling fix.

## Conclusion

The owner's prior is correct: **the scalings ARE already derived, in the content blocks** (`energy-scale-planck.md`, `skein-mass-from-linking.md`, `per-braid-mass-tower.md`, `neutron-qvalue-symbolic.md`). The scripts implement them faithfully in different conventions. My β-decay Q_β prediction (commit `4649650f`) uses convention A and the operator at single wrap; this is internally consistent and within the structural bound. Phase 3+ Triton/³He/⁴He binding work must use convention B (the canonical `hecke_core._canon` chain), NOT convention A.

No fitting required; the scalings line up if each operator is consumed in its proper convention.

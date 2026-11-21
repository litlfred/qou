# Cite and cross-check exposition blocks: wave-1 findings (2026-11-21)

Bean-drain list `expo-cite-xcheck` (47 beans), issue #8802, branch
`claude/expo-cite-xcheck-2026-11-21`. Every citation was checked against the
held library text (`library/<doc-id>/sections/` or `ocr/`) before it was added.
Mismatches are recorded here as statement-correctness findings for the owner;
no mathematical statement was rewritten.

Each bean was also checked against `docs/coordination/owner-rulings.md` (today's
main) for superseded premises; those found are listed in §3.

## 1. Citations added (13 beans)

| bean | key | where | what the source says (checked) |
|---|---|---|---|
| qou-4kmu | `hodgson2012` | `mass-theory/hyperbolic-knot-positive-volume-via-reeb.md` | §1: Cao–Meyerhoff, exactly two orientable cusped manifolds of least volume 2.029883 (m004, m003). See finding F1. |
| qou-7neb | `neumann-reid` | `braids-and-knots/cusp-shape-bar-parity.md` | Thm 2.2 and §2–3 (invariant trace field); p. 35, the figure-eight group lies in PGL₂(O₃) and its cusp parameter is in ℚ(√−3). |
| qou-6vo0 | `tran2014` | `QOU/BraidKnot/AJTrefoil.lean` (header and class docstring) | §0.3: strong AJ confirmed for the trefoil (Sikora) and all torus knots (Tran); Thm 1, most cables. |
| qou-8kn5 | `lin2024` | `QOU/QBeta/C1ConnectionPoles.lean` | explicit connection formula and q-Stokes matrix for a confluent ₙφₙ₋₁; whether it covers the C1 module is not checked (stated in the Ref line). |
| qou-afzu | `porti2015` | `QOU/OneLoopEdgeLattice.lean` | §5.1 `prop:change`: ratio of torsions for two peripheral curves is ± the Jacobian of the change of local parameter. |
| qou-cjkt | `rozansky1995` | `QOU/BraidKnot/KeystoneRTSurgeryConstruction.lean` | Prop 1.1 (on p. 6 of the held copy, not p. 5), eq. (1.6), §4 (lens spaces and Seifert manifolds). Documents the (RT) hypothesis; does not discharge it. |
| qou-lxqf | `murakami2006` | `QOU/Knot/FigureEightComplexVolume.lean`; `docs/audits/2026-07-26-sdeformed-channel-signflip.md` | §1 records the Murakami–Yokota theorem for 4₁ for r near 1. See finding F2. |
| qou-vo5j | `sniady2006asymptotics` | `QOU/BraidsAndKnots/DeltaLambdaDReduction.lean` | §4.5 second-order expansion at n = 4 gives Σ̂₃ = R₄ + R₂ + (degree ≤ 0); the constant vanishes on the empty diagram. The bean's "Thm 4.14" number could not be confirmed from the held text. |
| qou-xiaj | `kegel2024` | `mass-theory/three-calibration-inputs-proof.md` | Ex. "volume of S³": vol_t(S³) = 2v₀ ≈ 2.02988, figure-eight the unique minimiser. |
| qou-z959 | `arxiv-1803.04009v2` | `q-geometric-langlands/mirror-3d-3d-correspondence.{md,ts}` | §2.3 (T^DGG sees only part of the flat connections), §4.1 (Dehn filling); both for one torus boundary, while B₃ has three cusps. |
| qou-zlr6 | `dimofte-gukov-lenells-zagier-2009` | `QOU/QBeta/StateIntegralRecursionLattice.lean` | §3, the state-integral model on an ideal triangulation from Faddeev's quantum dilogarithm. |
| qou-zyr2 | `garoufalidis-hodgson-hoffman-rubinstein2016` | `computations/probes/figure_eight_3d_index.py` (docstring) | §10.3 corollary `1-efficient_degrees`: on a 1-efficient triangulation every non-zero irreducible closed normal class has q^{1/2}-degree ≥ 1. Probe re-run; payload byte-identical. |
| qou-otpa | `epelbaum2008`, `jurgenson2009srg` | `computations/deltalambda/mu4_vs_nuclear_4n_force_bound_probe.py` (+ witness) | Tjon line, Fig. 10 p. 12; 4N forces start at ν = 4 (p. 13). Probe re-run; numbers byte-identical, only the reference strings gained keys. |

Lean edits are comment/docstring only. No Lean toolchain was available in this
container, so they were **not** lean-direct verified; each file's `/-` and `-/`
counts were checked unchanged. The math-bearing `.md` edits add a `\cite{…}`
only and were not render-checked by the pipeline.

## 2. Cross-checks run (pre-registered, exact arithmetic)

`computations/probes/expo_xcheck_exact_identities_probe.py`; criteria are in its
docstring, written before running.

| bean | check | result |
|---|---|---|
| qou-07m1 | M₁ = g₀·2G₀ through q⁴ (arXiv:2302.08363 §3 vs the corpus's printed fantini–wheeler blocks) | **PASS**: product (1, −8, −9, 18, 46). Reported: M₂/g₀ = −9q − 12q² + 9q³ + 36q⁴; M₂/(g₀·2G₀) = −9q − 75q² − 642q³ − 5580q⁴. The source says the exact forms "were conjectured in [ggm1]". |
| qou-mmq7 | [n]_q − [n−1]_q = Δ_{T(2,2n−1)}, n = 2..16 | **PASS** with the balanced q-integer. With the unbalanced [n]_q = 1 + … + q^{n−1} the difference is q^{n−1}: the identity is convention-dependent. |
| qou-e1me | 4₁ A-polynomial in `qbeta_nz_even_series_fourone_probe.py` vs Takata/Hoste–Shanahan A_{K₋₁} | **PASS**, coefficient by coefficient under (l, m) = (L, M). The probe can cite `[takata2004]` §2. |
| qou-5rou | Ohtsuki λ_n of the corpus's affine form q(q−1)Z_∞ = 1 − ½S_JL | **PASS**: Z_∞ = 1 − 6h + 45h² − 464h³ + 6224h⁴ − 102816h⁵. (λ₁, λ₂) = (−6, 45) is Lin–Wang's (6, 39) under orientation reversal (λ₂(M̄) = λ₂(M) + λ₁(M)); λ₂ ∈ 3ℤ. The corpus series carries the reversed orientation of "+1 surgery on the right-handed trefoil". |

Measured without a probe:

- **qou-t8mi** already done on main: `keystone_colored_sigma235_wrt.py` separates Ψ_LZ = q^{1/120}·S_JL and the affine wrapper (corrected 2026-08-09), citing p. 55. Check D above now also confirms the wrapper against Lin–Wang.
- **qou-u8cp**: the probe and `TjonSimplexForm.lean` use 0.300 MeV as "the N³LO four-nucleon estimate". Jurgenson et al. p. 3 give it as a "rough estimate" from their Ref. [20], "of order a few hundred keV", that is, a range. The SRG-induced 50 keV is a separate number and is used separately. See finding F4.

## 3. Statement-correctness findings for the owner

- **F1 (qou-4kmu).** `hyperbolic-knot-positive-volume-via-reeb.md` says 4₁ "carries the minimal hyperbolic volume 2v₃". The source says minimal among **orientable cusped** hyperbolic 3-manifolds, shared with its sister m003; the closed Weeks manifold (0.9427) is smaller. Among hyperbolic knot or link complements in S³ it is the unique minimum (kegel2024). The cite was added; the sentence was not changed.
- **F2 (qou-lxqf).** `FigureEightComplexVolume.lean` and the 2026-07-26 audit write the limit as `J_N(4₁; e^{(2πi+u)/N}) → 𝔙(u)` and call it a theorem. The held source states the limit of `log J_N / N` and only for r near 1 (small u). The missing log/N and the small-u scope are notation and scope slips, not changes to the result.
- **F3 (qou-u33z, qou-epkn, qou-ohl6, qou-68uk).** Not run in this wave (need the NZ-matrix machinery); listed in NEXT.
- **F4 (qou-u8cp, superseded-premise rule).** `TjonSimplexForm.mu4_target_exceeds_n3lo_bound` proves `34 · 0.300 < 4.591 · 2.224566` by `norm_num`. It puts an empirical literature number and AME B(D) inside a Lean theorem. It is labelled as a certification of a probe's arithmetic, not a structural result, but it sits under the "no empirical values inside proofs" rule. The ×34 also depends on choosing 0.300 inside "a few hundred keV": the >10× verdict holds for any value under 1.02 MeV.
- **F5 (qou-1rgm, premise stale).** `q-game-of-life-proof.md` no longer asserts unitarity: it now says invertibility, not unitarity, and that σᵢ is not unitary for any inner product when q ≠ 1. That is correct for a positive-definite form at real q. Squier's result is unitarity for a bar-Hermitian (indefinite) form over ℤ[s, s⁻¹]. Citing Squier would mean adding a contrast sentence, which is new exposition, so no cite was added.
- **F6 (qou-njry, mis-sourced).** Neumann–Reid Prop. 3.4 is a *necessary* condition (amphicheiral ⇒ conjugation-closed trace field). It does not source the claim that 4₁ is amphichiral. Not added; a knot-table source is the right cite.
- **F7 (qou-udpt, mis-sourced).** Susskind–Thorlacius argue for black-hole complementarity (information in the radiation, with no observer able to see the duplicate). That is not the "preserved but inaccessible" position the remark adopts. Not added. The remark already cites Harlow–Hayden and Lowe–Polchinski–Susskind.
- **F8 (qou-7q3s bean text).** The bean writes Vol(4₁) = 2Λ(π/3). The correct value is 6Λ(π/3) = 2Cl₂(π/3) ≈ 2.0299 (AGENTS.md, Λ vs Cl₂). The cross-check itself was not run in this wave.
- **F9 (qou-mmq7, superseded premise).** The bean wants the identity placed in the T(2,n) *lepton* tower (`lepton_t2n_torus_tower.py`, electron = T(2,3)). That rests on the trefoil-as-electron premise, superseded on 2026-11-21. The identity is verified as algebra only and is not wired anywhere. The same script's electron = T(2,3) header is a superseded label (not edited here).
- **F10.** `AJTrefoil.lean` called the trefoil "the QOU electron knot"; relabelled as the backup candidate per the 2026-11-21 ruling (docstring only).

## 4. Premise stale or already done (no edit)

- **qou-femd, qou-fs87, qou-ystb.** `prop:q-plancherel-asymptotic-skeleton` was rewritten. Clause 1 now cites vershik-kerov1977 and biane1998; clause 2 is a generic-q statement sourced to feray-meliot2012, and the feray2010 fluctuation claim is gone. `conj:jet-convergence-classical-limit` already cites `[ivanov-olshanski2003] §7`.
- **qou-uwcc.** `alg:delta-lambda-closure` already cites springer1976 and shoji2019 for "signed Springer dimension", with a "name only" disclaimer.
- **qou-owbd.** `TjonSimplexForm.lean` already uses `[jurgenson2009srg]`.
- **qou-pd8e.** `hh1_h5_cocenter_action.py` makes no Geck–Rouquier or "dim Z = 7" claim; it computes dim HH₀ directly over ℤ[ζ]. The bean is misaddressed.
- **qou-jncu.** A re-upload request (arXiv:0901.1612, 1207.1793) with no computation; recorded, still open.
- **qou-xugx.** Blocked: Gasper–Rahman is not in `library/`, so the section locator cannot be checked here.

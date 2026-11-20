# Bean claims released after the batch-PR closure — 2026-11-20

On the owner's instruction (W4 session), the beans held `in-progress` by the 147 closed batch PRs were checked and, where safe, reset. JSON twin: `2026-11-20-batch-pr-bean-release.json`. Triage: `2026-11-20-batch-pr-triage.md`.

## Method

1. **Population.** 735 bean ids cited by a closed PR that had status `in-progress` at triage time. (The triage reported 734; one id is counted under two spellings.)
2. **Status now.** Read from a freshly mounted `cat/cat-harness/beans`.
3. **Prior status.** The status a bean had just before the batch generator's claim commit (`chore(beans): mark … in-progress`), read from the beans-branch history. For all 656 reset beans it was `todo`.
4. **Live claim.** Any currently open PR outside the closed set that cites the bean.
5. **Completed?** Three checks:
   - Is the status `completed` or `scrapped` now?
   - Does any main commit dated on or after the claim name the bean together with a closing word?
   - Separately, for review only: does any main commit **subject** ever name the bean together with a closing word (closed / resolved / derived / proved / pinned)?
6. **Reset.** Only beans that are still `in-progress`, carry no live claim, are not an epic or milestone, and show no completion since the claim. Each was set back to its prior status, and a dated note recording why was appended. Pushed with `branch-store push --id beans` (beans-branch commit `e483e883ca`: 656 files, 2 lines changed + note each).

## Result

| class | beans | action |
|---|---:|---|
| RESET | 656 | reset to prior status (`todo`) |
| LIVE-CLAIM | 36 | left `in-progress`: an open PR outside the closed set cites it |
| EPIC-KEEP | 18 | left: epic or milestone |
| MISSING | 12 | no bean file on the mount |
| NOT-IN-PROGRESS(todo) | 7 | already `todo` again |
| ALREADY-COMPLETED | 5 | left `completed` |
| ALREADY-SCRAPPED | 1 | left `scrapped` |

**No bean in the population shows completion after the batch claim**: zero main commits dated on or after the claim name one of them together with a closing word. All 656 reset beans were `todo` before the batch generator claimed them.

## Review before closing: 94 reset beans whose history suggests the work may already be done

Each of these has a main commit **subject** naming it together with a closing word. Most of those commits predate the batch claim, and the bean stayed `todo` regardless. A subject like that often records partial progress ("item 3 done … bean stays todo") rather than completion, and some of these beans track open conjectures, which AGENTS.md rule 13a says must not be closed. So they were reset to `todo`, not closed. Each carries a **Review before closing** line in its note.

| bean | title | main commit |
|---|---|---|
| `qou-07ts` | compute_atom_chi_rust 3He is nondeterministic at the 50th digit: 4 dis | 2026-09-05 `4062a354b9` beans(qou-07ts): 4He wobbles too — the 'unmeasured' caveat resolves the wrong way |
| `qou-19jc` | 2H ATTACK B: test whether the required d = -0.1195h is the sigma^2 sta | 2026-08-31 `6f746a3374` beans(qou-19jc): colour weighting priced at 0.097% of the gap; once-only condition proved |
| `qou-1gkf` | qou-dw20 convergence (B): (2π/N)log S_{n*,k*} → 4·clausen(π/2) at sadd | 2026-08-07 `1b7f0979e5` chore(beans): qou-kvvu completed (catalanG bridge verified); qou-1gkf lower-envelope progr |
| `qou-2g9j` | Delta=2 Milnor residual: the mod-delta formula is HELD (Mellor-Melvin) | 2026-09-04 `046296ff06` beans(qou-2g9j): mubar vanishes on every triple -- residual closed, and my Seifert-surface |
| `qou-2joi` | y_lambda closed form cites the wrong Lusztig paper; BLM is absent and  | 2026-08-24 `8a42b2dcab` bean(qou-2joi): both disagreements resolved; the straddle is a class of 11 |
| `qou-2tuv` | H_3 vs H_{3A}: the proper sum is infeasible past A~12, so substitution | 2026-08-22 `fbaeb2a652` beans(qou-2tuv): 4He closes the pattern — max/V_hat/ is A-invariant, and the failed guess  |
| `qou-324i` | The `independent` q0 disposition tests override-sensitivity, not q0-in | 2026-08-29 `7b36127e07` beans: close v90i / dkm2 / rh31, re-measure 324i — each verified on main, not assumed |
| `qou-3kni` | Two conj: labels named by the pole-to-cusp producers have no carrier - | 2026-10-11 `70c8befd9f` beans(qou-3kni): item 3 done — surface drained 26 -> 0; bean stays todo |
| `qou-3quc` | GAP(lean): general-n Molien/fake-degree q-analogue -- concrete n<=4 pr | 2026-09-03 `33f9b789ac` chore(beans): qou-3quc -- Lean side CLOSED, normalizedSum n q = 1 unconditional (PR #6447) |
| `qou-4383` | Ordering fingerprint audit: find grouped-era artifacts by VALUE, not b | 2026-09-13 `1ee14c582d` fix(qou-4383): TR_M_AT_Q0 becomes a live view — the last hardcoded grouped registry, close |
| `qou-49vn` | The committed chi caches carry a value no live route reproduces: cache | 2026-09-06 `986cad4db7` resolve(qou-49vn): the tension was my arithmetic -- and Rust is now the likelier outlier,  |
| `qou-51l1` | GAP: is chi(A) = -6 forced or read off Bring''s surface? two corpus st | 2026-09-15 `7ee7600f5d` beans(qou-51l1): chi(A) = -6 is derived-modulo-one-input; three of my own claims were wron |
| `qou-5c64` | binding-single-pipeline-comparison is 3 months stale and RED when re-r | 2026-09-13 `b08e109338` retract(qou-5c64): the two "unidentified" per-nucleon free factors do not exist — I used a |
| `qou-742w` | The M1 leading constants are typed into twelve scripts, not imported | 2026-09-07 `af31a017f0` measure(qou-742w, qou-3f7a, qou-9ies): the closed form decided, a false positive that inve |
| `qou-8iru` | H4/C5 answered: convention D IS Temperley-Lieb. Radical = TL ideal, di | 2026-09-27 `284354ca57` beans(qou-7vht, qou-8iru): item 1 closed and the dimension chain with it — still not an is |
| `qou-8vt2` | DEFINE ϑ_K: the channel has no definition for it, only a docstring phr | 2026-08-08 `1c90365372` beans(qou-8vt2): AV1 resolved NEGATIVE — no glyph collision, and theta_K IS c_3 |
| `qou-9p9y` | T3: full GSWZ module-membership harness (Frobenius + dilog + eps_m); c | 2026-08-01 `ad465fe580` chore(beans): qou-9p9y touch — dilog layer complete, eps_m remains |
| `qou-b7cf` | LAUNDERED refilled 0 -> 34 files on main -- drain the mpf(str(f64)) si | 2026-09-04 `f7b58d4355` beans(qou-b7cf): sweep complete -- 0/34 verdict changes, and the three method traps |
| `qou-b8vx` | q-integer audit coverage gap: 208 of 366 definitions are not symbolica | 2026-09-13 `dfcd70e437` audit(qou-b8vx): retract my own "29 genuinely q0-pinned" — 23 were my bug; 81 -> 102 |
| `qou-bimg` | Dense triton Magnus probe is 87x slower than the sparse route that alr | 2026-09-13 `0feb5c54d8` docs(qou-q2q7,qou-za3q,qou-bimg): close the naming half, tick three sibling-done items, op |
| `qou-buxs` | Delta_lambda binding sign = chiral T3 / Wigner-SU(4) grading (qou-20sx | 2026-08-29 `36cf3369c2` qou-buxs: caveat 3 resolved by corpus-grep, and it resolves NEGATIVELY |
| `qou-cblw` | p-n interface factor: colour-BLIND z - h/2 where canonical is z - h*(1 | 2026-08-26 `8823f66583` beans(qou-cblw): §3 closed as a negative; open qou-s24v for the arithmetic-vs-geometric fo |
| `qou-cdh4` | H4 (hygiene): convention-label hygiene — history must say it is histor | 2026-08-16 `75a4efa2dc` H4(qou-cdh4): registries were already labelled — and one sentence describing a closed ques |
| `qou-ck2w` | GAP: Milnor exact-order leading coefficient mubar_A != 0 (exact law or | 2026-08-31 `6676c90ea4` beans(qou-ck2w): cross-ref the recursion proof — math gap CLOSED, only Lean instance remai |
| `qou-cwdx` | #6 counting LB: skein 3^{3n} tree → VNP/arithmetic-circuit lower bound | 2026-08-07 `77f886747a` beans: qou-ftre completed; cwdx/l525 found corpus-covered (no duplication) |
| `qou-d5e8` | 2H ATTACK C: check whether B = -alpha*ln(mu) is the right functional a | 2026-08-31 `222582557a` correct(qou-d5e8): the binding functional IS derived — the 2026-08-25 grep missed it in it |
| `qou-d7h1` | GAP: Eightfold Way flavor SU(3) from QOU components — distinguish from | 2026-08-25 `1b9b341118` content(qou-d7h1): wire the proved gate scope into the chapter; inventory overturns the re |
| `qou-d8de` | GAP W1: construct the q-difference prolongation D_q from the color spe | 2026-09-13 `2c43a9e267` lean(qou-d8de): close the prose-only finite-order step -- it was pigeonhole, not Moebius |
| `qou-e6db` | Formalize HOMFLY + braid closure in Lean — the sole residue of MFW (sp | 2026-08-29 `3ff213aab3` chore(beans): qou-m7nj block-factorisation join; qou-e6db cycleLen_inv closed |
| `qou-epxx` | raw-float64 drain: two float() casts on full-precision inputs — q0_pro | 2026-09-26 `be07fbd97f` beans(qou-epxx): the g1 run completed and REFUTED my own prediction -- zero numbers moved |
| `qou-f1qs` | Lean: general-n normalisation and indexing for the two-row weights (yw | 2026-08-11 `969fdb2094` lean(qou-f1qs): sum_lambda dim_lambda * y_lambda = 1 at every n, proved |
| `qou-fi93` | Derived substrate matter/antimatter asymmetry: bar_defect r(z)-r(-z) = | 2026-09-14 `bf2e569531` beans(qou-hjs8, qou-fi93): the theta claim is live in two blocks, and fi93's search is clo |
| `qou-fngs` | Vacuous: instance canonical makes GBFiltrationCollapsesAtE2 free for e | 2026-08-24 `fec42ef881` qou-fngs: collapse PROVED from a parity grading, not assumed |
| `qou-gd90` | qou-q425 torus links gcd(r,s)>1: exact periodic-state correction to Mi | 2026-10-12 `00b54c3665` qou-gd90/qou-q425: bean appends — full-twist scalar proved |
| `qou-gpb5` | Implement the multi-level character ratio: quark and nuclear-jet level | 2026-09-05 `9318478b41` merge: intra-word ordering — beta_Bor confinement core, the invariance proved in Lean, and |
| `qou-h0zz` | V6: braid words per chiral fermion -- the actual blocker for T(t) | 2026-10-12 `abd21ab416` qou-h0zz: the lepton half of the braid-word blocker is already derived |
| `qou-hjs8` | theta_res^2 vs PDG e+/e- mass split: is the 72x overshoot real or high | 2026-09-14 `bf2e569531` beans(qou-hjs8, qou-fi93): the theta claim is live in two blocks, and fi93's search is clo |
| `qou-hms1` | GENERALISE?: three blocks justified their base field / R codomain by a | 2026-08-09 `28e39db79b` bean qou-hms1: the sqrt-justified base fields -- two resolved, one open Lean question |
| `qou-i9gk` | ROAST of Steps 27-28: is the trace-blind sector physical, and is E_2/E | 2026-09-01 `85c2bb0468` fix(qou-i9gk): the tanh(ln q) / EM match is formal — Step 28's last positive downgraded; b |
| `qou-j3w6` | DECISION (owner): condition 5 and the eightfold fundamental — keep N=2 | 2026-09-03 `c066ad4e74` beans(qou-icj2): eightfold session closed — PR #6458 merged, four fronts completed, qou-j3 |
| `qou-j6gb` | mpf_import_time_dps_audit is NOT wired into precision-gates.sh — 288 f | 2026-08-15 `e8855a5e20` beans: close qou-s41x; record post-merge state on qou-j6gb |
| `qou-k12x` | DERIVED: the canonical braid fixes the bonded-pair linking number — no | 2026-08-30 `ce53e90e3d` correct(qou-k12x): the bond-set "finding" was already resolved in the corpus |
| `qou-k4ud` | FRONTIER A: Δ_λ MAGNITUDE assembly — sign done (valuation); is /Δ_λ/=d | 2026-07-19 `9c7aaad289` beans(qou-k4ud): b4 scalar m=g_reeb settled (deformed ss-pole); open object re-scoped to p |
| `qou-k5r5` | GAP: M_1>0 (first odd moment) — rigorous all-n proof OPEN; identity Le | 2026-09-11 `e4275899de` beans(qou-k5r5): the tilt derivative is PROVED in Lean, sorry-free -- and the answer to 'a |
| `qou-ke35` | The mpf migration of the constant modules is HALF DONE, and a consumer | 2026-09-14 `aa181ffe1f` beans(qou-ke35, qou-sogb): the constant modules' mpf migration is half done — and my r5 le |
| `qou-l39s` | Wire proved Δ_λ=(-1)^{n(λ)}·dim (signed Springer dim) as canonical per | 2026-08-02 `a43bc9ed35` wire(Δ_λ): emit proved value witness + honest consumer + appendix sync (qou-l39s) |
| `qou-lq6k` | EM-linking O1 (antisymmetry obstruction): mu-bar_123 is TOTALLY ANTISY | 2026-09-12 `d54e1c7160` lean(qou-lq6k): only two nucleon species exist, so pigeonhole closes the charge-weighting  |
| `qou-lsp9` | GAP: wire the net(T(2,n)) -> lepton mass map. Corpus assigns T(2,n) to | 2026-08-07 `2a465c8211` lean(qou-lsp9): positivity closes the node escape the rigidity law leaves open |
| `qou-luq7` | DEFECT: Hecke/Wedderburn.trace_decomposition is SELF-ASSUMING -- tr_M  | 2026-08-30 `52f850c976` beans(qou-luq7): item 2 closed — blockDim computed, y_lambda determined |
| `qou-lzzi` | Route C M3: the pretzel''s level-2 Stokes matrix and the s(x) adjoint- | 2026-09-14 `8044373026` audit(qou-lzzi): close the obvious escape -- sigma cannot cancel in the pairing |
| `qou-m7py` | D2: Rust gram.rs TR_M[5]=z^3 bug is load-bearing under convention D | 2026-08-15 `993bcf80cc` docs(pyhecke-native): native gram path ENABLED — qou-m7py resolved |
| `qou-mpq5` | R2: prove (1)↔(2) Schur-Weyl — tr over (ℂ^N)^{⊗n} = Σ_{λ⊢n}(dim V_λ)χ_ | 2026-08-19 `bab05902e1` beans(qou-jr8y): closed -- the orphaned mpq5 fragment landed with #4600 |
| `qou-n4pv` | PI-1: Hadamard factorization theorem in Mathlib — entire function of f | 2026-08-08 `91a038dcbe` beans: settle qou-n4pv's open compile verification — the file builds |
| `qou-ng7j` | Detector is blind to non-y_lambda convention-C quantities (tr_M, z); S | 2026-09-15 `4ccff20e61` excise(qou-ng7j): the z row closes too — 16 convention-C z values in unlabelled fields |
| `qou-omiu` | check-sidecars JUST regex: bare ≤/≥ make ℕ index comparisons read as a | 2026-08-24 `aad975eb80` beans(qou-omiu): §7c half closed on main — and their fix beats mine by 45 files |
| `qou-omr7` | Magnus probes: d_q was the hook product, weight inverted (4 files) | 2026-09-04 `c600f413bc` beans(qou-omr7): he4-sparse complete, and this bean's own "2 of 4" count was wrong |
| `qou-oyty` | Two Hecke normalisations coexist and give different Ext^1: Z vs Z[i] | 2026-08-24 `c5982b94d5` QOU: znut resolved as definitional, tpt6 resolved by deletion, oyty/fwah queued |
| `qou-pbwj` | ROAST: red-team the six takeover fronts (observable C, #7092 coboundar | 2026-09-11 `b207541261` audit(qou-pbwj): roast the six takeover fronts — two are already answered, one closed unde |
| `qou-pc85` | EM-linking route 2: the MUTUAL O''Hara channel is integrable WITHOUT O | 2026-09-13 `790f5ee235` lean(qou-pc85): close the two proofs — verified sorry-free against the library SOURCE |
| `qou-po72` | M1 machinery: explicit constants C_W, C_P, C_D for Var(Sum c^2), Cov,  | 2026-08-29 `51bd8408f2` po72(qou-k5r5): de-poissonized (CS) leading constants in closed form; rho_P = 2 sqrt(6)/5 |
| `qou-pwut` | 287 root-level ad-hoc QA writers bypass qa-agent-entry.ts and emit no  | 2026-08-29 `034769b5e4` beans(qou-pwut): both OPEN items closed — the writers were already fixed, the guard was wh |
| `qou-qb8g` | c_3's bar-parity is UNDETERMINED — neither named split is derived | 2026-08-29 `37cfae1a4d` chore(beans): avt1 G2 + qb8g alpha_D obstruction now proved-lean (landed) |
| `qou-qint` | Reconcile the 8 q-integer definitions — `qInt` names two conventions | 2026-08-09 `a65654a854` consolidate(qou-qint): the Laurent twist, and closing the census at 47 of 55 |
| `qou-qpj9` | GAP: define canonical meson flux-tube threading braid (J/ψ underived) | 2026-08-25 `7290c0477c` audit(qou-qpj9): the closed-3-braid volume tool is in the library, and it bounds the heavy |
| `qou-s16e` | T5: no-free-parameter certificate for the mass chain | 2026-10-10 `b94e255b54` qou-s16e: T5's target is a data lookup, not a closed term — taxonomy row 50 |
| `qou-slpd` | ROAST: slope ½ is a definition, not a derivation — and the two ½s are  | 2026-08-08 `60968f685c` lean(qou-slpd): the Newton slope is the q-Gevrey LEVEL — item 5, chain closed |
| `qou-svnb` | F4 option-2: prove abstract cyclic_iff_gram_symm reduction; refactor t | 2026-07-19 `9e85264c35` lean(h4): prove the bilinear cyclicity reduction sorry-free — trM_cyclic now derived (bean |
| `qou-t1kv` | GAP: HeckeGenerators is H_infinity — Schur cascade (PROVED, #5766) blo | 2026-08-25 `bc06253f74` beans(qou-t1kv): COMPLETED -- every item proved and merged |
| `qou-tjys` | hmerge: the A-1 interfaces each merge one cycle pair -- discharge Clas | 2026-09-05 `945e4929f6` beans(qou-tjys): Lean half done — and the block collapsed further than predicted |
| `qou-tqr9` | Agent-adjudicated QA axes are silently lost by "regenerate rather than | 2026-08-22 `13cf116280` qa: pre-resolve the two sidecar conflicts with main — script from main, agent unioned [qou |
| `qou-tvok` | M1 machinery: explicit theta^-1 Euler-Maclaurin constant C_A for Var(S | 2026-08-29 `e9efee94b7` tvok(qou-k5r5) step 2: the V_A remainder rate is theta^-1 (RESOLVED), c_1 ~ -0.0678 measur |
| `qou-uabo` | prop:habiro-residue-sum-equivalence cites a cross-pipeline witness tha | 2026-08-15 `7fdd2dedcd` qou-uabo resolved: the block quotes the path its own producer calls non-canonical |
| `qou-uz7q` | alpha_5_lp_dual_crystal exceeds a 7-min budget and lacks the required  | 2026-08-24 `a2273a899a` bean(qou-uz7q): step 1 complete — 2 of 6 refuted, 4 long and none of them measured |
| `qou-v1eu` | Route C M3: derive the pretzel''s GL(r) normalisation from the q-Wrons | 2026-09-15 `51181ae9f3` gate3(qou-v1eu Part 10): GATE 3 DONE — SL-vs-GL is FORCED by the Casoratian ratio, not cho |
| `qou-v7ro` | GAP: bridge Magnus coeff mu-bar(12..A)=+/-1 to the QOU Markov-trace de | 2026-09-03 `7091dcca94` beans(qou-v7ro): brick 3 minimal wedge landed — first concrete ρ(w₃), closes to certified  |
| `qou-vkg5` | GAP: the Ecalle bridge equation (AlienDerivation §4) is unproved | 2026-08-08 `c9cc8229d7` lean(qou-vkg5): the twist -- E_q is FORCED, proved; and a correction to my own structure |
| `qou-vr3q` | Deep-dive 1: G3 monodromy/Stokes-constant keystone — derive A_ω (odd-f | 2026-07-18 `490f5a7ca7` vr3q T1: hspan CLOSED — period lattice basis from b²∉ℝ (lean exit 0) |
| `qou-vtlj` | Delta is not a two-way fork: the corpus carries FOUR net values, and t | 2026-09-04 `0acb6686d1` content(qou-vtlj): RETRACT my own positivity caveat — it cited struck text, and the basis  |
| `qou-w0zn` | GAP: hup off-diagonal (DU-UD=I) on the Young lattice — the last brick  | 2026-09-08 `a207d70bec` beans(qou-7dzg closed, qou-w0zn advanced): batch 7 -- and route 2 landed unconditionally |
| `qou-w2vy` | GAP: binding_from_frobenius_pairing raises on object dtype -- latent b | 2026-09-04 `d22015db2e` beans(qou-w2vy): retract my own "input precision NOT measured" — the corpus closed it on 2 |
| `qou-w3eg` | H4/T2: Vol(alpha,beta,gamma) = Lambda-sum — Milnor''s computation, dec | 2026-09-12 `ab489b9327` beans(qou-w3eg): the γ = π/2 slice is closed — and I had its difficulty backwards |
| `qou-wc8f` | GAP: topic2 mirror-pair Phi_8 multiplicities do not reproduce on main, | 2026-08-31 `afcb8aec61` research(qou-wc8f) SETTLED: the fresh column is correct -- and my own leading hypothesis w |
| `qou-wdij` | REGRESSION: the Borromean atom word is non-monotone, so every monotone | 2026-09-06 `89ff8a5ec2` wire(qou-wdij): non-monotone words take the window transfer — and the low-isotope dashboar |
| `qou-wg3c` | GAP: three inconsistent Wigner coefficients, and the [5]_q! block conf | 2026-10-12 `02a1c8d8df` qou-wg3c: neither Wigner candidate is derived; C_lambda has two definitions |
| `qou-wpr6` | The classicalisation IS derived (delta>0, +1 crossing) but by 0.069%;  | 2026-08-30 `311f344e96` derive(qou-wpr6): the classicalisation IS derived — by the sign of delta, and by 0.069% |
| `qou-wy2h` | P≠NP #2: NP→Jones encoding — SAT instance → link L with J_L(q₀) decidi | 2026-07-31 `8b8e785ac2` beans: close 0pd5 (reconciliation done), drop wy2h (dup of SkeinNPEncoding) |
| `qou-x3iv` | M3 Part 8: the (-2,3,7) holomorphic blocks from its 2-dim state integr | 2026-09-14 `d1ab8c7620` route-c(qou-x3iv Part 14): the Gaussians contribute a MONOMIAL to the fusion, not 1 — deri |
| `qou-x631` | Prove the Δ_λ covariance kernel Cov_Planch(f^λ,Σc²)≤0 | 2026-07-25 `a168710a0d` attack(deltalambda covariance qou-x631): PROVED even hook-power moment positivity |
| `qou-xf14` | PINNED: the normaliser convention is delta = [2]_q, forced by the iden | 2026-09-05 `8fd0133449` qou-xf14: normaliser convention pinned to delta = [2]_q by an identity in q; qou-ib3g clos |
| `qou-xq3f` | GAP: Rosso-Jones product-collapse for spectral Q-value decomposition ( | 2026-08-28 `902a1953cf` beans(qou-xq3f): record general telescope already proved; re-scope T-n1 to carrier bridge |
| `qou-y98b` | Gate the q0Anchor refill: ~50% of newly-added witnesses land unstamped | 2026-09-04 `b660b27185` audit(qou-y98b): decide a baked q0 pin by VALUE, closing the cone trace's blind spot |
| `qou-z03j` | Symbolic closed form for the colour-cubic saddle points via the palind | 2026-09-06 `f5077c477d` CORRECT(qou-z03j): most of what I called new, the corpus already had Lean-proved -- and I  |
| `qou-z4ba` | The c1 mirror asymmetry has the WRONG SIGN, 0/230 against AME -- and i | 2026-09-04 `f0dab71510` science(qou-z4ba): the derived c1 mirror asymmetry is WRONG IN SIGN — 0/230 against AME, a |
| `qou-zut2` | Ext^1 = Z for the mixed-channel extension contradicts H_n(q0) semisimp | 2026-08-24 `f7e8f7f71e` beans: record the Hecke-normalisation caveat (qou-oyty) and resolve qou-zut2 |

## Left in-progress because another open PR claims them

`qou-00c5` (#8206), `qou-04ub` (#8311), `qou-0fmb` (#7481), `qou-11l4` (#7610), `qou-3nva` (#7205), `qou-4jhp` (#8096), `qou-6poy` (#8286), `qou-840k` (#8170), `qou-9l0d` (#8150), `qou-b5h9` (#8246), `qou-bhrx` (#8160), `qou-cc4t` (#8493), `qou-cjkt` (#8498), `qou-cyon` (#8271), `qou-db24` (#7477), `qou-dh8d` (#8498), `qou-dmar` (#8498), `qou-ebs6` (#8329), `qou-hok7` (#8408), `qou-hu1f` (#8295), `qou-jfx8` (#8351), `qou-lrvc` (#8246), `qou-m8f3` (#7210), `qou-ndt5` (#8304), `qou-oiz3` (#8560,#7440), `qou-px38` (#8342), `qou-qqm4` (#8410), `qou-sw8n` (#7406), `qou-thj7` (#8436), `qou-upbq` (#8351), `qou-v4in` (#8351), `qou-vd7j` (#8564), `qou-vwu3` (#8279), `qou-w49j` (#8358), `qou-wuxx` (#8593), `qou-z08b` (#7876)
